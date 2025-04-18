# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import chat_pb2 as chat__pb2
import heartbeat_pb2 as heartbeat__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in proxy_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ProxyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Join = channel.unary_unary(
                '/chat.ProxyService/Join',
                request_serializer=chat__pb2.JoinRequest.SerializeToString,
                response_deserializer=chat__pb2.JoinResponse.FromString,
                _registered_method=True)
        self.SendMessage = channel.unary_unary(
                '/chat.ProxyService/SendMessage',
                request_serializer=chat__pb2.Message.SerializeToString,
                response_deserializer=chat__pb2.Empty.FromString,
                _registered_method=True)
        self.ReceiveMessages = channel.unary_stream(
                '/chat.ProxyService/ReceiveMessages',
                request_serializer=chat__pb2.Empty.SerializeToString,
                response_deserializer=chat__pb2.Message.FromString,
                _registered_method=True)
        self.SwitchServer = channel.unary_unary(
                '/chat.ProxyService/SwitchServer',
                request_serializer=heartbeat__pb2.SwitchRequest.SerializeToString,
                response_deserializer=heartbeat__pb2.SwitchResponse.FromString,
                _registered_method=True)


class ProxyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Join(self, request, context):
        """Client joins the chatroom
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessage(self, request, context):
        """Client sends a message to the server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveMessages(self, request, context):
        """Client receives chat messages as a stream
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SwitchServer(self, request, context):
        """Proxy receives switch server request from the heartbeat service
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProxyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Join': grpc.unary_unary_rpc_method_handler(
                    servicer.Join,
                    request_deserializer=chat__pb2.JoinRequest.FromString,
                    response_serializer=chat__pb2.JoinResponse.SerializeToString,
            ),
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=chat__pb2.Message.FromString,
                    response_serializer=chat__pb2.Empty.SerializeToString,
            ),
            'ReceiveMessages': grpc.unary_stream_rpc_method_handler(
                    servicer.ReceiveMessages,
                    request_deserializer=chat__pb2.Empty.FromString,
                    response_serializer=chat__pb2.Message.SerializeToString,
            ),
            'SwitchServer': grpc.unary_unary_rpc_method_handler(
                    servicer.SwitchServer,
                    request_deserializer=heartbeat__pb2.SwitchRequest.FromString,
                    response_serializer=heartbeat__pb2.SwitchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'chat.ProxyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('chat.ProxyService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ProxyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Join(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/chat.ProxyService/Join',
            chat__pb2.JoinRequest.SerializeToString,
            chat__pb2.JoinResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/chat.ProxyService/SendMessage',
            chat__pb2.Message.SerializeToString,
            chat__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReceiveMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/chat.ProxyService/ReceiveMessages',
            chat__pb2.Empty.SerializeToString,
            chat__pb2.Message.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SwitchServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/chat.ProxyService/SwitchServer',
            heartbeat__pb2.SwitchRequest.SerializeToString,
            heartbeat__pb2.SwitchResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
