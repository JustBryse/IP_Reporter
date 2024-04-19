import urllib.request

# this function returns None if there was a problem with the http request
def get_public_ip_address() -> None|str:
    public_ip = None
    try:
        response= urllib.request.urlopen(url='https://ident.me') # this website simply returns the requester's public IP address
        public_ip = response.read().decode('utf8')
    except Exception as e:
        print(f"Error in get_public_ip_address(): {str(e)}")

    return public_ip

if __name__ == '__main__':
    print(get_public_ip_address())
