# Declarations in the bthddi header
This header Bthddi contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [IS_CODING_FORMAT_RESERVED function](nf-bthddi-is-coding-format-reserved.md) | TBD |
| [IS_CO_TYPE_REQUIRED function](nf-bthddi-is-co-type-required.md) | TBD |
| [IS_PCM_FORMAT_RESERVED function](nf-bthddi-is-pcm-format-reserved.md) | TBD |
| [IS_CO_TYPE_HINT function](nf-bthddi-is-co-type-hint.md) | TBD |
| [ALL_RESERVED_DATA_FORMAT_BITS_ARE_ZERO function](nf-bthddi-all-reserved-data-format-bits-are-zero.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [BRB_SCO_UNREGISTER_SERVER structure](ns-bthddi--brb-sco-unregister-server.md) | TBD |
| [CHANNEL_CONFIG_PARAMETERS_ENHANCED structure](ns-bthddi--channel-config-parameters-enhanced.md) | The CHANNEL_CONFIG_PARAMETERS_ENHANCED structure describes configuration parameters for inbound and outbound directions of an L2CAP channel. |
| [BRB_L2CA_PING structure](ns-bthddi--brb-l2ca-ping.md) | TBD |
| [BASEBAND_CHANNEL_INFO structure](ns-bthddi--baseband-channel-info.md) | The BASEBAND_CHANNEL_INFO structure describes output information about the baseband channel that is used by a SCO link after a BRB_GET_CHANNEL_INFO BRB completes. |
| [BRB_ACL_ENTER_ACTIVE_MODE structure](ns-bthddi--brb-acl-enter-active-mode.md) | TBD |
| [BRB_GET_LOCAL_BD_ADDR structure](ns-bthddi--brb-get-local-bd-addr.md) | TBD |
| [CHANNEL_CONFIG_RESULTS_ENHANCED structure](ns-bthddi--channel-config-results-enhanced.md) | The CHANNEL_CONFIG_RESULTS_ENHANCED structure describes configuration parameters and the buffer size of any extra option for the inbound and outbound directions of an L2CAP channel. |
| [BRB_SCO_GET_CHANNEL_INFO structure](ns-bthddi--brb-sco-get-channel-info.md) | TBD |
| [CHANNEL_CONFIG_RESULTS structure](ns-bthddi--channel-config-results.md) | The CHANNEL_CONFIG_RESULTS structure contains configuration parameters and the buffer size of any extra options for the inbound and outbound directions of a L2CAP channel. |
| [BRB_SCO_REGISTER_SERVER structure](ns-bthddi--brb-sco-register-server.md) | TBD |
| [BRB_HEADER structure](ns-bthddi--brb-header.md) | The BRB_HEADER structure contains header information about a Bluetooth request block (BRB), including information about the BRB type that the Bluetooth driver stack uses to determine which kind of BRB type to process. |
| [BRB_L2CA_UPDATE_CHANNEL structure](ns-bthddi--brb-l2ca-update-channel.md) | TBD |
| [BRB_SCO_FLUSH_CHANNEL structure](ns-bthddi--brb-sco-flush-channel.md) | TBD |
| [INDICATION_PARAMETERS_ENHANCED structure](ns-bthddi--indication-parameters-enhanced~r1.md) | The INDICATION_PARAMETERS_ENHANCED structure is passed as the Parameters parameter to a profile driver's enhanced L2CAP Callback Function. |
| [L2CAP_FLOWSPEC structure](ns-bthddi--l2cap-flowspec.md) | TBD |
| [BRB_L2CA_REGISTER_SERVER structure](ns-bthddi--brb-l2ca-register-server.md) | TBD |
| [SCO_INDICATION_PARAMETERS structure](ns-bthddi--sco-indication-parameters.md) | The SCO_INDICATION_PARAMETERS structure describes indication parameters about a SCO connect or disconnect notification. |
| [BRB_PSM structure](ns-bthddi--brb-psm.md) | TBD |
| [CHANNEL_CONFIG_PARAMETERS structure](ns-bthddi--channel-config-parameters.md) | The CHANNEL_CONFIG_PARAMETERS structure contains configuration parameters for inbound and outbound directions of a L2CAP channel. |
| [CO_HEADER structure](ns-bthddi--co-header.md) | The CO_HEADER structure is used to specify values for the Header member of the L2CAP_CONFIG_OPTION structure. |
| [INDICATION_PARAMETERS structure](ns-bthddi--indication-parameters.md) | TBD |
| [BRB_L2CA_UNREGISTER_SERVER structure](ns-bthddi--brb-l2ca-unregister-server.md) | TBD |
| [BRB structure](ns-bthddi--brb.md) | Profile drivers use Bluetooth request blocks (BRBs), to send requests to the Bluetooth driver stack. The BRB structure defines the format for all supported commands that can be sent to a Bluetooth device. |
| [L2CAP_CONFIG_OPTION structure](ns-bthddi--l2cap-config-option.md) | An array of L2CAP_CONFIG_OPTION structures is used to specify values for the ExtraOptions member of the CHANNEL_CONFIG_PARAMETERS, _BRB_L2CA_OPEN_CHANNEL, and INDICATION_PARAMETERS structures. |
| [BRB_L2CA_OPEN_CHANNEL structure](ns-bthddi--brb-l2ca-open-channel.md) | TBD |
| [L2CAP_CONFIG_RANGE structure](ns-bthddi--l2cap-config-range.md) | The L2CAP_CONFIG_RANGE structure is used to specify a range of possible values for the FlushTO member of the _BRB_L2CA_OPEN_CHANNEL structure during incoming requests. |
| [BRB_SCO_GET_SYSTEM_INFO structure](ns-bthddi--brb-sco-get-system-info.md) | TBD |
| [BRB_ACL_GET_MODE structure](ns-bthddi--brb-acl-get-mode.md) | TBD |
| [L2CAP_CONFIG_VALUE_RANGE structure](ns-bthddi--l2cap-config-value-range.md) | The L2CAP_CONFIG_VALUE_RANGE structure is used to specify values for the Mtu and FlushTO members of the _BRB_L2CA_OPEN_CHANNEL structure. |
| [BRB_SCO_CLOSE_CHANNEL structure](ns-bthddi--brb-sco-close-channel.md) | TBD |
| [BRB_SCO_OPEN_CHANNEL structure](ns-bthddi--brb-sco-open-channel.md) | TBD |
| [L2CAP_EXTENDED_FLOW_SPEC structure](ns-bthddi--l2cap-extended-flow-spec.md) | The L2CAP_EXTENDED_FLOW_SPEC is reserved for future use. |
| [BRB_GET_DEVICE_INTERFACE_STRING structure](ns-bthddi--brb-get-device-interface-string.md) | TBD |
| [INDICATION_PARAMETERS structure](ns-bthddi--indication-parameters~r1.md) | The INDICATION_PARAMETERS structure is passed as the Parameters parameter to a profile driver's L2CAP Callback Function. |
| [BRB_L2CA_OPEN_ENHANCED_CHANNEL structure](ns-bthddi--brb-l2ca-open-enhanced-channel.md) | TBD |
| [L2CAP_RETRANSMISSION_AND_FLOW_CONTROL structure](ns-bthddi--l2cap-retransmission-and-flow-control.md) | The L2CAP_RETRANSMISSION_AND_FLOW_CONTROL structure describes configuration parameters for enhanced retransmission mode and streaming mode. |
| [BRB_L2CA_CLOSE_CHANNEL structure](ns-bthddi--brb-l2ca-close-channel.md) | TBD |
| [INDICATION_PARAMETERS_ENHANCED structure](ns-bthddi--indication-parameters-enhanced.md) | TBD |
| [BRB_L2CA_ACL_TRANSFER structure](ns-bthddi--brb-l2ca-acl-transfer.md) | TBD |
| [BTH_ENUMERATOR_INFO structure](ns-bthddi--bth-enumerator-info.md) | The BTH_ENUMERATOR_INFO structure contains information about an underlying device and the service that caused the Plug and Play (PnP) manager to load the profile driver. |
| [BRB_SCO_TRANSFER structure](ns-bthddi--brb-sco-transfer.md) | TBD |
| [BTH_PROFILE_DRIVER_INTERFACE structure](ns-bthddi--bth-profile-driver-interface.md) | The BTH_PROFILE_DRIVER_INTERFACE structure provides functions to allocate, free, initialize, and reuse BRBs, and to determine the currently installed Bluetooth version. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [PCM_DATA_FORMAT enumeration](ne-bthddi--pcm-data-format.md) | TBD |
| [BRB_VERSION enumeration](ne-bthddi--brb-version.md) | TBD |
| [SCO_RETRANSMISSION_EFFORT enumeration](ne-bthddi--sco-retransmission-effort.md) | The SCO_RETRANSMISSION_EFFORT enumeration type is used to determine the retransmission policies of a SCO channel. |
| [BRB_TYPE enumeration](ne-bthddi--brb-type.md) | The BRB_TYPE enumeration type is used to determine the Bluetooth request block when a profile driver builds and sends a BRB. |
| [ENUMERATOR_ACTION enumeration](ne-bthddi--enumerator-action.md) | TBD |
| [ENUMERATOR_TYPE enumeration](ne-bthddi--enumerator-type.md) | The ENUMERATOR_TYPE enumeration type is used to determine whether the enumerated device is associated with a service or a protocol. The ENUMERATOR_TYPE enumeration is intended for internal use only and should not be used by profile drivers. |
| [INDICATION_CODE enumeration](ne-bthddi--indication-code.md) | The INDICATION_CODE enumeration type indicates to a profile driver what type of L2CAP event has occurred. |
| [INDICATION_CODE enumeration](ne-bthddi--indication-code~r1.md) | The INDICATION_CODE enumeration type indicates to a profile driver what type of L2CAP event has occurred. |
| [ACL_MODE enumeration](ne-bthddi--acl-mode.md) | The ACL_MODE enumeration type is used to list the possible states of an ACL connection. |
| [SCO_INDICATION_CODE enumeration](ne-bthddi--sco-indication-code.md) | The SCO_INDICATION_CODE enumeration type describes the type of an incoming SCO connection or bonding state change. The Bluetooth driver stack passes a value from this enumeration in the Indication argument of a profile driver's SCO Callback Function. |
| [SCO_DISCONNECT_REASON enumeration](ne-bthddi--sco-disconnect-reason.md) | The SCO_DISCONNECT_REASON enumeration type gives the reason an SCO channel has been disconnected. |
| [CODING_FORMAT enumeration](ne-bthddi--coding-format.md) | TBD |
| [L2CAP_DISCONNECT_REASON enumeration](ne-bthddi--l2cap-disconnect-reason.md) | The L2CAP_DISCONNECT_REASON enumeration type gives the reason an L2CAP channel has been disconnected. |
| [SCO_LINK_TYPE enumeration](ne-bthddi--sco-link-type.md) | The SCO_LINK_TYPE enumeration type describes the type of link used by the SCO connection when a ScoIndicationRemoteConnect indication event is processed. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFNBTH_ALLOCATE_BRB callback](nc-bthddi-pfnbth-allocate-brb.md) | The BthAllocateBrb function allocates a Bluetooth request block (BRB) of the specified type. |
| [PFNBTH_REUSE_BRB callback](nc-bthddi-pfnbth-reuse-brb.md) | The BthReuseBrb function reinitializes a Bluetooth request block (BRB) to be reused. |
| [PFNBTH_INITIALIZE_BRB callback](nc-bthddi-pfnbth-initialize-brb.md) | The BthInitializeBrb function initializes a Bluetooth request block (BRB) allocated on the local stack. |
| [PFNBTH_IS_BLUETOOTH_VERSION_AVAILABLE callback](nc-bthddi-pfnbth-is-bluetooth-version-available.md) | The IsBluetoothVersionAvailable function checks whether a given Bluetooth version is supported by the operating system. |
| [PFNSCO_INDICATION_CALLBACK callback](nc-bthddi-pfnsco-indication-callback.md) | Profile drivers implement a SCO callback function to provide the Bluetooth driver stack with a mechanism to notify the profile driver about incoming SCO connection requests from remote devices, and any changes to the status of a currently open SCO connection. |
| [PFNBTHPORT_INDICATION_CALLBACK_ENHANCED callback](nc-bthddi-pfnbthport-indication-callback-enhanced.md) | Profile drivers implement an enhanced L2CAP callback function to provide the Bluetooth driver stack with a mechanism to notify the profile driver about any changes to the status of a currently open L2CAP or eL2CAP connection. |
| [PFNBTHPORT_INDICATION_CALLBACK callback](nc-bthddi-pfnbthport-indication-callback.md) | Profile drivers implement a L2CAP callback function to provide the Bluetooth driver stack with a mechanism to notify the profile driver about incoming L2CAP connection requests from remote devices, and any changes to the status of a currently open L2CAP connection. |
| [PFNBTH_FREE_BRB callback](nc-bthddi-pfnbth-free-brb.md) | The BthFreeBrb function frees a Bluetooth request block (BRB) that was allocated previously with BthAllocateBrb. |

This header is used in these topics:

- [bltooth](..content/_bltooth)
