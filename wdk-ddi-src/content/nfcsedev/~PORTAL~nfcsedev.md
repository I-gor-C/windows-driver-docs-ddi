# Declarations in the nfcsedev header
This header Nfcsedev contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SECURE_ELEMENT_ENDPOINT_LIST structure](ns-nfcsedev--secure-element-endpoint-list.md) | The output parameter for IOCTL_NFCSE_ENUM_ENDPOINTS. |
| [SECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD structure](ns-nfcsedev--secure-element-hce-activation-payload.md) | . |
| [SECURE_ELEMENT_TECH_ROUTING_INFO structure](ns-nfcsedev--secure-element-tech-routing-info.md) | TBD |
| [SECURE_ELEMENT_ROUTING_TABLE structure](ns-nfcsedev--secure-element-routing-table.md) | SECURE_ELEMENT_ROUTING_TABLE is an input parameter for IOCTL_NFCSE_SET_ROUTING_TABLE. |
| [SECURE_ELEMENT_EVENT_SUBSCRIPTION_INFO structure](ns-nfcsedev--secure-element-event-subscription-info.md) | The SECURE_ELEMENT_EVENT_SUBSCRIPTION_INFO structure is an input parameter to IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT. |
| [SECURE_ELEMENT_HCE_DATA_PACKET structure](ns-nfcsedev--secure-element-hce-data-packet.md) | SECURE_ELEMENT_HCE_DATA_PACKET is an input buffer to IOCTL_NFCSE_HCE_REMOTE_SEND and output buffer for IOCTL_NFCSE_HCE_REMOTE_RECV. |
| [SECURE_ELEMENT_NFCC_CAPABILITIES structure](ns-nfcsedev--secure-element-nfcc-capabilities.md) | SECURE_ELEMENT_NFCC_CAPABILITIES contains NFC controller capabilities. |
| [SECURE_ELEMENT_EVENT_INFO structure](ns-nfcsedev--secure-element-event-info.md) | This structure provides information about a secure element event. |
| [SECURE_ELEMENT_SET_CARD_EMULATION_MODE_INFO structure](ns-nfcsedev--secure-element-set-card-emulation-mode-info.md) | SECURE_ELEMENT_SET_CARD_EMULATION_MODE_INFO is the input parameter for IOCTL_NFCSE_SET_CARD_EMULATION_MODE. |
| [SECURE_ELEMENT_ENDPOINT_INFO structure](ns-nfcsedev--secure-element-endpoint-info.md) | SECURE_ELEMENT_ENDPOINT_INFO is a member of SECURE_ELEMENT_ENDPOINT_LIST. |
| [SECURE_ELEMENT_PROTO_ROUTING_INFO structure](ns-nfcsedev--secure-element-proto-routing-info.md) | TBD |
| [SECURE_ELEMENT_ROUTING_TABLE_ENTRY structure](ns-nfcsedev--secure-element-routing-table-entry.md) | SECURE_ELEMENT_ROUTING_TABLE_ENTRY is a member of SECURE_ELEMENT_ROUTING_TABLE. |
| [SECURE_ELEMENT_AID_ROUTING_INFO structure](ns-nfcsedev--secure-element-aid-routing-info.md) | SECURE_ELEMENT_AID_ROUTING_INFO is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_NFCSE_GET_NEXT_EVENT IOCTL](ni-nfcsedev-ioctl-nfcse-get-next-event.md) | TBD |
| [IOCTL_NFCSE_HCE_REMOTE_RECV IOCTL](ni-nfcsedev-ioctl-nfcse-hce-remote-recv.md) | TBD |
| [IOCTL_NFCSE_GET_ROUTING_TABLE IOCTL](ni-nfcsedev-ioctl-nfcse-get-routing-table.md) | TBD |
| [IOCTL_NFCSE_SET_CARD_EMULATION_MODE IOCTL](ni-nfcsedev-ioctl-nfcse-set-card-emulation-mode.md) | TBD |
| [IOCTL_NFCSE_SET_ROUTING_TABLE IOCTL](ni-nfcsedev-ioctl-nfcse-set-routing-table.md) | TBD |
| [IOCTL_NFCSE_ENUM_ENDPOINTS IOCTL](ni-nfcsedev-ioctl-nfcse-enum-endpoints.md) | TBD |
| [IOCTL_NFCSE_HCE_REMOTE_SEND IOCTL](ni-nfcsedev-ioctl-nfcse-hce-remote-send.md) | TBD |
| [IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT IOCTL](ni-nfcsedev-ioctl-nfcse-subscribe-for-event.md) | TBD |
| [IOCTL_NFCSE_GET_NFCC_CAPABILITIES IOCTL](ni-nfcsedev-ioctl-nfcse-get-nfcc-capabilities.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [SECURE_ELEMENT_CARD_EMULATION_MODE enumeration](ne-nfcsedev--secure-element-card-emulation-mode.md) | This enumeration indicates the card emulation mode of a secure element. |
| [SECURE_ELEMENT_ROUTING_TYPE enumeration](ne-nfcsedev--secure-element-routing-type.md) | SECURE_ELEMENT_ROUTING_TYPE is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY. |
| [SECURE_ELEMENT_TYPE enumeration](ne-nfcsedev--secure-element-type.md) | Indicates the type of a secure element. |
| [SECURE_ELEMENT_EVENT_TYPE enumeration](ne-nfcsedev--secure-element-event-type.md) | Indicates the type of secure element events. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [SECURE_ELEMENT_ENDPOINT_LIST_AND_ENTRIES function](nf-nfcsedev-secure-element-endpoint-list-and-entries.md) | TBD |
| [SECURE_ELEMENT_EVENT_INFO_AND_PAYLOAD function](nf-nfcsedev-secure-element-event-info-and-payload.md) | TBD |
| [SECURE_ELEMENT_ROUTING_TABLE_AND_ENTRIES function](nf-nfcsedev-secure-element-routing-table-and-entries.md) | TBD |

This header is used in these topics:

- [nfpdrivers](..content/_nfpdrivers)
