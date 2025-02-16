import sys
sys.dont_write_bytecode = True
import xRedUtils.regexes as sync_regexes
import xRedUtilsAsync.regexes as async_regexes


def sync_custom(_rmodule = None) -> None:
    REGEXES = _rmodule or sync_regexes
    
    if (found := REGEXES.ANSI_PATTERN.findall("\x1b[38;5;16mHi, this is test\x1b[0m")) != ["\x1b[38;5;16m", "\x1b[0m"]:
        print("regexes.ANSI_PATTERN failed to find all patterns. Found:", found)

    if (found := REGEXES.DATE_PATTERN.findall("Test 2005-12-05")) != ["2005-12-05"]:
        print("regexes.DATE_PATTERN failed to find all patterns Found:", found)
    
    if (found := REGEXES.IPv4_PATTERN.findall("Test 192.168.0.1 then 127.0.0.1")) != ["192.168.0.1", "127.0.0.1"]:
        print("regexes.IPv4_PATTERN failed to find all patterns Found:", found)

    if (found := REGEXES.IPv6_PATTERN.findall("some random ip is 2001:0db8:85a3:0000:0000:8a2e:0370:7334 lol")) != ["2001:0db8:85a3:0000:0000:8a2e:0370:7334"]:
        print("regexes.IPv6_PATTERN failed to find all patterns Found:", found)

    if (found := REGEXES.MAC_ADDR_PATTERN.findall("MAC 01:23:45:67:89:AB, also 01-23-45-67-89-AB")) != ["01:23:45:67:89:AB", "01-23-45-67-89-AB"]:
        print("regexes.MAC_ADDR_PATTERN failed to find all patterns Found:", found)

    if (found := REGEXES.URL_PATTERN.findall("lets go to https://google.com also youtube link https://www.youtube.com/watch?v=dQw4w9WgXcQ")) != ["https://google.com", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"]:
        print("regexes.URL_PATTERN failed to find all patterns Found:", found)


async def async_custom() -> None:
    # regexes are sync, passing to sync_custom
    sync_custom(async_regexes)
