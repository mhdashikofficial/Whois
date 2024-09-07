# Import necessary libraries
import whois
import os
import sys

# Function to clear console (for better readability)
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Banner display
def display_banner():
    banner = """
    =======================================================
    |                                                     |
    |       WELCOME TO THE DOMAIN WHOIS LOOKUP TOOL        |
    |                                                     |
    =======================================================
                 Powered by Ashverse - YouTube Channel
    =======================================================
    """
    print(banner)

# Function to perform whois lookup
def whois_lookup(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# Main function to run the tool
def main():
    clear_console()
    display_banner()

    # Get domain input from the user
    domain = input("Enter the domain to perform WHOIS lookup: ").strip()

    if not domain:
        print("You must enter a domain!")
        sys.exit(1)

    print("\nPerforming WHOIS lookup...\n")
    
    # Get the domain information
    domain_info = whois_lookup(domain)
    
    # If information is retrieved, display it
    if domain_info:
        print("Domain WHOIS Information:\n")
        for key, value in domain_info.items():
            print(f"{key}: {value}")
    else:
        print("No information found or an error occurred.")
    
    print("\n====================================================")
    print("Thank you for using the WHOIS Lookup Tool!")
    print("Don't forget to check out Ashverse on YouTube!")
    print("====================================================")

if __name__ == "__main__":
    main()
