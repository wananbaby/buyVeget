# -*- encoding=utf8 -*-
__author__ = "coder"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/ukpzpfhem7v4dy4d?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH",])


# script content
print("start...")
import time
print("请提前进入购物车界面")
i = 0
tm_hour = 21 #也就是美团买菜的第一次抢菜时间的提前一分半进入
tm_min = 7 # 分钟 也就是美团买菜的第一次抢菜时间的提前一分半进入
tm_sec = 0 # 秒
while i==0:
    localtime = time.localtime(time.time())
    if localtime.tm_min==tm_min and localtime.tm_sec==tm_sec:
        print(localtime)
        i = 1
        break
    elif localtime.tm_hour>tm_hour or localtime.tm_min>tm_min:
        i==1
        break
            
while i == 1:
    touch(Template(r"tpl1649168167972.png", record_pos=(0.306, 0.969), resolution=(1080, 2340)))
    if exists(Template(r"tpl1649228877024.png", record_pos=(-0.014, 0.967), resolution=(1080, 2340))) == False:
        touch(Template(r"tpl1649228896835.png", record_pos=(-0.416, -0.943), resolution=(1080, 2340)))
    else:
        touch(Template(r"tpl1649228916561.png", record_pos=(0.452, -0.457), resolution=(1080, 2340)))
        touch(Template(r"tpl1649229045722.png", record_pos=(-0.085, 0.294), resolution=(1080, 2340)))
        touch(Template(r"tpl1649228925787.png", record_pos=(0.337, 0.968), resolution=(1080, 2340)))
        if exists(Template(r"tpl1649228942806.png", record_pos=(0.007, -0.935), resolution=(1080, 2340))) != False:
            while True:
                touch(Template(r"tpl1649229192554.png", record_pos=(0.332, 0.971), resolution=(1080, 2340)))
                if touch(Template(r"tpl1649229222621.png", record_pos=(0.011, -0.932), resolution=(1080, 2340))) == False:
                    break
        else:
            print("结束")
            break






# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)