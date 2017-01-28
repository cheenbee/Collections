---
title: isa 指针
date: 2016-08-02 22:19:56
tags:
---
1. isa 是什么
	先来看一下 isa 指针所处的位置 
	查看objc/runtime.h中objc_class结构体:
	![](http://obr2ozlb6.bkt.clouddn.com/14712708907916.jpg)
在 objc.h 中可以查找到 Class 是一个 objc_class 结构体类型指针:
 ```/// An opaque type that represents an Objective-C class.  
 typedef struct objc_class *Class;
```
而 isa 是一个 Class 类型的指针
![](http://obr2ozlb6.bkt.clouddn.com/14712763926115.jpg)

	
参考
	[Objective-C Runtime 运行时之一：类与对象](http://southpeak.github.io/blog/2014/10/25/objective-c-runtime-yun-xing-shi-zhi-lei-yu-dui-xiang/) by 南峰子


