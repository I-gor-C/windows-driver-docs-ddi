# Ndischimney.h header


This header is used by Networking drivers for Windows Vista and later. For more information, see
- [Networking drivers for Windows Vista and later](../_netvista/index.md)

Ndischimney.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [NdisInitiateOffload function](nf-ndischimney-ndisinitiateoffload.md) | A protocol or intermediate driver calls the NdisInitiateOffload function to offload TCP chimney state objects. |
| [NdisInvalidateOffload function](nf-ndischimney-ndisinvalidateoffload.md) | A protocol or intermediate driver calls the NdisInvalidateOffload function to invalidate previously offloaded TCP chimney state objects. |
| [NdisMGetOffloadHandlers function](nf-ndischimney-ndismgetoffloadhandlers.md) | This function obtains the entry points of the NDIS functions for a particular chimney type. |
| [NdisMInitiateOffloadComplete function](nf-ndischimney-ndisminitiateoffloadcomplete.md) | An offload target calls the NdisMInitiateOffloadComplete function to complete an offload operation that was initiated by a previous call to the MiniportInitiateOffload function. |
| [NdisMInvalidateOffloadComplete function](nf-ndischimney-ndisminvalidateoffloadcomplete.md) | An offload target calls the NdisMInvalidateOffloadComplete function to complete an invalidate offload operation that was initiated by a previous call to the MiniportInvalidateOffload function of the offload target. |
| [NdisMOffloadEventIndicate function](nf-ndischimney-ndismoffloadeventindicate.md) | An offload target calls the NdisMOffloadEventIndicate function to indicate various events to the host stack. |
| [NdisMQueryOffloadStateComplete function](nf-ndischimney-ndismqueryoffloadstatecomplete.md) | An offload target calls the NdisMQueryOffloadStateComplete function to complete a query offload operation that was initiated by a previous call to the offload target's MiniportQueryOffload function. |
| [NdisMTerminateOffloadComplete function](nf-ndischimney-ndismterminateoffloadcomplete.md) | An offload target calls the NdisMTerminateOffloadComplete function to complete a terminate offload operation that was initiated by a previous call to the MiniportTerminateOffload function of the offload target. |
| [NdisMUpdateOffloadComplete function](nf-ndischimney-ndismupdateoffloadcomplete.md) | An offload target calls the NdisMUpdateOffloadComplete function to complete an update offload operation that was initiated by a previous call to the MiniportUpdateOffload function of the offload target. |
| [NdisOffloadTcpDisconnect function](nf-ndischimney-ndisoffloadtcpdisconnect.md) | A protocol or intermediate driver calls the NdisOffloadTcpDisconnect function to close the send half of an offloaded TCP connection. |
| [NdisOffloadTcpForward function](nf-ndischimney-ndisoffloadtcpforward.md) | A protocol driver or an intermediate driver calls the NdisOffloadTcpForward function to forward unacknowledged received TCP segments to an underlying driver or offload target. |
| [NdisOffloadTcpReceive function](nf-ndischimney-ndisoffloadtcpreceive.md) | A protocol driver or an intermediate driver calls the NdisOffloadTcpReceive function to post receive requests (receive buffers) on an offloaded TCP connection. |
| [NdisOffloadTcpReceiveReturn function](nf-ndischimney-ndisoffloadtcpreceivereturn.md) | A protocol driver or intermediate driver calls the NdisOffloadTcpReceiveReturn function to return ownership of NET_BUFFER_LIST and associated structures to an underlying offload target. |
| [NdisOffloadTcpSend function](nf-ndischimney-ndisoffloadtcpsend.md) | A protocol driver or intermediate driver calls the NdisOffloadTcpSend function to transmit data on an offloaded TCP connection. |
| [NdisTerminateOffload function](nf-ndischimney-ndisterminateoffload.md) | A protocol driver or intermediate driver calls the NdisTerminateOffload function to terminate the offload of one or more state objects |
| [NdisUpdateOffload function](nf-ndischimney-ndisupdateoffload.md) | A protocol or intermediate driver calls the NdisUpdateOffload function to update previously offloaded TCP chimney state objects. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [INDICATE_OFFLOAD_EVENT_HANDLER callback](nc-ndischimney-indicate-offload-event-handler.md) | NDIS calls a protocol driver's or intermediate driver's ProtocolIndicateOffloadEvent function to post an indication that was initiated by an underlying driver's or offload target's call to the NdisMOffloadEventIndicate function. |
| [INITIATE_OFFLOAD_COMPLETE_HANDLER callback](nc-ndischimney-initiate-offload-complete-handler.md) | NDIS calls a protocol driver's or intermediate driver's ProtocolInitiateOffloadComplete function to complete an offload operation that the driver previously initiated by calling the NdisInitiateOffload function. |
| [INVALIDATE_OFFLOAD_COMPLETE_HANDLER callback](nc-ndischimney-invalidate-offload-complete-handler.md) | NDIS calls a protocol driver's or intermediate driver's ProtocolInvalidateOffloadComplete function to complete an invalidate operation that the driver previously initiated by calling the NdisInvalidateOffload function. |
| [NDIS_TCP_OFFLOAD_DISCONNECT_COMPLETE callback](nc-ndischimney-ndis-tcp-offload-disconnect-complete.md) | An offload target calls the NdisTcpOffloadDisconnectComplete function to complete a disconnect request that was initiated by a previous call to the MiniportTcpOffloadDisconnect function of the offload target. |
| [NDIS_TCP_OFFLOAD_EVENT_INDICATE callback](nc-ndischimney-ndis-tcp-offload-event-indicate.md) | An offload target calls the NdisTcpOffloadEventHandler function to indicate an event that pertains to an offloaded TCP connection. |
| [NDIS_TCP_OFFLOAD_FORWARD_COMPLETE callback](nc-ndischimney-ndis-tcp-offload-forward-complete.md) | An offload target calls the NdisTcpOffloadForwardComplete function to complete one or more forward requests that were made to the MiniportTcpOffloadForward function of the offload target. |
| [NDIS_TCP_OFFLOAD_RECEIVE_COMPLETE callback](nc-ndischimney-ndis-tcp-offload-receive-complete.md) | An offload target calls the NdisTcpOffloadReceiveComplete function to return posted receive requests (receive buffers) to the host stack. |
| [NDIS_TCP_OFFLOAD_RECEIVE_INDICATE callback](nc-ndischimney-ndis-tcp-offload-receive-indicate.md) | An offload target calls the NdisTcpOffloadReceiveHandler function to indicate that received network data is available for consumption by a client application. |
| [NDIS_TCP_OFFLOAD_SEND_COMPLETE callback](nc-ndischimney-ndis-tcp-offload-send-complete.md) | An offload target calls the NdisTcpOffloadSendComplete function to complete one or more send requests that were made to the MiniportTcpOffloadSend function of the offload target. |
| [QUERY_OFFLOAD_COMPLETE_HANDLER callback](nc-ndischimney-query-offload-complete-handler.md) | NDIS calls a protocol driver's or intermediate driver's ProtocolQueryOffloadComplete function to complete a query offload operation that the driver previously initiated by calling the NdisQueryOffload function. |
| [TCP_OFFLOAD_DISCONNECT_COMPLETE_HANDLER callback](nc-ndischimney-tcp-offload-disconnect-complete-handler.md) | NDIS calls a protocol driver's or intermediate driver's ProtocolTcpOffloadDisconnectComplete function to complete a disconnect operation that the driver previously initiated by calling the NdisOffloadTcpDisconnect function. |
| [TCP_OFFLOAD_EVENT_HANDLER callback](nc-ndischimney-tcp-offload-event-handler.md) | NDIS calls a protocol driver's or intermediate driver's ProtocolIndicateOffloadEvent function to post an indication that was initiated by an underlying driver's or offload target's call to the NdisTcpOffloadEventHandler function. |
| [TCP_OFFLOAD_FORWARD_COMPLETE_HANDLER callback](nc-ndischimney-tcp-offload-forward-complete-handler.md) | NDIS calls a protocol or intermediate driver's ProtocolTcpOffloadForwardComplete function to complete a forward operation that the driver previously initiated by calling the NdisOffloadTcpForward function. |
| [TCP_OFFLOAD_RECEIVE_INDICATE_HANDLER callback](nc-ndischimney-tcp-offload-receive-indicate-handler.md) | NDIS calls a protocol driver's or intermediate driver's ProtocolTcpOffloadReceiveIndicate function to deliver received data that is being indicated by an underlying driver or offload target. |
| [TCP_OFFLOAD_RECV_COMPLETE_HANDLER callback](nc-ndischimney-tcp-offload-recv-complete-handler.md) | NDIS calls a protocol or intermediate driver's ProtocolTcpOffloadReceiveComplete function to complete a receive operation that the driver previously initiated by calling the NdisOffloadTcpReceive function. |
| [TCP_OFFLOAD_SEND_COMPLETE_HANDLER callback](nc-ndischimney-tcp-offload-send-complete-handler.md) | NDIS calls a protocol or intermediate driver's ProtocolTcpOffloadSendComplete function to complete a send operation that the driver previously initiated by calling the NdisOffloadTcpSend function. |
| [TERMINATE_OFFLOAD_COMPLETE_HANDLER callback](nc-ndischimney-terminate-offload-complete-handler.md) | NDIS calls a protocol or intermediate driver's ProtocolTerminateOffloadComplete function to complete a terminate offload operation that the driver previously initiated by calling the NdisTerminateOffload function. |
| [UPDATE_OFFLOAD_COMPLETE_HANDLER callback](nc-ndischimney-update-offload-complete-handler.md) | NDIS calls a protocol driver's or intermediate driver's ProtocolUpdateOffloadComplete function to complete an update offload operation that the driver previously initiated by calling the NdisUpdateOffload function. |
| [W_INITIATE_OFFLOAD_HANDLER callback](nc-ndischimney-w-initiate-offload-handler.md) | MiniportInitiateOffload offloads TCP chimney state from the host stack. |
| [W_INVALIDATE_OFFLOAD_HANDLER callback](nc-ndischimney-w-invalidate-offload-handler.md) | The MiniportInvalidateOffload function invalidates previously offloaded TCP chimney state objects. |
| [W_QUERY_OFFLOAD_HANDLER callback](nc-ndischimney-w-query-offload-handler.md) | The MiniportQueryOffload function queries previously offloaded TCP chimney state objects. |
| [W_TCP_OFFLOAD_DISCONNECT_HANDLER callback](nc-ndischimney-w-tcp-offload-disconnect-handler.md) | The MiniportTcpOffloadDisconnect function closes the send half of an offloaded TCP connection. |
| [W_TCP_OFFLOAD_FORWARD_HANDLER callback](nc-ndischimney-w-tcp-offload-forward-handler.md) | NDIS calls the MiniportTcpOffloadForward function to forward unacknowledged received TCP segments to an offload target. |
| [W_TCP_OFFLOAD_RECEIVE_HANDLER callback](nc-ndischimney-w-tcp-offload-receive-handler.md) | NDIS calls the MiniportTcpOffloadReceive function to post receive requests (receive buffers) on an offloaded TCP connection. |
| [W_TCP_OFFLOAD_RECEIVE_RETURN_HANDLER callback](nc-ndischimney-w-tcp-offload-receive-return-handler.md) | NDIS calls the MiniportTcpOffloadReceiveReturn function to return ownership of NET_BUFFER_LIST and associated structures to an offload target. |
| [W_TCP_OFFLOAD_SEND_HANDLER callback](nc-ndischimney-w-tcp-offload-send-handler.md) | NDIS calls the MiniportTcpOffloadSend function to transmit data on an offloaded TCP connection. |
| [W_TERMINATE_OFFLOAD_HANDLER callback](nc-ndischimney-w-terminate-offload-handler.md) | The MiniportTerminateOffload function terminates the offload of one or more state objects. |
| [W_UPDATE_OFFLOAD_HANDLER callback](nc-ndischimney-w-update-offload-handler.md) | The MiniportUpdateOffload function updates previously offloaded TCP chimney state objects. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [IP_OFFLOAD_STATS structure](ns-ndischimney--ip-offload-stats.md) | The IP_OFFLOAD_STATS structure contains statistics that an offload target supplies in response to a query of OID_IP4_OFFLOAD_STATS or OID_IP6_OFFLOAD_STATS. |
| [NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS structure](ns-ndischimney--ndis-client-chimney-offload-generic-characteristics.md) | The NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS structure specifies a protocol driver's generic chimney offload entry points. |
| [NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure](ns-ndischimney--ndis-client-chimney-offload-tcp-characteristics.md) | The NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure specifies a protocol or intermediate driver's TCP chimney offload-specific entry points. |
| [NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure](ns-ndischimney--ndis-miniport-offload-block-list.md) | The NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure is the basic building block of a TCP chimney offload state tree. An offload state tree can contain one or more NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structures. |
| [NDIS_OFFLOAD_HANDLE structure](ns-ndischimney--ndis-offload-handle.md) | The NDIS_OFFLOAD_HANDLE structure represents a driver's context for an offloaded state object. |
| [NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure](ns-ndischimney--ndis-protocol-offload-block-list.md) | The NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure. |
| [NDIS_PROVIDER_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS structure](ns-ndischimney--ndis-provider-chimney-offload-generic-characteristics.md) | The NDIS_PROVIDER_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS structure specifies the generic chimney offload miniport entry points of an offload target or intermediate driver. |
| [NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure](ns-ndischimney--ndis-provider-chimney-offload-tcp-characteristics.md) | The NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS structure specifies an offload target's TCP chimney offload-specific entry points. |
| [NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS structure](ns-ndischimney--ndis-tcp-connection-offload-parameters.md) | The NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS structure provides TCP chimney offload information in the OID_TCP_CONNECTION_OFFLOAD_PARAMETERS OIDs |
| [NDIS_TCP_OFFLOAD_EVENT_HANDLERS structure](ns-ndischimney--ndis-tcp-offload-event-handlers.md) | The NDIS_TCP_OFFLOAD_EVENT_HANDLERS structure contains the entry points for the NDIS functions for the TCP chimney. |
| [NEIGHBOR_OFFLOAD_STATE_CACHED structure](ns-ndischimney--neighbor-offload-state-cached.md) | The NEIGHBOR_OFFLOAD_STATE_CACHED structure contains the cached variables of a neighbor state object. |
| [NEIGHBOR_OFFLOAD_STATE_CONST structure](ns-ndischimney--neighbor-offload-state-const.md) | The NEIGHBOR_OFFLOAD_STATE_CONST structure contains the constant variables of a neighbor state object. |
| [NEIGHBOR_OFFLOAD_STATE_DELEGATED structure](ns-ndischimney--neighbor-offload-state-delegated.md) | The NEIGHBOR_OFFLOAD_STATE_DELGATED structure contains the delegated variable of a neighbor state object. |
| [OFFLOAD_STATE_HEADER structure](ns-ndischimney--offload-state-header.md) | The OFFLOAD_STATE_HEADER structure serves as a header in an offload state structure. |
| [PATH_OFFLOAD_STATE_CACHED structure](ns-ndischimney--path-offload-state-cached.md) | The PATH_OFFLOAD_STATE_CACHED structure contains the cached variable of a path state object. |
| [PATH_OFFLOAD_STATE_CONST structure](ns-ndischimney--path-offload-state-const.md) | The PATH_OFFLOAD_STATE_CONST structure contains the constant variables of a path state object. |
| [PATH_OFFLOAD_STATE_DELEGATED structure](ns-ndischimney--path-offload-state-delegated.md) | The PATH_OFFLOAD_STATE_DELEGATED structure contains the delegated variables of a path state object. |
| [TCP_OFFLOAD_STATE_CACHED structure](ns-ndischimney--tcp-offload-state-cached.md) | The TCP_OFFLOAD_STATE_CACHED structure contains the cached variables of a TCP connection state object. |
| [TCP_OFFLOAD_STATE_CONST structure](ns-ndischimney--tcp-offload-state-const.md) | The TCP_OFFLOAD_STATE_CONST structure contains the constant variables of a TCP connection state object. |
| [TCP_OFFLOAD_STATE_DELEGATED structure](ns-ndischimney--tcp-offload-state-delegated.md) | The TCP_OFFLOAD_STATE_DELEGATED structure contains the delegated variables of a TCP connection state object. |
| [TCP_OFFLOAD_STATS structure](ns-ndischimney--tcp-offload-stats.md) | The TCP_OFFLOAD_STATS structure contains statistics that an offload target supplies in response to a query of OID_TCP4_OFFLOAD_STATS or OID_TCP6_OFFLOAD_STATS. |
