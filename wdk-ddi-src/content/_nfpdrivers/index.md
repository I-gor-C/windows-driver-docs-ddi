# Near field communications (NFC)

Overview of the Near field communications (NFC) technology.

To develop Near field communications (NFC), you need these headers:

 * [nfccx.h](..\nfccx\index.md)
 * [nfcradiodev.h](..\nfcradiodev\index.md)
 * [nfcsedev.h](..\nfcsedev\index.md)
 * [nfpdev.h](..\nfpdev\index.md)
 * [winsmcrd.h](..\winsmcrd\index.md)

For the programming guide, see [Near field communications (NFC)](===404===https://docs.microsoft.com/en-us/windows-hardware/drivers/nfpdrivers).

## Functions

| Title   | Description   |
| ---- |:---- |
| [NFC_CX_CLIENT_CONFIG_INIT function](..\nfccx\nf-nfccx-nfc-cx-client-config-init.md) | The NFC_CX_CLIENT_CONFIG_INIT function initializes the NFC_CX_CLIENT_CONFIG structure. |
| [NFC_CX_LLCP_CONFIG_INIT function](..\nfccx\nf-nfccx-nfc-cx-llcp-config-init.md) | The NFC_CX_LLCP_CONFIG_INIT function initializes the NFC_CX_LLCP_CONFIG structure. |
| [NFC_CX_RF_DISCOVERY_CONFIG_INIT function](..\nfccx\nf-nfccx-nfc-cx-rf-discovery-config-init.md) | The NFC_CX_RF_DISCOVERY_CONFIG_INIT function initializes the NFC_CX_RF_DISCOVERY_CONFIG structure. |
| [NfcCxDeviceDeinitialize function](..\nfccx\nf-nfccx-nfccxdevicedeinitialize.md) | Called by the client driver after a WDF device has been created during the AddDevice routine. |
| [NfcCxDeviceInitialize function](..\nfccx\nf-nfccx-nfccxdeviceinitialize.md) | Called by the client driver after a WDF device has been created during the AddDevice routine. |
| [NfcCxHardwareEvent function](..\nfccx\nf-nfccx-nfccxhardwareevent.md) | Called by the client driver when a hardware event occurs like D0Entry and D0Exit callbacks to start or stop the device. For drivers that require firmware download on initialization or boot-up, it is recommended to move this call to a separate work item. However, the client driver is responsible for the following |
| [NfcCxNciReadNotification function](..\nfccx\nf-nfccx-nfccxncireadnotification.md) | Called by the client driver when a read packet is available. |
| [NfcCxRegisterSequenceHandler function](..\nfccx\nf-nfccx-nfccxregistersequencehandler.md) | Called by the client driver during initialization to register for handling specific sequences. |
| [NfcCxSetLlcpConfig function](..\nfccx\nf-nfccx-nfccxsetllcpconfig.md) | Called by the client driver to configure the LLCP parameters. |
| [NfcCxSetRfDiscoveryConfig function](..\nfccx\nf-nfccx-nfccxsetrfdiscoveryconfig.md) | Called by the client driver to configure the RF discovery parameters. |
| [NfcCxUnregisterSequenceHandler function](..\nfccx\nf-nfccx-nfccxunregistersequencehandler.md) | Called by the client driver during device shutdown to unregister for the previously registered sequence handler callback. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [EVT_NFC_CX_DEVICE_IO_CONTROL callback](..\nfccx\nc-nfccx-evt-nfc-cx-device-io-control.md) | Called by the NFC CX to send an unhandled IOCTL to the client driver. |
| [EVT_NFC_CX_SEQUENCE_HANDLER callback](..\nfccx\nc-nfccx-evt-nfc-cx-sequence-handler.md) | Called by the NFC CX to notify the client driver to handle the specific registered sequence. |
| [EVT_NFC_CX_WRITE_NCI_PACKET callback](..\nfccx\nc-nfccx-evt-nfc-cx-write-nci-packet.md) | Called by the NFC CX to send a write packet to the client driver. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [NFCCX_DRIVER_GLOBALS structure](..\nfccx\ns-nfccx--nfccx-driver-globals.md) | . |
| [NFCRM_RADIO_STATE structure](..\nfcradiodev\ns-nfcradiodev--nfcrm-radio-state.md) | This structure is used to indicate the radio state. |
| [NFCRM_SET_RADIO_STATE structure](..\nfcradiodev\ns-nfcradiodev--nfcrm-set-radio-state.md) | This structure is used to set the radio state. The driver, in the case of airplane mode, has to persist the radio state and restore it when airplane mode is disabled. |
| [NFC_CX_CLIENT_CONFIG structure](..\nfccx\ns-nfccx--nfc-cx-client-config.md) | The NFC_CX_CLIENT_CONFIG structure is an input parameter to NfcCxDeviceInitConfig. |
| [NFC_CX_HARDWARE_EVENT structure](..\nfccx\ns-nfccx--nfc-cx-hardware-event.md) | The NFC_CX_HARDWARE_EVENT structure is an input parameter to NfcCxHardwareEvent. |
| [NFC_CX_LLCP_CONFIG structure](..\nfccx\ns-nfccx--nfc-cx-llcp-config.md) | The NFC_CX_LLCP_CONFIG structure is an input parameter to NfcCxSetLlcpConfig. |
| [NFC_CX_RF_DISCOVERY_CONFIG structure](..\nfccx\ns-nfccx--nfc-cx-rf-discovery-config.md) | The NFC_CX_RF_DISCOVERY_CONFIG structure contains RF discovery configuration settings. Discovery configuration should be completed during initialization after calling NfcDxDeviceInitialize, otherwise an error is returned. |
| [SCARD_IO_REQUEST structure](..\winsmcrd\ns-winsmcrd--scard-io-request.md) | This structure is used to identify a smart card I/O request. |
| [SECURE_ELEMENT_AID_ROUTING_INFO structure](..\nfcsedev\ns-nfcsedev--secure-element-aid-routing-info.md) | SECURE_ELEMENT_AID_ROUTING_INFO is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY. |
| [SECURE_ELEMENT_ENDPOINT_INFO structure](..\nfcsedev\ns-nfcsedev--secure-element-endpoint-info.md) | SECURE_ELEMENT_ENDPOINT_INFO is a member of SECURE_ELEMENT_ENDPOINT_LIST. |
| [SECURE_ELEMENT_ENDPOINT_LIST structure](..\nfcsedev\ns-nfcsedev--secure-element-endpoint-list.md) | The output parameter for IOCTL_NFCSE_ENUM_ENDPOINTS. |
| [SECURE_ELEMENT_EVENT_INFO structure](..\nfcsedev\ns-nfcsedev--secure-element-event-info.md) | This structure provides information about a secure element event. |
| [SECURE_ELEMENT_EVENT_SUBSCRIPTION_INFO structure](..\nfcsedev\ns-nfcsedev--secure-element-event-subscription-info.md) | The SECURE_ELEMENT_EVENT_SUBSCRIPTION_INFO structure is an input parameter to IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT. |
| [SECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD structure](..\nfcsedev\ns-nfcsedev--secure-element-hce-activation-payload.md) | . |
| [SECURE_ELEMENT_HCE_DATA_PACKET structure](..\nfcsedev\ns-nfcsedev--secure-element-hce-data-packet.md) | SECURE_ELEMENT_HCE_DATA_PACKET is an input buffer to IOCTL_NFCSE_HCE_REMOTE_SEND and output buffer for IOCTL_NFCSE_HCE_REMOTE_RECV. |
| [SECURE_ELEMENT_NFCC_CAPABILITIES structure](..\nfcsedev\ns-nfcsedev--secure-element-nfcc-capabilities.md) | SECURE_ELEMENT_NFCC_CAPABILITIES contains NFC controller capabilities. |
| [SECURE_ELEMENT_PROTO_ROUTING_INFO structure](..\nfcsedev\ns-nfcsedev--secure-element-proto-routing-info.md) | SECURE_ELEMENT_PROTO_ROUTING_INFO is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY. |
| [SECURE_ELEMENT_ROUTING_TABLE structure](..\nfcsedev\ns-nfcsedev--secure-element-routing-table.md) | SECURE_ELEMENT_ROUTING_TABLE is an input parameter for IOCTL_NFCSE_SET_ROUTING_TABLE. |
| [SECURE_ELEMENT_ROUTING_TABLE_ENTRY structure](..\nfcsedev\ns-nfcsedev--secure-element-routing-table-entry.md) | SECURE_ELEMENT_ROUTING_TABLE_ENTRY is a member of SECURE_ELEMENT_ROUTING_TABLE. |
| [SECURE_ELEMENT_SET_CARD_EMULATION_MODE_INFO structure](..\nfcsedev\ns-nfcsedev--secure-element-set-card-emulation-mode-info.md) | SECURE_ELEMENT_SET_CARD_EMULATION_MODE_INFO is the input parameter for IOCTL_NFCSE_SET_CARD_EMULATION_MODE. |
| [SECURE_ELEMENT_TECH_ROUTING_INFO structure](..\nfcsedev\ns-nfcsedev--secure-element-tech-routing-info.md) | SECURE_ELEMENT_TECH_ROUTING_INFO is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [NFC_CX_CE_MODE_CONFIG enumeration](..\nfccx\ne-nfccx--nfc-cx-ce-mode-config.md) | This enumeration specifies CE listening mode flags. |
| [NFC_CX_DEVICE_MODE enumeration](..\nfccx\ne-nfccx--nfc-cx-device-mode.md) | Specifies device mode flags. |
| [NFC_CX_DRIVER_FLAGS enumeration](..\nfccx\ne-nfccx--nfc-cx-driver-flags.md) | Specifies run-time driver flags. |
| [NFC_CX_HOST_ACTION enumeration](..\nfccx\ne-nfccx--nfc-cx-host-action.md) | The NFC_CX_HOST_ACTION enumeration specifies host actions. |
| [NFC_CX_NFCIP_MODE_CONFIG enumeration](..\nfccx\ne-nfccx--nfc-cx-nfcip-mode-config.md) | The NFC_CX_NFCIP_MODE_CONFIG enumeration specifies the NFC-IP initiator mode. |
| [NFC_CX_NFCIP_TGT_MODE_CONFIG enumeration](..\nfccx\ne-nfccx--nfc-cx-nfcip-tgt-mode-config.md) | The NFC_CX_NFCIP_TGT_MODE_CONFIG enumeration specifies NFC-IP target mode. |
| [NFC_CX_POLL_BAILOUT_CONFIG enumeration](..\nfccx\ne-nfccx--nfc-cx-poll-bailout-config.md) | The NFC_CX_POLL_BAILOUT_CONFIG enumeration specifies poll mode bail out. |
| [NFC_CX_POLL_MODE_CONFIG enumeration](..\nfccx\ne-nfccx--nfc-cx-poll-mode-config.md) | The NFC_CX_POLL_MODE_CONFIG enumeration specifies poll mode. |
| [NFC_CX_SEQUENCE enumeration](..\nfccx\ne-nfccx--nfc-cx-sequence.md) | The NFC_CX_SEQUENCE enumeration specifies sequences. |
| [NFC_CX_TRANSPORT_TYPE enumeration](..\nfccx\ne-nfccx--nfc-cx-transport-type.md) | The NFC_CX_TRANSPORT_TYPE enumeration specifies transport types. |
| [SECURE_ELEMENT_CARD_EMULATION_MODE enumeration](..\nfcsedev\ne-nfcsedev--secure-element-card-emulation-mode.md) | This enumeration indicates the card emulation mode of a secure element. |
| [SECURE_ELEMENT_EVENT_TYPE enumeration](..\nfcsedev\ne-nfcsedev--secure-element-event-type.md) | Indicates the type of secure element events. |
| [SECURE_ELEMENT_ROUTING_TYPE enumeration](..\nfcsedev\ne-nfcsedev--secure-element-routing-type.md) | SECURE_ELEMENT_ROUTING_TYPE is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY. |
| [SECURE_ELEMENT_TYPE enumeration](..\nfcsedev\ne-nfcsedev--secure-element-type.md) | Indicates the type of a secure element. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_NFCRM_QUERY_RADIO_STATE IOCTL](..\nfcradiodev\ni-nfcradiodev-ioctl-nfcrm-query-radio-state.md) | This IOCTL is used by the radio management application or service to query the current radio power state of the proximity device. |
| [IOCTL_NFCRM_SET_RADIO_STATE IOCTL](..\nfcradiodev\ni-nfcradiodev-ioctl-nfcrm-set-radio-state.md) | This IOCTL is used by the radio management application or service to set the radio power state of the proximity device. |
| [IOCTL_NFCSERM_QUERY_RADIO_STATE IOCTL](..\nfcradiodev\ni-nfcradiodev-ioctl-nfcserm-query-radio-state.md) | This IOCTL is used by the SE radio management application or service to query the current radio power state of the proximity device. |
| [IOCTL_NFCSERM_SET_RADIO_STATE IOCTL](..\nfcradiodev\ni-nfcradiodev-ioctl-nfcserm-set-radio-state.md) | This IOCTL is used by the SE radio management application or service to query the current radio power state of the proximity device. |
| [IOCTL_NFCSE_ENUM_ENDPOINTS IOCTL](..\nfcsedev\ni-nfcsedev-ioctl-nfcse-enum-endpoints.md) | Returns information regarding the list of all the secure elements attached to the NFC controller. |
| [IOCTL_NFCSE_GET_NEXT_EVENT IOCTL](..\nfcsedev\ni-nfcsedev-ioctl-nfcse-get-next-event.md) | The IOCTL_NFCSE_GET_NEXT_EVENT control code returns the next event available in the buffer, or if there are no more buffered events remains pending until a secure element event is available. The event details must then be returned to the caller. |
| [IOCTL_NFCSE_GET_NFCC_CAPABILITIES IOCTL](..\nfcsedev\ni-nfcsedev-ioctl-nfcse-get-nfcc-capabilities.md) | The IOCTL_NFCSE_GET_NFCC_CAPABILITIES control code returns information about the current NFC controller capabilities, including the maximum Listen Mode Routing table size (defined in section 4.2 of the NFC Controller Interface (NCI) Technical Specification Version 1.1) and supported routing modes. |
| [IOCTL_NFCSE_GET_ROUTING_TABLE IOCTL](..\nfcsedev\ni-nfcsedev-ioctl-nfcse-get-routing-table.md) | Returns information regarding the current configuration of listen mode routing table. |
| [IOCTL_NFCSE_HCE_REMOTE_RECV IOCTL](..\nfcsedev\ni-nfcsedev-ioctl-nfcse-hce-remote-recv.md) | Either returns the next data buffer available, or if there are no more buffered data, the request shall stay pending until an APDU buffer is available for reading. |
| [IOCTL_NFCSE_HCE_REMOTE_SEND IOCTL](..\nfcsedev\ni-nfcsedev-ioctl-nfcse-hce-remote-send.md) | Transmits response APDU from DeviceHost NFCEE to remote device. The caller must be sure that response APDU is conformant to ISO-IEC 7816-4. |
| [IOCTL_NFCSE_SET_CARD_EMULATION_MODE IOCTL](..\nfcsedev\ni-nfcsedev-ioctl-nfcse-set-card-emulation-mode.md) | The IOCTL_NFCSE_SET_CARD_EMULATION_MODE control code sets whether the specified secure element is exposed in card emulation mode. |
| [IOCTL_NFCSE_SET_ROUTING_TABLE IOCTL](..\nfcsedev\ni-nfcsedev-ioctl-nfcse-set-routing-table.md) | Configures NFC controller listen mode routing table. |
| [IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT IOCTL](..\nfcsedev\ni-nfcsedev-ioctl-nfcse-subscribe-for-event.md) | The IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT control code is issued by a client to subscribe to a specific event. |
| [IOCTL_NFP_DISABLE IOCTL](..\nfpdev\ni-nfpdev-ioctl-nfp-disable.md) | A client sends the IOCTL_NFP_DISABLE request to temporarily disable subscriptions, publications, and presence events. |
| [IOCTL_NFP_ENABLE IOCTL](..\nfpdev\ni-nfpdev-ioctl-nfp-enable.md) | The client sends the IOCTL_NFP_ENABLE request to re-enable previously disabled subscriptions, publications, and presence events. |
| [IOCTL_NFP_GET_KILO_BYTES_PER_SECOND IOCTL](..\nfpdev\ni-nfpdev-ioctl-nfp-get-kilo-bytes-per-second.md) | A client sends the IOCTL_NFP_GET_KILO_BYTES_PER_SECOND request to any generic handle, one that is non-published and non-subscribed, to the provider device. |
| [IOCTL_NFP_GET_MAX_MESSAGE_BYTES IOCTL](..\nfpdev\ni-nfpdev-ioctl-nfp-get-max-message-bytes.md) | A client sends the IOCTL_NFP_GET_MAX_MESSAGE_BYTES request to any generic handle, one that is non-published and non-subscribed, to the provider device to determine the maximum message size supported. |
| [IOCTL_NFP_GET_NEXT_SUBSCRIBED_MESSAGE IOCTL](..\nfpdev\ni-nfpdev-ioctl-nfp-get-next-subscribed-message.md) | The client sends the IOCTL_NFP_GET_NEXT_SUBSCRIBED_MESSAGE request to the subscription handle repeatedly in order to receive subscribed messages as they arrive. |
| [IOCTL_NFP_GET_NEXT_TRANSMITTED_MESSAGE IOCTL](..\nfpdev\ni-nfpdev-ioctl-nfp-get-next-transmitted-message.md) | A client interested in receiving notifications that a message has been transmitted will send the IOCTL_NFP_GET_NEXT_TRANSMITTED_MESSAGE request to the proximity driver. |
| [IOCTL_NFP_SET_PAYLOAD IOCTL](..\nfpdev\ni-nfpdev-ioctl-nfp-set-payload.md) | A client application sends message data and confirms publication with the IOCTL_NFP_SET_PAYLOAD request. |
| [IOCTL_SMARTCARD_GET_ATTRIBUTE IOCTL](..\winsmcrd\ni-winsmcrd-ioctl-smartcard-get-attribute.md) | The IOCTL_SMARTCARD_GET_ATTRIBUTE control code queries for smart card attribues. |
| [IOCTL_SMARTCARD_GET_STATE IOCTL](..\winsmcrd\ni-winsmcrd-ioctl-smartcard-get-state.md) | The IOCTL_SMARTCARD_GET_STATE control code gets the current status of the smart card. |
| [IOCTL_SMARTCARD_IS_ABSENT IOCTL](..\winsmcrd\ni-winsmcrd-ioctl-smartcard-is-absent.md) | The IOCTL_SMARTCARD_IS_ABSENT control code returns immediately with STATUS_SUCCESS if no smart card is currently detected. |
| [IOCTL_SMARTCARD_IS_PRESENT IOCTL](..\winsmcrd\ni-winsmcrd-ioctl-smartcard-is-present.md) | The IOCTL_SMARTCARD_IS_PRESENT control code detects whether a smart card is currently detected. |
| [IOCTL_SMARTCARD_POWER IOCTL](..\winsmcrd\ni-winsmcrd-ioctl-smartcard-power.md) | Windows may require a driver to have this IOCTL to be NOP and return success. |
| [IOCTL_SMARTCARD_SET_ATTRIBUTE IOCTL](..\winsmcrd\ni-winsmcrd-ioctl-smartcard-set-attribute.md) | The IOCTL_SMARTCARD_SET_ATTRIBUTE control code sets an attribute and returns STATUS_SUCCESS on SCARD_ATTR_DEVICE_IN_USE; otherwise, it returns STATUS_NOT_SUPPORTED. |
| [IOCTL_SMARTCARD_SET_PROTOCOL IOCTL](..\winsmcrd\ni-winsmcrd-ioctl-smartcard-set-protocol.md) | Sets the procotol the driver communicates to the smart card with after the card is detected. |
| [IOCTL_SMARTCARD_TRANSMIT IOCTL](..\winsmcrd\ni-winsmcrd-ioctl-smartcard-transmit.md) | Transmits data from the client to the detected smart card in ISO7816-4 compliant APDU. |
