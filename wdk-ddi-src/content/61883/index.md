# 61883.h header


This header is used by IEEE. For more information, see
- [IEEE](../_IEEE/index.md)

61883.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PBUS_RESET_ROUTINE callback](nc-61883-pbus-reset-routine.md) | This is a caller-supplied function to be called by the protocol driver when the 1394 bus is reset. |
| [PCMP_MONITOR_ROUTINE callback](nc-61883-pcmp-monitor-routine.md) | This routine is called for plug monitoring. |
| [PCMP_NOTIFY_ROUTINE callback](nc-61883-pcmp-notify-routine.md) | This routine is called for plug notification. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [AV_61883_REQUEST structure](ns-61883--av-61883-request.md) | The AV_61883_REQUEST structure is used to pass requests to the IEC-61883 protocol driver. |
| [AV_PCR structure](ns-61883--av-pcr.md) | The AV_PCR structure specifies settings for an input or output plug. |
| [BUS_GENERATION_NODE structure](ns-61883--bus-generation-node.md) | The BUS_GENERATION_NODE structure is used in conjunction with the Av61883_GetUnitInfo request to retrieve bus characteristics. |
| [BUS_RESET_NOTIFY structure](ns-61883--bus-reset-notify.md) | This structure is used to register or deregister the PBUS_RESET_ROUTINE callback. |
| [CIP_ATTACH_FRAME structure](ns-61883--cip-attach-frame.md) | This structure is used in an attach frame request. |
| [CIP_CANCEL_FRAME structure](ns-61883--cip-cancel-frame.md) | This structure is used in a cancel frame request. |
| [CIP_DATA_FORMAT_VER2 structure](ns-61883--cip-data-format-ver2.md) | This structure is a CIP data format which is used by CMP_CONNECT_VER2. |
| [CIP_DATA_FORMAT_VER3 structure](ns-61883--cip-data-format-ver3.md) | This structure is used by CipDataFormat. |
| [CIP_FRAME structure](ns-61883--cip-frame.md) | The CIP_FRAME structure describes a frame to be attached to an input or output plug. |
| [CIP_FRAME structure](ns-61883--cip-frame~r1.md) | The CIP_FRAME structure describes a frame to be attached to an input or output plug. |
| [CIP_LISTEN structure](ns-61883--cip-listen.md) | This structure is used for a listen request. |
| [CIP_NOTIFY_INFO structure](ns-61883--cip-notify-info.md) | The CIP_NOTIFY_INFO structure contains information about the frame. |
| [CIP_STOP structure](ns-61883--cip-stop.md) | This structure is used to stop transmission or reception. |
| [CIP_TALK structure](ns-61883--cip-talk.md) | This structure is used to begin transmission. |
| [CIP_VALIDATE_INFO structure](ns-61883--cip-validate-info.md) | The CIP_VALIDATE_INFO structure contains information about the frame. |
| [CMP_CONNECT_VER2 structure](ns-61883--cmp-connect-ver2.md) | This structure contains information for a connection request. |
| [CMP_CONNECT_VER3 structure](ns-61883--cmp-connect-ver3.md) | This structure contains information for a connection request. |
| [CMP_CREATE_PLUG structure](ns-61883--cmp-create-plug.md) | This structure is used to create a plug. |
| [CMP_DELETE_PLUG structure](ns-61883--cmp-delete-plug.md) | This structure is used to create a plug. |
| [CMP_DISCONNECT structure](ns-61883--cmp-disconnect.md) | This structure is used to break a connection. |
| [CMP_GET_PLUG_HANDLE structure](ns-61883--cmp-get-plug-handle.md) | This structure is used in getting the handle of a plug. |
| [CMP_GET_PLUG_STATE structure](ns-61883--cmp-get-plug-state.md) | This structure is used in getting the state of a plug. |
| [CMP_MONITOR_INFO structure](ns-61883--cmp-monitor-info.md) | The CMP_MONITOR_INFO structure is used in conjunction with the Av61883_MonitorPlugs request to allow a driver to monitor access to local oPCR and iPCR plugs. |
| [CMP_MONITOR_PLUGS structure](ns-61883--cmp-monitor-plugs.md) | This structure is used to monitor plug access. |
| [CMP_NOTIFY_INFO structure](ns-61883--cmp-notify-info.md) | This structure is used by the PCMP_NOTIFY_ROUTINE callback. |
| [CMP_SET_PLUG structure](ns-61883--cmp-set-plug.md) | This structure is used to assign settings to a plug. |
| [FCP_FRAME structure](ns-61883--fcp-frame.md) | The FCP_FRAME structure describes a function control protocol (FCP) request. |
| [FCP_GET_REQUEST structure](ns-61883--fcp-get-request.md) | This structure is used for a get request. |
| [FCP_GET_RESPONSE structure](ns-61883--fcp-get-response.md) | This structure is used for a get response. |
| [FCP_GET_RESPONSE structure](ns-61883--fcp-get-response~r1.md) | This structure is used for a get response. |
| [FCP_SEND_REQUEST structure](ns-61883--fcp-send-request.md) | This structure is used for a send request. |
| [FCP_SEND_REQUEST structure](ns-61883--fcp-send-request~r1.md) | This structure is used for a send request. |
| [FCP_SEND_RESPONSE structure](ns-61883--fcp-send-response.md) | This structure is used for a send response. |
| [GET_UNIT_CAPABILITIES structure](ns-61883--get-unit-capabilities.md) | The GET_UNIT_CAPABILITIES structure is used in conjunction with the Av61883_GetUnitInfo request to retrieve unit information about a device's capabilities. |
| [GET_UNIT_IDS structure](ns-61883--get-unit-ids.md) | The GET_UNIT_CAPABILITIES structure is used in conjunction with the Av61883_GetUnitInfo request to retrieve device identifiers. |
| [GET_UNIT_INFO structure](ns-61883--get-unit-info.md) | This structure is used to get unit information. |
| [IPCR structure](ns-61883--ipcr.md) | The IPCR structure contains initialization values for an input plug. |
| [OPCR structure](ns-61883--opcr.md) | The OPCR structure contains initialization values for an output plug. |
| [SET_CMP_ADDRESS_TYPE structure](ns-61883--set-cmp-address-type.md) | The SET_CMP_ADDRESS_TYPE structure is used in conjunction with the Av61883_SetUnitInfo request to set the parameters that the IEC-61883 protocol driver should use when capturing and transmitting isochronous packets. |
| [SET_FCP_NOTIFY structure](ns-61883--set-fcp-notify.md) | This structure is used for FCP notification. |
| [SET_UNIT_DIRECTORY structure](ns-61883--set-unit-directory.md) | This structure is used to assign settings for a unit directory. |
| [SET_UNIT_INFO structure](ns-61883--set-unit-info.md) | This structure is used to set unit information. |
| [UNIT_DDI_VERSION structure](ns-61883--unit-ddi-version.md) | The UNIT_DDI_VERSION structure is used in conjunction with the Av61883_GetUnitInfo request to retrieve the current 61883 DDI version. |
| [UNIT_DIAG_LEVEL structure](ns-61883--unit-diag-level.md) | The UNIT_DDI_VERSION structure is used in conjunction with the Av61883_GetUnitInfo request to retrieve the current diag level |
| [UNIT_ISOCH_PARAMS structure](ns-61883--unit-isoch-params.md) | The UNIT_ISOCH_PARAMS structure is used to get or set the parameters that the IEC-61883 protocol driver uses when capturing or transmitting isochronous packets. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_61883_CLASS IOCTL](ni-61883-ioctl-61883-class.md) | An IEC-61883 client driver uses the IRP_MJ_INTERNAL_DEVICE_CONTROL IRP with IoControlCode IOCTL_61883_CLASS to communicate with 1394 driver stack using the IEC-61883 protocol. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [CMP_CONNECT_TYPE enumeration](ne-61883-cmp-connect-type.md) | This enumeration specifies a connection type. |
| [CMP_PLUG_LOCATION enumeration](ne-61883-cmp-plug-location.md) | This enumeration specifies the location of a plug. |
| [CMP_PLUG_TYPE enumeration](ne-61883-cmp-plug-type.md) | This enumeration specifies the type of a plug. |
