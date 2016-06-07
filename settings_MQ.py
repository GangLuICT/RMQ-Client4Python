#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename='rmq.log',  
                    filemode='a')

RMQClientJAR = '/home/deploy/rocketmq/alibaba-rocketmq/lib/'
JAVA_EXT_DIRS = RMQClientJAR

#startJVM中的options参数不能包含空格！只能一项一项填写
#JVM_OPTIONS = '-Xms32m -Xmx256m -mx256m'
JVM_OPTIONS = '-mx256m'

pullMaxNums = 32
MsgBodyEncoding = 'utf-8'
