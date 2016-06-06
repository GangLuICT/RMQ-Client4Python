#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import logging
import jpype

__all__ = ["PullConsumer"]

DefaultMQPullConsumer= jpype.JPackage('com.alibaba.rocketmq.client.consumer.DefaultMQPullConsumer')
MQClientException = jpype.JPackage('com.alibaba.rocketmq.client.exception.MQClientException')
PullResult = jpype.JPackage('com.alibaba.rocketmq.client.consumer.PullResult')
MessageQueue = jpype.JPackage('com.alibaba.rocketmq.common.message.MessageQueue')

class PullConsumer(object):
    
    def ___init__(self):
    
    def start(self):
    # JAVA prototype
    #    public void start() throws MQClientException {
    
    def shutdown(self):
    # JAVA prototype
    #    public void shutdown() {
    
    def pullBlockIfNotFound(self, queue, ):
    # JAVA prototype
    #    public PullResult pullBlockIfNotFound(MessageQueue mq, String subExpression, long offset, int maxNums)
    #            throws MQClientException, RemotingException, MQBrokerException, InterruptedException {
    #    public void pullBlockIfNotFound(MessageQueue mq, String subExpression, long offset, int maxNums,
    #            PullCallback pullCallback) throws MQClientException, RemotingException, InterruptedException {
    
    def fetchSubscribeMessageQueues(self, topic):
    # JAVA prototype
    #    public Set<MessageQueue> fetchSubscribeMessageQueues(String topic) throws MQClientException {

