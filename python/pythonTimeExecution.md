# Decorator

```python
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.22f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed

@timeit
def foo():
    do_some_work()
```

# Terminal

> python -m cProfile nameOfPythonCode.py

```Python
204 function calls in 0.000 seconds

Ordered by: standard name

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1    0.000    0.000    0.000    0.000 1313-decompress-run-length-encoded-list.py:2(<module>)
1    0.000    0.000    0.000    0.000 {len}
1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
200  0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
1    0.000    0.000    0.000    0.000 {range}
```
