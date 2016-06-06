#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import logging
import jpype

__all__ = ["RMQClient"]

DefaultMQProducer = jpype.JPackage('com.alibaba.rocketmq.client.producer.DefaultMQProducer')
MQClientException = jpype.JPackage('com.alibaba.rocketmq.client.exception.MQClientException')
SendResult = jpype.JPackage('com.alibaba.rocketmq.client.producer.SendResult')
Message = jpype.JPackage('com.alibaba.rocketmq.common.message.Message')

class Producer(object):

    def ___init__(self):
    
    def start(self):
    # JAVA prototype
    #    public void start() throws MQClientException {
    
    def shutdown(self):
    # JAVA prototype
    #     public void shutdown() {
    
    def send(self, msg):
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
    
    
    def sendOneway(self):
    # JAVA prototype
    #    public void sendOneway(Message msg, MessageQueue mq) throws MQClientException, RemotingException,
    #            InterruptedException {
    #    public void sendOneway(Message msg, MessageQueueSelector selector, Object arg) throws MQClientException,
    #            RemotingException, InterruptedException {

