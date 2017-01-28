---
title: pod search XXX 仓库版本低于 Github 仓库版本
date: 2016-09-30 17:05:02
tags:
---

## pod search XXX 仓库版本低于 Github 仓库版本
XXX 为第三方库的名字,以 pod search SDWebImage 为例

本地终端命令进行搜索,显示最最新版本为 3.7.3
![](http://obr2ozlb6.bkt.clouddn.com/14752042330301.jpg)

而 github 上的SDWebImage已经更新到了 3.8 版本
![](http://obr2ozlb6.bkt.clouddn.com/14752193391208.jpg)

原因:Cocoapods 在安装时会将第三方库的索引下载到本地 **~/.cocoapods/repos/master/Specs**目录下
![](http://obr2ozlb6.bkt.clouddn.com/14752214374894.jpg)
我们在本地搜索的时候搜到只是 cocoapods 安装时下载到本地的索引,搜索不到最新版本,是因为 Cocoapods 镜像索引库更新了,而本地的索引库却没更新! 
前往 **~/.cocoapods/repos/master** 目录下查看 **CocoaPods-version.yml** 确认本地Cocoapods的版本   
	`min: 0.32.1`     
	`last: 0.39.0` 

再来到 [github上的Cocoapods版本描述](https://github.com/CocoaPods/Specs/blob/master/CocoaPods-version.yml)查看Cocoapods最新的版本描述,明显是本地的Cocoapods版本过低
    ![](http://obr2ozlb6.bkt.clouddn.com/14752035139251.jpg)
        
解决方法:</br>
第一种: [更新本地索引库 ](https://guides.cocoapods.org/terminal/commands.html#pod_repo_update)   
`$ pod repo update`         
第二种: 升级 Cocoapods    
    `$ sudo gem update --system`       
    `$ gem sources --remove https://rubygems.org/`           
    `$ gem sources -a https://ruby.taobao.org/`              
    `$ sudo gem install cocoapods `             
    `$ pod setup`      
第三种: 卸载 重装         
   ` sudo gem uninstall cocoapods `       
    重复第二种方法安装Cocoapods      
第四种: `$ pod setup ` 
   
再次 `$ pod search SDWebimage` 已成功搜索到 SDWebimage 3.8.1 版本
![](http://obr2ozlb6.bkt.clouddn.com/14752256205791.jpg)

#### 参考链接
[解决pod search出来的仓库版本低于github仓库版本的方法](https://github.com/dabing1022/Blog/issues/3)

[从项目中移除 CocoaPods](http://stackoverflow.com/questions/16427421/how-to-remove-cocoapods-from-a-project?rq=1)

[NSHipster 上对Cocoa​Pods的介绍与使用](http://nshipster.cn/cocoapods/)

[Cocoapods官方命令使用](https://guides.cocoapods.org/terminal/commands.html#commands)

[第三方库在Cocoapodss上的使用文档](http://cocoadocs.org/)

[最新Mac OS X 10.11.1 安装cocoapods及使用详解](http://www.jianshu.com/p/b64b4fd08d3c)


