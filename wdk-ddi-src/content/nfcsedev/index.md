---
UID : NA:nfcsedev
ms.assetid : 71f179ce-e2f5-3602-a35a-5134da7d7128
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# nfcsedev.h header



nfcsedev.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_NFCSE_ENUM_ENDPOINTS](ni-nfcsedev-ioctl_nfcse_enum_endpoints.md) | Returns information regarding the list of all the secure elements attached to the NFC controller. |
| [IOCTL_NFCSE_GET_NEXT_EVENT](ni-nfcsedev-ioctl_nfcse_get_next_event.md) | The IOCTL_NFCSE_GET_NEXT_EVENT control code returns the next event available in the buffer, or if there are no more buffered events remains pending until a secure element event is available. The event details must then be returned to the caller. |
| [IOCTL_NFCSE_GET_NFCC_CAPABILITIES](ni-nfcsedev-ioctl_nfcse_get_nfcc_capabilities.md) | The IOCTL_NFCSE_GET_NFCC_CAPABILITIES control code returns information about the current NFC controller capabilities, including the maximum Listen Mode Routing table size (defined in section 4.2 of the NFC Controller Interface (NCI) Technical Specification Version 1.1) and supported routing modes. |
| [IOCTL_NFCSE_GET_ROUTING_TABLE](ni-nfcsedev-ioctl_nfcse_get_routing_table.md) | Returns information regarding the current configuration of listen mode routing table. |
| [IOCTL_NFCSE_HCE_REMOTE_RECV](ni-nfcsedev-ioctl_nfcse_hce_remote_recv.md) | Either returns the next data buffer available, or if there are no more buffered data, the request shall stay pending until an APDU buffer is available for reading. |
| [IOCTL_NFCSE_HCE_REMOTE_SEND](ni-nfcsedev-ioctl_nfcse_hce_remote_send.md) | Transmits response APDU from DeviceHost NFCEE to remote device. The caller must be sure that response APDU is conformant to ISO-IEC 7816-4. |
| [IOCTL_NFCSE_SET_CARD_EMULATION_MODE](ni-nfcsedev-ioctl_nfcse_set_card_emulation_mode.md) | The IOCTL_NFCSE_SET_CARD_EMULATION_MODE control code sets whether the specified secure element is exposed in card emulation mode. |
| [IOCTL_NFCSE_SET_ROUTING_TABLE](ni-nfcsedev-ioctl_nfcse_set_routing_table.md) | Configures NFC controller listen mode routing table. |
| [IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT](ni-nfcsedev-ioctl_nfcse_subscribe_for_event.md) | The IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT control code is issued by a client to subscribe to a specific event. |




## Structures
| Title | Description |
| ---- |:---- |
| [_SECURE_ELEMENT_AID_ROUTING_INFO](ns-nfcsedev-_secure_element_aid_routing_info.md) | SECURE_ELEMENT_AID_ROUTING_INFO is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY. |
| [_SECURE_ELEMENT_ENDPOINT_INFO](ns-nfcsedev-_secure_element_endpoint_info.md) | SECURE_ELEMENT_ENDPOINT_INFO is a member of SECURE_ELEMENT_ENDPOINT_LIST. |
| [_SECURE_ELEMENT_ENDPOINT_LIST](ns-nfcsedev-_secure_element_endpoint_list.md) | The output parameter for IOCTL_NFCSE_ENUM_ENDPOINTS. |
| [_SECURE_ELEMENT_EVENT_INFO](ns-nfcsedev-_secure_element_event_info.md) | This structure provides information about a secure element event. |
| [_SECURE_ELEMENT_EVENT_SUBSCRIPTION_INFO](ns-nfcsedev-_secure_element_event_subscription_info.md) | The SECURE_ELEMENT_EVENT_SUBSCRIPTION_INFO structure is an input parameter to IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT. |
| [_SECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD](ns-nfcsedev-_secure_element_hce_activation_payload.md) | "." |
| [_SECURE_ELEMENT_HCE_DATA_PACKET](ns-nfcsedev-_secure_element_hce_data_packet.md) | SECURE_ELEMENT_HCE_DATA_PACKET is an input buffer to IOCTL_NFCSE_HCE_REMOTE_SEND and output buffer for IOCTL_NFCSE_HCE_REMOTE_RECV. |
| [_SECURE_ELEMENT_NFCC_CAPABILITIES](ns-nfcsedev-_secure_element_nfcc_capabilities.md) | SECURE_ELEMENT_NFCC_CAPABILITIES contains NFC controller capabilities. |
| [_SECURE_ELEMENT_PROTO_ROUTING_INFO](ns-nfcsedev-_secure_element_proto_routing_info.md) | SECURE_ELEMENT_PROTO_ROUTING_INFO is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY. |
| [_SECURE_ELEMENT_ROUTING_TABLE](ns-nfcsedev-_secure_element_routing_table.md) | SECURE_ELEMENT_ROUTING_TABLE is an input parameter for IOCTL_NFCSE_SET_ROUTING_TABLE. |
| [_SECURE_ELEMENT_ROUTING_TABLE_ENTRY](ns-nfcsedev-_secure_element_routing_table_entry.md) | SECURE_ELEMENT_ROUTING_TABLE_ENTRY is a member of SECURE_ELEMENT_ROUTING_TABLE. |
| [_SECURE_ELEMENT_SET_CARD_EMULATION_MODE_INFO](ns-nfcsedev-_secure_element_set_card_emulation_mode_info.md) | SECURE_ELEMENT_SET_CARD_EMULATION_MODE_INFO is the input parameter for IOCTL_NFCSE_SET_CARD_EMULATION_MODE. |
| [_SECURE_ELEMENT_TECH_ROUTING_INFO](ns-nfcsedev-_secure_element_tech_routing_info.md) | SECURE_ELEMENT_TECH_ROUTING_INFO is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_SECURE_ELEMENT_CARD_EMULATION_MODE](ne-nfcsedev-_secure_element_card_emulation_mode.md) | This enumeration indicates the card emulation mode of a secure element. |
| [_SECURE_ELEMENT_EVENT_TYPE](ne-nfcsedev-_secure_element_event_type.md) | Indicates the type of secure element events. |
| [_SECURE_ELEMENT_ROUTING_TYPE](ne-nfcsedev-_secure_element_routing_type.md) | SECURE_ELEMENT_ROUTING_TYPE is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY. |
| [_SECURE_ELEMENT_TYPE](ne-nfcsedev-_secure_element_type.md) | Indicates the type of a secure element. |