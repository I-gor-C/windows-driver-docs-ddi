# Declarations in the bthioctl header
This header Bthioctl contains these programming interfaces:

Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_BTH_GET_LOCAL_INFO IOCTL](ni-bthioctl-ioctl-bth-get-local-info.md) | TBD |
| [IOCTL_BTH_SDP_SUBMIT_RECORD IOCTL](ni-bthioctl-ioctl-bth-sdp-submit-record.md) | TBD |
| [IOCTL_BTH_GET_DEVICE_INFO IOCTL](ni-bthioctl-ioctl-bth-get-device-info.md) | TBD |
| [IOCTL_BTH_GET_RADIO_INFO IOCTL](ni-bthioctl-ioctl-bth-get-radio-info.md) | TBD |
| [IOCTL_INTERNAL_BTH_SUBMIT_BRB IOCTL](ni-bthioctl-ioctl-internal-bth-submit-brb.md) | TBD |
| [IOCTL_BTH_SDP_DISCONNECT IOCTL](ni-bthioctl-ioctl-bth-sdp-disconnect.md) | TBD |
| [IOCTL_BTH_SDP_REMOVE_RECORD IOCTL](ni-bthioctl-ioctl-bth-sdp-remove-record.md) | TBD |
| [IOCTL_BTH_GET_HOST_SUPPORTED_FEATURES IOCTL](ni-bthioctl-ioctl-bth-get-host-supported-features.md) | TBD |
| [IOCTL_BTH_DISCONNECT_DEVICE IOCTL](ni-bthioctl-ioctl-bth-disconnect-device.md) | TBD |
| [IOCTL_BTH_SDP_SUBMIT_RECORD_WITH_INFO IOCTL](ni-bthioctl-ioctl-bth-sdp-submit-record-with-info.md) | TBD |
| [IOCTL_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH IOCTL](ni-bthioctl-ioctl-bth-sdp-service-attribute-search.md) | TBD |
| [IOCTL_BTH_HCI_VENDOR_COMMAND IOCTL](ni-bthioctl-ioctl-bth-hci-vendor-command.md) | TBD |
| [IOCTL_INTERNAL_BTHENUM_GET_DEVINFO IOCTL](ni-bthioctl-ioctl-internal-bthenum-get-devinfo.md) | TBD |
| [IOCTL_BTH_SDP_CONNECT IOCTL](ni-bthioctl-ioctl-bth-sdp-connect.md) | TBD |
| [IOCTL_BTH_SDP_ATTRIBUTE_SEARCH IOCTL](ni-bthioctl-ioctl-bth-sdp-attribute-search.md) | TBD |
| [IOCTL_INTERNAL_BTHENUM_GET_ENUMINFO IOCTL](ni-bthioctl-ioctl-internal-bthenum-get-enuminfo.md) | TBD |
| [IOCTL_BTH_SDP_SERVICE_SEARCH IOCTL](ni-bthioctl-ioctl-bth-sdp-service-search.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [BTH_KERNEL_CTL function](nf-bthioctl-bth-kernel-ctl.md) | TBD |
| [BTH_CTL function](nf-bthioctl-bth-ctl.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [BTH_SDP_STREAM_RESPONSE structure](ns-bthioctl--bth-sdp-stream-response.md) | The BTH_SDP_STREAM_RESPONSE structure contains information about an SDP record. |
| [BTH_VENDOR_EVENT_INFO structure](ns-bthioctl--bth-vendor-event-info.md) | The BTH_VENDOR_EVENT_INFO structure specifies the buffer that is associated with the GUID_BLUETOOTH_HCI_VENDOR_EVENT GUID. |
| [BTH_SDP_SERVICE_ATTRIBUTE_SEARCH_REQUEST structure](ns-bthioctl--bth-sdp-service-attribute-search-request.md) | TBD |
| [BTH_VENDOR_SPECIFIC_COMMAND structure](ns-bthioctl--bth-vendor-specific-command.md) | The BTH_VENDOR_SPECIFIC_COMMAND structure specifies a Bluetooth vendor-specific command. |
| [BTH_RADIO_INFO structure](ns-bthioctl--bth-radio-info.md) | The BTH_RADIO_INFO structure contains information about a remote radio. |
| [BTH_DEVICE_INFO_LIST structure](ns-bthioctl--bth-device-info-list.md) | The BTH_DEVICE_INFO_LIST structure contains output information about all cached, previously discovered remote devices. |
| [BTH_HOST_FEATURE_MASK structure](ns-bthioctl--bth-host-feature-mask.md) | TBD |
| [BTH_SDP_ATTRIBUTE_SEARCH_REQUEST structure](ns-bthioctl--bth-sdp-attribute-search-request.md) | The BTH_SDP_ATTRIBUTE_SEARCH_REQUEST structure contains information pertinent to an SDP attribute search. |
| [BTH_VENDOR_PATTERN structure](ns-bthioctl--bth-vendor-pattern.md) | The BTH_VENDOR_PATTERN structure specifies a vendor pattern. |
| [BTH_LOCAL_RADIO_INFO structure](ns-bthioctl--bth-local-radio-info.md) | The BTH_LOCAL_RADIO_INFO structure contains information about the local Bluetooth system and radio. |
| [BTH_COMMAND_HEADER structure](ns-bthioctl--bth-command-header.md) | The BTH_COMMAND_HEADER structure specifies header information for a vendor-specific HCI command. |
| [BTH_SDP_RECORD structure](ns-bthioctl--bth-sdp-record.md) | The BTH_SDP_RECORD structure contains information about an SDP record that is to be added to the local SDP server. |
| [BTH_SDP_DISCONNECT structure](ns-bthioctl--bth-sdp-disconnect.md) | The BTH_SDP_DISCONNECT structure contains input information about a connection handle to the remote SDP connection to terminate. This structure is passed as the input buffer of IOCTL_BTH_SDP_DISCONNECT. |
| [BTH_SDP_SERVICE_SEARCH_REQUEST structure](ns-bthioctl--bth-sdp-service-search-request.md) | The BTH_SDP_SERVICE_SEARCH_REQUEST structure contains information pertinent to an SDP service search. |
| [BTH_SDP_CONNECT structure](ns-bthioctl--bth-sdp-connect.md) | The BTH_SDP_CONNECT structure contains input and output information about a connection between the local Bluetooth system and a remote SDP server. This structure is passed as the input buffer and output buffer of IOCTL_BTH_SDP_CONNECT. |

This header is used in these topics:

- [bltooth](..content/_bltooth)
