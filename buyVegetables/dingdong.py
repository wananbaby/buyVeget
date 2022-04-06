# -*- encoding=utf8 -*-
__author__ = "coder"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",])


# script content
print("start...")
import time
print("请提前进入购物车界面")
i = 0
tm_hour = 8 #也就是叮咚买菜的第一次抢菜时间的提前一分半进入
tm_min = 29 # 分钟 也就是叮咚买菜的第一次抢菜时间的提前一分半进入
tm_sec = 0 # 秒
while i==0:
    localtime = time.localtime(time.time())
    if localtime.tm_min==tm_min and localtime.tm_sec==tm_sec:
        print(localtime)
        i = 1
    elif localtime.tm_hour>tm_hour or localtime.tm_min>tm_min:
        i==1
        break
            
while i == 1:
    touch(Template(r"tpl1649162756961.png", record_pos=(0.324, 0.846), resolution=(1080, 2340)))
    if exists(Template(r"tpl1649162767030.png", record_pos=(0.319, 0.844), resolution=(1080, 2340))) == False:
        touch(Template(r"tpl1649162783804.png", record_pos=(0.317, 0.846), resolution=(1080, 2340)))
    else:
        if exists(Template(r"tpl1649204520440.png", record_pos=(-0.309, 0.216), resolution=(1080, 2340))) == False:
            touch(Template(r"tpl1649168635592.png", record_pos=(-0.434, -0.922), resolution=(1080, 2340)))
        else:
            touch(Template(r"tpl1649204635849.png", record_pos=(0.436, -0.575), resolution=(1080, 2340)))
            touch(Template(r"tpl1649230688782.png", record_pos=(-0.025, 0.087), resolution=(1080, 2340)))
#             touch(Template(r"tpl1649162856214.png", record_pos=(0.419, -0.128), resolution=(1080, 2340)))
            touch(Template(r"tpl1649162871868.png", record_pos=(-0.341, 0.871), resolution=(1080, 2340)))
            touch(Template(r"tpl1649162882958.png", record_pos=(0.324, 0.977), resolution=(1080, 2340)))
            if exists(Template(r"tpl1649168420452.png", record_pos=(0.006, -0.932), resolution=(1080, 2340)))!= False:
                touch(Template(r"tpl1649162882958.png", record_pos=(0.324, 0.977), resolution=(1080, 2340)))
                touch(Template(r"tpl1649168268535.png", record_pos=(-0.424, -0.925), resolution=(1080, 2340)))
                touch(Template(r"tpl1649168635592.png", record_pos=(-0.434, -0.922), resolution=(1080, 2340)))
            else:
                break
print("END")


            

    

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)