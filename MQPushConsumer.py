#!/usr/bin/python
# -*- coding:utf-8 -*-

from jpype import *
import logging
import time
import settings_MQ as settings

logger = logging.getLogger("MQPullConsumer")

__all__ = ["MQPushConsumer"]

DefaultMQPushConsumer= JPackage('com.alibaba.rocketmq.client.consumer').DefaultMQPushConsumer
MQClientException = JPackage('com.alibaba.rocketmq.client.exception').MQClientException
#MessageExt = JPackage('com.alibaba.rocketmq.common.message').MessageExt
#ConsumeConsurrentlyContext = JPackage('com.alibaba.rocketmq.client.consumer.listener').ConsumeConsurrentlyContext
#ConsumeConsurrentlyStatus = JPackage('com.alibaba.rocketmq.client.consumer.listener').ConsumeConsurrentlyStatus
#MessageListenerConcurrently = JPackage('com.alibaba.rocketmq.client.consumer.listener').MessageListenerConcurrently

#from MQMessage import ConsumeConcurrentlyStatus, ConsumeOrderlyStatus

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
        logger.info('Setting message model of instance ' + self.instanceName + ' to ' + str(messageModel))
        #self.consumer.setMessageModel(JObject(messageModel, "com.alibaba.rocketmq.common.protocol.heartbeat.MessageModel"))
        self.consumer.setMessageModel(messageModel)

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
        #self.consumer.setConsumeFromWhere(JObject(fromwhere, "com.alibaba.rocketmq.common.consumer.ConsumeFromWhere"))
        self.consumer.setConsumeFromWhere(fromwhere)

    def registerMessageListener(self, listener):
    # JAVA prototype
    #    public void registerMessageListener(MessageListenerConcurrently messageListener) {
    #    public void registerMessageListener(MessageListenerOrderly messageListener) {
        self.consumer.registerMessageListener(listener)

# 下面内容移除到MQMesasgeListener.py中
#
# class MessageListenerConcurrently:
#     '''接口类MessageListenerConcurrently的实现
#     public interface MessageListenerConcurrently extends MessageListener {
#     '''
#     def consumeMessage(self, msgs, context):
#         '''
#     # JAVA prototype
#     #    ConsumeConcurrentlyStatus consumeMessage(final List<MessageExt> msgs, final ConsumeConcurrentlyContext context);
#         '''
#         logger.debug("Into consumerMessage of MessageListenerConcurrently")
#         #msg = msgs.get(JInt(0))
#         for msg in msgs:
#             topic = msg.getTopic()
#             tags = msg.getTags()
#             body = str(msg.getBody()).decode(settings.MsgBodyEncoding)
#
#             logger.debug(msg.toString())
#             # In Python 2.x, bytes is just an alias for str. 所以bytes解码时要注意了, msg.body.decode会出错(bytes没有decode方法)！
#             #logger.debug("Message body: " + str(msg.getBody()))
#             #logger.debug("Message body: " + str(msg.getBody()).decode(settings.MsgBodyEncoding))
#             logger.debug("Message body: " + body)
#
#             if topic == "RMQTopicTest":
#                 # 执行TopicTest的消费逻辑
#                 if tags == "TagA":
#                     # 执行TagA的消费
#                     logger.debug("Got message with topic " + topic + " and tags " + tags)
#                 elif tags == "TagB":
#                     # 执行TagB的消费
#                     logger.debug("Got message with topic " + topic + " and tags " + tags)
#                 elif tags == "TagC":
#                     # 执行TagC的消费
#                     logger.debug("Got message with topic " + topic + " and tags " + tags)
#                 else:
#                     # 错误的Tag
#                     logger.error("Got message with topic " + topic + " and UNKNOWN tags " + tags)
#             elif topic == "TopicTest1":
#                 # 执行TopicTest1的消费逻辑
#                 logger.debug("Got message with topic " + topic + " and tags " + tags)
#             else:
#                 logger.debug("Got message with UNKNOWN topic " + topic )
#
#         return ConsumeConcurrentlyStatus['CONSUME_SUCCESS']
#
# #实现
# msgListenerConcurrently = MessageListenerConcurrently()
# #JProxy("MessageListenerConcurrently", inst = msgListenerConcurrently)
# msgListenerConcurrentlyProxy = JProxy("com.alibaba.rocketmq.client.consumer.listener.MessageListenerConcurrently", inst = msgListenerConcurrently)
#
# class MessageListenerOrderly:
#     '''接口类MessageListenerOrderly的实现
#     public interface MessageListenerOrderly extends MessageListener {
#     '''
#     def __init__(self):
#         #JAVA原子类
#         self.consumeTimes = java.util.concurrent.atomic.AtomicLong(0)
#
#     def consumeMessage(self, msgs, context):
#     # JAVA prototype
#     #    ConsumeOrderlyStatus consumeMessage(final List<MessageExt> msgs, final ConsumeOrderlyContext context);
#         context.setAutoCommit(False)
#         logger.debug(java.lang.Thread.currentThread().getName() + " Receive New Messages: " + msgs.toString())
#         #TODO: msgs.toString()可能需要改成for msg in msgs: msg.toString()
#
#         self.consumeTimes.incrementAndGet()
#         consumeTimes = self.consumeTimes.get()
# #	print consumeTimes
# #	print type(consumeTimes)
#
#         if (consumeTimes % 2) == 0:
#             logger.debug("consumeTimes % 2 = 0, return SUCCESS")
#             return ConsumeOrderlyStatus['SUCCESS']
#         elif (consumeTimes % 3) == 0:
#             logger.debug("consumeTimes % 3 = 0, return ROLLBACK")
#             return ConsumeOrderlyStatus['ROLLBACK']
#         elif (consumeTimes % 4) == 0:
#             logger.debug("consumeTimes % 4 = 0, return COMMIT")
#             return ConsumeOrderlyStatus['COMMIT']
#         elif (consumeTimes % 5) == 0:
#             logger.debug("consumeTimes % 5 = 0, return SUSPEND_CURRENT_QUEUE_A_MOMENT")
#             context.setSuspendCurrentQueueTimeMillis(3000)
#             return ConsumeOrderlyStatus['SUSPEND_CURRENT_QUEUE_A_MOMENT']
#         else:
#             logger.debug("consumeTimes is not times of 2, 3, 4, 5, return SUCCESS")
#             return ConsumeOrderlyStatus['SUCCESS']
#
# #实现
# msgListenerOrderly = MessageListenerOrderly()
# #JProxy("MessageListenerOrderly", inst = msgListenerOrderly)
# msgListenerOrderlyProxy = JProxy("com.alibaba.rocketmq.client.consumer.listener.MessageListenerOrderly", inst = msgListenerOrderly)
#
