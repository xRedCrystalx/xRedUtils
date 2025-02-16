import sys, random
sys.dont_write_bytecode = True

import xRedUtils.cache as sync_cache
import xRedUtilsAsync.cache as async_cache


def sync_custom(_cmodule = None) -> None:
    CACHE = _cmodule or sync_cache

    iterations = 1000
    max_value = 100
    
    data: list[int] = [random.randint(0, max_value) for x in range(iterations)]

    # Limited
    limited_cache = CACHE.LimitedCache(max_capacity=20)
    for d in data:
        try:
            limited_cache.put(d, d)
        except MemoryError:
            if len(limited_cache) != 20:
                print("Error with LimitedCache, errored out before reaching max_capacity.")
            
            break

        except Exception as error:
            print(f"LimitedCache: {type(error).__name__}: {error}")
            break

    # Better limited
    better_limited_cache = CACHE.BetterLimitedCache(max_capacity=20)
    for d in data:
        try:
            better_limited_cache.put(d, d)
        except MemoryError:
            if len(better_limited_cache) not in (20, 50):
                print("Error with LimitedCache, errored out before reaching max_capacity.")
            
            if better_limited_cache.max_capacity == 20:
                better_limited_cache.change_size(50)
                continue

            break
        
        except Exception as error:
            print(f"BetterLimitedCache: {type(error).__name__}: {error}")
            break

    # LRU
    lru_cache = CACHE.LRUCache(max_capacity=20)
    for d in data:
        try:
            lru_cache.put(d, d)
        except Exception as error:
            print(f"LRUCache: {type(error).__name__}: {error}")
            break
    else:
        if len(lru_cache) != 20:
            print(f"Error with LRUCache, not reached max_capacity (20) after {iterations} iterations.\nRestart test, sometime randomness can fail.")


    # Better lru
    better_lru_cache = CACHE.BetterLRU(max_capacity=20)
    for d in data:
        try:
            better_lru_cache.put(d, d)

            if len(better_lru_cache) == 20:
                better_lru_cache.change_size(50)

        except Exception as error:
            print(f"LRUCache: {type(error).__name__}: {error}")
            break
    else:
        if len(better_lru_cache) <= 20:
            print(f"Error with BetterLRU, not higher than intial max_capacity (20) after {iterations} iterations.\nRestart test, sometime randomness can fail.")

    
    del limited_cache, better_limited_cache, lru_cache, better_lru_cache

async def async_custom() -> None:
    # caches are sync, passing to sync_custom
    sync_custom(async_cache)