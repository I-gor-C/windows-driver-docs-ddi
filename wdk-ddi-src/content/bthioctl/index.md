---
UID: NA:bthioctl
ms.assetid: dbb85592-b165-3196-b65b-0910ea02316f
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# bthioctl.h header



bthioctl.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_BTH_DISCONNECT_DEVICE](ni-bthioctl-ioctl_bth_disconnect_device.md) | Profile drivers use IOCTL_BTH_DISCONNECT_DEVICE to request the operating system to disconnect the specified remote device. |
| [IOCTL_BTH_GET_DEVICE_INFO](ni-bthioctl-ioctl_bth_get_device_info.md) | The IOCTL_BTH_GET_DEVICE_INFO request returns information about all cached, previously discovered remote radios that are Bluetooth-enabled. |
| [IOCTL_BTH_GET_LOCAL_INFO](ni-bthioctl-ioctl_bth_get_local_info.md) | The IOCTL_BTH_GET_LOCAL_INFO request returns information about the local Bluetooth system and radio. |
| [IOCTL_BTH_GET_RADIO_INFO](ni-bthioctl-ioctl_bth_get_radio_info.md) | The IOCTL_BTH_GET_RADIO_INFO request obtains information about the specified remote radio. |
| [IOCTL_BTH_HCI_VENDOR_COMMAND](ni-bthioctl-ioctl_bth_hci_vendor_command.md) | The IOCTL_BTH_HCI_VENDOR_COMMAND request allows Bluetooth applications to send vendor-specific commands to radios. |
| [IOCTL_BTH_SDP_ATTRIBUTE_SEARCH](ni-bthioctl-ioctl_bth_sdp_attribute_search.md) | The IOCTL_BTH_SDP_ATTRIBUTE_SEARCH request obtains attributes for the specified SDP record. |
| [IOCTL_BTH_SDP_CONNECT](ni-bthioctl-ioctl_bth_sdp_connect.md) | The IOCTL_BTH_SDP_CONNECT request creates a connection to the SDP service on a remote Bluetooth device. |
| [IOCTL_BTH_SDP_DISCONNECT](ni-bthioctl-ioctl_bth_sdp_disconnect.md) | The IOCTL_BTH_SDP_DISCONNECT request closes a connection to a remote SDP server. |
| [IOCTL_BTH_SDP_REMOVE_RECORD](ni-bthioctl-ioctl_bth_sdp_remove_record.md) | The IOCTL_BTH_SDP_REMOVE_RECORD request removes a local SDP record that the profile driver previously submitted. The local server will no longer offer this record to remote devices. |
| [IOCTL_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH](ni-bthioctl-ioctl_bth_sdp_service_attribute_search.md) | The IOCTL_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH request combines an SDP service and attribute search into a single operation. This allows a caller to directly obtain SDP records from a remote device. |
| [IOCTL_BTH_SDP_SERVICE_SEARCH](ni-bthioctl-ioctl_bth_sdp_service_search.md) | The IOCTL_BTH_SDP_SERVICE_SEARCH request contacts a remote device with an SDP request for handles to SDP records of a particular service class or classes. |
| [IOCTL_BTH_SDP_SUBMIT_RECORD](ni-bthioctl-ioctl_bth_sdp_submit_record.md) | The IOCTL_BTH_SDP_SUBMIT_RECORD request allows a profile driver to add an SDP record to the local SDP server, allowing the client to advertise that a service is available on the local computer. |
| [IOCTL_BTH_SDP_SUBMIT_RECORD_WITH_INFO](ni-bthioctl-ioctl_bth_sdp_submit_record_with_info.md) | The IOCTL_BTH_SDP_SUBMIT_RECORD_WITH_INFO request adds an SDP record to the local SDP server along with attributes that are not part of the SDP record itself. |
| [IOCTL_INTERNAL_BTH_SUBMIT_BRB](ni-bthioctl-ioctl_internal_bth_submit_brb.md) | Profile drivers use IOCTL_INTERNAL_BTH_SUBMIT_BRB to submit a Bluetooth Request Block (BRB) to the Bluetooth driver stack. |
| [IOCTL_INTERNAL_BTHENUM_GET_DEVINFO](ni-bthioctl-ioctl_internal_bthenum_get_devinfo.md) | The IOCTL_INTERNAL_BTHENUM_GET_DEVINFO request returns information about the remote device that caused the Plug and Play (PnP) manager to load the current instance of the profile driver. |
| [IOCTL_INTERNAL_BTHENUM_GET_ENUMINFO](ni-bthioctl-ioctl_internal_bthenum_get_enuminfo.md) | The IOCTL_INTERNAL_BTHENUM_GET_ENUMINFO request obtains information about the underlying device and service that caused the Plug and Play (PnP) manager to load the profile driver. |




