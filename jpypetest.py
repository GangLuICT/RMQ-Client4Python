#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import logging
import jpype

# 为了支持中文输入，要显式设置编码
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8');

if __name__ == "__main__":
    jvmPath = jpype.getDefaultJVMPath()
    print jvmPath
    jpype.startJVM(jvmPath)
    #jpype.startJVM(jvmPath, "-Xms32m", "-Xmx256m", "-mx256m", "-Djava.class.path=/Users/tan9le/temp/some-lib.jar:")
    jpype.java.lang.System.out.println( " hello world! " )
    map = jpype.JClass("java.util.HashMap")()
    map.put("123","123124测试中文")
    print map.get("123")
    jpype.shutdownJVM()

