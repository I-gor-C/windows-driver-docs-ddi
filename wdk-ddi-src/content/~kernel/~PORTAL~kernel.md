# Declarations in the kernel technology
This technology  contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [AuxKlibInitialize function](..\aux_klib\nf-aux-klib-auxklibinitialize.md) | The AuxKlibInitialize routine initializes the Auxiliary Kernel-Mode Library. |
| [AuxKlibGetSystemFirmwareTable function](..\aux_klib\nf-aux-klib-auxklibgetsystemfirmwaretable.md) | The AuxKlibGetSystemFirmwareTable routine retrieves the specified firmware table from the firmware table provider. |
| [AuxKlibGetImageExportDirectory function](..\aux_klib\nf-aux-klib-auxklibgetimageexportdirectory.md) | The AuxKlibGetImageExportDirectory routine returns an image module's export directory. |
| [AuxKlibQueryModuleInformation function](..\aux_klib\nf-aux-klib-auxklibquerymoduleinformation.md) | The AuxKlibQueryModuleInformation routine retrieves information about the image modules that the operating system has loaded. |
| [AuxKlibEnumerateSystemFirmwareTables function](..\aux_klib\nf-aux-klib-auxklibenumeratesystemfirmwaretables.md) | The AuxKlibEnumerateSystemFirmwareTables routine enumerates all system firmware tables of the specified type. |
| [AuxKlibGetBugCheckData function](..\aux_klib\nf-aux-klib-auxklibgetbugcheckdata.md) | The AuxKlibGetBugCheckData routine retrieves information about a bug check that has just occurred. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [AUX_MODULE_BASIC_INFO structure](..\aux_klib\ns-aux-klib--aux-module-basic-info.md) | The AUX_MODULE_BASIC_INFO structure contains basic information about a loaded image module. |
| [AUX_MODULE_EXTENDED_INFO structure](..\aux_klib\ns-aux-klib--aux-module-extended-info.md) | The AUX_MODULE_EXTENDED_INFO structure contains extended information about a loaded image module. |
| [KBUGCHECK_DATA structure](..\aux_klib\ns-aux-klib--kbugcheck-data.md) | The KBUGCHECK_DATA structure contains bug check parameters. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdmlibIoDisconnectInterruptEx function](..\iointex\nf-iointex-wdmlibiodisconnectinterruptex.md) | The WdmlibIoDisconnectInterruptEx function unregisters an interrupt service routine (ISR) that was registered by a previous call to the WdmlibIoConnectInterruptEx function. |
| [WdmlibIoGetAffinityInterrupt function](..\iointex\nf-iointex-wdmlibiogetaffinityinterrupt.md) | The WdmlibIoGetAffinityInterrupt function gets the group affinity of an interrupt object. |
| [WdmlibIoConnectInterruptEx function](..\iointex\nf-iointex-wdmlibioconnectinterruptex.md) | The WdmlibIoConnectInterruptEx function registers an interrupt-handling routine for a device's interrupts. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [HalExamineMBR function](..\ntddk\nf-ntddk-halexaminembr.md) | The HalExamineMBR routine reads the master boot record (MBR) of a disk and returns data from the MBR if the MBR is of the type specified by the caller. |
| [HalAllocateHardwareCounters function](..\ntddk\nf-ntddk-halallocatehardwarecounters.md) | The HalAllocateHardwareCounters routine allocates a set of hardware performance counters. |
| [IoVerifyPartitionTable function](..\ntddk\nf-ntddk-ioverifypartitiontable.md) | The IoVerifyPartitionTable routine checks the validity of the partition table for a disk. |
| [IoSetThreadHardErrorMode function](..\ntddk\nf-ntddk-iosetthreadharderrormode.md) | The IoSetThreadHardErrorMode routine enables or disables hard error reporting for the current thread. |
| [RtlConvertUlongToLuid function](..\ntddk\nf-ntddk-rtlconvertulongtoluid.md) | The RtlConvertUlongToLuid routine converts an unsigned long integer to a locally unique identifier (LUID), which is used by the system to represent a security privilege. |
| [KeQueryHardwareCounterConfiguration function](..\ntddk\nf-ntddk-kequeryhardwarecounterconfiguration.md) | The KeQueryHardwareCounterConfiguration routine queries the operating system for the list of hardware counters to use for thread profiling. |
| [KeLeaveCriticalRegion function](..\ntddk\nf-ntddk-keleavecriticalregion.md) | The KeLeaveCriticalRegion routine reenables the delivery of normal kernel-mode APCs that were disabled by a preceding call to KeEnterCriticalRegion. |
| [KeGetCurrentProcessorNumber function](..\ntddk\nf-ntddk-kegetcurrentprocessornumber~r1.md) | The KeGetCurrentProcessorNumber routine returns the system-assigned number of the current processor on which the caller is running. |
| [KeQueryTickCount function](..\ntddk\nf-ntddk-kequerytickcount.md) | The KeQueryTickCount routine maintains a count of the interval timer interrupts that have occurred since the system was booted. |
| [RtlIsStateSeparationEnabled function](..\ntddk\nf-ntddk-rtlisstateseparationenabled.md) | Checks if the SKU for the current context supports multiple sessions. |
| [RtlRunOnceInitialize function](..\ntddk\nf-ntddk-rtlrunonceinitialize.md) | The RtlRunOnceInitialize routine initializes a RTL_RUN_ONCE structure. |
| [MmIsAddressValid function](..\ntddk\nf-ntddk-mmisaddressvalid.md) | The MmIsAddressValid routine checks whether a page fault will occur for a read or write operation at a given virtual address.Warning  We do not recommend using this function. |
| [PsSetCreateProcessNotifyRoutine function](..\ntddk\nf-ntddk-pssetcreateprocessnotifyroutine.md) | The PsSetCreateProcessNotifyRoutine routine adds a driver-supplied callback routine to, or removes it from, a list of routines to be called whenever a process is created or deleted. |
| [RtlRunOnceExecuteOnce function](..\ntddk\nf-ntddk-rtlrunonceexecuteonce.md) | The RtlRunOnceExecuteOnce performs a one-time initialization. |
| [MmAllocateContiguousMemory function](..\ntddk\nf-ntddk-mmallocatecontiguousmemory.md) | The MmAllocateContiguousMemory routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space. |
| [IoSetActivityIdIrp function](..\ntddk\nf-ntddk-iosetactivityidirp.md) | The IoSetActivityIdIrp routine associates an activity ID with an IRP. |
| [PsAllocSiloContextSlot function](..\ntddk\nf-ntddk-psallocsilocontextslot.md) | This routine allocates a slot that can be used to insert, retrieve, and delete an object in all silos. . |
| [PsRemoveCreateThreadNotifyRoutine function](..\ntddk\nf-ntddk-psremovecreatethreadnotifyroutine.md) | The PsRemoveCreateThreadNotifyRoutine routine removes a callback routine that was registered by the PsSetCreateThreadNotifyRoutine routine. |
| [KeLeaveGuardedRegion function](..\ntddk\nf-ntddk-keleaveguardedregion.md) | The KeLeaveGuardedRegion routine exits a guarded region entered by KeEnterGuardedRegion. |
| [PsSetCreateProcessNotifyRoutineEx function](..\ntddk\nf-ntddk-pssetcreateprocessnotifyroutineex.md) | The PsSetCreateProcessNotifyRoutineEx routine registers or removes a callback routine that notifies the caller when a process is created or exits. |
| [KeQueryActiveProcessorCount function](..\ntddk\nf-ntddk-kequeryactiveprocessorcount.md) | The KeQueryActiveProcessorCount routine returns the number of currently active processors. |
| [KeQueryLogicalProcessorRelationship function](..\ntddk\nf-ntddk-kequerylogicalprocessorrelationship.md) | The KeQueryLogicalProcessorRelationship routine gets information about the relationships of one or more processors to the other processors in a multiprocessor system. |
| [PsSetCreateThreadNotifyRoutineEx function](..\ntddk\nf-ntddk-pssetcreatethreadnotifyroutineex.md) | The PsSetCreateThreadNotifyRoutineEx routine registers a driver-supplied callback that is subsequently notified when a new thread is created and when such a thread is deleted. |
| [PsInsertPermanentSiloContext function](..\ntddk\nf-ntddk-psinsertpermanentsilocontext.md) | This routine inserts an object in an empty slot in a Silo. |
| [ZwPowerInformation function](..\ntddk\nf-ntddk-zwpowerinformation.md) | The ZwPowerInformation routine sets or retrieves system power information. |
| [KePulseEvent function](..\ntddk\nf-ntddk-kepulseevent.md) | The KePulseEvent routine atomically sets an event object to a signaled state, attempts to satisfy as many waits as possible, and then resets the event object to a not-signaled state. |
| [PsAttachSiloToCurrentThread function](..\ntddk\nf-ntddk-psattachsilotocurrentthread.md) | This routine places a thread temporarily into the specified Silo. |
| [KeGetCurrentNodeNumber function](..\ntddk\nf-ntddk-kegetcurrentnodenumber.md) | The KeGetCurrentNodeNumber routine gets the NUMA node number for the logical processor that the caller is running on. |
| [PsGetCurrentThreadId function](..\ntddk\nf-ntddk-psgetcurrentthreadid.md) | The PsGetCurrentThreadId routine identifies the current thread. |
| [KeQueryActiveProcessors function](..\ntddk\nf-ntddk-kequeryactiveprocessors.md) | The KeQueryActiveProcessors routine returns a bitmask of the currently active processors. |
| [RtlMapGenericMask function](..\ntddk\nf-ntddk-rtlmapgenericmask.md) | The RtlMapGenericMask routine determines the nongeneric access rights specified by an ACCESS_MASK. |
| [PsSetCreateProcessNotifyRoutineEx2 function](..\ntddk\nf-ntddk-pssetcreateprocessnotifyroutineex2.md) | The PsSetCreateProcessNotifyRoutineEx2 routine registers or removes a callback routine that notifies the caller when a process is created or deleted. |
| [HalFreeHardwareCounters function](..\ntddk\nf-ntddk-halfreehardwarecounters.md) | The HalFreeHardwareCounters routine frees a set of hardware performance counters that was acquired in a previous call to HalAllocateHardwareCounters routine. |
| [ExRaiseDatatypeMisalignment function](..\ntddk\nf-ntddk-exraisedatatypemisalignment.md) | The ExRaiseDatatypeMisalignment routine can be used with structured exception handling to throw a driver-determined exception for a misaligned data type that occurs when a driver processes I/O requests. |
| [ExUuidCreate function](..\ntddk\nf-ntddk-exuuidcreate.md) | The ExUuidCreate routine initializes a UUID (GUID) structure to a newly generated value. |
| [RtlIncrementCorrelationVector function](..\ntddk\nf-ntddk-rtlincrementcorrelationvector.md) | Increments the specified correlation vector. For a correlation vector of the form X.i, the incremented value is be X.(i+1). |
| [KeGetCurrentProcessorNumberEx function](..\ntddk\nf-ntddk-kegetcurrentprocessornumberex.md) | The KeGetCurrentProcessorNumberEx routine gets the processor number of the logical processor that the caller is running on. |
| [IoGetConfigurationInformation function](..\ntddk\nf-ntddk-iogetconfigurationinformation.md) | The IoGetConfigurationInformation routine returns a pointer to the I/O manager's global configuration information structure, which contains the current values for how many physical disk, floppy, CD-ROM, tape, SCSI HBA, serial, and parallel devices have device objects created to represent them by drivers as they are loaded. |
| [PsGetHostSilo function](..\ntddk\nf-ntddk-psgethostsilo.md) | This routine returns the host silo. |
| [KeEnterCriticalRegion function](..\ntddk\nf-ntddk-keentercriticalregion.md) | The KeEnterCriticalRegion routine temporarily disables the execution of normal kernel APCs, but does not prevent special kernel APCs from running. |
| [RtlVolumeDeviceToDosName function](..\ntddk\nf-ntddk-rtlvolumedevicetodosname.md) | The RtlVolumeDeviceToDosName routine is obsolete for Windows XP and later versions of Windows. Use IoVolumeDeviceToDosName instead.RtlVolumeDeviceToDosName returns the MS-DOS path for a specified device object that represents a file system volume. |
| [IoRegisterBootDriverCallback function](..\ntddk\nf-ntddk-ioregisterbootdrivercallback.md) | The IoRegisterBootDriverCallback routine registers a BOOT_DRIVER_CALLBACK_FUNCTION routine to be called during the initialization of a boot-start driver and its dependent DLLs. |
| [PsGetParentSilo function](..\ntddk\nf-ntddk-psgetparentsilo.md) | Retrieves the most immediate parent silo in the hierarchy for a given job object. |
| [IoClearActivityIdThread function](..\ntddk\nf-ntddk-ioclearactivityidthread.md) | The IoClearActivityIdThread routine clears the activity ID of the current thread. |
| [IoGetPagingIoPriority function](..\ntddk\nf-ntddk-iogetpagingiopriority.md) | The IoGetPagingIoPriority routine indicates the priority level of a paging I/O request. |
| [KeQueryMaximumProcessorCountEx function](..\ntddk\nf-ntddk-kequerymaximumprocessorcountex.md) | The KeQueryMaximumProcessorCountEx routine returns the maximum number of logical processors in a specified group in a multiprocessor system. |
| [PsDereferenceSiloContext function](..\ntddk\nf-ntddk-psdereferencesilocontext.md) | This routine decrements the reference count on the object. |
| [RtlUpperString function](..\ntddk\nf-ntddk-rtlupperstring.md) | The RtlUpperString routine copies the given SourceString to the DestinationString buffer, converting it to uppercase. |
| [KeGetCurrentProcessorNumber function](..\ntddk\nf-ntddk-kegetcurrentprocessornumber.md) | The KeGetCurrentProcessorNumber routine returns the system-assigned number of the current processor on which the caller is running. |
| [IoPropagateActivityIdToThread function](..\ntddk\nf-ntddk-iopropagateactivityidtothread.md) | The IoPropagateActivityIdToThread routine associates the activity ID from an IRP with the current thread. |
| [IoSetActivityIdThread function](..\ntddk\nf-ntddk-iosetactivityidthread.md) | The IoSetActivityIdThread routine associates an activity ID with the current thread. Drivers should use this routine when they are tracing aware and are issuing I/O on a worker thread. |
| [PsGetSiloMonitorContextSlot function](..\ntddk\nf-ntddk-psgetsilomonitorcontextslot.md) | This routine returns the silo context slot that was allocated by the monitor during the registration. |
| [KeSetImportanceDpc function](..\ntddk\nf-ntddk-kesetimportancedpc.md) | The KeSetImportanceDpc routine specifies how soon the DPC routine is run. |
| [PsGetCurrentThreadTeb function](..\ntddk\nf-ntddk-psgetcurrentthreadteb.md) | The PsGetCurrentThreadTeb routine returns the Thread Environment Block (TEB) of the current thread. The call must be made in kernel-mode. |
| [RtlRunOnceComplete function](..\ntddk\nf-ntddk-rtlrunoncecomplete.md) | The RtlRunOnceComplete routine completes the one-time initialization began by RtlRunOnceBeginInitialize. |
| [ExRaiseAccessViolation function](..\ntddk\nf-ntddk-exraiseaccessviolation.md) | The ExRaiseAccessViolation routine can be used with structured exception handling to throw a driver-determined exception for a memory access violation that occurs when a driver processes I/O requests. |
| [MmAllocateContiguousMemorySpecifyCache function](..\ntddk\nf-ntddk-mmallocatecontiguousmemoryspecifycache.md) | The MmAllocateContiguousMemorySpecifyCache routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space. |
| [PsSetLoadImageNotifyRoutine function](..\ntddk\nf-ntddk-pssetloadimagenotifyroutine.md) | The PsSetLoadImageNotifyRoutine routine registers a driver-supplied callback that is subsequently notified whenever an image is loaded (or mapped into memory). |
| [IoDecrementKeepAliveCount function](..\ntddk\nf-ntddk-iodecrementkeepalivecount.md) | The IoDecrementKeepAliveCount routine decrements a reference count associated with an Windows app on a specific device. |
| [KeInvalidateAllCaches function](..\ntddk\nf-ntddk-keinvalidateallcaches.md) | The KeInvalidateAllCaches routine flushes all processor caches. |
| [IoAllocateController function](..\ntddk\nf-ntddk-ioallocatecontroller.md) | The IoAllocateController routine sets up the call to a driver-supplied ControllerControl routine as soon as the device controller, represented by the given controller object, is available to carry out an I/O operation for the target device, represented by the given device object. |
| [IoFreeController function](..\ntddk\nf-ntddk-iofreecontroller.md) | The IoFreeController routine releases a previously allocated controller object when the driver has completed an I/O request. |
| [KeEnterGuardedRegion function](..\ntddk\nf-ntddk-keenterguardedregion.md) | The KeEnterGuardedRegion routine enters a guarded region, which disables all kernel-mode APC delivery to the current thread. |
| [PsGetCurrentSilo function](..\ntddk\nf-ntddk-psgetcurrentsilo.md) | This routine returns the current silo for the calling thread. First the thread is checked to see if it has been attached to a silo. If not, then the thread is checked to see if it is in a silo. |
| [PsGetCurrentThread function](..\ntddk\nf-ntddk-psgetcurrentthread.md) | The PsGetCurrentThread routine identifies the current thread. |
| [RtlUpperChar function](..\ntddk\nf-ntddk-rtlupperchar.md) | The RtlUpperChar routine converts the specified character to uppercase. |
| [RtlUpcaseUnicodeString function](..\ntddk\nf-ntddk-rtlupcaseunicodestring.md) | The RtlUpcaseUnicodeString routine converts a copy of the source string to uppercase and writes the converted string in the destination buffer. |
| [IoRegisterBootDriverReinitialization function](..\ntddk\nf-ntddk-ioregisterbootdriverreinitialization.md) | The IoRegisterBootDriverReinitialization routine is called by a boot driver to register the driver's reinitialization routine with the I/O manager to be called after all devices have been enumerated and started. |
| [PsInsertSiloContext function](..\ntddk\nf-ntddk-psinsertsilocontext.md) | This routine inserts an object in an empty slot in a Silo. |
| [KeExpandKernelStackAndCallout function](..\ntddk\nf-ntddk-keexpandkernelstackandcallout.md) | The KeExpandKernelStackAndCallout routine calls a routine with a guaranteed amount of stack space. |
| [RtlInitializeCorrelationVector function](..\ntddk\nf-ntddk-rtlinitializecorrelationvector.md) | Initializes the specified correlation vector with the supplied GUID. |
| [IoSetMasterIrpStatus function](..\ntddk\nf-ntddk-iosetmasterirpstatus.md) | The IoSetMasterIrpStatus routine conditionally replaces the Status value in an IRP with the specified NTSTATUS value. |
| [MmCopyMemory function](..\ntddk\nf-ntddk-mmcopymemory.md) | The MmCopyMemory routine copies the specified range of virtual or physical memory into the caller-supplied buffer. |
| [ZwSetInformationThread function](..\ntddk\nf-ntddk-zwsetinformationthread.md) | The ZwSetInformationThread routine sets the priority of a thread. |
| [PsSetLoadImageNotifyRoutineEx function](..\ntddk\nf-ntddk-pssetloadimagenotifyroutineex.md) | The PsSetLoadImageNotifyRoutineEx routine registers a driver-supplied callback that is subsequently notified whenever an image is loaded (or mapped into memory). |
| [PsUnregisterSiloMonitor function](..\ntddk\nf-ntddk-psunregistersilomonitor.md) | This routine unregisters a server silo monitor. |
| [MmUnsecureVirtualMemory function](..\ntddk\nf-ntddk-mmunsecurevirtualmemory.md) | The MmUnsecureVirtualMemory routine unsecures a memory address range secured by the MmSecureVirtualMemory routine. |
| [IoRaiseHardError function](..\ntddk\nf-ntddk-ioraiseharderror.md) | The IoRaiseHardError routine causes a dialog box to appears that warns the user that a device I/O error has occurred, which might indicate that a physical device is failing. |
| [MmLockPagableSectionByHandle function](..\ntddk\nf-ntddk-mmlockpagablesectionbyhandle.md) | The MmLockPagableSectionByHandle routine locks a pageable code or data section into system memory by incrementing the reference count on the handle to the section. |
| [KeQueryNodeMaximumProcessorCount function](..\ntddk\nf-ntddk-kequerynodemaximumprocessorcount.md) | The KeQueryNodeMaximumProcessorCount routine returns the maximum number of logical processors that a specified node in a non-uniform memory access (NUMA) multiprocessor system can contain. |
| [ExFreePool function](..\ntddk\nf-ntddk-exfreepool.md) | The ExFreePool routine deallocates a block of pool memory. |
| [IoGetActivityIdIrp function](..\ntddk\nf-ntddk-iogetactivityidirp.md) | The IoGetActivityIdIrp routine retrieves the current activity ID associated with an IRP. |
| [MmAllocateContiguousMemorySpecifyCacheNode function](..\ntddk\nf-ntddk-mmallocatecontiguousmemoryspecifycachenode.md) | The MmAllocateContiguousMemorySpecifyCacheNode routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space. |
| [PsStartSiloMonitor function](..\ntddk\nf-ntddk-psstartsilomonitor.md) | This routine tries to start the server silo monitor. |
| [ZwTerminateProcess function](..\ntddk\nf-ntddk-zwterminateprocess.md) | The ZwTerminateProcess routine terminates a process and all of its threads. |
| [PsRemoveLoadImageNotifyRoutine function](..\ntddk\nf-ntddk-psremoveloadimagenotifyroutine.md) | The PsRemoveLoadImageNotifyRoutine routine removes a callback routine that was registered by the PsSetLoadImageNotifyRoutine routine. |
| [MmIsThisAnNtAsSystem function](..\ntddk\nf-ntddk-mmisthisanntassystem.md) | The MmIsThisAnNtAsSystem routine is obsolete for Windows XP and later versions of Windows. Use RtlGetVersion or RtlVerifyVersionInfo instead. |
| [IoGetActivityIdThread function](..\ntddk\nf-ntddk-iogetactivityidthread.md) | The IoGetActivityIdThread routine returns the activity ID associated with the current thread. |
| [PsFreeSiloContextSlot function](..\ntddk\nf-ntddk-psfreesilocontextslot.md) | This routine frees the specified slot and makes it available in the system. It undoes the effects of the PsAllocSiloContextSlot routine. |
| [IoGetFileObjectGenericMapping function](..\ntddk\nf-ntddk-iogetfileobjectgenericmapping.md) | The IoGetFileObjectGenericMapping routine returns information about the mapping between each generic access right and the set of specific access rights for file objects. |
| [PsMakeSiloContextPermanent function](..\ntddk\nf-ntddk-psmakesilocontextpermanent.md) | This routine makes the slot in a silo instance read-only, allowing the object in the slot to be retrieved without affecting the reference count on that object. |
| [KeQueryTickCount function](..\ntddk\nf-ntddk-kequerytickcount~r1.md) | The KeQueryTickCount routine maintains a count of the interval timer interrupts that have occurred since the system was booted. |
| [PsReferenceSiloContext function](..\ntddk\nf-ntddk-psreferencesilocontext.md) | This routine increments the reference count on the object. |
| [PsGetProcessId function](..\ntddk\nf-ntddk-psgetprocessid.md) | The PsGetProcessId routine returns the process identifier (process ID) that is associated with a specified process. |
| [RtlRunOnceBeginInitialize function](..\ntddk\nf-ntddk-rtlrunoncebegininitialize.md) | The RtlRunOnceBeginInitialize routine begins a one-time initialization. |
| [PsGetPermanentSiloContext function](..\ntddk\nf-ntddk-psgetpermanentsilocontext.md) | This routine retrieves an object that was inserted in the Silo without incrementing the reference count. |
| [RtlExtendCorrelationVector function](..\ntddk\nf-ntddk-rtlextendcorrelationvector.md) | This routine extends the supplied correlation vector. For a correlation vector of the form X.i, the extended value is X.i.0. |
| [IoMakeAssociatedIrp function](..\ntddk\nf-ntddk-iomakeassociatedirp.md) | This routine is reserved for use by file systems and file system filter drivers. |
| [ZwAllocateLocallyUniqueId function](..\ntddk\nf-ntddk-zwallocatelocallyuniqueid.md) | The ZwAllocateLocallyUniqueId routine allocates a locally unique identifier (LUID). |
| [IoCreateController function](..\ntddk\nf-ntddk-iocreatecontroller.md) | The IoCreateController routine allocates memory for and initializes a controller object with a controller extension of a driver-determined size. |
| [KeAreApcsDisabled function](..\ntddk\nf-ntddk-keareapcsdisabled.md) | The KeAreApcsDisabled routine returns whether the calling thread is within a critical region or a guarded region, which disables normal kernel APC delivery. |
| [MmFreeContiguousMemorySpecifyCache function](..\ntddk\nf-ntddk-mmfreecontiguousmemoryspecifycache.md) | The MmFreeContiguousMemorySpecifyCache routine frees a buffer that was allocated by an MmAllocateContiguousMemorySpecifyCacheXxx routine. |
| [KeSetBasePriorityThread function](..\ntddk\nf-ntddk-kesetbaseprioritythread.md) | The KeSetBasePriorityThread routine sets the run-time priority, relative to the current process, for a given thread. |
| [KeQueryMaximumGroupCount function](..\ntddk\nf-ntddk-kequerymaximumgroupcount.md) | The KeQueryMaximumGroupCount routine returns the maximum number of groups in a multiprocessor system. |
| [IoRegisterDriverReinitialization function](..\ntddk\nf-ntddk-ioregisterdriverreinitialization.md) | The IoRegisterDriverReinitialization routine is called by a driver during its initialization or reinitialization to register its Reinitialize routine to be called again before the driver's and, possibly the system's, initialization is complete. |
| [IoVolumeDeviceToDosName function](..\ntddk\nf-ntddk-iovolumedevicetodosname.md) | The IoVolumeDeviceToDosName routine returns the MS-DOS path for a specified device object that represents a file system volume. |
| [RtlGetEnabledExtendedFeatures function](..\ntddk\nf-ntddk-rtlgetenabledextendedfeatures.md) | The RtlGetEnabledExtendedFeatures routine returns a mask of extended processor features that are enabled by the system. |
| [IoTransferActivityId function](..\ntddk\nf-ntddk-iotransferactivityid.md) | The IoTransferActivityId routine logs an ETW transfer event using the I/O tracing provider on behalf of the caller. This allows a driver to associate two related activity IDs without requiring a specific provider to be enabled. |
| [KeQueryGroupAffinity function](..\ntddk\nf-ntddk-kequerygroupaffinity.md) | The KeQueryGroupAffinity routine returns an affinity mask that identifies the active logical processors in a specified group in a multiprocessor system. |
| [IoReportResourceForDetection function](..\ntddk\nf-ntddk-ioreportresourcefordetection.md) | The IoReportResourceForDetection routine claims hardware resources in the configuration registry for a legacy device. |
| [KeQueryActiveGroupCount function](..\ntddk\nf-ntddk-kequeryactivegroupcount.md) | The KeQueryActiveGroupCount routine returns the number of active processor groups in a multiprocessor system. |
| [IoReportRootDevice function](..\ntddk\nf-ntddk-ioreportrootdevice.md) | The IoReportRootDevice routine reports a device that cannot be detected by a PnP bus driver to the PnP Manager. IoReportRootDevice allows only one device per driver to be created. |
| [MmAllocateNonCachedMemory function](..\ntddk\nf-ntddk-mmallocatenoncachedmemory.md) | The MmAllocateNonCachedMemory routine allocates a virtual address range of noncached and cache-aligned memory. |
| [IoUnregisterBootDriverCallback function](..\ntddk\nf-ntddk-iounregisterbootdrivercallback.md) | The IoUnRegisterBootDriverCallback routine unregisters a previously registered BOOT_DRIVER_CALLBACK_FUNCTION routine. |
| [IoDeleteController function](..\ntddk\nf-ntddk-iodeletecontroller.md) | The IoDeleteController routine removes a given controller object from the system, for example, when the driver that created it is being unloaded. |
| [RtlCopyString function](..\ntddk\nf-ntddk-rtlcopystring.md) | The RtlCopyString routine copies a source string to a destination string. |
| [PsDetachSiloFromCurrentThread function](..\ntddk\nf-ntddk-psdetachsilofromcurrentthread.md) | This routine removes a thread from a silo which was added by an attach. For more info about attaching, see the PsAttachSiloToCurrentThread routine. |
| [KeQueryHighestNodeNumber function](..\ntddk\nf-ntddk-kequeryhighestnodenumber.md) | The KeQueryHighestNodeNumber routine returns the highest node number in a multiprocessor system that has a non-uniform memory access (NUMA) architecture. |
| [KeQueryNodeActiveAffinity function](..\ntddk\nf-ntddk-kequerynodeactiveaffinity.md) | The KeQueryNodeActiveAffinity routine gets the current processor affinity of a specified node in a multiprocessor system that has a non-uniform memory access (NUMA) architecture. |
| [PsGetServerSiloActiveConsoleId function](..\ntddk\nf-ntddk-psgetserversiloactiveconsoleid.md) | Gets the active console for the current server silo context for the supplied thread. |
| [ZwOpenProcess function](..\ntddk\nf-ntddk-zwopenprocess.md) | The ZwOpenProcess routine opens a handle to a process object and sets the access rights to this object. |
| [IoReportDetectedDevice function](..\ntddk\nf-ntddk-ioreportdetecteddevice.md) | The IoReportDetectedDevice routine reports a non-PnP device to the PnP manager. |
| [RtlPrefixUnicodeString function](..\ntddk\nf-ntddk-rtlprefixunicodestring.md) | The RtlPrefixUnicodeString routine compares two Unicode strings to determine whether one string is a prefix of the other. |
| [KeQueryActiveProcessorCountEx function](..\ntddk\nf-ntddk-kequeryactiveprocessorcountex.md) | The KeQueryActiveProcessorCountEx routine returns the number of active logical processors in a specified group in a multiprocessor system or in the entire system. |
| [RtlCompareString function](..\ntddk\nf-ntddk-rtlcomparestring.md) | The RtlCompareString routine compares two counted strings. |
| [KeGetCurrentProcessorNumber function](..\ntddk\nf-ntddk-kegetcurrentprocessornumber~r2.md) | The KeGetCurrentProcessorNumber routine returns the system-assigned number of the current processor on which the caller is running. |
| [KeBugCheck function](..\ntddk\nf-ntddk-kebugcheck.md) | The KeBugCheck routine brings down the system in a controlled manner when the caller discovers an unrecoverable inconsistency that would corrupt the system if the caller continued to run. |
| [IoIncrementKeepAliveCount function](..\ntddk\nf-ntddk-ioincrementkeepalivecount.md) | The IoIncrementKeepAliveCount routine increments a reference count associated with an Windows app process on a specific device. |
| [PsGetProcessCreateTimeQuadPart function](..\ntddk\nf-ntddk-psgetprocesscreatetimequadpart.md) | The PsGetProcessCreateTimeQuadPart routine returns a LONGLONG value that represents the time at which the process was created. |
| [KeRaiseIrqlToDpcLevel function](..\ntddk\nf-ntddk-keraiseirqltodpclevel~r1.md) | The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [PsIsHostSilo function](..\ntddk\nf-ntddk-psishostsilo.md) | This routine will check if the supplied Silo is the host silo. |
| [IoSetHardErrorOrVerifyDevice function](..\ntddk\nf-ntddk-iosetharderrororverifydevice.md) | Lower-level drivers call the IoSetHardErrorOrVerifyDevice routine to identify a removable media device that has encountered an error, so that a file system driver can prompt the user to verify that the medium is valid. |
| [IoGetInitiatorProcess function](..\ntddk\nf-ntddk-iogetinitiatorprocess.md) | The IoGetInitiatorProcess routine retrieves the process which initiated the creation of a file object if different than the process which is issuing the create. |
| [PsSetCreateThreadNotifyRoutine function](..\ntddk\nf-ntddk-pssetcreatethreadnotifyroutine.md) | The PsSetCreateThreadNotifyRoutine routine registers a driver-supplied callback that is subsequently notified when a new thread is created and when such a thread is deleted. |
| [KeRaiseIrqlToDpcLevel function](..\ntddk\nf-ntddk-keraiseirqltodpclevel~r3.md) | The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [IoQueryFullDriverPath function](..\ntddk\nf-ntddk-ioqueryfulldriverpath.md) | The IoQueryFullDriverPath routine retrieves the full path name of the binary file that is loaded for the specified driver object. |
| [PsRemoveSiloContext function](..\ntddk\nf-ntddk-psremovesilocontext.md) | This routine removes an object that was inserted in the Silo. |
| [PsGetCurrentServerSilo function](..\ntddk\nf-ntddk-psgetcurrentserversilo.md) | This routine returns the effective server silo for the thread. |
| [PsGetJobSilo function](..\ntddk\nf-ntddk-psgetjobsilo.md) | This routine returns the first job in the hierarchy that is a Silo. The returned pointer is valid as long as the supplied Job object remains referenced. |
| [PsTerminateServerSilo function](..\ntddk\nf-ntddk-psterminateserversilo.md) | This routine terminates the specified silo. |
| [RtlCharToInteger function](..\ntddk\nf-ntddk-rtlchartointeger.md) | The RtlCharToInteger routine converts a single-byte character string to an integer value in the specified base. |
| [PsGetEffectiveServerSilo function](..\ntddk\nf-ntddk-psgeteffectiveserversilo.md) | This routine traverses the parent chain of the Silo until finding the effective server silo or host silo. |
| [KeGetCurrentProcessorNumber function](..\ntddk\nf-ntddk-kegetcurrentprocessornumber~r3.md) | The KeGetCurrentProcessorNumber routine returns the system-assigned number of the current processor on which the caller is running. |
| [KeRaiseIrqlToDpcLevel function](..\ntddk\nf-ntddk-keraiseirqltodpclevel~r2.md) | The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [SeSinglePrivilegeCheck function](..\ntddk\nf-ntddk-sesingleprivilegecheck.md) | The SeSinglePrivilegeCheck routine checks for the passed privilege value in the context of the current thread. |
| [PsGetCurrentProcessId function](..\ntddk\nf-ntddk-psgetcurrentprocessid.md) | The PsGetCurrentProcessId routine identifies the current thread's process. |
| [KeSetTargetProcessorDpc function](..\ntddk\nf-ntddk-kesettargetprocessordpc.md) | The KeSetTargetProcessorDpc routine specifies the processor that a DPC routine will be run on. |
| [MmGetPhysicalAddress function](..\ntddk\nf-ntddk-mmgetphysicaladdress.md) | The MmGetPhysicalAddress routine returns the physical address corresponding to a valid nonpaged virtual address. |
| [KeQueryMaximumProcessorCount function](..\ntddk\nf-ntddk-kequerymaximumprocessorcount.md) | The KeQueryMaximumProcessorCount routine returns the maximum number of processors. |
| [KeSetHardwareCounterConfiguration function](..\ntddk\nf-ntddk-kesethardwarecounterconfiguration.md) | The KeSetHardwareCounterConfiguration routine specifies a list of hardware counters to use for thread profiling. |
| [IoAssignArcName function](..\ntddk\nf-ntddk-ioassignarcname.md) | The IoAssignArcName routine creates a symbolic link between the ARC name of a physical device and the name of the corresponding device object when it has been created. |
| [IoRaiseInformationalHardError function](..\ntddk\nf-ntddk-ioraiseinformationalharderror.md) | The IoRaiseInformationalHardError routine sends a dialog box to the user, warning about a device I/O error that indicates why a user I/O request failed. |
| [PsGetJobServerSilo function](..\ntddk\nf-ntddk-psgetjobserversilo.md) | This routine returns the effective ServerSilo for the job. The returned pointer is valid as long as the supplied Job object remains referenced. |
| [MmFreeNonCachedMemory function](..\ntddk\nf-ntddk-mmfreenoncachedmemory.md) | The MmFreeNonCachedMemory routine releases a range of noncached memory that was allocated by the MmAllocateNonCachedMemory routine. |
| [PsCreateSiloContext function](..\ntddk\nf-ntddk-pscreatesilocontext.md) | This routine creates an object that will be inserted in a Silo. |
| [KeQueryTickCount function](..\ntddk\nf-ntddk-kequerytickcount~r2.md) | The KeQueryTickCount routine maintains a count of the interval timer interrupts that have occurred since the system was booted. |
| [RtlEqualString function](..\ntddk\nf-ntddk-rtlequalstring.md) | The RtlEqualString routine compares two counted strings to determine whether they are equal. |
| [IoSetSystemPartition function](..\ntddk\nf-ntddk-iosetsystempartition.md) | The IoSetSystemPartition routine sets the boot partition for the system. |
| [PsRegisterSiloMonitor function](..\ntddk\nf-ntddk-psregistersilomonitor.md) | This routine registers a server silo monitor that can receive notifications about server silo events. |
| [PsReplaceSiloContext function](..\ntddk\nf-ntddk-psreplacesilocontext.md) | This routine inserts an object in a Silo. |
| [IoDeassignArcName function](..\ntddk\nf-ntddk-iodeassignarcname.md) | The IoDeassignArcName routine removes a symbolic link between the ARC name for a device and the named device object. |
| [MmSecureVirtualMemory function](..\ntddk\nf-ntddk-mmsecurevirtualmemory.md) | The MmSecureVirtualMemory routine secures a user-space memory address range so that it cannot be freed and its protection type cannot be made more restrictive. |
| [MmFreeContiguousMemory function](..\ntddk\nf-ntddk-mmfreecontiguousmemory.md) | The MmFreeContiguousMemory routine releases a range of physically contiguous memory that was allocated by an MmAllocateContiguousMemoryXxx routine. |
| [IoIsValidIrpStatus function](..\ntddk\nf-ntddk-ioisvalidirpstatus.md) | The IoIsValidIrpStatus routine validates the specified NTSTATUS status code value. |
| [RtlValidateCorrelationVector function](..\ntddk\nf-ntddk-rtlvalidatecorrelationvector.md) | Validates the specified correlation vector to check whether it conforms to the Correlation Vector Specification (v2). |
| [PsGetSiloContext function](..\ntddk\nf-ntddk-psgetsilocontext.md) | This routine retrieves the silo context from the specified silo and slot. |
| [KeRaiseIrqlToDpcLevel function](..\ntddk\nf-ntddk-keraiseirqltodpclevel.md) | The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [RtlConvertLongToLuid function](..\ntddk\nf-ntddk-rtlconvertlongtoluid.md) | The RtlConvertLongToLuid routine converts a long integer to a locally unique identifier (LUID), which is used by the system to represent a security privilege. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PCREATE_PROCESS_NOTIFY_ROUTINE callback](..\ntddk\nc-ntddk-pcreate-process-notify-routine.md) | Process-creation callback implemented by a driver to track the system-wide creation and deletion of processes against the driver's internal state. |
| [PLOAD_IMAGE_NOTIFY_ROUTINE callback](..\ntddk\nc-ntddk-pload-image-notify-routine.md) | Called by the operating system to notify the driver when a driver image or a user image (for example, a DLL or EXE) is mapped into virtual memory. |
| [PCREATE_THREAD_NOTIFY_ROUTINE callback](..\ntddk\nc-ntddk-pcreate-thread-notify-routine.md) | A callback routine implemented by a driver to notify the caller when a thread is created or deleted. |
| [SILO_MONITOR_CREATE_CALLBACK callback](..\ntddk\nc-ntddk-silo-monitor-create-callback.md) | This is callback is invoked when a new silo is created. |
| [SILO_CONTEXT_CLEANUP_CALLBACK callback](..\ntddk\nc-ntddk-silo-context-cleanup-callback.md) | This callback is invoked when the context object reaches a reference count of zero. |
| [PCREATE_PROCESS_NOTIFY_ROUTINE_EX callback](..\ntddk\nc-ntddk-pcreate-process-notify-routine-ex.md) | A callback routine implemented by a driver to notify the caller when a process is created or exits. |
| [SILO_MONITOR_TERMINATE_CALLBACK callback](..\ntddk\nc-ntddk-silo-monitor-terminate-callback.md) | This callback is invoked when a silo is terminated. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [HARDWARE_COUNTER structure](..\ntddk\ns-ntddk--hardware-counter.md) | The HARDWARE_COUNTER structure contains information about a hardware counter. |
| [POWER_THROTTLING_THREAD_STATE structure](..\ntddk\ns-ntddk--power-throttling-thread-state.md) | Stores the throttling policies and how to apply them to a target thread when that thread is subject to power management. |
| [BDCB_STATUS_UPDATE_CONTEXT structure](..\ntddk\ns-ntddk--bdcb-status-update-context.md) | The BDCB_STATUS_UPDATE_CONTEXT structure describes a status update provided by Windows to a boot-start driver's BOOT_DRIVER_CALLBACK_FUNCTION routine. |
| [CORRELATION_VECTOR structure](..\ntddk\ns-ntddk-correlation-vector.md) | Store the correlation vector that is used to reference events and the generated logs for diagnostic purposes. |
| [MM_COPY_ADDRESS structure](..\ntddk\ns-ntddk--mm-copy-address.md) | The MM_COPY_ADDRESS structure contains either a virtual memory address or a physical memory address. |
| [FILE_ATTRIBUTE_TAG_INFORMATION structure](..\ntddk\ns-ntddk--file-attribute-tag-information.md) | The FILE_ATTRIBUTE_TAG_INFORMATION structure is used as an argument to ZwQueryInformationFile. |
| [CONTROLLER_OBJECT structure](..\ntddk\ns-ntddk--controller-object.md) | A controller object represents a hardware adapter or controller with homogenous devices that are the actual targets for I/O requests. |
| [PS_CREATE_NOTIFY_INFO structure](..\ntddk\ns-ntddk--ps-create-notify-info.md) | The PS_CREATE_NOTIFY_INFO structure provides information about a newly created process. |
| [FILE_NAME_INFORMATION structure](..\ntddk\ns-ntddk--file-name-information.md) | The FILE_NAME_INFORMATION structure is used as argument to the ZwQueryInformationFile and ZwSetInformationFile routines. |
| [IMAGE_INFO_EX structure](..\ntddk\ns-ntddk--image-info-ex.md) | Extended version of the image information structure (see IMAGE_INFO). |
| [KEY_CACHED_INFORMATION structure](..\ntddk\ns-ntddk--key-cached-information.md) | The KEY_CACHED_INFORMATION structure holds the cached information available for a registry key or subkey. |
| [PHYSICAL_COUNTER_RESOURCE_LIST structure](..\ntddk\ns-ntddk--physical-counter-resource-list.md) | The PHYSICAL_COUNTER_RESOURCE_LIST structure describes an array of PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structures. |
| [PROCESS_READWRITEVM_LOGGING_INFORMATION structure](..\ntddk\ns-ntddk--process-readwritevm-logging-information.md) | Stores options for read/write access for telemetry per process. |
| [PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY structure](..\ntddk\ns-ntddk--process-mitigation-payload-restriction-policy.md) | Stores information about process mitigation policy. |
| [PNP_LOCATION_INTERFACE structure](..\ntddk\ns-ntddk--pnp-location-interface.md) | The PNP_LOCATION_INTERFACE structure describes the GUID_PNP_LOCATION_INTERFACE interface. |
| [FILE_END_OF_FILE_INFORMATION structure](..\ntddk\ns-ntddk--file-end-of-file-information.md) | The FILE_END_OF_FILE_INFORMATION structure is used as an argument to the ZwSetInformationFile routine. |
| [POWER_THROTTLING_PROCESS_STATE structure](..\ntddk\ns-ntddk--power-throttling-process-state.md) | Stores the throttling policies and how to apply them to a target process when that process is subject to power management. |
| [PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structure](..\ntddk\ns-ntddk--physical-counter-resource-descriptor.md) | The PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structure describes the counter resources available on the platform. |
| [KEY_VIRTUALIZATION_INFORMATION structure](..\ntddk\ns-ntddk--key-virtualization-information.md) | The KEY_VIRTUALIZATION_INFORMATION structure defines the basic information that is available for a registry key or subkey. |
| [KEY_NAME_INFORMATION structure](..\ntddk\ns-ntddk--key-name-information.md) | The KEY_NAME_INFORMATION structure holds the name and name length of the key. |
| [IMAGE_INFO structure](..\ntddk\ns-ntddk--image-info.md) | Used by driver's load-image routine (PLOAD_IMAGE_NOTIFY_ROUTINE) to specify image information. |
| [FILE_VALID_DATA_LENGTH_INFORMATION structure](..\ntddk\ns-ntddk--file-valid-data-length-information.md) | The FILE_VALID_DATA_LENGTH_INFORMATION structure is used as an argument to ZwSetInformationFile. |
| [PROCESS_MITIGATION_CHILD_PROCESS_POLICY structure](..\ntddk\ns-ntddk--process-mitigation-child-process-policy.md) | Stores policy information about creating child processes. |
| [SILO_MONITOR_REGISTRATION structure](..\ntddk\ns-ntddk--silo-monitor-registration.md) | This structure specifies a server silo monitor that can receive notifications about server silo events. |
| [FILE_ALIGNMENT_INFORMATION structure](..\ntddk\ns-ntddk--file-alignment-information.md) | The FILE_ALIGNMENT_INFORMATION structure is used as an argument to the ZwQueryInformationFile routine. |
| [FILE_DISPOSITION_INFORMATION structure](..\ntddk\ns-ntddk--file-disposition-information.md) | The FILE_DISPOSITION_INFORMATION structure is used as an argument to the ZwSetInformationFile routine. |
| [BDCB_IMAGE_INFORMATION structure](..\ntddk\ns-ntddk--bdcb-image-information.md) | The BDCB_IMAGE_INFORMATION structure describes information about a boot-start driver that is about to be initialized, provided by Windows to a boot-start driver's BOOT_DRIVER_CALLBACK_FUNCTION routine. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [BDCB_CALLBACK_TYPE enumeration](..\ntddk\ne-ntddk--bdcb-callback-type.md) | The BDCB_CALLBACK_TYPE enumeration specifies whether the callback being passed to a BOOT_DRIVER_CALLBACK_FUNCTION routine is a status update or a boot-start driver initialization notification. |
| [PSCREATEPROCESSNOTIFYTYPE enumeration](..\ntddk\ne-ntddk--pscreateprocessnotifytype.md) | Indicates the type of process notification. This enumeration is used in PsSetCreateProcessNotifyRoutineEx2 to register callback notifications. |
| [BUS_DATA_TYPE enumeration](..\ntddk\ne-ntddk--bus-data-type.md) | The BUS_DATA_TYPE enumeration indicates the type of bus configuration space. |
| [PSCREATETHREADNOTIFYTYPE enumeration](..\ntddk\ne-ntddk--pscreatethreadnotifytype.md) | Indicates the type of thread notification. This enumeration is used in PsSetCreateThreadNotifyRoutineEx to register callback notifications associated with thread creation or deletion. |
| [BDCB_STATUS_UPDATE_TYPE enumeration](..\ntddk\ne-ntddk--bdcb-status-update-type.md) | The BDCB_STATUS_UPDATE_TYPE enumeration lists the types of boot-driver callback status updates. |
| [SUBSYSTEM_INFORMATION_TYPE enumeration](..\ntddk\ne-ntddk--subsystem-information-type.md) | Indicates the type of subsystem for a process or thread. This enumeration is used in NtQueryInformationProcess and NtQueryInformationThread calls. |
| [HARDWARE_COUNTER_TYPE enumeration](..\ntddk\ne-ntddk--hardware-counter-type.md) | The HARDWARE_COUNTER_TYPE enumeration specifies the type of a hardware counter. |
| [BDCB_CLASSIFICATION enumeration](..\ntddk\ne-ntddk--bdcb-classification.md) | The BDCB_CLASSIFICATION enumeration lists different classifications of boot start images. |
| [PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR_TYPE enumeration](..\ntddk\ne-ntddk--physical-counter-resource-descriptor-type.md) | The PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR_TYPE enumeration contains constants that indicate the type of hardware performance counter resource that is described by a PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structure. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [IO_ACCESS_TYPE enumeration](..\ntddsfio\ne-ntddsfio--io-access-type.md) | Defines the access rights for Scheduled File I/O (SFIO). |
| [IO_ACCESS_MODE enumeration](..\ntddsfio\ne-ntddsfio--io-access-mode.md) | Defines the types of access mode for Scheduled File I/O (SFIO). |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SYSENV_VARIABLE structure](..\ntddsysenv\ns-ntddsysenv--sysenv-variable.md) | Stores the name a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_GET_VARIABLE request. |
| [SYSENV_VALUE structure](..\ntddsysenv\ns-ntddsysenv--sysenv-value.md) | Stores the value of a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_GET_VARIABLE request. |
| [SYSENV_VARIABLE_INFO structure](..\ntddsysenv\ns-ntddsysenv--sysenv-variable-info.md) | Stores the information about a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_QUERY_VARIABLE_INFO request. |
| [XVARIABLE_NAME structure](..\ntddsysenv\ns-ntddsysenv--xvariable-name.md) | Stores the name of a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_ENUM_VARIABLES request. |
| [XVARIABLE_NAME_AND_VALUE structure](..\ntddsysenv\ns-ntddsysenv--xvariable-name-and-value.md) | Stores the name and value of a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_ENUM_VARIABLES and IOCTL_SYSENV_SET_VARIABLE requests. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_SYSENV_ENUM_VARIABLES IOCTL](..\ntddsysenv\ni-ntddsysenv-ioctl-sysenv-enum-variables.md) | Returns information about system environment variables using SysEnv device. |
| [IOCTL_SYSENV_QUERY_VARIABLE_INFO IOCTL](..\ntddsysenv\ni-ntddsysenv-ioctl-sysenv-query-variable-info.md) | Returns information about system environment variables using SysEnv device. |
| [IOCTL_SYSENV_SET_VARIABLE IOCTL](..\ntddsysenv\ni-ntddsysenv-ioctl-sysenv-set-variable.md) | Sets the value of the specified system environment variables using SysEnv device. |
| [IOCTL_SYSENV_GET_VARIABLE IOCTL](..\ntddsysenv\ni-ntddsysenv-ioctl-sysenv-get-variable.md) | Gets the value of the specified system environment variables using SysEnv device. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RtlUIntPtrToShort function](..\ntintsafe\nf-ntintsafe-rtluintptrtoshort.md) | Converts a value of type UINT_PTR to a value of type SHORT. |
| [RtlShortMult function](..\ntintsafe\nf-ntintsafe-rtlshortmult.md) | Multiplies one value of type SHORT by another. |
| [RtlLongPtrToUInt function](..\ntintsafe\nf-ntintsafe-rtllongptrtouint.md) | Converts a value of type LONG_PTR to a value of type UINT. |
| [RtlIntToInt8 function](..\ntintsafe\nf-ntintsafe-rtlinttoint8.md) | Converts a value of type INT to a value of type INT8. |
| [RtlIntPtrToLongPtr function](..\ntintsafe\nf-ntintsafe-rtlintptrtolongptr.md) | Converts a value of type INT_PTR to a value of type LONG_PTR. |
| [RtlShortToULongLong function](..\ntintsafe\nf-ntintsafe-rtlshorttoulonglong.md) | Converts a value of type SHORT to a value of type ULONGLONG. |
| [RtlShortToUInt8 function](..\ntintsafe\nf-ntintsafe-rtlshorttouint8.md) | Converts a value of type SHORT to a value of type UINT8. |
| [RtlUShortToInt8 function](..\ntintsafe\nf-ntintsafe-rtlushorttoint8.md) | Converts a value of type USHORT to a value of type INT8. |
| [RtlShortAdd function](..\ntintsafe\nf-ntintsafe-rtlshortadd.md) | Adds two values of type SHORT. |
| [RtlInt8Sub function](..\ntintsafe\nf-ntintsafe-rtlint8sub.md) | Subtracts one value of type INT8 from another. |
| [RtlUInt8Mult function](..\ntintsafe\nf-ntintsafe-rtluint8mult.md) | Multiplies one value of type UINT8 by another. |
| [RtlIntPtrToShort function](..\ntintsafe\nf-ntintsafe-rtlintptrtoshort.md) | Converts a value of type INT_PTR to a value of type SHORT. |
| [RtlULongMult function](..\ntintsafe\nf-ntintsafe-rtlulongmult.md) | Multiplies one value of type ULONG by another. |
| [RtlLongLongToUInt8 function](..\ntintsafe\nf-ntintsafe-rtllonglongtouint8.md) | Converts a value of type LONGLONG to a value of type UNIT8. |
| [RtlUIntToIntPtr function](..\ntintsafe\nf-ntintsafe-rtluinttointptr.md) | Converts a value of type UINT to a value of type INT_PTR. |
| [RtlULongLongToULong function](..\ntintsafe\nf-ntintsafe-rtlulonglongtoulong.md) | Converts a value of type ULONGLONG to a value of type ULONG. |
| [RtlUIntToUChar function](..\ntintsafe\nf-ntintsafe-rtluinttouchar.md) | Converts a value of type UINT to a value of type UCHAR. |
| [RtlSIZETAdd function](..\ntintsafe\nf-ntintsafe-rtlsizetadd~r1.md) | Adds two values of type SIZE_T. |
| [RtlULongToInt8 function](..\ntintsafe\nf-ntintsafe-rtlulongtoint8.md) | Converts a value of type ULONG to a value of type INT8. |
| [RtlInt8ToULongPtr function](..\ntintsafe\nf-ntintsafe-rtlint8toulongptr.md) | Converts a value of type INT8 to a value of type ULONG_PTR. |
| [RtlLongToUChar function](..\ntintsafe\nf-ntintsafe-rtllongtouchar.md) | Converts a value of type LONG to a value of type UCHAR. |
| [RtlSSIZETSub function](..\ntintsafe\nf-ntintsafe-rtlssizetsub.md) | Subtracts one value of type SSIZE_T from another. |
| [RtlInt8ToUChar function](..\ntintsafe\nf-ntintsafe-rtlint8touchar.md) | Converts a value of type INT8 to a value of type UCHAR. |
| [RtlIntPtrToULongLong function](..\ntintsafe\nf-ntintsafe-rtlintptrtoulonglong.md) | Converts a value of type INT_PTR to a value of type ULONGLONG. |
| [RtlIntToULongLong function](..\ntintsafe\nf-ntintsafe-rtlinttoulonglong.md) | Converts a value of type INT to a value of type ULONGLONG. |
| [RtlLongLongToUChar function](..\ntintsafe\nf-ntintsafe-rtllonglongtouchar.md) | Converts a value of type LONGLONG to a value of type UCHAR. |
| [RtlShortToUInt function](..\ntintsafe\nf-ntintsafe-rtlshorttouint.md) | Converts a value of type SHORT to a value of type UINT. |
| [RtlUIntSub function](..\ntintsafe\nf-ntintsafe-rtluintsub.md) | Subtracts one value of type UINT from another. |
| [RtlULongToLong function](..\ntintsafe\nf-ntintsafe-rtlulongtolong.md) | Converts a value of type ULONG to a value of type LONG. |
| [RtlInt8ToUInt8 function](..\ntintsafe\nf-ntintsafe-rtlint8touint8.md) | Converts a value of type INT8 to a value of type UINT8. |
| [RtlLongLongToIntPtr function](..\ntintsafe\nf-ntintsafe-rtllonglongtointptr.md) | Converts a value of type LONGLONG to a value of type INT_PTR. |
| [RtlShortToULong function](..\ntintsafe\nf-ntintsafe-rtlshorttoulong.md) | Converts a value of type SHORT to a value of type ULONG. |
| [RtlUIntPtrToInt8 function](..\ntintsafe\nf-ntintsafe-rtluintptrtoint8.md) | Converts a value of type UINT_PTR to a value of type INT8. |
| [RtlUIntPtrToLong function](..\ntintsafe\nf-ntintsafe-rtluintptrtolong.md) | Converts a value of type UINT_PTR to a value of type LONG. |
| [RtlIntToULong function](..\ntintsafe\nf-ntintsafe-rtlinttoulong.md) | Converts a value of type INT to a value of type ULONG. |
| [RtlLongMult function](..\ntintsafe\nf-ntintsafe-rtllongmult.md) | Multiplies one value of type LONG by another. |
| [RtlIntToUShort function](..\ntintsafe\nf-ntintsafe-rtlinttoushort.md) | Converts a value of type INT to a value of type USHORT. |
| [RtlUInt8ToInt8 function](..\ntintsafe\nf-ntintsafe-rtluint8toint8.md) | Converts a value of type UINT8 to a value of type INT8. |
| [RtlULongPtrSub function](..\ntintsafe\nf-ntintsafe-rtlulongptrsub.md) | Subtracts one value of type ULONG_PTR from another. |
| [RtlInt8Add function](..\ntintsafe\nf-ntintsafe-rtlint8add.md) | Adds two values of type INT8. |
| [RtlULongToUIntPtr function](..\ntintsafe\nf-ntintsafe-rtlulongtouintptr.md) | Converts a value of type ULONG_PTR to a value of type UINT_PTR. |
| [RtlLongLongSub function](..\ntintsafe\nf-ntintsafe-rtllonglongsub.md) | Subtracts one value of type LONGLONG from another. |
| [RtlPtrdiffTMult function](..\ntintsafe\nf-ntintsafe-rtlptrdifftmult.md) | Multiplies one value of type PTRDIFF_T by another. |
| [RtlSizeTSub function](..\ntintsafe\nf-ntintsafe-rtlsizetsub.md) | Subtracts one value of type SIZE_T from another. |
| [RtlShortToULongPtr function](..\ntintsafe\nf-ntintsafe-rtlshorttoulongptr.md) | Converts a value of type SHORT to a value of type ULONG_PTR. |
| [RtlLongPtrToInt8 function](..\ntintsafe\nf-ntintsafe-rtllongptrtoint8.md) | Converts a value of type LONG_PTR to a value of type INT8. |
| [RtlUIntPtrToUInt16 function](..\ntintsafe\nf-ntintsafe-rtluintptrtouint16.md) | Converts a value of type UINT_PTR to a value of type UINT16. |
| [RtlULongLongToShort function](..\ntintsafe\nf-ntintsafe-rtlulonglongtoshort.md) | Converts a value of type ULONGLONG to a value of type SHORT. |
| [RtlShortToInt8 function](..\ntintsafe\nf-ntintsafe-rtlshorttoint8.md) | Converts a value of type SHORT to a value of type INT8. |
| [RtlULongPtrToUShort function](..\ntintsafe\nf-ntintsafe-rtlulongptrtoushort.md) | Converts a value of type ULONG_PTR to a value of type USHORT. |
| [RtlULongLongToUShort function](..\ntintsafe\nf-ntintsafe-rtlulonglongtoushort.md) | Converts a value of type ULONGLONG to a value of type USHORT. |
| [RtlSIZETSub function](..\ntintsafe\nf-ntintsafe-rtlsizetsub~r1.md) | Subtracts one value of type SIZE_T from another. |
| [RtlUIntPtrToIntPtr function](..\ntintsafe\nf-ntintsafe-rtluintptrtointptr.md) | Converts a value of type UINT_PTR to a value of type INT_PTR. |
| [RtlULongPtrToInt8 function](..\ntintsafe\nf-ntintsafe-rtlulongptrtoint8.md) | Converts a value of type ULONG_PTR to a value of type INT8. |
| [RtlLongPtrToInt function](..\ntintsafe\nf-ntintsafe-rtllongptrtoint.md) | Converts a value of type LONG_PTR to a value of type INT. |
| [RtlUIntPtrToLongLong function](..\ntintsafe\nf-ntintsafe-rtluintptrtolonglong.md) | Converts a value of type UINT_PTR to a value of type LONGLONG. |
| [RtlLongLongToShort function](..\ntintsafe\nf-ntintsafe-rtllonglongtoshort.md) | Converts a value of type LONGLONG to a value of type SHORT. |
| [RtlULongToUInt function](..\ntintsafe\nf-ntintsafe-rtlulongtouint.md) | Converts a value of type ULONG to a value of type UINT. |
| [RtlULongLongMult function](..\ntintsafe\nf-ntintsafe-rtlulonglongmult.md) | Multiplies one value of type ULONGLONG by another. |
| [RtlLongPtrToUChar function](..\ntintsafe\nf-ntintsafe-rtllongptrtouchar.md) | Converts a value of type LONG_PTR to a value of type UCHAR. |
| [RtlLongPtrToULongPtr function](..\ntintsafe\nf-ntintsafe-rtllongptrtoulongptr.md) | Converts a value of type LONG_PTR to a value of type ULONG_PTR. |
| [RtlIntPtrToUInt function](..\ntintsafe\nf-ntintsafe-rtlintptrtouint.md) | Converts a value of type INT_PTR to a value of type UINT. |
| [RtlULongPtrAdd function](..\ntintsafe\nf-ntintsafe-rtlulongptradd.md) | Adds two values of type ULONG_PTR. |
| [RtlULongToUInt8 function](..\ntintsafe\nf-ntintsafe-rtlulongtouint8.md) | Converts a value of type ULONG_PTR to a value of type UINT8. |
| [RtlUShortToChar function](..\ntintsafe\nf-ntintsafe-rtlushorttochar.md) | Converts a value of type USHORT to a value of type CHAR. |
| [RtlIntAdd function](..\ntintsafe\nf-ntintsafe-rtlintadd.md) | Adds two values of type INT. |
| [RtlULongLongToUChar function](..\ntintsafe\nf-ntintsafe-rtlulonglongtouchar.md) | Converts a value of type ULONGLONG to a value of type UCHAR. |
| [RtlLongPtrToIntPtr function](..\ntintsafe\nf-ntintsafe-rtllongptrtointptr.md) | Converts a value of type LONG_PTR to a value of type INT_PTR. |
| [RtlShortToUShort function](..\ntintsafe\nf-ntintsafe-rtlshorttoushort.md) | Converts a value of type SHORT to a value of type USHORT. |
| [RtlIntPtrToULong function](..\ntintsafe\nf-ntintsafe-rtlintptrtoulong.md) | Converts a value of type INT_PTR to a value of type ULONG. |
| [RtlIntPtrToULongPtr function](..\ntintsafe\nf-ntintsafe-rtlintptrtoulongptr.md) | Converts a value of type INT_PTR to a value of type ULONG_PTR. |
| [RtlIntPtrToUIntPtr function](..\ntintsafe\nf-ntintsafe-rtlintptrtouintptr.md) | Converts a value of type INT_PTR to a value of type UINT_PTR. |
| [RtlLongToUIntPtr function](..\ntintsafe\nf-ntintsafe-rtllongtouintptr.md) | Converts a value of type LONG to a value of type UINT_PTR. |
| [RtlULongPtrToUIntPtr function](..\ntintsafe\nf-ntintsafe-rtlulongptrtouintptr.md) | Converts a value of type ULONG_PTR to a value of type UINT_PTR. |
| [RtlByteToChar function](..\ntintsafe\nf-ntintsafe-rtlbytetochar.md) | Converts a value of type BYTE to a value of type CHAR. |
| [RtlIntPtrToChar function](..\ntintsafe\nf-ntintsafe-rtlintptrtochar.md) | Converts a value of type INT_PTR to a value of type CHAR. |
| [RtlIntPtrToUShort function](..\ntintsafe\nf-ntintsafe-rtlintptrtoushort.md) | Converts a value of type INT_PTR to a value of type USHORT. |
| [RtlLongToIntPtr function](..\ntintsafe\nf-ntintsafe-rtllongtointptr.md) | Converts a value of type LONG to a value of type INT_PTR. |
| [RtlUShortToShort function](..\ntintsafe\nf-ntintsafe-rtlushorttoshort.md) | Converts a value of type USHORT to a value of type SHORT. |
| [RtlUIntPtrToInt16 function](..\ntintsafe\nf-ntintsafe-rtluintptrtoint16.md) | Converts a value of type UINT_PTR to a value of type INT16. |
| [RtlULongToChar function](..\ntintsafe\nf-ntintsafe-rtlulongtochar.md) | Converts a value of type ULONG to a value of type CHAR. |
| [RtlLongToULongPtr function](..\ntintsafe\nf-ntintsafe-rtllongtoulongptr.md) | Converts a value of type LONG to a value of type ULONG_PTR. |
| [RtlLongLongAdd function](..\ntintsafe\nf-ntintsafe-rtllonglongadd.md) | Adds two values of type LONGLONG. |
| [RtlULongLongToInt8 function](..\ntintsafe\nf-ntintsafe-rtlulonglongtoint8.md) | Converts a value of type ULONGLONG to a value of type INT8. |
| [RtlULongLongToLongPtr function](..\ntintsafe\nf-ntintsafe-rtlulonglongtolongptr.md) | Converts a value of type ULONGLONG to a value of type LONG_PTR. |
| [RtlULongPtrToIntPtr function](..\ntintsafe\nf-ntintsafe-rtlulongptrtointptr.md) | Converts a value of type ULONG_PTR to a value of type INT_PTR. |
| [RtlLongPtrToUShort function](..\ntintsafe\nf-ntintsafe-rtllongptrtoushort.md) | Converts a value of type LONG_PTR to a value of type USHORT. |
| [RtlIntPtrAdd function](..\ntintsafe\nf-ntintsafe-rtlintptradd.md) | Adds two values of type INT_PTR. |
| [RtlULongToIntPtr function](..\ntintsafe\nf-ntintsafe-rtlulongtointptr.md) | Converts a value of type ULONG to a value of type INT_PTR. |
| [RtlLongLongToLongPtr function](..\ntintsafe\nf-ntintsafe-rtllonglongtolongptr.md) | Converts a value of type LONGLONG to a value of type LONG_PTR. |
| [RtlIntMult function](..\ntintsafe\nf-ntintsafe-rtlintmult.md) | Multiplies one value of type INT by another. |
| [RtlUIntPtrToUChar function](..\ntintsafe\nf-ntintsafe-rtluintptrtouchar.md) | Converts a value of type UINT_PTR to a value of type UCHAR. |
| [RtlLongAdd function](..\ntintsafe\nf-ntintsafe-rtllongadd.md) | Adds two values of type LONG. |
| [RtlULongLongToUIntPtr function](..\ntintsafe\nf-ntintsafe-rtlulonglongtouintptr.md) | Converts a value of type ULONGLONG to a value of type UINT_PTR. |
| [RtlUInt8Add function](..\ntintsafe\nf-ntintsafe-rtluint8add.md) | Adds two values of type UINT8. |
| [RtlInt8ToUInt function](..\ntintsafe\nf-ntintsafe-rtlint8touint.md) | Converts a value of type INT8 to a value of type UINT. |
| [RtlLongToChar function](..\ntintsafe\nf-ntintsafe-rtllongtochar.md) | Converts a value of type LONG to a value of type CHAR. |
| [RtlUIntToInt8 function](..\ntintsafe\nf-ntintsafe-rtluinttoint8.md) | Converts a value of type UINT to a value of type INT8. |
| [RtlLongPtrToLong function](..\ntintsafe\nf-ntintsafe-rtllongptrtolong.md) | Converts a value of type LONG_PTR to a value of type LONG. |
| [RtlULongPtrToLongLong function](..\ntintsafe\nf-ntintsafe-rtlulongptrtolonglong.md) | Converts a value of type ULONG_PTR to a value of type LONGLONG. |
| [RtlLongToUInt8 function](..\ntintsafe\nf-ntintsafe-rtllongtouint8.md) | Converts a value of type LONG to a value of type UINT8. |
| [RtlULongPtrToChar function](..\ntintsafe\nf-ntintsafe-rtlulongptrtochar.md) | Converts a value of type ULONG_PTR to a value of type CHAR. |
| [RtlUShortMult function](..\ntintsafe\nf-ntintsafe-rtlushortmult.md) | Multiplies one value of type USHORT by another. |
| [RtlUIntPtrSub function](..\ntintsafe\nf-ntintsafe-rtluintptrsub.md) | Subtracts one value of type UINT_PTR from another. |
| [RtlLongPtrMult function](..\ntintsafe\nf-ntintsafe-rtllongptrmult.md) | Multiplies one value of type LONG_PTR by another. |
| [RtlLongPtrToUIntPtr function](..\ntintsafe\nf-ntintsafe-rtllongptrtouintptr.md) | Converts a value of type LONG_PTR to a value of type UINT_PTR. |
| [RtlULongLongToChar function](..\ntintsafe\nf-ntintsafe-rtlulonglongtochar.md) | Converts a value of type ULONGLONG to a value of type CHAR. |
| [RtlDWordPtrSub function](..\ntintsafe\nf-ntintsafe-rtldwordptrsub.md) | Subtracts one value of type DWORD_PTR from another. |
| [RtlULongPtrToLong function](..\ntintsafe\nf-ntintsafe-rtlulongptrtolong.md) | Converts a value of type ULONG_PTR to a value of type LONG. |
| [RtlUIntPtrToULong function](..\ntintsafe\nf-ntintsafe-rtluintptrtoulong.md) | Converts a value of type UINT_PTR to a value of type LONG. |
| [RtlUIntToChar function](..\ntintsafe\nf-ntintsafe-rtluinttochar.md) | Converts a value of type UINT to a value of type CHAR. |
| [RtlULongPtrToULong function](..\ntintsafe\nf-ntintsafe-rtlulongptrtoulong.md) | Converts a value of type ULONG_PTR to a value of type ULONG. |
| [RtlIntToChar function](..\ntintsafe\nf-ntintsafe-rtlinttochar.md) | Converts a value of type INT to a value of type CHAR. |
| [RtlShortSub function](..\ntintsafe\nf-ntintsafe-rtlshortsub.md) | Subtracts one value of type SHORT from another. |
| [RtlIntSub function](..\ntintsafe\nf-ntintsafe-rtlintsub.md) | Subtracts one value of type INT from another. |
| [RtlByteToInt8 function](..\ntintsafe\nf-ntintsafe-rtlbytetoint8.md) | Converts a value of type BYTE to a value of type INT8. |
| [RtlUIntPtrToChar function](..\ntintsafe\nf-ntintsafe-rtluintptrtochar.md) | Converts a value of type UINT_PTR to a value of type CHAR. |
| [RtlIntPtrToLong function](..\ntintsafe\nf-ntintsafe-rtlintptrtolong.md) | Converts a value of type INT_PTR to a value of type LONG. |
| [RtlULongSub function](..\ntintsafe\nf-ntintsafe-rtlulongsub.md) | Subtracts one value of type ULONG from another. |
| [RtlIntPtrToUInt8 function](..\ntintsafe\nf-ntintsafe-rtlintptrtouint8.md) | Converts a value of type INT_PTR to a value of type UINT8. |
| [RtlUIntToLongPtr function](..\ntintsafe\nf-ntintsafe-rtluinttolongptr.md) | Converts a value of type UINT to a value of type LONG_PTR. |
| [RtlUIntAdd function](..\ntintsafe\nf-ntintsafe-rtluintadd.md) | Adds two values of type UINT. |
| [RtlLongPtrToUInt8 function](..\ntintsafe\nf-ntintsafe-rtllongptrtouint8.md) | Converts a value of type LONG_PTR to a value of type UINT8. |
| [RtlULongPtrToShort function](..\ntintsafe\nf-ntintsafe-rtlulongptrtoshort.md) | Converts a value of type ULONG_PTR to a value of type SHORT. |
| [RtlUShortAdd function](..\ntintsafe\nf-ntintsafe-rtlushortadd.md) | Adds two values of type USHORT. |
| [RtlUShortToUInt8 function](..\ntintsafe\nf-ntintsafe-rtlushorttouint8.md) | Converts a value of type USHORT to a value of type UINT8. |
| [RtlLongToShort function](..\ntintsafe\nf-ntintsafe-rtllongtoshort.md) | Converts a value of type LONG to a value of type SHORT. |
| [RtlULongPtrToLongPtr function](..\ntintsafe\nf-ntintsafe-rtlulongptrtolongptr.md) | Converts a value of type ULONG_PTR to a value of type LONG_PTR. |
| [RtlIntPtrSub function](..\ntintsafe\nf-ntintsafe-rtlintptrsub.md) | Subtracts one value of type INT_PTR from another. |
| [RtlLongPtrToChar function](..\ntintsafe\nf-ntintsafe-rtllongptrtochar.md) | Converts a value of type LONG_PTR to a value of type CHAR. |
| [RtlDWordPtrAdd function](..\ntintsafe\nf-ntintsafe-rtldwordptradd.md) | Adds two values of type DWORD_PTR. |
| [RtlUIntToLong function](..\ntintsafe\nf-ntintsafe-rtluinttolong.md) | Converts a value of type UINT to a value of type LONG. |
| [RtlUShortSub function](..\ntintsafe\nf-ntintsafe-rtlushortsub.md) | Subtracts one value of type USHORT from another. |
| [RtlULongPtrToUChar function](..\ntintsafe\nf-ntintsafe-rtlulongptrtouchar.md) | Converts a value of type ULONG_PTR to a value of type UCHAR. |
| [RtlULongLongToUInt function](..\ntintsafe\nf-ntintsafe-rtlulonglongtouint.md) | Converts a value of type ULONGLONG to a value of type UINT. |
| [RtlLongLongToChar function](..\ntintsafe\nf-ntintsafe-rtllonglongtochar.md) | Converts a value of type LONGLONG to a value of type CHAR. |
| [RtlUIntPtrMult function](..\ntintsafe\nf-ntintsafe-rtluintptrmult.md) | Multiplies one value of type UINT_PTR by another. |
| [RtlULongLongToUInt8 function](..\ntintsafe\nf-ntintsafe-rtlulonglongtouint8.md) | Converts a value of type ULONGLONG to a value of type UINT8. |
| [RtlShortToUChar function](..\ntintsafe\nf-ntintsafe-rtlshorttouchar.md) | Converts a value of type SHORT to a value of type UCHAR. |
| [RtlLongLongToULong function](..\ntintsafe\nf-ntintsafe-rtllonglongtoulong.md) | Converts a value of type LONGLONG to a value of type ULONG. |
| [RtlSizeTMult function](..\ntintsafe\nf-ntintsafe-rtlsizetmult.md) | Multiplies one value of type SIZE_T by another. |
| [RtlLongLongMult function](..\ntintsafe\nf-ntintsafe-rtllonglongmult.md) | Multiplies one value of type LONGLONG by another. |
| [RtlLongPtrAdd function](..\ntintsafe\nf-ntintsafe-rtllongptradd.md) | Adds two values of type LONG_PTR. |
| [RtlUInt8Sub function](..\ntintsafe\nf-ntintsafe-rtluint8sub.md) | The RtlUInt8Sub routine subtracts one value of type UINT8 from another. |
| [RtlUIntToUInt8 function](..\ntintsafe\nf-ntintsafe-rtluinttouint8.md) | Converts a value of type UINT to a value of type UINT8. |
| [RtlInt8ToUIntPtr function](..\ntintsafe\nf-ntintsafe-rtlint8touintptr.md) | Converts a value of type INT8 to a value of type UINT_PTR. |
| [RtlULongPtrToUInt8 function](..\ntintsafe\nf-ntintsafe-rtlulongptrtouint8.md) | Converts a value of type ULONG_PTR to a value of type UINT8. |
| [RtlUIntToUShort function](..\ntintsafe\nf-ntintsafe-rtluinttoushort.md) | Converts a value of type UINT to a value of type USHORT. |
| [RtlUIntPtrToUInt function](..\ntintsafe\nf-ntintsafe-rtluintptrtouint.md) | Converts a value of type UINT_PTR to a value of type UINT. |
| [RtlLongSub function](..\ntintsafe\nf-ntintsafe-rtllongsub.md) | Subtracts one value of type LONG from another. |
| [RtlIntToUInt function](..\ntintsafe\nf-ntintsafe-rtlinttouint.md) | Converts a value of type INT to a value of type UINT. |
| [RtlULongToLongPtr function](..\ntintsafe\nf-ntintsafe-rtlulongtolongptr.md) | Converts a value of type ULONG to a value of type LONG_PTR. |
| [RtlIntPtrToInt function](..\ntintsafe\nf-ntintsafe-rtlintptrtoint.md) | Converts a value of type INT_PTR to a value of type INT. |
| [RtlUShortToUChar function](..\ntintsafe\nf-ntintsafe-rtlushorttouchar.md) | Converts a value of type USHORT to a value of type UCHAR. |
| [RtlLongPtrToULongLong function](..\ntintsafe\nf-ntintsafe-rtllongptrtoulonglong.md) | Converts a value of type LONG_PTR to a value of type ULONGLONG. |
| [RtlIntPtrMult function](..\ntintsafe\nf-ntintsafe-rtlintptrmult.md) | Multiplies one value of type INT_PTR by another. |
| [RtlUIntPtrAdd function](..\ntintsafe\nf-ntintsafe-rtluintptradd.md) | Adds two values of type UINT_PTR. |
| [RtlLongToULongLong function](..\ntintsafe\nf-ntintsafe-rtllongtoulonglong.md) | Converts a value of type LONG to a value of type ULONGLONG. |
| [RtlUIntPtrToUInt8 function](..\ntintsafe\nf-ntintsafe-rtluintptrtouint8.md) | Converts a value of type UINT_PTR to a value of type UINT8. |
| [RtlLongToUInt function](..\ntintsafe\nf-ntintsafe-rtllongtouint.md) | Converts a value of type LONG to a value of type UINT. |
| [RtlPtrdiffTSub function](..\ntintsafe\nf-ntintsafe-rtlptrdifftsub.md) | Subtracts one value of type PTRDIFF_T from another. |
| [RtlIntPtrToUChar function](..\ntintsafe\nf-ntintsafe-rtlintptrtouchar.md) | Converts a value of type INT_PTR to a value of type UCHAR. |
| [RtlULongLongToInt function](..\ntintsafe\nf-ntintsafe-rtlulonglongtoint.md) | Converts a value of type ULONGLONG to a value of type INT. |
| [RtlSizeTAdd function](..\ntintsafe\nf-ntintsafe-rtlsizetadd.md) | Adds two values of type SIZE_T. |
| [RtlSSIZETMult function](..\ntintsafe\nf-ntintsafe-rtlssizetmult.md) | Multiplies one value of type SSIZE_T by another. |
| [RtlInt8ToULong function](..\ntintsafe\nf-ntintsafe-rtlint8toulong.md) | Converts a value of type INT8 to a value of type ULONG. |
| [RtlULongLongSub function](..\ntintsafe\nf-ntintsafe-rtlulonglongsub.md) | Subtracts one value of type ULONGLONG from another. |
| [RtlIntToUInt8 function](..\ntintsafe\nf-ntintsafe-rtlinttouint8.md) | Converts a value of type INT to a value of type UINT8. |
| [RtlULongLongToULongPtr function](..\ntintsafe\nf-ntintsafe-rtlulonglongtoulongptr.md) | Converts a value of type ULONGLONG to a value of type ULONG_PTR. |
| [RtlUIntPtrToInt function](..\ntintsafe\nf-ntintsafe-rtluintptrtoint.md) | Converts a value of type UINT_PTR to a value of type INT. |
| [RtlULongToUShort function](..\ntintsafe\nf-ntintsafe-rtlulongtoushort.md) | Converts a value of type ULONG to a value of type USHORT. |
| [RtlLongLongToInt function](..\ntintsafe\nf-ntintsafe-rtllonglongtoint.md) | Converts a value of type LONGLONG to a value of type INT. |
| [RtlIntToShort function](..\ntintsafe\nf-ntintsafe-rtlinttoshort.md) | Converts a value of type INT to a value of type SHORT. |
| [RtlPtrdiffTAdd function](..\ntintsafe\nf-ntintsafe-rtlptrdifftadd.md) | Adds two values of type PTRDIFF_T. |
| [RtlLongToInt function](..\ntintsafe\nf-ntintsafe-rtllongtoint.md) | Converts a value of type LONG to a value of type INT. |
| [RtlIntPtrToInt8 function](..\ntintsafe\nf-ntintsafe-rtlintptrtoint8.md) | Converts a value of type INT_PTR to a value of type INT8. |
| [RtlULongLongToLong function](..\ntintsafe\nf-ntintsafe-rtlulonglongtolong.md) | Converts a value of type ULONGLONG to a value of type LONG. |
| [RtlULongToInt function](..\ntintsafe\nf-ntintsafe-rtlulongtoint.md) | Converts a value of type ULONG to a value of type INT. |
| [RtlULongAdd function](..\ntintsafe\nf-ntintsafe-rtlulongadd.md) | Adds two values of type ULONG. |
| [RtlULongLongAdd function](..\ntintsafe\nf-ntintsafe-rtlulonglongadd.md) | Adds two values of type ULONGLONG. |
| [RtlUIntPtrToLongPtr function](..\ntintsafe\nf-ntintsafe-rtluintptrtolongptr.md) | Converts a value of type UINT_PTR to a value of type LONG_PTR. |
| [RtlShortToUIntPtr function](..\ntintsafe\nf-ntintsafe-rtlshorttouintptr.md) | Converts a value of type SHORT to a value of type UINT_PTR. |
| [RtlUIntPtrToUShort function](..\ntintsafe\nf-ntintsafe-rtluintptrtoushort.md) | Converts a value of type UINT_PTR to a value of type USHORT. |
| [RtlLongLongToUInt function](..\ntintsafe\nf-ntintsafe-rtllonglongtouint.md) | Converts a value of type LONGLONG to a value of type UINT. |
| [RtlSIZETMult function](..\ntintsafe\nf-ntintsafe-rtlsizetmult~r1.md) | Multiplies one value of type SIZE_T by another. |
| [RtlLongPtrToULong function](..\ntintsafe\nf-ntintsafe-rtllongptrtoulong.md) | Converts a value of type LONG_PTR to a value of type ULONG. |
| [RtlShortToChar function](..\ntintsafe\nf-ntintsafe-rtlshorttochar.md) | Converts a value of type SHORT to a value of type CHAR. |
| [RtlUIntMult function](..\ntintsafe\nf-ntintsafe-rtluintmult.md) | Multiplies one value of type UINT by another. |
| [RtlUIntToInt function](..\ntintsafe\nf-ntintsafe-rtluinttoint.md) | Converts a value of type UINT to a value of type INT. |
| [RtlULongToShort function](..\ntintsafe\nf-ntintsafe-rtlulongtoshort.md) | Converts a value of type ULONG to a value of type SHORT. |
| [RtlLongToUShort function](..\ntintsafe\nf-ntintsafe-rtllongtoushort.md) | Converts a value of type LONG to a value of type USHORT. |
| [RtlLongLongToULongLong function](..\ntintsafe\nf-ntintsafe-rtllonglongtoulonglong.md) | Converts a value of type LONGLONG to a value of type LONGLONG. |
| [RtlInt8Mult function](..\ntintsafe\nf-ntintsafe-rtlint8mult.md) | Multiplies one value of type INT8 by another. |
| [RtlLongPtrSub function](..\ntintsafe\nf-ntintsafe-rtllongptrsub.md) | Subtracts one value of type LONG_PTR from another. |
| [RtlULongPtrMult function](..\ntintsafe\nf-ntintsafe-rtlulongptrmult.md) | Multiplies one value of type ULONG_PTR by another. |
| [RtlLongLongToInt8 function](..\ntintsafe\nf-ntintsafe-rtllonglongtoint8.md) | Converts a value of type LONGLONG to a value of type INT8. |
| [RtlInt8ToULongLong function](..\ntintsafe\nf-ntintsafe-rtlint8toulonglong.md) | Converts a value of type INT8 to a value of type ULONGLONG. |
| [RtlLongLongToLong function](..\ntintsafe\nf-ntintsafe-rtllonglongtolong.md) | Converts a value of type LONGLONG to a value of type LONG. |
| [RtlULongToUChar function](..\ntintsafe\nf-ntintsafe-rtlulongtouchar.md) | Converts a value of type ULONG to a value of type UCHAR. |
| [RtlULongPtrToUInt function](..\ntintsafe\nf-ntintsafe-rtlulongptrtouint.md) | Converts a value of type ULONG_PTR to a value of type UINT. |
| [RtlLongPtrToShort function](..\ntintsafe\nf-ntintsafe-rtllongptrtoshort.md) | Converts a value of type LONG_PTR to a value of type SHORT. |
| [RtlLongToInt8 function](..\ntintsafe\nf-ntintsafe-rtllongtoint8.md) | Converts a value of type LONG to a value of type INT8. |
| [RtlULongPtrToInt function](..\ntintsafe\nf-ntintsafe-rtlulongptrtoint.md) | Converts a value of type ULONG_PTR to a value of type INT. |
| [RtlLongToULong function](..\ntintsafe\nf-ntintsafe-rtllongtoulong.md) | Converts a value of type LONG to a value of type ULONG. |
| [RtlInt8ToUShort function](..\ntintsafe\nf-ntintsafe-rtlint8toushort.md) | Converts a value of type INT8 to a value of type USHORT. |
| [RtlULongLongToLongLong function](..\ntintsafe\nf-ntintsafe-rtlulonglongtolonglong.md) | Converts a value of type ULONGLONG to a value of type LONGLONG. |
| [RtlSSIZETAdd function](..\ntintsafe\nf-ntintsafe-rtlssizetadd.md) | Adds two values of type SSIZE_T. |
| [RtlIntToUChar function](..\ntintsafe\nf-ntintsafe-rtlinttouchar.md) | Converts a value of type INT to a value of type UCHAR. |
| [RtlUIntToShort function](..\ntintsafe\nf-ntintsafe-rtluinttoshort.md) | Converts a value of type UINT to a value of type SHORT. |
| [RtlLongLongToUShort function](..\ntintsafe\nf-ntintsafe-rtllonglongtoushort.md) | Converts a value of type LONGLONG to a value of type USHORT. |
| [RtlShortToDWordPtr function](..\ntintsafe\nf-ntintsafe-rtlshorttodwordptr.md) | Converts a value of type SHORT to a value of type DWORD_PTR. |
| [RtlDWordPtrMult function](..\ntintsafe\nf-ntintsafe-rtldwordptrmult.md) | Multiplies one value of type DWORD_PTR by another. |
| [RtlUInt8ToChar function](..\ntintsafe\nf-ntintsafe-rtluint8tochar.md) | Converts a value of type UINT8 to a value of type CHAR. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [CPTABLEINFO structure](..\ntnls\ns-ntnls--cptableinfo.md) | Stores the NLS file formats. |
| [NLSTABLEINFO structure](..\ntnls\ns-ntnls--nlstableinfo.md) | Stores the NLS file formats . |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RtlUnicodeStringCbCatStringNEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcbcatstringnex.md) | The RtlUnicodeStringCbCatStringNEx function concatenates two strings when the destination string is contained in a UNICODE_STRING structure, while limiting the size of the appended string. |
| [RtlUnicodeStringCbCopyStringNEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcbcopystringnex.md) | The RtlUnicodeStringCbCopyStringNEx function copies a string into a UNICODE_STRING structure while limiting the size of the copied string. |
| [RtlUnicodeStringInitEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringinitex.md) | The RtlUnicodeStringInitEx function initializes a UNICODE_STRING structure. |
| [RtlUnicodeStringCatEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcatex.md) | The RtlUnicodeStringCatEx function concatenates two strings that are contained in UNICODE_STRING structures. |
| [RtlUnicodeStringCchCopyNEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcchcopynex.md) | The RtlUnicodeStringCchCopyNEx function copies a string from one UNICODE_STRING structure to another while limiting the size of the copied string. |
| [RtlUnicodeStringCchCatStringNEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcchcatstringnex.md) | The RtlUnicodeStringCchCatStringNEx function concatenates two strings when the destination string is contained in a UNICODE_STRING structure, while limiting the size of the appended string. |
| [RtlStringCbCopyUnicodeStringEx function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcopyunicodestringex.md) | The RtlStringCbCopyUnicodeStringEx function copies the contents of a UNICODE_STRING structure to a specified destination. |
| [RtlUnicodeStringCbCatN function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcbcatn.md) | The RtlUnicodeStringCbCatN function concatenates two strings that are contained in UNICODE_STRING structures while limiting the size of the copied string. |
| [RtlUnicodeStringValidateEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringvalidateex.md) | The RtlUnicodeStringValidateEx function validates the contents of a UNICODE_STRING structure. |
| [RtlUnicodeStringPrintfEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringprintfex.md) | The RtlUnicodeStringPrintfEx function creates a text string, with formatting that is based on supplied formatting information, and stores the string in a UNICODE_STRING structure. |
| [RtlUnicodeStringVPrintf function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringvprintf.md) | The RtlUnicodeStringVPrintf function creates a text string, with formatting that is based on supplied formatting information, and stores the string in a UNICODE_STRING structure. |
| [RtlUnicodeStringCchCatNEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcchcatnex.md) | The RtlUnicodeStringCchCatNEx function concatenates two strings that are contained in UNICODE_STRING structures while limiting the size of the copied string. |
| [RtlUnicodeStringValidate function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringvalidate.md) | The RtlUnicodeStringValidate function validates the contents of a UNICODE_STRING structure. |
| [RtlUnicodeStringCbCopyStringN function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcbcopystringn.md) | The RtlUnicodeStringCbCopyStringN function copies a string into a UNICODE_STRING structure while limiting the size of the copied string. |
| [RtlStringCchCopyUnicodeStringEx function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcopyunicodestringex.md) | The RtlStringCchCopyUnicodeStringEx function copies the contents of a UNICODE_STRING structure to a specified destination. |
| [RtlUnicodeStringCchCatStringN function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcchcatstringn.md) | The RtlUnicodeStringCchCatStringN function concatenates two strings when the destination string is contained in a UNICODE_STRING structure, while limiting the size of the appended string. |
| [RtlUnicodeStringPrintf function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringprintf.md) | The RtlUnicodeStringPrintf function creates a text string, with formatting that is based on supplied formatting information, and stores the string in a UNICODE_STRING structure. |
| [RtlStringCchCopyUnicodeString function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcopyunicodestring.md) | The RtlStringCchCopyUnicodeString function copies the contents of a UNICODE_STRING structure to a specified destination. |
| [RtlUnicodeStringInit function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringinit.md) | The RtlUnicodeStringInit function initializes a UNICODE_STRING structure. |
| [RtlUnicodeStringCbCatStringN function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcbcatstringn.md) | The RtlUnicodeStringCbCatStringN function concatenates two strings when the destination string is contained in a UNICODE_STRING structure, while limiting the size of the appended string. |
| [RtlUnicodeStringCopyStringEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcopystringex.md) | The RtlUnicodeStringCopyStringEx function copies a string into a UNICODE_STRING structure. |
| [RtlUnicodeStringCchCopyStringN function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcchcopystringn.md) | The RtlUnicodeStringCchCopyStringN function copies a string into a UNICODE_STRING structure while limiting the size of the copied string. |
| [RtlUnicodeStringCchCopyN function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcchcopyn.md) | The RtlUnicodeStringCchCopyN function copies a string from one UNICODE_STRING structure to another while limiting the size of the copied string. |
| [RtlUnicodeStringCopyString function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcopystring.md) | The RtlUnicodeStringCopyString function copies a string into a UNICODE_STRING structure. |
| [RtlUnicodeStringCatString function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcatstring.md) | The RtlUnicodeStringCatString function concatenates two strings when the destination string is contained in a UNICODE_STRING structure. |
| [RtlUnicodeStringCopy function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcopy.md) | The RtlUnicodeStringCopy function copies a string from one UNICODE_STRING structure to another. |
| [RtlUnicodeStringCat function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcat.md) | The RtlUnicodeStringCat function concatenates two strings that are contained in UNICODE_STRING structures. |
| [RtlUnicodeStringCbCopyN function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcbcopyn.md) | The RtlUnicodeStringCbCopyN function copies a string from one UNICODE_STRING structure to another while limiting the size of the copied string. |
| [RtlUnicodeStringCbCopyNEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcbcopynex.md) | The RtlUnicodeStringCbCopyNEx function copies a string from one UNICODE_STRING structure to another while limiting the size of the copied string. |
| [RtlUnicodeStringVPrintfEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringvprintfex.md) | The RtlUnicodeStringVPrintfEx function creates a text string, with formatting that is based on supplied formatting information, and stores the string in a UNICODE_STRING structure. |
| [RtlUnicodeStringCchCatN function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcchcatn.md) | The RtlUnicodeStringCchCatN function concatenates two strings that are contained in UNICODE_STRING structures while limiting the size of the copied string. |
| [RtlStringCbCopyUnicodeString function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcopyunicodestring.md) | The RtlStringCbCopyUnicodeString function copies the contents of a UNICODE_STRING structure to a specified destination. |
| [RtlUnicodeStringCopyEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcopyex.md) | The RtlUnicodeStringCopyEx function copies a string from one UNICODE_STRING structure to another. |
| [RtlUnicodeStringCatStringEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcatstringex.md) | The RtlUnicodeStringCatStringEx function concatenates two strings when the destination string is contained in a UNICODE_STRING structure. |
| [RtlUnicodeStringCchCopyStringNEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcchcopystringnex.md) | The RtlUnicodeStringCchCopyStringNEx function copies a string into a UNICODE_STRING structure while limiting the size of the copied string. |
| [RtlUnicodeStringCbCatNEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcbcatnex.md) | The RtlUnicodeStringCbCatNEx function concatenates two strings that are contained in UNICODE_STRING structures while limiting the size of the copied string. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [PEP_QUERY_COMPONENT_PERF_STATES structure](..\pepfx\ns-pepfx--pep-query-component-perf-states.md) | The PEP_QUERY_COMPONENT_PERF_STATES structure contains a list of discrete performance state (P-state) values for the specified P-state set. |
| [PEP_PPM_QUERY_PLATFORM_STATE structure](..\pepfx\ns-pepfx--pep-ppm-query-platform-state.md) | The PEP_PPM_QUERY_PLATFORM_STATE structure contains information about a platform idle state. |
| [PEP_UNREGISTER_DEVICE structure](..\pepfx\ns-pepfx--pep-unregister-device.md) | The PEP_UNREGISTER_DEVICE structure identifies a device whose registration is being removed from the Windows power management framework (PoFx). |
| [PEP_PPM_CONTEXT_QUERY_PARKING_PAGE structure](..\pepfx\ns-pepfx--pep-ppm-context-query-parking-page.md) | The PEP_PPM_CONTEXT_QUERY_PARKING_PAGE structure describes the parking page for a processor. |
| [PEP_PPM_RESUME_FROM_SYSTEM_STATE structure](..\pepfx\ns-pepfx--pep-ppm-resume-from-system-state.md) | Used by the PEP_NOTIFY_PPM_RESUME_FROM_SYSTEM_STATE notification that notifies the PEP that the system has just resumed from a system power state. |
| [PEP_PPM_IDLE_COMPLETE_V2 structure](..\pepfx\ns-pepfx--pep-ppm-idle-complete-v2.md) | The PEP_PPM_IDLE_COMPLETE_V2 structure describe the idle states from which the processor and hardware platform are waking. |
| [PEP_PPM_QUERY_DISCRETE_PERF_STATES structure](..\pepfx\ns-pepfx--pep-ppm-query-discrete-perf-states.md) | Used in the PEP_NOTIFY_PPM_QUERY_DISCRETE_PERF_STATES notification that stores the list of discrete performance states that PEP supports, if the PEP_NOTIFY_PPM_QUERY_CAPABILITIES notification indicates support for discrete performance states. . |
| [PEP_CRASHDUMP_INFORMATION structure](..\pepfx\ns-pepfx--pep-crashdump-information.md) | The PEP_CRASHDUMP_INFORMATION structure contains information about a crash-dump device. |
| [PEP_PPM_FEEDBACK_READ structure](..\pepfx\ns-pepfx--pep-ppm-feedback-read.md) | The PEP_PPM_FEEDBACK_READ structure contains the value read from a processor performance feedback counter. |
| [PEP_ACPI_EVALUATE_CONTROL_METHOD structure](..\pepfx\ns-pepfx--pep-acpi-evaluate-control-method.md) | The PEP_ACPI_EVALUATE_CONTROL_METHOD structure specifies an ACPI control method to evaluate, an input argument to supply to this method, and an output buffer for the result of the evaluation. |
| [PEP_ACPI_RESOURCE structure](..\pepfx\ns-pepfx--pep-acpi-resource.md) | The PEP_ACPI_RESOURCE structure contains hardware details for a specific ACPI resource. |
| [PEP_ACPI_REGISTER_DEVICE structure](..\pepfx\ns-pepfx--pep-acpi-register-device.md) | The PEP_ACPI_REGISTER_DEVICE structure contains registration information about a device for which the platform extension plug-in (PEP) is to provide ACPI services. |
| [PEP_PPM_QUERY_IDLE_STATES_V2 structure](..\pepfx\ns-pepfx--pep-ppm-query-idle-states-v2.md) | The PEP_PPM_QUERY_IDLE_STATES_V2 structure is used during processor initialization to query the platform extension plug-in (PEP) for a list of processor idle states that the processor supports. |
| [PEP_ACPI_QUERY_OBJECT_INFORMATION structure](..\pepfx\ns-pepfx--pep-acpi-query-object-information.md) | The PEP_ACPI_QUERY_OBJECT_INFORMATION structure contains information about an ACPI object. |
| [PEP_WORK_ACPI_NOTIFY structure](..\pepfx\ns-pepfx--pep-work-acpi-notify.md) | The PEP_WORK_ACPI_NOTIFY structure contains the ACPI Notify code for a device that has generated a hardware event. |
| [PEP_LOW_POWER_EPOCH structure](..\pepfx\ns-pepfx--pep-low-power-epoch.md) | The PEP_LOW_POWER_EPOCH structure is used to provide data for a PEP_DPM_LOW_POWER_EPOCH notification (deprecated). |
| [PEP_ACPI_IO_MEMORY_RESOURCE structure](..\pepfx\ns-pepfx--pep-acpi-io-memory-resource.md) | The PEP_ACPI_IO_MEMORY_RESOURCE structure describes an ACPI IO port descriptor resource. |
| [PEP_COMPONENT_PERF_INFO structure](..\pepfx\ns-pepfx--pep-component-perf-info.md) | The PEP_COMPONENT_PERF_INFO structure describes the performance states (P-states) of a component. |
| [PEP_PPM_IS_PROCESSOR_HALTED structure](..\pepfx\ns-pepfx--pep-ppm-is-processor-halted.md) | The PEP_PPM_IS_PROCESSOR_HALTED structure indicates whether the processor is currently halted in its selected idle state. |
| [PEP_QUERY_COMPONENT_PERF_SET_NAME structure](..\pepfx\ns-pepfx--pep-query-component-perf-set-name.md) | The PEP_QUERY_COMPONENT_PERF_SET_NAME structure contains query information about a set of performance state values (P-state set) for a component. |
| [PEP_REGISTER_CRASHDUMP_DEVICE structure](..\pepfx\ns-pepfx--pep-register-crashdump-device.md) | The PEP_REGISTER_CRASHDUMP_DEVICE structure provides a callback routine to turn on a crash-dump device. |
| [PEP_PLATFORM_IDLE_STATE_UPDATE structure](..\pepfx\ns-pepfx--pep-platform-idle-state-update.md) | The PEP_PLATFORM_IDLE_STATE_UPDATE structure contains the updated properties of a platform idle state. |
| [PEP_REGISTER_DEBUGGER structure](..\pepfx\ns-pepfx--pep-register-debugger.md) | The PEP_REGISTER_DEBUGGER structure identifies a registered device that is a core system resource that provides debugger transport. |
| [PEP_REGISTER_COMPONENT_PERF_STATES structure](..\pepfx\ns-pepfx--pep-register-component-perf-states.md) | The PEP_REGISTER_COMPONENT_PERF_STATES structure describes the performance states (P-states) of the specified component. |
| [PEP_ACPI_GPIO_RESOURCE structure](..\pepfx\ns-pepfx--pep-acpi-gpio-resource.md) | The PEP_ACPI_GPIO_RESOURCE structure describes the ACPI configuration for a general purpose input/output (GPIO) resource. |
| [PEP_ACPI_SPB_UART_RESOURCE structure](..\pepfx\ns-pepfx--pep-acpi-spb-uart-resource.md) | The PEP_ACPI_SPB_UART_RESOURCE structure describes an ACPI UART serial bus resource. |
| [PEP_PPM_CST_STATE structure](..\pepfx\ns-pepfx--pep-ppm-cst-state.md) | The PEP_PPM_CST_STATE structure specifies the properties of a C state (ACPI processor power state). |
| [PEP_DEBUGGER_TRANSITION_REQUIREMENTS structure](..\pepfx\ns-pepfx--pep-debugger-transition-requirements.md) | The PEP_DEBUGGER_TRANSITION_REQUIREMENTS structure indicates the platform idle states for which the debugger device must be turned on. |
| [PEP_ACPI_PREPARE_DEVICE structure](..\pepfx\ns-pepfx--pep-acpi-prepare-device.md) | The PEP_ACPI_PREPARE_DEVICE structure indicates whether a platform extension plug-in (PEP) is prepared to provide ACPI services for the specified device. |
| [PEP_COORDINATED_DEPENDENCY_OPTION structure](..\pepfx\ns-pepfx--pep-coordinated-dependency-option.md) | The PEP_COORIDNATED_DEPENDENCY_OPTION structure describes a coordinated idle stateâ€™s dependency to the OS. |
| [PEP_POWER_CONTROL_REQUEST structure](..\pepfx\ns-pepfx--pep-power-control-request.md) | The PEP_POWER_CONTROL_REQUEST structure contains a request from a driver for a power control operation. |
| [PO_FX_CORE_DEVICE structure](..\pepfx\ns-pepfx--po-fx-core-device.md) | The PO_FX_CORE_DEVICE structure contains information about the power-state attributes of the components in a core system resource, and provides a software interface for power-managing these components. |
| [PEP_PPM_QUERY_COORDINATED_STATES structure](..\pepfx\ns-pepfx--pep-ppm-query-coordinated-states.md) | The PEP_PPM_QUERY_COORDINATED_STATES structure contains information about each coordinated idle state that the platform extension plug-in (PEP) supports. |
| [PEP_PLATFORM_IDLE_STATE structure](..\pepfx\ns-pepfx--pep-platform-idle-state.md) | The PEP_PLATFORM_IDLE_STATE structure specifies the properties of a platform idle state. |
| [PEP_PPM_QUERY_STATE_NAME structure](..\pepfx\ns-pepfx--pep-ppm-query-state-name.md) | The PEP_PPM_QUERY_STATE_NAME structure contains information about a specific coordinated or platform idle state. |
| [PEP_WORK_POWER_CONTROL structure](..\pepfx\ns-pepfx--pep-work-power-control.md) | The PEP_WORK_POWER_CONTROL structure contains the parameters for a power control request that the platform extension plug-in (PEP) sends directly to a processor driver. |
| [PEP_PPM_QUERY_VETO_REASON structure](..\pepfx\ns-pepfx--pep-ppm-query-veto-reason.md) | The PEP_PPM_QUERY_VETO_REASON structure supplies a wide-character, null-terminated string that contains a descriptive, human-readable name for a veto reason. |
| [PEP_UNMASKED_INTERRUPT_INFORMATION structure](..\pepfx\ns-pepfx--pep-unmasked-interrupt-information.md) | The PEP_UNMASKED_INTERRUPT_INFORMATION structure contains information about an interrupt source. |
| [PEP_PROCESSOR_IDLE_STATE_V2 structure](..\pepfx\ns-pepfx--pep-processor-idle-state-v2.md) | The PEP_PROCESSOR_IDLE_STATE_V2 structure describes a processor idle state that the platform extension plug-in (PEP) supports. |
| [PEP_ACPI_INTERRUPT_RESOURCE structure](..\pepfx\ns-pepfx--pep-acpi-interrupt-resource.md) | The PEP_ACPI_INTERRUPT_RESOURCE structure describes an ACPI interrupt resource. |
| [PEP_PPM_PLATFORM_STATE_RESIDENCY structure](..\pepfx\ns-pepfx--pep-ppm-platform-state-residency.md) | The PEP_PPM_PLATFORM_STATE_RESIDENCY structure specifies the accumulated residency time and transition count for a particular platform idle state. |
| [PEP_PPM_TEST_IDLE_STATE structure](..\pepfx\ns-pepfx--pep-ppm-test-idle-state.md) | The PEP_PPM_TEST_IDLE_STATE structure contains information about whether the processor can immediately enter a processor idle state. |
| [PEP_REGISTER_DEVICE_V2 structure](..\pepfx\ns-pepfx--pep-register-device-v2.md) | The PEP_REGISTER_DEVICE_V2 structure describes a device whose driver stack has just registered with the Windows power management framework (PoFx). |
| [PEP_NOTIFY_COMPONENT_IDLE_STATE structure](..\pepfx\ns-pepfx--pep-notify-component-idle-state.md) | The PEP_NOTIFY_COMPONENT_IDLE_STATE structure contains status information about a component's pending transition to a new Fx power state. |
| [PEP_WORK_COMPLETE_PERF_STATE structure](..\pepfx\ns-pepfx--pep-work-complete-perf-state.md) | The PEP_WORK_COMPLETE_PERF_STATE structure describes the completion status of a previously requested update to the performance values assigned to a list of performance state (P-state) sets. |
| [PEP_PPM_PERF_SET structure](..\pepfx\ns-pepfx--pep-ppm-perf-set.md) | The PEP_PPM_PERF_SET structure specifies the new performance level that the operating system is requesting for the processor. |
| [PEP_ABANDON_DEVICE structure](..\pepfx\ns-pepfx--pep-abandon-device.md) | The PEP_ABANDON_DEVICE structure identifies a device that has been abandoned and will no longer be used by the operating system. |
| [PEP_POWER_CONTROL_COMPLETE structure](..\pepfx\ns-pepfx--pep-power-control-complete.md) | The PEP_POWER_CONTROL_COMPLETE structure contains status information for a power control operation that the PEP previously requested and that the device driver has completed. |
| [PEP_PPM_PERF_SET_STATE structure](..\pepfx\ns-pepfx--pep-ppm-perf-set-state.md) | Used in the PEP_NOTIFY_PPM_PERF_SET notification at runtime to set the current operating performance of the processor.  . |
| [PEP_PPM_PARK_SELECTION structure](..\pepfx\ns-pepfx--pep-ppm-park-selection.md) | The PEP_PPM_PARK_SELECTION structure indicates the preferences of the operating system and platform extension plug-in (PEP) regarding which processors in the platform should be parked to reduce power consumption. |
| [PEP_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME structure](..\pepfx\ns-pepfx--pep-query-soc-subsystem-blocking-time.md) | The PEP_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME structure is used by the PEP_DPM_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME notification to collect details about the blocking duration for a particular system on a chip (SoC) subsystem. |
| [PEP_ACPI_SPB_SPI_RESOURCE structure](..\pepfx\ns-pepfx--pep-acpi-spb-spi-resource.md) | The PEP_ACPI_SPB_SPI_RESOURCE structure describes an ACPI SPI serial bus resource. |
| [PEP_PPM_QUERY_COORDINATED_DEPENDENCY structure](..\pepfx\ns-pepfx--pep-ppm-query-coordinated-dependency.md) | The PEP_PPM_QUERY_COORDINATED_DEPENDENCY structure describes dependencies for coordinated idle states. |
| [PEP_ACPI_RESOURCE_FLAGS structure](..\pepfx\ns-pepfx--pep-acpi-resource-flags.md) | The PEP_ACPI_RESOURCE_FLAGS structure contains flags describing an ACPI resource. |
| [PEP_PROCESSOR_PARK_PREFERENCE structure](..\pepfx\ns-pepfx--pep-processor-park-preference.md) | The PEP_PROCESSOR_PARK_PREFERENCE structure indicates the preferences of the operating system and platform extension plug-in (PEP) regarding whether the specified processor should be parked to reduce power consumption. |
| [PEP_COORDINATED_IDLE_STATE structure](..\pepfx\ns-pepfx--pep-coordinated-idle-state.md) | The PEP_COORIDNATED_IDLE_STATE structure describes a coordinated idle state to the OS. |
| [PEP_QUERY_SOC_SUBSYSTEM_METADATA structure](..\pepfx\ns-pepfx--pep-query-soc-subsystem-metadata.md) | The PEP_QUERY_SOC_SUBSYSTEM_METADATA structure is used with the PEP_DPM_QUERY_SOC_SUBSYSTEM_METADATA notification to collect optional metadata about the system on a chip (SoC) subsystem whose blocking time has just been queried. |
| [PEP_ACPI_OBJECT_NAME_WITH_TYPE structure](..\pepfx\ns-pepfx--pep-acpi-object-name-with-type.md) | The PEP_ACPI_OBJECT_NAME_WITH_TYPE structure that specifies both the path-relative name of an ACPI object and the type of this object. |
| [PEP_COMPONENT_PERF_SET structure](..\pepfx\ns-pepfx--pep-component-perf-set.md) | The PEP_COMPONENT_PERF_SET structure describes the performance states (P-states) in a P-state set. |
| [PEP_ACPI_OBJECT_NAME structure](..\pepfx\ns-pepfx--pep-acpi-object-name.md) | The PEP_ACPI_OBJECT_NAME union contains the four-character name of an ACPI object. |
| [PEP_PPM_QUERY_DOMAIN_INFO structure](..\pepfx\ns-pepfx--pep-ppm-query-domain-info.md) | Used in the PEP_NOTIFY_PPM_QUERY_DOMAIN_INFO notification that queries for information about a performance domain. . |
| [PEP_PPM_QUERY_PERF_CAPABILITIES structure](..\pepfx\ns-pepfx--pep-ppm-query-perf-capabilities.md) | The PEP_PPM_QUERY_PERF_CAPABILITIES structure describes the performance capabilities of the processors in the specified processor performance domain. |
| [PEP_ACPI_EXTENDED_ADDRESS structure](..\pepfx\ns-pepfx--pep-acpi-extended-address.md) | The PEP_ACPI_EXTENDED_ADDRESS structure is used to report resource usage in the address space such as memory and IO. |
| [PEP_ACPI_UNREGISTER_DEVICE structure](..\pepfx\ns-pepfx--pep-acpi-unregister-device.md) | The PEP_ACPI_UNREGISTER_DEVICE structure contains information about a device that has been unregistered from ACPI services. |
| [PEP_PROCESSOR_IDLE_DEPENDENCY structure](..\pepfx\ns-pepfx--pep-processor-idle-dependency.md) | The PEP_PROCESSOR_IDLE_DEPENDENCY structure specifies the dependencies of a platform idle state on the specified processor. |
| [PEP_PPM_CST_STATES structure](..\pepfx\ns-pepfx--pep-ppm-cst-states.md) | The PEP_PPM_CST_STATES structure specifies the properties of the C states (ACPI processor power states) that are supported for a processor. |
| [PEP_QUERY_SOC_SUBSYSTEM_COUNT structure](..\pepfx\ns-pepfx--pep-query-soc-subsystem-count.md) | The PEP_QUERY_SOC_SUBSYSTEM_COUNT structure is used to tell the OS whether the PEP supports system on a chip (SoC) subsystem accounting for a given platform idle state. |
| [PEP_PROCESSOR_FEEDBACK_COUNTER structure](..\pepfx\ns-pepfx--pep-processor-feedback-counter.md) | The PEP_PROCESSOR_FEEDBACK_COUNTER structure describes a feedback counter to the operating system. |
| [PEP_SOC_SUBSYSTEM_METADATA structure](..\pepfx\ns-pepfx--pep-soc-subsystem-metadata.md) | The PEP_SOC_SUBSYSTEM_METADATA structure contains key-value pairs that contain metadata for a system on a chip (SoC) subsystem. It is used in the context of a PEP_DPM_QUERY_SOC_SUBSYSTEM_METADATA notification sent to a platform extension plug-in (PEP). |
| [PEP_DEVICE_POWER_STATE structure](..\pepfx\ns-pepfx--pep-device-power-state.md) | The PEP_DEVICE_POWER_STATE structure indicates the status of a transition to a new Dx (device power) state. |
| [PEP_PREPARE_DEVICE structure](..\pepfx\ns-pepfx--pep-prepare-device.md) | The PEP_PREPARE_DEVICE structure identifies a device that must be started up in preparation for its use by the operating system. |
| [PEP_PPM_QUERY_VETO_REASONS structure](..\pepfx\ns-pepfx--pep-ppm-query-veto-reasons.md) | The PEP_PPM_QUERY_VETO_REASONS structure specifies the total number of veto reasons that the PEP uses in calls to the ProcessorIdleVeto and PlatformIdleVeto routines. |
| [PEP_PPM_QUERY_PERF_CONSTRAINTS structure](..\pepfx\ns-pepfx--pep-ppm-query-perf-constraints.md) | The PEP_PPM_PERF_CONSTRAINTS structure describes the performance limits to apply to the processor. |
| [PEP_INFORMATION structure](..\pepfx\ns-pepfx--pep-information.md) | The PEP_INFORMATION structure specifies the interface that the platform extension plug-in (PEP) uses to receive notifications from the Windows power management framework (PoFx). |
| [PEP_PPM_PLATFORM_STATE_RESIDENCIES structure](..\pepfx\ns-pepfx--pep-ppm-platform-state-residencies.md) | The PEP_PPM_PLATFORM_STATE_RESIDENCIES structure contains the accumulated residency times and transition counts for the idle states that are supported by the hardware platform. |
| [PEP_KERNEL_INFORMATION_STRUCT_V3 structure](..\pepfx\ns-pepfx--pep-kernel-information-struct-v3.md) | The PEP_KERNEL_INFORMATION_STRUCT_V3 structure specifies the interface that the power extension plug-in (PEP) uses to request services from the Windows power management framework (PoFx). |
| [PEP_PPM_PARK_MASK structure](..\pepfx\ns-pepfx--pep-ppm-park-mask.md) | The PEP_PROCESSOR_PARK_MASK structure contains the current core parking mask. |
| [PEP_ACPI_ABANDON_DEVICE structure](..\pepfx\ns-pepfx--pep-acpi-abandon-device.md) | The PEP_ACPI_ABANDON_DEVICE structure indicates whether the platform extension plug-in (PEP) accepts ownership of an abandoned device. |
| [PEP_PPM_QUERY_PLATFORM_STATES structure](..\pepfx\ns-pepfx--pep-ppm-query-platform-states.md) | The PEP_PPM_QUERY_PLATFORM_STATES structure specifies the number of platform idle states the hardware platform supports. |
| [PEP_PROCESSOR_IDLE_STATE_UPDATE structure](..\pepfx\ns-pepfx--pep-processor-idle-state-update.md) | The PEP_PROCESSOR_IDLE_STATE_UPDATE structure contains the updated properties of a processor idle state. |
| [PEP_PPM_PERF_CHECK_COMPLETE structure](..\pepfx\ns-pepfx--pep-ppm-perf-check-complete.md) | The PEP_PPM_PERF_CHECK_COMPLETE structure is used to inform the PEP of details regarding the completion of a periodic performance check evaluation. |
| [PEP_DEVICE_PLATFORM_CONSTRAINTS structure](..\pepfx\ns-pepfx--pep-device-platform-constraints.md) | The PEP_DEVICE_PLATFORM_CONSTRAINTS structure specifies the constraints for entry to the various Dx power states that are supported by a device. |
| [PEP_PROCESSOR_PARK_STATE structure](..\pepfx\ns-pepfx--pep-processor-park-state.md) | The PEP_PROCESSOR_PARK_STATE structure describes the parking state for a single processor. |
| [PEP_REQUEST_COMPONENT_PERF_STATE structure](..\pepfx\ns-pepfx--pep-request-component-perf-state.md) | The PEP_REQUEST_COMPONENT_PERF_STATE structure contains a list of performance state (P-state) changes requested by the Windows power management framework (PoFx), plus status information about the handling of these requests by the platform extension plug-in (PEP). |
| [PEP_QUERY_SOC_SUBSYSTEM structure](..\pepfx\ns-pepfx--pep-query-soc-subsystem.md) | The PEP_QUERY_SOC_SUBSYSTEM structure is used by the PEP_DPM_QUERY_SOC_SUBSYSTEM notification to gather basic information about a particular system on a chip (SoC) subsystem. |
| [PEP_PPM_QUERY_FEEDBACK_COUNTERS structure](..\pepfx\ns-pepfx--pep-ppm-query-feedback-counters.md) | The PEP_PPM_QUERY_FEEDBACK_COUNTERS structure describes all the processor performance counters that the platform extension plug-in (PEP) supports for a particular processor. |
| [PEP_WORK structure](..\pepfx\ns-pepfx--pep-work.md) | The PEP_WORK structure indicates whether the PEP has a work request to submit to the Windows power management framework (PoFx). |
| [PEP_ACPI_SPB_I2C_RESOURCE structure](..\pepfx\ns-pepfx--pep-acpi-spb-i2c-resource.md) | The PEP_ACPI_SPB_I2C_RESOURCE structure describes an ACPI I2C serial bus resource. |
| [PEP_PPM_IDLE_EXECUTE_V2 structure](..\pepfx\ns-pepfx--pep-ppm-idle-execute-v2.md) | The PEP_PPM_IDLE_EXECUTE_V2 structure specifies the idle state that the processor is to enter. |
| [PEP_UNMASKED_INTERRUPT_FLAGS structure](..\pepfx\ns-pepfx--pep-unmasked-interrupt-flags.md) | The PEP_UNMASKED_INTERRUPT_FLAGS union indicates whether an unmasked interrupt source is a primary interrupt or a secondary interrupt. |
| [PEP_PERF_STATE structure](..\pepfx\ns-pepfx--pep-perf-state.md) | The PEP_PERF_STATE structure describes a performance state (P-state) in a P-state set in which the P-states are specified as a list of one or more discrete values. |
| [PEP_PPM_PARK_SELECTION_V2 structure](..\pepfx\ns-pepfx--pep-ppm-park-selection-v2.md) | The PEP_PPM_PARK_SELECTION_V2 structure indicates the preferences of the operating system and platform extension plug-in (PEP) regarding which processors in the platform should be parked to reduce power consumption. |
| [PEP_PPM_INITIATE_WAKE structure](..\pepfx\ns-pepfx--pep-ppm-initiate-wake.md) | The PEP_PPM_INITIATE_WAKE structure indicates whether a processor requires an interrupt to wake up from an idle state. |
| [PEP_RESET_SOC_SUBSYSTEM_ACCOUNTING structure](..\pepfx\ns-pepfx--pep-reset-soc-subsystem-accounting.md) | The PEP_RESET_SOC_SUBSYSTEM_ACCOUNTING structure is provided to the platform extension plug-in (PEP) as part of a PEP_DPM_RESET_SOC_SUBSYSTEM_ACCOUNTING notification. |
| [PEP_DEVICE_REGISTER_V2 structure](..\pepfx\ns-pepfx--pep-device-register-v2.md) | The PEP_DEVICE_REGISTER structure describes all the components in a particular device. |
| [PEP_DEVICE_STARTED structure](..\pepfx\ns-pepfx--pep-device-started.md) | The PEP_DEVICE_STARTED structure identifies a device whose driver has completed its registration with the Windows power management framework (PoFx). |
| [PEP_ACPI_SPB_RESOURCE structure](..\pepfx\ns-pepfx--pep-acpi-spb-resource.md) | The PEP_ACPI_SPB_RESOURCE structure describes an ACPI serial bus connection resource. |
| [PEP_WORK_COMPLETE_IDLE_STATE structure](..\pepfx\ns-pepfx--pep-work-complete-idle-state.md) | The PEP_WORK_COMPLETE_IDLE_STATE structure identifies a component that the platform extension plug-in (PEP) has prepared for a transition to a new Fx power state. |
| [PEP_PROCESSOR_PERF_STATE structure](..\pepfx\ns-pepfx--pep-processor-perf-state.md) | Use in the PEP_NOTIFY_PPM_QUERY_DISCRETE_PERF_STATES  notification. This structure describes the properties of a single performance state.  . |
| [PEP_ACPI_ENUMERATE_DEVICE_NAMESPACE structure](..\pepfx\ns-pepfx--pep-acpi-enumerate-device-namespace.md) | The PEP_ACPI_ENUMERATE_DEVICE_NAMESPACE structure contains an enumeration of the objects in the namespace of the device. |
| [PEP_PPM_IDLE_EXECUTE structure](..\pepfx\ns-pepfx--pep-ppm-idle-execute.md) | The PEP_PPM_IDLE_EXECUTE structure specifies the idle state that the processor is to enter. |
| [PEP_COMPONENT_PLATFORM_CONSTRAINTS structure](..\pepfx\ns-pepfx--pep-component-platform-constraints.md) | The PEP_COMPONENT_PLATFORM_CONSTRAINTS structure describes the lowest-powered Fx state of that a component can be in when the platform is in a particular idle state. |
| [PEP_COMPONENT_PERF_STATE_REQUEST structure](..\pepfx\ns-pepfx--pep-component-perf-state-request.md) | The PEP_COMPONENT_PERF_STATE_REQUEST structure specifies a performance state (P-state) set and a new performance level to assign to this set. |
| [PEP_SYSTEM_LATENCY structure](..\pepfx\ns-pepfx--pep-system-latency.md) | The PEP_SYSTEM_LATENCY structure specifies the new value for the system latency tolerance. |
| [PEP_QUERY_COMPONENT_PERF_SET structure](..\pepfx\ns-pepfx--pep-query-component-perf-set.md) | The PEP_QUERY_COMPONENT_PERF_SET structure contains query information about a set of performance state values (P-state set) for a component. |
| [PEP_PPM_QUERY_CAPABILITIES structure](..\pepfx\ns-pepfx--pep-ppm-query-capabilities.md) | The PEP_PPM_QUERY_CAPABILITIES structure contains information about the processor power management (PPM) capabilities of the platform extension plug-in (PEP). |
| [PEP_PPM_IDLE_COMPLETE structure](..\pepfx\ns-pepfx--pep-ppm-idle-complete.md) | The PEP_PPM_IDLE_COMPLETE structure describe the idle states from which the processor and hardware platform are waking. |
| [PEP_COMPONENT_V2 structure](..\pepfx\ns-pepfx--pep-component-v2.md) | The PEP_COMPONENT_V2 structure specifies the power state attributes of a component in the device. |
| [PEP_PPM_ENTER_SYSTEM_STATE structure](..\pepfx\ns-pepfx--pep-ppm-enter-system-state.md) | Used in the PEP_NOTIFY_PPM_ENTER_SYSTEM_STATE notification to notify PEP that the system is about to enter a system power state.  . |
| [PEP_WORK_INFORMATION structure](..\pepfx\ns-pepfx--pep-work-information.md) | The PEP_WORK_INFORMATION structure describes a work item that the PEP is submitting to the Windows power management framework (PoFx). |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [PEP_PERF_STATE_TYPE enumeration](..\pepfx\ne-pepfx--pep-perf-state-type.md) | The PEP_PERF_STATE_TYPE enumeration indicates the type of performance information that is specified for a performance state (P-state) of a component. |
| [PEP_DEVICE_ACCEPTANCE_TYPE enumeration](..\pepfx\ne-pepfx--pep-device-acceptance-type.md) | The PEP_DEVICE_ACCEPTANCE_TYPE enumeration indicates whether a PEP accepts ownership of a device. |
| [GPIO_PIN_CONFIG_TYPE enumeration](..\pepfx\ne-pepfx--gpio-pin-config-type.md) | The GPIO_PIN_CONFIG_TYPE enumeration describes a connection IO resource. |
| [PEP_ACPI_OBJECT_TYPE enumeration](..\pepfx\ne-pepfx--pep-acpi-object-type.md) | The PEP_ACPI_OBJECT_TYPE enumeration indicates the type of ACPI object. |
| [GPIO_PIN_IORESTRICTION_TYPE enumeration](..\pepfx\ne-pepfx--gpio-pin-iorestriction-type.md) | The GPIO_PIN_IORESTRICTION_TYPE enumeration describes the functions that a GPIO pin is limited to performing. |
| [PEP_WORK_TYPE enumeration](..\pepfx\ne-pepfx--pep-work-type.md) | The PEP_WORK_TYPE enumeration describes the type of work that the platform extension plug-in (PEP) is requesting. |
| [PEP_ACPI_RESOURCE_TYPE enumeration](..\pepfx\ne-pepfx--pep-acpi-resource-type.md) | The PEP_ACPI_RESOURCE_TYPE enumeration is used to identify the type of ACPI resource that is contained in the PEP_ACPI_RESOURCE union. |
| [PEP_PERF_STATE_UNIT enumeration](..\pepfx\ne-pepfx--pep-perf-state-unit.md) | The PEP_PERF_STATE_UNIT enumeration indicates the measurement units in which the performance state (P-state) of a component is specified. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [PEP_ACPI_INITIALIZE_MEMORY_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-memory-resource.md) | The PEP_ACPI_INITIALIZE_MEMORY_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_IO_MEMORY_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_SPB_UART_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-spb-uart-resource.md) | The PEP_ACPI_INITIALIZE_SPB_UART_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_SPB_UART_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_INTERRUPT_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-interrupt-resource.md) | The PEP_ACPI_INITIALIZE_INTERRUPT_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_INTERRUPT_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_SPB_SPI_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-spb-spi-resource.md) | The PEP_ACPI_INITIALIZE_SPB_SPI_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_SPB_SPI_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_GPIO_INT_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-gpio-int-resource.md) | The PEP_ACPI_INITIALIZE_GPIO_INT_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_GPIO_RESOURCE structure. |
| [PoFxRegisterPluginEx function](..\pepfx\nf-pepfx-pofxregisterpluginex.md) | The PoFxRegisterPluginEx routine registers a platform extension plug-in (PEP) with the Windows power management framework (PoFx). |
| [PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-extended-memory-resource.md) | The PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_EXTENDED_ADDRESS structure. |
| [PEP_ACPI_INITIALIZE_SPB_I2C_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-spb-i2c-resource.md) | The PEP_ACPI_INITIALIZE_SPB_I2C_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_SPB_I2C_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-extended-io-resource.md) | The PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_EXTENDED_ADDRESS structure. |
| [PoFxRegisterCoreDevice function](..\pepfx\nf-pepfx-pofxregistercoredevice.md) | The PoFxRegisterCoreDevice routine registers a new core system resource with the Windows power management framework (PoFx). |
| [PoFxRegisterPlugin function](..\pepfx\nf-pepfx-pofxregisterplugin.md) | The PoFxRegisterPlugin routine registers a platform extension plug-in (PEP) with the Windows power management framework (PoFx). |
| [PEP_ACPI_INITIALIZE_GPIO_IO_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-gpio-io-resource.md) | The PEP_ACPI_INITIALIZE_GPIO_IO_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_GPIO_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_IOPORT_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-ioport-resource.md) | The PEP_ACPI_INITIALIZE_IOPORT_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_IO_MEMORY_RESOURCE structure. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdmlibProcgrpInitialize function](..\procgrp\nf-procgrp-wdmlibprocgrpinitialize.md) | The WdmlibProcgrpInitialize function initializes the Processor Group (ProcGrp) compatibility library. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_VPCI_WRITE_BLOCK IOCTL](..\vpci\ni-vpci-ioctl-vpci-write-block.md) | The driver for a PCI Express (PCIe) virtual function (VF) issues an IOCTL_VPCI_WRITE_BLOCK I/O control code (IOCTL) in order to write data to a VF configuration block. The driver issues this IOCTL to the next-lower driver in the driver stack. |
| [IOCTL_VPCI_INVALIDATE_BLOCK IOCTL](..\vpci\ni-vpci-ioctl-vpci-invalidate-block.md) | The driver for a PCI Express (PCIe) virtual function (VF) issues the IOCTL_VPCI_INVALIDATE_BLOCK IOCTL request in order to be notified of changes to data in one or more VF configuration blocks. |
| [IOCTL_VPCI_READ_BLOCK IOCTL](..\vpci\ni-vpci-ioctl-vpci-read-block.md) | The driver for a PCI Express (PCIe) virtual function (VF) issues an IOCTL_VPCI_READ_BLOCK I/O control code (IOCTL) in order to read data from a VF configuration block. The driver issues this IOCTL to the next-lower driver in the driver stack. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [VPCI_READ_BLOCK_INPUT structure](..\vpci\ns-vpci--vpci-read-block-input.md) | The VPCI_READ_BLOCK_INPUT structure is used in an IOCTL_VPCI_READ_BLOCK IOCTL request to read data from a specified configuration block of data for a PCI Express (PCIe) virtual function (VF). |
| [VPCI_WRITE_BLOCK_INPUT structure](..\vpci\ns-vpci--vpci-write-block-input.md) | The VPCI_WRITE_BLOCK_INPUT structure is used in an IOCTL_VPCI_WRITE_BLOCK IOCTL request to write data to a specified configuration block for a PCI Express (PCIe) virtual function (VF). |
| [VPCI_INVALIDATE_BLOCK_OUTPUT structure](..\vpci\ns-vpci--vpci-invalidate-block-output.md) | The VPCI_INVALIDATE_BLOCK_OUTPUT structure is used in an IOCTL_VPCI_INVALIDATE_BLOCK IOCTL request. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [ZwMapViewOfSection function](..\wdm\nf-wdm-zwmapviewofsection.md) | The ZwMapViewOfSection routine maps a view of a section into the virtual address space of a subject process. |
| [WRITE_PORT_BUFFER_UCHAR function](..\wdm\nf-wdm-write-port-buffer-uchar.md) | The WRITE_PORT_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified port. |
| [IoWMIQuerySingleInstanceMultiple function](..\wdm\nf-wdm-iowmiquerysingleinstancemultiple.md) | The IoWMIQuerySingleInstanceMultiple routine returns all WMI data block instances that implement the specified WMI classes with the specified instance names. |
| [IoBuildAsynchronousFsdRequest function](..\wdm\nf-wdm-iobuildasynchronousfsdrequest.md) | The IoBuildAsynchronousFsdRequest routine allocates and sets up an IRP to be sent to lower-level drivers. |
| [ExAllocateTimer function](..\wdm\nf-wdm-exallocatetimer.md) | The ExAllocateTimer routine allocates and initializes a timer object. |
| [KeDeregisterBoundCallback function](..\wdm\nf-wdm-kederegisterboundcallback.md) | The KeDeregisterBoundCallback routine deregisters a user-mode bound exception callback registered by KeRegisterBoundCallback. |
| [TmDereferenceEnlistmentKey function](..\wdm\nf-wdm-tmdereferenceenlistmentkey.md) | The TmDereferenceEnlistmentKey routine decrements the reference count for the key of a specified enlistment object. |
| [IoDisconnectInterrupt function](..\wdm\nf-wdm-iodisconnectinterrupt.md) | The IoDisconnectInterrupt routine releases a device driver's set of interrupt object(s) when the device is paused or removed, or when the driver is being unloaded. |
| [MmLockPagableDataSection function](..\wdm\nf-wdm-mmlockpagabledatasection.md) | The MmLockPagableDataSection routine locks an entire section of driver data into system space. |
| [IoWMIHandleToInstanceName function](..\wdm\nf-wdm-iowmihandletoinstancename.md) | The IoWMIHandleToInstanceName routine determines the instance name for the WMI class instance implemented by the driver that is specified by a file handle. |
| [IoCompleteRequest function](..\wdm\nf-wdm-iocompleterequest.md) | The IoCompleteRequest routine indicates that the caller has completed all processing for a given I/O request and is returning the given IRP to the I/O manager. |
| [READ_PORT_ULONG function](..\wdm\nf-wdm-read-port-ulong~r2.md) | The READ_PORT_ULONG routine reads a ULONG value from the specified port address. |
| [KeQuerySystemTimePrecise function](..\wdm\nf-wdm-kequerysystemtimeprecise.md) | The KeQuerySystemTimePrecise routine retrieves the current system time, and is more precise than the KeQuerySystemTime routine. |
| [ExGetExclusiveWaiterCount function](..\wdm\nf-wdm-exgetexclusivewaitercount.md) | The ExGetExclusiveWaiterCount routine returns the number of waiters on exclusive access to a given resource. |
| [PoSetSystemWake function](..\wdm\nf-wdm-posetsystemwake.md) | The PoSetSystemWake routine marks the specified IRP as one that contributed to waking the system from a sleep state. |
| [ClfsMgmtTailAdvanceFailure function](..\wdm\nf-wdm-clfsmgmttailadvancefailure.md) | The ClfsMgmtTailAdvanceFailure routine notifies CLFS management that the client could not advance the log's tail. |
| [IoUninitializeWorkItem function](..\wdm\nf-wdm-iouninitializeworkitem.md) | The IoUninitializeWorkItem routine uninitializes a work item that was initialized by IoInitializeWorkItem. |
| [IoCreateNotificationEvent function](..\wdm\nf-wdm-iocreatenotificationevent.md) | The IoCreateNotificationEvent routine creates or opens a named notification event used to notify one or more threads of execution that an event has occurred. |
| [ClfsMgmtRegisterManagedClient function](..\wdm\nf-wdm-clfsmgmtregistermanagedclient.md) | The ClfsMgmtRegisterManagedClient routine creates a client that will manage a CLFS log. |
| [ClfsLsnGreater function](..\wdm\nf-wdm-clfslsngreater.md) | The ClfsLsnGreater routine determines whether one LSN is greater than another LSN. The two LSNs must be from the same stream. |
| [ZwCreateKeyTransacted function](..\wdm\nf-wdm-zwcreatekeytransacted.md) | The ZwCreateKeyTransacted routine creates a new registry key or opens an existing one, and it associates the key with a transaction. |
| [PoFxCompleteIdleCondition function](..\wdm\nf-wdm-pofxcompleteidlecondition.md) | The PoFxCompleteIdleCondition routine informs the power management framework (PoFx) that the specified component has completed a pending change to the idle condition. |
| [RtlFindSetBits function](..\wdm\nf-wdm-rtlfindsetbits.md) | The RtlFindSetBits routine searches for a range of set bits of a requested size within a bitmap. |
| [ExInitializeSetTimerParameters function](..\wdm\nf-wdm-exinitializesettimerparameters.md) | The ExInitializeSetTimerParameters routine initializes an EXT_SET_PARAMETERS structure. |
| [WRITE_REGISTER_USHORT function](..\wdm\nf-wdm-write-register-ushort~r1.md) | The WRITE_REGISTER_USHORT routine writes a USHORT value to the specified address. |
| [ExAcquireRundownProtectionEx function](..\wdm\nf-wdm-exacquirerundownprotectionex.md) | The ExAcquireRundownProtectionEx routine tries to acquire run-down protection on a shared object so the caller can safely access the object. |
| [RtlUnicodeToUTF8N function](..\wdm\nf-wdm-rtlunicodetoutf8n.md) | The RtlUnicodeToUTF8N routine converts a Unicode string to a UTF-8 string. |
| [IoForwardIrpSynchronously function](..\wdm\nf-wdm-ioforwardirpsynchronously.md) | The IoForwardIrpSynchronously routine sends an IRP to a specified driver and waits for that driver to complete the IRP. |
| [WRITE_PORT_USHORT function](..\wdm\nf-wdm-write-port-ushort.md) | The WRITE_PORT_USHORT routine writes a USHORT value to the specified port address. |
| [KeInitializeSemaphore function](..\wdm\nf-wdm-keinitializesemaphore.md) | The KeInitializeSemaphore routine initializes a semaphore object with a specified count and specifies an upper limit that the count can attain. |
| [PsGetCurrentThread function](..\wdm\nf-wdm-psgetcurrentthread.md) | The PsGetCurrentThread routine identifies the current thread. |
| [READ_REGISTER_BUFFER_USHORT function](..\wdm\nf-wdm-read-register-buffer-ushort~r3.md) | The READ_REGISTER_BUFFER_USHORT routine reads a number of USHORT values from the specified register address into a buffer. |
| [IoUpdateShareAccess function](..\wdm\nf-wdm-ioupdateshareaccess.md) | The IoUpdateShareAccess routine updates the share access for the given file object, usually when the file is being opened. |
| [PsQueryTotalCycleTimeProcess function](..\wdm\nf-wdm-psquerytotalcycletimeprocess.md) | The PsQueryTotalCycleTimeProcess routine returns the accumulated cycle time for the specified process. |
| [ZwOpenTransaction function](..\wdm\nf-wdm-zwopentransaction.md) | The ZwOpenTransaction routine obtains a handle to an existing transaction object. |
| [IoQueueWorkItemEx function](..\wdm\nf-wdm-ioqueueworkitemex.md) | The IoQueueWorkItemEx routine associates a WorkItemEx routine with a work item, and it inserts the work item into a queue for later processing by a system worker thread. |
| [IoCallDriver function](..\wdm\nf-wdm-iocalldriver.md) | The IoCallDriver routine sends an IRP to the driver associated with a specified device object. |
| [IoCancelIrp function](..\wdm\nf-wdm-iocancelirp.md) | The IoCancelIrp routine sets the cancel bit in a given IRP and calls the cancel routine for the IRP if there is one. |
| [WRITE_PORT_USHORT function](..\wdm\nf-wdm-write-port-ushort~r1.md) | The WRITE_PORT_USHORT routine writes a USHORT value to the specified port address. |
| [ExSetFirmwareEnvironmentVariable function](..\wdm\nf-wdm-exsetfirmwareenvironmentvariable.md) | The ExSetFirmwareEnvironmentVariable routine sets the value of the specified system firmware environment variable. |
| [ExAllocateFromPagedLookasideList function](..\wdm\nf-wdm-exallocatefrompagedlookasidelist~r1.md) | The ExAllocateFromPagedLookasideList routine returns a pointer to a paged entry from the given lookaside list, or it returns a pointer to a newly allocated paged entry. |
| [RtlSecureZeroMemory function](..\wdm\nf-wdm-rtlsecurezeromemory.md) | The RtlSecureZeroMemory routine fills a block of memory with zeros in a way that is guaranteed to be secure. |
| [KeGetCurrentIrql function](..\wdm\nf-wdm-kegetcurrentirql~r2.md) | The KeGetCurrentIrql routine returns the current IRQL. |
| [MmAllocateMdlForIoSpace function](..\wdm\nf-wdm-mmallocatemdlforiospace.md) | The MmAllocateMdlForIoSpace routine allocates an MDL and initializes this MDL to describe a set of physical address ranges in I/O address space. |
| [IoCopyCurrentIrpStackLocationToNext function](..\wdm\nf-wdm-iocopycurrentirpstacklocationtonext.md) | The IoCopyCurrentIrpStackLocationToNext routine copies the IRP stack parameters from the current I/O stack location to the stack location of the next-lower driver. |
| [PoFxStartDevicePowerManagement function](..\wdm\nf-wdm-pofxstartdevicepowermanagement.md) | The PoFxStartDevicePowerManagement routine completes the registration of a device with the power management framework (PoFx) and starts device power management. |
| [ObDereferenceObjectDeferDeleteWithTag function](..\wdm\nf-wdm-obdereferenceobjectdeferdeletewithtag.md) | The ObDereferenceObjectDeferDeleteWithTag routine decrements the reference count for the specified object, defers deletion of the object to avoid deadlocks, and writes a four-byte tag value to the object to support object reference tracing. |
| [IoAcquireRemoveLock function](..\wdm\nf-wdm-ioacquireremovelock.md) | The IoAcquireRemoveLock routine increments the count for a remove lock, indicating that the associated device object should not be detached from the device stack or deleted. |
| [KeGetCurrentNodeNumber function](..\wdm\nf-wdm-kegetcurrentnodenumber.md) | The KeGetCurrentNodeNumber routine gets the NUMA node number for the logical processor that the caller is running on. |
| [RtlFindLeastSignificantBit function](..\wdm\nf-wdm-rtlfindleastsignificantbit.md) | The RtlFindLeastSignificantBit routine returns the zero-based position of the least significant nonzero bit in its parameter. |
| [IsListEmpty function](..\wdm\nf-wdm-islistempty.md) | The IsListEmpty routine indicates whether a doubly linked list of LIST_ENTRY structures is empty. |
| [RtlUnicodeStringToAnsiString function](..\wdm\nf-wdm-rtlunicodestringtoansistring.md) | The RtlUnicodeStringToAnsiString routine converts a given Unicode string into an ANSI string. |
| [IoRegisterDeviceInterface function](..\wdm\nf-wdm-ioregisterdeviceinterface.md) | The IoRegisterDeviceInterface routine registers a device interface class, if it has not been previously registered, and creates a new instance of the interface class, which a driver can subsequently enable for use by applications or other system components. |
| [InterlockedCompareExchange function](..\wdm\nf-wdm-interlockedcompareexchange.md) | The InterlockedCompareExchange routine performs an atomic operation that compares the input value pointed to by Destination with the value of Comparand. |
| [IoCreateSymbolicLink function](..\wdm\nf-wdm-iocreatesymboliclink.md) | The IoCreateSymbolicLink routine sets up a symbolic link between a device object name and a user-visible name for the device. |
| [WRITE_PORT_BUFFER_ULONG function](..\wdm\nf-wdm-write-port-buffer-ulong~r2.md) | The WRITE_PORT_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified port address. |
| [MmMapLockedPages function](..\wdm\nf-wdm-mmmaplockedpages.md) | The MmMapLockedPages routine is obsolete for Windows 2000 and later versions of Windows, and for Windows Me. |
| [MmUnlockPagableImageSection function](..\wdm\nf-wdm-mmunlockpagableimagesection.md) | The MmUnlockPagableImageSection routine releases a section of driver code or driver data, previously locked into system space with MmLockPagableCodeSection, MmLockPagableDataSection or MmLockPagableSectionByHandle, so the section can be paged out again. |
| [KeReadStateSemaphore function](..\wdm\nf-wdm-kereadstatesemaphore.md) | The KeReadStateSemaphore routine returns the current state, signaled or not-signaled, of the specified semaphore object. |
| [READ_REGISTER_BUFFER_ULONG function](..\wdm\nf-wdm-read-register-buffer-ulong~r2.md) | The READ_REGISTER_BUFFER_ULONG routine reads a number of ULONG values from the specified register address into a buffer. |
| [MmAllocateMappingAddress function](..\wdm\nf-wdm-mmallocatemappingaddress.md) | The MmAllocateMappingAddress routine reserves a range of system virtual address space of the specified size. |
| [WRITE_REGISTER_ULONG function](..\wdm\nf-wdm-write-register-ulong~r3.md) | The WRITE_REGISTER_ULONG routine writes a ULONG value to the specified address. |
| [READ_REGISTER_BUFFER_ULONG function](..\wdm\nf-wdm-read-register-buffer-ulong.md) | The READ_REGISTER_BUFFER_ULONG routine reads a number of ULONG values from the specified register address into a buffer. |
| [WmiTraceMessageVa function](..\wdm\nf-wdm-wmitracemessageva.md) | The WmiTraceMessageVa routine adds a message to the output log of a WPP software tracing session. |
| [KeInitializeTimerEx function](..\wdm\nf-wdm-keinitializetimerex.md) | The KeInitializeTimerEx routine initializes an extended kernel timer object. |
| [RtlDeleteRegistryValue function](..\wdm\nf-wdm-rtldeleteregistryvalue.md) | The RtlDeleteRegistryValue routine removes the specified entry name and the associated values from the registry along the given relative path. |
| [PoSetDeviceBusyEx function](..\wdm\nf-wdm-posetdevicebusyex.md) | The PoSetDeviceBusyEx routine notifies the power manager that the device associated with the specified idle counter is busy. |
| [ExInterlockedRemoveHeadList function](..\wdm\nf-wdm-exinterlockedremoveheadlist.md) | The ExInterlockedRemoveHeadList routine removes an entry from the beginning of a doubly linked list of LIST_ENTRY structures. |
| [ExReInitializeRundownProtection function](..\wdm\nf-wdm-exreinitializerundownprotection.md) | The ExReInitializeRundownProtection routine reinitializes an EX_RUNDOWN_REF structure after the associated object is run down. |
| [KeSetTimerEx function](..\wdm\nf-wdm-kesettimerex.md) | The KeSetTimerEx routine sets the absolute or relative interval at which a timer object is to be set to a signaled state, optionally supplies a CustomTimerDpc routine to be executed when that interval expires, and optionally supplies a recurring interval for the timer. |
| [ExReleaseRundownProtection function](..\wdm\nf-wdm-exreleaserundownprotection.md) | The ExReleaseRundownProtection routine releases run-down protection that the caller previously acquired by calling the ExAcquireRundownProtection routine. |
| [SeValidSecurityDescriptor function](..\wdm\nf-wdm-sevalidsecuritydescriptor.md) | The SeValidSecurityDescriptor routine returns whether a given security descriptor is structurally valid. |
| [READ_REGISTER_BUFFER_UCHAR function](..\wdm\nf-wdm-read-register-buffer-uchar~r1.md) | The READ_REGISTER_BUFFER_UCHAR routine reads a number of bytes from the specified register address into a buffer. |
| [IoSetShareAccessEx function](..\wdm\nf-wdm-iosetshareaccessex.md) | The IoSetShareAccessEx routine sets the access rights for sharing the specified file object. |
| [READ_REGISTER_UCHAR function](..\wdm\nf-wdm-read-register-uchar~r3.md) | The READ_REGISTER_UCHAR routine reads a byte from the specified register address. |
| [IoGetContainerInformation function](..\wdm\nf-wdm-iogetcontainerinformation.md) | The IoGetContainerInformation routine provides information about the current state of a user session. |
| [KeQueryTimeIncrement function](..\wdm\nf-wdm-kequerytimeincrement.md) | The KeQueryTimeIncrement routine returns the number of 100-nanosecond units that are added to the system time each time the interval clock interrupts. |
| [RtlCopyMemory function](..\wdm\nf-wdm-rtlcopymemory.md) | The RtlCopyMemory routine copies the contents of a source memory block to a destination memory block. |
| [TmSinglePhaseReject function](..\wdm\nf-wdm-tmsinglephasereject.md) | The TmSinglePhaseReject routine informs KTM that the calling resource manager will not support a single-phase commit operation for a specified enlistment. |
| [READ_PORT_USHORT function](..\wdm\nf-wdm-read-port-ushort~r1.md) | The READ_PORT_USHORT routine reads a USHORT value from the specified port address. |
| [KeRegisterBugCheckCallback function](..\wdm\nf-wdm-keregisterbugcheckcallback.md) | The KeRegisterBugCheckCallback routine registers a BugCheckCallback routine, which executes when the operating system issues a bug check. |
| [PoRegisterSystemState function](..\wdm\nf-wdm-poregistersystemstate.md) | The PoRegisterSystemState routine registers the system as busy due to certain activity. |
| [TmPrepareComplete function](..\wdm\nf-wdm-tmpreparecomplete.md) | The TmPrepareComplete routine notifies KTM that the calling resource manager has finished preparing a transaction's data. |
| [RtlSetAllBits function](..\wdm\nf-wdm-rtlsetallbits.md) | The RtlSetAllBits routine sets all bits in a given bitmap variable. |
| [IoSetShareAccess function](..\wdm\nf-wdm-iosetshareaccess.md) | The IoSetShareAccess routine sets the access rights for sharing the given file object. |
| [KeFlushIoBuffers function](..\wdm\nf-wdm-keflushiobuffers~r3.md) | The KeFlushIoBuffers routine flushes the memory region described by an MDL from caches of all processors. |
| [ZwPrePrepareComplete function](..\wdm\nf-wdm-zwprepreparecomplete.md) | The ZwPrePrepareComplete routine notifies KTM that the calling resource manager has finished preliminary preparation of a transaction's data. |
| [IoSetLinkShareAccess function](..\wdm\nf-wdm-iosetlinkshareaccess.md) | The IoSetLinkShareAccess routine sets the access rights for link sharing the specified file object. |
| [PoStartNextPowerIrp function](..\wdm\nf-wdm-postartnextpowerirp.md) | The PoStartNextPowerIrp routine signals the power manager that the driver is ready to handle the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only.). |
| [FirstEntrySList function](..\wdm\nf-wdm-firstentryslist.md) | The FirstEntrySList routine returns the first entry in a sequenced singly linked list. |
| [READ_REGISTER_BUFFER_ULONG function](..\wdm\nf-wdm-read-register-buffer-ulong~r3.md) | The READ_REGISTER_BUFFER_ULONG routine reads a number of ULONG values from the specified register address into a buffer. |
| [RtlClearBits function](..\wdm\nf-wdm-rtlclearbits.md) | The RtlClearBits routine sets all bits in the specified range of bits in the bitmap to zero. |
| [InterlockedAnd function](..\wdm\nf-wdm-interlockedand.md) | The InterlockedAnd macro atomically computes a bitwise AND operation. |
| [ExAllocateFromNPagedLookasideList function](..\wdm\nf-wdm-exallocatefromnpagedlookasidelist.md) | The ExAllocateFromNPagedLookasideList routine returns a pointer to a nonpaged entry from the given lookaside list, or it returns a pointer to a newly allocated nonpaged entry. |
| [KeRestoreFloatingPointState function](..\wdm\nf-wdm-kerestorefloatingpointstate~r1.md) | The KeRestoreFloatingPointState routine restores the nonvolatile floating-point context saved by the preceding call to KeSaveFloatingPointState. |
| [ExAllocatePoolWithQuotaTag function](..\wdm\nf-wdm-exallocatepoolwithquotatag~r1.md) | The ExAllocatePoolWithQuotaTag routine allocates pool memory, charging the quota against the current process. |
| [IoWMIQueryAllData function](..\wdm\nf-wdm-iowmiqueryalldata.md) | The IoWMIQueryAllData routine returns all WMI data blocks that implement a given WMI class. |
| [IoGetCurrentIrpStackLocation function](..\wdm\nf-wdm-iogetcurrentirpstacklocation.md) | The IoGetCurrentIrpStackLocation routine returns a pointer to the caller's I/O stack location in the specified IRP. |
| [KeReleaseSpinLock function](..\wdm\nf-wdm-kereleasespinlock.md) | The KeReleaseSpinLock routine releases a spin lock and restores the original IRQL at which the caller was running. |
| [PoFxSetComponentLatency function](..\wdm\nf-wdm-pofxsetcomponentlatency.md) | The PoFxSetComponentLatency routine specifies the maximum latency that can be tolerated in the transition from the idle condition to the active condition in the specified component. |
| [IoStartNextPacket function](..\wdm\nf-wdm-iostartnextpacket.md) | The IoStartNextPacket routine dequeues the next IRP, if any, from the given device object's associated device queue and calls the driver's StartIo routine. |
| [READ_PORT_BUFFER_USHORT function](..\wdm\nf-wdm-read-port-buffer-ushort~r3.md) | The READ_PORT_BUFFER_USHORT routine reads a number of USHORT values from the specified port address into a buffer. |
| [ExSystemTimeToLocalTime function](..\wdm\nf-wdm-exsystemtimetolocaltime.md) | The ExSystemTimeToLocalTime routine converts a GMT system time value to the local system time for the current time zone. |
| [RtlFindClearRuns function](..\wdm\nf-wdm-rtlfindclearruns.md) | The RtlFindClearRuns routine finds the specified number of runs of clear bits within a given bitmap. |
| [ZwQueryInformationFile function](..\wdm\nf-wdm-zwqueryinformationfile.md) | The ZwQueryInformationFile routine returns various kinds of information about a file object. |
| [IoSetStartIoAttributes function](..\wdm\nf-wdm-iosetstartioattributes.md) | The IoSetStartIoAttributes routine sets attributes for the driver's StartIo routine. |
| [InterlockedCompareExchangePointer function](..\wdm\nf-wdm-interlockedcompareexchangepointer.md) | The InterlockedCompareExchangePointer routine performs an atomic operation that compares the input pointer value pointed to by Destination with the pointer value Comparand. |
| [KeTryToAcquireSpinLockAtDpcLevel function](..\wdm\nf-wdm-ketrytoacquirespinlockatdpclevel.md) | The KeTryToAcquireSpinLockAtDpcLevel routine attempts to acquire a spin lock at DISPATCH_LEVEL. |
| [InterlockedXor function](..\wdm\nf-wdm-interlockedxor.md) | The InterlockedOr routine atomically computes a bitwise exclusive OR operation. |
| [KeRestoreExtendedProcessorState function](..\wdm\nf-wdm-kerestoreextendedprocessorstate.md) | The KeRestoreExtendedProcessorState routine restores extended processor state information that was previously saved. |
| [KeWaitForMultipleObjects function](..\wdm\nf-wdm-kewaitformultipleobjects.md) | The KeWaitForMultipleObjects routine puts the current thread into an alertable or nonalertable wait state until any or all of a number of dispatcher objects are set to a signaled state or (optionally) until the wait times out. |
| [RtlFindNextForwardRunClear function](..\wdm\nf-wdm-rtlfindnextforwardrunclear.md) | The RtlFindNextForwardRunClear routine searches a given bitmap variable for the next clear run of bits, starting from the specified index position. |
| [ClfsCreateMarshallingArea function](..\wdm\nf-wdm-clfscreatemarshallingarea.md) | The ClfsCreateMarshallingArea routine creates a marshalling area for a CLFS stream and returns a pointer to an opaque context that represents the new marshalling area. |
| [KeInitializeMutex function](..\wdm\nf-wdm-keinitializemutex.md) | The KeInitializeMutex routine initializes a mutex object, setting it to a signaled state. |
| [ExInitializeLookasideListEx function](..\wdm\nf-wdm-exinitializelookasidelistex.md) | The ExInitializeLookasideListEx routine initializes a lookaside list. |
| [KeRevertToUserGroupAffinityThread function](..\wdm\nf-wdm-kereverttousergroupaffinitythread.md) | The KeRevertToUserGroupAffinityThread routine restores the group affinity of the calling thread to its original value at the time that the thread was created. |
| [ExInterlockedPushEntrySList function](..\wdm\nf-wdm-exinterlockedpushentryslist.md) | The ExInterlockedPushEntrySList routine atomically inserts an entry at the beginning of a sequenced singly linked list. |
| [PoFxSetTargetDripsDevicePowerState function](..\wdm\nf-wdm-pofxsettargetdripsdevicepowerstate.md) | This routine is called to notify the power manager of the device's target device power state for DRIPS. The driver can override the DRIPS constraint provided by the PEP. |
| [TmGetTransactionId function](..\wdm\nf-wdm-tmgettransactionid.md) | The TmGetTransactionId routine retrieves a transaction object's unit of work (UOW) identifier. |
| [KeDeregisterBugCheckCallback function](..\wdm\nf-wdm-kederegisterbugcheckcallback.md) | The KeDeregisterBugCheckCallback routine removes a callback routine that was registered by KeRegisterBugCheckCallback. |
| [IoAllocateErrorLogEntry function](..\wdm\nf-wdm-ioallocateerrorlogentry.md) | The IoAllocateErrorLogEntry routine allocates an error log entry, and returns a pointer to the packet that the caller uses to supply information about an I/O error. |
| [READ_PORT_USHORT function](..\wdm\nf-wdm-read-port-ushort.md) | The READ_PORT_USHORT routine reads a USHORT value from the specified port address. |
| [ZwEnumerateValueKey function](..\wdm\nf-wdm-zwenumeratevaluekey.md) | The ZwEnumerateValueKey routine gets information about the value entries of an open key. |
| [KeInsertQueueDpc function](..\wdm\nf-wdm-keinsertqueuedpc.md) | The KeInsertQueueDpc routine queues a DPC for execution. |
| [IoAllocateWorkItem function](..\wdm\nf-wdm-ioallocateworkitem.md) | The IoAllocateWorkItem routine allocates a work item. |
| [ClfsDeleteLogByPointer function](..\wdm\nf-wdm-clfsdeletelogbypointer.md) | The ClfsDeleteLogByPointer routine marks a CLFS stream for deletion. |
| [WRITE_PORT_USHORT function](..\wdm\nf-wdm-write-port-ushort~r3.md) | The WRITE_PORT_USHORT routine writes a USHORT value to the specified port address. |
| [PoFxPowerControl function](..\wdm\nf-wdm-pofxpowercontrol.md) | The PoFxPowerControl routine sends a power control request to the power management framework (PoFx). |
| [ZwQueryInformationEnlistment function](..\wdm\nf-wdm-zwqueryinformationenlistment.md) | The ZwQueryInformationEnlistment routine retrieves information about a specified enlistment object. |
| [IoGetCurrentProcess function](..\wdm\nf-wdm-iogetcurrentprocess.md) | The IoGetCurrentProcess routine returns a pointer to the current process. |
| [ClfsDeleteLogFile function](..\wdm\nf-wdm-clfsdeletelogfile.md) | The ClfsDeleteLogFile routine marks a CLFS stream for deletion. |
| [RtlIsServicePackVersionInstalled function](..\wdm\nf-wdm-rtlisservicepackversioninstalled.md) | The RtlIsServicePackVersionInstalled routine determines if a specified service pack version of the Microsoft Windows device driver interface (DDI) is installed. |
| [PoUnregisterSystemState function](..\wdm\nf-wdm-pounregistersystemstate.md) | The PoUnregisterSystemState routine cancels a system state registration created by PoRegisterSystemState. |
| [PoSetPowerRequest function](..\wdm\nf-wdm-posetpowerrequest.md) | The PoSetPowerRequest routine increments the count for the specified power request type. |
| [TmCreateEnlistment function](..\wdm\nf-wdm-tmcreateenlistment.md) | The TmCreateEnlistment routine creates a new enlistment object for a transaction. |
| [KeDelayExecutionThread function](..\wdm\nf-wdm-kedelayexecutionthread.md) | The KeDelayExecutionThread routine puts the current thread into an alertable or nonalertable wait state for a specified interval. |
| [MmAdvanceMdl function](..\wdm\nf-wdm-mmadvancemdl.md) | The MmAdvanceMdl routine advances the beginning of an MDL's virtual memory range by the specified number of bytes. |
| [ClfsCreateScanContext function](..\wdm\nf-wdm-clfscreatescancontext.md) | The ClfsCreateScanContext routine creates a scan context that can be used to iterate over the containers of a specified CLFS log. |
| [IoStartTimer function](..\wdm\nf-wdm-iostarttimer.md) | The IoStartTimer routine enables the timer associated with a given device object so the driver-supplied IoTimer routine is called once per second. |
| [KeRevertToUserAffinityThreadEx function](..\wdm\nf-wdm-kereverttouseraffinitythreadex.md) | The KeRevertToUserAffinityThreadEx routine restores the previous affinity of the current thread. |
| [IoWMIDeviceObjectToInstanceName function](..\wdm\nf-wdm-iowmideviceobjecttoinstancename.md) | The IoWMIDeviceObjectToInstanceName routine determines the instance name for the WMI class instance implemented by the driver that is specified by a device object. |
| [MmMapIoSpaceEx function](..\wdm\nf-wdm-mmmapiospaceex.md) | The MmMapIoSpaceEx routine maps the given physical address range to non-paged system space using the specified page protection. |
| [IoStopTimer function](..\wdm\nf-wdm-iostoptimer.md) | The IoStopTimer routine disables the timer for a specified device object so the driver-supplied IoTimer routine is not called. |
| [ExGetSharedWaiterCount function](..\wdm\nf-wdm-exgetsharedwaitercount.md) | The ExGetSharedWaiterCount routine returns the number of waiters on shared access to a given resource. |
| [TmRecoverEnlistment function](..\wdm\nf-wdm-tmrecoverenlistment.md) | The TmRecoverEnlistment routine initiates a recovery operation for the transaction that is associated with a specified enlistment. |
| [ExAllocateFromPagedLookasideList function](..\wdm\nf-wdm-exallocatefrompagedlookasidelist.md) | The ExAllocateFromPagedLookasideList routine returns a pointer to a paged entry from the given lookaside list, or it returns a pointer to a newly allocated paged entry. |
| [ClfsReserveAndAppendLog function](..\wdm\nf-wdm-clfsreserveandappendlog.md) | The ClfsReserveAndAppendLog routine reserves space in a marshalling area or appends a record to a marshalling area or does both atomically. |
| [KeRegisterBugCheckReasonCallback function](..\wdm\nf-wdm-keregisterbugcheckreasoncallback.md) | The KeRegisterBugCheckReasonCallback routine registers a BugCheckDumpIoCallback, BugCheckSecondaryDumpDataCallback, or BugCheckAddPagesCallback routine, which executes when the operating system issues a bug check. |
| [WRITE_REGISTER_USHORT function](..\wdm\nf-wdm-write-register-ushort~r3.md) | The WRITE_REGISTER_USHORT routine writes a USHORT value to the specified address. |
| [READ_PORT_UCHAR function](..\wdm\nf-wdm-read-port-uchar~r3.md) | The READ_PORT_UCHAR routine reads a byte from the specified port address. |
| [KeSaveFloatingPointState function](..\wdm\nf-wdm-kesavefloatingpointstate.md) | The KeSaveFloatingPointState routine saves the nonvolatile floating-point context so the caller can carry out floating-point operations. |
| [ExCreateCallback function](..\wdm\nf-wdm-excreatecallback.md) | The ExCreateCallback routine either creates a new callback object or opens an existing callback object on behalf of the caller. |
| [KeRemoveByKeyDeviceQueue function](..\wdm\nf-wdm-keremovebykeydevicequeue.md) | The KeRemoveByKeyDeviceQueue routine removes an entry, selected according to a sort key value, from the specified device queue. |
| [ClfsQueryLogFileInformation function](..\wdm\nf-wdm-clfsquerylogfileinformation.md) | The ClfsQueryLogFileInformation routine returns metadata and state information for a specified CLFS stream or its underlying physical log or both. |
| [RtlConvertUlongToLargeInteger function](..\wdm\nf-wdm-rtlconvertulongtolargeinteger.md) | The RtlConvertUlongToLargeInteger routine converts the input unsigned integer to a signed large integer. For Windows XP and later versions of Windows, do not use this routine; use the native support for __int64. |
| [ZwCreateFile function](..\wdm\nf-wdm-zwcreatefile.md) | The ZwCreateFile routine creates a new file or opens an existing file. |
| [IoRequestDeviceEject function](..\wdm\nf-wdm-iorequestdeviceeject.md) | The IoRequestDeviceEject routine notifies the PnP manager that the device eject button was pressed. |
| [ExAllocatePoolWithTagPriority function](..\wdm\nf-wdm-exallocatepoolwithtagpriority.md) | The ExAllocatePoolWithTagPriority routine allocates pool memory of the specified type. |
| [ZwOpenEnlistment function](..\wdm\nf-wdm-zwopenenlistment.md) | The ZwOpenEnlistment routine obtains a handle to an existing enlistment object. |
| [RtlTimeFieldsToTime function](..\wdm\nf-wdm-rtltimefieldstotime.md) | The RtlTimeFieldsToTime routine converts TIME_FIELDS information to a system time value. |
| [IoDisconnectInterruptEx function](..\wdm\nf-wdm-iodisconnectinterruptex.md) | For more information, see the WdmlibIoDisconnectInterruptEx function.#define IoDisconnectInterruptEx WdmlibIoDisconnectInterruptEx |
| [RtlTimeToTimeFields function](..\wdm\nf-wdm-rtltimetotimefields.md) | The RtlTimeToTimeFields routine converts system time into a TIME_FIELDS structure. |
| [RtlAnsiStringToUnicodeSize function](..\wdm\nf-wdm-rtlansistringtounicodesize.md) | The RtlAnsiStringToUnicodeSize routine returns the number of bytes required to hold an ANSI string converted into a Unicode string. |
| [ClfsLsnNull function](..\wdm\nf-wdm-clfslsnnull.md) | The ClfsLsnNull routine determines whether a specified LSN is equal to the smallest possible LSN, CLFS_LSN_NULL. |
| [IoWMISetSingleItem function](..\wdm\nf-wdm-iowmisetsingleitem.md) | The IoWMISetSingleItem routine sets a single property in the data block instance that matches the specified WMI class and instance name. |
| [WRITE_REGISTER_USHORT function](..\wdm\nf-wdm-write-register-ushort~r2.md) | The WRITE_REGISTER_USHORT routine writes a USHORT value to the specified address. |
| [ExInterlockedPopEntrySList function](..\wdm\nf-wdm-exinterlockedpopentryslist.md) | The ExInterlockedPopEntrySList routine atomically removes the first entry from a sequenced singly linked list. |
| [KeSaveFloatingPointState function](..\wdm\nf-wdm-kesavefloatingpointstate~r1.md) | The KeSaveFloatingPointState routine saves the nonvolatile floating-point context so the caller can carry out floating-point operations. |
| [RtlUnicodeStringToInteger function](..\wdm\nf-wdm-rtlunicodestringtointeger.md) | The RtlUnicodeStringToInteger routine converts a Unicode string representation of a number to the equivalent integer value. |
| [KeMemoryBarrier function](..\wdm\nf-wdm-kememorybarrier.md) | The KeMemoryBarrier routine creates a barrier at its position in the code&#8212;across which the compiler and the processor cannot move any operations. |
| [WRITE_REGISTER_UCHAR function](..\wdm\nf-wdm-write-register-uchar~r1.md) | The WRITE_REGISTER_UCHAR routine writes a byte to the specified address. |
| [KeQueryRuntimeThread function](..\wdm\nf-wdm-kequeryruntimethread.md) | The KeQueryRuntimeThread routine reports the accumulated kernel-mode and user-mode run time of a thread, in clock ticks. |
| [RtlCopyUnicodeString function](..\wdm\nf-wdm-rtlcopyunicodestring.md) | The RtlCopyUnicodeString routine copies a source string to a destination string. |
| [RtlClearAllBits function](..\wdm\nf-wdm-rtlclearallbits.md) | The RtlClearAllBits routine sets all bits in a given bitmap variable to zero. |
| [ExDeleteLookasideListEx function](..\wdm\nf-wdm-exdeletelookasidelistex.md) | The ExDeleteLookasideListEx routine deletes a lookaside list. |
| [IoSizeofWorkItem function](..\wdm\nf-wdm-iosizeofworkitem.md) | The IoSizeofWorkItem routine returns the size, in bytes, of an IO_WORKITEM structure. |
| [RtlCompareUnicodeString function](..\wdm\nf-wdm-rtlcompareunicodestring.md) | The RtlCompareUnicodeString routine compares two Unicode strings. |
| [RtlNumberOfSetBitsUlongPtr function](..\wdm\nf-wdm-rtlnumberofsetbitsulongptr.md) | The RtlNumberOfSetBitsUlongPtr routine returns the number of bits in the specified ULONG_PTR integer value that are set to one. |
| [MmUnmapReservedMapping function](..\wdm\nf-wdm-mmunmapreservedmapping.md) | The MmUnmapReservedMapping routine unmaps a memory buffer that was mapped by the MmMapLockedPagesWithReservedMapping routine. |
| [ExGetPreviousMode function](..\wdm\nf-wdm-exgetpreviousmode.md) | The ExGetPreviousMode routine returns the previous processor mode for the current thread. |
| [RtlCheckBit function](..\wdm\nf-wdm-rtlcheckbit.md) | The RtlCheckBit routine determines whether a particular bit in a given bitmap variable is clear or set. |
| [KeSetTargetProcessorDpc function](..\wdm\nf-wdm-kesettargetprocessordpc.md) | The KeSetTargetProcessorDpc routine specifies the processor that a DPC routine will be run on. |
| [KeSetImportanceDpc function](..\wdm\nf-wdm-kesetimportancedpc.md) | The KeSetImportanceDpc routine specifies how soon the DPC routine is run. |
| [ClfsMgmtQueryPolicy function](..\wdm\nf-wdm-clfsmgmtquerypolicy.md) | The ClfsMgmtQueryPolicy routine retrieves a specific CLFS_MGMT_POLICY structure for a log. |
| [READ_PORT_BUFFER_ULONG function](..\wdm\nf-wdm-read-port-buffer-ulong.md) | The READ_PORT_BUFFER_ULONG routine reads a number of ULONG values from the specified port address into a buffer. |
| [ExFreeToLookasideListEx function](..\wdm\nf-wdm-exfreetolookasidelistex.md) | The ExFreeToLookasideListEx routine inserts an entry into a lookaside list, or, if the list is full, frees the allocated storage for the entry. |
| [ExInitializeDeleteTimerParameters function](..\wdm\nf-wdm-exinitializedeletetimerparameters.md) | The ExInitializeDeleteTimerParameters routine initializes an EXT_DELETE_PARAMETERS structure. |
| [ZwCreateKey function](..\wdm\nf-wdm-zwcreatekey.md) | The ZwCreateKey routine creates a new registry key or opens an existing one. |
| [IoGetNextIrpStackLocation function](..\wdm\nf-wdm-iogetnextirpstacklocation.md) | The IoGetNextIrpStackLocation routine gives a higher level driver access to the next-lower driver's I/O stack location in an IRP so the caller can set it up for the lower driver. |
| [InterlockedAnd function](..\wdm\nf-wdm-interlockedand~r1.md) | The InterlockedAnd macro atomically computes a bitwise AND operation. |
| [ObReferenceObjectByHandleWithTag function](..\wdm\nf-wdm-obreferenceobjectbyhandlewithtag.md) | The ObReferenceObjectByHandleWithTag routine increments the reference count of the object that is identified by the specified handle, and writes a four-byte tag value to the object to support object reference tracing. |
| [InterlockedExchangeAdd function](..\wdm\nf-wdm-interlockedexchangeadd~r1.md) | The InterlockedExchangeAdd routine adds a value to a given integer as an atomic operation and returns the original value of the given integer. |
| [IoCreateFile function](..\wdm\nf-wdm-iocreatefile.md) | The IoCreateFile routine either causes a new file or directory to be created, or it opens an existing file, device, directory, or volume, giving the caller a handle for the file object. |
| [RtlCmEncodeMemIoResource function](..\wdm\nf-wdm-rtlcmencodememioresource.md) | The RtlCmEncodeMemIoResource routine updates a CM_PARTIAL_RESOURCE_DESCRIPTOR structure to describe a range of memory or I/O port addresses. |
| [KeRegisterNmiCallback function](..\wdm\nf-wdm-keregisternmicallback.md) | The KeRegisterNmiCallback routine registers a routine to be called whenever a nonmaskable interrupt (NMI) occurs. |
| [KeDeregisterBugCheckReasonCallback function](..\wdm\nf-wdm-kederegisterbugcheckreasoncallback.md) | The KeDeregisterBugCheckReasonCallback routine removes a callback routine that was registered by KeRegisterBugCheckReasonCallback. |
| [ZwOpenKeyTransacted function](..\wdm\nf-wdm-zwopenkeytransacted.md) | The ZwOpenKeyTransacted routine opens an existing registry key and associates the key with a transaction. |
| [RemoveEntryList function](..\wdm\nf-wdm-removeentrylist~r1.md) | The RemoveEntryList routine removes an entry from a doubly linked list of LIST_ENTRY structures. |
| [ZwReadOnlyEnlistment function](..\wdm\nf-wdm-zwreadonlyenlistment.md) | The ZwReadOnlyEnlistment routine sets a specified enlistment to be read-only. |
| [MmAllocateContiguousNodeMemory function](..\wdm\nf-wdm-mmallocatecontiguousnodememory.md) | The MmAllocateContiguousNodeMemory routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space. |
| [ExAcquireSharedStarveExclusive function](..\wdm\nf-wdm-exacquiresharedstarveexclusive.md) | The ExAcquireSharedStarveExclusive routine acquires a given resource for shared access without waiting for any pending attempts to acquire exclusive access to the same resource. |
| [WRITE_REGISTER_UCHAR function](..\wdm\nf-wdm-write-register-uchar~r3.md) | The WRITE_REGISTER_UCHAR routine writes a byte to the specified address. |
| [IoSetNextIrpStackLocation function](..\wdm\nf-wdm-iosetnextirpstacklocation.md) | The IoSetNextIrpStackLocation routine sets the IRP stack location in a driver-allocated IRP to that of the caller. |
| [RtlUshortByteSwap function](..\wdm\nf-wdm-rtlushortbyteswap~r1.md) | The RtlUshortByteSwap routine reverses the ordering of the two bytes in a 16-bit unsigned integer value. |
| [IoReportInterruptInactive function](..\wdm\nf-wdm-ioreportinterruptinactive.md) | The IoReportInterruptInactive routine informs the operating system that a registered interrupt service routine (ISR) is inactive and is not expecting interrupt requests. |
| [ExAcquireRundownProtection function](..\wdm\nf-wdm-exacquirerundownprotection.md) | The ExAcquireRundownProtection routine tries to acquire run-down protection on a shared object so the caller can safely access the object. |
| [MmUnmapLockedPages function](..\wdm\nf-wdm-mmunmaplockedpages.md) | The MmUnmapLockedPages routine releases a mapping that was set up by a preceding call to the MmMapLockedPages or MmMapLockedPagesSpecifyCache routine. |
| [TmReadOnlyEnlistment function](..\wdm\nf-wdm-tmreadonlyenlistment.md) | The TmReadOnlyEnlistment routine sets a specified enlistment to be read-only. |
| [IoCreateSynchronizationEvent function](..\wdm\nf-wdm-iocreatesynchronizationevent.md) | The IoCreateSynchronizationEvent routine creates or opens a named synchronization event for use in serialization of access to hardware between two otherwise unrelated drivers. |
| [IoSetIoPriorityHint function](..\wdm\nf-wdm-iosetiopriorityhint.md) | The IoSetIoPriorityHint routine sets the priority hint value for an IRP. |
| [ClfsReadPreviousRestartArea function](..\wdm\nf-wdm-clfsreadpreviousrestartarea.md) | The ClfsReadPreviousRestartArea routine reads the previous restart record relative to the current record in a read context. |
| [ObReferenceObjectByHandle function](..\wdm\nf-wdm-obreferenceobjectbyhandle.md) | The ObReferenceObjectByHandle routine provides access validation on the object handle, and, if access can be granted, returns the corresponding pointer to the object's body. |
| [ClfsLsnEqual function](..\wdm\nf-wdm-clfslsnequal.md) | The ClfsLsnEqual routine determines whether two LSNs from the same stream are equal. |
| [IoSizeOfIrp function](..\wdm\nf-wdm-iosizeofirp.md) | The IoSizeOfIrp routine determines the size in bytes for an IRP, given the number of stack locations in the IRP. |
| [ClfsRemoveLogContainerSet function](..\wdm\nf-wdm-clfsremovelogcontainerset.md) | The ClfsRemoveLogContainerSet routine atomically removes a set of containers from a CLFS log. |
| [SeDeassignSecurity function](..\wdm\nf-wdm-sedeassignsecurity.md) | The SeDeassignSecurity routine deallocates the memory associated with a security descriptor that was assigned using SeAssignSecurity. |
| [WRITE_REGISTER_USHORT function](..\wdm\nf-wdm-write-register-ushort.md) | The WRITE_REGISTER_USHORT routine writes a USHORT value to the specified address. |
| [IoReuseIrp function](..\wdm\nf-wdm-ioreuseirp.md) | The IoReuseIrp routine reinitializes an IRP so that it can be reused. |
| [ZwSetInformationEnlistment function](..\wdm\nf-wdm-zwsetinformationenlistment.md) | The ZwSetInformationEnlistment routine sets information for a specified enlistment object. |
| [RtlZeroMemory function](..\wdm\nf-wdm-rtlzeromemory.md) | The RtlZeroMemory routine fills a block of memory with zeros, given a pointer to the block and the length, in bytes, to be filled. |
| [WRITE_REGISTER_UCHAR function](..\wdm\nf-wdm-write-register-uchar.md) | The WRITE_REGISTER_UCHAR routine writes a byte to the specified address. |
| [KeRegisterBoundCallback function](..\wdm\nf-wdm-keregisterboundcallback.md) | The KeRegisterBoundCallback routine registers a routine to be called whenever a user-mode bound exception occurs. |
| [IoRemoveShareAccess function](..\wdm\nf-wdm-ioremoveshareaccess.md) | The IoRemoveShareAccess routine removes the access and share-access information for a given open instance of a file object. |
| [KeIpiGenericCall function](..\wdm\nf-wdm-keipigenericcall.md) | The KeIpiGenericCall routine causes the specified routine to run on all processors simultaneously. |
| [RtlFindSetBitsAndClear function](..\wdm\nf-wdm-rtlfindsetbitsandclear.md) | The RtlFindSetBitsAndClear routine searches for a range of set bits of a requested size within a bitmap and clears all bits in the range when it has been located. |
| [IoGetDeviceObjectPointer function](..\wdm\nf-wdm-iogetdeviceobjectpointer.md) | The IoGetDeviceObjectPointer routine returns a pointer to the top object in the named device object's stack and a pointer to the corresponding file object, if the requested access to the objects can be granted. |
| [READ_PORT_BUFFER_UCHAR function](..\wdm\nf-wdm-read-port-buffer-uchar~r2.md) | The READ_PORT_BUFFER_UCHAR routine reads a number of bytes from the specified port address into a buffer. |
| [ZwRollbackEnlistment function](..\wdm\nf-wdm-zwrollbackenlistment.md) | The ZwRollbackEnlistment routine rolls back the transaction that is associated with a specified enlistment. |
| [ExAcquireSharedWaitForExclusive function](..\wdm\nf-wdm-exacquiresharedwaitforexclusive.md) | The ExAcquireSharedWaitForExclusive routine acquires the given resource for shared access if shared access can be granted and there are no exclusive waiters. |
| [ZwOpenFile function](..\wdm\nf-wdm-zwopenfile.md) | The ZwOpenFile routine opens an existing file, directory, device, or volume. |
| [READ_PORT_BUFFER_ULONG function](..\wdm\nf-wdm-read-port-buffer-ulong~r3.md) | The READ_PORT_BUFFER_ULONG routine reads a number of ULONG values from the specified port address into a buffer. |
| [ZwQuerySymbolicLinkObject function](..\wdm\nf-wdm-zwquerysymboliclinkobject.md) | The ZwQuerySymbolicLinkObject routine returns a Unicode string that contains the target of a symbolic link. |
| [ExFreeToPagedLookasideList function](..\wdm\nf-wdm-exfreetopagedlookasidelist~r1.md) | The ExFreeToPagedLookasideList routine returns a pageable entry to the given lookaside list or to paged pool. |
| [InsertTailList function](..\wdm\nf-wdm-inserttaillist~r1.md) | The InsertTailList routine inserts an entry at the tail of a doubly linked list of LIST_ENTRY structures. |
| [ObDereferenceObjectDeferDelete function](..\wdm\nf-wdm-obdereferenceobjectdeferdelete.md) | The ObDereferenceObjectDeferDelete routine decrements the reference count for the given object, checks for object retention, and avoids deadlocks. |
| [RtlSetBit function](..\wdm\nf-wdm-rtlsetbit.md) | The RtlSetBit routine sets the specified bit in a bitmap to one. |
| [ExInitializePagedLookasideList function](..\wdm\nf-wdm-exinitializepagedlookasidelist.md) | The ExInitializePagedLookasideList routine initializes a lookaside list for pageable entries of the specified size. |
| [IoUnregisterPlugPlayNotificationEx function](..\wdm\nf-wdm-iounregisterplugplaynotificationex.md) | The IoUnregisterPlugPlayNotificationEx routine cancels the registration of a driver's callback routine for notifications of Plug and Play (PnP) events. |
| [READ_PORT_USHORT function](..\wdm\nf-wdm-read-port-ushort~r3.md) | The READ_PORT_USHORT routine reads a USHORT value from the specified port address. |
| [KeLowerIrql function](..\wdm\nf-wdm-kelowerirql~r1.md) | The KeLowerIrql routine restores the IRQL on the current processor to its original value. |
| [WRITE_REGISTER_BUFFER_USHORT function](..\wdm\nf-wdm-write-register-buffer-ushort.md) | The WRITE_REGISTER_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified register. |
| [READ_PORT_USHORT function](..\wdm\nf-wdm-read-port-ushort~r2.md) | The READ_PORT_USHORT routine reads a USHORT value from the specified port address. |
| [TmRequestOutcomeEnlistment function](..\wdm\nf-wdm-tmrequestoutcomeenlistment.md) | The TmRequestOutcomeEnlistment routine asks KTM to try to provide an immediate outcome (commit or rollback) for the transaction that is associated with a specified enlistment. |
| [ExTryConvertSharedSpinLockExclusive function](..\wdm\nf-wdm-extryconvertsharedspinlockexclusive.md) | The ExTryConvertSharedSpinLockExclusive routine attempts to convert the access state of a spin lock from acquired for shared access to exclusive access. |
| [ClfsCloseAndResetLogFile function](..\wdm\nf-wdm-clfscloseandresetlogfile.md) | The ClfsCloseAndResetLogFile routine releases all references to a specified log file object and marks its associated stream for reset. |
| [MmSizeOfMdl function](..\wdm\nf-wdm-mmsizeofmdl.md) | The MmSizeOfMdl routine returns the number of bytes to allocate for an MDL describing a given address range. |
| [IoSetDeviceInterfaceState function](..\wdm\nf-wdm-iosetdeviceinterfacestate.md) | The IoSetDeviceInterfaceState routine enables or disables an instance of a previously registered device interface class. |
| [RtlUlonglongByteSwap function](..\wdm\nf-wdm-rtlulonglongbyteswap.md) | The RtlUlonglongByteSwap routine reverses the ordering of the eight bytes in a 64-bit unsigned integer value. |
| [RtlValidRelativeSecurityDescriptor function](..\wdm\nf-wdm-rtlvalidrelativesecuritydescriptor.md) | The RtlValidRelativeSecurityDescriptor routine checks the validity of a self-relative security descriptor. |
| [ClfsMgmtDeregisterManagedClient function](..\wdm\nf-wdm-clfsmgmtderegistermanagedclient.md) | The ClfsMgmtDeregisterManagedClient routine removes the connection between a client and a log, so that the client no longer manages the log. |
| [ExConvertExclusiveToSharedLite function](..\wdm\nf-wdm-exconvertexclusivetosharedlite.md) | The ExConvertExclusiveToSharedLite routine converts a given resource from acquired for exclusive access to acquired for shared access. |
| [KeDeregisterNmiCallback function](..\wdm\nf-wdm-kederegisternmicallback.md) | The KeDeregisterNmiCallback routine deregisters a nonmaskable interrupt (NMI) callback registered by KeRegisterNmiCallback. |
| [KeSetTargetProcessorDpcEx function](..\wdm\nf-wdm-kesettargetprocessordpcex.md) | The KeSetTargetProcessorDpcEx routine specifies the processor that a DPC routine will run on. |
| [ClfsSetEndOfLog function](..\wdm\nf-wdm-clfssetendoflog.md) | The ClfsSetEndOfLog routine truncates a CLFS stream. |
| [KeRaiseIrql function](..\wdm\nf-wdm-keraiseirql.md) | The KeRaiseIrql routine raises the hardware priority to the specified IRQL value, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [KeLowerIrql function](..\wdm\nf-wdm-kelowerirql.md) | The KeLowerIrql routine restores the IRQL on the current processor to its original value. |
| [KeQueryNodeMaximumProcessorCount function](..\wdm\nf-wdm-kequerynodemaximumprocessorcount.md) | The KeQueryNodeMaximumProcessorCount routine returns the maximum number of logical processors that a specified node in a non-uniform memory access (NUMA) multiprocessor system can contain. |
| [IoIsErrorUserInduced function](..\wdm\nf-wdm-ioiserroruserinduced.md) | The IoIsErrorUserInduced routine determines whether an I/O error encountered while processing a request to a removable-media device was caused by the user. |
| [ExQueryDepthSList function](..\wdm\nf-wdm-exquerydepthslist~r2.md) | The ExQueryDepthSList routine returns the number of entries currently in a given sequenced singly linked list. |
| [SeAccessCheck function](..\wdm\nf-wdm-seaccesscheck.md) | The SeAccessCheck routine determines whether the requested access rights can be granted to an object protected by a security descriptor and an object owner. |
| [IoDeleteDevice function](..\wdm\nf-wdm-iodeletedevice.md) | The IoDeleteDevice routine removes a device object from the system, for example, when the underlying device is removed from the system. |
| [IoRegisterContainerNotification function](..\wdm\nf-wdm-ioregistercontainernotification.md) | The IoRegisterContainerNotification routine registers a kernel-mode driver to receive notifications about a specified class of events. |
| [WRITE_REGISTER_ULONG function](..\wdm\nf-wdm-write-register-ulong.md) | The WRITE_REGISTER_ULONG routine writes a ULONG value to the specified address. |
| [RtlIsNtDdiVersionAvailable function](..\wdm\nf-wdm-rtlisntddiversionavailable.md) | The RtlIsNtDdiVersionAvailable routine determines if a specified version of the Microsoft Windows device driver interface (DDI) is available. |
| [KeSetEvent function](..\wdm\nf-wdm-kesetevent.md) | The KeSetEvent routine sets an event object to a signaled state if the event was not already signaled, and returns the previous state of the event object. |
| [InterlockedExchange function](..\wdm\nf-wdm-interlockedexchange~r1.md) | The InterlockedExchange routine sets an integer variable to a given value as an atomic operation. |
| [InterlockedIncrement function](..\wdm\nf-wdm-interlockedincrement.md) | The InterlockedIncrement routine increments a caller-supplied variable as an atomic operation. |
| [IoGetDevicePropertyData function](..\wdm\nf-wdm-iogetdevicepropertydata.md) | The IoGetDevicePropertyData routine retrieves the current setting for a device property. |
| [RtlAppendUnicodeToString function](..\wdm\nf-wdm-rtlappendunicodetostring.md) | The RtlAppendUnicodeToString routine concatenates the supplied Unicode string to a buffered Unicode string. |
| [ExAllocatePoolWithTag function](..\wdm\nf-wdm-exallocatepoolwithtag.md) | The ExAllocatePoolWithTag routine allocates pool memory of the specified type and returns a pointer to the allocated block. |
| [ZwRecoverTransactionManager function](..\wdm\nf-wdm-zwrecovertransactionmanager.md) | The ZwRecoverTransactionManager routine reconstructs the state of the transaction manager object (including all transactions, enlistments, and resource managers) from the recovery information that is in the log stream. |
| [ZwEnumerateTransactionObject function](..\wdm\nf-wdm-zwenumeratetransactionobject.md) | The ZwEnumerateTransactionObject routine enumerates the KTM objects on a computer. |
| [KeAcquireSpinLock function](..\wdm\nf-wdm-keacquirespinlock.md) | The KeAcquireSpinLock routine acquires a spin lock so the caller can synchronize access to shared data in a multiprocessor-safe way by raising IRQL. |
| [MmFreePagesFromMdl function](..\wdm\nf-wdm-mmfreepagesfrommdl.md) | The MmFreePagesFromMdl routine frees all the physical pages that are described by an MDL that was created by the MmAllocatePagesForMdl routine. |
| [READ_PORT_BUFFER_USHORT function](..\wdm\nf-wdm-read-port-buffer-ushort.md) | The READ_PORT_BUFFER_USHORT routine reads a number of USHORT values from the specified port address into a buffer. |
| [RemoveHeadList function](..\wdm\nf-wdm-removeheadlist~r1.md) | The RemoveHeadList routine removes an entry from the beginning of a doubly linked list of LIST_ENTRY structures. |
| [KeQueryPerformanceCounter function](..\wdm\nf-wdm-kequeryperformancecounter.md) | The KeQueryPerformanceCounter routine retrieves the current value and frequency of the performance counter.Use KeQueryPerformanceCounter to acquire high resolution (&lt;1us) time stamps for time interval measurements. |
| [MmProbeAndLockPages function](..\wdm\nf-wdm-mmprobeandlockpages.md) | The MmProbeAndLockPages routine probes the specified virtual memory pages, makes them resident, and locks them in memory. |
| [CmUnRegisterCallback function](..\wdm\nf-wdm-cmunregistercallback.md) | The CmUnRegisterCallback routine unregisters a RegistryCallback routine that a CmRegisterCallback or CmRegisterCallbackEx routine previously registered. |
| [READ_REGISTER_BUFFER_ULONG function](..\wdm\nf-wdm-read-register-buffer-ulong~r1.md) | The READ_REGISTER_BUFFER_ULONG routine reads a number of ULONG values from the specified register address into a buffer. |
| [RtlEqualMemory function](..\wdm\nf-wdm-rtlequalmemory.md) | The RtlEqualMemory routine compares two blocks of memory to determine whether the specified number of bytes are identical. |
| [PoClearPowerRequest function](..\wdm\nf-wdm-poclearpowerrequest.md) | The PoClearPowerRequest routine decrements the count for the specified power request type. |
| [PoUnregisterPowerSettingCallback function](..\wdm\nf-wdm-pounregisterpowersettingcallback.md) | The PoUnregisterPowerSettingCallback routine unregisters a power-setting callback routine that a driver previously registered by calling the PoRegisterPowerSettingCallback routine. |
| [KeLeaveGuardedRegion function](..\wdm\nf-wdm-keleaveguardedregion.md) | The KeLeaveGuardedRegion routine exits a guarded region entered by KeEnterGuardedRegion. |
| [ClfsLsnContainer function](..\wdm\nf-wdm-clfslsncontainer.md) | The ClfsLsnContainer routine returns the logical container identifier contained in a specified LSN. |
| [TmPrePrepareComplete function](..\wdm\nf-wdm-tmprepreparecomplete.md) | The TmPrePrepareComplete routine notifies KTM that the calling resource manager has finished preliminary preparation of a transaction's data. |
| [IoGetDeviceInterfaces function](..\wdm\nf-wdm-iogetdeviceinterfaces.md) | The IoGetDeviceInterfaces routine returns a list of device interface instances of a particular device interface class (such as all devices on the system that support a HID interface). |
| [KeQueryActiveGroupCount function](..\wdm\nf-wdm-kequeryactivegroupcount.md) | The KeQueryActiveGroupCount routine returns the number of active processor groups in a multiprocessor system. |
| [ZwOpenSection function](..\wdm\nf-wdm-zwopensection.md) | The ZwOpenSection routine opens a handle for an existing section object. |
| [InterlockedExchange function](..\wdm\nf-wdm-interlockedexchange.md) | The InterlockedExchange routine sets an integer variable to a given value as an atomic operation. |
| [KeGetCurrentIrql function](..\wdm\nf-wdm-kegetcurrentirql.md) | The KeGetCurrentIrql routine returns the current IRQL. |
| [WRITE_REGISTER_BUFFER_USHORT function](..\wdm\nf-wdm-write-register-buffer-ushort~r3.md) | The WRITE_REGISTER_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified register. |
| [ZwOpenResourceManager function](..\wdm\nf-wdm-zwopenresourcemanager.md) | The ZwOpenResourceManager routine returns a handle to an existing resource manager object. |
| [WRITE_PORT_ULONG function](..\wdm\nf-wdm-write-port-ulong~r3.md) | The WRITE_PORT_ULONG routine writes a ULONG value to the specified port address. |
| [KeAcquireSpinLockAtDpcLevel function](..\wdm\nf-wdm-keacquirespinlockatdpclevel.md) | The KeAcquireSpinLockAtDpcLevel routine acquires a spin lock when the caller is already running at IRQL &gt;= DISPATCH_LEVEL. |
| [ExSetTimerResolution function](..\wdm\nf-wdm-exsettimerresolution.md) | The ExSetTimerResolution routine modifies the frequency at which the system clock interrupts. Use this routine with extreme caution (see the following Remarks section). |
| [CmCallbackGetKeyObjectIDEx function](..\wdm\nf-wdm-cmcallbackgetkeyobjectidex.md) | The CmCallbackGetKeyObjectIDEx routine retrieves the unique identifier and object name that are associated with a specified registry key object. |
| [PoFxSetDeviceIdleTimeout function](..\wdm\nf-wdm-pofxsetdeviceidletimeout.md) | The PoFxSetDeviceIdleTimeout routine specifies the minimum time interval from when the last component of the device enters the idle condition to when the power management framework (PoFx) calls the driver's DevicePowerNotRequiredCallback routine. |
| [WRITE_REGISTER_BUFFER_UCHAR function](..\wdm\nf-wdm-write-register-buffer-uchar.md) | The WRITE_REGISTER_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified register. |
| [IoFreeWorkItem function](..\wdm\nf-wdm-iofreeworkitem.md) | The IoFreeWorkItem routine frees a work item that was allocated by IoAllocateWorkItem. |
| [KeRemoveDeviceQueue function](..\wdm\nf-wdm-keremovedevicequeue.md) | The KeRemoveDeviceQueue routine removes an entry from the head of a specified device queue. |
| [PsCreateSystemThread function](..\wdm\nf-wdm-pscreatesystemthread.md) | The PsCreateSystemThread routine creates a system thread that executes in kernel mode and returns a handle for the thread. |
| [READ_REGISTER_BUFFER_UCHAR function](..\wdm\nf-wdm-read-register-buffer-uchar~r3.md) | The READ_REGISTER_BUFFER_UCHAR routine reads a number of bytes from the specified register address into a buffer. |
| [ExIsResourceAcquiredSharedLite function](..\wdm\nf-wdm-exisresourceacquiredsharedlite.md) | The ExIsResourceAcquiredSharedLite routine returns whether the current thread has access (either shared or exclusive) to a given resource. |
| [RtlInitString function](..\wdm\nf-wdm-rtlinitstring.md) | The RtlInitString routine initializes a counted string of 8-bit characters. |
| [ExIsSoftBoot function](..\wdm\nf-wdm-exissoftboot.md) | Determines whether the system has gone through a soft restart. |
| [ExInterlockedPushEntrySList function](..\wdm\nf-wdm-exinterlockedpushentryslist~r2.md) | The ExInterlockedPushEntrySList routine atomically inserts an entry at the beginning of a sequenced singly linked list. |
| [MmAllocateNodePagesForMdlEx function](..\wdm\nf-wdm-mmallocatenodepagesformdlex.md) | The MmAllocateNodePagesForMdlEx routine allocates nonpaged physical memory from an ideal node, and allocates an MDL structure to describe this memory. |
| [WRITE_PORT_UCHAR function](..\wdm\nf-wdm-write-port-uchar~r3.md) | The WRITE_PORT_UCHAR routine writes a byte to the specified port address. |
| [IoRegisterPlugPlayNotification function](..\wdm\nf-wdm-ioregisterplugplaynotification.md) | The IoRegisterPlugPlayNotification routine registers a Plug and Play (PnP) notification callback routine to be called when a PnP event of the specified category occurs. |
| [ExAllocatePool function](..\wdm\nf-wdm-exallocatepool.md) | The ExAllocatePool routine is obsolete, and is exported only for existing binaries. Use ExAllocatePoolWithTag instead.ExAllocatePool allocates pool memory of the specified type and returns a pointer to the allocated block. |
| [KeInitializeThreadedDpc function](..\wdm\nf-wdm-keinitializethreadeddpc.md) | The KeInitializeThreadedDpc routine initializes a threaded DPC object, and registers a CustomThreadedDpc routine for that object. |
| [MmIsDriverVerifying function](..\wdm\nf-wdm-mmisdriververifying.md) | The MmIsDriverVerifying routine indicates whether the kernel-mode driver that is identified by the specified driver object is being verified or calls a driver that is being verified by Driver Verifier. |
| [IoStartPacket function](..\wdm\nf-wdm-iostartpacket.md) | The IoStartPacket routine calls the driver's StartIo routine with the given IRP or inserts the IRP into the device queue associated with the given device object if the device is already busy. |
| [KeQueryInterruptTime function](..\wdm\nf-wdm-kequeryinterrupttime.md) | The KeQueryInterruptTime routine returns the current value of the system interrupt time count, with accuracy to within system clock tick. |
| [InitializeListHead function](..\wdm\nf-wdm-initializelisthead.md) | The InitializeListHead routine initializes a LIST_ENTRY structure that represents the head of a doubly linked list. |
| [WRITE_PORT_BUFFER_UCHAR function](..\wdm\nf-wdm-write-port-buffer-uchar~r2.md) | The WRITE_PORT_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified port. |
| [ExInitializeRundownProtection function](..\wdm\nf-wdm-exinitializerundownprotection.md) | The ExInitializeRundownProtection routine initializes run-down protection on a shared object. |
| [ZwSinglePhaseReject function](..\wdm\nf-wdm-zwsinglephasereject.md) | The ZwSinglePhaseReject routine informs KTM that the calling resource manager will not support single-phase commit operations for a specified enlistment. |
| [InsertTailList function](..\wdm\nf-wdm-inserttaillist.md) | The InsertTailList routine inserts an entry at the tail of a doubly linked list of LIST_ENTRY structures. |
| [RtlAreBitsSet function](..\wdm\nf-wdm-rtlarebitsset.md) | The RtlAreBitsSet routine determines whether a given range of bits within a bitmap variable is set. |
| [KeTestSpinLock function](..\wdm\nf-wdm-ketestspinlock.md) | The KeTestSpinLock routine tests for the availability of a spin lock. |
| [ZwCommitTransaction function](..\wdm\nf-wdm-zwcommittransaction.md) | The ZwCommitTransaction routine initiates a commit operation for a specified transaction. |
| [MmGetSystemAddressForMdl function](..\wdm\nf-wdm-mmgetsystemaddressformdl.md) | The MmGetSystemAddressForMdl routine is obsolete for Windows 2000 and later versions of Windows, and for Windows Me. |
| [RtlInitializeBitMap function](..\wdm\nf-wdm-rtlinitializebitmap.md) | The RtlInitializeBitMap routine initializes the header of a bitmap variable. |
| [SeAssignSecurity function](..\wdm\nf-wdm-seassignsecurity.md) | The SeAssignSecurity routine builds a self-relative security descriptor for a new object, given the security descriptor of its parent directory and any originally requested security for the object. |
| [KeReadStateTimer function](..\wdm\nf-wdm-kereadstatetimer.md) | The KeReadStateTimer routine reads the current state of a timer object. |
| [IoWMIQueryAllDataMultiple function](..\wdm\nf-wdm-iowmiqueryalldatamultiple.md) | The IoWMIQueryAllDataMultiple routine returns all WMI data blocks that implement one of a set of WMI classes. |
| [InterlockedCompareExchange function](..\wdm\nf-wdm-interlockedcompareexchange~r1.md) | The InterlockedCompareExchange routine performs an atomic operation that compares the input value pointed to by Destination with the value of Comparand. |
| [ClfsReserveAndAppendLogAligned function](..\wdm\nf-wdm-clfsreserveandappendlogaligned.md) | The ClfsReserveAndAppendLogAligned routine reserves space in a marshalling area or appends a record to a marshalling area or does both atomically. The record's data is aligned on specified boundaries. |
| [RtlIoEncodeMemIoResource function](..\wdm\nf-wdm-rtlioencodememioresource.md) | The RtlIoEncodeMemIoResource routine updates an IO_RESOURCE_DESCRIPTOR structure to describe a range of memory or I/O port addresses. |
| [IoCreateSystemThread function](..\wdm\nf-wdm-iocreatesystemthread.md) | The IoCreateSystemThread routine creates a system thread that executes in kernel mode, and supplies a handle for the thread. |
| [ZwQueryInformationTransactionManager function](..\wdm\nf-wdm-zwqueryinformationtransactionmanager.md) | The ZwQueryInformationTransactionManager routine retrieves information about a specified transaction manager object. |
| [PoFxReportDevicePoweredOn function](..\wdm\nf-wdm-pofxreportdevicepoweredon.md) | The PoFxReportDevicePoweredOn routine notifies the power management framework (PoFx) that the device completed the requested transition to the D0 (fully on) power state. |
| [READ_PORT_UCHAR function](..\wdm\nf-wdm-read-port-uchar~r1.md) | The READ_PORT_UCHAR routine reads a byte from the specified port address. |
| [IoUnregisterContainerNotification function](..\wdm\nf-wdm-iounregistercontainernotification.md) | The IoUnregisterContainerNotification routine cancels a container notification registration that was previously created by the IoRegisterContainerNotification routine. |
| [ZwRollbackTransaction function](..\wdm\nf-wdm-zwrollbacktransaction.md) | The ZwRollbackTransaction routine initiates a rollback operation for a specified transaction. |
| [ClfsReadLogRecord function](..\wdm\nf-wdm-clfsreadlogrecord.md) | The ClfsReadLogRecord routine reads a target record in a CLFS stream and returns a read context that the caller can use to read the records preceding or following it in the stream. |
| [IoWMISetSingleInstance function](..\wdm\nf-wdm-iowmisetsingleinstance.md) | The IoWMISetSingleInstance routine sets the values for properties within the data block instance that matches the specified WMI class and instance name. |
| [PoCreatePowerRequest function](..\wdm\nf-wdm-pocreatepowerrequest.md) | The PoCreatePowerRequest routine creates a power request object. |
| [TmRollbackTransaction function](..\wdm\nf-wdm-tmrollbacktransaction.md) | The TmRollbackTransaction routine initiates a rollback operation for a specified transaction. |
| [TmReferenceEnlistmentKey function](..\wdm\nf-wdm-tmreferenceenlistmentkey.md) | The TmReferenceEnlistmentKey routine increments the reference count for the key of a specified enlistment object and retrieves the key. |
| [RemoveEntryList function](..\wdm\nf-wdm-removeentrylist.md) | The RemoveEntryList routine removes an entry from a doubly linked list of LIST_ENTRY structures. |
| [RtlDowncaseUnicodeChar function](..\wdm\nf-wdm-rtldowncaseunicodechar.md) | The RtlDowncaseUnicodeChar routine converts the specified Unicode character to lowercase. |
| [ExInterlockedFlushSList function](..\wdm\nf-wdm-exinterlockedflushslist~r1.md) | The ExInterlockedFlushSList routine atomically removes all entries from a sequenced singly linked list. |
| [RtlUlongByteSwap function](..\wdm\nf-wdm-rtlulongbyteswap.md) | The RtlUlongByteSwap routine reverses the ordering of the four bytes in a 32-bit unsigned integer value. |
| [WRITE_PORT_BUFFER_USHORT function](..\wdm\nf-wdm-write-port-buffer-ushort.md) | The WRITE_PORT_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified port address. |
| [PoStartDeviceBusy function](..\wdm\nf-wdm-postartdevicebusy.md) | The PoStartDeviceBusy routine marks the start of a period of time in which the device is busy. |
| [WRITE_PORT_BUFFER_USHORT function](..\wdm\nf-wdm-write-port-buffer-ushort~r3.md) | The WRITE_PORT_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified port address. |
| [WRITE_PORT_BUFFER_ULONG function](..\wdm\nf-wdm-write-port-buffer-ulong.md) | The WRITE_PORT_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified port address. |
| [IoRegisterLastChanceShutdownNotification function](..\wdm\nf-wdm-ioregisterlastchanceshutdownnotification.md) | The IoRegisterLastChanceShutdownNotification routine registers a driver to receive an IRP_MJ_SHUTDOWN IRP when the system is shut down, after all file systems have been flushed. |
| [KeRemoveEntryDeviceQueue function](..\wdm\nf-wdm-keremoveentrydevicequeue.md) | The KeRemoveEntryDeviceQueue routine returns whether the specified entry is in the device queue and removes it, if it was queued, from the device queue. |
| [ObDereferenceObjectWithTag function](..\wdm\nf-wdm-obdereferenceobjectwithtag.md) | The ObDereferenceObjectWithTag routine decrements the reference count of the specified object, and writes a four-byte tag value to the object to support object reference tracing. |
| [ExFreeToPagedLookasideList function](..\wdm\nf-wdm-exfreetopagedlookasidelist.md) | The ExFreeToPagedLookasideList routine returns a pageable entry to the given lookaside list or to paged pool. |
| [ExDeleteResourceLite function](..\wdm\nf-wdm-exdeleteresourcelite.md) | The ExDeleteResourceLite routine deletes a given resource from the system's resource list. |
| [IoIsWdmVersionAvailable function](..\wdm\nf-wdm-ioiswdmversionavailable.md) | The IoIsWdmVersionAvailable routine checks whether a given WDM version is supported by the operating system. |
| [KeReleaseMutex function](..\wdm\nf-wdm-kereleasemutex.md) | The KeReleaseMutex routine releases a mutex object, and specifies whether the caller is to call one of the KeWaitXxx routines as soon as KeReleaseMutex returns control. |
| [WmiQueryTraceInformation function](..\wdm\nf-wdm-wmiquerytraceinformation.md) | The WmiQueryTraceInformation routine returns information about a WMI event trace. |
| [PoFxRegisterDevice function](..\wdm\nf-wdm-pofxregisterdevice.md) | The PoFxRegisterDevice routine registers a device with the power management framework (PoFx). |
| [ExFreeToNPagedLookasideList function](..\wdm\nf-wdm-exfreetonpagedlookasidelist.md) | The ExFreeToNPagedLookasideList routine returns a nonpaged entry to the given lookaside list or to nonpaged pool. |
| [CmSetCallbackObjectContext function](..\wdm\nf-wdm-cmsetcallbackobjectcontext.md) | The CmSetCallbackObjectContext routine associates specified context information with a specified registry object. |
| [ExAllocatePoolWithQuotaTag function](..\wdm\nf-wdm-exallocatepoolwithquotatag.md) | The ExAllocatePoolWithQuotaTag routine allocates pool memory, charging the quota against the current process. |
| [MmResetDriverPaging function](..\wdm\nf-wdm-mmresetdriverpaging.md) | The MmResetDriverPaging routine resets the pageable status of a driver's sections to that specified when the driver was compiled. |
| [RtlLengthSecurityDescriptor function](..\wdm\nf-wdm-rtllengthsecuritydescriptor.md) | The RtlLengthSecurityDescriptor routine returns the size of a given security descriptor. |
| [PopEntryList function](..\wdm\nf-wdm-popentrylist.md) | The PopEntryList routine removes the first entry from a singly linked list of SINGLE_LIST_ENTRY structures. |
| [ExQueryDepthSList function](..\wdm\nf-wdm-exquerydepthslist~r1.md) | The ExQueryDepthSList routine returns the number of entries currently in a given sequenced singly linked list. |
| [ZwOpenKeyEx function](..\wdm\nf-wdm-zwopenkeyex.md) | The ZwOpenKeyEx routine opens an existing registry key. |
| [WRITE_PORT_ULONG function](..\wdm\nf-wdm-write-port-ulong.md) | The WRITE_PORT_ULONG routine writes a ULONG value to the specified port address. |
| [IoGetIoPriorityHint function](..\wdm\nf-wdm-iogetiopriorityhint.md) | The IoGetIoPriorityHint routine gets the priority hint value from an IRP. |
| [RtlFindFirstRunClear function](..\wdm\nf-wdm-rtlfindfirstrunclear.md) | The RtlFindFirstRunClear routine searches for the initial contiguous range of clear bits within a given bitmap. |
| [ObReferenceObjectByPointerWithTag function](..\wdm\nf-wdm-obreferenceobjectbypointerwithtag.md) | The ObReferenceObjectByPointerWithTag routine increments the reference count of the specified object, and writes a four-byte tag value to the object to support object reference tracing. |
| [ExIsProcessorFeaturePresent function](..\wdm\nf-wdm-exisprocessorfeaturepresent.md) | The ExIsProcessorFeaturePresent routine queries for the existence of a specified processor feature. |
| [ClfsFlushBuffers function](..\wdm\nf-wdm-clfsflushbuffers.md) | The ClfsFlushBuffers routine forces all log I/O blocks in a specified marshalling area to stable storage. |
| [PoFxUnregisterDevice function](..\wdm\nf-wdm-pofxunregisterdevice.md) | The PoFxUnregisterDevice routine removes the registration of a device from the power management framework (PoFx). |
| [ZwPrepareEnlistment function](..\wdm\nf-wdm-zwprepareenlistment.md) | The ZwPrepareEnlistment routine initiates the prepare operation for a specified enlistment's transaction. |
| [KeEnterCriticalRegion function](..\wdm\nf-wdm-keentercriticalregion.md) | The KeEnterCriticalRegion routine temporarily disables the execution of normal kernel APCs, but does not prevent special kernel APCs from running. |
| [ExDeleteTimer function](..\wdm\nf-wdm-exdeletetimer.md) | The ExDeleteTimer routine deletes a timer object that was previously allocated by the ExAllocateTimer routine. |
| [READ_PORT_ULONG function](..\wdm\nf-wdm-read-port-ulong~r3.md) | The READ_PORT_ULONG routine reads a ULONG value from the specified port address. |
| [ExInterlockedPushEntryList function](..\wdm\nf-wdm-exinterlockedpushentrylist.md) | The ExInterlockedPushEntryList routine atomically inserts an entry at the beginning of a singly linked list of SINGLE_LIST_ENTRY structures. |
| [ExGetFirmwareEnvironmentVariable function](..\wdm\nf-wdm-exgetfirmwareenvironmentvariable.md) | The ExGetFirmwareEnvironmentVariable routine gets the value of the specified system firmware environment variable. |
| [SeAssignSecurityEx function](..\wdm\nf-wdm-seassignsecurityex.md) | The SeAssignSecurityEx routine builds a self-relative security descriptor for a new object given the following optional parameters |
| [IoAdjustPagingPathCount function](..\wdm\nf-wdm-ioadjustpagingpathcount.md) | The IoAdjustPagingPathCount routine increments or decrements a caller-supplied page-file counter as an atomic operation. |
| [KeReleaseSemaphore function](..\wdm\nf-wdm-kereleasesemaphore.md) | The KeReleaseSemaphore routine releases the specified semaphore object. |
| [IoReportTargetDeviceChangeAsynchronous function](..\wdm\nf-wdm-ioreporttargetdevicechangeasynchronous.md) | The IoReportTargetDeviceChangeAsynchronous routine notifies the PnP manager that a custom event has occurred on a device. |
| [READ_REGISTER_USHORT function](..\wdm\nf-wdm-read-register-ushort.md) | The READ_REGISTER_USHORT routine reads a USHORT value from the specified register address. |
| [READ_REGISTER_USHORT function](..\wdm\nf-wdm-read-register-ushort~r1.md) | The READ_REGISTER_USHORT routine reads a USHORT value from the specified register address. |
| [ZwQueryInformationResourceManager function](..\wdm\nf-wdm-zwqueryinformationresourcemanager.md) | The ZwQueryInformationResourceManager routine retrieves information about a specified resource manager object. |
| [RtlIntegerToUnicodeString function](..\wdm\nf-wdm-rtlintegertounicodestring.md) | The RtlIntegerToUnicodeString routine converts an unsigned integer value to a null-terminated string of one or more Unicode characters in the specified base. |
| [TmPrePrepareEnlistment function](..\wdm\nf-wdm-tmpreprepareenlistment.md) | The TmPrePrepareEnlistment routine initiates the pre-prepare operation for a specified enlistment's transaction. |
| [ZwCreateResourceManager function](..\wdm\nf-wdm-zwcreateresourcemanager.md) | The ZwCreateResourceManager routine creates a resource manager object. |
| [MmIsDriverVerifyingByAddress function](..\wdm\nf-wdm-mmisdriververifyingbyaddress.md) | The MmIsDriverVerifyingByAddress routine checks whether the kernel-mode driver that is identified by the specified image address is being verified or calls a driver that is being verified by Driver Verifier. |
| [IoGetDeviceProperty function](..\wdm\nf-wdm-iogetdeviceproperty.md) | The IoGetDeviceProperty routine retrieves information about a device such as configuration information and the name of its PDO. |
| [RtlFreeUnicodeString function](..\wdm\nf-wdm-rtlfreeunicodestring.md) | The RtlFreeUnicodeString routine releases storage that was allocated by RtlAnsiStringToUnicodeString or RtlUpcaseUnicodeString. |
| [RtlFindLastBackwardRunClear function](..\wdm\nf-wdm-rtlfindlastbackwardrunclear.md) | The RtlFindLastBackwardRunClear routine searches a given bitmap for the preceding clear run of bits, starting from the specified index position. |
| [ClfsReadRestartArea function](..\wdm\nf-wdm-clfsreadrestartarea.md) | The ClfsReadRestartArea routine reads the restart record that was most recently written to a specified CLFS stream. |
| [IoDeleteSymbolicLink function](..\wdm\nf-wdm-iodeletesymboliclink.md) | The IoDeleteSymbolicLink routine removes a symbolic link from the system. |
| [IoAllocateIrp function](..\wdm\nf-wdm-ioallocateirp.md) | The IoAllocateIrp routine allocates an IRP, given the number of I/O stack locations for each driver layered under the caller, and, optionally, for the caller. |
| [PoFxNotifySurprisePowerOn function](..\wdm\nf-wdm-pofxnotifysurprisepoweron.md) | The PoFxNotifySurprisePowerOn routine notifies the power management framework (PoFx) that a device was turned on as a side effect of supplying power to some other device. |
| [ExQueryDepthSList function](..\wdm\nf-wdm-exquerydepthslist.md) | The ExQueryDepthSList routine returns the number of entries currently in a given sequenced singly linked list. |
| [KeCancelTimer function](..\wdm\nf-wdm-kecanceltimer.md) | The KeCancelTimer routine dequeues a timer object before the timer interval, if any was set, expires. |
| [KeQueryMaximumGroupCount function](..\wdm\nf-wdm-kequerymaximumgroupcount.md) | The KeQueryMaximumGroupCount routine returns the maximum number of groups in a multiprocessor system. |
| [AppendTailList function](..\wdm\nf-wdm-appendtaillist.md) | The AppendTailList routine appends a doubly linked list of LIST_ENTRY structures to the tail of another doubly linked list of LIST_ENTRY structures. |
| [MmMapLockedPagesWithReservedMapping function](..\wdm\nf-wdm-mmmaplockedpageswithreservedmapping.md) | The MmMapLockedPagesWithReservedMapping routine maps all or part of an address range that was previously reserved by the MmAllocateMappingAddress routine. |
| [KeConvertAuxiliaryCounterToPerformanceCounter function](..\wdm\nf-wdm-keconvertauxiliarycountertoperformancecounter.md) | The KeConvertAuxiliaryCounterToPerformanceCounter routine converts the specified auxiliary counter value into a performance counter value. |
| [KeDeregisterProcessorChangeCallback function](..\wdm\nf-wdm-kederegisterprocessorchangecallback.md) | The KeDeregisterProcessorChangeCallback routine unregisters a callback function that was previously registered with the operating system by calling the KeRegisterProcessorChangeCallback routine. |
| [IoWMIAllocateInstanceIds function](..\wdm\nf-wdm-iowmiallocateinstanceids.md) | The IoWMIAllocateInstanceIds routine allocates one or more instance IDs that are unique to the GUID. |
| [IoGetDeviceInterfacePropertyData function](..\wdm\nf-wdm-iogetdeviceinterfacepropertydata.md) | The IoGetDeviceInterfacePropertyData routine retrieves the current value of a device interface property. |
| [ProbeForRead function](..\wdm\nf-wdm-probeforread.md) | The ProbeForRead routine checks that a user-mode buffer actually resides in the user portion of the address space, and is correctly aligned. |
| [WRITE_REGISTER_BUFFER_UCHAR function](..\wdm\nf-wdm-write-register-buffer-uchar~r2.md) | The WRITE_REGISTER_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified register. |
| [ZwReadFile function](..\wdm\nf-wdm-zwreadfile.md) | The ZwReadFile routine reads data from an open file. |
| [ExInterlockedPushEntrySList function](..\wdm\nf-wdm-exinterlockedpushentryslist~r1.md) | The ExInterlockedPushEntrySList routine atomically inserts an entry at the beginning of a sequenced singly linked list. |
| [ZwMakeTemporaryObject function](..\wdm\nf-wdm-zwmaketemporaryobject.md) | The ZwMakeTemporaryObject routine changes the attributes of an object to make it temporary. |
| [TmCommitTransaction function](..\wdm\nf-wdm-tmcommittransaction.md) | The TmCommitTransaction routine initiates a commit operation for a specified transaction. |
| [RtlUnicodeStringToAnsiSize function](..\wdm\nf-wdm-rtlunicodestringtoansisize.md) | The RtlUnicodeStringToAnsiSize routine returns the number of bytes required for a null-terminated ANSI string that is equivalent to a specified Unicode string. |
| [ExReleaseResourceForThreadLite function](..\wdm\nf-wdm-exreleaseresourceforthreadlite.md) | The ExReleaseResourceForThreadLite routine releases the input resource of the indicated thread. |
| [WRITE_PORT_UCHAR function](..\wdm\nf-wdm-write-port-uchar~r2.md) | The WRITE_PORT_UCHAR routine writes a byte to the specified port address. |
| [IoWMIDeviceObjectToProviderId function](..\wdm\nf-wdm-iowmideviceobjecttoproviderid.md) | The IoWMIDeviceObjectToProviderId routine translates the specified device object into the corresponding WMI Provider ID. |
| [ZwFlushKey function](..\wdm\nf-wdm-zwflushkey.md) | The ZwFlushKey routine forces a registry key to be committed to disk. |
| [ClfsTerminateReadLog function](..\wdm\nf-wdm-clfsterminatereadlog.md) | The ClfsTerminateReadLog routine invalidates a specified read context after freeing resources associated with the context. |
| [ExIsResourceAcquiredExclusiveLite function](..\wdm\nf-wdm-exisresourceacquiredexclusivelite.md) | The ExIsResourceAcquiredExclusiveLite routine returns whether the current thread has exclusive access to a given resource. |
| [ClfsMgmtHandleLogFileFull function](..\wdm\nf-wdm-clfsmgmthandlelogfilefull.md) | The ClfsMgmtHandleLogFileFull routine attempts to make more space available in a log. It might make more space available by adding containers to the log, or it might ask clients to move their log tails. |
| [RtlGUIDFromString function](..\wdm\nf-wdm-rtlguidfromstring.md) | The RtlGUIDFromString routine converts the given Unicode string to a GUID in binary format. |
| [RtlCreateRegistryKey function](..\wdm\nf-wdm-rtlcreateregistrykey.md) | The RtlCreateRegistryKey routine adds a key object in the registry along a given relative path. |
| [RtlHashUnicodeString function](..\wdm\nf-wdm-rtlhashunicodestring.md) | The RtlHashUnicodeString routine creates a hash value from a given Unicode string and hash algorithm. |
| [IoSetDevicePropertyData function](..\wdm\nf-wdm-iosetdevicepropertydata.md) | The IoSetDevicePropertyData routine modifies the current setting for a device property. |
| [IoGetStackLimits function](..\wdm\nf-wdm-iogetstacklimits.md) | The IoGetStackLimits routine returns the boundaries of the current thread's stack frame. |
| [IoWMISetNotificationCallback function](..\wdm\nf-wdm-iowmisetnotificationcallback.md) | The IoWMISetNotificationCallback routine registers a notification callback for a WMI event. |
| [IoFreeIrp function](..\wdm\nf-wdm-iofreeirp.md) | The IoFreeIrp routine releases a caller-allocated IRP from the caller's IoCompletion routine. |
| [KeClearEvent function](..\wdm\nf-wdm-keclearevent.md) | The KeClearEvent routine sets an event to a not-signaled state. |
| [IoSetCompletionRoutineEx function](..\wdm\nf-wdm-iosetcompletionroutineex.md) | The IoSetCompletionRoutineEx routine registers an IoCompletion routine, which is called when the next-lower-level driver has completed the requested operation for the given IRP. |
| [IoCsqInsertIrpEx function](..\wdm\nf-wdm-iocsqinsertirpex.md) | The IoCsqInsertIrpEx routine inserts an IRP into the driver's cancel-safe IRP queue. |
| [IoValidateDeviceIoControlAccess function](..\wdm\nf-wdm-iovalidatedeviceiocontrolaccess.md) | For more information, see the WdmlibIoValidateDeviceIoControlAccess function. |
| [READ_REGISTER_ULONG function](..\wdm\nf-wdm-read-register-ulong~r2.md) | The READ_REGISTER_ULONG routine reads a ULONG value from the specified register address. |
| [KeStallExecutionProcessor function](..\wdm\nf-wdm-kestallexecutionprocessor.md) | The KeStallExecutionProcessor routine stalls the caller on the current processor for a specified time interval. |
| [ClfsAdvanceLogBase function](..\wdm\nf-wdm-clfsadvancelogbase.md) | The ClfsAdvanceLogBase routine sets the base LSN of a CLFS stream. |
| [MmLockPagableCodeSection function](..\wdm\nf-wdm-mmlockpagablecodesection.md) | The MmLockPagableCodeSection routine locks a section of driver code, containing a set of driver routines marked with a special compiler directive, into system space. |
| [KeGetRecommendedSharedDataAlignment function](..\wdm\nf-wdm-kegetrecommendedshareddataalignment.md) | The KeGetRecommendedSharedDataAlignment routine returns the preferred alignment for memory structures that can be accessed by more than one processor. |
| [CmCallbackReleaseKeyObjectIDEx function](..\wdm\nf-wdm-cmcallbackreleasekeyobjectidex.md) | The CmCallbackReleaseKeyObjectIDEx routine frees an object name string obtained from the CmCallbackGetKeyObjectIDEx routine. |
| [KeQueryHighestNodeNumber function](..\wdm\nf-wdm-kequeryhighestnodenumber.md) | The KeQueryHighestNodeNumber routine returns the highest node number in a multiprocessor system that has a non-uniform memory access (NUMA) architecture. |
| [KeQueryPriorityThread function](..\wdm\nf-wdm-kequeryprioritythread.md) | The KeQueryPriorityThread routine returns the current priority of a particular thread. |
| [ObDereferenceObject function](..\wdm\nf-wdm-obdereferenceobject.md) | The ObDereferenceObject routine decrements the given object's reference count and performs retention checks. |
| [KeInitializeDeviceQueue function](..\wdm\nf-wdm-keinitializedevicequeue.md) | The KeInitializeDeviceQueue routine initializes a device queue object to a not-busy state. |
| [CmGetCallbackVersion function](..\wdm\nf-wdm-cmgetcallbackversion.md) | The CmGetCallbackVersion routine retrieves the major and minor version numbers for the current version of the configuration manager's registry callback feature. |
| [ObReferenceObject function](..\wdm\nf-wdm-obreferenceobject.md) | The ObReferenceObject routine increments the reference count to the given object. |
| [ExInitializeFastMutex function](..\wdm\nf-wdm-exinitializefastmutex.md) | The ExInitializeFastMutex routine initializes a fast mutex variable, used to synchronize mutually exclusive access by a set of threads to a shared resource. |
| [RtlCompareMemory function](..\wdm\nf-wdm-rtlcomparememory.md) | The RtlCompareMemory routine compares two blocks of memory and returns the number of bytes that match. |
| [IoCheckShareAccess function](..\wdm\nf-wdm-iocheckshareaccess.md) | The IoCheckShareAccess routine is called by file system drivers (FSDs) or other highest-level drivers to check whether shared access to a file object is permitted. |
| [IoDetachDevice function](..\wdm\nf-wdm-iodetachdevice.md) | The IoDetachDevice routine releases an attachment between the caller's device object and a lower driver's device object. |
| [READ_PORT_UCHAR function](..\wdm\nf-wdm-read-port-uchar.md) | The READ_PORT_UCHAR routine reads a byte from the specified port address. |
| [ZwSetValueKey function](..\wdm\nf-wdm-zwsetvaluekey.md) | The ZwSetValueKey routine creates or replaces a registry key's value entry. |
| [IoUnregisterShutdownNotification function](..\wdm\nf-wdm-iounregistershutdownnotification.md) | The IoUnregisterShutdownNotification routine removes a registered driver from the shutdown notification queue. |
| [IoCsqRemoveIrp function](..\wdm\nf-wdm-iocsqremoveirp.md) | The IoCsqRemoveIrp routine removes a particular IRP from the queue. |
| [ObReferenceObjectByPointer function](..\wdm\nf-wdm-obreferenceobjectbypointer.md) | The ObReferenceObjectByPointer routine increments the pointer reference count for a given object. |
| [PoGetSystemWake function](..\wdm\nf-wdm-pogetsystemwake.md) | The PoGetSystemWake routine determines whether a specified IRP has been marked as waking the system from a sleeping state. |
| [IoCsqInitializeEx function](..\wdm\nf-wdm-iocsqinitializeex.md) | The IoCsqInitializeEx routine initializes the dispatch table for a cancel-safe IRP queue. |
| [IoInitializeWorkItem function](..\wdm\nf-wdm-ioinitializeworkitem.md) | The IoInitializeWorkItem routine initializes a work item that the caller has already allocated. |
| [ZwOpenSymbolicLinkObject function](..\wdm\nf-wdm-zwopensymboliclinkobject.md) | The ZwOpenSymbolicLinkObject routine opens an existing symbolic link. |
| [RtlSetBits function](..\wdm\nf-wdm-rtlsetbits.md) | The RtlSetBits routine sets all bits in a given range of a given bitmap variable. |
| [IoGetFunctionCodeFromCtlCode function](..\wdm\nf-wdm-iogetfunctioncodefromctlcode.md) | The IoGetFunctionCodeFromCtlCode macro returns the value of the function code contained in an I/O control code. |
| [IoAttachDeviceToDeviceStack function](..\wdm\nf-wdm-ioattachdevicetodevicestack.md) | The IoAttachDeviceToDeviceStack routine attaches the caller's device object to the highest device object in the chain and returns a pointer to the previously highest device object. |
| [KeQueryMaximumProcessorCountEx function](..\wdm\nf-wdm-kequerymaximumprocessorcountex.md) | The KeQueryMaximumProcessorCountEx routine returns the maximum number of logical processors in a specified group in a multiprocessor system. |
| [ExInitializeNPagedLookasideList function](..\wdm\nf-wdm-exinitializenpagedlookasidelist.md) | The ExInitializeNPagedLookasideList routine initializes a lookaside list for nonpaged entries of the specified size. |
| [KeLeaveCriticalRegion function](..\wdm\nf-wdm-keleavecriticalregion.md) | The KeLeaveCriticalRegion routine reenables the delivery of normal kernel-mode APCs that were disabled by a preceding call to KeEnterCriticalRegion. |
| [IoUpdateLinkShareAccess function](..\wdm\nf-wdm-ioupdatelinkshareaccess.md) | The IoUpdateLinkShareAccess routine updates the share access for the given file object, usually when the file is being opened. |
| [RtlFindClearBits function](..\wdm\nf-wdm-rtlfindclearbits.md) | The RtlFindClearBits routine searches for a range of clear bits of a requested size within a bitmap. |
| [CmCallbackGetKeyObjectID function](..\wdm\nf-wdm-cmcallbackgetkeyobjectid.md) | The CmCallbackGetKeyObjectID routine retrieves the unique identifier and object name that are associated with a specified registry key object. |
| [KeRestoreFloatingPointState function](..\wdm\nf-wdm-kerestorefloatingpointstate~r2.md) | The KeRestoreFloatingPointState routine restores the nonvolatile floating-point context saved by the preceding call to KeSaveFloatingPointState. |
| [ObReferenceObjectWithTag function](..\wdm\nf-wdm-obreferenceobjectwithtag.md) | The ObReferenceObjectWithTag routine increments the reference count of the specified object, and writes a four-byte tag value to the object to support object reference tracing. |
| [KeAcquireSpinLock function](..\wdm\nf-wdm-keacquirespinlock~r1.md) | The KeAcquireSpinLock routine acquires a spin lock so the caller can synchronize access to shared data in a multiprocessor-safe way by raising IRQL. |
| [TmRollbackEnlistment function](..\wdm\nf-wdm-tmrollbackenlistment.md) | The TmRollbackEnlistment routine rolls back a specified enlistment. |
| [IoGetBootDiskInformation function](..\wdm\nf-wdm-iogetbootdiskinformation.md) | The IoGetBootDiskInformation routine returns information describing the boot and system disks. |
| [RemoveHeadList function](..\wdm\nf-wdm-removeheadlist.md) | The RemoveHeadList routine removes an entry from the beginning of a doubly linked list of LIST_ENTRY structures. |
| [PoFxCompleteDevicePowerNotRequired function](..\wdm\nf-wdm-pofxcompletedevicepowernotrequired.md) | The PoFxCompleteDevicePowerNotRequired routine notifies the power management framework (PoFx) that the calling driver has completed its response to a call to the driver's DevicePowerNotRequiredCallback callback routine. |
| [TmRecoverResourceManager function](..\wdm\nf-wdm-tmrecoverresourcemanager.md) | The TmRecoverResourceManager routine tries to recover the transaction that is associated with each enlistment of a specified resource manager object. |
| [WRITE_REGISTER_BUFFER_UCHAR function](..\wdm\nf-wdm-write-register-buffer-uchar~r3.md) | The WRITE_REGISTER_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified register. |
| [IoWithinStackLimits function](..\wdm\nf-wdm-iowithinstacklimits.md) | The IoWithinStackLimits routine determines whether a region of memory is within the stack limit of the current thread. |
| [ClfsAddLogContainer function](..\wdm\nf-wdm-clfsaddlogcontainer.md) | The ClfsAddLogContainer routine adds a container to a CLFS log. |
| [KeSaveFloatingPointState function](..\wdm\nf-wdm-kesavefloatingpointstate~r3.md) | The KeSaveFloatingPointState routine saves the nonvolatile floating-point context so the caller can carry out floating-point operations. |
| [ExInterlockedCompareExchange64 function](..\wdm\nf-wdm-exinterlockedcompareexchange64.md) | The ExInterlockedCompareExchange64 routine compares one integer variable to another and, if they are equal, sets the first variable to a caller-supplied value. |
| [PoDeletePowerRequest function](..\wdm\nf-wdm-podeletepowerrequest.md) | The PoDeletePowerRequest routine deletes a power request object. |
| [IoWMIExecuteMethod function](..\wdm\nf-wdm-iowmiexecutemethod.md) | The IoWMIExecuteMethod routine runs a WMI class method on the specified WMI data block instance. |
| [KeGetCurrentThread function](..\wdm\nf-wdm-kegetcurrentthread~r1.md) | The KeGetCurrentThread routine identifies the current thread. |
| [IoAllocateDriverObjectExtension function](..\wdm\nf-wdm-ioallocatedriverobjectextension.md) | The IoAllocateDriverObjectExtension routine allocates a per-driver context area, called a driver object extension, and assigns a unique identifier to it. |
| [IoWMIDeviceObjectToProviderId function](..\wdm\nf-wdm-iowmideviceobjecttoproviderid~r1.md) | The IoWMIDeviceObjectToProviderId routine translates the specified device object into the corresponding WMI Provider ID. |
| [KeInsertByKeyDeviceQueue function](..\wdm\nf-wdm-keinsertbykeydevicequeue.md) | The KeInsertByKeyDeviceQueue routine acquires the spin lock for the specified DeviceQueue and queues an entry according to the specified sort-key value if the device queue is set to a busy state. |
| [IoSetCompletionRoutine function](..\wdm\nf-wdm-iosetcompletionroutine.md) | The IoSetCompletionRoutine routine registers an IoCompletion routine, which will be called when the next-lower-level driver has completed the requested operation for the given IRP. |
| [KeMemoryBarrier function](..\wdm\nf-wdm-kememorybarrier~r3.md) | The KeMemoryBarrier routine creates a barrier at its position in the code&#8212;across which the compiler and the processor cannot move any operations. |
| [ExInterlockedPopEntrySList function](..\wdm\nf-wdm-exinterlockedpopentryslist~r1.md) | The ExInterlockedPopEntrySList routine atomically removes the first entry from a sequenced singly linked list. |
| [TmCommitEnlistment function](..\wdm\nf-wdm-tmcommitenlistment.md) | The TmCommitEnlistment routine initiates the commit operation for a specified enlistment's transaction. |
| [ClfsMgmtRemovePolicy function](..\wdm\nf-wdm-clfsmgmtremovepolicy.md) | The ClfsMgmtRemovePolicy routine resets a log's CLFS_MGMT_POLICY structure to its default value. |
| [ExInterlockedInsertTailList function](..\wdm\nf-wdm-exinterlockedinserttaillist.md) | The ExInterlockedInsertTailList routine atomically inserts an entry at the end of a doubly linked list of LIST_ENTRY structures. |
| [WmiTraceMessage function](..\wdm\nf-wdm-wmitracemessage.md) | The WmiTraceMessage routine adds a message to the output log of a WPP software tracing session. |
| [WRITE_REGISTER_BUFFER_USHORT function](..\wdm\nf-wdm-write-register-buffer-ushort~r1.md) | The WRITE_REGISTER_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified register. |
| [IoAttachDevice function](..\wdm\nf-wdm-ioattachdevice.md) | The IoAttachDevice routine attaches the caller's device object to a named target device object, so that I/O requests bound for the target device are routed first to the caller. |
| [READ_PORT_BUFFER_ULONG function](..\wdm\nf-wdm-read-port-buffer-ulong~r2.md) | The READ_PORT_BUFFER_ULONG routine reads a number of ULONG values from the specified port address into a buffer. |
| [InterlockedDecrement function](..\wdm\nf-wdm-interlockeddecrement.md) | The InterlockedDecrement routine decrements a caller-supplied variable of type LONG as an atomic operation. |
| [ExCancelTimer function](..\wdm\nf-wdm-excanceltimer.md) | The ExCancelTimer routine cancels a timer that was set by a previous call to the ExSetTimer routine. |
| [IoOpenDeviceInterfaceRegistryKey function](..\wdm\nf-wdm-ioopendeviceinterfaceregistrykey.md) | The IoOpenDeviceInterfaceRegistryKey routine returns a handle to a registry key for storing information about a particular device interface instance. |
| [KeSetSystemGroupAffinityThread function](..\wdm\nf-wdm-kesetsystemgroupaffinitythread.md) | The KeSetSystemGroupAffinityThread routine changes the group number and affinity mask of the calling thread. |
| [ClfsMgmtSetLogFileSize function](..\wdm\nf-wdm-clfsmgmtsetlogfilesize.md) | The ClfsMgmtSetLogFileSize routine adds containers to a log or deletes containers from a log. |
| [PoRegisterDeviceForIdleDetection function](..\wdm\nf-wdm-poregisterdeviceforidledetection.md) | The PoRegisterDeviceForIdleDetection routine enables or cancels idle detection and sets idle time-out values for a device. |
| [ZwPrepareComplete function](..\wdm\nf-wdm-zwpreparecomplete.md) | The ZwPrepareComplete routine notifies KTM that the calling resource manager has finished preparing a transaction's data. |
| [ProbeForWrite function](..\wdm\nf-wdm-probeforwrite.md) | The ProbeForWrite routine checks that a user-mode buffer actually resides in the user-mode portion of the address space, is writable, and is correctly aligned. |
| [ObCloseHandle function](..\wdm\nf-wdm-obclosehandle.md) | The ObCloseHandle routine closes an object handle. |
| [ZwLoadDriver function](..\wdm\nf-wdm-zwloaddriver.md) | The ZwLoadDriver routine loads a driver into the system. |
| [ObGetObjectSecurity function](..\wdm\nf-wdm-obgetobjectsecurity.md) | The ObGetObjectSecurity routine gets the security descriptor for a given object. |
| [ExAllocatePoolWithTag function](..\wdm\nf-wdm-exallocatepoolwithtag~r1.md) | The ExAllocatePoolWithTag routine allocates pool memory of the specified type and returns a pointer to the allocated block. |
| [KeGetCurrentIrql function](..\wdm\nf-wdm-kegetcurrentirql~r3.md) | The KeGetCurrentIrql routine returns the current IRQL. |
| [ExRaiseStatus function](..\wdm\nf-wdm-exraisestatus.md) | The ExRaiseStatus routine is called by drivers that supply structured exception handlers to handle particular errors that occur while they are processing I/O requests. |
| [WRITE_PORT_UCHAR function](..\wdm\nf-wdm-write-port-uchar.md) | The WRITE_PORT_UCHAR routine writes a byte to the specified port address. |
| [ZwCreateEnlistment function](..\wdm\nf-wdm-zwcreateenlistment.md) | The ZwCreateEnlistment routine creates a new enlistment object for a transaction. |
| [WRITE_REGISTER_BUFFER_ULONG function](..\wdm\nf-wdm-write-register-buffer-ulong~r2.md) | The WRITE_REGISTER_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified register. |
| [READ_PORT_BUFFER_UCHAR function](..\wdm\nf-wdm-read-port-buffer-uchar.md) | The READ_PORT_BUFFER_UCHAR routine reads a number of bytes from the specified port address into a buffer. |
| [KeInitializeEvent function](..\wdm\nf-wdm-keinitializeevent.md) | The KeInitializeEvent routine initializes an event object as a synchronization (single waiter) or notification type event and sets it to a signaled or not-signaled state. |
| [WRITE_REGISTER_ULONG function](..\wdm\nf-wdm-write-register-ulong~r1.md) | The WRITE_REGISTER_ULONG routine writes a ULONG value to the specified address. |
| [KeGetProcessorNumberFromIndex function](..\wdm\nf-wdm-kegetprocessornumberfromindex.md) | The KeGetProcessorNumberFromIndex routine converts a systemwide processor index to a group number and a group-relative processor number. |
| [READ_REGISTER_ULONG function](..\wdm\nf-wdm-read-register-ulong~r1.md) | The READ_REGISTER_ULONG routine reads a ULONG value from the specified register address. |
| [IoCreateUnprotectedSymbolicLink function](..\wdm\nf-wdm-iocreateunprotectedsymboliclink.md) | The IoCreateUnprotectedSymbolicLink routine sets up an unprotected symbolic link between a device object name and a corresponding Win32-visible name. |
| [IoStartNextPacketByKey function](..\wdm\nf-wdm-iostartnextpacketbykey.md) | The IoStartNextPacketByKey routine dequeues the next I/O request packet from the specified device object's associated device queue according to a specified sort-key value and calls the driver's StartIo routine with that IRP. |
| [IoCheckLinkShareAccess function](..\wdm\nf-wdm-iochecklinkshareaccess.md) | The IoCheckLinkShareAccess routine is called by file system drivers (FSDs) or other highest-level drivers to check whether link shared access to a file object is permitted. |
| [KeRemoveQueueDpc function](..\wdm\nf-wdm-keremovequeuedpc.md) | The KeRemoveQueueDpc routine removes the specified DPC object from the system DPC queue. |
| [ObReleaseObjectSecurity function](..\wdm\nf-wdm-obreleaseobjectsecurity.md) | The ObReleaseObjectSecurity routine is the reciprocal to ObGetObjectSecurity. |
| [MmUnlockPages function](..\wdm\nf-wdm-mmunlockpages.md) | The MmUnlockPages routine unlocks the physical pages that are described by the specified memory descriptor list (MDL). |
| [PoFxQueryCurrentComponentPerfState function](..\wdm\nf-wdm-pofxquerycurrentcomponentperfstate.md) | The PoFxQueryCurrentComponentPerfState routine retrieves the active performance state in a component's performance state set. |
| [ExInterlockedFlushSList function](..\wdm\nf-wdm-exinterlockedflushslist.md) | The ExInterlockedFlushSList routine atomically removes all entries from a sequenced singly linked list. |
| [WRITE_PORT_USHORT function](..\wdm\nf-wdm-write-port-ushort~r2.md) | The WRITE_PORT_USHORT routine writes a USHORT value to the specified port address. |
| [ExInterlockedAddLargeInteger function](..\wdm\nf-wdm-exinterlockedaddlargeinteger.md) | The ExInterlockedAddLargeInteger routine adds a large integer value to the specified variable as an atomic operation. |
| [IoConnectInterruptEx function](..\wdm\nf-wdm-ioconnectinterruptex.md) | For more information, see the WdmlibIoConnectInterruptEx function.#define IoConnectInterruptEx WdmlibIoConnectInterruptEx |
| [ZwQueryInformationTransaction function](..\wdm\nf-wdm-zwqueryinformationtransaction.md) | The ZwQueryInformationTransaction routine retrieves information about a specified transaction. |
| [ZwEnumerateKey function](..\wdm\nf-wdm-zwenumeratekey.md) | The ZwEnumerateKey routine returns information about a subkey of an open registry key. |
| [PoFxSetComponentResidency function](..\wdm\nf-wdm-pofxsetcomponentresidency.md) | The PoFxSetComponentResidency routine sets the estimated time for how long a component is likely to remain idle after the component enters the idle condition. |
| [READ_PORT_UCHAR function](..\wdm\nf-wdm-read-port-uchar~r2.md) | The READ_PORT_UCHAR routine reads a byte from the specified port address. |
| [ZwQueryKey function](..\wdm\nf-wdm-zwquerykey.md) | The ZwQueryKey routine provides information about the class of a registry key, and the number and sizes of its subkeys. |
| [TmPrepareEnlistment function](..\wdm\nf-wdm-tmprepareenlistment.md) | The TmPrepareEnlistment routine initiates the prepare operation for a specified enlistment's transaction. |
| [KeBugCheckEx function](..\wdm\nf-wdm-kebugcheckex.md) | The KeBugCheckEx routine brings down the system in a controlled manner when the caller discovers an unrecoverable inconsistency that would corrupt the system if the caller continued to run. |
| [IoGetRemainingStackSize function](..\wdm\nf-wdm-iogetremainingstacksize.md) | The IoGetRemainingStackSize routine returns the current amount of available kernel-mode stack space. |
| [IoRemoveLinkShareAccess function](..\wdm\nf-wdm-ioremovelinkshareaccess.md) | The IoRemoveLinkShareAccess routine removes the access and link share-access information for a given open instance of a file object. |
| [IoIs32bitProcess function](..\wdm\nf-wdm-iois32bitprocess.md) | The IoIs32bitProcess routine checks whether the originator of the current I/O request is a 32-bit user-mode application. |
| [ExInitializeResourceLite function](..\wdm\nf-wdm-exinitializeresourcelite.md) | The ExInitializeResourceLite routine initializes a resource variable. |
| [IoGetAttachedDeviceReference function](..\wdm\nf-wdm-iogetattacheddevicereference.md) | The IoGetAttachedDeviceReference routine returns a pointer to the highest level device object in a driver stack and increments the reference count on that object. |
| [READ_REGISTER_BUFFER_USHORT function](..\wdm\nf-wdm-read-register-buffer-ushort~r1.md) | The READ_REGISTER_BUFFER_USHORT routine reads a number of USHORT values from the specified register address into a buffer. |
| [IoWriteErrorLogEntry function](..\wdm\nf-wdm-iowriteerrorlogentry.md) | The IoWriteErrorLogEntry routine queues a given error log packet to the system error logging thread. |
| [KeQueryDpcWatchdogInformation function](..\wdm\nf-wdm-kequerydpcwatchdoginformation.md) | The KeQueryDpcWatchdogInformation routine returns the deferred procedure call (DPC) watchdog timer values for the current processor. |
| [PoCallDriver function](..\wdm\nf-wdm-pocalldriver.md) | The PoCallDriver routine passes a power IRP to the next-lower driver in the device stack. (Windows Server 2003, Windows XP, and Windows 2000 only.). |
| [RtlAnsiStringToUnicodeString function](..\wdm\nf-wdm-rtlansistringtounicodestring.md) | RtlAnsiStringToUnicodeString converts the given ANSI source string into a Unicode string. |
| [ClfsLsnCreate function](..\wdm\nf-wdm-clfslsncreate.md) | The ClfsLsnCreate routine creates a log sequence number (LSN), given a container identifier, a block offset, and a record sequence number. |
| [ExGetFirmwareType function](..\wdm\nf-wdm-exgetfirmwaretype.md) | Returns the system firmware type. |
| [ExReleaseRundownProtectionEx function](..\wdm\nf-wdm-exreleaserundownprotectionex.md) | The ExReleaseRundownProtectionEx routine releases run-down protection that the caller previously acquired by calling the ExAcquireRundownProtectionEx routine. |
| [KeResetEvent function](..\wdm\nf-wdm-keresetevent.md) | The KeResetEvent routine resets a specified event object to a not-signaled state and returns the previous state of that event object. |
| [IoSetDeviceInterfacePropertyData function](..\wdm\nf-wdm-iosetdeviceinterfacepropertydata.md) | The IoSetDeviceInterfacePropertyData routine modifies the current value of a device interface property. |
| [MmUnmapIoSpace function](..\wdm\nf-wdm-mmunmapiospace.md) | The MmUnmapIoSpace routine unmaps a specified range of physical addresses previously mapped by MmMapIoSpace. |
| [RtlUTF8ToUnicodeN function](..\wdm\nf-wdm-rtlutf8tounicoden.md) | The RtlUTF8ToUnicodeN routine converts a UTF-8 string to a Unicode string. |
| [IoWMIRegistrationControl function](..\wdm\nf-wdm-iowmiregistrationcontrol.md) | The IoWMIRegistrationControl routine registers or unregisters the caller as a WMI data provider for a specified device object. |
| [RtlMoveMemory function](..\wdm\nf-wdm-rtlmovememory.md) | The RtlMoveMemory routine copies the contents of a source memory block to a destination memory block, and supports overlapping source and destination memory blocks. |
| [TmCommitComplete function](..\wdm\nf-wdm-tmcommitcomplete.md) | The TmCommitComplete routine notifies KTM that the calling resource manager has finished committing a transaction. |
| [IoGetAffinityInterrupt function](..\wdm\nf-wdm-iogetaffinityinterrupt.md) | For more information, see the WdmlibIoGetAffinityInterrupt function.#define IoGetAffinityInterrupt WdmlibIoGetAffinityInterrupt |
| [ExInterlockedInsertHeadList function](..\wdm\nf-wdm-exinterlockedinsertheadlist.md) | The ExInterlockedInsertHeadList routine atomically inserts an entry at the beginning of a doubly linked list of LIST_ENTRY structures. |
| [ClfsReadNextLogRecord function](..\wdm\nf-wdm-clfsreadnextlogrecord.md) | The ClfsReadNextLogRecord routine reads the next record in a sequence, relative to the current record in a read context. |
| [PoFxRegisterComponentPerfStates function](..\wdm\nf-wdm-pofxregistercomponentperfstates.md) | The PoFxRegisterComponentPerfStates routine registers a device component for performance state management by the power management framework (PoFx). |
| [ClfsLsnLess function](..\wdm\nf-wdm-clfslsnless.md) | The ClfsLsnLess routine determines whether one LSN is less than another LSN. The two LSNs must be from the same stream. |
| [KeInitializeSpinLock function](..\wdm\nf-wdm-keinitializespinlock.md) | The KeInitializeSpinLock routine initializes a variable of type KSPIN_LOCK. |
| [RtlFindClearBitsAndSet function](..\wdm\nf-wdm-rtlfindclearbitsandset.md) | The RtlFindClearBitsAndSet routine searches for a range of clear bits of a requested size within a bitmap and sets all bits in the range when it has been located. |
| [IoInitializeRemoveLock function](..\wdm\nf-wdm-ioinitializeremovelock.md) | The IoInitializeRemoveLock routine initializes a remove lock for a device object. |
| [KeWaitForSingleObject function](..\wdm\nf-wdm-kewaitforsingleobject.md) | The KeWaitForSingleObject routine puts the current thread into a wait state until the given dispatcher object is set to a signaled state or (optionally) until the wait times out. |
| [KeRestoreFloatingPointState function](..\wdm\nf-wdm-kerestorefloatingpointstate.md) | The KeRestoreFloatingPointState routine restores the nonvolatile floating-point context saved by the preceding call to KeSaveFloatingPointState. |
| [ZwCommitEnlistment function](..\wdm\nf-wdm-zwcommitenlistment.md) | The ZwCommitEnlistment routine initiates the commit operation for a specified enlistment's transaction. |
| [ClfsSetLogFileInformation function](..\wdm\nf-wdm-clfssetlogfileinformation.md) | The ClfsSetLogFileInformation routine sets metadata and state information for a specified stream and its underlying physical log. |
| [IoBuildSynchronousFsdRequest function](..\wdm\nf-wdm-iobuildsynchronousfsdrequest.md) | The IoBuildSynchronousFsdRequest routine allocates and sets up an IRP for a synchronously processed I/O request. |
| [ZwSetInformationFile function](..\wdm\nf-wdm-zwsetinformationfile.md) | The ZwSetInformationFile routine changes various kinds of information about a file object. |
| [IoGetDeviceInterfaceAlias function](..\wdm\nf-wdm-iogetdeviceinterfacealias.md) | The IoGetDeviceInterfaceAlias routine returns the alias device interface of the specified device interface instance, if the alias exists. |
| [ExInterlockedAddLargeStatistic function](..\wdm\nf-wdm-exinterlockedaddlargestatistic.md) | The ExInterlockedAddLargeStatistic routine performs an interlocked addition of a ULONG increment value to a LARGE_INTEGER variable. |
| [IoCheckShareAccessEx function](..\wdm\nf-wdm-iocheckshareaccessex.md) | The IoCheckShareAccessEx routine is called by file system drivers (FSDs) or other highest-level drivers to check whether shared access to a file object is permitted. |
| [IoRequestDpc function](..\wdm\nf-wdm-iorequestdpc.md) | The IoRequestDpc routine queues a driver-supplied DpcForIsr routine to complete interrupt-driven I/O processing at a lower IRQL. |
| [IoWMISuggestInstanceName function](..\wdm\nf-wdm-iowmisuggestinstancename.md) | The IoWMISuggestInstanceName routine is used to request that WMI suggest a base name which a driver can use to build WMI instance names for the device. |
| [READ_PORT_BUFFER_USHORT function](..\wdm\nf-wdm-read-port-buffer-ushort~r2.md) | The READ_PORT_BUFFER_USHORT routine reads a number of USHORT values from the specified port address into a buffer. |
| [IoMarkIrpPending function](..\wdm\nf-wdm-iomarkirppending.md) | The IoMarkIrpPending routine marks the specified IRP, indicating that a driver's dispatch routine subsequently returned STATUS_PENDING because further processing is required by other driver routines. |
| [ZwRollforwardTransactionManager function](..\wdm\nf-wdm-zwrollforwardtransactionmanager.md) | The ZwRollforwardTransactionManager routine initiates recovery operations for all of the in-progress transactions that are assigned to a specified transaction manager. |
| [IoReportInterruptActive function](..\wdm\nf-wdm-ioreportinterruptactive.md) | The IoReportInterruptActive routine informs the operating system that a registered interrupt service routine (ISR) is active and ready to handle interrupt requests. |
| [PoSetPowerState function](..\wdm\nf-wdm-posetpowerstate.md) | The PoSetPowerState routine notifies the system of a change in the device power state for a device. |
| [MmPageEntireDriver function](..\wdm\nf-wdm-mmpageentiredriver.md) | The MmPageEntireDriver routine causes all of a driver's code and data to be made pageable, overriding the attributes of the various sections that make up the driver's image. |
| [ExQueryTimerResolution function](..\wdm\nf-wdm-exquerytimerresolution.md) | The ExQueryTimerResolution routine reports the range of timer resolutions that are supported by the system clock. |
| [KeSetCoalescableTimer function](..\wdm\nf-wdm-kesetcoalescabletimer.md) | The KeSetCoalescableTimer routine sets the initial expiration time and period of a timer object and specifies how much delay can be tolerated in the expiration times. |
| [IoInvalidateDeviceRelations function](..\wdm\nf-wdm-ioinvalidatedevicerelations.md) | The IoInvalidateDeviceRelations routine notifies the PnP manager that the relations for a device (such as bus relations, ejection relations, removal relations, and the target device relation) have changed. |
| [READ_PORT_BUFFER_ULONG function](..\wdm\nf-wdm-read-port-buffer-ulong~r1.md) | The READ_PORT_BUFFER_ULONG routine reads a number of ULONG values from the specified port address into a buffer. |
| [ZwDeleteValueKey function](..\wdm\nf-wdm-zwdeletevaluekey.md) | The ZwDeleteValueKey routine deletes a value entry matching a name from an open key in the registry. If no such entry exists, an error is returned. |
| [RtlWriteRegistryValue function](..\wdm\nf-wdm-rtlwriteregistryvalue.md) | The RtlWriteRegistryValue routine writes caller-supplied data into the registry along the specified relative path at the given value name. |
| [ClfsGetIoStatistics function](..\wdm\nf-wdm-clfsgetiostatistics.md) | The ClfsGetIoStatistics routine returns I/O statistics for a specified CLFS log. |
| [ZwCreateTransaction function](..\wdm\nf-wdm-zwcreatetransaction.md) | The ZwCreateTransaction routine creates a transaction object. |
| [ExInterlockedAddUlong function](..\wdm\nf-wdm-exinterlockedaddulong.md) | The ExInterlockedAddUlong routine adds an unsigned long value to a given unsigned integer as an atomic operation. |
| [IoAllocateMdl function](..\wdm\nf-wdm-ioallocatemdl.md) | The IoAllocateMdl routine allocates a memory descriptor list (MDL) large enough to map a buffer, given the buffer's starting address and length. Optionally, this routine associates the MDL with an IRP. |
| [PoEndDeviceBusy function](..\wdm\nf-wdm-poenddevicebusy.md) | The PoEndDeviceBusy routine marks the end of a period of time in which the device is busy. |
| [ZwQueryFullAttributesFile function](..\wdm\nf-wdm-zwqueryfullattributesfile.md) | The ZwQueryFullAttributesFile routine supplies network open information for the specified file. |
| [KeQueryActiveProcessorCountEx function](..\wdm\nf-wdm-kequeryactiveprocessorcountex.md) | The KeQueryActiveProcessorCountEx routine returns the number of active logical processors in a specified group in a multiprocessor system or in the entire system. |
| [ZwUnloadDriver function](..\wdm\nf-wdm-zwunloaddriver.md) | The ZwUnloadDriver routine unloads a driver from the system. |
| [IoOpenDeviceRegistryKey function](..\wdm\nf-wdm-ioopendeviceregistrykey.md) | The IoOpenDeviceRegistryKey routine returns a handle to a device-specific or a driver-specific registry key for a particular device instance. |
| [PoFxActivateComponent function](..\wdm\nf-wdm-pofxactivatecomponent.md) | The PoFxActivateComponent routine increments the activation reference count on the specified component. |
| [ZwPrePrepareEnlistment function](..\wdm\nf-wdm-zwpreprepareenlistment.md) | The ZwPrePrepareEnlistment routine initiates the pre-prepare operation for a specified enlistment's transaction. |
| [RtlStringFromGUID function](..\wdm\nf-wdm-rtlstringfromguid.md) | The RtlStringFromGUID routine converts a given GUID from binary format into a Unicode string. |
| [KeGetCurrentProcessorNumberEx function](..\wdm\nf-wdm-kegetcurrentprocessornumberex.md) | The KeGetCurrentProcessorNumberEx routine gets the processor number of the logical processor that the caller is running on. |
| [RtlIntPtrToUnicodeString function](..\wdm\nf-wdm-rtlintptrtounicodestring.md) | The RtlIntPtrToUnicodeString routine converts a specified ULONG_PTR value to a Unicode string that represents the value in a specified base. |
| [ZwDeleteKey function](..\wdm\nf-wdm-zwdeletekey.md) | The ZwDeleteKey routine deletes an open key from the registry. |
| [KeQueryUnbiasedInterruptTime function](..\wdm\nf-wdm-kequeryunbiasedinterrupttime.md) | The KeQueryUnbiasedInterruptTime routine returns the current value of the system interrupt time count. |
| [RtlUshortByteSwap function](..\wdm\nf-wdm-rtlushortbyteswap.md) | The RtlUshortByteSwap routine reverses the ordering of the two bytes in a 16-bit unsigned integer value. |
| [RtlxUnicodeStringToAnsiSize function](..\wdm\nf-wdm-rtlxunicodestringtoansisize.md) | The RtlxUnicodeStringToAnsiSize routine returns the number of bytes required for a null-terminated ANSI string that is equivalent to a specified Unicode string. |
| [KeReleaseSpinLockFromDpcLevel function](..\wdm\nf-wdm-kereleasespinlockfromdpclevel.md) | The KeReleaseSpinLockFromDpcLevel routine releases an executive spin lock without changing the IRQL. |
| [MmMapIoSpace function](..\wdm\nf-wdm-mmmapiospace.md) | The MmMapIoSpace routine maps the given physical address range to nonpaged system space. |
| [KeReadStateEvent function](..\wdm\nf-wdm-kereadstateevent.md) | The KeReadStateEvent routine returns the current state, signaled or not-signaled, of an event object. |
| [IoWMIWriteEvent function](..\wdm\nf-wdm-iowmiwriteevent.md) | The IoWMIWriteEvent routine delivers a given event to the user-mode WMI components for notification. |
| [PoRequestPowerIrp function](..\wdm\nf-wdm-porequestpowerirp.md) | The PoRequestPowerIrp routine allocates a power IRP and sends it to the top driver in the device stack for the specified device. |
| [TmRollbackComplete function](..\wdm\nf-wdm-tmrollbackcomplete.md) | The TmRollbackComplete routine notifies KTM that the calling resource manager has finished rolling back a transaction's data. |
| [ClfsWriteRestartArea function](..\wdm\nf-wdm-clfswriterestartarea.md) | The ClfsWriteRestartArea routine atomically appends a new restart record to a CLFS stream, flushes the restart record to stable storage, and optionally updates the base LSN of the stream. |
| [RtlNumberOfSetBits function](..\wdm\nf-wdm-rtlnumberofsetbits.md) | The RtlNumberOfSetBits routine returns a count of the set bits in a given bitmap variable. |
| [RtlUpcaseUnicodeChar function](..\wdm\nf-wdm-rtlupcaseunicodechar.md) | The RtlUpcaseUnicodeChar routine converts the specified Unicode character to uppercase. |
| [ClfsLsnRecordSequence function](..\wdm\nf-wdm-clfslsnrecordsequence.md) | The ClfsLsnRecordSequence routine returns the record sequence number contained in a specified LSN. |
| [KeEnterGuardedRegion function](..\wdm\nf-wdm-keenterguardedregion.md) | The KeEnterGuardedRegion routine enters a guarded region, which disables all kernel-mode APC delivery to the current thread. |
| [ClfsScanLogContainers function](..\wdm\nf-wdm-clfsscanlogcontainers.md) | The ClfsScanLogContainers routine retrieves descriptive information for a sequence of containers that belong to a particular CLFS log. |
| [READ_REGISTER_ULONG function](..\wdm\nf-wdm-read-register-ulong~r3.md) | The READ_REGISTER_ULONG routine reads a ULONG value from the specified register address. |
| [IoInitializeTimer function](..\wdm\nf-wdm-ioinitializetimer.md) | The IoInitializeTimer routine sets up a driver-supplied IoTimer routine associated with a given device object. |
| [WRITE_PORT_BUFFER_ULONG function](..\wdm\nf-wdm-write-port-buffer-ulong~r3.md) | The WRITE_PORT_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified port address. |
| [KeAreApcsDisabled function](..\wdm\nf-wdm-keareapcsdisabled.md) | The KeAreApcsDisabled routine returns whether the calling thread is within a critical region or a guarded region, which disables normal kernel APC delivery. |
| [IoFreeErrorLogEntry function](..\wdm\nf-wdm-iofreeerrorlogentry.md) | The IoFreeErrorLogEntry routine frees an unused error log entry. |
| [InterlockedOr function](..\wdm\nf-wdm-interlockedor.md) | The InterlockedOr routine atomically computes a bitwise OR operation. |
| [IoUnregisterPlugPlayNotification function](..\wdm\nf-wdm-iounregisterplugplaynotification.md) | This routine is obsolete in Windows 7 and later versions of Windows. For more information, see the following Remarks section.The IoUnregisterPlugPlayNotification routine removes the registration of a driver's callback routine for a PnP event. |
| [FIELD_OFFSET function](..\wdm\nf-wdm-field-offset.md) | The FIELD_OFFSET macro returns the byte offset of a named field in a known structure type. |
| [ZwCreateDirectoryObject function](..\wdm\nf-wdm-zwcreatedirectoryobject.md) | The ZwCreateDirectoryObject routine creates or opens an object-directory object. |
| [WRITE_REGISTER_ULONG function](..\wdm\nf-wdm-write-register-ulong~r2.md) | The WRITE_REGISTER_ULONG routine writes a ULONG value to the specified address. |
| [WRITE_REGISTER_BUFFER_ULONG function](..\wdm\nf-wdm-write-register-buffer-ulong~r1.md) | The WRITE_REGISTER_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified register. |
| [ProbeForRead function](..\wdm\nf-wdm-probeforread~r1.md) | The ProbeForRead routine checks that a user-mode buffer actually resides in the user portion of the address space, and is correctly aligned. |
| [RtlCheckRegistryKey function](..\wdm\nf-wdm-rtlcheckregistrykey.md) | The RtlCheckRegistryKey routine checks for the existence of a given named key in the registry. |
| [RtlConvertLongToLargeInteger function](..\wdm\nf-wdm-rtlconvertlongtolargeinteger.md) | The RtlConvertLongToLargeInteger routine converts the input signed integer to a signed large integer. |
| [READ_PORT_BUFFER_UCHAR function](..\wdm\nf-wdm-read-port-buffer-uchar~r3.md) | The READ_PORT_BUFFER_UCHAR routine reads a number of bytes from the specified port address into a buffer. |
| [ZwWriteFile function](..\wdm\nf-wdm-zwwritefile.md) | The ZwWriteFile routine writes data to an open file. |
| [READ_REGISTER_ULONG function](..\wdm\nf-wdm-read-register-ulong.md) | The READ_REGISTER_ULONG routine reads a ULONG value from the specified register address. |
| [RtlFindMostSignificantBit function](..\wdm\nf-wdm-rtlfindmostsignificantbit.md) | The RtlFindMostSignificantBit routine returns the zero-based position of the most significant nonzero bit in its parameter. |
| [KeSetSystemAffinityThreadEx function](..\wdm\nf-wdm-kesetsystemaffinitythreadex.md) | The KeSetSystemAffinityThreadEx routine sets the system affinity of the current thread. |
| [ExSetResourceOwnerPointerEx function](..\wdm\nf-wdm-exsetresourceownerpointerex.md) | The ExSetResourceOwnerPointerEx routine transfers the ownership of an executive resource from the calling thread to an owner pointer, which is a system address that identifies the resource owner. |
| [READ_PORT_BUFFER_UCHAR function](..\wdm\nf-wdm-read-port-buffer-uchar~r1.md) | The READ_PORT_BUFFER_UCHAR routine reads a number of bytes from the specified port address into a buffer. |
| [ZwCreateTransactionManager function](..\wdm\nf-wdm-zwcreatetransactionmanager.md) | The ZwCreateTransactionManager routine creates a new transaction manager object. |
| [ClfsCloseLogFileObject function](..\wdm\nf-wdm-clfscloselogfileobject.md) | The ClfsCloseLogFileObject routine releases all references to a log file object. |
| [IoCreateDevice function](..\wdm\nf-wdm-iocreatedevice.md) | The IoCreateDevice routine creates a device object for use by a driver. |
| [WRITE_PORT_BUFFER_USHORT function](..\wdm\nf-wdm-write-port-buffer-ushort~r1.md) | The WRITE_PORT_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified port address. |
| [ZwOpenEvent function](..\wdm\nf-wdm-zwopenevent.md) | The ZwOpenEvent routine opens a handle to an existing named event object with the specified desired access. |
| [ZwQueryValueKey function](..\wdm\nf-wdm-zwqueryvaluekey.md) | The ZwQueryValueKey routine returns a value entry for a registry key. |
| [PoFxCompleteIdleState function](..\wdm\nf-wdm-pofxcompleteidlestate.md) | The PoFxCompleteIdleState routine informs the power management framework (PoFx) that the specified component has completed a pending change to an Fx state. |
| [RtlUlongByteSwap function](..\wdm\nf-wdm-rtlulongbyteswap~r1.md) | The RtlUlongByteSwap routine reverses the ordering of the four bytes in a 32-bit unsigned integer value. |
| [TmIsTransactionActive function](..\wdm\nf-wdm-tmistransactionactive.md) | The TmIsTransactionActive routine indicates whether a specified transaction is in its active state. |
| [KeSetSystemAffinityThread function](..\wdm\nf-wdm-kesetsystemaffinitythread.md) | The KeSetSystemAffinityThread routine sets the system affinity of the current thread. |
| [IoGetInitialStack function](..\wdm\nf-wdm-iogetinitialstack.md) | The IoGetInitialStack routine returns the base address of the current thread's stack. |
| [ExLocalTimeToSystemTime function](..\wdm\nf-wdm-exlocaltimetosystemtime.md) | The ExLocalTimeToSystemTime routine converts a system time value for the current time zone to an unbiased, GreenGMT value. |
| [WRITE_PORT_UCHAR function](..\wdm\nf-wdm-write-port-uchar~r1.md) | The WRITE_PORT_UCHAR routine writes a byte to the specified port address. |
| [TmRecoverTransactionManager function](..\wdm\nf-wdm-tmrecovertransactionmanager.md) | The TmRecoverTransactionManager routine reconstructs the state of the transaction manager object (including all transactions, enlistments, and resource managers) from the recovery information that is in the log stream. |
| [READ_REGISTER_USHORT function](..\wdm\nf-wdm-read-register-ushort~r3.md) | The READ_REGISTER_USHORT routine reads a USHORT value from the specified register address. |
| [WRITE_REGISTER_UCHAR function](..\wdm\nf-wdm-write-register-uchar~r2.md) | The WRITE_REGISTER_UCHAR routine writes a byte to the specified address. |
| [IoInitializeIrp function](..\wdm\nf-wdm-ioinitializeirp.md) | The IoInitializeIrp routine initializes a given IRP that was allocated by the caller. |
| [RtlFillMemory function](..\wdm\nf-wdm-rtlfillmemory.md) | The RtlFillMemory routine fills a block of memory with the specified fill value. |
| [IoReleaseRemoveLock function](..\wdm\nf-wdm-ioreleaseremovelock.md) | The IoReleaseRemoveLock routine releases a remove lock acquired with a previous call to IoAcquireRemoveLock. |
| [ObUnRegisterCallbacks function](..\wdm\nf-wdm-obunregistercallbacks.md) | The ObUnRegisterCallbacks routine unregisters a set of callback routines that were registered with the ObRegisterCallbacks routine. |
| [IoWMIOpenBlock function](..\wdm\nf-wdm-iowmiopenblock.md) | The IoWMIOpenBlock routine opens the WMI data block object for the specified WMI class. |
| [ZwRecoverResourceManager function](..\wdm\nf-wdm-zwrecoverresourcemanager.md) | The ZwRecoverResourceManager routine tries to recover the transaction that is associated with each enlistment of a specified resource manager object. |
| [WRITE_REGISTER_BUFFER_UCHAR function](..\wdm\nf-wdm-write-register-buffer-uchar~r1.md) | The WRITE_REGISTER_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified register. |
| [KeQueryGroupAffinity function](..\wdm\nf-wdm-kequerygroupaffinity.md) | The KeQueryGroupAffinity routine returns an affinity mask that identifies the active logical processors in a specified group in a multiprocessor system. |
| [ZwClose function](..\wdm\nf-wdm-zwclose.md) | The ZwClose routine closes an object handle. |
| [RtlSetDaclSecurityDescriptor function](..\wdm\nf-wdm-rtlsetdaclsecuritydescriptor.md) | The RtlSetDaclSecurityDescriptor routine sets the DACL information of an absolute-format security descriptor, or if there is already a DACL present in the security descriptor, it is superseded. |
| [InterlockedExchangePointer function](..\wdm\nf-wdm-interlockedexchangepointer.md) | The InterlockedExchangePointer routine performs an atomic operation that sets a pointer to a new value. |
| [InsertHeadList function](..\wdm\nf-wdm-insertheadlist~r1.md) | The InsertHeadList routine inserts an entry at the head of a doubly linked list of LIST_ENTRY structures. |
| [RtlxAnsiStringToUnicodeSize function](..\wdm\nf-wdm-rtlxansistringtounicodesize.md) | The RtlxAnsiStringToUnicodeSize routine returns the number of bytes that are required for a null-terminated Unicode string that is equivalent to a specified ANSI string. |
| [ClfsRemoveLogContainer function](..\wdm\nf-wdm-clfsremovelogcontainer.md) | The ClfsRemoveLogContainer routine removes a container from a CLFS log. |
| [KeQuerySystemTime function](..\wdm\nf-wdm-kequerysystemtime~r1.md) | The KeQuerySystemTime routine obtains the current system time. |
| [IoCsqInitialize function](..\wdm\nf-wdm-iocsqinitialize.md) | The IoCsqInitialize routine initializes the driver's cancel-safe IRP queue dispatch table. |
| [KeTryToAcquireGuardedMutex function](..\wdm\nf-wdm-ketrytoacquireguardedmutex.md) | The KeTryToAcquireGuardedMutex routine acquires a guarded mutex, if available. |
| [ClfsCreateLogFile function](..\wdm\nf-wdm-clfscreatelogfile.md) | The ClfsCreateLogFile routine creates or opens a CLFS stream. If necessary, ClfsCreateLogFile also creates the underlying physical log that holds the stream's records. |
| [RtlIoDecodeMemIoResource function](..\wdm\nf-wdm-rtliodecodememioresource.md) | The RtlIoDecodeMemIoResource routine provides the address information that is contained in an IO_RESOURCE_DESCRIPTOR structure that describes a range of memory or I/O port addresses. |
| [KeQueryAuxiliaryCounterFrequency function](..\wdm\nf-wdm-kequeryauxiliarycounterfrequency.md) | The KeQueryAuxiliaryCounterFrequency routine returns frequency of the auxiliary counter in units of Hz. |
| [KeQueryNodeActiveAffinity function](..\wdm\nf-wdm-kequerynodeactiveaffinity.md) | The KeQueryNodeActiveAffinity routine gets the current processor affinity of a specified node in a multiprocessor system that has a non-uniform memory access (NUMA) architecture. |
| [PsTerminateSystemThread function](..\wdm\nf-wdm-psterminatesystemthread.md) | The PsTerminateSystemThread routine terminates the current system thread. |
| [READ_REGISTER_BUFFER_UCHAR function](..\wdm\nf-wdm-read-register-buffer-uchar.md) | The READ_REGISTER_BUFFER_UCHAR routine reads a number of bytes from the specified register address into a buffer. |
| [ClfsAlignReservedLog function](..\wdm\nf-wdm-clfsalignreservedlog.md) | The ClfsAlignReservedLog routine calculates the size of the space that must be reserved for a specified set of records. The size calculation includes the space required for headers and the space required for sector alignment. |
| [READ_REGISTER_USHORT function](..\wdm\nf-wdm-read-register-ushort~r2.md) | The READ_REGISTER_USHORT routine reads a USHORT value from the specified register address. |
| [WRITE_REGISTER_BUFFER_ULONG function](..\wdm\nf-wdm-write-register-buffer-ulong~r3.md) | The WRITE_REGISTER_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified register. |
| [KeSetPriorityThread function](..\wdm\nf-wdm-kesetprioritythread.md) | The KeSetPriorityThread routine sets the run-time priority of a driver-created thread. |
| [IoConnectInterrupt function](..\wdm\nf-wdm-ioconnectinterrupt.md) | The IoConnectInterrupt routine registers a device driver's InterruptService routine (ISR), so that it will be called when a device interrupts on any of a specified set of processors. |
| [KeRegisterProcessorChangeCallback function](..\wdm\nf-wdm-keregisterprocessorchangecallback.md) | The KeRegisterProcessorChangeCallback routine registers a callback function with the operating system so that the operating system will notify the driver when a new processor is added to the hardware partition. |
| [ClfsGetContainerName function](..\wdm\nf-wdm-clfsgetcontainername.md) | The ClfsGetContainerName routine returns the path name of a specified container. |
| [InterlockedIncrement function](..\wdm\nf-wdm-interlockedincrement~r1.md) | The InterlockedIncrement routine increments a caller-supplied variable as an atomic operation. |
| [KeQueryInterruptTimePrecise function](..\wdm\nf-wdm-kequeryinterrupttimeprecise.md) | The KeQueryInterruptTimePrecise routine returns the current value of the system interrupt time count, with accuracy to within a microsecond. |
| [KeQueryTickCount function](..\wdm\nf-wdm-kequerytickcount.md) | The KeQueryTickCount routine maintains a count of the interval timer interrupts that have occurred since the system was booted. |
| [RtlCmDecodeMemIoResource function](..\wdm\nf-wdm-rtlcmdecodememioresource.md) | The RtlCmDecodeMemIoResource routine provides the starting address and length of a CM_PARTIAL_RESOURCE_DESCRIPTOR structure that describes a range of memory or I/O port addresses. |
| [RtlQueryRegistryValues function](..\wdm\nf-wdm-rtlqueryregistryvalues.md) | The RtlQueryRegistryValues routine allows the caller to query several values from the registry subtree with a single call. |
| [RtlInitUnicodeString function](..\wdm\nf-wdm-rtlinitunicodestring.md) | For more information, see the WdmlibRtlInitUnicodeStringEx function. |
| [MmProtectMdlSystemAddress function](..\wdm\nf-wdm-mmprotectmdlsystemaddress.md) | The MmProtectMdlSystemAddress routine sets the protection type for a memory address range. |
| [IoBuildDeviceIoControlRequest function](..\wdm\nf-wdm-iobuilddeviceiocontrolrequest.md) | The IoBuildDeviceIoControlRequest routine allocates and sets up an IRP for a synchronously processed device control request. |
| [WRITE_REGISTER_BUFFER_USHORT function](..\wdm\nf-wdm-write-register-buffer-ushort~r2.md) | The WRITE_REGISTER_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified register. |
| [ObRegisterCallbacks function](..\wdm\nf-wdm-obregistercallbacks.md) | The ObRegisterCallbacks routine registers a list of callback routines for thread, process, and desktop handle operations. |
| [ExRundownCompleted function](..\wdm\nf-wdm-exrundowncompleted.md) | The ExRundownCompleted routine updates the run-down status of a shared object to indicate that the run down of the object has completed. |
| [PoRegisterPowerSettingCallback function](..\wdm\nf-wdm-poregisterpowersettingcallback.md) | The PoRegisterPowerSettingCallback routine registers a power-setting callback routine to receive notifications of changes in the specified power setting. |
| [ClfsLsnBlockOffset function](..\wdm\nf-wdm-clfslsnblockoffset.md) | The ClfsLsnBlockOffset routine returns the sector-aligned block offset contained in a specified LSN. |
| [MmAllocatePagesForMdl function](..\wdm\nf-wdm-mmallocatepagesformdl.md) | The MmAllocatePagesForMdl routine allocates zero-filled, nonpaged, physical memory pages to an MDL. |
| [PoFxSetComponentWake function](..\wdm\nf-wdm-pofxsetcomponentwake.md) | The PoFxSetComponentWake routine indicates whether the driver arms the specified component to wake whenever the component enters the idle condition. |
| [IoSetCancelRoutine function](..\wdm\nf-wdm-iosetcancelroutine.md) | The IoSetCancelRoutine routine sets up a driver-supplied Cancel routine to be called if a given IRP is canceled. |
| [IoReportTargetDeviceChange function](..\wdm\nf-wdm-ioreporttargetdevicechange.md) | The IoReportTargetDeviceChange routine notifies the PnP manager that a custom event has occurred on a device. |
| [ExAllocatePoolWithQuota function](..\wdm\nf-wdm-exallocatepoolwithquota.md) | The ExAllocatePoolWithQuota routine is obsolete, and is exported only for existing driver binaries. Use ExAllocatePoolWithQuotaTag instead.ExAllocatePoolWithQuota allocates pool memory, charging quota against the current process. |
| [READ_REGISTER_BUFFER_UCHAR function](..\wdm\nf-wdm-read-register-buffer-uchar~r2.md) | The READ_REGISTER_BUFFER_UCHAR routine reads a number of bytes from the specified register address into a buffer. |
| [IoBuildPartialMdl function](..\wdm\nf-wdm-iobuildpartialmdl.md) | The IoBuildPartialMdl routine builds a new memory descriptor list (MDL) that represents part of a buffer that is described by an existing MDL. |
| [ExDeletePagedLookasideList function](..\wdm\nf-wdm-exdeletepagedlookasidelist.md) | The ExDeletePagedLookasideList routine destroys a paged lookaside list. |
| [ZwOpenKeyTransactedEx function](..\wdm\nf-wdm-zwopenkeytransactedex.md) | The ZwOpenKeyTransactedEx routine opens an existing registry key and associates the key with a transaction. |
| [READ_PORT_ULONG function](..\wdm\nf-wdm-read-port-ulong.md) | The READ_PORT_ULONG routine reads a ULONG value from the specified port address. |
| [ExAcquireResourceSharedLite function](..\wdm\nf-wdm-exacquireresourcesharedlite.md) | The ExAcquireResourceSharedLite routine acquires the given resource for shared access by the calling thread. |
| [KeFlushIoBuffers function](..\wdm\nf-wdm-keflushiobuffers~r2.md) | The KeFlushIoBuffers routine flushes the memory region described by an MDL from caches of all processors. |
| [ZwCommitComplete function](..\wdm\nf-wdm-zwcommitcomplete.md) | The ZwCommitComplete routine notifies KTM that the calling resource manager has finished committing a transaction's data. |
| [KeInitializeTimer function](..\wdm\nf-wdm-keinitializetimer.md) | The KeInitializeTimer routine initializes a timer object. |
| [InterlockedDecrement function](..\wdm\nf-wdm-interlockeddecrement~r1.md) | The InterlockedDecrement routine decrements a caller-supplied variable of type LONG as an atomic operation. |
| [TmEnableCallbacks function](..\wdm\nf-wdm-tmenablecallbacks.md) | The TmEnableCallbacks routine enables a callback routine that receives transaction notifications. |
| [ClfsSetArchiveTail function](..\wdm\nf-wdm-clfssetarchivetail.md) | The ClfsSetArchiveTail routine sets the archive tail of a CLFS log to a specified LSN. |
| [CmGetBoundTransaction function](..\wdm\nf-wdm-cmgetboundtransaction.md) | The CmGetBoundTransaction routine returns a pointer to the transaction object that represents the transaction, if any, that is associated with a specified registry key object. |
| [KeMemoryBarrier function](..\wdm\nf-wdm-kememorybarrier~r2.md) | The KeMemoryBarrier routine creates a barrier at its position in the code&#8212;across which the compiler and the processor cannot move any operations. |
| [KeGetCurrentThread function](..\wdm\nf-wdm-kegetcurrentthread.md) | The KeGetCurrentThread routine identifies the current thread. |
| [ClfsDeleteMarshallingArea function](..\wdm\nf-wdm-clfsdeletemarshallingarea.md) | The ClfsDeleteMarshallingArea routine deletes a marshalling area. |
| [InsertHeadList function](..\wdm\nf-wdm-insertheadlist.md) | The InsertHeadList routine inserts an entry at the head of a doubly linked list of LIST_ENTRY structures. |
| [KeGetProcessorIndexFromNumber function](..\wdm\nf-wdm-kegetprocessorindexfromnumber.md) | The KeGetProcessorIndexFromNumber routine converts a group number and a group-relative processor number to a systemwide processor index. |
| [ZwOpenTransactionManager function](..\wdm\nf-wdm-zwopentransactionmanager.md) | The ZwOpenTransactionManager routine obtains a handle to an existing transaction manager object. |
| [KeFlushIoBuffers function](..\wdm\nf-wdm-keflushiobuffers.md) | The KeFlushIoBuffers routine flushes the memory region described by an MDL from caches of all processors. |
| [RtlClearBit function](..\wdm\nf-wdm-rtlclearbit.md) | The RtlClearBit routine sets the specified bit in a bitmap to zero. |
| [ExSetTimer function](..\wdm\nf-wdm-exsettimer.md) | The ExSetTimer routine starts a timer operation and sets the timer to expire at the specified due time. |
| [RemoveTailList function](..\wdm\nf-wdm-removetaillist.md) | The RemoveTailList routine removes an entry from the end of a doubly linked list of LIST_ENTRY structures. |
| [CmRegisterCallback function](..\wdm\nf-wdm-cmregistercallback.md) | The CmRegisterCallback routine is obsolete for Windows Vista and later operating system versions. Use CmRegisterCallbackEx instead.The CmRegisterCallback routine registers a RegistryCallback routine. |
| [InterlockedOr function](..\wdm\nf-wdm-interlockedor~r1.md) | The InterlockedOr routine atomically computes a bitwise OR operation. |
| [ZwOpenKey function](..\wdm\nf-wdm-zwopenkey.md) | The ZwOpenKey routine opens an existing registry key. |
| [READ_REGISTER_UCHAR function](..\wdm\nf-wdm-read-register-uchar~r2.md) | The READ_REGISTER_UCHAR routine reads a byte from the specified register address. |
| [WRITE_PORT_ULONG function](..\wdm\nf-wdm-write-port-ulong~r2.md) | The WRITE_PORT_ULONG routine writes a ULONG value to the specified port address. |
| [MmFreeMappingAddress function](..\wdm\nf-wdm-mmfreemappingaddress.md) | The MmFreeMappingAddress routine frees a range of virtual memory reserved by the MmAllocateMappingAddress routine. |
| [ClfsFlushToLsn function](..\wdm\nf-wdm-clfsflushtolsn.md) | The ClfsFlushToLsn routine forces, to stable storage, all records that have an LSN less than or equal to a specified LSN. |
| [RtlEqualUnicodeString function](..\wdm\nf-wdm-rtlequalunicodestring.md) | The RtlEqualUnicodeString routine compares two Unicode strings to determine whether they are equal. |
| [MmQuerySystemSize function](..\wdm\nf-wdm-mmquerysystemsize.md) | The MmQuerySystemSize routine returns an estimate of the amount of memory in the system. |
| [KeInitializeDpc function](..\wdm\nf-wdm-keinitializedpc.md) | The KeInitializeDpc routine initializes a DPC object, and registers a CustomDpc routine for that object. |
| [KeGetCurrentIrql function](..\wdm\nf-wdm-kegetcurrentirql~r1.md) | The KeGetCurrentIrql routine returns the current IRQL. |
| [READ_PORT_ULONG function](..\wdm\nf-wdm-read-port-ulong~r1.md) | The READ_PORT_ULONG routine reads a ULONG value from the specified port address. |
| [ExFlushLookasideListEx function](..\wdm\nf-wdm-exflushlookasidelistex.md) | The ExFlushLookasideListEx routine flushes all entries from the specified lookaside list and frees the allocated storage for each entry. |
| [IoInvalidateDeviceState function](..\wdm\nf-wdm-ioinvalidatedevicestate.md) | The IoInvalidateDeviceState routine notifies the PnP manager that some aspect of the PnP state of a device has changed. |
| [KeConvertPerformanceCounterToAuxiliaryCounter function](..\wdm\nf-wdm-keconvertperformancecountertoauxiliarycounter.md) | The KeConvertPerformanceCounterToAuxiliaryCounter routine converts the specified performance counter value into an auxiliary counter value. |
| [WRITE_REGISTER_BUFFER_ULONG function](..\wdm\nf-wdm-write-register-buffer-ulong.md) | The WRITE_REGISTER_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified register. |
| [PoFxIssueComponentPerfStateChange function](..\wdm\nf-wdm-pofxissuecomponentperfstatechange.md) | The PoFxIssueComponentPerfStateChange routine submits a request to place a device component in a particular performance state. |
| [KeSaveExtendedProcessorState function](..\wdm\nf-wdm-kesaveextendedprocessorstate.md) | The KeSaveExtendedProcessorState routine saves extended processor state information. |
| [RtlPrefetchMemoryNonTemporal function](..\wdm\nf-wdm-rtlprefetchmemorynontemporal.md) | The RtlPrefetchMemoryNonTemporal routine provides a hint to the processor that a buffer should be temporarily moved into the processor cache. |
| [KeReadStateMutex function](..\wdm\nf-wdm-kereadstatemutex.md) | The KeReadStateMutex routine returns the current state, signaled or not-signaled, of the specified mutex object. |
| [PoQueryWatchdogTime function](..\wdm\nf-wdm-poquerywatchdogtime.md) | The PoQueryWatchdogTime routine indicates whether the power manager has enabled a watchdog time-out counter for any power IRP that is currently assigned to the device stack. |
| [CmRegisterCallbackEx function](..\wdm\nf-wdm-cmregistercallbackex.md) | The CmRegisterCallbackEx routine registers a RegistryCallback routine. |
| [RtlUlonglongByteSwap function](..\wdm\nf-wdm-rtlulonglongbyteswap~r1.md) | The RtlUlonglongByteSwap routine reverses the ordering of the eight bytes in a 64-bit unsigned integer value. |
| [RtlCheckBit function](..\wdm\nf-wdm-rtlcheckbit~r1.md) | The RtlCheckBit routine determines whether a particular bit in a given bitmap variable is clear or set. |
| [IoGetDriverObjectExtension function](..\wdm\nf-wdm-iogetdriverobjectextension.md) | The IoGetDriverObjectExtension routine retrieves a previously allocated per-driver context area. |
| [RtlAreBitsClear function](..\wdm\nf-wdm-rtlarebitsclear.md) | The RtlAreBitsClear routine determines whether a given range of bits within a bitmap variable is clear. |
| [IoGetDeviceNumaNode function](..\wdm\nf-wdm-iogetdevicenumanode.md) | The IoGetDeviceNumaNode routine gets the node number of a device. |
| [PushEntryList function](..\wdm\nf-wdm-pushentrylist.md) | The PushEntryList routine inserts an entry at the beginning of a singly linked list of SINGLE_LIST_ENTRY structures. |
| [ExAllocateFromLookasideListEx function](..\wdm\nf-wdm-exallocatefromlookasidelistex.md) | The ExAllocateFromLookasideListEx routine removes the first entry from the specified lookaside list, or, if the list is empty, dynamically allocates the storage for a new entry. |
| [MmGetSystemRoutineAddress function](..\wdm\nf-wdm-mmgetsystemroutineaddress~r1.md) | The MmGetSystemRoutineAddress routine returns a pointer to a function specified by SystemRoutineName. |
| [ClfsAddLogContainerSet function](..\wdm\nf-wdm-clfsaddlogcontainerset.md) | The ClfsAddLogContainerSet routine atomically adds a set of containers to a CLFS log. |
| [MmAllocatePagesForMdlEx function](..\wdm\nf-wdm-mmallocatepagesformdlex.md) | The MmAllocatePagesForMdlEx routine allocates nonpaged, physical memory pages to an MDL. |
| [KeSetTimer function](..\wdm\nf-wdm-kesettimer.md) | The KeSetTimer routine sets the absolute or relative interval at which a timer object is to be set to a signaled state and, optionally, supplies a CustomTimerDpc routine to be executed when that interval expires. |
| [RtlAppendUnicodeStringToString function](..\wdm\nf-wdm-rtlappendunicodestringtostring.md) | The RtlAppendUnicodeStringToString routine concatenates two Unicode strings. |
| [ZwGetNotificationResourceManager function](..\wdm\nf-wdm-zwgetnotificationresourcemanager.md) | The ZwGetNotificationResourceManager routine retrieves the next transaction notification from a specified resource manager's notification queue. |
| [PoFxIdleComponent function](..\wdm\nf-wdm-pofxidlecomponent.md) | The PoFxIdleComponent routine decrements the activation reference count on the specified component. |
| [IoCsqInsertIrp function](..\wdm\nf-wdm-iocsqinsertirp.md) | The IoCsqInsertIrp routine inserts an IRP in the driver's cancel-safe IRP queue. |
| [IoCsqRemoveNextIrp function](..\wdm\nf-wdm-iocsqremovenextirp.md) | The IoCsqRemoveNextIrp routine removes the next matching IRP in the queue. |
| [ExInterlockedPopEntryList function](..\wdm\nf-wdm-exinterlockedpopentrylist.md) | The ExInterlockedPopEntryList routine atomically removes an entry from the beginning of a singly linked list of SINGLE_LIST_ENTRY structures. |
| [KeInitializeCrashDumpHeader function](..\wdm\nf-wdm-keinitializecrashdumpheader.md) | The KeInitializeCrashDumpHeader routine supplies the header information the system requires for a crash dump file. |
| [ZwRollbackComplete function](..\wdm\nf-wdm-zwrollbackcomplete.md) | The ZwRollbackComplete routine notifies KTM that the calling resource manager has finished rolling back a transaction's data. |
| [PoFxIssueComponentPerfStateChangeMultiple function](..\wdm\nf-wdm-pofxissuecomponentperfstatechangemultiple.md) | The PoFxIssueComponentPerfStateChangeMultiple routine submits a request to change the performance states in multiple performance state sets simultaneously for a device component. |
| [READ_REGISTER_BUFFER_USHORT function](..\wdm\nf-wdm-read-register-buffer-ushort.md) | The READ_REGISTER_BUFFER_USHORT routine reads a number of USHORT values from the specified register address into a buffer. |
| [WRITE_PORT_BUFFER_USHORT function](..\wdm\nf-wdm-write-port-buffer-ushort~r2.md) | The WRITE_PORT_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified port address. |
| [InterlockedExchangeAdd function](..\wdm\nf-wdm-interlockedexchangeadd.md) | The InterlockedExchangeAdd routine adds a value to a given integer as an atomic operation and returns the original value of the given integer. |
| [WRITE_PORT_BUFFER_ULONG function](..\wdm\nf-wdm-write-port-buffer-ulong~r1.md) | The WRITE_PORT_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified port address. |
| [InterlockedXor function](..\wdm\nf-wdm-interlockedxor~r1.md) | The InterlockedOr routine atomically computes a bitwise exclusive OR operation. |
| [ExDeleteNPagedLookasideList function](..\wdm\nf-wdm-exdeletenpagedlookasidelist.md) | The ExDeleteNPagedLookasideList routine destroys a nonpaged lookaside list. |
| [KeAreAllApcsDisabled function](..\wdm\nf-wdm-keareallapcsdisabled.md) | The KeAreAllApcsDisabled routine indicates whether the calling thread is inside a guarded region or running at IRQL &gt;= APC_LEVEL, which disables all APC delivery. |
| [ZwCreateSection function](..\wdm\nf-wdm-zwcreatesection.md) | The ZwCreateSection routine creates a section object. |
| [RemoveTailList function](..\wdm\nf-wdm-removetaillist~r1.md) | The RemoveTailList routine removes an entry from the end of a doubly linked list of LIST_ENTRY structures. |
| [READ_REGISTER_UCHAR function](..\wdm\nf-wdm-read-register-uchar~r1.md) | The READ_REGISTER_UCHAR routine reads a byte from the specified register address. |
| [ExSetResourceOwnerPointer function](..\wdm\nf-wdm-exsetresourceownerpointer.md) | The ExSetResourceOwnerPointer routine sets the owner thread pointer for an executive resource. |
| [KeInsertDeviceQueue function](..\wdm\nf-wdm-keinsertdevicequeue.md) | The KeInsertDeviceQueue routine acquires the spin lock for the specified device queue object and, if the device queue is set to a busy state, queues the specified entry. |
| [RtlTestBit function](..\wdm\nf-wdm-rtltestbit.md) | The RtlTestBit routine returns the value of a bit in a bitmap. |
| [IoReleaseRemoveLockAndWait function](..\wdm\nf-wdm-ioreleaseremovelockandwait.md) | The IoReleaseRemoveLockAndWait routine releases a remove lock that the driver acquired in a previous call to IoAcquireRemoveLock, and waits until all acquisitions of the lock have been released. |
| [IoInitializeDpcRequest function](..\wdm\nf-wdm-ioinitializedpcrequest.md) | The IoInitializeDpcRequest routine registers a driver-supplied DpcForIsr routine. |
| [WRITE_PORT_ULONG function](..\wdm\nf-wdm-write-port-ulong~r1.md) | The WRITE_PORT_ULONG routine writes a ULONG value to the specified port address. |
| [MmMapMdl function](..\wdm\nf-wdm-mmmapmdl.md) | This function maps physical pages described by a memory descriptor list (MDL) into the system virtual address space. |
| [RtlInitStringEx function](..\wdm\nf-wdm-rtlinitstringex.md) | The RtlInitStringEx routine initializes a counted string of 8-bit characters. |
| [READ_REGISTER_BUFFER_USHORT function](..\wdm\nf-wdm-read-register-buffer-ushort~r2.md) | The READ_REGISTER_BUFFER_USHORT routine reads a number of USHORT values from the specified register address into a buffer. |
| [IoRegisterShutdownNotification function](..\wdm\nf-wdm-ioregistershutdownnotification.md) | The IoRegisterShutdownNotification routine registers the driver to receive an IRP_MJ_SHUTDOWN IRP when the system is shut down. |
| [RtlFindLongestRunClear function](..\wdm\nf-wdm-rtlfindlongestrunclear.md) | The RtlFindLongestRunClear routine searches for the largest contiguous range of clear bits within a given bitmap. |
| [KeSynchronizeExecution function](..\wdm\nf-wdm-kesynchronizeexecution.md) | The KeSynchronizeExecution routine synchronizes the execution of the specified routine with the interrupt service routine (ISR) that is assigned to a set of one or more interrupt objects. |
| [MmMapLockedPagesSpecifyCache function](..\wdm\nf-wdm-mmmaplockedpagesspecifycache.md) | The MmMapLockedPagesSpecifyCache routine maps the physical pages that are described by an MDL to a virtual address, and enables the caller to specify the cache attribute that is used to create the mapping. |
| [KeInitializeGuardedMutex function](..\wdm\nf-wdm-keinitializeguardedmutex.md) | The KeInitializeGuardedMutex routine initializes a guarded mutex. |
| [ZwUnmapViewOfSection function](..\wdm\nf-wdm-zwunmapviewofsection.md) | The ZwUnmapViewOfSection routine unmaps a view of a section from the virtual address space of a subject process. |
| [IoWMIQuerySingleInstance function](..\wdm\nf-wdm-iowmiquerysingleinstance.md) | The IoWMIQuerySingleInstance routine returns the specified instance of a WMI data block. |
| [KeMemoryBarrier function](..\wdm\nf-wdm-kememorybarrier~r1.md) | The KeMemoryBarrier routine creates a barrier at its position in the code&#8212;across which the compiler and the processor cannot move any operations. |
| [KeQueryLogicalProcessorRelationship function](..\wdm\nf-wdm-kequerylogicalprocessorrelationship.md) | The KeQueryLogicalProcessorRelationship routine gets information about the relationships of one or more processors to the other processors in a multiprocessor system. |
| [ExFreePoolWithTag function](..\wdm\nf-wdm-exfreepoolwithtag.md) | The ExFreePoolWithTag routine deallocates a block of pool memory allocated with the specified tag. |
| [READ_PORT_BUFFER_USHORT function](..\wdm\nf-wdm-read-port-buffer-ushort~r1.md) | The READ_PORT_BUFFER_USHORT routine reads a number of USHORT values from the specified port address into a buffer. |
| [ExAcquireResourceExclusiveLite function](..\wdm\nf-wdm-exacquireresourceexclusivelite.md) | The ExAcquireResourceExclusiveLite routine acquires the given resource for exclusive access by the calling thread. |
| [ZwSetInformationTransaction function](..\wdm\nf-wdm-zwsetinformationtransaction.md) | The ZwSetInformationTransaction routine sets information for a specified transaction. |
| [ExFreePool function](..\wdm\nf-wdm-exfreepool.md) | The ExFreePool routine deallocates a block of pool memory. |
| [ZwRecoverEnlistment function](..\wdm\nf-wdm-zwrecoverenlistment.md) | The ZwRecoverEnlistment routine initiates a recovery operation for the transaction that is associated with a specified enlistment. |
| [ExNotifyCallback function](..\wdm\nf-wdm-exnotifycallback.md) | The ExNotifyCallback routine causes all callback routines registered for the given object to be called. |
| [RtlValidSecurityDescriptor function](..\wdm\nf-wdm-rtlvalidsecuritydescriptor.md) | The RtlValidSecurityDescriptor routine checks a given security descriptor's validity. |
| [ExWaitForRundownProtectionRelease function](..\wdm\nf-wdm-exwaitforrundownprotectionrelease.md) | The ExWaitForRundownProtectionRelease routine waits until all drivers that have already been granted run-down protection complete their accesses of the shared object. |
| [RtlNumberOfClearBits function](..\wdm\nf-wdm-rtlnumberofclearbits.md) | The RtlNumberOfClearBits routine returns a count of the clear bits in a given bitmap variable. |
| [WRITE_PORT_BUFFER_UCHAR function](..\wdm\nf-wdm-write-port-buffer-uchar~r1.md) | The WRITE_PORT_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified port. |
| [IoFreeMdl function](..\wdm\nf-wdm-iofreemdl.md) | The IoFreeMdl routine releases a caller-allocated memory descriptor list (MDL). |
| [ClfsAllocReservedLog function](..\wdm\nf-wdm-clfsallocreservedlog.md) | The ClfsAllocReservedLog routine reserves space in a marshalling area for a set of records. |
| [ExInterlockedPopEntrySList function](..\wdm\nf-wdm-exinterlockedpopentryslist~r2.md) | The ExInterlockedPopEntrySList routine atomically removes the first entry from a sequenced singly linked list. |
| [KeFlushIoBuffers function](..\wdm\nf-wdm-keflushiobuffers~r4.md) | The KeFlushIoBuffers routine flushes the memory region described by an MDL from caches of all processors. |
| [KeRestoreFloatingPointState function](..\wdm\nf-wdm-kerestorefloatingpointstate~r3.md) | The KeRestoreFloatingPointState routine restores the nonvolatile floating-point context saved by the preceding call to KeSaveFloatingPointState. |
| [IoGetRelatedDeviceObject function](..\wdm\nf-wdm-iogetrelateddeviceobject.md) | Given a file object, the IoGetRelatedDeviceObject routine returns a pointer to the corresponding device object. |
| [ExUnregisterCallback function](..\wdm\nf-wdm-exunregistercallback.md) | The ExUnregisterCallback routine removes a callback routine previously registered with a callback object from the list of routines to be called during the notification process. |
| [KeFlushIoBuffers function](..\wdm\nf-wdm-keflushiobuffers~r1.md) | The KeFlushIoBuffers routine flushes the memory region described by an MDL from caches of all processors. |
| [ExReinitializeResourceLite function](..\wdm\nf-wdm-exreinitializeresourcelite.md) | The ExReinitializeResourceLite routine reinitializes an existing resource variable. |
| [KeFlushQueuedDpcs function](..\wdm\nf-wdm-keflushqueueddpcs.md) | The KeFlushQueuedDpcs routine returns after all queued DPCs on all processors have executed. |
| [RtlFreeAnsiString function](..\wdm\nf-wdm-rtlfreeansistring.md) | The RtlFreeAnsiString routine releases storage that was allocated by RtlUnicodeStringToAnsiString. |
| [AppendTailList function](..\wdm\nf-wdm-appendtaillist~r1.md) | The AppendTailList routine appends a doubly linked list of LIST_ENTRY structures to the tail of another doubly linked list of LIST_ENTRY structures. |
| [KeSaveFloatingPointState function](..\wdm\nf-wdm-kesavefloatingpointstate~r2.md) | The KeSaveFloatingPointState routine saves the nonvolatile floating-point context so the caller can carry out floating-point operations. |
| [RtlInt64ToUnicodeString function](..\wdm\nf-wdm-rtlint64tounicodestring.md) | The RtlInt64ToUnicodeString routine converts a specified unsigned 64-bit integer value to a Unicode string that represents the value in a specified base. |
| [MmBuildMdlForNonPagedPool function](..\wdm\nf-wdm-mmbuildmdlfornonpagedpool.md) | The MmBuildMdlForNonPagedPool routine receives an MDL that specifies a nonpaged virtual memory buffer, and updates it to describe the underlying physical pages. |
| [KeQuerySystemTime function](..\wdm\nf-wdm-kequerysystemtime.md) | The KeQuerySystemTime routine obtains the current system time. |
| [PoSetSystemState function](..\wdm\nf-wdm-posetsystemstate.md) | Drivers call the PoSetSystemState routine to indicate that the system is active. |
| [RtlCreateSecurityDescriptor function](..\wdm\nf-wdm-rtlcreatesecuritydescriptor.md) | The RtlCreateSecurityDescriptor routine initializes a new absolute-format security descriptor. On return, the security descriptor is initialized with no system ACL, no discretionary ACL, no owner, no primary group, and all control flags set to zero. |
| [RtlInitAnsiString function](..\wdm\nf-wdm-rtlinitansistring.md) | The RtlInitAnsiString routine initializes a counted string of ANSI characters. |
| [MmGetSystemRoutineAddress function](..\wdm\nf-wdm-mmgetsystemroutineaddress.md) | The MmGetSystemRoutineAddress routine returns a pointer to a function specified by SystemRoutineName. |
| [IoQueueWorkItem function](..\wdm\nf-wdm-ioqueueworkitem.md) | The IoQueueWorkItem routine associates a WorkItem routine with a work item, and it inserts the work item into a queue for later processing by a system worker thread. |
| [ExRegisterCallback function](..\wdm\nf-wdm-exregistercallback.md) | The ExRegisterCallback routine registers a given callback routine with a given callback object. |
| [WRITE_PORT_BUFFER_UCHAR function](..\wdm\nf-wdm-write-port-buffer-uchar~r3.md) | The WRITE_PORT_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified port. |
| [READ_REGISTER_UCHAR function](..\wdm\nf-wdm-read-register-uchar.md) | The READ_REGISTER_UCHAR routine reads a byte from the specified register address. |
| [ClfsMgmtInstallPolicy function](..\wdm\nf-wdm-clfsmgmtinstallpolicy.md) | The ClfsMgmtInstallPolicy routine adds a CLFS_MGMT_POLICY structure to a physical log. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [IO_ALLOCATION_ACTION enumeration](..\wdm\ne-wdm--io-allocation-action.md) | The IO_ALLOCATION_ACTION enumerated type is used to specify return values for AdapterControl and ControllerControl routines. |
| [IO_SESSION_EVENT enumeration](..\wdm\ne-wdm--io-session-event.md) | The IO_SESSION_EVENT enumeration indicates the type of session event for which a driver is receiving notification. |
| [IO_CONTAINER_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--io-container-information-class.md) | The IO_CONTAINER_INFORMATION_CLASS enumeration contains constants that indicate the classes of system information that a kernel-mode driver can request. |
| [INTERFACE_TYPE enumeration](..\wdm\ne-wdm--interface-type.md) | The INTERFACE_TYPE enumeration indicates the bus type. |
| [KINTERRUPT_MODE enumeration](..\wdm\ne-wdm--kinterrupt-mode.md) | The KINTERRUPT_MODE enumeration type indicates whether an interrupt is level-triggered or edge-triggered. |
| [POWER_REQUEST_TYPE enumeration](..\wdm\ne-wdm--power-request-type.md) | The POWER_REQUEST_TYPE enumeration indicates the power request type. |
| [PO_FX_PERF_STATE_TYPE enumeration](..\wdm\ne-wdm--po-fx-perf-state-type.md) | The PO_FX_PERF_STATE_TYPE enumeration contains values that describe the type of performance states in a PO_FX_COMPONENT_PERF_SET. |
| [CLFS_CONTEXT_MODE enumeration](..\wdm\ne-wdm--clfs-context-mode.md) | The CLFS_CONTEXT_MODE enumeration indicates the type of sequence that the Common Log File System (CLFS) driver follows when it reads a set of records from a stream. |
| [RESOURCEMANAGER_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--resourcemanager-information-class.md) | The RESOURCEMANAGER_INFORMATION_CLASS enumeration identifies the type of information that the ZwQueryInformationResourceManager routine can retrieve for a resource manager object. |
| [D3COLD_LAST_TRANSITION_STATUS enumeration](..\wdm\ne-wdm--d3cold-last-transition-status.md) | The D3COLD_LAST_TRANSITION_STATUS enumeration indicates whether the most recent transition to the D3hot device power state was followed by a transition to the D3cold device power state. |
| [PO_FX_PERF_STATE_UNIT enumeration](..\wdm\ne-wdm--po-fx-perf-state-unit.md) | The PO_FX_PERF_STATE_UNIT enumeration contains values that describe the type of unit that is controlled by the performance states in a PO_FX_COMPONENT_PERF_SET. |
| [KBUGCHECK_DUMP_IO_TYPE enumeration](..\wdm\ne-wdm--kbugcheck-dump-io-type.md) | The KBUGCHECK_DUMP_IO_TYPE enumeration type identifies the type of a section of data within a crash dump file. |
| [TRANSACTIONMANAGER_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--transactionmanager-information-class.md) | The TRANSACTIONMANAGER_INFORMATION_CLASS enumeration specifies the type of information that the ZwQueryInformationTransactionManager routine can retrieve for a transaction manager object. |
| [KEY_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--key-information-class.md) | The KEY_INFORMATION_CLASS enumeration type represents the type of information to supply about a registry key. |
| [DMA_COMPLETION_STATUS enumeration](..\wdm\ne-wdm-dma-completion-status.md) | The DMA_COMPLETION_STATUS enumeration describes the completion status of a DMA transfer. |
| [TRACE_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--trace-information-class.md) | The TRACE_INFORMATION_CLASS enumeration type is used to indicate types of information associated with a WMI event tracing session. |
| [BOUND_CALLBACK_STATUS enumeration](..\wdm\ne-wdm--bound-callback-status.md) | The BOUND_CALLBACK_STATUS enumeration indicates how a user-mode bounds exception was processed by the BoundCallback function. |
| [KTMOBJECT_TYPE enumeration](..\wdm\ne-wdm--ktmobject-type.md) | The KTMOBJECT_TYPE enumeration identifies the types of objects that KTM supports. |
| [IO_CONTAINER_NOTIFICATION_CLASS enumeration](..\wdm\ne-wdm--io-container-notification-class.md) | The IO_CONTAINER_NOTIFICATION_CLASS enumeration contains constants that indicate the classes of events for which a kernel-mode driver can register to receive notifications. |
| [IO_PAGING_PRIORITY enumeration](..\wdm\ne-wdm--io-paging-priority.md) | The IO_PAGING_PRIORITY enumeration describes the priority value for a paging I/O IRP. |
| [DEVICE_REMOVAL_POLICY enumeration](..\wdm\ne-wdm--device-removal-policy.md) | The DEVICE_REMOVAL_POLICY enumeration describes a device's removal policy. |
| [MEMORY_CACHING_TYPE enumeration](..\wdm\ne-wdm--memory-caching-type.md) | The MEMORY_CACHING_TYPE enumeration type specifies the permitted caching behavior when allocating or mapping memory. |
| [IO_SESSION_STATE enumeration](..\wdm\ne-wdm--io-session-state.md) | The IO_SESSION_STATE enumeration contains constants that indicate the current state of a user session. |
| [SYSTEM_POWER_STATE enumeration](..\wdm\ne-wdm--system-power-state.md) | The SYSTEM_POWER_STATE enumeration type is used to indicate a system power state. |
| [CLFS_MGMT_POLICY_TYPE enumeration](..\wdm\ne-wdm--clfs-mgmt-policy-type.md) | The CLFS_MGMT_POLICY_TYPE enumeration type identifies the type of a CLFS management policy. |
| [KBUGCHECK_CALLBACK_REASON enumeration](..\wdm\ne-wdm--kbugcheck-callback-reason.md) | The KBUGCHECK_CALLBACK_REASON enumeration type specifies the situations in which a bug-check callback executes. |
| [POOL_TYPE enumeration](..\wdm\ne-wdm--pool-type.md) | The POOL_TYPE enumeration type specifies the type of system memory to allocate. |
| [KEY_VALUE_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--key-value-information-class.md) | The KEY_VALUE_INFORMATION_CLASS enumeration type specifies the type of information to supply about the value of a registry key. |
| [POWER_INFORMATION_LEVEL enumeration](..\wdm\ne-wdm-power-information-level.md) | Indicates power level information. |
| [KEY_SET_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--key-set-information-class.md) | The KEY_SET_INFORMATION_CLASS enumeration type represents the type of information to set for a registry key. |
| [TRANSACTION_STATE enumeration](..\wdm\ne-wdm--transaction-state.md) | The TRANSACTION_STATE enumeration defines the states that KTM can assign to a transaction. |
| [DEVICE_INSTALL_STATE enumeration](..\wdm\ne-wdm--device-install-state.md) | The DEVICE_INSTALL_STATE enumeration describes a device's installation state. |
| [ENLISTMENT_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--enlistment-information-class.md) | The ENLISTMENT_INFORMATION_CLASS enumeration identifies the type of information that the ZwSetInformationEnlistment routine can set and that the ZwQueryInformationEnlistment routine can retrieve for an enlistment object. |
| [IO_PRIORITY_HINT enumeration](..\wdm\ne-wdm--io-priority-hint.md) | The IO_PRIORITY_HINT enumeration type specifies the priority hint for an IRP. |
| [POWER_STATE_TYPE enumeration](..\wdm\ne-wdm--power-state-type.md) | The POWER_STATE_TYPE enumeration type indicates that a power state value is a system power state or a device power state. |
| [KINTERRUPT_POLARITY enumeration](..\wdm\ne-wdm--kinterrupt-polarity.md) | The KINTERRUPT_POLARITY enumeration indicates how a device signals an interrupt request on an interrupt line. |
| [TRANSACTION_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--transaction-information-class.md) | The TRANSACTION_INFORMATION_CLASS enumeration specifies the type of information that ZwSetInformationTransaction can set and ZwQueryInformationTransaction can retrieve for a transaction manager object. |
| [IRQ_DEVICE_POLICY enumeration](..\wdm\ne-wdm--irq-device-policy.md) | The IRQ_DEVICE_POLICY enumeration type indicates the policy the operating system can use to assign the interrupts from a device to different processors. |
| [DEVICE_POWER_STATE enumeration](..\wdm\ne-wdm--device-power-state.md) | The DEVICE_POWER_STATE enumeration type indicates a device power state. |
| [IRQ_PRIORITY enumeration](..\wdm\ne-wdm--irq-priority.md) | The IRQ_PRIORITY enumeration type indicates the priority the system should give to servicing a device's interrupts. |
| [DEVICE_WAKE_DEPTH enumeration](..\wdm\ne-wdm--device-wake-depth.md) | The DEVICE_WAKE_DEPTH enumeration specifies the deepest device power state from which a device can trigger a wake signal. |
| [TRANSACTION_OUTCOME enumeration](..\wdm\ne-wdm--transaction-outcome.md) | The TRANSACTION_OUTCOME enumeration defines the outcomes (results) that KTM can assign to a transaction. |
| [WORK_QUEUE_TYPE enumeration](..\wdm\ne-wdm--work-queue-type.md) | The WORK_QUEUE_TYPE enumeration type indicates the type of system worker thread that handles a work item. |
| [MONITOR_DISPLAY_STATE enumeration](..\wdm\ne-wdm--monitor-display-state.md) | Indicates the power state of the monitor being displayed on. |
| [POOL_TYPE enumeration](..\wdm\ne-wdm--pool-type~r1.md) | The POOL_TYPE enumeration type specifies the type of system memory to allocate. |
| [DEVICE_RESET_TYPE enumeration](..\wdm\ne-wdm--device-reset-type.md) | The DEVICE_RESET_TYPE enumeration specifies the type of device reset that is being requested by a call to the DeviceReset routine of the GUID_DEVICE_RESET_INTERFACE_STANDARD interface. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [OB_PRE_OPERATION_PARAMETERS structure](..\wdm\ns-wdm--ob-pre-operation-parameters.md) | The OB_PRE_OPERATION_PARAMETERS union describes the operation-specific parameters for an ObjectPreCallback routine. |
| [OB_OPERATION_REGISTRATION structure](..\wdm\ns-wdm--ob-operation-registration.md) | The OB_OPERATION_REGISTRATION structure specifies ObjectPreCallback and ObjectPostCallback callback routines and the types of operations that the routines are called for. |
| [DEVICE_RESET_INTERFACE_STANDARD structure](..\wdm\ns-wdm--device-reset-interface-standard.md) | The DEVICE_RESET_INTERFACE_STANDARD structure enables function drivers to reset and recover malfunctioning devices. This structure describes the GUID_DEVICE_RESET_INTERFACE_STANDARD interface. |
| [CM_Power_Data_s structure](..\wdm\ns-wdm-cm-power-data-s.md) | The CM_POWER_DATA structure contains information about a device's power management state and capabilities. |
| [FILE_FULL_EA_INFORMATION structure](..\wdm\ns-wdm--file-full-ea-information.md) | The FILE_FULL_EA_INFORMATION structure provides extended attribute (EA) information. This structure is used primarily by network drivers. |
| [REG_QUERY_KEY_SECURITY_INFORMATION structure](..\wdm\ns-wdm--reg-query-key-security-information.md) | The REG_QUERY_KEY_SECURITY_INFORMATION structure receives security information for a registry key object. |
| [OB_CALLBACK_REGISTRATION structure](..\wdm\ns-wdm--ob-callback-registration.md) | The OB_CALLBACK_REGISTRATION structure specifies the parameters when the ObRegisterCallbacks routine registers ObjectPreCallback and ObjectPostCallback callback routines. |
| [REG_UNLOAD_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-unload-key-information.md) | The REG_UNLOAD_KEY_INFORMATION structure contains information that a driver's RegistryCallback routine can use when a registry hive is unloaded. |
| [ENLISTMENT_BASIC_INFORMATION structure](..\wdm\ns-wdm--enlistment-basic-information.md) | The ENLISTMENT_BASIC_INFORMATION structure contains information about an enlistment object. |
| [REG_SET_INFORMATION_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-set-information-key-information.md) | The REG_SET_INFORMATION_KEY_INFORMATION structure describes a new setting for a key's metadata. |
| [PRIVILEGE_SET structure](..\wdm\ns-wdm--privilege-set.md) | The PRIVILEGE_SET structure specifies a set of security privileges. For more information, see the reference page for PRIVILEGE_SET in the Microsoft Windows SDK documentation. |
| [FUNCTION_LEVEL_DEVICE_RESET_PARAMETERS structure](..\wdm\ns-wdm--function-level-device-reset-parameters.md) | The FUNCTION_LEVEL_DEVICE_RESET_PARAMETER structure is used as an argument to the DeviceReset routine of the GUID_DEVICE_RESET_INTERFACE_STANDARD interface. |
| [TRANSACTIONMANAGER_RECOVERY_INFORMATION structure](..\wdm\ns-wdm--transactionmanager-recovery-information.md) | The TRANSACTIONMANAGER_RECOVERY_INFORMATION structure contains information about a transaction manager object. |
| [REG_SAVE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-save-key-information.md) | The REG_SAVE_KEY_INFORMATION structure contains the information for a registry key that is about to be saved. |
| [RESOURCEMANAGER_COMPLETION_INFORMATION structure](..\wdm\ns-wdm--resourcemanager-completion-information.md) | The RESOURCEMANAGER_COMPLETION_INFORMATION structure is not used. |
| [REENUMERATE_SELF_INTERFACE_STANDARD structure](..\wdm\ns-wdm--reenumerate-self-interface-standard.md) | The REENUMERATE_SELF_INTERFACE_STANDARD interface structure enables a driver to request that its parent bus driver reenumerate the driver's device. This structure defines the GUID_REENUMERATE_SELF_INTERFACE_STANDARD interface. |
| [REG_REPLACE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-replace-key-information.md) | The REG_REPLACE_KEY_INFORMATION structure describes the metadata that is about to be replaced for a key. |
| [TARGET_DEVICE_CUSTOM_NOTIFICATION structure](..\wdm\ns-wdm--target-device-custom-notification.md) | The TARGET_DEVICE_CUSTOM_NOTIFICATION structure describes a custom device event. |
| [TRANSACTIONMANAGER_LOGPATH_INFORMATION structure](..\wdm\ns-wdm--transactionmanager-logpath-information.md) | The TRANSACTIONMANAGER_LOGPATH_INFORMATION structure contains information about a transaction manager object. |
| [REG_CREATE_KEY_INFORMATION_V1 structure](..\wdm\ns-wdm--reg-create-key-information-v1.md) | The REG_OPEN_KEY_INFORMATION_V1 structure contains information that a filter driver's RegistryCallback routine can use when a registry key is being opened. |
| [DEVICE_DESCRIPTION structure](..\wdm\ns-wdm--device-description~r1.md) | The DEVICE_DESCRIPTION structure describes the attributes of the physical device for which a driver is requesting a DMA adapter. |
| [TARGET_DEVICE_REMOVAL_NOTIFICATION structure](..\wdm\ns-wdm--target-device-removal-notification.md) | The TARGET_DEVICE_REMOVAL_NOTIFICATION structure describes a device-removal event. The PnP manager sends this structure to a driver that registered a callback routine for notification of EventCategoryTargetDeviceChange events. |
| [PO_FX_PERF_STATE_CHANGE structure](..\wdm\ns-wdm--po-fx-perf-state-change.md) | The PO_FX_PERF_STATE_CHANGE structure contains information about a change to a performance state that is being requested by calling the PoFxIssueComponentPerfStateChange or PoFxIssueComponentPerfStateChangeMultiple routine. |
| [OB_POST_OPERATION_INFORMATION structure](..\wdm\ns-wdm--ob-post-operation-information.md) | The OB_POST_OPERATION_INFORMATION structure provides information about a process or thread handle operation to an ObjectPostCallback routine. |
| [SECTION_OBJECT_POINTERS structure](..\wdm\ns-wdm--section-object-pointers.md) | The SECTION_OBJECT_POINTERS structure, allocated by a file system or a redirector driver, is used by the memory manager and cache manager to store file-mapping and cache-related information for a file stream. |
| [PCI_VIRTUALIZATION_INTERFACE structure](..\wdm\ns-wdm--pci-virtualization-interface.md) | The PCI_VIRTUALIZATION_INTERFACE structure enables drivers to manage and configure the PCI Express (PCIe) configuration space for a virtual function (VF). |
| [FILE_STANDARD_INFORMATION structure](..\wdm\ns-wdm--file-standard-information.md) | The FILE_STANDARD_INFORMATION structure is used as an argument to routines that query or set file information. |
| [HWPROFILE_CHANGE_NOTIFICATION structure](..\wdm\ns-wdm--hwprofile-change-notification.md) | The HWPROFILE_CHANGE_NOTIFICATION structure describes an event related to a hardware profile configuration change. |
| [FILE_STANDARD_INFORMATION_EX structure](..\wdm\ns-wdm--file-standard-information-ex.md) | The FILE_STANDARD_INFORMATION_EX structure is used as an argument to routines that query or set file information. |
| [REG_ENUMERATE_VALUE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-enumerate-value-key-information.md) | The REG_ENUMERATE_VALUE_KEY_INFORMATION structure describes one value entry of a key whose value entries are being enumerated. |
| [PLUGPLAY_NOTIFICATION_HEADER structure](..\wdm\ns-wdm--plugplay-notification-header.md) | A PLUGPLAY_NOTIFICATION_HEADER structure is included at the beginning of each PnP notification structure, such as a DEVICE_INTERFACE_CHANGE_NOTIFICATION structure. |
| [OB_POST_OPERATION_PARAMETERS structure](..\wdm\ns-wdm--ob-post-operation-parameters.md) | The OB_POST_OPERATION_PARAMETERS union describes the operation-specific parameters for an ObjectPostCallback routine. |
| [IO_INTERRUPT_MESSAGE_INFO structure](..\wdm\ns-wdm--io-interrupt-message-info.md) | The IO_INTERRUPT_MESSAGE_INFO structure describes the driver's message-signaled interrupts. |
| [BOOTDISK_INFORMATION structure](..\wdm\ns-wdm--bootdisk-information.md) | The BOOTDISK_INFORMATION structure contains basic information describing the boot and system disks. |
| [OB_PRE_CREATE_HANDLE_INFORMATION structure](..\wdm\ns-wdm--ob-pre-create-handle-information.md) | The OB_PRE_CREATE_HANDLE_INFORMATION structure provides information to an ObjectPreCallback routine about a thread or process handle that is being opened. |
| [MDL structure](..\wdm\ns-wdm--mdl.md) | An MDL structure is a partially opaque structure that represents a memory descriptor list (MDL). |
| [CM_EISA_SLOT_INFORMATION structure](..\wdm\ns-wdm--cm-eisa-slot-information.md) | The CM_EISA_SLOT_INFORMATION structure defines EISA configuration header information returned by HalGetBusData for the input BusDataType = EisaConfiguration, or by HalGetBusDataByOffset for the inputs BusDataType = EisaConfiguration and Offset = 0, assuming the caller-allocated Buffer is of sufficient Length. |
| [TRANSACTIONMANAGER_BASIC_INFORMATION structure](..\wdm\ns-wdm--transactionmanager-basic-information.md) | The TRANSACTIONMANAGER_BASIC_INFORMATION structure contains information about a transaction manager object. |
| [INTERFACE structure](..\wdm\ns-wdm--interface.md) | The INTERFACE structure describes an interface that is exported by a driver for use by other drivers. |
| [CM_FLOPPY_DEVICE_DATA structure](..\wdm\ns-wdm--cm-floppy-device-data.md) | The CM_FLOPPY_DEVICE_DATA structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a floppy controller if the system can collect this information during the boot process. |
| [DMA_ADAPTER_INFO_V1 structure](..\wdm\ns-wdm--dma-adapter-info-v1.md) | The DMA_ADAPTER_INFO_V1 structure describes the capabilities of the system DMA controller that is represented by an adapter object. |
| [PCI_SLOT_NUMBER structure](..\wdm\ns-wdm--pci-slot-number.md) | The PCI_SLOT_NUMBER structure is obsolete. |
| [POWER_PLATFORM_INFORMATION structure](..\wdm\ns-wdm--power-platform-information.md) | The POWER_PLATFORM_INFORMATION structure contains information about the power capabilities of the system. |
| [PCI_COMMON_CONFIG structure](..\wdm\ns-wdm--pci-common-config.md) | The PCI_COMMON_CONFIG structure is obsolete. |
| [FILE_IS_REMOTE_DEVICE_INFORMATION structure](..\wdm\ns-wdm--file-is-remote-device-information.md) | The FILE_IS_REMOTE_DEVICE_INFORMATION structure is used as an argument to the ZwQueryInformationFile routine. |
| [CM_PARTIAL_RESOURCE_LIST structure](..\wdm\ns-wdm--cm-partial-resource-list.md) | The CM_PARTIAL_RESOURCE_LIST structure specifies a set of system hardware resources, of various types, assigned to a device. This structure is contained within a CM_FULL_RESOURCE_DESCRIPTOR structure. |
| [KEY_VALUE_ENTRY structure](..\wdm\ns-wdm--key-value-entry.md) | The KEY_VALUE_ENTRY structure is used by the REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION structure to describe a single value entry for a registry key. |
| [FILE_NETWORK_OPEN_INFORMATION structure](..\wdm\ns-wdm--file-network-open-information.md) | The FILE_NETWORK_OPEN_INFORMATION structure is used as an argument to ZwQueryInformationFile. |
| [FILE_OBJECT structure](..\wdm\ns-wdm--file-object~r1.md) | The FILE_OBJECT structure is used by the system to represent a file object. |
| [IO_INTERRUPT_MESSAGE_INFO_ENTRY structure](..\wdm\ns-wdm--io-interrupt-message-info-entry.md) | The IO_INTERRUPT_MESSAGE_INFO_ENTRY structure describes the properties of a single message-signaled interrupt. |
| [REG_CREATE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-create-key-information.md) | The REG_OPEN_KEY_INFORMATION structure contains the name of a registry key that is about to be opened. |
| [RESOURCEMANAGER_BASIC_INFORMATION structure](..\wdm\ns-wdm--resourcemanager-basic-information.md) | The RESOURCEMANAGER_BASIC INFORMATION structure contains information about a resource manager object. |
| [KDPC_WATCHDOG_INFORMATION structure](..\wdm\ns-wdm--kdpc-watchdog-information.md) | The KDPC_WATCHDOG_INFORMATION structure holds time-out information about the current deferred procedure call (DPC). |
| [FILE_BASIC_INFORMATION structure](..\wdm\ns-wdm--file-basic-information.md) | The FILE_BASIC_INFORMATION structure is used as an argument to routines that query or set file information. |
| [PO_FX_COMPONENT_PERF_SET structure](..\wdm\ns-wdm--po-fx-component-perf-set.md) | The PO_FX_COMPONENT_PERF_SET structure represents a set of performance states for a single component within a device. |
| [REG_QUERY_KEY_NAME structure](..\wdm\ns-wdm--reg-query-key-name.md) | The REG_QUERY_KEY_NAME structure describes the full registry key name of an object being queried. |
| [FILE_IO_PRIORITY_HINT_INFORMATION structure](..\wdm\ns-wdm--file-io-priority-hint-information.md) | The FILE_IO_PRIORITY_HINT_INFORMATION structure is used by the ZwQueryInformationFile and ZwSetInformationFile routines to query and set the default IRP priority hint for requests on the specified file handle. |
| [SDEV_IDENTIFIER_INTERFACE structure](..\wdm\ns-wdm--sdev-identifier-interface.md) | TBD. |
| [POWER_STATE structure](..\wdm\ns-wdm--power-state.md) | The POWER_STATE union specifies a system power state value or a device power state value. |
| [MM_PHYSICAL_ADDRESS_LIST structure](..\wdm\ns-wdm--mm-physical-address-list.md) | The MM_PHYSICAL_ADDRESS_LIST structure specifies a range of physical addresses. |
| [TRANSACTION_ENLISTMENT_PAIR structure](..\wdm\ns-wdm--transaction-enlistment-pair.md) | The TRANSACTION_ENLISTMENT_PAIR structure contains information about an enlistment that is associated with a transaction object. |
| [KEY_VALUE_FULL_INFORMATION structure](..\wdm\ns-wdm--key-value-full-information.md) | The KEY_VALUE_FULL_INFORMATION structure defines information available for a value entry of a registry key. |
| [IO_RESOURCE_LIST structure](..\wdm\ns-wdm--io-resource-list.md) | The IO_RESOURCE_LIST structure describes a range of raw hardware resources, of various types, that can be used by a device. |
| [DMA_TRANSFER_INFO structure](..\wdm\ns-wdm--dma-transfer-info.md) | The DMA_TRANSFER_INFO structure is a container for a DMA_TRANSFER_INFO_XXX structure that describes the allocation requirements for a scatter/gather list. |
| [IO_STATUS_BLOCK structure](..\wdm\ns-wdm--io-status-block.md) | A driver sets an IRP's I/O status block to indicate the final status of an I/O request, before calling IoCompleteRequest for the IRP. |
| [TRANSACTION_BASIC_INFORMATION structure](..\wdm\ns-wdm--transaction-basic-information.md) | The TRANSACTION_BASIC_INFORMATION structure contains information about a transaction object. |
| [IO_STACK_LOCATION structure](..\wdm\ns-wdm--io-stack-location.md) | The IO_STACK_LOCATION structure defines an I/O stack location, which is an entry in the I/O stack that is associated with each IRP. |
| [PNP_BUS_INFORMATION structure](..\wdm\ns-wdm--pnp-bus-information.md) | The PNP_BUS_INFORMATION structure describes a bus. |
| [CLFS_MGMT_CLIENT_REGISTRATION structure](..\wdm\ns-wdm--clfs-mgmt-client-registration.md) | The CLFS_MGMT_CLIENT_REGISTRATION structure is given to CLFS management by clients who manage their own logs. |
| [CM_SCSI_DEVICE_DATA structure](..\wdm\ns-wdm--cm-scsi-device-data.md) | The CM_SCSI_DEVICE_DATA structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a SCSI HBA if the system can collect this information during the boot process. |
| [DMA_OPERATIONS structure](..\wdm\ns-wdm--dma-operations~r1.md) | The DMA_OPERATIONS structure provides a table of pointers to functions that control the operation of a DMA controller. |
| [KEY_FULL_INFORMATION structure](..\wdm\ns-wdm--key-full-information.md) | The KEY_FULL_INFORMATION structure defines the information available for a registry key, including information about its subkeys and the maximum length for their names and value entries. |
| [SYSTEM_POWER_STATE_CONTEXT structure](..\wdm\ns-wdm--system-power-state-context.md) | The SYSTEM_POWER_STATE_CONTEXT structure is a partially opaque system structure that contains information about the previous system power states of a computer. |
| [IO_SESSION_CONNECT_INFO structure](..\wdm\ns-wdm--io-session-connect-info.md) | The IO_SESSION_CONNECT_INFO structure provides information about a user session. |
| [BOOTDISK_INFORMATION_EX structure](..\wdm\ns-wdm--bootdisk-information-ex.md) | The BOOTDISK_INFORMATION_EX structure contains extended information describing the boot and system disks. |
| [REG_KEY_HANDLE_CLOSE_INFORMATION structure](..\wdm\ns-wdm--reg-key-handle-close-information.md) | The REG_KEY_HANDLE_CLOSE_INFORMATION structure contains information about a registry key whose handle is about to be closed. |
| [REG_ENUMERATE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-enumerate-key-information.md) | The REG_ENUMERATE_KEY_INFORMATION structure describes one subkey of a key whose subkeys are being enumerated. |
| [REG_RENAME_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-rename-key-information.md) | The REG_RENAME_KEY_INFORMATION structure contains the new name for a registry key whose name is about to be changed. |
| [KBUGCHECK_SECONDARY_DUMP_DATA structure](..\wdm\ns-wdm--kbugcheck-secondary-dump-data.md) | The KBUGCHECK_SECONDARY_DUMP_DATA structure describes a section of driver-supplied data to be written by BugCheckSecondaryDumpDataCallback to the crash dump file. |
| [SCATTER_GATHER_LIST structure](..\wdm\ns-wdm--scatter-gather-list~r1.md) | The SCATTER_GATHER_LIST structure describes the scatter/gather list for a DMA operation. |
| [LINK_SHARE_ACCESS structure](..\wdm\ns-wdm--link-share-access.md) | The share access structure used by file systems for only link files. |
| [IO_SESSION_STATE_NOTIFICATION structure](..\wdm\ns-wdm--io-session-state-notification.md) | The IO_SESSION_STATE_NOTIFICATION structure contains information that a kernel-mode driver supplies to the IoRegisterContainerNotification routine when the driver registers to receive notifications of session events. |
| [REG_POST_OPERATION_INFORMATION structure](..\wdm\ns-wdm--reg-post-operation-information.md) | The REG_POST_OPERATION_INFORMATION structure contains information about a completed registry operation that a RegistryCallback routine can use. |
| [IO_CONNECT_INTERRUPT_PARAMETERS structure](..\wdm\ns-wdm--io-connect-interrupt-parameters.md) | The IO_CONNECT_INTERRUPT_PARAMETERS structure contains the parameters that a driver supplies to the IoConnectInterruptEx routine to register an interrupt service routine (ISR). |
| [KEY_VALUE_BASIC_INFORMATION structure](..\wdm\ns-wdm--key-value-basic-information.md) | The KEY_VALUE_BASIC_INFORMATION structure defines a subset of the full information available for a value entry of a registry key. |
| [DMA_TRANSFER_INFO_V1 structure](..\wdm\ns-wdm--dma-transfer-info-v1.md) | The DMA_TRANSFER_INFO_V1 structure contains the allocation requirements for a scatter/gather list that describes the I/O data buffer for a DMA transfer. |
| [IO_RESOURCE_DESCRIPTOR structure](..\wdm\ns-wdm--io-resource-descriptor.md) | The IO_RESOURCE_DESCRIPTOR structure describes a range of raw hardware resources, of one type, that can be used by a device. An array of IO_RESOURCE_DESCRIPTOR structures is contained within each IO_RESOURCE_LIST structure. |
| [KEY_NODE_INFORMATION structure](..\wdm\ns-wdm--key-node-information.md) | The KEY_NODE_INFORMATION structure defines the basic information available for a registry (sub)key. |
| [CLFS_MGMT_POLICY structure](..\wdm\ns-wdm--clfs-mgmt-policy.md) | The CLFS_MGMT_POLICY structure holds a description of a policy for managing a CLFS log. |
| [IO_SESSION_STATE_INFORMATION structure](..\wdm\ns-wdm--io-session-state-information.md) | The IO_SESSION_STATE_INFORMATION structure contains information about the state of a user session. |
| [REG_POST_CREATE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-post-create-key-information.md) | The REG_POST_OPEN_KEY_INFORMATION structure contains the result of an attempt to open a registry key. |
| [REG_QUERY_VALUE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-query-value-key-information.md) | The REG_QUERY_VALUE_KEY_INFORMATION structure contains information about a registry key's value entry that is being queried. |
| [OB_PRE_DUPLICATE_HANDLE_INFORMATION structure](..\wdm\ns-wdm--ob-pre-duplicate-handle-information.md) | The OB_PRE_DUPLICATE_HANDLE_INFORMATION structure provides information to an ObjectPreCallback routine about a thread or process handle that is being duplicated. |
| [KEY_WRITE_TIME_INFORMATION structure](..\wdm\ns-wdm--key-write-time-information.md) | The KEY_WRITE_TIME_INFORMATION structure is used by the system to set the last write time for a registry key. |
| [D3COLD_SUPPORT_INTERFACE structure](..\wdm\ns-wdm--d3cold-support-interface.md) | The D3COLD_SUPPORT_INTERFACE interface structure contains pointers to the routines in the GUID_D3COLD_SUPPORT_INTERFACE driver interface. |
| [IO_DISCONNECT_INTERRUPT_PARAMETERS structure](..\wdm\ns-wdm--io-disconnect-interrupt-parameters.md) | The IO_DISCONNECT_INTERRUPT_PARAMETERS structure describes the parameters when unregistering an interrupt-handling routine with IoDisconnectInterruptEx. |
| [REG_DELETE_VALUE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-delete-value-key-information.md) | The REG_DELETE_VALUE_KEY_INFORMATION structure contains information that a driver's RegistryCallback routine can use when a registry key's value is being deleted. |
| [COUNTED_REASON_CONTEXT structure](..\wdm\ns-wdm--counted-reason-context.md) | The COUNTED_REASON_CONTEXT structure contains one or more strings that give reasons for a power request. |
| [DEVICE_CAPABILITIES structure](..\wdm\ns-wdm--device-capabilities.md) | A DEVICE_CAPABILITIES structure describes PnP and power capabilities of a device. This structure is returned in response to an IRP_MN_QUERY_CAPABILITIES IRP. |
| [KTMOBJECT_CURSOR structure](..\wdm\ns-wdm--ktmobject-cursor.md) | The KTMOBJECT_CURSOR structure receives enumeration information about KTM objects when a component calls ZwEnumerateTransactionObject. |
| [EXT_DELETE_PARAMETERS structure](..\wdm\ns-wdm--ext-delete-parameters.md) | The EXT_DELETE_PARAMETERS structure contains an extended set of parameters for the ExDeleteTimer routine. |
| [FILE_FS_DEVICE_INFORMATION structure](..\wdm\ns-wdm--file-fs-device-information.md) | The FILE_FS_DEVICE_INFORMATION structure provides file system device information about the type of device object associated with a file object. |
| [OB_PRE_OPERATION_INFORMATION structure](..\wdm\ns-wdm--ob-pre-operation-information.md) | The OB_PRE_OPERATION_INFORMATION structure provides information about a process or thread handle operation to an ObjectPreCallback routine. |
| [KE_PROCESSOR_CHANGE_NOTIFY_CONTEXT structure](..\wdm\ns-wdm--ke-processor-change-notify-context.md) | The KE_PROCESSOR_CHANGE_NOTIFY_CONTEXT structure describes the notification context that is passed to a registered callback function when a new processor is dynamically added to a hardware partition. |
| [DRIVER_OBJECT structure](..\wdm\ns-wdm--driver-object~r3.md) | Each driver object represents the image of a loaded kernel-mode driver. |
| [CLFS_LOG_NAME_INFORMATION structure](..\wdm\ns-wdm--clfs-log-name-information.md) | The CLFS_LOG_NAME_INFORMATION structure holds the name of a Common Log File System (CLFS) stream or log. |
| [GENERIC_MAPPING structure](..\wdm\ns-wdm--generic-mapping.md) | The GENERIC_MAPPING structure describes the ACCESS_MASK value of specific access rights associated with each type of generic access right. |
| [REG_PRE_CREATE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-pre-create-key-information.md) | The REG_PRE_OPEN_KEY_INFORMATION structure contains the name of a registry key that is about to be opened. |
| [PCI_COMMON_CONFIG structure](..\wdm\ns-wdm--pci-common-config~r1.md) | The PCI_COMMON_CONFIG structure is obsolete. |
| [PO_FX_COMPONENT_PERF_INFO structure](..\wdm\ns-wdm--po-fx-component-perf-info.md) | The PO_FX_COMPONENT_PERF_INFO structure describes all the sets of performance states for a single component within a device. |
| [CM_INT13_DRIVE_PARAMETER structure](..\wdm\ns-wdm--cm-int13-drive-parameter.md) | The CM_INT13_DRIVE_PARAMETER structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a disk controller if the system can collect this information during the boot process. |
| [DMA_ADAPTER_INFO structure](..\wdm\ns-wdm--dma-adapter-info.md) | The DMA_ADAPTER_INFO structure is a container for a DMA_ADAPTER_INFO_XXX structure that describes the capabilities of a system DMA controller. |
| [CM_SERIAL_DEVICE_DATA structure](..\wdm\ns-wdm--cm-serial-device-data.md) | The CM_SERIAL_DEVICE_DATA structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a serial controller if the system can collect this information during the boot process. |
| [EXT_SET_PARAMETERS_V0 structure](..\wdm\ns-wdm--ext-set-parameters-v0.md) | The EXT_SET_PARAMETERS structure contains an extended set of parameters for the ExSetTimer routine. |
| [PCI_MSIX_TABLE_CONFIG_INTERFACE structure](..\wdm\ns-wdm--pci-msix-table-config-interface.md) | The PCI_MSIX_TABLE_CONFIG_INTERFACE structure enables device drivers to modify their MSI-X interrupt settings. This structure describes the GUID_MSIX_TABLE_CONFIG_INTERFACE interface. |
| [CM_KEYBOARD_DEVICE_DATA structure](..\wdm\ns-wdm--cm-keyboard-device-data.md) | The CM_KEYBOARD_DEVICE_DATA structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a keyboard peripheral if the system can collect this information during the boot process. |
| [CM_RESOURCE_LIST structure](..\wdm\ns-wdm--cm-resource-list.md) | The CM_RESOURCE_LIST structure specifies all of the system hardware resources assigned to a device. |
| [PO_FX_COMPONENT_IDLE_STATE structure](..\wdm\ns-wdm--po-fx-component-idle-state.md) | The PO_FX_COMPONENT_IDLE_STATE structure specifies the attributes of an Fx power state of a component in a device. |
| [REG_SET_KEY_SECURITY_INFORMATION structure](..\wdm\ns-wdm--reg-set-key-security-information.md) | The REG_SET_KEY_SECURITY_INFORMATION structure specifies security information for a registry key object. |
| [TRANSACTIONMANAGER_LOG_INFORMATION structure](..\wdm\ns-wdm--transactionmanager-log-information.md) | The TRANSACTIONMANAGER_LOG_INFORMATION structure contains information about a transaction manager object. |
| [IO_RESOURCE_REQUIREMENTS_LIST structure](..\wdm\ns-wdm--io-resource-requirements-list.md) | The IO_RESOURCE_REQUIREMENTS_LIST structure describes sets of resource configurations that can be used by a device. Each configuration represents a range of raw resources, of various types, that can be used by a device. |
| [OB_POST_CREATE_HANDLE_INFORMATION structure](..\wdm\ns-wdm--ob-post-create-handle-information.md) | The OB_POST_CREATE_HANDLE_INFORMATION structure provides information to a ObjectPostCallback routine about a thread or process handle that has been opened. |
| [CLFS_STREAM_ID_INFORMATION structure](..\wdm\ns-wdm--clfs-stream-id-information.md) | The CLFS_STREAM_ID_INFORMATION structure holds a value that identifies a stream in a Common Log File System (CLFS) log. |
| [REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-query-multiple-value-key-information.md) | The REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION structure describes the multiple value entries that are being retrieved for a key. |
| [CM_EISA_FUNCTION_INFORMATION structure](..\wdm\ns-wdm--cm-eisa-function-information.md) | The CM_EISA_FUNCTION_INFORMATION structure defines detailed EISA configuration information returned by HalGetBusData for the input BusDataType EisaConfiguration, or by HalGetBusDataByOffset for the input BusDataType EisaConfiguration and the Offset zero, assuming the caller-allocated Buffer is of sufficient Length. |
| [DMA_ADAPTER structure](..\wdm\ns-wdm--dma-adapter~r5.md) | The DMA_ADAPTER structure describes a system-defined interface to a DMA controller for a given device. A driver calls IoGetDmaAdapter to obtain this structure. |
| [DEVICE_INTERFACE_CHANGE_NOTIFICATION structure](..\wdm\ns-wdm--device-interface-change-notification.md) | The DEVICE_INTERFACE_CHANGE_NOTIFICATION structure describes a device interface that has been enabled (arrived) or disabled (removed). |
| [TRANSACTION_ENLISTMENTS_INFORMATION structure](..\wdm\ns-wdm--transaction-enlistments-information.md) | The TRANSACTION_ENLISTMENTS_INFORMATION structure contains information about the enlistments that are associated with a transaction object. |
| [IO_ERROR_LOG_PACKET structure](..\wdm\ns-wdm--io-error-log-packet.md) | The IO_ERROR_LOG_PACKET structure serves as the header for an error log entry. |
| [KEY_BASIC_INFORMATION structure](..\wdm\ns-wdm--key-basic-information.md) | The KEY_BASIC_INFORMATION structure defines a subset of the full information that is available for a registry key. |
| [BUS_INTERFACE_STANDARD structure](..\wdm\ns-wdm--bus-interface-standard.md) | The BUS_INTERFACE_STANDARD interface structure enables device drivers to make direct calls to parent bus driver routines. This structure defines the GUID_BUS_INTERFACE_STANDARD interface. |
| [PO_FX_PERF_STATE structure](..\wdm\ns-wdm--po-fx-perf-state.md) | The PO_FX_PERF_STATE structure represents a performance state for a single component within a device. |
| [REG_SET_VALUE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-set-value-key-information.md) | The REG_SET_VALUE_INFORMATION structure describes a new setting for a registry key's value entry. |
| [KEY_VALUE_PARTIAL_INFORMATION structure](..\wdm\ns-wdm--key-value-partial-information.md) | The KEY_VALUE_PARTIAL_INFORMATION structure defines a subset of the value information available for a value entry of a registry key. |
| [FILE_POSITION_INFORMATION structure](..\wdm\ns-wdm--file-position-information.md) | The FILE_POSITION_INFORMATION structure is used as an argument to routines that query or set file information. |
| [KBUGCHECK_ADD_PAGES structure](..\wdm\ns-wdm--kbugcheck-add-pages.md) | The KBUGCHECK_ADD_PAGES structure describes one or more pages of driver-supplied data to be written by a BugCheckAddPagesCallback callback routine to the crash dump file. |
| [CM_PARTIAL_RESOURCE_DESCRIPTOR structure](..\wdm\ns-wdm--cm-partial-resource-descriptor.md) | The CM_PARTIAL_RESOURCE_DESCRIPTOR structure specifies one or more system hardware resources, of a single type, assigned to a device. |
| [OB_POST_DUPLICATE_HANDLE_INFORMATION structure](..\wdm\ns-wdm--ob-post-duplicate-handle-information.md) | The OB_POST_DUPLICATE_HANDLE_INFORMATION structure provides information to an ObjectPostCallback routine about a thread or process handle that has been duplicated. |
| [REG_CALLBACK_CONTEXT_CLEANUP_INFORMATION structure](..\wdm\ns-wdm--reg-callback-context-cleanup-information.md) | The REG_CALLBACK_CONTEXT_CLEANUP_INFORMATION structure contains information that a driver's RegistryCallback routine can use to free resources that the driver previously allocated for the context that is associated with a registry object. |
| [REG_LOAD_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-load-key-information.md) | The REG_LOAD_KEY_INFORMATION structure contains information about a registry hive that is being loaded. |
| [CM_FULL_RESOURCE_DESCRIPTOR structure](..\wdm\ns-wdm--cm-full-resource-descriptor.md) | The CM_FULL_RESOURCE_DESCRIPTOR structure specifies a set of system hardware resources of various types, assigned to a device that is connected to a specific bus. This structure is contained within a CM_RESOURCE_LIST structure. |
| [IO_SECURITY_CONTEXT structure](..\wdm\ns-wdm--io-security-context.md) | The IO_SECURITY_CONTEXT structure represents the security context of an IRP_MJ_CREATE request. |
| [TRANSACTION_PROPERTIES_INFORMATION structure](..\wdm\ns-wdm--transaction-properties-information.md) | The TRANSACTION_PROPERTIES_INFORMATION structure contains a transaction object's properties. |
| [CM_MCA_POS_DATA structure](..\wdm\ns-wdm--cm-mca-pos-data.md) | The CM_MCA_POS_DATA structure is obsolete. It defines IBM-compatible MCA POS configuration information for a slot. |
| [REG_RESTORE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-restore-key-information.md) | The REG_RESTORE_KEY_INFORMATION structure contains the information for a registry key that is about to be restored. |
| [REG_QUERY_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-query-key-information.md) | The REG_QUERY_KEY_INFORMATION structure describes the metadata that is about to be queried for a key. |
| [KBUGCHECK_DUMP_IO structure](..\wdm\ns-wdm--kbugcheck-dump-io.md) | The KBUGCHECK_DUMP_IO structure describes an I/O operation on the crash dump file. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdmlibIoCreateDeviceSecure function](..\wdmsec\nf-wdmsec-wdmlibiocreatedevicesecure.md) | The WdmlibIoCreateDeviceSecure function creates a named device object and applies the specified security settings. |
| [WdmlibIoValidateDeviceIoControlAccess function](..\wdmsec\nf-wdmsec-wdmlibiovalidatedeviceiocontrolaccess.md) | The WdmlibIoValidateDeviceIoControlAccess function verifies that the sender of an IRP_MJ_DEVICE_CONTROL or IRP_MJ_FILE_SYSTEM_CONTROL IRP has the specified access to the device object. |
| [WdmlibRtlInitUnicodeStringEx function](..\wdmsec\nf-wdmsec-wdmlibrtlinitunicodestringex.md) | The WdmlibRtlInitUnicodeStringEx function initializes a counted string of Unicode characters. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WMIGUIDREGINFO structure](..\wmilib\ns-wmilib--wmiguidreginfo.md) | The WMIGUIDREGINFO structure contains registration information for a given data block or event block exposed by a driver that uses the WMI library support routines. |
| [WMILIB_CONTEXT structure](..\wmilib\ns-wmilib--wmilib-context.md) | The WMILIB_CONTEXT structure provides registration information for a driver's data blocks and event blocks and defines entry points for the driver's WMI library callback routines. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WmiSystemControl function](..\wmilib\nf-wmilib-wmisystemcontrol.md) | The WmiSystemControl routine is a dispatch routine for drivers that use WMI library support routines to handle WMI IRPs. |
| [WmiFireEvent function](..\wmilib\nf-wmilib-wmifireevent.md) | The WmiFireEvent routine sends an event to WMI for delivery to data consumers that have requested notification of the event. |
| [WmiCompleteRequest function](..\wmilib\nf-wmilib-wmicompleterequest.md) | The WmiCompleteRequest routine indicates that a driver has finished processing a WMI request in a DpWmiXxx routine. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [tagWNODE_ALL_DATA structure](..\wmistr\ns-wmistr-tagwnode-all-data.md) | The WNODE_ALL_DATA structure contains data for all instances of a data block or event block. |
| [tagWNODE_TOO_SMALL structure](..\wmistr\ns-wmistr-tagwnode-too-small.md) | The WNODE_TOO_SMALL structure indicates the size of the buffer needed to receive output from a request. |
| [tagWNODE_EVENT_ITEM structure](..\wmistr\ns-wmistr-tagwnode-event-item.md) | The WNODE_EVENT_ITEM structure contains data generated by a driver for an event. |
| [tagWNODE_METHOD_ITEM structure](..\wmistr\ns-wmistr-tagwnode-method-item.md) | The WNODE_METHOD_ITEM structure indicates a method associated with an instance of a data block and contains any input data for the method. |
| [tagWNODE_SINGLE_INSTANCE structure](..\wmistr\ns-wmistr-tagwnode-single-instance.md) | The WNODE_SINGLE_INSTANCE structure contains values for all data items in one instance of a data block. |
| [tagWNODE_EVENT_REFERENCE structure](..\wmistr\ns-wmistr-tagwnode-event-reference.md) | The WNODE_EVENT_REFERENCE structure contains information that WMI can use to query for an event that exceeds the event size limit set in the registry. |
| [tagWNODE_SINGLE_ITEM structure](..\wmistr\ns-wmistr-tagwnode-single-item.md) | The WNODE_SINGLE_ITEM structure contains the value of a single data item in an instance of a data block. |
| [WNODE_HEADER structure](..\wmistr\ns-wmistr--wnode-header.md) | The WNODE_HEADER structure is the first member of all other WNODE_XXX structures. It contains information common to all such structures. |


This technology is in the following headers:


| Header        | 

| [aux_klib](..\aux_klib\~PORTAL~aux_klib.md) | 

| [buffring](..\buffring\~PORTAL~buffring.md) | 

| [hwnclx](..\hwnclx\~PORTAL~hwnclx.md) | 

| [ioaccess](..\ioaccess\~PORTAL~ioaccess.md) | 

| [iointex](..\iointex\~PORTAL~iointex.md) | 

| [ntddk](..\ntddk\~PORTAL~ntddk.md) | 

| [ntddsfio](..\ntddsfio\~PORTAL~ntddsfio.md) | 

| [ntddsysenv](..\ntddsysenv\~PORTAL~ntddsysenv.md) | 

| [ntimage](..\ntimage\~PORTAL~ntimage.md) | 

| [ntintsafe](..\ntintsafe\~PORTAL~ntintsafe.md) | 

| [ntnls](..\ntnls\~PORTAL~ntnls.md) | 

| [ntpoapi](..\ntpoapi\~PORTAL~ntpoapi.md) | 

| [ntstrsafe](..\ntstrsafe\~PORTAL~ntstrsafe.md) | 

| [pcivirt](..\pcivirt\~PORTAL~pcivirt.md) | 

| [pep_x](..\pep_x\~PORTAL~pep_x.md) | 

| [pepevents](..\pepevents\~PORTAL~pepevents.md) | 

| [pepfx](..\pepfx\~PORTAL~pepfx.md) | 

| [procgrp](..\procgrp\~PORTAL~procgrp.md) | 

| [vpci](..\vpci\~PORTAL~vpci.md) | 

| [wdm](..\wdm\~PORTAL~wdm.md) | 

| [wdmsec](..\wdmsec\~PORTAL~wdmsec.md) | 

| [wmidata](..\wmidata\~PORTAL~wmidata.md) | 

| [wmilib](..\wmilib\~PORTAL~wmilib.md) | 

| [wmistr](..\wmistr\~PORTAL~wmistr.md) | 
