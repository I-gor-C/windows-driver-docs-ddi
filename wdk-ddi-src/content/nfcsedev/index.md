---
UID: NA:nfcsedev
---

# Nfcsedev.h header

## -description

This header is used by Near field communications (NFC). For more information, see
- [Near field communications (NFC)](../_nfpdrivers/index.md)

Nfcsedev.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [_SECURE_ELEMENT_AID_ROUTING_INFO structure](ns-nfcsedev-_secure_element_aid_routing_info.md) | SECURE_ELEMENT_AID_ROUTING_INFO is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY. |
| [_SECURE_ELEMENT_ENDPOINT_INFO structure](ns-nfcsedev-_secure_element_endpoint_info.md) | SECURE_ELEMENT_ENDPOINT_INFO is a member of SECURE_ELEMENT_ENDPOINT_LIST. |
| [_SECURE_ELEMENT_ENDPOINT_LIST structure](ns-nfcsedev-_secure_element_endpoint_list.md) | The output parameter for IOCTL_NFCSE_ENUM_ENDPOINTS. |
| [_SECURE_ELEMENT_EVENT_INFO structure](ns-nfcsedev-_secure_element_event_info.md) | This structure provides information about a secure element event. |
| [_SECURE_ELEMENT_EVENT_SUBSCRIPTION_INFO structure](ns-nfcsedev-_secure_element_event_subscription_info.md) | The SECURE_ELEMENT_EVENT_SUBSCRIPTION_INFO structure is an input parameter to IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT. |
| [_SECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD structure](ns-nfcsedev-_secure_element_hce_activation_payload.md) | . |
| [_SECURE_ELEMENT_HCE_DATA_PACKET structure](ns-nfcsedev-_secure_element_hce_data_packet.md) | SECURE_ELEMENT_HCE_DATA_PACKET is an input buffer to IOCTL_NFCSE_HCE_REMOTE_SEND and output buffer for IOCTL_NFCSE_HCE_REMOTE_RECV. |
| [_SECURE_ELEMENT_NFCC_CAPABILITIES structure](ns-nfcsedev-_secure_element_nfcc_capabilities.md) | SECURE_ELEMENT_NFCC_CAPABILITIES contains NFC controller capabilities. |
| [_SECURE_ELEMENT_PROTO_ROUTING_INFO structure](ns-nfcsedev-_secure_element_proto_routing_info.md) | SECURE_ELEMENT_PROTO_ROUTING_INFO is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY. |
| [_SECURE_ELEMENT_ROUTING_TABLE structure](ns-nfcsedev-_secure_element_routing_table.md) | SECURE_ELEMENT_ROUTING_TABLE is an input parameter for IOCTL_NFCSE_SET_ROUTING_TABLE. |
| [_SECURE_ELEMENT_ROUTING_TABLE_ENTRY structure](ns-nfcsedev-_secure_element_routing_table_entry.md) | SECURE_ELEMENT_ROUTING_TABLE_ENTRY is a member of SECURE_ELEMENT_ROUTING_TABLE. |
| [_SECURE_ELEMENT_SET_CARD_EMULATION_MODE_INFO structure](ns-nfcsedev-_secure_element_set_card_emulation_mode_info.md) | SECURE_ELEMENT_SET_CARD_EMULATION_MODE_INFO is the input parameter for IOCTL_NFCSE_SET_CARD_EMULATION_MODE. |
| [_SECURE_ELEMENT_TECH_ROUTING_INFO structure](ns-nfcsedev-_secure_element_tech_routing_info.md) | SECURE_ELEMENT_TECH_ROUTING_INFO is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_NFCSE_ENUM_ENDPOINTS IOCTL](ni-nfcsedev-ioctl_nfcse_enum_endpoints.md) | Returns information regarding the list of all the secure elements attached to the NFC controller. |
| [IOCTL_NFCSE_GET_NEXT_EVENT IOCTL](ni-nfcsedev-ioctl_nfcse_get_next_event.md) | The IOCTL_NFCSE_GET_NEXT_EVENT control code returns the next event available in the buffer, or if there are no more buffered events remains pending until a secure element event is available. The event details must then be returned to the caller. |
| [IOCTL_NFCSE_GET_NFCC_CAPABILITIES IOCTL](ni-nfcsedev-ioctl_nfcse_get_nfcc_capabilities.md) | The IOCTL_NFCSE_GET_NFCC_CAPABILITIES control code returns information about the current NFC controller capabilities, including the maximum Listen Mode Routing table size (defined in section 4.2 of the NFC Controller Interface (NCI) Technical Specification Version 1.1) and supported routing modes. |
| [IOCTL_NFCSE_GET_ROUTING_TABLE IOCTL](ni-nfcsedev-ioctl_nfcse_get_routing_table.md) | Returns information regarding the current configuration of listen mode routing table. |
| [IOCTL_NFCSE_HCE_REMOTE_RECV IOCTL](ni-nfcsedev-ioctl_nfcse_hce_remote_recv.md) | Either returns the next data buffer available, or if there are no more buffered data, the request shall stay pending until an APDU buffer is available for reading. |
| [IOCTL_NFCSE_HCE_REMOTE_SEND IOCTL](ni-nfcsedev-ioctl_nfcse_hce_remote_send.md) | Transmits response APDU from DeviceHost NFCEE to remote device. The caller must be sure that response APDU is conformant to ISO-IEC 7816-4. |
| [IOCTL_NFCSE_SET_CARD_EMULATION_MODE IOCTL](ni-nfcsedev-ioctl_nfcse_set_card_emulation_mode.md) | The IOCTL_NFCSE_SET_CARD_EMULATION_MODE control code sets whether the specified secure element is exposed in card emulation mode. |
| [IOCTL_NFCSE_SET_ROUTING_TABLE IOCTL](ni-nfcsedev-ioctl_nfcse_set_routing_table.md) | Configures NFC controller listen mode routing table. |
| [IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT IOCTL](ni-nfcsedev-ioctl_nfcse_subscribe_for_event.md) | The IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT control code is issued by a client to subscribe to a specific event. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_SECURE_ELEMENT_CARD_EMULATION_MODE enumeration](ne-nfcsedev-_secure_element_card_emulation_mode.md) | This enumeration indicates the card emulation mode of a secure element. |
| [_SECURE_ELEMENT_EVENT_TYPE enumeration](ne-nfcsedev-_secure_element_event_type.md) | Indicates the type of secure element events. |
| [_SECURE_ELEMENT_ROUTING_TYPE enumeration](ne-nfcsedev-_secure_element_routing_type.md) | SECURE_ELEMENT_ROUTING_TYPE is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY. |
| [_SECURE_ELEMENT_TYPE enumeration](ne-nfcsedev-_secure_element_type.md) | Indicates the type of a secure element. |
