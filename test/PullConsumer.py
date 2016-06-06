#!/usr/bin/python
# -*- coding:utf-8 -*-

from jpype import *
from MQPullConsumer import *
from MQMessage import MQMessage, PULLSTATUS

from goto import goto, label

import logging
import settings_MQ as settings

logger = logging.getLogger("PullConsumer test")

if __name__ == '__main__':
    jvmPath = getDefaultJVMPath()
    startJVM(jvmPath, "-ea", "-Djava.class.path=" + settings.RMQClientJAR)
    #jpype.startJVM(jvmPath, "-Xms32m", "-Xmx256m", "-mx256m", "-Djava.class.path=/Users/tan9le/temp/some-lib.jar:")

    consumer = MQPullConsumer('MQClient4Python-Consumer', 'jfxr-7:9876;jfxr-6:9876')
    consumer.init()
    consumer.start()

    consumer.fetchSubscribeMessageQueues("TopicTest") #获取所有消息队列
    for mq in consumer.mqs:
        label .SINGLE_MQ
        while True:
            try:
                pullResult = consumer.pullBlockIfNotFound(mq, '', consumer.getMessageQueueOffset(mq), settings.pullMaxNums)
                consumer.putMessageQueueOffset(mq, pullResult.getNextBeginOffset())
                pullStatus = pullResult.getPullStatus()
                if pullStatus == PULLSTATUS['FOUND']:
                    logger.debug('Found')
                    #TODO
                elif pullStatus == PULLSTATUS['NO_NEW_MSG']:
                    logger.debug('NO_NEW_MSG')
                    goto .SINGLE_MQ
                elif pullStatus == PULLSTATUS['NO_MATCHED_MSG']:
                    logger.debug('NO_MATCHED_MSG')
                elif pullStatus == PULLSTATUS['OFFSET_ILLEGAL']:
                    logger.debug('OFFSET_ILLEGAL')
                else:
                    logger.debug('Found')
            except JavaException, ex:
                logger.error(str(ex.javaClass()) + str(ex.message()))
                logger.error(str(ex.stacktrace()))

    consumer.shutdown()

    shutdownJVM()
