# Declarations in the ntddk header
This header Ntddk contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [RtlInitHashTableContextFromEnumerator function](nf-ntddk-rtlinithashtablecontextfromenumerator.md) | TBD |
| [RtlSubtreePredecessor function](nf-ntddk-rtlsubtreepredecessor.md) | The RtlSubtreePredecessor routine returns a pointer to the predecessor of the specified node within the subtree that is rooted at that node. |
| [PsGetThreadCreateTime function](nf-ntddk-psgetthreadcreatetime.md) | TBD |
| [HalExamineMBR function](nf-ntddk-halexaminembr.md) | The HalExamineMBR routine reads the master boot record (MBR) of a disk and returns data from the MBR if the MBR is of the type specified by the caller. |
| [HalAllocateHardwareCounters function](nf-ntddk-halallocatehardwarecounters.md) | The HalAllocateHardwareCounters routine allocates a set of hardware performance counters. |
| [MmAllocateContiguousNodeMemory function](nf-ntddk-mmallocatecontiguousnodememory.md) | TBD |
| [IoVolumeDeviceToGuid function](nf-ntddk-iovolumedevicetoguid.md) | TBD |
| [IO_DRIVER_CREATE_CONTEXT_IS_MIN_SIZE function](nf-ntddk-io-driver-create-context-is-min-size.md) | TBD |
| [IoVerifyPartitionTable function](nf-ntddk-ioverifypartitiontable.md) | The IoVerifyPartitionTable routine checks the validity of the partition table for a disk. |
| [IoSetThreadHardErrorMode function](nf-ntddk-iosetthreadharderrormode.md) | The IoSetThreadHardErrorMode routine enables or disables hard error reporting for the current thread. |
| [RtlConvertUlongToLuid function](nf-ntddk-rtlconvertulongtoluid.md) | The RtlConvertUlongToLuid routine converts an unsigned long integer to a locally unique identifier (LUID), which is used by the system to represent a security privilege. |
| [PsGetThreadExitStatus function](nf-ntddk-psgetthreadexitstatus.md) | TBD |
| [IoAttachDeviceByPointer function](nf-ntddk-ioattachdevicebypointer.md) | TBD |
| [HalDmaFreeCrashDumpRegistersEx function](nf-ntddk-haldmafreecrashdumpregistersex.md) | TBD |
| [NtOpenProcess function](nf-ntddk-ntopenprocess.md) | TBD |
| [RtlGetCallersAddress function](nf-ntddk-rtlgetcallersaddress~r1.md) | TBD |
| [KeQueryHardwareCounterConfiguration function](nf-ntddk-kequeryhardwarecounterconfiguration.md) | The KeQueryHardwareCounterConfiguration routine queries the operating system for the list of hardware counters to use for thread profiling. |
| [IoSetFsZeroingOffset function](nf-ntddk-iosetfszeroingoffset.md) | TBD |
| [KeLeaveCriticalRegion function](nf-ntddk-keleavecriticalregion.md) | The KeLeaveCriticalRegion routine reenables the delivery of normal kernel-mode APCs that were disabled by a preceding call to KeEnterCriticalRegion. |
| [_ExInterlockedDecrementLong function](nf-ntddk--exinterlockeddecrementlong~r1.md) | TBD |
| [WheaFindErrorRecordSection function](nf-ntddk-wheafinderrorrecordsection.md) | The WheaFindErrorRecordSection function searches for a specified Windows Hardware Error Architecture (WHEA) error record section within a WHEA error record. The error record section is formatted as a WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure. |
| [ExInterlockedIncrementLong function](nf-ntddk-exinterlockedincrementlong.md) | TBD |
| [IoIsFileObjectIgnoringSharing function](nf-ntddk-ioisfileobjectignoringsharing.md) | The IoIsFileObjectIgnoringSharing routine determines if a file object is set with the option to ignore file sharing access checks. |
| [RtlIsMultiUsersInSessionSku function](nf-ntddk-rtlismultiusersinsessionsku.md) | TBD |
| [MmMapUserAddressesToPage function](nf-ntddk-mmmapuseraddressestopage.md) | TBD |
| [KeGetCurrentProcessorNumber function](nf-ntddk-kegetcurrentprocessornumber~r1.md) | The KeGetCurrentProcessorNumber routine returns the system-assigned number of the current processor on which the caller is running. |
| [RtlGetSuiteMask function](nf-ntddk-rtlgetsuitemask.md) | TBD |
| [KeQueryTickCount function](nf-ntddk-kequerytickcount.md) | The KeQueryTickCount routine maintains a count of the interval timer interrupts that have occurred since the system was booted. |
| [RtlIsStateSeparationEnabled function](nf-ntddk-rtlisstateseparationenabled.md) | Checks if the SKU for the current context supports multiple sessions. |
| [_ExInterlockedIncrementLong function](nf-ntddk--exinterlockedincrementlong~r1.md) | TBD |
| [RtlRunOnceInitialize function](nf-ntddk-rtlrunonceinitialize.md) | The RtlRunOnceInitialize routine initializes a RTL_RUN_ONCE structure. |
| [RtlDeleteNoSplay function](nf-ntddk-rtldeletenosplay.md) | The RtlDeleteNoSplay routine deletes the specified node from the splay link tree. |
| [HalReadDmaCounter function](nf-ntddk-halreaddmacounter.md) | TBD |
| [RtlNumberGenericTableElements function](nf-ntddk-rtlnumbergenerictableelements.md) | The RtlNumberGenericTableElements routine returns the number of elements in a generic table. |
| [MmIsAddressValid function](nf-ntddk-mmisaddressvalid.md) | The MmIsAddressValid routine checks whether a page fault will occur for a read or write operation at a given virtual address.Warning  We do not recommend using this function. |
| [PsSetCreateProcessNotifyRoutine function](nf-ntddk-pssetcreateprocessnotifyroutine.md) | The PsSetCreateProcessNotifyRoutine routine adds a driver-supplied callback routine to, or removes it from, a list of routines to be called whenever a process is created or deleted. |
| [RtlGetNextEntryHashTable function](nf-ntddk-rtlgetnextentryhashtable.md) | TBD |
| [RtlRunOnceExecuteOnce function](nf-ntddk-rtlrunonceexecuteonce.md) | The RtlRunOnceExecuteOnce performs a one-time initialization. |
| [MmAllocateContiguousMemory function](nf-ntddk-mmallocatecontiguousmemory.md) | The MmAllocateContiguousMemory routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space. |
| [IoSetActivityIdIrp function](nf-ntddk-iosetactivityidirp.md) | The IoSetActivityIdIrp routine associates an activity ID with an IRP. |
| [HvlRegisterWheaErrorNotification function](nf-ntddk-hvlregisterwheaerrornotification.md) | TBD |
| [PsAllocSiloContextSlot function](nf-ntddk-psallocsilocontextslot.md) | This routine allocates a slot that can be used to insert, retrieve, and delete an object in all silos. . |
| [PsRemoveCreateThreadNotifyRoutine function](nf-ntddk-psremovecreatethreadnotifyroutine.md) | The PsRemoveCreateThreadNotifyRoutine routine removes a callback routine that was registered by the PsSetCreateThreadNotifyRoutine routine. |
| [MmUnmapViewInSystemSpace function](nf-ntddk-mmunmapviewinsystemspace.md) | TBD |
| [KeLeaveGuardedRegion function](nf-ntddk-keleaveguardedregion.md) | The KeLeaveGuardedRegion routine exits a guarded region entered by KeEnterGuardedRegion. |
| [FsRtlIsTotalDeviceFailure function](nf-ntddk-fsrtlistotaldevicefailure.md) | The FsRtlIsTotalDeviceFailure routine determines whether a media or other hardware failure has occurred. |
| [IO_DRIVER_CREATE_CONTEXT_CONTAINS_SILO_CONTEXT function](nf-ntddk-io-driver-create-context-contains-silo-context.md) | TBD |
| [RtlInitializeGenericTable function](nf-ntddk-rtlinitializegenerictable.md) | The RtlInitializeGenericTable routine initializes a generic table. |
| [KeGetPcr function](nf-ntddk-kegetpcr.md) | TBD |
| [IoGetOplockKeyContext function](nf-ntddk-iogetoplockkeycontext.md) | The IoGetOplockKeyContext routine returns a target oplock key context for a file object. |
| [RtlLookupElementGenericTableFull function](nf-ntddk-rtllookupelementgenerictablefull.md) | TBD |
| [RtlTotalEntriesHashTable function](nf-ntddk-rtltotalentrieshashtable.md) | TBD |
| [IoFlushAdapterBuffers function](nf-ntddk-ioflushadapterbuffers.md) | TBD |
| [IoCreateDisk function](nf-ntddk-iocreatedisk.md) | The IoCreateDisk routine initializes a raw disk by creating a new partition table. |
| [ExFreeToZone function](nf-ntddk-exfreetozone.md) | TBD |
| [PsSetCreateProcessNotifyRoutineEx function](nf-ntddk-pssetcreateprocessnotifyroutineex.md) | The PsSetCreateProcessNotifyRoutineEx routine registers or removes a callback routine that notifies the caller when a process is created or exits. |
| [KeQueryActiveProcessorCount function](nf-ntddk-kequeryactiveprocessorcount.md) | The KeQueryActiveProcessorCount routine returns the number of currently active processors. |
| [KeQueryLogicalProcessorRelationship function](nf-ntddk-kequerylogicalprocessorrelationship.md) | The KeQueryLogicalProcessorRelationship routine gets information about the relationships of one or more processors to the other processors in a multiprocessor system. |
| [IoMapTransfer function](nf-ntddk-iomaptransfer.md) | TBD |
| [PsSetCreateThreadNotifyRoutineEx function](nf-ntddk-pssetcreatethreadnotifyroutineex.md) | The PsSetCreateThreadNotifyRoutineEx routine registers a driver-supplied callback that is subsequently notified when a new thread is created and when such a thread is deleted. |
| [RtlRightChild function](nf-ntddk-rtlrightchild.md) | The RtlRightChild routine returns a pointer to the right child of the specified splay link node. |
| [_ReturnAddress function](nf-ntddk--returnaddress.md) | TBD |
| [IoGetIrpExtraCreateParameter function](nf-ntddk-iogetirpextracreateparameter.md) | TBD |
| [IoReportResourceUsage function](nf-ntddk-ioreportresourceusage.md) | TBD |
| [PsInsertPermanentSiloContext function](nf-ntddk-psinsertpermanentsilocontext.md) | This routine inserts an object in an empty slot in a Silo. |
| [RtlSplay function](nf-ntddk-rtlsplay.md) | The RtlSplay routine rebalances, or &#0034;splays,&#0034; a splay link tree around the specified splay link, making that link the new root of the tree. |
| [RtlEqualLuid function](nf-ntddk-rtlequalluid.md) | TBD |
| [ZwPowerInformation function](nf-ntddk-zwpowerinformation.md) | The ZwPowerInformation routine sets or retrieves system power information. |
| [KePulseEvent function](nf-ntddk-kepulseevent.md) | The KePulseEvent routine atomically sets an event object to a signaled state, attempts to satisfy as many waits as possible, and then resets the event object to a not-signaled state. |
| [_mm_prefetch function](nf-ntddk--mm-prefetch.md) | TBD |
| [MmAddPhysicalMemory function](nf-ntddk-mmaddphysicalmemory.md) | TBD |
| [PsAttachSiloToCurrentThread function](nf-ntddk-psattachsilotocurrentthread.md) | This routine places a thread temporarily into the specified Silo. |
| [ZwDeviceIoControlFile function](nf-ntddk-zwdeviceiocontrolfile.md) | TBD |
| [MmMapViewInSessionSpaceEx function](nf-ntddk-mmmapviewinsessionspaceex.md) | TBD |
| [PrefetchForWrite function](nf-ntddk-prefetchforwrite.md) | TBD |
| [KeInitializeCrashDumpHeader function](nf-ntddk-keinitializecrashdumpheader.md) | TBD |
| [KeGetCurrentNodeNumber function](nf-ntddk-kegetcurrentnodenumber.md) | The KeGetCurrentNodeNumber routine gets the NUMA node number for the logical processor that the caller is running on. |
| [KeRaiseIrqlToSynchLevel function](nf-ntddk-keraiseirqltosynchlevel.md) | TBD |
| [PsGetCurrentThreadId function](nf-ntddk-psgetcurrentthreadid.md) | The PsGetCurrentThreadId routine identifies the current thread. |
| [IoFreeAdapterChannel function](nf-ntddk-iofreeadapterchannel.md) | TBD |
| [IoAssignResources function](nf-ntddk-ioassignresources.md) | TBD |
| [KeQueryActiveProcessors function](nf-ntddk-kequeryactiveprocessors.md) | The KeQueryActiveProcessors routine returns a bitmask of the currently active processors. |
| [RtlMapGenericMask function](nf-ntddk-rtlmapgenericmask.md) | The RtlMapGenericMask routine determines the nongeneric access rights specified by an ACCESS_MASK. |
| [PsGetThreadProcessId function](nf-ntddk-psgetthreadprocessid.md) | TBD |
| [PsSetCreateProcessNotifyRoutineEx2 function](nf-ntddk-pssetcreateprocessnotifyroutineex2.md) | The PsSetCreateProcessNotifyRoutineEx2 routine registers or removes a callback routine that notifies the caller when a process is created or deleted. |
| [HalFreeHardwareCounters function](nf-ntddk-halfreehardwarecounters.md) | The HalFreeHardwareCounters routine frees a set of hardware performance counters that was acquired in a previous call to HalAllocateHardwareCounters routine. |
| [ExInterlockedAllocateFromZone function](nf-ntddk-exinterlockedallocatefromzone.md) | TBD |
| [ExInitializeZone function](nf-ntddk-exinitializezone.md) | TBD |
| [ExRaiseDatatypeMisalignment function](nf-ntddk-exraisedatatypemisalignment.md) | The ExRaiseDatatypeMisalignment routine can be used with structured exception handling to throw a driver-determined exception for a misaligned data type that occurs when a driver processes I/O requests. |
| [ExUuidCreate function](nf-ntddk-exuuidcreate.md) | The ExUuidCreate routine initializes a UUID (GUID) structure to a newly generated value. |
| [MmMapVideoDisplay function](nf-ntddk-mmmapvideodisplay.md) | TBD |
| [RtlEnumerateGenericTableAvl function](nf-ntddk-rtlenumerategenerictableavl.md) | The RtlEnumerateGenericTableAvl routine is used to enumerate the elements in a generic table. |
| [RtlIncrementCorrelationVector function](nf-ntddk-rtlincrementcorrelationvector.md) | Increments the specified correlation vector. For a correlation vector of the form X.i, the incremented value is be X.(i+1). |
| [Exfi386InterlockedDecrementLong function](nf-ntddk-exfi386interlockeddecrementlong.md) | TBD |
| [RtlLargeIntegerDivide function](nf-ntddk-rtllargeintegerdivide.md) | TBD |
| [ExIsObjectInFirstZoneSegment function](nf-ntddk-exisobjectinfirstzonesegment.md) | TBD |
| [IoInitializeDriverCreateContext function](nf-ntddk-ioinitializedrivercreatecontext.md) | The IoInitializeDriverCreateContext routine initializes a caller-allocated variable of type IO_DRIVER_CREATE_CONTEXT. |
| [MmMapViewInSessionSpace function](nf-ntddk-mmmapviewinsessionspace.md) | TBD |
| [ExInterlockedExtendZone function](nf-ntddk-exinterlockedextendzone.md) | TBD |
| [CPER_FIELD_CHECK function](nf-ntddk-cper-field-check.md) | TBD |
| [KeGetCurrentProcessorNumberEx function](nf-ntddk-kegetcurrentprocessornumberex.md) | The KeGetCurrentProcessorNumberEx routine gets the processor number of the logical processor that the caller is running on. |
| [RtlLookupElementGenericTable function](nf-ntddk-rtllookupelementgenerictable.md) | The RtlLookupElementGenericTable routine searches a generic table for an element that matches the specified data. |
| [ZwSetTimerEx function](nf-ntddk-zwsettimerex.md) | TBD |
| [IoGetConfigurationInformation function](nf-ntddk-iogetconfigurationinformation.md) | The IoGetConfigurationInformation routine returns a pointer to the I/O manager's global configuration information structure, which contains the current values for how many physical disk, floppy, CD-ROM, tape, SCSI HBA, serial, and parallel devices have device objects created to represent them by drivers as they are loaded. |
| [PsGetHostSilo function](nf-ntddk-psgethostsilo.md) | This routine returns the host silo. |
| [KeEnterCriticalRegion function](nf-ntddk-keentercriticalregion.md) | The KeEnterCriticalRegion routine temporarily disables the execution of normal kernel APCs, but does not prevent special kernel APCs from running. |
| [RtlVolumeDeviceToDosName function](nf-ntddk-rtlvolumedevicetodosname.md) | The RtlVolumeDeviceToDosName routine is obsolete for Windows XP and later versions of Windows. Use IoVolumeDeviceToDosName instead.RtlVolumeDeviceToDosName returns the MS-DOS path for a specified device object that represents a file system volume. |
| [WheaRegisterInUsePageOfflineNotification function](nf-ntddk-whearegisterinusepageofflinenotification.md) | TBD |
| [HalGetBusDataByOffset function](nf-ntddk-halgetbusdatabyoffset.md) | TBD |
| [IoRegisterBootDriverCallback function](nf-ntddk-ioregisterbootdrivercallback.md) | The IoRegisterBootDriverCallback routine registers a BOOT_DRIVER_CALLBACK_FUNCTION routine to be called during the initialization of a boot-start driver and its dependent DLLs. |
| [PsGetParentSilo function](nf-ntddk-psgetparentsilo.md) | Retrieves the most immediate parent silo in the hierarchy for a given job object. |
| [HalAllocateCrashDumpRegisters function](nf-ntddk-halallocatecrashdumpregisters.md) | TBD |
| [WheaUnregisterInUsePageOfflineNotification function](nf-ntddk-wheaunregisterinusepageofflinenotification.md) | TBD |
| [IoClearActivityIdThread function](nf-ntddk-ioclearactivityidthread.md) | The IoClearActivityIdThread routine clears the activity ID of the current thread. |
| [IoGetPagingIoPriority function](nf-ntddk-iogetpagingiopriority.md) | The IoGetPagingIoPriority routine indicates the priority level of a paging I/O request. |
| [KeQueryMaximumProcessorCountEx function](nf-ntddk-kequerymaximumprocessorcountex.md) | The KeQueryMaximumProcessorCountEx routine returns the maximum number of logical processors in a specified group in a multiprocessor system. |
| [MmUnmapViewInSessionSpace function](nf-ntddk-mmunmapviewinsessionspace.md) | TBD |
| [IoSetPartitionInformation function](nf-ntddk-iosetpartitioninformation.md) | The IoSetPartitionInformation routine is obsolete and is provided only to support existing drivers. |
| [PsDereferenceSiloContext function](nf-ntddk-psdereferencesilocontext.md) | This routine decrements the reference count on the object. |
| [RtlSuffixUnicodeString function](nf-ntddk-rtlsuffixunicodestring.md) | TBD |
| [LSAP_SE_ADT_PARAMETER_ARRAY_TRUE_SIZE function](nf-ntddk-lsap-se-adt-parameter-array-true-size.md) | TBD |
| [ExAllocateFromZone function](nf-ntddk-exallocatefromzone.md) | TBD |
| [RtlExpandHashTable function](nf-ntddk-rtlexpandhashtable.md) | TBD |
| [RtlUpperString function](nf-ntddk-rtlupperstring.md) | The RtlUpperString routine copies the given SourceString to the DestinationString buffer, converting it to uppercase. |
| [_ExInterlockedDecrementLong function](nf-ntddk--exinterlockeddecrementlong~r2.md) | TBD |
| [MmGetPhysicalMemoryRanges function](nf-ntddk-mmgetphysicalmemoryranges.md) | TBD |
| [KeGetCurrentProcessorNumber function](nf-ntddk-kegetcurrentprocessornumber.md) | The KeGetCurrentProcessorNumber routine returns the system-assigned number of the current processor on which the caller is running. |
| [IoPropagateActivityIdToThread function](nf-ntddk-iopropagateactivityidtothread.md) | The IoPropagateActivityIdToThread routine associates the activity ID from an IRP with the current thread. |
| [IoSetActivityIdThread function](nf-ntddk-iosetactivityidthread.md) | The IoSetActivityIdThread routine associates an activity ID with the current thread. Drivers should use this routine when they are tracing aware and are issuing I/O on a worker thread. |
| [MmCreateMirror function](nf-ntddk-mmcreatemirror.md) | TBD |
| [RtlRealSuccessor function](nf-ntddk-rtlrealsuccessor.md) | The RtlRealSuccessor routine returns a pointer to the successor of the specified node in the splay link tree. |
| [IoCancelFileOpen function](nf-ntddk-iocancelfileopen.md) | The IoCancelFileOpen routine can be used by a file system filter driver to close a file that has been opened by a file system driver in the filter driver's device stack. |
| [IoWritePartitionTableEx function](nf-ntddk-iowritepartitiontableex.md) | The IoWritePartitionTableEx routine writes partition tables from the entries in the partition list buffer for each partition on the disk represented by the given device object. |
| [PsGetSiloMonitorContextSlot function](nf-ntddk-psgetsilomonitorcontextslot.md) | This routine returns the silo context slot that was allocated by the monitor during the registration. |
| [KeSetImportanceDpc function](nf-ntddk-kesetimportancedpc.md) | The KeSetImportanceDpc routine specifies how soon the DPC routine is run. |
| [RtlEnumerateEntryHashTable function](nf-ntddk-rtlenumerateentryhashtable.md) | TBD |
| [HalGetScatterGatherList function](nf-ntddk-halgetscattergatherlist.md) | TBD |
| [PsGetCurrentThreadTeb function](nf-ntddk-psgetcurrentthreadteb.md) | The PsGetCurrentThreadTeb routine returns the Thread Environment Block (TEB) of the current thread. The call must be made in kernel-mode. |
| [RtlRunOnceComplete function](nf-ntddk-rtlrunoncecomplete.md) | The RtlRunOnceComplete routine completes the one-time initialization began by RtlRunOnceBeginInitialize. |
| [ExRaiseAccessViolation function](nf-ntddk-exraiseaccessviolation.md) | The ExRaiseAccessViolation routine can be used with structured exception handling to throw a driver-determined exception for a memory access violation that occurs when a driver processes I/O requests. |
| [RtlIsRoot function](nf-ntddk-rtlisroot.md) | The RtlIsRoot routine determines whether the specified node is the root node of a splay link tree. |
| [RtlGetConsoleSessionForegroundProcessId function](nf-ntddk-rtlgetconsolesessionforegroundprocessid.md) | TBD |
| [IoClearIrpExtraCreateParameter function](nf-ntddk-ioclearirpextracreateparameter.md) | TBD |
| [RtlCreateHashTable function](nf-ntddk-rtlcreatehashtable.md) | TBD |
| [MmMapViewInSystemSpaceEx function](nf-ntddk-mmmapviewinsystemspaceex.md) | TBD |
| [PsGetThreadId function](nf-ntddk-psgetthreadid.md) | TBD |
| [MmAllocateContiguousMemorySpecifyCache function](nf-ntddk-mmallocatecontiguousmemoryspecifycache.md) | The MmAllocateContiguousMemorySpecifyCache routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space. |
| [HalAllocateAdapterChannel function](nf-ntddk-halallocateadapterchannel.md) | TBD |
| [PsSetLoadImageNotifyRoutine function](nf-ntddk-pssetloadimagenotifyroutine.md) | The PsSetLoadImageNotifyRoutine routine registers a driver-supplied callback that is subsequently notified whenever an image is loaded (or mapped into memory). |
| [RtlInitEnumerationHashTable function](nf-ntddk-rtlinitenumerationhashtable.md) | TBD |
| [RtlEnumerateGenericTable function](nf-ntddk-rtlenumerategenerictable.md) | The RtlEnumerateGenericTable routine is used to enumerate the elements in a generic table. |
| [IoDecrementKeepAliveCount function](nf-ntddk-iodecrementkeepalivecount.md) | The IoDecrementKeepAliveCount routine decrements a reference count associated with an Windows app on a specific device. |
| [DEVICE_TYPE_FROM_CTL_CODE function](nf-ntddk-device-type-from-ctl-code.md) | TBD |
| [HvlUnregisterWheaErrorNotification function](nf-ntddk-hvlunregisterwheaerrornotification.md) | TBD |
| [WheaIsValidErrorRecordSignature function](nf-ntddk-wheaisvaliderrorrecordsignature.md) | The WheaIsValidErrorRecordSignature function verifies whether a WHEA error record is valid. |
| [RtlIsGenericTableEmpty function](nf-ntddk-rtlisgenerictableempty.md) | The RtlIsGenericTableEmpty routine determines if a generic table is empty. |
| [KeInvalidateAllCaches function](nf-ntddk-keinvalidateallcaches.md) | The KeInvalidateAllCaches routine flushes all processor caches. |
| [IoAllocateController function](nf-ntddk-ioallocatecontroller.md) | The IoAllocateController routine sets up the call to a driver-supplied ControllerControl routine as soon as the device controller, represented by the given controller object, is available to carry out an I/O operation for the target device, represented by the given device object. |
| [IoFreeController function](nf-ntddk-iofreecontroller.md) | The IoFreeController routine releases a previously allocated controller object when the driver has completed an I/O request. |
| [RtlInsertEntryHashTable function](nf-ntddk-rtlinsertentryhashtable.md) | TBD |
| [HalBugCheckSystem function](nf-ntddk-halbugchecksystem.md) | TBD |
| [KeEnterGuardedRegion function](nf-ntddk-keenterguardedregion.md) | The KeEnterGuardedRegion routine enters a guarded region, which disables all kernel-mode APC delivery to the current thread. |
| [RtlStronglyEnumerateEntryHashTable function](nf-ntddk-rtlstronglyenumerateentryhashtable.md) | TBD |
| [RtlLookupElementGenericTableFullAvl function](nf-ntddk-rtllookupelementgenerictablefullavl.md) | The RtlLookupElementGenericTableFullAvl routine searches a generic table for an element that matches the specified data. |
| [RtlInsertElementGenericTableFull function](nf-ntddk-rtlinsertelementgenerictablefull.md) | TBD |
| [IoReadDiskSignature function](nf-ntddk-ioreaddisksignature.md) | The IoReadDiskSignature routine reads the disk signature information for the partition table of a disk. |
| [IoTranslateBusAddress function](nf-ntddk-iotranslatebusaddress.md) | TBD |
| [RtlEnumerateGenericTableWithoutSplaying function](nf-ntddk-rtlenumerategenerictablewithoutsplaying.md) | The RtlEnumerateGenericTableWithoutSplaying routine is used to enumerate the elements in a generic table. |
| [IoCreateFileSpecifyDeviceObjectHint function](nf-ntddk-iocreatefilespecifydeviceobjecthint.md) | The IoCreateFileSpecifyDeviceObjectHint routine is used by file system filter drivers to send a create request only to the filters below a specified device object and to the file system. |
| [PsGetCurrentSilo function](nf-ntddk-psgetcurrentsilo.md) | This routine returns the current silo for the calling thread. First the thread is checked to see if it has been attached to a silo. If not, then the thread is checked to see if it is in a silo. |
| [RtlLookupFirstMatchingElementGenericTableAvl function](nf-ntddk-rtllookupfirstmatchingelementgenerictableavl.md) | The RtlLookupFirstMatchingElementGenericTableAvl routine finds the left-most element in the tree that matches the indicated data. |
| [PsGetCurrentThread function](nf-ntddk-psgetcurrentthread.md) | The PsGetCurrentThread routine identifies the current thread. |
| [PshedIsSystemWheaEnabled function](nf-ntddk-pshedissystemwheaenabled.md) | The PshedIsSystemWheaEnabled function returns a Boolean value that indicates whether the system is WHEA-enabled. |
| [RtlUpperChar function](nf-ntddk-rtlupperchar.md) | The RtlUpperChar routine converts the specified character to uppercase. |
| [RtlGetNonVolatileToken function](nf-ntddk-rtlgetnonvolatiletoken.md) | The routine, RtlGetNonVolatileToken, gets various properties about a non-volatile memory buffer and stores them in the variable NvToken. |
| [RtlDeleteElementGenericTableAvlEx function](nf-ntddk-rtldeleteelementgenerictableavlex.md) | TBD |
| [RtlUpcaseUnicodeString function](nf-ntddk-rtlupcaseunicodestring.md) | The RtlUpcaseUnicodeString routine converts a copy of the source string to uppercase and writes the converted string in the destination buffer. |
| [HalSetBusDataByOffset function](nf-ntddk-halsetbusdatabyoffset.md) | TBD |
| [IoRegisterBootDriverReinitialization function](nf-ntddk-ioregisterbootdriverreinitialization.md) | The IoRegisterBootDriverReinitialization routine is called by a boot driver to register the driver's reinitialization routine with the I/O manager to be called after all devices have been enumerated and started. |
| [RtlWalkFrameChain function](nf-ntddk-rtlwalkframechain.md) | TBD |
| [MmRemovePhysicalMemory function](nf-ntddk-mmremovephysicalmemory.md) | TBD |
| [PsInsertSiloContext function](nf-ntddk-psinsertsilocontext.md) | This routine inserts an object in an empty slot in a Silo. |
| [KeExpandKernelStackAndCallout function](nf-ntddk-keexpandkernelstackandcallout.md) | The KeExpandKernelStackAndCallout routine calls a routine with a guaranteed amount of stack space. |
| [RtlInitHashTableContext function](nf-ntddk-rtlinithashtablecontext.md) | TBD |
| [RtlInsertElementGenericTable function](nf-ntddk-rtlinsertelementgenerictable.md) | The RtlInsertElementGenericTable routine adds a new element to a generic table. |
| [IoVolumeDeviceToGuidPath function](nf-ntddk-iovolumedevicetoguidpath.md) | TBD |
| [RtlRemoveEntryHashTable function](nf-ntddk-rtlremoveentryhashtable.md) | TBD |
| [ZwCreateTimer function](nf-ntddk-zwcreatetimer.md) | TBD |
| [RtlInitializeCorrelationVector function](nf-ntddk-rtlinitializecorrelationvector.md) | Initializes the specified correlation vector with the supplied GUID. |
| [IoSetMasterIrpStatus function](nf-ntddk-iosetmasterirpstatus.md) | The IoSetMasterIrpStatus routine conditionally replaces the Status value in an IRP with the specified NTSTATUS value. |
| [MmCopyMemory function](nf-ntddk-mmcopymemory.md) | The MmCopyMemory routine copies the specified range of virtual or physical memory into the caller-supplied buffer. |
| [ZwSetTimer function](nf-ntddk-zwsettimer.md) | TBD |
| [ZwSetInformationThread function](nf-ntddk-zwsetinformationthread.md) | The ZwSetInformationThread routine sets the priority of a thread. |
| [PsSetLoadImageNotifyRoutineEx function](nf-ntddk-pssetloadimagenotifyroutineex.md) | The PsSetLoadImageNotifyRoutineEx routine registers a driver-supplied callback that is subsequently notified whenever an image is loaded (or mapped into memory). |
| [PsUnregisterSiloMonitor function](nf-ntddk-psunregistersilomonitor.md) | This routine unregisters a server silo monitor. |
| [MmUnsecureVirtualMemory function](nf-ntddk-mmunsecurevirtualmemory.md) | The MmUnsecureVirtualMemory routine unsecures a memory address range secured by the MmSecureVirtualMemory routine. |
| [HalGetInterruptVector function](nf-ntddk-halgetinterruptvector.md) | TBD |
| [IoReadPartitionTableEx function](nf-ntddk-ioreadpartitiontableex.md) | The IoReadPartitionTableEx routine reads a list of partitions on a disk having a specified sector size and creates an entry in the partition list for each recognized partition. |
| [PshedRegisterPlugin function](nf-ntddk-pshedregisterplugin.md) | The PshedRegisterPlugin function registers a PSHED plug-in with the PSHED. |
| [RtlInitializeSplayLinks function](nf-ntddk-rtlinitializesplaylinks.md) | The RtlInitializeSplayLinks routine initializes a splay link node. |
| [EX_TEST_CLEAR_BIT function](nf-ntddk-ex-test-clear-bit.md) | TBD |
| [IoRaiseHardError function](nf-ntddk-ioraiseharderror.md) | The IoRaiseHardError routine causes a dialog box to appears that warns the user that a device I/O error has occurred, which might indicate that a physical device is failing. |
| [METHOD_FROM_CTL_CODE function](nf-ntddk-method-from-ctl-code.md) | TBD |
| [MmLockPagableSectionByHandle function](nf-ntddk-mmlockpagablesectionbyhandle.md) | The MmLockPagableSectionByHandle routine locks a pageable code or data section into system memory by incrementing the reference count on the handle to the section. |
| [IoVolumeDeviceNameToGuidPath function](nf-ntddk-iovolumedevicenametoguidpath.md) | TBD |
| [IoGetTransactionParameterBlock function](nf-ntddk-iogettransactionparameterblock.md) | The IoGetTransactionParameterBlock routine returns the transaction parameter block for a transacted file operation. |
| [PsGetProcessStartKey function](nf-ntddk-psgetprocessstartkey.md) | TBD |
| [HalGetBusData function](nf-ntddk-halgetbusdata.md) | TBD |
| [RtlLookupEntryHashTable function](nf-ntddk-rtllookupentryhashtable.md) | TBD |
| [KeQueryNodeMaximumProcessorCount function](nf-ntddk-kequerynodemaximumprocessorcount.md) | The KeQueryNodeMaximumProcessorCount routine returns the maximum number of logical processors that a specified node in a non-uniform memory access (NUMA) multiprocessor system can contain. |
| [ExFreePool function](nf-ntddk-exfreepool.md) | The ExFreePool routine deallocates a block of pool memory. |
| [IoGetActivityIdIrp function](nf-ntddk-iogetactivityidirp.md) | The IoGetActivityIdIrp routine retrieves the current activity ID associated with an IRP. |
| [HalAssignSlotResources function](nf-ntddk-halassignslotresources.md) | TBD |
| [MmAllocateContiguousMemorySpecifyCacheNode function](nf-ntddk-mmallocatecontiguousmemoryspecifycachenode.md) | The MmAllocateContiguousMemorySpecifyCacheNode routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space. |
| [IoSetPartitionInformationEx function](nf-ntddk-iosetpartitioninformationex.md) | For the disk represented by DeviceObject, the IoSetPartitionInformationEx routine initializes a partition table entry with the information specified in the SET_PARTITION_INFORMATION_EX structure. |
| [RtlDelete function](nf-ntddk-rtldelete.md) | The RtlDelete routine deletes the specified node from the splay link tree. |
| [PsStartSiloMonitor function](nf-ntddk-psstartsilomonitor.md) | This routine tries to start the server silo monitor. |
| [RtlInsertAsRightChild function](nf-ntddk-rtlinsertasrightchild.md) | The RtlInsertAsRightChild routine inserts a given splay link into the tree as the right child of a given node in that tree. |
| [HASH_ENTRY_KEY function](nf-ntddk-hash-entry-key.md) | TBD |
| [ZwTerminateProcess function](nf-ntddk-zwterminateprocess.md) | The ZwTerminateProcess routine terminates a process and all of its threads. |
| [RtlFlushNonVolatileMemoryRanges function](nf-ntddk-rtlflushnonvolatilememoryranges.md) | The routine RtlFlushNonVolatileMemoryRanges optimally flushes the given non-volatile memory regions. |
| [RtlLeftChild function](nf-ntddk-rtlleftchild.md) | The RtlLeftChild routine returns a pointer to the left child of the specified splay link node. |
| [PsRemoveLoadImageNotifyRoutine function](nf-ntddk-psremoveloadimagenotifyroutine.md) | The PsRemoveLoadImageNotifyRoutine routine removes a callback routine that was registered by the PsSetLoadImageNotifyRoutine routine. |
| [MmIsThisAnNtAsSystem function](nf-ntddk-mmisthisanntassystem.md) | The MmIsThisAnNtAsSystem routine is obsolete for Windows XP and later versions of Windows. Use RtlGetVersion or RtlVerifyVersionInfo instead. |
| [IoGetActivityIdThread function](nf-ntddk-iogetactivityidthread.md) | The IoGetActivityIdThread routine returns the activity ID associated with the current thread. |
| [PsFreeSiloContextSlot function](nf-ntddk-psfreesilocontextslot.md) | This routine frees the specified slot and makes it available in the system. It undoes the effects of the PsAllocSiloContextSlot routine. |
| [IoGetFileObjectGenericMapping function](nf-ntddk-iogetfileobjectgenericmapping.md) | The IoGetFileObjectGenericMapping routine returns information about the mapping between each generic access right and the set of specific access rights for file objects. |
| [IoGetFsZeroingOffset function](nf-ntddk-iogetfszeroingoffset.md) | TBD |
| [MmIsNonPagedSystemAddressValid function](nf-ntddk-mmisnonpagedsystemaddressvalid.md) | TBD |
| [PsMakeSiloContextPermanent function](nf-ntddk-psmakesilocontextpermanent.md) | This routine makes the slot in a silo instance read-only, allowing the object in the slot to be retrieved without affecting the reference count on that object. |
| [ZwQueryVolumeInformationFile function](nf-ntddk-zwqueryvolumeinformationfile.md) | TBD |
| [KeShouldYieldProcessor function](nf-ntddk-keshouldyieldprocessor.md) | TBD |
| [KeGetPcr function](nf-ntddk-kegetpcr~r2.md) | TBD |
| [KeQueryTickCount function](nf-ntddk-kequerytickcount~r1.md) | The KeQueryTickCount routine maintains a count of the interval timer interrupts that have occurred since the system was booted. |
| [PsReferenceSiloContext function](nf-ntddk-psreferencesilocontext.md) | This routine increments the reference count on the object. |
| [PsGetProcessId function](nf-ntddk-psgetprocessid.md) | The PsGetProcessId routine returns the process identifier (process ID) that is associated with a specified process. |
| [IoVolumeDeviceNameToGuid function](nf-ntddk-iovolumedevicenametoguid.md) | TBD |
| [RtlDeleteElementGenericTableAvl function](nf-ntddk-rtldeleteelementgenerictableavl.md) | The RtlDeleteElementGenericTableAvl routine deletes an element from a generic table. |
| [RtlRunOnceBeginInitialize function](nf-ntddk-rtlrunoncebegininitialize.md) | The RtlRunOnceBeginInitialize routine begins a one-time initialization. |
| [ExInterlockedDecrementLong function](nf-ntddk-exinterlockeddecrementlong.md) | TBD |
| [PsGetPermanentSiloContext function](nf-ntddk-psgetpermanentsilocontext.md) | This routine retrieves an object that was inserted in the Silo without incrementing the reference count. |
| [RtlExtendCorrelationVector function](nf-ntddk-rtlextendcorrelationvector.md) | This routine extends the supplied correlation vector. For a correlation vector of the form X.i, the extended value is X.i.0. |
| [IoMakeAssociatedIrp function](nf-ntddk-iomakeassociatedirp.md) | This routine is reserved for use by file systems and file system filter drivers. |
| [ZwAllocateLocallyUniqueId function](nf-ntddk-zwallocatelocallyuniqueid.md) | The ZwAllocateLocallyUniqueId routine allocates a locally unique identifier (LUID). |
| [HalBugCheckSystem function](nf-ntddk-halbugchecksystem~r1.md) | TBD |
| [IoCreateController function](nf-ntddk-iocreatecontroller.md) | The IoCreateController routine allocates memory for and initializes a controller object with a controller extension of a driver-determined size. |
| [KeAreApcsDisabled function](nf-ntddk-keareapcsdisabled.md) | The KeAreApcsDisabled routine returns whether the calling thread is within a critical region or a guarded region, which disables normal kernel APC delivery. |
| [EX_TEST_SET_BIT function](nf-ntddk-ex-test-set-bit.md) | TBD |
| [MmRotatePhysicalView function](nf-ntddk-mmrotatephysicalview.md) | TBD |
| [IoQueryInformationByName function](nf-ntddk-ioqueryinformationbyname.md) | TBD |
| [KeRaiseIrqlToSynchLevel function](nf-ntddk-keraiseirqltosynchlevel~r1.md) | TBD |
| [MmFreeContiguousMemorySpecifyCache function](nf-ntddk-mmfreecontiguousmemoryspecifycache.md) | The MmFreeContiguousMemorySpecifyCache routine frees a buffer that was allocated by an MmAllocateContiguousMemorySpecifyCacheXxx routine. |
| [KeSetBasePriorityThread function](nf-ntddk-kesetbaseprioritythread.md) | The KeSetBasePriorityThread routine sets the run-time priority, relative to the current process, for a given thread. |
| [MmGetVirtualForPhysical function](nf-ntddk-mmgetvirtualforphysical.md) | TBD |
| [IoGetOplockKeyContextEx function](nf-ntddk-iogetoplockkeycontextex.md) | The IoGetOplockKeyContextEx routine returns a parent and target oplock key context for a file object. |
| [KeQueryMaximumGroupCount function](nf-ntddk-kequerymaximumgroupcount.md) | The KeQueryMaximumGroupCount routine returns the maximum number of groups in a multiprocessor system. |
| [RtlWriteNonVolatileMemory function](nf-ntddk-rtlwritenonvolatilememory.md) | The routine RtlWriteNonVolatileMemory copies the contents of a source buffer to a non-volatile destination memory buffer. |
| [RtlLargeIntegerDivide function](nf-ntddk-rtllargeintegerdivide~r1.md) | TBD |
| [IoRegisterDriverReinitialization function](nf-ntddk-ioregisterdriverreinitialization.md) | The IoRegisterDriverReinitialization routine is called by a driver during its initialization or reinitialization to register its Reinitialize routine to be called again before the driver's and, possibly the system's, initialization is complete. |
| [MmMapViewInSystemSpace function](nf-ntddk-mmmapviewinsystemspace.md) | TBD |
| [RtlGetCallersAddress function](nf-ntddk-rtlgetcallersaddress.md) | TBD |
| [IoVolumeDeviceToDosName function](nf-ntddk-iovolumedevicetodosname.md) | The IoVolumeDeviceToDosName routine returns the MS-DOS path for a specified device object that represents a file system volume. |
| [WheaGetErrPacketFromErrRecord function](nf-ntddk-wheageterrpacketfromerrrecord.md) | The WheaGetErrPacketFromErrRecord function returns a pointer to the hardware error packet that is contained within a WHEA error record. The hardware error packet is formatted as a WHEA_ERROR_PACKET structure. |
| [_ExInterlockedExchangeUlong function](nf-ntddk--exinterlockedexchangeulong~r2.md) | TBD |
| [RtlGetEnabledExtendedFeatures function](nf-ntddk-rtlgetenabledextendedfeatures.md) | The RtlGetEnabledExtendedFeatures routine returns a mask of extended processor features that are enabled by the system. |
| [IoWritePartitionTable function](nf-ntddk-iowritepartitiontable.md) | The IoWritePartitionTable routine is obsolete and is provided only to support existing drivers. |
| [IoTransferActivityId function](nf-ntddk-iotransferactivityid.md) | The IoTransferActivityId routine logs an ETW transfer event using the I/O tracing provider on behalf of the caller. This allows a driver to associate two related activity IDs without requiring a specific provider to be enabled. |
| [KeQueryGroupAffinity function](nf-ntddk-kequerygroupaffinity.md) | The KeQueryGroupAffinity routine returns an affinity mask that identifies the active logical processors in a specified group in a multiprocessor system. |
| [HalMakeBeep function](nf-ntddk-halmakebeep.md) | TBD |
| [IoReportResourceForDetection function](nf-ntddk-ioreportresourcefordetection.md) | The IoReportResourceForDetection routine claims hardware resources in the configuration registry for a legacy device. |
| [_ExInterlockedExchangeUlong function](nf-ntddk--exinterlockedexchangeulong~r1.md) | TBD |
| [RtlIsRightChild function](nf-ntddk-rtlisrightchild.md) | The RtlIsRightChild routine determines whether a given splay link is the right child of a node in a splay link tree. |
| [KeQueryActiveGroupCount function](nf-ntddk-kequeryactivegroupcount.md) | The KeQueryActiveGroupCount routine returns the number of active processor groups in a multiprocessor system. |
| [IoReportRootDevice function](nf-ntddk-ioreportrootdevice.md) | The IoReportRootDevice routine reports a device that cannot be detected by a PnP bus driver to the PnP Manager. IoReportRootDevice allows only one device per driver to be created. |
| [MmAllocateNonCachedMemory function](nf-ntddk-mmallocatenoncachedmemory.md) | The MmAllocateNonCachedMemory routine allocates a virtual address range of noncached and cache-aligned memory. |
| [IoUnregisterBootDriverCallback function](nf-ntddk-iounregisterbootdrivercallback.md) | The IoUnRegisterBootDriverCallback routine unregisters a previously registered BOOT_DRIVER_CALLBACK_FUNCTION routine. |
| [IoSetFsZeroingOffsetRequired function](nf-ntddk-iosetfszeroingoffsetrequired.md) | TBD |
| [RtlInitializeGenericTableAvl function](nf-ntddk-rtlinitializegenerictableavl.md) | The RtlInitializeGenericTableAvl routine initializes a generic table using Adelson-Velsky/Landis (AVL) trees. |
| [RtlReleaseHashTableContext function](nf-ntddk-rtlreleasehashtablecontext.md) | TBD |
| [PreFetchCacheLine function](nf-ntddk-prefetchcacheline.md) | TBD |
| [RtlInitStrongEnumerationHashTable function](nf-ntddk-rtlinitstrongenumerationhashtable.md) | TBD |
| [RtlIsUntrustedObject function](nf-ntddk-rtlisuntrustedobject.md) | TBD |
| [_ExInterlockedDecrementLong function](nf-ntddk--exinterlockeddecrementlong.md) | TBD |
| [ExInterlockedExchangeUlong function](nf-ntddk-exinterlockedexchangeulong.md) | TBD |
| [IoIsFileOriginRemote function](nf-ntddk-ioisfileoriginremote.md) | The IoIsFileOriginRemote routine determines whether a given file object is for a remote create request. |
| [TraceLoggingCORRELATION_VECTOR function](nf-ntddk-traceloggingcorrelation-vector.md) | TBD |
| [RtlEnumerateGenericTableLikeADirectory function](nf-ntddk-rtlenumerategenerictablelikeadirectory.md) | The RtlEnumerateGenericTableLikeADirectory routine returns the elements of a generic table, one-by-one, in collation order. |
| [HalPutScatterGatherList function](nf-ntddk-halputscattergatherlist.md) | TBD |
| [IoDeleteController function](nf-ntddk-iodeletecontroller.md) | The IoDeleteController routine removes a given controller object from the system, for example, when the driver that created it is being unloaded. |
| [MmGetPhysicalMemoryRangesEx function](nf-ntddk-mmgetphysicalmemoryrangesex.md) | TBD |
| [RtlCopyString function](nf-ntddk-rtlcopystring.md) | The RtlCopyString routine copies a source string to a destination string. |
| [RtlNumberGenericTableElementsAvl function](nf-ntddk-rtlnumbergenerictableelementsavl.md) | The RtlNumberGenericTableElementsAvl routine returns the number of elements in a generic table. |
| [ExExtendZone function](nf-ntddk-exextendzone.md) | TBD |
| [DbgPrompt function](nf-ntddk-dbgprompt.md) | The DbgPrompt routine displays a caller-specified user prompt string on the kernel debugger's display device and obtains a user response string. |
| [RtlParent function](nf-ntddk-rtlparent.md) | The RtlParent routine returns a pointer to the parent of the specified node in a splay link tree. |
| [PsDetachSiloFromCurrentThread function](nf-ntddk-psdetachsilofromcurrentthread.md) | This routine removes a thread from a silo which was added by an attach. For more info about attaching, see the PsAttachSiloToCurrentThread routine. |
| [RtlEndWeakEnumerationHashTable function](nf-ntddk-rtlendweakenumerationhashtable.md) | TBD |
| [KeQueryHighestNodeNumber function](nf-ntddk-kequeryhighestnodenumber.md) | The KeQueryHighestNodeNumber routine returns the highest node number in a multiprocessor system that has a non-uniform memory access (NUMA) architecture. |
| [KeQueryNodeActiveAffinity function](nf-ntddk-kequerynodeactiveaffinity.md) | The KeQueryNodeActiveAffinity routine gets the current processor affinity of a specified node in a multiprocessor system that has a non-uniform memory access (NUMA) architecture. |
| [KeRaiseIrqlToSynchLevel function](nf-ntddk-keraiseirqltosynchlevel~r3.md) | TBD |
| [Exfi386InterlockedIncrementLong function](nf-ntddk-exfi386interlockedincrementlong.md) | TBD |
| [PsGetServerSiloActiveConsoleId function](nf-ntddk-psgetserversiloactiveconsoleid.md) | Gets the active console for the current server silo context for the supplied thread. |
| [ZwOpenProcess function](nf-ntddk-zwopenprocess.md) | The ZwOpenProcess routine opens a handle to a process object and sets the access rights to this object. |
| [IoReportDetectedDevice function](nf-ntddk-ioreportdetecteddevice.md) | The IoReportDetectedDevice routine reports a non-PnP device to the PnP manager. |
| [CTL_CODE function](nf-ntddk-ctl-code.md) | TBD |
| [RtlPrefixUnicodeString function](nf-ntddk-rtlprefixunicodestring.md) | The RtlPrefixUnicodeString routine compares two Unicode strings to determine whether one string is a prefix of the other. |
| [KeQueryActiveProcessorCountEx function](nf-ntddk-kequeryactiveprocessorcountex.md) | The KeQueryActiveProcessorCountEx routine returns the number of active logical processors in a specified group in a multiprocessor system or in the entire system. |
| [RtlCompareString function](nf-ntddk-rtlcomparestring.md) | The RtlCompareString routine compares two counted strings. |
| [KeGetCurrentProcessorNumber function](nf-ntddk-kegetcurrentprocessornumber~r2.md) | The KeGetCurrentProcessorNumber routine returns the system-assigned number of the current processor on which the caller is running. |
| [RtlInsertAsLeftChild function](nf-ntddk-rtlinsertasleftchild.md) | The RtlInsertAsLeftChild routine inserts a splay link node into the tree as the left child of the specified node. |
| [HalTranslateBusAddress function](nf-ntddk-haltranslatebusaddress.md) | TBD |
| [KeBugCheck function](nf-ntddk-kebugcheck.md) | The KeBugCheck routine brings down the system in a controlled manner when the caller discovers an unrecoverable inconsistency that would corrupt the system if the caller continued to run. |
| [IoIncrementKeepAliveCount function](nf-ntddk-ioincrementkeepalivecount.md) | The IoIncrementKeepAliveCount routine increments a reference count associated with an Windows app process on a specific device. |
| [IoAttachDeviceToDeviceStackSafe function](nf-ntddk-ioattachdevicetodevicestacksafe.md) | The IoAttachDeviceToDeviceStackSafe routine attaches the caller's device object to the topmost device object in a driver stack. |
| [PsGetProcessCreateTimeQuadPart function](nf-ntddk-psgetprocesscreatetimequadpart.md) | The PsGetProcessCreateTimeQuadPart routine returns a LONGLONG value that represents the time at which the process was created. |
| [HalAcquireDisplayOwnership function](nf-ntddk-halacquiredisplayownership.md) | TBD |
| [RtlTotalBucketsHashTable function](nf-ntddk-rtltotalbucketshashtable.md) | TBD |
| [RtlNonEmptyBucketsHashTable function](nf-ntddk-rtlnonemptybucketshashtable.md) | TBD |
| [KeRaiseIrqlToDpcLevel function](nf-ntddk-keraiseirqltodpclevel~r1.md) | The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [PsIsHostSilo function](nf-ntddk-psishostsilo.md) | This routine will check if the supplied Silo is the host silo. |
| [RtlRealPredecessor function](nf-ntddk-rtlrealpredecessor.md) | The RtlRealPredecessor routine returns a pointer to the predecessor of the specified node in the splay link tree. |
| [PsAcquireSiloHardReference function](nf-ntddk-psacquiresilohardreference.md) | TBD |
| [IoSetHardErrorOrVerifyDevice function](nf-ntddk-iosetharderrororverifydevice.md) | Lower-level drivers call the IoSetHardErrorOrVerifyDevice routine to identify a removable media device that has encountered an error, so that a file system driver can prompt the user to verify that the medium is valid. |
| [RtlContractHashTable function](nf-ntddk-rtlcontracthashtable.md) | TBD |
| [IoGetInitiatorProcess function](nf-ntddk-iogetinitiatorprocess.md) | The IoGetInitiatorProcess routine retrieves the process which initiated the creation of a file object if different than the process which is issuing the create. |
| [EX_INIT_BITS function](nf-ntddk-ex-init-bits.md) | TBD |
| [PsSetCreateThreadNotifyRoutine function](nf-ntddk-pssetcreatethreadnotifyroutine.md) | The PsSetCreateThreadNotifyRoutine routine registers a driver-supplied callback that is subsequently notified when a new thread is created and when such a thread is deleted. |
| [KeRaiseIrqlToDpcLevel function](nf-ntddk-keraiseirqltodpclevel~r3.md) | The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [IoQueryFullDriverPath function](nf-ntddk-ioqueryfulldriverpath.md) | The IoQueryFullDriverPath routine retrieves the full path name of the binary file that is loaded for the specified driver object. |
| [__readpmc function](nf-ntddk---readpmc.md) | TBD |
| [RtlDeleteHashTable function](nf-ntddk-rtldeletehashtable.md) | TBD |
| [PsRemoveSiloContext function](nf-ntddk-psremovesilocontext.md) | This routine removes an object that was inserted in the Silo. |
| [PsIsCurrentThreadPrefetching function](nf-ntddk-psiscurrentthreadprefetching.md) | TBD |
| [RtlDrainNonVolatileFlush function](nf-ntddk-rtldrainnonvolatileflush.md) | The routine RtlDrainNonVolatileFlush waits for the flushes initiated by RtlFlushNonVolatileMemory to finish. |
| [RtlGetActiveConsoleId function](nf-ntddk-rtlgetactiveconsoleid.md) | TBD |
| [RtlIsLeftChild function](nf-ntddk-rtlisleftchild.md) | The RtlIsLeftChild routine determines whether a given splay link is the left child of a node in a splay link tree. |
| [FsRtlIsChecksumError function](nf-ntddk-fsrtlischecksumerror.md) | TBD |
| [KeGetPcr function](nf-ntddk-kegetpcr~r1.md) | TBD |
| [ZwCancelTimer function](nf-ntddk-zwcanceltimer.md) | TBD |
| [PshedAllocateMemory function](nf-ntddk-pshedallocatememory.md) | The PshedAllocateMemory function allocates a block of memory from the nonpaged pool. |
| [PsGetCurrentServerSilo function](nf-ntddk-psgetcurrentserversilo.md) | This routine returns the effective server silo for the thread. |
| [PsGetCurrentServerSiloName function](nf-ntddk-psgetcurrentserversiloname.md) | TBD |
| [IoGetSiloParameters function](nf-ntddk-iogetsiloparameters.md) | This routine indicates if a file is within a Container context. |
| [PsGetJobSilo function](nf-ntddk-psgetjobsilo.md) | This routine returns the first job in the hierarchy that is a Silo. The returned pointer is valid as long as the supplied Job object remains referenced. |
| [ExInterlockedFreeToZone function](nf-ntddk-exinterlockedfreetozone.md) | TBD |
| [PsTerminateServerSilo function](nf-ntddk-psterminateserversilo.md) | This routine terminates the specified silo. |
| [RtlGetProductInfo function](nf-ntddk-rtlgetproductinfo.md) | TBD |
| [IoSetFileOrigin function](nf-ntddk-iosetfileorigin.md) | The IoSetFileOrigin routine specifies whether a given file object is for a remote create request. |
| [RtlCharToInteger function](nf-ntddk-rtlchartointeger.md) | The RtlCharToInteger routine converts a single-byte character string to an integer value in the specified base. |
| [PsGetEffectiveServerSilo function](nf-ntddk-psgeteffectiveserversilo.md) | This routine traverses the parent chain of the Silo until finding the effective server silo or host silo. |
| [Exfi386InterlockedExchangeUlong function](nf-ntddk-exfi386interlockedexchangeulong.md) | TBD |
| [IoSetFileObjectIgnoreSharing function](nf-ntddk-iosetfileobjectignoresharing.md) | The IoSetFileObjectIgnoreSharing routine sets a file object to ignore file sharing access checks. |
| [KeGetCurrentProcessorNumber function](nf-ntddk-kegetcurrentprocessornumber~r3.md) | The KeGetCurrentProcessorNumber routine returns the system-assigned number of the current processor on which the caller is running. |
| [KeRaiseIrqlToDpcLevel function](nf-ntddk-keraiseirqltodpclevel~r2.md) | The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [SeSinglePrivilegeCheck function](nf-ntddk-sesingleprivilegecheck.md) | The SeSinglePrivilegeCheck routine checks for the passed privilege value in the context of the current thread. |
| [RtlLookupElementGenericTableAvl function](nf-ntddk-rtllookupelementgenerictableavl.md) | The RtlLookupElementGenericTableAvl routine searches a generic table for an element that matches the specified data. |
| [HalDmaAllocateCrashDumpRegistersEx function](nf-ntddk-haldmaallocatecrashdumpregistersex.md) | TBD |
| [PsGetCurrentProcessId function](nf-ntddk-psgetcurrentprocessid.md) | The PsGetCurrentProcessId routine identifies the current thread's process. |
| [RtlEndStrongEnumerationHashTable function](nf-ntddk-rtlendstrongenumerationhashtable.md) | TBD |
| [KeSetTargetProcessorDpc function](nf-ntddk-kesettargetprocessordpc.md) | The KeSetTargetProcessorDpc routine specifies the processor that a DPC routine will be run on. |
| [RtlCreateHashTableEx function](nf-ntddk-rtlcreatehashtableex.md) | TBD |
| [__rdtsc function](nf-ntddk---rdtsc.md) | TBD |
| [MmGetPhysicalAddress function](nf-ntddk-mmgetphysicaladdress.md) | The MmGetPhysicalAddress routine returns the physical address corresponding to a valid nonpaged virtual address. |
| [ZwOpenTimer function](nf-ntddk-zwopentimer.md) | TBD |
| [HalPutDmaAdapter function](nf-ntddk-halputdmaadapter.md) | TBD |
| [KeQueryMaximumProcessorCount function](nf-ntddk-kequerymaximumprocessorcount.md) | The KeQueryMaximumProcessorCount routine returns the maximum number of processors. |
| [KeSetHardwareCounterConfiguration function](nf-ntddk-kesethardwarecounterconfiguration.md) | The KeSetHardwareCounterConfiguration routine specifies a list of hardware counters to use for thread profiling. |
| [RtlActiveEnumeratorsHashTable function](nf-ntddk-rtlactiveenumeratorshashtable.md) | TBD |
| [PsSetCurrentThreadPrefetching function](nf-ntddk-pssetcurrentthreadprefetching.md) | TBD |
| [HalSetBusData function](nf-ntddk-halsetbusdata.md) | TBD |
| [IoCreateFileEx function](nf-ntddk-iocreatefileex.md) | The IoCreateFileEx routine either causes a new file or directory to be created, or opens an existing file, device, directory, or volume and gives the caller a handle for the file object. |
| [RtlFreeNonVolatileToken function](nf-ntddk-rtlfreenonvolatiletoken.md) | The routine RtlFreeNonVolatileToken is a cleanup function for the opaque NvToken which is given by a successful call to RtlGetNonVolatileToken. |
| [_ExInterlockedExchangeUlong function](nf-ntddk--exinterlockedexchangeulong.md) | TBD |
| [PsGetServerSiloServiceSessionId function](nf-ntddk-psgetserversiloservicesessionid.md) | TBD |
| [IoFreeMapRegisters function](nf-ntddk-iofreemapregisters.md) | TBD |
| [RtlInitWeakEnumerationHashTable function](nf-ntddk-rtlinitweakenumerationhashtable.md) | TBD |
| [_ExInterlockedIncrementLong function](nf-ntddk--exinterlockedincrementlong~r2.md) | TBD |
| [HalAllocateCommonBuffer function](nf-ntddk-halallocatecommonbuffer.md) | TBD |
| [IoAssignArcName function](nf-ntddk-ioassignarcname.md) | The IoAssignArcName routine creates a symbolic link between the ARC name of a physical device and the name of the corresponding device object when it has been created. |
| [IoRaiseInformationalHardError function](nf-ntddk-ioraiseinformationalharderror.md) | The IoRaiseInformationalHardError routine sends a dialog box to the user, warning about a device I/O error that indicates why a user I/O request failed. |
| [PsGetJobServerSilo function](nf-ntddk-psgetjobserversilo.md) | This routine returns the effective ServerSilo for the job. The returned pointer is valid as long as the supplied Job object remains referenced. |
| [PshedFreeMemory function](nf-ntddk-pshedfreememory.md) | The PshedFreeMemory function frees a block of memory that was previously allocated by calling the PshedAllocateMemory function. |
| [MmFreeNonCachedMemory function](nf-ntddk-mmfreenoncachedmemory.md) | The MmFreeNonCachedMemory routine releases a range of noncached memory that was allocated by the MmAllocateNonCachedMemory routine. |
| [PsCreateSiloContext function](nf-ntddk-pscreatesilocontext.md) | This routine creates an object that will be inserted in a Silo. |
| [RtlGetElementGenericTableAvl function](nf-ntddk-rtlgetelementgenerictableavl.md) | The RtlGetElementGenericTableAvl routine returns a pointer to the caller-supplied data for a particular generic Adelson-Velsky/Landis (AVL) table element. |
| [RtlIsMultiSessionSku function](nf-ntddk-rtlismultisessionsku.md) | TBD |
| [KeQueryTickCount function](nf-ntddk-kequerytickcount~r2.md) | The KeQueryTickCount routine maintains a count of the interval timer interrupts that have occurred since the system was booted. |
| [PsGetProcessExitStatus function](nf-ntddk-psgetprocessexitstatus.md) | TBD |
| [IoGetSilo function](nf-ntddk-iogetsilo.md) | TBD |
| [PsReleaseSiloHardReference function](nf-ntddk-psreleasesilohardreference.md) | TBD |
| [RtlGetNtProductType function](nf-ntddk-rtlgetntproducttype.md) | TBD |
| [RtlEqualString function](nf-ntddk-rtlequalstring.md) | The RtlEqualString routine compares two counted strings to determine whether they are equal. |
| [IoMakeAssociatedIrpEx function](nf-ntddk-iomakeassociatedirpex.md) | TBD |
| [IoReadPartitionTable function](nf-ntddk-ioreadpartitiontable.md) | The IoReadPartitionTable routine is obsolete and is provided only to support existing drivers. |
| [PshedSynchronizeExecution function](nf-ntddk-pshedsynchronizeexecution.md) | The PshedSynchronizeExecution function synchronizes the execution of a given function with the hardware error processing for an error source. |
| [IoQueryDeviceDescription function](nf-ntddk-ioquerydevicedescription.md) | TBD |
| [RtlEndEnumerationHashTable function](nf-ntddk-rtlendenumerationhashtable.md) | TBD |
| [RtlFlushNonVolatileMemory function](nf-ntddk-rtlflushnonvolatilememory.md) | The routine RtlFlushNonVolatileMemory optimally flushes the given non-volatile memory region. |
| [RtlSubtreeSuccessor function](nf-ntddk-rtlsubtreesuccessor.md) | The RtlSubtreeSuccessor routine returns a pointer to the successor of the specified node within the subtree that is rooted at that node. |
| [ZwDisplayString function](nf-ntddk-zwdisplaystring.md) | TBD |
| [RtlIsZeroLuid function](nf-ntddk-rtliszeroluid.md) | TBD |
| [WheaFindNextErrorRecordSection function](nf-ntddk-wheafindnexterrorrecordsection.md) | The WheaFindNextErrorRecordSection function allows a caller to iteratively examine the WHEA error record sections within a WHEA error record. Each error record section is formatted as a WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure. |
| [RtlDeleteElementGenericTable function](nf-ntddk-rtldeleteelementgenerictable.md) | The RtlDeleteElementGenericTable routine deletes an element from a generic table. |
| [KeRaiseIrqlToSynchLevel function](nf-ntddk-keraiseirqltosynchlevel~r2.md) | TBD |
| [HalGetAdapter function](nf-ntddk-halgetadapter.md) | TBD |
| [MmUnmapVideoDisplay function](nf-ntddk-mmunmapvideodisplay.md) | TBD |
| [RtlInsertElementGenericTableFullAvl function](nf-ntddk-rtlinsertelementgenerictablefullavl.md) | The RtlInsertElementGenericTableFullAvl routine adds a new entry to a generic table. |
| [RtlWeaklyEnumerateEntryHashTable function](nf-ntddk-rtlweaklyenumerateentryhashtable.md) | TBD |
| [IoSetSystemPartition function](nf-ntddk-iosetsystempartition.md) | The IoSetSystemPartition routine sets the boot partition for the system. |
| [ExIsFullZone function](nf-ntddk-exisfullzone.md) | TBD |
| [PsRegisterSiloMonitor function](nf-ntddk-psregistersilomonitor.md) | This routine registers a server silo monitor that can receive notifications about server silo events. |
| [MemoryBarrier function](nf-ntddk-memorybarrier.md) | TBD |
| [PsReplaceSiloContext function](nf-ntddk-psreplacesilocontext.md) | This routine inserts an object in a Silo. |
| [PsGetThreadProperty function](nf-ntddk-psgetthreadproperty.md) | TBD |
| [MmGetCacheAttribute function](nf-ntddk-mmgetcacheattribute.md) | TBD |
| [IoDeassignArcName function](nf-ntddk-iodeassignarcname.md) | The IoDeassignArcName routine removes a symbolic link between the ARC name for a device and the named device object. |
| [PsIsCurrentThreadInServerSilo function](nf-ntddk-psiscurrentthreadinserversilo.md) | TBD |
| [MmSecureVirtualMemory function](nf-ntddk-mmsecurevirtualmemory.md) | The MmSecureVirtualMemory routine secures a user-space memory address range so that it cannot be freed and its protection type cannot be made more restrictive. |
| [RtlGetNtSystemRoot function](nf-ntddk-rtlgetntsystemroot.md) | TBD |
| [HalFreeCommonBuffer function](nf-ntddk-halfreecommonbuffer.md) | TBD |
| [MmFreeContiguousMemory function](nf-ntddk-mmfreecontiguousmemory.md) | The MmFreeContiguousMemory routine releases a range of physically contiguous memory that was allocated by an MmAllocateContiguousMemoryXxx routine. |
| [ReadForWriteAccess function](nf-ntddk-readforwriteaccess.md) | TBD |
| [RtlIsGenericTableEmptyAvl function](nf-ntddk-rtlisgenerictableemptyavl.md) | The RtlIsGenericTableEmptyAvl routine determines if a generic table is empty. |
| [RtlEnumerateGenericTableWithoutSplayingAvl function](nf-ntddk-rtlenumerategenerictablewithoutsplayingavl.md) | The RtlEnumerateGenericTableWithoutSplayingAvl routine is used to enumerate the elements in a generic table. |
| [RtlGetElementGenericTable function](nf-ntddk-rtlgetelementgenerictable.md) | The RtlGetElementGenericTable routine returns a pointer to the caller-supplied data for a particular generic table element. |
| [RtlEmptyBucketsHashTable function](nf-ntddk-rtlemptybucketshashtable.md) | TBD |
| [_ExInterlockedIncrementLong function](nf-ntddk--exinterlockedincrementlong.md) | TBD |
| [IoSetIrpExtraCreateParameter function](nf-ntddk-iosetirpextracreateparameter.md) | TBD |
| [IoIsValidIrpStatus function](nf-ntddk-ioisvalidirpstatus.md) | The IoIsValidIrpStatus routine validates the specified NTSTATUS status code value. |
| [RtlValidateCorrelationVector function](nf-ntddk-rtlvalidatecorrelationvector.md) | Validates the specified correlation vector to check whether it conforms to the Correlation Vector Specification (v2). |
| [KeInvalidateRangeAllCaches function](nf-ntddk-keinvalidaterangeallcaches.md) | TBD |
| [PsGetSiloContext function](nf-ntddk-psgetsilocontext.md) | This routine retrieves the silo context from the specified silo and slot. |
| [RtlInsertElementGenericTableAvl function](nf-ntddk-rtlinsertelementgenerictableavl.md) | The RtlInsertElementGenericTableAvl routine adds a new entry to a generic table. |
| [KeRaiseIrqlToDpcLevel function](nf-ntddk-keraiseirqltodpclevel.md) | The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [RtlConvertLongToLuid function](nf-ntddk-rtlconvertlongtoluid.md) | The RtlConvertLongToLuid routine converts a long integer to a locally unique identifier (LUID), which is used by the system to represent a security privilege. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [PCI_EXPRESS_LINK_STATUS_REGISTER structure](ns-ntddk--pci-express-link-status-register.md) | The PCI_EXPRESS_LINK_STATUS_REGISTER structure describes a PCI Express (PCIe) link status register of a PCIe capability structure. |
| [WHEA_AER_BRIDGE_DESCRIPTOR structure](ns-ntddk--whea-aer-bridge-descriptor.md) | The WHEA_AER_BRIDGE_DESCRIPTOR structure describes a PCI Express (PCIe) bridge error source. |
| [AER_BRIDGE_DESCRIPTOR_FLAGS structure](ns-ntddk--aer-bridge-descriptor-flags.md) | TBD |
| [WHEA_REVISION structure](ns-ntddk--whea-revision.md) | The WHEA_REVISION union describes the revision of the error record data structures. |
| [PCI_EXPRESS_TPH_REQUESTER_CONTROL_REGISTER structure](ns-ntddk--pci-express-tph-requester-control-register.md) | TBD |
| [AER_ENDPOINT_DESCRIPTOR_FLAGS structure](ns-ntddk--aer-endpoint-descriptor-flags.md) | TBD |
| [WHEA_PCI_SLOT_NUMBER structure](ns-ntddk--whea-pci-slot-number.md) | The WHEA_PCI_SLOT_NUMBER structure describes a logical PCI slot. |
| [PCI_EXPRESS_L1_PM_SS_CAPABILITY structure](ns-ntddk--pci-express-l1-pm-ss-capability.md) | TBD |
| [DUMMYUNIONNAME structure](ns-ntddk-dummyunionname.md) | TBD |
| [PCI_EXPRESS_DEVICE_STATUS_REGISTER structure](ns-ntddk--pci-express-device-status-register.md) | The PCI_EXPRESS_DEVICE_STATUS_REGISTER structure describes a PCI Express (PCIe) device status register of a PCIe capability structure. |
| [EJOB structure](ns-ntddk--ejob.md) | TBD |
| [WHEA_PCIXDEVICE_ID structure](ns-ntddk--whea-pcixdevice-id.md) | TBD |
| [WHEA_GENERIC_ERROR_DATA_ENTRY_V2 structure](ns-ntddk--whea-generic-error-data-entry-v2~r1.md) | TBD |
| [CALLBACK_OBJECT structure](ns-ntddk--callback-object.md) | TBD |
| [PROCESS_MITIGATION_ASLR_POLICY structure](ns-ntddk--process-mitigation-aslr-policy.md) | TBD |
| [HARDWARE_COUNTER structure](ns-ntddk--hardware-counter.md) | The HARDWARE_COUNTER structure contains information about a hardware counter. |
| [POWER_THROTTLING_THREAD_STATE structure](ns-ntddk--power-throttling-thread-state.md) | Stores the throttling policies and how to apply them to a target thread when that thread is subject to power management. |
| [WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS structure](ns-ntddk--whea-xpf-processor-error-section-validbits.md) | TBD |
| [WHEA_PCIXBUS_ID structure](ns-ntddk--whea-pcixbus-id.md) | TBD |
| [KAFFINITY_EX structure](ns-ntddk--kaffinity-ex.md) | TBD |
| [PCI_EXPRESS_L1_PM_SS_CONTROL_1_REGISTER structure](ns-ntddk--pci-express-l1-pm-ss-control-1-register.md) | TBD |
| [MAP_REGISTER_ENTRY structure](ns-ntddk--map-register-entry.md) | TBD |
| [WHEA_PCIXBUS_COMMAND structure](ns-ntddk--whea-pcixbus-command.md) | TBD |
| [KEXCEPTION_FRAME structure](ns-ntddk--kexception-frame~r4.md) | TBD |
| [KEXCEPTION_FRAME structure](ns-ntddk--kexception-frame~r3.md) | TBD |
| [PHAL_DISPATCH structure](ns-ntddk-phal-dispatch.md) | TBD |
| [WHEA_ARM_PROCESSOR_ERROR_CONTEXT_INFORMATION_HEADER_FLAGS structure](ns-ntddk--whea-arm-processor-error-context-information-header-flags.md) | TBD |
| [BDCB_STATUS_UPDATE_CONTEXT structure](ns-ntddk--bdcb-status-update-context.md) | The BDCB_STATUS_UPDATE_CONTEXT structure describes a status update provided by Windows to a boot-start driver's BOOT_DRIVER_CALLBACK_FUNCTION routine. |
| [SOC_SUBSYSTEM_FAILURE_DETAILS structure](ns-ntddk--soc-subsystem-failure-details.md) | The SOC_SUBSYSTEM_FAILURE_DETAILS structure holds information related to a System on a Chip (SoC) bug code. |
| [CORRELATION_VECTOR structure](ns-ntddk-correlation-vector.md) | Store the correlation vector that is used to reference events and the generated logs for diagnostic purposes. |
| [PCI_BUS_INTERFACE_STANDARD structure](ns-ntddk--pci-bus-interface-standard.md) | TBD |
| [PCI_EXPRESS_TPH_ST_TABLE_ENTRY structure](ns-ntddk--pci-express-tph-st-table-entry.md) | TBD |
| [PCIBUSDATA structure](ns-ntddk--pcibusdata.md) | TBD |
| [WHEA_ERROR_RECORD_HEADER_VALIDBITS structure](ns-ntddk--whea-error-record-header-validbits.md) | The WHEA_ERROR_RECORD_HEADER_VALIDBITS union describes which members of a WHEA_ERROR_RECORD_HEADER structure contain valid data. |
| [WHEA_XPF_PROCESSOR_ERROR_SECTION structure](ns-ntddk-whea-xpf-processor-error-section.md) | TBD |
| [ARBITER_LIST_ENTRY structure](ns-ntddk--arbiter-list-entry.md) | TBD |
| [MM_COPY_ADDRESS structure](ns-ntddk--mm-copy-address.md) | The MM_COPY_ADDRESS structure contains either a virtual memory address or a physical memory address. |
| [PCI_EXPRESS_CAPABILITY structure](ns-ntddk--pci-express-capability.md) | The PCI_EXPRESS_CAPABILITY structure describes a PCI Express (PCIe) capability structure. |
| [WHEA_ARM_AARCH64_EL2_CSR structure](ns-ntddk--whea-arm-aarch64-el2-csr.md) | TBD |
| [WHEA_XPF_TLB_CHECK structure](ns-ntddk--whea-xpf-tlb-check.md) | The WHEA_XPF_TLB_CHECK union describes translation lookaside buffer (TLB) error information for an x86 or x64 processor. |
| [NT_TIB structure](ns-ntddk--nt-tib.md) | TBD |
| [PCI_EXPRESS_TPH_REQUESTER_CAPABILITY structure](ns-ntddk--pci-express-tph-requester-capability.md) | TBD |
| [VM_COUNTERS_EX structure](ns-ntddk--vm-counters-ex.md) | TBD |
| [WHEA_GENERIC_ERROR_DATA_ENTRY_V2 structure](ns-ntddk--whea-generic-error-data-entry-v2.md) | TBD |
| [WHEA_PCIEXPRESS_BRIDGE_CONTROL_STATUS structure](ns-ntddk--whea-pciexpress-bridge-control-status.md) | TBD |
| [PROCESS_MITIGATION_IMAGE_LOAD_POLICY structure](ns-ntddk--process-mitigation-image-load-policy.md) | TBD |
| [KUMS_CONTEXT_HEADER structure](ns-ntddk--kums-context-header.md) | TBD |
| [IMAGE_NT_HEADERS structure](ns-ntddk--image-nt-headers.md) | TBD |
| [PROCESS_BASIC_INFORMATION structure](ns-ntddk--process-basic-information.md) | TBD |
| [WHEA_ERROR_INJECTION_CAPABILITIES structure](ns-ntddk--whea-error-injection-capabilities.md) | The WHEA_ERROR_INJECTION_CAPABILITIES union describes the types of hardware errors that can be injected into a hardware platform. |
| [WHEA_XPF_NMI_DESCRIPTOR structure](ns-ntddk--whea-xpf-nmi-descriptor.md) | The WHEA_XPF_NMI_DESCRIPTOR structure describes a nonmaskable interrupt (NMI) error source for an x86 or x64 processor. |
| [WHEA_MEMORY_ERROR_SECTION_VALIDBITS structure](ns-ntddk--whea-memory-error-section-validbits.md) | TBD |
| [WHEA_TIMESTAMP structure](ns-ntddk--whea-timestamp.md) | The WHEA_TIMESTAMP union describes the time that an error was reported to the operating system. |
| [WHEA_IPF_MCA_DESCRIPTOR structure](ns-ntddk--whea-ipf-mca-descriptor.md) | The WHEA_IPF_MCA_DESCRIPTOR structure describes a machine check abort (MCA) error source for an Itanium processor. |
| [WHEA_ARMV8_AARCH64_GPRS structure](ns-ntddk--whea-armv8-aarch64-gprs.md) | TBD |
| [FILE_ATTRIBUTE_TAG_INFORMATION structure](ns-ntddk--file-attribute-tag-information.md) | The FILE_ATTRIBUTE_TAG_INFORMATION structure is used as an argument to ZwQueryInformationFile. |
| [CPE_DRIVER_INFO structure](ns-ntddk--cpe-driver-info.md) | TBD |
| [SE_ADT_OBJECT_TYPE structure](ns-ntddk--se-adt-object-type.md) | TBD |
| [WHEA_ERROR_RECORD structure](ns-ntddk--whea-error-record~r1.md) | TBD |
| [WHEA_RECOVERY_CONTEXT structure](ns-ntddk--whea-recovery-context.md) | TBD |
| [WHEA_ERROR_RECORD_HEADER_FLAGS structure](ns-ntddk--whea-error-record-header-flags.md) | TBD |
| [FILE_FS_SECTOR_SIZE_INFORMATION structure](ns-ntddk--file-fs-sector-size-information.md) | The FILE_FS_SECTOR_SIZE_INFORMATION structure is used to query physical and logical sector size information for a file system volume. |
| [KARM64_VFP_STATE structure](ns-ntddk--karm64-vfp-state.md) | TBD |
| [PCI_AGP_CAPABILITY structure](ns-ntddk--pci-agp-capability.md) | TBD |
| [PCI_EXPRESS_DEVICE_STATUS_2_REGISTER structure](ns-ntddk--pci-express-device-status-2-register.md) | TBD |
| [WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS structure](ns-ntddk--whea-pcixbus-error-section-validbits.md) | The WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS union describes which members of a WHEA_PCIXBUS_ERROR_SECTION structure contain valid data. |
| [KEXCEPTION_FRAME structure](ns-ntddk--kexception-frame.md) | TBD |
| [FILE_FS_OBJECTID_INFORMATION structure](ns-ntddk--file-fs-objectid-information.md) | The FILE_FS_OBJECTID_INFORMATION structure is used to query or set the object ID for a file system volume. |
| [KTRAP_FRAME structure](ns-ntddk--ktrap-frame.md) | TBD |
| [KTRAP_FRAME structure](ns-ntddk--ktrap-frame~r4.md) | TBD |
| [MCA_DRIVER_INFO structure](ns-ntddk--mca-driver-info.md) | TBD |
| [BUS_HANDLER structure](ns-ntddk--bus-handler.md) | TBD |
| [EPROCESS structure](ns-ntddk--eprocess.md) | TBD |
| [WHEA_ARM_BUS_ERROR_VALID_BITS structure](ns-ntddk--whea-arm-bus-error-valid-bits.md) | TBD |
| [VM_COUNTERS structure](ns-ntddk--vm-counters.md) | TBD |
| [WHEA_XPF_PROCINFO_VALIDBITS structure](ns-ntddk--whea-xpf-procinfo-validbits.md) | The WHEA_XPF_PROCINFO_VALIDBITS union describes which members of a WHEA_XPF_PROCINFO structure contain valid data. |
| [CONTROLLER_OBJECT structure](ns-ntddk--controller-object.md) | A controller object represents a hardware adapter or controller with homogenous devices that are the actual targets for I/O requests. |
| [PHYSICAL_MEMORY_RANGE structure](ns-ntddk--physical-memory-range.md) | TBD |
| [SE_ADT_ACCESS_REASON structure](ns-ntddk--se-adt-access-reason.md) | TBD |
| [WHEA_ARM_BUS_ERROR structure](ns-ntddk--whea-arm-bus-error.md) | TBD |
| [ARBITER_TEST_ALLOCATION_PARAMETERS structure](ns-ntddk--arbiter-test-allocation-parameters.md) | TBD |
| [ARBITER_QUERY_ARBITRATE_PARAMETERS structure](ns-ntddk--arbiter-query-arbitrate-parameters.md) | TBD |
| [PCI_AGP_ISOCH_STATUS structure](ns-ntddk--pci-agp-isoch-status.md) | TBD |
| [WHEA_ARM_AARCH32_EL1_CSR structure](ns-ntddk--whea-arm-aarch32-el1-csr.md) | TBD |
| [XSTATE_FEATURE structure](ns-ntddk--xstate-feature.md) | TBD |
| [RTL_AVL_TABLE structure](ns-ntddk--rtl-avl-table.md) | TBD |
| [RTL_GENERIC_TABLE structure](ns-ntddk--rtl-generic-table.md) | TBD |
| [PCI_EXPRESS_SLOT_CONTROL_REGISTER structure](ns-ntddk--pci-express-slot-control-register.md) | The PCI_EXPRESS_SLOT_CONTROL_REGISTER structure describes a PCI Express (PCIe) slot control register of a PCIe capability structure. |
| [WHEA_PROCESSOR_FAMILY_INFO structure](ns-ntddk--whea-processor-family-info.md) | The WHEA_PROCESSOR_FAMILY_INFO union describes the processor family information for an x86 or x64 processor. |
| [KARM_VFP_STATE structure](ns-ntddk--karm-vfp-state.md) | TBD |
| [ZONE_SEGMENT_HEADER structure](ns-ntddk--zone-segment-header.md) | TBD |
| [PROCESS_MITIGATION_EXTENSION_POINT_DISABLE_POLICY structure](ns-ntddk--process-mitigation-extension-point-disable-policy.md) | TBD |
| [WHEA_ERROR_STATUS structure](ns-ntddk--whea-error-status.md) | The WHEA_ERROR_STATUS union describes generic error codes that are abstracted from the data contained in implementation-specific error registers. |
| [WHEA_XPF_BUS_CHECK structure](ns-ntddk--whea-xpf-bus-check.md) | The WHEA_XPF_BUS_CHECK union describes bus error information for an x86 or x64 processor. |
| [PROCESS_MITIGATION_SYSTEM_CALL_DISABLE_POLICY structure](ns-ntddk--process-mitigation-system-call-disable-policy.md) | TBD |
| [WHEA_ERROR_PACKET_FLAGS structure](ns-ntddk--whea-error-packet-flags.md) | The WHEA_ERROR_PACKET_FLAGS union defines the error condition reported through a WHEA_ERROR_PACKET structure. |
| [PROCESS_WS_WATCH_INFORMATION structure](ns-ntddk--process-ws-watch-information.md) | TBD |
| [PM_DISPATCH_TABLE structure](ns-ntddk--pm-dispatch-table.md) | TBD |
| [RTL_DYNAMIC_HASH_TABLE_ENUMERATOR structure](ns-ntddk--rtl-dynamic-hash-table-enumerator.md) | TBD |
| [EJOB structure](ns-ntddk--ejob~r1.md) | TBD |
| [PROCESS_KEEPALIVE_COUNT_INFORMATION structure](ns-ntddk--process-keepalive-count-information.md) | TBD |
| [PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure](ns-ntddk--pci-express-device-capabilities-register.md) | The PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) device capabilities register of a PCIe capability structure. |
| [WHEA_ARM_TLB_ERROR_VALID_BITS structure](ns-ntddk--whea-arm-tlb-error-valid-bits.md) | TBD |
| [WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS structure](ns-ntddk--whea-pciexpress-error-section-validbits.md) | TBD |
| [WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS structure](ns-ntddk--whea-error-record-section-descriptor-flags.md) | TBD |
| [DEBUGGING_DEVICE_IN_USE_INFORMATION structure](ns-ntddk--debugging-device-in-use-information.md) | TBD |
| [FILE_DISPOSITION_INFORMATION_EX structure](ns-ntddk--file-disposition-information-ex.md) | The FILE_DISPOSITION_INFORMATION_EX structure is used as an argument to the ZwSetInformationFileEx routine and indicates how the operating system should delete a file. |
| [WHEA_PCIEXPRESS_DEVICE_ID structure](ns-ntddk--whea-pciexpress-device-id.md) | TBD |
| [PROCESS_MITIGATION_STRICT_HANDLE_CHECK_POLICY structure](ns-ntddk--process-mitigation-strict-handle-check-policy.md) | TBD |
| [PS_CREATE_NOTIFY_INFO structure](ns-ntddk--ps-create-notify-info.md) | The PS_CREATE_NOTIFY_INFO structure provides information about a newly created process. |
| [TRANSLATOR_INTERFACE structure](ns-ntddk--translator-interface.md) | TBD |
| [IO_COUNTERS structure](ns-ntddk--io-counters.md) | TBD |
| [FILE_NAME_INFORMATION structure](ns-ntddk--file-name-information.md) | The FILE_NAME_INFORMATION structure is used as argument to the ZwQueryInformationFile and ZwSetInformationFile routines. |
| [FLOATING_SAVE_AREA structure](ns-ntddk--floating-save-area.md) | TBD |
| [IMAGE_INFO_EX structure](ns-ntddk--image-info-ex.md) | Extended version of the image information structure (see IMAGE_INFO). |
| [PROCESS_MITIGATION_SYSTEM_CALL_FILTER_POLICY structure](ns-ntddk--process-mitigation-system-call-filter-policy.md) | TBD |
| [PDEBUG_DEVICE_ADDRESS structure](ns-ntddk-pdebug-device-address.md) | TBD |
| [IMAGE_NT_HEADERS64 structure](ns-ntddk--image-nt-headers64.md) | TBD |
| [HAL_AMLI_BAD_IO_ADDRESS_LIST structure](ns-ntddk--hal-amli-bad-io-address-list.md) | TBD |
| [QUOTA_LIMITS_EX structure](ns-ntddk--quota-limits-ex.md) | TBD |
| [DEBUGGING_DEVICE_IN_USE structure](ns-ntddk--debugging-device-in-use.md) | TBD |
| [WHEA_ARM_MISC_CSR structure](ns-ntddk--whea-arm-misc-csr.md) | TBD |
| [KEY_CACHED_INFORMATION structure](ns-ntddk--key-cached-information.md) | The KEY_CACHED_INFORMATION structure holds the cached information available for a registry key or subkey. |
| [PCI_ROOT_BUS_OSC_SUPPORT_FIELD structure](ns-ntddk--pci-root-bus-osc-support-field.md) | TBD |
| [PCIX_BRIDGE_CAPABILITY structure](ns-ntddk--pcix-bridge-capability.md) | TBD |
| [SE_ADT_PARAMETER_ARRAY structure](ns-ntddk--se-adt-parameter-array.md) | TBD |
| [CM_PCCARD_DEVICE_DATA structure](ns-ntddk--cm-pccard-device-data.md) | TBD |
| [DEBUG_DEVICE_DESCRIPTOR structure](ns-ntddk--debug-device-descriptor.md) | TBD |
| [WHEA_ERROR_RECORD structure](ns-ntddk--whea-error-record~r2.md) | The WHEA_ERROR_RECORD structure describes an error record that contains error information about a hardware error condition that occurred. |
| [PHYSICAL_COUNTER_RESOURCE_LIST structure](ns-ntddk--physical-counter-resource-list.md) | The PHYSICAL_COUNTER_RESOURCE_LIST structure describes an array of PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structures. |
| [PROCESS_READWRITEVM_LOGGING_INFORMATION structure](ns-ntddk--process-readwritevm-logging-information.md) | Stores options for read/write access for telemetry per process. |
| [DMA_ADAPTER structure](ns-ntddk--dma-adapter.md) | TBD |
| [WHEA_XPF_MCE_DESCRIPTOR structure](ns-ntddk--whea-xpf-mce-descriptor.md) | The WHEA_XPF_MCE_DESCRIPTOR structure describes a machine check exception (MCE) error source for an x86 or x64 processor. |
| [HAL_MCA_INTERFACE structure](ns-ntddk--hal-mca-interface.md) | TBD |
| [PCI_EXPRESS_DEVICE_CONTROL_REGISTER structure](ns-ntddk--pci-express-device-control-register.md) | The PCI_EXPRESS_DEVICE_CONTROL_REGISTER structure describes a PCI Express (PCIe) device control register of a PCIe capability structure. |
| [WHEA_ARM_PROCESSOR_ERROR structure](ns-ntddk--whea-arm-processor-error.md) | TBD |
| [KEXCEPTION_FRAME structure](ns-ntddk--kexception-frame~r1.md) | TBD |
| [PROCESS_MITIGATION_CONTROL_FLOW_GUARD_POLICY structure](ns-ntddk--process-mitigation-control-flow-guard-policy.md) | TBD |
| [PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY structure](ns-ntddk--process-mitigation-payload-restriction-policy.md) | Stores information about process mitigation policy. |
| [DRIVER_VERIFIER_THUNK_PAIRS structure](ns-ntddk--driver-verifier-thunk-pairs.md) | TBD |
| [PROCESS_EXCEPTION_PORT structure](ns-ntddk--process-exception-port.md) | TBD |
| [WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS structure](ns-ntddk-whea-xpf-processor-error-section-validbits.md) | TBD |
| [RATE_QUOTA_LIMIT structure](ns-ntddk--rate-quota-limit.md) | TBD |
| [SE_ADT_PARAMETER_ARRAY_ENTRY structure](ns-ntddk--se-adt-parameter-array-entry.md) | TBD |
| [ARBITER_QUERY_ALLOCATED_RESOURCES_PARAMETERS structure](ns-ntddk--arbiter-query-allocated-resources-parameters.md) | TBD |
| [WHEA_ARM_AARCH32_EL2_CSR structure](ns-ntddk--whea-arm-aarch32-el2-csr.md) | TBD |
| [PCI_EXPRESS_LINK_CONTROL_REGISTER structure](ns-ntddk--pci-express-link-control-register.md) | The PCI_EXPRESS_LINK_CONTROL_REGISTER structure describes a PCI Express (PCIe) link control register of a PCIe capability structure. |
| [DEVICE_HANDLER_OBJECT structure](ns-ntddk--device-handler-object.md) | TBD |
| [PNP_LOCATION_INTERFACE structure](ns-ntddk--pnp-location-interface.md) | The PNP_LOCATION_INTERFACE structure describes the GUID_PNP_LOCATION_INTERFACE interface. |
| [PCI_EXPRESS_LINK_CAPABILITIES_REGISTER structure](ns-ntddk--pci-express-link-capabilities-register.md) | The PCI_EXPRESS_LINK_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) link capabilities register of a PCIe capability structure. |
| [WHEA_PCIXDEVICE_REGISTER_PAIR structure](ns-ntddk-whea-pcixdevice-register-pair.md) | TBD |
| [HAL_BUS_INFORMATION structure](ns-ntddk--hal-bus-information.md) | TBD |
| [NV_MEMORY_RANGE structure](ns-ntddk--nv-memory-range.md) | TBD |
| [PROCESS_DEVICEMAP_INFORMATION_EX structure](ns-ntddk--process-devicemap-information-ex.md) | TBD |
| [DUMMYUNIONNAME structure](ns-ntddk-dummyunionname~r2.md) | TBD |
| [FILE_END_OF_FILE_INFORMATION structure](ns-ntddk--file-end-of-file-information.md) | The FILE_END_OF_FILE_INFORMATION structure is used as an argument to the ZwSetInformationFile routine. |
| [KPCR structure](ns-ntddk--kpcr.md) | TBD |
| [PCI_EXPRESS_DEVICE_CAPABILITIES_2_REGISTER structure](ns-ntddk--pci-express-device-capabilities-2-register.md) | TBD |
| [WHEA_GENERIC_ERROR_BLOCKSTATUS structure](ns-ntddk--whea-generic-error-blockstatus.md) | The WHEA_GENERIC_ERROR_BLOCKSTATUS union indicates what kind of error data is reported in a generic error status block. |
| [KERNEL_USER_TIMES structure](ns-ntddk--kernel-user-times.md) | TBD |
| [POWER_THROTTLING_PROCESS_STATE structure](ns-ntddk--power-throttling-process-state.md) | Stores the throttling policies and how to apply them to a target process when that process is subject to power management. |
| [WHEA_ARM_AARCH32_SECURE_CSR structure](ns-ntddk--whea-arm-aarch32-secure-csr.md) | TBD |
| [WHEA_NMI_ERROR_SECTION_FLAGS structure](ns-ntddk--whea-nmi-error-section-flags.md) | TBD |
| [WHEA_ARMV8_AARCH32_GPRS structure](ns-ntddk--whea-armv8-aarch32-gprs.md) | TBD |
| [PCI_EXPRESS_RESIZABLE_BAR_CAPABILITY_REGISTER structure](ns-ntddk--pci-express-resizable-bar-capability-register.md) | TBD |
| [WHEA_ERROR_RECORD_HEADER structure](ns-ntddk--whea-error-record-header.md) | The WHEA_ERROR_RECORD_HEADER structure describes general information about a hardware error condition. |
| [PROCESS_ACCESS_TOKEN structure](ns-ntddk--process-access-token.md) | TBD |
| [PCI_EXPRESS_TPH_REQUESTER_CAPABILITY_REGISTER structure](ns-ntddk--pci-express-tph-requester-capability-register.md) | TBD |
| [KPROCESS structure](ns-ntddk--kprocess.md) | TBD |
| [KTRAP_FRAME structure](ns-ntddk--ktrap-frame~r2.md) | TBD |
| [WHEA_NMI_ERROR_SECTION structure](ns-ntddk--whea-nmi-error-section.md) | The WHEA_NMI_ERROR_SECTION structure describes nonmaskable interrupt (NMI) error data. |
| [ARBITER_QUERY_CONFLICT_PARAMETERS structure](ns-ntddk--arbiter-query-conflict-parameters.md) | TBD |
| [CONFIGURATION_INFORMATION structure](ns-ntddk--configuration-information.md) | TBD |
| [PCI_EXPRESS_ROOT_CONTROL_REGISTER structure](ns-ntddk--pci-express-root-control-register.md) | The PCI_EXPRESS_ROOT_CONTROL_REGISTER structure describes a PCI Express (PCIe) root control register of a PCIe capability structure. |
| [WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS structure](ns-ntddk--whea-error-record-section-descriptor-validbits.md) | TBD |
| [ZONE_HEADER structure](ns-ntddk--zone-header.md) | TBD |
| [SYSTEM_FIRMWARE_TABLE_HANDLER structure](ns-ntddk--system-firmware-table-handler.md) | TBD |
| [PCI_EXPRESS_RESIZABLE_BAR_CAPABILITY structure](ns-ntddk--pci-express-resizable-bar-capability.md) | TBD |
| [HAL_PLATFORM_INFORMATION structure](ns-ntddk--hal-platform-information.md) | TBD |
| [HAL_CALLBACKS structure](ns-ntddk--hal-callbacks.md) | TBD |
| [MCG_STATUS structure](ns-ntddk--mcg-status.md) | TBD |
| [VM_COUNTERS_EX2 structure](ns-ntddk--vm-counters-ex2.md) | TBD |
| [WHEA_ARM_PROCESSOR_ERROR_SECTION structure](ns-ntddk--whea-arm-processor-error-section.md) | TBD |
| [RTL_SPLAY_LINKS structure](ns-ntddk--rtl-splay-links.md) | The RTL_SPLAY_LINKS structure is an opaque structure and is used by the system to represent a splay link tree node. |
| [CONTEXT structure](ns-ntddk--context.md) | TBD |
| [HAL_PROCESSOR_SPEED_INFO structure](ns-ntddk--hal-processor-speed-info.md) | TBD |
| [PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structure](ns-ntddk--physical-counter-resource-descriptor.md) | The PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structure describes the counter resources available on the platform. |
| [WHEA_PCIXDEVICE_ERROR_SECTION_VALIDBITS structure](ns-ntddk--whea-pcixdevice-error-section-validbits.md) | TBD |
| [WHEA_PSHED_PLUGIN_CALLBACKS structure](ns-ntddk--whea-pshed-plugin-callbacks.md) | The WHEA_PSHED_PLUGIN_CALLBACKS structure describes the callback functions for a PSHED plug-in. |
| [XPF_MC_BANK_FLAGS structure](ns-ntddk--xpf-mc-bank-flags.md) | TBD |
| [PCI_EXPRESS_L1_PM_SS_CAPABILITIES_REGISTER structure](ns-ntddk--pci-express-l1-pm-ss-capabilities-register.md) | TBD |
| [RTL_GENERIC_TABLE structure](ns-ntddk--rtl-generic-table~r1.md) | The RTL_GENERIC_TABLE structure contains file system-specific data for a splay tree. |
| [KEY_VIRTUALIZATION_INFORMATION structure](ns-ntddk--key-virtualization-information.md) | The KEY_VIRTUALIZATION_INFORMATION structure defines the basic information that is available for a registry key or subkey. |
| [PROCESS_SESSION_INFORMATION structure](ns-ntddk--process-session-information.md) | TBD |
| [XSTATE_CONFIGURATION structure](ns-ntddk--xstate-configuration.md) | TBD |
| [DEBUG_TRANSPORT_DATA structure](ns-ntddk--debug-transport-data.md) | TBD |
| [KEY_NAME_INFORMATION structure](ns-ntddk--key-name-information.md) | The KEY_NAME_INFORMATION structure holds the name and name length of the key. |
| [WHEA_ARMV8_AARCH64_EL3_CSR structure](ns-ntddk--whea-armv8-aarch64-el3-csr.md) | TBD |
| [KPCR structure](ns-ntddk--kpcr~r3.md) | TBD |
| [KPROCESS structure](ns-ntddk--kprocess~r1.md) | TBD |
| [WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS structure](ns-ntddk--whea-processor-generic-error-section-validbits.md) | TBD |
| [WHEA_XPF_PROCESSOR_ERROR_SECTION structure](ns-ntddk--whea-xpf-processor-error-section.md) | The WHEA_XPF_PROCESSOR_ERROR_SECTION structure describes processor error data that is specific to the x86/x64 processor architecture. |
| [ARBITER_CONFLICT_INFO structure](ns-ntddk--arbiter-conflict-info.md) | TBD |
| [WHEA_ARM_PROCESSOR_ERROR_INFORMATION_VALID_BITS structure](ns-ntddk--whea-arm-processor-error-information-valid-bits.md) | TBD |
| [WHEA_XPF_MS_CHECK structure](ns-ntddk--whea-xpf-ms-check.md) | The WHEA_XPF_MS_CHECK union describes microarchitecture-specific error information for an x86 or x64 processor. |
| [PCI_EXPRESS_CAPABILITIES_REGISTER structure](ns-ntddk--pci-express-capabilities-register.md) | The PCI_EXPRESS_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) capabilities register of a PCIe capability structure. |
| [WHEA_NOTIFICATION_FLAGS structure](ns-ntddk--whea-notification-flags.md) | TBD |
| [PCI_EXPRESS_LTR_CAPABILITY structure](ns-ntddk--pci-express-ltr-capability.md) | TBD |
| [HAL_PROCESSOR_FEATURE structure](ns-ntddk--hal-processor-feature.md) | TBD |
| [PROCESS_MITIGATION_BINARY_SIGNATURE_POLICY structure](ns-ntddk--process-mitigation-binary-signature-policy.md) | TBD |
| [PROCESS_HANDLE_TRACING_ENABLE_EX structure](ns-ntddk--process-handle-tracing-enable-ex.md) | TBD |
| [WHEA_XPF_MC_BANK_DESCRIPTOR structure](ns-ntddk--whea-xpf-mc-bank-descriptor.md) | The WHEA_XPF_MC_BANK_DESCRIPTOR structure describes a bank of machine check registers for an x86 or x64 processor. |
| [OBJECT_TYPE structure](ns-ntddk--object-type.md) | TBD |
| [QUOTA_LIMITS structure](ns-ntddk--quota-limits.md) | TBD |
| [WHEA_XPF_PROCINFO structure](ns-ntddk--whea-xpf-procinfo.md) | The WHEA_XPF_PROCINFO structure describes processor error information that is specific to the x86 and x64 processor architectures. |
| [IMAGE_INFO structure](ns-ntddk--image-info.md) | Used by driver's load-image routine (PLOAD_IMAGE_NOTIFY_ROUTINE) to specify image information. |
| [WHEA_NOTIFICATION_DESCRIPTOR structure](ns-ntddk--whea-notification-descriptor.md) | The WHEA_NOTIFICATION_DESCRIPTOR structure describes the notification mechanism that is used by an error source. |
| [KEY_LAYER_INFORMATION structure](ns-ntddk--key-layer-information.md) | TBD |
| [FILE_FS_SIZE_INFORMATION structure](ns-ntddk--file-fs-size-information.md) | The FILE_FS_SIZE_INFORMATION structure is used to query sector size information for a file system volume. |
| [DUMMYUNIONNAME structure](ns-ntddk-dummyunionname~r1.md) | TBD |
| [PROCESS_DEVICEMAP_INFORMATION structure](ns-ntddk--process-devicemap-information.md) | TBD |
| [HAL_POWER_INFORMATION structure](ns-ntddk--hal-power-information.md) | TBD |
| [FILE_FS_LABEL_INFORMATION structure](ns-ntddk--file-fs-label-information.md) | The FILE_FS_LABEL_INFORMATION structure is used to set the label for a file system volume. |
| [PCI_EXPRESS_DEVICE_CONTROL_2_REGISTER structure](ns-ntddk--pci-express-device-control-2-register.md) | TBD |
| [ARM64_NT_NEON128 structure](ns-ntddk--arm64-nt-neon128.md) | TBD |
| [PCI_AGP_ISOCH_COMMAND structure](ns-ntddk--pci-agp-isoch-command.md) | TBD |
| [PCI_FIRMWARE_BUS_CAPS structure](ns-ntddk--pci-firmware-bus-caps.md) | TBD |
| [PROCESS_MITIGATION_FONT_DISABLE_POLICY structure](ns-ntddk--process-mitigation-font-disable-policy.md) | TBD |
| [PROCESS_HANDLE_TRACING_ENTRY structure](ns-ntddk--process-handle-tracing-entry.md) | TBD |
| [PCI_AGP_EXTENDED_CAPABILITY structure](ns-ntddk-pci-agp-extended-capability.md) | TBD |
| [WHEA_PCIXDEVICE_ERROR_SECTION structure](ns-ntddk--whea-pcixdevice-error-section.md) | The WHEA_PCIXDEVICE_ERROR_SECTION structure describes PCI or PCI-X device error data. |
| [HAL_ERROR_INFO structure](ns-ntddk--hal-error-info.md) | TBD |
| [WHEA_PROCESSOR_GENERIC_ERROR_SECTION structure](ns-ntddk--whea-processor-generic-error-section.md) | Describes processor error data that is not specific to a particular processor architecture. |
| [RTL_AVL_TABLE structure](ns-ntddk--rtl-avl-table~r1.md) | The RTL_AVL_TABLE structure contains file system-specific data for an Adelson-Velsky/Landis (AVL) tree. |
| [FILE_VALID_DATA_LENGTH_INFORMATION structure](ns-ntddk--file-valid-data-length-information.md) | The FILE_VALID_DATA_LENGTH_INFORMATION structure is used as an argument to ZwSetInformationFile. |
| [WHEA_ARM_CACHE_ERROR structure](ns-ntddk--whea-arm-cache-error.md) | TBD |
| [POOLED_USAGE_AND_LIMITS structure](ns-ntddk--pooled-usage-and-limits.md) | TBD |
| [WHEA_ARM_PROCESSOR_ERROR_CONTEXT_INFORMATION_HEADER structure](ns-ntddk--whea-arm-processor-error-context-information-header.md) | TBD |
| [WHEA_IPF_CMC_DESCRIPTOR structure](ns-ntddk--whea-ipf-cmc-descriptor.md) | The WHEA_IPF_CMC_DESCRIPTOR structure describes a corrected machine check (CMC) error source for an Itanium processor. |
| [CMC_DRIVER_INFO structure](ns-ntddk--cmc-driver-info.md) | TBD |
| [WHEA_ERROR_SOURCE_DESCRIPTOR structure](ns-ntddk--whea-error-source-descriptor.md) | TBD |
| [WHEA_XPF_CACHE_CHECK structure](ns-ntddk--whea-xpf-cache-check.md) | The WHEA_XPF_CACHE_CHECK union describes cache error information for an x86 or x64 processor. |
| [WHEA_GENERIC_ERROR_DESCRIPTOR structure](ns-ntddk--whea-generic-error-descriptor.md) | The WHEA_GENERIC_ERROR_DESCRIPTOR structure describes a generic error source. |
| [SYSTEM_FIRMWARE_TABLE_INFORMATION structure](ns-ntddk--system-firmware-table-information.md) | TBD |
| [WHEA_PCIEXPRESS_VERSION structure](ns-ntddk--whea-pciexpress-version.md) | TBD |
| [RTL_BALANCED_LINKS structure](ns-ntddk--rtl-balanced-links.md) | TBD |
| [PROCESS_HANDLE_TRACING_ENABLE structure](ns-ntddk--process-handle-tracing-enable.md) | TBD |
| [WHEA_GENERIC_ERROR structure](ns-ntddk--whea-generic-error.md) | The WHEA_GENERIC_ERROR structure describes error status data for a generic error source. |
| [AGP_TARGET_BUS_INTERFACE_STANDARD structure](ns-ntddk--agp-target-bus-interface-standard.md) | TBD |
| [WHEA_PCIXBUS_ERROR_SECTION structure](ns-ntddk--whea-pcixbus-error-section.md) | The WHEA_PCIXBUS_ERROR_SECTION structure describes PCI or PCI-X bus error data. |
| [ARBITER_RETEST_ALLOCATION_PARAMETERS structure](ns-ntddk--arbiter-retest-allocation-parameters.md) | TBD |
| [KTRAP_FRAME structure](ns-ntddk--ktrap-frame~r1.md) | TBD |
| [ARBITER_PARAMETERS structure](ns-ntddk--arbiter-parameters.md) | TBD |
| [PCI_ROOT_BUS_OSC_CONTROL_FIELD structure](ns-ntddk--pci-root-bus-osc-control-field.md) | TBD |
| [PROCESS_MITIGATION_DEP_POLICY structure](ns-ntddk--process-mitigation-dep-policy.md) | TBD |
| [ETHREAD structure](ns-ntddk--ethread.md) | TBD |
| [WHEA_ERROR_PACKET_V2 structure](ns-ntddk--whea-error-packet-v2.md) | The WHEA_ERROR_PACKET_V2 structure describes the hardware error data that is passed to the operating system by a low-level hardware error handler (LLHEH).Note  The WHEA_ERROR_PACKET_V2 structure is supported in Windows 7 and later versions of Windows. |
| [KTHREAD structure](ns-ntddk--kthread~r1.md) | TBD |
| [PCI_AGP_APERTURE_PAGE_SIZE structure](ns-ntddk--pci-agp-aperture-page-size.md) | TBD |
| [PCI_ROOT_BUS_HARDWARE_CAPABILITY structure](ns-ntddk--pci-root-bus-hardware-capability.md) | TBD |
| [PROCESS_HANDLE_TRACING_QUERY structure](ns-ntddk--process-handle-tracing-query.md) | TBD |
| [WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure](ns-ntddk--whea-error-record-section-descriptor.md) | The WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure describes a section of error information that is part of an error record. |
| [CREATE_USER_PROCESS_ECP_CONTEXT structure](ns-ntddk--create-user-process-ecp-context.md) | TBD |
| [PCI_FIRMWARE_BUS_CAPS_RETURN_BUFFER structure](ns-ntddk--pci-firmware-bus-caps-return-buffer.md) | TBD |
| [KTRAP_FRAME structure](ns-ntddk--ktrap-frame~r3.md) | TBD |
| [PCI_EXPRESS_SLOT_STATUS_REGISTER structure](ns-ntddk--pci-express-slot-status-register.md) | The PCI_EXPRESS_SLOT_STATUS_REGISTER structure describes a PCI Express (PCIe) slot status register of a PCIe capability structure. |
| [WHEA_X64_REGISTER_STATE structure](ns-ntddk--whea-x64-register-state.md) | The WHEA_X64_REGISTER_STATE structure describes the state of an x64 processor's registers. |
| [WHEA_ERROR_PACKET_V1 structure](ns-ntddk--whea-error-packet-v1~r1.md) | TBD |
| [PCI_EXPRESS_L1_PM_SS_CONTROL_2_REGISTER structure](ns-ntddk--pci-express-l1-pm-ss-control-2-register.md) | TBD |
| [TIMER_SET_COALESCABLE_TIMER_INFO structure](ns-ntddk--timer-set-coalescable-timer-info.md) | TBD |
| [AER_ROOTPORT_DESCRIPTOR_FLAGS structure](ns-ntddk--aer-rootport-descriptor-flags.md) | TBD |
| [PEB structure](ns-ntddk--peb.md) | TBD |
| [RTL_DYNAMIC_HASH_TABLE structure](ns-ntddk--rtl-dynamic-hash-table.md) | TBD |
| [MCI_STATUS structure](ns-ntddk--mci-status.md) | TBD |
| [WHEA_ERROR_RECORD structure](ns-ntddk--whea-error-record.md) | TBD |
| [PCI_DEBUGGING_DEVICE_IN_USE structure](ns-ntddk--pci-debugging-device-in-use.md) | TBD |
| [NEON128 structure](ns-ntddk--neon128.md) | TBD |
| [ETHREAD structure](ns-ntddk--ethread~r1.md) | TBD |
| [OPLOCK_KEY_CONTEXT structure](ns-ntddk--oplock-key-context.md) | The OPLOCK_KEY_CONTEXT structure is returned from IoGetOplockKeyContextEx. This structure contains oplock keys for a specific file object. |
| [WHEA_XPF_MCA_SECTION structure](ns-ntddk--whea-xpf-mca-section.md) | TBD |
| [RTL_DYNAMIC_HASH_TABLE_ENTRY structure](ns-ntddk--rtl-dynamic-hash-table-entry.md) | TBD |
| [WHEA_ARM_PROCESSOR_ERROR_INFORMATION structure](ns-ntddk--whea-arm-processor-error-information.md) | TBD |
| [PCI_EXPRESS_SLOT_CAPABILITIES_REGISTER structure](ns-ntddk--pci-express-slot-capabilities-register.md) | The PCI_EXPRESS_SLOT_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) slot capabilities register of a PCIe capability structure. |
| [PROCESS_MITIGATION_CHILD_PROCESS_POLICY structure](ns-ntddk--process-mitigation-child-process-policy.md) | Stores policy information about creating child processes. |
| [WHEA_GENERIC_ERROR_DATA_ENTRY_V1 structure](ns-ntddk--whea-generic-error-data-entry-v1.md) | TBD |
| [SILO_MONITOR_REGISTRATION structure](ns-ntddk--silo-monitor-registration.md) | This structure specifies a server silo monitor that can receive notifications about server silo events. |
| [FILE_ALIGNMENT_INFORMATION structure](ns-ntddk--file-alignment-information.md) | The FILE_ALIGNMENT_INFORMATION structure is used as an argument to the ZwQueryInformationFile routine. |
| [WHEA_GENERIC_ERROR_DESCRIPTOR_V2 structure](ns-ntddk--whea-generic-error-descriptor-v2.md) | TBD |
| [PCI_EXPRESS_LTR_MAX_LATENCY_REGISTER structure](ns-ntddk--pci-express-ltr-max-latency-register.md) | TBD |
| [WHEA_ARM_CACHE_ERROR_VALID_BITS structure](ns-ntddk--whea-arm-cache-error-valid-bits.md) | TBD |
| [WHEA_FIRMWARE_ERROR_RECORD_REFERENCE structure](ns-ntddk--whea-firmware-error-record-reference.md) | The WHEA_FIRMWARE_ERROR_RECORD_REFERENCE structure describes a reference to a firmware error record that is specific to the Itanium processor architecture. |
| [FILE_FS_METADATA_SIZE_INFORMATION structure](ns-ntddk--file-fs-metadata-size-information.md) | TBD |
| [PCI_ADVANCED_FEATURES_CAPABILITY structure](ns-ntddk--pci-advanced-features-capability.md) | TBD |
| [XPF_MCE_FLAGS structure](ns-ntddk--xpf-mce-flags.md) | TBD |
| [PROCESS_EXTENDED_BASIC_INFORMATION structure](ns-ntddk--process-extended-basic-information.md) | TBD |
| [OPLOCK_KEY_ECP_CONTEXT structure](ns-ntddk--oplock-key-ecp-context.md) | TBD |
| [PCI_EXPRESS_RESIZABLE_BAR_ENTRY structure](ns-ntddk--pci-express-resizable-bar-entry.md) | TBD |
| [SILO_MONITOR structure](ns-ntddk--silo-monitor.md) | TBD |
| [KINTERRUPT structure](ns-ntddk--kinterrupt.md) | TBD |
| [PCI_AGP_CONTROL structure](ns-ntddk--pci-agp-control.md) | TBD |
| [PDEBUG_MEMORY_REQUIREMENTS structure](ns-ntddk-pdebug-memory-requirements.md) | TBD |
| [IO_TIMER structure](ns-ntddk--io-timer.md) | TBD |
| [KPCR structure](ns-ntddk--kpcr~r1.md) | TBD |
| [WHEA_IPF_CPE_DESCRIPTOR structure](ns-ntddk--whea-ipf-cpe-descriptor.md) | The WHEA_IPF_CPE_DESCRIPTOR structure describes a corrected platform error (CPE) error source for an Itanium processor. |
| [DISK_SIGNATURE structure](ns-ntddk--disk-signature.md) | DISK_SIGNATURE contains the disk signature information for a disk's partition table. |
| [EXCEPTION_REGISTRATION_RECORD structure](ns-ntddk--exception-registration-record.md) | TBD |
| [ACPI_DEBUGGING_DEVICE_IN_USE structure](ns-ntddk--acpi-debugging-device-in-use.md) | TBD |
| [NT_TIB32 structure](ns-ntddk--nt-tib32.md) | TBD |
| [KEXCEPTION_FRAME structure](ns-ntddk--kexception-frame~r2.md) | TBD |
| [WHEA_MEMORY_ERROR_SECTION structure](ns-ntddk--whea-memory-error-section.md) | The WHEA_MEMORY_ERROR_SECTION structure describes platform memory error data. |
| [WHEA_ARM_PROCESSOR_ERROR_SECTION_VALID_BITS structure](ns-ntddk--whea-arm-processor-error-section-valid-bits.md) | TBD |
| [WHEA_AER_ROOTPORT_DESCRIPTOR structure](ns-ntddk--whea-aer-rootport-descriptor.md) | The WHEA_AER_ROOTPORT_DESCRIPTOR structure describes a PCI Express (PCIe) root port error source. |
| [WHEA_ERROR_PACKET_V1 structure](ns-ntddk--whea-error-packet-v1.md) | The WHEA_ERROR_PACKET_V1 structure describes the hardware error data that is passed to the operating system by a low-level hardware error handler (LLHEH).Note  The WHEA_ERROR_PACKET_V1 structure is supported in Windows Server 2008 and Windows Vista SP1. |
| [PCI_SUBSYSTEM_IDS_CAPABILITY structure](ns-ntddk--pci-subsystem-ids-capability.md) | TBD |
| [WHEA_AER_ENDPOINT_DESCRIPTOR structure](ns-ntddk--whea-aer-endpoint-descriptor.md) | The WHEA_AER_ENDPOINT_DESCRIPTOR structure describes a PCI Express (PCIe) endpoint error source. |
| [SE_ADT_PARAMETER_ARRAY_EX structure](ns-ntddk--se-adt-parameter-array-ex.md) | TBD |
| [PAGE_PRIORITY_INFORMATION structure](ns-ntddk--page-priority-information.md) | TBD |
| [TXN_PARAMETER_BLOCK structure](ns-ntddk--txn-parameter-block.md) | The TXN_PARAMETER_BLOCK structure contains information about a transacted file operation. |
| [RTL_RUN_ONCE structure](ns-ntddk--rtl-run-once.md) | TBD |
| [ARBITER_BOOT_ALLOCATION_PARAMETERS structure](ns-ntddk--arbiter-boot-allocation-parameters.md) | TBD |
| [FILE_FS_FULL_SIZE_INFORMATION structure](ns-ntddk--file-fs-full-size-information.md) | The FILE_FS_FULL_SIZE_INFORMATION structure is used to query sector size information for a file system volume. |
| [KTHREAD structure](ns-ntddk--kthread.md) | TBD |
| [WHEA_ARM_AARCH64_EL1_CSR structure](ns-ntddk--whea-arm-aarch64-el1-csr.md) | TBD |
| [PROCESS_MITIGATION_DYNAMIC_CODE_POLICY structure](ns-ntddk--process-mitigation-dynamic-code-policy.md) | TBD |
| [SE_ADT_CLAIMS structure](ns-ntddk--se-adt-claims.md) | TBD |
| [KUSER_SHARED_DATA structure](ns-ntddk--kuser-shared-data.md) | TBD |
| [FILE_FS_VOLUME_INFORMATION structure](ns-ntddk--file-fs-volume-information.md) | The FILE_FS_VOLUME_INFORMATION structure is used to query information about a volume on which a file system is mounted. |
| [NT_TIB64 structure](ns-ntddk--nt-tib64.md) | TBD |
| [FILE_DISPOSITION_INFORMATION structure](ns-ntddk--file-disposition-information.md) | The FILE_DISPOSITION_INFORMATION structure is used as an argument to the ZwSetInformationFile routine. |
| [PCI_EXPRESS_RESIZABLE_BAR_CONTROL_REGISTER structure](ns-ntddk--pci-express-resizable-bar-control-register.md) | TBD |
| [PCI_EXPRESS_ROOT_CAPABILITIES_REGISTER structure](ns-ntddk--pci-express-root-capabilities-register.md) | The PCI_EXPRESS_ROOT_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) root capabilities register of a PCIe capability structure. |
| [WHEA_PCIEXPRESS_ERROR_SECTION structure](ns-ntddk--whea-pciexpress-error-section.md) | The WHEA_PCIEXPRESS_ERROR_SECTION structure describes PCI Express (PCIe) error data. |
| [WHEA_PERSISTENCE_INFO structure](ns-ntddk--whea-persistence-info.md) | The WHEA_PERSISTENCE_INFO union describes data that is used by the error record persistence interface for storing an error record. |
| [WHEA_X86_REGISTER_STATE structure](ns-ntddk--whea-x86-register-state.md) | The WHEA_X86_REGISTER_STATE structure describes the state of an x86 processor's registers. |
| [WHEA_XPF_CONTEXT_INFO structure](ns-ntddk--whea-xpf-context-info.md) | The WHEA_XPF_CONTEXT_INFO structure describes processor context information for an x86 or x64 processor. |
| [IO_DRIVER_CREATE_CONTEXT structure](ns-ntddk--io-driver-create-context.md) | The IO_DRIVER_CREATE_CONTEXT structure is used to pass additional parameters to the IoCreateFileEx and FltCreateFileEx2 routines. |
| [PCI_EXPRESS_ROOT_STATUS_REGISTER structure](ns-ntddk--pci-express-root-status-register.md) | The PCI_EXPRESS_ROOT_STATUS_REGISTER structure describes a PCI Express (PCIe) root status register of a PCIe capability structure. |
| [WHEA_ERROR_PACKET_V2 structure](ns-ntddk--whea-error-packet-v2~r1.md) | TBD |
| [WHEA_PCIEXPRESS_COMMAND_STATUS structure](ns-ntddk--whea-pciexpress-command-status.md) | TBD |
| [IO_FOEXT_SILO_PARAMETERS structure](ns-ntddk--io-foext-silo-parameters.md) | This structure describes the Container context that's identified by the IoGetSiloParameters routine. |
| [BDCB_IMAGE_INFORMATION structure](ns-ntddk--bdcb-image-information.md) | The BDCB_IMAGE_INFORMATION structure describes information about a boot-start driver that is about to be initialized, provided by Windows to a boot-start driver's BOOT_DRIVER_CALLBACK_FUNCTION routine. |
| [PROCESS_REVOKE_FILE_HANDLES_INFORMATION structure](ns-ntddk--process-revoke-file-handles-information.md) | TBD |
| [PCI_EXPRESS_PME_REQUESTOR_ID structure](ns-ntddk--pci-express-pme-requestor-id.md) | The PCI_EXPRESS_PME_REQUESTOR_ID structure describes the identifier of the requester of a power management event (PME). |
| [ARBITER_ADD_RESERVED_PARAMETERS structure](ns-ntddk--arbiter-add-reserved-parameters.md) | TBD |
| [WHEA_ARM_TLB_ERROR structure](ns-ntddk--whea-arm-tlb-error.md) | TBD |
| [WHEA_XPF_CMC_DESCRIPTOR structure](ns-ntddk--whea-xpf-cmc-descriptor.md) | The WHEA_XPF_CMC_DESCRIPTOR structure describes a corrected machine check (CMC) error source for an x86 or x64 processor. |
| [WHEA_ERROR_SOURCE_DESCRIPTOR structure](ns-ntddk--whea-error-source-descriptor~r1.md) | The WHEA_ERROR_SOURCE_DESCRIPTOR structure describes an error source. |
| [RTL_DYNAMIC_HASH_TABLE_CONTEXT structure](ns-ntddk--rtl-dynamic-hash-table-context.md) | TBD |
| [WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure](ns-ntddk--whea-pshed-plugin-registration-packet.md) | TBD |
| [ARBITER_INTERFACE structure](ns-ntddk--arbiter-interface.md) | TBD |
| [KPCR structure](ns-ntddk--kpcr~r2.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [SOC_SUBSYSTEM_TYPE enumeration](ne-ntddk--soc-subsystem-type.md) | TBD |
| [INTERLOCKED_RESULT enumeration](ne-ntddk--interlocked-result~r1.md) | TBD |
| [WHEA_ERROR_TYPE enumeration](ne-ntddk--whea-error-type.md) | The WHEA_ERROR_TYPE enumeration defines the different types of hardware components that can report a hardware error. |
| [INTERLOCKED_RESULT enumeration](ne-ntddk--interlocked-result~r3.md) | TBD |
| [WELL_KNOWN_SID_TYPE enumeration](ne-ntddk-well-known-sid-type.md) | TBD |
| [BDCB_CALLBACK_TYPE enumeration](ne-ntddk--bdcb-callback-type.md) | The BDCB_CALLBACK_TYPE enumeration specifies whether the callback being passed to a BOOT_DRIVER_CALLBACK_FUNCTION routine is a status update or a boot-start driver initialization notification. |
| [SE_IMAGE_SIGNATURE_TYPE enumeration](ne-ntddk--se-image-signature-type.md) | TBD |
| [PSCREATEPROCESSNOTIFYTYPE enumeration](ne-ntddk--pscreateprocessnotifytype.md) | Indicates the type of process notification. This enumeration is used in PsSetCreateProcessNotifyRoutineEx2 to register callback notifications. |
| [HAL_SET_INFORMATION_CLASS enumeration](ne-ntddk--hal-set-information-class.md) | TBD |
| [RTL_GENERIC_COMPARE_RESULTS enumeration](ne-ntddk--rtl-generic-compare-results.md) | TBD |
| [EXTENDED_AGP_REGISTER enumeration](ne-ntddk--extended-agp-register.md) | TBD |
| [BUS_DATA_TYPE enumeration](ne-ntddk--bus-data-type.md) | The BUS_DATA_TYPE enumeration indicates the type of bus configuration space. |
| [WHEA_ERROR_PACKET_DATA_FORMAT enumeration](ne-ntddk--whea-error-packet-data-format.md) | The WHEA_ERROR_PACKET_DATA_FORMAT enumeration defines the raw hardware error data format in a hardware error packet. |
| [HAL_DMA_CRASH_DUMP_REGISTER_TYPE enumeration](ne-ntddk--hal-dma-crash-dump-register-type.md) | TBD |
| [PCI_EXPRESS_POWER_STATE enumeration](ne-ntddk-pci-express-power-state.md) | TBD |
| [WHEA_ERROR_SOURCE_STATE enumeration](ne-ntddk--whea-error-source-state.md) | The WHEA_ERROR_SOURCE_STATE enumeration defines the different runtime states for an error source. |
| [PKD_CALLBACK_ACTION enumeration](ne-ntddk-pkd-callback-action.md) | TBD |
| [WHEA_RAW_DATA_FORMAT enumeration](ne-ntddk--whea-raw-data-format.md) | The WHEA_RAW_DATA_FORMAT enumeration defines the possible formats that raw hardware error data can be encoded in a hardware error packet. |
| [WHEA_ERROR_SEVERITY enumeration](ne-ntddk--whea-error-severity.md) | The WHEA_ERROR_SEVERITY enumeration defines the possible severity levels of a hardware error condition. |
| [CONFIGURATION_TYPE enumeration](ne-ntddk--configuration-type.md) | TBD |
| [PCI_EXPRESS_L1_EXIT_LATENCY enumeration](ne-ntddk-pci-express-l1-exit-latency.md) | TBD |
| [SYSTEM_FIRMWARE_TABLE_ACTION enumeration](ne-ntddk--system-firmware-table-action.md) | TBD |
| [PKD_NAMESPACE_ENUM enumeration](ne-ntddk-pkd-namespace-enum.md) | TBD |
| [PCI_EXPRESS_L0s_EXIT_LATENCY enumeration](ne-ntddk-pci-express-l0s-exit-latency.md) | TBD |
| [THREADINFOCLASS enumeration](ne-ntddk--threadinfoclass.md) | TBD |
| [PCI_EXPRESS_DEVICE_TYPE enumeration](ne-ntddk-pci-express-device-type.md) | TBD |
| [RESOURCE_TRANSLATION_DIRECTION enumeration](ne-ntddk--resource-translation-direction.md) | TBD |
| [PROCESSINFOCLASS enumeration](ne-ntddk--processinfoclass.md) | TBD |
| [WHEA_CPU_VENDOR enumeration](ne-ntddk--whea-cpu-vendor.md) | TBD |
| [MM_ROTATE_DIRECTION enumeration](ne-ntddk--mm-rotate-direction.md) | TBD |
| [PCI_EXPRESS_INDICATOR_STATE enumeration](ne-ntddk-pci-express-indicator-state.md) | TBD |
| [ARBITER_REQUEST_SOURCE enumeration](ne-ntddk--arbiter-request-source.md) | TBD |
| [IO_QUERY_DEVICE_DATA_FORMAT enumeration](ne-ntddk--io-query-device-data-format.md) | TBD |
| [PSCREATETHREADNOTIFYTYPE enumeration](ne-ntddk--pscreatethreadnotifytype.md) | Indicates the type of thread notification. This enumeration is used in PsSetCreateThreadNotifyRoutineEx to register callback notifications associated with thread creation or deletion. |
| [PHAL_APIC_DESTINATION_MODE enumeration](ne-ntddk-phal-apic-destination-mode.md) | TBD |
| [PCI_EXPRESS_ASPM_CONTROL enumeration](ne-ntddk-pci-express-aspm-control.md) | TBD |
| [HAL_DISPLAY_BIOS_INFORMATION enumeration](ne-ntddk--hal-display-bios-information.md) | TBD |
| [TABLE_SEARCH_RESULT enumeration](ne-ntddk--table-search-result.md) | TBD |
| [HAL_QUERY_INFORMATION_CLASS enumeration](ne-ntddk--hal-query-information-class.md) | TBD |
| [ARBITER_ACTION enumeration](ne-ntddk--arbiter-action.md) | TBD |
| [PCI_EXPRESS_ASPM_SUPPORT enumeration](ne-ntddk-pci-express-aspm-support.md) | TBD |
| [TIMER_SET_INFORMATION_CLASS enumeration](ne-ntddk--timer-set-information-class.md) | TBD |
| [WHEA_ERROR_SOURCE_TYPE enumeration](ne-ntddk--whea-error-source-type.md) | The WHEA_ERROR_SOURCE_TYPE enumeration defines the different types of error sources that can report hardware errors. |
| [SE_ADT_PARAMETER_TYPE enumeration](ne-ntddk--se-adt-parameter-type.md) | TBD |
| [PCI_EXPRESS_MRL_STATE enumeration](ne-ntddk-pci-express-mrl-state.md) | TBD |
| [BDCB_STATUS_UPDATE_TYPE enumeration](ne-ntddk--bdcb-status-update-type.md) | The BDCB_STATUS_UPDATE_TYPE enumeration lists the types of boot-driver callback status updates. |
| [PCI_EXPRESS_CARD_PRESENCE enumeration](ne-ntddk-pci-express-card-presence.md) | TBD |
| [WHEA_PCIEXPRESS_DEVICE_TYPE enumeration](ne-ntddk--whea-pciexpress-device-type.md) | TBD |
| [PCI_HARDWARE_INTERFACE enumeration](ne-ntddk--pci-hardware-interface.md) | TBD |
| [SUBSYSTEM_INFORMATION_TYPE enumeration](ne-ntddk--subsystem-information-type.md) | Indicates the type of subsystem for a process or thread. This enumeration is used in NtQueryInformationProcess and NtQueryInformationThread calls. |
| [HARDWARE_COUNTER_TYPE enumeration](ne-ntddk--hardware-counter-type.md) | The HARDWARE_COUNTER_TYPE enumeration specifies the type of a hardware counter. |
| [BDCB_CLASSIFICATION enumeration](ne-ntddk--bdcb-classification.md) | The BDCB_CLASSIFICATION enumeration lists different classifications of boot start images. |
| [PROCESS_MITIGATION_POLICY enumeration](ne-ntddk--process-mitigation-policy.md) | TBD |
| [INTERLOCKED_RESULT enumeration](ne-ntddk--interlocked-result.md) | TBD |
| [INTERLOCKED_RESULT enumeration](ne-ntddk--interlocked-result~r2.md) | TBD |
| [PCI_BUS_WIDTH enumeration](ne-ntddk-pci-bus-width.md) | TBD |
| [PCI_EXPRESS_MAX_PAYLOAD_SIZE enumeration](ne-ntddk-pci-express-max-payload-size.md) | TBD |
| [PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR_TYPE enumeration](ne-ntddk--physical-counter-resource-descriptor-type.md) | The PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR_TYPE enumeration contains constants that indicate the type of hardware performance counter resource that is described by a PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structure. |
| [ARBITER_RESULT enumeration](ne-ntddk--arbiter-result.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [pHalExamineMBR callback function](nc-ntddk-phalexaminembr.md) | TBD |
| [pKdGetAcpiTablePhase0 callback function](nc-ntddk-pkdgetacpitablephase0.md) | TBD |
| [PCREATE_PROCESS_NOTIFY_ROUTINE callback](nc-ntddk-pcreate-process-notify-routine.md) | Process-creation callback implemented by a driver to track the system-wide creation and deletion of processes against the driver's internal state. |
| [pHalIoWritePartitionTable callback function](nc-ntddk-phaliowritepartitiontable.md) | TBD |
| [PDRIVER_EXCPTN_CALLBACK callback function](nc-ntddk-pdriver-excptn-callback~r1.md) | TBD |
| [pKdUnmapVirtualAddress callback function](nc-ntddk-pkdunmapvirtualaddress.md) | TBD |
| [PSHED_PI_RETRIEVE_ERROR_INFO callback](nc-ntddk-pshed-pi-retrieve-error-info.md) | A PSHED plug-in's RetrieveErrorInfo callback function retrieves platform-specific error information about a hardware error that has occurred. |
| [PCI_ERROR_HANDLER_CALLBACK callback function](nc-ntddk-pci-error-handler-callback.md) | TBD |
| [pHalGetInterruptTranslator callback function](nc-ntddk-phalgetinterrupttranslator.md) | TBD |
| [PciReadWriteConfig callback function](nc-ntddk-pcireadwriteconfig.md) | TBD |
| [pHalInitPowerManagement callback function](nc-ntddk-phalinitpowermanagement.md) | TBD |
| [PLOAD_IMAGE_NOTIFY_ROUTINE callback](nc-ntddk-pload-image-notify-routine.md) | Called by the operating system to notify the driver when a driver image or a user image (for example, a DLL or EXE) is mapped into virtual memory. |
| [PIO_QUERY_DEVICE_ROUTINE callback function](nc-ntddk-pio-query-device-routine.md) | TBD |
| [RTL_GENERIC_FREE_ROUTINE callback function](nc-ntddk-rtl-generic-free-routine.md) | TBD |
| [PHALMCAINTERFACELOCK callback function](nc-ntddk-phalmcainterfacelock.md) | TBD |
| [PCI_PREPARE_MULTISTAGE_RESUME callback function](nc-ntddk-pci-prepare-multistage-resume.md) | TBD |
| [pKdSetupIntegratedDeviceForDebugging callback function](nc-ntddk-pkdsetupintegrateddevicefordebugging.md) | TBD |
| [PCREATE_THREAD_NOTIFY_ROUTINE callback](nc-ntddk-pcreate-thread-notify-routine.md) | A callback routine implemented by a driver to notify the caller when a thread is created or deleted. |
| [PMM_ROTATE_COPY_CALLBACK_FUNCTION callback function](nc-ntddk-pmm-rotate-copy-callback-function.md) | TBD |
| [PDRIVER_VERIFIER_THUNK_ROUTINE callback function](nc-ntddk-pdriver-verifier-thunk-routine.md) | TBD |
| [PHAL_RESET_DISPLAY_PARAMETERS callback function](nc-ntddk-phal-reset-display-parameters.md) | TBD |
| [PSHED_PI_CLEAR_ERROR_STATUS callback](nc-ntddk-pshed-pi-clear-error-status.md) | A PSHED plug-in's ClearErrorStatus callback function clears any platform-specific error status registers for a corrected hardware error condition. |
| [pHalSetSystemInformation callback function](nc-ntddk-phalsetsysteminformation.md) | TBD |
| [pHalAssignSlotResources callback function](nc-ntddk-phalassignslotresources.md) | TBD |
| [PDRIVER_EXCPTN_CALLBACK callback function](nc-ntddk-pdriver-excptn-callback.md) | TBD |
| [PDRIVER_EXCPTN_CALLBACK callback function](nc-ntddk-pdriver-excptn-callback~r2.md) | TBD |
| [PSHED_PI_ENABLE_ERROR_SOURCE callback](nc-ntddk-pshed-pi-enable-error-source.md) | A PSHED plug-in's EnableErrorSource callback function enables an error source. |
| [PSHED_PI_GET_ERROR_SOURCE_INFO callback](nc-ntddk-pshed-pi-get-error-source-info.md) | A PSHED plug-in's GetErrorSourceInfo callback function returns an error source descriptor structure that represents a particular error source that is implemented by the hardware platform. |
| [RTL_GENERIC_COMPARE_ROUTINE callback function](nc-ntddk-rtl-generic-compare-routine.md) | TBD |
| [pKdMapPhysicalMemory64 callback function](nc-ntddk-pkdmapphysicalmemory64.md) | TBD |
| [pHalVectorToIDTEntry callback function](nc-ntddk-phalvectortoidtentry.md) | TBD |
| [PSHED_PI_GET_INJECTION_CAPABILITIES callback](nc-ntddk-pshed-pi-get-injection-capabilities.md) | A PSHED plug-in's GetInjectionCapabilities callback function returns an error injection capabilities union that describes the types of hardware errors that can be injected into the hardware platform. |
| [PTIMER_APC_ROUTINE callback function](nc-ntddk-ptimer-apc-routine.md) | TBD |
| [PSHED_PI_INJECT_ERROR callback](nc-ntddk-pshed-pi-inject-error.md) | A PSHED plug-in's InjectError callback function injects an error into the hardware platform. |
| [PFNFTH callback function](nc-ntddk-pfnfth.md) | TBD |
| [PHALIOREADWRITEHANDLER callback function](nc-ntddk-phalioreadwritehandler.md) | TBD |
| [PCI_PIN_TO_LINE callback function](nc-ntddk-pci-pin-to-line.md) | TBD |
| [SILO_MONITOR_CREATE_CALLBACK callback](nc-ntddk-silo-monitor-create-callback.md) | This is callback is invoked when a new silo is created. |
| [PSHED_PI_READ_ERROR_RECORD callback](nc-ntddk-pshed-pi-read-error-record.md) | A PSHED plug-in's ReadErrorRecord callback function reads an error record from the system's persistent data storage. |
| [pHalEndMirroring callback function](nc-ntddk-phalendmirroring.md) | TBD |
| [RTL_RUN_ONCE_INIT_FN callback function](nc-ntddk-rtl-run-once-init-fn.md) | TBD |
| [PTRANSLATE_RESOURCE_HANDLER callback function](nc-ntddk-ptranslate-resource-handler.md) | TBD |
| [SILO_CONTEXT_CLEANUP_CALLBACK callback](nc-ntddk-silo-context-cleanup-callback.md) | This callback is invoked when the context object reaches a reference count of zero. |
| [pHalTranslateBusAddress callback function](nc-ntddk-phaltranslatebusaddress.md) | TBD |
| [HVL_WHEA_ERROR_NOTIFICATION callback function](nc-ntddk-hvl-whea-error-notification.md) | TBD |
| [PSHED_PI_SET_ERROR_SOURCE_INFO callback](nc-ntddk-pshed-pi-set-error-source-info.md) | A PSHED plug-in's SetErrorSourceInfo callback function configures an error source. |
| [PciPin2Line callback function](nc-ntddk-pcipin2line.md) | TBD |
| [PCREATE_PROCESS_NOTIFY_ROUTINE_EX callback](nc-ntddk-pcreate-process-notify-routine-ex.md) | A callback routine implemented by a driver to notify the caller when a process is created or exits. |
| [PTRANSLATE_RESOURCE_REQUIREMENTS_HANDLER callback function](nc-ntddk-ptranslate-resource-requirements-handler.md) | TBD |
| [pHalQuerySystemInformation callback function](nc-ntddk-phalquerysysteminformation.md) | TBD |
| [pHalEndOfBoot callback function](nc-ntddk-phalendofboot.md) | TBD |
| [PciLine2Pin callback function](nc-ntddk-pciline2pin.md) | TBD |
| [pHalIoReadPartitionTable callback function](nc-ntddk-phalioreadpartitiontable.md) | TBD |
| [PDRIVER_CMC_EXCEPTION_CALLBACK callback function](nc-ntddk-pdriver-cmc-exception-callback.md) | TBD |
| [PCI_ROOT_BUS_CAPABILITY callback function](nc-ntddk-pci-root-bus-capability.md) | TBD |
| [RTL_AVL_FREE_ROUTINE callback function](nc-ntddk-rtl-avl-free-routine.md) | TBD |
| [PCI_LINE_TO_PIN callback function](nc-ntddk-pci-line-to-pin.md) | TBD |
| [pKdReleasePciDeviceForDebugging callback function](nc-ntddk-pkdreleasepcidevicefordebugging.md) | TBD |
| [PHALMCAINTERFACEREADREGISTER callback function](nc-ntddk-phalmcainterfacereadregister.md) | TBD |
| [pHalHaltSystem callback function](nc-ntddk-phalhaltsystem.md) | TBD |
| [SILO_MONITOR_TERMINATE_CALLBACK callback](nc-ntddk-silo-monitor-terminate-callback.md) | This callback is invoked when a silo is terminated. |
| [PSHED_PI_DISABLE_ERROR_SOURCE callback](nc-ntddk-pshed-pi-disable-error-source.md) | A PSHED plug-in's DisableErrorSource callback function disables an error source. |
| [PSHED_PI_FINALIZE_ERROR_RECORD callback](nc-ntddk-pshed-pi-finalize-error-record.md) | A PSHED plug-in's FinalizeErrorRecord callback function adds supplementary error record sections to an error record that more fully describe the error condition. |
| [PDRIVER_CPE_EXCEPTION_CALLBACK callback function](nc-ntddk-pdriver-cpe-exception-callback.md) | TBD |
| [pKdReleaseIntegratedDeviceForDebugging callback function](nc-ntddk-pkdreleaseintegrateddevicefordebugging.md) | TBD |
| [pHalIoSetPartitionInformation callback function](nc-ntddk-phaliosetpartitioninformation.md) | TBD |
| [PCI_EXPRESS_WAKE_CONTROL callback function](nc-ntddk-pci-express-wake-control.md) | TBD |
| [PCI_READ_WRITE_CONFIG callback function](nc-ntddk-pci-read-write-config.md) | TBD |
| [pHalInitPnpDriver callback function](nc-ntddk-phalinitpnpdriver.md) | TBD |
| [pKdGetPciDataByOffset callback function](nc-ntddk-pkdgetpcidatabyoffset.md) | TBD |
| [PGET_LOCATION_STRING callback function](nc-ntddk-pget-location-string.md) | TBD |
| [PSHED_PI_WRITE_ERROR_RECORD callback](nc-ntddk-pshed-pi-write-error-record.md) | A PSHED plug-in's WriteErrorRecord callback function writes an error record to the system's persistent data storage. |
| [pKdSetPciDataByOffset callback function](nc-ntddk-pkdsetpcidatabyoffset.md) | TBD |
| [PSHED_PI_CLEAR_ERROR_RECORD callback](nc-ntddk-pshed-pi-clear-error-record.md) | A PSHED plug-in's ClearErrorRecord callback function clears the specified error record from the system's persistent data storage. |
| [PDEBUG_DEVICE_FOUND_FUNCTION callback function](nc-ntddk-pdebug-device-found-function.md) | TBD |
| [PHALMCAINTERFACEUNLOCK callback function](nc-ntddk-phalmcainterfaceunlock.md) | TBD |
| [pHalSetPciErrorHandlerCallback callback function](nc-ntddk-phalsetpcierrorhandlercallback.md) | TBD |
| [pHalGetAcpiTable callback function](nc-ntddk-phalgetacpitable.md) | TBD |
| [pHalQueryBusSlots callback function](nc-ntddk-phalquerybusslots.md) | TBD |
| [RTL_GENERIC_ALLOCATE_ROUTINE callback function](nc-ntddk-rtl-generic-allocate-routine.md) | TBD |
| [PSHED_PI_GET_ALL_ERROR_SOURCES callback](nc-ntddk-pshed-pi-get-all-error-sources.md) | A PSHED plug-in's GetAllErrorSources callback function returns a list of error source descriptor structures that represents all of the error sources that are implemented by the hardware platform. |
| [pKdSetupPciDeviceForDebugging callback function](nc-ntddk-pkdsetuppcidevicefordebugging.md) | TBD |
| [pHalHandlerForBus callback function](nc-ntddk-phalhandlerforbus.md) | TBD |
| [pHalResetDisplay callback function](nc-ntddk-phalresetdisplay.md) | TBD |
| [PSHED_PI_ATTEMPT_ERROR_RECOVERY callback](nc-ntddk-pshed-pi-attempt-error-recovery.md) | A PSHED plug-in's AttemptRecovery callback function attempts to recover from a recoverable hardware error. |
| [pHalMirrorPhysicalMemory callback function](nc-ntddk-phalmirrorphysicalmemory.md) | TBD |
| [pHalMirrorVerify callback function](nc-ntddk-phalmirrorverify.md) | TBD |
| [RTL_AVL_ALLOCATE_ROUTINE callback function](nc-ntddk-rtl-avl-allocate-routine.md) | TBD |
| [pKdEnumerateDebuggingDevices callback function](nc-ntddk-pkdenumeratedebuggingdevices.md) | TBD |
| [RTL_AVL_COMPARE_ROUTINE callback function](nc-ntddk-rtl-avl-compare-routine.md) | TBD |
| [PFN_IN_USE_PAGE_OFFLINE_NOTIFY callback function](nc-ntddk-pfn-in-use-page-offline-notify.md) | TBD |
| [PARBITER_HANDLER callback function](nc-ntddk-parbiter-handler.md) | TBD |
| [RTL_AVL_MATCH_FUNCTION callback function](nc-ntddk-rtl-avl-match-function.md) | TBD |
| [pHalFindBusAddressTranslation callback function](nc-ntddk-phalfindbusaddresstranslation.md) | TBD |
| [pKdCheckPowerButton callback function](nc-ntddk-pkdcheckpowerbutton.md) | TBD |
| [EXPAND_STACK_CALLOUT callback function](nc-ntddk-expand-stack-callout.md) | TBD |
| [pHalReferenceBusHandler callback function](nc-ntddk-phalreferencebushandler.md) | TBD |
| [pHalStartMirroring callback function](nc-ntddk-phalstartmirroring.md) | TBD |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_AVIO_MODIFY_STREAM IOCTL](ni-ntddk-ioctl-avio-modify-stream.md) | TBD |
| [IOCTL_AVIO_FREE_STREAM IOCTL](ni-ntddk-ioctl-avio-free-stream.md) | TBD |
| [IOCTL_AVIO_ALLOCATE_STREAM IOCTL](ni-ntddk-ioctl-avio-allocate-stream.md) | TBD |

This header is used in these topics:

- [PCI](..content/_PCI)
- [whea](..content/_whea)
- [ifsk](..content/_ifsk)
- [kernel](..content/_kernel)
- [Storage](..content/_Storage)
- [devtest](..content/_devtest)
