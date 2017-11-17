# Declarations in the fwpsk header
This header Fwpsk contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [FWPS_CALLOUT_NOTIFY_FN1 callback](nc-fwpsk-fwps-callout-notify-fn1.md) | The filter engine calls a callout's notifyFn1 callout function to notify the callout driver about events that are associated with the callout.Note  notifyFn1 is the specific version of notifyFn used in Windows 7 and later. |
| [FWPS_NET_BUFFER_LIST_NOTIFY_FN1 callback](nc-fwpsk-fwps-net-buffer-list-notify-fn1.md) | The filter engine calls the FWPS_NET_BUFFER_LIST_NOTIFY_FN1 callout function to notify the callout driver about events that are associated with packets tagged by the callout.Note   FWPS_NET_BUFFER_LIST_NOTIFY_FN1 is the specific version of FWPS_NET_BUFFER_LIST_NOTIFY_FN used in Windows 8 and later. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. For Windows 7, FWPS_NET_BUFFER_LIST_NOTIFY_FN0 is available. |
| [FWPS_INJECT_COMPLETE0 callback](nc-fwpsk-fwps-inject-complete0.md) | The filter engine calls a callout's completionFn callout function whenever packet data, described by the netBufferList parameter in one of the packet injection functions, has been injected into the network stack. |
| [FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0 callback](nc-fwpsk-fwps-vswitch-runtime-state-save-callback0.md) | The filter engine calls the vSwitchRuntimeStateSaveNotifyFn (FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0) callout function to notify a callout driver about virtual switch run-time state save events.Note  FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0 is a specific version of FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. |
| [FWPS_CALLOUT_FLOW_DELETE_NOTIFY_FN0 callback](nc-fwpsk-fwps-callout-flow-delete-notify-fn0.md) | The filter engine calls a callout's flowDeleteFn callout function to notify the callout that a data flow that is being processed by the callout is being terminated. |
| [FWPS_CALLOUT_NOTIFY_FN2 callback](nc-fwpsk-fwps-callout-notify-fn2.md) | The filter engine calls a callout's notifyFn2 callout function to notify the callout driver about events that are associated with the callout.Note  notifyFn2 is the specific version of notifyFn used in Windows 8 and later. |
| [FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0 callback](nc-fwpsk-fwps-vswitch-runtime-state-restore-callback0.md) | The filter engine calls the vSwitchRuntimeStateRestoreNotifyFn (FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0) callout function to notify a callout driver about virtual switch run-time state restore events.Note  FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0 is a specific version of FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. |
| [FWPS_VSWITCH_POLICY_EVENT_CALLBACK0 callback](nc-fwpsk-fwps-vswitch-policy-event-callback0.md) | The filter engine calls the vSwitchPolicyEventNotifyFn (FWPS_VSWITCH_POLICY_EVENT_CALLBACK0) callout function to notify the callout driver about virtual switch policy events.Note  FWPS_VSWITCH_POLICY_EVENT_CALLBACK0 is a specific version of FWPS_VSWITCH_POLICY_EVENT_CALLBACK. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. |
| [FWPS_CALLOUT_NOTIFY_FN3 callback function](nc-fwpsk-fwps-callout-notify-fn3.md) | TBD |
| [FWPS_VSWITCH_PORT_EVENT_CALLBACK0 callback](nc-fwpsk-fwps-vswitch-port-event-callback0.md) | The filter engine calls the vSwitchPortEventNotifyFn (FWPS_VSWITCH_PORT_EVENT_CALLBACK0) callout function to notify the callout driver about events that are associated a virtual switch (vSwitch) port.Note  FWPS_VSWITCH_PORT_EVENT_CALLBACK0 is a specific version of FWPS_VSWITCH_PORT_EVENT_CALLBACK. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. |
| [FWPS_CALLOUT_BOOTTIME_CALLOUT_DELETE_NOTIFY_FN0 callback function](nc-fwpsk-fwps-callout-boottime-callout-delete-notify-fn0.md) | TBD |
| [FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK0 callback](nc-fwpsk-fwps-vswitch-filter-engine-reorder-callback0.md) | The filter engine calls the vSwitchFilterEngineReorderNotifyRn (FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK0) callout function to notify the callout driver about events that are associated the virtual switch filter engine reordering.Note  FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK0 is a specific version of FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. |
| [FWPS_CALLOUT_NOTIFY_FN0 callback](nc-fwpsk-fwps-callout-notify-fn0.md) | The filter engine calls a callout's notifyFn0 callout function to notify the callout driver about events that are associated with the callout.Note  notifyFn0 is the specific version of notifyFn used in Windows Vista and later. |
| [FWPS_VSWITCH_INTERFACE_EVENT_CALLBACK0 callback](nc-fwpsk-fwps-vswitch-interface-event-callback0.md) | The filter engine calls the vSwitchInterfaceEventNotifyFn (FWPS_VSWITCH_INTERFACE_EVENT_CALLBACK0) callout function to notify the callout driver about events that are associated the virtual switch interface.Note  FWPS_VSWITCH_INTERFACE_EVENT_CALLBACK0 is a specific version of FWPS_VSWITCH_INTERFACE_EVENT_CALLBACK. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. |
| [FWPS_CALLOUT_CLASSIFY_FN1 callback](nc-fwpsk-fwps-callout-classify-fn1.md) | The filter engine calls a callout's classifyFn1 callout function whenever there is data to be processed by the callout.Note  classifyFn1 is the specific version of classifyFn used in Windows 7 and later. |
| [FWPS_CALLOUT_CLASSIFY_FN0 callback](nc-fwpsk-fwps-callout-classify-fn0.md) | The filter engine calls a callout's classifyFn0 callout function whenever there is data to be processed by the callout.Note  classifyFn0 is the specific version of classifyFn used in Windows Vista and later. |
| [FWPS_CALLOUT_CLASSIFY_FN2 callback](nc-fwpsk-fwps-callout-classify-fn2.md) | The filter engine calls a callout's classifyFn2 callout function whenever there is data to be processed by the callout.Note  classifyFn2 is the specific version of classifyFn used in Windows 8 and later. |
| [FWPS_NET_BUFFER_LIST_NOTIFY_FN0 callback](nc-fwpsk-fwps-net-buffer-list-notify-fn0.md) | The filter engine calls the FWPS_NET_BUFFER_LIST_NOTIFY_FN0 callout function to notify the callout driver about events that are associated with packets tagged by the callout.Note  FWPS_NET_BUFFER_LIST_NOTIFY_FN0 is the specific version of FWPS_NET_BUFFER_LIST_NOTIFY_FN used in Windows 7 and later. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. For Windows 8, FWPS_NET_BUFFER_LIST_NOTIFY_FN1 is available. |
| [FWPS_CALLOUT_CLASSIFY_FN3 callback function](nc-fwpsk-fwps-callout-classify-fn3.md) | TBD |
| [FWPS_VSWITCH_LIFETIME_EVENT_CALLBACK0 callback](nc-fwpsk-fwps-vswitch-lifetime-event-callback0.md) | The filter engine calls the vSwitchLifetimeNotifyFn (FWPS_VSWITCH_LIFETIME_EVENT_CALLBACK0) callout function to notify the callout driver about create and delete events for a virtual switch.Note  FWPS_VSWITCH_LIFETIME_EVENT_CALLBACK0 is a specific version of FWPS_VSWITCH_LIFETIME_EVENT_CALLBACK. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [FWPS_FIELDS_ALE_RESOURCE_ASSIGNMENT_V6_ enumeration](ne-fwpsk-fwps-fields-ale-resource-assignment-v6-.md) | TBD |
| [FWPS_FIELDS_INBOUND_MAC_FRAME_ETHERNET_ enumeration](ne-fwpsk-fwps-fields-inbound-mac-frame-ethernet-.md) | TBD |
| [FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V6_ enumeration](ne-fwpsk-fwps-fields-egress-vswitch-transport-v6-.md) | TBD |
| [FWPS_FIELDS_OUTBOUND_TRANSPORT_V4_ enumeration](ne-fwpsk-fwps-fields-outbound-transport-v4-.md) | TBD |
| [FWPS_FIELDS_EGRESS_VSWITCH_ETHERNET_ enumeration](ne-fwpsk-fwps-fields-egress-vswitch-ethernet-.md) | TBD |
| [FWPS_FIELDS_IPSEC_KM_DEMUX_V6_ enumeration](ne-fwpsk-fwps-fields-ipsec-km-demux-v6-.md) | TBD |
| [FWPS_FIELDS_RPC_PROXY_IF_ enumeration](ne-fwpsk-fwps-fields-rpc-proxy-if-.md) | TBD |
| [FWPS_FIELDS_ALE_CONNECT_REDIRECT_V4_ enumeration](ne-fwpsk-fwps-fields-ale-connect-redirect-v4-.md) | TBD |
| [FWPS_FIELDS_ALE_PRECLASSIFY_IP_LOCAL_PORT_V6_ enumeration](ne-fwpsk-fwps-fields-ale-preclassify-ip-local-port-v6-.md) | TBD |
| [FWPS_STREAM_ACTION_TYPE_ enumeration](ne-fwpsk-fwps-stream-action-type-.md) | TBD |
| [FWPS_FIELDS_DATAGRAM_DATA_V4_ enumeration](ne-fwpsk-fwps-fields-datagram-data-v4-.md) | TBD |
| [FWPS_FIELDS_ALE_PRECLASSIFY_IP_LOCAL_PORT_V4_ enumeration](ne-fwpsk-fwps-fields-ale-preclassify-ip-local-port-v4-.md) | TBD |
| [FWPS_FIELDS_KM_AUTHORIZATION_ enumeration](ne-fwpsk-fwps-fields-km-authorization-.md) | TBD |
| [FWPS_FIELDS_DATAGRAM_DATA_V6_ enumeration](ne-fwpsk-fwps-fields-datagram-data-v6-.md) | TBD |
| [FWPS_FIELDS_ALE_PRECLASSIFY_IP_REMOTE_PORT_V4_ enumeration](ne-fwpsk-fwps-fields-ale-preclassify-ip-remote-port-v4-.md) | TBD |
| [FWPS_FIELDS_INBOUND_MAC_FRAME_NATIVE_FAST_ enumeration](ne-fwpsk-fwps-fields-inbound-mac-frame-native-fast-.md) | TBD |
| [FWPS_FIELDS_INBOUND_ICMP_ERROR_V6_ enumeration](ne-fwpsk-fwps-fields-inbound-icmp-error-v6-.md) | TBD |
| [FWPS_FIELDS_OUTBOUND_IPPACKET_V4_ enumeration](ne-fwpsk-fwps-fields-outbound-ippacket-v4-.md) | TBD |
| [FWPS_FIELDS_INBOUND_IPPACKET_V4_ enumeration](ne-fwpsk-fwps-fields-inbound-ippacket-v4-.md) | TBD |
| [FWPS_FIELDS_ALE_RESOURCE_RELEASE_V4_ enumeration](ne-fwpsk-fwps-fields-ale-resource-release-v4-.md) | TBD |
| [FWPS_FIELDS_INBOUND_TRANSPORT_V4_ enumeration](ne-fwpsk-fwps-fields-inbound-transport-v4-.md) | TBD |
| [FWPS_FIELDS_OUTBOUND_MAC_FRAME_NATIVE_ enumeration](ne-fwpsk-fwps-fields-outbound-mac-frame-native-.md) | TBD |
| [FWPS_FIELDS_ALE_ENDPOINT_CLOSURE_V6_ enumeration](ne-fwpsk-fwps-fields-ale-endpoint-closure-v6-.md) | TBD |
| [FWPS_FIELDS_INGRESS_VSWITCH_TRANSPORT_V6_ enumeration](ne-fwpsk-fwps-fields-ingress-vswitch-transport-v6-.md) | TBD |
| [PINET_DISCARD_REASON enumeration](ne-fwpsk-pinet-discard-reason.md) | TBD |
| [FWPS_FIELDS_NAME_RESOLUTION_CACHE_V4_ enumeration](ne-fwpsk-fwps-fields-name-resolution-cache-v4-.md) | TBD |
| [FWPS_FIELDS_IKEEXT_V6_ enumeration](ne-fwpsk-fwps-fields-ikeext-v6-.md) | TBD |
| [FWPS_FIELDS_OUTBOUND_TRANSPORT_FAST enumeration](ne-fwpsk-fwps-fields-outbound-transport-fast.md) | TBD |
| [FWPS_FIELDS_ALE_PRECLASSIFY_IP_REMOTE_ADDRESS_V4_ enumeration](ne-fwpsk-fwps-fields-ale-preclassify-ip-remote-address-v4-.md) | TBD |
| [FWPS_FIELDS_INBOUND_TRANSPORT_FAST enumeration](ne-fwpsk-fwps-fields-inbound-transport-fast.md) | TBD |
| [PIP_DISCARD_REASON enumeration](ne-fwpsk-pip-discard-reason.md) | TBD |
| [FWPS_FIELDS_ALE_BIND_REDIRECT_V4_ enumeration](ne-fwpsk-fwps-fields-ale-bind-redirect-v4-.md) | TBD |
| [FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V4_ enumeration](ne-fwpsk-fwps-fields-egress-vswitch-transport-v4-.md) | TBD |
| [FWPS_FIELDS_STREAM_PACKET_V4_ enumeration](ne-fwpsk-fwps-fields-stream-packet-v4-.md) | TBD |
| [FWPS_FIELDS_RPC_PROXY_CONN_ enumeration](ne-fwpsk-fwps-fields-rpc-proxy-conn-.md) | TBD |
| [FWPS_FIELDS_ALE_ENDPOINT_CLOSURE_V4_ enumeration](ne-fwpsk-fwps-fields-ale-endpoint-closure-v4-.md) | TBD |
| [FWPS_FIELDS_OUTBOUND_TRANSPORT_V6_ enumeration](ne-fwpsk-fwps-fields-outbound-transport-v6-.md) | TBD |
| [FWPS_FIELDS_IPSEC_V4_ enumeration](ne-fwpsk-fwps-fields-ipsec-v4-.md) | TBD |
| [FWPS_FIELDS_RPC_EP_ADD_ enumeration](ne-fwpsk-fwps-fields-rpc-ep-add-.md) | TBD |
| [FWPS_FIELDS_INBOUND_RESERVED2_ enumeration](ne-fwpsk-fwps-fields-inbound-reserved2-.md) | TBD |
| [FWPS_FIELDS_ALE_AUTH_RECV_ACCEPT_V6_ enumeration](ne-fwpsk-fwps-fields-ale-auth-recv-accept-v6-.md) | TBD |
| [FWPS_FIELDS_INBOUND_ICMP_ERROR_V4_ enumeration](ne-fwpsk-fwps-fields-inbound-icmp-error-v4-.md) | TBD |
| [FWPS_FIELDS_ALE_RESOURCE_ASSIGNMENT_V4_ enumeration](ne-fwpsk-fwps-fields-ale-resource-assignment-v4-.md) | TBD |
| [FWPS_FIELDS_IPFORWARD_V6_ enumeration](ne-fwpsk-fwps-fields-ipforward-v6-.md) | TBD |
| [FWPS_FIELDS_STREAM_PACKET_V6_ enumeration](ne-fwpsk-fwps-fields-stream-packet-v6-.md) | TBD |
| [FWPS_FIELDS_ALE_PRECLASSIFY_IP_LOCAL_ADDRESS_V6_ enumeration](ne-fwpsk-fwps-fields-ale-preclassify-ip-local-address-v6-.md) | TBD |
| [FWPS_FIELDS_INBOUND_IPPACKET_V6_ enumeration](ne-fwpsk-fwps-fields-inbound-ippacket-v6-.md) | TBD |
| [FWPS_FIELDS_ALE_CONNECT_REDIRECT_V6_ enumeration](ne-fwpsk-fwps-fields-ale-connect-redirect-v6-.md) | TBD |
| [FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V6_ enumeration](ne-fwpsk-fwps-fields-outbound-icmp-error-v6-.md) | TBD |
| [FWPS_FIELDS_OUTBOUND_IPPACKET_V6_ enumeration](ne-fwpsk-fwps-fields-outbound-ippacket-v6-.md) | TBD |
| [FWPS_PACKET_INJECTION_STATE_ enumeration](ne-fwpsk-fwps-packet-injection-state-.md) | TBD |
| [FWPS_NET_BUFFER_LIST_EVENT_TYPE0_ enumeration](ne-fwpsk-fwps-net-buffer-list-event-type0-.md) | TBD |
| [FWPS_FIELDS_RPC_UM_ enumeration](ne-fwpsk-fwps-fields-rpc-um-.md) | TBD |
| [FWPS_FIELDS_OUTBOUND_MAC_FRAME_ETHERNET_ enumeration](ne-fwpsk-fwps-fields-outbound-mac-frame-ethernet-.md) | TBD |
| [FWPS_FIELDS_INGRESS_VSWITCH_ETHERNET_ enumeration](ne-fwpsk-fwps-fields-ingress-vswitch-ethernet-.md) | TBD |
| [FWPS_FIELDS_ALE_PRECLASSIFY_IP_REMOTE_PORT_V6_ enumeration](ne-fwpsk-fwps-fields-ale-preclassify-ip-remote-port-v6-.md) | TBD |
| [FWPS_FIELDS_INBOUND_TRANSPORT_V6_ enumeration](ne-fwpsk-fwps-fields-inbound-transport-v6-.md) | TBD |
| [FWPS_FIELDS_IPSEC_V6_ enumeration](ne-fwpsk-fwps-fields-ipsec-v6-.md) | TBD |
| [FWPS_BUILTIN_LAYERS_ enumeration](ne-fwpsk-fwps-builtin-layers-.md) | TBD |
| [FWPS_FIELDS_INBOUND_MAC_FRAME_NATIVE_ enumeration](ne-fwpsk-fwps-fields-inbound-mac-frame-native-.md) | TBD |
| [FWPS_FIELDS_ALE_AUTH_CONNECT_V4_ enumeration](ne-fwpsk-fwps-fields-ale-auth-connect-v4-.md) | TBD |
| [FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V4_ enumeration](ne-fwpsk-fwps-fields-ale-flow-established-v4-.md) | TBD |
| [FWPS_FIELDS_ALE_PRECLASSIFY_IP_LOCAL_ADDRESS_V4_ enumeration](ne-fwpsk-fwps-fields-ale-preclassify-ip-local-address-v4-.md) | TBD |
| [FWPS_FIELDS_RPC_EPMAP_ enumeration](ne-fwpsk-fwps-fields-rpc-epmap-.md) | TBD |
| [FWPS_FIELDS_ALE_RESOURCE_RELEASE_V6_ enumeration](ne-fwpsk-fwps-fields-ale-resource-release-v6-.md) | TBD |
| [FWPS_FIELDS_ALE_AUTH_LISTEN_V6_ enumeration](ne-fwpsk-fwps-fields-ale-auth-listen-v6-.md) | TBD |
| [FWPS_FIELDS_ALE_PRECLASSIFY_IP_REMOTE_ADDRESS_V6_ enumeration](ne-fwpsk-fwps-fields-ale-preclassify-ip-remote-address-v6-.md) | TBD |
| [FWPS_FIELDS_OUTBOUND_MAC_FRAME_NATIVE_FAST enumeration](ne-fwpsk-fwps-fields-outbound-mac-frame-native-fast.md) | TBD |
| [FWPS_FIELDS_IPSEC_KM_DEMUX_V4_ enumeration](ne-fwpsk-fwps-fields-ipsec-km-demux-v4-.md) | TBD |
| [FWPS_FIELDS_ALE_AUTH_LISTEN_V4_ enumeration](ne-fwpsk-fwps-fields-ale-auth-listen-v4-.md) | TBD |
| [FWPS_CONNECTION_REDIRECT_STATE_ enumeration](ne-fwpsk-fwps-connection-redirect-state-.md) | TBD |
| [FWPS_FIELDS_STREAM_V4_ enumeration](ne-fwpsk-fwps-fields-stream-v4-.md) | TBD |
| [FWPS_FIELDS_IPFORWARD_V4_ enumeration](ne-fwpsk-fwps-fields-ipforward-v4-.md) | TBD |
| [FWPS_FIELDS_ALE_AUTH_CONNECT_V6_ enumeration](ne-fwpsk-fwps-fields-ale-auth-connect-v6-.md) | TBD |
| [FWPS_FIELDS_INGRESS_VSWITCH_TRANSPORT_V4_ enumeration](ne-fwpsk-fwps-fields-ingress-vswitch-transport-v4-.md) | TBD |
| [FWPS_FIELDS_NAME_RESOLUTION_CACHE_V6_ enumeration](ne-fwpsk-fwps-fields-name-resolution-cache-v6-.md) | TBD |
| [FWPS_FIELDS_IKEEXT_V4_ enumeration](ne-fwpsk-fwps-fields-ikeext-v4-.md) | TBD |
| [FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V4_ enumeration](ne-fwpsk-fwps-fields-outbound-icmp-error-v4-.md) | TBD |
| [FWPS_VSWITCH_EVENT_TYPE_ enumeration](ne-fwpsk-fwps-vswitch-event-type-.md) | TBD |
| [FWPS_FIELDS_ALE_BIND_REDIRECT_V6_ enumeration](ne-fwpsk-fwps-fields-ale-bind-redirect-v6-.md) | TBD |
| [FWPS_FIELDS_ALE_AUTH_RECV_ACCEPT_V4_ enumeration](ne-fwpsk-fwps-fields-ale-auth-recv-accept-v4-.md) | TBD |
| [FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6_ enumeration](ne-fwpsk-fwps-fields-ale-flow-established-v6-.md) | TBD |
| [FWPS_FIELDS_STREAM_V6_ enumeration](ne-fwpsk-fwps-fields-stream-v6-.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [FwpsDereferencevSwitchPacketContext0 function](nf-fwpsk-fwpsdereferencevswitchpacketcontext0.md) | TBD |
| [FwpsInjectMacSendAsync0 function](nf-fwpsk-fwpsinjectmacsendasync0.md) | The FwpsInjectMacSendAsync0 function can reinject a previously absorbed media access control (MAC) frame (or a clone of the frame) back to the layer 2 outbound data path it was intercepted from, or inject an invented MAC frame. |
| [FwpsvSwitchNotifyComplete0 function](nf-fwpsk-fwpsvswitchnotifycomplete0.md) | The FwpsvSwitchNotifyComplete0 function completes a pending virtual switch event notification.Note  FwpsvSwitchNotifyComplete0 is a specific version of FwpsvSwitchNotifyComplete. |
| [FwpsStreamInjectAsync0 function](nf-fwpsk-fwpsstreaminjectasync0.md) | The FwpsStreamInjectAsync0 function injects TCP data segments into a TCP data stream.Note  FwpsStreamInjectAsync0 is a specific version of FwpsStreamInjectAsync. |
| [FwpsAleEndpointEnum0 function](nf-fwpsk-fwpsaleendpointenum0.md) | The FwpsAleEndpointEnum0 function enumerates application layer enforcement (ALE) endpoints.Note  FwpsAleEndpointEnum0 is a specific version of FwpsAleEndpointEnum. |
| [FwpsInjectionHandleCreate0 function](nf-fwpsk-fwpsinjectionhandlecreate0.md) | The FwpsInjectionHandleCreate0 function creates a handle that can be used by packet injection functions to inject packet or stream data into the TCP/IP network stack and by the FwpsQueryPacketInjectionState0 function to query the packet injection state.Note  FwpsInjectionHandleCreate0 is a specific version of FwpsInjectionHandleCreate. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. |
| [FwpsInjectNetworkSendAsync0 function](nf-fwpsk-fwpsinjectnetworksendasync0.md) | The FwpsInjectNetworkSendAsync0 function injects packet data into the send data path.Note  FwpsInjectNetworkSendAsync0 is a specific version of FwpsInjectNetworkSendAsync. |
| [FwpsCompleteClassify0 function](nf-fwpsk-fwpscompleteclassify0.md) | A callout driver calls FwpsCompleteClassify0 to asynchronously complete a pended classify request. |
| [FwpsNetBufferListRetrieveContext0 function](nf-fwpsk-fwpsnetbufferlistretrievecontext0.md) | The FwpsNetBufferListRetrieveContext0 function retrieves the context associated with a network buffer list that was tagged in another layer.Note  FwpsNetBufferListRetrieveContext0 is a specific version of FwpsNetBufferListRetrieveContext. |
| [FwpsRedirectHandleDestroy0 function](nf-fwpsk-fwpsredirecthandledestroy0.md) | The FwpsRedirectHandleDestroy0 function destroys a redirect handle that was previously created by calling the FwpsRedirectHandleCreate0 function.Note  FwpsRedirectHandleDestroy0 is a specific version of FwpsRedirectHandleDestroy. |
| [FwpsReferenceNetBufferList0 function](nf-fwpsk-fwpsreferencenetbufferlist0.md) | The FwpsReferenceNetBufferList0 function increments the reference count for a NET_BUFFER_LIST structure.Note  FwpsReferenceNetBufferList0 is a specific version of FwpsReferenceNetBufferList. |
| [FwpsCalloutRegister2 function](nf-fwpsk-fwpscalloutregister2.md) | The FwpsCalloutRegister2 function registers a callout with the filter engine.Note  FwpsCalloutRegister2 is the specific version of FwpsCalloutRegister used in Windows 8 and later. |
| [FwpsInjectionHandleDestroy0 function](nf-fwpsk-fwpsinjectionhandledestroy0.md) | The FwpsInjectionHandleDestroy0 function destroys an injection handle that was previously created by calling the FwpsInjectionHandleCreate0 function.Note  FwpsInjectionHandleDestroy0 is a specific version of FwpsInjectionHandleDestroy. |
| [FwpsInjectTransportReceiveAsync0 function](nf-fwpsk-fwpsinjecttransportreceiveasync0.md) | The FwpsInjectTransportReceiveAsync0 function injects packet data from the transport, datagram data, or ICMP error layers into the receive data path.Note  FwpsInjectTransportReceiveAsync0 is a specific version of FwpsInjectTransportReceiveAsync. |
| [FwpsReferencevSwitchPacketContext0 function](nf-fwpsk-fwpsreferencevswitchpacketcontext0.md) | TBD |
| [FwpsInjectTransportSendAsync0 function](nf-fwpsk-fwpsinjecttransportsendasync0.md) | The FwpsInjectTransportSendAsync0 function injects packet data from the transport, datagram data, or ICMP error layers into the send data path.Note  FwpsInjectTransportSendAsync0 is the specific version of FwpsInjectTransportSendAsync used in Windows Vista and later. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. For Windows 7, FwpsInjectTransportSendAsync1 is available. |
| [FwpsConstructIpHeaderForTransportPacket0 function](nf-fwpsk-fwpsconstructipheaderfortransportpacket0.md) | The FwpsConstructIpHeaderForTransportPacket0 function is called by a callout to construct a new IP header or to rebuild a preexisting IP packet header for only one net buffer.Note  FwpsConstructIpHeaderForTransportPacket0 is a specific version of FwpsConstructIpHeaderForTransportPacket. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. |
| [FwpsInjectNetworkReceiveAsync0 function](nf-fwpsk-fwpsinjectnetworkreceiveasync0.md) | The FwpsInjectNetworkReceiveAsync0 function injects packet data into the receive data path.Note  FwpsInjectNetworkReceiveAsync0 is a specific version of FwpsInjectNetworkReceiveAsync. |
| [FwpsNetBufferListGetTagForContext0 function](nf-fwpsk-fwpsnetbufferlistgettagforcontext0.md) | The FwpsNetBufferListGetTagForContext0 function gets a locally unique context tag that can be used to associate packets with the callout driver.Note  FwpsNetBufferListGetTagForContext0 is a specific version of FwpsNetBufferListGetTagForContext. |
| [FwpsFlowRemoveContext0 function](nf-fwpsk-fwpsflowremovecontext0.md) | The FwpsFlowRemoveContext0 function removes a previously associated context from a data flow.Note  FwpsFlowRemoveContext0 is a specific version of FwpsFlowRemoveContext. |
| [FwpsNetBufferListRemoveContext0 function](nf-fwpsk-fwpsnetbufferlistremovecontext0.md) | The FwpsNetBufferListRemoveContext0 function removes the context associated with a network buffer list.Note  FwpsNetBufferListRemoveContext0 is a specific version of FwpsNetBufferListRemoveContext. |
| [FwpsGetPacketListSecurityInformation0 function](nf-fwpsk-fwpsgetpacketlistsecurityinformation0.md) | The FwpsGetPacketListSecurityInformation0 function retrieves information associated with a packet list.Note  FwpsGetPacketListSecurityInformation0 is a specific version of FwpsGetPacketListSecurityInformation. |
| [FwpsCloneStreamData0 function](nf-fwpsk-fwpsclonestreamdata0.md) | The FwpsCloneStreamData0 function allocates a clone of an existing FWPS_STREAM_DATA0 data stream.Note  FwpsCloneStreamData0 is a specific version of FwpsCloneStreamData. |
| [FwpsCalloutRegister0 function](nf-fwpsk-fwpscalloutregister0.md) | The FwpsCalloutRegister0 function registers a callout with the filter engine.Note  FwpsCalloutRegister0 is the specific version of FwpsCalloutRegister used in Windows Vista and later. |
| [FwpsAcquireClassifyHandle0 function](nf-fwpsk-fwpsacquireclassifyhandle0.md) | The FwpsAcquireClassifyHandle0 function generates a classification handle that is used to identify asynchronous classification operations and requests for writable layer data.Note  FwpsAcquireClassifyHandle0 is a specific version of FwpsAcquireClassifyHandle. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. |
| [FwpsPendOperation0 function](nf-fwpsk-fwpspendoperation0.md) | The FwpsPendOperation0 function is called by a callout to suspend packet processing pending completion of another operation.Note  FwpsPendOperation0 is a specific version of FwpsPendOperation. |
| [FwpsFlowAssociateContext0 function](nf-fwpsk-fwpsflowassociatecontext0.md) | The FwpsFlowAssociateContext0 function associates a callout driver-defined context with a data flow.Note  FwpsFlowAssociateContext0 is a specific version of FwpsFlowAssociateContext. |
| [FwpsNetBufferListAssociateContext0 function](nf-fwpsk-fwpsnetbufferlistassociatecontext0.md) | The FwpsNetBufferListAssociateContext0 function associates the callout driver's context with a network buffer list and configures notification for network buffer list events.Note  FwpsNetBufferListAssociateContext0 is the specific version of FwpsNetBufferListAssociateContext used in Windows 7 and later. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. For Windows 8, FwpsNetBufferListAssociateContext1 is available. |
| [FwpsAleEndpointGetSecurityInfo0 function](nf-fwpsk-fwpsaleendpointgetsecurityinfo0.md) | The FwpsAleEndpointGetSecurityInfo0 function retrieves security information about the application layer enforcement (ALE) endpoint enumeration session.Note  FwpsAleEndpointGetSecurityInfo0 is a specific version of FwpsAleEndpointGetSecurityInfo. |
| [FwpsOpenToken0 function](nf-fwpsk-fwpsopentoken0.md) | The FwpsOpenToken0 function opens an access token. |
| [FwpsInjectForwardAsync0 function](nf-fwpsk-fwpsinjectforwardasync0.md) | The FwpsInjectForwardAsync0 function injects packet data into the forwarding data path.Note  FwpsInjectForwardAsync0 is a specific version of FwpsInjectForwardAsync. |
| [FwpsReassembleForwardFragmentGroup0 function](nf-fwpsk-fwpsreassembleforwardfragmentgroup0.md) | The FwpsReassembleForwardFragmentGroup0 function assembles a list of IP fragments in the forwarding data path into a single packet.Note  FwpsReassembleForwardFragmentGroup0 is a specific version of FwpsReassembleForwardFragmentGroup. |
| [FwpsAleEndpointDestroyEnumHandle0 function](nf-fwpsk-fwpsaleendpointdestroyenumhandle0.md) | The FwpsAleEndpointDestroyEnumHandle0 function destroys an endpoint enumeration handle that was created by calling FwpsAleEndpointCreateEnumHandle0.Note  FwpsAleEndpointDestroyEnumHandle0 is a specific version of FwpsAleEndpointDestroyEnumHandle. |
| [FwpsInjectTransportSendAsync1 function](nf-fwpsk-fwpsinjecttransportsendasync1.md) | The FwpsInjectTransportSendAsync1 function injects packet data from the transport, datagram data, or ICMP error layers into the send data path. |
| [FwpsQueryConnectionSioFormatRedirectRecords0 function](nf-fwpsk-fwpsqueryconnectionsioformatredirectrecords0.md) | The FwpsQueryConnectionSioFormatRedirectRecords0 function returns the connection redirect records for a redirected connection. |
| [FwpsPendClassify0 function](nf-fwpsk-fwpspendclassify0.md) | A callout's classifyFn function calls FwpsPendClassify0 to pend the current classify request. |
| [FwpsCalloutRegister1 function](nf-fwpsk-fwpscalloutregister1.md) | The FwpsCalloutRegister1 function registers a callout with the filter engine.Note  FwpsCalloutRegister1 is the specific version of FwpsCalloutRegister used in Windows 7 and later. |
| [FwpsCalloutRegister3 function](nf-fwpsk-fwpscalloutregister3.md) | TBD |
| [FwpsAllocateCloneNetBufferList0 function](nf-fwpsk-fwpsallocateclonenetbufferlist0.md) | The FwpsAllocateCloneNetBufferList0 function allocates a NET_BUFFER_LIST structure that is a clone of an existing NET_BUFFER_LIST structure.Note  FwpsAllocateCloneNetBufferList0 is a specific version of FwpsAllocateCloneNetBufferList. |
| [FwpsCompleteOperation0 function](nf-fwpsk-fwpscompleteoperation0.md) | The FwpsCompleteOperation0 function is called by a callout to resume packet processing that was suspended pending completion of another operation.Note  FwpsCompleteOperation0 is a specific version of FwpsCompleteOperation. |
| [FwpsStreamContinue0 function](nf-fwpsk-fwpsstreamcontinue0.md) | The FwpsStreamContinue0 function resumes the processing of an inbound data stream that was previously deferred.Note  FwpsStreamContinue0 is a specific version of FwpsStreamContinue. |
| [FwpsDiscardClonedStreamData0 function](nf-fwpsk-fwpsdiscardclonedstreamdata0.md) | The FwpsDiscardClonedStreamData0 function frees the memory buffer that is allocated by the FwpsCloneStreamData0 function.Note  FwpsDiscardClonedStreamData0 is a specific version of FwpsDiscardClonedStreamData. |
| [FwpsAleEndpointCreateEnumHandle0 function](nf-fwpsk-fwpsaleendpointcreateenumhandle0.md) | The FwpsAleEndpointCreateEnumHandle0 function creates a handle that can be used with other application layer enforcement (ALE) endpoint functions to enumerate endpoint data.Note  FwpsAleEndpointCreateEnumHandle0 is a specific version of FwpsAleEndpointCreateEnumHandle. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. |
| [FwpsVirtualIfTunnelInfoSet0 function](nf-fwpsk-fwpsvirtualiftunnelinfoset0.md) | TBD |
| [FwpsAleEndpointSetSecurityInfo0 function](nf-fwpsk-fwpsaleendpointsetsecurityinfo0.md) | The FwpsAleEndpointSetSecurityInfo0 function sets security information about the application layer enforcement (ALE) endpoint enumeration session.Note  FwpsAleEndpointSetSecurityInfo0 is a specific version of FwpsAleEndpointSetSecurityInfo. |
| [FwpsAcquireWritableLayerDataPointer0 function](nf-fwpsk-fwpsacquirewritablelayerdatapointer0.md) | The FwpsAcquireWritableLayerDataPointer0 function returns layer-specific data that can be inspected and changed.Note  FwpsAcquireWritableLayerDataPointer0 is a specific version of FwpsAcquireWritableLayerDataPointer. |
| [FwpsFreeCloneNetBufferList0 function](nf-fwpsk-fwpsfreeclonenetbufferlist0.md) | The FwpsFreeCloneNetBufferList0 function frees a clone NET_BUFFER_LIST structure that was previously allocated by a call to the FwpsAllocateCloneNetBufferList0 function.Note  FwpsFreeCloneNetBufferList0 is a specific version of FwpsFreeCloneNetBufferList. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. |
| [FwpsNetBufferListAssociateContext1 function](nf-fwpsk-fwpsnetbufferlistassociatecontext1.md) | The FwpsNetBufferListAssociateContext1 function associates the callout driver's context with a network buffer list and configures notification for network buffer list events.Note  FwpsNetBufferListAssociateContext1 is the specific version of FwpsNetBufferListAssociateContext used in Windows 8 and later. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. For Windows 7, FwpsNetBufferListAssociateContext0 is available. |
| [FwpsClassifyOptionSet0 function](nf-fwpsk-fwpsclassifyoptionset0.md) | The FwpsClassifyOptionSet0 function is called by a callout filter's classifyFn function to specify additional information that affects the characteristics of permitted filtering operations.Note  FwpsClassifyOptionSet0 is a specific version of FwpsClassifyOptionSet. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. |
| [FWPS_IS_L2_METADATA_FIELD_PRESENT function](nf-fwpsk-fwps-is-l2-metadata-field-present.md) | TBD |
| [FwpsApplyModifiedLayerData0 function](nf-fwpsk-fwpsapplymodifiedlayerdata0.md) | The FwpsApplyModifiedLayerData0 function applies changes to layer-specific data made after a call to FwpsAcquireWritableLayerDataPointer0.Note  FwpsApplyModifiedLayerData0 is a specific version of FwpsApplyModifiedLayerData. |
| [FWPS_IS_METADATA_FIELD_PRESENT function](nf-fwpsk-fwps-is-metadata-field-present.md) | TBD |
| [FwpsInjectMacReceiveAsync0 function](nf-fwpsk-fwpsinjectmacreceiveasync0.md) | The FwpsInjectMacReceiveAsync0 function can reinject a previously absorbed media access control (MAC) frame (or a clone of the frame) back to the layer 2 inbound data path it was intercepted from, or inject an invented MAC frame. |
| [FwpsVirtualIfTunnelInfoGet0 function](nf-fwpsk-fwpsvirtualiftunnelinfoget0.md) | TBD |
| [FwpsQueryPacketInjectionState0 function](nf-fwpsk-fwpsquerypacketinjectionstate0.md) | The FwpsQueryPacketInjectionState0 function is called by a callout to query the injection state of packet data.Note  FwpsQueryPacketInjectionState0 is a specific version of FwpsQueryPacketInjectionState. |
| [FwpsRedirectHandleCreate0 function](nf-fwpsk-fwpsredirecthandlecreate0.md) | The FwpsRedirectHandleCreate0 function creates a handle that connection redirection functions can use to redirect connections to a local process. |
| [FwpsAleEndpointGetById0 function](nf-fwpsk-fwpsaleendpointgetbyid0.md) | The FwpsAleEndpointGetById0 function retrieves information about an application layer enforcement (ALE) endpoint.Note  FwpsAleEndpointGetById0 is a specific version of FwpsAleEndpointGetById. |
| [FwpsFreeNetBufferList0 function](nf-fwpsk-fwpsfreenetbufferlist0.md) | The FwpsFreeNetBufferList0 function frees a NET_BUFFER_LIST structure that was previously allocated by a call to the FwpsAllocateNetBufferAndNetBufferList0 function.Note  FwpsFreeNetBufferList0 is a specific version of FwpsFreeNetBufferList. |
| [FwpsCopyStreamDataToBuffer0 function](nf-fwpsk-fwpscopystreamdatatobuffer0.md) | The FwpsCopyStreamDataToBuffer0 function copies stream data to a buffer.Note  FwpsCopyStreamDataToBuffer0 is a specific version of FwpsCopyStreamDataToBuffer. |
| [FwpsFlowAbort0 function](nf-fwpsk-fwpsflowabort0.md) | The FwpsFlowAbort0 function aborts a data flow.Note  FwpsFlowAbort0 is a specific version of FwpsFlowAbort. |
| [FwpsCalloutUnregisterById0 function](nf-fwpsk-fwpscalloutunregisterbyid0.md) | The FwpsCalloutUnregisterById0 function unregisters a callout from the filter engine.Note  FwpsCalloutUnregisterById0 is a specific version of FwpsCalloutUnregisterById. |
| [FwpsvSwitchEventsSubscribe0 function](nf-fwpsk-fwpsvswitcheventssubscribe0.md) | The FwpsvSwitchEventsSubscribe0 function registers callback entry points for virtual switch layer events such as virtual port creation and deletion.Note  FwpsvSwitchEventsSubscribe0 is a specific version of FwpsvSwitchEventsSubscribe. |
| [FwpsCalloutUnregisterByKey0 function](nf-fwpsk-fwpscalloutunregisterbykey0.md) | The FwpsCalloutUnregisterByKey0 function unregisters a callout from the filter engine.Note  FwpsCalloutUnregisterByKey0 is a specific version of FwpsCalloutUnregisterByKey. |
| [FwpsReleaseClassifyHandle0 function](nf-fwpsk-fwpsreleaseclassifyhandle0.md) | A callout driver calls FwpsReleaseClassifyHandle0 to release a classification handle that was previously acquired through a call to FwpsAcquireClassifyHandle0.Note  FwpsReleaseClassifyHandle0 is a specific version of FwpsReleaseClassifyHandle. |
| [FwpsvSwitchEventsUnsubscribe0 function](nf-fwpsk-fwpsvswitcheventsunsubscribe0.md) | The FwpsvSwitchEventsUnsubscribe0 function releases resources that are associated with virtual switch notification subscriptions.Note  FwpsvSwitchEventsUnsubscribe0 is a specific version of FwpsvSwitchEventsUnsubscribe. |
| [FwpsInjectvSwitchEthernetIngressAsync0 function](nf-fwpsk-fwpsinjectvswitchethernetingressasync0.md) | The FwpsInjectvSwitchEthernetIngressAsync0 (was FwpsInjectvSwitchIngressAsync0) function reinjects a previously absorbed virtual switch packet (unmodified) back to the virtual switch ingress data path where it was intercepted. |
| [FwpsAllocateNetBufferAndNetBufferList0 function](nf-fwpsk-fwpsallocatenetbufferandnetbufferlist0.md) | The FwpsAllocateNetBufferAndNetBufferList0 function allocates a new NET_BUFFER_LIST structure.Note  FwpsAllocateNetBufferAndNetBufferList0 is a specific version of FwpsAllocateNetBufferAndNetBufferList. |
| [FwpsQueryConnectionRedirectState0 function](nf-fwpsk-fwpsqueryconnectionredirectstate0.md) | The FwpsQueryConnectionRedirectState0 function returns the connection redirect state.Note  FwpsQueryConnectionRedirectState0 is a specific version of FwpsQueryConnectionRedirectState. |
| [FwpsDereferenceNetBufferList0 function](nf-fwpsk-fwpsdereferencenetbufferlist0.md) | The FwpsDereferenceNetBufferList0 function decrements the reference count for a NET_BUFFER_LIST structure that a callout driver had acquired earlier using the FwpsReferenceNetBufferList0 function.Note  FwpsDereferenceNetBufferList0 is a specific version of FwpsDereferenceNetBufferList. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [FWPS_PACKET_LIST_IPSEC_INFORMATION0_ structure](ns-fwpsk-fwps-packet-list-ipsec-information0-.md) | The FWPS_PACKET_LIST_IPSEC_INFORMATION0 structure defines IPsec information associated with a packet list.Note  FWPS_PACKET_LIST_IPSEC_INFORMATION0 is a specific version of FWPS_PACKET_LIST_IPSEC_INFORMATION. |
| [NDIS_SWITCH_NIC_PARAMETERS structure](ns-fwpsk--ndis-switch-nic-parameters.md) | TBD |
| [NDIS_SWITCH_PORT_PROPERTY_DELETE_PARAMETERS structure](ns-fwpsk--ndis-switch-port-property-delete-parameters.md) | TBD |
| [FWPS_CALLOUT3_ structure](ns-fwpsk-fwps-callout3-.md) | TBD |
| [FWPS_TRANSPORT_SEND_PARAMS0_ structure](ns-fwpsk-fwps-transport-send-params0-.md) | The FWPS_TRANSPORT_SEND_PARAMS0 structure defines properties of an outbound transport layer packet.Note  FWPS_TRANSPORT_SEND_PARAMS0 is the specific version of FWPS_TRANSPORT_SEND_PARAMS used in Windows Vista and later. |
| [NDIS_SWITCH_PORT_PROPERTY_PARAMETERS structure](ns-fwpsk--ndis-switch-port-property-parameters.md) | TBD |
| [FWPS_CALLOUT1_ structure](ns-fwpsk-fwps-callout1-.md) | The FWPS_CALLOUT1 structure defines the data that is required for a callout driver to register a callout with the filter engine.Note  FWPS_CALLOUT1 is the specific version of FWPS_CALLOUT used in Windows 7 and later. |
| [FWPS_INCOMING_METADATA_VALUES0_ structure](ns-fwpsk-fwps-incoming-metadata-values0-.md) | The FWPS_INCOMING_METADATA_VALUES0 structure defines metadata values that the filter engine passes to a callout's classifyFn callout function.Note  FWPS_INCOMING_METADATA_VALUES0 is a specific version of FWPS_INCOMING_METADATA_VALUES. |
| [FWPS_CALLOUT2_ structure](ns-fwpsk-fwps-callout2-.md) | The FWPS_CALLOUT2 structure defines the data that is required for a callout driver to register a callout with the filter engine.Note  FWPS_CALLOUT2 is the specific version of FWPS_CALLOUT used in Windows 8 and later. |
| [FWPS_PACKET_LIST_FWP_INFORMATION0_ structure](ns-fwpsk-fwps-packet-list-fwp-information0-.md) | The FWPS_PACKET_LIST_FWP_INFORMATION0 structure defines Windows Filtering Platform information associated with a packet list.Note  FWPS_PACKET_LIST_FWP_INFORMATION0 is a specific version of FWPS_PACKET_LIST_FWP_INFORMATION. |
| [NDIS_SWITCH_NIC_SAVE_STATE structure](ns-fwpsk--ndis-switch-nic-save-state.md) | TBD |
| [FWPS_VSWITCH_EVENT_DISPATCH_TABLE0_ structure](ns-fwpsk-fwps-vswitch-event-dispatch-table0-.md) | The FWPS_VSWITCH_EVENT_DISPATCH_TABLE0 structure specifies a callout driver-supplied virtual switch event dispatch table.Note  FWPS_VSWITCH_EVENT_DISPATCH_TABLE0 is a specific version of FWPS_VSWITCH_EVENT_DISPATCH_TABLE. |
| [FWPS_PACKET_LIST_INBOUND_IPSEC_INFORMATION0_ structure](ns-fwpsk-fwps-packet-list-inbound-ipsec-information0-.md) | The FWPS_PACKET_LIST_INBOUND_IPSEC_INFORMATION0 structure defines IPsec information associated with inbound packet data.Note  FWPS_PACKET_LIST_INBOUND_IPSEC_INFORMATION0 is a specific version of FWPS_PACKET_LIST_INBOUND_IPSEC_INFORMATION. |
| [FWPS_STREAM_DATA_OFFSET0_ structure](ns-fwpsk-fwps-stream-data-offset0-.md) | The FWPS_STREAM_DATA_OFFSET0 structure defines an offset into a portion of a data stream that is described by an FWPS_STREAM_DATA0 structure.Note  FWPS_STREAM_DATA_OFFSET0 is a specific version of FWPS_STREAM_DATA_OFFSET. |
| [FWPS_CALLOUT0_ structure](ns-fwpsk-fwps-callout0-.md) | The FWPS_CALLOUT0 structure defines the data that is required for a callout driver to register a callout with the filter engine.Note  FWPS_CALLOUT0 is the specific version of FWPS_CALLOUT used in Windows Vista and later. |
| [FWPS_BIND_REQUEST0 structure](ns-fwpsk--fwps-bind-request0.md) | The FWPS_BIND_REQUEST0 structure defines modifiable data for the FWPM_LAYER_ALE_AUTH_BIND_REDIRECT_V4 and FWPM_LAYER_ALE_AUTH_BIND_REDIRECT_V6 layers. |
| [NDIS_SWITCH_PARAMETERS structure](ns-fwpsk--ndis-switch-parameters.md) | TBD |
| [FWPS_CONNECT_REQUEST0 structure](ns-fwpsk--fwps-connect-request0.md) | The FWPS_CONNECT_REQUEST0 structure defines modifiable data for the FWPM_LAYER_ALE_AUTH_CONNECT_REDIRECT_V4 and FWPM_LAYER_ALE_AUTH_CONNECT_REDIRECT_V6 layers. |
| [NDIS_SWITCH_PORT_PARAMETERS structure](ns-fwpsk--ndis-switch-port-parameters.md) | TBD |
| [FWPS_TRANSPORT_SEND_PARAMS1_ structure](ns-fwpsk-fwps-transport-send-params1-.md) | The FWPS_TRANSPORT_SEND_PARAMS1 structure defines properties of an outbound transport layer packet.Note  FWPS_TRANSPORT_SEND_PARAMS1 is the specific version of FWPS_TRANSPORT_SEND_PARAMS used in Windows 7 and later. |
| [FWPS_PACKET_LIST_INFORMATION0_ structure](ns-fwpsk-fwps-packet-list-information0-.md) | The FWPS_PACKET_LIST_INFORMATION0 structure defines information associated with a packet list.Note  FWPS_PACKET_LIST_INFORMATION0 is a specific version of FWPS_PACKET_LIST_INFORMATION. |
| [FWPS_PACKET_LIST_OUTBOUND_IPSEC_INFORMATION0_ structure](ns-fwpsk-fwps-packet-list-outbound-ipsec-information0-.md) | The FWPS_PACKET_LIST_OUTBOUND_IPSEC_INFORMATION0 structure defines IPsec information associated with outbound packet data.Note  FWPS_PACKET_LIST_OUTBOUND_IPSEC_INFORMATION0 is a specific version of FWPS_PACKET_LIST_OUTBOUND_IPSEC_INFORMATION. |
| [FWPS_STREAM_CALLOUT_IO_PACKET0_ structure](ns-fwpsk-fwps-stream-callout-io-packet0-.md) | The FWPS_STREAM_CALLOUT_IO_PACKET0 structure describes the data passed by the filter engine to a callout's classifyFn callout function when filtering a data stream.Note  FWPS_STREAM_CALLOUT_IO_PACKET0 is a specific version of FWPS_STREAM_CALLOUT_IO_PACKET. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. |
| [NDIS_SWITCH_NIC_ARRAY structure](ns-fwpsk--ndis-switch-nic-array.md) | TBD |
| [NDIS_SWITCH_PORT_ARRAY structure](ns-fwpsk--ndis-switch-port-array.md) | TBD |
| [FWPS_STREAM_DATA0_ structure](ns-fwpsk-fwps-stream-data0-.md) | The FWPS_STREAM_DATA0 structure describes a portion of a data stream.Note  FWPS_STREAM_DATA0 is a specific version of FWPS_STREAM_DATA. |

This header is used in these topics:

- [netvista](..content/_netvista)
