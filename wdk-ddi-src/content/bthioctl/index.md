# Bthioctl.h header


This header is used by Bluetooth. For more information, see
- [Bluetooth](../_bltooth/index.md)

Bthioctl.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [BTH_COMMAND_HEADER structure](ns-bthioctl--bth-command-header.md) | The BTH_COMMAND_HEADER structure specifies header information for a vendor-specific HCI command. |
| [BTH_DEVICE_INFO_LIST structure](ns-bthioctl--bth-device-info-list.md) | The BTH_DEVICE_INFO_LIST structure contains output information about all cached, previously discovered remote devices. |
| [BTH_LOCAL_RADIO_INFO structure](ns-bthioctl--bth-local-radio-info.md) | The BTH_LOCAL_RADIO_INFO structure contains information about the local Bluetooth system and radio. |
| [BTH_RADIO_INFO structure](ns-bthioctl--bth-radio-info.md) | The BTH_RADIO_INFO structure contains information about a remote radio. |
| [BTH_SDP_ATTRIBUTE_SEARCH_REQUEST structure](ns-bthioctl--bth-sdp-attribute-search-request.md) | The BTH_SDP_ATTRIBUTE_SEARCH_REQUEST structure contains information pertinent to an SDP attribute search. |
| [BTH_SDP_CONNECT structure](ns-bthioctl--bth-sdp-connect.md) | The BTH_SDP_CONNECT structure contains input and output information about a connection between the local Bluetooth system and a remote SDP server. This structure is passed as the input buffer and output buffer of IOCTL_BTH_SDP_CONNECT. |
| [BTH_SDP_DISCONNECT structure](ns-bthioctl--bth-sdp-disconnect.md) | The BTH_SDP_DISCONNECT structure contains input information about a connection handle to the remote SDP connection to terminate. This structure is passed as the input buffer of IOCTL_BTH_SDP_DISCONNECT. |
| [BTH_SDP_RECORD structure](ns-bthioctl--bth-sdp-record.md) | The BTH_SDP_RECORD structure contains information about an SDP record that is to be added to the local SDP server. |
| [BTH_SDP_SERVICE_ATTRIBUTE_SEARCH_REQUEST structure](ns-bthioctl--bth-sdp-service-attribute-search-request.md) | The BTH_SDP_SERVICE_ATTRIBUTE_SEARCH_REQUEST structure contains information pertinent to a combined SDP service and attribute search. This structure is passed as the input buffer to the IOCTL_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH IOCTL. |
| [BTH_SDP_SERVICE_SEARCH_REQUEST structure](ns-bthioctl--bth-sdp-service-search-request.md) | The BTH_SDP_SERVICE_SEARCH_REQUEST structure contains information pertinent to an SDP service search. |
| [BTH_SDP_STREAM_RESPONSE structure](ns-bthioctl--bth-sdp-stream-response.md) | The BTH_SDP_STREAM_RESPONSE structure contains information about an SDP record. |
| [BTH_VENDOR_EVENT_INFO structure](ns-bthioctl--bth-vendor-event-info.md) | The BTH_VENDOR_EVENT_INFO structure specifies the buffer that is associated with the GUID_BLUETOOTH_HCI_VENDOR_EVENT GUID. |
| [BTH_VENDOR_PATTERN structure](ns-bthioctl--bth-vendor-pattern.md) | The BTH_VENDOR_PATTERN structure specifies a vendor pattern. |
| [BTH_VENDOR_SPECIFIC_COMMAND structure](ns-bthioctl--bth-vendor-specific-command.md) | The BTH_VENDOR_SPECIFIC_COMMAND structure specifies a Bluetooth vendor-specific command. |
