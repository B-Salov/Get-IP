import requests


def get_ip():
    url = 'https://freegeoip.app/json/'
    data = requests.get(url).json()

    return data


def _main():
    data = get_ip()

    data_dictionary = {
        'ip': data['ip'],
        'Country': data['country_name'],
        'Region': data['region_name'],
        'City': data['city'],
        'Latitude': data['latitude'],
        'Longitude': data['longitude']
    }

    for key, item in data_dictionary.items():
        print(f'{key} - {item}')


if __name__ == '__main__':
    _main()
