#!/usr/bin/env python
#-*- coding=utf-8 -*-
# codeby @nightwish

import web
import time

from wechat import wechatmsg

urls  = ('/',wechatmsg)

if __name__ == "__main__":
    # web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app = web.application(urls, globals())
    time.sleep(0.01)
    app.run()
