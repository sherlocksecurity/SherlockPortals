import argparse
import requests

def check_for_service(domain, service_name):
    # Set the URL structure for the service
    if service_name == "zendesk":
        service_url = f"https://{domain}.zendesk.com/"
    elif service_name == "onedirect":
        service_url = f"https://{domain}.onedirect.in/"
    elif service_name == "freshdesk":
        service_url = f"https://{domain}.freshdesk.com/"
    elif service_name == "freshworks":
        service_url = f"https://{domain}.freshworks.com/"
    else:
        return f"{service_name} is not a recognized service."

    # Check if the URL returns a 200 status code (indicating it exists)
    try:
        r = requests.get(service_url)
        if r.status_code == 200:
            return f"{service_name} is in use at {service_url}."
        else:
            return f"{service_name} is not in use at {domain}."
    except:
        return f"Unable to check {service_name} at {domain}."

# Set up the command line argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="The domain to check")
args = parser.parse_args()

# Get the domain from the command line argument
if args.url:
    domain = args.url
else:
    domain = input("Enter a domain: ")

# Check for each service
print(check_for_service(domain, "zendesk"))
print(check_for_service(domain, "onedirect"))
print(check_for_service(domain, "freshdesk"))
print(check_for_service(domain, "freshworks"))

##ignore this
##ZOMATO DATADOG_API_KEY: 64e7131113efa9425555e45dee6dab56 Not mine :) Pls dont report this on Hackerone; they will fire me :( 
