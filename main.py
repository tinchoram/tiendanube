import requests


def getdata(URL):
    """
        Get data URL
    """
    try:
        data = requests.get(URL)
        data = data.json()
        data = data.get('shipping_options')
        return data

    except Exception as e:
        print('Error: ', e.__class__)


def order_best(data):
    """
        Order data for "cost" & "estimated_days"
    """
    try:
        response = []
        if data is []:
            return response
        else:
            #print(data)
            #data = sorted(data, key=lambda data : data['cost'])
            #data = sorted(data, key=lambda data : data['estimated_days'])
            
            # Modificacion para rdenar por 2 campos
            response = sorted(data, key=lambda data: (data['cost'], data['estimated_days']))
            
            return response
    except Exception as e:
        print('Error: ', e.__class__)


if __name__ == "__main__":
    print("start")
    URL= 'https://shipping-options-api.herokuapp.com/v1/shipping_options'

    data = getdata(URL)
    print('Request_data: ', data)

    response = order_best(data)
    print('---------')
    print ('Response:', response)