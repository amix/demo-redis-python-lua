## How to use Redis+Lua from Python

This is a small demo that showcases how to use Redis and Lua from Python to increase performance at least 3x.

This is a recommend optimization strategy when you create custom data structures on top of Redis.


### Benchmark of a simple incr command
I've re-implemented `incr` in Python and in Python+Lua. Below you can see a benchmark of 300.000 incr commands. The Lua version performs about 3 times better. Both versions support nice things like atomicity. 


### Incr implemented in Python (~37.7 sec execution) 
```bash
time python test_incr_python.py 300000
python test_incr_python.py 300000  37.77s user 12.00s system 73% cpu 1:07.73 total
```


### Incr implemented in Lua (~10.7 sec execution) 
```bash
time python test_incr_lua.py 300000
python test_incr_lua.py 300000  10.76s user 2.85s system 66% cpu 20.513 total
```
