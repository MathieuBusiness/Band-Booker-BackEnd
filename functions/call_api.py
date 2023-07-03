import requests
import getters
"""
THIS IS ALL API ENDPOINTS

Get all bands
/get/allBands


"""
def post_specific_band_by_id(specific_id=None):
    band = getters.get_specific_band_by_id(specific_id=specific_id)
    headers = {'Content-Type': 'application/json'}
    url = 'http://127.0.0.1:5000/post/bandById'
    response = requests.post(url, json=band, headers=headers)
    if response.status_code == requests.codes.ok:
        return response
    else:
        response.raise_for_status()


def get_all_bands():
    headers = {'Content-Type': 'application/json'}
    url = 'http://127.0.0.1:5000/get/allBands'
    response = requests.get(url, headers=headers)
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        response.raise_for_status()

if __name__ == '__main__':
    data = post_specific_band_by_id(1122)
    print(data)