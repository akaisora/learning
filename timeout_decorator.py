import stopit
import time

@stopit.threading_timeoutable(default="not finished")
def sleep_30seconds():
    #for i in range(30):
    time.sleep(30)
    return "bahar"
	
	
def timeout(seconds):
def outer(function):
    @functools.wraps(function)
    def inner(*args, **kwargs):
        result = None
        with stopit.ThreadingTimeout(seconds) as to_ctx_mgr:
            assert to_ctx_mgr.state == to_ctx_mgr.EXECUTING
            result = sleep_30seconds()
        if to_ctx_mgr.state == to_ctx_mgr.TIMED_OUT:
            print("timed out")
        return result
    return inner
return outer
	
	
@timeout(5)
def print_my_name():
	print("bahar oezkan")