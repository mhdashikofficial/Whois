import os
import subprocess
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot API configuration
api_id = 7789657  # Replace with your correct API ID as an integer from my.telegram.org
api_hash = "124b302f0d2aebd8049cf953303612d5"  # Replace with your correct API hash as a string from my.telegram.org
bot_token = "6889233025:AAEh8EepYmQzLLNvrTTdBRWwvRDu1svMdXc"  # Replace with your bot token as a string from BotFather

# Dictionary to keep track of connected devices
connected_devices = {}

# Initialize the Pyrogram client
app = Client("termux_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Helper function to get device identifier (hostname)
def get_device_identifier():
    try:
        # Get the hostname of the device
        device_id = subprocess.check_output('uname -n', shell=True).decode().strip()
    except Exception as e:
        device_id = f"Unknown_Device_{len(connected_devices)+1}"
    return device_id

# Start command handler
@app.on_message(filters.command("start"))
async def start(client, message):
    # Get the device identifier
    device_id = get_device_identifier()
    user_id = message.from_user.id

    # Add the device if it's not already registered
    if device_id not in connected_devices:
        connected_devices[device_id] = {"user_id": user_id, "username": message.from_user.username or f"User {user_id}"}

    # List connected devices
    device_list = "\n".join([f"{i+1}. {dev}" for i, dev in enumerate(connected_devices.keys())])
    await message.reply(
        f"Connected Devices:\n{device_list}\n\nSelect an option for this device:",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("Access Terminal", callback_data=f"terminal_{device_id}"),
                InlineKeyboardButton("Download Files", callback_data=f"files_{device_id}")
            ]]
        )
    )

# Handle button press events
@app.on_callback_query()
async def callback_handler(client, callback_query):
    data = callback_query.data
    device_id = data.split("_")[-1]  # Extract device ID from callback data

    if data.startswith("terminal"):
        await callback_query.message.reply(f"Send me a shell command to execute on device {device_id}:")

    elif data.startswith("files"):
        await callback_query.message.reply(f"Send me the file path to download from device {device_id} (e.g., /sdcard/Download):")

# Handle terminal command execution
@app.on_message(filters.text & ~filters.command("start"))
async def handle_text(client, message):
    user_id = message.from_user.id
    device_id = get_device_identifier()

    if device_id in connected_devices and connected_devices[device_id]["user_id"] == user_id:
        user_input = message.text

        if user_input.startswith("/"):
            # Treat input as file path for download
            if os.path.exists(user_input):
                await message.reply_document(document=user_input)
            else:
                await message.reply("File not found!")
        else:
            # Treat input as a shell command
            try:
                result = subprocess.run(user_input, shell=True, capture_output=True, text=True)
                if result.stdout:
                    await message.reply(f"Output:\n{result.stdout}")
                if result.stderr:
                    await message.reply(f"Error:\n{result.stderr}")
            except Exception as e:
                await message.reply(f"Error occurred: {str(e)}")
    else:
        await message.reply("You are not authorized to run commands on this device.")

# Run the bot
app.run()
