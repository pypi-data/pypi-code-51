
import simlib.flags as flags
import functools


__all__ = [
    'experimental'
]


# Decorator to indicate if still in development
# TODO this should probably be moved out of __init__
def experimental(f=None):
    # Wrapper to run function
    def execute_function(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            use_experimental = flags.use_experimental
            # if 'use_experimental' in kwargs:
            #     use_experimental = kwargs['use_experimental']
            #     del kwargs['use_experimental']

            # If false, then we cannot use this function
            if not use_experimental:
                raise PermissionError('cannot use function because it is experimental')

            return f(*args, **kwargs)
        return wrapper

    if f is None:
        return execute_function
    else:
        return execute_function(f)
