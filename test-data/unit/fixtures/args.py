# Builtins stub used to support *args, **kwargs.

from typing import TypeVar, Generic, Iterable, Tuple, Dict, Any, overload

Tco = TypeVar('Tco', covariant=True)
T = TypeVar('T')
S = TypeVar('S')

class object:
    def __init__(self) -> None: pass

class type:
    @overload
    def __init__(self, o: object) -> None: pass
    @overload
    def __init__(self, name: str, bases: Tuple[type, ...], dict: Dict[str, Any]) -> None: pass

class tuple(Iterable[Tco], Generic[Tco]): pass
class dict(Generic[T, S]): pass

class int: pass
class str: pass
class bool: pass
class function: pass
