---
title: 使用 Github Pages 和 Hexo 搭建个人博客
date: 2014-07-27 09:34:47
tags:
---


参考了许多网上的教程,终于搭建出属于自己的个人博客,在此记录下遇到的一些问题及流程

##### 缠绕的问题
	1. 需不需要建立 github-pages 分支,答案是 不需要
	2. 在完成所有的操作后需要手动git push到主分支吗,结果是根本不需要将  
	github上的仓库clone到本地,在本地任意文件夹下配置好deploy参数之后,只  
	需执行hexo g -d 可自动commit,push到github上(后面会提到一个站点配置文件)
##### 搭建流程
* 在 [github](https://github.com) 的操作
	* 注册账号并创建一个名称为 username.github.io 的仓库,此处的username为你注册账号的用户名, [参考地址](https://pages.github.com/)
	* 通过 SSH Key 与本地建立 git 链接 [Generating an SSH key](https://help.github.com/articles/generating-an-ssh-key/)
	* [git的学习资料](https://github.com/xirong/my-git)
	
* 本地电脑端的操作
	* 安装 HEXO 参考 [hexo文档](https://hexo.io/zh-cn/docs/index.html) 依次按顺序来完成即可完成建站, [Node.js](http://nodejs.org) 和 [git](https://git-scm.com) ,再使用终端命令安装 hexo <br>
	` $ npm install -g hexo-cli `
	* 在本地任意新建一个博客目录在此举例名为Blog,在终端 cd 到 Blog 目录执行如下命令<br> 
	``` 
		$ hexo init
		$ npm install
		$ hexo g # 或者hexo generate 
		$ hexo s # 或者hexo server，可以在http://localhost:4000/ 查看
	```

	* 博客架构有了,还需要搭配一个漂亮主题,在此我是用的是NEXT主题,可以到 [HEXO Themes](https://hexo.io/themes/) 查看使用你自己喜欢的主题
	* 在命令行Blog目录下clone主题到themes目录下<br>
	` git clone https://github.com/iissnan/hexo-theme-next.git themes/NEXT`
	* Blog目录下有一个站点配置文件 **_config.yml**, 打开此文件,更改theme字段为 **theme: NEXT**,
	* 将Blog部署到github上
		* `npm install hexo-deployer-git --save` 安装git依赖
		* 在配置文件_config.xml中作如下修改：<br>
		```
		   deploy:
  		  	type: git
  		  	repo: git@github.com:usename/username.github.io.git  
  		  	branch: master  			
  		```
  		* 命令行执行 hexo g -d 即可发布到github上
	
* 自定义博客功能如多说评论,搜索,站长统计,修改外观等,直接参考 [NEXT主题使用文档](http://theme-next.iissnan.com) ,应有尽有

* hexo n "文章名" 即可在Blog/source/_post/文件夹下 创建 文章名.md 文件, hexo 支持 [markdown语法](https://github.com/riku/Markdown-Syntax-CN/blob/master/syntax.md#img)
* hexo g -d 即可发布文章
* 域名转换可参考 [如何搭建一个独立博客——简明 Github Pages与 jekyll 教程](http://cnfeat.com/blog/2014/05/10/how-to-build-a-blog/)
* 使用 github pages 和 gitcafe 实现分流 [Github Pages 服务太慢？来试试分流吧!](http://yumemor.com/Github-Pages-服务太慢？来试试分流吧/)
##### 建站参考资料
[从 Octopress 迁移到 Hexo](http://blog.devtang.com/2016/02/16/from-octopress-to-hexo/)<br>
[如何搭建一个独立博客——简明Github Pages与Hexo教程](http://www.jianshu.com/p/05289a4bc8b2)<br>
[如何在一天之内搭建以你自己名字为域名的很cool的个人博客](https://wingjay.com/2015/12/07/如何在一天之内搭建以你自己名字为域名的很cool的个人博客/)<br>
[手把手教你使用Hexo + Github Pages搭建个人独立博客](http://jiji262.github.io/2016/04/15/2016-04-15-hexo-github-pages-blog/)<br>
[使用 Github Pages + Hexo + 多说 搭建博客全过程 - 基础篇](http://kiya.space/2015/11/10/use-Github-Pages-Hexo-duoshuo-to-set-up-a-blog-basic-steps/)<br>