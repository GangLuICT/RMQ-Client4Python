#!/usr/bin/python
# -*- coding:utf-8 -*-

from jpype import *
import logging
import settings_MQ as settings

logger = logging.getLogger("MQMessage")

__all__ = ["MQMessage", "PullStatus", "ConsumeFromWhere", "ConsumeConcurrentlyStatus", "ConsumeOrderlyStatus",
           "MessageModel"]

Message = JPackage('com.alibaba.rocketmq.common.message').Message


class MQMessage(object):
    def __init__(self, topic, tags, keys, body):
        self.topic = topic
        self.tags = tags
        self.keys = keys
        self.body = body
        self.msg = Message(JString(self.topic), JString(self.tags), JString(self.keys), self.body.encode(encoding = settings.MsgBodyEncoding))
	# JAVA prototype of Message
	#    public Message()
	#    public Message(String topic, byte[] body)
	#    public Message(String topic, String tags, String keys, byte[] body)
	#    public Message(String topic, String tags, String keys, int flag, byte[] body, boolean waitStoreMsgOK) 
    
    def tostr(self):
        """
        Translate the object into a string
        """
        return self.topic + "::" + self.tags + "::" + self.keys + "::" + self.body


# PullResult的返回结果
PullStatus = {
    'FOUND': 0,  # Founded
    'NO_NEW_MSG': 1,  # No new message can be pull
    'NO_MATCHED_MSG': 2,  # Filtering results can not match
    'OFFSET_ILLEGAL': 3   # Illegal offset，may be too big or too small
}

# PushConsumer消费时选择第一次订阅时的消费位置
ConsumeFromWhere = {
    # 一个新的订阅组第一次启动从队列的最后位置开始消费
    # 后续再启动接着上次消费的进度开始消费
    'CONSUME_FROM_LAST_OFFSET': 0,
    #@Deprecated
    'CONSUME_FROM_LAST_OFFSET_AND_FROM_MIN_WHEN_BOOT_FIRST': 1,
    #@Deprecated
    'CONSUME_FROM_MIN_OFFSET': 2,
    #@Deprecated
    'CONSUME_FROM_MAX_OFFSET': 3,
     # 一个新的订阅组第一次启动从队列的最前位置开始消费<br>
     # 后续再启动接着上次消费的进度开始消费
    'CONSUME_FROM_FIRST_OFFSET': 4,
     # 一个新的订阅组第一次启动从指定时间点开始消费,时间点设置参见DefaultMQPushConsumer.consumeTimestamp参数
     # 后续再启动接着上次消费的进度开始消费
    'CONSUME_FROM_TIMESTAMP': 5,
}

# PushConsumer消费后的返回值(并发消费时)
ConsumeConcurrentlyStatus = {
    'CONSUME_SUCCESS': 0,  # Success consumption
    'RECONSUME_LATER': 1,  # Failure consumption,later try to consume
}

# PushConsumer消费后的返回值(顺序消费时)
ConsumeOrderlyStatus ={
    'SUCCESS': 0,  # Success consumption
    'ROLLBACK': 1,  # Rollback consumption(only for binlog consumption)
    'COMMIT': 2,  # Commit offset(only for binlog consumption)
    'SUSPEND_CURRENT_QUEUE_A_MOMENT': 3   # Suspend current queue a moment
}

# PushConsumer的消息model
MessageModel = {
    'BROADCASTING': 0,  # broadcast
    'CLUSTERING': 1     # clustering
}