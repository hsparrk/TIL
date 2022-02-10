# -*- coding:utf-8 -*-

import requests
import json

def getSiDo():
    # __ajaxCall("/store/getSidoList.do", {}, true, "json", "post",
    url = "https://www.starbucks.co.kr/store/getSidoList.do"
    resp = requests.post(url) # 해당 url에 post 방식으로 요청
    # print(resp) #Response 200 나오면 성공
    # print(resp.text) # 응답받은 문자열
    # # print(resp.json()) # 응답받은 거를 json 객체 형태로 바꿔줌
    # area = (resp.json().get('list'))
    # sido_code = list()
    # sido_nm = list()
    # for i in range(len(area)):
    #     sido_code.append(area[i].get('sido_cd'))
    #     sido_nm.append(area[i].get('sido_nm'))
    # print(sido_code)
    # print(sido_nm)
    sido_list = resp.json()['list']
    sido_code = list(map(lambda x: x['sido_cd'] , sido_list))
    sido_nm = list(map(lambda x: x['sido_nm'] , sido_list))
    # print(sido_code)
    # print(sido_nm)
    sido_dict = dict(zip(sido_code , sido_nm))
    # print(sido_dict)
    return sido_dict

def getGuGun(sido_code):
    # __ajaxCall("/store/getGugunList.do", {"sido_cd":sido}, true, "json", "post",
    url = "https://www.starbucks.co.kr/store/getGugunList.do"
    resp = requests.post(url , data={"sido_cd":sido_code})
    gugun_list = resp.json()['list']
    gugun_dict = dict(zip(list(map(lambda x:x['gugun_cd'], gugun_list)),
                          list(map(lambda x:x['gugun_nm'], gugun_list))))
    # print(gugun_dict)
    return gugun_dict

def getStore(sido_code='' , gugun_code=''):
    url = 'https://www.starbucks.co.kr/store/getStore.do'
    resp = requests.post(url, data={'ins_lat': '37.5414327',
                                    'ins_lng': '126.8792316',
                                    'p_sido_cd': sido_code,
                                    'p_gugun_cd': gugun_code,
                                    'in_biz_cd': '',
                                    'set_date':'' })
    # print(resp.json())
    store_list = resp.json()['list']
    # s_name , tel, doro_address , lat , lot
    # {'store_list' : [{} , {}, {} ]}
    result_list = list()
    for store in store_list:
        store_dict = dict()
        store_dict['s_name'] =store['s_name']
        store_dict['tel'] = store['tel']
        store_dict['doro_address'] =store['doro_address']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']
        result_list.append(store_dict)
    # print(result_list)

    result_dict = dict()
    result_dict['store_list']=result_list
    # print(result_dict)
    
    # json 저장
    result_json = json.dumps(result_dict , ensure_ascii=False)
    with open('starbuck01.json' , 'w' , encoding='utf-8') as f:
        f.write(result_json)

    return result_json

if __name__ == '__main__':

    print(getSiDo())
    sido = input('도시 코드를 입력해 주세요 : ')
    if sido == '17':
        getStore(sido_code='17' , gugun_code='')

    else:
        print(getGuGun(sido))
        gugun = input('구군 코드를 입력해 주세요 :')
        print(getStore(gugun_code=gugun))