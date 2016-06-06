#!/usr/bin/python
# -*- coding:utf-8 -*-

from jpype import *
from MQProducer import *
from MQMessage import MQMessage
import settings_MQ as settings

if __name__ == '__main__':
    jvmPath = getDefaultJVMPath()
    startJVM(jvmPath, "-ea", "-Djava.class.path=" + settings.RMQClientJAR)
    #jpype.startJVM(jvmPath, "-Xms32m", "-Xmx256m", "-mx256m", "-Djava.class.path=/Users/tan9le/temp/some-lib.jar:")

    producer = MQProducer('MQClient4Python-Producer', 'jfxr-7:9876;jfxr-6:9876')
    producer.init()
    producer.start()
    MQMsg = MQMessage('TopicTest',  # topic
                  'TagB',   # tag
                  'OrderID001',   # key
                  'Hello, RocketMQ!')  # body
    producer.send(MQMsg)
    producer.shutdown()

    shutdownJVM()
