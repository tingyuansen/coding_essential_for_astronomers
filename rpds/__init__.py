"""Fallback implementations of rpds persistent containers.

These mimic the subset of the rpds API used by the `referencing` package so
that nbformat/jsonschema can run in environments where the compiled rpds
extension is unavailable (e.g. architecture mismatches). The real rpds types
are immutable and persistent; these Python implementations instead return new
container instances backed by standard built-in types, which is sufficient for
our static site build script.
"""
from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any, Iterator, Tuple, TypeVar

K = TypeVar("K")
V = TypeVar("V")
T = TypeVar("T")


class HashTrieMap(dict[K, V]):
    """Simplified drop-in replacement for rpds.HashTrieMap."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__()
        if args or kwargs:
            dict.update(self, dict(*args, **kwargs))

    @classmethod
    def convert(cls, value: Mapping[K, V] | Iterable[Tuple[K, V]]) -> "HashTrieMap[K, V]":
        if isinstance(value, cls):
            return value
        return cls(value)

    def insert(self, key: K, value: V) -> "HashTrieMap[K, V]":
        new = HashTrieMap(self)
        dict.__setitem__(new, key, value)
        return new

    def remove(self, key: K) -> "HashTrieMap[K, V]":
        new = HashTrieMap(self)
        del new[key]
        return new

    def update(self, other: Mapping[K, V] | Iterable[Tuple[K, V]]) -> "HashTrieMap[K, V]":  # type: ignore[override]
        new = HashTrieMap(self)
        dict.update(new, dict(other))
        return new


class HashTrieSet(set[T]):
    """Simplified drop-in replacement for rpds.HashTrieSet."""

    def insert(self, value: T) -> "HashTrieSet[T]":
        new = HashTrieSet(self)
        set.add(new, value)
        return new

    def discard(self, value: T) -> "HashTrieSet[T]":  # type: ignore[override]
        new = HashTrieSet(self)
        set.discard(new, value)
        return new

    def update(self, other: Iterable[T]) -> "HashTrieSet[T]":  # type: ignore[override]
        new = HashTrieSet(self)
        set.update(new, other)
        return new


class List(tuple[T, ...]):
    """Simplified drop-in replacement for rpds.List."""

    def __new__(cls, iterable: Iterable[T] | None = None) -> "List[T]":
        if iterable is None:
            iterable = ()
        return super().__new__(cls, tuple(iterable))

    def push_front(self, value: T) -> "List[T]":
        return List((value, *self))

    def __iter__(self) -> Iterator[T]:  # type: ignore[override]
        return tuple.__iter__(self)
