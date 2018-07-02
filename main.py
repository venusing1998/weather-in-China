import requests


def get_weather(city):
    url = 'http://jisutqybmf.market.alicloudapi.com/weather/query'
    appcode = '964bd2e5ac4141438c9b7b3140210336'
    headers = {'Authorization': 'APPCODE ' + appcode}
    try:
        content = requests.get(url=url, params={'city': city}, headers=headers)
    except requests.exceptions.Timeout:
        return 'TimeoutError'
    except requests.exceptions.ConnectionError:
        return 'ConnectionError'
    except requests.exceptions.HTTPError:
        return 'HTTPError'
    except requests.exceptions.TooManyRedirects:
        return 'TooManyRedirects'
    except:
        return 'OtherError'
    else:
        if content.status_code == 200 and content.json():
            return content.json()
        else:
            return ''


ErrorList = ['TimeoutError', 'ConnectionError',
             'HTTPError', 'TooManyRedirects', 'OtherError']
# print(demo)
# city = input('Input the city:\n')
demo = get_weather('上海')
if demo in ErrorList:
    print(demo)
else:
    test = demo.get("result")
    # 城市
    city = test.get('city')
    # 日期
    date = test.get('date')
    # 天气
    weather = test.get('weather')
    # 气温
    temp = test.get('temp')
    # 更新日期
    updatetime = test.get('updatetime')
    print('city: %s\ndate: %s\nweather: %s\ntemp: %s\nupdatetime: %s' %
          (city, date, weather, temp, updatetime))
