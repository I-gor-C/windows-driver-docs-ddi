# Declarations in the usbcamdi header
This header Usbcamdi contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PADAPTER_RECEIVE_PACKET_ROUTINE callback function](nc-usbcamdi-padapter-receive-packet-routine.md) | TBD |
| [PCAM_PROCESS_PACKET_ROUTINE_EX callback function](nc-usbcamdi-pcam-process-packet-routine-ex.md) | TBD |
| [PCAM_STATE_ROUTINE callback function](nc-usbcamdi-pcam-state-routine.md) | TBD |
| [PCAM_ALLOCATE_BW_ROUTINE callback function](nc-usbcamdi-pcam-allocate-bw-routine.md) | TBD |
| [PCAM_NEW_FRAME_ROUTINE_EX callback function](nc-usbcamdi-pcam-new-frame-routine-ex.md) | TBD |
| [PCAM_INITIALIZE_ROUTINE callback function](nc-usbcamdi-pcam-initialize-routine.md) | TBD |
| [PSTREAM_RECEIVE_PACKET callback function](nc-usbcamdi-pstream-receive-packet.md) | TBD |
| [PFNUSBCAMD_BulkReadWrite callback function](nc-usbcamdi-pfnusbcamd-bulkreadwrite.md) | TBD |
| [PFNUSBCAMD_SetIsoPipeState callback function](nc-usbcamdi-pfnusbcamd-setisopipestate.md) | TBD |
| [PCOMMAND_COMPLETE_FUNCTION callback function](nc-usbcamdi-pcommand-complete-function.md) | TBD |
| [PFNUSBCAMD_CancelBulkReadWrite callback function](nc-usbcamdi-pfnusbcamd-cancelbulkreadwrite.md) | TBD |
| [PCAM_CONFIGURE_ROUTINE callback function](nc-usbcamdi-pcam-configure-routine.md) | TBD |
| [PFNUSBCAMD_WaitOnDeviceEvent callback function](nc-usbcamdi-pfnusbcamd-waitondeviceevent.md) | TBD |
| [PCAM_PROCESS_RAW_FRAME_ROUTINE_EX callback function](nc-usbcamdi-pcam-process-raw-frame-routine-ex.md) | TBD |
| [PCAM_STOP_CAPTURE_ROUTINE callback function](nc-usbcamdi-pcam-stop-capture-routine.md) | TBD |
| [PCAM_STOP_CAPTURE_ROUTINE_EX callback function](nc-usbcamdi-pcam-stop-capture-routine-ex.md) | TBD |
| [PCAM_ALLOCATE_BW_ROUTINE_EX callback function](nc-usbcamdi-pcam-allocate-bw-routine-ex.md) | TBD |
| [PCAM_CONFIGURE_ROUTINE_EX callback function](nc-usbcamdi-pcam-configure-routine-ex.md) | TBD |
| [PCAM_START_CAPTURE_ROUTINE callback function](nc-usbcamdi-pcam-start-capture-routine.md) | TBD |
| [PFNUSBCAMD_SetVideoFormat callback function](nc-usbcamdi-pfnusbcamd-setvideoformat.md) | TBD |
| [PCAM_NEW_FRAME_ROUTINE callback function](nc-usbcamdi-pcam-new-frame-routine.md) | TBD |
| [PCAM_PROCESS_PACKET_ROUTINE callback function](nc-usbcamdi-pcam-process-packet-routine.md) | TBD |
| [PCAM_FREE_BW_ROUTINE callback function](nc-usbcamdi-pcam-free-bw-routine.md) | TBD |
| [PCAM_PROCESS_RAW_FRAME_ROUTINE callback function](nc-usbcamdi-pcam-process-raw-frame-routine.md) | TBD |
| [PCAM_FREE_BW_ROUTINE_EX callback function](nc-usbcamdi-pcam-free-bw-routine-ex.md) | TBD |
| [PCAM_START_CAPTURE_ROUTINE_EX callback function](nc-usbcamdi-pcam-start-capture-routine-ex.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [PUSBCAMD_INTERFACE structure](ns-usbcamdi-pusbcamd-interface.md) | The USBCAMD_INTERFACE structure defines a set of services related to the USB bus interfaces. |
| [pipe_config_descriptor structure](ns-usbcamdi--pipe-config-descriptor.md) | The USBCAMD_Pipe_Config_Descriptor structure describes the association between pipes and streams. |
| [USBCAMD_DEVICE_DATA structure](ns-usbcamdi--usbcamd-device-data.md) | This structure is obsolete and is provided to maintain backward compatibility with the original USBCAMD. |
| [USBCAMD_DEVICE_DATA2 structure](ns-usbcamdi--usbcamd-device-data2.md) | The USBCAMD_DEVICE_DATA2 structure specifies the entry points for a camera minidriver's functions that USBCAMD calls. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [USBCAMD_CamControlFlags enumeration](ne-usbcamdi-usbcamd-camcontrolflags.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [USBCAMD_AdapterReceivePacket function](nf-usbcamdi-usbcamd-adapterreceivepacket.md) | The USBCAMD_AdapterReceivePacket function allows USBCAMD to process an adapter-based stream request block (SRB). |
| [USBCAMD_Debug_LogEntry function](nf-usbcamdi-usbcamd-debug-logentry.md) | The USBCAMD_Debug_LogEntry function is called by the camera minidriver to log debugging information to a file. |
| [USBCAMD_InitializeNewInterface function](nf-usbcamdi-usbcamd-initializenewinterface.md) | The USBCAMD_InitializeNewInterface function provides USBCAMD with all the necessary information to configure the camera minidriver to work correctly with the stream class driver and the USB bus driver. |
| [USBCAMD_SelectAlternateInterface function](nf-usbcamdi-usbcamd-selectalternateinterface.md) | The USBCAMD_SelectAlternateInterface function selects an alternate setting within the USB video streaming interface. |
| [USBCAMD_DriverEntry function](nf-usbcamdi-usbcamd-driverentry.md) | The USBCAMD_DriverEntry function registers the minidriver with USBCAMD, effectively binding USBCAMD and the minidriver together. |
| [USBCAMD_ControlVendorCommand function](nf-usbcamdi-usbcamd-controlvendorcommand.md) | The USBCAMD_ControlVendorCommand function sends vendor-specific commands to the control pipe. |
| [USBCAMD_GetRegistryKeyValue function](nf-usbcamdi-usbcamd-getregistrykeyvalue.md) | The USBCAMD_GetRegistryKeyValue function retrieves the device-instance-specific registry key value. |
| [ILOGENTRY function](nf-usbcamdi-ilogentry.md) | TBD |

This header is used in these topics:

- [stream](..content/_stream)
