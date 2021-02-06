import time
from grpc._channel import _Rendezvous, _UnaryUnaryMultiCallable, _UnaryStreamMultiCallable, _InactiveRpcError

MAX_RETRIES = 5

def retry_stub(method):
    def inner(*args, **kwargs):
        retry_attempt = 0
        while True:
            try:
                future_response = method.future(*args, **kwargs)
                return future_response.result()
            except (_Rendezvous, _InactiveRpcError) as excp:
                error_code = excp.code()
                if retry_attempt > MAX_RETRIES:
                    raise
                backoff_time = 1.0
                print("Request Failed with :{} \n(retrying after : {})".format(error_code, backoff_time))
                retry_attempt += 1
                time.sleep(backoff_time)
    return inner

def create_retry_stub(stub_obj):
    for rpc_key, rpc_obj in stub_obj.__dict__.items():
        if isinstance(rpc_obj, _UnaryUnaryMultiCallable):
            setattr(stub_obj, rpc_key, retry_stub(rpc_obj))
