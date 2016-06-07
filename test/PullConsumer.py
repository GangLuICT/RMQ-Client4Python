#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
logger = logging.getLogger("PullConsumer")

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
from MQPullConsumer import *
from MQMessage import MQMessage, PullStatus

#开启goto语句的功能
from goto import goto, label

# 为了支持文本中文输入，要显式设置编码；该编码不影响Message的Body的编码
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8');

if __name__ == '__main__':
    consumer = MQPullConsumer('MQClient4Python-Consumer', 'jfxr-7:9876;jfxr-6:9876')
    consumer.init()
    consumer.start()

    consumer.fetchSubscribeMessageQueues("TopicTest") #获取所有消息队列,返回值存储到consumer.mqs
    for mq in consumer.mqs:
        label .SINGLE_MQ
        while True:
            try:
                pullResult = consumer.pullBlockIfNotFound(mq, '', consumer.getMessageQueueOffset(mq), settings.pullMaxNums)
                consumer.putMessageQueueOffset(mq, pullResult.getNextBeginOffset())
                pullStatus = pullResult.getPullStatus()
                if pullStatus == PullStatus['FOUND']:
                    logger.debug('Found')
                    print pullResult.toString()
                    #TODO: 进一步分析pull下来的result
                elif pullStatus == PullStatus['NO_NEW_MSG']:
                    logger.debug('NO_NEW_MSG')
                    goto .SINGLE_MQ
                elif pullStatus == PullStatus['NO_MATCHED_MSG']:
                    logger.debug('NO_MATCHED_MSG')
                elif pullStatus == PullStatus['OFFSET_ILLEGAL']:
                    logger.debug('OFFSET_ILLEGAL')
                else:
                    logger.debug('Found')
            except JavaException, ex:
                logger.error(str(ex.javaClass()) + str(ex.message()))
                logger.error(str(ex.stacktrace()))

    consumer.shutdown()

    shutdownJVM()
