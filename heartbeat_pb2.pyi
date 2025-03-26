from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HeartbeatRequest(_message.Message):
    __slots__ = ("server_id",)
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    def __init__(self, server_id: _Optional[str] = ...) -> None: ...

class HeartbeatResponse(_message.Message):
    __slots__ = ("received",)
    RECEIVED_FIELD_NUMBER: _ClassVar[int]
    received: bool
    def __init__(self, received: bool = ...) -> None: ...

class SwitchRequest(_message.Message):
    __slots__ = ("new_primary",)
    NEW_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    new_primary: str
    def __init__(self, new_primary: _Optional[str] = ...) -> None: ...

class SwitchResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
