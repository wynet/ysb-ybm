import execjs
import os

class jscode(object):
    def code(self):
        os.environ['NODE_OPTIONS'] = '--no-warnings --inspect=0'
        with open("./js/js.js", "r", encoding="utf-8") as f:
            js_code = f.read()
        ctx = execjs.compile(js_code)
        result = ctx.call("codes")
        return result


