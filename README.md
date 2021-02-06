# Retry Stub

Usage:

Taken example of the greeter_client.py

```py
# import the module
from retry_grpc import create_retry_stub

def run():
    with grpc.insecure_channel('localhost:50000') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        # this decorates the stub with retry_stub
        create_retry_stub(stub)

        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
        print("Greeter client received: "+ response.message)

if __name__ == '__main__':
    run()
```
