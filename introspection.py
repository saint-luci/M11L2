import inspect

def introspection_info(obj):
    dict = {}
    dict['type'] = type(obj)
    dict['attributes'] =[ x for x in dir(obj) if not callable(getattr(obj, x))]
    dict['methods'] = [x for x in dir(obj) if callable(getattr(obj, x))]
    dict['module'] = inspect.getmodule(obj)

    return dict

number_info = introspection_info(42)
print(number_info)