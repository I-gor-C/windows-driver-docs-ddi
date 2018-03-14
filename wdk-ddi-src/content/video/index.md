---
UID: NA:video
ms.assetid: 674c88a6-47af-3f20-8f7a-e79f72def812
ms.author: windowsdriverdev
ms.date: 03/13/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# video.h header



video.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [VideoPortAcquireDeviceLock](nf-video-videoportacquiredevicelock.md) | The VideoPortAcquireDeviceLock function acquires the device lock maintained by the video port driver. |
| [VideoPortAcquireSpinLock](nf-video-videoportacquirespinlock.md) | The VideoPortAcquireSpinLock function obtains the specified spin lock. |
| [VideoPortAcquireSpinLockAtDpcLevel](nf-video-videoportacquirespinlockatdpclevel.md) | The VideoPortAcquireSpinLockAtDpcLevel function acquires a spin lock when the caller is already running at IRQL = DISPATCH_LEVEL. |
| [VideoPortAllocateBuffer](nf-video-videoportallocatebuffer.md) | The VideoPortAllocateBuffer function is obsolete in Windows 2000 and later. In its place, video miniport drivers should instead use VideoPortAllocatePool. VideoPortAllocateBuffer allocates a buffer of paged pool memory. |
| [VideoPortAllocateCommonBuffer](nf-video-videoportallocatecommonbuffer.md) | The VideoPortAllocateCommonBuffer function allocates and maps system memory so that it is simultaneously accessible from both the processor and a device for common-buffer DMA operations. |
| [VideoPortAllocateContiguousMemory](nf-video-videoportallocatecontiguousmemory.md) | The VideoPortAllocateContiguousMemory function is obsolete in Windows 2000 and later. |
| [VideoPortAllocatePool](nf-video-videoportallocatepool.md) | The VideoPortAllocatePool function allocates a block of pool memory, inserting a caller-supplied tag at the beginning of the memory. |
| [VideoPortAssociateEventsWithDmaHandle](nf-video-videoportassociateeventswithdmahandle.md) | The VideoPortAssociateEventsWithDmaHandle function is obsolete in Windows 2000 and later.VideoPortAssociateEventsWithDmaHandle associates an event, which is shared by the video display driver and the video miniport driver, with a DMA handle. |
| [VideoPortCheckForDeviceExistence](nf-video-videoportcheckfordeviceexistence.md) | The VideoPortCheckForDeviceExistence function determines whether the specified PCI device exists in the system. |
| [VideoPortClearEvent](nf-video-videoportclearevent.md) | The VideoPortClearEvent function sets a given event object to the nonsignaled state. |
| [VideoPortCompareMemory](nf-video-videoportcomparememory.md) | The VideoPortCompareMemory function compares two blocks of system memory, byte-by-byte, and returns the number of compared bytes that are equivalent. |
| [VideoPortCompleteDma](nf-video-videoportcompletedma.md) | The VideoPortCompleteDma function flushes any data remaining in a bus-master adapter's internal cache at the end of a DMA transfer operation, and then frees the previously allocated map registers and scatter/gather list used in scatter/gather DMA operations. |
| [VideoPortCreateEvent](nf-video-videoportcreateevent.md) | The VideoPortCreateEvent function creates an event object. |
| [VideoPortCreateSecondaryDisplay](nf-video-videoportcreatesecondarydisplay.md) | The VideoPortCreateSecondaryDisplay function enables dual-view support by creating a secondary device object for the given device. |
| [VideoPortCreateSpinLock](nf-video-videoportcreatespinlock.md) | The VideoPortCreateSpinLock function creates a spin lock. |
| [VideoPortDDCMonitorHelper](nf-video-videoportddcmonitorhelper.md) | Queries a monitor for EDID information using the DDC protocol. |
| [VideoPortDebugPrint](nf-video-videoportdebugprint.md) | Video miniport drivers should not call the VideoPortDebugPrint function. Instead, they should call the VideoDebugPrint macro. |
| [VideoPortDeleteEvent](nf-video-videoportdeleteevent.md) | The VideoPortDeleteEvent function deletes the specified event object. |
| [VideoPortDeleteSpinLock](nf-video-videoportdeletespinlock.md) | The VideoPortDeleteSpinLock function deletes a given spin lock. |
| [VideoPortDisableInterrupt](nf-video-videoportdisableinterrupt.md) | The VideoPortDisableInterrupt function is obsolete and should not be called.The VideoPortDisableInterrupt function disables interrupts from a video adapter. |
| [VideoPortDoDma](nf-video-videoportdodma.md) | The VideoPortDoDma function is obsolete in Windows 2000 and later. VideoPortDoDma causes the miniport driver's HwVidStartDma function to be called. |
| [VideoPortEnableInterrupt](nf-video-videoportenableinterrupt.md) | The VideoPortEnableInterrupt function is obsolete and should not be called.The VideoPortEnableInterrupt function reenables interrupts from a video adapter after a call to VideoPortDisableInterrupt. |
| [VideoPortEnumerateChildren](nf-video-videoportenumeratechildren.md) | The VideoPortEnumerateChildren function allows a video miniport driver to force a reenumeration of its child devices. |
| [VideoPortFlushRegistry](nf-video-videoportflushregistry.md) | The VideoPortFlushRegistry function flushes registry keys and values associated with the video miniport driver. |
| [VideoPortFreeCommonBuffer](nf-video-videoportfreecommonbuffer.md) | The VideoPortFreeCommonBuffer function is obsolete and is supported only for backward compatibility with existing drivers. |
| [VideoPortFreeDeviceBase](nf-video-videoportfreedevicebase.md) | The VideoPortFreeDeviceBase function frees a range of bus-relative device I/O ports or memory addresses previously mapped into the system address space. It does this by calling VideoPortGetDeviceBase. |
| [VideoPortFreePool](nf-video-videoportfreepool.md) | The VideoPortFreePool function deallocates a block of pool memory previously allocated by VideoPortAllocatePool. |
| [VideoPortGetAccessRanges](nf-video-videoportgetaccessranges.md) | The VideoPortGetAccessRanges function retrieves bus-relative configuration information and, if possible, claims these hardware resources in the registry for the caller. |
| [VideoPortGetAssociatedDeviceExtension](nf-video-videoportgetassociateddeviceextension.md) | The VideoPortGetAssociatedDeviceExtension function returns the device extension for the parent of the specified device object. |
| [VideoPortGetAssociatedDeviceID](nf-video-videoportgetassociateddeviceid.md) | The VideoPortGetAssociatedDeviceID function obtains the child ID for a specified device object. |
| [VideoPortGetBusData](nf-video-videoportgetbusdata.md) | The VideoPortGetBusData function returns bus-type-specific configuration information. |
| [VideoPortGetBytesUsed](nf-video-videoportgetbytesused.md) | The VideoPortGetBytesUsed function is obsolete in Windows 2000 and later.VideoPortGetBytesUsed determines the size, in bytes, of the buffer associated with a DMA handle. |
| [VideoPortGetCommonBuffer](nf-video-videoportgetcommonbuffer.md) | The VideoPortGetCommonBuffer function is obsolete in Windows XP and later, and is supported only for backward compatibility with existing drivers. |
| [VideoPortGetCurrentIrql](nf-video-videoportgetcurrentirql.md) | The VideoPortGetCurrentIrql function gets the current IRQL. |
| [VideoPortGetDeviceBase](nf-video-videoportgetdevicebase.md) | The VideoPortGetDeviceBase function maps a range of bus-relative device memory or I/O addresses into system space. |
| [VideoPortGetDeviceData](nf-video-videoportgetdevicedata.md) | The VideoPortGetDeviceData function retrieves system-detected configuration information from the ..\Machine\Hardware\Description tree in the registry. |
| [VideoPortGetDmaAdapter](nf-video-videoportgetdmaadapter.md) | The VideoPortGetDmaAdapter function returns a pointer to a VP_DMA_ADAPTER structure, which is used in subsequent calls to other DMA-related functions. |
| [VideoPortGetDmaContext](nf-video-videoportgetdmacontext.md) | The VideoPortGetDmaContext function is obsolete in Windows 2000 and later.VideoPortGetDmaContext gets the context previously associated with the specified DMA handle. |
| [VideoPortGetMdl](nf-video-videoportgetmdl.md) | The VideoPortGetMdl function is obsolete in Windows 2000 and later.VideoPortGetMdl retrieves the memory descriptor list (MDL) that represents the page table of the locked buffer. |
| [VideoPortGetRegistryParameters](nf-video-videoportgetregistryparameters.md) | The VideoPortGetRegistryParameters function retrieves device-specific configuration information under the adapter key in the registry at startup. |
| [VideoPortGetRomImage](nf-video-videoportgetromimage.md) | Reads the device's read-only memory (ROM). |
| [VideoPortGetVersion](nf-video-videoportgetversion.md) | The VideoPortGetVersion function gets version information about the currently running operating system. |
| [VideoPortGetVgaStatus](nf-video-videoportgetvgastatus.md) | The VideoPortGetVgaStatus function detects whether the calling device is decoding a VGA I/O address. |
| [VideoPortInitialize](nf-video-videoportinitialize.md) | The VideoPortInitialize function performs part of the miniport driver initialization, allocating system resources for the miniport driver. |
| [VideoPortInt10](nf-video-videoportint10.md) | The VideoPortInt10 function performs the equivalent of an MS-DOS INT10 operation, such as setting the video mode. VideoPortInt10 runs the BIOS ROM code on the device. |
| [VideoPortInterlockedDecrement](nf-video-videoportinterlockeddecrement.md) | The VideoPortInterlockedDecrement function decrements a caller-supplied variable as an atomic operation. |
| [VideoPortInterlockedExchange](nf-video-videoportinterlockedexchange.md) | The VideoPortInterlockedExchange function locks or unlocks a block of memory by setting a user-defined lock variable to TRUE or FALSE, respectively. It returns the previously-held value of the lock variable. |
| [VideoPortInterlockedIncrement](nf-video-videoportinterlockedincrement.md) | The VideoPortInterlockedIncrement function increments a caller-supplied variable as an atomic operation. |
| [VideoPortIsNoVesa](nf-video-videoportisnovesa.md) | The VideoPortIsNoVesa function determines whether a video miniport driver that does not support Plug and Play (PnP) is restricted to legacy VGA resources. |
| [VideoPortLockBuffer](nf-video-videoportlockbuffer.md) | The VideoPortLockBuffer function probes the specified buffer, makes the buffer's memory pages resident in memory, and locks the physical pages mapped by the virtual address range. |
| [VideoPortLockPages](nf-video-videoportlockpages.md) | The VideoPortLockPages function is obsolete in Windows 2000 and later. Use VideoPortLockBuffer in place of this function.VideoPortLockPages locks the specified virtual memory and possibly performs part or all of a DMA transfer. |
| [VideoPortLogError](nf-video-videoportlogerror.md) | The VideoPortLogError function logs errors to the system event log when a miniport driver detects a hardware error condition during I/O operations. |
| [VideoPortMapBankedMemory](nf-video-videoportmapbankedmemory.md) | The VideoPortMapBankedMemory function is obsolete, and is supported only for Windows NT 4.0 and previous drivers. |
| [VideoPortMapDmaMemory](nf-video-videoportmapdmamemory.md) | The VideoPortMapDmaMemory function is obsolete in Windows 2000 and later.VideoPortMapDmaMemory maps a range of memory for use in DMA transfers. |
| [VideoPortMapMemory](nf-video-videoportmapmemory.md) | The VideoPortMapMemory function maps a range of bus-relative physical addresses of video memory into system space or into the virtual address space of a user-mode process. |
| [VideoPortMoveMemory](nf-video-videoportmovememory.md) | The VideoPortMoveMemory function copies data from the source location to the destination location in system memory. |
| [VideoPortPutDmaAdapter](nf-video-videoportputdmaadapter.md) | The VideoPortPutDmaAdapter function frees a VP_DMA_ADAPTER structure that was previously allocated by a call to VideoPortGetDmaAdapter. |
| [VideoPortQueryPerformanceCounter](nf-video-videoportqueryperformancecounter.md) | The VideoPortQueryPerformanceCounter function provides the finest-grained running count available in the system. |
| [VideoPortQueryServices](nf-video-videoportqueryservices.md) | The VideoPortQueryServices function exposes a specified interface that is implemented by the video port driver. |
| [VideoPortQuerySystemTime](nf-video-videoportquerysystemtime.md) | The VideoPortQuerySystemTime function obtains the current system time. |
| [VideoPortQueueDpc](nf-video-videoportqueuedpc.md) | The VideoPortQueueDpc function allows a miniport driver to queue a DPC. |
| [VideoPortReadPortBufferUchar](nf-video-videoportreadportbufferuchar.md) | The VideoPortReadPortBufferUchar function reads a number of bytes from a mapped I/O port and writes them into a buffer. |
| [VideoPortReadPortBufferUlong](nf-video-videoportreadportbufferulong.md) | The VideoPortReadPortBufferUlong function reads a number of ULONG values from a mapped I/O port and writes them into a buffer. |
| [VideoPortReadPortBufferUshort](nf-video-videoportreadportbufferushort.md) | The VideoPortReadPortBufferUshort function reads a number of USHORT values from a mapped I/O port and writes them into a buffer. |
| [VideoPortReadPortUchar](nf-video-videoportreadportuchar.md) | The VideoPortReadPortUchar function reads a byte from a mapped I/O port. |
| [VideoPortReadPortUlong](nf-video-videoportreadportulong.md) | The VideoPortReadPortUlong function reads a ULONG value from a mapped I/O port. |
| [VideoPortReadPortUshort](nf-video-videoportreadportushort.md) | The VideoPortReadPortUshort function reads a USHORT value from a mapped I/O port. |
| [VideoPortReadRegisterBufferUchar](nf-video-videoportreadregisterbufferuchar.md) | The VideoPortReadRegisterBufferUchar function reads a number of bytes from a mapped device memory range and writes them into a buffer. |
| [VideoPortReadRegisterBufferUlong](nf-video-videoportreadregisterbufferulong.md) | The VideoPortReadRegisterBufferUlong function reads a number of ULONG values from a mapped device memory range and writes them into a buffer. |
| [VideoPortReadRegisterBufferUshort](nf-video-videoportreadregisterbufferushort.md) | The VideoPortReadRegisterBufferUshort function reads a number of USHORT values from a mapped device memory range and writes them into a buffer. |
| [VideoPortReadRegisterUchar](nf-video-videoportreadregisteruchar.md) | The VideoPortReadRegisterUchar function reads a byte from a mapped register. |
| [VideoPortReadRegisterUlong](nf-video-videoportreadregisterulong.md) | The VideoPortReadRegisterUlong function reads a ULONG value from a mapped register range. |
| [VideoPortReadRegisterUshort](nf-video-videoportreadregisterushort.md) | The VideoPortReadRegisterUshort function reads a USHORT value from a mapped register range. |
| [VideoPortReadStateEvent](nf-video-videoportreadstateevent.md) | The VideoPortReadStateEvent function returns the current state of a given event object:\_signaled or nonsignaled. |
| [VideoPortRegisterBugcheckCallback](nf-video-videoportregisterbugcheckcallback.md) | The VideoPortRegisterBugcheckCallback function allows a video miniport driver to register for, or hook, a callback that is invoked when a specified bug check occurs. |
| [VideoPortReleaseBuffer](nf-video-videoportreleasebuffer.md) | The VideoPortReleaseBuffer function is obsolete in Windows 2000 and later. In its place, video miniport drivers should instead use VideoPortFreePool. VideoPortReleaseBuffer deallocates a block of paged pool memory. |
| [VideoPortReleaseCommonBuffer](nf-video-videoportreleasecommonbuffer.md) | The VideoPortReleaseCommonBuffer function frees a common buffer that was previously allocated by VideoPortAllocateCommonBuffer. |
| [VideoPortReleaseDeviceLock](nf-video-videoportreleasedevicelock.md) | The VideoPortReleaseDeviceLock function releases the device lock acquired in a prior call to VideoPortAcquireDeviceLock. |
| [VideoPortReleaseSpinLock](nf-video-videoportreleasespinlock.md) | The VideoPortReleaseSpinLock function releases ownership of a given spin lock and restores the original IRQL at which the caller was running. |
| [VideoPortReleaseSpinLockFromDpcLevel](nf-video-videoportreleasespinlockfromdpclevel.md) | The VideoPortReleaseSpinLockFromDpcLevel function releases the spin lock obtained by a previous call to VideoPortAcquireSpinLockAtDpcLevel. |
| [VideoPortScanRom](nf-video-videoportscanrom.md) | The VideoPortScanRom function is obsolete in Windows XP and later versions. It is supported only for backward compatibility. VideoPortScanRom performs a case-sensitive search for a specified string in ROM. |
| [VideoPortSetBusData](nf-video-videoportsetbusdata.md) | The VideoPortSetBusData function sets bus-configuration data for an adapter on a dynamically configurable I/O bus with a published, standard interface. |
| [VideoPortSetBytesUsed](nf-video-videoportsetbytesused.md) | The VideoPortSetBytesUsed function is obsolete in Windows 2000 and later. |
| [VideoPortSetDmaContext](nf-video-videoportsetdmacontext.md) | The VideoPortSetDmaContext function is obsolete in Windows 2000 and later. |
| [VideoPortSetEvent](nf-video-videoportsetevent.md) | The VideoPortSetEvent function sets an event object to the signaled state if it was not already in that state, and returns the event object's previous state. |
| [VideoPortSetRegistryParameters](nf-video-videoportsetregistryparameters.md) | The VideoPortSetRegistryParameters function writes information under the adapter key in the registry. |
| [VideoPortSetTrappedEmulatorPorts](nf-video-videoportsettrappedemulatorports.md) | VGA-compatible (SVGA) miniport drivers call the VideoPortSetTrappedEmulatorPorts function to dynamically change the list of I/O ports that are trapped when a VDM runs in full-screen mode on an x86-based machine. |
| [VideoPortSignalDmaComplete](nf-video-videoportsignaldmacomplete.md) | The VideoPortSignalDmaComplete function is obsolete in Windows 2000 and later.VideoPortSignalDmaComplete indicates to the video miniport driver whether the current DMA transfer is complete. |
| [VideoPortStallExecution](nf-video-videoportstallexecution.md) | The VideoPortStallExecution function retains control of the processor for the specified number of microseconds and returns to the caller. |
| [VideoPortStartDma](nf-video-videoportstartdma.md) | The VideoPortStartDma function prepares the system for a DMA operation. |
| [VideoPortStartTimer](nf-video-videoportstarttimer.md) | The VideoPortStartTimer function enables calls to a miniport driver's HwVidTimer function. |
| [VideoPortStopTimer](nf-video-videoportstoptimer.md) | The VideoPortStopTimer function disables calls to a miniport driver's HwVidTimer function. |
| [VideoPortSynchronizeExecution](nf-video-videoportsynchronizeexecution.md) | The VideoPortSynchronizeExecution function synchronizes the execution of a miniport driver-supplied HwVidSynchronizeExecutionCallback function with the miniport driver's HwVidInterrupt function, if any. |
| [VideoPortUnlockBuffer](nf-video-videoportunlockbuffer.md) | The VideoPortUnLockBuffer function unlocks physical pages described by the specified memory descriptor list (MDL). |
| [VideoPortUnlockPages](nf-video-videoportunlockpages.md) | The VideoPortUnlockPages function is obsolete in Windows 2000 and later. Use VideoPortUnlockBuffer in place of this function.VideoPortUnlockPages releases memory used for packet-based DMA. |
| [VideoPortUnmapDmaMemory](nf-video-videoportunmapdmamemory.md) | The VideoPortUnmapDmaMemory function is obsolete in Windows 2000 and later.VideoPortUnmapDmaMemory unmaps a range of memory previously mapped by VideoPortMapDmaMemory. |
| [VideoPortUnmapMemory](nf-video-videoportunmapmemory.md) | The VideoPortUnmapMemory function releases a mapping between a logical address range for the adapter and a virtual address range in the user-mode address space of a particular thread. This function is the complement of VideoPortMapMemory. |
| [VideoPortVerifyAccessRanges](nf-video-videoportverifyaccessranges.md) | The VideoPortVerifyAccessRanges function checks the registry for whether another driver has already claimed ownership of the specified bus-relative access ranges and any other hardware resources specified in the VIDEO_PORT_CONFIG_INFO structure. |
| [VideoPortWaitForSingleObject](nf-video-videoportwaitforsingleobject.md) | The VideoPortWaitForSingleObject function puts the current thread into a wait state until the given dispatch object is set to the signaled state, or (optionally) until the wait times out. |
| [VideoPortWritePortBufferUchar](nf-video-videoportwriteportbufferuchar.md) | The VideoPortWritePortBufferUchar function writes a number of bytes to a mapped I/O port. |
| [VideoPortWritePortBufferUlong](nf-video-videoportwriteportbufferulong.md) | The VideoPortWritePortBufferUlong function writes a number of ULONG values to a mapped I/O port. |
| [VideoPortWritePortBufferUshort](nf-video-videoportwriteportbufferushort.md) | The VideoPortWritePortBufferUshort function writes a number of USHORT values to a mapped I/O port. |
| [VideoPortWritePortUchar](nf-video-videoportwriteportuchar.md) | The VideoPortWritePortUchar function writes a byte to a mapped I/O port. |
| [VideoPortWritePortUlong](nf-video-videoportwriteportulong.md) | The VideoPortWritePortUlong function writes a ULONG value to a mapped I/O port. |
| [VideoPortWritePortUshort](nf-video-videoportwriteportushort.md) | The VideoPortWritePortUshort function writes a USHORT value to a mapped I/O port. |
| [VideoPortWriteRegisterBufferUchar](nf-video-videoportwriteregisterbufferuchar.md) | The VideoPortWriteRegisterBufferUchar function writes a number of unsigned bytes to a mapped register. |
| [VideoPortWriteRegisterBufferUlong](nf-video-videoportwriteregisterbufferulong.md) | The VideoPortWriteRegisterBufferUlong function writes a number of ULONG values to a mapped register. |
| [VideoPortWriteRegisterBufferUshort](nf-video-videoportwriteregisterbufferushort.md) | The VideoPortWriteRegisterBufferUshort function writes a number of USHORT values to a mapped register. |
| [VideoPortWriteRegisterUchar](nf-video-videoportwriteregisteruchar.md) | The VideoPortWriteRegisterUchar function writes a byte to a mapped register. |
| [VideoPortWriteRegisterUlong](nf-video-videoportwriteregisterulong.md) | The VideoPortWriteRegisterUlong function writes a ULONG value to a mapped register. |
| [VideoPortWriteRegisterUshort](nf-video-videoportwriteregisterushort.md) | The VideoPortWriteRegisterUshort function writes a USHORT value to a mapped register. |
| [VideoPortZeroDeviceMemory](nf-video-videoportzerodevicememory.md) | The VideoPortZeroDeviceMemory function fills an adapter frame buffer or other device memory with zeros. |
| [VideoPortZeroMemory](nf-video-videoportzeromemory.md) | The VideoPortZeroMemory function fills a block of system memory with zeros. |


