# Declarations in the bltooth technology
This technology  contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [CHANNEL_CONFIG_PARAMETERS_ENHANCED structure](..\bthddi\ns-bthddi--channel-config-parameters-enhanced.md) | The CHANNEL_CONFIG_PARAMETERS_ENHANCED structure describes configuration parameters for inbound and outbound directions of an L2CAP channel. |
| [BASEBAND_CHANNEL_INFO structure](..\bthddi\ns-bthddi--baseband-channel-info.md) | The BASEBAND_CHANNEL_INFO structure describes output information about the baseband channel that is used by a SCO link after a BRB_GET_CHANNEL_INFO BRB completes. |
| [CHANNEL_CONFIG_RESULTS_ENHANCED structure](..\bthddi\ns-bthddi--channel-config-results-enhanced.md) | The CHANNEL_CONFIG_RESULTS_ENHANCED structure describes configuration parameters and the buffer size of any extra option for the inbound and outbound directions of an L2CAP channel. |
| [CHANNEL_CONFIG_RESULTS structure](..\bthddi\ns-bthddi--channel-config-results.md) | The CHANNEL_CONFIG_RESULTS structure contains configuration parameters and the buffer size of any extra options for the inbound and outbound directions of a L2CAP channel. |
| [BRB_HEADER structure](..\bthddi\ns-bthddi--brb-header.md) | The BRB_HEADER structure contains header information about a Bluetooth request block (BRB), including information about the BRB type that the Bluetooth driver stack uses to determine which kind of BRB type to process. |
| [INDICATION_PARAMETERS_ENHANCED structure](..\bthddi\ns-bthddi--indication-parameters-enhanced~r1.md) | The INDICATION_PARAMETERS_ENHANCED structure is passed as the Parameters parameter to a profile driver's enhanced L2CAP Callback Function. |
| [SCO_INDICATION_PARAMETERS structure](..\bthddi\ns-bthddi--sco-indication-parameters.md) | The SCO_INDICATION_PARAMETERS structure describes indication parameters about a SCO connect or disconnect notification. |
| [CHANNEL_CONFIG_PARAMETERS structure](..\bthddi\ns-bthddi--channel-config-parameters.md) | The CHANNEL_CONFIG_PARAMETERS structure contains configuration parameters for inbound and outbound directions of a L2CAP channel. |
| [CO_HEADER structure](..\bthddi\ns-bthddi--co-header.md) | The CO_HEADER structure is used to specify values for the Header member of the L2CAP_CONFIG_OPTION structure. |
| [BRB structure](..\bthddi\ns-bthddi--brb.md) | Profile drivers use Bluetooth request blocks (BRBs), to send requests to the Bluetooth driver stack. The BRB structure defines the format for all supported commands that can be sent to a Bluetooth device. |
| [L2CAP_CONFIG_OPTION structure](..\bthddi\ns-bthddi--l2cap-config-option.md) | An array of L2CAP_CONFIG_OPTION structures is used to specify values for the ExtraOptions member of the CHANNEL_CONFIG_PARAMETERS, _BRB_L2CA_OPEN_CHANNEL, and INDICATION_PARAMETERS structures. |
| [L2CAP_CONFIG_RANGE structure](..\bthddi\ns-bthddi--l2cap-config-range.md) | The L2CAP_CONFIG_RANGE structure is used to specify a range of possible values for the FlushTO member of the _BRB_L2CA_OPEN_CHANNEL structure during incoming requests. |
| [L2CAP_CONFIG_VALUE_RANGE structure](..\bthddi\ns-bthddi--l2cap-config-value-range.md) | The L2CAP_CONFIG_VALUE_RANGE structure is used to specify values for the Mtu and FlushTO members of the _BRB_L2CA_OPEN_CHANNEL structure. |
| [L2CAP_EXTENDED_FLOW_SPEC structure](..\bthddi\ns-bthddi--l2cap-extended-flow-spec.md) | The L2CAP_EXTENDED_FLOW_SPEC is reserved for future use. |
| [INDICATION_PARAMETERS structure](..\bthddi\ns-bthddi--indication-parameters~r1.md) | The INDICATION_PARAMETERS structure is passed as the Parameters parameter to a profile driver's L2CAP Callback Function. |
| [L2CAP_RETRANSMISSION_AND_FLOW_CONTROL structure](..\bthddi\ns-bthddi--l2cap-retransmission-and-flow-control.md) | The L2CAP_RETRANSMISSION_AND_FLOW_CONTROL structure describes configuration parameters for enhanced retransmission mode and streaming mode. |
| [BTH_ENUMERATOR_INFO structure](..\bthddi\ns-bthddi--bth-enumerator-info.md) | The BTH_ENUMERATOR_INFO structure contains information about an underlying device and the service that caused the Plug and Play (PnP) manager to load the profile driver. |
| [BTH_PROFILE_DRIVER_INTERFACE structure](..\bthddi\ns-bthddi--bth-profile-driver-interface.md) | The BTH_PROFILE_DRIVER_INTERFACE structure provides functions to allocate, free, initialize, and reuse BRBs, and to determine the currently installed Bluetooth version. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFNBTH_ALLOCATE_BRB callback](..\bthddi\nc-bthddi-pfnbth-allocate-brb.md) | The BthAllocateBrb function allocates a Bluetooth request block (BRB) of the specified type. |
| [PFNBTH_REUSE_BRB callback](..\bthddi\nc-bthddi-pfnbth-reuse-brb.md) | The BthReuseBrb function reinitializes a Bluetooth request block (BRB) to be reused. |
| [PFNBTH_INITIALIZE_BRB callback](..\bthddi\nc-bthddi-pfnbth-initialize-brb.md) | The BthInitializeBrb function initializes a Bluetooth request block (BRB) allocated on the local stack. |
| [PFNBTH_IS_BLUETOOTH_VERSION_AVAILABLE callback](..\bthddi\nc-bthddi-pfnbth-is-bluetooth-version-available.md) | The IsBluetoothVersionAvailable function checks whether a given Bluetooth version is supported by the operating system. |
| [PFNSCO_INDICATION_CALLBACK callback](..\bthddi\nc-bthddi-pfnsco-indication-callback.md) | Profile drivers implement a SCO callback function to provide the Bluetooth driver stack with a mechanism to notify the profile driver about incoming SCO connection requests from remote devices, and any changes to the status of a currently open SCO connection. |
| [PFNBTHPORT_INDICATION_CALLBACK_ENHANCED callback](..\bthddi\nc-bthddi-pfnbthport-indication-callback-enhanced.md) | Profile drivers implement an enhanced L2CAP callback function to provide the Bluetooth driver stack with a mechanism to notify the profile driver about any changes to the status of a currently open L2CAP or eL2CAP connection. |
| [PFNBTHPORT_INDICATION_CALLBACK callback](..\bthddi\nc-bthddi-pfnbthport-indication-callback.md) | Profile drivers implement a L2CAP callback function to provide the Bluetooth driver stack with a mechanism to notify the profile driver about incoming L2CAP connection requests from remote devices, and any changes to the status of a currently open L2CAP connection. |
| [PFNBTH_FREE_BRB callback](..\bthddi\nc-bthddi-pfnbth-free-brb.md) | The BthFreeBrb function frees a Bluetooth request block (BRB) that was allocated previously with BthAllocateBrb. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [SCO_RETRANSMISSION_EFFORT enumeration](..\bthddi\ne-bthddi--sco-retransmission-effort.md) | The SCO_RETRANSMISSION_EFFORT enumeration type is used to determine the retransmission policies of a SCO channel. |
| [BRB_TYPE enumeration](..\bthddi\ne-bthddi--brb-type.md) | The BRB_TYPE enumeration type is used to determine the Bluetooth request block when a profile driver builds and sends a BRB. |
| [ENUMERATOR_TYPE enumeration](..\bthddi\ne-bthddi--enumerator-type.md) | The ENUMERATOR_TYPE enumeration type is used to determine whether the enumerated device is associated with a service or a protocol. The ENUMERATOR_TYPE enumeration is intended for internal use only and should not be used by profile drivers. |
| [INDICATION_CODE enumeration](..\bthddi\ne-bthddi--indication-code.md) | The INDICATION_CODE enumeration type indicates to a profile driver what type of L2CAP event has occurred. |
| [INDICATION_CODE enumeration](..\bthddi\ne-bthddi--indication-code~r1.md) | The INDICATION_CODE enumeration type indicates to a profile driver what type of L2CAP event has occurred. |
| [ACL_MODE enumeration](..\bthddi\ne-bthddi--acl-mode.md) | The ACL_MODE enumeration type is used to list the possible states of an ACL connection. |
| [SCO_INDICATION_CODE enumeration](..\bthddi\ne-bthddi--sco-indication-code.md) | The SCO_INDICATION_CODE enumeration type describes the type of an incoming SCO connection or bonding state change. The Bluetooth driver stack passes a value from this enumeration in the Indication argument of a profile driver's SCO Callback Function. |
| [SCO_DISCONNECT_REASON enumeration](..\bthddi\ne-bthddi--sco-disconnect-reason.md) | The SCO_DISCONNECT_REASON enumeration type gives the reason an SCO channel has been disconnected. |
| [L2CAP_DISCONNECT_REASON enumeration](..\bthddi\ne-bthddi--l2cap-disconnect-reason.md) | The L2CAP_DISCONNECT_REASON enumeration type gives the reason an L2CAP channel has been disconnected. |
| [SCO_LINK_TYPE enumeration](..\bthddi\ne-bthddi--sco-link-type.md) | The SCO_LINK_TYPE enumeration type describes the type of link used by the SCO connection when a ScoIndicationRemoteConnect indication event is processed. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [BTH_SDP_STREAM_RESPONSE structure](..\bthioctl\ns-bthioctl--bth-sdp-stream-response.md) | The BTH_SDP_STREAM_RESPONSE structure contains information about an SDP record. |
| [BTH_VENDOR_EVENT_INFO structure](..\bthioctl\ns-bthioctl--bth-vendor-event-info.md) | The BTH_VENDOR_EVENT_INFO structure specifies the buffer that is associated with the GUID_BLUETOOTH_HCI_VENDOR_EVENT GUID. |
| [BTH_VENDOR_SPECIFIC_COMMAND structure](..\bthioctl\ns-bthioctl--bth-vendor-specific-command.md) | The BTH_VENDOR_SPECIFIC_COMMAND structure specifies a Bluetooth vendor-specific command. |
| [BTH_RADIO_INFO structure](..\bthioctl\ns-bthioctl--bth-radio-info.md) | The BTH_RADIO_INFO structure contains information about a remote radio. |
| [BTH_DEVICE_INFO_LIST structure](..\bthioctl\ns-bthioctl--bth-device-info-list.md) | The BTH_DEVICE_INFO_LIST structure contains output information about all cached, previously discovered remote devices. |
| [BTH_SDP_ATTRIBUTE_SEARCH_REQUEST structure](..\bthioctl\ns-bthioctl--bth-sdp-attribute-search-request.md) | The BTH_SDP_ATTRIBUTE_SEARCH_REQUEST structure contains information pertinent to an SDP attribute search. |
| [BTH_VENDOR_PATTERN structure](..\bthioctl\ns-bthioctl--bth-vendor-pattern.md) | The BTH_VENDOR_PATTERN structure specifies a vendor pattern. |
| [BTH_LOCAL_RADIO_INFO structure](..\bthioctl\ns-bthioctl--bth-local-radio-info.md) | The BTH_LOCAL_RADIO_INFO structure contains information about the local Bluetooth system and radio. |
| [BTH_COMMAND_HEADER structure](..\bthioctl\ns-bthioctl--bth-command-header.md) | The BTH_COMMAND_HEADER structure specifies header information for a vendor-specific HCI command. |
| [BTH_SDP_RECORD structure](..\bthioctl\ns-bthioctl--bth-sdp-record.md) | The BTH_SDP_RECORD structure contains information about an SDP record that is to be added to the local SDP server. |
| [BTH_SDP_DISCONNECT structure](..\bthioctl\ns-bthioctl--bth-sdp-disconnect.md) | The BTH_SDP_DISCONNECT structure contains input information about a connection handle to the remote SDP connection to terminate. This structure is passed as the input buffer of IOCTL_BTH_SDP_DISCONNECT. |
| [BTH_SDP_SERVICE_SEARCH_REQUEST structure](..\bthioctl\ns-bthioctl--bth-sdp-service-search-request.md) | The BTH_SDP_SERVICE_SEARCH_REQUEST structure contains information pertinent to an SDP service search. |
| [BTH_SDP_CONNECT structure](..\bthioctl\ns-bthioctl--bth-sdp-connect.md) | The BTH_SDP_CONNECT structure contains input and output information about a connection between the local Bluetooth system and a remote SDP server. This structure is passed as the input buffer and output buffer of IOCTL_BTH_SDP_CONNECT. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [BTHDDI_SDP_NODE_INTERFACE structure](..\bthsdpddi\ns-bthsdpddi--bthddi-sdp-node-interface.md) | The BTHDDI_SDP_NODE_INTERFACE structure provides functions for manipulating SDP records, including converting them to and from a tree representation that profile drivers can more easily parse. |
| [BTHDDI_SDP_PARSE_INTERFACE structure](..\bthsdpddi\ns-bthsdpddi--bthddi-sdp-parse-interface.md) | The BTHDDI_SDP_PARSE_INTERFACE structure provides functions for parsing SDP records. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [BTHX_SCO_SUPPORT enumeration](..\bthxddi\ne-bthxddi--bthx-sco-support.md) | The BTHX_SCO_SUPPORT enumeration lists the different types of SCO supported by the transport driver. |
| [BTHX_HCI_PACKET_TYPE enumeration](..\bthxddi\ne-bthxddi--bthx-hci-packet-type.md) | The BTHX_HCI_PACKET_TYPE enumeration lists the different types of packets being sent from the Bluetooth stack to the transport driver. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_BTHX_WRITE_HCI IOCTL](..\bthxddi\ni-bthxddi-ioctl-bthx-write-hci.md) | IOCTL_BTHX_WRITE_HCI is used to write Bluetooth ACL Data and Commands to the transport layer. |
| [IOCTL_BTHX_QUERY_CAPABILITIES IOCTL](..\bthxddi\ni-bthxddi-ioctl-bthx-query-capabilities.md) | IOCTL_BTHX_QUERY_CAPABILITIES is used to query the capabilities of the transport driver. |
| [IOCTL_BTHX_READ_HCI IOCTL](..\bthxddi\ni-bthxddi-ioctl-bthx-read-hci.md) | IOCTL_BTHX_READ_HCI is used to read Bluetooth ACL Data and Events from the transport layer. |
| [IOCTL_BTHX_GET_VERSION IOCTL](..\bthxddi\ni-bthxddi-ioctl-bthx-get-version.md) | Profile drivers use IOCTL_BTHX_GET_VERSION to get the version supported by the transport driver. |
| [IOCTL_BTHX_SET_VERSION IOCTL](..\bthxddi\ni-bthxddi-ioctl-bthx-set-version.md) | IOCTL_BTHX_SET_VERSION is used to inform the transport driver of the version of the extensibility interface being used. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [BTHX_VERSION structure](..\bthxddi\ns-bthxddi--bthx-version.md) | The BTHX_VERSION structure describes the version or versions that the transport driver supports. |
| [BTHX_HCI_READ_WRITE_CONTEXT structure](..\bthxddi\ns-bthxddi--bthx-hci-read-write-context.md) | The BTHX_HCI_READ_WRITE_CONTEXT structure is used as an input/output structure for the IOCTL_BTHX_READ_HCI and IOCTL_BTHX_WRITE_HCI IOCTLs. |
| [BTHX_CAPABILITIES structure](..\bthxddi\ns-bthxddi--bthx-capabilities.md) | The BTHX_CAPABILITIES structure describes the capabilities of the Bluetooth Extensible Transport Driver. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [SdpCreateNodeAlternative function](..\sdplib\nf-sdplib-sdpcreatenodealternative~r1.md) | The Bluetooth SdpCreateNodeAlternative function is used to create an empty alternative sequence SDP node. |
| [SdpCreateNodeUUID128 function](..\sdplib\nf-sdplib-sdpcreatenodeuuid128.md) | The Bluetooth SdpCreateNodeUUID128 function is used to allocate and initialize an SDP_NODE structure to a 128-bit UUID type. |
| [SdpCreateNodeUUID16 function](..\sdplib\nf-sdplib-sdpcreatenodeuuid16.md) | The Bluetooth SdpCreateNodeUUID16 function is used to allocate and initialize an SDP_NODE structure to a 16-bit UUID type. |
| [SdpCreateNodeUInt16 function](..\sdplib\nf-sdplib-sdpcreatenodeuint16.md) | The Bluetooth SdpCreateNodeUInt16 function is used to allocate and initialize an SDP_NODE structure to an unsigned 16-bit integer type. |
| [SdpCreateNodeAlternative function](..\sdplib\nf-sdplib-sdpcreatenodealternative.md) | The Bluetooth SdpCreateNodeAlternative function is used to create an empty alternative sequence SDP node. |
| [SdpAddAttributeToTree function](..\sdplib\nf-sdplib-sdpaddattributetotree.md) | The Bluetooth SdpAddAttributeToTree function is used to attach an SDP attribute node to the top level of an SDP record. |
| [SdpCreateNodeInt16 function](..\sdplib\nf-sdplib-sdpcreatenodeint16~r1.md) | The Bluetooth SdpCreateNodeInt16 function is used to allocate and initialize an SDP_NODE structure to a 16-bit integer type. |
| [SdpCreateNodeUInt128 function](..\sdplib\nf-sdplib-sdpcreatenodeuint128~r1.md) | The Bluetooth SdpCreateNodeUInt128 function is used to allocate and initialize an SDP_NODE structure to an unsigned 128-bit integer type. |
| [SdpCreateNodeUUID32 function](..\sdplib\nf-sdplib-sdpcreatenodeuuid32~r1.md) | The Bluetooth SdpCreateNodeUUID32 function is used to allocate and initialize an SDP_NODE structure to a 32-bit UUID type. |
| [SdpCreateNodeInt64 function](..\sdplib\nf-sdplib-sdpcreatenodeint64.md) | The Bluetooth SdpCreateNodeInt64 function is used to allocate and initialize an SDP_NODE structure to a 64-bit integer type. |
| [SdpCreateNodeBoolean function](..\sdplib\nf-sdplib-sdpcreatenodeboolean.md) | The Bluetooth SdpCreateNodeBoolean function is used to allocate and initialize an SDP_NODE structure to a Boolean type. |
| [SdpCreateNodeUrl function](..\sdplib\nf-sdplib-sdpcreatenodeurl~r1.md) | The Bluetooth SdpCreateNodeUrl function is used to allocate and initialize an SDP_NODE structure to a URL type. |
| [SdpFindAttributeInTree function](..\sdplib\nf-sdplib-sdpfindattributeintree.md) | The Bluetooth SdpFindAttributeInTree function is used to locate the specified attribute node in the tree-based representation of an SDP record. |
| [SdpCreateNodeInt8 function](..\sdplib\nf-sdplib-sdpcreatenodeint8~r1.md) | The Bluetooth SdpCreateNodeInt8 function is used to allocate and initialize an SDP_NODE structure to an 8-bit integer type. |
| [SdpCreateNodeInt128 function](..\sdplib\nf-sdplib-sdpcreatenodeint128~r1.md) | The Bluetooth SdpCreateNodeInt128 function is used to allocate and initialize an SDP_NODE structure to a 128-bit integer type. |
| [SdpAddAttributeToTree function](..\sdplib\nf-sdplib-sdpaddattributetotree~r1.md) | The Bluetooth SdpAddAttributeToTree function is used to attach an SDP attribute node to the top level of an SDP record. |
| [SdpCreateNodeUInt64 function](..\sdplib\nf-sdplib-sdpcreatenodeuint64.md) | The Bluetooth SdpCreateNodeUInt64 function is used to allocate and initialize an SDP_NODE structure to an unsigned 64-bit integer type. |
| [SdpCreateNodeUUID32 function](..\sdplib\nf-sdplib-sdpcreatenodeuuid32.md) | The Bluetooth SdpCreateNodeUUID32 function is used to allocate and initialize an SDP_NODE structure to a 32-bit UUID type. |
| [SdpCreateNodeUInt32 function](..\sdplib\nf-sdplib-sdpcreatenodeuint32~r1.md) | The Bluetooth SdpCreateNodeUInt32 function is used to allocate and initialize an SDP_NODE structure to an unsigned 32-bit integer type. |
| [SdpCreateNodeInt8 function](..\sdplib\nf-sdplib-sdpcreatenodeint8.md) | The Bluetooth SdpCreateNodeInt8 function is used to allocate and initialize an SDP_NODE structure to an 8-bit integer type. |
| [SdpCreateNodeSequence function](..\sdplib\nf-sdplib-sdpcreatenodesequence.md) | The Bluetooth SdpCreateNodeSequence function is used to create an empty sequence SDP node. |
| [SdpCreateNodeNil function](..\sdplib\nf-sdplib-sdpcreatenodenil~r1.md) | The Bluetooth SdpCreateNodeNil function is used to allocate and initialize an SDP_NODE structure to an empty node type. |
| [SdpCreateNodeUInt128 function](..\sdplib\nf-sdplib-sdpcreatenodeuint128.md) | The Bluetooth SdpCreateNodeUInt128 function is used to allocate and initialize an SDP_NODE structure to an unsigned 128-bit integer type. |
| [SdpCreateNodeInt16 function](..\sdplib\nf-sdplib-sdpcreatenodeint16.md) | The Bluetooth SdpCreateNodeInt16 function is used to allocate and initialize an SDP_NODE structure to a 16-bit integer type. |
| [SdpCreateNodeString function](..\sdplib\nf-sdplib-sdpcreatenodestring.md) | The Bluetooth SdpCreateNodeString function is used to allocate and initialize an SDP_NODE structure to a string type. |
| [SdpCreateNodeUInt8 function](..\sdplib\nf-sdplib-sdpcreatenodeuint8.md) | The Bluetooth SdpCreateNodeUInt8 function is used to allocate and initialize an SDP_NODE structure to an unsigned 8-bit integer type. |
| [SdpCreateNodeInt64 function](..\sdplib\nf-sdplib-sdpcreatenodeint64~r1.md) | The Bluetooth SdpCreateNodeInt64 function is used to allocate and initialize an SDP_NODE structure to a 64-bit integer type. |
| [SdpFreeTree function](..\sdplib\nf-sdplib-sdpfreetree.md) | The Bluetooth SdpFreeTree function is used to free the memory allocated for the tree-based representation of an SDP record. |
| [SdpCreateNodeInt128 function](..\sdplib\nf-sdplib-sdpcreatenodeint128.md) | The Bluetooth SdpCreateNodeInt128 function is used to allocate and initialize an SDP_NODE structure to a 128-bit integer type. |
| [SdpCreateNodeUInt16 function](..\sdplib\nf-sdplib-sdpcreatenodeuint16~r1.md) | The Bluetooth SdpCreateNodeUInt16 function is used to allocate and initialize an SDP_NODE structure to an unsigned 16-bit integer type. |
| [SdpCreateNodeUUID128 function](..\sdplib\nf-sdplib-sdpcreatenodeuuid128~r1.md) | The Bluetooth SdpCreateNodeUUID128 function is used to allocate and initialize an SDP_NODE structure to a 128-bit UUID type. |
| [SdpCreateNodeBoolean function](..\sdplib\nf-sdplib-sdpcreatenodeboolean~r1.md) | The Bluetooth SdpCreateNodeBoolean function is used to allocate and initialize an SDP_NODE structure to a Boolean type. |
| [SdpCreateNodeTree function](..\sdplib\nf-sdplib-sdpcreatenodetree~r1.md) | The Bluetooth SdpCreateNodeTree function is used to allocate an empty root SDP_TREE_ROOT_NODE structure. |
| [SdpCreateNodeInt32 function](..\sdplib\nf-sdplib-sdpcreatenodeint32~r1.md) | The Bluetooth SdpCreateNodeInt32 function is used to allocate and initialize an SDP_NODE structure to a 32-bit integer type. |
| [SdpCreateNodeUrl function](..\sdplib\nf-sdplib-sdpcreatenodeurl.md) | The Bluetooth SdpCreateNodeUrl function is used to allocate and initialize an SDP_NODE structure to a URL type. |
| [SdpCreateNodeUUID16 function](..\sdplib\nf-sdplib-sdpcreatenodeuuid16~r1.md) | The Bluetooth SdpCreateNodeUUID16 function is used to allocate and initialize an SDP_NODE structure to a 16-bit UUID type. |
| [SdpAppendNodeToContainerNode function](..\sdplib\nf-sdplib-sdpappendnodetocontainernode.md) | The Bluetooth SdpAppendNodeToContainerNode function is used to attach an SDP node to a sequence or alternative SDP node. |
| [SdpCreateNodeUInt32 function](..\sdplib\nf-sdplib-sdpcreatenodeuint32.md) | The Bluetooth SdpCreateNodeUInt32 function is used to allocate and initialize an SDP_NODE structure to an unsigned 32-bit integer type. |
| [SdpCreateNodeUInt8 function](..\sdplib\nf-sdplib-sdpcreatenodeuint8~r1.md) | The Bluetooth SdpCreateNodeUInt8 function is used to allocate and initialize an SDP_NODE structure to an unsigned 8-bit integer type. |
| [SdpCreateNodeSequence function](..\sdplib\nf-sdplib-sdpcreatenodesequence~r1.md) | The Bluetooth SdpCreateNodeSequence function is used to create an empty sequence SDP node. |
| [SdpCreateNodeString function](..\sdplib\nf-sdplib-sdpcreatenodestring~r1.md) | The Bluetooth SdpCreateNodeString function is used to allocate and initialize an SDP_NODE structure to a string type. |
| [SdpCreateNodeNil function](..\sdplib\nf-sdplib-sdpcreatenodenil.md) | The Bluetooth SdpCreateNodeNil function is used to allocate and initialize an SDP_NODE structure to an empty node type. |
| [SdpCreateNodeTree function](..\sdplib\nf-sdplib-sdpcreatenodetree.md) | The Bluetooth SdpCreateNodeTree function is used to allocate an empty root SDP_TREE_ROOT_NODE structure. |
| [SdpCreateNodeInt32 function](..\sdplib\nf-sdplib-sdpcreatenodeint32.md) | The Bluetooth SdpCreateNodeInt32 function is used to allocate and initialize an SDP_NODE structure to a 32-bit integer type. |
| [SdpCreateNodeUInt64 function](..\sdplib\nf-sdplib-sdpcreatenodeuint64~r1.md) | The Bluetooth SdpCreateNodeUInt64 function is used to allocate and initialize an SDP_NODE structure to an unsigned 64-bit integer type. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SDP_NODE_DATA structure](..\sdpnode\ns-sdpnode--sdp-node-data.md) | The SDP_NODE_DATA union holds the data of an element in a tree-based representation of an SDP record. |
| [SDP_NODE_HEADER structure](..\sdpnode\ns-sdpnode--sdp-node-header.md) | The SDP_NODE_HEADER structure holds information about an element in a tree-based representation of an SDP record. |
| [SDP_NODE structure](..\sdpnode\ns-sdpnode--sdp-node.md) | The SDP_NODE structure holds information about an element in a tree-based representation of an SDP record. |
| [SDP_TREE_ROOT_NODE structure](..\sdpnode\ns-sdpnode--sdp-tree-root-node.md) | The SDP_TREE_ROOT_NODE structure is the root element of a tree-based representation of an SDP record. |


This technology is in the following headers:


| Header        | 

| [bthddi](..\bthddi\~PORTAL~bthddi.md) | 

| [bthioctl](..\bthioctl\~PORTAL~bthioctl.md) | 

| [bthsdpddi](..\bthsdpddi\~PORTAL~bthsdpddi.md) | 

| [bthxddi](..\bthxddi\~PORTAL~bthxddi.md) | 

| [sdplib](..\sdplib\~PORTAL~sdplib.md) | 

| [sdpnode](..\sdpnode\~PORTAL~sdpnode.md) | 
