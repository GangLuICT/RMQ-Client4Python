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
startJVM(jvmPath, "-ea", "-Djava.ext.dirs=" + settings.JAVA_EXT_DIRS)
#startJVM(jvmPath, "-Djava.class.path=" + settings.RMQClientJAR + ":")
print settings.JAVA_EXT_DIRS
logger.info(java.lang.System.getProperty("java.class.path"))
logger.info(java.lang.System.getProperty("java.ext.dirs"))

#启动JVM之后才能调用JPackage,否则找不到相关的jar包
from MQPullConsumer import *
from MQMessage import MQMessage, PullStatus

# 为了支持文本中文输入，要显式设置编码；该编码不影响Message的Body的编码
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8');

if __name__ == '__main__':
    consumer = MQPullConsumer('MQClient4Python-Consumer', 'jfxr-7:9876;jfxr-6:9876')
    consumer.init()
    consumer.start()

    consumer.fetchSubscribeMessageQueues("RMQTopicTest") #获取所有消息队列,返回值存储到consumer.mqs
    #TODO:
    #    1. fetchSubscribeMessageQueues可能返回异常：Can not find Message Queue for this topic
    #       如果不存在Topic，则创建topic：createTopic(String key, String newTopic, int queueNum)
    #    2. MessageQueue的数目，如何确定的！
    #    3. PullConsumer没有ConsumeFromWhere这项设置

    while True:
        for mq in consumer.mqs:
            logger.debug("Pulling from message queue: " + str(mq.queueId))
            while True:
                try:
                    pullResult = consumer.pullBlockIfNotFound(mq, '', consumer.getMessageQueueOffset(mq), settings.pullMaxNums)	# brokerSuspendMaxTimeMillis默认值是20s
                    consumer.putMessageQueueOffset(mq, pullResult.getNextBeginOffset())
                    pullStatus = PullStatus[str(pullResult.getPullStatus())]	# JAVA中的enum对应到Python中没有转换为Int，是原来的字符串！
                    if pullStatus == PullStatus['FOUND']:
                        logger.debug('Found')
                        logger.debug(pullResult.toString())
                        msgList = pullResult.getMsgFoundList()
                        for msg in msgList:
			    logger.debug(msg.toString())
                            # In Python 2.x, bytes is just an alias for str. 所以bytes解码时要注意了, msg.body.decode会出错！
			    logger.debug("Message body" + str(msg.body))
#			    logger.debug("Message body" + str(msg.body).decode(settings.MsgBodyEncoding))
                        #TODO: 进一步分析pull下来的result
                    elif pullStatus == PullStatus['NO_NEW_MSG']:
                        logger.debug('NO_NEW_MSG')
                        break
                    elif pullStatus == PullStatus['NO_MATCHED_MSG']:
                        logger.debug('NO_MATCHED_MSG')
                    elif pullStatus == PullStatus['OFFSET_ILLEGAL']:
                        logger.debug('OFFSET_ILLEGAL')
                    else:
                        logger.error('Wrong pull status: ' + str(pullStatus))
                except JavaException, ex:
                    logger.error(str(ex.javaClass()) + str(ex.message()))
                    logger.error(str(ex.stacktrace()))

    consumer.shutdown()

    shutdownJVM()
