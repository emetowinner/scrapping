# importing the requests library 
import requests
# Note: at each run, the file get's overwritten.
# And make sure Icat correct Username and password is used.
# The default pulled Icat data is the Icat open XML data, 
# Icat has an enterprise plan for pulling full realtime data


# Creating link dictionary where each key points to different API endpoint 
urls = {'icat_open_data':'https://data.icecat.biz/export/freexml/EN',
        'icat_product':'https://prf.icecat.biz/?prod_id=LX.TEQ06.029&vendor=acer&shopname=openICEcat-url&lang=en',
        'icat_brand':'https://data.icecat.biz/xml_s3/xml_server3.cgi?prod_id=RJ459AV;brand=hp;lang=en;output=productxml',
        }

def get_data_icat(**kwargs):

    #Define the context manaager to handle the file
    with open('data.xml','wb') as xml_file:
        # Creating get request with user defind auth
        try:
            data = requests.get(kwargs['url'],auth = (kwargs['username'],kwargs['password']))
            print(f'Connection was Successful, Status is {data.status_code}')
                    
        #Catching all errors if not successful
        except Exception:
            print(f'Erro occured while trying {data.status_code}')

        #Writing the response data to XML file
        try:
            web_data = data.content
            print(web_data)
            xml_file.write(data.content)
            return web_data
        except Exception:
            print(f'Error occured during writig and reading web data {Exception.with_traceback}')
def main():
    if __name__ == "__main__":
        username = str(input('Enter your icat Username: '))
        password = str(input('Enter your Icat Password: '))
        get_data_icat(url = urls['icat_open_data'],username = username, password = password)
    else:
        print('Can\'t load, not a module. Kiddly run as a script!')
main()
    


