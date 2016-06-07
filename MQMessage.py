#!/usr/bin/python
# -*- coding:utf-8 -*-

from jpype import *
import logging
import settings_MQ as settings

logger = logging.getLogger("MQMessage")

__all__ = ["MQMessage", "PULLSTATUS"]

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
PULLSTATUS = {
    'FOUND': 0,  # Founded
    'NO_NEW_MSG': 1,  # No new message can be pull
    'NO_MATCHED_MSG': 2,  # Filtering results can not match
    'OFFSET_ILLEGAL': 3   # Illegal offset，may be too big or too small
}

