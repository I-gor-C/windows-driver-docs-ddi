---
UID : NA:storport
ms.assetid : 366530f2-be44-3f7d-92e4-e74a385c6480
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# storport.h header



storport.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [HW_ADAPTER_CONTROL](nc-storport-hw_adapter_control.md) | A miniport driver's HwStorAdapterControl routine is called to perform synchronous operations to control the state or behavior of an adapter, such as stopping or restarting the HBA for power management. |
| [HW_BUILDIO](nc-storport-hw_buildio.md) | The HwStorBuildIo routine processes the SRB with unsynchronized access to shared system data structures before passing it to HwStorStartIo. |
| [HW_CLEANUP_TRACING](nc-storport-hw_cleanup_tracing.md) | The HwStorCleanupTracing callback routine allows the Storport virtual miniport driver to stop tracing and to free any related resources. |
| [HW_COMPLETE_SERVICE_IRP](nc-storport-hw_complete_service_irp.md) | The HwStorCompleteServiceIrp routine is called when the virtual adapter is being removed. When this happens, the Storport virtual miniport can complete any reverse-callback IRPs received in HwStorCompleteServiceIrp. |
| [HW_DPC_ROUTINE](nc-storport-hw_dpc_routine.md) | The HwStorDpcRoutine routine is a routine that is deferred for execution at DISPATCH IRQL by means of the deferred procedure call (DPC) mechanism. |
| [HW_FIND_ADAPTER](nc-storport-hw_find_adapter.md) | The HwStorFindAdapter routine uses the supplied configuration to determine whether a specific HBA is supported and, if it is, to return configuration information about that adapter. |
| [HW_FREE_ADAPTER_RESOURCES](nc-storport-hw_free_adapter_resources.md) | The HwStorFreeAdapterResources callback routine allows the Storport virtual miniport driver to free resources when the virtual adapter is being removed. This is the last callback routine for the adapter. |
| [HW_INITIALIZE](nc-storport-hw_initialize.md) | The HwStorInitialize routine initializes the miniport driver after a system reboot or power failure occurs. |
| [HW_INITIALIZE_TRACING](nc-storport-hw_initialize_tracing.md) | The HwStorInitializeTracing callback routine allows the Storport virtual miniport driver to set up tracing and any related resources. |
| [HW_INTERRUPT](nc-storport-hw_interrupt.md) | The Storport driver calls the HwStorInterrupt routine after the HBA generates an interrupt request. |
| [HW_MESSAGE_SIGNALED_INTERRUPT_ROUTINE](nc-storport-hw_message_signaled_interrupt_routine.md) | The HwMSInterruptRoutine routine handles a message signaled interrupt (MSI). |
| [HW_PASSIVE_INITIALIZE_ROUTINE](nc-storport-hw_passive_initialize_routine.md) | The HwStorPassiveInitializeRoutine callback routine is called after the HwStorInitialize routine when the current IRQL is at PASSIVE_LEVEL. |
| [HW_PROCESS_SERVICE_REQUEST](nc-storport-hw_process_service_request.md) | The HwStorProcessServiceRequest callback routine receives the device control IRP that contains the IOCTL_MINIPORT_PROCESS_SERVICE_IRP request when a caller, such as a user-mode application or kernel-mode driver, requires a &#0034;reverse callback&#0034; operation. |
| [HW_RESET_BUS](nc-storport-hw_reset_bus.md) | The HwStorResetBus routine is called by the port driver to clear error conditions. |
| [HW_STARTIO](nc-storport-hw_startio.md) | The Storport driver calls the HwStorStartIo routine one time for each incoming I/O request. |
| [HW_STATE_CHANGE](nc-storport-hw_state_change.md) | A miniport-provided callback that is called after a notification from StorPortStateChangeDetected is processed. |
| [HW_TIMER](nc-storport-hw_timer.md) | The HwStorTimer routine is called after the interval that is specified when the miniport driver called StorPortNotification with the RequestTimerCall NotificationType value. |
| [HW_TRACING_ENABLED](nc-storport-hw_tracing_enabled.md) | The HwStorTracingEnabled callback routine enables the Storport to notify a miniport that event tracing is enabled. |
| [HW_UNIT_CONTROL](nc-storport-hw_unit_control.md) | A miniport driver's HwStorUnitControl routine is called to perform synchronous operations to control the state of storage unit device. The miniport driver is notified to start a unit or handle a power state transition for a unit device. |
| [HW_WORKITEM](nc-storport-hw_workitem.md) | A miniport-provided callback function for processing a Storport work item request. |
| [VIRTUAL_HW_FIND_ADAPTER](nc-storport-virtual_hw_find_adapter.md) | The Storport virtual miniport uses configuration information supplied to the VirtualHwStorFindAdapter routine to further initialize itself. |
| [StorPortAcquireMSISpinLock](nf-storport-storportacquiremsispinlock.md) | The StorPortAcquireMSISpinLock routine acquires the message signaled interrupt (MSI) spin lock that is associated with the specified message. |
| [StorPortAcquireSpinLock](nf-storport-storportacquirespinlock.md) | The StorPortAcquireSpinLock routine acquires the specified spin lock. |
| [StorPortAllocateContiguousMemorySpecifyCacheNode](nf-storport-storportallocatecontiguousmemoryspecifycachenode.md) | The StorPortAllocateContiguousMemorySpecifyCacheNode routine allocates a range of physically contiguous noncached, nonpaged memory. |
| [StorPortAllocateHostMemoryBuffer](nf-storport-storportallocatehostmemorybuffer.md) | This function allocates one or more ranges of physically contiguous memory to be used as a Host Memory Buffer (HMB). |
| [StorPortAllocateMdl](nf-storport-storportallocatemdl.md) | The StorPortAllocateMdl routine allocates an MDL to describe the given non-paged pool memory. |
| [StorPortAllocatePool](nf-storport-storportallocatepool.md) | The StorPortAllocatePool routine allocates a block of non-contiguous, non-paged pool memory. |
| [StorPortAllocateRegistryBuffer](nf-storport-storportallocateregistrybuffer.md) | The StorPortAllocateRegistryBuffer routine is called by the miniport driver to allocate a buffer that can be used to read and write registry data. |
| [StorPortAsyncNotificationDetected](nf-storport-storportasyncnotificationdetected.md) | A storage miniport driver calls StorPortAsyncNotificationDetected to notify the Storport driver of a storage device status change event. |
| [StorPortBuildMdlForNonPagedPool](nf-storport-storportbuildmdlfornonpagedpool.md) | The StorPortBuildMdlForNonPagedPool routine updates the MDL to describe the associated non-paged memory. |
| [StorPortBuildScatterGatherList](nf-storport-storportbuildscattergatherlist.md) | The StorPortBuildScatterGatherList routine creates a scatter/gather list for the specified data buffer. |
| [StorPortBusy](nf-storport-storportbusy.md) | The StorPortBusy routine notifies the port driver that the adapter is currently busy, handling outstanding requests. |
| [StorPortCompleteRequest](nf-storport-storportcompleterequest.md) | The StorPortCompleteRequest routine completes all outstanding requests setting the SRB status value to SrbStatus. |
| [StorPortCompleteServiceIrp](nf-storport-storportcompleteserviceirp.md) | The StorPortCompleteServiceIrp routine is called by a Storport virtual miniport driver when it needs to complete a request that it received in its HwStorProcessServiceRequest callback routine. |
| [StorPortConvertUlongToPhysicalAddress](nf-storport-storportconvertulongtophysicaladdress.md) | The StorPortConvertUlongToPhysicalAddress routine converts an unsigned long address into a physical address. |
| [StorPortDebugPrint](nf-storport-storportdebugprint.md) | The StorPortDebugPrint routine prints a debug string to the kernel debugger, if the debugger is attached. |
| [StorPortDeviceBusy](nf-storport-storportdevicebusy.md) | The StorPortDeviceBusy routine notifies the port driver that the specified logical unit is currently busy, handling outstanding requests. |
| [StorPortDeviceReady](nf-storport-storportdeviceready.md) | The StorPortDeviceReady routine notifies the port driver that the indicated logical unit is ready to handle new requests. |
| [StorPortEnablePassiveInitialization](nf-storport-storportenablepassiveinitialization.md) | The StorPortEnablePassiveInitialization routine enables the miniport's HwStorPassiveInitializeRoutine callback routine to execute at PASSIVE_LEVEL during miniport initialization. |
| [StorPortEtwEvent2](nf-storport-storportetwevent2.md) | The StorPortEtwEvent2 publishes an Event Tracing for Windows (ETW) event to a storage trace channel. The miniport can log two general purpose ETW parameters. The ETW parameters are expressed as two name-value pairs. |
| [StorPortEtwEvent4](nf-storport-storportetwevent4.md) | The StorPortEtwEvent4 publishes an Event Tracing for Windows (ETW) event to a storage trace channel. The miniport can log four general purpose ETW parameters. The ETW parameters are expressed as four name-value pairs. |
| [StorPortEtwEvent8](nf-storport-storportetwevent8.md) | The StorPortEtwEvent8 publishes an Event Tracing for Windows (ETW) event to a storage trace channel. The miniport can log eight general purpose ETW parameters. The ETW parameters are expressed as eight name-value pairs. |
| [StorPortFreeContiguousMemorySpecifyCache](nf-storport-storportfreecontiguousmemoryspecifycache.md) | The StorPortFreeContiguousMemorySpecifyCache routine deallocates a range of noncached memory in the nonpaged portion of the system address space. |
| [StorPortFreeDeviceBase](nf-storport-storportfreedevicebase.md) | StorPortFreeDeviceBase frees a range of device I/O memory that was mapped by StorPortGetDeviceBase. |
| [StorPortFreeHostMemoryBuffer](nf-storport-storportfreehostmemorybuffer.md) | The StorPortFreeHostMemoryBuffer routine frees the physically contiguous memory that was allocated to be used for a Host Memory Buffer (HMB). |
| [StorPortFreeMdl](nf-storport-storportfreemdl.md) | The StorPortFreeMdl routine frees a memory descriptor list (MDL) describing non-paged pool memory. |
| [StorPortFreePool](nf-storport-storportfreepool.md) | The StorPortFreePool routine frees a block of memory that was previously allocated by a call to the StorPortAllocatePool routine. |
| [StorPortFreeRegistryBuffer](nf-storport-storportfreeregistrybuffer.md) | The StorPortFreeRegistryBuffer routine frees the buffer that was allocated for storing registry data. |
| [StorPortFreeTimer](nf-storport-storportfreetimer.md) | Frees a Storport timer context object previously created by the StorPortInitializeTimer routine. |
| [StorPortFreeWorker](nf-storport-storportfreeworker.md) | Frees a Storport work item previously allocated by the StorPortInitializeWorker routine. |
| [StorPortGetActiveGroupCount](nf-storport-storportgetactivegroupcount.md) | The StorPortGetActiveGroupCount routine returns the number of processor groups that are present in the system. |
| [StorPortGetActiveNodeCount](nf-storport-storportgetactivenodecount.md) | The StorPortGetActiveNodeCount routine returns the number of nodes that are present in the system. |
| [StorPortGetActivityIdSrb](nf-storport-storportgetactivityidsrb.md) | Retrieves the Event Tracing for Windows (ETW) activity ID associated with a request block. |
| [StorPortGetBusData](nf-storport-storportgetbusdata.md) | The StorPortGetBusData routine retrieves the bus-specific configuration information necessary to initialize the HBA. |
| [StorPortGetCurrentProcessorNumber](nf-storport-storportgetcurrentprocessornumber.md) | The StorPortGetCurrentProcessorNumber routine retrieves the current processor number from the kernel. |
| [StorPortGetDataInBufferMdl](nf-storport-storportgetdatainbuffermdl.md) | Returns an MDL associated with the input data buffer of a SCSI request block (SRB). |
| [StorPortGetDataInBufferScatterGatherList](nf-storport-storportgetdatainbufferscattergatherlist.md) | Returns the scatter-gather list associated with the input data buffer of a SCSI request block (SRB). |
| [StorPortGetDataInBufferSystemAddress](nf-storport-storportgetdatainbuffersystemaddress.md) | Returns the system address for the input data buffer of a SCSI request block (SRB). |
| [StorPortGetDeviceBase](nf-storport-storportgetdevicebase.md) | The StorPortGetDeviceBase routine maps an I/O address to system address space. |
| [StorPortGetDeviceObjects](nf-storport-storportgetdeviceobjects.md) | The StorPortGetDeviceObjects routine returns the device objects that are associated with the adapter device stack. |
| [StorPortGetGroupAffinity](nf-storport-storportgetgroupaffinity.md) | The StorPortGetGroupAffinity routine constructs a mask of the active processors in a requested group. |
| [StorPortGetHighestNodeNumber](nf-storport-storportgethighestnodenumber.md) | The StorPortGetHighestNodeNumber routine returns the largest possible node number on the system. |
| [StorPortGetLogicalProcessorRelationship](nf-storport-storportgetlogicalprocessorrelationship.md) | The StorPortGetLogicalProcessorRelationship routine returns relationship information for one or more specified types. |
| [StorPortGetLogicalUnit](nf-storport-storportgetlogicalunit.md) | The StorPortGetLogicalUnit routine returns a pointer to the miniport driver's per-logical-unit storage area. |
| [StorPortGetMSIInfo](nf-storport-storportgetmsiinfo.md) | The StorPortGetMSIInfo routine retrieves the message signaled interrupt (MSI) information for the specified message. |
| [StorPortGetNodeAffinity](nf-storport-storportgetnodeaffinity.md) | The StorPortGetNodeAffinity routine constructs a mask of the active processors in a requested non-uniform memory access (NUMA) node. |
| [StorPortGetOriginalMdl](nf-storport-storportgetoriginalmdl.md) | The StorPortGetOriginalMdl routine returns the MDL associated with the given SRB. |
| [StorPortGetPfns](nf-storport-storportgetpfns.md) | The StorPortGetPfns routine can be called when a miniport needs to retreive PFNs associated with a MDL for a SRB. |
| [StorPortGetPhysicalAddress](nf-storport-storportgetphysicaladdress.md) | The StorPortGetPhysicalAddress routine converts a given virtual address range to a physical address range for a DMA operation. |
| [StorPortGetRequestCryptoInfo](nf-storport-storportgetrequestcryptoinfo.md) | Reserved for system use. |
| [StorPortGetRequestInfo](nf-storport-storportgetrequestinfo.md) | The StorPortGetRequestInfo routine retrieves the IO request information associated with a SCSI request block (SRB) and returns it in a STOR_REQUEST_INFO structure. |
| [StorPortGetScatterGatherList](nf-storport-storportgetscattergatherlist.md) | The StorPortGetScatterGatherList routine retrieves the associated scatter/gather list for the specified SCSI request block (SRB). |
| [StorPortGetStartIoPerfParams](nf-storport-storportgetstartioperfparams.md) | The StorPortGetStartIoPerfParams routine places the performance parameters for a given I/O request in a STARTIO_PERFORMANCE_PARAMETERS structure. |
| [StorPortGetSystemAddress](nf-storport-storportgetsystemaddress.md) | The StorPortGetSystemAddress routine returns a virtual address in system space for the data buffer of the specified SCSI request block (SRB). |
| [StorPortGetSystemPortNumber](nf-storport-storportgetsystemportnumber.md) | The StorPortGetSystemPortNumber routine retrieves the system assigned port number for a storage adapter. |
| [StorPortGetUncachedExtension](nf-storport-storportgetuncachedextension.md) | The StorPortGetUncachedExtension routine allocates an uncached common buffer to be shared by the CPU and the device. |
| [StorPortGetVirtualAddress](nf-storport-storportgetvirtualaddress.md) | The StorPortGetVirtualAddress routine obtains a virtual address that maps to the indicated physical address. |
| [StorPortInitialize](nf-storport-storportinitialize.md) | The StorPortInitilize routine initializes the port driver parameters and extension data. StorPortInitilize also saves the adapter information provided from the miniport driver. |
| [StorPortInitializeCryptoEngine](nf-storport-storportinitializecryptoengine.md) | Reserved for system use. |
| [StorPortInitializeDpc](nf-storport-storportinitializedpc.md) | The StorPortInitializeDpc routine initializes a StorPort DPC. |
| [StorPortInitializeListHead](nf-storport-storportinitializelisthead.md) | The StorPortInitializeListHead routine initializes a STOR_LIST_ENTRY structure that represents the head of a doubly linked list. |
| [StorPortInitializePerfOpts](nf-storport-storportinitializeperfopts.md) | The StorPortInitializePerfOpts function initializes the performance optimizations that both the miniport driver and the Storport driver support using a PERF_CONFIGURATION_DATA structure. |
| [StorPortInitializePoFxPower](nf-storport-storportinitializepofxpower.md) | A miniport driver calls StorPortInitializePoFxPower to register a storage device with the power management framework (PoFx). |
| [StorPortInitializeSListHead](nf-storport-storportinitializeslisthead.md) | Initializes the head of a Storport managed singly linked list. |
| [StorPortInitializeSpinlock](nf-storport-storportinitializespinlock.md) | The StorPortInitializeSpinLock routine initializes a variable of type STOR_KSPIN_LOCK. |
| [StorPortInitializeTimer](nf-storport-storportinitializetimer.md) | Creates a Storport timer context object. |
| [StorPortInitializeWorker](nf-storport-storportinitializeworker.md) | Creates a new Storport work item that runs in a system worker thread. |
| [StorPortInterlockedFlushSList](nf-storport-storportinterlockedflushslist.md) | Removes all items from a Storport managed singly linked list. Access to the list is synchronized on a multiprocessor system. |
| [StorPortInterlockedInsertHeadList](nf-storport-storportinterlockedinsertheadlist.md) | The StorPortInterlockedInsertHeadList routine atomically inserts an entry at the beginning of a doubly linked list of STOR_LIST_ENTRY structures. |
| [StorPortInterlockedInsertTailList](nf-storport-storportinterlockedinserttaillist.md) | The StorPortInterlockedInsertTailList routine atomically inserts an entry at the end of a doubly linked list of STOR_LIST_ENTRY structures. |
| [StorPortInterlockedPopEntrySList](nf-storport-storportinterlockedpopentryslist.md) | Removes an item from the front of a Storport managed singly linked list. Access to the list is synchronized on a multiprocessor system. Syntax. |
| [StorPortInterlockedPushEntrySList](nf-storport-storportinterlockedpushentryslist.md) | Inserts an item at the front of a Storport managed singly linked list. Access to the list is synchronized on a multiprocessor system. |
| [StorPortInterlockedRemoveHeadList](nf-storport-storportinterlockedremoveheadlist.md) | The StorPortInterlockedRemoveHeadList routine removes an entry from the beginning of a doubly linked list of STOR_LIST_ENTRY structures. |
| [StorPortInvokeAcpiMethod](nf-storport-storportinvokeacpimethod.md) | The StorPortInvokeAcpiMethod routine executes an ACPI method for a storage device. |
| [StorPortIsCurrentOsInstallationUpgrade](nf-storport-storportiscurrentosinstallationupgrade.md) | The StorPortIsCurrentOsInstallationUpgrade routine checks if the current installation of Windows is an upgrade from a previous version or not. |
| [StorPortIsDeviceOperationAllowed](nf-storport-storportisdeviceoperationallowed.md) | A miniport driver can call the StorPortIsDeviceOperationAllowedminiport routine to determine if operations for a certain device management class are allowed. |
| [StorPortIssueDpc](nf-storport-storportissuedpc.md) | The StorPortIssueDpc routine issues a deferred procedure call (DPC). |
| [StorPortLogError](nf-storport-storportlogerror.md) | The StorPortLogError routine notifies the port driver that an error occurred. |
| [StorPortLogSystemEvent](nf-storport-storportlogsystemevent.md) | The StorPortLogSystemEvent routine gives miniport drivers full access to the capabilities of the Windows kernel event facility, enabling miniport drivers to create event log entries that are truly useful in troubleshooting storage issues. |
| [StorPortLogTelemetry](nf-storport-storportlogtelemetry.md) | The StorPortLogTelemetry routine logs a miniport telemetry event to help diagnose or collect any useful information. |
| [StorPortMarkDumpMemory](nf-storport-storportmarkdumpmemory.md) | A miniport should mark memory used for the dump file or the hibernation file. |
| [StorPortMoveMemory](nf-storport-storportmovememory.md) | The StorPortMoveMemory routine copies memory from one buffer to another. |
| [StorPortNotification](nf-storport-storportnotification.md) | The miniport driver uses the StorPortNotification routine to notify the Storport driver of certain events and conditions. |
| [StorPortPause](nf-storport-storportpause.md) | The StorPortPause routine pauses an adapter for the specified period of time. |
| [StorPortPauseDevice](nf-storport-storportpausedevice.md) | The StorPortPauseDevice routine pauses a specific logical unit device for the specified period of time. |
| [StorPortPoFxActivateComponent](nf-storport-storportpofxactivatecomponent.md) | The StorPortPoFxActivateComponent routine increments the activation reference count on the specified component of a storage device. |
| [StorPortPoFxIdleComponent](nf-storport-storportpofxidlecomponent.md) | The StorPortPoFxIdleComponent routine decrements the activation reference count of a specified component of a storage device. |
| [StorPortPoFxPowerControl](nf-storport-storportpofxpowercontrol.md) | The StorPortPoFxPowerControl routine sends a power control request to the power management framework (PoFx) to forward to the power engine plug-in (PEP). |
| [StorPortPoFxSetComponentLatency](nf-storport-storportpofxsetcomponentlatency.md) | The StorPortPoFxSetComponentLatency routine specifies the maximum latency that can be tolerated in the transition from the idle condition to the active condition in the specified storage device component. |
| [StorPortPoFxSetComponentResidency](nf-storport-storportpofxsetcomponentresidency.md) | The StorPortPoFxSetComponentResidency routine sets the estimated time for how long a storage device component is likely to remain idle after the component enters the idle condition. |
| [StorPortPutScatterGatherList](nf-storport-storportputscattergatherlist.md) | The StorPortPutScatterGatherList routine releases any resources associated with a scatter/gather list that was previously created by a call to the StorPortBuildScatterGatherList routine. |
| [StorPortQueryDepthSList](nf-storport-storportquerydepthslist.md) | Retrieves the number of entries in a Storport managed singly linked list. |
| [StorPortQueryPerformanceCounter](nf-storport-storportqueryperformancecounter.md) | The current system performance counter value is queried is returned by the StorPortQueryPerformanceCounter routine. |
| [StorPortQuerySystemTime](nf-storport-storportquerysystemtime.md) | The StoriPortQuerySystemTime routine obtains the current system time. |
| [StorPortQueueWorkItem](nf-storport-storportqueueworkitem.md) | Schedules a Storport work item to execute within the context of a system worker thread. |
| [StorPortReadPortBufferUchar](nf-storport-storportreadportbufferuchar.md) | The StorPortReadPortBufferUchar routine reads a value from a specified port address |
| [StorPortReadPortBufferUlong](nf-storport-storportreadportbufferulong.md) | The StorPortReadPortBufferUlong routine reads a value from a specified port address. |
| [StorPortReadPortBufferUshort](nf-storport-storportreadportbufferushort.md) | The StorPortReadPortBufferUshort routine reads a value from a specified port address. |
| [StorPortReadPortUchar](nf-storport-storportreadportuchar.md) | The StorPortReadPortUchar routine reads a value from a specified port address |
| [StorPortReadPortUlong](nf-storport-storportreadportulong.md) | The StorPortReadPortUlong routine reads a value from a specified port address. |
| [StorPortReadPortUshort](nf-storport-storportreadportushort.md) | The StorPortReadPortUshort routine reads a value from a specified port address. |
| [StorPortReadRegisterBufferUchar](nf-storport-storportreadregisterbufferuchar.md) | The StorPortReadRegisterBufferUchar routine reads a value from a specified register address. |
| [StorPortReadRegisterBufferUlong](nf-storport-storportreadregisterbufferulong.md) | The StorPortReadRegisterBufferUlong routine reads a value from a specified register address. |
| [StorPortReadRegisterBufferUlong64](nf-storport-storportreadregisterbufferulong64.md) | This StorPortReadRegisterBufferUlong64 routine reads a number of ULONG64 values from the specified 64-bit register address into a buffer. |
| [StorPortReadRegisterBufferUshort](nf-storport-storportreadregisterbufferushort.md) | The StorPortReadRegisterBufferUshort routine reads a value from a specified register address. |
| [StorPortReadRegisterUchar](nf-storport-storportreadregisteruchar.md) | The StorPortReadRegisterUchar routine reads a value from a specified register address. |
| [StorPortReadRegisterUlong](nf-storport-storportreadregisterulong.md) | The StorPortReadRegisterUlong routine reads a value from a specified register address. |
| [StorPortReadRegisterUlong64](nf-storport-storportreadregisterulong64.md) | The StorPortReadRegisterUlong64 routine reads a 64-bit value from a specified 64-bit register address. |
| [StorPortReadRegisterUshort](nf-storport-storportreadregisterushort.md) | The StorPortReadRegisterUshort routine reads a value from a specified register address. |
| [StorPortReady](nf-storport-storportready.md) | The StorPortReady routine notifies the port driver that the adapter is no longer busy. |
| [StorPortRegistryRead](nf-storport-storportregistryread.md) | The StorPortRegistryRead routine reads the registry data for the indicated device and value. |
| [StorPortRegistryReadAdapterKey](nf-storport-storportregistryreadadapterkey.md) | The StorPortRegistryReadAdapterKey routine is called by the miniport driver to read the hardware or device registry adapter keys located in registry at HKLM/CurrentControlSet/Enum/&lt;Instance path&gt;/DeviceParameters/... |
| [StorPortRegistryWrite](nf-storport-storportregistrywrite.md) | The StorPortRegistryWrite routine is called by the miniport driver to convert the registry data contained in a specified buffer from ASCII to Unicode and to then write the data to the miniport driver's per-HBA storage area. |
| [StorPortRegistryWriteAdapterKey](nf-storport-storportregistrywriteadapterkey.md) | The StorPortRegistryWriteAdapterKey routine is called by the miniport driver to write the hardware or device registry adapter keys located in registry at HKLM/CurrentControlSet/Enum/&lt;Instance path&gt;/DeviceParameters/... |
| [StorPortReleaseMSISpinLock](nf-storport-storportreleasemsispinlock.md) | The StorPortReleaseMSISpinLock routine releases a previously acquired message signaled interrupt (MSI) spin lock for the specified message. |
| [StorPortReleaseSpinLock](nf-storport-storportreleasespinlock.md) | The StorPortReleaseSpinLock routine releases a spinlock acquired by StorPortAcquireSpinLock. |
| [StorPortRequestTimer](nf-storport-storportrequesttimer.md) | Schedules a callback event for a Storport timer context object. |
| [StorPortResume](nf-storport-storportresume.md) | The StorPortResume routine resumes a paused adapter. |
| [StorPortResumeDevice](nf-storport-storportresumedevice.md) | The StorPortResumeDevice routine resumes a previously paused logical unit. |
| [StorPortSetAdapterBusType](nf-storport-storportsetadapterbustype.md) | Used to adjust the BusType of the adapter depending on its current configuration. |
| [StorPortSetBusDataByOffset](nf-storport-storportsetbusdatabyoffset.md) | The StorPortSetBusDataByOffset routine writes bus-specific configuration information. |
| [StorPortSetDeviceQueueDepth](nf-storport-storportsetdevicequeuedepth.md) | The StorPortSetDeviceQueueDepth routine sets the maximum depth of the device queue for the indicated device. |
| [StorPortSetPowerSettingNotificationGuids](nf-storport-storportsetpowersettingnotificationguids.md) | The StorPortSetPowerSettingNotificationGuids routine enables a miniport to receive power setting notifications. The miniport registers an array of GUIDs which identify the power settings to receive power change notifications for. |
| [StorPortSetUnitAttributes](nf-storport-storportsetunitattributes.md) | The StorPortSetUnitAttributes routine registers the power attributes of a storage unit device with the Storport driver. |
| [StorPortStallExecution](nf-storport-storportstallexecution.md) | The StorPortStallExecution routine stalls the miniport driver. |
| [StorPortStateChangeDetected](nf-storport-storportstatechangedetected.md) | Notifies the Storport port driver of a state change for a logical unit number (LUN), host bus adapter (HBA) port, or target device. |
| [StorPortSynchronizeAccess](nf-storport-storportsynchronizeaccess.md) | The StorPortSynchronizeAccess routine provides synchronized access to a miniport driver's device extension. |
| [StorPortUpdateAdapterMaxIO](nf-storport-storportupdateadaptermaxio.md) | This function can be called by a miniport to update the maximum IO's supported by an adapter. This function is valid during HwInitialize/HwPassiveInitRoutine callback and has effect only during adapter initialization. |
| [StorPortValidateRange](nf-storport-storportvalidaterange.md) | The StorPortValidateRange routine determines whether a specified range of I/O addresses is in use by another adapter. This routine is obsolete in Windows NT 4.0 and later operating systems. |
| [StorPortWritePortBufferUchar](nf-storport-storportwriteportbufferuchar.md) | The StorPortWritePortBufferUchar routine writes a value to a specified register address. |
| [StorPortWritePortBufferUlong](nf-storport-storportwriteportbufferulong.md) | The StorPortWritePortBufferUlong routine writes a value to a specified register address. |
| [StorPortWritePortBufferUshort](nf-storport-storportwriteportbufferushort.md) | The StorPortWritePortBufferUshort routine writes a value to a specified register address. |
| [StorPortWritePortUchar](nf-storport-storportwriteportuchar.md) | The StorPortWritePortUchar routine writes a value to a specified register address. |
| [StorPortWritePortUlong](nf-storport-storportwriteportulong.md) | The StorPortWritePortUlong routine writes a value to a specified register address. |
| [StorPortWritePortUshort](nf-storport-storportwriteportushort.md) | The StorPortWritePortUshort routine writes a value to a specified register address. |
| [StorPortWriteRegisterBufferUchar](nf-storport-storportwriteregisterbufferuchar.md) | The StorPortWriteRegisterBufferUchar routine transfers a given number of unsigned bytes from a buffer to the HBA. |
| [StorPortWriteRegisterBufferUlong](nf-storport-storportwriteregisterbufferulong.md) | The StorPortWriteRegisterBufferUlong routine transfers a given number of ULONG values from a buffer to the HBA. |
| [StorPortWriteRegisterBufferUlong64](nf-storport-storportwriteregisterbufferulong64.md) | This StorPortWriteRegisterBufferUlong64 routine writes a number of ULONG64 values from a the specified 64-bit register address. |
| [StorPortWriteRegisterBufferUshort](nf-storport-storportwriteregisterbufferushort.md) | The StorPortWriteRegisterBufferUshort routine transfers a given number of USHORT values from a buffer to the HBA. |
| [StorPortWriteRegisterUchar](nf-storport-storportwriteregisteruchar.md) | The StorPortWriteRegisterBufferUshort routine transfers a given number of character values from a buffer to the indicated HBA register address. |
| [StorPortWriteRegisterUlong](nf-storport-storportwriteregisterulong.md) | The StorPortWriteRegisterUlong routine transfers a ULONG value to the indicated HBA register address. |
| [StorPortWriteRegisterUlong64](nf-storport-storportwriteregisterulong64.md) | This StorPortWriteRegisterUlong64 routine writes a ULONG64 value to the specified register address. |
| [StorPortWriteRegisterUshort](nf-storport-storportwriteregisterushort.md) | The StorPortWriteRegisterUshort routine transfers a ULONG value to the indicated HBA register address. |



