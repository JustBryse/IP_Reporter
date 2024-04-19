from ip_reader import get_public_ip_address
from ip_reporter import send_email
from platform import node
from json import dumps,loads

# these are important variables that determine the source and destination of emails sent by this script
EMAIL_HOST = ""
SENDER_EMAIL = ""
SENDER_PASSWORD = ""
RECIPIENT_EMAIL = ""

# This function reads a json file that contains the most recent public ip of this network
def read_last_public_ip() -> str:
    
    ip_record_file = open('ip_record.json','r')
    ip_record_content = ip_record_file.read()
    ip_record = loads(ip_record_content)
    ip_address = ip_record['ip_address']
    return ip_address

# This function overwrites the ip address in the json file. This is used to save the current public IP address
def write_current_public_ip(ip_address) -> None:

    ip_record_file = open('ip_record.json','w')
    content = dumps({"ip_address":ip_address})
    ip_record_file.write(content)

# This function reads the network's current public IP address and sends a notification email if the address has changed since last checking.
def report_public_ip_address()-> None:

    current_public_ip = get_public_ip_address()

    if current_public_ip is None:
        print("Failed to get public IP address. Shutting down.")
        return
    
    last_public_ip = read_last_public_ip()

    # if the current public ip is different than the old one, then update the json file and send a notification email
    if current_public_ip != last_public_ip:

        write_current_public_ip(current_public_ip)

        device_name = node()
        content = f"The network's public IP address is {current_public_ip}. Sent by {device_name}."

        send_email(host=EMAIL_HOST
                ,sender_email=SENDER_EMAIL
                ,sender_password=SENDER_PASSWORD
                ,recipient_email=RECIPIENT_EMAIL
                ,subject="Public IP Report"
                ,content=content)

if __name__ == '__main__':
    report_public_ip_address()
