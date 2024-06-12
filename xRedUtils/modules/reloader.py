import sys, importlib.util, types
sys.dont_write_bytecode = True

__all__ = (
    "load_module", "unload_module", "reload_module"
)

def resolve_name(name: str, package: str = None) -> str:
    return importlib.util.resolve_name(name, package)

def load_module(name: str, package: str = None) -> types.ModuleType:
    return importlib.import_module(name, package)

def unload_module(name: str, package: str = None) -> str | None:
    """
    Removes cached module (sys.modules) from the current running instance.
    
    ## WARNING: Removing a module dynamically can result to errors, crashes etc. if not used properly. USE WITH YOUR OWN RISK!
    
    ### Parameters:
    - `name` - Python like path of the module. (using `.` as seperators)
    - `package` - 

    ### Returns:
    - Python path, if sucessful else `None`

    """
    path: str = resolve_name(name, package)
    if path in sys.modules:
        try:
            del sys.modules[path]
            return path
        except: pass

def reload_module(name: str, package: str = None, ignore_not_loaded: bool = False) -> types.ModuleType | None:
    # removing cached module from system
    if not unload_module(name, package) and not ignore_not_loaded:
        raise ImportWarning("Module not loaded. Use `ignore_not_loaded = True` to bypass this warning or load the module using `load_module`")

    return load_module(name, package)


"""


def levenshtein_distance(string1: str, string2: str) -> int:    
    
    # switch (first argument must be longer than second)
    if len(string1) < len(string2):
        return levenshtein_distance(string2, string1)

    # if second string is empty, means len(string1) instertions
    if len(string2) == 0:
        return len(string1)

    previous_row: list[int] = range(len(string2) + 1)
    
    for index1, char1 in enumerate(string1):
        current_row: list[int] = [index1+1]

        for index2, char2 in enumerate(string2):
            insertions: int = previous_row[index2+1] + 1
            deletions: int = current_row[index2] + 1
            substitutions: int = previous_row[index2] + (char1 != char2)
            current_row.append(min(insertions, deletions, substitutions))
    
        previous_row: list[int] = current_row
    
    return previous_row[-1]


def similarity_percentage(s1: str, s2: str) -> float:
    max_len = max(len(s1), len(s2))
    if max_len == 0:
        return 100.0  # Both strings are empty, hence 100% similar
    distance = levenshtein_distance(s1, s2)
    print(distance)

    similarity = ((max_len - distance) / max_len) * 100
    return similarity

# Example usage
if __name__ == "__main__":
    s1 = "Free 18+ Teen Porn + Latina Nudes + Onlyfans Leaks + Hot Girls + Hot pussys +E-Girls Porn + Hentai Porn  🍑🔞@everyone "
    s2 = "@everyone 🔞 Free 18+ Teen Porn, Onlyfans Leaks, Hot Girls, E-Girls Porn and Hentai Porn 🍑"
    similarity = similarity_percentage(s1, s2)
    print(f"Similarity between\n'{s1}' and\n'{s2}'\nis {similarity:.2f}%")
"""