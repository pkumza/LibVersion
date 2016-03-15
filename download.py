# -*- coding:utf-8 -*-
import os
import glob
__author__ = 'zach'
__time__ = '2016年3月15日12:55:53'


if not os.path.exists("./ResultVersion4/"):
    os.mkdir("ResultVersion4")

Result3 = glob.glob("ResultVersion3/*")
for result3 in Result3:
    res = open(result3, 'r')
    if not os.path.exists("ResultVersion4/" + result3.split("\\")[-1] + "/"):
        os.chdir("ResultVersion4")
        os.mkdir("" + result3.split("\\")[-1] + "/")
        os.chdir("..")
    for line in res:
        command = "cp /home/ubuntu/apk0/androidApp/app_201311260117/" +\
            line[:-1] + " ~/ResultVersion4/" + result3.split("\\")[-1] + "/"
        # command = "scp -i maza_aws_virginia.pem ubuntu@52.4.5.131:/home/ubuntu/apk0/androidApp/app_201311260117/" +\
        #          line[:-1] + " ./ResultVersion4/" + result3.split("\\")[-1] + "/"
        print command
        os.system(command)
