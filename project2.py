import requests
import urllib.request
import json

def get_koreanexim_exchange_rate():
    koreanexim_url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    koreanexim_param = {
        'authkey': 'kC9Nb61QodMBnHlQSvWwasWwGuCNyXLd',
        'searchdate': '20240430',
        'data': 'AP01'
    }

    response = requests.get(koreanexim_url, params=koreanexim_param)

    resposeData = [{'result': 1, 'cur_unit': 'AED', 'ttb': '371.6', 'tts': '379.11', 'deal_bas_r': '375.36', 'bkpr': '375', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '375', 'kftc_deal_bas_r': '375.36', 'cur_nm': '아랍에미리트 디르함'}, {'result': 1, 'cur_unit': 'AUD', 'ttb': '895.93', 'tts': '914.02', 'deal_bas_r': '904.98', 'bkpr': '904', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '904', 'kftc_deal_bas_r': '904.98', 'cur_nm': '호주 달러'}, {'result': 1, 'cur_unit': 'BHD', 'ttb': '3,620.55', 'tts': '3,693.7', 'deal_bas_r': '3,657.13', 'bkpr': '3,657', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '3,657', 'kftc_deal_bas_r': '3,657.13', 'cur_nm': '바레인 디나르'}, {'result': 1, 'cur_unit': 'BND', 'ttb': '1,003.68', 'tts': '1,023.95', 'deal_bas_r': '1,013.82', 'bkpr': '1,013', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '1,013', 'kftc_deal_bas_r': '1,013.82', 'cur_nm': '브루나이 달러'}, {'result': 1, 'cur_unit': 'CAD', 'ttb': '998.84', 'tts': '1,019.01', 'deal_bas_r': '1,008.93', 'bkpr': '1,008', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '1,008', 'kftc_deal_bas_r': '1,008.93', 'cur_nm': '캐나다 달러'}, {'result': 1, 'cur_unit': 'CHF', 'ttb': '1,498.42', 'tts': '1,528.69', 'deal_bas_r': '1,513.56', 'bkpr': '1,513', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '1,513', 'kftc_deal_bas_r': '1,513.56', 'cur_nm': '스위스 프랑'}, {'result': 1, 'cur_unit': 'CNH', 'ttb': '188.14', 'tts': '191.95', 'deal_bas_r': '190.05', 'bkpr': '190', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '190', 'kftc_deal_bas_r': '190.05', 'cur_nm': '위안화'}, {'result': 1, 'cur_unit': 'DKK', 'ttb': '196.14', 'tts': '200.11', 'deal_bas_r': '198.13', 'bkpr': '198', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '198', 'kftc_deal_bas_r': '198.13', 'cur_nm': '덴마아크 크로네'}, {'result': 1, 'cur_unit': 'EUR', 'ttb': '1,462.7', 'tts': '1,492.25', 'deal_bas_r': '1,477.48', 'bkpr': '1,477', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '1,477', 'kftc_deal_bas_r': '1,477.48', 'cur_nm': '유로'}, {'result': 1, 'cur_unit': 'GBP', 'ttb': '1,714.53', 'tts': '1,749.16', 'deal_bas_r': '1,731.85', 'bkpr': '1,731', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '1,731', 'kftc_deal_bas_r': '1,731.85', 'cur_nm': '영국 파운드'}, {'result': 1, 'cur_unit': 'HKD', 'ttb': '174.42', 'tts': '177.95', 'deal_bas_r': '176.19', 'bkpr': '176', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '176', 'kftc_deal_bas_r': '176.19', 'cur_nm': '홍콩 달러'}, {'result': 1, 'cur_unit': 'IDR(100)', 'ttb': '8.39', 'tts': '8.56', 'deal_bas_r': '8.48', 'bkpr': '8', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '8', 'kftc_deal_bas_r': '8.48', 'cur_nm': '인도네시아 루피아'}, {'result': 1, 'cur_unit': 'JPY(100)', 'ttb': '873.85', 'tts': '891.5', 'deal_bas_r': '882.68', 'bkpr': '882', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '882', 'kftc_deal_bas_r': '882.68', 'cur_nm': '일본 옌'}, {'result': 1, 'cur_unit': 'KRW', 'ttb': '0', 'tts': '0', 'deal_bas_r': '1', 'bkpr': '1', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '1', 'kftc_deal_bas_r': '1', 'cur_nm': '한국 원'}, {'result': 1, 'cur_unit': 'KWD', 'ttb': '4,433.25', 'tts': '4,522.82', 'deal_bas_r': '4,478.04', 'bkpr': '4,478', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '4,478', 'kftc_deal_bas_r': '4,478.04', 'cur_nm': '쿠웨이트 디나르'}, {'result': 1, 'cur_unit': 'MYR', 'ttb': '286.29', 'tts': '292.08', 'deal_bas_r': '289.19', 'bkpr': '289', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '289', 'kftc_deal_bas_r': '289.19', 'cur_nm': '말레이지아 링기트'}, {'result': 1, 'cur_unit': 'NOK', 'ttb': '124.11', 'tts': '126.62', 'deal_bas_r': '125.37', 'bkpr': '125', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '125', 'kftc_deal_bas_r': '125.37', 'cur_nm': '노르웨이 크로네'}, {'result': 1, 'cur_unit': 'NZD', 'ttb': '815.94', 'tts': '832.43', 'deal_bas_r': '824.19', 'bkpr': '824', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '824', 'kftc_deal_bas_r': '824.19', 'cur_nm': '뉴질랜드 달러'}, {'result': 1, 'cur_unit': 'SAR', 'ttb': '363.91', 'tts': '371.26', 'deal_bas_r': '367.59', 'bkpr': '367', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '367', 'kftc_deal_bas_r': '367.59', 'cur_nm': '사우디 리얄'}, {'result': 1, 'cur_unit': 'SEK', 'ttb': '124.88', 'tts': '127.41', 'deal_bas_r': '126.15', 'bkpr': '126', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '126', 'kftc_deal_bas_r': '126.15', 'cur_nm': '스웨덴 크로나'}, {'result': 1, 'cur_unit': 'SGD', 'ttb': '1,003.68', 'tts': '1,023.95', 'deal_bas_r': '1,013.82', 'bkpr': '1,013', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '1,013', 'kftc_deal_bas_r': '1,013.82', 'cur_nm': '싱가포르 달러'}, {'result': 1, 'cur_unit': 'THB', 'ttb': '36.89', 'tts': '37.64', 'deal_bas_r': '37.27', 'bkpr': '37', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '37', 'kftc_deal_bas_r': '37.27', 'cur_nm': '태국 바트'}, {'result': 1, 'cur_unit': 'USD', 'ttb': '1,364.91', 'tts': '1,392.48', 'deal_bas_r': '1,378.7', 'bkpr': '1,378', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '1,378', 'kftc_deal_bas_r': '1,378.7', 'cur_nm': '미국 달러'}]

    print(response.json())
    return response.json()


def get_naver_news_data():
    client_id = "WeUyeJW5iOrZHgAbmnWv"
    client_secret = "1hfKaScyTR"
    encText = urllib.parse.quote("달러 환율")
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText  # JSON 결과

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)
        return "ERROR"