# Ntddk.h header


This header is used by Windows kernel, Installable file system, PCI, Windows Hardware Error Architecture (WHEA), Storage, Driver test tools. For more information, see
- [Windows kernel](../_kernel/index.md)
- [Installable file system](../_ifsk/index.md)
- [PCI](../_PCI/index.md)
- [Windows Hardware Error Architecture (WHEA)](../_whea/index.md)
- [Storage](../_storage/index.md)
- [Driver test tools](../_devtest/index.md)

Ntddk.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [DbgPrompt function](nf-ntddk-dbgprompt.md) | The DbgPrompt routine displays a caller-specified user prompt string on the kernel debugger's display device and obtains a user response string. |
| [ExFreePool function](nf-ntddk-exfreepool.md) | The ExFreePool routine deallocates a block of pool memory. |
| [ExRaiseAccessViolation function](nf-ntddk-exraiseaccessviolation.md) | The ExRaiseAccessViolation routine can be used with structured exception handling to throw a driver-determined exception for a memory access violation that occurs when a driver processes I/O requests. |
| [ExRaiseDatatypeMisalignment function](nf-ntddk-exraisedatatypemisalignment.md) | The ExRaiseDatatypeMisalignment routine can be used with structured exception handling to throw a driver-determined exception for a misaligned data type that occurs when a driver processes I/O requests. |
| [ExUuidCreate function](nf-ntddk-exuuidcreate.md) | The ExUuidCreate routine initializes a UUID (GUID) structure to a newly generated value. |
| [FsRtlIsTotalDeviceFailure function](nf-ntddk-fsrtlistotaldevicefailure.md) | The FsRtlIsTotalDeviceFailure routine determines whether a media or other hardware failure has occurred. |
| [HalAllocateHardwareCounters function](nf-ntddk-halallocatehardwarecounters.md) | The HalAllocateHardwareCounters routine allocates a set of hardware performance counters. |
| [HalExamineMBR function](nf-ntddk-halexaminembr.md) | The HalExamineMBR routine reads the master boot record (MBR) of a disk and returns data from the MBR if the MBR is of the type specified by the caller. |
| [HalFreeHardwareCounters function](nf-ntddk-halfreehardwarecounters.md) | The HalFreeHardwareCounters routine frees a set of hardware performance counters that was acquired in a previous call to HalAllocateHardwareCounters routine. |
| [IoAllocateController function](nf-ntddk-ioallocatecontroller.md) | The IoAllocateController routine sets up the call to a driver-supplied ControllerControl routine as soon as the device controller, represented by the given controller object, is available to carry out an I/O operation for the target device, represented by the given device object. |
| [IoAssignArcName function](nf-ntddk-ioassignarcname.md) | The IoAssignArcName routine creates a symbolic link between the ARC name of a physical device and the name of the corresponding device object when it has been created. |
| [IoAttachDeviceToDeviceStackSafe function](nf-ntddk-ioattachdevicetodevicestacksafe.md) | The IoAttachDeviceToDeviceStackSafe routine attaches the caller's device object to the topmost device object in a driver stack. |
| [IoCancelFileOpen function](nf-ntddk-iocancelfileopen.md) | The IoCancelFileOpen routine can be used by a file system filter driver to close a file that has been opened by a file system driver in the filter driver's device stack. |
| [IoClearActivityIdThread function](nf-ntddk-ioclearactivityidthread.md) | The IoClearActivityIdThread routine clears the activity ID of the current thread. |
| [IoCreateController function](nf-ntddk-iocreatecontroller.md) | The IoCreateController routine allocates memory for and initializes a controller object with a controller extension of a driver-determined size. |
| [IoCreateDisk function](nf-ntddk-iocreatedisk.md) | The IoCreateDisk routine initializes a raw disk by creating a new partition table. |
| [IoCreateFileEx function](nf-ntddk-iocreatefileex.md) | The IoCreateFileEx routine either causes a new file or directory to be created, or opens an existing file, device, directory, or volume and gives the caller a handle for the file object. |
| [IoCreateFileSpecifyDeviceObjectHint function](nf-ntddk-iocreatefilespecifydeviceobjecthint.md) | The IoCreateFileSpecifyDeviceObjectHint routine is used by file system filter drivers to send a create request only to the filters below a specified device object and to the file system. |
| [IoDeassignArcName function](nf-ntddk-iodeassignarcname.md) | The IoDeassignArcName routine removes a symbolic link between the ARC name for a device and the named device object. |
| [IoDecrementKeepAliveCount function](nf-ntddk-iodecrementkeepalivecount.md) | The IoDecrementKeepAliveCount routine decrements a reference count associated with an Windows app on a specific device. |
| [IoDeleteController function](nf-ntddk-iodeletecontroller.md) | The IoDeleteController routine removes a given controller object from the system, for example, when the driver that created it is being unloaded. |
| [IoFreeController function](nf-ntddk-iofreecontroller.md) | The IoFreeController routine releases a previously allocated controller object when the driver has completed an I/O request. |
| [IoGetActivityIdIrp function](nf-ntddk-iogetactivityidirp.md) | The IoGetActivityIdIrp routine retrieves the current activity ID associated with an IRP. |
| [IoGetActivityIdThread function](nf-ntddk-iogetactivityidthread.md) | The IoGetActivityIdThread routine returns the activity ID associated with the current thread. |
| [IoGetConfigurationInformation function](nf-ntddk-iogetconfigurationinformation.md) | The IoGetConfigurationInformation routine returns a pointer to the I/O manager's global configuration information structure, which contains the current values for how many physical disk, floppy, CD-ROM, tape, SCSI HBA, serial, and parallel devices have device objects created to represent them by drivers as they are loaded. |
| [IoGetFileObjectGenericMapping function](nf-ntddk-iogetfileobjectgenericmapping.md) | The IoGetFileObjectGenericMapping routine returns information about the mapping between each generic access right and the set of specific access rights for file objects. |
| [IoGetInitiatorProcess function](nf-ntddk-iogetinitiatorprocess.md) | The IoGetInitiatorProcess routine retrieves the process which initiated the creation of a file object if different than the process which is issuing the create. |
| [IoGetOplockKeyContext function](nf-ntddk-iogetoplockkeycontext.md) | The IoGetOplockKeyContext routine returns a target oplock key context for a file object. |
| [IoGetOplockKeyContextEx function](nf-ntddk-iogetoplockkeycontextex.md) | The IoGetOplockKeyContextEx routine returns a parent and target oplock key context for a file object. |
| [IoGetPagingIoPriority function](nf-ntddk-iogetpagingiopriority.md) | The IoGetPagingIoPriority routine indicates the priority level of a paging I/O request. |
| [IoGetSiloParameters function](nf-ntddk-iogetsiloparameters.md) | This routine indicates if a file is within a Container context. |
| [IoGetTransactionParameterBlock function](nf-ntddk-iogettransactionparameterblock.md) | The IoGetTransactionParameterBlock routine returns the transaction parameter block for a transacted file operation. |
| [IoIncrementKeepAliveCount function](nf-ntddk-ioincrementkeepalivecount.md) | The IoIncrementKeepAliveCount routine increments a reference count associated with an Windows app process on a specific device. |
| [IoInitializeDriverCreateContext function](nf-ntddk-ioinitializedrivercreatecontext.md) | The IoInitializeDriverCreateContext routine initializes a caller-allocated variable of type IO_DRIVER_CREATE_CONTEXT. |
| [IoIsFileObjectIgnoringSharing function](nf-ntddk-ioisfileobjectignoringsharing.md) | The IoIsFileObjectIgnoringSharing routine determines if a file object is set with the option to ignore file sharing access checks. |
| [IoIsFileOriginRemote function](nf-ntddk-ioisfileoriginremote.md) | The IoIsFileOriginRemote routine determines whether a given file object is for a remote create request. |
| [IoIsValidIrpStatus function](nf-ntddk-ioisvalidirpstatus.md) | The IoIsValidIrpStatus routine validates the specified NTSTATUS status code value. |
| [IoMakeAssociatedIrp function](nf-ntddk-iomakeassociatedirp.md) | This routine is reserved for use by file systems and file system filter drivers. |
| [IoPropagateActivityIdToThread function](nf-ntddk-iopropagateactivityidtothread.md) | The IoPropagateActivityIdToThread routine associates the activity ID from an IRP with the current thread. |
| [IoQueryFullDriverPath function](nf-ntddk-ioqueryfulldriverpath.md) | The IoQueryFullDriverPath routine retrieves the full path name of the binary file that is loaded for the specified driver object. |
| [IoRaiseHardError function](nf-ntddk-ioraiseharderror.md) | The IoRaiseHardError routine causes a dialog box to appears that warns the user that a device I/O error has occurred, which might indicate that a physical device is failing. |
| [IoRaiseInformationalHardError function](nf-ntddk-ioraiseinformationalharderror.md) | The IoRaiseInformationalHardError routine sends a dialog box to the user, warning about a device I/O error that indicates why a user I/O request failed. |
| [IoReadDiskSignature function](nf-ntddk-ioreaddisksignature.md) | The IoReadDiskSignature routine reads the disk signature information for the partition table of a disk. |
| [IoReadPartitionTable function](nf-ntddk-ioreadpartitiontable.md) | The IoReadPartitionTable routine is obsolete and is provided only to support existing drivers. |
| [IoReadPartitionTableEx function](nf-ntddk-ioreadpartitiontableex.md) | The IoReadPartitionTableEx routine reads a list of partitions on a disk having a specified sector size and creates an entry in the partition list for each recognized partition. |
| [IoRegisterBootDriverCallback function](nf-ntddk-ioregisterbootdrivercallback.md) | The IoRegisterBootDriverCallback routine registers a BOOT_DRIVER_CALLBACK_FUNCTION routine to be called during the initialization of a boot-start driver and its dependent DLLs. |
| [IoRegisterBootDriverReinitialization function](nf-ntddk-ioregisterbootdriverreinitialization.md) | The IoRegisterBootDriverReinitialization routine is called by a boot driver to register the driver's reinitialization routine with the I/O manager to be called after all devices have been enumerated and started. |
| [IoRegisterDriverReinitialization function](nf-ntddk-ioregisterdriverreinitialization.md) | The IoRegisterDriverReinitialization routine is called by a driver during its initialization or reinitialization to register its Reinitialize routine to be called again before the driver's and, possibly the system's, initialization is complete. |
| [IoReportDetectedDevice function](nf-ntddk-ioreportdetecteddevice.md) | The IoReportDetectedDevice routine reports a non-PnP device to the PnP manager. |
| [IoReportResourceForDetection function](nf-ntddk-ioreportresourcefordetection.md) | The IoReportResourceForDetection routine claims hardware resources in the configuration registry for a legacy device. |
| [IoReportRootDevice function](nf-ntddk-ioreportrootdevice.md) | The IoReportRootDevice routine reports a device that cannot be detected by a PnP bus driver to the PnP Manager. IoReportRootDevice allows only one device per driver to be created. |
| [IoSetActivityIdIrp function](nf-ntddk-iosetactivityidirp.md) | The IoSetActivityIdIrp routine associates an activity ID with an IRP. |
| [IoSetActivityIdThread function](nf-ntddk-iosetactivityidthread.md) | The IoSetActivityIdThread routine associates an activity ID with the current thread. Drivers should use this routine when they are tracing aware and are issuing I/O on a worker thread. |
| [IoSetFileObjectIgnoreSharing function](nf-ntddk-iosetfileobjectignoresharing.md) | The IoSetFileObjectIgnoreSharing routine sets a file object to ignore file sharing access checks. |
| [IoSetFileOrigin function](nf-ntddk-iosetfileorigin.md) | The IoSetFileOrigin routine specifies whether a given file object is for a remote create request. |
| [IoSetHardErrorOrVerifyDevice function](nf-ntddk-iosetharderrororverifydevice.md) | Lower-level drivers call the IoSetHardErrorOrVerifyDevice routine to identify a removable media device that has encountered an error, so that a file system driver can prompt the user to verify that the medium is valid. |
| [IoSetMasterIrpStatus function](nf-ntddk-iosetmasterirpstatus.md) | The IoSetMasterIrpStatus routine conditionally replaces the Status value in an IRP with the specified NTSTATUS value. |
| [IoSetPartitionInformation function](nf-ntddk-iosetpartitioninformation.md) | The IoSetPartitionInformation routine is obsolete and is provided only to support existing drivers. |
| [IoSetPartitionInformationEx function](nf-ntddk-iosetpartitioninformationex.md) | For the disk represented by DeviceObject, the IoSetPartitionInformationEx routine initializes a partition table entry with the information specified in the SET_PARTITION_INFORMATION_EX structure. |
| [IoSetSystemPartition function](nf-ntddk-iosetsystempartition.md) | The IoSetSystemPartition routine sets the boot partition for the system. |
| [IoSetThreadHardErrorMode function](nf-ntddk-iosetthreadharderrormode.md) | The IoSetThreadHardErrorMode routine enables or disables hard error reporting for the current thread. |
| [IoTransferActivityId function](nf-ntddk-iotransferactivityid.md) | The IoTransferActivityId routine logs an ETW transfer event using the I/O tracing provider on behalf of the caller. This allows a driver to associate two related activity IDs without requiring a specific provider to be enabled. |
| [IoUnregisterBootDriverCallback function](nf-ntddk-iounregisterbootdrivercallback.md) | The IoUnRegisterBootDriverCallback routine unregisters a previously registered BOOT_DRIVER_CALLBACK_FUNCTION routine. |
| [IoVerifyPartitionTable function](nf-ntddk-ioverifypartitiontable.md) | The IoVerifyPartitionTable routine checks the validity of the partition table for a disk. |
| [IoVolumeDeviceToDosName function](nf-ntddk-iovolumedevicetodosname.md) | The IoVolumeDeviceToDosName routine returns the MS-DOS path for a specified device object that represents a file system volume. |
| [IoWritePartitionTable function](nf-ntddk-iowritepartitiontable.md) | The IoWritePartitionTable routine is obsolete and is provided only to support existing drivers. |
| [IoWritePartitionTableEx function](nf-ntddk-iowritepartitiontableex.md) | The IoWritePartitionTableEx routine writes partition tables from the entries in the partition list buffer for each partition on the disk represented by the given device object. |
| [KeAreApcsDisabled function](nf-ntddk-keareapcsdisabled.md) | The KeAreApcsDisabled routine returns whether the calling thread is within a critical region or a guarded region, which disables normal kernel APC delivery. |
| [KeBugCheck function](nf-ntddk-kebugcheck.md) | The KeBugCheck routine brings down the system in a controlled manner when the caller discovers an unrecoverable inconsistency that would corrupt the system if the caller continued to run. |
| [KeEnterCriticalRegion function](nf-ntddk-keentercriticalregion.md) | The KeEnterCriticalRegion routine temporarily disables the execution of normal kernel APCs, but does not prevent special kernel APCs from running. |
| [KeEnterGuardedRegion function](nf-ntddk-keenterguardedregion.md) | The KeEnterGuardedRegion routine enters a guarded region, which disables all kernel-mode APC delivery to the current thread. |
| [KeExpandKernelStackAndCallout function](nf-ntddk-keexpandkernelstackandcallout.md) | The KeExpandKernelStackAndCallout routine calls a routine with a guaranteed amount of stack space. |
| [KeGetCurrentNodeNumber function](nf-ntddk-kegetcurrentnodenumber.md) | The KeGetCurrentNodeNumber routine gets the NUMA node number for the logical processor that the caller is running on. |
| [KeGetCurrentProcessorNumber function](nf-ntddk-kegetcurrentprocessornumber.md) | The KeGetCurrentProcessorNumber routine returns the system-assigned number of the current processor on which the caller is running. |
| [KeGetCurrentProcessorNumber function](nf-ntddk-kegetcurrentprocessornumber~r1.md) | The KeGetCurrentProcessorNumber routine returns the system-assigned number of the current processor on which the caller is running. |
| [KeGetCurrentProcessorNumber function](nf-ntddk-kegetcurrentprocessornumber~r2.md) | The KeGetCurrentProcessorNumber routine returns the system-assigned number of the current processor on which the caller is running. |
| [KeGetCurrentProcessorNumber function](nf-ntddk-kegetcurrentprocessornumber~r3.md) | The KeGetCurrentProcessorNumber routine returns the system-assigned number of the current processor on which the caller is running. |
| [KeGetCurrentProcessorNumberEx function](nf-ntddk-kegetcurrentprocessornumberex.md) | The KeGetCurrentProcessorNumberEx routine gets the processor number of the logical processor that the caller is running on. |
| [KeInvalidateAllCaches function](nf-ntddk-keinvalidateallcaches.md) | The KeInvalidateAllCaches routine flushes all processor caches. |
| [KeLeaveCriticalRegion function](nf-ntddk-keleavecriticalregion.md) | The KeLeaveCriticalRegion routine reenables the delivery of normal kernel-mode APCs that were disabled by a preceding call to KeEnterCriticalRegion. |
| [KeLeaveGuardedRegion function](nf-ntddk-keleaveguardedregion.md) | The KeLeaveGuardedRegion routine exits a guarded region entered by KeEnterGuardedRegion. |
| [KePulseEvent function](nf-ntddk-kepulseevent.md) | The KePulseEvent routine atomically sets an event object to a signaled state, attempts to satisfy as many waits as possible, and then resets the event object to a not-signaled state. |
| [KeQueryActiveGroupCount function](nf-ntddk-kequeryactivegroupcount.md) | The KeQueryActiveGroupCount routine returns the number of active processor groups in a multiprocessor system. |
| [KeQueryActiveProcessorCount function](nf-ntddk-kequeryactiveprocessorcount.md) | The KeQueryActiveProcessorCount routine returns the number of currently active processors. |
| [KeQueryActiveProcessorCountEx function](nf-ntddk-kequeryactiveprocessorcountex.md) | The KeQueryActiveProcessorCountEx routine returns the number of active logical processors in a specified group in a multiprocessor system or in the entire system. |
| [KeQueryActiveProcessors function](nf-ntddk-kequeryactiveprocessors.md) | The KeQueryActiveProcessors routine returns a bitmask of the currently active processors. |
| [KeQueryGroupAffinity function](nf-ntddk-kequerygroupaffinity.md) | The KeQueryGroupAffinity routine returns an affinity mask that identifies the active logical processors in a specified group in a multiprocessor system. |
| [KeQueryHardwareCounterConfiguration function](nf-ntddk-kequeryhardwarecounterconfiguration.md) | The KeQueryHardwareCounterConfiguration routine queries the operating system for the list of hardware counters to use for thread profiling. |
| [KeQueryHighestNodeNumber function](nf-ntddk-kequeryhighestnodenumber.md) | The KeQueryHighestNodeNumber routine returns the highest node number in a multiprocessor system that has a non-uniform memory access (NUMA) architecture. |
| [KeQueryLogicalProcessorRelationship function](nf-ntddk-kequerylogicalprocessorrelationship.md) | The KeQueryLogicalProcessorRelationship routine gets information about the relationships of one or more processors to the other processors in a multiprocessor system. |
| [KeQueryMaximumGroupCount function](nf-ntddk-kequerymaximumgroupcount.md) | The KeQueryMaximumGroupCount routine returns the maximum number of groups in a multiprocessor system. |
| [KeQueryMaximumProcessorCount function](nf-ntddk-kequerymaximumprocessorcount.md) | The KeQueryMaximumProcessorCount routine returns the maximum number of processors. |
| [KeQueryMaximumProcessorCountEx function](nf-ntddk-kequerymaximumprocessorcountex.md) | The KeQueryMaximumProcessorCountEx routine returns the maximum number of logical processors in a specified group in a multiprocessor system. |
| [KeQueryNodeActiveAffinity function](nf-ntddk-kequerynodeactiveaffinity.md) | The KeQueryNodeActiveAffinity routine gets the current processor affinity of a specified node in a multiprocessor system that has a non-uniform memory access (NUMA) architecture. |
| [KeQueryNodeMaximumProcessorCount function](nf-ntddk-kequerynodemaximumprocessorcount.md) | The KeQueryNodeMaximumProcessorCount routine returns the maximum number of logical processors that a specified node in a non-uniform memory access (NUMA) multiprocessor system can contain. |
| [KeQueryTickCount function](nf-ntddk-kequerytickcount.md) | The KeQueryTickCount routine maintains a count of the interval timer interrupts that have occurred since the system was booted. |
| [KeQueryTickCount function](nf-ntddk-kequerytickcount~r1.md) | The KeQueryTickCount routine maintains a count of the interval timer interrupts that have occurred since the system was booted. |
| [KeQueryTickCount function](nf-ntddk-kequerytickcount~r2.md) | The KeQueryTickCount routine maintains a count of the interval timer interrupts that have occurred since the system was booted. |
| [KeRaiseIrqlToDpcLevel function](nf-ntddk-keraiseirqltodpclevel.md) | The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [KeRaiseIrqlToDpcLevel function](nf-ntddk-keraiseirqltodpclevel~r1.md) | The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [KeRaiseIrqlToDpcLevel function](nf-ntddk-keraiseirqltodpclevel~r2.md) | The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [KeRaiseIrqlToDpcLevel function](nf-ntddk-keraiseirqltodpclevel~r3.md) | The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [KeSetBasePriorityThread function](nf-ntddk-kesetbaseprioritythread.md) | The KeSetBasePriorityThread routine sets the run-time priority, relative to the current process, for a given thread. |
| [KeSetHardwareCounterConfiguration function](nf-ntddk-kesethardwarecounterconfiguration.md) | The KeSetHardwareCounterConfiguration routine specifies a list of hardware counters to use for thread profiling. |
| [KeSetImportanceDpc function](nf-ntddk-kesetimportancedpc.md) | The KeSetImportanceDpc routine specifies how soon the DPC routine is run. |
| [KeSetTargetProcessorDpc function](nf-ntddk-kesettargetprocessordpc.md) | The KeSetTargetProcessorDpc routine specifies the processor that a DPC routine will be run on. |
| [MmAllocateContiguousMemory function](nf-ntddk-mmallocatecontiguousmemory.md) | The MmAllocateContiguousMemory routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space. |
| [MmAllocateContiguousMemorySpecifyCache function](nf-ntddk-mmallocatecontiguousmemoryspecifycache.md) | The MmAllocateContiguousMemorySpecifyCache routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space. |
| [MmAllocateContiguousMemorySpecifyCacheNode function](nf-ntddk-mmallocatecontiguousmemoryspecifycachenode.md) | The MmAllocateContiguousMemorySpecifyCacheNode routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space. |
| [MmAllocateNonCachedMemory function](nf-ntddk-mmallocatenoncachedmemory.md) | The MmAllocateNonCachedMemory routine allocates a virtual address range of noncached and cache-aligned memory. |
| [MmCopyMemory function](nf-ntddk-mmcopymemory.md) | The MmCopyMemory routine copies the specified range of virtual or physical memory into the caller-supplied buffer. |
| [MmFreeContiguousMemory function](nf-ntddk-mmfreecontiguousmemory.md) | The MmFreeContiguousMemory routine releases a range of physically contiguous memory that was allocated by an MmAllocateContiguousMemoryXxx routine. |
| [MmFreeContiguousMemorySpecifyCache function](nf-ntddk-mmfreecontiguousmemoryspecifycache.md) | The MmFreeContiguousMemorySpecifyCache routine frees a buffer that was allocated by an MmAllocateContiguousMemorySpecifyCacheXxx routine. |
| [MmFreeNonCachedMemory function](nf-ntddk-mmfreenoncachedmemory.md) | The MmFreeNonCachedMemory routine releases a range of noncached memory that was allocated by the MmAllocateNonCachedMemory routine. |
| [MmGetPhysicalAddress function](nf-ntddk-mmgetphysicaladdress.md) | The MmGetPhysicalAddress routine returns the physical address corresponding to a valid nonpaged virtual address. |
| [MmIsAddressValid function](nf-ntddk-mmisaddressvalid.md) | The MmIsAddressValid routine checks whether a page fault will occur for a read or write operation at a given virtual address.Warning  We do not recommend using this function. |
| [MmIsThisAnNtAsSystem function](nf-ntddk-mmisthisanntassystem.md) | The MmIsThisAnNtAsSystem routine is obsolete for Windows XP and later versions of Windows. Use RtlGetVersion or RtlVerifyVersionInfo instead. |
| [MmLockPagableSectionByHandle function](nf-ntddk-mmlockpagablesectionbyhandle.md) | The MmLockPagableSectionByHandle routine locks a pageable code or data section into system memory by incrementing the reference count on the handle to the section. |
| [MmSecureVirtualMemory function](nf-ntddk-mmsecurevirtualmemory.md) | The MmSecureVirtualMemory routine secures a user-space memory address range so that it cannot be freed and its protection type cannot be made more restrictive. |
| [MmUnsecureVirtualMemory function](nf-ntddk-mmunsecurevirtualmemory.md) | The MmUnsecureVirtualMemory routine unsecures a memory address range secured by the MmSecureVirtualMemory routine. |
| [NtOpenProcess function](nf-ntddk-ntopenprocess.md) | The ZwOpenProcess routine opens a handle to a process object and sets the access rights to this object. |
| [PsAllocSiloContextSlot function](nf-ntddk-psallocsilocontextslot.md) | This routine allocates a slot that can be used to insert, retrieve, and delete an object in all silos. . |
| [PsAttachSiloToCurrentThread function](nf-ntddk-psattachsilotocurrentthread.md) | This routine places a thread temporarily into the specified Silo. |
| [PsCreateSiloContext function](nf-ntddk-pscreatesilocontext.md) | This routine creates an object that will be inserted in a Silo. |
| [PsDereferenceSiloContext function](nf-ntddk-psdereferencesilocontext.md) | This routine decrements the reference count on the object. |
| [PsDetachSiloFromCurrentThread function](nf-ntddk-psdetachsilofromcurrentthread.md) | This routine removes a thread from a silo which was added by an attach. For more info about attaching, see the PsAttachSiloToCurrentThread routine. |
| [PsFreeSiloContextSlot function](nf-ntddk-psfreesilocontextslot.md) | This routine frees the specified slot and makes it available in the system. It undoes the effects of the PsAllocSiloContextSlot routine. |
| [PsGetCurrentProcessId function](nf-ntddk-psgetcurrentprocessid.md) | The PsGetCurrentProcessId routine identifies the current thread's process. |
| [PsGetCurrentServerSilo function](nf-ntddk-psgetcurrentserversilo.md) | This routine returns the effective server silo for the thread. |
| [PsGetCurrentSilo function](nf-ntddk-psgetcurrentsilo.md) | This routine returns the current silo for the calling thread. First the thread is checked to see if it has been attached to a silo. If not, then the thread is checked to see if it is in a silo. |
| [PsGetCurrentThread function](nf-ntddk-psgetcurrentthread.md) | The PsGetCurrentThread routine identifies the current thread. |
| [PsGetCurrentThreadId function](nf-ntddk-psgetcurrentthreadid.md) | The PsGetCurrentThreadId routine identifies the current thread. |
| [PsGetCurrentThreadTeb function](nf-ntddk-psgetcurrentthreadteb.md) | The PsGetCurrentThreadTeb routine returns the Thread Environment Block (TEB) of the current thread. The call must be made in kernel-mode. |
| [PsGetEffectiveServerSilo function](nf-ntddk-psgeteffectiveserversilo.md) | This routine traverses the parent chain of the Silo until finding the effective server silo or host silo. |
| [PsGetHostSilo function](nf-ntddk-psgethostsilo.md) | This routine returns the host silo. |
| [PsGetJobServerSilo function](nf-ntddk-psgetjobserversilo.md) | This routine returns the effective ServerSilo for the job. The returned pointer is valid as long as the supplied Job object remains referenced. |
| [PsGetJobSilo function](nf-ntddk-psgetjobsilo.md) | This routine returns the first job in the hierarchy that is a Silo. The returned pointer is valid as long as the supplied Job object remains referenced. |
| [PsGetParentSilo function](nf-ntddk-psgetparentsilo.md) | Retrieves the most immediate parent silo in the hierarchy for a given job object. |
| [PsGetPermanentSiloContext function](nf-ntddk-psgetpermanentsilocontext.md) | This routine retrieves an object that was inserted in the Silo without incrementing the reference count. |
| [PsGetProcessCreateTimeQuadPart function](nf-ntddk-psgetprocesscreatetimequadpart.md) | The PsGetProcessCreateTimeQuadPart routine returns a LONGLONG value that represents the time at which the process was created. |
| [PsGetProcessId function](nf-ntddk-psgetprocessid.md) | The PsGetProcessId routine returns the process identifier (process ID) that is associated with a specified process. |
| [PsGetServerSiloActiveConsoleId function](nf-ntddk-psgetserversiloactiveconsoleid.md) | Gets the active console for the current server silo context for the supplied thread. |
| [PsGetSiloContext function](nf-ntddk-psgetsilocontext.md) | This routine retrieves the silo context from the specified silo and slot. |
| [PsGetSiloMonitorContextSlot function](nf-ntddk-psgetsilomonitorcontextslot.md) | This routine returns the silo context slot that was allocated by the monitor during the registration. |
| [PsInsertPermanentSiloContext function](nf-ntddk-psinsertpermanentsilocontext.md) | This routine inserts an object in an empty slot in a Silo. |
| [PsInsertSiloContext function](nf-ntddk-psinsertsilocontext.md) | This routine inserts an object in an empty slot in a Silo. |
| [PsIsHostSilo function](nf-ntddk-psishostsilo.md) | This routine will check if the supplied Silo is the host silo. |
| [PsMakeSiloContextPermanent function](nf-ntddk-psmakesilocontextpermanent.md) | This routine makes the slot in a silo instance read-only, allowing the object in the slot to be retrieved without affecting the reference count on that object. |
| [PsReferenceSiloContext function](nf-ntddk-psreferencesilocontext.md) | This routine increments the reference count on the object. |
| [PsRegisterSiloMonitor function](nf-ntddk-psregistersilomonitor.md) | This routine registers a server silo monitor that can receive notifications about server silo events. |
| [PsRemoveCreateThreadNotifyRoutine function](nf-ntddk-psremovecreatethreadnotifyroutine.md) | The PsRemoveCreateThreadNotifyRoutine routine removes a callback routine that was registered by the PsSetCreateThreadNotifyRoutine routine. |
| [PsRemoveLoadImageNotifyRoutine function](nf-ntddk-psremoveloadimagenotifyroutine.md) | The PsRemoveLoadImageNotifyRoutine routine removes a callback routine that was registered by the PsSetLoadImageNotifyRoutine routine. |
| [PsRemoveSiloContext function](nf-ntddk-psremovesilocontext.md) | This routine removes an object that was inserted in the Silo. |
| [PsReplaceSiloContext function](nf-ntddk-psreplacesilocontext.md) | This routine inserts an object in a Silo. |
| [PsSetCreateProcessNotifyRoutine function](nf-ntddk-pssetcreateprocessnotifyroutine.md) | The PsSetCreateProcessNotifyRoutine routine adds a driver-supplied callback routine to, or removes it from, a list of routines to be called whenever a process is created or deleted. |
| [PsSetCreateProcessNotifyRoutineEx function](nf-ntddk-pssetcreateprocessnotifyroutineex.md) | The PsSetCreateProcessNotifyRoutineEx routine registers or removes a callback routine that notifies the caller when a process is created or exits. |
| [PsSetCreateProcessNotifyRoutineEx2 function](nf-ntddk-pssetcreateprocessnotifyroutineex2.md) | The PsSetCreateProcessNotifyRoutineEx2 routine registers or removes a callback routine that notifies the caller when a process is created or deleted. |
| [PsSetCreateThreadNotifyRoutine function](nf-ntddk-pssetcreatethreadnotifyroutine.md) | The PsSetCreateThreadNotifyRoutine routine registers a driver-supplied callback that is subsequently notified when a new thread is created and when such a thread is deleted. |
| [PsSetCreateThreadNotifyRoutineEx function](nf-ntddk-pssetcreatethreadnotifyroutineex.md) | The PsSetCreateThreadNotifyRoutineEx routine registers a driver-supplied callback that is subsequently notified when a new thread is created and when such a thread is deleted. |
| [PsSetLoadImageNotifyRoutine function](nf-ntddk-pssetloadimagenotifyroutine.md) | The PsSetLoadImageNotifyRoutine routine registers a driver-supplied callback that is subsequently notified whenever an image is loaded (or mapped into memory). |
| [PsSetLoadImageNotifyRoutineEx function](nf-ntddk-pssetloadimagenotifyroutineex.md) | The PsSetLoadImageNotifyRoutineEx routine registers a driver-supplied callback that is subsequently notified whenever an image is loaded (or mapped into memory). |
| [PsStartSiloMonitor function](nf-ntddk-psstartsilomonitor.md) | This routine tries to start the server silo monitor. |
| [PsTerminateServerSilo function](nf-ntddk-psterminateserversilo.md) | This routine terminates the specified silo. |
| [PsUnregisterSiloMonitor function](nf-ntddk-psunregistersilomonitor.md) | This routine unregisters a server silo monitor. |
| [PshedAllocateMemory function](nf-ntddk-pshedallocatememory.md) | The PshedAllocateMemory function allocates a block of memory from the nonpaged pool. |
| [PshedFreeMemory function](nf-ntddk-pshedfreememory.md) | The PshedFreeMemory function frees a block of memory that was previously allocated by calling the PshedAllocateMemory function. |
| [PshedIsSystemWheaEnabled function](nf-ntddk-pshedissystemwheaenabled.md) | The PshedIsSystemWheaEnabled function returns a Boolean value that indicates whether the system is WHEA-enabled. |
| [PshedRegisterPlugin function](nf-ntddk-pshedregisterplugin.md) | The PshedRegisterPlugin function registers a PSHED plug-in with the PSHED. |
| [PshedSynchronizeExecution function](nf-ntddk-pshedsynchronizeexecution.md) | The PshedSynchronizeExecution function synchronizes the execution of a given function with the hardware error processing for an error source. |
| [RtlCharToInteger function](nf-ntddk-rtlchartointeger.md) | The RtlCharToInteger routine converts a single-byte character string to an integer value in the specified base. |
| [RtlCompareString function](nf-ntddk-rtlcomparestring.md) | The RtlCompareString routine compares two counted strings. |
| [RtlConvertLongToLuid function](nf-ntddk-rtlconvertlongtoluid.md) | The RtlConvertLongToLuid routine converts a long integer to a locally unique identifier (LUID), which is used by the system to represent a security privilege. |
| [RtlConvertUlongToLuid function](nf-ntddk-rtlconvertulongtoluid.md) | The RtlConvertUlongToLuid routine converts an unsigned long integer to a locally unique identifier (LUID), which is used by the system to represent a security privilege. |
| [RtlCopyString function](nf-ntddk-rtlcopystring.md) | The RtlCopyString routine copies a source string to a destination string. |
| [RtlDelete function](nf-ntddk-rtldelete.md) | The RtlDelete routine deletes the specified node from the splay link tree. |
| [RtlDeleteElementGenericTable function](nf-ntddk-rtldeleteelementgenerictable.md) | The RtlDeleteElementGenericTable routine deletes an element from a generic table. |
| [RtlDeleteElementGenericTableAvl function](nf-ntddk-rtldeleteelementgenerictableavl.md) | The RtlDeleteElementGenericTableAvl routine deletes an element from a generic table. |
| [RtlDeleteNoSplay function](nf-ntddk-rtldeletenosplay.md) | The RtlDeleteNoSplay routine deletes the specified node from the splay link tree. |
| [RtlDrainNonVolatileFlush function](nf-ntddk-rtldrainnonvolatileflush.md) | The routine RtlDrainNonVolatileFlush waits for the flushes initiated by RtlFlushNonVolatileMemory to finish. |
| [RtlEnumerateGenericTable function](nf-ntddk-rtlenumerategenerictable.md) | The RtlEnumerateGenericTable routine is used to enumerate the elements in a generic table. |
| [RtlEnumerateGenericTableAvl function](nf-ntddk-rtlenumerategenerictableavl.md) | The RtlEnumerateGenericTableAvl routine is used to enumerate the elements in a generic table. |
| [RtlEnumerateGenericTableLikeADirectory function](nf-ntddk-rtlenumerategenerictablelikeadirectory.md) | The RtlEnumerateGenericTableLikeADirectory routine returns the elements of a generic table, one-by-one, in collation order. |
| [RtlEnumerateGenericTableWithoutSplaying function](nf-ntddk-rtlenumerategenerictablewithoutsplaying.md) | The RtlEnumerateGenericTableWithoutSplaying routine is used to enumerate the elements in a generic table. |
| [RtlEnumerateGenericTableWithoutSplayingAvl function](nf-ntddk-rtlenumerategenerictablewithoutsplayingavl.md) | The RtlEnumerateGenericTableWithoutSplayingAvl routine is used to enumerate the elements in a generic table. |
| [RtlEqualString function](nf-ntddk-rtlequalstring.md) | The RtlEqualString routine compares two counted strings to determine whether they are equal. |
| [RtlExtendCorrelationVector function](nf-ntddk-rtlextendcorrelationvector.md) | This routine extends the supplied correlation vector. For a correlation vector of the form X.i, the extended value is X.i.0. |
| [RtlFlushNonVolatileMemory function](nf-ntddk-rtlflushnonvolatilememory.md) | The routine RtlFlushNonVolatileMemory optimally flushes the given non-volatile memory region. |
| [RtlFlushNonVolatileMemoryRanges function](nf-ntddk-rtlflushnonvolatilememoryranges.md) | The routine RtlFlushNonVolatileMemoryRanges optimally flushes the given non-volatile memory regions. |
| [RtlFreeNonVolatileToken function](nf-ntddk-rtlfreenonvolatiletoken.md) | The routine RtlFreeNonVolatileToken is a cleanup function for the opaque NvToken which is given by a successful call to RtlGetNonVolatileToken. |
| [RtlGetElementGenericTable function](nf-ntddk-rtlgetelementgenerictable.md) | The RtlGetElementGenericTable routine returns a pointer to the caller-supplied data for a particular generic table element. |
| [RtlGetElementGenericTableAvl function](nf-ntddk-rtlgetelementgenerictableavl.md) | The RtlGetElementGenericTableAvl routine returns a pointer to the caller-supplied data for a particular generic Adelson-Velsky/Landis (AVL) table element. |
| [RtlGetEnabledExtendedFeatures function](nf-ntddk-rtlgetenabledextendedfeatures.md) | The RtlGetEnabledExtendedFeatures routine returns a mask of extended processor features that are enabled by the system. |
| [RtlGetNonVolatileToken function](nf-ntddk-rtlgetnonvolatiletoken.md) | The routine, RtlGetNonVolatileToken, gets various properties about a non-volatile memory buffer and stores them in the variable NvToken. |
| [RtlIncrementCorrelationVector function](nf-ntddk-rtlincrementcorrelationvector.md) | Increments the specified correlation vector. For a correlation vector of the form X.i, the incremented value is be X.(i+1). |
| [RtlInitializeCorrelationVector function](nf-ntddk-rtlinitializecorrelationvector.md) | Initializes the specified correlation vector with the supplied GUID. |
| [RtlInitializeGenericTable function](nf-ntddk-rtlinitializegenerictable.md) | The RtlInitializeGenericTable routine initializes a generic table. |
| [RtlInitializeGenericTableAvl function](nf-ntddk-rtlinitializegenerictableavl.md) | The RtlInitializeGenericTableAvl routine initializes a generic table using Adelson-Velsky/Landis (AVL) trees. |
| [RtlInitializeSplayLinks function](nf-ntddk-rtlinitializesplaylinks.md) | The RtlInitializeSplayLinks routine initializes a splay link node. |
| [RtlInsertAsLeftChild function](nf-ntddk-rtlinsertasleftchild.md) | The RtlInsertAsLeftChild routine inserts a splay link node into the tree as the left child of the specified node. |
| [RtlInsertAsRightChild function](nf-ntddk-rtlinsertasrightchild.md) | The RtlInsertAsRightChild routine inserts a given splay link into the tree as the right child of a given node in that tree. |
| [RtlInsertElementGenericTable function](nf-ntddk-rtlinsertelementgenerictable.md) | The RtlInsertElementGenericTable routine adds a new element to a generic table. |
| [RtlInsertElementGenericTableAvl function](nf-ntddk-rtlinsertelementgenerictableavl.md) | The RtlInsertElementGenericTableAvl routine adds a new entry to a generic table. |
| [RtlInsertElementGenericTableFullAvl function](nf-ntddk-rtlinsertelementgenerictablefullavl.md) | The RtlInsertElementGenericTableFullAvl routine adds a new entry to a generic table. |
| [RtlIsGenericTableEmpty function](nf-ntddk-rtlisgenerictableempty.md) | The RtlIsGenericTableEmpty routine determines if a generic table is empty. |
| [RtlIsGenericTableEmptyAvl function](nf-ntddk-rtlisgenerictableemptyavl.md) | The RtlIsGenericTableEmptyAvl routine determines if a generic table is empty. |
| [RtlIsLeftChild function](nf-ntddk-rtlisleftchild.md) | The RtlIsLeftChild routine determines whether a given splay link is the left child of a node in a splay link tree. |
| [RtlIsRightChild function](nf-ntddk-rtlisrightchild.md) | The RtlIsRightChild routine determines whether a given splay link is the right child of a node in a splay link tree. |
| [RtlIsRoot function](nf-ntddk-rtlisroot.md) | The RtlIsRoot routine determines whether the specified node is the root node of a splay link tree. |
| [RtlIsStateSeparationEnabled function](nf-ntddk-rtlisstateseparationenabled.md) | Checks if the SKU for the current context supports multiple sessions. |
| [RtlLeftChild function](nf-ntddk-rtlleftchild.md) | The RtlLeftChild routine returns a pointer to the left child of the specified splay link node. |
| [RtlLookupElementGenericTable function](nf-ntddk-rtllookupelementgenerictable.md) | The RtlLookupElementGenericTable routine searches a generic table for an element that matches the specified data. |
| [RtlLookupElementGenericTableAvl function](nf-ntddk-rtllookupelementgenerictableavl.md) | The RtlLookupElementGenericTableAvl routine searches a generic table for an element that matches the specified data. |
| [RtlLookupElementGenericTableFullAvl function](nf-ntddk-rtllookupelementgenerictablefullavl.md) | The RtlLookupElementGenericTableFullAvl routine searches a generic table for an element that matches the specified data. |
| [RtlLookupFirstMatchingElementGenericTableAvl function](nf-ntddk-rtllookupfirstmatchingelementgenerictableavl.md) | The RtlLookupFirstMatchingElementGenericTableAvl routine finds the left-most element in the tree that matches the indicated data. |
| [RtlMapGenericMask function](nf-ntddk-rtlmapgenericmask.md) | The RtlMapGenericMask routine determines the nongeneric access rights specified by an ACCESS_MASK. |
| [RtlNumberGenericTableElements function](nf-ntddk-rtlnumbergenerictableelements.md) | The RtlNumberGenericTableElements routine returns the number of elements in a generic table. |
| [RtlNumberGenericTableElementsAvl function](nf-ntddk-rtlnumbergenerictableelementsavl.md) | The RtlNumberGenericTableElementsAvl routine returns the number of elements in a generic table. |
| [RtlParent function](nf-ntddk-rtlparent.md) | The RtlParent routine returns a pointer to the parent of the specified node in a splay link tree. |
| [RtlPrefixUnicodeString function](nf-ntddk-rtlprefixunicodestring.md) | The RtlPrefixUnicodeString routine compares two Unicode strings to determine whether one string is a prefix of the other. |
| [RtlRealPredecessor function](nf-ntddk-rtlrealpredecessor.md) | The RtlRealPredecessor routine returns a pointer to the predecessor of the specified node in the splay link tree. |
| [RtlRealSuccessor function](nf-ntddk-rtlrealsuccessor.md) | The RtlRealSuccessor routine returns a pointer to the successor of the specified node in the splay link tree. |
| [RtlRightChild function](nf-ntddk-rtlrightchild.md) | The RtlRightChild routine returns a pointer to the right child of the specified splay link node. |
| [RtlRunOnceBeginInitialize function](nf-ntddk-rtlrunoncebegininitialize.md) | The RtlRunOnceBeginInitialize routine begins a one-time initialization. |
| [RtlRunOnceComplete function](nf-ntddk-rtlrunoncecomplete.md) | The RtlRunOnceComplete routine completes the one-time initialization began by RtlRunOnceBeginInitialize. |
| [RtlRunOnceExecuteOnce function](nf-ntddk-rtlrunonceexecuteonce.md) | The RtlRunOnceExecuteOnce performs a one-time initialization. |
| [RtlRunOnceInitialize function](nf-ntddk-rtlrunonceinitialize.md) | The RtlRunOnceInitialize routine initializes a RTL_RUN_ONCE structure. |
| [RtlSplay function](nf-ntddk-rtlsplay.md) | The RtlSplay routine rebalances, or &#0034;splays,&#0034; a splay link tree around the specified splay link, making that link the new root of the tree. |
| [RtlSubtreePredecessor function](nf-ntddk-rtlsubtreepredecessor.md) | The RtlSubtreePredecessor routine returns a pointer to the predecessor of the specified node within the subtree that is rooted at that node. |
| [RtlSubtreeSuccessor function](nf-ntddk-rtlsubtreesuccessor.md) | The RtlSubtreeSuccessor routine returns a pointer to the successor of the specified node within the subtree that is rooted at that node. |
| [RtlUpcaseUnicodeString function](nf-ntddk-rtlupcaseunicodestring.md) | The RtlUpcaseUnicodeString routine converts a copy of the source string to uppercase and writes the converted string in the destination buffer. |
| [RtlUpperChar function](nf-ntddk-rtlupperchar.md) | The RtlUpperChar routine converts the specified character to uppercase. |
| [RtlUpperString function](nf-ntddk-rtlupperstring.md) | The RtlUpperString routine copies the given SourceString to the DestinationString buffer, converting it to uppercase. |
| [RtlValidateCorrelationVector function](nf-ntddk-rtlvalidatecorrelationvector.md) | Validates the specified correlation vector to check whether it conforms to the Correlation Vector Specification (v2). |
| [RtlVolumeDeviceToDosName function](nf-ntddk-rtlvolumedevicetodosname.md) | The RtlVolumeDeviceToDosName routine is obsolete for Windows XP and later versions of Windows. Use IoVolumeDeviceToDosName instead.RtlVolumeDeviceToDosName returns the MS-DOS path for a specified device object that represents a file system volume. |
| [RtlWriteNonVolatileMemory function](nf-ntddk-rtlwritenonvolatilememory.md) | The routine RtlWriteNonVolatileMemory copies the contents of a source buffer to a non-volatile destination memory buffer. |
| [SeSinglePrivilegeCheck function](nf-ntddk-sesingleprivilegecheck.md) | The SeSinglePrivilegeCheck routine checks for the passed privilege value in the context of the current thread. |
| [WheaFindErrorRecordSection function](nf-ntddk-wheafinderrorrecordsection.md) | The WheaFindErrorRecordSection function searches for a specified Windows Hardware Error Architecture (WHEA) error record section within a WHEA error record. The error record section is formatted as a WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure. |
| [WheaFindNextErrorRecordSection function](nf-ntddk-wheafindnexterrorrecordsection.md) | The WheaFindNextErrorRecordSection function allows a caller to iteratively examine the WHEA error record sections within a WHEA error record. Each error record section is formatted as a WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure. |
| [WheaGetErrPacketFromErrRecord function](nf-ntddk-wheageterrpacketfromerrrecord.md) | The WheaGetErrPacketFromErrRecord function returns a pointer to the hardware error packet that is contained within a WHEA error record. The hardware error packet is formatted as a WHEA_ERROR_PACKET structure. |
| [WheaIsValidErrorRecordSignature function](nf-ntddk-wheaisvaliderrorrecordsignature.md) | The WheaIsValidErrorRecordSignature function verifies whether a WHEA error record is valid. |
| [ZwAllocateLocallyUniqueId function](nf-ntddk-zwallocatelocallyuniqueid.md) | The ZwAllocateLocallyUniqueId routine allocates a locally unique identifier (LUID). |
| [ZwOpenProcess function](nf-ntddk-zwopenprocess.md) | The ZwOpenProcess routine opens a handle to a process object and sets the access rights to this object. |
| [ZwPowerInformation function](nf-ntddk-zwpowerinformation.md) | The ZwPowerInformation routine sets or retrieves system power information. |
| [ZwSetInformationThread function](nf-ntddk-zwsetinformationthread.md) | The ZwSetInformationThread routine sets the priority of a thread. |
| [ZwTerminateProcess function](nf-ntddk-zwterminateprocess.md) | The ZwTerminateProcess routine terminates a process and all of its threads. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [DRIVER_REINITIALIZE callback](nc-ntddk-driver-reinitialize.md) | The Reinitialize routine continues driver and device initialization after the driver's DriverEntry routine returns. |
| [EXPAND_STACK_CALLOUT callback](nc-ntddk-expand-stack-callout.md) | The ExpandedStackCall routine executes with a guaranteed stack size. |
| [PCREATE_PROCESS_NOTIFY_ROUTINE callback](nc-ntddk-pcreate-process-notify-routine.md) | Process-creation callback implemented by a driver to track the system-wide creation and deletion of processes against the driver's internal state. |
| [PCREATE_PROCESS_NOTIFY_ROUTINE_EX callback](nc-ntddk-pcreate-process-notify-routine-ex.md) | A callback routine implemented by a driver to notify the caller when a process is created or exits. |
| [PCREATE_THREAD_NOTIFY_ROUTINE callback](nc-ntddk-pcreate-thread-notify-routine.md) | A callback routine implemented by a driver to notify the caller when a thread is created or deleted. |
| [PGET_LOCATION_STRING callback](nc-ntddk-pget-location-string.md) | The PnpGetLocationString routine provides the device-specific part of the device's SPDRP_LOCATION_PATHS property. |
| [PLOAD_IMAGE_NOTIFY_ROUTINE callback](nc-ntddk-pload-image-notify-routine.md) | Called by the operating system to notify the driver when a driver image or a user image (for example, a DLL or EXE) is mapped into virtual memory. |
| [PSHED_PI_ATTEMPT_ERROR_RECOVERY callback](nc-ntddk-pshed-pi-attempt-error-recovery.md) | A PSHED plug-in's AttemptRecovery callback function attempts to recover from a recoverable hardware error. |
| [PSHED_PI_CLEAR_ERROR_RECORD callback](nc-ntddk-pshed-pi-clear-error-record.md) | A PSHED plug-in's ClearErrorRecord callback function clears the specified error record from the system's persistent data storage. |
| [PSHED_PI_CLEAR_ERROR_STATUS callback](nc-ntddk-pshed-pi-clear-error-status.md) | A PSHED plug-in's ClearErrorStatus callback function clears any platform-specific error status registers for a corrected hardware error condition. |
| [PSHED_PI_DISABLE_ERROR_SOURCE callback](nc-ntddk-pshed-pi-disable-error-source.md) | A PSHED plug-in's DisableErrorSource callback function disables an error source. |
| [PSHED_PI_ENABLE_ERROR_SOURCE callback](nc-ntddk-pshed-pi-enable-error-source.md) | A PSHED plug-in's EnableErrorSource callback function enables an error source. |
| [PSHED_PI_FINALIZE_ERROR_RECORD callback](nc-ntddk-pshed-pi-finalize-error-record.md) | A PSHED plug-in's FinalizeErrorRecord callback function adds supplementary error record sections to an error record that more fully describe the error condition. |
| [PSHED_PI_GET_ALL_ERROR_SOURCES callback](nc-ntddk-pshed-pi-get-all-error-sources.md) | A PSHED plug-in's GetAllErrorSources callback function returns a list of error source descriptor structures that represents all of the error sources that are implemented by the hardware platform. |
| [PSHED_PI_GET_ERROR_SOURCE_INFO callback](nc-ntddk-pshed-pi-get-error-source-info.md) | A PSHED plug-in's GetErrorSourceInfo callback function returns an error source descriptor structure that represents a particular error source that is implemented by the hardware platform. |
| [PSHED_PI_GET_INJECTION_CAPABILITIES callback](nc-ntddk-pshed-pi-get-injection-capabilities.md) | A PSHED plug-in's GetInjectionCapabilities callback function returns an error injection capabilities union that describes the types of hardware errors that can be injected into the hardware platform. |
| [PSHED_PI_INJECT_ERROR callback](nc-ntddk-pshed-pi-inject-error.md) | A PSHED plug-in's InjectError callback function injects an error into the hardware platform. |
| [PSHED_PI_READ_ERROR_RECORD callback](nc-ntddk-pshed-pi-read-error-record.md) | A PSHED plug-in's ReadErrorRecord callback function reads an error record from the system's persistent data storage. |
| [PSHED_PI_RETRIEVE_ERROR_INFO callback](nc-ntddk-pshed-pi-retrieve-error-info.md) | A PSHED plug-in's RetrieveErrorInfo callback function retrieves platform-specific error information about a hardware error that has occurred. |
| [PSHED_PI_SET_ERROR_SOURCE_INFO callback](nc-ntddk-pshed-pi-set-error-source-info.md) | A PSHED plug-in's SetErrorSourceInfo callback function configures an error source. |
| [PSHED_PI_WRITE_ERROR_RECORD callback](nc-ntddk-pshed-pi-write-error-record.md) | A PSHED plug-in's WriteErrorRecord callback function writes an error record to the system's persistent data storage. |
| [RTL_RUN_ONCE_INIT_FN callback](nc-ntddk-rtl-run-once-init-fn.md) | The RunOnceInitialization routine performs a one-time initialization operation. |
| [SILO_CONTEXT_CLEANUP_CALLBACK callback](nc-ntddk-silo-context-cleanup-callback.md) | This callback is invoked when the context object reaches a reference count of zero. |
| [SILO_MONITOR_CREATE_CALLBACK callback](nc-ntddk-silo-monitor-create-callback.md) | This is callback is invoked when a new silo is created. |
| [SILO_MONITOR_TERMINATE_CALLBACK callback](nc-ntddk-silo-monitor-terminate-callback.md) | This callback is invoked when a silo is terminated. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [BDCB_IMAGE_INFORMATION structure](ns-ntddk--bdcb-image-information.md) | The BDCB_IMAGE_INFORMATION structure describes information about a boot-start driver that is about to be initialized, provided by Windows to a boot-start driver's BOOT_DRIVER_CALLBACK_FUNCTION routine. |
| [BDCB_STATUS_UPDATE_CONTEXT structure](ns-ntddk--bdcb-status-update-context.md) | The BDCB_STATUS_UPDATE_CONTEXT structure describes a status update provided by Windows to a boot-start driver's BOOT_DRIVER_CALLBACK_FUNCTION routine. |
| [CONTROLLER_OBJECT structure](ns-ntddk--controller-object.md) | A controller object represents a hardware adapter or controller with homogenous devices that are the actual targets for I/O requests. |
| [CORRELATION_VECTOR structure](ns-ntddk-correlation-vector.md) | Store the correlation vector that is used to reference events and the generated logs for diagnostic purposes. |
| [DISK_SIGNATURE structure](ns-ntddk--disk-signature.md) | DISK_SIGNATURE contains the disk signature information for a disk's partition table. |
| [DMA_ADAPTER structure](ns-ntddk--dma-adapter.md) | The DMA_ADAPTER structure describes a system-defined interface to a DMA controller for a given device. A driver calls IoGetDmaAdapter to obtain this structure. |
| [FILE_ALIGNMENT_INFORMATION structure](ns-ntddk--file-alignment-information.md) | The FILE_ALIGNMENT_INFORMATION structure is used as an argument to the ZwQueryInformationFile routine. |
| [FILE_ATTRIBUTE_TAG_INFORMATION structure](ns-ntddk--file-attribute-tag-information.md) | The FILE_ATTRIBUTE_TAG_INFORMATION structure is used as an argument to ZwQueryInformationFile. |
| [FILE_DISPOSITION_INFORMATION structure](ns-ntddk--file-disposition-information.md) | The FILE_DISPOSITION_INFORMATION structure is used as an argument to the ZwSetInformationFile routine. |
| [FILE_DISPOSITION_INFORMATION_EX structure](ns-ntddk--file-disposition-information-ex.md) | The FILE_DISPOSITION_INFORMATION_EX structure is used as an argument to the ZwSetInformationFileEx routine and indicates how the operating system should delete a file. |
| [FILE_END_OF_FILE_INFORMATION structure](ns-ntddk--file-end-of-file-information.md) | The FILE_END_OF_FILE_INFORMATION structure is used as an argument to the ZwSetInformationFile routine. |
| [FILE_FS_FULL_SIZE_INFORMATION structure](ns-ntddk--file-fs-full-size-information.md) | The FILE_FS_FULL_SIZE_INFORMATION structure is used to query sector size information for a file system volume. |
| [FILE_FS_LABEL_INFORMATION structure](ns-ntddk--file-fs-label-information.md) | The FILE_FS_LABEL_INFORMATION structure is used to set the label for a file system volume. |
| [FILE_FS_OBJECTID_INFORMATION structure](ns-ntddk--file-fs-objectid-information.md) | The FILE_FS_OBJECTID_INFORMATION structure is used to query or set the object ID for a file system volume. |
| [FILE_FS_SECTOR_SIZE_INFORMATION structure](ns-ntddk--file-fs-sector-size-information.md) | The FILE_FS_SECTOR_SIZE_INFORMATION structure is used to query physical and logical sector size information for a file system volume. |
| [FILE_FS_SIZE_INFORMATION structure](ns-ntddk--file-fs-size-information.md) | The FILE_FS_SIZE_INFORMATION structure is used to query sector size information for a file system volume. |
| [FILE_FS_VOLUME_INFORMATION structure](ns-ntddk--file-fs-volume-information.md) | The FILE_FS_VOLUME_INFORMATION structure is used to query information about a volume on which a file system is mounted. |
| [FILE_NAME_INFORMATION structure](ns-ntddk--file-name-information.md) | The FILE_NAME_INFORMATION structure is used as argument to the ZwQueryInformationFile and ZwSetInformationFile routines. |
| [FILE_VALID_DATA_LENGTH_INFORMATION structure](ns-ntddk--file-valid-data-length-information.md) | The FILE_VALID_DATA_LENGTH_INFORMATION structure is used as an argument to ZwSetInformationFile. |
| [HARDWARE_COUNTER structure](ns-ntddk--hardware-counter.md) | The HARDWARE_COUNTER structure contains information about a hardware counter. |
| [IMAGE_INFO structure](ns-ntddk--image-info.md) | Used by driver's load-image routine (PLOAD_IMAGE_NOTIFY_ROUTINE) to specify image information. |
| [IMAGE_INFO_EX structure](ns-ntddk--image-info-ex.md) | Extended version of the image information structure (see IMAGE_INFO). |
| [IO_DRIVER_CREATE_CONTEXT structure](ns-ntddk--io-driver-create-context.md) | The IO_DRIVER_CREATE_CONTEXT structure is used to pass additional parameters to the IoCreateFileEx and FltCreateFileEx2 routines. |
| [IO_FOEXT_SILO_PARAMETERS structure](ns-ntddk--io-foext-silo-parameters.md) | This structure describes the Container context that's identified by the IoGetSiloParameters routine. |
| [KEY_CACHED_INFORMATION structure](ns-ntddk--key-cached-information.md) | The KEY_CACHED_INFORMATION structure holds the cached information available for a registry key or subkey. |
| [KEY_NAME_INFORMATION structure](ns-ntddk--key-name-information.md) | The KEY_NAME_INFORMATION structure holds the name and name length of the key. |
| [KEY_VIRTUALIZATION_INFORMATION structure](ns-ntddk--key-virtualization-information.md) | The KEY_VIRTUALIZATION_INFORMATION structure defines the basic information that is available for a registry key or subkey. |
| [MM_COPY_ADDRESS structure](ns-ntddk--mm-copy-address.md) | The MM_COPY_ADDRESS structure contains either a virtual memory address or a physical memory address. |
| [OPLOCK_KEY_CONTEXT structure](ns-ntddk--oplock-key-context.md) | The OPLOCK_KEY_CONTEXT structure is returned from IoGetOplockKeyContextEx. This structure contains oplock keys for a specific file object. |
| [OPLOCK_KEY_ECP_CONTEXT structure](ns-ntddk--oplock-key-ecp-context.md) | The OPLOCK_KEY_ECP_CONTEXT structure is used to attach an oplock key to a file. |
| [PCI_EXPRESS_CAPABILITIES_REGISTER structure](ns-ntddk--pci-express-capabilities-register.md) | The PCI_EXPRESS_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) capabilities register of a PCIe capability structure. |
| [PCI_EXPRESS_CAPABILITY structure](ns-ntddk--pci-express-capability.md) | The PCI_EXPRESS_CAPABILITY structure describes a PCI Express (PCIe) capability structure. |
| [PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure](ns-ntddk--pci-express-device-capabilities-register.md) | The PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) device capabilities register of a PCIe capability structure. |
| [PCI_EXPRESS_DEVICE_CONTROL_REGISTER structure](ns-ntddk--pci-express-device-control-register.md) | The PCI_EXPRESS_DEVICE_CONTROL_REGISTER structure describes a PCI Express (PCIe) device control register of a PCIe capability structure. |
| [PCI_EXPRESS_DEVICE_STATUS_REGISTER structure](ns-ntddk--pci-express-device-status-register.md) | The PCI_EXPRESS_DEVICE_STATUS_REGISTER structure describes a PCI Express (PCIe) device status register of a PCIe capability structure. |
| [PCI_EXPRESS_LINK_CAPABILITIES_REGISTER structure](ns-ntddk--pci-express-link-capabilities-register.md) | The PCI_EXPRESS_LINK_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) link capabilities register of a PCIe capability structure. |
| [PCI_EXPRESS_LINK_CONTROL_REGISTER structure](ns-ntddk--pci-express-link-control-register.md) | The PCI_EXPRESS_LINK_CONTROL_REGISTER structure describes a PCI Express (PCIe) link control register of a PCIe capability structure. |
| [PCI_EXPRESS_LINK_STATUS_REGISTER structure](ns-ntddk--pci-express-link-status-register.md) | The PCI_EXPRESS_LINK_STATUS_REGISTER structure describes a PCI Express (PCIe) link status register of a PCIe capability structure. |
| [PCI_EXPRESS_PME_REQUESTOR_ID structure](ns-ntddk--pci-express-pme-requestor-id.md) | The PCI_EXPRESS_PME_REQUESTOR_ID structure describes the identifier of the requester of a power management event (PME). |
| [PCI_EXPRESS_ROOT_CAPABILITIES_REGISTER structure](ns-ntddk--pci-express-root-capabilities-register.md) | The PCI_EXPRESS_ROOT_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) root capabilities register of a PCIe capability structure. |
| [PCI_EXPRESS_ROOT_CONTROL_REGISTER structure](ns-ntddk--pci-express-root-control-register.md) | The PCI_EXPRESS_ROOT_CONTROL_REGISTER structure describes a PCI Express (PCIe) root control register of a PCIe capability structure. |
| [PCI_EXPRESS_ROOT_STATUS_REGISTER structure](ns-ntddk--pci-express-root-status-register.md) | The PCI_EXPRESS_ROOT_STATUS_REGISTER structure describes a PCI Express (PCIe) root status register of a PCIe capability structure. |
| [PCI_EXPRESS_SLOT_CAPABILITIES_REGISTER structure](ns-ntddk--pci-express-slot-capabilities-register.md) | The PCI_EXPRESS_SLOT_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) slot capabilities register of a PCIe capability structure. |
| [PCI_EXPRESS_SLOT_CONTROL_REGISTER structure](ns-ntddk--pci-express-slot-control-register.md) | The PCI_EXPRESS_SLOT_CONTROL_REGISTER structure describes a PCI Express (PCIe) slot control register of a PCIe capability structure. |
| [PCI_EXPRESS_SLOT_STATUS_REGISTER structure](ns-ntddk--pci-express-slot-status-register.md) | The PCI_EXPRESS_SLOT_STATUS_REGISTER structure describes a PCI Express (PCIe) slot status register of a PCIe capability structure. |
| [PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structure](ns-ntddk--physical-counter-resource-descriptor.md) | The PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structure describes the counter resources available on the platform. |
| [PHYSICAL_COUNTER_RESOURCE_LIST structure](ns-ntddk--physical-counter-resource-list.md) | The PHYSICAL_COUNTER_RESOURCE_LIST structure describes an array of PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structures. |
| [PNP_LOCATION_INTERFACE structure](ns-ntddk--pnp-location-interface.md) | The PNP_LOCATION_INTERFACE structure describes the GUID_PNP_LOCATION_INTERFACE interface. |
| [POWER_THROTTLING_PROCESS_STATE structure](ns-ntddk--power-throttling-process-state.md) | Stores the throttling policies and how to apply them to a target process when that process is subject to power management. |
| [POWER_THROTTLING_THREAD_STATE structure](ns-ntddk--power-throttling-thread-state.md) | Stores the throttling policies and how to apply them to a target thread when that thread is subject to power management. |
| [PROCESS_MITIGATION_CHILD_PROCESS_POLICY structure](ns-ntddk--process-mitigation-child-process-policy.md) | Stores policy information about creating child processes. |
| [PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY structure](ns-ntddk--process-mitigation-payload-restriction-policy.md) | Stores information about process mitigation policy. |
| [PROCESS_READWRITEVM_LOGGING_INFORMATION structure](ns-ntddk--process-readwritevm-logging-information.md) | Stores options for read/write access for telemetry per process. |
| [PS_CREATE_NOTIFY_INFO structure](ns-ntddk--ps-create-notify-info.md) | The PS_CREATE_NOTIFY_INFO structure provides information about a newly created process. |
| [RTL_AVL_TABLE structure](ns-ntddk--rtl-avl-table.md) | The RTL_AVL_TABLE structure contains file system-specific data for an Adelson-Velsky/Landis (AVL) tree. |
| [RTL_AVL_TABLE structure](ns-ntddk--rtl-avl-table~r1.md) | The RTL_AVL_TABLE structure contains file system-specific data for an Adelson-Velsky/Landis (AVL) tree. |
| [RTL_GENERIC_TABLE structure](ns-ntddk--rtl-generic-table.md) | The RTL_GENERIC_TABLE structure contains file system-specific data for a splay tree. |
| [RTL_GENERIC_TABLE structure](ns-ntddk--rtl-generic-table~r1.md) | The RTL_GENERIC_TABLE structure contains file system-specific data for a splay tree. |
| [RTL_SPLAY_LINKS structure](ns-ntddk--rtl-splay-links.md) | The RTL_SPLAY_LINKS structure is an opaque structure and is used by the system to represent a splay link tree node. |
| [SILO_MONITOR_REGISTRATION structure](ns-ntddk--silo-monitor-registration.md) | This structure specifies a server silo monitor that can receive notifications about server silo events. |
| [SOC_SUBSYSTEM_FAILURE_DETAILS structure](ns-ntddk--soc-subsystem-failure-details.md) | The SOC_SUBSYSTEM_FAILURE_DETAILS structure holds information related to a System on a Chip (SoC) bug code. |
| [TXN_PARAMETER_BLOCK structure](ns-ntddk--txn-parameter-block.md) | The TXN_PARAMETER_BLOCK structure contains information about a transacted file operation. |
| [WHEA_AER_BRIDGE_DESCRIPTOR structure](ns-ntddk--whea-aer-bridge-descriptor.md) | The WHEA_AER_BRIDGE_DESCRIPTOR structure describes a PCI Express (PCIe) bridge error source. |
| [WHEA_AER_ENDPOINT_DESCRIPTOR structure](ns-ntddk--whea-aer-endpoint-descriptor.md) | The WHEA_AER_ENDPOINT_DESCRIPTOR structure describes a PCI Express (PCIe) endpoint error source. |
| [WHEA_AER_ROOTPORT_DESCRIPTOR structure](ns-ntddk--whea-aer-rootport-descriptor.md) | The WHEA_AER_ROOTPORT_DESCRIPTOR structure describes a PCI Express (PCIe) root port error source. |
| [WHEA_ERROR_INJECTION_CAPABILITIES structure](ns-ntddk--whea-error-injection-capabilities.md) | The WHEA_ERROR_INJECTION_CAPABILITIES union describes the types of hardware errors that can be injected into a hardware platform. |
| [WHEA_ERROR_PACKET_FLAGS structure](ns-ntddk--whea-error-packet-flags.md) | The WHEA_ERROR_PACKET_FLAGS union defines the error condition reported through a WHEA_ERROR_PACKET structure. |
| [WHEA_ERROR_PACKET_V1 structure](ns-ntddk--whea-error-packet-v1.md) | The WHEA_ERROR_PACKET_V1 structure describes the hardware error data that is passed to the operating system by a low-level hardware error handler (LLHEH).Note  The WHEA_ERROR_PACKET_V1 structure is supported in Windows Server 2008 and Windows Vista SP1. |
| [WHEA_ERROR_PACKET_V1 structure](ns-ntddk--whea-error-packet-v1~r1.md) | The WHEA_ERROR_PACKET_V1 structure describes the hardware error data that is passed to the operating system by a low-level hardware error handler (LLHEH).Note  The WHEA_ERROR_PACKET_V1 structure is supported in Windows Server 2008 and Windows Vista SP1. |
| [WHEA_ERROR_PACKET_V2 structure](ns-ntddk--whea-error-packet-v2.md) | The WHEA_ERROR_PACKET_V2 structure describes the hardware error data that is passed to the operating system by a low-level hardware error handler (LLHEH).Note  The WHEA_ERROR_PACKET_V2 structure is supported in Windows 7 and later versions of Windows. |
| [WHEA_ERROR_PACKET_V2 structure](ns-ntddk--whea-error-packet-v2~r1.md) | The WHEA_ERROR_PACKET_V2 structure describes the hardware error data that is passed to the operating system by a low-level hardware error handler (LLHEH).Note  The WHEA_ERROR_PACKET_V2 structure is supported in Windows 7 and later versions of Windows. |
| [WHEA_ERROR_RECORD structure](ns-ntddk--whea-error-record.md) | The WHEA_ERROR_RECORD structure describes an error record that contains error information about a hardware error condition that occurred. |
| [WHEA_ERROR_RECORD structure](ns-ntddk--whea-error-record~r1.md) | The WHEA_ERROR_RECORD structure describes an error record that contains error information about a hardware error condition that occurred. |
| [WHEA_ERROR_RECORD structure](ns-ntddk--whea-error-record~r2.md) | The WHEA_ERROR_RECORD structure describes an error record that contains error information about a hardware error condition that occurred. |
| [WHEA_ERROR_RECORD_HEADER structure](ns-ntddk--whea-error-record-header.md) | The WHEA_ERROR_RECORD_HEADER structure describes general information about a hardware error condition. |
| [WHEA_ERROR_RECORD_HEADER_VALIDBITS structure](ns-ntddk--whea-error-record-header-validbits.md) | The WHEA_ERROR_RECORD_HEADER_VALIDBITS union describes which members of a WHEA_ERROR_RECORD_HEADER structure contain valid data. |
| [WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure](ns-ntddk--whea-error-record-section-descriptor.md) | The WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure describes a section of error information that is part of an error record. |
| [WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS structure](ns-ntddk--whea-error-record-section-descriptor-validbits.md) | The WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS union describes which members of a WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure contain valid data. |
| [WHEA_ERROR_SOURCE_DESCRIPTOR structure](ns-ntddk--whea-error-source-descriptor.md) | The WHEA_ERROR_SOURCE_DESCRIPTOR structure describes an error source. |
| [WHEA_ERROR_SOURCE_DESCRIPTOR structure](ns-ntddk--whea-error-source-descriptor~r1.md) | The WHEA_ERROR_SOURCE_DESCRIPTOR structure describes an error source. |
| [WHEA_ERROR_STATUS structure](ns-ntddk--whea-error-status.md) | The WHEA_ERROR_STATUS union describes generic error codes that are abstracted from the data contained in implementation-specific error registers. |
| [WHEA_FIRMWARE_ERROR_RECORD_REFERENCE structure](ns-ntddk--whea-firmware-error-record-reference.md) | The WHEA_FIRMWARE_ERROR_RECORD_REFERENCE structure describes a reference to a firmware error record that is specific to the Itanium processor architecture. |
| [WHEA_GENERIC_ERROR structure](ns-ntddk--whea-generic-error.md) | The WHEA_GENERIC_ERROR structure describes error status data for a generic error source. |
| [WHEA_GENERIC_ERROR_BLOCKSTATUS structure](ns-ntddk--whea-generic-error-blockstatus.md) | The WHEA_GENERIC_ERROR_BLOCKSTATUS union indicates what kind of error data is reported in a generic error status block. |
| [WHEA_GENERIC_ERROR_DESCRIPTOR structure](ns-ntddk--whea-generic-error-descriptor.md) | The WHEA_GENERIC_ERROR_DESCRIPTOR structure describes a generic error source. |
| [WHEA_IPF_CMC_DESCRIPTOR structure](ns-ntddk--whea-ipf-cmc-descriptor.md) | The WHEA_IPF_CMC_DESCRIPTOR structure describes a corrected machine check (CMC) error source for an Itanium processor. |
| [WHEA_IPF_CPE_DESCRIPTOR structure](ns-ntddk--whea-ipf-cpe-descriptor.md) | The WHEA_IPF_CPE_DESCRIPTOR structure describes a corrected platform error (CPE) error source for an Itanium processor. |
| [WHEA_IPF_MCA_DESCRIPTOR structure](ns-ntddk--whea-ipf-mca-descriptor.md) | The WHEA_IPF_MCA_DESCRIPTOR structure describes a machine check abort (MCA) error source for an Itanium processor. |
| [WHEA_MEMORY_ERROR_SECTION structure](ns-ntddk--whea-memory-error-section.md) | The WHEA_MEMORY_ERROR_SECTION structure describes platform memory error data. |
| [WHEA_MEMORY_ERROR_SECTION_VALIDBITS structure](ns-ntddk--whea-memory-error-section-validbits.md) | The WHEA_MEMORY_ERROR_SECTION_VALIDBITS union describes which members of a WHEA_MEMORY_ERROR_SECTION structure contain valid data. |
| [WHEA_NMI_ERROR_SECTION structure](ns-ntddk--whea-nmi-error-section.md) | The WHEA_NMI_ERROR_SECTION structure describes nonmaskable interrupt (NMI) error data. |
| [WHEA_NOTIFICATION_DESCRIPTOR structure](ns-ntddk--whea-notification-descriptor.md) | The WHEA_NOTIFICATION_DESCRIPTOR structure describes the notification mechanism that is used by an error source. |
| [WHEA_PCIEXPRESS_ERROR_SECTION structure](ns-ntddk--whea-pciexpress-error-section.md) | The WHEA_PCIEXPRESS_ERROR_SECTION structure describes PCI Express (PCIe) error data. |
| [WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS structure](ns-ntddk--whea-pciexpress-error-section-validbits.md) | The WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS union describes which members of a WHEA_PCIEXPRESS_ERROR_SECTION structure contain valid data. |
| [WHEA_PCIXBUS_ERROR_SECTION structure](ns-ntddk--whea-pcixbus-error-section.md) | The WHEA_PCIXBUS_ERROR_SECTION structure describes PCI or PCI-X bus error data. |
| [WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS structure](ns-ntddk--whea-pcixbus-error-section-validbits.md) | The WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS union describes which members of a WHEA_PCIXBUS_ERROR_SECTION structure contain valid data. |
| [WHEA_PCIXDEVICE_ERROR_SECTION structure](ns-ntddk--whea-pcixdevice-error-section.md) | The WHEA_PCIXDEVICE_ERROR_SECTION structure describes PCI or PCI-X device error data. |
| [WHEA_PCIXDEVICE_ERROR_SECTION_VALIDBITS structure](ns-ntddk--whea-pcixdevice-error-section-validbits.md) | The WHEA_PCIXDEVICE_ERROR_SECTION_VALIDBITS union describes which members of a WHEA_PCIXDEVICE_ERROR_SECTION structure contain valid data. |
| [WHEA_PCI_SLOT_NUMBER structure](ns-ntddk--whea-pci-slot-number.md) | The WHEA_PCI_SLOT_NUMBER structure describes a logical PCI slot. |
| [WHEA_PERSISTENCE_INFO structure](ns-ntddk--whea-persistence-info.md) | The WHEA_PERSISTENCE_INFO union describes data that is used by the error record persistence interface for storing an error record. |
| [WHEA_PROCESSOR_FAMILY_INFO structure](ns-ntddk--whea-processor-family-info.md) | The WHEA_PROCESSOR_FAMILY_INFO union describes the processor family information for an x86 or x64 processor. |
| [WHEA_PROCESSOR_GENERIC_ERROR_SECTION structure](ns-ntddk--whea-processor-generic-error-section.md) | Describes processor error data that is not specific to a particular processor architecture. |
| [WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS structure](ns-ntddk--whea-processor-generic-error-section-validbits.md) | The WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS union describes which members of a WHEA_PROCESSOR_GENERIC_ERROR_SECTION structure contain valid data. |
| [WHEA_PSHED_PLUGIN_CALLBACKS structure](ns-ntddk--whea-pshed-plugin-callbacks.md) | The WHEA_PSHED_PLUGIN_CALLBACKS structure describes the callback functions for a PSHED plug-in. |
| [WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure](ns-ntddk--whea-pshed-plugin-registration-packet.md) | The WHEA_PSHED_PLUGIN_REGISTRATION_PACKET structure describes the data required for registering a PSHED plug-in with the PSHED. |
| [WHEA_REVISION structure](ns-ntddk--whea-revision.md) | The WHEA_REVISION union describes the revision of the error record data structures. |
| [WHEA_TIMESTAMP structure](ns-ntddk--whea-timestamp.md) | The WHEA_TIMESTAMP union describes the time that an error was reported to the operating system. |
| [WHEA_X64_REGISTER_STATE structure](ns-ntddk--whea-x64-register-state.md) | The WHEA_X64_REGISTER_STATE structure describes the state of an x64 processor's registers. |
| [WHEA_X86_REGISTER_STATE structure](ns-ntddk--whea-x86-register-state.md) | The WHEA_X86_REGISTER_STATE structure describes the state of an x86 processor's registers. |
| [WHEA_XPF_BUS_CHECK structure](ns-ntddk--whea-xpf-bus-check.md) | The WHEA_XPF_BUS_CHECK union describes bus error information for an x86 or x64 processor. |
| [WHEA_XPF_CACHE_CHECK structure](ns-ntddk--whea-xpf-cache-check.md) | The WHEA_XPF_CACHE_CHECK union describes cache error information for an x86 or x64 processor. |
| [WHEA_XPF_CMC_DESCRIPTOR structure](ns-ntddk--whea-xpf-cmc-descriptor.md) | The WHEA_XPF_CMC_DESCRIPTOR structure describes a corrected machine check (CMC) error source for an x86 or x64 processor. |
| [WHEA_XPF_CONTEXT_INFO structure](ns-ntddk--whea-xpf-context-info.md) | The WHEA_XPF_CONTEXT_INFO structure describes processor context information for an x86 or x64 processor. |
| [WHEA_XPF_MCE_DESCRIPTOR structure](ns-ntddk--whea-xpf-mce-descriptor.md) | The WHEA_XPF_MCE_DESCRIPTOR structure describes a machine check exception (MCE) error source for an x86 or x64 processor. |
| [WHEA_XPF_MC_BANK_DESCRIPTOR structure](ns-ntddk--whea-xpf-mc-bank-descriptor.md) | The WHEA_XPF_MC_BANK_DESCRIPTOR structure describes a bank of machine check registers for an x86 or x64 processor. |
| [WHEA_XPF_MS_CHECK structure](ns-ntddk--whea-xpf-ms-check.md) | The WHEA_XPF_MS_CHECK union describes microarchitecture-specific error information for an x86 or x64 processor. |
| [WHEA_XPF_NMI_DESCRIPTOR structure](ns-ntddk--whea-xpf-nmi-descriptor.md) | The WHEA_XPF_NMI_DESCRIPTOR structure describes a nonmaskable interrupt (NMI) error source for an x86 or x64 processor. |
| [WHEA_XPF_PROCESSOR_ERROR_SECTION structure](ns-ntddk--whea-xpf-processor-error-section.md) | The WHEA_XPF_PROCESSOR_ERROR_SECTION structure describes processor error data that is specific to the x86/x64 processor architecture. |
| [WHEA_XPF_PROCESSOR_ERROR_SECTION structure](ns-ntddk-whea-xpf-processor-error-section.md) | The WHEA_XPF_PROCESSOR_ERROR_SECTION structure describes processor error data that is specific to the x86/x64 processor architecture. |
| [WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS structure](ns-ntddk--whea-xpf-processor-error-section-validbits.md) | The WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS union describes which members of a WHEA_XPF_PROCESSOR_ERROR_SECTION structure contain valid data and the number of structures that are contained in the WHEA_XPF_PROCESSOR_ERROR_SECTION structure's VariableInfo member. |
| [WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS structure](ns-ntddk-whea-xpf-processor-error-section-validbits.md) | The WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS union describes which members of a WHEA_XPF_PROCESSOR_ERROR_SECTION structure contain valid data and the number of structures that are contained in the WHEA_XPF_PROCESSOR_ERROR_SECTION structure's VariableInfo member. |
| [WHEA_XPF_PROCINFO structure](ns-ntddk--whea-xpf-procinfo.md) | The WHEA_XPF_PROCINFO structure describes processor error information that is specific to the x86 and x64 processor architectures. |
| [WHEA_XPF_PROCINFO_VALIDBITS structure](ns-ntddk--whea-xpf-procinfo-validbits.md) | The WHEA_XPF_PROCINFO_VALIDBITS union describes which members of a WHEA_XPF_PROCINFO structure contain valid data. |
| [WHEA_XPF_TLB_CHECK structure](ns-ntddk--whea-xpf-tlb-check.md) | The WHEA_XPF_TLB_CHECK union describes translation lookaside buffer (TLB) error information for an x86 or x64 processor. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [BDCB_CALLBACK_TYPE enumeration](ne-ntddk--bdcb-callback-type.md) | The BDCB_CALLBACK_TYPE enumeration specifies whether the callback being passed to a BOOT_DRIVER_CALLBACK_FUNCTION routine is a status update or a boot-start driver initialization notification. |
| [BDCB_CLASSIFICATION enumeration](ne-ntddk--bdcb-classification.md) | The BDCB_CLASSIFICATION enumeration lists different classifications of boot start images. |
| [BDCB_STATUS_UPDATE_TYPE enumeration](ne-ntddk--bdcb-status-update-type.md) | The BDCB_STATUS_UPDATE_TYPE enumeration lists the types of boot-driver callback status updates. |
| [BUS_DATA_TYPE enumeration](ne-ntddk--bus-data-type.md) | The BUS_DATA_TYPE enumeration indicates the type of bus configuration space. |
| [HARDWARE_COUNTER_TYPE enumeration](ne-ntddk--hardware-counter-type.md) | The HARDWARE_COUNTER_TYPE enumeration specifies the type of a hardware counter. |
| [PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR_TYPE enumeration](ne-ntddk--physical-counter-resource-descriptor-type.md) | The PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR_TYPE enumeration contains constants that indicate the type of hardware performance counter resource that is described by a PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structure. |
| [PSCREATEPROCESSNOTIFYTYPE enumeration](ne-ntddk--pscreateprocessnotifytype.md) | Indicates the type of process notification. This enumeration is used in PsSetCreateProcessNotifyRoutineEx2 to register callback notifications. |
| [PSCREATETHREADNOTIFYTYPE enumeration](ne-ntddk--pscreatethreadnotifytype.md) | Indicates the type of thread notification. This enumeration is used in PsSetCreateThreadNotifyRoutineEx to register callback notifications associated with thread creation or deletion. |
| [SUBSYSTEM_INFORMATION_TYPE enumeration](ne-ntddk--subsystem-information-type.md) | Indicates the type of subsystem for a process or thread. This enumeration is used in NtQueryInformationProcess and NtQueryInformationThread calls. |
| [WHEA_ERROR_PACKET_DATA_FORMAT enumeration](ne-ntddk--whea-error-packet-data-format.md) | The WHEA_ERROR_PACKET_DATA_FORMAT enumeration defines the raw hardware error data format in a hardware error packet. |
| [WHEA_ERROR_SEVERITY enumeration](ne-ntddk--whea-error-severity.md) | The WHEA_ERROR_SEVERITY enumeration defines the possible severity levels of a hardware error condition. |
| [WHEA_ERROR_SOURCE_STATE enumeration](ne-ntddk--whea-error-source-state.md) | The WHEA_ERROR_SOURCE_STATE enumeration defines the different runtime states for an error source. |
| [WHEA_ERROR_SOURCE_TYPE enumeration](ne-ntddk--whea-error-source-type.md) | The WHEA_ERROR_SOURCE_TYPE enumeration defines the different types of error sources that can report hardware errors. |
| [WHEA_ERROR_TYPE enumeration](ne-ntddk--whea-error-type.md) | The WHEA_ERROR_TYPE enumeration defines the different types of hardware components that can report a hardware error. |
| [WHEA_RAW_DATA_FORMAT enumeration](ne-ntddk--whea-raw-data-format.md) | The WHEA_RAW_DATA_FORMAT enumeration defines the possible formats that raw hardware error data can be encoded in a hardware error packet. |
