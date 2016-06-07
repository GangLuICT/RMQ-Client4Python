#!/usr/bin/python
# -*- coding:utf-8 -*-

from jpype import *
import logging
import time

logger = logging.getLogger("MQPullConsumer")

__all__ = ["MQPushConsumer", "msgListenerConcurrently", "msgListenerOrderly"]

DefaultMQPushConsumer= JPackage('com.alibaba.rocketmq.client.consumer').DefaultMQPushConsumer
MQClientException = JPackage('com.alibaba.rocketmq.client.exception').MQClientException
#MessageExt = JPackage('com.alibaba.rocketmq.common.message').MessageExt
#ConsumeConsurrentlyContext = JPackage('com.alibaba.rocketmq.client.consumer.listener').ConsumeConsurrentlyContext
#ConsumeConsurrentlyStatus = JPackage('com.alibaba.rocketmq.client.consumer.listener').ConsumeConsurrentlyStatus
#MessageListenerConcurrently = JPackage('com.alibaba.rocketmq.client.consumer.listener').MessageListenerConcurrently

from MQMessage import ConsumeConcurrentlyStatus, ConsumeOrderlyStatus

class MQPushConsumer(object):
    '''实现类
    public class DefaultMQPushConsumer extends ClientConfig implements MQPushConsumer {
    '''
    
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

    def init(self):
        """批量设置一些基本项(为了尽可能少实现这些API接口,如以后有需要,可以逐个移出init)"""
        logger.info('Initializing consumer ' + self.instanceName + ' ...')
        self.consumer = DefaultMQPushConsumer(JString(self.groupName))   #创建实例
        self.consumer.setNamesrvAddr(JString(self.namesrvAddr))
        self.consumer.setInstanceName(JString(self.instanceName))

    def start(self):
        """
    # JAVA prototype
    #    public void start() throws MQClientException {
        """
        logger.info('Starting consumer ' + self.instanceName + ' ...')
        self.consumer.start()

    def shutdown(self):
        """
    # JAVA prototype
    #    public void shutdown() {
        """
        logger.info('Shutting down consumer ' + self.instanceName + ' ...')
        self.consumer.shutdown()

    def setMessageModel(self, messageModel):
        """
    # JAVA prototype
    #    public void setMessageModel(MessageModel messageModel)
        """
        logger.info('Setting message model of instance ' + self.instanceName + ' to ' + messageModel)
        self.consumer.setMessageModel(JInt(messageModel))

    def subscribe(self, topic, subExpression):
    # JAVA prototype
    #    public void subscribe(String topic, String subExpression) throws MQClientException {
    #    public void subscribe(String topic, String fullClassName, String filterClassSource) throws MQClientException {
        self.consumer.subscribe(JString(topic), JString(subExpression))

    def unsubscribe(self, topic):
    # JAVA prototype
    #    public void unsubscribe(String topic) {
        self.consumer.unsubscribe(JString(topic))

    def setConsumeFromWhere(self, fromwhere):
    # JAVA prototype
    #    public void setConsumeFromWhere(ConsumeFromWhere consumeFromWhere) {
        self.consumer.setConsumeFromWhere(JInt(fromwhere))

    def registerMessageListener(self, listener):
    # JAVA prototype
    #    public void registerMessageListener(MessageListenerConcurrently messageListener) {
    #    public void registerMessageListener(MessageListenerOrderly messageListener) {
        self.consumer.registerMessageListener(listener)


class MessageListenerConcurrently:
    '''接口类MessageListenerConcurrently的实现
    public interface MessageListenerConcurrently extends MessageListener {
    '''
    def consumeMessage(self, msgs, context):
    # JAVA prototype
    #    ConsumeConcurrentlyStatus consumeMessage(final List<MessageExt> msgs, final ConsumeConcurrentlyContext context);
        msg = msgs.get(JInt(0))
        if msg.getTopic() == "TopicTest":
            # 执行TopicTest的消费逻辑
            if msg.getTags() == "TagA":
                # 执行TagA的消费
                logger.debug("Got message with topic " + msg.getTopic() + " and tags " + msg.getTags)
            elif msg.getTags() == "TagC":
                # 执行TagC的消费
                logger.debug("Got message with topic " + msg.getTopic() + " and tags " + msg.getTags)
            elif msg.getTags() == "TagD":
                # 执行TagD的消费
                logger.debug("Got message with topic " + msg.getTopic() + " and tags " + msg.getTags)
        elif msg.getTopic() == "TopicTest1":
            # 执行TopicTest1的消费逻辑
            logger.debug("Got message with topic " + msg.getTopic() + " and tags " + msg.getTags)

        return ConsumeConcurrentlyStatus['CONSUME_SUCCESS']

#实现
msgListenerConcurrently = MessageListenerConcurrently()
JProxy("MessageListenerConcurrently", inst = msgListenerConcurrently)

class MessageListenerOrderly:
    '''接口类MessageListenerOrderly的实现
    public interface MessageListenerOrderly extends MessageListener {
    '''
    def __init__(self):
        #JAVA原子类
        self.consumeTimes = java.util.concurrent.atomic.AtomicLong(0)

    def consumeMessage(self, msgs, context):
    # JAVA prototype
    #    ConsumeOrderlyStatus consumeMessage(final List<MessageExt> msgs, final ConsumeOrderlyContext context);
        context.setAutoCommit(False)
        logger.debug(java.lang.Thread.currentThread().getName() + " Receive New Messages: " + msgs.toString())
        #TODO: msgs.toString()可能需要改成for msg in msgs: msg.toString()

        self.consumeTimes.incrementAndGet()

        if (self.consumeTimes.get() % 2) == 0:
            return ConsumeOrderlyStatus['SUCCESS']
        elif (self.consumeTimes.get() % 3) == 0:
            return ConsumeOrderlyStatus['ROLLBACK']
        elif (self.consumeTimes.get() % 4) == 0:
            return ConsumeOrderlyStatus['COMMIT']
        elif (self.consumeTimes.get() % 5) == 0:
            context.setSuspendCurrentQueueTimeMillis(3000)
            return ConsumeOrderlyStatus['SUSPEND_CURRENT_QUEUE_A_MOMENT']

        return ConsumeOrderlyStatus['SUCCESS']

#实现
msgListenerOrderly = MessageListenerOrderly()
JProxy("MessageListenerOrderly", inst = msgListenerOrderly)
