# Ndkpi.h header


This header is used by Networking drivers for Windows Vista and later. For more information, see
- [Networking drivers for Windows Vista and later](../_netvista/index.md)

Ndkpi.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [NDK_FN_ACCEPT callback](nc-ndkpi-ndk-fn-accept.md) | The NdkAccept (NDK_FN_ACCEPT) function accepts an incoming connection request over a listener object. |
| [NDK_FN_ARM_CQ callback](nc-ndkpi-ndk-fn-arm-cq.md) | The NdkArmCq (NDK_FN_ARM_CQ) function arms an NDK completion queue (CQ) notification. |
| [NDK_FN_BIND callback](nc-ndkpi-ndk-fn-bind.md) | The NdkBind (NDK_FN_BIND) function binds a memory window to a specific sub-region of a memory region (MR). |
| [NDK_FN_BUILD_LAM callback](nc-ndkpi-ndk-fn-build-lam.md) | The NdkBuildLam (NDK_FN_BUILD_LAM) function gets an adapter logical address mapping (LAM) from the NDK provider for a virtually contiguous memory region. |
| [NDK_FN_CLOSE_COMPLETION callback](nc-ndkpi-ndk-fn-close-completion.md) | The NdkCloseCompletion (NDK_FN_CLOSE_COMPLETION) function is an asynchronous completion function for closing NDK objects. |
| [NDK_FN_CLOSE_OBJECT callback](nc-ndkpi-ndk-fn-close-object.md) | The NdkCloseObject (NDK_FN_CLOSE_OBJECT) function initiates a close request for an NDK object. |
| [NDK_FN_COMPLETE_CONNECT callback](nc-ndkpi-ndk-fn-complete-connect.md) | The NdkCompleteConnect (NDK_FN_COMPLETE_CONNECT) function completes an asynchronous connection request. |
| [NDK_FN_CONNECT callback](nc-ndkpi-ndk-fn-connect.md) | The NdkConnect (NDK_FN_CONNECT) function initiates an NDK connect request. |
| [NDK_FN_CONNECT_EVENT_CALLBACK callback](nc-ndkpi-ndk-fn-connect-event-callback.md) | The NdkConnectEventCallback (NDK_FN_CONNECT_EVENT_CALLBACK) function is called by an NDK provider to notify a consumer about an incoming connection request. |
| [NDK_FN_CONNECT_WITH_SHARED_ENDPOINT callback](nc-ndkpi-ndk-fn-connect-with-shared-endpoint.md) | The NdkConnectWithSharedEndpoint (NDK_FN_CONNECT_WITH_SHARED_ENDPOINT) function initiates an NDK connect request from a shared local address to a remote address. |
| [NDK_FN_CONTROL_CONNECT_EVENTS callback](nc-ndkpi-ndk-fn-control-connect-events.md) | The NdkControlConnectEvents (NDK_FN_CONTROL_CONNECT_EVENTS) function pauses and restarts NDK connect event callback functions. |
| [NDK_FN_CONTROL_CQ_INTERRUPT_MODERATION callback](nc-ndkpi-ndk-fn-control-cq-interrupt-moderation.md) | The NdkControlCqInterruptModeration (NDK_FN_CONTROL_CQ_INTERRUPT_MODERATION) function controls interrupt moderation on an NDK completion queue (CQ). |
| [NDK_FN_CQ_NOTIFICATION_CALLBACK callback](nc-ndkpi-ndk-fn-cq-notification-callback.md) | The NdkCqNotificationCallback (NDK_FN_CQ_NOTIFICATION_CALLBACK) function is called by the NDK provider to notify the consumer about a completion queue (CQ) event. |
| [NDK_FN_CREATE_COMPLETION callback](nc-ndkpi-ndk-fn-create-completion.md) | The NdkCreateCompletion (NDK_FN_CREATE_COMPLETION) function completes the creation of an NDK object. |
| [NDK_FN_CREATE_CONNECTOR callback](nc-ndkpi-ndk-fn-create-connector.md) | The NdkCreateConnector (NDK_FN_CREATE_CONNECTOR) function creates an NDK connector object. |
| [NDK_FN_CREATE_CQ callback](nc-ndkpi-ndk-fn-create-cq.md) | The NdkCreateCq (NDK_FN_CREATE_CQ) function creates an NDK completion queue (CQ) object. |
| [NDK_FN_CREATE_LISTENER callback](nc-ndkpi-ndk-fn-create-listener.md) | The NdkCreateListener (NDK_FN_CREATE_LISTENER) function creates an NDK listener object. |
| [NDK_FN_CREATE_MR callback](nc-ndkpi-ndk-fn-create-mr.md) | The NdkCreateMr (NDK_FN_CREATE_MR) function creates an NDK memory region (MR) object. |
| [NDK_FN_CREATE_MW callback](nc-ndkpi-ndk-fn-create-mw.md) | The NdkCreateMw (NDK_FN_CREATE_MW) function creates an NDK memory window (MW) object. |
| [NDK_FN_CREATE_PD callback](nc-ndkpi-ndk-fn-create-pd.md) | The NdkCreatePd (NDK_FN_CREATE_PD) function creates an NDK protection domain (PD) object. |
| [NDK_FN_CREATE_QP callback](nc-ndkpi-ndk-fn-create-qp.md) | The NdkCreateQp (NDK_FN_CREATE_QP) function creates an NDK queue pair (QP) object. |
| [NDK_FN_CREATE_QP_WITH_SRQ callback](nc-ndkpi-ndk-fn-create-qp-with-srq.md) | The NdkCreateQpWithSrq (NDK_FN_CREATE_QP_WITH_SRQ) function create an NDK queue pair (QP) object with an NDK shared receive queue (SRQ) object. |
| [NDK_FN_CREATE_SHARED_ENDPOINT callback](nc-ndkpi-ndk-fn-create-shared-endpoint.md) | The NdkCreateSharedEndpoint (NDK_FN_CREATE_SHARED_ENDPOINT) function creates an NDK shared endpoint. |
| [NDK_FN_CREATE_SRQ callback](nc-ndkpi-ndk-fn-create-srq.md) | The NdkCreateSrq (NDK_FN_CREATE_SRQ) function creates an NDK shared receive queue (SRQ) object. |
| [NDK_FN_DEREGISTER_MR callback](nc-ndkpi-ndk-fn-deregister-mr.md) | The NdkDeregisterMr (NDK_FN_DEREGISTER_MR) function deregisters a memory region that was previously registered with the NdkRegisterMr (NDK_FN_REGISTER_MR) function. |
| [NDK_FN_DISCONNECT callback](nc-ndkpi-ndk-fn-disconnect.md) | The NdkDisconnect (NDK_FN_DISCONNECT) function starts a disconnect on an NDK connection. |
| [NDK_FN_DISCONNECT_EVENT_CALLBACK callback](nc-ndkpi-ndk-fn-disconnect-event-callback.md) | The NdkDisconnectEventCallback (NDK_FN_DISCONNECT_EVENT_CALLBACK) function is called by the NDK provider once when the peer disconnects. |
| [NDK_FN_FAST_REGISTER callback](nc-ndkpi-ndk-fn-fast-register.md) | The NdkFastRegister (NDK_FN_FAST_REGISTER) function fast-registers an array of adapter logical pages over an existing memory region. |
| [NDK_FN_FLUSH callback](nc-ndkpi-ndk-fn-flush.md) | The NdkFlush (NDK_FN_FLUSH) function initiates cancelling of the receive and the initiator queue requests that are currently pending on an NDK queue pair (QP) object. |
| [NDK_FN_GET_CONNECTION_DATA callback](nc-ndkpi-ndk-fn-get-connection-data.md) | The NdkGetConnectionData (NDK_FN_GET_CONNECTION_DATA) function gets read limit values and the private data sent by the peer. |
| [NDK_FN_GET_CQ_RESULTS callback](nc-ndkpi-ndk-fn-get-cq-results.md) | The NdkGetCqResults (NDK_FN_GET_CQ_RESULTS) function removes completions from an NDK completion queue (CQ) object. |
| [NDK_FN_GET_CQ_RESULTS_EX callback](nc-ndkpi-ndk-fn-get-cq-results-ex.md) | The NdkGetCqResultsEx (NDK_FN_GET_CQ_RESULTS_EX) function removes completions from an NDK completion queue (CQ) object. |
| [NDK_FN_GET_LISTENER_LOCAL_ADDRESS callback](nc-ndkpi-ndk-fn-get-listener-local-address.md) | The NdkGetListenerLocalAddress (NDK_FN_GET_LISTENER_LOCAL_ADDRESS) function returns the local address for an NDK listener. |
| [NDK_FN_GET_LOCAL_ADDRESS callback](nc-ndkpi-ndk-fn-get-local-address.md) | The NdkGetLocalAddress (NDK_FN_GET_LOCAL_ADDRESS) function returns the local address for an NDK connection. |
| [NDK_FN_GET_LOCAL_TOKEN_FROM_MR callback](nc-ndkpi-ndk-fn-get-local-token-from-mr.md) | The NdkGetLocalTokenFromMr (NDK_FN_GET_LOCAL_TOKEN_FROM_MR) function gets a memory token from a local NDK memory region (MR). |
| [NDK_FN_GET_PEER_ADDRESS callback](nc-ndkpi-ndk-fn-get-peer-address.md) | The NdkGetPeerAddress (NDK_FN_GET_PEER_ADDRESS) function returns the remote address for an NDK connection. |
| [NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN callback](nc-ndkpi-ndk-fn-get-privileged-memory-region-token.md) | The NdkGetPrivilegedMemoryRegionToken (NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN) function gets an NDK privileged memory region token. |
| [NDK_FN_GET_REMOTE_TOKEN_FROM_MR callback](nc-ndkpi-ndk-fn-get-remote-token-from-mr.md) | The NdkGetRemoteTokenFromMr (NDK_FN_GET_REMOTE_TOKEN_FROM_MR) function gets a memory token from a remote NDK memory region (MR). |
| [NDK_FN_GET_REMOTE_TOKEN_FROM_MW callback](nc-ndkpi-ndk-fn-get-remote-token-from-mw.md) | The NdkGetRemoteTokenFromMw (NDK_FN_GET_REMOTE_TOKEN_FROM_MW) function gets a memory token from a remote NDK memory window (MW). |
| [NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS callback](nc-ndkpi-ndk-fn-get-shared-endpoint-local-address.md) | The NdkGetSharedEndpointLocalAddress (NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS) function returns the local address for an NDK shared endpoint. |
| [NDK_FN_INITIALIZE_FAST_REGISTER_MR callback](nc-ndkpi-ndk-fn-initialize-fast-register-mr.md) | The NdkInitializeFastRegisterMr (NDK_FN_INITIALIZE_FAST_REGISTER_MR) function initializes an NDK memory region (MR) for fast registration. |
| [NDK_FN_INVALIDATE callback](nc-ndkpi-ndk-fn-invalidate.md) | The NdkInvalidate (NDK_FN_INVALIDATE) function Invalidates a fast-register NDK memory region (MR) or memory window (MW). |
| [NDK_FN_LISTEN callback](nc-ndkpi-ndk-fn-listen.md) | The NdkListen (NDK_FN_LISTEN) function puts an NDK listener object into listening mode. |
| [NDK_FN_MODIFY_SRQ callback](nc-ndkpi-ndk-fn-modify-srq.md) | The NdkModifySrq (NDK_FN_MODIFY_SRQ) function modifies the size and notification threshold of an NDK shared receive queue (SRQ). |
| [NDK_FN_QUERY_ADAPTER_INFO callback](nc-ndkpi-ndk-fn-query-adapter-info.md) | The NdkQueryAdapterInfo (NDK_FN_QUERY_ADAPTER_INFO) function retrieves information about limits and capabilities of an NDK adapter. |
| [NDK_FN_QUERY_EXTENSION_INTERFACE callback](nc-ndkpi-ndk-fn-query-extension-interface.md) | The NdkQqueryExtensionInterface (NDK_FN_QUERY_EXTENSION_INTERFACE) function gets information about an NDK extension interface. |
| [NDK_FN_READ callback](nc-ndkpi-ndk-fn-read.md) | The NdkRead (NDK_FN_READ) function posts a read request on an NDK queue pair (QP). |
| [NDK_FN_RECEIVE callback](nc-ndkpi-ndk-fn-receive.md) | The NdkReceive (NDK_FN_RECEIVE) function posts a receive request on an NDK queue pair (QP). |
| [NDK_FN_REGISTER_MR callback](nc-ndkpi-ndk-fn-register-mr.md) | The NdkRegisterMr (NDK_FN_REGISTER_MR) function registers a virtually contiguous memory region with an NDK adapter. |
| [NDK_FN_REJECT callback](nc-ndkpi-ndk-fn-reject.md) | The NdkReject (NDK_FN_REJECT) function rejects an incoming NDK connection request. |
| [NDK_FN_RELEASE_LAM callback](nc-ndkpi-ndk-fn-release-lam.md) | The NdkReleaseLam (NDK_FN_RELEASE_LAM) function releases an NDK adapter logical address mapping (LAM). |
| [NDK_FN_REQUEST_COMPLETION callback](nc-ndkpi-ndk-fn-request-completion.md) | The NdkRequestCompletion (NDK_FN_REQUEST_COMPLETION) function completes a pending NDK request. |
| [NDK_FN_RESIZE_CQ callback](nc-ndkpi-ndk-fn-resize-cq.md) | The NdkResizeCq (NDK_FN_RESIZE_CQ) function changes the size of an NDK completion queue (CQ). |
| [NDK_FN_SEND callback](nc-ndkpi-ndk-fn-send.md) | The NdkSend (NDK_FN_SEND) function posts a send request on an NDK queue pair (QP). |
| [NDK_FN_SEND_AND_INVALIDATE callback](nc-ndkpi-ndk-fn-send-and-invalidate.md) | The NdkSendAndInvalidate (NDK_FN_SEND_AND_INVALIDATE) function posts a send request on an NDK queue pair (QP) and supplies a token to be invalidated at the remote peer upon receive completion. |
| [NDK_FN_SRQ_NOTIFICATION_CALLBACK callback](nc-ndkpi-ndk-fn-srq-notification-callback.md) | The NdkSrqNotificationCallback (NDK_FN_SRQ_NOTIFICATION_CALLBACK) function provides NDK shared receive queue (SRQ) notifications from an NDK provider. |
| [NDK_FN_SRQ_RECEIVE callback](nc-ndkpi-ndk-fn-srq-receive.md) | The NdkSrqReceive (NDK_FN_SRQ_RECEIVE) function posts a receive request on an NDK shared receive queue (SRQ). |
| [NDK_FN_WRITE callback](nc-ndkpi-ndk-fn-write.md) | The NdkWrite (NDK_FN_WRITE) function posts a write request on an NDK queue pair (QP). |

