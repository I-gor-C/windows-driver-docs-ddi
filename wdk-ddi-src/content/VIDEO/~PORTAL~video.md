# Declarations in the video header
This header Video contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE structure](ns-video--video-port-wcmemoryprotection-interface.md) | The VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE structure describes the Write Combined video memory protection service routines implemented by the video port driver. The protected video memory cannot be accessed by the CPU. |
| [VIDEO_HW_INITIALIZATION_DATA structure](ns-video--video-hw-initialization-data.md) | The VIDEO_HW_INITIALIZATION_DATA structure specifies the entry points and storage requirements for the miniport driver. This structure is created on the stack and initialized by the miniport driver's DriverEntry function. |
| [VIDEO_CHILD_ENUM_INFO structure](ns-video--video-child-enum-info.md) | Describes the child device to be enumerated by the miniport driver. All members are set by the video port driver. |
| [VIDEO_I2C_CONTROL structure](ns-video--video-i2c-control.md) | TBD |
| [VRB_SG structure](ns-video---vrb-sg.md) | TBD |
| [I2C_FNC_TABLE structure](ns-video--i2c-fnc-table.md) | TBD |
| [VIDEO_DEBUG_REPORT structure](ns-video--video-debug-report.md) | TBD |
| [VIDEO_PORT_AGP_INTERFACE structure](ns-video--video-port-agp-interface.md) | The VIDEO_PORT_AGP_INTERFACE structure describes the AGP service routines provided by the video port driver. |
| [VP_DMA_ADAPTER structure](ns-video---vp-dma-adapter.md) | TBD |
| [VP_DEVICE_DESCRIPTION structure](ns-video--vp-device-description.md) | The VP_DEVICE_DESCRIPTION structure describes the attributes of the physical device for which a driver is requesting a DMA object. |
| [VIDEO_CHILD_STATE structure](ns-video--video-child-state.md) | The VIDEO_CHILD_STATE structure contains information about a child device and the state into which it should be placed. |
| [VIDEO_REQUEST_PACKET structure](ns-video--video-request-packet.md) | A pointer to a VIDEO_REQUEST_PACKET structure is passed to the miniport driver's HwVidStartIO function by the video port driver. |
| [VIDEO_PORT_I2C_INTERFACE_2 structure](ns-video--video-port-i2c-interface-2.md) | TBD |
| [VIDEO_PORT_CONFIG_INFO structure](ns-video--video-port-config-info.md) | The VIDEO_PORT_CONFIG_INFO structure contains bus-specific adapter configuration information. |
| [VIDEO_PORT_SPIN_LOCK structure](ns-video--video-port-spin-lock.md) | TBD |
| [VIDEO_PORT_AGP_INTERFACE_2 structure](ns-video--video-port-agp-interface-2.md) | The VIDEO_PORT_AGP_INTERFACE_2 structure describes the AGP service routines provided by the video port driver. |
| [VIDEO_CHILD_STATE_CONFIGURATION structure](ns-video--video-child-state-configuration.md) | The VIDEO_CHILD_STATE_CONFIGURATION structure contains an array of VIDEO_CHILD_STATE structures, each holding the state of a particular child device. |
| [I2C_CALLBACKS structure](ns-video--i2c-callbacks.md) | The I2C_CALLBACKS structure contains pointers to functions, implemented by the video miniport driver, that read from and write to the serial data and serial clock lines of the I2C bus. |
| [VP_SCATTER_GATHER_LIST structure](ns-video--vp-scatter-gather-list.md) | The VP_SCATTER_GATHER_LIST structure is a collection of one or more scatter/gather elements. |
| [DDC_CONTROL structure](ns-video--ddc-control.md) | The DDC_CONTROL structure holds function pointers and EDID segment information needed by the VideoPortDDCMonitorHelper function, which is exported by the video port driver. |
| [VIDEO_X86_BIOS_ARGUMENTS structure](ns-video--video-x86-bios-arguments.md) | The VIDEO_x86_BIOS_ARGUMENTS structure is used to support full-screen MS-DOS application INT10 calls. It contains seven of the high-end x86 microprocessor registers. |
| [VIDEO_HARDWARE_CONFIGURATION_DATA structure](ns-video--video-hardware-configuration-data.md) | TBD |
| [VIDEO_PORT_DEBUG_REPORT_INTERFACE structure](ns-video--video-port-debug-report-interface.md) | The VIDEO_PORT_DEBUG_REPORT_INTERFACE structure holds pointers to the Debug Report functions, which are implemented by the video port driver. |
| [QUERY_INTERFACE structure](ns-video--query-interface.md) | The QUERY_INTERFACE structure describes the interface being requested. |
| [INT10_BIOS_ARGUMENTS structure](ns-video--int10-bios-arguments.md) | The INT10_BIOS_ARGUMENTS structure is used to support full-screen MS-DOS application INT10 calls. It contains nine of the high-end x86 microprocessor registers. |
| [STATUS_BLOCK structure](ns-video--status-block.md) | The STATUS_BLOCK structure is a substructure within the VIDEO_REQUEST_PACKET structure. A miniport driver's HwVidStartIO function must set the status block of each VRP that it gets. |
| [VIDEO_ACCESS_RANGE structure](ns-video--video-access-range.md) | The VIDEO_ACCESS_RANGE structure defines a device I/O port or memory range for the video adapter. |
| [VP_SCATTER_GATHER_ELEMENT structure](ns-video--vp-scatter-gather-element.md) | The VP_SCATTER_GATHER_ELEMENT structure is used to store information about a single scatter/gather element. |
| [VIDEO_PORT_INT10_INTERFACE structure](ns-video--video-port-int10-interface.md) | The VIDEO_PORT_INT10_INTERFACE structure provides a way to allocate and deallocate memory in another thread's context, read from and write to that memory, and make INT10 BIOS calls. |
| [DMA_PARAMETERS structure](ns-video---dma-parameters.md) | TBD |
| [VPOSVERSIONINFO structure](ns-video--vposversioninfo.md) | The VPOSVERSIONINFO structure contains version information about the currently running operating system. |
| [VIDEO_PORT_I2C_INTERFACE structure](ns-video--video-port-i2c-interface.md) | The VIDEO_PORT_I2C_INTERFACE structure describes the I2C service routines provided by the video port driver. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [VideoPortMoveMemory function](nf-video-videoportmovememory.md) | The VideoPortMoveMemory function copies data from the source location to the destination location in system memory. |
| [VideoPortCreateSpinLock function](nf-video-videoportcreatespinlock.md) | The VideoPortCreateSpinLock function creates a spin lock. |
| [VideoPortReadRegisterBufferUshort function](nf-video-videoportreadregisterbufferushort.md) | The VideoPortReadRegisterBufferUshort function reads a number of USHORT values from a mapped device memory range and writes them into a buffer. |
| [VideoPortWriteRegisterUchar function](nf-video-videoportwriteregisteruchar.md) | The VideoPortWriteRegisterUchar function writes a byte to a mapped register. |
| [VideoPortDDCMonitorHelper function](nf-video-videoportddcmonitorhelper.md) | Queries a monitor for EDID information using the DDC protocol. |
| [VideoPortScanRom function](nf-video-videoportscanrom.md) | The VideoPortScanRom function is obsolete in Windows XP and later versions. It is supported only for backward compatibility. VideoPortScanRom performs a case-sensitive search for a specified string in ROM. |
| [VideoPortCreateEvent function](nf-video-videoportcreateevent.md) | The VideoPortCreateEvent function creates an event object. |
| [VideoPortGetMdl function](nf-video-videoportgetmdl.md) | The VideoPortGetMdl function is obsolete in Windows 2000 and later.VideoPortGetMdl retrieves the memory descriptor list (MDL) that represents the page table of the locked buffer. |
| [VideoPortMapDmaMemory function](nf-video-videoportmapdmamemory.md) | The VideoPortMapDmaMemory function is obsolete in Windows 2000 and later.VideoPortMapDmaMemory maps a range of memory for use in DMA transfers. |
| [VideoPortSetBusData function](nf-video-videoportsetbusdata.md) | The VideoPortSetBusData function sets bus-configuration data for an adapter on a dynamically configurable I/O bus with a published, standard interface. |
| [VideoPortReadRegisterBufferUchar function](nf-video-videoportreadregisterbufferuchar.md) | The VideoPortReadRegisterBufferUchar function reads a number of bytes from a mapped device memory range and writes them into a buffer. |
| [VideoPortAssociateEventsWithDmaHandle function](nf-video-videoportassociateeventswithdmahandle.md) | The VideoPortAssociateEventsWithDmaHandle function is obsolete in Windows 2000 and later.VideoPortAssociateEventsWithDmaHandle associates an event, which is shared by the video display driver and the video miniport driver, with a DMA handle. |
| [VideoPortZeroMemory function](nf-video-videoportzeromemory.md) | The VideoPortZeroMemory function fills a block of system memory with zeros. |
| [VideoPortReleaseSpinLock function](nf-video-videoportreleasespinlock.md) | The VideoPortReleaseSpinLock function releases ownership of a given spin lock and restores the original IRQL at which the caller was running. |
| [VideoPortGetCommonBuffer function](nf-video-videoportgetcommonbuffer.md) | The VideoPortGetCommonBuffer function is obsolete in Windows XP and later, and is supported only for backward compatibility with existing drivers. |
| [VideoPortGetVgaStatus function](nf-video-videoportgetvgastatus.md) | The VideoPortGetVgaStatus function detects whether the calling device is decoding a VGA I/O address. |
| [VideoPortWriteRegisterBufferUlong function](nf-video-videoportwriteregisterbufferulong.md) | The VideoPortWriteRegisterBufferUlong function writes a number of ULONG values to a mapped register. |
| [VideoPortWritePortUshort function](nf-video-videoportwriteportushort.md) | The VideoPortWritePortUshort function writes a USHORT value to a mapped I/O port. |
| [VideoPortWriteRegisterUshort function](nf-video-videoportwriteregisterushort.md) | The VideoPortWriteRegisterUshort function writes a USHORT value to a mapped register. |
| [VideoPortReadPortBufferUshort function](nf-video-videoportreadportbufferushort.md) | The VideoPortReadPortBufferUshort function reads a number of USHORT values from a mapped I/O port and writes them into a buffer. |
| [VideoPortAcquireSpinLock function](nf-video-videoportacquirespinlock.md) | The VideoPortAcquireSpinLock function obtains the specified spin lock. |
| [VideoPortReadStateEvent function](nf-video-videoportreadstateevent.md) | The VideoPortReadStateEvent function returns the current state of a given event object |
| [GET_VIDEO_PHYSICAL_ADDRESS function](nf-video-get-video-physical-address.md) | TBD |
| [VideoPortDbgReportSecondaryData function](nf-video-videoportdbgreportsecondarydata.md) | TBD |
| [VideoDebugPrint function](nf-video-videodebugprint.md) | TBD |
| [VideoPortInitialize function](nf-video-videoportinitialize.md) | The VideoPortInitialize function performs part of the miniport driver initialization, allocating system resources for the miniport driver. |
| [VideoPortInterlockedIncrement function](nf-video-videoportinterlockedincrement.md) | The VideoPortInterlockedIncrement function increments a caller-supplied variable as an atomic operation. |
| [VideoPortAcquireDeviceLock function](nf-video-videoportacquiredevicelock.md) | The VideoPortAcquireDeviceLock function acquires the device lock maintained by the video port driver. |
| [VideoPortInterlockedDecrement function](nf-video-videoportinterlockeddecrement.md) | The VideoPortInterlockedDecrement function decrements a caller-supplied variable as an atomic operation. |
| [VideoPortAllocatePool function](nf-video-videoportallocatepool.md) | The VideoPortAllocatePool function allocates a block of pool memory, inserting a caller-supplied tag at the beginning of the memory. |
| [VideoPortCheckForDeviceExistence function](nf-video-videoportcheckfordeviceexistence.md) | The VideoPortCheckForDeviceExistence function determines whether the specified PCI device exists in the system. |
| [VideoPortCreateSecondaryDisplay function](nf-video-videoportcreatesecondarydisplay.md) | The VideoPortCreateSecondaryDisplay function enables dual-view support by creating a secondary device object for the given device. |
| [VideoPortAllocateCommonBuffer function](nf-video-videoportallocatecommonbuffer.md) | The VideoPortAllocateCommonBuffer function allocates and maps system memory so that it is simultaneously accessible from both the processor and a device for common-buffer DMA operations. |
| [VideoPortWritePortBufferUchar function](nf-video-videoportwriteportbufferuchar.md) | The VideoPortWritePortBufferUchar function writes a number of bytes to a mapped I/O port. |
| [VideoPortReleaseDeviceLock function](nf-video-videoportreleasedevicelock.md) | The VideoPortReleaseDeviceLock function releases the device lock acquired in a prior call to VideoPortAcquireDeviceLock. |
| [VideoPortGetDeviceData function](nf-video-videoportgetdevicedata.md) | The VideoPortGetDeviceData function retrieves system-detected configuration information from the ..\Machine\Hardware\Description tree in the registry. |
| [DriverEntry function](nf-video-driverentry.md) | TBD |
| [VideoPortGetRomImage function](nf-video-videoportgetromimage.md) | Reads the device's read-only memory (ROM). |
| [VideoPortSetEvent function](nf-video-videoportsetevent.md) | The VideoPortSetEvent function sets an event object to the signaled state if it was not already in that state, and returns the event object's previous state. |
| [VideoPortLockBuffer function](nf-video-videoportlockbuffer.md) | The VideoPortLockBuffer function probes the specified buffer, makes the buffer's memory pages resident in memory, and locks the physical pages mapped by the virtual address range. |
| [VideoPortWritePortBufferUshort function](nf-video-videoportwriteportbufferushort.md) | The VideoPortWritePortBufferUshort function writes a number of USHORT values to a mapped I/O port. |
| [VideoPortGetDmaAdapter function](nf-video-videoportgetdmaadapter.md) | The VideoPortGetDmaAdapter function returns a pointer to a VP_DMA_ADAPTER structure, which is used in subsequent calls to other DMA-related functions. |
| [VideoPortWriteRegisterBufferUshort function](nf-video-videoportwriteregisterbufferushort.md) | The VideoPortWriteRegisterBufferUshort function writes a number of USHORT values to a mapped register. |
| [VideoPortGetAccessRanges function](nf-video-videoportgetaccessranges.md) | The VideoPortGetAccessRanges function retrieves bus-relative configuration information and, if possible, claims these hardware resources in the registry for the caller. |
| [VideoPortReadPortBufferUlong function](nf-video-videoportreadportbufferulong.md) | The VideoPortReadPortBufferUlong function reads a number of ULONG values from a mapped I/O port and writes them into a buffer. |
| [VideoPortDeleteEvent function](nf-video-videoportdeleteevent.md) | The VideoPortDeleteEvent function deletes the specified event object. |
| [VideoPortStartDma function](nf-video-videoportstartdma.md) | The VideoPortStartDma function prepares the system for a DMA operation. |
| [VideoPortUnlockBuffer function](nf-video-videoportunlockbuffer.md) | The VideoPortUnLockBuffer function unlocks physical pages described by the specified memory descriptor list (MDL). |
| [VideoPortAcquireSpinLockAtDpcLevel function](nf-video-videoportacquirespinlockatdpclevel.md) | The VideoPortAcquireSpinLockAtDpcLevel function acquires a spin lock when the caller is already running at IRQL = DISPATCH_LEVEL. |
| [VideoPortFreePool function](nf-video-videoportfreepool.md) | The VideoPortFreePool function deallocates a block of pool memory previously allocated by VideoPortAllocatePool. |
| [VideoPortVerifyAccessRanges function](nf-video-videoportverifyaccessranges.md) | The VideoPortVerifyAccessRanges function checks the registry for whether another driver has already claimed ownership of the specified bus-relative access ranges and any other hardware resources specified in the VIDEO_PORT_CONFIG_INFO structure. |
| [VideoPortDisableInterrupt function](nf-video-videoportdisableinterrupt.md) | The VideoPortDisableInterrupt function is obsolete and should not be called.The VideoPortDisableInterrupt function disables interrupts from a video adapter. |
| [VideoPortGetDeviceBase function](nf-video-videoportgetdevicebase.md) | The VideoPortGetDeviceBase function maps a range of bus-relative device memory or I/O addresses into system space. |
| [VideoPortDbgReportComplete function](nf-video-videoportdbgreportcomplete.md) | TBD |
| [VideoPortReleaseCommonBuffer function](nf-video-videoportreleasecommonbuffer.md) | The VideoPortReleaseCommonBuffer function frees a common buffer that was previously allocated by VideoPortAllocateCommonBuffer. |
| [VideoPortSetTrappedEmulatorPorts function](nf-video-videoportsettrappedemulatorports.md) | VGA-compatible (SVGA) miniport drivers call the VideoPortSetTrappedEmulatorPorts function to dynamically change the list of I/O ports that are trapped when a VDM runs in full-screen mode on an x86-based machine. |
| [VideoPortSetRegistryParameters function](nf-video-videoportsetregistryparameters.md) | The VideoPortSetRegistryParameters function writes information under the adapter key in the registry. |
| [VideoPortReadRegisterUshort function](nf-video-videoportreadregisterushort.md) | The VideoPortReadRegisterUshort function reads a USHORT value from a mapped register range. |
| [VideoPortReleaseBuffer function](nf-video-videoportreleasebuffer.md) | The VideoPortReleaseBuffer function is obsolete in Windows 2000 and later. In its place, video miniport drivers should instead use VideoPortFreePool. VideoPortReleaseBuffer deallocates a block of paged pool memory. |
| [VideoPortStartTimer function](nf-video-videoportstarttimer.md) | The VideoPortStartTimer function enables calls to a miniport driver's HwVidTimer function. |
| [VideoPortGetAssociatedDeviceExtension function](nf-video-videoportgetassociateddeviceextension.md) | The VideoPortGetAssociatedDeviceExtension function returns the device extension for the parent of the specified device object. |
| [VideoPortDbgReportCreate function](nf-video-videoportdbgreportcreate.md) | TBD |
| [VideoPortUnlockPages function](nf-video-videoportunlockpages.md) | The VideoPortUnlockPages function is obsolete in Windows 2000 and later. Use VideoPortUnlockBuffer in place of this function.VideoPortUnlockPages releases memory used for packet-based DMA. |
| [VideoPortLockPages function](nf-video-videoportlockpages.md) | The VideoPortLockPages function is obsolete in Windows 2000 and later. Use VideoPortLockBuffer in place of this function.VideoPortLockPages locks the specified virtual memory and possibly performs part or all of a DMA transfer. |
| [VideoPortQueryServices function](nf-video-videoportqueryservices.md) | The VideoPortQueryServices function exposes a specified interface that is implemented by the video port driver. |
| [VideoPortReleaseSpinLockFromDpcLevel function](nf-video-videoportreleasespinlockfromdpclevel.md) | The VideoPortReleaseSpinLockFromDpcLevel function releases the spin lock obtained by a previous call to VideoPortAcquireSpinLockAtDpcLevel. |
| [VideoPortPutDmaAdapter function](nf-video-videoportputdmaadapter.md) | The VideoPortPutDmaAdapter function frees a VP_DMA_ADAPTER structure that was previously allocated by a call to VideoPortGetDmaAdapter. |
| [VideoPortGetRegistryParameters function](nf-video-videoportgetregistryparameters.md) | The VideoPortGetRegistryParameters function retrieves device-specific configuration information under the adapter key in the registry at startup. |
| [VideoPortEnableInterrupt function](nf-video-videoportenableinterrupt.md) | The VideoPortEnableInterrupt function is obsolete and should not be called.The VideoPortEnableInterrupt function reenables interrupts from a video adapter after a call to VideoPortDisableInterrupt. |
| [VideoPortReadRegisterBufferUlong function](nf-video-videoportreadregisterbufferulong.md) | The VideoPortReadRegisterBufferUlong function reads a number of ULONG values from a mapped device memory range and writes them into a buffer. |
| [VideoPortSetBytesUsed function](nf-video-videoportsetbytesused.md) | The VideoPortSetBytesUsed function is obsolete in Windows 2000 and later. |
| [VideoPortFreeDeviceBase function](nf-video-videoportfreedevicebase.md) | The VideoPortFreeDeviceBase function frees a range of bus-relative device I/O ports or memory addresses previously mapped into the system address space. It does this by calling VideoPortGetDeviceBase. |
| [VideoPortReadRegisterUlong function](nf-video-videoportreadregisterulong.md) | The VideoPortReadRegisterUlong function reads a ULONG value from a mapped register range. |
| [VideoPortInt10 function](nf-video-videoportint10.md) | The VideoPortInt10 function performs the equivalent of an MS-DOS INT10 operation, such as setting the video mode. VideoPortInt10 runs the BIOS ROM code on the device. |
| [VideoPortEnumerateChildren function](nf-video-videoportenumeratechildren.md) | The VideoPortEnumerateChildren function allows a video miniport driver to force a reenumeration of its child devices. |
| [VideoPortGetBytesUsed function](nf-video-videoportgetbytesused.md) | The VideoPortGetBytesUsed function is obsolete in Windows 2000 and later.VideoPortGetBytesUsed determines the size, in bytes, of the buffer associated with a DMA handle. |
| [VideoPortStopTimer function](nf-video-videoportstoptimer.md) | The VideoPortStopTimer function disables calls to a miniport driver's HwVidTimer function. |
| [VideoPortUnmapMemory function](nf-video-videoportunmapmemory.md) | The VideoPortUnmapMemory function releases a mapping between a logical address range for the adapter and a virtual address range in the user-mode address space of a particular thread. This function is the complement of VideoPortMapMemory. |
| [VideoPortQuerySystemTime function](nf-video-videoportquerysystemtime.md) | The VideoPortQuerySystemTime function obtains the current system time. |
| [VideoPortFreeCommonBuffer function](nf-video-videoportfreecommonbuffer.md) | The VideoPortFreeCommonBuffer function is obsolete and is supported only for backward compatibility with existing drivers. |
| [VideoPortFlushRegistry function](nf-video-videoportflushregistry.md) | The VideoPortFlushRegistry function flushes registry keys and values associated with the video miniport driver. |
| [VideoPortClearEvent function](nf-video-videoportclearevent.md) | The VideoPortClearEvent function sets a given event object to the nonsignaled state. |
| [VideoPortRegisterBugcheckCallback function](nf-video-videoportregisterbugcheckcallback.md) | The VideoPortRegisterBugcheckCallback function allows a video miniport driver to register for, or hook, a callback that is invoked when a specified bug check occurs. |
| [VideoPortSynchronizeExecution function](nf-video-videoportsynchronizeexecution.md) | The VideoPortSynchronizeExecution function synchronizes the execution of a miniport driver-supplied HwVidSynchronizeExecutionCallback function with the miniport driver's HwVidInterrupt function, if any. |
| [VideoPortLogError function](nf-video-videoportlogerror.md) | The VideoPortLogError function logs errors to the system event log when a miniport driver detects a hardware error condition during I/O operations. |
| [VideoPortWriteRegisterBufferUchar function](nf-video-videoportwriteregisterbufferuchar.md) | The VideoPortWriteRegisterBufferUchar function writes a number of unsigned bytes to a mapped register. |
| [VideoPortGetAssociatedDeviceID function](nf-video-videoportgetassociateddeviceid.md) | The VideoPortGetAssociatedDeviceID function obtains the child ID for a specified device object. |
| [VideoPortUnmapDmaMemory function](nf-video-videoportunmapdmamemory.md) | The VideoPortUnmapDmaMemory function is obsolete in Windows 2000 and later.VideoPortUnmapDmaMemory unmaps a range of memory previously mapped by VideoPortMapDmaMemory. |
| [VideoPortDoDma function](nf-video-videoportdodma.md) | The VideoPortDoDma function is obsolete in Windows 2000 and later. VideoPortDoDma causes the miniport driver's HwVidStartDma function to be called. |
| [GET_VIDEO_SCATTERGATHER function](nf-video-get-video-scattergather.md) | TBD |
| [VideoPortMapMemory function](nf-video-videoportmapmemory.md) | The VideoPortMapMemory function maps a range of bus-relative physical addresses of video memory into system space or into the virtual address space of a user-mode process. |
| [VideoPortSignalDmaComplete function](nf-video-videoportsignaldmacomplete.md) | The VideoPortSignalDmaComplete function is obsolete in Windows 2000 and later.VideoPortSignalDmaComplete indicates to the video miniport driver whether the current DMA transfer is complete. |
| [VideoPortAllocateContiguousMemory function](nf-video-videoportallocatecontiguousmemory.md) | The VideoPortAllocateContiguousMemory function is obsolete in Windows 2000 and later. |
| [VideoPortWriteRegisterUlong function](nf-video-videoportwriteregisterulong.md) | The VideoPortWriteRegisterUlong function writes a ULONG value to a mapped register. |
| [VideoPortIsNoVesa function](nf-video-videoportisnovesa.md) | The VideoPortIsNoVesa function determines whether a video miniport driver that does not support Plug and Play (PnP) is restricted to legacy VGA resources. |
| [VideoPortCompareMemory function](nf-video-videoportcomparememory.md) | The VideoPortCompareMemory function compares two blocks of system memory, byte-by-byte, and returns the number of compared bytes that are equivalent. |
| [VideoPortZeroDeviceMemory function](nf-video-videoportzerodevicememory.md) | The VideoPortZeroDeviceMemory function fills an adapter frame buffer or other device memory with zeros. |
| [VideoPortWritePortBufferUlong function](nf-video-videoportwriteportbufferulong.md) | The VideoPortWritePortBufferUlong function writes a number of ULONG values to a mapped I/O port. |
| [VideoPortWritePortUchar function](nf-video-videoportwriteportuchar.md) | The VideoPortWritePortUchar function writes a byte to a mapped I/O port. |
| [VideoPortDebugPrint function](nf-video-videoportdebugprint.md) | TBD |
| [VideoPortReadPortUshort function](nf-video-videoportreadportushort.md) | The VideoPortReadPortUshort function reads a USHORT value from a mapped I/O port. |
| [VideoPortSetDmaContext function](nf-video-videoportsetdmacontext.md) | The VideoPortSetDmaContext function is obsolete in Windows 2000 and later. |
| [VideoPortReadPortBufferUchar function](nf-video-videoportreadportbufferuchar.md) | The VideoPortReadPortBufferUchar function reads a number of bytes from a mapped I/O port and writes them into a buffer. |
| [VideoPortAllocateBuffer function](nf-video-videoportallocatebuffer.md) | The VideoPortAllocateBuffer function is obsolete in Windows 2000 and later. In its place, video miniport drivers should instead use VideoPortAllocatePool. VideoPortAllocateBuffer allocates a buffer of paged pool memory. |
| [VideoPortGetDmaContext function](nf-video-videoportgetdmacontext.md) | The VideoPortGetDmaContext function is obsolete in Windows 2000 and later.VideoPortGetDmaContext gets the context previously associated with the specified DMA handle. |
| [VideoPortWritePortUlong function](nf-video-videoportwriteportulong.md) | The VideoPortWritePortUlong function writes a ULONG value to a mapped I/O port. |
| [VideoPortWaitForSingleObject function](nf-video-videoportwaitforsingleobject.md) | The VideoPortWaitForSingleObject function puts the current thread into a wait state until the given dispatch object is set to the signaled state, or (optionally) until the wait times out. |
| [VideoPortQueryPerformanceCounter function](nf-video-videoportqueryperformancecounter.md) | The VideoPortQueryPerformanceCounter function provides the finest-grained running count available in the system. |
| [VideoPortMapBankedMemory function](nf-video-videoportmapbankedmemory.md) | The VideoPortMapBankedMemory function is obsolete, and is supported only for Windows NT 4.0 and previous drivers. |
| [VideoPortReadPortUchar function](nf-video-videoportreadportuchar.md) | The VideoPortReadPortUchar function reads a byte from a mapped I/O port. |
| [VideoPortQueueDpc function](nf-video-videoportqueuedpc.md) | The VideoPortQueueDpc function allows a miniport driver to queue a DPC. |
| [VideoPortCompleteDma function](nf-video-videoportcompletedma.md) | The VideoPortCompleteDma function flushes any data remaining in a bus-master adapter's internal cache at the end of a DMA transfer operation, and then frees the previously allocated map registers and scatter/gather list used in scatter/gather DMA operations. |
| [VideoPortStallExecution function](nf-video-videoportstallexecution.md) | The VideoPortStallExecution function retains control of the processor for the specified number of microseconds and returns to the caller. |
| [VideoPortInterlockedExchange function](nf-video-videoportinterlockedexchange.md) | The VideoPortInterlockedExchange function locks or unlocks a block of memory by setting a user-defined lock variable to TRUE or FALSE, respectively. It returns the previously-held value of the lock variable. |
| [VideoPortGetBusData function](nf-video-videoportgetbusdata.md) | The VideoPortGetBusData function returns bus-type-specific configuration information. |
| [VideoPortReadRegisterUchar function](nf-video-videoportreadregisteruchar.md) | The VideoPortReadRegisterUchar function reads a byte from a mapped register. |
| [VideoPortDeleteSpinLock function](nf-video-videoportdeletespinlock.md) | The VideoPortDeleteSpinLock function deletes a given spin lock. |
| [VideoPortReadPortUlong function](nf-video-videoportreadportulong.md) | The VideoPortReadPortUlong function reads a ULONG value from a mapped I/O port. |
| [VideoPortGetVersion function](nf-video-videoportgetversion.md) | The VideoPortGetVersion function gets version information about the currently running operating system. |
| [VideoPortGetCurrentIrql function](nf-video-videoportgetcurrentirql.md) | The VideoPortGetCurrentIrql function gets the current IRQL. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PVIDEO_READ_CLOCK_LINE callback](nc-video-pvideo-read-clock-line.md) | ReadClockLine reads a single data bit from the I2C serial clock line. |
| [PVIDEO_PORT_GET_PROC_ADDRESS callback](nc-video-pvideo-port-get-proc-address.md) | The VideoPortGetProcAddress callback routine retrieves the address of a Windows 2000 or later video port driver function. |
| [PVIDEO_HW_RESET_HW callback](nc-video-pvideo-hw-reset-hw.md) | HwVidResetHw resets the adapter to character mode. |
| [PI2C_WRITE_2 callback function](nc-video-pi2c-write-2.md) | TBD |
| [PDRIVER_IO_PORT_ULONG callback](nc-video-pdriver-io-port-ulong.md) | SvgaHwIoPortUlong traps an I/O port range to which a full-screen MS-DOS application in an x86-based machine is sending a sequence of ULONG-sized data. |
| [PINT10_CALL_BIOS callback](nc-video-pint10-call-bios.md) | The Int10CallBios function allows a miniport driver to call the kernel to perform an INT 10h operation, causing the BIOS ROM code on the device to execute natively. |
| [PINT10_FREE_BUFFER callback](nc-video-pint10-free-buffer.md) | The Int10FreeBuffer function frees a buffer previously allocated by Int10AllocateBuffer. |
| [PVIDEO_HW_GET_CHILD_DESCRIPTOR callback](nc-video-pvideo-hw-get-child-descriptor.md) | HwVidGetVideoChildDescriptor returns a descriptor, a type, and an identification number for a particular child device of the display adapter. |
| [RESTORE_WC_MEMORY callback](nc-video-restore-wc-memory.md) | The VideoPortRestoreWCMemory callback routine restores Write Combined video memory from a protected state after the VideoPortProtectWCMemory callback routine was called. |
| [PDRIVER_IO_PORT_USHORT callback](nc-video-pdriver-io-port-ushort.md) | SvgaHwIoPortUshort traps an I/O port range to which a full-screen MS-DOS application in an x86-based machine is sending a sequence of USHORT-sized data. |
| [PEXECUTE_DMA callback](nc-video-pexecute-dma.md) | HwVidExecuteDma is a miniport driver-implemented callback routine that is responsible for retrieving physical address/length pairs from a scatter/gather list, and for programming the hardware to start the actual DMA transfer. |
| [PDRIVER_IO_PORT_UCHAR callback](nc-video-pdriver-io-port-uchar.md) | SvgaHwIoPortUchar traps an I/O port to which a full-screen MS-DOS application in an x86-based machine is sending UCHAR-sized data. |
| [PMINIPORT_QUERY_DEVICE_ROUTINE callback](nc-video-pminiport-query-device-routine.md) | HwVidQueryDeviceCallback uses the specified configuration data to configure its adapter, and, possibly, to fill in missing configuration information in the VIDEO_PORT_CONFIG_INFO structure. |
| [PVIDEO_WRITE_DATA_LINE callback](nc-video-pvideo-write-data-line.md) | WriteDataLine sets the I2C serial data line to high or low. |
| [PINT10_ALLOCATE_BUFFER callback](nc-video-pint10-allocate-buffer.md) | The Int10AllocateBuffer function can be used to allocate a single 4 KB block of memory in the context of another thread. After the block of memory has been allocated, it must be freed before another block of memory can be allocated. |
| [PVIDEO_HW_START_IO callback](nc-video-pvideo-hw-start-io.md) | HwVidStartIO processes the specified VRP. |
| [PVIDEO_HW_QUERY_INTERFACE callback](nc-video-pvideo-hw-query-interface.md) | HwVidQueryInterface returns a miniport driver-implemented functional interface that a child device can call. |
| [PI2C_START_2 callback function](nc-video-pi2c-start-2.md) | TBD |
| [PVIDEO_HW_INTERRUPT callback](nc-video-pvideo-hw-interrupt.md) | HwVidInterrupt detects and dismisses interrupts generated by the associated video adapter. |
| [PVIDEO_HW_POWER_GET callback](nc-video-pvideo-hw-power-get.md) | HwVidGetPowerState queries whether the device can support the requested power state. |
| [PVIDEO_HW_TIMER callback](nc-video-pvideo-hw-timer.md) | HwVidTimer is a video miniport driver routine called at timed intervals by the video port driver. |
| [PINT10_READ_MEMORY callback](nc-video-pint10-read-memory.md) | The Int10ReadMemory function reads a block of memory in the context of another thread and stores it in an output buffer. |
| [PI2C_STOP callback](nc-video-pi2c-stop.md) | The I2CStop function ends I2C communication. |
| [PI2C_WRITE callback](nc-video-pi2c-write.md) | The I2CWrite function writes data over the I2C channel. |
| [PINT10_WRITE_MEMORY callback](nc-video-pint10-write-memory.md) | The Int10WriteMemory function writes the contents of an input buffer to memory in the context of another thread. |
| [PI2C_START callback](nc-video-pi2c-start.md) | The I2CStart function starts I2C communication. |
| [PVIDEO_HW_POWER_SET callback](nc-video-pvideo-hw-power-set.md) | HwVidSetPowerState sets the power state of the specified device. |
| [PVIDEO_HW_INITIALIZE callback](nc-video-pvideo-hw-initialize.md) | HwVidInitialize performs the first initialization of the adapter, after the HAL has given up control of the video hardware to the video port driver. |
| [PDRIVER_IO_PORT_UCHAR_STRING callback](nc-video-pdriver-io-port-uchar-string.md) | SvgaHwIoPortUcharString traps an I/O port to which a full-screen MS-DOS application in an x86-based machine is sending a sequence of UCHAR-sized data. |
| [PVIDEO_WAIT_VSYNC_ACTIVE callback function](nc-video-pvideo-wait-vsync-active.md) | TBD |
| [PI2C_READ callback](nc-video-pi2c-read.md) | The I2CRead function reads data over the I2C channel. |
| [PVIDEO_READ_DATA_LINE callback](nc-video-pvideo-read-data-line.md) | ReadDataLine reads a single data bit from the I2C serial data line. |
| [PI2C_READ_2 callback function](nc-video-pi2c-read-2.md) | TBD |
| [PMINIPORT_GET_REGISTRY_ROUTINE callback](nc-video-pminiport-get-registry-routine.md) | HwVidQueryNamedValueCallback processes the specified data retrieved from the registry. |
| [PVIDEO_BUGCHECK_CALLBACK callback](nc-video-pvideo-bugcheck-callback.md) | The HwVidBugcheckCallback function enables the miniport driver to append data to a dump file when a bug check occurs. |
| [PVIDEO_HW_CHILD_CALLBACK callback function](nc-video-pvideo-hw-child-callback.md) | TBD |
| [PVIDEO_HW_START_DMA callback function](nc-video-pvideo-hw-start-dma.md) | TBD |
| [PMINIPORT_DPC_ROUTINE callback](nc-video-pminiport-dpc-routine.md) | The HwVidDpcRoutine function is a miniport driver-implemented callback that is called when a queued DPC gets scheduled. |
| [PDRIVER_IO_PORT_ULONG_STRING callback](nc-video-pdriver-io-port-ulong-string.md) | SvgaHwIoPortUlongString traps an I/O port range to which a full-screen MS-DOS application in an x86-based machine is sending a sequence of ULONG-sized data. |
| [PVIDEO_HW_LEGACYRESOURCES callback](nc-video-pvideo-hw-legacyresources.md) | HwVidLegacyResources returns a list of resources that are not listed in a device's PCI configuration space but that are decoded by the device. |
| [PVIDEO_WRITE_CLOCK_LINE callback](nc-video-pvideo-write-clock-line.md) | WriteClockLine sets the I2C serial clock line to high or low. |
| [PROTECT_WC_MEMORY callback](nc-video-protect-wc-memory.md) | The VideoPortProtectWCMemory callback routine protects Write Combined (WC) video memory from being accessed by the CPU. |
| [PMINIPORT_SYNCHRONIZE_ROUTINE callback](nc-video-pminiport-synchronize-routine.md) | HwVidSynchronizeExecutionCallback is an optional miniport driver function, passed in calls to VideoPortSynchronizeExecution. |
| [PI2C_STOP_2 callback function](nc-video-pi2c-stop-2.md) | TBD |
| [PDRIVER_IO_PORT_USHORT_STRING callback](nc-video-pdriver-io-port-ushort-string.md) | SvgaHwIoPortUshortString traps an I/O port range to which a full-screen MS-DOS application in an x86-based machine is sending a sequence of USHORT-sized data. |
| [PVIDEO_HW_FIND_ADAPTER callback](nc-video-pvideo-hw-find-adapter.md) | HwVidFindAdapter performs initialization of data specific to the miniport driver and devices supported by the miniport driver. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [VIDEO_DEBUG_LEVEL enumeration](ne-video-video-debug-level.md) | TBD |
| [VIDEO_SYNCHRONIZE_PRIORITY enumeration](ne-video-video-synchronize-priority.md) | TBD |
| [VP_LOCK_OPERATION enumeration](ne-video--vp-lock-operation.md) | TBD |
| [PVIDEO_CHILD_TYPE enumeration](ne-video-pvideo-child-type.md) | TBD |
| [HW_DMA_RETURN enumeration](ne-video--hw-dma-return.md) | TBD |
| [VP_POOL_TYPE enumeration](ne-video--vp-pool-type.md) | TBD |
| [VIDEO_DEVICE_DATA_TYPE enumeration](ne-video--video-device-data-type.md) | TBD |
| [DMA_FLAGS enumeration](ne-video-dma-flags.md) | TBD |
| [VIDEO_PORT_SERVICES enumeration](ne-video-video-port-services.md) | The VIDEO_PORT_SERVICES enumerated type lists the interfaces that the video miniport driver can request from the video port driver by calling VideoPortQueryServices. |

This header is used in these topics:

- [display](..content/_display)
