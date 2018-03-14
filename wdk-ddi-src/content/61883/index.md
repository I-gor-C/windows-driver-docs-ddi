---
UID: NA:61883
ms.assetid: e401eb24-793e-3800-b0b7-55496f44fbb8
ms.author: windowsdriverdev
ms.date: 03/13/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# 61883.h header



61883.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_61883_CLASS](ni-61883-ioctl_61883_class.md) | An IEC-61883 client driver uses the IRP_MJ_INTERNAL_DEVICE_CONTROL IRP with IoControlCode IOCTL_61883_CLASS to communicate with 1394 driver stack using the IEC-61883 protocol. |



## Callback functions
| Title | Description |
| ---- |:---- |
| [PBUS_RESET_ROUTINE](nc-61883-pbus_reset_routine.md) | This is a caller-supplied function to be called by the protocol driver when the 1394 bus is reset. |
| [PCMP_MONITOR_ROUTINE](nc-61883-pcmp_monitor_routine.md) | This routine is called for plug monitoring. |
| [PCMP_NOTIFY_ROUTINE](nc-61883-pcmp_notify_routine.md) | This routine is called for plug notification. |


## Structures
| Title | Description |
| ---- |:---- |
| [_AV_61883_REQUEST](ns-61883-_av_61883_request.md) | The AV_61883_REQUEST structure is used to pass requests to the IEC-61883 protocol driver. |
| [_AV_PCR](ns-61883-_av_pcr.md) | The AV_PCR structure specifies settings for an input or output plug. |
| [_BUS_GENERATION_NODE](ns-61883-_bus_generation_node.md) | The BUS_GENERATION_NODE structure is used in conjunction with the Av61883_GetUnitInfo request to retrieve bus characteristics. |
| [_BUS_RESET_NOTIFY](ns-61883-_bus_reset_notify.md) | This structure is used to register or deregister the PBUS_RESET_ROUTINE callback. |
| [_CIP_ATTACH_FRAME](ns-61883-_cip_attach_frame.md) | This structure is used in an attach frame request. |
| [_CIP_CANCEL_FRAME](ns-61883-_cip_cancel_frame.md) | The request cancels an attached frame buffer. A frame can be canceled while the stream is running. |
| [_CIP_DATA_FORMAT_VER2](ns-61883-_cip_data_format_ver2.md) | This structure is a CIP data format which is used by CMP_CONNECT_VER2. |
| [_CIP_DATA_FORMAT_VER3](ns-61883-_cip_data_format_ver3.md) | This structure is used by CipDataFormat. |
| [_CIP_FRAME](ns-61883-_cip_frame.md) | The CIP_FRAME structure describes a frame to be attached to an input or output plug. |
| [_CIP_LISTEN](ns-61883-_cip_listen.md) | This structure is used for a listen request. The request begins isochronous reception on the specified connection. |
| [_CIP_NOTIFY_INFO](ns-61883-_cip_notify_info.md) | The CIP_NOTIFY_INFO structure contains information about the frame. |
| [_CIP_STOP](ns-61883-_cip_stop.md) | This structure is used to stop transmission or reception. |
| [_CIP_TALK](ns-61883-_cip_talk.md) | This structure is used to begin transmission. |
| [_CIP_VALIDATE_INFO](ns-61883-_cip_validate_info.md) | The CIP_VALIDATE_INFO structure contains information about the frame. |
| [_CMP_CONNECT_VER2](ns-61883-_cmp_connect_ver2.md) | This structure contains information for a connection request. The request attempts to make a connection to a plug control register on the local host. |
| [_CMP_CONNECT_VER3](ns-61883-_cmp_connect_ver3.md) | This structure contains information for a connection request. |
| [_CMP_CREATE_PLUG](ns-61883-_cmp_create_plug.md) | This structure is used to create a plug. |
| [_CMP_DELETE_PLUG](ns-61883-_cmp_delete_plug.md) | This structure is used to delete a plug.Av61883_CreatePlug. |
| [_CMP_DISCONNECT](ns-61883-_cmp_disconnect.md) | This structure is used to break a connection. |
| [_CMP_GET_PLUG_HANDLE](ns-61883-_cmp_get_plug_handle.md) | This structure is used in getting the handle of a plug. |
| [_CMP_GET_PLUG_STATE](ns-61883-_cmp_get_plug_state.md) | This structure is used in getting the state of a plug. |
| [_CMP_MONITOR_INFO](ns-61883-_cmp_monitor_info.md) | The CMP_MONITOR_INFO structure is used in conjunction with the Av61883_MonitorPlugs request to allow a driver to monitor access to local oPCR and iPCR plugs. |
| [_CMP_MONITOR_PLUGS](ns-61883-_cmp_monitor_plugs.md) | This structure is used to monitor plug access. The request allows a driver to monitor all access to local oPCR and iPCR plugs. |
| [_CMP_NOTIFY_INFO](ns-61883-_cmp_notify_info.md) | This structure is used by the PCMP_NOTIFY_ROUTINE callback. |
| [_CMP_SET_PLUG](ns-61883-_cmp_set_plug.md) | This structure is used to assign settings to a plug. |
| [_FCP_FRAME](ns-61883-_fcp_frame.md) | The FCP_FRAME structure describes a function control protocol (FCP) request. |
| [_FCP_GET_REQUEST](ns-61883-_fcp_get_request.md) | This structure is used for a get request. |
| [_FCP_GET_RESPONSE](ns-61883-_fcp_get_response.md) | The structure is used in a request yjsy retrieves the next FCP response from the queue of requests maintained by the IEC-61883 protocol driver. |
| [_FCP_SEND_REQUEST](ns-61883-_fcp_send_request.md) | This structure is used for a send request. |
| [_FCP_SEND_RESPONSE](ns-61883-_fcp_send_response.md) | This structure is used for a send response. |
| [_GET_UNIT_CAPABILITIES](ns-61883-_get_unit_capabilities.md) | The GET_UNIT_CAPABILITIES structure is used in conjunction with the Av61883_GetUnitInfo request to retrieve unit information about a device's capabilities. |
| [_GET_UNIT_IDS](ns-61883-_get_unit_ids.md) | The GET_UNIT_CAPABILITIES structure is used in conjunction with the Av61883_GetUnitInfo request to retrieve device identifiers. |
| [_GET_UNIT_INFO](ns-61883-_get_unit_info.md) | This structure is used to get unit information. |
| [_IPCR](ns-61883-_ipcr.md) | The IPCR structure contains initialization values for an input plug. |
| [_OPCR](ns-61883-_opcr.md) | The OPCR structure contains initialization values for an output plug. |
| [_SET_CMP_ADDRESS_TYPE](ns-61883-_set_cmp_address_type.md) | The SET_CMP_ADDRESS_TYPE structure is used in conjunction with the Av61883_SetUnitInfo request to set the parameters that the IEC-61883 protocol driver should use when capturing and transmitting isochronous packets. |
| [_SET_FCP_NOTIFY](ns-61883-_set_fcp_notify.md) | This structure is used for FCP notification. |
| [_SET_UNIT_DIRECTORY](ns-61883-_set_unit_directory.md) | This structure is used to assign settings for a unit directory. |
| [_SET_UNIT_INFO](ns-61883-_set_unit_info.md) | This structure is used to set unit information. |
| [_UNIT_DDI_VERSION](ns-61883-_unit_ddi_version.md) | The UNIT_DDI_VERSION structure is used in conjunction with the Av61883_GetUnitInfo request to retrieve the current 61883 DDI version. |
| [_UNIT_DIAG_LEVEL](ns-61883-_unit_diag_level.md) | The UNIT_DDI_VERSION structure is used in conjunction with the Av61883_GetUnitInfo request to retrieve the current diag level |
| [_UNIT_ISOCH_PARAMS](ns-61883-_unit_isoch_params.md) | The UNIT_ISOCH_PARAMS structure is used to get or set the parameters that the IEC-61883 protocol driver uses when capturing or transmitting isochronous packets. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [CMP_CONNECT_TYPE](ne-61883-cmp_connect_type.md) | This enumeration specifies a connection type. |
| [CMP_PLUG_LOCATION](ne-61883-cmp_plug_location.md) | This enumeration specifies the location of a plug. |
| [CMP_PLUG_TYPE](ne-61883-cmp_plug_type.md) | This enumeration specifies the type of a plug. |