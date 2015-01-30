import sys
import incr_example

if __name__ == '__main__':
    incr_example.set_redis(redis_host='localhost',
                           redis_port=6380,
                           set_scripts=True)

    incr_example.get_redis()[0].delete('test')

    for i in xrange(0, int(sys.argv[1])):
        incr_example.incr_lua('test')
