# Storport.h header


This header is used by Storage. For more information, see
- [Storage](../_storage/index.md)

Storport.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [StorPortAcquireMSISpinLock function](nf-storport-storportacquiremsispinlock.md) | The StorPortAcquireMSISpinLock routine acquires the message signaled interrupt (MSI) spin lock that is associated with the specified message. |
| [StorPortAcquireSpinLock function](nf-storport-storportacquirespinlock.md) | The StorPortAcquireSpinLock routine acquires the specified spin lock. |
| [StorPortAllocateContiguousMemorySpecifyCacheNode function](nf-storport-storportallocatecontiguousmemoryspecifycachenode.md) | The StorPortAllocateContiguousMemorySpecifyCacheNode routine allocates a range of physically contiguous noncached, nonpaged memory. |
| [StorPortAllocateHostMemoryBuffer function](nf-storport-storportallocatehostmemorybuffer.md) | This function allocates one or more ranges of physically contiguous memory to be used as a Host Memory Buffer (HMB). |
| [StorPortAllocateMdl function](nf-storport-storportallocatemdl.md) | The StorPortAllocateMdl routine allocates an MDL to describe the given non-paged pool memory. |
| [StorPortAllocatePool function](nf-storport-storportallocatepool.md) | The StorPortAllocatePool routine allocates a block of non-contiguous, non-paged pool memory. |
| [StorPortAllocateRegistryBuffer function](nf-storport-storportallocateregistrybuffer.md) | The StorPortAllocateRegistryBuffer routine is called by the miniport driver to allocate a buffer that can be used to read and write registry data. |
| [StorPortAsyncNotificationDetected function](nf-storport-storportasyncnotificationdetected.md) | A storage miniport driver calls StorPortAsyncNotificationDetected to notify the Storport driver of a storage device status change event. |
| [StorPortBuildMdlForNonPagedPool function](nf-storport-storportbuildmdlfornonpagedpool.md) | The StorPortBuildMdlForNonPagedPool routine updates the MDL to describe the associated non-paged memory. |
| [StorPortBuildScatterGatherList function](nf-storport-storportbuildscattergatherlist.md) | The StorPortBuildScatterGatherList routine creates a scatter/gather list for the specified data buffer. |
| [StorPortBusy function](nf-storport-storportbusy.md) | The StorPortBusy routine notifies the port driver that the adapter is currently busy, handling outstanding requests. |
| [StorPortCompleteRequest function](nf-storport-storportcompleterequest.md) | The StorPortCompleteRequest routine completes all outstanding requests setting the SRB status value to SrbStatus. |
| [StorPortCompleteServiceIrp function](nf-storport-storportcompleteserviceirp.md) | The StorPortCompleteServiceIrp routine is called by a Storport virtual miniport driver when it needs to complete a request that it received in its HwStorProcessServiceRequest callback routine. |
| [StorPortConvertUlongToPhysicalAddress function](nf-storport-storportconvertulongtophysicaladdress.md) | The StorPortConvertUlongToPhysicalAddress routine converts an unsigned long address into a physical address. |
| [StorPortDebugPrint function](nf-storport-storportdebugprint.md) | The StorPortDebugPrint routine prints a debug string to the kernel debugger, if the debugger is attached. |
| [StorPortDeviceBusy function](nf-storport-storportdevicebusy.md) | The StorPortDeviceBusy routine notifies the port driver that the specified logical unit is currently busy, handling outstanding requests. |
| [StorPortDeviceReady function](nf-storport-storportdeviceready.md) | The StorPortDeviceReady routine notifies the port driver that the indicated logical unit is ready to handle new requests. |
| [StorPortEnablePassiveInitialization function](nf-storport-storportenablepassiveinitialization.md) | The StorPortEnablePassiveInitialization routine enables the miniport's HwStorPassiveInitializeRoutine callback routine to execute at PASSIVE_LEVEL during miniport initialization. |
| [StorPortEtwEvent2 function](nf-storport-storportetwevent2.md) | The StorPortEtwEvent2 publishes an Event Tracing for Windows (ETW) event to a storage trace channel. The miniport can log two general purpose ETW parameters. The ETW parameters are expressed as two name-value pairs. |
| [StorPortEtwEvent4 function](nf-storport-storportetwevent4.md) | The StorPortEtwEvent4 publishes an Event Tracing for Windows (ETW) event to a storage trace channel. The miniport can log four general purpose ETW parameters. The ETW parameters are expressed as four name-value pairs. |
| [StorPortEtwEvent8 function](nf-storport-storportetwevent8.md) | The StorPortEtwEvent8 publishes an Event Tracing for Windows (ETW) event to a storage trace channel. The miniport can log eight general purpose ETW parameters. The ETW parameters are expressed as eight name-value pairs. |
| [StorPortFreeContiguousMemorySpecifyCache function](nf-storport-storportfreecontiguousmemoryspecifycache.md) | The StorPortFreeContiguousMemorySpecifyCache routine deallocates a range of noncached memory in the nonpaged portion of the system address space. |
| [StorPortFreeDeviceBase function](nf-storport-storportfreedevicebase.md) | StorPortFreeDeviceBase frees a range of device I/O memory that was mapped by StorPortGetDeviceBase. |
| [StorPortFreeHostMemoryBuffer function](nf-storport-storportfreehostmemorybuffer.md) | The StorPortFreeHostMemoryBuffer routine frees the physically contiguous memory that was allocated to be used for a Host Memory Buffer (HMB). |
| [StorPortFreeMdl function](nf-storport-storportfreemdl.md) | The StorPortFreeMdl routine frees a memory descriptor list (MDL) describing non-paged pool memory. |
| [StorPortFreePool function](nf-storport-storportfreepool.md) | The StorPortFreePool routine frees a block of memory that was previously allocated by a call to the StorPortAllocatePool routine. |
| [StorPortFreeRegistryBuffer function](nf-storport-storportfreeregistrybuffer.md) | The StorPortFreeRegistryBuffer routine frees the buffer that was allocated for storing registry data. |
| [StorPortFreeTimer function](nf-storport-storportfreetimer.md) | Frees a Storport timer context object previously created by the StorPortInitializeTimer routine. |
| [StorPortFreeWorker function](nf-storport-storportfreeworker.md) | Frees a Storport work item previously allocated by the StorPortInitializeWorker routine. |
| [StorPortGetActiveGroupCount function](nf-storport-storportgetactivegroupcount.md) | The StorPortGetActiveGroupCount routine returns the number of processor groups that are present in the system. |
| [StorPortGetActiveNodeCount function](nf-storport-storportgetactivenodecount.md) | The StorPortGetActiveNodeCount routine returns the number of nodes that are present in the system. |
| [StorPortGetActivityIdSrb function](nf-storport-storportgetactivityidsrb.md) | Retrieves the Event Tracing for Windows (ETW) activity ID associated with a request block. |
| [StorPortGetBusData function](nf-storport-storportgetbusdata.md) | The StorPortGetBusData routine retrieves the bus-specific configuration information necessary to initialize the HBA. |
| [StorPortGetCurrentProcessorNumber function](nf-storport-storportgetcurrentprocessornumber.md) | The StorPortGetCurrentProcessorNumber routine retrieves the current processor number from the kernel. |
| [StorPortGetDataInBufferMdl function](nf-storport-storportgetdatainbuffermdl.md) | Returns an MDL associated with the input data buffer of a SCSI request block (SRB). |
| [StorPortGetDataInBufferScatterGatherList function](nf-storport-storportgetdatainbufferscattergatherlist.md) | Returns the scatter-gather list associated with the input data buffer of a SCSI request block (SRB). |
| [StorPortGetDataInBufferSystemAddress function](nf-storport-storportgetdatainbuffersystemaddress.md) | Returns the system address for the input data buffer of a SCSI request block (SRB). |
| [StorPortGetDeviceBase function](nf-storport-storportgetdevicebase.md) | The StorPortGetDeviceBase routine maps an I/O address to system address space. |
| [StorPortGetDeviceObjects function](nf-storport-storportgetdeviceobjects.md) | The StorPortGetDeviceObjects routine returns the device objects that are associated with the adapter device stack. |
| [StorPortGetGroupAffinity function](nf-storport-storportgetgroupaffinity.md) | The StorPortGetGroupAffinity routine constructs a mask of the active processors in a requested group. |
| [StorPortGetHighestNodeNumber function](nf-storport-storportgethighestnodenumber.md) | The StorPortGetHighestNodeNumber routine returns the largest possible node number on the system. |
| [StorPortGetLogicalProcessorRelationship function](nf-storport-storportgetlogicalprocessorrelationship.md) | The StorPortGetLogicalProcessorRelationship routine returns relationship information for one or more specified types. |
| [StorPortGetLogicalUnit function](nf-storport-storportgetlogicalunit.md) | The StorPortGetLogicalUnit routine returns a pointer to the miniport driver's per-logical-unit storage area. |
| [StorPortGetMSIInfo function](nf-storport-storportgetmsiinfo.md) | The StorPortGetMSIInfo routine retrieves the message signaled interrupt (MSI) information for the specified message. |
| [StorPortGetNodeAffinity function](nf-storport-storportgetnodeaffinity.md) | The StorPortGetNodeAffinity routine constructs a mask of the active processors in a requested non-uniform memory access (NUMA) node. |
| [StorPortGetOriginalMdl function](nf-storport-storportgetoriginalmdl.md) | The StorPortGetOriginalMdl routine returns the MDL associated with the given SRB. |
| [StorPortGetPfns function](nf-storport-storportgetpfns.md) | The StorPortGetPfns routine can be called when a miniport needs to retreive PFNs associated with a MDL for a SRB. |
| [StorPortGetPhysicalAddress function](nf-storport-storportgetphysicaladdress.md) | The StorPortGetPhysicalAddress routine converts a given virtual address range to a physical address range for a DMA operation. |
| [StorPortGetRequestCryptoInfo function](nf-storport-storportgetrequestcryptoinfo.md) | Reserved for system use. |
| [StorPortGetRequestInfo function](nf-storport-storportgetrequestinfo.md) | The StorPortGetRequestInfo routine retrieves the IO request information associated with a SCSI request block (SRB) and returns it in a STOR_REQUEST_INFO structure. |
| [StorPortGetScatterGatherList function](nf-storport-storportgetscattergatherlist.md) | The StorPortGetScatterGatherList routine retrieves the associated scatter/gather list for the specified SCSI request block (SRB). |
| [StorPortGetStartIoPerfParams function](nf-storport-storportgetstartioperfparams.md) | The StorPortGetStartIoPerfParams routine places the performance parameters for a given I/O request in a STARTIO_PERFORMANCE_PARAMETERS structure. |
| [StorPortGetSystemAddress function](nf-storport-storportgetsystemaddress.md) | The StorPortGetSystemAddress routine returns a virtual address in system space for the data buffer of the specified SCSI request block (SRB). |
| [StorPortGetSystemPortNumber function](nf-storport-storportgetsystemportnumber.md) | The StorPortGetSystemPortNumber routine retrieves the system assigned port number for a storage adapter. |
| [StorPortGetUncachedExtension function](nf-storport-storportgetuncachedextension.md) | The StorPortGetUncachedExtension routine allocates an uncached common buffer to be shared by the CPU and the device. |
| [StorPortGetVirtualAddress function](nf-storport-storportgetvirtualaddress.md) | The StorPortGetVirtualAddress routine obtains a virtual address that maps to the indicated physical address. |
| [StorPortInitialize function](nf-storport-storportinitialize.md) | The StorPortInitilize routine initializes the port driver parameters and extension data. StorPortInitilize also saves the adapter information provided from the miniport driver. |
| [StorPortInitializeCryptoEngine function](nf-storport-storportinitializecryptoengine.md) | Reserved for system use. |
| [StorPortInitializeDpc function](nf-storport-storportinitializedpc.md) | The StorPortInitializeDpc routine initializes a StorPort DPC. |
| [StorPortInitializeListHead function](nf-storport-storportinitializelisthead.md) | The StorPortInitializeListHead routine initializes a STOR_LIST_ENTRY structure that represents the head of a doubly linked list. |
| [StorPortInitializePerfOpts function](nf-storport-storportinitializeperfopts.md) | The StorPortInitializePerfOpts function initializes the performance optimizations that both the miniport driver and the Storport driver support using a PERF_CONFIGURATION_DATA structure. |
| [StorPortInitializePoFxPower function](nf-storport-storportinitializepofxpower.md) | A miniport driver calls StorPortInitializePoFxPower to register a storage device with the power management framework (PoFx). |
| [StorPortInitializeSListHead function](nf-storport-storportinitializeslisthead.md) | Initializes the head of a Storport managed singly linked list. |
| [StorPortInitializeSpinlock function](nf-storport-storportinitializespinlock.md) | The StorPortInitializeSpinLock routine initializes a variable of type STOR_KSPIN_LOCK. |
| [StorPortInitializeTimer function](nf-storport-storportinitializetimer.md) | Creates a Storport timer context object. |
| [StorPortInitializeWorker function](nf-storport-storportinitializeworker.md) | Creates a new Storport work item that runs in a system worker thread. |
| [StorPortInterlockedFlushSList function](nf-storport-storportinterlockedflushslist.md) | Removes all items from a Storport managed singly linked list. Access to the list is synchronized on a multiprocessor system. |
| [StorPortInterlockedInsertHeadList function](nf-storport-storportinterlockedinsertheadlist.md) | The StorPortInterlockedInsertHeadList routine atomically inserts an entry at the beginning of a doubly linked list of STOR_LIST_ENTRY structures. |
| [StorPortInterlockedInsertTailList function](nf-storport-storportinterlockedinserttaillist.md) | The StorPortInterlockedInsertTailList routine atomically inserts an entry at the end of a doubly linked list of STOR_LIST_ENTRY structures. |
| [StorPortInterlockedPopEntrySList function](nf-storport-storportinterlockedpopentryslist.md) | Removes an item from the front of a Storport managed singly linked list. Access to the list is synchronized on a multiprocessor system. Syntax. |
| [StorPortInterlockedPushEntrySList function](nf-storport-storportinterlockedpushentryslist.md) | Inserts an item at the front of a Storport managed singly linked list. Access to the list is synchronized on a multiprocessor system. |
| [StorPortInterlockedRemoveHeadList function](nf-storport-storportinterlockedremoveheadlist.md) | The StorPortInterlockedRemoveHeadList routine removes an entry from the beginning of a doubly linked list of STOR_LIST_ENTRY structures. |
| [StorPortInvokeAcpiMethod function](nf-storport-storportinvokeacpimethod.md) | The StorPortInvokeAcpiMethod routine executes an ACPI method for a storage device. |
| [StorPortIsCurrentOsInstallationUpgrade function](nf-storport-storportiscurrentosinstallationupgrade.md) | The StorPortIsCurrentOsInstallationUpgrade routine checks if the current installation of Windows is an upgrade from a previous version or not. |
| [StorPortIsDeviceOperationAllowed function](nf-storport-storportisdeviceoperationallowed.md) | A miniport driver can call the StorPortIsDeviceOperationAllowedminiport routine to determine if operations for a certain device management class are allowed. |
| [StorPortIssueDpc function](nf-storport-storportissuedpc.md) | The StorPortIssueDpc routine issues a deferred procedure call (DPC). |
| [StorPortLogError function](nf-storport-storportlogerror.md) | The StorPortLogError routine notifies the port driver that an error occurred. |
| [StorPortLogSystemEvent function](nf-storport-storportlogsystemevent.md) | The StorPortLogSystemEvent routine gives miniport drivers full access to the capabilities of the Windows kernel event facility, enabling miniport drivers to create event log entries that are truly useful in troubleshooting storage issues. |
| [StorPortLogTelemetry function](nf-storport-storportlogtelemetry.md) | The StorPortLogTelemetry routine logs a miniport telemetry event to help diagnose or collect any useful information. |
| [StorPortMarkDumpMemory function](nf-storport-storportmarkdumpmemory.md) | A miniport should mark memory used for the dump file or the hibernation file. |
| [StorPortMoveMemory function](nf-storport-storportmovememory.md) | The StorPortMoveMemory routine copies memory from one buffer to another. |
| [StorPortNotification function](nf-storport-storportnotification.md) | The miniport driver uses the StorPortNotification routine to notify the Storport driver of certain events and conditions. |
| [StorPortPause function](nf-storport-storportpause.md) | The StorPortPause routine pauses an adapter for the specified period of time. |
| [StorPortPauseDevice function](nf-storport-storportpausedevice.md) | The StorPortPauseDevice routine pauses a specific logical unit device for the specified period of time. |
| [StorPortPoFxActivateComponent function](nf-storport-storportpofxactivatecomponent.md) | The StorPortPoFxActivateComponent routine increments the activation reference count on the specified component of a storage device. |
| [StorPortPoFxIdleComponent function](nf-storport-storportpofxidlecomponent.md) | The StorPortPoFxIdleComponent routine decrements the activation reference count of a specified component of a storage device. |
| [StorPortPoFxPowerControl function](nf-storport-storportpofxpowercontrol.md) | The StorPortPoFxPowerControl routine sends a power control request to the power management framework (PoFx) to forward to the power engine plug-in (PEP). |
| [StorPortPoFxSetComponentLatency function](nf-storport-storportpofxsetcomponentlatency.md) | The StorPortPoFxSetComponentLatency routine specifies the maximum latency that can be tolerated in the transition from the idle condition to the active condition in the specified storage device component. |
| [StorPortPoFxSetComponentResidency function](nf-storport-storportpofxsetcomponentresidency.md) | The StorPortPoFxSetComponentResidency routine sets the estimated time for how long a storage device component is likely to remain idle after the component enters the idle condition. |
| [StorPortPutScatterGatherList function](nf-storport-storportputscattergatherlist.md) | The StorPortPutScatterGatherList routine releases any resources associated with a scatter/gather list that was previously created by a call to the StorPortBuildScatterGatherList routine. |
| [StorPortQueryDepthSList function](nf-storport-storportquerydepthslist.md) | Retrieves the number of entries in a Storport managed singly linked list. |
| [StorPortQueryPerformanceCounter function](nf-storport-storportqueryperformancecounter.md) | The current system performance counter value is queried is returned by the StorPortQueryPerformanceCounter routine. |
| [StorPortQuerySystemTime function](nf-storport-storportquerysystemtime.md) | The StoriPortQuerySystemTime routine obtains the current system time. |
| [StorPortQueueWorkItem function](nf-storport-storportqueueworkitem.md) | Schedules a Storport work item to execute within the context of a system worker thread. |
| [StorPortReadPortBufferUchar function](nf-storport-storportreadportbufferuchar.md) | The StorPortReadPortBufferUchar routine reads a value from a specified port address |
| [StorPortReadPortBufferUchar function](nf-storport-storportreadportbufferuchar~r1.md) | The StorPortReadPortBufferUchar routine reads a value from a specified port address |
| [StorPortReadPortBufferUlong function](nf-storport-storportreadportbufferulong.md) | The StorPortReadPortBufferUlong routine reads a value from a specified port address. |
| [StorPortReadPortBufferUlong function](nf-storport-storportreadportbufferulong~r1.md) | The StorPortReadPortBufferUlong routine reads a value from a specified port address. |
| [StorPortReadPortBufferUshort function](nf-storport-storportreadportbufferushort.md) | The StorPortReadPortBufferUshort routine reads a value from a specified port address. |
| [StorPortReadPortBufferUshort function](nf-storport-storportreadportbufferushort~r1.md) | The StorPortReadPortBufferUshort routine reads a value from a specified port address. |
| [StorPortReadPortUchar function](nf-storport-storportreadportuchar.md) | The StorPortReadPortUchar routine reads a value from a specified port address |
| [StorPortReadPortUchar function](nf-storport-storportreadportuchar~r1.md) | The StorPortReadPortUchar routine reads a value from a specified port address |
| [StorPortReadPortUlong function](nf-storport-storportreadportulong.md) | The StorPortReadPortUlong routine reads a value from a specified port address. |
| [StorPortReadPortUlong function](nf-storport-storportreadportulong~r1.md) | The StorPortReadPortUlong routine reads a value from a specified port address. |
| [StorPortReadPortUshort function](nf-storport-storportreadportushort.md) | The StorPortReadPortUshort routine reads a value from a specified port address. |
| [StorPortReadPortUshort function](nf-storport-storportreadportushort~r1.md) | The StorPortReadPortUshort routine reads a value from a specified port address. |
| [StorPortReadRegisterBufferUchar function](nf-storport-storportreadregisterbufferuchar.md) | The StorPortReadRegisterBufferUchar routine reads a value from a specified register address. |
| [StorPortReadRegisterBufferUchar function](nf-storport-storportreadregisterbufferuchar~r1.md) | The StorPortReadRegisterBufferUchar routine reads a value from a specified register address. |
| [StorPortReadRegisterBufferUlong function](nf-storport-storportreadregisterbufferulong.md) | The StorPortReadRegisterBufferUlong routine reads a value from a specified register address. |
| [StorPortReadRegisterBufferUlong function](nf-storport-storportreadregisterbufferulong~r1.md) | The StorPortReadRegisterBufferUlong routine reads a value from a specified register address. |
| [StorPortReadRegisterBufferUlong64 function](nf-storport-storportreadregisterbufferulong64.md) | This StorPortReadRegisterBufferUlong64 routine reads a number of ULONG64 values from the specified 64-bit register address into a buffer. |
| [StorPortReadRegisterBufferUshort function](nf-storport-storportreadregisterbufferushort.md) | The StorPortReadRegisterBufferUshort routine reads a value from a specified register address. |
| [StorPortReadRegisterBufferUshort function](nf-storport-storportreadregisterbufferushort~r1.md) | The StorPortReadRegisterBufferUshort routine reads a value from a specified register address. |
| [StorPortReadRegisterUchar function](nf-storport-storportreadregisteruchar.md) | The StorPortReadRegisterUchar routine reads a value from a specified register address. |
| [StorPortReadRegisterUchar function](nf-storport-storportreadregisteruchar~r1.md) | The StorPortReadRegisterUchar routine reads a value from a specified register address. |
| [StorPortReadRegisterUlong function](nf-storport-storportreadregisterulong.md) | The StorPortReadRegisterUlong routine reads a value from a specified register address. |
| [StorPortReadRegisterUlong function](nf-storport-storportreadregisterulong~r1.md) | The StorPortReadRegisterUlong routine reads a value from a specified register address. |
| [StorPortReadRegisterUlong64 function](nf-storport-storportreadregisterulong64.md) | The StorPortReadRegisterUlong64 routine reads a 64-bit value from a specified 64-bit register address. |
| [StorPortReadRegisterUshort function](nf-storport-storportreadregisterushort.md) | The StorPortReadRegisterUshort routine reads a value from a specified register address. |
| [StorPortReadRegisterUshort function](nf-storport-storportreadregisterushort~r1.md) | The StorPortReadRegisterUshort routine reads a value from a specified register address. |
| [StorPortReady function](nf-storport-storportready.md) | The StorPortReady routine notifies the port driver that the adapter is no longer busy. |
| [StorPortRegistryRead function](nf-storport-storportregistryread.md) | The StorPortRegistryRead routine reads the registry data for the indicated device and value. |
| [StorPortRegistryReadAdapterKey function](nf-storport-storportregistryreadadapterkey.md) | The StorPortRegistryReadAdapterKey routine is called by the miniport driver to read the hardware or device registry adapter keys located in registry at HKLM/CurrentControlSet/Enum/&lt;Instance path&gt;/DeviceParameters/... |
| [StorPortRegistryWrite function](nf-storport-storportregistrywrite.md) | The StorPortRegistryWrite routine is called by the miniport driver to convert the registry data contained in a specified buffer from ASCII to Unicode and to then write the data to the miniport driver's per-HBA storage area. |
| [StorPortRegistryWriteAdapterKey function](nf-storport-storportregistrywriteadapterkey.md) | The StorPortRegistryWriteAdapterKey routine is called by the miniport driver to write the hardware or device registry adapter keys located in registry at HKLM/CurrentControlSet/Enum/&lt;Instance path&gt;/DeviceParameters/... |
| [StorPortReleaseMSISpinLock function](nf-storport-storportreleasemsispinlock.md) | The StorPortReleaseMSISpinLock routine releases a previously acquired message signaled interrupt (MSI) spin lock for the specified message. |
| [StorPortReleaseSpinLock function](nf-storport-storportreleasespinlock.md) | The StorPortReleaseSpinLock routine releases a spinlock acquired by StorPortAcquireSpinLock. |
| [StorPortRequestTimer function](nf-storport-storportrequesttimer.md) | Schedules a callback event for a Storport timer context object. |
| [StorPortResume function](nf-storport-storportresume.md) | The StorPortResume routine resumes a paused adapter. |
| [StorPortResumeDevice function](nf-storport-storportresumedevice.md) | The StorPortResumeDevice routine resumes a previously paused logical unit. |
| [StorPortSetAdapterBusType function](nf-storport-storportsetadapterbustype.md) | Used to adjust the BusType of the adapter depending on its current configuration. |
| [StorPortSetBusDataByOffset function](nf-storport-storportsetbusdatabyoffset.md) | The StorPortSetBusDataByOffset routine writes bus-specific configuration information. |
| [StorPortSetDeviceQueueDepth function](nf-storport-storportsetdevicequeuedepth.md) | The StorPortSetDeviceQueueDepth routine sets the maximum depth of the device queue for the indicated device. |
| [StorPortSetPowerSettingNotificationGuids function](nf-storport-storportsetpowersettingnotificationguids.md) | The StorPortSetPowerSettingNotificationGuids routine enables a miniport to receive power setting notifications. The miniport registers an array of GUIDs which identify the power settings to receive power change notifications for. |
| [StorPortSetUnitAttributes function](nf-storport-storportsetunitattributes.md) | The StorPortSetUnitAttributes routine registers the power attributes of a storage unit device with the Storport driver. |
| [StorPortStallExecution function](nf-storport-storportstallexecution.md) | The StorPortStallExecution routine stalls the miniport driver. |
| [StorPortStateChangeDetected function](nf-storport-storportstatechangedetected.md) | Notifies the Storport port driver of a state change for a logical unit number (LUN), host bus adapter (HBA) port, or target device. |
| [StorPortSynchronizeAccess function](nf-storport-storportsynchronizeaccess.md) | The StorPortSynchronizeAccess routine provides synchronized access to a miniport driver's device extension. |
| [StorPortUpdateAdapterMaxIO function](nf-storport-storportupdateadaptermaxio.md) | This function can be called by a miniport to update the maximum IO's supported by an adapter. This function is valid during HwInitialize/HwPassiveInitRoutine callback and has effect only during adapter initialization. |
| [StorPortValidateRange function](nf-storport-storportvalidaterange.md) | The StorPortValidateRange routine determines whether a specified range of I/O addresses is in use by another adapter. This routine is obsolete in Windows NT 4.0 and later operating systems. |
| [StorPortWritePortBufferUchar function](nf-storport-storportwriteportbufferuchar.md) | The StorPortWritePortBufferUchar routine writes a value to a specified register address. |
| [StorPortWritePortBufferUchar function](nf-storport-storportwriteportbufferuchar~r1.md) | The StorPortWritePortBufferUchar routine writes a value to a specified register address. |
| [StorPortWritePortBufferUlong function](nf-storport-storportwriteportbufferulong.md) | The StorPortWritePortBufferUlong routine writes a value to a specified register address. |
| [StorPortWritePortBufferUlong function](nf-storport-storportwriteportbufferulong~r1.md) | The StorPortWritePortBufferUlong routine writes a value to a specified register address. |
| [StorPortWritePortBufferUshort function](nf-storport-storportwriteportbufferushort.md) | The StorPortWritePortBufferUshort routine writes a value to a specified register address. |
| [StorPortWritePortBufferUshort function](nf-storport-storportwriteportbufferushort~r1.md) | The StorPortWritePortBufferUshort routine writes a value to a specified register address. |
| [StorPortWritePortUchar function](nf-storport-storportwriteportuchar.md) | The StorPortWritePortUchar routine writes a value to a specified register address. |
| [StorPortWritePortUchar function](nf-storport-storportwriteportuchar~r1.md) | The StorPortWritePortUchar routine writes a value to a specified register address. |
| [StorPortWritePortUlong function](nf-storport-storportwriteportulong.md) | The StorPortWritePortUlong routine writes a value to a specified register address. |
| [StorPortWritePortUlong function](nf-storport-storportwriteportulong~r1.md) | The StorPortWritePortUlong routine writes a value to a specified register address. |
| [StorPortWritePortUshort function](nf-storport-storportwriteportushort.md) | The StorPortWritePortUshort routine writes a value to a specified register address. |
| [StorPortWritePortUshort function](nf-storport-storportwriteportushort~r1.md) | The StorPortWritePortUshort routine writes a value to a specified register address. |
| [StorPortWriteRegisterBufferUchar function](nf-storport-storportwriteregisterbufferuchar.md) | The StorPortWriteRegisterBufferUchar routine transfers a given number of unsigned bytes from a buffer to the HBA. |
| [StorPortWriteRegisterBufferUchar function](nf-storport-storportwriteregisterbufferuchar~r1.md) | The StorPortWriteRegisterBufferUchar routine transfers a given number of unsigned bytes from a buffer to the HBA. |
| [StorPortWriteRegisterBufferUlong function](nf-storport-storportwriteregisterbufferulong.md) | The StorPortWriteRegisterBufferUlong routine transfers a given number of ULONG values from a buffer to the HBA. |
| [StorPortWriteRegisterBufferUlong function](nf-storport-storportwriteregisterbufferulong~r1.md) | The StorPortWriteRegisterBufferUlong routine transfers a given number of ULONG values from a buffer to the HBA. |
| [StorPortWriteRegisterBufferUlong64 function](nf-storport-storportwriteregisterbufferulong64.md) | This StorPortWriteRegisterBufferUlong64 routine writes a number of ULONG64 values from a the specified 64-bit register address. |
| [StorPortWriteRegisterBufferUshort function](nf-storport-storportwriteregisterbufferushort.md) | The StorPortWriteRegisterBufferUshort routine transfers a given number of USHORT values from a buffer to the HBA. |
| [StorPortWriteRegisterBufferUshort function](nf-storport-storportwriteregisterbufferushort~r1.md) | The StorPortWriteRegisterBufferUshort routine transfers a given number of USHORT values from a buffer to the HBA. |
| [StorPortWriteRegisterUchar function](nf-storport-storportwriteregisteruchar.md) | The StorPortWriteRegisterBufferUshort routine transfers a given number of character values from a buffer to the indicated HBA register address. |
| [StorPortWriteRegisterUchar function](nf-storport-storportwriteregisteruchar~r1.md) | The StorPortWriteRegisterBufferUshort routine transfers a given number of character values from a buffer to the indicated HBA register address. |
| [StorPortWriteRegisterUlong function](nf-storport-storportwriteregisterulong.md) | The StorPortWriteRegisterUlong routine transfers a ULONG value to the indicated HBA register address. |
| [StorPortWriteRegisterUlong function](nf-storport-storportwriteregisterulong~r1.md) | The StorPortWriteRegisterUlong routine transfers a ULONG value to the indicated HBA register address. |
| [StorPortWriteRegisterUlong64 function](nf-storport-storportwriteregisterulong64.md) | This StorPortWriteRegisterUlong64 routine writes a ULONG64 value to the specified register address. |
| [StorPortWriteRegisterUshort function](nf-storport-storportwriteregisterushort.md) | The StorPortWriteRegisterUshort routine transfers a ULONG value to the indicated HBA register address. |
| [StorPortWriteRegisterUshort function](nf-storport-storportwriteregisterushort~r1.md) | The StorPortWriteRegisterUshort routine transfers a ULONG value to the indicated HBA register address. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [HW_ADAPTER_CONTROL callback](nc-storport-hw-adapter-control.md) | A miniport driver's HwStorAdapterControl routine is called to perform synchronous operations to control the state or behavior of an adapter, such as stopping or restarting the HBA for power management. |
| [HW_BUILDIO callback](nc-storport-hw-buildio.md) | The HwStorBuildIo routine processes the SRB with unsynchronized access to shared system data structures before passing it to HwStorStartIo. |
| [HW_CLEANUP_TRACING callback](nc-storport-hw-cleanup-tracing.md) | The HwStorCleanupTracing callback routine allows the Storport virtual miniport driver to stop tracing and to free any related resources. |
| [HW_COMPLETE_SERVICE_IRP callback](nc-storport-hw-complete-service-irp.md) | The HwStorCompleteServiceIrp routine is called when the virtual adapter is being removed. When this happens, the Storport virtual miniport can complete any reverse-callback IRPs received in HwStorCompleteServiceIrp. |
| [HW_DPC_ROUTINE callback](nc-storport-hw-dpc-routine.md) | The HwStorDpcRoutine routine is a routine that is deferred for execution at DISPATCH IRQL by means of the deferred procedure call (DPC) mechanism. |
| [HW_FIND_ADAPTER callback](nc-storport-hw-find-adapter.md) | The HwStorFindAdapter routine uses the supplied configuration to determine whether a specific HBA is supported and, if it is, to return configuration information about that adapter. |
| [HW_FREE_ADAPTER_RESOURCES callback](nc-storport-hw-free-adapter-resources.md) | The HwStorFreeAdapterResources callback routine allows the Storport virtual miniport driver to free resources when the virtual adapter is being removed. This is the last callback routine for the adapter. |
| [HW_INITIALIZE callback](nc-storport-hw-initialize.md) | The HwStorInitialize routine initializes the miniport driver after a system reboot or power failure occurs. |
| [HW_INITIALIZE_TRACING callback](nc-storport-hw-initialize-tracing.md) | The HwStorInitializeTracing callback routine allows the Storport virtual miniport driver to set up tracing and any related resources. |
| [HW_INTERRUPT callback](nc-storport-hw-interrupt.md) | The Storport driver calls the HwStorInterrupt routine after the HBA generates an interrupt request. |
| [HW_MESSAGE_SIGNALED_INTERRUPT_ROUTINE callback](nc-storport-hw-message-signaled-interrupt-routine.md) | The HwMSInterruptRoutine routine handles a message signaled interrupt (MSI). |
| [HW_PASSIVE_INITIALIZE_ROUTINE callback](nc-storport-hw-passive-initialize-routine.md) | The HwStorPassiveInitializeRoutine callback routine is called after the HwStorInitialize routine when the current IRQL is at PASSIVE_LEVEL. |
| [HW_PROCESS_SERVICE_REQUEST callback](nc-storport-hw-process-service-request.md) | The HwStorProcessServiceRequest callback routine receives the device control IRP that contains the IOCTL_MINIPORT_PROCESS_SERVICE_IRP request when a caller, such as a user-mode application or kernel-mode driver, requires a &#0034;reverse callback&#0034; operation. |
| [HW_RESET_BUS callback](nc-storport-hw-reset-bus.md) | The HwStorResetBus routine is called by the port driver to clear error conditions. |
| [HW_STARTIO callback](nc-storport-hw-startio.md) | The Storport driver calls the HwStorStartIo routine one time for each incoming I/O request. |
| [HW_TIMER callback](nc-storport-hw-timer.md) | The HwStorTimer routine is called after the interval that is specified when the miniport driver called StorPortNotification with the RequestTimerCall NotificationType value. |
| [VIRTUAL_HW_FIND_ADAPTER callback](nc-storport-virtual-hw-find-adapter.md) | The Storport virtual miniport uses configuration information supplied to the VirtualHwStorFindAdapter routine to further initialize itself. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [MEMORY_REGION structure](ns-storport--memory-region.md) | The MEMORY_REGION structure describes a region of physically contiguous memory. |
| [MESSAGE_INTERRUPT_INFORMATION structure](ns-storport--message-interrupt-information.md) | The MESSAGE_INTERRUPT_INFORMATION structure describes a message signaled interrupt (MSI). |
| [MINIPORT_DUMP_POINTERS structure](ns-storport--miniport-dump-pointers.md) | A Storport miniport driver uses this structure to support the SCSI_REQUEST_BLOCK (SRB) function code SRB_FUNCTION_DUMP_POINTERS. |
| [PERF_CONFIGURATION_DATA structure](ns-storport--perf-configuration-data.md) | The PERF_CONFIGURATION_DATA structure describes the performance optimizations that are supported by the StorPortInitializePerfOpts routine. |
| [PORT_CONFIGURATION_INFORMATION structure](ns-storport--port-configuration-information.md) | The PORT_CONFIGURATION_INFORMATION contains configuration information for a host bus adapter (HBA). |
| [PPRI_REGISTRATION_LIST structure](ns-storport-ppri-registration-list.md) | The PRI_REGISTRATION_LIST structure is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION_ACTION_READ_KEYS. |
| [PPRI_RESERVATION_DESCRIPTOR structure](ns-storport-ppri-reservation-descriptor.md) | The PRI_RESERVATION_DESCRIPTOR structure is used to construct the PRI_RESERVATION_LIST structure that is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION_ACTION_READ_RESERVATIONS. |
| [PPRI_RESERVATION_LIST structure](ns-storport-ppri-reservation-list.md) | The PRI_RESERVATION_LIST structure is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION_ACTION_READ_RESERVATIONS. |
| [PPRO_PARAMETER_LIST structure](ns-storport-ppro-parameter-list.md) | The PRO_PARAMETER_LIST structure is sent in a Persistent Reserve Out command to a device server. |
| [PRT_PARAMETER_DATA structure](ns-storport-prt-parameter-data.md) | The RT_PARAMETER_DATA structure contains the parameter data for the report timestamp command. |
| [PST_PARAMETER_DATA structure](ns-storport-pst-parameter-data.md) | The ST_PARAMETER_DATA structure contains the parameter list for the set timestamp command. |
| [REPORT_ZONES_DATA structure](ns-storport--report-zones-data.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [SCSI_PNP_REQUEST_BLOCK structure](ns-storport--scsi-pnp-request-block.md) | TheSCSI_PNP_REQUEST_BLOCK structure is a special version of a SCSI_REQUEST_BLOCK that is used for plug and play (PNP) requests.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [SCSI_POWER_REQUEST_BLOCK structure](ns-storport--scsi-power-request-block.md) | The SCSI_POWER_REQUEST_BLOCK structure is a special version of a SCSI_REQUEST_BLOCK that is used for power management requests.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [SCSI_WMI_REQUEST_BLOCK structure](ns-storport--scsi-wmi-request-block.md) | This structure is a special version of a SCSI_REQUEST_BLOCK for use with WMI commands. |
| [SES_CONFIGURATION_DIAGNOSTIC_PAGE structure](ns-storport--ses-configuration-diagnostic-page.md) | TBD. |
| [SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure](ns-storport--ses-download-microcode-control-diagnostic-page.md) | The SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure contains a vendor specific microcode (i.e., firmware) image for use by the enclosure services process. |
| [SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure](ns-storport--ses-download-microcode-status-descriptor.md) | The SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure specifies the status and additional status of a download microcode. |
| [SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE structure](ns-storport--ses-download-microcode-status-diagnostic-page.md) | The Download Microcode Status diagnostic page includes information about the status of one or more download microcode operations. |
| [SRBEX_DATA structure](ns-storport--srbex-data.md) | The SRBEX_DATA structure is the generalized format for containing extended SRB data. |
| [SRBEX_DATA_BIDIRECTIONAL structure](ns-storport--srbex-data-bidirectional.md) | The SRBEX_DATA_BIDIRECTIONAL structure contains the extended SRB data for bi-directional transfer commands. |
| [SRBEX_DATA_IO_INFO structure](ns-storport--srbex-data-io-info.md) | The SRBEX_DATA_IO_INFO structure contains additional information related to a read or write request in an extended SRB. |
| [SRBEX_DATA_PNP structure](ns-storport--srbex-data-pnp.md) | The SRBEX_DATA_PNP structure contains the request data for an extended plug and play (PNP) SRB. |
| [SRBEX_DATA_POWER structure](ns-storport--srbex-data-power.md) | The SRBEX_DATA_POWER structure contains the request data for an extended power SRB. |
| [SRBEX_DATA_SCSI_CDB16 structure](ns-storport--srbex-data-scsi-cdb16.md) | The SRBEX_DATA_SCSI_CDB16 structure contains the extended SRB data for a 16-byte SCSI command data block (CDB). |
| [SRBEX_DATA_SCSI_CDB32 structure](ns-storport--srbex-data-scsi-cdb32.md) | The SRBEX_DATA_SCSI_CDB32 structure contains the extended SRB data for a 32-byte SCSI command data block (CDB). |
| [SRBEX_DATA_SCSI_CDB_VAR structure](ns-storport--srbex-data-scsi-cdb-var.md) | The SRBEX_DATA_SCSI_CDB_VAR structure contains the extended SRB data for a variable length SCSI command data block (CDB). |
| [SRBEX_DATA_WMI structure](ns-storport--srbex-data-wmi.md) | The SRBEX_DATA_WMI structure contains the request data for an extended WMI SRB. |
| [STARTIO_PERFORMANCE_PARAMETERS structure](ns-storport--startio-performance-parameters.md) | The STARTIO_PERFORMANCE_PARAMETERS structure describes the performance parameters that are returned to the miniport driver by the StorPortGetStartIoPerfParams routine. |
| [STORAGE_REQUEST_BLOCK structure](ns-storport--storage-request-block.md) | The STORAGE_REQUEST_BLOCK is the extended format SCSI Request Block (SRB) structure. |
| [STORPORT_TELEMETRY_EVENT structure](ns-storport--storport-telemetry-event.md) | The STORPORT_TELEMETRY_EVENT structure describes the miniport telemetry data payload. |
| [STOR_ADDRESS structure](ns-storport--stor-address.md) | A general structure for holding a storage device address. |
| [STOR_ADDR_BTL8 structure](ns-storport--stor-addr-btl8.md) | The STOR_ADDR_BTL8 address structure contains the addressing information for an 8-bit Bus-Target-LUN (BTL8) address. |
| [STOR_CRYPTO_CAPABILITIES_DATA structure](ns-storport--stor-crypto-capabilities-data.md) | Reserved for system use. |
| [STOR_CRYPTO_CAPABILITY structure](ns-storport--stor-crypto-capability.md) | Reserved for system use. |
| [STOR_CRYPTO_KEY_INFO structure](ns-storport--stor-crypto-key-info.md) | Reserved for system use. |
| [STOR_CRYPTO_OPERATION_INSERT_KEY structure](ns-storport--stor-crypto-operation-insert-key.md) | Reserved for system use. |
| [STOR_DEVICE_CAPABILITIES structure](ns-storport--stor-device-capabilities.md) | The STOR_DEVICE_CAPABILITIES structure reports device capabilities to the Storport driver in response to a capabilities query in a SCSI request block (SRB) with a function of SRB_FUNCTION_PNP. |
| [STOR_DEVICE_CAPABILITIES_EX structure](ns-storport--stor-device-capabilities-ex.md) | The STOR_DEVICE_CAPABILITIES_EX structure reports device capabilities to the Storport driver in response to a capabilities query in a SCSI request block (SRB) with a function of SRB_FUNCTION_PNP. |
| [STOR_DPC structure](ns-storport--stor-dpc.md) | The STOR_DPC structure is an opaque structure that represents a DPC object. Do not set the members of this structure directly. |
| [STOR_LIST_ENTRY structure](ns-storport--stor-list-entry.md) | A STOR_LIST_ENTRY structure describes an entry in a doubly linked list or serves as the header for such a list. |
| [STOR_LOG_EVENT_DETAILS structure](ns-storport--stor-log-event-details.md) | The STOR_LOG_EVENT_DETAILS structure provides details pertaining to Storport-specific error log events and system log events. |
| [STOR_POFX_COMPONENT structure](ns-storport--stor-pofx-component.md) | The STOR_POFX_COMPONENT structure describes the power state attributes of a storage device component. |
| [STOR_POFX_COMPONENT_IDLE_STATE structure](ns-storport--stor-pofx-component-idle-state.md) | The STOR_POFX_COMPONENT_IDLE_STATE structure specifies the attributes of an functional power state (F-state) of a component in a storage device. |
| [STOR_POFX_COMPONENT_V2 structure](ns-storport--stor-pofx-component-v2.md) | The STOR_POFX_COMPONENT_V2 structure describes the power state attributes of a storage device component. |
| [STOR_POFX_DEVICE structure](ns-storport--stor-pofx-device.md) | The STOR_POFX_DEVICE structure describes the power attributes of a storage device to the power management framework (PoFx). |
| [STOR_POFX_DEVICE_V2 structure](ns-storport--stor-pofx-device-v2.md) | The STOR_POFX_DEVICE_V2 structure describes the power attributes of a storage device to the power management framework (PoFx). |
| [STOR_POFX_DEVICE_V3 structure](ns-storport--stor-pofx-device-v3.md) | The STOR_POFX_DEVICE_V3 structure describes the power attributes of a storage device to the power management framework (PoFx). |
| [STOR_RICH_DEVICE_DESCRIPTION structure](ns-storport--stor-rich-device-description.md) | The STOR_RICH_DEVICE_DESCRIPTION structure describes the attributes of the physical device for which a driver is requesting a DMA (direct memory access) adapter. |
| [STOR_SCATTER_GATHER_ELEMENT structure](ns-storport--stor-scatter-gather-element.md) | The STOR_SCATTER_GATHER_ELEMENT structure is used with STOR_SCATTER_GATHER_LIST to build a list of scatter/gather elements. |
| [STOR_SCATTER_GATHER_LIST structure](ns-storport--stor-scatter-gather-list.md) | The STOR_SCATTER_GATHER_LIST structure is used in conjunction with the StorPortGetScatterGatherList routine to retrieve the scatter/gather list for a SCSI request block (SRB). |
| [STOR_UNIT_ATTRIBUTES structure](ns-storport--stor-unit-attributes.md) | The STOR_UNIT_ATTRIBUTES structure contains bitfields indicating attribute support for a storage device unit. |
| [VIRTUAL_HW_INITIALIZATION_DATA structure](ns-storport--virtual-hw-initialization-data.md) | The VIRTUAL_HW_INITIALIZATION_DATA structure contains information particular to each virtual miniport driver. |
| [VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE structure](ns-storport--vpd-zoned-block-device-characteristics-page.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [ZONE_DESCRIPTIOR structure](ns-storport--zone-descriptior.md) | Note  This structure is for internal use only and should not be called from your code. . |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [INTERRUPT_SYNCHRONIZATION_MODE enumeration](ne-storport--interrupt-synchronization-mode.md) | The INTERRUPT_SYNCHRONIZATION_MODE enumerator specifies the interrupt synchronization mode. |
| [PSTOR_POWER_ACTION enumeration](ne-storport-pstor-power-action.md) | The STOR_POWER_ACTION enumerator indicates the power state that the system is about to enter during a power transition. |
| [SES_DOWNLOAD_MICROCODE_STATE enumeration](ne-storport--ses-download-microcode-state.md) | TBD. |
| [STOR_DEVICE_POWER_STATE enumeration](ne-storport--stor-device-power-state.md) | The STOR_DEVICE_POWER_STATE enumerator specifies a device power state. |
| [STOR_EVENT_ASSOCIATION_ENUM enumeration](ne-storport--stor-event-association-enum.md) | The STOR_EVENT_ASSOCIATION_ENUM enumerator specifies the type of device that is associated with an event. |
| [STOR_SPINLOCK enumeration](ne-storport--stor-spinlock.md) | The STOR_SPINLOCK enumeration is used to specify the type of a spinlock. |
