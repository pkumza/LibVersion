# -*- coding:utf-8 -*-
import json
import pymongo
__author__ = 'zach'
__time__ = '2016年3月14日13:37:07'


class MongoConnector:
    def __init__(self):
        conn = pymongo.MongoClient('localhost', 27017)
        db = conn['lib-detect']
        self.packages = db['brief_packages']

    def find_one(self, depth, btc, btn, bh):
        return self.packages.find_one({"depth": depth, "b_total_call": btc, "b_total_num": btn, "b_hash": bh})


class TGReader:
    def __init__(self):
        self.tg = open("tgst5.dat", "r")

    def read(self):
        mc = MongoConnector()
        for line in self.tg:
            lib = json.loads(line)
            if lib['lib'] == "":
                continue
            # print lib['lib'].split(';')[1]
            depth = len(lib['sp'].split('/'))
            apk_txt = open('ResultVersion2/' + lib['sp'].replace('/','.') + '.txt', 'a')
            lib_info = mc.find_one(depth, lib['btc'], lib['btn'], lib['bh'])
            # print lib_info
            apk_txt.write(lib_info['apk'].split('/')[-1] + '\n')
            apk_txt.close()

tgReader = TGReader()
tgReader.read()
