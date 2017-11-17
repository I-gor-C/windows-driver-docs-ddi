# Declarations in the nfpdrivers technology
This technology  contains these programming interfaces:

Enum

| Title        | Description    |
| ------------- |:-------------:|
| [NFC_CX_NFCIP_TGT_MODE_CONFIG enumeration](..\nfccx\ne-nfccx--nfc-cx-nfcip-tgt-mode-config.md) | The NFC_CX_NFCIP_TGT_MODE_CONFIG enumeration specifies NFC-IP target mode. |
| [NFC_CX_DEVICE_MODE enumeration](..\nfccx\ne-nfccx--nfc-cx-device-mode.md) | Specifies device mode flags. |
| [NFC_CX_TRANSPORT_TYPE enumeration](..\nfccx\ne-nfccx--nfc-cx-transport-type.md) | The NFC_CX_TRANSPORT_TYPE enumeration specifies transport types. |
| [NFC_CX_CE_MODE_CONFIG enumeration](..\nfccx\ne-nfccx--nfc-cx-ce-mode-config.md) | This enumeration specifies CE listening mode flags. |
| [NFC_CX_DRIVER_FLAGS enumeration](..\nfccx\ne-nfccx--nfc-cx-driver-flags.md) | Specifies run-time driver flags. |
| [NFC_CX_POLL_BAILOUT_CONFIG enumeration](..\nfccx\ne-nfccx--nfc-cx-poll-bailout-config.md) | The NFC_CX_POLL_BAILOUT_CONFIG enumeration specifies poll mode bail out. |
| [NFC_CX_NFCIP_MODE_CONFIG enumeration](..\nfccx\ne-nfccx--nfc-cx-nfcip-mode-config.md) | The NFC_CX_NFCIP_MODE_CONFIG enumeration specifies the NFC-IP initiator mode. |
| [NFC_CX_SEQUENCE enumeration](..\nfccx\ne-nfccx--nfc-cx-sequence.md) | The NFC_CX_SEQUENCE enumeration specifies sequences. |
| [NFC_CX_HOST_ACTION enumeration](..\nfccx\ne-nfccx--nfc-cx-host-action.md) | The NFC_CX_HOST_ACTION enumeration specifies host actions. |
| [NFC_CX_POLL_MODE_CONFIG enumeration](..\nfccx\ne-nfccx--nfc-cx-poll-mode-config.md) | The NFC_CX_POLL_MODE_CONFIG enumeration specifies poll mode. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [NfcCxDeviceDeinitialize function](..\nfccx\nf-nfccx-nfccxdevicedeinitialize.md) | Called by the client driver after a WDF device has been created during the AddDevice routine. |
| [NFC_CX_RF_DISCOVERY_CONFIG_INIT function](..\nfccx\nf-nfccx-nfc-cx-rf-discovery-config-init.md) | The NFC_CX_RF_DISCOVERY_CONFIG_INIT function initializes the NFC_CX_RF_DISCOVERY_CONFIG structure. |
| [NfcCxSetRfDiscoveryConfig function](..\nfccx\nf-nfccx-nfccxsetrfdiscoveryconfig.md) | Called by the client driver to configure the RF discovery parameters. |
| [NfcCxHardwareEvent function](..\nfccx\nf-nfccx-nfccxhardwareevent.md) | Called by the client driver when a hardware event occurs like D0Entry and D0Exit callbacks to start or stop the device. For drivers that require firmware download on initialization or boot-up, it is recommended to move this call to a separate work item. However, the client driver is responsible for the following |
| [NfcCxNciReadNotification function](..\nfccx\nf-nfccx-nfccxncireadnotification.md) | Called by the client driver when a read packet is available. |
| [NFC_CX_CLIENT_CONFIG_INIT function](..\nfccx\nf-nfccx-nfc-cx-client-config-init.md) | The NFC_CX_CLIENT_CONFIG_INIT function initializes the NFC_CX_CLIENT_CONFIG structure. |
| [NFC_CX_LLCP_CONFIG_INIT function](..\nfccx\nf-nfccx-nfc-cx-llcp-config-init.md) | The NFC_CX_LLCP_CONFIG_INIT function initializes the NFC_CX_LLCP_CONFIG structure. |
| [NfcCxDeviceInitialize function](..\nfccx\nf-nfccx-nfccxdeviceinitialize.md) | Called by the client driver after a WDF device has been created during the AddDevice routine. |
| [NfcCxSetLlcpConfig function](..\nfccx\nf-nfccx-nfccxsetllcpconfig.md) | Called by the client driver to configure the LLCP parameters. |
| [NfcCxRegisterSequenceHandler function](..\nfccx\nf-nfccx-nfccxregistersequencehandler.md) | Called by the client driver during initialization to register for handling specific sequences. |
| [NfcCxUnregisterSequenceHandler function](..\nfccx\nf-nfccx-nfccxunregistersequencehandler.md) | Called by the client driver during device shutdown to unregister for the previously registered sequence handler callback. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [NFC_CX_HARDWARE_EVENT structure](..\nfccx\ns-nfccx--nfc-cx-hardware-event.md) | The NFC_CX_HARDWARE_EVENT structure is an input parameter to NfcCxHardwareEvent. |
| [NFC_CX_CLIENT_CONFIG structure](..\nfccx\ns-nfccx--nfc-cx-client-config.md) | The NFC_CX_CLIENT_CONFIG structure is an input parameter to NfcCxDeviceInitConfig. |
| [NFCCX_DRIVER_GLOBALS structure](..\nfccx\ns-nfccx--nfccx-driver-globals.md) | . |
| [NFC_CX_RF_DISCOVERY_CONFIG structure](..\nfccx\ns-nfccx--nfc-cx-rf-discovery-config.md) | The NFC_CX_RF_DISCOVERY_CONFIG structure contains RF discovery configuration settings. Discovery configuration should be completed during initialization after calling NfcDxDeviceInitialize, otherwise an error is returned. |
| [NFC_CX_LLCP_CONFIG structure](..\nfccx\ns-nfccx--nfc-cx-llcp-config.md) | The NFC_CX_LLCP_CONFIG structure is an input parameter to NfcCxSetLlcpConfig. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_NFC_CX_SEQUENCE_HANDLER callback](..\nfccx\nc-nfccx-evt-nfc-cx-sequence-handler.md) | Called by the NFC CX to notify the client driver to handle the specific registered sequence. |
| [EVT_NFC_CX_WRITE_NCI_PACKET callback](..\nfccx\nc-nfccx-evt-nfc-cx-write-nci-packet.md) | Called by the NFC CX to send a write packet to the client driver. |
| [EVT_NFC_CX_DEVICE_IO_CONTROL callback](..\nfccx\nc-nfccx-evt-nfc-cx-device-io-control.md) | Called by the NFC CX to send an unhandled IOCTL to the client driver. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SECURE_ELEMENT_ENDPOINT_LIST structure](..\nfcsedev\ns-nfcsedev--secure-element-endpoint-list.md) | The output parameter for IOCTL_NFCSE_ENUM_ENDPOINTS. |
| [SECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD structure](..\nfcsedev\ns-nfcsedev--secure-element-hce-activation-payload.md) | . |
| [SECURE_ELEMENT_ROUTING_TABLE structure](..\nfcsedev\ns-nfcsedev--secure-element-routing-table.md) | SECURE_ELEMENT_ROUTING_TABLE is an input parameter for IOCTL_NFCSE_SET_ROUTING_TABLE. |
| [SECURE_ELEMENT_EVENT_SUBSCRIPTION_INFO structure](..\nfcsedev\ns-nfcsedev--secure-element-event-subscription-info.md) | The SECURE_ELEMENT_EVENT_SUBSCRIPTION_INFO structure is an input parameter to IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT. |
| [SECURE_ELEMENT_HCE_DATA_PACKET structure](..\nfcsedev\ns-nfcsedev--secure-element-hce-data-packet.md) | SECURE_ELEMENT_HCE_DATA_PACKET is an input buffer to IOCTL_NFCSE_HCE_REMOTE_SEND and output buffer for IOCTL_NFCSE_HCE_REMOTE_RECV. |
| [SECURE_ELEMENT_NFCC_CAPABILITIES structure](..\nfcsedev\ns-nfcsedev--secure-element-nfcc-capabilities.md) | SECURE_ELEMENT_NFCC_CAPABILITIES contains NFC controller capabilities. |
| [SECURE_ELEMENT_EVENT_INFO structure](..\nfcsedev\ns-nfcsedev--secure-element-event-info.md) | This structure provides information about a secure element event. |
| [SECURE_ELEMENT_SET_CARD_EMULATION_MODE_INFO structure](..\nfcsedev\ns-nfcsedev--secure-element-set-card-emulation-mode-info.md) | SECURE_ELEMENT_SET_CARD_EMULATION_MODE_INFO is the input parameter for IOCTL_NFCSE_SET_CARD_EMULATION_MODE. |
| [SECURE_ELEMENT_ENDPOINT_INFO structure](..\nfcsedev\ns-nfcsedev--secure-element-endpoint-info.md) | SECURE_ELEMENT_ENDPOINT_INFO is a member of SECURE_ELEMENT_ENDPOINT_LIST. |
| [SECURE_ELEMENT_ROUTING_TABLE_ENTRY structure](..\nfcsedev\ns-nfcsedev--secure-element-routing-table-entry.md) | SECURE_ELEMENT_ROUTING_TABLE_ENTRY is a member of SECURE_ELEMENT_ROUTING_TABLE. |
| [SECURE_ELEMENT_AID_ROUTING_INFO structure](..\nfcsedev\ns-nfcsedev--secure-element-aid-routing-info.md) | SECURE_ELEMENT_AID_ROUTING_INFO is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [SECURE_ELEMENT_CARD_EMULATION_MODE enumeration](..\nfcsedev\ne-nfcsedev--secure-element-card-emulation-mode.md) | This enumeration indicates the card emulation mode of a secure element. |
| [SECURE_ELEMENT_ROUTING_TYPE enumeration](..\nfcsedev\ne-nfcsedev--secure-element-routing-type.md) | SECURE_ELEMENT_ROUTING_TYPE is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY. |
| [SECURE_ELEMENT_TYPE enumeration](..\nfcsedev\ne-nfcsedev--secure-element-type.md) | Indicates the type of a secure element. |
| [SECURE_ELEMENT_EVENT_TYPE enumeration](..\nfcsedev\ne-nfcsedev--secure-element-event-type.md) | Indicates the type of secure element events. |


This technology is in the following headers:


| Header        | 

| [ncidef](..\ncidef\~PORTAL~ncidef.md) | 

| [nfccx](..\nfccx\~PORTAL~nfccx.md) | 

| [nfcradiodev](..\nfcradiodev\~PORTAL~nfcradiodev.md) | 

| [nfcsedev](..\nfcsedev\~PORTAL~nfcsedev.md) | 

| [nfpdev](..\nfpdev\~PORTAL~nfpdev.md) | 

| [winsmcrd](..\winsmcrd\~PORTAL~winsmcrd.md) | 