## Callback functions
| Title | Description |
| ---- |:---- |
| [PDRIVER_IO_PORT_UCHAR](nc-video-pdriver_io_port_uchar.md) | SvgaHwIoPortUchar traps an I/O port to which a full-screen MS-DOS application in an x86-based machine is sending UCHAR-sized data. |
| [PDRIVER_IO_PORT_UCHAR_STRING](nc-video-pdriver_io_port_uchar_string.md) | SvgaHwIoPortUcharString traps an I/O port to which a full-screen MS-DOS application in an x86-based machine is sending a sequence of UCHAR-sized data. |
| [PDRIVER_IO_PORT_ULONG](nc-video-pdriver_io_port_ulong.md) | SvgaHwIoPortUlong traps an I/O port range to which a full-screen MS-DOS application in an x86-based machine is sending a sequence of ULONG-sized data. |
| [PDRIVER_IO_PORT_ULONG_STRING](nc-video-pdriver_io_port_ulong_string.md) | SvgaHwIoPortUlongString traps an I/O port range to which a full-screen MS-DOS application in an x86-based machine is sending a sequence of ULONG-sized data. |
| [PDRIVER_IO_PORT_USHORT](nc-video-pdriver_io_port_ushort.md) | SvgaHwIoPortUshort traps an I/O port range to which a full-screen MS-DOS application in an x86-based machine is sending a sequence of USHORT-sized data. |
| [PDRIVER_IO_PORT_USHORT_STRING](nc-video-pdriver_io_port_ushort_string.md) | SvgaHwIoPortUshortString traps an I/O port range to which a full-screen MS-DOS application in an x86-based machine is sending a sequence of USHORT-sized data. |
| [PEXECUTE_DMA](nc-video-pexecute_dma.md) | HwVidExecuteDma is a miniport driver-implemented callback routine that is responsible for retrieving physical address/length pairs from a scatter/gather list, and for programming the hardware to start the actual DMA transfer. |
| [PI2C_READ](nc-video-pi2c_read.md) | The I2CRead function reads data over the I2C channel. |
| [PI2C_START](nc-video-pi2c_start.md) | The I2CStart function starts I2C communication. |
| [PI2C_STOP](nc-video-pi2c_stop.md) | The I2CStop function ends I2C communication. |
| [PI2C_WRITE](nc-video-pi2c_write.md) | The I2CWrite function writes data over the I2C channel. |
| [PINT10_ALLOCATE_BUFFER](nc-video-pint10_allocate_buffer.md) | The Int10AllocateBuffer function can be used to allocate a single 4 KB block of memory in the context of another thread. After the block of memory has been allocated, it must be freed before another block of memory can be allocated. |
| [PINT10_CALL_BIOS](nc-video-pint10_call_bios.md) | The Int10CallBios function allows a miniport driver to call the kernel to perform an INT 10h operation, causing the BIOS ROM code on the device to execute natively. |
| [PINT10_FREE_BUFFER](nc-video-pint10_free_buffer.md) | The Int10FreeBuffer function frees a buffer previously allocated by Int10AllocateBuffer. |
| [PINT10_READ_MEMORY](nc-video-pint10_read_memory.md) | The Int10ReadMemory function reads a block of memory in the context of another thread and stores it in an output buffer. |
| [PINT10_WRITE_MEMORY](nc-video-pint10_write_memory.md) | The Int10WriteMemory function writes the contents of an input buffer to memory in the context of another thread. |
| [PMINIPORT_DPC_ROUTINE](nc-video-pminiport_dpc_routine.md) | The HwVidDpcRoutine function is a miniport driver-implemented callback that is called when a queued DPC gets scheduled. |
| [PMINIPORT_GET_REGISTRY_ROUTINE](nc-video-pminiport_get_registry_routine.md) | HwVidQueryNamedValueCallback processes the specified data retrieved from the registry. |
| [PMINIPORT_QUERY_DEVICE_ROUTINE](nc-video-pminiport_query_device_routine.md) | HwVidQueryDeviceCallback uses the specified configuration data to configure its adapter, and, possibly, to fill in missing configuration information in the VIDEO_PORT_CONFIG_INFO structure. |
| [PMINIPORT_SYNCHRONIZE_ROUTINE](nc-video-pminiport_synchronize_routine.md) | HwVidSynchronizeExecutionCallback is an optional miniport driver function, passed in calls to VideoPortSynchronizeExecution. |
| [PROTECT_WC_MEMORY](nc-video-protect_wc_memory.md) | The VideoPortProtectWCMemory callback routine protects Write Combined (WC) video memory from being accessed by the CPU. |
| [PVIDEO_BUGCHECK_CALLBACK](nc-video-pvideo_bugcheck_callback.md) | The HwVidBugcheckCallback function enables the miniport driver to append data to a dump file when a bug check occurs. |
| [PVIDEO_HW_FIND_ADAPTER](nc-video-pvideo_hw_find_adapter.md) | HwVidFindAdapter performs initialization of data specific to the miniport driver and devices supported by the miniport driver. |
| [PVIDEO_HW_GET_CHILD_DESCRIPTOR](nc-video-pvideo_hw_get_child_descriptor.md) | HwVidGetVideoChildDescriptor returns a descriptor, a type, and an identification number for a particular child device of the display adapter. |
| [PVIDEO_HW_INITIALIZE](nc-video-pvideo_hw_initialize.md) | HwVidInitialize performs the first initialization of the adapter, after the HAL has given up control of the video hardware to the video port driver. |
| [PVIDEO_HW_INTERRUPT](nc-video-pvideo_hw_interrupt.md) | HwVidInterrupt detects and dismisses interrupts generated by the associated video adapter. |
| [PVIDEO_HW_LEGACYRESOURCES](nc-video-pvideo_hw_legacyresources.md) | HwVidLegacyResources returns a list of resources that are not listed in a device's PCI configuration space but that are decoded by the device. |
| [PVIDEO_HW_POWER_GET](nc-video-pvideo_hw_power_get.md) | HwVidGetPowerState queries whether the device can support the requested power state. |
| [PVIDEO_HW_POWER_SET](nc-video-pvideo_hw_power_set.md) | HwVidSetPowerState sets the power state of the specified device. |
| [PVIDEO_HW_QUERY_INTERFACE](nc-video-pvideo_hw_query_interface.md) | HwVidQueryInterface returns a miniport driver-implemented functional interface that a child device can call. |
| [PVIDEO_HW_RESET_HW](nc-video-pvideo_hw_reset_hw.md) | HwVidResetHw resets the adapter to character mode. |
| [PVIDEO_HW_START_IO](nc-video-pvideo_hw_start_io.md) | HwVidStartIO processes the specified VRP. |
| [PVIDEO_HW_TIMER](nc-video-pvideo_hw_timer.md) | HwVidTimer is a video miniport driver routine called at timed intervals by the video port driver. |
| [PVIDEO_PORT_GET_PROC_ADDRESS](nc-video-pvideo_port_get_proc_address.md) | The VideoPortGetProcAddress callback routine retrieves the address of a Windows 2000 or later video port driver function. |
| [PVIDEO_READ_CLOCK_LINE](nc-video-pvideo_read_clock_line.md) | ReadClockLine reads a single data bit from the I2C serial clock line. |
| [PVIDEO_READ_DATA_LINE](nc-video-pvideo_read_data_line.md) | ReadDataLine reads a single data bit from the I2C serial data line. |
| [PVIDEO_WRITE_CLOCK_LINE](nc-video-pvideo_write_clock_line.md) | WriteClockLine sets the I2C serial clock line to high or low. |
| [PVIDEO_WRITE_DATA_LINE](nc-video-pvideo_write_data_line.md) | WriteDataLine sets the I2C serial data line to high or low. |
| [RESTORE_WC_MEMORY](nc-video-restore_wc_memory.md) | The VideoPortRestoreWCMemory callback routine restores Write Combined video memory from a protected state after the VideoPortProtectWCMemory callback routine was called. |


