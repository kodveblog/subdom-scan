import requests
def domain_scanner(domain_name, sub_domnames):
    print('-----------Scanner Started-----------')
    print('----URL after scanning subdomains----')
    for subdomain in sub_domnames:
        url = f"https://{subdomain}.{domain_name}"
        try:
            requests.get(url)
            print(f'[+] {url}')
        except requests.ConnectionError:
            pass
    print('\n')
    print('----Scanning Finished----')
    print('-----Scanner Stopped-----')
# main function
if __name__ == '__main__':
    dom_name = input("Enter the Domain Name:")
    print('\n')
    with open('subdomain_names1.txt', 'r') as file:
        name = file.read()
        sub_dom = name.splitlines()
    domain_scanner(dom_name, sub_dom)