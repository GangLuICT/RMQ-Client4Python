# coding=utf-8

import os
import logging
import jpype

def main():
    jvmPath = jpype.getDefaultJVMPath()
    print jvmPath
    jpype.startJVM(jvmPath)
    #jpype.startJVM(jvmPath, "-Xms32m", "-Xmx256m", "-mx256m", "-Djava.class.path=/Users/tan9le/temp/some-lib.jar:")
    jpype.java.lang.System.out.println( " hello world! " )
    map = jpype.JClass("java.util.HashMap")()
    map.put("陆钢","123124")
    print map.get("陆钢")
    jpype.shutdownJVM()