## Structures
| Title | Description |
| ---- |:---- |
| [_DDC_CONTROL](ns-video-_ddc_control.md) | The DDC_CONTROL structure holds function pointers and EDID segment information needed by the VideoPortDDCMonitorHelper function, which is exported by the video port driver. |
| [_I2C_CALLBACKS](ns-video-_i2c_callbacks.md) | The I2C_CALLBACKS structure contains pointers to functions, implemented by the video miniport driver, that read from and write to the serial data and serial clock lines of the I2C bus. |
| [_INT10_BIOS_ARGUMENTS](ns-video-_int10_bios_arguments.md) | The INT10_BIOS_ARGUMENTS structure is used to support full-screen MS-DOS application INT10 calls. It contains nine of the high-end x86 microprocessor registers. |
| [_QUERY_INTERFACE](ns-video-_query_interface.md) | The QUERY_INTERFACE structure describes the interface being requested. |
| [_STATUS_BLOCK](ns-video-_status_block.md) | The STATUS_BLOCK structure is a substructure within the VIDEO_REQUEST_PACKET structure. A miniport driver's HwVidStartIO function must set the status block of each VRP that it gets. |
| [_VIDEO_ACCESS_RANGE](ns-video-_video_access_range.md) | The VIDEO_ACCESS_RANGE structure defines a device I/O port or memory range for the video adapter. |
| [_VIDEO_CHILD_ENUM_INFO](ns-video-_video_child_enum_info.md) | Describes the child device to be enumerated by the miniport driver. All members are set by the video port driver. |
| [_VIDEO_CHILD_STATE](ns-video-_video_child_state.md) | The VIDEO_CHILD_STATE structure contains information about a child device and the state into which it should be placed. |
| [_VIDEO_CHILD_STATE_CONFIGURATION](ns-video-_video_child_state_configuration.md) | The VIDEO_CHILD_STATE_CONFIGURATION structure contains an array of VIDEO_CHILD_STATE structures, each holding the state of a particular child device. |
| [_VIDEO_HW_INITIALIZATION_DATA](ns-video-_video_hw_initialization_data.md) | The VIDEO_HW_INITIALIZATION_DATA structure specifies the entry points and storage requirements for the miniport driver. This structure is created on the stack and initialized by the miniport driver's DriverEntry function. |
| [_VIDEO_PORT_AGP_INTERFACE](ns-video-_video_port_agp_interface.md) | The VIDEO_PORT_AGP_INTERFACE structure describes the AGP service routines provided by the video port driver. |
| [_VIDEO_PORT_AGP_INTERFACE_2](ns-video-_video_port_agp_interface_2.md) | The VIDEO_PORT_AGP_INTERFACE_2 structure describes the AGP service routines provided by the video port driver. |
| [_VIDEO_PORT_CONFIG_INFO](ns-video-_video_port_config_info.md) | The VIDEO_PORT_CONFIG_INFO structure contains bus-specific adapter configuration information. |
| [_VIDEO_PORT_DEBUG_REPORT_INTERFACE](ns-video-_video_port_debug_report_interface.md) | The VIDEO_PORT_DEBUG_REPORT_INTERFACE structure holds pointers to the Debug Report functions, which are implemented by the video port driver. |
| [_VIDEO_PORT_I2C_INTERFACE](ns-video-_video_port_i2c_interface.md) | The VIDEO_PORT_I2C_INTERFACE structure describes the I2C service routines provided by the video port driver. |
| [_VIDEO_PORT_INT10_INTERFACE](ns-video-_video_port_int10_interface.md) | The VIDEO_PORT_INT10_INTERFACE structure provides a way to allocate and deallocate memory in another thread's context, read from and write to that memory, and make INT10 BIOS calls. |
| [_VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE](ns-video-_video_port_wcmemoryprotection_interface.md) | The VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE structure describes the Write Combined video memory protection service routines implemented by the video port driver. The protected video memory cannot be accessed by the CPU. |
| [_VIDEO_REQUEST_PACKET](ns-video-_video_request_packet.md) | A pointer to a VIDEO_REQUEST_PACKET structure is passed to the miniport driver's HwVidStartIO function by the video port driver. |
| [_VIDEO_X86_BIOS_ARGUMENTS](ns-video-_video_x86_bios_arguments.md) | The VIDEO_x86_BIOS_ARGUMENTS structure is used to support full-screen MS-DOS application INT10 calls. It contains seven of the high-end x86 microprocessor registers. |
| [_VP_DEVICE_DESCRIPTION](ns-video-_vp_device_description.md) | The VP_DEVICE_DESCRIPTION structure describes the attributes of the physical device for which a driver is requesting a DMA object. |
| [_VP_SCATTER_GATHER_ELEMENT](ns-video-_vp_scatter_gather_element.md) | The VP_SCATTER_GATHER_ELEMENT structure is used to store information about a single scatter/gather element. |
| [_VP_SCATTER_GATHER_LIST](ns-video-_vp_scatter_gather_list.md) | The VP_SCATTER_GATHER_LIST structure is a collection of one or more scatter/gather elements. |
| [_VPOSVERSIONINFO](ns-video-_vposversioninfo.md) | The VPOSVERSIONINFO structure contains version information about the currently running operating system. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [VIDEO_PORT_SERVICES](ne-video-video_port_services.md) | The VIDEO_PORT_SERVICES enumerated type lists the interfaces that the video miniport driver can request from the video port driver by calling VideoPortQueryServices. |