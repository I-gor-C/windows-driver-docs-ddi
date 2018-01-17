---
UID: TP:stream
ms.assetid: 955ea1c2-d8bc-36d6-8195-eadc9d53b016
ms.author: windowsdriverdev
ms.date: 01/16/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# Streaming media devices


Overview of the Streaming media devices technology.

To develop Streaming media devices, you need these headers:

 * [avc.h](..\avc\index.md)
 * [avcstrm.h](..\avcstrm\index.md)
 * [bdasup.h](..\bdasup\index.md)
 * [kcom.h](..\kcom\index.md)
 * [ksi.h](..\ksi\index.md)
 * [msviddrv.h](..\msviddrv\index.md)
 * [strmini.h](..\strmini\index.md)
 * [swenum.h](..\swenum\index.md)
 * [usbcamdi.h](..\usbcamdi\index.md)

For the programming guide, see [Streaming media devices](https://docs.microsoft.com/en-us/windows-hardware/drivers/stream).

## Functions

| Title   | Description   |
| ---- |:---- |
| [BdaCheckChanges function](..\bdasup\nf-bdasup-bdacheckchanges.md) | The BdaCheckChanges function verifies a new set of BDA topology changes before they are committed. |
| [BdaCommitChanges function](..\bdasup\nf-bdasup-bdacommitchanges.md) | The BdaCommitChanges function commits the changes to BDA topology that have occurred since the last call to the BdaStartChanges function. |
| [BdaCreateFilterFactory function](..\bdasup\nf-bdasup-bdacreatefilterfactory.md) | The BdaCreateFilterFactory function adds the specified filter descriptor as a filter factory to the specified device and associates the filter factory with the specified BDA template topology. |
| [BdaCreateFilterFactoryEx function](..\bdasup\nf-bdasup-bdacreatefilterfactoryex.md) | The BdaCreateFilterFactoryEx function adds the specified filter descriptor as a filter factory to the specified device and associates the filter factory with the specified BDA template topology. |
| [BdaCreatePin function](..\bdasup\nf-bdasup-bdacreatepin.md) | The BdaCreatePin function creates a new pin in the specified filter. |
| [BdaCreateTopology function](..\bdasup\nf-bdasup-bdacreatetopology.md) | The BdaCreateTopology function creates the topology between two pins. |
| [BdaDeletePin function](..\bdasup\nf-bdasup-bdadeletepin.md) | The BdaDeletePin function deletes a pin from the specified filter. |
| [BdaFilterFactoryUpdateCacheData function](..\bdasup\nf-bdasup-bdafilterfactoryupdatecachedata.md) | The BdaFilterFactoryUpdateCacheData function updates the pin data cache for an instance of a filter. |
| [BdaGetChangeState function](..\bdasup\nf-bdasup-bdagetchangestate.md) | The BdaGetChangeState function returns the current change state of BDA topology. |
| [BdaInitFilter function](..\bdasup\nf-bdasup-bdainitfilter.md) | The BdaInitFilter function initializes the BDA filter context associated with a filter instance. |
| [BdaMethodCreatePin function](..\bdasup\nf-bdasup-bdamethodcreatepin.md) | The BdaMethodCreatePin function creates a pin factory. |
| [BdaMethodCreateTopology function](..\bdasup\nf-bdasup-bdamethodcreatetopology.md) | The BdaMethodCreateTopology function creates a template topology between two pins of a filter. |
| [BdaMethodDeletePin function](..\bdasup\nf-bdasup-bdamethoddeletepin.md) | The BdaMethodDeletePin function deletes a pin factory. |
| [BdaPropertyGetControllingPinId function](..\bdasup\nf-bdasup-bdapropertygetcontrollingpinid.md) | The BdaPropertyGetControllingPinId function retrieves the identifier of a pin on which to control the properties, methods, and events of a specific node. |
| [BdaPropertyGetPinControl function](..\bdasup\nf-bdasup-bdapropertygetpincontrol.md) | The BdaPropertyGetPinControl function retrieves either the identifier or type of a pin. |
| [BdaPropertyNodeDescriptors function](..\bdasup\nf-bdasup-bdapropertynodedescriptors.md) | The BdaPropertyNodeDescriptors function retrieves a list of nodes in a template topology. |
| [BdaPropertyNodeEvents function](..\bdasup\nf-bdasup-bdapropertynodeevents.md) | The BdaPropertyNodeEvents function retrieves a list of events that a node supports. |
| [BdaPropertyNodeMethods function](..\bdasup\nf-bdasup-bdapropertynodemethods.md) | The BdaPropertyNodeMethods function retrieves a list of methods that a node supports. |
| [BdaPropertyNodeProperties function](..\bdasup\nf-bdasup-bdapropertynodeproperties.md) | The BdaPropertyNodeProperties function retrieves a list of properties that a node supports. |
| [BdaPropertyNodeTypes function](..\bdasup\nf-bdasup-bdapropertynodetypes.md) | The BdaPropertyNodeTypes function retrieves a list of node types in a template topology. |
| [BdaPropertyPinTypes function](..\bdasup\nf-bdasup-bdapropertypintypes.md) | The BdaPropertyPinTypes function retrieves a list of pin types in a template topology. |
| [BdaPropertyTemplateConnections function](..\bdasup\nf-bdasup-bdapropertytemplateconnections.md) | The BdaPropertyTemplateConnections function retrieves a list of connections that describe how pin types and node types are connected in a template topology. |
| [BdaStartChanges function](..\bdasup\nf-bdasup-bdastartchanges.md) | The BdaStartChanges function initiates the setting of new BDA topology changes. |
| [BdaUninitFilter function](..\bdasup\nf-bdasup-bdauninitfilter.md) | The BdaUninitFilter function removes the BDA filter context from the associated filter instance. |
| [BdaValidateNodeProperty function](..\bdasup\nf-bdasup-bdavalidatenodeproperty.md) | The BdaValidateNodeProperty function validates that a node property request is associated with a specific pin. |
| [KoCreateInstance function](..\kcom\nf-kcom-kocreateinstance.md) | The KoCreateInstance function creates an object of the class with the specified CLSID. |
| [KoDeviceInitialize function](..\kcom\nf-kcom-kodeviceinitialize.md) | The KoDeviceInitialize function adds a kernel COM create-item entry to the specified device object. |
| [KoDriverInitialize function](..\kcom\nf-kcom-kodriverinitialize.md) | The KoDriverInitialize function initializes a driver object to handle the kernel streaming interface. |
| [KoRelease function](..\kcom\nf-kcom-korelease.md) | The KoRelease function decrements the reference count for the calling interface on an object. |
| [KsCreateBusEnumObject function](..\swenum\nf-swenum-kscreatebusenumobject.md) | The KsCreateBusEnumObject function creates a demand-load bus enumerator object and initializes it for use with the demand-load bus enumerator services. |
| [KsDereferenceSoftwareBusObject function](..\swenum\nf-swenum-ksdereferencesoftwarebusobject.md) | The KsDereferenceSoftwareBusObject function decrements the reference count of the demand-load bus enumerator object's PDO. |
| [KsGetBusEnumIdentifier function](..\swenum\nf-swenum-ksgetbusenumidentifier.md) | The KsGetBusEnumIdentifier function retrieves the software bus enumerator identifier for the bus device associated with the given IRP. |
| [KsGetBusEnumParentFDOFromChildPDO function](..\swenum\nf-swenum-ksgetbusenumparentfdofromchildpdo.md) | The KsGetBusEnumParentFDOFromChildPDO function retrieves the FDO of the parent of the given child PDO. |
| [KsGetBusEnumPnpDeviceObject function](..\swenum\nf-swenum-ksgetbusenumpnpdeviceobject.md) | The KsGetBusEnumPnpDeviceObject function retrieves the Plug and Play device object attached to the given device object. |
| [KsInstallBusEnumInterface function](..\swenum\nf-swenum-ksinstallbusenuminterface.md) | The KsInstallBusEnumInterface function installs an interface to the demand-load bus enumerator object. |
| [KsIsBusEnumChildDevice function](..\swenum\nf-swenum-ksisbusenumchilddevice.md) | The KsIsBusEnumChildDevice function determines if the given device object is a child device of the demand-load bus enumerator object. |
| [KsQuerySoftwareBusInterface function](..\swenum\nf-swenum-ksquerysoftwarebusinterface.md) | The KsQuerySoftwareBusInterface function creates a buffer from the paged pool and copies the reference string associated with the demand-load bus enumerator object's PDO into the buffer. |
| [KsReferenceSoftwareBusObject function](..\swenum\nf-swenum-ksreferencesoftwarebusobject.md) | The KsReferenceSoftwareBusObject function increments the reference count of the demand-load bus enumerator object's PDO. |
| [KsRemoveBusEnumInterface function](..\swenum\nf-swenum-ksremovebusenuminterface.md) | The KsRemoveBusEnumInterface function removes an interface to the demand-load bus enumerator object. |
| [KsServiceBusEnumCreateRequest function](..\swenum\nf-swenum-ksservicebusenumcreaterequest.md) | The KsServiceBusEnumCreateRequest function services IRP_MJ_CREATE requests for the software bus device interface. |
| [KsServiceBusEnumPnpRequest function](..\swenum\nf-swenum-ksservicebusenumpnprequest.md) | The KsServiceBusEnumPnpRequest function services IRP_MJ_PNP requests on behalf of the demand-load bus enumerator object that was created with KsCreateBusEnumObject. |
| [StreamClassAbortOutstandingRequests function](..\strmini\nf-strmini-streamclassabortoutstandingrequests.md) | The StreamClassAbortOutstandingRequests routine aborts all outstanding requests, either to a particular stream, or to the entire driver. |
| [StreamClassCallAtNewPriority function](..\strmini\nf-strmini-streamclasscallatnewpriority.md) | The StreamClassCallAtNewPriority routine schedules a routine to be called at a different priority. |
| [StreamClassCompleteRequestAndMarkQueueReady function](..\strmini\nf-strmini-streamclasscompleterequestandmarkqueueready.md) | The StreamClassCompleteRequestAndMarkQueueReady routine completes a request, and signals the class driver that the minidriver is ready to receive a new request of the same type. |
| [StreamClassDebugAssert function](..\strmini\nf-strmini-streamclassdebugassert.md) | A minidriver can use the StreamClassDebugAssert routine in a checked build environment to fail an assert, causing the stream class driver to output a debug message and break into the kernel debugger. |
| [StreamClassDebugPrint function](..\strmini\nf-strmini-streamclassdebugprint.md) | In a checked build environment, the minidriver can use the StreamClassDebugPrint routine to print debug messages to the application window and to the Debugger Command window. |
| [StreamClassDeviceNotification function](..\strmini\nf-strmini-streamclassdevicenotification.md) | Minidrivers use the StreamClassDeviceNotification routine to notify the class driver that it has completed a stream request, or that an event has occurred. |
| [StreamClassFilterReenumerateStreams function](..\strmini\nf-strmini-streamclassfilterreenumeratestreams.md) | Obsolete. Do not use. |
| [StreamClassGetDmaBuffer function](..\strmini\nf-strmini-streamclassgetdmabuffer.md) | The StreamClassGetDmaBuffer routine returns a pointer to the DMA buffer that the class driver allocates for the minidriver. |
| [StreamClassGetNextEvent function](..\strmini\nf-strmini-streamclassgetnextevent.md) | Minidrivers can use the StreamClassGetNextEvent routine to search the event queue of a device or of a particular stream. |
| [StreamClassGetPhysicalAddress function](..\strmini\nf-strmini-streamclassgetphysicaladdress.md) | The StreamClassGetPhysicalAddress routine translates a virtual memory address to a physical memory address and locks the corresponding physical memory for a DMA operation. |
| [StreamClassQueryMasterClock function](..\strmini\nf-strmini-streamclassquerymasterclock.md) | When the minidriver calls the StreamClassQueryMasterClock routine, the class driver queries the appropriate time value of the master clock asynchronously, and passes the result to the routine passed in the ClockCallbackRoutine parameter. |
| [StreamClassQueryMasterClockSync function](..\strmini\nf-strmini-streamclassquerymasterclocksync.md) | The minidriver may call the StreamClassQueryMasterClockSync routine to synchronously query a stream's master clock. |
| [StreamClassReadWriteConfig function](..\strmini\nf-strmini-streamclassreadwriteconfig.md) | The StreamClassReadWriteConfig routine reads or writes configuration data for the minidriver's parent bus driver. |
| [StreamClassReenumerateStreams function](..\strmini\nf-strmini-streamclassreenumeratestreams.md) | Obsolete. Do not use. |
| [StreamClassRegisterAdapter function](..\strmini\nf-strmini-streamclassregisteradapter.md) | The StreamClassRegisterAdapter routine registers a stream class minidriver. |
| [StreamClassRegisterFilterWithNoKSPins function](..\strmini\nf-strmini-streamclassregisterfilterwithnokspins.md) | The StreamClassRegisterFilterWithNoKSPins routine is used to register filter drivers with Microsoft DirectShow that have no kernel streaming pins and, therefore, do not stream in kernel mode. |
| [StreamClassScheduleTimer function](..\strmini\nf-strmini-streamclassscheduletimer.md) | The minidriver calls the StreamClassScheduleTimer routine to schedule a timer, and to specify a routine that is called when the timer expires. |
| [StreamClassStreamNotification function](..\strmini\nf-strmini-streamclassstreamnotification.md) | Streams use the StreamClassStreamNotification routine to notify the class driver that it has completed a stream request, or that an event has occurred. |
| [USBCAMD_AdapterReceivePacket function](..\usbcamdi\nf-usbcamdi-usbcamd_adapterreceivepacket.md) | The USBCAMD_AdapterReceivePacket function allows USBCAMD to process an adapter-based stream request block (SRB). |
| [USBCAMD_ControlVendorCommand function](..\usbcamdi\nf-usbcamdi-usbcamd_controlvendorcommand.md) | The USBCAMD_ControlVendorCommand function sends vendor-specific commands to the control pipe. |
| [USBCAMD_Debug_LogEntry function](..\usbcamdi\nf-usbcamdi-usbcamd_debug_logentry.md) | The USBCAMD_Debug_LogEntry function is called by the camera minidriver to log debugging information to a file. |
| [USBCAMD_DriverEntry function](..\usbcamdi\nf-usbcamdi-usbcamd_driverentry.md) | The USBCAMD_DriverEntry function registers the minidriver with USBCAMD, effectively binding USBCAMD and the minidriver together. |
| [USBCAMD_GetRegistryKeyValue function](..\usbcamdi\nf-usbcamdi-usbcamd_getregistrykeyvalue.md) | The USBCAMD_GetRegistryKeyValue function retrieves the device-instance-specific registry key value. |
| [USBCAMD_InitializeNewInterface function](..\usbcamdi\nf-usbcamdi-usbcamd_initializenewinterface.md) | The USBCAMD_InitializeNewInterface function provides USBCAMD with all the necessary information to configure the camera minidriver to work correctly with the stream class driver and the USB bus driver. |
| [USBCAMD_SelectAlternateInterface function](..\usbcamdi\nf-usbcamdi-usbcamd_selectalternateinterface.md) | The USBCAMD_SelectAlternateInterface function selects an alternate setting within the USB video streaming interface. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PADAPTER_RECEIVE_PACKET_ROUTINE callback](..\usbcamdi\nc-usbcamdi-padapter_receive_packet_routine.md) | A camera minidriver's AdapterReceivePacket callback function processes adapter-based stream request blocks (SRBs) passed to it by the stream class driver. |
| [PCAM_ALLOCATE_BW_ROUTINE callback](..\usbcamdi\nc-usbcamdi-pcam_allocate_bw_routine.md) | A camera minidriver's CamAllocateBandwidth callback function selects the appropriate alternate setting within the USB video streaming interface and prepares the device to stream. |
| [PCAM_ALLOCATE_BW_ROUTINE_EX callback](..\usbcamdi\nc-usbcamdi-pcam_allocate_bw_routine_ex.md) | A camera minidriver's CamAllocateBandwidthEx callback function selects the appropriate alternate setting within the USB video streaming interface and prepares the device to stream. |
| [PCAM_CONFIGURE_ROUTINE callback](..\usbcamdi\nc-usbcamdi-pcam_configure_routine.md) | A camera minidriver's CamConfigure callback function configures the isochronous streaming interface. |
| [PCAM_CONFIGURE_ROUTINE_EX callback](..\usbcamdi\nc-usbcamdi-pcam_configure_routine_ex.md) | A camera minidriver's CamConfigureEx callback function configures the isochronous streaming interface. |
| [PCAM_FREE_BW_ROUTINE callback](..\usbcamdi\nc-usbcamdi-pcam_free_bw_routine.md) | A camera minidriver's CamFreeBandwidth callback function selects an alternate setting within the USB video streaming interface that uses no bandwidth. |
| [PCAM_FREE_BW_ROUTINE_EX callback](..\usbcamdi\nc-usbcamdi-pcam_free_bw_routine_ex.md) | A camera minidriver's CamFreeBandwidthEx callback function selects an alternate setting within the USB video streaming interface that uses no bandwidth. |
| [PCAM_INITIALIZE_ROUTINE callback](..\usbcamdi\nc-usbcamdi-pcam_initialize_routine.md) | A camera minidriver's callback function initializes the device or performs any minidriver-specific clean-up that is required. |
| [PCAM_NEW_FRAME_ROUTINE callback](..\usbcamdi\nc-usbcamdi-pcam_new_frame_routine.md) | A camera minidriver's CamNewVideoFrame callback function initializes a new video frame context structure. |
| [PCAM_NEW_FRAME_ROUTINE_EX callback](..\usbcamdi\nc-usbcamdi-pcam_new_frame_routine_ex.md) | A camera minidriver's CamNewVideoFrameEx callback function initializes a new video frame context structure. |
| [PCAM_PROCESS_PACKET_ROUTINE callback](..\usbcamdi\nc-usbcamdi-pcam_process_packet_routine.md) | A camera minidriver's CamProcessUSBPacket callback function processes a USB packet. |
| [PCAM_PROCESS_PACKET_ROUTINE_EX callback](..\usbcamdi\nc-usbcamdi-pcam_process_packet_routine_ex.md) | A camera minidriver's CamProcessUSBPacketEx callback function processes a USB packet. |
| [PCAM_PROCESS_RAW_FRAME_ROUTINE callback](..\usbcamdi\nc-usbcamdi-pcam_process_raw_frame_routine.md) | A camera minidriver's CamProcessRawVideoFrame callback function decodes a raw video frame. |
| [PCAM_PROCESS_RAW_FRAME_ROUTINE_EX callback](..\usbcamdi\nc-usbcamdi-pcam_process_raw_frame_routine_ex.md) | A camera minidriver's CamProcessRawVideoFrameEx callback function decodes a raw video frame. |
| [PCAM_START_CAPTURE_ROUTINE callback](..\usbcamdi\nc-usbcamdi-pcam_start_capture_routine.md) | A camera minidriver's CamStartCapture callback function selects the appropriate alternate setting within the USB video streaming interface and prepares the device to stream. |
| [PCAM_START_CAPTURE_ROUTINE_EX callback](..\usbcamdi\nc-usbcamdi-pcam_start_capture_routine_ex.md) | A camera minidriver's CamStartCaptureEx callback function selects the appropriate alternate setting within the USB video streaming interface and prepares the device to stream. |
| [PCAM_STATE_ROUTINE callback](..\usbcamdi\nc-usbcamdi-pcam_state_routine.md) | A camera minidriver's state callback function restores a previously saved device context state or saves the current device context state. |
| [PCAM_STOP_CAPTURE_ROUTINE callback](..\usbcamdi\nc-usbcamdi-pcam_stop_capture_routine.md) | A camera minidriver's CamStopCapture callback function performs any processing after the stream is stopped. |
| [PCAM_STOP_CAPTURE_ROUTINE_EX callback](..\usbcamdi\nc-usbcamdi-pcam_stop_capture_routine_ex.md) | A camera minidriver's CamStopCaptureEx callback function performs any processing after the stream is stopped. |
| [PCOMMAND_COMPLETE_FUNCTION callback](..\usbcamdi\nc-usbcamdi-pcommand_complete_function.md) | A camera minidriver's CommandCompleteFunction callback function allows the camera minidriver to perform any additional tasks necessary to complete certain USBCAMD services |
| [PFNAVCINTERSECTHANDLER callback](..\avc\nc-avc-pfnavcintersecthandler.md) | The AV/C intersect handler determines if the data ranges are compatible. |
| [PFNUSBCAMD_BulkReadWrite callback](..\usbcamdi\nc-usbcamdi-pfnusbcamd_bulkreadwrite.md) | The USBCAMD_BulkReadWrite service performs a read or write operation on the specified bulk pipe. |
| [PFNUSBCAMD_CancelBulkReadWrite callback](..\usbcamdi\nc-usbcamdi-pfnusbcamd_cancelbulkreadwrite.md) | The USBCAMD_CancelBulkReadWrite service cancels a pending bulk read or write request. |
| [PFNUSBCAMD_SetIsoPipeState callback](..\usbcamdi\nc-usbcamdi-pfnusbcamd_setisopipestate.md) | The USBCAMD_SetIsoPipeState service permits the camera minidriver to control the streaming state on the isochronous pipe. |
| [PFNUSBCAMD_SetVideoFormat callback](..\usbcamdi\nc-usbcamdi-pfnusbcamd_setvideoformat.md) | The USBCAMD_SetVideoFormat service is used to notify USBCAMD that the video format has changed. |
| [PFNUSBCAMD_WaitOnDeviceEvent callback](..\usbcamdi\nc-usbcamdi-pfnusbcamd_waitondeviceevent.md) | The USBCAMD_WaitOnDeviceEvent service is used to perform a read from the interrupt pipe if the camera has an interrupt pipe for external event notifications. |
| [PHW_CANCEL_SRB callback](..\strmini\nc-strmini-phw_cancel_srb.md) | The class driver calls the minidriver's StrMiniCancelPacket routine to signal that a stream request has been canceled. |
| [PHW_EVENT_ROUTINE callback](..\strmini\nc-strmini-phw_event_routine.md) | The class driver calls the stream minidriver's StrMiniEvent routine to signal to a minidriver an event should be enabled or disabled. |
| [PHW_INTERRUPT callback](..\strmini\nc-strmini-phw_interrupt.md) | StrMiniInterrupt is the minidriver's interrupt service routine. |
| [PHW_PRIORITY_ROUTINE callback](..\strmini\nc-strmini-phw_priority_routine.md) | StrMiniPriorityRoutine is a minidriver-supplied callback routine to be executed at a specified priority level. |
| [PHW_QUERY_CLOCK_ROUTINE callback](..\strmini\nc-strmini-phw_query_clock_routine.md) | Each stream may have a clock associated to it. The class driver queries the clock by calling the stream minidriver-supplied StrMiniClock function, provided in each stream's HW_STREAM_OBJECT. |
| [PHW_RECEIVE_DEVICE_SRB callback](..\strmini\nc-strmini-phw_receive_device_srb.md) | The stream class driver calls the minidriver's StrMiniReceiveStreamControlPacket routine to handle I/O requests for a specific stream. |
| [PHW_REQUEST_TIMEOUT_HANDLER callback](..\strmini\nc-strmini-phw_request_timeout_handler.md) | The stream class driver calls the minidriver's StrMiniRequestTimeout routine to signal to the minidriver that a request has timed out. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [KSCLOCKINSTANCE structure](..\ksi\ns-ksi-ksclockinstance.md) | . |
| [KSIDEFAULTCLOCK structure](..\ksi\ns-ksi-ksidefaultclock.md) | . |
| [KSSCATTER_GATHER structure](..\strmini\ns-strmini-ksscatter_gather.md) | . |
| [USBCAMD_INTERFACE structure](..\usbcamdi\ns-usbcamdi-usbcamd_interface.md) | The USBCAMD_INTERFACE structure defines a set of services related to the USB bus interfaces. |
| [_AVCCONNECTINFO structure](..\avc\ns-avc-_avcconnectinfo.md) | The AVCCONNECTINFO structure is used to initialize a subunit driver and establish pin connections. |
| [_AVCPRECONNECTINFO structure](..\avc\ns-avc-_avcpreconnectinfo.md) | The AVCPRECONNECTINFO structure is used to initialize a subunit driver and establish pin connections. |
| [_AVCSTRM_BUFFER_STRUCT structure](..\avcstrm\ns-avcstrm-_avcstrm_buffer_struct.md) | The AVCSTRM_BUFFER_STRUCT structure describes a buffer to be submitted to avcstrm.sys for read or write operations. |
| [_AVCSTRM_FORMAT_INFO structure](..\avcstrm\ns-avcstrm-_avcstrm_format_info.md) | The AVCSTRM_FORMAT_INFO structure is used to describe a data stream. |
| [_AVCSTRM_OPEN_STRUCT structure](..\avcstrm\ns-avcstrm-_avcstrm_open_struct.md) | The AVCSTRM_OPEN_STRUCT structure describes a data stream to be opened. |
| [_AVC_COMMAND_IRB structure](..\avc\ns-avc-_avc_command_irb.md) | The AVC_COMMAND_IRB structure defines a structure that contains an AV/C command and response pair. |
| [_AVC_EXT_PLUG_COUNTS structure](..\avc\ns-avc-_avc_ext_plug_counts.md) | The AVC_EXT_PLUG_COUNTS structure describes the number of external plugs on the subunit. |
| [_AVC_IRB structure](..\avc\ns-avc-_avc_irb.md) | The AVC_IRB structure is an I/O Request Block (IRB) header structure where a function number is stored. |
| [_AVC_MULTIFUNC_IRB structure](..\avc\ns-avc-_avc_multifunc_irb.md) | The AVC_MULTIFUNC_IRB structure contains other AV/C related structures in a union. |
| [_AVC_PEER_DO_LIST structure](..\avc\ns-avc-_avc_peer_do_list.md) | The AVC_PEER_DO_LIST describes all nonvirtual (peer) instances of avc.sys. |
| [_AVC_PEER_DO_LOCATOR structure](..\avc\ns-avc-_avc_peer_do_locator.md) | The AVC_PEER_DO_LOCATOR describes nonvirtual (peer) instances of avc.sys. |
| [_AVC_PIN_COUNT structure](..\avc\ns-avc-_avc_pin_count.md) | The AVC_PIN_COUNT structure specifies the number of pins on an AV/C subunit device. |
| [_AVC_PIN_DESCRIPTOR structure](..\avc\ns-avc-_avc_pin_descriptor.md) | The AVC_PIN_DESCRIPTOR structure describes a pin on an AV/C subunit device. |
| [_AVC_PIN_ID structure](..\avc\ns-avc-_avc_pin_id.md) | The AVC_PIN_ID structure describes a pin on a subunit. |
| [_AVC_PRECONNECT_INFO structure](..\avc\ns-avc-_avc_preconnect_info.md) | The AVC_PRECONNECT_INFO structure specifies the preconnection information for the specified pin ID (zero-based offset) on an AV/C subunit device. |
| [_AVC_SETCONNECT_INFO structure](..\avc\ns-avc-_avc_setconnect_info.md) | The AVC_SETCONNECT_INFO structure is used to initialize a subunit driver and establish pin connections. |
| [_AVC_STREAM_REQUEST_BLOCK structure](..\avcstrm\ns-avcstrm-_avc_stream_request_block.md) | The AVC_STREAM_REQUEST_BLOCK structure describes an AV/C streaming request to be processed by avcstrm.sys. |
| [_AVC_SUBUNIT_ADDR_SPEC structure](..\avc\ns-avc-_avc_subunit_addr_spec.md) | The AVC_SUBUNIT_ADDR_SPEC structure is used with virtual instances of avc.sys to describe virtual subunit addresses. |
| [_AVC_SUBUNIT_INFO_BLOCK structure](..\avc\ns-avc-_avc_subunit_info_block.md) | The AVC_SUBUNIT_INFO_BLOCK structure describes subunit information. |
| [_AVC_UNIQUE_ID structure](..\avc\ns-avc-_avc_unique_id.md) | The AVC_UNIQUE_ID describe the unique ID of the AV/C unit. |
| [_BDA_FILTER_TEMPLATE structure](..\bdasup\ns-bdasup-_bda_filter_template.md) | The BDA_FILTER_TEMPLATE structure describes the template topology for a BDA filter. |
| [_BDA_PIN_PAIRING structure](..\bdasup\ns-bdasup-_bda_pin_pairing.md) | The BDA_PIN_PAIRING structure describes the topology between a pair of input and output pins. |
| [_BUS_INTERFACE_SWENUM structure](..\swenum\ns-swenum-_bus_interface_swenum.md) | The BUS_INTERFACE_SWENUM structure describes the demand-load bus enumerator object's interface. |
| [_CIP_HDR1 structure](..\avcstrm\ns-avcstrm-_cip_hdr1.md) | The CIP_HDR1 structure describes the generic data structure of the two quadlet CIP headers (first quadlet of the pair). |
| [_CIP_HDR2_FDF structure](..\avcstrm\ns-avcstrm-_cip_hdr2_fdf.md) | The CIP_HDR2_FDF structure describes the second quadlet of a CIP header pair. |
| [_CIP_HDR2_MPEGTS structure](..\avcstrm\ns-avcstrm-_cip_hdr2_mpegts.md) | The CIP_HDR2_MPEGTS structure describes the second quadlet of a CIP header pair for an MPEGTS format stream. |
| [_CIP_HDR2_SYT structure](..\avcstrm\ns-avcstrm-_cip_hdr2_syt.md) | The CIP_HDR2_SYT structure describes the second quadlet of a CIP header pair for a DV format stream. |
| [_DVINFO structure](..\avcstrm\ns-avcstrm-_dvinfo.md) | The DVINFO structure describes a DV stream format including its default streaming source information and stream control information. |
| [_HW_CLOCK_OBJECT structure](..\strmini\ns-strmini-_hw_clock_object.md) | The HW_CLOCK_OBJECT structure describes the clock associated with a stream. |
| [_HW_EVENT_DESCRIPTOR structure](..\strmini\ns-strmini-_hw_event_descriptor.md) | When the class driver calls one of the minidriver's StrMiniEvent routines, it passes a pointer to an HW_EVENT_DESCRIPTOR structure to describe the event as enabled or disabled. |
| [_HW_STREAM_DESCRIPTOR structure](..\strmini\ns-strmini-_hw_stream_descriptor.md) | The minidriver uses the HW_STREAM_DESCRIPTOR structure to return stream information to the stream class driver. |
| [_HW_STREAM_HEADER structure](..\strmini\ns-strmini-_hw_stream_header.md) | The HW_STREAM_HEADER structure describes the kernel streaming semantics supported by the minidriver as a whole, as part of a HW_STREAM_DESCRIPTOR structure. |
| [_HW_STREAM_INFORMATION structure](..\strmini\ns-strmini-_hw_stream_information.md) | The HW_STREAM_INFORMATION structure describes the kernel streaming semantics supported by individual streams, as part of an HW_STREAM_DESCRIPTOR structure. |
| [_HW_STREAM_OBJECT structure](..\strmini\ns-strmini-_hw_stream_object.md) | HW_STREAM_OBJECT describes an instance of a minidriver stream. |
| [_HW_STREAM_REQUEST_BLOCK structure](..\strmini\ns-strmini-_hw_stream_request_block.md) | The stream class driver uses the HW_STREAM_REQUEST_BLOCK structure to pass information to and from the minidriver, using minidriver provided callbacks. |
| [_HW_TIME_CONTEXT structure](..\strmini\ns-strmini-_hw_time_context.md) | The class driver passes an HW_TIME_CONTEXT structure as a parameter to be filled in by a stream's StrMiniClock routine, or returns a completed HW_TIME_CONTEXT structure when it responds to a StreamClassQueryMasterClock or StreamClassQueryMasterClockSync request. |
| [_KSM_PIN structure](..\bdasup\ns-bdasup-_ksm_pin.md) | The KSM_PIN structure describes a method request to create or delete a pin factory for a filter. |
| [_KSM_PIN_PAIR structure](..\bdasup\ns-bdasup-_ksm_pin_pair.md) | The KSM_PIN_PAIR structure describes a method request to retrieve the pin pairing structure (BDA_PIN_PAIRING) between a pair of input and output pins. |
| [_STREAM_DATA_INTERSECT_INFO structure](..\strmini\ns-strmini-_stream_data_intersect_info.md) | STREAM_DATA_INTERSECT_INFO describes the parameters of a data intersection operation. |
| [_STREAM_METHOD_DESCRIPTOR structure](..\strmini\ns-strmini-_stream_method_descriptor.md) | . |
| [_STREAM_PROPERTY_DESCRIPTOR structure](..\strmini\ns-strmini-_stream_property_descriptor.md) | STREAM_PROPERTY_DESCRIPTOR specifies the parameters of property get/set requests that the class driver passes to the minidriver. |
| [_STREAM_TIME_REFERENCE structure](..\strmini\ns-strmini-_stream_time_reference.md) | . |
| [_SWENUM_INSTALL_INTERFACE structure](..\swenum\ns-swenum-_swenum_install_interface.md) | The SWENUM_INSTALL_INTERFACE structure describes a specific demand-load bus enumerator object interface to install. |
| [_USBCAMD_DEVICE_DATA structure](..\usbcamdi\ns-usbcamdi-_usbcamd_device_data.md) | This structure is obsolete and is provided to maintain backward compatibility with the original USBCAMD. |
| [_USBCAMD_DEVICE_DATA2 structure](..\usbcamdi\ns-usbcamdi-_usbcamd_device_data2.md) | The USBCAMD_DEVICE_DATA2 structure specifies the entry points for a camera minidriver's functions that USBCAMD calls. |
| [_pipe_config_descriptor structure](..\usbcamdi\ns-usbcamdi-_pipe_config_descriptor.md) | The USBCAMD_Pipe_Config_Descriptor structure describes the association between pipes and streams. |
| [tagKS_DATAFORMAT_DV_AVC structure](..\avcstrm\ns-avcstrm-tagks_dataformat_dv_avc.md) | The KS_DATAFORMAT_DV_AVC structure stores the data format for an AV/C digital video connection. |
| [tagKS_DATAFORMAT_MPEG2TS_AVC structure](..\avcstrm\ns-avcstrm-tagks_dataformat_mpeg2ts_avc.md) | The KS_DATAFORMAT_MPEG2TS_AVC structure stores the data format for an AV/C MPEG2 connection. |
| [tagKS_DATARANGE_DVVIDEO structure](..\avcstrm\ns-avcstrm-tagks_datarange_dvvideo.md) | The KS_DATARANGE_DV_AVC structure stores a range of digital video formats. |
| [tagKS_DATARANGE_DV_AVC structure](..\avcstrm\ns-avcstrm-tagks_datarange_dv_avc.md) | The KS_DATARANGE_DV_AVC structure stores a range of AV/C digital video formats. |
| [tagKS_DATARANGE_MPEG2TS_AVC structure](..\avcstrm\ns-avcstrm-tagks_datarange_mpeg2ts_avc.md) | The KS_DATARANGE_MPEG2TS_AVC structure stores a range of AV/C MPEG2 formats. |
| [tag_video_configure_parms structure](..\msviddrv\ns-msviddrv-tag_video_configure_parms.md) | . |
| [tag_video_geterrortext_parms structure](..\msviddrv\ns-msviddrv-tag_video_geterrortext_parms.md) | . |
| [tag_video_open_parms structure](..\msviddrv\ns-msviddrv-tag_video_open_parms.md) | . |
| [tag_video_stream_init_parms structure](..\msviddrv\ns-msviddrv-tag_video_stream_init_parms.md) | . |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [KSPROPERTY_SERVICE enumeration](..\ksi\ne-ksi-ksproperty_service.md) | . |
| [STREAM_BUFFER_TYPE enumeration](..\strmini\ne-strmini-stream_buffer_type.md) | This enumeration defines the buffer types for StreamClassGetPhysicalAddress. |
| [STREAM_DEBUG_LEVEL enumeration](..\strmini\ne-strmini-stream_debug_level.md) | The STREAM_DEBUG_LEVEL enumeration lists incrementally increasing levels of debugger output. |
| [TIME_FUNCTION enumeration](..\strmini\ne-strmini-time_function.md) | . |
| [_AVCSTRM_FORMAT enumeration](..\avcstrm\ne-avcstrm-_avcstrm_format.md) | The AVCSTRM_FUNCTION enumeration defines the AV/C subunit stream formats supported by avcstrm.sys. |
| [_AVCSTRM_FUNCTION enumeration](..\avcstrm\ne-avcstrm-_avcstrm_function.md) | The AVCSTRM_FUNCTION enumeration defines the functionality exposed by the avcstrm.sys driver. |
| [_KSPIN_FLAG_AVC enumeration](..\avc\ne-avc-_kspin_flag_avc.md) | The KSPIN_FLAG_AVC enumeration type is used for connection management and in the AVC_FUNCTION_GET_CONNECTINFO function code. |
| [_SRB_COMMAND enumeration](..\strmini\ne-strmini-_srb_command.md) | . |
| [_STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE enumeration](..\strmini\ne-strmini-_stream_minidriver_device_notification_type.md) | . |
| [_STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE enumeration](..\strmini\ne-strmini-_stream_minidriver_stream_notification_type.md) | . |
| [_STREAM_PRIORITY enumeration](..\strmini\ne-strmini-_stream_priority.md) | TD. |
| [_tagAVC_FUNCTION enumeration](..\avc\ne-avc-_tagavc_function.md) | The AVC_FUNCTION enumeration type is used to specify AV/C subunit functions. |
| [_tagAvcCommandType enumeration](..\avc\ne-avc-_tagavccommandtype.md) | The AvcCommandType enumeration type is used to indicate the type of command issued by a subunit driver to its AV/C subunit through AVC_FUNCTION_COMMAND or AVC_FUNCTION_GET_REQUEST function codes. |
| [_tagAvcResponseCode enumeration](..\avc\ne-avc-_tagavcresponsecode.md) | The AvcResponseCode enumeration type is used to indicate the type of response received by a subunit driver from its AV/C subunit through AVC_FUNCTION_COMMAND or AVC_FUNCTION_SEND_RESPONSE function codes. |
| [_tagAvcSubunitType enumeration](..\avc\ne-avc-_tagavcsubunittype.md) | The AvcSubunitType enumeration type is used to indicate the type of AV/C subunit. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_AVCSTRM_CLASS IOCTL](..\avcstrm\ni-avcstrm-ioctl_avcstrm_class.md) | An AV/C subunit driver uses the IRP_MJ_INTERNAL_DEVICE_CONTROL IRP, with the IoControlCode member set to IOCTL_AVCSTRM_CLASS, to communicate with avcstrm.sys. |
| [IOCTL_AVC_BUS_RESET IOCTL](..\avc\ni-avc-ioctl_avc_bus_reset.md) | The IOCTL_AVC_BUS_RESET I/O control code allows the caller to complete any previous IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO and IOCTL_AVC_REMOVE_VIRTUAL_SUBUNIT_INFO control requests that did not use the AVC_SUBUNIT_ADDR_TRIGGERBUSRESET flag. |
| [IOCTL_AVC_CLASS IOCTL](..\avc\ni-avc-ioctl_avc_class.md) | The IOCTL_AVC_CLASS I/O control code is supported only from kernel mode, using the IRP_MJ_INTERNAL_DEVICE_CONTROL dispatch.Avc.sys supports two device interfaces, depending upon the type of instance (peer or virtual). |
| [IOCTL_AVC_REMOVE_VIRTUAL_SUBUNIT_INFO IOCTL](..\avc\ni-avc-ioctl_avc_remove_virtual_subunit_info.md) | The IOCTL_AVC_REMOVE_VIRTUAL_SUBUNIT_INFO I/O control code controls the enumeration of virtual subunits. |
| [IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO IOCTL](..\avc\ni-avc-ioctl_avc_update_virtual_subunit_info.md) | The IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO I/O control code controls the enumeration of virtual subunits. |
| [IOCTL_SWENUM_GET_BUS_ID IOCTL](..\swenum\ni-swenum-ioctl_swenum_get_bus_id.md) | TBD |
| [IOCTL_SWENUM_INSTALL_INTERFACE IOCTL](..\swenum\ni-swenum-ioctl_swenum_install_interface.md) | TBD |
| [IOCTL_SWENUM_REMOVE_INTERFACE IOCTL](..\swenum\ni-swenum-ioctl_swenum_remove_interface.md) | TBD |

## Macros

| Title   | Description   |
| ---- |:---- |
| [INIT_AVCSTRM_HEADER macro](..\avcstrm\nf-avcstrm-init_avcstrm_header.md) | The INIT_AVCSTRM_HEADER macro initializes the SizeOfThisBlock, Version and Function members of the AVC_STREAM_REQUEST_BLOCK structure. |