## Structures

| Title   | Description   |
| ---- |:---- |
| [NDK_ADAPTER structure](ns-ndkpi--ndk-adapter.md) | The NDK_ADAPTER structure specifies the attributes of an NDK adapter object. |
| [NDK_ADAPTER structure](ns-ndkpi--ndk-adapter~r1.md) | The NDK_ADAPTER structure specifies the attributes of an NDK adapter object. |
| [NDK_ADAPTER_DISPATCH structure](ns-ndkpi--ndk-adapter-dispatch.md) | The NDK_ADAPTER_DISPATCH structure specifies dispatch function entry points for the NDK adapter object. |
| [NDK_CONNECTOR structure](ns-ndkpi--ndk-connector.md) | The NDK_CONNECTOR structure specifies the attributes of an NDK connector object. |
| [NDK_CONNECTOR structure](ns-ndkpi--ndk-connector~r1.md) | The NDK_CONNECTOR structure specifies the attributes of an NDK connector object. |
| [NDK_CONNECTOR_DISPATCH structure](ns-ndkpi--ndk-connector-dispatch.md) | The NDK_CONNECTOR_DISPATCH structure specifies dispatch function entry points for the NDK connector object. |
| [NDK_CQ structure](ns-ndkpi--ndk-cq.md) | The NDK_CQ structure specifies the attributes of an NDK completion queue (CQ) object. |
| [NDK_CQ structure](ns-ndkpi--ndk-cq~r1.md) | The NDK_CQ structure specifies the attributes of an NDK completion queue (CQ) object. |
| [NDK_CQ_DISPATCH structure](ns-ndkpi--ndk-cq-dispatch.md) | The NDK_CQ_DISPATCH structure specifies dispatch function entry points for the NDK completion queue (CQ) object. |
| [NDK_EXTENSION_INTERFACE structure](ns-ndkpi--ndk-extension-interface.md) | The NDK_EXTENSION_INTERFACE structure specifies dispatch function entry points for an NDK extension interface. |
| [NDK_LISTENER structure](ns-ndkpi--ndk-listener.md) | The NDK_LISTENER structure specifies the attributes of an NDK listener object. |
| [NDK_LISTENER structure](ns-ndkpi--ndk-listener~r1.md) | The NDK_LISTENER structure specifies the attributes of an NDK listener object. |
| [NDK_LISTENER_DISPATCH structure](ns-ndkpi--ndk-listener-dispatch.md) | The NDK_LISTENER_DISPATCH structure specifies dispatch function entry points for the NDK listener object. |
| [NDK_LOGICAL_ADDRESS_MAPPING structure](ns-ndkpi--ndk-logical-address-mapping.md) | The NDK_LOGICAL_ADDRESS_MAPPING structure contains an array of adapter logical addresses. |
| [NDK_MR structure](ns-ndkpi--ndk-mr.md) | The NDK_MR structure specifies the attributes of an NDK memory region (MR) object. |
| [NDK_MR structure](ns-ndkpi--ndk-mr~r1.md) | The NDK_MR structure specifies the attributes of an NDK memory region (MR) object. |
| [NDK_MR_DISPATCH structure](ns-ndkpi--ndk-mr-dispatch.md) | The NDK_MR_DISPATCH structure specifies dispatch function entry points for the NDK memory region (MR) object. |
| [NDK_MW structure](ns-ndkpi--ndk-mw.md) | The NDK_MW structure specifies the attributes of an NDK memory window (MW) object. |
| [NDK_MW structure](ns-ndkpi--ndk-mw~r1.md) | The NDK_MW structure specifies the attributes of an NDK memory window (MW) object. |
| [NDK_MW_DISPATCH structure](ns-ndkpi--ndk-mw-dispatch.md) | The NDK_MW_DISPATCH structure specifies dispatch function entry points for the NDK memory window (MW) object. |
| [NDK_OBJECT_HEADER structure](ns-ndkpi--ndk-object-header.md) | The NDK_OBJECT_HEADER structure specifies the object version, type, and other information. It is used in the Header member of every NDK object. |
| [NDK_OBJECT_HEADER_RESERVED_BLOCK structure](ns-ndkpi--ndk-object-header-reserved-block.md) | The NDK_OBJECT_HEADER_RESERVED_BLOCK structure specifies reserved information in an NDK object. |
| [NDK_PD structure](ns-ndkpi--ndk-pd.md) | The NDK_PD structure specifies the attributes of an NDK protection domain (PD) object. |
| [NDK_PD structure](ns-ndkpi--ndk-pd~r1.md) | The NDK_PD structure specifies the attributes of an NDK protection domain (PD) object. |
| [NDK_PD_DISPATCH structure](ns-ndkpi--ndk-pd-dispatch.md) | The NDK_PD_DISPATCH structure specifies dispatch function entry points for the NDK protection domain (PD) object. |
| [NDK_QP structure](ns-ndkpi--ndk-qp.md) | The NDK_QP structure specifies the attributes of an NDK queue pair (QP) object. |
| [NDK_QP structure](ns-ndkpi--ndk-qp~r1.md) | The NDK_QP structure specifies the attributes of an NDK queue pair (QP) object. |
| [NDK_QP_DISPATCH structure](ns-ndkpi--ndk-qp-dispatch.md) | The NDK_QP_DISPATCH structure specifies dispatch function entry points for the NDK queue pair (QP) object. |
| [NDK_RESULT structure](ns-ndkpi--ndk-result.md) | The NDK_RESULT structure returns the results for an NDK request operation. |
| [NDK_RESULT_EX structure](ns-ndkpi--ndk-result-ex.md) | The NDK_RESULT_EX structure returns the results for an NDK request operation. It is identical to the NDK_RESULT structure, except that it has additional Type and TypeSpecificCompletionOutput members. |
| [NDK_SGE structure](ns-ndkpi--ndk-sge.md) | The NDK_SGE structure specifies the local buffers for NDK work requests. |
| [NDK_SHARED_ENDPOINT structure](ns-ndkpi--ndk-shared-endpoint.md) | The NDK_SHARED_ENDPOINT structure specifies the attributes of an NDK shared endpoint object. |
| [NDK_SHARED_ENDPOINT structure](ns-ndkpi--ndk-shared-endpoint~r1.md) | The NDK_SHARED_ENDPOINT structure specifies the attributes of an NDK shared endpoint object. |
| [NDK_SHARED_ENDPOINT_DISPATCH structure](ns-ndkpi--ndk-shared-endpoint-dispatch.md) | The NDK_SHARED_ENDPOINT_DISPATCH structure specifies dispatch function entry points for the NDK shared endpoint object. |
| [NDK_SRQ structure](ns-ndkpi--ndk-srq.md) | The NDK_SRQ structure specifies the attributes of an NDK shared receive queue (SRQ) object. |
| [NDK_SRQ structure](ns-ndkpi--ndk-srq~r1.md) | The NDK_SRQ structure specifies the attributes of an NDK shared receive queue (SRQ) object. |
| [NDK_SRQ_DISPATCH structure](ns-ndkpi--ndk-srq-dispatch.md) | The NDK_SRQ_DISPATCH structure specifies dispatch function entry points for the NDK shared receive queue (SRQ) object. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [NDK_OBJECT_TYPE enumeration](ne-ndkpi--ndk-object-type.md) | The NDK_OBJECT_TYPE enumeration defines types of Network Direct Kernel (NDK) objects. |
| [NDK_OPERATION_TYPE enumeration](ne-ndkpi--ndk-operation-type.md) | The NDK_OPERATION_TYPE enumeration defines types of NDK operations. Its enumeration values are used in the Type member of the NDK_RESULT_EX structure. |
