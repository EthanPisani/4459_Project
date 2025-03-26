from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class JoinRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class JoinResponse(_message.Message):
    __slots__ = ("welcome_message",)
    WELCOME_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    welcome_message: str
    def __init__(self, welcome_message: _Optional[str] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("sender", "content")
    SENDER_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    sender: str
    content: str
    def __init__(self, sender: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
