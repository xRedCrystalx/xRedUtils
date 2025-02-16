import sys, typing
sys.dont_write_bytecode = True
import xRedUtils.modules as sync_modules
import xRedUtilsAsync.modules as async_modules


def sync_custom() -> None:
    import xRedUtils.cache as cache_module

    result: list[type] = sync_modules.get_types_of_module(cache_module)
    if len(result) != 5:
        print(f"modules.get_types_of_module returned {len(result)}, expected 5.")


async def async_custom() -> None:
    import xRedUtilsAsync.cache as cache_module

    result: list[type] = await async_modules.get_types_of_module(cache_module)
    if len(result) != 5:
        print(f"modules.get_types_of_module returned {len(result)}, expected 5.")
