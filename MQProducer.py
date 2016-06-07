#!/usr/bin/python
# -*- coding:utf-8 -*-

from jpype import *
import logging
import time

logger = logging.getLogger("MQProducer")

__all__ = ["MQProducer"]

DefaultMQProducer = JPackage('com.alibaba.rocketmq.client.producer').DefaultMQProducer
MQClientException = JPackage('com.alibaba.rocketmq.client.exception').MQClientException
SendResult = JPackage('com.alibaba.rocketmq.client.producer').SendResult

class MQProducer(object):
    def __init__(self, groupName, namesrvAddr):
        """
        :param groupName:
        :param namesrvAddr:
        :return:
    # JAVA prototype(实现的是第2个,见init函数 实例化)
    #    public DefaultMQProducer() {
    #    public DefaultMQProducer(final String producerGroup) {
    #    public DefaultMQProducer(RPCHook rpcHook) {
    #    public DefaultMQProducer(final String producerGroup, RPCHook rpcHook) {
        """
        self.producer = None    #初始化放在了init函数中
        self.groupName = groupName
        self.namesrvAddr = namesrvAddr
        self.instanceName = str(int(time.time()*1000))  #毫秒值作为instance name
        self.compressMsgBodyOverHowmuch = 4096  #消息压缩阈值

    def init(self):
        """批量设置一些基本项(为了尽可能少实现这些API接口,如以后有需要,可以逐个移出init)"""
        logger.info('Initializing producer ' + self.instanceName + ' ...')
        self.producer = DefaultMQProducer(JString(self.groupName))   #创建实例
        self.producer.setNamesrvAddr(JString(self.namesrvAddr))
        self.producer.setInstanceName(JString(self.instanceName))
        self.producer.setCompressMsgBodyOverHowmuch(JInt(self.compressMsgBodyOverHowmuch))

    def start(self):
        """
    # JAVA prototype
    #    public void start() throws MQClientException {
        """
        logger.info('Starting producer ' + self.instanceName + ' ...')
        self.producer.start()
    
    def shutdown(self):
        """
    # JAVA prototype
    #     public void shutdown() {
        """
        logger.info('Shutting down producer ' + self.instanceName + ' ...')
        self.producer.shutdown()
    
    def send(self, MQMsg):
        """
    # JAVA prototype
    #    public SendResult send(Message msg, long timeout) throws MQClientException, RemotingException,
    #            MQBrokerException, InterruptedException {
    #    public void send(Message msg, SendCallback sendCallback) throws MQClientException, RemotingException,
    #            InterruptedException {
    #    public void send(Message msg, SendCallback sendCallback, long timeout) throws MQClientException,
    #            RemotingException, InterruptedException {
    #    public void sendOneway(Message msg) throws MQClientException, RemotingException, InterruptedException {
    #    public SendResult send(Message msg, MessageQueue mq) throws MQClientException, RemotingException,
    #            MQBrokerException, InterruptedException {
    #    public SendResult send(Message msg, MessageQueue mq, long timeout) throws MQClientException,
    #            RemotingException, MQBrokerException, InterruptedException {
    #    public void send(Message msg, MessageQueue mq, SendCallback sendCallback) throws MQClientException,
    #            RemotingException, InterruptedException {
    #    public void send(Message msg, MessageQueue mq, SendCallback sendCallback, long timeout)
    #            throws MQClientException, RemotingException, InterruptedException {
    #    public SendResult send(Message msg, MessageQueueSelector selector, Object arg) throws MQClientException,
    #            RemotingException, MQBrokerException, InterruptedException {
    #    public SendResult send(Message msg, MessageQueueSelector selector, Object arg, long timeout)
    #            throws MQClientException, RemotingException, MQBrokerException, InterruptedException {
    #    public void send(Message msg, MessageQueueSelector selector, Object arg, SendCallback sendCallback)
    #            throws MQClientException, RemotingException, InterruptedException {
    #    public void send(Message msg, MessageQueueSelector selector, Object arg, SendCallback sendCallback,
    #            long timeout) throws MQClientException, RemotingException, InterruptedException {
        """
        logger.debug('Producer ' + self.instanceName + ' sending message: ' + MQMsg.tostr())
        self.producer.send(MQMsg.msg)
    
    def sendOneway(self, MQMsg):
        """
    # JAVA prototype
    #    public void sendOneway(Message msg) throws MQClientException, RemotingException, InterruptedException {
    #    public void sendOneway(Message msg, MessageQueue mq) throws MQClientException, RemotingException,
    #            InterruptedException {
    #    public void sendOneway(Message msg, MessageQueueSelector selector, Object arg) throws MQClientException,
    #            RemotingException, InterruptedException {
        """
        logger.debug('Producer ' + self.instanceName + ' sending one-way message: ' + MQMsg.tostr())
        self.producer.sendOneway(MQMsg.msg)
