#!/usr/bin/python
# -*- coding:utf-8 -*-

from jpype import *
import logging
import time

logger = logging.getLogger("MQPullConsumer")

__all__ = ["MQPullConsumer", "getMessageQueueOffset", "putMessageQueueOffset"]

DefaultMQPullConsumer= JPackage('com.alibaba.rocketmq.client.consumer').DefaultMQPullConsumer
MQClientException = JPackage('com.alibaba.rocketmq.client.exception').MQClientException
PullResult = JPackage('com.alibaba.rocketmq.client.consumer').PullResult
MessageQueue = JPackage('com.alibaba.rocketmq.common.message').MessageQueue


class MQPullConsumer(object):
    
    def __init__(self, groupName, namesrvAddr):
        """
        :param groupName:
        :param namesrvAddr:
        :return:
        """
        self.consumer = None    #初始化放在了init函数中
        self.groupName = groupName
        self.namesrvAddr = namesrvAddr
        self.instanceName = str(int(time.time()*1000))  #毫秒值作为instance name

        self.mqs = None
        self.offseTable = {}    # map of message queue id to queue offset

    @classmethod
    def init(self):
        """批量设置一些基本项(为了尽可能少实现这些API接口,如以后有需要,可以逐个移出init)"""
        logger.info('Initializing consumer ' + self.instanceName + ' ...')
        self.consumer = DefaultMQPullConsumer(JString(self.groupName))   #创建实例
        self.consumer.setNamesrvAddr(JString(self.namesrvAddr))
        self.consumer.setInstanceName(JString(self.instanceName))

    @classmethod
    def start(self):
        """
    # JAVA prototype
    #    public void start() throws MQClientException {
        """
        logger.info('Starting consumer ' + self.instanceName + ' ...')
        self.consumer.start()

    @classmethod
    def shutdown(self):
        """
    # JAVA prototype
    #    public void shutdown() {
        """
        logger.info('Shutting down consumer ' + self.instanceName + ' ...')
        self.consumer.shutdown()

    @classmethod
    def pullBlockIfNotFound(self, mq, subExpression, offset, maxNums):
        """
    # JAVA prototype
    #    public PullResult pullBlockIfNotFound(MessageQueue mq, String subExpression, long offset, int maxNums)
    #            throws MQClientException, RemotingException, MQBrokerException, InterruptedException {
    #    public void pullBlockIfNotFound(MessageQueue mq, String subExpression, long offset, int maxNums,
    #            PullCallback pullCallback) throws MQClientException, RemotingException, InterruptedException {
        """
        pullResult = self.consumer.pullBlockIfNotFound(mq, subExpression, self.getMessageQueueOffset(mq), maxNums)
        return pullResult

    @classmethod
    def fetchSubscribeMessageQueues(self, topic):
        """
    # JAVA prototype
    #    public Set<MessageQueue> fetchSubscribeMessageQueues(String topic) throws MQClientException {
        """
        self.mqs = self.consumer.fetchSubscribeMessageQueues(JString(topic))

    @classmethod
    def getMessageQueueOffset(self, mq):
        """
        获取某个MQ中的当前消息的offset
        :param mq:
        :return:
        """
        offset = self.offseTable[mq.queueId]
        if offset != None:
            return offset
        else:
            return 0

    @classmethod
    def putMessageQueueOffset(self, mq, offset):
        """
        设置某个MQ中的当前消息的offset(更新后的值)
        :param mq:
        :param offset:
        :return:
        """
        self.offseTable[mq.queueId] = offset
