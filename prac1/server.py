from wsgiref.simple_server import make_server
from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class Calculator(ServiceBase):

    @rpc(Integer, Integer, _returns=Integer)
    def add(self, a, b):
        return a + b

    @rpc(Integer, Integer, _returns=Integer)
    def subtract(self, a, b):
        return a - b

    @rpc(Integer, Integer, _returns=Integer)
    def multiply(self, a, b):
        return a * b

    @rpc(Integer, _returns=Integer)
    def square(self, a):
        return a * a

    @rpc(Integer, Integer, _returns=Unicode)
    def divide(self, a, b):
        return "Error" if b == 0 else str(a / b)


app = Application([Calculator],
                  'calculator.soap',
                  in_protocol=Soap11(),
                  out_protocol=Soap11())

server = make_server('127.0.0.1', 10000, WsgiApplication(app))

print("Server running at http://127.0.0.1:10000")
server.serve_forever()