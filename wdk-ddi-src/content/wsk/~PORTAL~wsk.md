# Wsk.h header


This header is used by unknown technology.

Wsk.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [WskCaptureProviderNPI function](nf-wsk-wskcaptureprovidernpi.md) | The WskCaptureProviderNPI function captures a provider Network Programming Interface (NPI) when it becomes available from the WSK subsystem. |
| [WskDeregister function](nf-wsk-wskderegister.md) | The WskDeregister function unregisters a WSK application's registration instance that was previously created by WskRegister. |
| [WskQueryProviderCharacteristics function](nf-wsk-wskqueryprovidercharacteristics.md) | The WskQueryProviderCharacteristics function queries the range of WSK NPI versions supported by the WSK subsystem. |
| [WskRegister function](nf-wsk-wskregister.md) | The WskRegister function registers a WSK application, given the application's WSK client Network Programming Interface (NPI). |
| [WskReleaseProviderNPI function](nf-wsk-wskreleaseprovidernpi.md) | The WskReleaseProviderNPI function releases a Network Programming Interface (NPI) that was captured with WskCaptureProviderNPI. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PFN_WSK_ABORT_EVENT callback](nc-wsk-pfn-wsk-abort-event.md) | The WskAbortEvent event callback function notifies a WSK application that an incoming connection request on a listening socket that has conditional accept mode enabled has been dropped. |
| [PFN_WSK_ACCEPT callback](nc-wsk-pfn-wsk-accept.md) | The WskAccept function accepts an incoming connection on a listening socket. |
| [PFN_WSK_ACCEPT_EVENT callback](nc-wsk-pfn-wsk-accept-event.md) | The WskAcceptEvent event callback function notifies a WSK application that an incoming connection on a listening socket has been accepted. |
| [PFN_WSK_BIND callback](nc-wsk-pfn-wsk-bind.md) | The WskBind function binds a socket to a local transport address. |
| [PFN_WSK_CLIENT_EVENT callback](nc-wsk-pfn-wsk-client-event.md) | The WskClientEvent event callback function notifies a WSK application about events that are not specific to a particular socket. |
| [PFN_WSK_CLOSE_SOCKET callback](nc-wsk-pfn-wsk-close-socket.md) | The WskCloseSocket function closes a socket and frees any associated resources. |
| [PFN_WSK_CONNECT callback](nc-wsk-pfn-wsk-connect.md) | The WskConnect function connects a connection-oriented or stream socket to a remote transport address. |
| [PFN_WSK_CONNECT_EX callback](nc-wsk-pfn-wsk-connect-ex.md) | The WskConnectEx function connects a connection-oriented or stream socket to a remote transport address.WskConnectEx is similar to WskConnect except that it can also optionally send a buffer of data during or after connection synchronization. |
| [PFN_WSK_CONTROL_CLIENT callback](nc-wsk-pfn-wsk-control-client.md) | The WskControlClient function performs control operations on a WSK client object. |
| [PFN_WSK_CONTROL_SOCKET callback](nc-wsk-pfn-wsk-control-socket.md) | The WskControlSocket function performs control operations on a socket. |
| [PFN_WSK_DISCONNECT callback](nc-wsk-pfn-wsk-disconnect.md) | The WskDisconnect function disconnects a connection-oriented or stream socket from a remote transport address. |
| [PFN_WSK_DISCONNECT_EVENT callback](nc-wsk-pfn-wsk-disconnect-event.md) | The WskDisconnectEvent event callback function notifies a WSK application that a connection on a connection-oriented socket has been disconnected by the remote application. |
| [PFN_WSK_FREE_ADDRESS_INFO callback](nc-wsk-pfn-wsk-free-address-info.md) | The WskFreeAddressInfo function frees address information that the WskGetAddressInfo function has dynamically allocated. |
| [PFN_WSK_GET_ADDRESS_INFO callback](nc-wsk-pfn-wsk-get-address-info.md) | The WskGetAddressInfo function performs protocol-independent translation from a host name to a transport address. |
| [PFN_WSK_GET_LOCAL_ADDRESS callback](nc-wsk-pfn-wsk-get-local-address.md) | The WskGetLocalAddress function retrieves the local transport address of a socket. |
| [PFN_WSK_GET_NAME_INFO callback](nc-wsk-pfn-wsk-get-name-info.md) | The WskGetNameInfo function provides protocol-independent translation from a transport address to a host name. |
| [PFN_WSK_GET_REMOTE_ADDRESS callback](nc-wsk-pfn-wsk-get-remote-address.md) | The WskGetRemoteAddress function retrieves the remote transport address of a connection-oriented or stream socket. |
| [PFN_WSK_INSPECT_COMPLETE callback](nc-wsk-pfn-wsk-inspect-complete.md) | The WskInspectComplete function completes the inspection of a previously pended incoming connection request that was received on a listening socket that has conditional accept mode enabled. |
| [PFN_WSK_INSPECT_EVENT callback](nc-wsk-pfn-wsk-inspect-event.md) | The WskInspectEvent event callback function notifies a WSK application that an incoming connection request on a listening socket that has conditional accept mode enabled has been received. |
| [PFN_WSK_LISTEN callback](nc-wsk-pfn-wsk-listen.md) | The WskListen function enables a stream socket to listen for incoming connections at the socket's bound address. |
| [PFN_WSK_RECEIVE callback](nc-wsk-pfn-wsk-receive.md) | The WskReceive function receives data over a connection-oriented or stream socket from a remote transport address. |
| [PFN_WSK_RECEIVE_EVENT callback](nc-wsk-pfn-wsk-receive-event.md) | The WskReceiveEvent event callback function notifies a WSK application that data has been received on a connection-oriented socket. |
| [PFN_WSK_RECEIVE_FROM callback](nc-wsk-pfn-wsk-receive-from.md) | The WskReceiveFrom function receives a datagram and any associated control information from a remote transport address. |
| [PFN_WSK_RECEIVE_FROM_EVENT callback](nc-wsk-pfn-wsk-receive-from-event.md) | The WskReceiveFromEvent event callback function notifies a WSK application that one or more datagrams have been received on a datagram socket. |
| [PFN_WSK_SEND callback](nc-wsk-pfn-wsk-send.md) | The WskSend function sends data over a connection-oriented or stream socket to a remote transport address. |
| [PFN_WSK_SEND_BACKLOG_EVENT callback](nc-wsk-pfn-wsk-send-backlog-event.md) | The WskSendBacklogEvent event callback function notifies a WSK application when the ideal send backlog size changes for a connection-oriented socket. |
| [PFN_WSK_SEND_TO callback](nc-wsk-pfn-wsk-send-to.md) | The WskSendTo function sends datagram data to a remote transport address. |
| [PFN_WSK_SOCKET callback](nc-wsk-pfn-wsk-socket.md) | The WskSocket function creates a new socket and returns a pointer to the associated socket object. |
| [PFN_WSK_SOCKET_CONNECT callback](nc-wsk-pfn-wsk-socket-connect.md) | The WskSocketConnect function creates a new connection-oriented socket, binds it to a local transport address, connects it to a given remote transport address, and returns a pointer to the associated socket object. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [WSK_BUF structure](ns-wsk--wsk-buf.md) | The WSK_BUF structure defines a data buffer that is used for sending and receiving data over a socket. |
| [WSK_CLIENT_CONNECTION_DISPATCH structure](ns-wsk--wsk-client-connection-dispatch.md) | The WSK_CLIENT_CONNECTION_DISPATCH structure specifies a WSK application's dispatch table of event callback functions for a connection-oriented socket. |
| [WSK_CLIENT_CONNECTION_DISPATCH structure](ns-wsk--wsk-client-connection-dispatch~r1.md) | The WSK_CLIENT_CONNECTION_DISPATCH structure specifies a WSK application's dispatch table of event callback functions for a connection-oriented socket. |
| [WSK_CLIENT_DATAGRAM_DISPATCH structure](ns-wsk--wsk-client-datagram-dispatch.md) | The WSK_CLIENT_DATAGRAM_DISPATCH structure specifies a WSK application's dispatch table of event callback functions for a datagram socket. |
| [WSK_CLIENT_DISPATCH structure](ns-wsk--wsk-client-dispatch.md) | The WSK_CLIENT_DISPATCH structure specifies a WSK application's dispatch table of event callback functions for events that are not specific to a particular socket. |
| [WSK_CLIENT_LISTEN_DISPATCH structure](ns-wsk--wsk-client-listen-dispatch.md) | The WSK_CLIENT_LISTEN_DISPATCH structure specifies a WSK application's dispatch table of event callback functions for a listening socket. |
| [WSK_CLIENT_NPI structure](ns-wsk--wsk-client-npi.md) | The WSK_CLIENT_NPI structure identifies a Network Programming Interface (NPI) implemented by a WSK client. |
| [WSK_CLIENT_STREAM_DISPATCH structure](ns-wsk--wsk-client-stream-dispatch.md) | The WSK_CLIENT_STREAM_DISPATCH structure specifies a WSK application's dispatch table of event callback functions for a stream socket. |
| [WSK_DATAGRAM_INDICATION structure](ns-wsk--wsk-datagram-indication.md) | The WSK_DATAGRAM_INDICATION structure describes a datagram that has been received on a datagram socket. |
| [WSK_DATA_INDICATION structure](ns-wsk--wsk-data-indication.md) | The WSK_DATA_INDICATION structure describes data that has been received on a connection-oriented socket. |
| [WSK_EVENT_CALLBACK_CONTROL structure](ns-wsk--wsk-event-callback-control.md) | The WSK_EVENT_CALLBACK_CONTROL structure specifies the information for enabling and disabling a socket's event callback functions. |
| [WSK_EXTENSION_CONTROL_IN structure](ns-wsk--wsk-extension-control-in.md) | The WSK_EXTENSION_CONTROL_IN structure specifies a WSK application's implementation of an extension interface for a socket. |
| [WSK_EXTENSION_CONTROL_OUT structure](ns-wsk--wsk-extension-control-out.md) | The WSK_EXTENSION_CONTROL_OUT structure specifies the WSK subsystem's implementation of an extension interface for a socket. |
| [WSK_INSPECT_ID structure](ns-wsk--wsk-inspect-id.md) | The WSK_INSPECT_ID structure specifies an identifier for an incoming connection request on a listening socket. |
| [WSK_PROVIDER_BASIC_DISPATCH structure](ns-wsk--wsk-provider-basic-dispatch.md) | The WSK_PROVIDER_BASIC_DISPATCH structure specifies the WSK subsystem's dispatch table of functions for a basic socket. |
| [WSK_PROVIDER_CHARACTERISTICS structure](ns-wsk--wsk-provider-characteristics.md) | The WSK_PROVIDER_CHARACTERISTICS structure specifies the characteristics of the WSK subsystem. |
| [WSK_PROVIDER_CONNECTION_DISPATCH structure](ns-wsk--wsk-provider-connection-dispatch.md) | The WSK_PROVIDER_CONNECTION_DISPATCH structure specifies the WSK subsystem's table of functions for a connection-oriented socket. |
| [WSK_PROVIDER_DATAGRAM_DISPATCH structure](ns-wsk--wsk-provider-datagram-dispatch.md) | The WSK_PROVIDER_DATAGRAM_DISPATCH structure specifies the WSK subsystem's table of functions for a datagram socket. |
| [WSK_PROVIDER_DISPATCH structure](ns-wsk--wsk-provider-dispatch.md) | The WSK_PROVIDER_DISPATCH structure specifies the WSK subsystem's dispatch table of functions that are not specific to a particular socket. |
| [WSK_PROVIDER_LISTEN_DISPATCH structure](ns-wsk--wsk-provider-listen-dispatch.md) | The WSK_PROVIDER_LISTEN_DISPATCH structure specifies the WSK subsystem's table of functions for a listening socket. |
| [WSK_PROVIDER_NPI structure](ns-wsk--wsk-provider-npi.md) | The WSK_PROVIDER_NPI structure identifies a provider Network Programming Interface (NPI) implemented by the WSK subsystem. |
| [WSK_PROVIDER_STREAM_DISPATCH structure](ns-wsk--wsk-provider-stream-dispatch.md) | The WSK_PROVIDER_STREAM_DISPATCH structure specifies the WSK subsystem's table of functions for a stream socket. |
| [WSK_REGISTRATION structure](ns-wsk--wsk-registration.md) | The WSK_REGISTRATION structure is used by the WSK subsystem to register or unregister a WSK application as a WSK client. |
| [WSK_SOCKET structure](ns-wsk--wsk-socket.md) | The WSK_SOCKET structure defines a socket object for a socket. |
| [WSK_TDI_MAP structure](ns-wsk--wsk-tdi-map.md) | The WSK_TDI_MAP structure specifies a mapping between a particular address family, socket type, and protocol to the device name of a TDI transport. |
| [WSK_TDI_MAP_INFO structure](ns-wsk--wsk-tdi-map-info.md) | The WSK_TDI_MAP_INFO structure specifies a list that contains mappings of a combination of an address family, a socket type, and a protocol to the device name of a TDI transport. |
| [WSK_TRANSPORT structure](ns-wsk--wsk-transport.md) | The WSK_TRANSPORT structure specifies an available transport that is supported by the WSK subsystem. |
