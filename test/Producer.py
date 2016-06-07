#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
logger = logging.getLogger("Producer")

#导入上级目录模块
import sys
sys.path.append("..")
import settings_MQ as settings

#启动JVM
from jpype import *
jvmPath = getDefaultJVMPath()
startJVM(jvmPath, settings.JVM_OPTIONS, "-Djava.ext.dirs="+settings.JAVA_EXT_DIRS)
#startJVM(jvmPath, "-Djava.class.path=" + settings.RMQClientJAR + ":")
logger.info(java.lang.System.getProperty("java.class.path"))
logger.info(java.lang.System.getProperty("java.ext.dirs"))

#启动JVM之后才能调用JPackage,否则找不到相关的jar包
from MQProducer import *
from MQMessage import MQMessage

# 为了支持文本中文输入，要显式设置编码；该编码不影响Message的Body的编码
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8');

###############################################################################
if __name__ == '__main__':
    #jpype.startJVM(jvmPath, "-Xms32m", "-Xmx256m", "-mx256m", "-Djava.class.path=/Users/tan9le/temp/some-lib.jar:")
    java.lang.System.out.println("Java runs correct!")

    producer = MQProducer('MQClient4Python-Producer', 'jfxr-7:9876;jfxr-6:9876')
    producer.init()
    producer.start()
    MQMsg = MQMessage('RMQTopicTest',  # topic
                  'TagB',   # tag
                  'OrderID001',   # key
                  'Hello, RocketMQ!')  # body
    producer.send(MQMsg)
    MQMsg = MQMessage('RMQTopicTest',  # topic
                  'TagC',   # tag
                  'OrderID001',   # key
                  'Hello, RocketMQ! I am 陆钢')  # body
    producer.send(MQMsg)

    producer.shutdown()

    shutdownJVM()
