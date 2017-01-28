---
title: Mac OS X El Capitan 下安装 Scrapy
date: 2016-10-10 17:00:00
tags: python spider
---

### Mac OS X El Capitan 下安装 Scrapy

##### `$ pip install scrapy`
##### 安装出错: OSError: [Errno 1] Operation not permitted
```
The directory '/Users/aiyouyou/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/aiyouyou/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting scrapy
  Downloading Scrapy-1.2.0-py2.py3-none-any.whl (294kB)
    100% |████████████████████████████████| 296kB 40kB/s 
Collecting service-identity (from scrapy)
  Downloading service_identity-16.0.0-py2.py3-none-any.whl
Collecting Twisted>=10.0.0 (from scrapy)
Collecting lxml (from scrapy)
Collecting parsel>=0.9.3 (from scrapy)
  Downloading parsel-1.0.3-py2.py3-none-any.whl
Collecting cssselect>=0.9 (from scrapy)
  Downloading cssselect-0.9.2-py2.py3-none-any.whl
Collecting PyDispatcher>=2.0.5 (from scrapy)
Collecting w3lib>=1.15.0 (from scrapy)
  Downloading w3lib-1.15.0-py2.py3-none-any.whl
Collecting queuelib (from scrapy)
  Downloading queuelib-1.4.2-py2.py3-none-any.whl
Collecting six>=1.5.2 (from scrapy)
  Downloading six-1.10.0-py2.py3-none-any.whl
Requirement already satisfied (use --upgrade to upgrade): pyOpenSSL in /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python (from scrapy)
Collecting pyasn1 (from service-identity->scrapy)
  Downloading pyasn1-0.1.9-py2.py3-none-any.whl
Collecting pyasn1-modules (from service-identity->scrapy)
  Downloading pyasn1_modules-0.0.8-py2.py3-none-any.whl
Collecting attrs (from service-identity->scrapy)
  Downloading attrs-16.2.0-py2.py3-none-any.whl
Requirement already satisfied (use --upgrade to upgrade): zope.interface>=3.6.0 in /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python (from Twisted>=10.0.0->scrapy)
Requirement already satisfied (use --upgrade to upgrade): setuptools in /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python (from zope.interface>=3.6.0->Twisted>=10.0.0->scrapy)

```

![](http://obr2ozlb6.bkt.clouddn.com/14760941648778.jpg)
    
##### 原因: 
 “OSError: [Errno 1] Operation not permitted” when installing Scrapy in OSX 10.11 (El Capitan) (System Integrity Protection).
  This is because OS X El Capitan ships with six 1.4.1 installed already and when it attempts to uninstall it (because awscli depends on botocore, botocore depends on python-dateutil, and python-dateutil depends on six >= 1.5) it doesn't have permission to do so because System Integrity Protection doesn't allow even root to modify those directories.
  Ideally, pip should just skip uninstalling those items since they aren't installed to site-packages they are installed to a special Apple directory. However, even if pip skips uninstalling those items and installs six into site-packages we'll hit another bug where Apple puts their pre-installed stuff earlier in the sys.path than site-packages. I've talked to Apple about this and I'm not sure if they're going to do anything about it or not.

大致意思是: OSX EI Capitan 内置了一个叫做 [系统健全保护](https://support.apple.com/en-us/HT204899) 的保护机制，OSX EI Capitan系统已经安装了six 1.4.1，任何用户（包括root）都没有权限卸载它,而使用 pip 安装 scrapy 的时候,需要卸载系统内置的 six, 然后重新安装,因此出错

    
##### 解决方法:
    第一种方法: 选择忽略 OS X El Capitan 系统已经安装的 six          
    $ sudo pip install scrapy --ignore-installed six
    
    第二种方法: 关闭苹果的 SIP (System Integrity Protection)
        1. 重启 Mac，按住 Command+R 键直到 Apple logo 出现，进入 Recovery Mode
        2. 顶部导航栏，点击 Utilities > Terminal
        3. 在 Terminal 中输入 csrutil disable，之后回车
        4. 重启 Mac
        5. 重启进入MAC之后再次csrutil status 
        6. 这时候系统会提示System Integrity Protection status: disabled.说明 SIP 功能已经被成功关闭




##### 查看是否安装成功
输入命令: ` $ scrapy ` 报错: ImportError: cannot import name xmlrpc_client
![](http://obr2ozlb6.bkt.clouddn.com/14761484635545.jpg)    

* 如果你已经关闭了苹果的 SIP ,可以使用命令删除系统内置的 six ,再次重新安装
```
$ sudo rm -rf /Library/Python/2.7/site-packages/six*
$ sudo rm -rf /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/six*
$ sudo pip install six
```

* 如果你没有关闭 SIP ,而是选择忽略系统内置的 six 方式安装 scrapy,请使用如下方式升级安装 six
`$ sudo easy_install --upgrade six`

* 再次查看 scrapy ,显示使用方法,安装成功
![](http://obr2ozlb6.bkt.clouddn.com/14761484288737.jpg)

 ##### 参考资料
    [Six issue when installing package](https://github.com/pypa/pip/issues/3165)
    [史上最完全Mac安装Scrapy指南](http://www.jianshu.com/p/a03aab073a35)
    [Homebrew macOS 不可或缺的套件管理器](http://brew.sh/index_zh-cn.html)
    [解决EI Capitan安装爬虫Scrapy问题](http://www.zeython.com/ei_capitan_scrapy.html)
    [ImportError: cannot import name xmlrpc_client](http://stackoverflow.com/search?q=ImportError%3A+cannot+import+name+xmlrpc_client)


