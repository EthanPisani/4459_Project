# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

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
        + f' but the generated code in heartbeat_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class HeartbeatStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendHeartbeat = channel.unary_unary(
                '/chat.Heartbeat/SendHeartbeat',
                request_serializer=heartbeat__pb2.HeartbeatRequest.SerializeToString,
                response_deserializer=heartbeat__pb2.HeartbeatResponse.FromString,
                _registered_method=True)
        self.SwitchServer = channel.unary_unary(
                '/chat.Heartbeat/SwitchServer',
                request_serializer=heartbeat__pb2.SwitchRequest.SerializeToString,
                response_deserializer=heartbeat__pb2.SwitchResponse.FromString,
                _registered_method=True)


class HeartbeatServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendHeartbeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SwitchServer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HeartbeatServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendHeartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.SendHeartbeat,
                    request_deserializer=heartbeat__pb2.HeartbeatRequest.FromString,
                    response_serializer=heartbeat__pb2.HeartbeatResponse.SerializeToString,
            ),
            'SwitchServer': grpc.unary_unary_rpc_method_handler(
                    servicer.SwitchServer,
                    request_deserializer=heartbeat__pb2.SwitchRequest.FromString,
                    response_serializer=heartbeat__pb2.SwitchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'chat.Heartbeat', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('chat.Heartbeat', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Heartbeat(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendHeartbeat(request,
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
            '/chat.Heartbeat/SendHeartbeat',
            heartbeat__pb2.HeartbeatRequest.SerializeToString,
            heartbeat__pb2.HeartbeatResponse.FromString,
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
            '/chat.Heartbeat/SwitchServer',
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
