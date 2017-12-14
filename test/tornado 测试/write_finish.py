
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):

    def prepare(self):

        self.write("1")
        self.finish("4")
        # return
        # print("hehe")
        # pass

    def get(self):
        # self.write("2")
        self.finish("3")
        return
        print("hehe")
        
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()