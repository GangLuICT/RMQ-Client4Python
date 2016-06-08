#!/usr/bin/python
# -*- coding:utf-8 -*-

from jpype import *
import logging
import settings_MQ as settings

logger = logging.getLogger("MQMessage")

__all__ = ["MQMessage", "PullStatus", "ConsumeFromWhere", "ConsumeConcurrentlyStatus", "ConsumeOrderlyStatus",
           "MessageModel"]

Message = JPackage('com.alibaba.rocketmq.common.message').Message
# enum classes:
PULLSTATUS = JPackage('com.alibaba.rocketmq.client.consumer').PullStatus
CONSUMEFROMWHERE = JPackage('com.alibaba.rocketmq.common.consumer').ConsumeFromWhere
CONSUMECONCURRENTLYSTATUS = JPackage('com.alibaba.rocketmq.client.consumer.listener').ConsumeConcurrentlyStatus
CONSUMEORDERLYSTATUS = JPackage('com.alibaba.rocketmq.client.consumer.listener').ConsumeOrderlyStatus
MESSAGEMODEL = JPackage('com.alibaba.rocketmq.common.protocol.heartbeat').MessageModel


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
    #'FOUND': 0,  # Founded
    'FOUND': PULLSTATUS.FOUND,
    #'NO_NEW_MSG': 1,  # No new message can be pull
    'NO_NEW_MSG': PULLSTATUS.NO_NEW_MSG,
    #'NO_MATCHED_MSG': 2,  # Filtering results can not match
    'NO_MATCHED_MSG': PULLSTATUS.NO_MATCHED_MSG,
    #'OFFSET_ILLEGAL': 3   # Illegal offset，may be too big or too small
    'OFFSET_ILLEGAL': PULLSTATUS.OFFSET_ILLEGAL
}

# PushConsumer消费时选择第一次订阅时的消费位置
ConsumeFromWhere = {
    # 一个新的订阅组第一次启动从队列的最后位置开始消费
    # 后续再启动接着上次消费的进度开始消费
    #'CONSUME_FROM_LAST_OFFSET': 0,
    'CONSUME_FROM_LAST_OFFSET': CONSUMEFROMWHERE.CONSUME_FROM_LAST_OFFSET,
    #@Deprecated
    #'CONSUME_FROM_LAST_OFFSET_AND_FROM_MIN_WHEN_BOOT_FIRST': 1,
    'CONSUME_FROM_LAST_OFFSET_AND_FROM_MIN_WHEN_BOOT_FIRST': CONSUMEFROMWHERE.CONSUME_FROM_LAST_OFFSET_AND_FROM_MIN_WHEN_BOOT_FIRST,
    #@Deprecated
    #'CONSUME_FROM_MIN_OFFSET': 2,
    'CONSUME_FROM_MIN_OFFSET': CONSUMEFROMWHERE.CONSUME_FROM_MIN_OFFSET,
    #@Deprecated
    #'CONSUME_FROM_MAX_OFFSET': 3,
    'CONSUME_FROM_MAX_OFFSET': CONSUMEFROMWHERE.CONSUME_FROM_MAX_OFFSET,
     # 一个新的订阅组第一次启动从队列的最前位置开始消费<br>
     # 后续再启动接着上次消费的进度开始消费
    #'CONSUME_FROM_FIRST_OFFSET': 4,
    'CONSUME_FROM_FIRST_OFFSET': CONSUMEFROMWHERE.CONSUME_FROM_FIRST_OFFSET,
     # 一个新的订阅组第一次启动从指定时间点开始消费,时间点设置参见DefaultMQPushConsumer.consumeTimestamp参数
     # 后续再启动接着上次消费的进度开始消费
    #'CONSUME_FROM_TIMESTAMP': 5,
    'CONSUME_FROM_TIMESTAMP': CONSUMEFROMWHERE.CONSUME_FROM_TIMESTAMP,
}

# PushConsumer消费后的返回值(并发消费时)
ConsumeConcurrentlyStatus = {
    #'CONSUME_SUCCESS': 0,  # Success consumption
    'CONSUME_SUCCESS': CONSUMECONCURRENTLYSTATUS.CONSUME_SUCCESS,
    #'RECONSUME_LATER': 1,  # Failure consumption,later try to consume
    'RECONSUME_LATER': CONSUMECONCURRENTLYSTATUS.RECONSUME_LATER,
}

# PushConsumer消费后的返回值(顺序消费时)
ConsumeOrderlyStatus ={
    #'SUCCESS': 0,  # Success consumption
    'SUCCESS': CONSUMEORDERLYSTATUS.SUCCESS,
    #'ROLLBACK': 1,  # Rollback consumption(only for binlog consumption)
    'ROLLBACK': CONSUMEORDERLYSTATUS.ROLLBACK,
    #'COMMIT': 2,  # Commit offset(only for binlog consumption)
    'COMMIT': CONSUMEORDERLYSTATUS.COMMIT,
    #'SUSPEND_CURRENT_QUEUE_A_MOMENT': 3   # Suspend current queue a moment
    'SUSPEND_CURRENT_QUEUE_A_MOMENT': CONSUMEORDERLYSTATUS.SUSPEND_CURRENT_QUEUE_A_MOMENT
}

# PushConsumer的消息model
MessageModel = {
    #'BROADCASTING': 0,  # broadcast
    'BROADCASTING': MESSAGEMODEL.BROADCASTING,
    #'CLUSTERING': 1     # clustering
    'CLUSTERING': MESSAGEMODEL.CLUSTERING
}