## Structures
| Title | Description |
| ---- |:---- |
| [_HW_INITIALIZATION_DATA](ns-storport-_hw_initialization_data.md) | The HW_INITIALIZATION_DATA (Storport) structure contains information particular to each miniport driver and the hardware that the miniport driver manages. |
| [_MEMORY_REGION](ns-storport-_memory_region.md) | The MEMORY_REGION structure describes a region of physically contiguous memory. |
| [_MESSAGE_INTERRUPT_INFORMATION](ns-storport-_message_interrupt_information.md) | The MESSAGE_INTERRUPT_INFORMATION structure describes a message signaled interrupt (MSI). |
| [_MINIPORT_DUMP_POINTERS](ns-storport-_miniport_dump_pointers.md) | A Storport miniport driver uses this structure to support the SCSI_REQUEST_BLOCK (SRB) function code SRB_FUNCTION_DUMP_POINTERS. |
| [_PERF_CONFIGURATION_DATA](ns-storport-_perf_configuration_data.md) | The PERF_CONFIGURATION_DATA structure describes the performance optimizations that are supported by the StorPortInitializePerfOpts routine. |
| [_REPORT_ZONES_DATA](ns-storport-_report_zones_data.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [_SCSI_PNP_REQUEST_BLOCK](ns-storport-_scsi_pnp_request_block.md) | TheSCSI_PNP_REQUEST_BLOCK structure is a special version of a SCSI_REQUEST_BLOCK that is used for plug and play (PNP) requests.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [_SCSI_POWER_REQUEST_BLOCK](ns-storport-_scsi_power_request_block.md) | The SCSI_POWER_REQUEST_BLOCK structure is a special version of a SCSI_REQUEST_BLOCK that is used for power management requests.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [_SCSI_WMI_REQUEST_BLOCK](ns-storport-_scsi_wmi_request_block.md) | This structure is a special version of a SCSI_REQUEST_BLOCK for use with WMI commands. |
| [_SES_CONFIGURATION_DIAGNOSTIC_PAGE](ns-storport-_ses_configuration_diagnostic_page.md) | TBD. |
| [_SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE](ns-storport-_ses_download_microcode_control_diagnostic_page.md) | The SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure contains a vendor specific microcode (i.e., firmware) image for use by the enclosure services process. |
| [_SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR](ns-storport-_ses_download_microcode_status_descriptor.md) | The SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure specifies the status and additional status of a download microcode. |
| [_SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE](ns-storport-_ses_download_microcode_status_diagnostic_page.md) | The Download Microcode Status diagnostic page includes information about the status of one or more download microcode operations. |
| [_SRBEX_DATA](ns-storport-_srbex_data.md) | The SRBEX_DATA structure is the generalized format for containing extended SRB data. |
| [_SRBEX_DATA_BIDIRECTIONAL](ns-storport-_srbex_data_bidirectional.md) | The SRBEX_DATA_BIDIRECTIONAL structure contains the extended SRB data for bi-directional transfer commands. |
| [_SRBEX_DATA_IO_INFO](ns-storport-_srbex_data_io_info.md) | The SRBEX_DATA_IO_INFO structure contains additional information related to a read or write request in an extended SRB. |
| [_SRBEX_DATA_PNP](ns-storport-_srbex_data_pnp.md) | The SRBEX_DATA_PNP structure contains the request data for an extended plug and play (PNP) SRB. |
| [_SRBEX_DATA_POWER](ns-storport-_srbex_data_power.md) | The SRBEX_DATA_POWER structure contains the request data for an extended power SRB. |
| [_SRBEX_DATA_SCSI_CDB_VAR](ns-storport-_srbex_data_scsi_cdb_var.md) | The SRBEX_DATA_SCSI_CDB_VAR structure contains the extended SRB data for a variable length SCSI command data block (CDB). |
| [_SRBEX_DATA_SCSI_CDB16](ns-storport-_srbex_data_scsi_cdb16.md) | The SRBEX_DATA_SCSI_CDB16 structure contains the extended SRB data for a 16-byte SCSI command data block (CDB). |
| [_SRBEX_DATA_SCSI_CDB32](ns-storport-_srbex_data_scsi_cdb32.md) | The SRBEX_DATA_SCSI_CDB32 structure contains the extended SRB data for a 32-byte SCSI command data block (CDB). |
| [_SRBEX_DATA_WMI](ns-storport-_srbex_data_wmi.md) | The SRBEX_DATA_WMI structure contains the request data for an extended WMI SRB. |
| [_STARTIO_PERFORMANCE_PARAMETERS](ns-storport-_startio_performance_parameters.md) | The STARTIO_PERFORMANCE_PARAMETERS structure describes the performance parameters that are returned to the miniport driver by the StorPortGetStartIoPerfParams routine. |
| [_STOR_ADDR_BTL8](ns-storport-_stor_addr_btl8.md) | The STOR_ADDR_BTL8 address structure contains the addressing information for an 8-bit Bus-Target-LUN (BTL8) address. |
| [_STOR_ADDRESS](ns-storport-_stor_address.md) | A general structure for holding a storage device address. |
| [_STOR_CRYPTO_CAPABILITIES_DATA](ns-storport-_stor_crypto_capabilities_data.md) | Reserved for system use. |
| [_STOR_CRYPTO_CAPABILITY](ns-storport-_stor_crypto_capability.md) | Reserved for system use. |
| [_STOR_CRYPTO_KEY_INFO](ns-storport-_stor_crypto_key_info.md) | Reserved for system use. |
| [_STOR_CRYPTO_OPERATION_INSERT_KEY](ns-storport-_stor_crypto_operation_insert_key.md) | Reserved for system use. |
| [_STOR_DEVICE_CAPABILITIES](ns-storport-_stor_device_capabilities.md) | The STOR_DEVICE_CAPABILITIES structure reports device capabilities to the Storport driver in response to a capabilities query in a SCSI request block (SRB) with a function of SRB_FUNCTION_PNP. |
| [_STOR_DEVICE_CAPABILITIES_EX](ns-storport-_stor_device_capabilities_ex.md) | The STOR_DEVICE_CAPABILITIES_EX structure reports device capabilities to the Storport driver in response to a capabilities query in a SCSI request block (SRB) with a function of SRB_FUNCTION_PNP. |
| [_STOR_DPC](ns-storport-_stor_dpc.md) | The STOR_DPC structure is an opaque structure that represents a DPC object. Do not set the members of this structure directly. |
| [_STOR_LIST_ENTRY](ns-storport-_stor_list_entry.md) | A STOR_LIST_ENTRY structure describes an entry in a doubly linked list or serves as the header for such a list. |
| [_STOR_LOG_EVENT_DETAILS](ns-storport-_stor_log_event_details.md) | The STOR_LOG_EVENT_DETAILS structure provides details pertaining to Storport-specific error log events and system log events. |
| [_STOR_POFX_COMPONENT](ns-storport-_stor_pofx_component.md) | The STOR_POFX_COMPONENT structure describes the power state attributes of a storage device component. |
| [_STOR_POFX_COMPONENT_IDLE_STATE](ns-storport-_stor_pofx_component_idle_state.md) | The STOR_POFX_COMPONENT_IDLE_STATE structure specifies the attributes of an functional power state (F-state) of a component in a storage device. |
| [_STOR_POFX_COMPONENT_V2](ns-storport-_stor_pofx_component_v2.md) | The STOR_POFX_COMPONENT_V2 structure describes the power state attributes of a storage device component. |
| [_STOR_POFX_DEVICE](ns-storport-_stor_pofx_device.md) | The STOR_POFX_DEVICE structure describes the power attributes of a storage device to the power management framework (PoFx). |
| [_STOR_POFX_DEVICE_V2](ns-storport-_stor_pofx_device_v2.md) | The STOR_POFX_DEVICE_V2 structure describes the power attributes of a storage device to the power management framework (PoFx). |
| [_STOR_POFX_DEVICE_V3](ns-storport-_stor_pofx_device_v3.md) | The STOR_POFX_DEVICE_V3 structure describes the power attributes of a storage device to the power management framework (PoFx). |
| [_STOR_REQUEST_INFO_V1](ns-storport-_stor_request_info_v1.md) | The _STOR_REQUEST_INFO_V1 structure contains details about the storage driver IO request associated with a SCSI request block (SRB). _STOR_REQUEST_INFO_V1 is returned by the StorPortGetRequestInfo routine. |
| [_STOR_RICH_DEVICE_DESCRIPTION](ns-storport-_stor_rich_device_description.md) | The STOR_RICH_DEVICE_DESCRIPTION structure describes the attributes of the physical device for which a driver is requesting a DMA (direct memory access) adapter. |
| [_STOR_SCATTER_GATHER_ELEMENT](ns-storport-_stor_scatter_gather_element.md) | The STOR_SCATTER_GATHER_ELEMENT structure is used with STOR_SCATTER_GATHER_LIST to build a list of scatter/gather elements. |
| [_STOR_SCATTER_GATHER_LIST](ns-storport-_stor_scatter_gather_list.md) | The STOR_SCATTER_GATHER_LIST structure is used in conjunction with the StorPortGetScatterGatherList routine to retrieve the scatter/gather list for a SCSI request block (SRB). |
| [_STOR_UNIT_ATTRIBUTES](ns-storport-_stor_unit_attributes.md) | The STOR_UNIT_ATTRIBUTES structure contains bitfields indicating attribute support for a storage device unit. |
| [_STORAGE_REQUEST_BLOCK](ns-storport-_storage_request_block.md) | The STORAGE_REQUEST_BLOCK is the extended format SCSI Request Block (SRB) structure. |
| [_STORPORT_TELEMETRY_EVENT](ns-storport-_storport_telemetry_event.md) | The STORPORT_TELEMETRY_EVENT structure describes the miniport telemetry data payload. |
| [_VIRTUAL_HW_INITIALIZATION_DATA](ns-storport-_virtual_hw_initialization_data.md) | The VIRTUAL_HW_INITIALIZATION_DATA structure contains information particular to each virtual miniport driver. |
| [_VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE](ns-storport-_vpd_zoned_block_device_characteristics_page.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [_ZONE_DESCRIPTIOR](ns-storport-_zone_descriptior.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [PRI_REGISTRATION_LIST](ns-storport-pri_registration_list.md) | The PRI_REGISTRATION_LIST structure is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION_ACTION_READ_KEYS. |
| [PRI_RESERVATION_DESCRIPTOR](ns-storport-pri_reservation_descriptor.md) | The PRI_RESERVATION_DESCRIPTOR structure is used to construct the PRI_RESERVATION_LIST structure that is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION_ACTION_READ_RESERVATIONS. |
| [PRI_RESERVATION_LIST](ns-storport-pri_reservation_list.md) | The PRI_RESERVATION_LIST structure is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION_ACTION_READ_RESERVATIONS. |
| [PRO_PARAMETER_LIST](ns-storport-pro_parameter_list.md) | The PRO_PARAMETER_LIST structure is sent in a Persistent Reserve Out command to a device server. |
| [RT_PARAMETER_DATA](ns-storport-rt_parameter_data.md) | The RT_PARAMETER_DATA structure contains the parameter data for the report timestamp command. |
| [ST_PARAMETER_DATA](ns-storport-st_parameter_data.md) | The ST_PARAMETER_DATA structure contains the parameter list for the set timestamp command. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_INTERRUPT_SYNCHRONIZATION_MODE](ne-storport-_interrupt_synchronization_mode.md) | The INTERRUPT_SYNCHRONIZATION_MODE enumerator specifies the interrupt synchronization mode. |
| [_SES_DOWNLOAD_MICROCODE_STATE](ne-storport-_ses_download_microcode_state.md) | TBD. |
| [_STOR_CRYPTO_ALGORITHM_ID](ne-storport-_stor_crypto_algorithm_id.md) | Reserved for system use. |
| [_STOR_CRYPTO_KEY_SIZE](ne-storport-_stor_crypto_key_size.md) | Reserved for system use. |
| [_STOR_CRYPTO_OPERATION_TYPE](ne-storport-_stor_crypto_operation_type.md) | Reserved for system use. |
| [_STOR_DEVICE_POWER_STATE](ne-storport-_stor_device_power_state.md) | The STOR_DEVICE_POWER_STATE enumerator specifies a device power state. |
| [_STOR_EVENT_ASSOCIATION_ENUM](ne-storport-_stor_event_association_enum.md) | The STOR_EVENT_ASSOCIATION_ENUM enumerator specifies the type of device that is associated with an event. |
| [_STOR_SPINLOCK](ne-storport-_stor_spinlock.md) | The STOR_SPINLOCK enumeration is used to specify the type of a spinlock. |
| [*PSTOR_POWER_ACTION](ne-storport-pstor_power_action.md) | The STOR_POWER_ACTION enumerator indicates the power state that the system is about to enter during a power transition. |