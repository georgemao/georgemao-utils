from typing import List, Any, Iterable

def chunk_list(lst: List[Any], size: int) -> Iterable[List[Any]]:
    """
    Yield successive n-sized chunks from a list.
    """
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """
    Flatten a shallowly nested list.
    """
    return [item for sublist in nested_list for item in (sublist if isinstance(sublist, list) else [sublist])]
