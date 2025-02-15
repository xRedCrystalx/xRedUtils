"""
This module provides classes/objects made for memory cache.
## NOTE: Cache methods are not async.

### Objects:
- `Cache` - Same as `dict` just renamed for better typing.
- `LimitedCache` - Classic limited cache, cannot exceed `max_capacity`.
- `BetterLimitedCache` - Better limited cache, can manipulate with `max_capacity` in the runtime.
- `LRUCache` - Classic LRU cache.
- `BetterLRU` - Better LRU cache, can manipulate with `max_capacity` in the runtime.

### Usage:
```py
import xRedUtilsAsync.cache as cache
or
from xRedUtilsAsync import cache
```
"""

import sys
sys.dont_write_bytecode = True
from collections import OrderedDict

from .annotations import K, V, Iterator

__all__: tuple[str, ...] = (
    "Cache", "LimitedCache", "BetterLimitedCache", "LRUCache", "BetterLRU"
)

class Cache(dict[K, V]):
    """Same as `dict` just renamed for better typing."""


class LimitedCache(Cache[K, V]):
    def __init__(self, max_capacity: int) -> None:
        """Classic limited cache, cannot exceed `max_capacity`."""
        super().__init__()
        self._max_capacity: int = max_capacity

    @property
    def max_capacity(self) -> int:
        return self._max_capacity
    
    @max_capacity.setter
    def max_capacity(self, size: int) -> RuntimeError:
        raise RuntimeError("You cannot change `max_capacity`. Use `BetterLimitedCache`.")
    
    def put(self, key: K, value: V) -> None:
        """
        Adds a new key-value pair, returns error if `max_capacity` is reached.
        """
        if len(self) == self._max_capacity:
            raise MemoryError(f"Max capacty reached! Limit: {self._max_capacity}")
        else:
            super().__setitem__(key, value)

    def __setitem__(self, key: K, value: V) -> None:
        """Overrides standard dictionary assignment to ensure LimitedCache behavior."""
        return self.put(key, value)

class BetterLimitedCache(LimitedCache[K, V]):
    def __init__(self, max_capacity: int) -> None:
        """Better limited cache, can manipulate with `max_capacity` in the runtime."""
        super().__init__(max_capacity)

    @property
    def max_capacity(self) -> int:
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, size: int) -> None:
        return self.change_size(int(size))
    
    def change_size(self, new_max_capacity: int) -> None:
        """
        Adjusts cache size. If shrinking, evicts first items.
        ### WARNING: shrinking can lead to data loss! Use with your own risk.
        """
        self._max_capacity = new_max_capacity
        
        # using iter for faster and more optimized removal
        keys: Iterator[K] = iter(self)
        while len(self) > new_max_capacity:
            self.pop(next(keys))


class LRUCache(OrderedDict[K, V]):
    def __init__(self, max_capacity: int) -> None:
        """Classic LRU cache."""    
        super().__init__()
        self._max_capacity: int = max_capacity

    @property
    def max_capacity(self) -> int:
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, size: int) -> RuntimeError:
        raise RuntimeError("You cannot change `max_size`. Use `BetterLRUCache`.")

    def touch(self, key: K, default: V | None = None) -> V | None:
        """Gets value without updating cache order."""
        return super().get(key, default)

    def get(self, key: K, default: V | None = None) -> V | None:
        """Retrieves a value and moves it to the top (most recently used)."""
        if key in self:
            self.move_to_end(key, last=True)
            return super().get(key)
        
        return default

    def put(self, key: K, value: V) -> None:
        """
        Adds a new key-value pair, moves it to the top, 
        and removes the least recently used item if `max_capacity` is exceeded.
        """
        if key in self:
            self.move_to_end(key, last=True)

        self
        super().__setitem__(key, value)

        if len(self) > self._max_capacity:
            self.popitem(last=False)

    def __setitem__(self, key: K, value: V) -> None:
        """Overrides standard dictionary assignment to ensure LRU behavior."""
        return self.put(key, value)

    def __getitem__(self, key: K) -> V:
        """Overrides standard dictionary retrieval to maintain LRU order."""
        return self.get(key)

class BetterLRU(LRUCache[K, V]):
    def __init__(self, max_capacity: int) -> None:
        """Better LRU cache, can manipulate with `max_capacity` in the runtime."""    
        super().__init__(max_capacity)

    @property
    def max_capacity(self) -> int:
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, size: int) -> None:
        return self.change_size(int(size))
    
    def change_size(self, new_max_capacity: int) -> None:
        """
        Adjusts cache size. If shrinking, evicts the oldest items.
        ### WARNING: shrinking can lead to data loss! Use with your own risk.
        """
        self._max_capacity = new_max_capacity

        while len(self) > new_max_capacity:
            self.popitem(last=False)
