import functools
from typing import Any

from pydantic import BaseModel, TypeAdapter


class A(BaseModel):
    a: int


class B(BaseModel):
    b: str


class C(BaseModel):
    c: str


@functools.singledispatch
def event_handler(event: Any) -> None:
    print("Unknown event")


@event_handler.register
def handle_a(event: A) -> None:
    print("A", event.a)


@event_handler.register
def handle_b(event: B) -> None:
    print("B", event.b)


payload = {"c": "12"}

supported_model = A | B | C
adapter: TypeAdapter = TypeAdapter(supported_model)
event = adapter.validate_python(payload)

event_handler(event)

match event:
    case A(a=_ as value):
        print(value)
    case B():
        print("B")
    case _:
        print("else")
