#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
logger = logging.getLogger("PushConsumer")

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
from MQPushConsumer import *
from MQMessage import ConsumeFromWhere, MessageModel

# 为了支持文本中文输入，要显式设置编码；该编码不影响Message的Body的编码
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8');

import time

if __name__ == '__main__':
    consumer = MQPushConsumer('MQClient4Python-Consumer', 'jfxr-7:9876;jfxr-6:9876')
    consumer.init()

    consumer.setMessageModel(MessageModel['CLUSTERING'])    # 默认是CLUSTERING
    #consumer.setMessageModel(MessageModel.CLUSTERING)    # 默认是CLUSTERING

    consumer.subscribe("RMQTopicTest", "TagB")

    consumer.setConsumeFromWhere(ConsumeFromWhere['CONSUME_FROM_LAST_OFFSET'])
    #consumer.setConsumeFromWhere(ConsumeFromWhere.CONSUME_FROM_LAST_OFFSET)

    #consumer.registerMessageListener(msgListenerConcurrentlyProxy)
    consumer.registerMessageListener(msgListenerOrderlyProxy)

    consumer.start()

    while True:
	time.sleep(1)

    #监听状态时不需要shutdown,除非真实想退出!
    #consumer.shutdown()
    #监听状态时JVM也不能退出,除非真实想退出!
    #shutdownJVM()
