import requests
import json
import urllib.request, json

def getdata():
    """
        Get data URL
    """
    try:
        with urllib.request.urlopen('https://shipping-options-api.herokuapp.com/v1/shipping_options') as url:
            data = json.loads(url.read().decode())
            #print(data)
            return data

        #datadict = json.loads(data)     

        #print(datadict)
        for element in data:
            print(element)

    except Exception as e:
        print('Error: ', e.__class__)

def order_best(data):
    response = []
    if data is []:
        return response
    else:
        #print(data)
        data = sorted(data, key=lambda data : data['cost'])
        data = sorted(data, key=lambda data : data['estimated_days'])
        return data




if __name__ == "__main__":
    print("start")
    #URL= 'https://shipping-options-api.herokuapp.com/v1/shipping_options'

    data = getdata()
    data = data.get('shipping_options')    

    print(data)

    response = order_best(data)

    print (response)
    
    
    