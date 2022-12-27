import requests

URL: str = 'https://httpbin.org'

def get() -> None:
    response: requests.models.Response = requests.get('https://httpbin.org/get')
    response_status_code: int = response.status_code 
    response_text: str = response.text
    response_json: dict = response.json() 
    
    print('---- ---- ---- ----')
    print(response_status_code)
    print(response_text)
    print(response_json)

def get_with_params() -> None:
    user_params: dict = {
        'name': 'Mat',
        'age': 25
    }
    response: requests.models.Response = requests.get('https://httpbin.org/get', params=user_params)
    response_url: str = response.url
    response_status_code: int = response.status_code 
    response_text: str = response.text
    
    print('---- ---- ---- ----')
    print(response_url)
    print(response_status_code)
    print(response_text)

def post() -> None:
    payload: dict = { 
        'name': 'Mat',
        'age': 25
    } #payload is standard name in for python post data

    response: requests.models.Response = requests.post('https://httpbin.org/post', data=payload)
    response_url: str = response.url
    response_status_code: int = response.status_code 
    response_text: str = response.text

    print('---- ---- ---- ----')
    print(response_url)
    print(response_status_code)
    print(response_text)

def status_codes() -> None:
    response: requests.models.Response = requests.post('https://httpbin.org/status/404')
    response_status_code: int = response.status_code 

    print('---- ---- ---- ----')
    if response_status_code == requests.codes.not_found:
        print('Not Found')
    else:
        print(response.status_code)

def user_agent() -> None:
    user_headers: dict = {
        'User-Agent': 'Mozilla/5.0'
    }
    response: requests.models.Response = requests.get('https://httpbin.org/user-agent', headers=user_headers)
    response_text: str = response.text

    print('---- ---- ---- ----')
    print(response_text)

def images_png() -> None:
    user_headers: dict = {
        'Accept': 'image/png'
    }
    response: requests.models.Response = requests.get('https://httpbin.org/image', headers=user_headers)
    response_text: str = response.text
    response_content: bytes = response.content

    print('---- ---- ---- ----')
    print(response_text) #binary

    with open('myimage.png', 'wb') as img:
        img.write(response_content)

def images_jpg() -> None:
    user_headers: dict = {
        'Accept': 'image/jpeg'
    }
    response: requests.models.Response = requests.get('https://httpbin.org/image', headers=user_headers)
    response_content: bytes = response.content

    print('---- ---- ---- ----')
    with open('myimage.jpg', 'wb') as jpg:
        jpg.write(response_content)

def timeout() -> None:
    print('---- ---- ---- ----')
    for timeout_seconds in [1,2,3]:
        try:
            response: requests.models.Response = requests.get('https://httpbin.org/delay/2', timeout=timeout_seconds)
            response_status_code: int = response.status_code 
            response_text: str = response.text
            print(response_status_code)
            print(response_text)

        except requests.exceptions.ReadTimeout:
            print('TOO LONG...')
    
def proxy() -> None:
    user_proxies: dict = {
        # 'http': '139.99.237.62:80', #user proxy server
        # 'https': '139.99.237.62:80', #user proxy server
    }
    response: requests.models.Response = requests.get('https://httpbin.org/get', proxies=user_proxies)
    response_text: str = response.text
    print(response_text)

if __name__ == '__main__':
    # get()
    # get_with_params()
    # post()
    # status_codes()
    # user_agent()
    # images_png()
    # images_jpg()
    timeout()
    # proxy()