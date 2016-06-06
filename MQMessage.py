#!/usr/bin/python
# -*- coding:utf-8 -*-

from jpype import *
import logging

logger = logging.getLogger("MQMessage")

__all__ = ["MQMessage", "PULLSTATUS"]

Message = JPackage('com.alibaba.rocketmq.common.message').Message


class MQMessage(object):
    def __init__(self, topic, tags, keys, body):
        self.topic = topic
        self.tags = tags
        self.keys = keys
        self.body = body
        self.msg = Message(JString(self.topic), JString(self.tags), JString(self.keys), JByte(self.body))
    
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