## Structures
| Title | Description |
| ---- |:---- |
| [_BTH_COMMAND_HEADER](ns-bthioctl-_bth_command_header.md) | The BTH_COMMAND_HEADER structure specifies header information for a vendor-specific HCI command. |
| [_BTH_DEVICE_INFO_LIST](ns-bthioctl-_bth_device_info_list.md) | The BTH_DEVICE_INFO_LIST structure contains output information about all cached, previously discovered remote devices. |
| [_BTH_LOCAL_RADIO_INFO](ns-bthioctl-_bth_local_radio_info.md) | The BTH_LOCAL_RADIO_INFO structure contains information about the local Bluetooth system and radio. |
| [_BTH_RADIO_INFO](ns-bthioctl-_bth_radio_info.md) | The BTH_RADIO_INFO structure contains information about a remote radio. |
| [_BTH_SDP_ATTRIBUTE_SEARCH_REQUEST](ns-bthioctl-_bth_sdp_attribute_search_request.md) | The BTH_SDP_ATTRIBUTE_SEARCH_REQUEST structure contains information pertinent to an SDP attribute search. |
| [_BTH_SDP_CONNECT](ns-bthioctl-_bth_sdp_connect.md) | The BTH_SDP_CONNECT structure contains input and output information about a connection between the local Bluetooth system and a remote SDP server. This structure is passed as the input buffer and output buffer of IOCTL_BTH_SDP_CONNECT. |
| [_BTH_SDP_DISCONNECT](ns-bthioctl-_bth_sdp_disconnect.md) | The BTH_SDP_DISCONNECT structure contains input information about a connection handle to the remote SDP connection to terminate. This structure is passed as the input buffer of IOCTL_BTH_SDP_DISCONNECT. |
| [_BTH_SDP_RECORD](ns-bthioctl-_bth_sdp_record.md) | The BTH_SDP_RECORD structure contains information about an SDP record that is to be added to the local SDP server. |
| [_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH_REQUEST](ns-bthioctl-_bth_sdp_service_attribute_search_request.md) | The BTH_SDP_SERVICE_ATTRIBUTE_SEARCH_REQUEST structure contains information pertinent to a combined SDP service and attribute search. This structure is passed as the input buffer to the IOCTL_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH IOCTL. |
| [_BTH_SDP_SERVICE_SEARCH_REQUEST](ns-bthioctl-_bth_sdp_service_search_request.md) | The BTH_SDP_SERVICE_SEARCH_REQUEST structure contains information pertinent to an SDP service search. |
| [_BTH_SDP_STREAM_RESPONSE](ns-bthioctl-_bth_sdp_stream_response.md) | The BTH_SDP_STREAM_RESPONSE structure contains information about an SDP record. |
| [_BTH_VENDOR_EVENT_INFO](ns-bthioctl-_bth_vendor_event_info.md) | The BTH_VENDOR_EVENT_INFO structure specifies the buffer that is associated with the GUID_BLUETOOTH_HCI_VENDOR_EVENT GUID. |
| [_BTH_VENDOR_PATTERN](ns-bthioctl-_bth_vendor_pattern.md) | The BTH_VENDOR_PATTERN structure specifies a vendor pattern. |
| [_BTH_VENDOR_SPECIFIC_COMMAND](ns-bthioctl-_bth_vendor_specific_command.md) | The BTH_VENDOR_SPECIFIC_COMMAND structure specifies a Bluetooth vendor-specific command. |