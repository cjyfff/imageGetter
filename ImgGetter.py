#! /usr/bin/env python
# author: cjyfff -- https://github.com/cjyfff
"""ImgGetter is a crawler to get images with PhantomJS.
Usage:
    ImgGetter.py <PhantomJS_script> [-o=<output path>] [-j=<number of threads>]

Examples:
    ImgGetter.py love_live.js
    ImgGetter.py love_live.js --output /home/cjyfff/img/
    ImgGetter.py love_live.js --output /home/cjyfff/img/ -j 5

Options:
    -h --help     Show this screen.
    --version     Show version.
    -o            Assign output path(use absolute path).
    -j            Assign number of threads.
"""

import urllib
import sys
import threading
import os
import settings
from docopt import docopt

VERSION = 'ImgGetter 0.5.0'
count = 0


class ErrorHandler(object):

    @staticmethod
    def access_error(msg='Access error!'):
        print msg
        sys.exit(1)

    @staticmethod
    def user_abort(msg='User abort!'):
        print msg
        sys.exit(0)

    @staticmethod
    def undefined_error(msg='Some error has happened!'):
        print msg
        sys.exit(1)


def get_picture_list(path):
    assert isinstance(path, str)

    def is_img(url):
        postfix = url.split('.')[-1].strip()
        if postfix not in settings.IMG_TYPES:
            return False
        return True

    def get_img_name(url):
        # TODO: add spec name
        return url.split('/')[-1].strip()

    pic_url_list = []
    try:
        with open(path, 'r') as f:
            for url in f:
                if not is_img(url):
                    continue
                name = get_img_name(url)
                pic_url_list.append({'name': name, 'url': url})
    except IOError:
        ErrorHandler.access_error('Can not read the output file!')
    return pic_url_list


def save_thread(pic_url_list, save_dir):
    assert isinstance(pic_url_list, list)
    assert isinstance(save_dir, str)

    def print_counting():
        global count
        if count != 0 and count % 10 == 0:
            print "%d pictures saved" % count
        count += 1

    for item in pic_url_list:
        try:
            urllib.urlretrieve(item['url'], save_dir + item['name'].strip())
            print_counting()
        except IOError:
            ErrorHandler.access_error(
                'You have no permission to save files in the specified path.')
        except KeyboardInterrupt:
            ErrorHandler.user_abort('Download abort, existing...')


def save_picture(pic_url_list, save_dir, jobs):
    assert isinstance(pic_url_list, list)
    assert isinstance(save_dir, str)
    assert isinstance(jobs, int) and not isinstance(jobs, bool)

    border = len(pic_url_list) / (jobs - 1)
    threads = []
    i = 0
    j = border
    while i < len(pic_url_list):
        t = threading.Thread(target=save_thread,
                             args=(pic_url_list[i: j], save_dir))
        threads.append(t)
        i = j
        j += border

    for t in threads:
        t.start()
    for t in threads:
        t.join()


def normalize(path):
    assert isinstance(path, str)
    if not path.startswith('/'):
        path = '/' + path
    if not path.endswith('/'):
        path = path + '/'
    return path


def main(output, jobs):
    global count
    assert isinstance(output, str)
    assert isinstance(jobs, int) and not isinstance(jobs, bool)

    path = os.getcwd() + '/temp/url_temp'
    pic_url_list = get_picture_list(path)
    save_picture(pic_url_list, output, jobs)
    print "Completed! Total %d images" % count


if __name__ == '__main__':
    arguments = docopt(__doc__, version=VERSION)
    _p_script = arguments['<PhantomJS_script>']
    output = arguments['-o']
    jobs = arguments['-j']

    p_script = os.getcwd() + settings.PhantomJS_PATH + _p_script

    if output:
        output = normalize(output)
    else:
        output = os.getcwd() + settings.DEFAULT_OUTPUT_PATH

    if not jobs:
        jobs = settings.DEFAULT_THREADING_NUM

    temp_file = os.getcwd() + settings.TEMP_FILE

    try:
        print "Begin to run PhantomJS script..."
        os.system('phantomjs {script} > {temp_file}'.format(script=p_script, temp_file=temp_file))
        print "PhantomJS script completed!"
        main(output, jobs)
    except KeyboardInterrupt:
        ErrorHandler.user_abort('Bye')
    except Exception, e:
        ErrorHandler.undefined_error(str(e))
