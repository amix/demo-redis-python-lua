import os
import redis


#--- System specific ----------------------------------------------
REDIS_SYSTEMS = {}

def set_redis(system_name='default', redis_host='localhost',
              redis_port=6379, db=0, set_scripts=True, **kw):
    client = redis.Redis(host=redis_host,
                         port=redis_port,
                         db=db, **kw)

    if set_scripts:
        scripts = {
            'incr': client.register_script(_load_lua_script('incr.lua'))
        }
    else:
        scripts = {}

    REDIS_SYSTEMS[system_name] = (client, scripts)

def get_redis(system='default'):
    return REDIS_SYSTEMS.get(system)


#--- Incr functions ----------------------------------------------
def incr_lua(key, delta=1, system='default'):
    """
    Lua implementation of the incr command
    """
    client, scripts = get_redis(system)
    return scripts['incr'](keys=['key', 'delta'], args=[key, delta])

def incr_python(key, delta=1, system='default'):
    """
    Python implementation of the incr command
    """
    client, scripts = get_redis(system)

    with client.pipeline() as p:
        p.watch(key)
        value = delta
        old = p.get(key)
        if old:
            value = int(old) + delta
        p.set(key, value)
        p.unwatch()
        return value


#--- Misc ----------------------------------------------
def _load_lua_script(filename):
    fp = os.path.realpath(os.path.dirname(__file__))
    return open(os.path.join(fp, 'lua', filename)).read()
