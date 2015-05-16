##基于PhantomJS图片爬虫工具：ImgGetter   
   
####2015.05.17更新：    
版本号：v0.5.0   
功能修改，获取图片url地址的逻辑改为由PhantomJS实现，图片的下载仍然由python实现。   
   
####2014.08.10更新：
版本号：v0.1.0   
初始v0.1版本，实现基础功能   
   
###依赖：   
* python      2.7   
* docopt      0.6.2   
* phantomjs   2.0.1   
     
###使用说明：   

* 确保合PhantomJS已经安装，并且已经把合PhantomJS的bin目录添加到环境变量。   
* 把PhantomJS的脚本放到pjs目录中   
* 程序的输入参数定义：    

   ImgGetter.py <PhantomJS_script> [-o=<output path>] [-j=<number of threads>]    
其中<PhantomJS_script>是必要参数，代表待执行的PhantomJS脚本名称。-o和-j是可选参数，-o可以指定图片保存的目录（需使用绝对路径），-j可以指定下载图片所使用的线程数。   
   
