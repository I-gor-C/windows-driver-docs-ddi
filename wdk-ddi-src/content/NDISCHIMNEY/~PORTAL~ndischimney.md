# Declarations in the ndischimney header
This header Ndischimney contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [TCP_OFFLOAD_RECEIVE_INDICATE_HANDLER callback](nc-ndischimney-tcp-offload-receive-indicate-handler.md) | NDIS calls a protocol driver's or intermediate driver's ProtocolTcpOffloadReceiveIndicate function to deliver received data that is being indicated by an underlying driver or offload target. |
| [UPDATE_OFFLOAD_COMPLETE_HANDLER callback](nc-ndischimney-update-offload-complete-handler.md) | NDIS calls a protocol driver's or intermediate driver's ProtocolUpdateOffloadComplete function to complete an update offload operation that the driver previously initiated by calling the NdisUpdateOffload function. |
| [INDICATE_OFFLOAD_EVENT_HANDLER callback](nc-ndischimney-indicate-offload-event-handler.md) | NDIS calls a protocol driver's or intermediate driver's ProtocolIndicateOffloadEvent function to post an indication that was initiated by an underlying driver's or offload target's call to the NdisMOffloadEventIndicate function. |
| [W_TCP_OFFLOAD_DISCONNECT_HANDLER callback](nc-ndischimney-w-tcp-offload-disconnect-handler.md) | The MiniportTcpOffloadDisconnect function closes the send half of an offloaded TCP connection. |
| [TCP_OFFLOAD_SEND_COMPLETE_HANDLER callback](nc-ndischimney-tcp-offload-send-complete-handler.md) | NDIS calls a protocol or intermediate driver's ProtocolTcpOffloadSendComplete function to complete a send operation that the driver previously initiated by calling the NdisOffloadTcpSend function. |
| [TCP_OFFLOAD_DISCONNECT_COMPLETE_HANDLER callback](nc-ndischimney-tcp-offload-disconnect-complete-handler.md) | NDIS calls a protocol driver's or intermediate driver's ProtocolTcpOffloadDisconnectComplete function to complete a disconnect operation that the driver previously initiated by calling the NdisOffloadTcpDisconnect function. |
| [W_TCP_OFFLOAD_RECEIVE_RETURN_HANDLER callback](nc-ndischimney-w-tcp-offload-receive-return-handler.md) | NDIS calls the MiniportTcpOffloadReceiveReturn function to return ownership of NET_BUFFER_LIST and associated structures to an offload target. |
| [QUERY_OFFLOAD_COMPLETE_HANDLER callback](nc-ndischimney-query-offload-complete-handler.md) | NDIS calls a protocol driver's or intermediate driver's ProtocolQueryOffloadComplete function to complete a query offload operation that the driver previously initiated by calling the NdisQueryOffload function. |
| [NDIS_TCP_OFFLOAD_FORWARD_COMPLETE callback function](nc-ndischimney-ndis-tcp-offload-forward-complete.md) | TBD |
| [NDIS_TCP_OFFLOAD_DISCONNECT_COMPLETE callback function](nc-ndischimney-ndis-tcp-offload-disconnect-complete.md) | TBD |
| [NDIS_TCP_OFFLOAD_EVENT_INDICATE callback function](nc-ndischimney-ndis-tcp-offload-event-indicate.md) | TBD |
| [INVALIDATE_OFFLOAD_COMPLETE_HANDLER callback](nc-ndischimney-invalidate-offload-complete-handler.md) | NDIS calls a protocol driver's or intermediate driver's ProtocolInvalidateOffloadComplete function to complete an invalidate operation that the driver previously initiated by calling the NdisInvalidateOffload function. |
| [TCP_OFFLOAD_RECV_COMPLETE_HANDLER callback](nc-ndischimney-tcp-offload-recv-complete-handler.md) | NDIS calls a protocol or intermediate driver's ProtocolTcpOffloadReceiveComplete function to complete a receive operation that the driver previously initiated by calling the NdisOffloadTcpReceive function. |
| [TCP_OFFLOAD_EVENT_HANDLER callback](nc-ndischimney-tcp-offload-event-handler.md) | NDIS calls a protocol driver's or intermediate driver's ProtocolIndicateOffloadEvent function to post an indication that was initiated by an underlying driver's or offload target's call to the NdisTcpOffloadEventHandler function. |
| [W_TCP_OFFLOAD_RECEIVE_HANDLER callback](nc-ndischimney-w-tcp-offload-receive-handler.md) | NDIS calls the MiniportTcpOffloadReceive function to post receive requests (receive buffers) on an offloaded TCP connection. |
| [W_QUERY_OFFLOAD_HANDLER callback](nc-ndischimney-w-query-offload-handler.md) | The MiniportQueryOffload function queries previously offloaded TCP chimney state objects. |
| [W_INVALIDATE_OFFLOAD_HANDLER callback](nc-ndischimney-w-invalidate-offload-handler.md) | The MiniportInvalidateOffload function invalidates previously offloaded TCP chimney state objects. |
| [W_INITIATE_OFFLOAD_HANDLER callback](nc-ndischimney-w-initiate-offload-handler.md) | MiniportInitiateOffload offloads TCP chimney state from the host stack. |
| [NDIS_TCP_OFFLOAD_RECEIVE_INDICATE callback function](nc-ndischimney-ndis-tcp-offload-receive-indicate.md) | TBD |
| [INITIATE_OFFLOAD_COMPLETE_HANDLER callback](nc-ndischimney-initiate-offload-complete-handler.md) | NDIS calls a protocol driver's or intermediate driver's ProtocolInitiateOffloadComplete function to complete an offload operation that the driver previously initiated by calling the NdisInitiateOffload function. |
| [W_TCP_OFFLOAD_SEND_HANDLER callback](nc-ndischimney-w-tcp-offload-send-handler.md) | NDIS calls the MiniportTcpOffloadSend function to transmit data on an offloaded TCP connection. |
| [W_TCP_OFFLOAD_FORWARD_HANDLER callback](nc-ndischimney-w-tcp-offload-forward-handler.md) | NDIS calls the MiniportTcpOffloadForward function to forward unacknowledged received TCP segments to an offload target. |
| [W_UPDATE_OFFLOAD_HANDLER callback](nc-ndischimney-w-update-offload-handler.md) | The MiniportUpdateOffload function updates previously offloaded TCP chimney state objects. |
| [NDIS_TCP_OFFLOAD_RECEIVE_COMPLETE callback function](nc-ndischimney-ndis-tcp-offload-receive-complete.md) | TBD |
| [TERMINATE_OFFLOAD_COMPLETE_HANDLER callback](nc-ndischimney-terminate-offload-complete-handler.md) | NDIS calls a protocol or intermediate driver's ProtocolTerminateOffloadComplete function to complete a terminate offload operation that the driver previously initiated by calling the NdisTerminateOffload function. |
| [NDIS_TCP_OFFLOAD_SEND_COMPLETE callback function](nc-ndischimney-ndis-tcp-offload-send-complete.md) | TBD |
| [TCP_OFFLOAD_FORWARD_COMPLETE_HANDLER callback](nc-ndischimney-tcp-offload-forward-complete-handler.md) | NDIS calls a protocol or intermediate driver's ProtocolTcpOffloadForwardComplete function to complete a forward operation that the driver previously initiated by calling the NdisOffloadTcpForward function. |
| [W_TERMINATE_OFFLOAD_HANDLER callback](nc-ndischimney-w-terminate-offload-handler.md) | The MiniportTerminateOffload function terminates the offload of one or more state objects. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [NDIS_TCP_OFFLOAD_EVENT_HANDLERS structure](ns-ndischimney--ndis-tcp-offload-event-handlers.md) | The NDIS_TCP_OFFLOAD_EVENT_HANDLERS structure contains the entry points for the NDIS functions for the TCP chimney. |
| [NDIS_OFFLOAD_HANDLE structure](ns-ndischimney--ndis-offload-handle.md) | The NDIS_OFFLOAD_HANDLE structure represents a driver's context for an offloaded state object. |
| [NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure](ns-ndischimney--ndis-miniport-offload-block-list.md) | The NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure is the basic building block of a TCP chimney offload state tree. An offload state tree can contain one or more NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structures. |
| [NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure](ns-ndischimney--ndis-protocol-offload-block-list.md) | The NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure. |
| [OFFLOAD_STATE_HEADER structure](ns-ndischimney--offload-state-header.md) | The OFFLOAD_STATE_HEADER structure serves as a header in an offload state structure. |
| [NEIGHBOR_OFFLOAD_STATE_DELEGATED structure](ns-ndischimney--neighbor-offload-state-delegated.md) | The NEIGHBOR_OFFLOAD_STATE_DELGATED structure contains the delegated variable of a neighbor state object. |
| [NDIS_TCP_OFFLOAD_CLIENT_HANDLERS structure](ns-ndischimney--ndis-tcp-offload-client-handlers.md) | TBD |
| [PATH_OFFLOAD_STATE_DELEGATED structure](ns-ndischimney--path-offload-state-delegated.md) | The PATH_OFFLOAD_STATE_DELEGATED structure contains the delegated variables of a path state object. |
| [NDIS_PROVIDER_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS structure](ns-ndischimney--ndis-provider-chimney-offload-generic-characteristics.md) | The NDIS_PROVIDER_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS structure specifies the generic chimney offload miniport entry points of an offload target or intermediate driver. |
| [NDIS_OFFLOAD_EVENT_HANDLERS structure](ns-ndischimney--ndis-offload-event-handlers.md) | TBD |
| [NDIS_OFFLOAD_HANDLE_PRIVATE structure](ns-ndischimney--ndis-offload-handle-private.md) | TBD |
| [NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure](ns-ndischimney--ndis-provider-chimney-offload-tcp-characteristics.md) | The NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure specifies an offload target's TCP chimney offload-specific entry points. |
| [NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure](ns-ndischimney--ndis-client-chimney-offload-tcp-characteristics.md) | The NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure specifies a protocol or intermediate driver's TCP chimney offload-specific entry points. |
| [PATH_OFFLOAD_STATE_CACHED structure](ns-ndischimney--path-offload-state-cached.md) | The PATH_OFFLOAD_STATE_CACHED structure contains the cached variable of a path state object. |
| [TCP_OFFLOAD_STATE_CACHED structure](ns-ndischimney--tcp-offload-state-cached.md) | The TCP_OFFLOAD_STATE_CACHED structure contains the cached variables of a TCP connection state object. |
| [NEIGHBOR_OFFLOAD_STATE_CACHED structure](ns-ndischimney--neighbor-offload-state-cached.md) | The NEIGHBOR_OFFLOAD_STATE_CACHED structure contains the cached variables of a neighbor state object. |
| [NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS structure](ns-ndischimney--ndis-client-chimney-offload-generic-characteristics.md) | The NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS structure specifies a protocol driver's generic chimney offload entry points. |
| [NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS structure](ns-ndischimney--ndis-tcp-connection-offload-parameters.md) | The NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS structure provides TCP chimney offload information in the OID_TCP_CONNECTION_OFFLOAD_PARAMETERS OIDs |
| [IP_OFFLOAD_STATS structure](ns-ndischimney--ip-offload-stats.md) | The IP_OFFLOAD_STATS structure contains statistics that an offload target supplies in response to a query of OID_IP4_OFFLOAD_STATS or OID_IP6_OFFLOAD_STATS. |
| [NDIS_OFFLOAD_CLIENT_HANDLERS structure](ns-ndischimney--ndis-offload-client-handlers.md) | TBD |
| [NDIS_TCP_CONNECTION_OFFLOAD_ENCAPSULATION structure](ns-ndischimney--ndis-tcp-connection-offload-encapsulation.md) | TBD |
| [NEIGHBOR_OFFLOAD_STATE_CONST structure](ns-ndischimney--neighbor-offload-state-const.md) | The NEIGHBOR_OFFLOAD_STATE_CONST structure contains the constant variables of a neighbor state object. |
| [TCP_OFFLOAD_STATE_CONST structure](ns-ndischimney--tcp-offload-state-const.md) | The TCP_OFFLOAD_STATE_CONST structure contains the constant variables of a TCP connection state object. |
| [PATH_OFFLOAD_STATE_CONST structure](ns-ndischimney--path-offload-state-const.md) | The PATH_OFFLOAD_STATE_CONST structure contains the constant variables of a path state object. |
| [TCP_OFFLOAD_STATE_DELEGATED structure](ns-ndischimney--tcp-offload-state-delegated.md) | The TCP_OFFLOAD_STATE_DELEGATED structure contains the delegated variables of a TCP connection state object. |
| [TCP_OFFLOAD_STATS structure](ns-ndischimney--tcp-offload-stats.md) | The TCP_OFFLOAD_STATS structure contains statistics that an offload target supplies in response to a query of OID_TCP4_OFFLOAD_STATS or OID_TCP6_OFFLOAD_STATS. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [NdisQueryOffloadState function](nf-ndischimney-ndisqueryoffloadstate.md) | TBD |
| [NdisMQueryOffloadStateComplete function](nf-ndischimney-ndismqueryoffloadstatecomplete.md) | An offload target calls the NdisMQueryOffloadStateComplete function to complete a query offload operation that was initiated by a previous call to the offload target's MiniportQueryOffload function. |
| [NdisOffloadTcpSend function](nf-ndischimney-ndisoffloadtcpsend.md) | A protocol driver or intermediate driver calls the NdisOffloadTcpSend function to transmit data on an offloaded TCP connection. |
| [NdisOffloadTcpReceive function](nf-ndischimney-ndisoffloadtcpreceive.md) | A protocol driver or an intermediate driver calls the NdisOffloadTcpReceive function to post receive requests (receive buffers) on an offloaded TCP connection. |
| [NdisUpdateOffload function](nf-ndischimney-ndisupdateoffload.md) | A protocol or intermediate driver calls the NdisUpdateOffload function to update previously offloaded TCP chimney state objects. |
| [NdisInvalidateOffload function](nf-ndischimney-ndisinvalidateoffload.md) | A protocol or intermediate driver calls the NdisInvalidateOffload function to invalidate previously offloaded TCP chimney state objects. |
| [NdisMTerminateOffloadComplete function](nf-ndischimney-ndismterminateoffloadcomplete.md) | An offload target calls the NdisMTerminateOffloadComplete function to complete a terminate offload operation that was initiated by a previous call to the MiniportTerminateOffload function of the offload target. |
| [NdisMInvalidateOffloadComplete function](nf-ndischimney-ndisminvalidateoffloadcomplete.md) | An offload target calls the NdisMInvalidateOffloadComplete function to complete an invalidate offload operation that was initiated by a previous call to the MiniportInvalidateOffload function of the offload target. |
| [NdisTerminateOffload function](nf-ndischimney-ndisterminateoffload.md) | A protocol driver or intermediate driver calls the NdisTerminateOffload function to terminate the offload of one or more state objects |
| [NdisMGetOffloadHandlers function](nf-ndischimney-ndismgetoffloadhandlers.md) | This function obtains the entry points of the NDIS functions for a particular chimney type. |
| [NdisMOffloadEventIndicate function](nf-ndischimney-ndismoffloadeventindicate.md) | An offload target calls the NdisMOffloadEventIndicate function to indicate various events to the host stack. |
| [NdisOffloadTcpDisconnect function](nf-ndischimney-ndisoffloadtcpdisconnect.md) | A protocol or intermediate driver calls the NdisOffloadTcpDisconnect function to close the send half of an offloaded TCP connection. |
| [NdisMUpdateOffloadComplete function](nf-ndischimney-ndismupdateoffloadcomplete.md) | An offload target calls the NdisMUpdateOffloadComplete function to complete an update offload operation that was initiated by a previous call to the MiniportUpdateOffload function of the offload target. |
| [NdisInitiateOffload function](nf-ndischimney-ndisinitiateoffload.md) | A protocol or intermediate driver calls the NdisInitiateOffload function to offload TCP chimney state objects. |
| [NdisOffloadTcpForward function](nf-ndischimney-ndisoffloadtcpforward.md) | A protocol driver or an intermediate driver calls the NdisOffloadTcpForward function to forward unacknowledged received TCP segments to an underlying driver or offload target. |
| [NdisMInitiateOffloadComplete function](nf-ndischimney-ndisminitiateoffloadcomplete.md) | An offload target calls the NdisMInitiateOffloadComplete function to complete an offload operation that was initiated by a previous call to the MiniportInitiateOffload function. |
| [NdisOffloadTcpReceiveReturn function](nf-ndischimney-ndisoffloadtcpreceivereturn.md) | A protocol driver or intermediate driver calls the NdisOffloadTcpReceiveReturn function to return ownership of NET_BUFFER_LIST and associated structures to an underlying offload target. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [PINDICATE_OFFLOAD_EVENT enumeration](ne-ndischimney-pindicate-offload-event.md) | TBD |
| [PTCP_UPLOAD_REASON enumeration](ne-ndischimney-ptcp-upload-reason.md) | TBD |
| [PTCP_OFFLOAD_EVENT_TYPE enumeration](ne-ndischimney-ptcp-offload-event-type.md) | TBD |
| [POFFLOAD_STATE_TYPE enumeration](ne-ndischimney-poffload-state-type.md) | TBD |
| [PTCP_OFFLOAD_CONNECTION_STATE enumeration](ne-ndischimney-ptcp-offload-connection-state.md) | TBD |
| [PNDIS_CHIMNEY_OFFLOAD_TYPE enumeration](ne-ndischimney-pndis-chimney-offload-type.md) | TBD |

This header is used in these topics:

- [netvista](..content/_netvista)
