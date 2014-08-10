#! /usr/bin/env python
#coding=utf-8
# An example to use the setting file:

'''
Choose 1 to input an url, or enter 2 to open a html file:
'''
opt = '2'

'''
The url which is contained the images:
'''
url = ''

'''
The regular to match the images, such like: http://imgsrc\.aaa\.com/forum/w%.*?\.jpg
'''
reg = r'http://imgsrc\.baidu\.com/forum/w%.*?\.jpg'

'''
The path of the html file:
'''
file_dir = '/home/cjyfff/pachong_content/content_n.html'

'''
Sometime we are visiting a page that is showing the thumbnails, and we want to
download the real images which are relate to these thumbnails, then we need to
enter the prefix of the real url. For example, the thumbnails url is www.aaa.com/thumb/111.jpg',
the real image url is 'www.aaa.com/images/111.jpg', so we need to enter the prefix 'www.abc.com/images/',
this script will download the real image. If the images in the current page is not an thumbnails,
or you just want to download thumbnails, you just need to enter nothing.
'''
prefix = 'http://imgsrc.baidu.com/forum/pic/item/'

'''
The path you want to save the images, enter nothing to save in the current path:
'''
save_dir = '/home/cjyfff/pachong_content/n/'

'''
The name you want to named the images.
If you enter 'football', the images will be save as 'football1.jpg', 'football2.jpg'...etc.
Enter nothing to save images with the origin name specified in the url.
'''
spec_name = ''
