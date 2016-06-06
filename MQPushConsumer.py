#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import logging
import jpype

__all__ = ["MQPushConsumer"]

DefaultMQPushConsumer= jpype.JPackage('com.alibaba.rocketmq.client.consumer.DefaultMQPushConsumer')
MQClientException = jpype.JPackage('com.alibaba.rocketmq.client.exception.MQClientException')
MessageExt = jpype.JPackage('com.alibaba.rocketmq.common.message.MessageExt')
ConsumeFromWhere = jpype.JPackage('com.alibaba.rocketmq.common.consumer.ConsumeFromWhere')
ConsumeConsurrentlyContext = jpype.JPackage('com.alibaba.rocketmq.client.consumer.listener.ConsumeConsurrentlyContext')
ConsumeConsurrentlyStatus = jpype.JPackage('com.alibaba.rocketmq.client.consumer.listener.ConsumeConsurrentlyStatus')
MessageListenerConcurrently = jpype.JPackage('com.alibaba.rocketmq.client.consumer.listener.MessageListenerConcurrently')


class MQPushConsumer(object):
    
    def ___init__(self):
    
    def start(self):
    # JAVA prototype
    #    public void start() throws MQClientException {
    
    def shutdown(self):
    # JAVA prototype
    #    public void shutdown() {
    
    def subscribe(self):
    # JAVA prototype
    #    public void subscribe(String topic, String subExpression) throws MQClientException {
    #    public void subscribe(String topic, String fullClassName, String filterClassSource) throws MQClientException {
    
    def unsubscribe(self):
    # JAVA prototype
    #    public void unsubscribe(String topic) {

    def setConsumeFromWhere(self):
    # JAVA prototype
    #    public void setConsumeFromWhere(ConsumeFromWhere consumeFromWhere) {
    
    def registerMessageListener(self, topic):
    # JAVA prototype
    #    public void registerMessageListener(MessageListenerConcurrently messageListener) {
    #    public void registerMessageListener(MessageListenerOrderly messageListener) {


