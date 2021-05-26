import urllib.request, json
import operator

def getdata(URL):
    """
        Get data URL
    """
    try:
        with urllib.request.urlopen(URL) as url:
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
    data = data.get('shipping_options')    

    print('Request_data: ', data)

    response = order_best(data)
    print('---------')
    print ('Response:', response)
    
    
    