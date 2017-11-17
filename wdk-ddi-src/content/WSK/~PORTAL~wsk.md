# Declarations in the wsk header
This header Wsk contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WSK_SOCKET_CONNECT callback function](nc-wsk-pfn-wsk-socket-connect.md) | TBD |
| [PFN_WSK_SEND_BACKLOG_EVENT callback](nc-wsk-pfn-wsk-send-backlog-event.md) | The WskSendBacklogEvent event callback function notifies a WSK application when the ideal send backlog size changes for a connection-oriented socket. |
| [PFN_WSK_RELEASE_DATAGRAM_INDICATION_LIST callback function](nc-wsk-pfn-wsk-release-datagram-indication-list.md) | TBD |
| [PFN_WSK_GET_REMOTE_ADDRESS callback function](nc-wsk-pfn-wsk-get-remote-address.md) | TBD |
| [PFN_WSK_CONNECT_EX callback function](nc-wsk-pfn-wsk-connect-ex.md) | TBD |
| [PFN_WSK_FREE_ADDRESS_INFO callback function](nc-wsk-pfn-wsk-free-address-info.md) | TBD |
| [PFN_WSK_RECEIVE_EVENT callback](nc-wsk-pfn-wsk-receive-event.md) | The WskReceiveEvent event callback function notifies a WSK application that data has been received on a connection-oriented socket. |
| [PFN_WSK_LISTEN callback function](nc-wsk-pfn-wsk-listen.md) | TBD |
| [PFN_WSK_RECEIVE_FROM_EVENT callback](nc-wsk-pfn-wsk-receive-from-event.md) | The WskReceiveFromEvent event callback function notifies a WSK application that one or more datagrams have been received on a datagram socket. |
| [PFN_WSK_DISCONNECT callback function](nc-wsk-pfn-wsk-disconnect.md) | TBD |
| [PFN_WSK_RECEIVE_FROM callback function](nc-wsk-pfn-wsk-receive-from.md) | TBD |
| [PFN_WSK_INSPECT_EVENT callback](nc-wsk-pfn-wsk-inspect-event.md) | The WskInspectEvent event callback function notifies a WSK application that an incoming connection request on a listening socket that has conditional accept mode enabled has been received. |
| [PFN_WSK_SOCKET callback function](nc-wsk-pfn-wsk-socket.md) | TBD |
| [PFN_WSK_CONTROL_SOCKET callback function](nc-wsk-pfn-wsk-control-socket.md) | TBD |
| [PFN_WSK_ACCEPT callback function](nc-wsk-pfn-wsk-accept.md) | TBD |
| [PFN_WSK_CONTROL_CLIENT callback function](nc-wsk-pfn-wsk-control-client.md) | TBD |
| [PFN_WSK_ABORT_EVENT callback](nc-wsk-pfn-wsk-abort-event.md) | The WskAbortEvent event callback function notifies a WSK application that an incoming connection request on a listening socket that has conditional accept mode enabled has been dropped. |
| [PFN_WSK_INSPECT_COMPLETE callback function](nc-wsk-pfn-wsk-inspect-complete.md) | TBD |
| [PFN_WSK_BIND callback function](nc-wsk-pfn-wsk-bind.md) | TBD |
| [PFN_WSK_GET_NAME_INFO callback function](nc-wsk-pfn-wsk-get-name-info.md) | TBD |
| [PFN_WSK_SEND callback function](nc-wsk-pfn-wsk-send.md) | TBD |
| [PFN_WSK_RELEASE_DATA_INDICATION_LIST callback function](nc-wsk-pfn-wsk-release-data-indication-list.md) | TBD |
| [PFN_WSK_ACCEPT_EVENT callback](nc-wsk-pfn-wsk-accept-event.md) | The WskAcceptEvent event callback function notifies a WSK application that an incoming connection on a listening socket has been accepted. |
| [PFN_WSK_GET_ADDRESS_INFO callback function](nc-wsk-pfn-wsk-get-address-info.md) | TBD |
| [PFN_WSK_CONNECT callback function](nc-wsk-pfn-wsk-connect.md) | TBD |
| [PFN_WSK_GET_LOCAL_ADDRESS callback function](nc-wsk-pfn-wsk-get-local-address.md) | TBD |
| [PFN_WSK_DISCONNECT_EVENT callback](nc-wsk-pfn-wsk-disconnect-event.md) | The WskDisconnectEvent event callback function notifies a WSK application that a connection on a connection-oriented socket has been disconnected by the remote application. |
| [PFN_WSK_CLIENT_EVENT callback](nc-wsk-pfn-wsk-client-event.md) | The WskClientEvent event callback function notifies a WSK application about events that are not specific to a particular socket. |
| [PFN_WSK_SEND_MESSAGES callback function](nc-wsk-pfn-wsk-send-messages.md) | TBD |
| [PFN_WSK_SEND_TO callback function](nc-wsk-pfn-wsk-send-to.md) | TBD |
| [PFN_WSK_CLOSE_SOCKET callback function](nc-wsk-pfn-wsk-close-socket.md) | TBD |
| [PFN_WSK_RECEIVE callback function](nc-wsk-pfn-wsk-receive.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WSK_BUF_LIST structure](ns-wsk--wsk-buf-list.md) | TBD |
| [WSK_CLIENT_NPI structure](ns-wsk--wsk-client-npi.md) | The WSK_CLIENT_NPI structure identifies a Network Programming Interface (NPI) implemented by a WSK client. |
| [WSK_EXTENSION_CONTROL_OUT structure](ns-wsk--wsk-extension-control-out.md) | The WSK_EXTENSION_CONTROL_OUT structure specifies the WSK subsystem's implementation of an extension interface for a socket. |
| [WSK_PROVIDER_CONNECTION_DISPATCH structure](ns-wsk--wsk-provider-connection-dispatch.md) | The WSK_PROVIDER_CONNECTION_DISPATCH structure specifies the WSK subsystem's table of functions for a connection-oriented socket. |
| [WSK_CLIENT_DATAGRAM_DISPATCH structure](ns-wsk--wsk-client-datagram-dispatch.md) | The WSK_CLIENT_DATAGRAM_DISPATCH structure specifies a WSK application's dispatch table of event callback functions for a datagram socket. |
| [WSK_DATA_INDICATION structure](ns-wsk--wsk-data-indication.md) | The WSK_DATA_INDICATION structure describes data that has been received on a connection-oriented socket. |
| [WSK_REGISTRATION structure](ns-wsk--wsk-registration.md) | The WSK_REGISTRATION structure is used by the WSK subsystem to register or unregister a WSK application as a WSK client. |
| [WSK_PROVIDER_BASIC_DISPATCH structure](ns-wsk--wsk-provider-basic-dispatch.md) | The WSK_PROVIDER_BASIC_DISPATCH structure specifies the WSK subsystem's dispatch table of functions for a basic socket. |
| [WSK_BUF structure](ns-wsk--wsk-buf.md) | The WSK_BUF structure defines a data buffer that is used for sending and receiving data over a socket. |
| [WSK_TDI_MAP_INFO structure](ns-wsk--wsk-tdi-map-info.md) | The WSK_TDI_MAP_INFO structure specifies a list that contains mappings of a combination of an address family, a socket type, and a protocol to the device name of a TDI transport. |
| [WSK_PROVIDER_NPI structure](ns-wsk--wsk-provider-npi.md) | The WSK_PROVIDER_NPI structure identifies a provider Network Programming Interface (NPI) implemented by the WSK subsystem. |
| [WSK_PROVIDER_DISPATCH structure](ns-wsk--wsk-provider-dispatch.md) | The WSK_PROVIDER_DISPATCH structure specifies the WSK subsystem's dispatch table of functions that are not specific to a particular socket. |
| [WSK_EVENT_CALLBACK_CONTROL structure](ns-wsk--wsk-event-callback-control.md) | The WSK_EVENT_CALLBACK_CONTROL structure specifies the information for enabling and disabling a socket's event callback functions. |
| [WSK_CLIENT_CONNECTION_DISPATCH structure](ns-wsk--wsk-client-connection-dispatch~r1.md) | The WSK_CLIENT_CONNECTION_DISPATCH structure specifies a WSK application's dispatch table of event callback functions for a connection-oriented socket. |
| [WSK_SOCKET structure](ns-wsk--wsk-socket.md) | The WSK_SOCKET structure defines a socket object for a socket. |
| [WSK_PROVIDER_DATAGRAM_DISPATCH structure](ns-wsk--wsk-provider-datagram-dispatch.md) | The WSK_PROVIDER_DATAGRAM_DISPATCH structure specifies the WSK subsystem's table of functions for a datagram socket. |
| [WSK_CLIENT_STREAM_DISPATCH structure](ns-wsk--wsk-client-stream-dispatch.md) | The WSK_CLIENT_STREAM_DISPATCH structure specifies a WSK application's dispatch table of event callback functions for a stream socket. |
| [WSK_TRANSPORT structure](ns-wsk--wsk-transport.md) | The WSK_TRANSPORT structure specifies an available transport that is supported by the WSK subsystem. |
| [WSK_EXTENSION_CONTROL_IN structure](ns-wsk--wsk-extension-control-in.md) | The WSK_EXTENSION_CONTROL_IN structure specifies a WSK application's implementation of an extension interface for a socket. |
| [WSK_INSPECT_ID structure](ns-wsk--wsk-inspect-id.md) | The WSK_INSPECT_ID structure specifies an identifier for an incoming connection request on a listening socket. |
| [WSK_PROVIDER_STREAM_DISPATCH structure](ns-wsk--wsk-provider-stream-dispatch.md) | The WSK_PROVIDER_STREAM_DISPATCH structure specifies the WSK subsystem's table of functions for a stream socket. |
| [WSK_PROVIDER_LISTEN_DISPATCH structure](ns-wsk--wsk-provider-listen-dispatch.md) | The WSK_PROVIDER_LISTEN_DISPATCH structure specifies the WSK subsystem's table of functions for a listening socket. |
| [WSK_DATAGRAM_INDICATION structure](ns-wsk--wsk-datagram-indication.md) | The WSK_DATAGRAM_INDICATION structure describes a datagram that has been received on a datagram socket. |
| [WSK_CLIENT_DISPATCH structure](ns-wsk--wsk-client-dispatch.md) | The WSK_CLIENT_DISPATCH structure specifies a WSK application's dispatch table of event callback functions for events that are not specific to a particular socket. |
| [WSK_CLIENT_CONNECTION_DISPATCH structure](ns-wsk--wsk-client-connection-dispatch.md) | TBD |
| [WSK_CLIENT_LISTEN_DISPATCH structure](ns-wsk--wsk-client-listen-dispatch.md) | The WSK_CLIENT_LISTEN_DISPATCH structure specifies a WSK application's dispatch table of event callback functions for a listening socket. |
| [WSK_TDI_MAP structure](ns-wsk--wsk-tdi-map.md) | The WSK_TDI_MAP structure specifies a mapping between a particular address family, socket type, and protocol to the device name of a TDI transport. |
| [WSK_PROVIDER_CHARACTERISTICS structure](ns-wsk--wsk-provider-characteristics.md) | The WSK_PROVIDER_CHARACTERISTICS structure specifies the characteristics of the WSK subsystem. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [PWSK_INSPECT_ACTION enumeration](ne-wsk-pwsk-inspect-action.md) | TBD |
| [PWSK_CONTROL_SOCKET_TYPE enumeration](ne-wsk-pwsk-control-socket-type.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WskDeregister function](nf-wsk-wskderegister.md) | The WskDeregister function unregisters a WSK application's registration instance that was previously created by WskRegister. |
| [WskQueryProviderCharacteristics function](nf-wsk-wskqueryprovidercharacteristics.md) | The WskQueryProviderCharacteristics function queries the range of WSK NPI versions supported by the WSK subsystem. |
| [WskCaptureProviderNPI function](nf-wsk-wskcaptureprovidernpi.md) | The WskCaptureProviderNPI function captures a provider Network Programming Interface (NPI) when it becomes available from the WSK subsystem. |
| [WskReleaseProviderNPI function](nf-wsk-wskreleaseprovidernpi.md) | The WskReleaseProviderNPI function releases a Network Programming Interface (NPI) that was captured with WskCaptureProviderNPI. |
| [MAKE_WSK_VERSION function](nf-wsk-make-wsk-version.md) | TBD |
| [WskRegister function](nf-wsk-wskregister.md) | The WskRegister function registers a WSK application, given the application's WSK client Network Programming Interface (NPI). |
| [WSK_MINOR_VERSION function](nf-wsk-wsk-minor-version.md) | TBD |
| [WSK_MAJOR_VERSION function](nf-wsk-wsk-major-version.md) | TBD |

This header is used in these topics:

- [netvista](..content/_netvista)
