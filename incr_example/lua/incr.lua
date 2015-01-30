local delta = tonumber(ARGV[2])
local value = delta
local old = tonumber(redis.call('get', ARGV[1]))
if old then
    value = value + old
end
if not redis.call('set', ARGV[1], value) then
    return nil
end
return value
