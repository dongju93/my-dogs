from datetime import date
import os

import requests

# from config import keys


# iamport 에서 토큰을 얻어옴
def get_token():
    access_data = {
        # 'imp_key': keys.IAMPORT_KEY,
        # 'imp_secret': keys.IAMPORT_SECRET
        # for heroku
        "imp_key": os.environ["IAMPORT_KEY"],
        "imp_secret": os.environ["IAMPORT_SECRET"],
    }

    url = "https://api.iamport.kr/users/getToken"
    # requests : 특정 서버와 http통신을 하게 해주는 모듈
    req = requests.post(url, data=access_data)
    access_res = req.json()

    if access_res["code"] == 0:
        return access_res["response"]["access_token"]
    else:
        return None


# 결제할 준비를 하는 함수 - iamport 에 주문번호와 금액을 미리 전송
def payments_prepare(order_id, amount, *args, **kwargs):
    access_token = get_token()

    print(order_id, 111)

    if access_token:
        access_data = {"merchant_uid": order_id + str(date.today()), "amount": amount}

        url = "https://api.iamport.kr/payments/prepare"
        headers = {"Authorization": access_token}
        req = requests.post(url, data=access_data, headers=headers)
        res = req.json()

        print(res)

        if res["code"] != 0:
            raise ValueError("API 통신 오류")
    else:
        raise ValueError("토큰 오류")


# 결제가 이루어졌음을 확인해주는 함수 - 실 결제 정보를 iamport에서 가져옴
def find_transaction(order_id, *args, **kwargs):
    access_token = get_token()

    if access_token:
        url = "https://api.iamport.kr/payments/find/" + order_id + str(date.today())

        headers = {"Authorization": access_token}

        req = requests.post(url, headers=headers)
        res = req.json()

        if res["code"] == 0:
            context = {
                "imp_id": res["response"]["imp_uid"],
                "merchant_order_id": res["response"]["merchant_uid"],
                "amount": res["response"]["amount"],
                "status": res["response"]["status"],
                "type": res["response"]["pay_method"],
                "receipt_url": res["response"]["receipt_url"],
            }
            return context
        else:
            return None
    else:
        raise ValueError("토큰 오류")
