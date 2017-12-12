---
UID: NA:
---

# Bthioctl.h header

## -description

This header is used by Bluetooth. For more information, see
- [Bluetooth](../_bltooth/index.md)

Bthioctl.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [_BTH_COMMAND_HEADER structure](ns-bthioctl-_bth_command_header.md) | The BTH_COMMAND_HEADER structure specifies header information for a vendor-specific HCI command. |
| [_BTH_DEVICE_INFO_LIST structure](ns-bthioctl-_bth_device_info_list.md) | The BTH_DEVICE_INFO_LIST structure contains output information about all cached, previously discovered remote devices. |
| [_BTH_LOCAL_RADIO_INFO structure](ns-bthioctl-_bth_local_radio_info.md) | The BTH_LOCAL_RADIO_INFO structure contains information about the local Bluetooth system and radio. |
| [_BTH_RADIO_INFO structure](ns-bthioctl-_bth_radio_info.md) | The BTH_RADIO_INFO structure contains information about a remote radio. |
| [_BTH_SDP_ATTRIBUTE_SEARCH_REQUEST structure](ns-bthioctl-_bth_sdp_attribute_search_request.md) | The BTH_SDP_ATTRIBUTE_SEARCH_REQUEST structure contains information pertinent to an SDP attribute search. |
| [_BTH_SDP_CONNECT structure](ns-bthioctl-_bth_sdp_connect.md) | The BTH_SDP_CONNECT structure contains input and output information about a connection between the local Bluetooth system and a remote SDP server. This structure is passed as the input buffer and output buffer of IOCTL_BTH_SDP_CONNECT. |
| [_BTH_SDP_DISCONNECT structure](ns-bthioctl-_bth_sdp_disconnect.md) | The BTH_SDP_DISCONNECT structure contains input information about a connection handle to the remote SDP connection to terminate. This structure is passed as the input buffer of IOCTL_BTH_SDP_DISCONNECT. |
| [_BTH_SDP_RECORD structure](ns-bthioctl-_bth_sdp_record.md) | The BTH_SDP_RECORD structure contains information about an SDP record that is to be added to the local SDP server. |
| [_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH_REQUEST structure](ns-bthioctl-_bth_sdp_service_attribute_search_request.md) | The BTH_SDP_SERVICE_ATTRIBUTE_SEARCH_REQUEST structure contains information pertinent to a combined SDP service and attribute search. This structure is passed as the input buffer to the IOCTL_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH IOCTL. |
| [_BTH_SDP_SERVICE_SEARCH_REQUEST structure](ns-bthioctl-_bth_sdp_service_search_request.md) | The BTH_SDP_SERVICE_SEARCH_REQUEST structure contains information pertinent to an SDP service search. |
| [_BTH_SDP_STREAM_RESPONSE structure](ns-bthioctl-_bth_sdp_stream_response.md) | The BTH_SDP_STREAM_RESPONSE structure contains information about an SDP record. |
| [_BTH_VENDOR_EVENT_INFO structure](ns-bthioctl-_bth_vendor_event_info.md) | The BTH_VENDOR_EVENT_INFO structure specifies the buffer that is associated with the GUID_BLUETOOTH_HCI_VENDOR_EVENT GUID. |
| [_BTH_VENDOR_PATTERN structure](ns-bthioctl-_bth_vendor_pattern.md) | The BTH_VENDOR_PATTERN structure specifies a vendor pattern. |
| [_BTH_VENDOR_SPECIFIC_COMMAND structure](ns-bthioctl-_bth_vendor_specific_command.md) | The BTH_VENDOR_SPECIFIC_COMMAND structure specifies a Bluetooth vendor-specific command. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_BTH_GET_RADIO_INFO IOCTL](ni-bthioctl-ioctl_bth_get_radio_info.md) | The IOCTL_BTH_GET_RADIO_INFO request obtains information about the specified remote radio. |
| [IOCTL_BTH_HCI_VENDOR_COMMAND IOCTL](ni-bthioctl-ioctl_bth_hci_vendor_command.md) | The IOCTL_BTH_HCI_VENDOR_COMMAND request allows Bluetooth applications to send vendor-specific commands to radios. |
| [IOCTL_BTH_SDP_ATTRIBUTE_SEARCH IOCTL](ni-bthioctl-ioctl_bth_sdp_attribute_search.md) | The IOCTL_BTH_SDP_ATTRIBUTE_SEARCH request obtains attributes for the specified SDP record. |
| [IOCTL_BTH_SDP_CONNECT IOCTL](ni-bthioctl-ioctl_bth_sdp_connect.md) | The IOCTL_BTH_SDP_CONNECT request creates a connection to the SDP service on a remote Bluetooth device. |
| [IOCTL_BTH_SDP_DISCONNECT IOCTL](ni-bthioctl-ioctl_bth_sdp_disconnect.md) | The IOCTL_BTH_SDP_DISCONNECT request closes a connection to a remote SDP server. |
