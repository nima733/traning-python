import urllib.request as urllib


def check_connection_site(url):
    print('check in connectivity ')

    response = urllib.urlopen(url)
    print('connected to {} successfully '.format(url))
    print('The response code was: ', response.getcode())


if __name__ == '__main__':
    print('this is a site connectivity checker program')
    input_url = input('input the url of the site: ')
    check_connection_site(input_url)
