# Declarations in the wdm header
This header Wdm contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [ZwMapViewOfSection function](nf-wdm-zwmapviewofsection.md) | The ZwMapViewOfSection routine maps a view of a section into the virtual address space of a subject process. |
| [_InlineInterlockedExchange64 function](nf-wdm--inlineinterlockedexchange64.md) | TBD |
| [_InlineInterlockedDecrement64 function](nf-wdm--inlineinterlockeddecrement64.md) | TBD |
| [WRITE_PORT_BUFFER_UCHAR function](nf-wdm-write-port-buffer-uchar.md) | The WRITE_PORT_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified port. |
| [IoWMIQuerySingleInstanceMultiple function](nf-wdm-iowmiquerysingleinstancemultiple.md) | The IoWMIQuerySingleInstanceMultiple routine returns all WMI data block instances that implement the specified WMI classes with the specified instance names. |
| [IoBuildAsynchronousFsdRequest function](nf-wdm-iobuildasynchronousfsdrequest.md) | The IoBuildAsynchronousFsdRequest routine allocates and sets up an IRP to be sent to lower-level drivers. |
| [IoSkipCurrentIrpStackLocation function](nf-wdm-ioskipcurrentirpstacklocation.md) | TBD |
| [ExAllocateTimer function](nf-wdm-exallocatetimer.md) | The ExAllocateTimer routine allocates and initializes a timer object. |
| [MapWakeDepthToDstate function](nf-wdm-mapwakedepthtodstate.md) | TBD |
| [IMAGE_POLICY_START function](nf-wdm-image-policy-start.md) | TBD |
| [DbgQueryDebugFilterState function](nf-wdm-dbgquerydebugfilterstate.md) | TBD |
| [KeDeregisterBoundCallback function](nf-wdm-kederegisterboundcallback.md) | The KeDeregisterBoundCallback routine deregisters a user-mode bound exception callback registered by KeRegisterBoundCallback. |
| [IS_TARGET_UNWIND function](nf-wdm-is-target-unwind.md) | TBD |
| [TmDereferenceEnlistmentKey function](nf-wdm-tmdereferenceenlistmentkey.md) | The TmDereferenceEnlistmentKey routine decrements the reference count for the key of a specified enlistment object. |
| [RtlInitAnsiStringEx function](nf-wdm-rtlinitansistringex.md) | TBD |
| [IoDisconnectInterrupt function](nf-wdm-iodisconnectinterrupt.md) | The IoDisconnectInterrupt routine releases a device driver's set of interrupt object(s) when the device is paused or removed, or when the driver is being unloaded. |
| [KeQueryUnbiasedInterruptTimePrecise function](nf-wdm-kequeryunbiasedinterrupttimeprecise.md) | TBD |
| [ExfInterlockedCompareExchange64 function](nf-wdm-exfinterlockedcompareexchange64.md) | TBD |
| [MmLockPagableDataSection function](nf-wdm-mmlockpagabledatasection.md) | The MmLockPagableDataSection routine locks an entire section of driver data into system space. |
| [RtlEnlargedUnsignedMultiply function](nf-wdm-rtlenlargedunsignedmultiply.md) | TBD |
| [IoWMIHandleToInstanceName function](nf-wdm-iowmihandletoinstancename.md) | The IoWMIHandleToInstanceName routine determines the instance name for the WMI class instance implemented by the driver that is specified by a file handle. |
| [ExInterlockedDecrementLong function](nf-wdm-exinterlockeddecrementlong.md) | TBD |
| [IoCompleteRequest function](nf-wdm-iocompleterequest.md) | The IoCompleteRequest routine indicates that the caller has completed all processing for a given I/O request and is returning the given IRP to the I/O manager. |
| [READ_PORT_ULONG function](nf-wdm-read-port-ulong~r2.md) | The READ_PORT_ULONG routine reads a ULONG value from the specified port address. |
| [RtlInterlockedAndBits function](nf-wdm-rtlinterlockedandbits.md) | TBD |
| [TmPropagationComplete function](nf-wdm-tmpropagationcomplete.md) | TBD |
| [ReadRaw8 function](nf-wdm-readraw8.md) | TBD |
| [KeQuerySystemTimePrecise function](nf-wdm-kequerysystemtimeprecise.md) | The KeQuerySystemTimePrecise routine retrieves the current system time, and is more precise than the KeQuerySystemTime routine. |
| [NtCreateTransactionManager function](nf-wdm-ntcreatetransactionmanager.md) | TBD |
| [ExGetExclusiveWaiterCount function](nf-wdm-exgetexclusivewaitercount.md) | The ExGetExclusiveWaiterCount routine returns the number of waiters on exclusive access to a given resource. |
| [PoSetSystemWake function](nf-wdm-posetsystemwake.md) | The PoSetSystemWake routine marks the specified IRP as one that contributed to waking the system from a sleep state. |
| [ClfsMgmtTailAdvanceFailure function](nf-wdm-clfsmgmttailadvancefailure.md) | The ClfsMgmtTailAdvanceFailure routine notifies CLFS management that the client could not advance the log's tail. |
| [IoUninitializeWorkItem function](nf-wdm-iouninitializeworkitem.md) | The IoUninitializeWorkItem routine uninitializes a work item that was initialized by IoInitializeWorkItem. |
| [IoCreateNotificationEvent function](nf-wdm-iocreatenotificationevent.md) | The IoCreateNotificationEvent routine creates or opens a named notification event used to notify one or more threads of execution that an event has occurred. |
| [READ_REGISTER_NOFENCE_BUFFER_ULONG function](nf-wdm-read-register-nofence-buffer-ulong.md) | TBD |
| [ClfsMgmtRegisterManagedClient function](nf-wdm-clfsmgmtregistermanagedclient.md) | The ClfsMgmtRegisterManagedClient routine creates a client that will manage a CLFS log. |
| [ClfsLsnGreater function](nf-wdm-clfslsngreater.md) | The ClfsLsnGreater routine determines whether one LSN is greater than another LSN. The two LSNs must be from the same stream. |
| [READ_REGISTER_NOFENCE_USHORT function](nf-wdm-read-register-nofence-ushort.md) | TBD |
| [ZwCreateKeyTransacted function](nf-wdm-zwcreatekeytransacted.md) | The ZwCreateKeyTransacted routine creates a new registry key or opens an existing one, and it associates the key with a transaction. |
| [PoFxCompleteIdleCondition function](nf-wdm-pofxcompleteidlecondition.md) | The PoFxCompleteIdleCondition routine informs the power management framework (PoFx) that the specified component has completed a pending change to the idle condition. |
| [RtlFindSetBits function](nf-wdm-rtlfindsetbits.md) | The RtlFindSetBits routine searches for a range of set bits of a requested size within a bitmap. |
| [ExInitializeSetTimerParameters function](nf-wdm-exinitializesettimerparameters.md) | The ExInitializeSetTimerParameters routine initializes an EXT_SET_PARAMETERS structure. |
| [WRITE_REGISTER_USHORT function](nf-wdm-write-register-ushort~r1.md) | The WRITE_REGISTER_USHORT routine writes a USHORT value to the specified address. |
| [YieldProcessor function](nf-wdm-yieldprocessor~r3.md) | TBD |
| [InterlockedDecrementSizeTNoFence function](nf-wdm-interlockeddecrementsizetnofence.md) | TBD |
| [ExAcquireRundownProtectionEx function](nf-wdm-exacquirerundownprotectionex.md) | The ExAcquireRundownProtectionEx routine tries to acquire run-down protection on a shared object so the caller can safely access the object. |
| [CTL_CODE function](nf-wdm-ctl-code.md) | TBD |
| [RtlUnicodeToUTF8N function](nf-wdm-rtlunicodetoutf8n.md) | The RtlUnicodeToUTF8N routine converts a Unicode string to a UTF-8 string. |
| [RtlLargeIntegerShiftLeft function](nf-wdm-rtllargeintegershiftleft.md) | TBD |
| [_InlineInterlockedAdd64 function](nf-wdm--inlineinterlockedadd64~r1.md) | TBD |
| [__readfsword function](nf-wdm---readfsword.md) | TBD |
| [IoForwardIrpSynchronously function](nf-wdm-ioforwardirpsynchronously.md) | The IoForwardIrpSynchronously routine sends an IRP to a specified driver and waits for that driver to complete the IRP. |
| [WRITE_PORT_USHORT function](nf-wdm-write-port-ushort.md) | The WRITE_PORT_USHORT routine writes a USHORT value to the specified port address. |
| [KeInitializeSemaphore function](nf-wdm-keinitializesemaphore.md) | The KeInitializeSemaphore routine initializes a semaphore object with a specified count and specifies an upper limit that the count can attain. |
| [PsGetCurrentThread function](nf-wdm-psgetcurrentthread.md) | The PsGetCurrentThread routine identifies the current thread. |
| [READ_REGISTER_BUFFER_USHORT function](nf-wdm-read-register-buffer-ushort~r3.md) | The READ_REGISTER_BUFFER_USHORT routine reads a number of USHORT values from the specified register address into a buffer. |
| [IoUpdateShareAccess function](nf-wdm-ioupdateshareaccess.md) | The IoUpdateShareAccess routine updates the share access for the given file object, usually when the file is being opened. |
| [PsQueryTotalCycleTimeProcess function](nf-wdm-psquerytotalcycletimeprocess.md) | The PsQueryTotalCycleTimeProcess routine returns the accumulated cycle time for the specified process. |
| [ZwOpenTransaction function](nf-wdm-zwopentransaction.md) | The ZwOpenTransaction routine obtains a handle to an existing transaction object. |
| [IoQueueWorkItemEx function](nf-wdm-ioqueueworkitemex.md) | The IoQueueWorkItemEx routine associates a WorkItemEx routine with a work item, and it inserts the work item into a queue for later processing by a system worker thread. |
| [IoCallDriver function](nf-wdm-iocalldriver.md) | The IoCallDriver routine sends an IRP to the driver associated with a specified device object. |
| [IoCancelIrp function](nf-wdm-iocancelirp.md) | The IoCancelIrp routine sets the cancel bit in a given IRP and calls the cancel routine for the IRP if there is one. |
| [ObfReferenceObject function](nf-wdm-obfreferenceobject.md) | TBD |
| [PoSetThermalPassiveCooling function](nf-wdm-posetthermalpassivecooling.md) | TBD |
| [ClfsLsnDifference function](nf-wdm-clfslsndifference.md) | TBD |
| [ExGetSystemFirmwareTable function](nf-wdm-exgetsystemfirmwaretable.md) | TBD |
| [__PREfastPagedCode function](nf-wdm---prefastpagedcode.md) | TBD |
| [ExReleaseRundownProtectionCacheAwareEx function](nf-wdm-exreleaserundownprotectioncacheawareex.md) | TBD |
| [WRITE_PORT_USHORT function](nf-wdm-write-port-ushort~r1.md) | The WRITE_PORT_USHORT routine writes a USHORT value to the specified port address. |
| [SeUnregisterImageVerificationCallback function](nf-wdm-seunregisterimageverificationcallback.md) | TBD |
| [ExSetFirmwareEnvironmentVariable function](nf-wdm-exsetfirmwareenvironmentvariable.md) | The ExSetFirmwareEnvironmentVariable routine sets the value of the specified system firmware environment variable. |
| [ExAllocateFromPagedLookasideList function](nf-wdm-exallocatefrompagedlookasidelist~r1.md) | The ExAllocateFromPagedLookasideList routine returns a pointer to a paged entry from the given lookaside list, or it returns a pointer to a newly allocated paged entry. |
| [RtlSecureZeroMemory function](nf-wdm-rtlsecurezeromemory.md) | The RtlSecureZeroMemory routine fills a block of memory with zeros in a way that is guaranteed to be secure. |
| [NtPrepareEnlistment function](nf-wdm-ntprepareenlistment.md) | TBD |
| [KeGetCurrentIrql function](nf-wdm-kegetcurrentirql~r2.md) | The KeGetCurrentIrql routine returns the current IRQL. |
| [_InlineInterlockedCompareExchangePointer function](nf-wdm--inlineinterlockedcompareexchangepointer.md) | TBD |
| [MmAllocateMdlForIoSpace function](nf-wdm-mmallocatemdlforiospace.md) | The MmAllocateMdlForIoSpace routine allocates an MDL and initializes this MDL to describe a set of physical address ranges in I/O address space. |
| [WriteULongRelease function](nf-wdm-writeulongrelease.md) | TBD |
| [IsEqualGUIDAligned function](nf-wdm-isequalguidaligned.md) | TBD |
| [IoCopyCurrentIrpStackLocationToNext function](nf-wdm-iocopycurrentirpstacklocationtonext.md) | The IoCopyCurrentIrpStackLocationToNext routine copies the IRP stack parameters from the current I/O stack location to the stack location of the next-lower driver. |
| [KdPrint function](nf-wdm-kdprint.md) | The KdPrint macro sends a message to the kernel debugger. |
| [InterlockedIncrement16 function](nf-wdm-interlockedincrement16~r1.md) | TBD |
| [ReadPointerNoFence function](nf-wdm-readpointernofence.md) | TBD |
| [PoFxStartDevicePowerManagement function](nf-wdm-pofxstartdevicepowermanagement.md) | The PoFxStartDevicePowerManagement routine completes the registration of a device with the power management framework (PoFx) and starts device power management. |
| [IoInitializeThreadedDpcRequest function](nf-wdm-ioinitializethreadeddpcrequest.md) | TBD |
| [ObDereferenceObjectDeferDeleteWithTag function](nf-wdm-obdereferenceobjectdeferdeletewithtag.md) | The ObDereferenceObjectDeferDeleteWithTag routine decrements the reference count for the specified object, defers deletion of the object to avoid deadlocks, and writes a four-byte tag value to the object to support object reference tracing. |
| [WRITE_REGISTER_NOFENCE_BUFFER_USHORT function](nf-wdm-write-register-nofence-buffer-ushort.md) | TBD |
| [IoAcquireRemoveLock function](nf-wdm-ioacquireremovelock.md) | The IoAcquireRemoveLock routine increments the count for a remove lock, indicating that the associated device object should not be detached from the device stack or deleted. |
| [KeGetCurrentNodeNumber function](nf-wdm-kegetcurrentnodenumber.md) | The KeGetCurrentNodeNumber routine gets the NUMA node number for the logical processor that the caller is running on. |
| [ALIGN_DOWN_BY function](nf-wdm-align-down-by.md) | TBD |
| [NtCreateTransaction function](nf-wdm-ntcreatetransaction.md) | TBD |
| [RtlFindLeastSignificantBit function](nf-wdm-rtlfindleastsignificantbit.md) | The RtlFindLeastSignificantBit routine returns the zero-based position of the least significant nonzero bit in its parameter. |
| [_bittestandcomplement64 function](nf-wdm--bittestandcomplement64.md) | TBD |
| [ReadTimeStampCounter function](nf-wdm-readtimestampcounter~r3.md) | TBD |
| [RtlLargeIntegerLessThanZero function](nf-wdm-rtllargeintegerlessthanzero.md) | TBD |
| [IsListEmpty function](nf-wdm-islistempty.md) | The IsListEmpty routine indicates whether a doubly linked list of LIST_ENTRY structures is empty. |
| [RtlUnicodeStringToAnsiString function](nf-wdm-rtlunicodestringtoansistring.md) | The RtlUnicodeStringToAnsiString routine converts a given Unicode string into an ANSI string. |
| [IoRegisterDeviceInterface function](nf-wdm-ioregisterdeviceinterface.md) | The IoRegisterDeviceInterface routine registers a device interface class, if it has not been previously registered, and creates a new instance of the interface class, which a driver can subsequently enable for use by applications or other system components. |
| [InterlockedCompareExchange function](nf-wdm-interlockedcompareexchange.md) | The InterlockedCompareExchange routine performs an atomic operation that compares the input value pointed to by Destination with the value of Comparand. |
| [IoCreateSymbolicLink function](nf-wdm-iocreatesymboliclink.md) | The IoCreateSymbolicLink routine sets up a symbolic link between a device object name and a user-visible name for the device. |
| [WRITE_PORT_BUFFER_ULONG function](nf-wdm-write-port-buffer-ulong~r2.md) | The WRITE_PORT_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified port address. |
| [KdBreakPointWithStatus function](nf-wdm-kdbreakpointwithstatus.md) | The KdBreakPointWithStatus macro breaks into the kernel debugger and sends the value of Status to the debugger. |
| [MmMapLockedPages function](nf-wdm-mmmaplockedpages.md) | The MmMapLockedPages routine is obsolete for Windows 2000 and later versions of Windows, and for Windows Me. |
| [MmUnlockPagableImageSection function](nf-wdm-mmunlockpagableimagesection.md) | The MmUnlockPagableImageSection routine releases a section of driver code or driver data, previously locked into system space with MmLockPagableCodeSection, MmLockPagableDataSection or MmLockPagableSectionByHandle, so the section can be paged out again. |
| [KeReadStateSemaphore function](nf-wdm-kereadstatesemaphore.md) | The KeReadStateSemaphore routine returns the current state, signaled or not-signaled, of the specified semaphore object. |
| [NtPrepareComplete function](nf-wdm-ntpreparecomplete.md) | TBD |
| [READ_REGISTER_BUFFER_ULONG function](nf-wdm-read-register-buffer-ulong~r2.md) | The READ_REGISTER_BUFFER_ULONG routine reads a number of ULONG values from the specified register address into a buffer. |
| [MmAllocateMappingAddress function](nf-wdm-mmallocatemappingaddress.md) | The MmAllocateMappingAddress routine reserves a range of system virtual address space of the specified size. |
| [WRITE_REGISTER_ULONG function](nf-wdm-write-register-ulong~r3.md) | The WRITE_REGISTER_ULONG routine writes a ULONG value to the specified address. |
| [READ_REGISTER_BUFFER_ULONG function](nf-wdm-read-register-buffer-ulong.md) | The READ_REGISTER_BUFFER_ULONG routine reads a number of ULONG values from the specified register address into a buffer. |
| [EtwWriteTransfer function](nf-wdm-etwwritetransfer.md) | The EtwWriteTransfer function marks an event that links two activities together; this type of event is referred to as a transfer event. |
| [WmiTraceMessageVa function](nf-wdm-wmitracemessageva.md) | The WmiTraceMessageVa routine adds a message to the output log of a WPP software tracing session. |
| [KeInitializeTimerEx function](nf-wdm-keinitializetimerex.md) | The KeInitializeTimerEx routine initializes an extended kernel timer object. |
| [RtlExtendedIntegerMultiply function](nf-wdm-rtlextendedintegermultiply~r1.md) | TBD |
| [RtlDeleteRegistryValue function](nf-wdm-rtldeleteregistryvalue.md) | The RtlDeleteRegistryValue routine removes the specified entry name and the associated values from the registry along the given relative path. |
| [WriteRaw function](nf-wdm-writeraw.md) | TBD |
| [PoSetDeviceBusyEx function](nf-wdm-posetdevicebusyex.md) | The PoSetDeviceBusyEx routine notifies the power manager that the device associated with the specified idle counter is busy. |
| [ExInterlockedRemoveHeadList function](nf-wdm-exinterlockedremoveheadlist.md) | The ExInterlockedRemoveHeadList routine removes an entry from the beginning of a doubly linked list of LIST_ENTRY structures. |
| [ExReInitializeRundownProtection function](nf-wdm-exreinitializerundownprotection.md) | The ExReInitializeRundownProtection routine reinitializes an EX_RUNDOWN_REF structure after the associated object is run down. |
| [KzLowerIrql function](nf-wdm-kzlowerirql.md) | TBD |
| [KeSetTimerEx function](nf-wdm-kesettimerex.md) | The KeSetTimerEx routine sets the absolute or relative interval at which a timer object is to be set to a signaled state, optionally supplies a CustomTimerDpc routine to be executed when that interval expires, and optionally supplies a recurring interval for the timer. |
| [ExReleaseRundownProtection function](nf-wdm-exreleaserundownprotection.md) | The ExReleaseRundownProtection routine releases run-down protection that the caller previously acquired by calling the ExAcquireRundownProtection routine. |
| [SeValidSecurityDescriptor function](nf-wdm-sevalidsecuritydescriptor.md) | The SeValidSecurityDescriptor routine returns whether a given security descriptor is structurally valid. |
| [UnsignedMultiply128 function](nf-wdm-unsignedmultiply128.md) | TBD |
| [READ_REGISTER_BUFFER_UCHAR function](nf-wdm-read-register-buffer-uchar~r1.md) | The READ_REGISTER_BUFFER_UCHAR routine reads a number of bytes from the specified register address into a buffer. |
| [IoSetShareAccessEx function](nf-wdm-iosetshareaccessex.md) | The IoSetShareAccessEx routine sets the access rights for sharing the specified file object. |
| [RtlInterlockedSetBits function](nf-wdm-rtlinterlockedsetbits.md) | TBD |
| [RTL_VERIFYMSG function](nf-wdm-rtl-verifymsg.md) | TBD |
| [MultiplyHigh function](nf-wdm-multiplyhigh.md) | TBD |
| [READ_REGISTER_UCHAR function](nf-wdm-read-register-uchar~r3.md) | The READ_REGISTER_UCHAR routine reads a byte from the specified register address. |
| [IoGetContainerInformation function](nf-wdm-iogetcontainerinformation.md) | The IoGetContainerInformation routine provides information about the current state of a user session. |
| [KeQueryTimeIncrement function](nf-wdm-kequerytimeincrement.md) | The KeQueryTimeIncrement routine returns the number of 100-nanosecond units that are added to the system time each time the interval clock interrupts. |
| [RtlLargeIntegerEqualToZero function](nf-wdm-rtllargeintegerequaltozero.md) | TBD |
| [RtlCopyMemory function](nf-wdm-rtlcopymemory.md) | The RtlCopyMemory routine copies the contents of a source memory block to a destination memory block. |
| [TmSinglePhaseReject function](nf-wdm-tmsinglephasereject.md) | The TmSinglePhaseReject routine informs KTM that the calling resource manager will not support a single-phase commit operation for a specified enlistment. |
| [READ_PORT_USHORT function](nf-wdm-read-port-ushort~r1.md) | The READ_PORT_USHORT routine reads a USHORT value from the specified port address. |
| [InterlockedPopEntrySList function](nf-wdm-interlockedpopentryslist~r1.md) | TBD |
| [KeRegisterBugCheckCallback function](nf-wdm-keregisterbugcheckcallback.md) | The KeRegisterBugCheckCallback routine registers a BugCheckCallback routine, which executes when the operating system issues a bug check. |
| [PoRegisterSystemState function](nf-wdm-poregistersystemstate.md) | The PoRegisterSystemState routine registers the system as busy due to certain activity. |
| [TmPrepareComplete function](nf-wdm-tmpreparecomplete.md) | The TmPrepareComplete routine notifies KTM that the calling resource manager has finished preparing a transaction's data. |
| [RtlSetAllBits function](nf-wdm-rtlsetallbits.md) | The RtlSetAllBits routine sets all bits in a given bitmap variable. |
| [IoSetShareAccess function](nf-wdm-iosetshareaccess.md) | The IoSetShareAccess routine sets the access rights for sharing the given file object. |
| [KeFlushIoBuffers function](nf-wdm-keflushiobuffers~r3.md) | The KeFlushIoBuffers routine flushes the memory region described by an MDL from caches of all processors. |
| [_InlineInterlockedOr64 function](nf-wdm--inlineinterlockedor64.md) | TBD |
| [InterlockedCompareExchange16 function](nf-wdm-interlockedcompareexchange16.md) | TBD |
| [ZwPrePrepareComplete function](nf-wdm-zwprepreparecomplete.md) | The ZwPrePrepareComplete routine notifies KTM that the calling resource manager has finished preliminary preparation of a transaction's data. |
| [__fastfail function](nf-wdm---fastfail.md) | TBD |
| [IoSetLinkShareAccess function](nf-wdm-iosetlinkshareaccess.md) | The IoSetLinkShareAccess routine sets the access rights for link sharing the specified file object. |
| [PoStartNextPowerIrp function](nf-wdm-postartnextpowerirp.md) | The PoStartNextPowerIrp routine signals the power manager that the driver is ready to handle the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only.). |
| [FirstEntrySList function](nf-wdm-firstentryslist.md) | The FirstEntrySList routine returns the first entry in a sequenced singly linked list. |
| [_InterlockedDecrement16 function](nf-wdm--interlockeddecrement16.md) | TBD |
| [READ_REGISTER_BUFFER_ULONG function](nf-wdm-read-register-buffer-ulong~r3.md) | The READ_REGISTER_BUFFER_ULONG routine reads a number of ULONG values from the specified register address into a buffer. |
| [RtlClearBits function](nf-wdm-rtlclearbits.md) | The RtlClearBits routine sets all bits in the specified range of bits in the bitmap to zero. |
| [InterlockedAnd function](nf-wdm-interlockedand.md) | The InterlockedAnd macro atomically computes a bitwise AND operation. |
| [ExAllocateFromNPagedLookasideList function](nf-wdm-exallocatefromnpagedlookasidelist.md) | The ExAllocateFromNPagedLookasideList routine returns a pointer to a nonpaged entry from the given lookaside list, or it returns a pointer to a newly allocated nonpaged entry. |
| [MmProbeAndLockProcessPages function](nf-wdm-mmprobeandlockprocesspages.md) | TBD |
| [__writecr3 function](nf-wdm---writecr3.md) | TBD |
| [RtlLargeIntegerLessThanOrEqualTo function](nf-wdm-rtllargeintegerlessthanorequalto.md) | TBD |
| [KeRestoreFloatingPointState function](nf-wdm-kerestorefloatingpointstate~r1.md) | The KeRestoreFloatingPointState routine restores the nonvolatile floating-point context saved by the preceding call to KeSaveFloatingPointState. |
| [ExAllocatePoolWithQuotaTag function](nf-wdm-exallocatepoolwithquotatag~r1.md) | The ExAllocatePoolWithQuotaTag routine allocates pool memory, charging the quota against the current process. |
| [EtwActivityIdControl function](nf-wdm-etwactivityidcontrol.md) | The EtwActivityIdControl function creates, queries, and sets the current activity identifier. |
| [WRITE_REGISTER_NOFENCE_USHORT function](nf-wdm-write-register-nofence-ushort.md) | TBD |
| [IoWMIQueryAllData function](nf-wdm-iowmiqueryalldata.md) | The IoWMIQueryAllData routine returns all WMI data blocks that implement a given WMI class. |
| [IoGetCurrentIrpStackLocation function](nf-wdm-iogetcurrentirpstacklocation.md) | The IoGetCurrentIrpStackLocation routine returns a pointer to the caller's I/O stack location in the specified IRP. |
| [KeReleaseSpinLock function](nf-wdm-kereleasespinlock.md) | The KeReleaseSpinLock routine releases a spin lock and restores the original IRQL at which the caller was running. |
| [MmGetSystemAddressForMdlSafe function](nf-wdm-mmgetsystemaddressformdlsafe.md) | TBD |
| [__stosb function](nf-wdm---stosb.md) | TBD |
| [PoFxSetComponentLatency function](nf-wdm-pofxsetcomponentlatency.md) | The PoFxSetComponentLatency routine specifies the maximum latency that can be tolerated in the transition from the idle condition to the active condition in the specified component. |
| [RtlInterlockedAndBitsDiscardReturn function](nf-wdm-rtlinterlockedandbitsdiscardreturn.md) | TBD |
| [RtlInterlockedSetBitsDiscardReturn function](nf-wdm-rtlinterlockedsetbitsdiscardreturn.md) | TBD |
| [IoStartNextPacket function](nf-wdm-iostartnextpacket.md) | The IoStartNextPacket routine dequeues the next IRP, if any, from the given device object's associated device queue and calls the driver's StartIo routine. |
| [SeReleaseSubjectContext function](nf-wdm-sereleasesubjectcontext.md) | TBD |
| [RTL_STATIC_LIST_HEAD function](nf-wdm-rtl-static-list-head.md) | TBD |
| [DbgBreakPointWithStatus function](nf-wdm-dbgbreakpointwithstatus.md) | The DbgBreakPointWithStatus routine breaks into the kernel debugger and sends the value of Status to the debugger. |
| [READ_PORT_BUFFER_USHORT function](nf-wdm-read-port-buffer-ushort~r3.md) | The READ_PORT_BUFFER_USHORT routine reads a number of USHORT values from the specified port address into a buffer. |
| [ExSystemTimeToLocalTime function](nf-wdm-exsystemtimetolocaltime.md) | The ExSystemTimeToLocalTime routine converts a GMT system time value to the local system time for the current time zone. |
| [RtlFindClearRuns function](nf-wdm-rtlfindclearruns.md) | The RtlFindClearRuns routine finds the specified number of runs of clear bits within a given bitmap. |
| [KdChangeOption function](nf-wdm-kdchangeoption.md) | The KdChangeOption routine accesses and changes state in the kernel that is related to kernel debugging. |
| [ZwQueryInformationFile function](nf-wdm-zwqueryinformationfile.md) | The ZwQueryInformationFile routine returns various kinds of information about a file object. |
| [InitializeListHead32 function](nf-wdm-initializelisthead32.md) | TBD |
| [_BitScanReverse function](nf-wdm--bitscanreverse~r1.md) | TBD |
| [KeInitializeCallbackRecord function](nf-wdm-keinitializecallbackrecord.md) | TBD |
| [IoRecordIoAttribution function](nf-wdm-iorecordioattribution.md) | TBD |
| [PoFxRegisterDripsWatchdogCallback function](nf-wdm-pofxregisterdripswatchdogcallback.md) | TBD |
| [IoSetStartIoAttributes function](nf-wdm-iosetstartioattributes.md) | The IoSetStartIoAttributes routine sets attributes for the driver's StartIo routine. |
| [InterlockedExchangeAddSizeTNoFence function](nf-wdm-interlockedexchangeaddsizetnofence.md) | TBD |
| [ReadAcquire function](nf-wdm-readacquire~r2.md) | TBD |
| [InterlockedCompareExchangePointer function](nf-wdm-interlockedcompareexchangepointer.md) | The InterlockedCompareExchangePointer routine performs an atomic operation that compares the input pointer value pointed to by Destination with the pointer value Comparand. |
| [MmAddVerifierThunks function](nf-wdm-mmaddverifierthunks.md) | TBD |
| [KeTryToAcquireSpinLockAtDpcLevel function](nf-wdm-ketrytoacquirespinlockatdpclevel.md) | The KeTryToAcquireSpinLockAtDpcLevel routine attempts to acquire a spin lock at DISPATCH_LEVEL. |
| [InterlockedXor function](nf-wdm-interlockedxor.md) | The InterlockedOr routine atomically computes a bitwise exclusive OR operation. |
| [WRITE_REGISTER_NOFENCE_BUFFER_UCHAR function](nf-wdm-write-register-nofence-buffer-uchar~r1.md) | TBD |
| [InterlockedOr8 function](nf-wdm-interlockedor8~r1.md) | TBD |
| [KeRestoreExtendedProcessorState function](nf-wdm-kerestoreextendedprocessorstate.md) | The KeRestoreExtendedProcessorState routine restores extended processor state information that was previously saved. |
| [KeWaitForMultipleObjects function](nf-wdm-kewaitformultipleobjects.md) | The KeWaitForMultipleObjects routine puts the current thread into an alertable or nonalertable wait state until any or all of a number of dispatcher objects are set to a signaled state or (optionally) until the wait times out. |
| [RtlFindNextForwardRunClear function](nf-wdm-rtlfindnextforwardrunclear.md) | The RtlFindNextForwardRunClear routine searches a given bitmap variable for the next clear run of bits, starting from the specified index position. |
| [ExAcquireSpinLock function](nf-wdm-exacquirespinlock.md) | TBD |
| [IMAGE_POLICY_BOOL function](nf-wdm-image-policy-bool.md) | TBD |
| [ClfsCreateMarshallingArea function](nf-wdm-clfscreatemarshallingarea.md) | The ClfsCreateMarshallingArea routine creates a marshalling area for a CLFS stream and returns a pointer to an opaque context that represents the new marshalling area. |
| [KeInitializeMutex function](nf-wdm-keinitializemutex.md) | The KeInitializeMutex routine initializes a mutex object, setting it to a signaled state. |
| [__stosw function](nf-wdm---stosw.md) | TBD |
| [ExInitializeLookasideListEx function](nf-wdm-exinitializelookasidelistex.md) | The ExInitializeLookasideListEx routine initializes a lookaside list. |
| [KeRevertToUserGroupAffinityThread function](nf-wdm-kereverttousergroupaffinitythread.md) | The KeRevertToUserGroupAffinityThread routine restores the group affinity of the calling thread to its original value at the time that the thread was created. |
| [ExInterlockedPushEntrySList function](nf-wdm-exinterlockedpushentryslist.md) | The ExInterlockedPushEntrySList routine atomically inserts an entry at the beginning of a sequenced singly linked list. |
| [PoFxSetTargetDripsDevicePowerState function](nf-wdm-pofxsettargetdripsdevicepowerstate.md) | This routine is called to notify the power manager of the device's target device power state for DRIPS. The driver can override the DRIPS constraint provided by the PEP. |
| [RtlLargeIntegerGreaterThan function](nf-wdm-rtllargeintegergreaterthan.md) | TBD |
| [TmGetTransactionId function](nf-wdm-tmgettransactionid.md) | The TmGetTransactionId routine retrieves a transaction object's unit of work (UOW) identifier. |
| [KeDeregisterBugCheckCallback function](nf-wdm-kederegisterbugcheckcallback.md) | The KeDeregisterBugCheckCallback routine removes a callback routine that was registered by KeRegisterBugCheckCallback. |
| [IoAllocateErrorLogEntry function](nf-wdm-ioallocateerrorlogentry.md) | The IoAllocateErrorLogEntry routine allocates an error log entry, and returns a pointer to the packet that the caller uses to supply information about an I/O error. |
| [READ_PORT_USHORT function](nf-wdm-read-port-ushort.md) | The READ_PORT_USHORT routine reads a USHORT value from the specified port address. |
| [ZwEnumerateValueKey function](nf-wdm-zwenumeratevaluekey.md) | The ZwEnumerateValueKey routine gets information about the value entries of an open key. |
| [_bittestandcomplement function](nf-wdm--bittestandcomplement.md) | TBD |
| [NtPrePrepareEnlistment function](nf-wdm-ntpreprepareenlistment.md) | TBD |
| [KeInsertQueueDpc function](nf-wdm-keinsertqueuedpc.md) | The KeInsertQueueDpc routine queues a DPC for execution. |
| [IoMapTransfer function](nf-wdm-iomaptransfer.md) | TBD |
| [READ_REGISTER_NOFENCE_BUFFER_ULONG function](nf-wdm-read-register-nofence-buffer-ulong~r1.md) | TBD |
| [InterlockedIncrementSizeTNoFence function](nf-wdm-interlockedincrementsizetnofence.md) | TBD |
| [IoAllocateWorkItem function](nf-wdm-ioallocateworkitem.md) | The IoAllocateWorkItem routine allocates a work item. |
| [ReadAcquire8 function](nf-wdm-readacquire8~r1.md) | TBD |
| [ClfsDeleteLogByPointer function](nf-wdm-clfsdeletelogbypointer.md) | The ClfsDeleteLogByPointer routine marks a CLFS stream for deletion. |
| [ClfsEarlierLsn function](nf-wdm-clfsearlierlsn.md) | TBD |
| [WRITE_PORT_USHORT function](nf-wdm-write-port-ushort~r3.md) | The WRITE_PORT_USHORT routine writes a USHORT value to the specified port address. |
| [PoFxPowerControl function](nf-wdm-pofxpowercontrol.md) | The PoFxPowerControl routine sends a power control request to the power management framework (PoFx). |
| [ZwQueryInformationEnlistment function](nf-wdm-zwqueryinformationenlistment.md) | The ZwQueryInformationEnlistment routine retrieves information about a specified enlistment object. |
| [ExAcquireRundownProtectionCacheAwareEx function](nf-wdm-exacquirerundownprotectioncacheawareex.md) | TBD |
| [__addgsdword function](nf-wdm---addgsdword.md) | TBD |
| [KeQueryTotalCycleTimeThread function](nf-wdm-kequerytotalcycletimethread.md) | TBD |
| [IoGetCurrentProcess function](nf-wdm-iogetcurrentprocess.md) | The IoGetCurrentProcess routine returns a pointer to the current process. |
| [ClfsDeleteLogFile function](nf-wdm-clfsdeletelogfile.md) | The ClfsDeleteLogFile routine marks a CLFS stream for deletion. |
| [NtSetInformationEnlistment function](nf-wdm-ntsetinformationenlistment.md) | TBD |
| [ClfsLaterLsn function](nf-wdm-clfslaterlsn.md) | TBD |
| [RtlIsServicePackVersionInstalled function](nf-wdm-rtlisservicepackversioninstalled.md) | The RtlIsServicePackVersionInstalled routine determines if a specified service pack version of the Microsoft Windows device driver interface (DDI) is installed. |
| [PopulationCount64 function](nf-wdm-populationcount64.md) | TBD |
| [PoUnregisterSystemState function](nf-wdm-pounregistersystemstate.md) | The PoUnregisterSystemState routine cancels a system state registration created by PoRegisterSystemState. |
| [ReadUCharAcquire function](nf-wdm-readucharacquire.md) | TBD |
| [ExInterlockedIncrementLong function](nf-wdm-exinterlockedincrementlong.md) | TBD |
| [PoSetPowerRequest function](nf-wdm-posetpowerrequest.md) | The PoSetPowerRequest routine increments the count for the specified power request type. |
| [TmCreateEnlistment function](nf-wdm-tmcreateenlistment.md) | The TmCreateEnlistment routine creates a new enlistment object for a transaction. |
| [KeDelayExecutionThread function](nf-wdm-kedelayexecutionthread.md) | The KeDelayExecutionThread routine puts the current thread into an alertable or nonalertable wait state for a specified interval. |
| [MmAdvanceMdl function](nf-wdm-mmadvancemdl.md) | The MmAdvanceMdl routine advances the beginning of an MDL's virtual memory range by the specified number of bytes. |
| [_bittest function](nf-wdm--bittest~r1.md) | TBD |
| [COMPUTE_PAGES_SPANNED function](nf-wdm-compute-pages-spanned.md) | TBD |
| [InterlockedExchangeAdd8 function](nf-wdm-interlockedexchangeadd8.md) | TBD |
| [EtwRegister function](nf-wdm-etwregister.md) | The EtwRegister function registers the event provider and must be called before a provider can start tracing. |
| [FIRSTBYTE function](nf-wdm-firstbyte.md) | TBD |
| [_InterlockedAnd16 function](nf-wdm--interlockedand16.md) | TBD |
| [ClfsCreateScanContext function](nf-wdm-clfscreatescancontext.md) | The ClfsCreateScanContext routine creates a scan context that can be used to iterate over the containers of a specified CLFS log. |
| [IMAGE_POLICY_UNICODE_STRING function](nf-wdm-image-policy-unicode-string.md) | TBD |
| [NT_ASSERTMSGW_ASSUME function](nf-wdm-nt-assertmsgw-assume.md) | TBD |
| [ReadAcquire8 function](nf-wdm-readacquire8~r2.md) | TBD |
| [NtOpenResourceManager function](nf-wdm-ntopenresourcemanager.md) | TBD |
| [InterlockedExchangeAdd64 function](nf-wdm-interlockedexchangeadd64.md) | TBD |
| [__inbyte function](nf-wdm---inbyte.md) | TBD |
| [_bittestandset function](nf-wdm--bittestandset.md) | TBD |
| [WriteUCharRaw function](nf-wdm-writeucharraw.md) | TBD |
| [IoStartTimer function](nf-wdm-iostarttimer.md) | The IoStartTimer routine enables the timer associated with a given device object so the driver-supplied IoTimer routine is called once per second. |
| [WriteRelease function](nf-wdm-writerelease~r1.md) | TBD |
| [KeRevertToUserAffinityThreadEx function](nf-wdm-kereverttouseraffinitythreadex.md) | The KeRevertToUserAffinityThreadEx routine restores the previous affinity of the current thread. |
| [IoWMIDeviceObjectToInstanceName function](nf-wdm-iowmideviceobjecttoinstancename.md) | The IoWMIDeviceObjectToInstanceName routine determines the instance name for the WMI class instance implemented by the driver that is specified by a device object. |
| [WRITE_REGISTER_ULONG64 function](nf-wdm-write-register-ulong64.md) | TBD |
| [KdDisableDebugger function](nf-wdm-kddisabledebugger.md) | The KdDisableDebugger routine disables the kernel debugger. |
| [READ_REGISTER_NOFENCE_BUFFER_UCHAR function](nf-wdm-read-register-nofence-buffer-uchar~r1.md) | TBD |
| [WriteULongNoFence function](nf-wdm-writeulongnofence.md) | TBD |
| [MmMapIoSpaceEx function](nf-wdm-mmmapiospaceex.md) | The MmMapIoSpaceEx routine maps the given physical address range to non-paged system space using the specified page protection. |
| [IoStopTimer function](nf-wdm-iostoptimer.md) | The IoStopTimer routine disables the timer for a specified device object so the driver-supplied IoTimer routine is not called. |
| [ExGetSharedWaiterCount function](nf-wdm-exgetsharedwaitercount.md) | The ExGetSharedWaiterCount routine returns the number of waiters on shared access to a given resource. |
| [InterlockedCompareExchange16 function](nf-wdm-interlockedcompareexchange16~r1.md) | TBD |
| [TmRecoverEnlistment function](nf-wdm-tmrecoverenlistment.md) | The TmRecoverEnlistment routine initiates a recovery operation for the transaction that is associated with a specified enlistment. |
| [ExAllocateFromPagedLookasideList function](nf-wdm-exallocatefrompagedlookasidelist.md) | The ExAllocateFromPagedLookasideList routine returns a pointer to a paged entry from the given lookaside list, or it returns a pointer to a newly allocated paged entry. |
| [InterlockedAnd64 function](nf-wdm-interlockedand64.md) | TBD |
| [DbgBreakPoint function](nf-wdm-dbgbreakpoint.md) | The DbgBreakPoint routine breaks into the kernel debugger. |
| [ClfsReserveAndAppendLog function](nf-wdm-clfsreserveandappendlog.md) | The ClfsReserveAndAppendLog routine reserves space in a marshalling area or appends a record to a marshalling area or does both atomically. |
| [KeRegisterBugCheckReasonCallback function](nf-wdm-keregisterbugcheckreasoncallback.md) | The KeRegisterBugCheckReasonCallback routine registers a BugCheckDumpIoCallback, BugCheckSecondaryDumpDataCallback, or BugCheckAddPagesCallback routine, which executes when the operating system issues a bug check. |
| [WRITE_REGISTER_USHORT function](nf-wdm-write-register-ushort~r3.md) | The WRITE_REGISTER_USHORT routine writes a USHORT value to the specified address. |
| [READ_PORT_UCHAR function](nf-wdm-read-port-uchar~r3.md) | The READ_PORT_UCHAR routine reads a byte from the specified port address. |
| [ZwRestoreKey function](nf-wdm-zwrestorekey.md) | TBD |
| [RtlRetrieveUshort function](nf-wdm-rtlretrieveushort.md) | TBD |
| [READ_REGISTER_BUFFER_ULONG64 function](nf-wdm-read-register-buffer-ulong64~r1.md) | TBD |
| [KeSaveFloatingPointState function](nf-wdm-kesavefloatingpointstate.md) | The KeSaveFloatingPointState routine saves the nonvolatile floating-point context so the caller can carry out floating-point operations. |
| [ExCreateCallback function](nf-wdm-excreatecallback.md) | The ExCreateCallback routine either creates a new callback object or opens an existing callback object on behalf of the caller. |
| [KeRemoveByKeyDeviceQueue function](nf-wdm-keremovebykeydevicequeue.md) | The KeRemoveByKeyDeviceQueue routine removes an entry, selected according to a sort key value, from the specified device queue. |
| [ClfsQueryLogFileInformation function](nf-wdm-clfsquerylogfileinformation.md) | The ClfsQueryLogFileInformation routine returns metadata and state information for a specified CLFS stream or its underlying physical log or both. |
| [RtlConvertUlongToLargeInteger function](nf-wdm-rtlconvertulongtolargeinteger.md) | The RtlConvertUlongToLargeInteger routine converts the input unsigned integer to a signed large integer. For Windows XP and later versions of Windows, do not use this routine; use the native support for __int64. |
| [ZwCreateFile function](nf-wdm-zwcreatefile.md) | The ZwCreateFile routine creates a new file or opens an existing file. |
| [IoRequestDeviceEject function](nf-wdm-iorequestdeviceeject.md) | The IoRequestDeviceEject routine notifies the PnP manager that the device eject button was pressed. |
| [memcpy_inline function](nf-wdm-memcpy-inline.md) | TBD |
| [ExAllocatePoolWithTagPriority function](nf-wdm-exallocatepoolwithtagpriority.md) | The ExAllocatePoolWithTagPriority routine allocates pool memory of the specified type. |
| [IoReleaseRemoveLockEx function](nf-wdm-ioreleaseremovelockex.md) | TBD |
| [NtQueryInformationResourceManager function](nf-wdm-ntqueryinformationresourcemanager.md) | TBD |
| [MmCreateMdl function](nf-wdm-mmcreatemdl.md) | TBD |
| [ZwOpenEnlistment function](nf-wdm-zwopenenlistment.md) | The ZwOpenEnlistment routine obtains a handle to an existing enlistment object. |
| [RtlTimeFieldsToTime function](nf-wdm-rtltimefieldstotime.md) | The RtlTimeFieldsToTime routine converts TIME_FIELDS information to a system time value. |
| [_mm_setcsr function](nf-wdm--mm-setcsr.md) | TBD |
| [__writecr8 function](nf-wdm---writecr8.md) | TBD |
| [InterlockedFlushSList function](nf-wdm-interlockedflushslist.md) | TBD |
| [WRITE_REGISTER_BUFFER_ULONG64 function](nf-wdm-write-register-buffer-ulong64.md) | TBD |
| [IoDisconnectInterruptEx function](nf-wdm-iodisconnectinterruptex.md) | For more information, see the WdmlibIoDisconnectInterruptEx function.#define IoDisconnectInterruptEx WdmlibIoDisconnectInterruptEx |
| [ReadAcquire64 function](nf-wdm-readacquire64~r1.md) | TBD |
| [RtlTimeToTimeFields function](nf-wdm-rtltimetotimefields.md) | The RtlTimeToTimeFields routine converts system time into a TIME_FIELDS structure. |
| [RtlAnsiStringToUnicodeSize function](nf-wdm-rtlansistringtounicodesize.md) | The RtlAnsiStringToUnicodeSize routine returns the number of bytes required to hold an ANSI string converted into a Unicode string. |
| [ReadNoFence16 function](nf-wdm-readnofence16~r1.md) | TBD |
| [KfRaiseIrql function](nf-wdm-kfraiseirql~r2.md) | TBD |
| [ClfsLsnNull function](nf-wdm-clfslsnnull.md) | The ClfsLsnNull routine determines whether a specified LSN is equal to the smallest possible LSN, CLFS_LSN_NULL. |
| [__wbinvd function](nf-wdm---wbinvd.md) | TBD |
| [WriteBooleanRelease function](nf-wdm-writebooleanrelease.md) | TBD |
| [WriteNoFence function](nf-wdm-writenofence~r2.md) | TBD |
| [InterlockedPopEntrySList function](nf-wdm-interlockedpopentryslist.md) | TBD |
| [IoWMISetSingleItem function](nf-wdm-iowmisetsingleitem.md) | The IoWMISetSingleItem routine sets a single property in the data block instance that matches the specified WMI class and instance name. |
| [NtRollforwardTransactionManager function](nf-wdm-ntrollforwardtransactionmanager.md) | TBD |
| [WRITE_REGISTER_USHORT function](nf-wdm-write-register-ushort~r2.md) | The WRITE_REGISTER_USHORT routine writes a USHORT value to the specified address. |
| [ExInterlockedPopEntrySList function](nf-wdm-exinterlockedpopentryslist.md) | The ExInterlockedPopEntrySList routine atomically removes the first entry from a sequenced singly linked list. |
| [operator>= function](nf-wdm-operator_=.md) | TBD |
| [KeSaveFloatingPointState function](nf-wdm-kesavefloatingpointstate~r1.md) | The KeSaveFloatingPointState routine saves the nonvolatile floating-point context so the caller can carry out floating-point operations. |
| [READ_REGISTER_BUFFER_ULONG64 function](nf-wdm-read-register-buffer-ulong64.md) | TBD |
| [_byteswap_ulong function](nf-wdm--byteswap-ulong.md) | TBD |
| [_bittestandset64 function](nf-wdm--bittestandset64.md) | TBD |
| [InterlockedExchangeAddSizeTAcquire function](nf-wdm-interlockedexchangeaddsizetacquire.md) | TBD |
| [TmRenameTransactionManager function](nf-wdm-tmrenametransactionmanager.md) | TBD |
| [RtlUnicodeStringToInteger function](nf-wdm-rtlunicodestringtointeger.md) | The RtlUnicodeStringToInteger routine converts a Unicode string representation of a number to the equivalent integer value. |
| [IoFreeMapRegisters function](nf-wdm-iofreemapregisters.md) | TBD |
| [KeMemoryBarrier function](nf-wdm-kememorybarrier.md) | The KeMemoryBarrier routine creates a barrier at its position in the code&#8212;across which the compiler and the processor cannot move any operations. |
| [WRITE_REGISTER_UCHAR function](nf-wdm-write-register-uchar~r1.md) | The WRITE_REGISTER_UCHAR routine writes a byte to the specified address. |
| [_InterlockedAddLargeStatistic function](nf-wdm--interlockedaddlargestatistic.md) | TBD |
| [NtRollbackRegistryTransaction function](nf-wdm-ntrollbackregistrytransaction.md) | TBD |
| [KeQueryRuntimeThread function](nf-wdm-kequeryruntimethread.md) | The KeQueryRuntimeThread routine reports the accumulated kernel-mode and user-mode run time of a thread, in clock ticks. |
| [NT_FRE_ASSERT function](nf-wdm-nt-fre-assert.md) | TBD |
| [WRITE_REGISTER_NOFENCE_ULONG function](nf-wdm-write-register-nofence-ulong~r1.md) | TBD |
| [RtlCopyUnicodeString function](nf-wdm-rtlcopyunicodestring.md) | The RtlCopyUnicodeString routine copies a source string to a destination string. |
| [ReadTimeStampCounter function](nf-wdm-readtimestampcounter~r2.md) | TBD |
| [vKdPrintExWithPrefix function](nf-wdm-vkdprintexwithprefix.md) | TBD |
| [RtlClearAllBits function](nf-wdm-rtlclearallbits.md) | The RtlClearAllBits routine sets all bits in a given bitmap variable to zero. |
| [ExDeleteLookasideListEx function](nf-wdm-exdeletelookasidelistex.md) | The ExDeleteLookasideListEx routine deletes a lookaside list. |
| [InterlockedIncrement16 function](nf-wdm-interlockedincrement16.md) | TBD |
| [IoSizeofWorkItem function](nf-wdm-iosizeofworkitem.md) | The IoSizeofWorkItem routine returns the size, in bytes, of an IO_WORKITEM structure. |
| [InterlockedPushEntrySList function](nf-wdm-interlockedpushentryslist~r1.md) | TBD |
| [ReadNoFence8 function](nf-wdm-readnofence8.md) | TBD |
| [RtlCompareUnicodeString function](nf-wdm-rtlcompareunicodestring.md) | The RtlCompareUnicodeString routine compares two Unicode strings. |
| [ASSERT function](nf-wdm-assert.md) | TBD |
| [__readfsbyte function](nf-wdm---readfsbyte.md) | TBD |
| [RtlNumberOfSetBitsUlongPtr function](nf-wdm-rtlnumberofsetbitsulongptr.md) | The RtlNumberOfSetBitsUlongPtr routine returns the number of bits in the specified ULONG_PTR integer value that are set to one. |
| [IMAGE_POLICY_ANSI_STRING function](nf-wdm-image-policy-ansi-string.md) | TBD |
| [MmUnmapReservedMapping function](nf-wdm-mmunmapreservedmapping.md) | The MmUnmapReservedMapping routine unmaps a memory buffer that was mapped by the MmMapLockedPagesWithReservedMapping routine. |
| [ExGetPreviousMode function](nf-wdm-exgetpreviousmode.md) | The ExGetPreviousMode routine returns the previous processor mode for the current thread. |
| [RtlCheckBit function](nf-wdm-rtlcheckbit.md) | The RtlCheckBit routine determines whether a particular bit in a given bitmap variable is clear or set. |
| [KeSetTargetProcessorDpc function](nf-wdm-kesettargetprocessordpc.md) | The KeSetTargetProcessorDpc routine specifies the processor that a DPC routine will be run on. |
| [KeSetImportanceDpc function](nf-wdm-kesetimportancedpc.md) | The KeSetImportanceDpc routine specifies how soon the DPC routine is run. |
| [DbgSetDebugFilterState function](nf-wdm-dbgsetdebugfilterstate.md) | TBD |
| [SeEtwWriteKMCveEvent function](nf-wdm-seetwwritekmcveevent.md) | The SeEtwWriteKMCveEvent function is a tracing function for publishing events when an attempted security vulnerability exploit is detected in your kernel-mode drivers. |
| [__incgsword function](nf-wdm---incgsword.md) | TBD |
| [ClfsMgmtQueryPolicy function](nf-wdm-clfsmgmtquerypolicy.md) | The ClfsMgmtQueryPolicy routine retrieves a specific CLFS_MGMT_POLICY structure for a log. |
| [RtlLargeIntegerGreaterThanZero function](nf-wdm-rtllargeintegergreaterthanzero.md) | TBD |
| [READ_PORT_BUFFER_ULONG function](nf-wdm-read-port-buffer-ulong.md) | The READ_PORT_BUFFER_ULONG routine reads a number of ULONG values from the specified port address into a buffer. |
| [ExWaitForRundownProtectionReleaseCacheAware function](nf-wdm-exwaitforrundownprotectionreleasecacheaware.md) | TBD |
| [ExFreeToLookasideListEx function](nf-wdm-exfreetolookasidelistex.md) | The ExFreeToLookasideListEx routine inserts an entry into a lookaside list, or, if the list is full, frees the allocated storage for the entry. |
| [ExInitializeDeleteTimerParameters function](nf-wdm-exinitializedeletetimerparameters.md) | The ExInitializeDeleteTimerParameters routine initializes an EXT_DELETE_PARAMETERS structure. |
| [ZwCreateKey function](nf-wdm-zwcreatekey.md) | The ZwCreateKey routine creates a new registry key or opens an existing one. |
| [__outdword function](nf-wdm---outdword.md) | TBD |
| [__addgsqword function](nf-wdm---addgsqword.md) | TBD |
| [__isb function](nf-wdm---isb.md) | TBD |
| [IoGetNextIrpStackLocation function](nf-wdm-iogetnextirpstacklocation.md) | The IoGetNextIrpStackLocation routine gives a higher level driver access to the next-lower driver's I/O stack location in an IRP so the caller can set it up for the lower driver. |
| [InterlockedAnd function](nf-wdm-interlockedand~r1.md) | The InterlockedAnd macro atomically computes a bitwise AND operation. |
| [ObReferenceObjectByHandleWithTag function](nf-wdm-obreferenceobjectbyhandlewithtag.md) | The ObReferenceObjectByHandleWithTag routine increments the reference count of the object that is identified by the specified handle, and writes a four-byte tag value to the object to support object reference tracing. |
| [InterlockedExchangeAdd function](nf-wdm-interlockedexchangeadd~r1.md) | The InterlockedExchangeAdd routine adds a value to a given integer as an atomic operation and returns the original value of the given integer. |
| [IoCreateFile function](nf-wdm-iocreatefile.md) | The IoCreateFile routine either causes a new file or directory to be created, or it opens an existing file, device, directory, or volume, giving the caller a handle for the file object. |
| [RtlCmEncodeMemIoResource function](nf-wdm-rtlcmencodememioresource.md) | The RtlCmEncodeMemIoResource routine updates a CM_PARTIAL_RESOURCE_DESCRIPTOR structure to describe a range of memory or I/O port addresses. |
| [ReadAcquire8 function](nf-wdm-readacquire8.md) | TBD |
| [VslDeleteSecureSection function](nf-wdm-vsldeletesecuresection.md) | TBD |
| [KeRegisterNmiCallback function](nf-wdm-keregisternmicallback.md) | The KeRegisterNmiCallback routine registers a routine to be called whenever a nonmaskable interrupt (NMI) occurs. |
| [__writefsbyte function](nf-wdm---writefsbyte.md) | TBD |
| [KeDeregisterBugCheckReasonCallback function](nf-wdm-kederegisterbugcheckreasoncallback.md) | The KeDeregisterBugCheckReasonCallback routine removes a callback routine that was registered by KeRegisterBugCheckReasonCallback. |
| [PoDeleteThermalRequest function](nf-wdm-podeletethermalrequest.md) | TBD |
| [__readfsdword function](nf-wdm---readfsdword.md) | TBD |
| [ZwOpenKeyTransacted function](nf-wdm-zwopenkeytransacted.md) | The ZwOpenKeyTransacted routine opens an existing registry key and associates the key with a transaction. |
| [ClfsLsnIncrement function](nf-wdm-clfslsnincrement.md) | TBD |
| [RemoveEntryList function](nf-wdm-removeentrylist~r1.md) | The RemoveEntryList routine removes an entry from a doubly linked list of LIST_ENTRY structures. |
| [SECONDBYTE function](nf-wdm-secondbyte.md) | TBD |
| [_bittestandreset function](nf-wdm--bittestandreset.md) | TBD |
| [RTL_SOFT_VERIFYMSG function](nf-wdm-rtl-soft-verifymsg.md) | TBD |
| [__indword function](nf-wdm---indword.md) | TBD |
| [ZwReadOnlyEnlistment function](nf-wdm-zwreadonlyenlistment.md) | The ZwReadOnlyEnlistment routine sets a specified enlistment to be read-only. |
| [__outword function](nf-wdm---outword.md) | TBD |
| [MmAllocateContiguousNodeMemory function](nf-wdm-mmallocatecontiguousnodememory.md) | The MmAllocateContiguousNodeMemory routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space. |
| [ASSERTMSG function](nf-wdm-assertmsg.md) | ASSERTMSG tests an expression. If the expression is false, it breaks into the kernel debugger and sends it the specified message. |
| [ExAcquireSharedStarveExclusive function](nf-wdm-exacquiresharedstarveexclusive.md) | The ExAcquireSharedStarveExclusive routine acquires a given resource for shared access without waiting for any pending attempts to acquire exclusive access to the same resource. |
| [WriteUShortRelease function](nf-wdm-writeushortrelease.md) | TBD |
| [IoCallDriverStackSafeDefault function](nf-wdm-iocalldriverstacksafedefault.md) | TBD |
| [DbgPrintReturnControlC function](nf-wdm-dbgprintreturncontrolc.md) | TBD |
| [WRITE_REGISTER_UCHAR function](nf-wdm-write-register-uchar~r3.md) | The WRITE_REGISTER_UCHAR routine writes a byte to the specified address. |
| [MmInitializeMdl function](nf-wdm-mminitializemdl.md) | TBD |
| [RtlInitEmptyAnsiString function](nf-wdm-rtlinitemptyansistring.md) | TBD |
| [ExReleaseResource function](nf-wdm-exreleaseresource.md) | TBD |
| [IoSetNextIrpStackLocation function](nf-wdm-iosetnextirpstacklocation.md) | The IoSetNextIrpStackLocation routine sets the IRP stack location in a driver-allocated IRP to that of the caller. |
| [RtlUshortByteSwap function](nf-wdm-rtlushortbyteswap~r1.md) | The RtlUshortByteSwap routine reverses the ordering of the two bytes in a 16-bit unsigned integer value. |
| [RtlStoreUlongPtr function](nf-wdm-rtlstoreulongptr.md) | TBD |
| [IoReportInterruptInactive function](nf-wdm-ioreportinterruptinactive.md) | The IoReportInterruptInactive routine informs the operating system that a registered interrupt service routine (ISR) is inactive and is not expecting interrupt requests. |
| [ReadNoFence8 function](nf-wdm-readnofence8~r1.md) | TBD |
| [ExAcquireRundownProtection function](nf-wdm-exacquirerundownprotection.md) | The ExAcquireRundownProtection routine tries to acquire run-down protection on a shared object so the caller can safely access the object. |
| [MmUnmapLockedPages function](nf-wdm-mmunmaplockedpages.md) | The MmUnmapLockedPages routine releases a mapping that was set up by a preceding call to the MmMapLockedPages or MmMapLockedPagesSpecifyCache routine. |
| [TmReadOnlyEnlistment function](nf-wdm-tmreadonlyenlistment.md) | The TmReadOnlyEnlistment routine sets a specified enlistment to be read-only. |
| [KfRaiseIrql function](nf-wdm-kfraiseirql.md) | TBD |
| [IoCreateSynchronizationEvent function](nf-wdm-iocreatesynchronizationevent.md) | The IoCreateSynchronizationEvent routine creates or opens a named synchronization event for use in serialization of access to hardware between two otherwise unrelated drivers. |
| [vKdPrintEx function](nf-wdm-vkdprintex.md) | TBD |
| [SeUnlockSubjectContext function](nf-wdm-seunlocksubjectcontext.md) | TBD |
| [IoSetIoPriorityHint function](nf-wdm-iosetiopriorityhint.md) | The IoSetIoPriorityHint routine sets the priority hint value for an IRP. |
| [ClfsReadPreviousRestartArea function](nf-wdm-clfsreadpreviousrestartarea.md) | The ClfsReadPreviousRestartArea routine reads the previous restart record relative to the current record in a read context. |
| [__dmb function](nf-wdm---dmb.md) | TBD |
| [ObReferenceObjectByHandle function](nf-wdm-obreferenceobjectbyhandle.md) | The ObReferenceObjectByHandle routine provides access validation on the object handle, and, if access can be granted, returns the corresponding pointer to the object's body. |
| [ClfsLsnEqual function](nf-wdm-clfslsnequal.md) | The ClfsLsnEqual routine determines whether two LSNs from the same stream are equal. |
| [IoSizeOfIrp function](nf-wdm-iosizeofirp.md) | The IoSizeOfIrp routine determines the size in bytes for an IRP, given the number of stack locations in the IRP. |
| [ExReInitializeRundownProtectionCacheAware function](nf-wdm-exreinitializerundownprotectioncacheaware.md) | TBD |
| [ClfsRemoveLogContainerSet function](nf-wdm-clfsremovelogcontainerset.md) | The ClfsRemoveLogContainerSet routine atomically removes a set of containers from a CLFS log. |
| [IMAGE_POLICY_UINT64 function](nf-wdm-image-policy-uint64.md) | TBD |
| [SeDeassignSecurity function](nf-wdm-sedeassignsecurity.md) | The SeDeassignSecurity routine deallocates the memory associated with a security descriptor that was assigned using SeAssignSecurity. |
| [WRITE_REGISTER_USHORT function](nf-wdm-write-register-ushort.md) | The WRITE_REGISTER_USHORT routine writes a USHORT value to the specified address. |
| [IoReuseIrp function](nf-wdm-ioreuseirp.md) | The IoReuseIrp routine reinitializes an IRP so that it can be reused. |
| [ZwSetInformationEnlistment function](nf-wdm-zwsetinformationenlistment.md) | The ZwSetInformationEnlistment routine sets information for a specified enlistment object. |
| [REGISTER_FENCE function](nf-wdm-register-fence.md) | TBD |
| [RtlpCheckListEntry function](nf-wdm-rtlpchecklistentry.md) | TBD |
| [RtlZeroMemory function](nf-wdm-rtlzeromemory.md) | The RtlZeroMemory routine fills a block of memory with zeros, given a pointer to the block and the length, in bytes, to be filled. |
| [WRITE_REGISTER_UCHAR function](nf-wdm-write-register-uchar.md) | The WRITE_REGISTER_UCHAR routine writes a byte to the specified address. |
| [WritePointerNoFence function](nf-wdm-writepointernofence~r1.md) | TBD |
| [WriteUCharRelease function](nf-wdm-writeucharrelease.md) | TBD |
| [KeRegisterBoundCallback function](nf-wdm-keregisterboundcallback.md) | The KeRegisterBoundCallback routine registers a routine to be called whenever a user-mode bound exception occurs. |
| [IoRemoveShareAccess function](nf-wdm-ioremoveshareaccess.md) | The IoRemoveShareAccess routine removes the access and share-access information for a given open instance of a file object. |
| [__emit function](nf-wdm---emit.md) | TBD |
| [RtlLargeIntegerLessThan function](nf-wdm-rtllargeintegerlessthan.md) | TBD |
| [WritePointerRelease function](nf-wdm-writepointerrelease~r1.md) | TBD |
| [KeIpiGenericCall function](nf-wdm-keipigenericcall.md) | The KeIpiGenericCall routine causes the specified routine to run on all processors simultaneously. |
| [RtlFindSetBitsAndClear function](nf-wdm-rtlfindsetbitsandclear.md) | The RtlFindSetBitsAndClear routine searches for a range of set bits of a requested size within a bitmap and clears all bits in the range when it has been located. |
| [PCI_CONFIGURATION_TYPE function](nf-wdm-pci-configuration-type.md) | TBD |
| [IoGetDeviceObjectPointer function](nf-wdm-iogetdeviceobjectpointer.md) | The IoGetDeviceObjectPointer routine returns a pointer to the top object in the named device object's stack and a pointer to the corresponding file object, if the requested access to the objects can be granted. |
| [READ_PORT_BUFFER_UCHAR function](nf-wdm-read-port-buffer-uchar~r2.md) | The READ_PORT_BUFFER_UCHAR routine reads a number of bytes from the specified port address into a buffer. |
| [READ_REGISTER_NOFENCE_USHORT function](nf-wdm-read-register-nofence-ushort~r1.md) | TBD |
| [ZwRollbackEnlistment function](nf-wdm-zwrollbackenlistment.md) | The ZwRollbackEnlistment routine rolls back the transaction that is associated with a specified enlistment. |
| [WriteRaw16 function](nf-wdm-writeraw16.md) | TBD |
| [ExAcquireSharedWaitForExclusive function](nf-wdm-exacquiresharedwaitforexclusive.md) | The ExAcquireSharedWaitForExclusive routine acquires the given resource for shared access if shared access can be granted and there are no exclusive waiters. |
| [EtwSetInformation function](nf-wdm-etwsetinformation.md) | TBD |
| [ZwOpenFile function](nf-wdm-zwopenfile.md) | The ZwOpenFile routine opens an existing file, directory, device, or volume. |
| [READ_PORT_BUFFER_ULONG function](nf-wdm-read-port-buffer-ulong~r3.md) | The READ_PORT_BUFFER_ULONG routine reads a number of ULONG values from the specified port address into a buffer. |
| [ZwQuerySymbolicLinkObject function](nf-wdm-zwquerysymboliclinkobject.md) | The ZwQuerySymbolicLinkObject routine returns a Unicode string that contains the target of a symbolic link. |
| [ExFreeToPagedLookasideList function](nf-wdm-exfreetopagedlookasidelist~r1.md) | The ExFreeToPagedLookasideList routine returns a pageable entry to the given lookaside list or to paged pool. |
| [InsertTailList function](nf-wdm-inserttaillist~r1.md) | The InsertTailList routine inserts an entry at the tail of a doubly linked list of LIST_ENTRY structures. |
| [ObDereferenceObjectDeferDelete function](nf-wdm-obdereferenceobjectdeferdelete.md) | The ObDereferenceObjectDeferDelete routine decrements the reference count for the given object, checks for object retention, and avoids deadlocks. |
| [RtlSetBit function](nf-wdm-rtlsetbit.md) | The RtlSetBit routine sets the specified bit in a bitmap to one. |
| [InterlockedExchangeAdd8 function](nf-wdm-interlockedexchangeadd8~r1.md) | TBD |
| [RTL_SOFT_ASSERT function](nf-wdm-rtl-soft-assert.md) | TBD |
| [ExInitializePagedLookasideList function](nf-wdm-exinitializepagedlookasidelist.md) | The ExInitializePagedLookasideList routine initializes a lookaside list for pageable entries of the specified size. |
| [PoFxRegisterCrashdumpDevice function](nf-wdm-pofxregistercrashdumpdevice.md) | TBD |
| [InterlockedAnd8 function](nf-wdm-interlockedand8.md) | TBD |
| [NtCommitComplete function](nf-wdm-ntcommitcomplete.md) | TBD |
| [_InlineInterlockedIncrement64 function](nf-wdm--inlineinterlockedincrement64.md) | TBD |
| [ALIGN_UP_BY function](nf-wdm-align-up-by.md) | TBD |
| [IoUnregisterPlugPlayNotificationEx function](nf-wdm-iounregisterplugplaynotificationex.md) | The IoUnregisterPlugPlayNotificationEx routine cancels the registration of a driver's callback routine for notifications of Plug and Play (PnP) events. |
| [READ_PORT_USHORT function](nf-wdm-read-port-ushort~r3.md) | The READ_PORT_USHORT routine reads a USHORT value from the specified port address. |
| [KeLowerIrql function](nf-wdm-kelowerirql~r1.md) | The KeLowerIrql routine restores the IRQL on the current processor to its original value. |
| [IMAGE_POLICY_INT8 function](nf-wdm-image-policy-int8.md) | TBD |
| [ADDRESS_AND_SIZE_TO_SPAN_PAGES function](nf-wdm-address-and-size-to-span-pages.md) | TBD |
| [WRITE_REGISTER_BUFFER_USHORT function](nf-wdm-write-register-buffer-ushort.md) | The WRITE_REGISTER_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified register. |
| [READ_PORT_USHORT function](nf-wdm-read-port-ushort~r2.md) | The READ_PORT_USHORT routine reads a USHORT value from the specified port address. |
| [TmRequestOutcomeEnlistment function](nf-wdm-tmrequestoutcomeenlistment.md) | The TmRequestOutcomeEnlistment routine asks KTM to try to provide an immediate outcome (commit or rollback) for the transaction that is associated with a specified enlistment. |
| [ExTryConvertSharedSpinLockExclusive function](nf-wdm-extryconvertsharedspinlockexclusive.md) | The ExTryConvertSharedSpinLockExclusive routine attempts to convert the access state of a spin lock from acquired for shared access to exclusive access. |
| [SeRegisterImageVerificationCallback function](nf-wdm-seregisterimageverificationcallback.md) | TBD |
| [_bittestandset function](nf-wdm--bittestandset~r1.md) | TBD |
| [ClfsCloseAndResetLogFile function](nf-wdm-clfscloseandresetlogfile.md) | The ClfsCloseAndResetLogFile routine releases all references to a specified log file object and marks its associated stream for reset. |
| [READ_REGISTER_NOFENCE_BUFFER_ULONG64 function](nf-wdm-read-register-nofence-buffer-ulong64.md) | TBD |
| [IMAGE_POLICY_UINT8 function](nf-wdm-image-policy-uint8.md) | TBD |
| [IoSizeOfIrpEx function](nf-wdm-iosizeofirpex.md) | TBD |
| [MmSizeOfMdl function](nf-wdm-mmsizeofmdl.md) | The MmSizeOfMdl routine returns the number of bytes to allocate for an MDL describing a given address range. |
| [QueryDepthSList function](nf-wdm-querydepthslist.md) | TBD |
| [IoSetDeviceInterfaceState function](nf-wdm-iosetdeviceinterfacestate.md) | The IoSetDeviceInterfaceState routine enables or disables an instance of a previously registered device interface class. |
| [RtlUlonglongByteSwap function](nf-wdm-rtlulonglongbyteswap.md) | The RtlUlonglongByteSwap routine reverses the ordering of the eight bytes in a 64-bit unsigned integer value. |
| [WriteNoFence8 function](nf-wdm-writenofence8~r1.md) | TBD |
| [WriteNoFence8 function](nf-wdm-writenofence8~r2.md) | TBD |
| [WriteRelease16 function](nf-wdm-writerelease16~r1.md) | TBD |
| [RtlValidRelativeSecurityDescriptor function](nf-wdm-rtlvalidrelativesecuritydescriptor.md) | The RtlValidRelativeSecurityDescriptor routine checks the validity of a self-relative security descriptor. |
| [WriteRelease8 function](nf-wdm-writerelease8~r2.md) | TBD |
| [ClfsMgmtDeregisterManagedClient function](nf-wdm-clfsmgmtderegistermanagedclient.md) | The ClfsMgmtDeregisterManagedClient routine removes the connection between a client and a log, so that the client no longer manages the log. |
| [READ_REGISTER_NOFENCE_UCHAR function](nf-wdm-read-register-nofence-uchar~r1.md) | TBD |
| [NtQueryInformationTransactionManager function](nf-wdm-ntqueryinformationtransactionmanager.md) | TBD |
| [ExConvertExclusiveToSharedLite function](nf-wdm-exconvertexclusivetosharedlite.md) | The ExConvertExclusiveToSharedLite routine converts a given resource from acquired for exclusive access to acquired for shared access. |
| [RtlInitEmptyUnicodeString function](nf-wdm-rtlinitemptyunicodestring.md) | TBD |
| [KeDeregisterNmiCallback function](nf-wdm-kederegisternmicallback.md) | The KeDeregisterNmiCallback routine deregisters a nonmaskable interrupt (NMI) callback registered by KeRegisterNmiCallback. |
| [RTL_SOFT_ASSERTMSG function](nf-wdm-rtl-soft-assertmsg.md) | TBD |
| [KeSetTargetProcessorDpcEx function](nf-wdm-kesettargetprocessordpcex.md) | The KeSetTargetProcessorDpcEx routine specifies the processor that a DPC routine will run on. |
| [InterlockedIncrementSizeT function](nf-wdm-interlockedincrementsizet.md) | TBD |
| [IoCleanupIrp function](nf-wdm-iocleanupirp.md) | TBD |
| [ClfsSetEndOfLog function](nf-wdm-clfssetendoflog.md) | The ClfsSetEndOfLog routine truncates a CLFS stream. |
| [InterlockedExchangeAddSizeT function](nf-wdm-interlockedexchangeaddsizet.md) | TBD |
| [KeRaiseIrql function](nf-wdm-keraiseirql.md) | The KeRaiseIrql routine raises the hardware priority to the specified IRQL value, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [PcwRegister function](nf-wdm-pcwregister.md) | The PcwRegister function registers the caller as a provider of the specified counter set. |
| [EtwUnregister function](nf-wdm-etwunregister.md) | The EtwUnregister function unregisters the event provider and must be called before the provider exits. |
| [KeLowerIrql function](nf-wdm-kelowerirql.md) | The KeLowerIrql routine restores the IRQL on the current processor to its original value. |
| [_BitScanReverse64 function](nf-wdm--bitscanreverse64.md) | TBD |
| [KeQueryNodeMaximumProcessorCount function](nf-wdm-kequerynodemaximumprocessorcount.md) | The KeQueryNodeMaximumProcessorCount routine returns the maximum number of logical processors that a specified node in a non-uniform memory access (NUMA) multiprocessor system can contain. |
| [_mm_clflush function](nf-wdm--mm-clflush.md) | TBD |
| [IoIsErrorUserInduced function](nf-wdm-ioiserroruserinduced.md) | The IoIsErrorUserInduced routine determines whether an I/O error encountered while processing a request to a removable-media device was caused by the user. |
| [ExQueryDepthSList function](nf-wdm-exquerydepthslist~r2.md) | The ExQueryDepthSList routine returns the number of entries currently in a given sequenced singly linked list. |
| [SeAccessCheck function](nf-wdm-seaccesscheck.md) | The SeAccessCheck routine determines whether the requested access rights can be granted to an object protected by a security descriptor and an object owner. |
| [IoDeleteDevice function](nf-wdm-iodeletedevice.md) | The IoDeleteDevice routine removes a device object from the system, for example, when the underlying device is removed from the system. |
| [RTL_VERIFY function](nf-wdm-rtl-verify.md) | TBD |
| [IoRegisterContainerNotification function](nf-wdm-ioregistercontainernotification.md) | The IoRegisterContainerNotification routine registers a kernel-mode driver to receive notifications about a specified class of events. |
| [WRITE_REGISTER_ULONG function](nf-wdm-write-register-ulong.md) | The WRITE_REGISTER_ULONG routine writes a ULONG value to the specified address. |
| [ExSizeOfRundownProtectionCacheAware function](nf-wdm-exsizeofrundownprotectioncacheaware.md) | TBD |
| [InterlockedPushEntrySList function](nf-wdm-interlockedpushentryslist.md) | TBD |
| [RtlIsNtDdiVersionAvailable function](nf-wdm-rtlisntddiversionavailable.md) | The RtlIsNtDdiVersionAvailable routine determines if a specified version of the Microsoft Windows device driver interface (DDI) is available. |
| [VslCreateSecureSection function](nf-wdm-vslcreatesecuresection.md) | TBD |
| [ClfsGetLogFileInformation function](nf-wdm-clfsgetlogfileinformation.md) | TBD |
| [KeSetEvent function](nf-wdm-kesetevent.md) | The KeSetEvent routine sets an event object to a signaled state if the event was not already signaled, and returns the previous state of the event object. |
| [InitializeSListHead function](nf-wdm-initializeslisthead~r1.md) | TBD |
| [NtRenameTransactionManager function](nf-wdm-ntrenametransactionmanager.md) | TBD |
| [RtlGenerateClass5Guid function](nf-wdm-rtlgenerateclass5guid.md) | TBD |
| [InterlockedExchange function](nf-wdm-interlockedexchange~r1.md) | The InterlockedExchange routine sets an integer variable to a given value as an atomic operation. |
| [InterlockedIncrement function](nf-wdm-interlockedincrement.md) | The InterlockedIncrement routine increments a caller-supplied variable as an atomic operation. |
| [SeCaptureSubjectContext function](nf-wdm-secapturesubjectcontext.md) | TBD |
| [IoGetDevicePropertyData function](nf-wdm-iogetdevicepropertydata.md) | The IoGetDevicePropertyData routine retrieves the current setting for a device property. |
| [VER_SET_CONDITION function](nf-wdm-ver-set-condition.md) | TBD |
| [_byteswap_ushort function](nf-wdm--byteswap-ushort.md) | TBD |
| [RtlAppendUnicodeToString function](nf-wdm-rtlappendunicodetostring.md) | The RtlAppendUnicodeToString routine concatenates the supplied Unicode string to a buffered Unicode string. |
| [ExAllocatePoolWithTag function](nf-wdm-exallocatepoolwithtag.md) | The ExAllocatePoolWithTag routine allocates pool memory of the specified type and returns a pointer to the allocated block. |
| [ZwRecoverTransactionManager function](nf-wdm-zwrecovertransactionmanager.md) | The ZwRecoverTransactionManager routine reconstructs the state of the transaction manager object (including all transactions, enlistments, and resource managers) from the recovery information that is in the log stream. |
| [operator++ function](nf-wdm-operator++.md) | TBD |
| [ZwEnumerateTransactionObject function](nf-wdm-zwenumeratetransactionobject.md) | The ZwEnumerateTransactionObject routine enumerates the KTM objects on a computer. |
| [KeAcquireSpinLock function](nf-wdm-keacquirespinlock.md) | The KeAcquireSpinLock routine acquires a spin lock so the caller can synchronize access to shared data in a multiprocessor-safe way by raising IRQL. |
| [ExFreeCacheAwareRundownProtection function](nf-wdm-exfreecacheawarerundownprotection.md) | TBD |
| [MmFreePagesFromMdl function](nf-wdm-mmfreepagesfrommdl.md) | The MmFreePagesFromMdl routine frees all the physical pages that are described by an MDL that was created by the MmAllocatePagesForMdl routine. |
| [MmIsDriverSuspectForVerifier function](nf-wdm-mmisdriversuspectforverifier.md) | TBD |
| [YieldProcessor function](nf-wdm-yieldprocessor~r2.md) | TBD |
| [ExpInterlockedPopEntrySList function](nf-wdm-expinterlockedpopentryslist.md) | TBD |
| [ReadTimeStampCounter function](nf-wdm-readtimestampcounter~r1.md) | TBD |
| [DbgSetDebugPrintCallback function](nf-wdm-dbgsetdebugprintcallback.md) | TBD |
| [READ_PORT_BUFFER_USHORT function](nf-wdm-read-port-buffer-ushort.md) | The READ_PORT_BUFFER_USHORT routine reads a number of USHORT values from the specified port address into a buffer. |
| [WRITE_REGISTER_BUFFER_ULONG64 function](nf-wdm-write-register-buffer-ulong64~r1.md) | TBD |
| [READ_REGISTER_ULONG64 function](nf-wdm-read-register-ulong64~r1.md) | TBD |
| [RemoveHeadList function](nf-wdm-removeheadlist~r1.md) | The RemoveHeadList routine removes an entry from the beginning of a doubly linked list of LIST_ENTRY structures. |
| [InitializeSListHead function](nf-wdm-initializeslisthead.md) | TBD |
| [__movsq function](nf-wdm---movsq.md) | TBD |
| [InterlockedAdd function](nf-wdm-interlockedadd.md) | TBD |
| [InterlockedCompareExchange128 function](nf-wdm-interlockedcompareexchange128.md) | TBD |
| [KeQueryPerformanceCounter function](nf-wdm-kequeryperformancecounter.md) | The KeQueryPerformanceCounter routine retrieves the current value and frequency of the performance counter.Use KeQueryPerformanceCounter to acquire high resolution (&lt;1us) time stamps for time interval measurements. |
| [MmProbeAndLockPages function](nf-wdm-mmprobeandlockpages.md) | The MmProbeAndLockPages routine probes the specified virtual memory pages, makes them resident, and locks them in memory. |
| [CmUnRegisterCallback function](nf-wdm-cmunregistercallback.md) | The CmUnRegisterCallback routine unregisters a RegistryCallback routine that a CmRegisterCallback or CmRegisterCallbackEx routine previously registered. |
| [READ_REGISTER_BUFFER_ULONG function](nf-wdm-read-register-buffer-ulong~r1.md) | The READ_REGISTER_BUFFER_ULONG routine reads a number of ULONG values from the specified register address into a buffer. |
| [WRITE_REGISTER_NOFENCE_UCHAR function](nf-wdm-write-register-nofence-uchar~r1.md) | TBD |
| [__PREfastPagedCodeLocked function](nf-wdm---prefastpagedcodelocked.md) | TBD |
| [RtlEqualMemory function](nf-wdm-rtlequalmemory.md) | The RtlEqualMemory routine compares two blocks of memory to determine whether the specified number of bytes are identical. |
| [PoClearPowerRequest function](nf-wdm-poclearpowerrequest.md) | The PoClearPowerRequest routine decrements the count for the specified power request type. |
| [PoUnregisterPowerSettingCallback function](nf-wdm-pounregisterpowersettingcallback.md) | The PoUnregisterPowerSettingCallback routine unregisters a power-setting callback routine that a driver previously registered by calling the PoRegisterPowerSettingCallback routine. |
| [KeLeaveGuardedRegion function](nf-wdm-keleaveguardedregion.md) | The KeLeaveGuardedRegion routine exits a guarded region entered by KeEnterGuardedRegion. |
| [ClfsLsnContainer function](nf-wdm-clfslsncontainer.md) | The ClfsLsnContainer routine returns the logical container identifier contained in a specified LSN. |
| [IS_UNWINDING function](nf-wdm-is-unwinding.md) | TBD |
| [__readgsword function](nf-wdm---readgsword.md) | TBD |
| [InterlockedExchange8 function](nf-wdm-interlockedexchange8~r1.md) | TBD |
| [InterlockedCompareExchange64 function](nf-wdm-interlockedcompareexchange64~r1.md) | TBD |
| [TmPrePrepareComplete function](nf-wdm-tmprepreparecomplete.md) | The TmPrePrepareComplete routine notifies KTM that the calling resource manager has finished preliminary preparation of a transaction's data. |
| [IoGetDeviceInterfaces function](nf-wdm-iogetdeviceinterfaces.md) | The IoGetDeviceInterfaces routine returns a list of device interface instances of a particular device interface class (such as all devices on the system that support a HID interface). |
| [KeQueryActiveGroupCount function](nf-wdm-kequeryactivegroupcount.md) | The KeQueryActiveGroupCount routine returns the number of active processor groups in a multiprocessor system. |
| [WriteRelease64 function](nf-wdm-writerelease64~r1.md) | TBD |
| [ZwOpenSection function](nf-wdm-zwopensection.md) | The ZwOpenSection routine opens a handle for an existing section object. |
| [InterlockedExchange function](nf-wdm-interlockedexchange.md) | The InterlockedExchange routine sets an integer variable to a given value as an atomic operation. |
| [ReadPointerRaw function](nf-wdm-readpointerraw.md) | TBD |
| [KeGetCurrentIrql function](nf-wdm-kegetcurrentirql.md) | The KeGetCurrentIrql routine returns the current IRQL. |
| [WRITE_REGISTER_BUFFER_USHORT function](nf-wdm-write-register-buffer-ushort~r3.md) | The WRITE_REGISTER_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified register. |
| [ZwOpenResourceManager function](nf-wdm-zwopenresourcemanager.md) | The ZwOpenResourceManager routine returns a handle to an existing resource manager object. |
| [_InlineInterlockedAnd64 function](nf-wdm--inlineinterlockedand64.md) | TBD |
| [ReadRaw function](nf-wdm-readraw.md) | TBD |
| [WRITE_PORT_ULONG function](nf-wdm-write-port-ulong~r3.md) | The WRITE_PORT_ULONG routine writes a ULONG value to the specified port address. |
| [KeAcquireSpinLockAtDpcLevel function](nf-wdm-keacquirespinlockatdpclevel.md) | The KeAcquireSpinLockAtDpcLevel routine acquires a spin lock when the caller is already running at IRQL &gt;= DISPATCH_LEVEL. |
| [ExSetTimerResolution function](nf-wdm-exsettimerresolution.md) | The ExSetTimerResolution routine modifies the frequency at which the system clock interrupts. Use this routine with extreme caution (see the following Remarks section). |
| [CmCallbackGetKeyObjectIDEx function](nf-wdm-cmcallbackgetkeyobjectidex.md) | The CmCallbackGetKeyObjectIDEx routine retrieves the unique identifier and object name that are associated with a specified registry key object. |
| [SeReportSecurityEvent function](nf-wdm-sereportsecurityevent.md) | TBD |
| [PoFxSetDeviceIdleTimeout function](nf-wdm-pofxsetdeviceidletimeout.md) | The PoFxSetDeviceIdleTimeout routine specifies the minimum time interval from when the last component of the device enters the idle condition to when the power management framework (PoFx) calls the driver's DevicePowerNotRequiredCallback routine. |
| [WRITE_REGISTER_BUFFER_UCHAR function](nf-wdm-write-register-buffer-uchar.md) | The WRITE_REGISTER_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified register. |
| [IoFreeWorkItem function](nf-wdm-iofreeworkitem.md) | The IoFreeWorkItem routine frees a work item that was allocated by IoAllocateWorkItem. |
| [_bittestandcomplement function](nf-wdm--bittestandcomplement~r1.md) | TBD |
| [KeRemoveDeviceQueue function](nf-wdm-keremovedevicequeue.md) | The KeRemoveDeviceQueue routine removes an entry from the head of a specified device queue. |
| [RtlStoreUshort function](nf-wdm-rtlstoreushort.md) | TBD |
| [PsCreateSystemThread function](nf-wdm-pscreatesystemthread.md) | The PsCreateSystemThread routine creates a system thread that executes in kernel mode and returns a handle for the thread. |
| [_InlineInterlockedExchangeAdd64 function](nf-wdm--inlineinterlockedexchangeadd64.md) | TBD |
| [READ_REGISTER_BUFFER_UCHAR function](nf-wdm-read-register-buffer-uchar~r3.md) | The READ_REGISTER_BUFFER_UCHAR routine reads a number of bytes from the specified register address into a buffer. |
| [__faststorefence function](nf-wdm---faststorefence.md) | TBD |
| [FatalListEntryError function](nf-wdm-fatallistentryerror.md) | TBD |
| [ExIsResourceAcquiredSharedLite function](nf-wdm-exisresourceacquiredsharedlite.md) | The ExIsResourceAcquiredSharedLite routine returns whether the current thread has access (either shared or exclusive) to a given resource. |
| [TmPropagationFailed function](nf-wdm-tmpropagationfailed.md) | TBD |
| [RtlInitString function](nf-wdm-rtlinitstring.md) | The RtlInitString routine initializes a counted string of 8-bit characters. |
| [ExIsSoftBoot function](nf-wdm-exissoftboot.md) | Determines whether the system has gone through a soft restart. |
| [MmProbeAndLockSelectedPages function](nf-wdm-mmprobeandlockselectedpages.md) | TBD |
| [ExInterlockedPushEntrySList function](nf-wdm-exinterlockedpushentryslist~r2.md) | The ExInterlockedPushEntrySList routine atomically inserts an entry at the beginning of a sequenced singly linked list. |
| [MmAllocateNodePagesForMdlEx function](nf-wdm-mmallocatenodepagesformdlex.md) | The MmAllocateNodePagesForMdlEx routine allocates nonpaged physical memory from an ideal node, and allocates an MDL structure to describe this memory. |
| [WRITE_PORT_UCHAR function](nf-wdm-write-port-uchar~r3.md) | The WRITE_PORT_UCHAR routine writes a byte to the specified port address. |
| [KeRaiseIrqlToDpcLevel function](nf-wdm-keraiseirqltodpclevel.md) | TBD |
| [__readpmc function](nf-wdm---readpmc.md) | TBD |
| [IoRegisterPlugPlayNotification function](nf-wdm-ioregisterplugplaynotification.md) | The IoRegisterPlugPlayNotification routine registers a Plug and Play (PnP) notification callback routine to be called when a PnP event of the specified category occurs. |
| [NT_ASSERT_ACTION function](nf-wdm-nt-assert-action.md) | TBD |
| [ExAllocatePool function](nf-wdm-exallocatepool.md) | The ExAllocatePool routine is obsolete, and is exported only for existing binaries. Use ExAllocatePoolWithTag instead.ExAllocatePool allocates pool memory of the specified type and returns a pointer to the allocated block. |
| [ReadPMC function](nf-wdm-readpmc~r1.md) | TBD |
| [KeInitializeThreadedDpc function](nf-wdm-keinitializethreadeddpc.md) | The KeInitializeThreadedDpc routine initializes a threaded DPC object, and registers a CustomThreadedDpc routine for that object. |
| [MmIsDriverVerifying function](nf-wdm-mmisdriververifying.md) | The MmIsDriverVerifying routine indicates whether the kernel-mode driver that is identified by the specified driver object is being verified or calls a driver that is being verified by Driver Verifier. |
| [IoReplacePartitionUnit function](nf-wdm-ioreplacepartitionunit.md) | TBD |
| [ClfsInitialize function](nf-wdm-clfsinitialize.md) | TBD |
| [UnsignedMultiplyExtract128 function](nf-wdm-unsignedmultiplyextract128.md) | TBD |
| [VerSetConditionMask function](nf-wdm-versetconditionmask.md) | TBD |
| [_mm_lfence function](nf-wdm--mm-lfence.md) | TBD |
| [IoStartPacket function](nf-wdm-iostartpacket.md) | The IoStartPacket routine calls the driver's StartIo routine with the given IRP or inserts the IRP into the device queue associated with the given device object if the device is already busy. |
| [ALIGN_UP function](nf-wdm-align-up.md) | TBD |
| [__inword function](nf-wdm---inword.md) | TBD |
| [KeRemoveByKeyDeviceQueueIfBusy function](nf-wdm-keremovebykeydevicequeueifbusy.md) | TBD |
| [RtlAssert function](nf-wdm-rtlassert.md) | TBD |
| [KeQueryInterruptTime function](nf-wdm-kequeryinterrupttime.md) | The KeQueryInterruptTime routine returns the current value of the system interrupt time count, with accuracy to within system clock tick. |
| [WRITE_REGISTER_NOFENCE_ULONG function](nf-wdm-write-register-nofence-ulong.md) | TBD |
| [InitializeListHead function](nf-wdm-initializelisthead.md) | The InitializeListHead routine initializes a LIST_ENTRY structure that represents the head of a doubly linked list. |
| [_InlineInterlockedAdd64 function](nf-wdm--inlineinterlockedadd64.md) | TBD |
| [WRITE_PORT_BUFFER_UCHAR function](nf-wdm-write-port-buffer-uchar~r2.md) | The WRITE_PORT_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified port. |
| [ExInitializeRundownProtection function](nf-wdm-exinitializerundownprotection.md) | The ExInitializeRundownProtection routine initializes run-down protection on a shared object. |
| [IMAGE_POLICY_INT32 function](nf-wdm-image-policy-int32.md) | TBD |
| [RtlOsDeploymentState function](nf-wdm-rtlosdeploymentstate.md) | TBD |
| [IoFlushAdapterBuffers function](nf-wdm-ioflushadapterbuffers.md) | TBD |
| [RtlInterlockedClearBitsDiscardReturn function](nf-wdm-rtlinterlockedclearbitsdiscardreturn.md) | TBD |
| [ZwSinglePhaseReject function](nf-wdm-zwsinglephasereject.md) | The ZwSinglePhaseReject routine informs KTM that the calling resource manager will not support single-phase commit operations for a specified enlistment. |
| [InsertTailList function](nf-wdm-inserttaillist.md) | The InsertTailList routine inserts an entry at the tail of a doubly linked list of LIST_ENTRY structures. |
| [ObfDereferenceObject function](nf-wdm-obfdereferenceobject.md) | TBD |
| [Multiply128 function](nf-wdm-multiply128.md) | TBD |
| [RtlAreBitsSet function](nf-wdm-rtlarebitsset.md) | The RtlAreBitsSet routine determines whether a given range of bits within a bitmap variable is set. |
| [KeTestSpinLock function](nf-wdm-ketestspinlock.md) | The KeTestSpinLock routine tests for the availability of a spin lock. |
| [ZwCommitTransaction function](nf-wdm-zwcommittransaction.md) | The ZwCommitTransaction routine initiates a commit operation for a specified transaction. |
| [MmGetSystemAddressForMdl function](nf-wdm-mmgetsystemaddressformdl.md) | The MmGetSystemAddressForMdl routine is obsolete for Windows 2000 and later versions of Windows, and for Windows Me. |
| [NtCreateEnlistment function](nf-wdm-ntcreateenlistment.md) | TBD |
| [RtlInitializeBitMap function](nf-wdm-rtlinitializebitmap.md) | The RtlInitializeBitMap routine initializes the header of a bitmap variable. |
| [SeAssignSecurity function](nf-wdm-seassignsecurity.md) | The SeAssignSecurity routine builds a self-relative security descriptor for a new object, given the security descriptor of its parent directory and any originally requested security for the object. |
| [__int2c function](nf-wdm---int2c.md) | TBD |
| [KeReadStateTimer function](nf-wdm-kereadstatetimer.md) | The KeReadStateTimer routine reads the current state of a timer object. |
| [RtlUnicodeStringToInt64 function](nf-wdm-rtlunicodestringtoint64.md) | TBD |
| [IoWMIQueryAllDataMultiple function](nf-wdm-iowmiqueryalldatamultiple.md) | The IoWMIQueryAllDataMultiple routine returns all WMI data blocks that implement one of a set of WMI classes. |
| [InterlockedCompareExchange function](nf-wdm-interlockedcompareexchange~r1.md) | The InterlockedCompareExchange routine performs an atomic operation that compares the input value pointed to by Destination with the value of Comparand. |
| [ClfsReserveAndAppendLogAligned function](nf-wdm-clfsreserveandappendlogaligned.md) | The ClfsReserveAndAppendLogAligned routine reserves space in a marshalling area or appends a record to a marshalling area or does both atomically. The record's data is aligned on specified boundaries. |
| [ReadNoFence16 function](nf-wdm-readnofence16.md) | TBD |
| [RtlIoEncodeMemIoResource function](nf-wdm-rtlioencodememioresource.md) | The RtlIoEncodeMemIoResource routine updates an IO_RESOURCE_DESCRIPTOR structure to describe a range of memory or I/O port addresses. |
| [RtlNumberOfClearBitsInRange function](nf-wdm-rtlnumberofclearbitsinrange.md) | TBD |
| [IoCreateSystemThread function](nf-wdm-iocreatesystemthread.md) | The IoCreateSystemThread routine creates a system thread that executes in kernel mode, and supplies a handle for the thread. |
| [ARM64_SYSINSTR function](nf-wdm-arm64-sysinstr.md) | TBD |
| [KdPrintEx function](nf-wdm-kdprintex.md) | The KdPrintEx macro sends a string to the kernel debugger if the conditions you specify are met.A call to KdPrintEx requires double parentheses. |
| [ZwQueryInformationTransactionManager function](nf-wdm-zwqueryinformationtransactionmanager.md) | The ZwQueryInformationTransactionManager routine retrieves information about a specified transaction manager object. |
| [PoFxReportDevicePoweredOn function](nf-wdm-pofxreportdevicepoweredon.md) | The PoFxReportDevicePoweredOn routine notifies the power management framework (PoFx) that the device completed the requested transition to the D0 (fully on) power state. |
| [READ_PORT_UCHAR function](nf-wdm-read-port-uchar~r1.md) | The READ_PORT_UCHAR routine reads a byte from the specified port address. |
| [IoUnregisterContainerNotification function](nf-wdm-iounregistercontainernotification.md) | The IoUnregisterContainerNotification routine cancels a container notification registration that was previously created by the IoRegisterContainerNotification routine. |
| [ZwRollbackTransaction function](nf-wdm-zwrollbacktransaction.md) | The ZwRollbackTransaction routine initiates a rollback operation for a specified transaction. |
| [ClfsReadLogRecord function](nf-wdm-clfsreadlogrecord.md) | The ClfsReadLogRecord routine reads a target record in a CLFS stream and returns a read context that the caller can use to read the records preceding or following it in the stream. |
| [METHOD_FROM_CTL_CODE function](nf-wdm-method-from-ctl-code.md) | TBD |
| [ZwSaveKeyEx function](nf-wdm-zwsavekeyex.md) | TBD |
| [__addgsbyte function](nf-wdm---addgsbyte.md) | TBD |
| [IoWMISetSingleInstance function](nf-wdm-iowmisetsingleinstance.md) | The IoWMISetSingleInstance routine sets the values for properties within the data block instance that matches the specified WMI class and instance name. |
| [PoCreatePowerRequest function](nf-wdm-pocreatepowerrequest.md) | The PoCreatePowerRequest routine creates a power request object. |
| [_mm_pause function](nf-wdm--mm-pause~r1.md) | TBD |
| [MmAreMdlPagesCached function](nf-wdm-mmaremdlpagescached.md) | TBD |
| [TmRollbackTransaction function](nf-wdm-tmrollbacktransaction.md) | The TmRollbackTransaction routine initiates a rollback operation for a specified transaction. |
| [TmReferenceEnlistmentKey function](nf-wdm-tmreferenceenlistmentkey.md) | The TmReferenceEnlistmentKey routine increments the reference count for the key of a specified enlistment object and retrieves the key. |
| [InterlockedAnd8 function](nf-wdm-interlockedand8~r1.md) | TBD |
| [RemoveEntryList function](nf-wdm-removeentrylist.md) | The RemoveEntryList routine removes an entry from a doubly linked list of LIST_ENTRY structures. |
| [RtlDowncaseUnicodeChar function](nf-wdm-rtldowncaseunicodechar.md) | The RtlDowncaseUnicodeChar routine converts the specified Unicode character to lowercase. |
| [_bittest function](nf-wdm--bittest.md) | TBD |
| [ExInterlockedFlushSList function](nf-wdm-exinterlockedflushslist~r1.md) | The ExInterlockedFlushSList routine atomically removes all entries from a sequenced singly linked list. |
| [RtlUlongByteSwap function](nf-wdm-rtlulongbyteswap.md) | The RtlUlongByteSwap routine reverses the ordering of the four bytes in a 32-bit unsigned integer value. |
| [ShiftRight128 function](nf-wdm-shiftright128.md) | TBD |
| [NtRollbackEnlistment function](nf-wdm-ntrollbackenlistment.md) | TBD |
| [WRITE_PORT_BUFFER_USHORT function](nf-wdm-write-port-buffer-ushort.md) | The WRITE_PORT_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified port address. |
| [__incfsbyte function](nf-wdm---incfsbyte.md) | TBD |
| [ExInitializeWorkItem function](nf-wdm-exinitializeworkitem.md) | ExInitializeWorkItem initializes a work-queue item with a caller-supplied context and callback routine to be queued for execution when a system worker thread is given control. |
| [WriteNoFence function](nf-wdm-writenofence.md) | TBD |
| [NtPropagationComplete function](nf-wdm-ntpropagationcomplete.md) | TBD |
| [KeQueryMaximumProcessorCount function](nf-wdm-kequerymaximumprocessorcount.md) | TBD |
| [PoStartDeviceBusy function](nf-wdm-postartdevicebusy.md) | The PoStartDeviceBusy routine marks the start of a period of time in which the device is busy. |
| [WRITE_PORT_BUFFER_USHORT function](nf-wdm-write-port-buffer-ushort~r3.md) | The WRITE_PORT_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified port address. |
| [MmAllocateContiguousMemorySpecifyCache function](nf-wdm-mmallocatecontiguousmemoryspecifycache.md) | TBD |
| [WRITE_PORT_BUFFER_ULONG function](nf-wdm-write-port-buffer-ulong.md) | The WRITE_PORT_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified port address. |
| [ASSERT_DEVICE_QUEUE function](nf-wdm-assert-device-queue.md) | TBD |
| [ARM64_SYSREG function](nf-wdm-arm64-sysreg.md) | TBD |
| [WritePointerNoFence function](nf-wdm-writepointernofence.md) | TBD |
| [IoRegisterLastChanceShutdownNotification function](nf-wdm-ioregisterlastchanceshutdownnotification.md) | The IoRegisterLastChanceShutdownNotification routine registers a driver to receive an IRP_MJ_SHUTDOWN IRP when the system is shut down, after all file systems have been flushed. |
| [PcwAddInstance function](nf-wdm-pcwaddinstance.md) | The PcwAddInstance function adds the specified instance of the counter set to the consumer buffer. |
| [KeRemoveEntryDeviceQueue function](nf-wdm-keremoveentrydevicequeue.md) | The KeRemoveEntryDeviceQueue routine returns whether the specified entry is in the device queue and removes it, if it was queued, from the device queue. |
| [NtPowerInformation function](nf-wdm-ntpowerinformation.md) | TBD |
| [ReadAcquire16 function](nf-wdm-readacquire16~r1.md) | TBD |
| [ObDereferenceObjectWithTag function](nf-wdm-obdereferenceobjectwithtag.md) | The ObDereferenceObjectWithTag routine decrements the reference count of the specified object, and writes a four-byte tag value to the object to support object reference tracing. |
| [_mm_getcsr function](nf-wdm--mm-getcsr.md) | TBD |
| [NtPrePrepareComplete function](nf-wdm-ntprepreparecomplete.md) | TBD |
| [ExFreeToPagedLookasideList function](nf-wdm-exfreetopagedlookasidelist.md) | The ExFreeToPagedLookasideList routine returns a pageable entry to the given lookaside list or to paged pool. |
| [RtlRetrieveUlong function](nf-wdm-rtlretrieveulong.md) | TBD |
| [RtlVerifyVersionInfo function](nf-wdm-rtlverifyversioninfo.md) | TBD |
| [BYTE_OFFSET function](nf-wdm-byte-offset.md) | TBD |
| [MmGetMdlVirtualAddress function](nf-wdm-mmgetmdlvirtualaddress.md) | TBD |
| [WriteRelease8 function](nf-wdm-writerelease8.md) | TBD |
| [ExDeleteResourceLite function](nf-wdm-exdeleteresourcelite.md) | The ExDeleteResourceLite routine deletes a given resource from the system's resource list. |
| [__addfsbyte function](nf-wdm---addfsbyte.md) | TBD |
| [ReadULongNoFence function](nf-wdm-readulongnofence.md) | TBD |
| [RtlNumberOfSetBitsInRange function](nf-wdm-rtlnumberofsetbitsinrange.md) | TBD |
| [BYTES_TO_PAGES function](nf-wdm-bytes-to-pages.md) | TBD |
| [IoIsWdmVersionAvailable function](nf-wdm-ioiswdmversionavailable.md) | The IoIsWdmVersionAvailable routine checks whether a given WDM version is supported by the operating system. |
| [NT_VERIFYMSG function](nf-wdm-nt-verifymsg.md) | TBD |
| [KeReleaseMutex function](nf-wdm-kereleasemutex.md) | The KeReleaseMutex routine releases a mutex object, and specifies whether the caller is to call one of the KeWaitXxx routines as soon as KeReleaseMutex returns control. |
| [__rdtsc function](nf-wdm---rdtsc.md) | TBD |
| [RtlExtendedMagicDivide function](nf-wdm-rtlextendedmagicdivide.md) | TBD |
| [WmiQueryTraceInformation function](nf-wdm-wmiquerytraceinformation.md) | The WmiQueryTraceInformation routine returns information about a WMI event trace. |
| [ObReferenceObjectSafeWithTag function](nf-wdm-obreferenceobjectsafewithtag.md) | TBD |
| [PoFxRegisterDevice function](nf-wdm-pofxregisterdevice.md) | The PoFxRegisterDevice routine registers a device with the power management framework (PoFx). |
| [ExFreeToNPagedLookasideList function](nf-wdm-exfreetonpagedlookasidelist.md) | The ExFreeToNPagedLookasideList routine returns a nonpaged entry to the given lookaside list or to nonpaged pool. |
| [CmSetCallbackObjectContext function](nf-wdm-cmsetcallbackobjectcontext.md) | The CmSetCallbackObjectContext routine associates specified context information with a specified registry object. |
| [_bittest64 function](nf-wdm--bittest64.md) | TBD |
| [SeGetWorldRights function](nf-wdm-segetworldrights.md) | TBD |
| [MmFreeContiguousMemory function](nf-wdm-mmfreecontiguousmemory.md) | TBD |
| [TmInitializeTransactionManager function](nf-wdm-tminitializetransactionmanager.md) | TBD |
| [ExAllocatePoolWithQuotaTag function](nf-wdm-exallocatepoolwithquotatag.md) | The ExAllocatePoolWithQuotaTag routine allocates pool memory, charging the quota against the current process. |
| [MultiplyExtract128 function](nf-wdm-multiplyextract128.md) | TBD |
| [READ_REGISTER_NOFENCE_UCHAR function](nf-wdm-read-register-nofence-uchar.md) | TBD |
| [MmResetDriverPaging function](nf-wdm-mmresetdriverpaging.md) | The MmResetDriverPaging routine resets the pageable status of a driver's sections to that specified when the driver was compiled. |
| [RtlLengthSecurityDescriptor function](nf-wdm-rtllengthsecuritydescriptor.md) | The RtlLengthSecurityDescriptor routine returns the size of a given security descriptor. |
| [PopEntryList function](nf-wdm-popentrylist.md) | The PopEntryList routine removes the first entry from a singly linked list of SINGLE_LIST_ENTRY structures. |
| [READ_REGISTER_NOFENCE_ULONG64 function](nf-wdm-read-register-nofence-ulong64.md) | TBD |
| [ExQueryDepthSList function](nf-wdm-exquerydepthslist~r1.md) | The ExQueryDepthSList routine returns the number of entries currently in a given sequenced singly linked list. |
| [HalGetDmaAlignment function](nf-wdm-halgetdmaalignment.md) | TBD |
| [ZwOpenKeyEx function](nf-wdm-zwopenkeyex.md) | The ZwOpenKeyEx routine opens an existing registry key. |
| [ExReleaseSpinLockExclusive function](nf-wdm-exreleasespinlockexclusive.md) | TBD |
| [WRITE_PORT_ULONG function](nf-wdm-write-port-ulong.md) | The WRITE_PORT_ULONG routine writes a ULONG value to the specified port address. |
| [WriteNoFence16 function](nf-wdm-writenofence16.md) | TBD |
| [IoGetIoPriorityHint function](nf-wdm-iogetiopriorityhint.md) | The IoGetIoPriorityHint routine gets the priority hint value from an IRP. |
| [RtlFindFirstRunClear function](nf-wdm-rtlfindfirstrunclear.md) | The RtlFindFirstRunClear routine searches for the initial contiguous range of clear bits within a given bitmap. |
| [__segmentlimit function](nf-wdm---segmentlimit.md) | TBD |
| [__readgsqword function](nf-wdm---readgsqword.md) | TBD |
| [ObReferenceObjectByPointerWithTag function](nf-wdm-obreferenceobjectbypointerwithtag.md) | The ObReferenceObjectByPointerWithTag routine increments the reference count of the specified object, and writes a four-byte tag value to the object to support object reference tracing. |
| [ExIsProcessorFeaturePresent function](nf-wdm-exisprocessorfeaturepresent.md) | The ExIsProcessorFeaturePresent routine queries for the existence of a specified processor feature. |
| [ClfsFlushBuffers function](nf-wdm-clfsflushbuffers.md) | The ClfsFlushBuffers routine forces all log I/O blocks in a specified marshalling area to stable storage. |
| [ClfsGetLastLsn function](nf-wdm-clfsgetlastlsn.md) | TBD |
| [PoFxUnregisterDevice function](nf-wdm-pofxunregisterdevice.md) | The PoFxUnregisterDevice routine removes the registration of a device from the power management framework (PoFx). |
| [ZwPrepareEnlistment function](nf-wdm-zwprepareenlistment.md) | The ZwPrepareEnlistment routine initiates the prepare operation for a specified enlistment's transaction. |
| [KeEnterCriticalRegion function](nf-wdm-keentercriticalregion.md) | The KeEnterCriticalRegion routine temporarily disables the execution of normal kernel APCs, but does not prevent special kernel APCs from running. |
| [ExDeleteTimer function](nf-wdm-exdeletetimer.md) | The ExDeleteTimer routine deletes a timer object that was previously allocated by the ExAllocateTimer routine. |
| [NtCommitTransaction function](nf-wdm-ntcommittransaction.md) | TBD |
| [READ_PORT_ULONG function](nf-wdm-read-port-ulong~r3.md) | The READ_PORT_ULONG routine reads a ULONG value from the specified port address. |
| [ExInterlockedPushEntryList function](nf-wdm-exinterlockedpushentrylist.md) | The ExInterlockedPushEntryList routine atomically inserts an entry at the beginning of a singly linked list of SINGLE_LIST_ENTRY structures. |
| [ExGetFirmwareEnvironmentVariable function](nf-wdm-exgetfirmwareenvironmentvariable.md) | The ExGetFirmwareEnvironmentVariable routine gets the value of the specified system firmware environment variable. |
| [MmFreePagesFromMdlEx function](nf-wdm-mmfreepagesfrommdlex.md) | TBD |
| [SeAssignSecurityEx function](nf-wdm-seassignsecurityex.md) | The SeAssignSecurityEx routine builds a self-relative security descriptor for a new object given the following optional parameters |
| [__cpuidex function](nf-wdm---cpuidex.md) | TBD |
| [IoAdjustPagingPathCount function](nf-wdm-ioadjustpagingpathcount.md) | The IoAdjustPagingPathCount routine increments or decrements a caller-supplied page-file counter as an atomic operation. |
| [KeReleaseSemaphore function](nf-wdm-kereleasesemaphore.md) | The KeReleaseSemaphore routine releases the specified semaphore object. |
| [IoReportTargetDeviceChangeAsynchronous function](nf-wdm-ioreporttargetdevicechangeasynchronous.md) | The IoReportTargetDeviceChangeAsynchronous routine notifies the PnP manager that a custom event has occurred on a device. |
| [READ_REGISTER_USHORT function](nf-wdm-read-register-ushort.md) | The READ_REGISTER_USHORT routine reads a USHORT value from the specified register address. |
| [RtlEnlargedIntegerMultiply function](nf-wdm-rtlenlargedintegermultiply.md) | TBD |
| [InterlockedDecrement64 function](nf-wdm-interlockeddecrement64.md) | TBD |
| [__invlpg function](nf-wdm---invlpg.md) | TBD |
| [KeInitializeTimer2SetParameters function](nf-wdm-keinitializetimer2setparameters.md) | TBD |
| [WriteULong64NoFence function](nf-wdm-writeulong64nofence.md) | TBD |
| [ZwCreateRegistryTransaction function](nf-wdm-zwcreateregistrytransaction.md) | TBD |
| [_InlineInterlockedAdd function](nf-wdm--inlineinterlockedadd.md) | TBD |
| [READ_REGISTER_USHORT function](nf-wdm-read-register-ushort~r1.md) | The READ_REGISTER_USHORT routine reads a USHORT value from the specified register address. |
| [ZwQueryInformationResourceManager function](nf-wdm-zwqueryinformationresourcemanager.md) | The ZwQueryInformationResourceManager routine retrieves information about a specified resource manager object. |
| [WRITE_REGISTER_ULONG64 function](nf-wdm-write-register-ulong64~r1.md) | TBD |
| [RtlIntegerToUnicodeString function](nf-wdm-rtlintegertounicodestring.md) | The RtlIntegerToUnicodeString routine converts an unsigned integer value to a null-terminated string of one or more Unicode characters in the specified base. |
| [ExAcquireSpinLockAtDpcLevel function](nf-wdm-exacquirespinlockatdpclevel.md) | TBD |
| [_mm_clflush function](nf-wdm--mm-clflush~r1.md) | TBD |
| [TmPrePrepareEnlistment function](nf-wdm-tmpreprepareenlistment.md) | The TmPrePrepareEnlistment routine initiates the pre-prepare operation for a specified enlistment's transaction. |
| [LSAP_SE_ADT_PARAMETER_ARRAY_TRUE_SIZE function](nf-wdm-lsap-se-adt-parameter-array-true-size.md) | TBD |
| [ZwCreateResourceManager function](nf-wdm-zwcreateresourcemanager.md) | The ZwCreateResourceManager routine creates a resource manager object. |
| [HalFreeCommonBuffer function](nf-wdm-halfreecommonbuffer.md) | TBD |
| [MmIsDriverVerifyingByAddress function](nf-wdm-mmisdriververifyingbyaddress.md) | The MmIsDriverVerifyingByAddress routine checks whether the kernel-mode driver that is identified by the specified image address is being verified or calls a driver that is being verified by Driver Verifier. |
| [ExVerifySuite function](nf-wdm-exverifysuite.md) | TBD |
| [IoGetDeviceProperty function](nf-wdm-iogetdeviceproperty.md) | The IoGetDeviceProperty routine retrieves information about a device such as configuration information and the name of its PDO. |
| [__int2c function](nf-wdm---int2c~r1.md) | TBD |
| [WriteNoFence64 function](nf-wdm-writenofence64~r2.md) | TBD |
| [RtlFreeUnicodeString function](nf-wdm-rtlfreeunicodestring.md) | The RtlFreeUnicodeString routine releases storage that was allocated by RtlAnsiStringToUnicodeString or RtlUpcaseUnicodeString. |
| [RtlFindLastBackwardRunClear function](nf-wdm-rtlfindlastbackwardrunclear.md) | The RtlFindLastBackwardRunClear routine searches a given bitmap for the preceding clear run of bits, starting from the specified index position. |
| [RtlLargeIntegerNotEqualToZero function](nf-wdm-rtllargeintegernotequaltozero.md) | TBD |
| [ReadULong64Raw function](nf-wdm-readulong64raw.md) | TBD |
| [ClfsReadRestartArea function](nf-wdm-clfsreadrestartarea.md) | The ClfsReadRestartArea routine reads the restart record that was most recently written to a specified CLFS stream. |
| [IoDeleteSymbolicLink function](nf-wdm-iodeletesymboliclink.md) | The IoDeleteSymbolicLink routine removes a symbolic link from the system. |
| [IoAllocateIrp function](nf-wdm-ioallocateirp.md) | The IoAllocateIrp routine allocates an IRP, given the number of I/O stack locations for each driver layered under the caller, and, optionally, for the caller. |
| [NtCommitEnlistment function](nf-wdm-ntcommitenlistment.md) | TBD |
| [MmSetPermanentCacheAttribute function](nf-wdm-mmsetpermanentcacheattribute.md) | TBD |
| [PoFxNotifySurprisePowerOn function](nf-wdm-pofxnotifysurprisepoweron.md) | The PoFxNotifySurprisePowerOn routine notifies the power management framework (PoFx) that a device was turned on as a side effect of supplying power to some other device. |
| [_interlockedbittestandreset function](nf-wdm--interlockedbittestandreset~r1.md) | TBD |
| [ExQueryDepthSList function](nf-wdm-exquerydepthslist.md) | The ExQueryDepthSList routine returns the number of entries currently in a given sequenced singly linked list. |
| [KeCancelTimer function](nf-wdm-kecanceltimer.md) | The KeCancelTimer routine dequeues a timer object before the timer interval, if any was set, expires. |
| [_BitScanForward function](nf-wdm--bitscanforward~r1.md) | TBD |
| [KeQueryMaximumGroupCount function](nf-wdm-kequerymaximumgroupcount.md) | The KeQueryMaximumGroupCount routine returns the maximum number of groups in a multiprocessor system. |
| [KeQueryActiveProcessorCount function](nf-wdm-kequeryactiveprocessorcount.md) | TBD |
| [AppendTailList function](nf-wdm-appendtaillist.md) | The AppendTailList routine appends a doubly linked list of LIST_ENTRY structures to the tail of another doubly linked list of LIST_ENTRY structures. |
| [MmMapLockedPagesWithReservedMapping function](nf-wdm-mmmaplockedpageswithreservedmapping.md) | The MmMapLockedPagesWithReservedMapping routine maps all or part of an address range that was previously reserved by the MmAllocateMappingAddress routine. |
| [KeConvertAuxiliaryCounterToPerformanceCounter function](nf-wdm-keconvertauxiliarycountertoperformancecounter.md) | The KeConvertAuxiliaryCounterToPerformanceCounter routine converts the specified auxiliary counter value into a performance counter value. |
| [EtwEventEnabled function](nf-wdm-etweventenabled.md) | The EtwEventEnabled function verifies whether an event is enabled. |
| [KeDeregisterProcessorChangeCallback function](nf-wdm-kederegisterprocessorchangecallback.md) | The KeDeregisterProcessorChangeCallback routine unregisters a callback function that was previously registered with the operating system by calling the KeRegisterProcessorChangeCallback routine. |
| [RtlExtendedLargeIntegerDivide function](nf-wdm-rtlextendedlargeintegerdivide~r1.md) | TBD |
| [IoWMIAllocateInstanceIds function](nf-wdm-iowmiallocateinstanceids.md) | The IoWMIAllocateInstanceIds routine allocates one or more instance IDs that are unique to the GUID. |
| [IoGetDeviceInterfacePropertyData function](nf-wdm-iogetdeviceinterfacepropertydata.md) | The IoGetDeviceInterfacePropertyData routine retrieves the current value of a device interface property. |
| [ProbeForRead function](nf-wdm-probeforread.md) | The ProbeForRead routine checks that a user-mode buffer actually resides in the user portion of the address space, and is correctly aligned. |
| [STATICGUIDOF function](nf-wdm-staticguidof.md) | TBD |
| [WRITE_REGISTER_BUFFER_UCHAR function](nf-wdm-write-register-buffer-uchar~r2.md) | The WRITE_REGISTER_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified register. |
| [ZwReadFile function](nf-wdm-zwreadfile.md) | The ZwReadFile routine reads data from an open file. |
| [NT_ASSERT_ASSUME function](nf-wdm-nt-assert-assume.md) | TBD |
| [RtlCopyBitMap function](nf-wdm-rtlcopybitmap.md) | TBD |
| [ZwQueryInformationByName function](nf-wdm-zwqueryinformationbyname.md) | TBD |
| [ExInterlockedPushEntrySList function](nf-wdm-exinterlockedpushentryslist~r1.md) | The ExInterlockedPushEntrySList routine atomically inserts an entry at the beginning of a sequenced singly linked list. |
| [ZwMakeTemporaryObject function](nf-wdm-zwmaketemporaryobject.md) | The ZwMakeTemporaryObject routine changes the attributes of an object to make it temporary. |
| [KzRaiseIrql function](nf-wdm-kzraiseirql.md) | TBD |
| [TmCommitTransaction function](nf-wdm-tmcommittransaction.md) | The TmCommitTransaction routine initiates a commit operation for a specified transaction. |
| [ReadUCharRaw function](nf-wdm-readucharraw.md) | TBD |
| [RtlUnicodeStringToAnsiSize function](nf-wdm-rtlunicodestringtoansisize.md) | The RtlUnicodeStringToAnsiSize routine returns the number of bytes required for a null-terminated ANSI string that is equivalent to a specified Unicode string. |
| [ExReleaseResourceForThreadLite function](nf-wdm-exreleaseresourceforthreadlite.md) | The ExReleaseResourceForThreadLite routine releases the input resource of the indicated thread. |
| [PAGE_ALIGN function](nf-wdm-page-align.md) | TBD |
| [__outbyte function](nf-wdm---outbyte.md) | TBD |
| [ReadBooleanNoFence function](nf-wdm-readbooleannofence.md) | TBD |
| [WRITE_PORT_UCHAR function](nf-wdm-write-port-uchar~r2.md) | The WRITE_PORT_UCHAR routine writes a byte to the specified port address. |
| [IoWMIDeviceObjectToProviderId function](nf-wdm-iowmideviceobjecttoproviderid.md) | The IoWMIDeviceObjectToProviderId routine translates the specified device object into the corresponding WMI Provider ID. |
| [__outdwordstring function](nf-wdm---outdwordstring.md) | TBD |
| [NtQueryInformationEnlistment function](nf-wdm-ntqueryinformationenlistment.md) | TBD |
| [RtlExtractBitMap function](nf-wdm-rtlextractbitmap.md) | TBD |
| [ZwFlushKey function](nf-wdm-zwflushkey.md) | The ZwFlushKey routine forces a registry key to be committed to disk. |
| [RtlCrc64 function](nf-wdm-rtlcrc64.md) | TBD |
| [ClfsTerminateReadLog function](nf-wdm-clfsterminatereadlog.md) | The ClfsTerminateReadLog routine invalidates a specified read context after freeing resources associated with the context. |
| [MmAllocatePartitionNodePagesForMdlEx function](nf-wdm-mmallocatepartitionnodepagesformdlex.md) | TBD |
| [ExIsResourceAcquiredExclusiveLite function](nf-wdm-exisresourceacquiredexclusivelite.md) | The ExIsResourceAcquiredExclusiveLite routine returns whether the current thread has exclusive access to a given resource. |
| [ClfsMgmtHandleLogFileFull function](nf-wdm-clfsmgmthandlelogfilefull.md) | The ClfsMgmtHandleLogFileFull routine attempts to make more space available in a log. It might make more space available by adding containers to the log, or it might ask clients to move their log tails. |
| [ExTryAcquireSpinLockSharedAtDpcLevel function](nf-wdm-extryacquirespinlocksharedatdpclevel.md) | TBD |
| [_interlockedbittestandreset64 function](nf-wdm--interlockedbittestandreset64.md) | TBD |
| [PAGED_ASSERT function](nf-wdm-paged-assert.md) | TBD |
| [CacheLineFlush function](nf-wdm-cachelineflush.md) | TBD |
| [RtlGUIDFromString function](nf-wdm-rtlguidfromstring.md) | The RtlGUIDFromString routine converts the given Unicode string to a GUID in binary format. |
| [RtlCreateRegistryKey function](nf-wdm-rtlcreateregistrykey.md) | The RtlCreateRegistryKey routine adds a key object in the registry along a given relative path. |
| [RtlHashUnicodeString function](nf-wdm-rtlhashunicodestring.md) | The RtlHashUnicodeString routine creates a hash value from a given Unicode string and hash algorithm. |
| [NtRollbackComplete function](nf-wdm-ntrollbackcomplete.md) | TBD |
| [__readeflags function](nf-wdm---readeflags.md) | TBD |
| [IoSetDevicePropertyData function](nf-wdm-iosetdevicepropertydata.md) | The IoSetDevicePropertyData routine modifies the current setting for a device property. |
| [RtlLargeIntegerNegate function](nf-wdm-rtllargeintegernegate.md) | TBD |
| [IoGetStackLimits function](nf-wdm-iogetstacklimits.md) | The IoGetStackLimits routine returns the boundaries of the current thread's stack frame. |
| [HalAllocateCommonBuffer function](nf-wdm-halallocatecommonbuffer.md) | TBD |
| [IoWMISetNotificationCallback function](nf-wdm-iowmisetnotificationcallback.md) | The IoWMISetNotificationCallback routine registers a notification callback for a WMI event. |
| [IoFreeIrp function](nf-wdm-iofreeirp.md) | The IoFreeIrp routine releases a caller-allocated IRP from the caller's IoCompletion routine. |
| [InterlockedXor8 function](nf-wdm-interlockedxor8.md) | TBD |
| [KeClearEvent function](nf-wdm-keclearevent.md) | The KeClearEvent routine sets an event to a not-signaled state. |
| [IoSetCompletionRoutineEx function](nf-wdm-iosetcompletionroutineex.md) | The IoSetCompletionRoutineEx routine registers an IoCompletion routine, which is called when the next-lower-level driver has completed the requested operation for the given IRP. |
| [IoCsqInsertIrpEx function](nf-wdm-iocsqinsertirpex.md) | The IoCsqInsertIrpEx routine inserts an IRP into the driver's cancel-safe IRP queue. |
| [IoInitializeIrpEx function](nf-wdm-ioinitializeirpex.md) | TBD |
| [InterlockedIncrement64 function](nf-wdm-interlockedincrement64.md) | TBD |
| [IoValidateDeviceIoControlAccess function](nf-wdm-iovalidatedeviceiocontrolaccess.md) | For more information, see the WdmlibIoValidateDeviceIoControlAccess function. |
| [MmIsVerifierEnabled function](nf-wdm-mmisverifierenabled.md) | TBD |
| [READ_REGISTER_ULONG function](nf-wdm-read-register-ulong~r2.md) | The READ_REGISTER_ULONG routine reads a ULONG value from the specified register address. |
| [KeStallExecutionProcessor function](nf-wdm-kestallexecutionprocessor.md) | The KeStallExecutionProcessor routine stalls the caller on the current processor for a specified time interval. |
| [vDbgPrintExWithPrefix function](nf-wdm-vdbgprintexwithprefix.md) | The vDbgPrintExWithPrefix routine sends a string to the kernel debugger if certain conditions that you specify are met. This routine can append a prefix to debugger output to help organize debugging results. |
| [WriteULongRaw function](nf-wdm-writeulongraw.md) | TBD |
| [ClfsAdvanceLogBase function](nf-wdm-clfsadvancelogbase.md) | The ClfsAdvanceLogBase routine sets the base LSN of a CLFS stream. |
| [RtlFailFast function](nf-wdm-rtlfailfast.md) | TBD |
| [MmLockPagableCodeSection function](nf-wdm-mmlockpagablecodesection.md) | The MmLockPagableCodeSection routine locks a section of driver code, containing a set of driver routines marked with a special compiler directive, into system space. |
| [KeGetRecommendedSharedDataAlignment function](nf-wdm-kegetrecommendedshareddataalignment.md) | The KeGetRecommendedSharedDataAlignment routine returns the preferred alignment for memory structures that can be accessed by more than one processor. |
| [CmCallbackReleaseKeyObjectIDEx function](nf-wdm-cmcallbackreleasekeyobjectidex.md) | The CmCallbackReleaseKeyObjectIDEx routine frees an object name string obtained from the CmCallbackGetKeyObjectIDEx routine. |
| [LOOKASIDE_CHECK function](nf-wdm-lookaside-check~r2.md) | TBD |
| [KeFlushWriteBuffer function](nf-wdm-keflushwritebuffer.md) | TBD |
| [KeQueryHighestNodeNumber function](nf-wdm-kequeryhighestnodenumber.md) | The KeQueryHighestNodeNumber routine returns the highest node number in a multiprocessor system that has a non-uniform memory access (NUMA) architecture. |
| [ReadNoFence function](nf-wdm-readnofence.md) | TBD |
| [RtlIsZeroLuid function](nf-wdm-rtliszeroluid.md) | TBD |
| [KeQueryPriorityThread function](nf-wdm-kequeryprioritythread.md) | The KeQueryPriorityThread routine returns the current priority of a particular thread. |
| [NtSetInformationTransaction function](nf-wdm-ntsetinformationtransaction.md) | TBD |
| [ObDereferenceObject function](nf-wdm-obdereferenceobject.md) | The ObDereferenceObject routine decrements the given object's reference count and performs retention checks. |
| [KeInitializeDeviceQueue function](nf-wdm-keinitializedevicequeue.md) | The KeInitializeDeviceQueue routine initializes a device queue object to a not-busy state. |
| [_InterlockedXor function](nf-wdm--interlockedxor.md) | TBD |
| [CmGetCallbackVersion function](nf-wdm-cmgetcallbackversion.md) | The CmGetCallbackVersion routine retrieves the major and minor version numbers for the current version of the configuration manager's registry callback feature. |
| [ObReferenceObject function](nf-wdm-obreferenceobject.md) | The ObReferenceObject routine increments the reference count to the given object. |
| [ExInitializeFastMutex function](nf-wdm-exinitializefastmutex.md) | The ExInitializeFastMutex routine initializes a fast mutex variable, used to synchronize mutually exclusive access by a set of threads to a shared resource. |
| [InterlockedExchange8 function](nf-wdm-interlockedexchange8.md) | TBD |
| [__writefsdword function](nf-wdm---writefsdword.md) | TBD |
| [MmGetMdlByteOffset function](nf-wdm-mmgetmdlbyteoffset.md) | TBD |
| [ReadNoFence8 function](nf-wdm-readnofence8~r2.md) | TBD |
| [RtlCompareMemory function](nf-wdm-rtlcomparememory.md) | The RtlCompareMemory routine compares two blocks of memory and returns the number of bytes that match. |
| [IoCheckShareAccess function](nf-wdm-iocheckshareaccess.md) | The IoCheckShareAccess routine is called by file system drivers (FSDs) or other highest-level drivers to check whether shared access to a file object is permitted. |
| [IoDetachDevice function](nf-wdm-iodetachdevice.md) | The IoDetachDevice routine releases an attachment between the caller's device object and a lower driver's device object. |
| [ReadNoFence64 function](nf-wdm-readnofence64~r1.md) | TBD |
| [READ_PORT_UCHAR function](nf-wdm-read-port-uchar.md) | The READ_PORT_UCHAR routine reads a byte from the specified port address. |
| [ZwSetValueKey function](nf-wdm-zwsetvaluekey.md) | The ZwSetValueKey routine creates or replaces a registry key's value entry. |
| [IoUnregisterShutdownNotification function](nf-wdm-iounregistershutdownnotification.md) | The IoUnregisterShutdownNotification routine removes a registered driver from the shutdown notification queue. |
| [__break function](nf-wdm---break.md) | TBD |
| [IoCsqRemoveIrp function](nf-wdm-iocsqremoveirp.md) | The IoCsqRemoveIrp routine removes a particular IRP from the queue. |
| [ObReferenceObjectByPointer function](nf-wdm-obreferenceobjectbypointer.md) | The ObReferenceObjectByPointer routine increments the pointer reference count for a given object. |
| [PoGetSystemWake function](nf-wdm-pogetsystemwake.md) | The PoGetSystemWake routine determines whether a specified IRP has been marked as waking the system from a sleeping state. |
| [IoCsqInitializeEx function](nf-wdm-iocsqinitializeex.md) | The IoCsqInitializeEx routine initializes the dispatch table for a cancel-safe IRP queue. |
| [IoInitializeWorkItem function](nf-wdm-ioinitializeworkitem.md) | The IoInitializeWorkItem routine initializes a work item that the caller has already allocated. |
| [ZwOpenSymbolicLinkObject function](nf-wdm-zwopensymboliclinkobject.md) | The ZwOpenSymbolicLinkObject routine opens an existing symbolic link. |
| [RtlSetBits function](nf-wdm-rtlsetbits.md) | The RtlSetBits routine sets all bits in a given range of a given bitmap variable. |
| [ClfsFreeReservedLog function](nf-wdm-clfsfreereservedlog.md) | TBD |
| [IoGetFunctionCodeFromCtlCode function](nf-wdm-iogetfunctioncodefromctlcode.md) | The IoGetFunctionCodeFromCtlCode macro returns the value of the function code contained in an I/O control code. |
| [ObfReferenceObjectWithTag function](nf-wdm-obfreferenceobjectwithtag.md) | TBD |
| [IoAttachDeviceToDeviceStack function](nf-wdm-ioattachdevicetodevicestack.md) | The IoAttachDeviceToDeviceStack routine attaches the caller's device object to the highest device object in the chain and returns a pointer to the previously highest device object. |
| [KeQueryMaximumProcessorCountEx function](nf-wdm-kequerymaximumprocessorcountex.md) | The KeQueryMaximumProcessorCountEx routine returns the maximum number of logical processors in a specified group in a multiprocessor system. |
| [WriteNoFence16 function](nf-wdm-writenofence16~r2.md) | TBD |
| [ExInitializeNPagedLookasideList function](nf-wdm-exinitializenpagedlookasidelist.md) | The ExInitializeNPagedLookasideList routine initializes a lookaside list for nonpaged entries of the specified size. |
| [IoSynchronousCallDriver function](nf-wdm-iosynchronouscalldriver.md) | TBD |
| [NT_ANALYSIS_ASSUME function](nf-wdm-nt-analysis-assume.md) | TBD |
| [operator> function](nf-wdm-operator_.md) | TBD |
| [KeLeaveCriticalRegion function](nf-wdm-keleavecriticalregion.md) | The KeLeaveCriticalRegion routine reenables the delivery of normal kernel-mode APCs that were disabled by a preceding call to KeEnterCriticalRegion. |
| [IoUpdateLinkShareAccess function](nf-wdm-ioupdatelinkshareaccess.md) | The IoUpdateLinkShareAccess routine updates the share access for the given file object, usually when the file is being opened. |
| [RtlFindClearBits function](nf-wdm-rtlfindclearbits.md) | The RtlFindClearBits routine searches for a range of clear bits of a requested size within a bitmap. |
| [WRITE_REGISTER_NOFENCE_BUFFER_ULONG64 function](nf-wdm-write-register-nofence-buffer-ulong64.md) | TBD |
| [CmCallbackGetKeyObjectID function](nf-wdm-cmcallbackgetkeyobjectid.md) | The CmCallbackGetKeyObjectID routine retrieves the unique identifier and object name that are associated with a specified registry key object. |
| [KeRestoreFloatingPointState function](nf-wdm-kerestorefloatingpointstate~r2.md) | The KeRestoreFloatingPointState routine restores the nonvolatile floating-point context saved by the preceding call to KeSaveFloatingPointState. |
| [ReadPMC function](nf-wdm-readpmc.md) | TBD |
| [ObReferenceObjectWithTag function](nf-wdm-obreferenceobjectwithtag.md) | The ObReferenceObjectWithTag routine increments the reference count of the specified object, and writes a four-byte tag value to the object to support object reference tracing. |
| [KeAcquireSpinLock function](nf-wdm-keacquirespinlock~r1.md) | The KeAcquireSpinLock routine acquires a spin lock so the caller can synchronize access to shared data in a multiprocessor-safe way by raising IRQL. |
| [UnsignedMultiplyHigh function](nf-wdm-unsignedmultiplyhigh.md) | TBD |
| [KdRefreshDebuggerNotPresent function](nf-wdm-kdrefreshdebuggernotpresent.md) | The KdRefreshDebuggerNotPresent macro refreshes the value of the KD_DEBUGGER_NOT_PRESENT global kernel variable. |
| [InterlockedCompareExchange64 function](nf-wdm-interlockedcompareexchange64.md) | TBD |
| [TmRollbackEnlistment function](nf-wdm-tmrollbackenlistment.md) | The TmRollbackEnlistment routine rolls back a specified enlistment. |
| [IoGetBootDiskInformation function](nf-wdm-iogetbootdiskinformation.md) | The IoGetBootDiskInformation routine returns information describing the boot and system disks. |
| [RemoveHeadList function](nf-wdm-removeheadlist.md) | The RemoveHeadList routine removes an entry from the beginning of a doubly linked list of LIST_ENTRY structures. |
| [PoFxCompleteDevicePowerNotRequired function](nf-wdm-pofxcompletedevicepowernotrequired.md) | The PoFxCompleteDevicePowerNotRequired routine notifies the power management framework (PoFx) that the calling driver has completed its response to a call to the driver's DevicePowerNotRequiredCallback callback routine. |
| [ReadAcquire function](nf-wdm-readacquire.md) | TBD |
| [TmRecoverResourceManager function](nf-wdm-tmrecoverresourcemanager.md) | The TmRecoverResourceManager routine tries to recover the transaction that is associated with each enlistment of a specified resource manager object. |
| [KfRaiseIrql function](nf-wdm-kfraiseirql~r1.md) | TBD |
| [WRITE_REGISTER_BUFFER_UCHAR function](nf-wdm-write-register-buffer-uchar~r3.md) | The WRITE_REGISTER_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified register. |
| [IoWithinStackLimits function](nf-wdm-iowithinstacklimits.md) | The IoWithinStackLimits routine determines whether a region of memory is within the stack limit of the current thread. |
| [ClfsAddLogContainer function](nf-wdm-clfsaddlogcontainer.md) | The ClfsAddLogContainer routine adds a container to a CLFS log. |
| [__stosd function](nf-wdm---stosd.md) | TBD |
| [KeSaveFloatingPointState function](nf-wdm-kesavefloatingpointstate~r3.md) | The KeSaveFloatingPointState routine saves the nonvolatile floating-point context so the caller can carry out floating-point operations. |
| [ExInterlockedCompareExchange64 function](nf-wdm-exinterlockedcompareexchange64.md) | The ExInterlockedCompareExchange64 routine compares one integer variable to another and, if they are equal, sets the first variable to a caller-supplied value. |
| [ExAllocateCacheAwareRundownProtection function](nf-wdm-exallocatecacheawarerundownprotection.md) | TBD |
| [ReadUShortRaw function](nf-wdm-readushortraw.md) | TBD |
| [WriteULong64Raw function](nf-wdm-writeulong64raw.md) | TBD |
| [PoDeletePowerRequest function](nf-wdm-podeletepowerrequest.md) | The PoDeletePowerRequest routine deletes a power request object. |
| [PcwCloseInstance function](nf-wdm-pcwcloseinstance.md) | The PcwCloseInstance function closes the specified instance of the counter set. |
| [IoSetIoAttributionIrp function](nf-wdm-iosetioattributionirp.md) | TBD |
| [__movsw function](nf-wdm---movsw.md) | TBD |
| [IoWMIExecuteMethod function](nf-wdm-iowmiexecutemethod.md) | The IoWMIExecuteMethod routine runs a WMI class method on the specified WMI data block instance. |
| [KeGetCurrentThread function](nf-wdm-kegetcurrentthread~r1.md) | The KeGetCurrentThread routine identifies the current thread. |
| [IoAllocateDriverObjectExtension function](nf-wdm-ioallocatedriverobjectextension.md) | The IoAllocateDriverObjectExtension routine allocates a per-driver context area, called a driver object extension, and assigns a unique identifier to it. |
| [IoWMIDeviceObjectToProviderId function](nf-wdm-iowmideviceobjecttoproviderid~r1.md) | The IoWMIDeviceObjectToProviderId routine translates the specified device object into the corresponding WMI Provider ID. |
| [__readcr3 function](nf-wdm---readcr3.md) | TBD |
| [KeInsertByKeyDeviceQueue function](nf-wdm-keinsertbykeydevicequeue.md) | The KeInsertByKeyDeviceQueue routine acquires the spin lock for the specified DeviceQueue and queues an entry according to the specified sort-key value if the device queue is set to a busy state. |
| [IoSetCompletionRoutine function](nf-wdm-iosetcompletionroutine.md) | The IoSetCompletionRoutine routine registers an IoCompletion routine, which will be called when the next-lower-level driver has completed the requested operation for the given IRP. |
| [KeMemoryBarrier function](nf-wdm-kememorybarrier~r3.md) | The KeMemoryBarrier routine creates a barrier at its position in the code&#8212;across which the compiler and the processor cannot move any operations. |
| [READ_REGISTER_NOFENCE_ULONG function](nf-wdm-read-register-nofence-ulong.md) | TBD |
| [_mm_mfence function](nf-wdm--mm-mfence.md) | TBD |
| [__inbytestring function](nf-wdm---inbytestring.md) | TBD |
| [EtwProviderEnabled function](nf-wdm-etwproviderenabled.md) | The EtwProviderEnabled function verifies that a provider is enabled for event logging at a specified level and keyword. |
| [InterlockedXor8 function](nf-wdm-interlockedxor8~r1.md) | TBD |
| [KeQueryActiveProcessors function](nf-wdm-kequeryactiveprocessors.md) | TBD |
| [RtlEnlargedUnsignedDivide function](nf-wdm-rtlenlargedunsigneddivide.md) | TBD |
| [ExInterlockedPopEntrySList function](nf-wdm-exinterlockedpopentryslist~r1.md) | The ExInterlockedPopEntrySList routine atomically removes the first entry from a sequenced singly linked list. |
| [NT_VERIFYMSGW function](nf-wdm-nt-verifymsgw.md) | TBD |
| [InterlockedXor16 function](nf-wdm-interlockedxor16~r1.md) | TBD |
| [WriteCR3 function](nf-wdm-writecr3.md) | TBD |
| [IoGetTopLevelIrp function](nf-wdm-iogettoplevelirp.md) | TBD |
| [WritePointerRaw function](nf-wdm-writepointerraw~r1.md) | TBD |
| [IoRequestDeviceEjectEx function](nf-wdm-iorequestdeviceejectex.md) | TBD |
| [TmCommitEnlistment function](nf-wdm-tmcommitenlistment.md) | The TmCommitEnlistment routine initiates the commit operation for a specified enlistment's transaction. |
| [ReadAcquire16 function](nf-wdm-readacquire16.md) | TBD |
| [InterlockedExchange16 function](nf-wdm-interlockedexchange16.md) | TBD |
| [ClfsMgmtRemovePolicy function](nf-wdm-clfsmgmtremovepolicy.md) | The ClfsMgmtRemovePolicy routine resets a log's CLFS_MGMT_POLICY structure to its default value. |
| [KeRevertToUserAffinityThread function](nf-wdm-kereverttouseraffinitythread.md) | TBD |
| [ExInterlockedInsertTailList function](nf-wdm-exinterlockedinserttaillist.md) | The ExInterlockedInsertTailList routine atomically inserts an entry at the end of a doubly linked list of LIST_ENTRY structures. |
| [WriteRelease16 function](nf-wdm-writerelease16~r2.md) | TBD |
| [WmiTraceMessage function](nf-wdm-wmitracemessage.md) | The WmiTraceMessage routine adds a message to the output log of a WPP software tracing session. |
| [ReadRaw16 function](nf-wdm-readraw16.md) | TBD |
| [WRITE_REGISTER_BUFFER_USHORT function](nf-wdm-write-register-buffer-ushort~r1.md) | The WRITE_REGISTER_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified register. |
| [__inwordstring function](nf-wdm---inwordstring.md) | TBD |
| [IoAttachDevice function](nf-wdm-ioattachdevice.md) | The IoAttachDevice routine attaches the caller's device object to a named target device object, so that I/O requests bound for the target device are routed first to the caller. |
| [READ_PORT_BUFFER_ULONG function](nf-wdm-read-port-buffer-ulong~r2.md) | The READ_PORT_BUFFER_ULONG routine reads a number of ULONG values from the specified port address into a buffer. |
| [InterlockedDecrement function](nf-wdm-interlockeddecrement.md) | The InterlockedDecrement routine decrements a caller-supplied variable of type LONG as an atomic operation. |
| [ExCancelTimer function](nf-wdm-excanceltimer.md) | The ExCancelTimer routine cancels a timer that was set by a previous call to the ExSetTimer routine. |
| [IoGetSfioStreamIdentifier function](nf-wdm-iogetsfiostreamidentifier.md) | TBD |
| [IoOpenDeviceInterfaceRegistryKey function](nf-wdm-ioopendeviceinterfaceregistrykey.md) | The IoOpenDeviceInterfaceRegistryKey routine returns a handle to a registry key for storing information about a particular device interface instance. |
| [KeSetSystemGroupAffinityThread function](nf-wdm-kesetsystemgroupaffinitythread.md) | The KeSetSystemGroupAffinityThread routine changes the group number and affinity mask of the calling thread. |
| [ClfsMgmtSetLogFileSize function](nf-wdm-clfsmgmtsetlogfilesize.md) | The ClfsMgmtSetLogFileSize routine adds containers to a log or deletes containers from a log. |
| [PoRegisterDeviceForIdleDetection function](nf-wdm-poregisterdeviceforidledetection.md) | The PoRegisterDeviceForIdleDetection routine enables or cancels idle detection and sets idle time-out values for a device. |
| [ZwPrepareComplete function](nf-wdm-zwpreparecomplete.md) | The ZwPrepareComplete routine notifies KTM that the calling resource manager has finished preparing a transaction's data. |
| [ProbeForWrite function](nf-wdm-probeforwrite.md) | The ProbeForWrite routine checks that a user-mode buffer actually resides in the user-mode portion of the address space, is writable, and is correctly aligned. |
| [operator!= function](nf-wdm-operator!=.md) | TBD |
| [KfLowerIrql function](nf-wdm-kflowerirql.md) | TBD |
| [__movsd function](nf-wdm---movsd.md) | TBD |
| [EtwWriteString function](nf-wdm-etwwritestring.md) | The EventWriteString function is a tracing function that you can use when no sophisticated data is required. This function is similar to a debug print statement. |
| [ExpInterlockedPushEntrySList function](nf-wdm-expinterlockedpushentryslist.md) | TBD |
| [ObCloseHandle function](nf-wdm-obclosehandle.md) | The ObCloseHandle routine closes an object handle. |
| [ZwLoadDriver function](nf-wdm-zwloaddriver.md) | The ZwLoadDriver routine loads a driver into the system. |
| [_mm_prefetch function](nf-wdm--mm-prefetch.md) | TBD |
| [ObGetObjectSecurity function](nf-wdm-obgetobjectsecurity.md) | The ObGetObjectSecurity routine gets the security descriptor for a given object. |
| [ExAllocatePoolWithTag function](nf-wdm-exallocatepoolwithtag~r1.md) | The ExAllocatePoolWithTag routine allocates pool memory of the specified type and returns a pointer to the allocated block. |
| [NtEnumerateTransactionObject function](nf-wdm-ntenumeratetransactionobject.md) | TBD |
| [KeGetCurrentIrql function](nf-wdm-kegetcurrentirql~r3.md) | The KeGetCurrentIrql routine returns the current IRQL. |
| [_mm_pause function](nf-wdm--mm-pause.md) | TBD |
| [ExRaiseStatus function](nf-wdm-exraisestatus.md) | The ExRaiseStatus routine is called by drivers that supply structured exception handlers to handle particular errors that occur while they are processing I/O requests. |
| [WRITE_PORT_UCHAR function](nf-wdm-write-port-uchar.md) | The WRITE_PORT_UCHAR routine writes a byte to the specified port address. |
| [ZwCreateEnlistment function](nf-wdm-zwcreateenlistment.md) | The ZwCreateEnlistment routine creates a new enlistment object for a transaction. |
| [RtlLargeIntegerEqualTo function](nf-wdm-rtllargeintegerequalto.md) | TBD |
| [REGISTER_FENCE function](nf-wdm-register-fence~r1.md) | TBD |
| [YieldProcessor function](nf-wdm-yieldprocessor.md) | TBD |
| [WRITE_REGISTER_BUFFER_ULONG function](nf-wdm-write-register-buffer-ulong~r2.md) | The WRITE_REGISTER_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified register. |
| [READ_PORT_BUFFER_UCHAR function](nf-wdm-read-port-buffer-uchar.md) | The READ_PORT_BUFFER_UCHAR routine reads a number of bytes from the specified port address into a buffer. |
| [__outwordstring function](nf-wdm---outwordstring.md) | TBD |
| [KeInitializeEvent function](nf-wdm-keinitializeevent.md) | The KeInitializeEvent routine initializes an event object as a synchronization (single waiter) or notification type event and sets it to a signaled or not-signaled state. |
| [WRITE_REGISTER_ULONG function](nf-wdm-write-register-ulong~r1.md) | The WRITE_REGISTER_ULONG routine writes a ULONG value to the specified address. |
| [KeGetProcessorNumberFromIndex function](nf-wdm-kegetprocessornumberfromindex.md) | The KeGetProcessorNumberFromIndex routine converts a systemwide processor index to a group number and a group-relative processor number. |
| [vDbgPrintEx function](nf-wdm-vdbgprintex.md) | The vDbgPrintEx routine sends a string to the kernel debugger if certain conditions are met. |
| [READ_REGISTER_ULONG function](nf-wdm-read-register-ulong~r1.md) | The READ_REGISTER_ULONG routine reads a ULONG value from the specified register address. |
| [IoCreateUnprotectedSymbolicLink function](nf-wdm-iocreateunprotectedsymboliclink.md) | The IoCreateUnprotectedSymbolicLink routine sets up an unprotected symbolic link between a device object name and a corresponding Win32-visible name. |
| [IoStartNextPacketByKey function](nf-wdm-iostartnextpacketbykey.md) | The IoStartNextPacketByKey routine dequeues the next I/O request packet from the specified device object's associated device queue according to a specified sort-key value and calls the driver's StartIo routine with that IRP. |
| [IoCheckLinkShareAccess function](nf-wdm-iochecklinkshareaccess.md) | The IoCheckLinkShareAccess routine is called by file system drivers (FSDs) or other highest-level drivers to check whether link shared access to a file object is permitted. |
| [KeRemoveQueueDpc function](nf-wdm-keremovequeuedpc.md) | The KeRemoveQueueDpc routine removes the specified DPC object from the system DPC queue. |
| [ObReleaseObjectSecurity function](nf-wdm-obreleaseobjectsecurity.md) | The ObReleaseObjectSecurity routine is the reciprocal to ObGetObjectSecurity. |
| [READ_REGISTER_NOFENCE_ULONG function](nf-wdm-read-register-nofence-ulong~r1.md) | TBD |
| [RtlExtendedIntegerMultiply function](nf-wdm-rtlextendedintegermultiply.md) | TBD |
| [MmUnlockPages function](nf-wdm-mmunlockpages.md) | The MmUnlockPages routine unlocks the physical pages that are described by the specified memory descriptor list (MDL). |
| [PoFxQueryCurrentComponentPerfState function](nf-wdm-pofxquerycurrentcomponentperfstate.md) | The PoFxQueryCurrentComponentPerfState routine retrieves the active performance state in a component's performance state set. |
| [NtGetNotificationResourceManager function](nf-wdm-ntgetnotificationresourcemanager.md) | TBD |
| [ExInterlockedFlushSList function](nf-wdm-exinterlockedflushslist.md) | The ExInterlockedFlushSList routine atomically removes all entries from a sequenced singly linked list. |
| [ReadPointerAcquire function](nf-wdm-readpointeracquire.md) | TBD |
| [WRITE_PORT_USHORT function](nf-wdm-write-port-ushort~r2.md) | The WRITE_PORT_USHORT routine writes a USHORT value to the specified port address. |
| [NtPropagationFailed function](nf-wdm-ntpropagationfailed.md) | TBD |
| [RtlLargeIntegerAdd function](nf-wdm-rtllargeintegeradd.md) | TBD |
| [ExInterlockedAddLargeInteger function](nf-wdm-exinterlockedaddlargeinteger.md) | The ExInterlockedAddLargeInteger routine adds a large integer value to the specified variable as an atomic operation. |
| [IoConnectInterruptEx function](nf-wdm-ioconnectinterruptex.md) | For more information, see the WdmlibIoConnectInterruptEx function.#define IoConnectInterruptEx WdmlibIoConnectInterruptEx |
| [ZwQueryInformationTransaction function](nf-wdm-zwqueryinformationtransaction.md) | The ZwQueryInformationTransaction routine retrieves information about a specified transaction. |
| [ZwEnumerateKey function](nf-wdm-zwenumeratekey.md) | The ZwEnumerateKey routine returns information about a subkey of an open registry key. |
| [PoFxSetComponentResidency function](nf-wdm-pofxsetcomponentresidency.md) | The PoFxSetComponentResidency routine sets the estimated time for how long a component is likely to remain idle after the component enters the idle condition. |
| [KeGetCurrentProcessorIndex function](nf-wdm-kegetcurrentprocessorindex.md) | TBD |
| [READ_PORT_UCHAR function](nf-wdm-read-port-uchar~r2.md) | The READ_PORT_UCHAR routine reads a byte from the specified port address. |
| [ZwQueryKey function](nf-wdm-zwquerykey.md) | The ZwQueryKey routine provides information about the class of a registry key, and the number and sizes of its subkeys. |
| [NT_ASSERTMSG_ASSUME function](nf-wdm-nt-assertmsg-assume.md) | TBD |
| [WRITE_REGISTER_NOFENCE_USHORT function](nf-wdm-write-register-nofence-ushort~r1.md) | TBD |
| [TmPrepareEnlistment function](nf-wdm-tmprepareenlistment.md) | The TmPrepareEnlistment routine initiates the prepare operation for a specified enlistment's transaction. |
| [KeBugCheckEx function](nf-wdm-kebugcheckex.md) | The KeBugCheckEx routine brings down the system in a controlled manner when the caller discovers an unrecoverable inconsistency that would corrupt the system if the caller continued to run. |
| [IoGetRemainingStackSize function](nf-wdm-iogetremainingstacksize.md) | The IoGetRemainingStackSize routine returns the current amount of available kernel-mode stack space. |
| [ReadNoFence16 function](nf-wdm-readnofence16~r2.md) | TBD |
| [IoRemoveLinkShareAccess function](nf-wdm-ioremovelinkshareaccess.md) | The IoRemoveLinkShareAccess routine removes the access and link share-access information for a given open instance of a file object. |
| [IoIs32bitProcess function](nf-wdm-iois32bitprocess.md) | The IoIs32bitProcess routine checks whether the originator of the current I/O request is a 32-bit user-mode application. |
| [ExInitializeResourceLite function](nf-wdm-exinitializeresourcelite.md) | The ExInitializeResourceLite routine initializes a resource variable. |
| [IoGetAttachedDeviceReference function](nf-wdm-iogetattacheddevicereference.md) | The IoGetAttachedDeviceReference routine returns a pointer to the highest level device object in a driver stack and increments the reference count on that object. |
| [ZwSetInformationResourceManager function](nf-wdm-zwsetinformationresourcemanager.md) | TBD |
| [READ_REGISTER_BUFFER_USHORT function](nf-wdm-read-register-buffer-ushort~r1.md) | The READ_REGISTER_BUFFER_USHORT routine reads a number of USHORT values from the specified register address into a buffer. |
| [IoWriteErrorLogEntry function](nf-wdm-iowriteerrorlogentry.md) | The IoWriteErrorLogEntry routine queues a given error log packet to the system error logging thread. |
| [KeQueryDpcWatchdogInformation function](nf-wdm-kequerydpcwatchdoginformation.md) | The KeQueryDpcWatchdogInformation routine returns the deferred procedure call (DPC) watchdog timer values for the current processor. |
| [__addgsword function](nf-wdm---addgsword.md) | TBD |
| [ReadNoFence function](nf-wdm-readnofence~r2.md) | TBD |
| [ExIsManufacturingModeEnabled function](nf-wdm-exismanufacturingmodeenabled.md) | TBD |
| [PoCallDriver function](nf-wdm-pocalldriver.md) | The PoCallDriver routine passes a power IRP to the next-lower driver in the device stack. (Windows Server 2003, Windows XP, and Windows 2000 only.). |
| [RtlAnsiStringToUnicodeString function](nf-wdm-rtlansistringtounicodestring.md) | RtlAnsiStringToUnicodeString converts the given ANSI source string into a Unicode string. |
| [_ReadWriteBarrier function](nf-wdm--readwritebarrier.md) | TBD |
| [NT_ASSERTMSG_NOASSUME function](nf-wdm-nt-assertmsg-noassume.md) | TBD |
| [__cpuidex function](nf-wdm---cpuidex~r1.md) | TBD |
| [ClfsLsnCreate function](nf-wdm-clfslsncreate.md) | The ClfsLsnCreate routine creates a log sequence number (LSN), given a container identifier, a block offset, and a record sequence number. |
| [ClfsLsnInvalid function](nf-wdm-clfslsninvalid.md) | TBD |
| [ExGetFirmwareType function](nf-wdm-exgetfirmwaretype.md) | Returns the system firmware type. |
| [ExReleaseRundownProtectionEx function](nf-wdm-exreleaserundownprotectionex.md) | The ExReleaseRundownProtectionEx routine releases run-down protection that the caller previously acquired by calling the ExAcquireRundownProtectionEx routine. |
| [KeResetEvent function](nf-wdm-keresetevent.md) | The KeResetEvent routine resets a specified event object to a not-signaled state and returns the previous state of that event object. |
| [IoSetDeviceInterfacePropertyData function](nf-wdm-iosetdeviceinterfacepropertydata.md) | The IoSetDeviceInterfacePropertyData routine modifies the current value of a device interface property. |
| [MmUnmapIoSpace function](nf-wdm-mmunmapiospace.md) | The MmUnmapIoSpace routine unmaps a specified range of physical addresses previously mapped by MmMapIoSpace. |
| [MmIsIoSpaceActive function](nf-wdm-mmisiospaceactive.md) | TBD |
| [RtlUTF8ToUnicodeN function](nf-wdm-rtlutf8tounicoden.md) | The RtlUTF8ToUnicodeN routine converts a UTF-8 string to a Unicode string. |
| [IoWMIRegistrationControl function](nf-wdm-iowmiregistrationcontrol.md) | The IoWMIRegistrationControl routine registers or unregisters the caller as a WMI data provider for a specified device object. |
| [ExCleanupRundownProtectionCacheAware function](nf-wdm-excleanuprundownprotectioncacheaware.md) | TBD |
| [IoAllocateIrpEx function](nf-wdm-ioallocateirpex.md) | TBD |
| [RtlMoveMemory function](nf-wdm-rtlmovememory.md) | The RtlMoveMemory routine copies the contents of a source memory block to a destination memory block, and supports overlapping source and destination memory blocks. |
| [RtlLargeIntegerSubtract function](nf-wdm-rtllargeintegersubtract.md) | TBD |
| [TmCommitComplete function](nf-wdm-tmcommitcomplete.md) | The TmCommitComplete routine notifies KTM that the calling resource manager has finished committing a transaction. |
| [NT_ASSERTMSGW_ACTION function](nf-wdm-nt-assertmsgw-action.md) | TBD |
| [IoGetAffinityInterrupt function](nf-wdm-iogetaffinityinterrupt.md) | For more information, see the WdmlibIoGetAffinityInterrupt function.#define IoGetAffinityInterrupt WdmlibIoGetAffinityInterrupt |
| [ExInterlockedInsertHeadList function](nf-wdm-exinterlockedinsertheadlist.md) | The ExInterlockedInsertHeadList routine atomically inserts an entry at the beginning of a doubly linked list of LIST_ENTRY structures. |
| [ClfsReadNextLogRecord function](nf-wdm-clfsreadnextlogrecord.md) | The ClfsReadNextLogRecord routine reads the next record in a sequence, relative to the current record in a read context. |
| [ALIGN_UP_POINTER function](nf-wdm-align-up-pointer.md) | TBD |
| [PoFxRegisterComponentPerfStates function](nf-wdm-pofxregistercomponentperfstates.md) | The PoFxRegisterComponentPerfStates routine registers a device component for performance state management by the power management framework (PoFx). |
| [ReadUCharNoFence function](nf-wdm-readucharnofence.md) | TBD |
| [ClfsLsnLess function](nf-wdm-clfslsnless.md) | The ClfsLsnLess routine determines whether one LSN is less than another LSN. The two LSNs must be from the same stream. |
| [KeInitializeSpinLock function](nf-wdm-keinitializespinlock.md) | The KeInitializeSpinLock routine initializes a variable of type KSPIN_LOCK. |
| [RtlFindClearBitsAndSet function](nf-wdm-rtlfindclearbitsandset.md) | The RtlFindClearBitsAndSet routine searches for a range of clear bits of a requested size within a bitmap and sets all bits in the range when it has been located. |
| [InterlockedOr16 function](nf-wdm-interlockedor16.md) | TBD |
| [__writegsdword function](nf-wdm---writegsdword.md) | TBD |
| [IoInitializeRemoveLock function](nf-wdm-ioinitializeremovelock.md) | The IoInitializeRemoveLock routine initializes a remove lock for a device object. |
| [KeWaitForSingleObject function](nf-wdm-kewaitforsingleobject.md) | The KeWaitForSingleObject routine puts the current thread into a wait state until the given dispatcher object is set to a signaled state or (optionally) until the wait times out. |
| [KeRestoreFloatingPointState function](nf-wdm-kerestorefloatingpointstate.md) | The KeRestoreFloatingPointState routine restores the nonvolatile floating-point context saved by the preceding call to KeSaveFloatingPointState. |
| [ZwCommitEnlistment function](nf-wdm-zwcommitenlistment.md) | The ZwCommitEnlistment routine initiates the commit operation for a specified enlistment's transaction. |
| [_bittestandreset function](nf-wdm--bittestandreset~r1.md) | TBD |
| [KdEnableDebugger function](nf-wdm-kdenabledebugger.md) | The KdEnableDebugger routine re-enables the kernel debugger after a call to the KdDisableDebugger routine disables the kernel debugger. |
| [ALIGN_DOWN function](nf-wdm-align-down.md) | TBD |
| [InterlockedOr64 function](nf-wdm-interlockedor64.md) | TBD |
| [ClfsSetLogFileInformation function](nf-wdm-clfssetlogfileinformation.md) | The ClfsSetLogFileInformation routine sets metadata and state information for a specified stream and its underlying physical log. |
| [RtlQueryValidationRunlevel function](nf-wdm-rtlqueryvalidationrunlevel.md) | TBD |
| [PsGetVersion function](nf-wdm-psgetversion.md) | TBD |
| [IoBuildSynchronousFsdRequest function](nf-wdm-iobuildsynchronousfsdrequest.md) | The IoBuildSynchronousFsdRequest routine allocates and sets up an IRP for a synchronously processed I/O request. |
| [HalReadDmaCounter function](nf-wdm-halreaddmacounter.md) | TBD |
| [ZwSetInformationFile function](nf-wdm-zwsetinformationfile.md) | The ZwSetInformationFile routine changes various kinds of information about a file object. |
| [ShiftLeft128 function](nf-wdm-shiftleft128.md) | TBD |
| [_BitScanForward function](nf-wdm--bitscanforward.md) | TBD |
| [IoGetDeviceInterfaceAlias function](nf-wdm-iogetdeviceinterfacealias.md) | The IoGetDeviceInterfaceAlias routine returns the alias device interface of the specified device interface instance, if the alias exists. |
| [MmPrepareMdlForReuse function](nf-wdm-mmpreparemdlforreuse.md) | TBD |
| [ReadTimeStampCounter function](nf-wdm-readtimestampcounter.md) | TBD |
| [ExInterlockedAddLargeStatistic function](nf-wdm-exinterlockedaddlargestatistic.md) | The ExInterlockedAddLargeStatistic routine performs an interlocked addition of a ULONG increment value to a LARGE_INTEGER variable. |
| [READ_REGISTER_ULONG64 function](nf-wdm-read-register-ulong64.md) | TBD |
| [ReadULong64Acquire function](nf-wdm-readulong64acquire.md) | TBD |
| [ExEnumerateSystemFirmwareTables function](nf-wdm-exenumeratesystemfirmwaretables.md) | TBD |
| [IoCheckShareAccessEx function](nf-wdm-iocheckshareaccessex.md) | The IoCheckShareAccessEx routine is called by file system drivers (FSDs) or other highest-level drivers to check whether shared access to a file object is permitted. |
| [MmAllocateContiguousMemory function](nf-wdm-mmallocatecontiguousmemory.md) | TBD |
| [IoRequestDpc function](nf-wdm-iorequestdpc.md) | The IoRequestDpc routine queues a driver-supplied DpcForIsr routine to complete interrupt-driven I/O processing at a lower IRQL. |
| [ReadAcquire64 function](nf-wdm-readacquire64.md) | TBD |
| [IoWMISuggestInstanceName function](nf-wdm-iowmisuggestinstancename.md) | The IoWMISuggestInstanceName routine is used to request that WMI suggest a base name which a driver can use to build WMI instance names for the device. |
| [ReadULongAcquire function](nf-wdm-readulongacquire.md) | TBD |
| [READ_PORT_BUFFER_USHORT function](nf-wdm-read-port-buffer-ushort~r2.md) | The READ_PORT_BUFFER_USHORT routine reads a number of USHORT values from the specified port address into a buffer. |
| [ReadULong64NoFence function](nf-wdm-readulong64nofence.md) | TBD |
| [IoMarkIrpPending function](nf-wdm-iomarkirppending.md) | The IoMarkIrpPending routine marks the specified IRP, indicating that a driver's dispatch routine subsequently returned STATUS_PENDING because further processing is required by other driver routines. |
| [MmFreeContiguousMemorySpecifyCache function](nf-wdm-mmfreecontiguousmemoryspecifycache.md) | TBD |
| [ZwRollforwardTransactionManager function](nf-wdm-zwrollforwardtransactionmanager.md) | The ZwRollforwardTransactionManager routine initiates recovery operations for all of the in-progress transactions that are assigned to a specified transaction manager. |
| [WriteRelease64 function](nf-wdm-writerelease64~r2.md) | TBD |
| [IoReportInterruptActive function](nf-wdm-ioreportinterruptactive.md) | The IoReportInterruptActive routine informs the operating system that a registered interrupt service routine (ISR) is active and ready to handle interrupt requests. |
| [PoSetPowerState function](nf-wdm-posetpowerstate.md) | The PoSetPowerState routine notifies the system of a change in the device power state for a device. |
| [__writegsbyte function](nf-wdm---writegsbyte.md) | TBD |
| [MmPageEntireDriver function](nf-wdm-mmpageentiredriver.md) | The MmPageEntireDriver routine causes all of a driver's code and data to be made pageable, overriding the attributes of the various sections that make up the driver's image. |
| [PsWrapApcWow64Thread function](nf-wdm-pswrapapcwow64thread.md) | TBD |
| [ReadUShortAcquire function](nf-wdm-readushortacquire.md) | TBD |
| [ExQueryTimerResolution function](nf-wdm-exquerytimerresolution.md) | The ExQueryTimerResolution routine reports the range of timer resolutions that are supported by the system clock. |
| [NT_ASSERTMSGW_NOASSUME function](nf-wdm-nt-assertmsgw-noassume.md) | TBD |
| [WriteRelease function](nf-wdm-writerelease.md) | TBD |
| [VALID_IMPERSONATION_LEVEL function](nf-wdm-valid-impersonation-level.md) | TBD |
| [KeSetCoalescableTimer function](nf-wdm-kesetcoalescabletimer.md) | The KeSetCoalescableTimer routine sets the initial expiration time and period of a timer object and specifies how much delay can be tolerated in the expiration times. |
| [READ_REGISTER_NOFENCE_BUFFER_UCHAR function](nf-wdm-read-register-nofence-buffer-uchar.md) | TBD |
| [NtQueryInformationTransaction function](nf-wdm-ntqueryinformationtransaction.md) | TBD |
| [IoInvalidateDeviceRelations function](nf-wdm-ioinvalidatedevicerelations.md) | The IoInvalidateDeviceRelations routine notifies the PnP manager that the relations for a device (such as bus relations, ejection relations, removal relations, and the target device relation) have changed. |
| [DEFINE_GUIDEX function](nf-wdm-define-guidex.md) | TBD |
| [READ_PORT_BUFFER_ULONG function](nf-wdm-read-port-buffer-ulong~r1.md) | The READ_PORT_BUFFER_ULONG routine reads a number of ULONG values from the specified port address into a buffer. |
| [SeObjectCreateSaclAccessBits function](nf-wdm-seobjectcreatesaclaccessbits.md) | TBD |
| [ZwDeleteValueKey function](nf-wdm-zwdeletevaluekey.md) | The ZwDeleteValueKey routine deletes a value entry matching a name from an open key in the registry. If no such entry exists, an error is returned. |
| [PoSetDeviceBusy function](nf-wdm-posetdevicebusy.md) | TBD |
| [RtlWriteRegistryValue function](nf-wdm-rtlwriteregistryvalue.md) | The RtlWriteRegistryValue routine writes caller-supplied data into the registry along the specified relative path at the given value name. |
| [ClfsGetIoStatistics function](nf-wdm-clfsgetiostatistics.md) | The ClfsGetIoStatistics routine returns I/O statistics for a specified CLFS log. |
| [ZwCreateTransaction function](nf-wdm-zwcreatetransaction.md) | The ZwCreateTransaction routine creates a transaction object. |
| [ExInterlockedAddUlong function](nf-wdm-exinterlockedaddulong.md) | The ExInterlockedAddUlong routine adds an unsigned long value to a given unsigned integer as an atomic operation. |
| [WriteUShortRaw function](nf-wdm-writeushortraw.md) | TBD |
| [ReadULongRaw function](nf-wdm-readulongraw.md) | TBD |
| [KeShouldYieldProcessor function](nf-wdm-keshouldyieldprocessor.md) | TBD |
| [NT_FRE_ASSERTMSG function](nf-wdm-nt-fre-assertmsg.md) | TBD |
| [_interlockedbittestandreset function](nf-wdm--interlockedbittestandreset.md) | TBD |
| [IoAllocateMdl function](nf-wdm-ioallocatemdl.md) | The IoAllocateMdl routine allocates a memory descriptor list (MDL) large enough to map a buffer, given the buffer's starting address and length. Optionally, this routine associates the MDL with an IRP. |
| [ReadBooleanAcquire function](nf-wdm-readbooleanacquire.md) | TBD |
| [ObfDereferenceObjectWithTag function](nf-wdm-obfdereferenceobjectwithtag.md) | TBD |
| [ReadRaw64 function](nf-wdm-readraw64.md) | TBD |
| [RtlInterlockedClearBits function](nf-wdm-rtlinterlockedclearbits.md) | TBD |
| [PoEndDeviceBusy function](nf-wdm-poenddevicebusy.md) | The PoEndDeviceBusy routine marks the end of a period of time in which the device is busy. |
| [_mm_sfence function](nf-wdm--mm-sfence.md) | TBD |
| [_interlockedbittestandset function](nf-wdm--interlockedbittestandset~r1.md) | TBD |
| [ZwQueryFullAttributesFile function](nf-wdm-zwqueryfullattributesfile.md) | The ZwQueryFullAttributesFile routine supplies network open information for the specified file. |
| [RtlGetVersion function](nf-wdm-rtlgetversion.md) | TBD |
| [__addfsdword function](nf-wdm---addfsdword.md) | TBD |
| [PreFetchCacheLine function](nf-wdm-prefetchcacheline.md) | TBD |
| [PCI_MULTIFUNCTION_DEVICE function](nf-wdm-pci-multifunction-device.md) | TBD |
| [KeQueryActiveProcessorCountEx function](nf-wdm-kequeryactiveprocessorcountex.md) | The KeQueryActiveProcessorCountEx routine returns the number of active logical processors in a specified group in a multiprocessor system or in the entire system. |
| [MmMapLockedPagesSpecifyCache_NXOptIn function](nf-wdm-mmmaplockedpagesspecifycache-nxoptin.md) | TBD |
| [__readcr8 function](nf-wdm---readcr8.md) | TBD |
| [ZwRenameKey function](nf-wdm-zwrenamekey.md) | TBD |
| [ZwUnloadDriver function](nf-wdm-zwunloaddriver.md) | The ZwUnloadDriver routine unloads a driver from the system. |
| [IoOpenDeviceRegistryKey function](nf-wdm-ioopendeviceregistrykey.md) | The IoOpenDeviceRegistryKey routine returns a handle to a device-specific or a driver-specific registry key for a particular device instance. |
| [WriteCR8 function](nf-wdm-writecr8.md) | TBD |
| [__stosq function](nf-wdm---stosq.md) | TBD |
| [PoFxActivateComponent function](nf-wdm-pofxactivatecomponent.md) | The PoFxActivateComponent routine increments the activation reference count on the specified component. |
| [PcwUnregister function](nf-wdm-pcwunregister.md) | The PcwUnregister function unregisters the provider of the specified counter set. |
| [__outbytestring function](nf-wdm---outbytestring.md) | TBD |
| [PoSetThermalActiveCooling function](nf-wdm-posetthermalactivecooling.md) | TBD |
| [WriteNoFence function](nf-wdm-writenofence~r1.md) | TBD |
| [RtlEqualLuid function](nf-wdm-rtlequalluid.md) | TBD |
| [ZwPrePrepareEnlistment function](nf-wdm-zwpreprepareenlistment.md) | The ZwPrePrepareEnlistment routine initiates the pre-prepare operation for a specified enlistment's transaction. |
| [MmGetMdlBaseVa function](nf-wdm-mmgetmdlbaseva.md) | TBD |
| [WriteNoFence64 function](nf-wdm-writenofence64.md) | TBD |
| [KeGetCurrentProcessorIndex function](nf-wdm-kegetcurrentprocessorindex~r2.md) | TBD |
| [KzInitializeSpinLock function](nf-wdm-kzinitializespinlock.md) | TBD |
| [RtlStringFromGUID function](nf-wdm-rtlstringfromguid.md) | The RtlStringFromGUID routine converts a given GUID from binary format into a Unicode string. |
| [KeGetCurrentProcessorNumberEx function](nf-wdm-kegetcurrentprocessornumberex.md) | The KeGetCurrentProcessorNumberEx routine gets the processor number of the logical processor that the caller is running on. |
| [ReadPointerNoFence function](nf-wdm-readpointernofence~r1.md) | TBD |
| [KeFlushIoRectangle function](nf-wdm-keflushiorectangle.md) | TBD |
| [RtlIntPtrToUnicodeString function](nf-wdm-rtlintptrtounicodestring.md) | The RtlIntPtrToUnicodeString routine converts a specified ULONG_PTR value to a Unicode string that represents the value in a specified base. |
| [ZwDeleteKey function](nf-wdm-zwdeletekey.md) | The ZwDeleteKey routine deletes an open key from the registry. |
| [KeQueryUnbiasedInterruptTime function](nf-wdm-kequeryunbiasedinterrupttime.md) | The KeQueryUnbiasedInterruptTime routine returns the current value of the system interrupt time count. |
| [RtlUshortByteSwap function](nf-wdm-rtlushortbyteswap.md) | The RtlUshortByteSwap routine reverses the ordering of the two bytes in a 16-bit unsigned integer value. |
| [RtlxUnicodeStringToAnsiSize function](nf-wdm-rtlxunicodestringtoansisize.md) | The RtlxUnicodeStringToAnsiSize routine returns the number of bytes required for a null-terminated ANSI string that is equivalent to a specified Unicode string. |
| [KeReleaseSpinLockFromDpcLevel function](nf-wdm-kereleasespinlockfromdpclevel.md) | The KeReleaseSpinLockFromDpcLevel routine releases an executive spin lock without changing the IRQL. |
| [IsEqualGUIDAligned function](nf-wdm-isequalguidaligned~r1.md) | TBD |
| [MmMapIoSpace function](nf-wdm-mmmapiospace.md) | The MmMapIoSpace routine maps the given physical address range to nonpaged system space. |
| [__writefsword function](nf-wdm---writefsword.md) | TBD |
| [KeReadStateEvent function](nf-wdm-kereadstateevent.md) | The KeReadStateEvent routine returns the current state, signaled or not-signaled, of an event object. |
| [FOURTHBYTE function](nf-wdm-fourthbyte.md) | TBD |
| [IoWMIWriteEvent function](nf-wdm-iowmiwriteevent.md) | The IoWMIWriteEvent routine delivers a given event to the user-mode WMI components for notification. |
| [PoRequestPowerIrp function](nf-wdm-porequestpowerirp.md) | The PoRequestPowerIrp routine allocates a power IRP and sends it to the top driver in the device stack for the specified device. |
| [TmRollbackComplete function](nf-wdm-tmrollbackcomplete.md) | The TmRollbackComplete routine notifies KTM that the calling resource manager has finished rolling back a transaction's data. |
| [ClfsWriteRestartArea function](nf-wdm-clfswriterestartarea.md) | The ClfsWriteRestartArea routine atomically appends a new restart record to a CLFS stream, flushes the restart record to stable storage, and optionally updates the base LSN of the stream. |
| [RtlNumberOfSetBits function](nf-wdm-rtlnumberofsetbits.md) | The RtlNumberOfSetBits routine returns a count of the set bits in a given bitmap variable. |
| [RtlUpcaseUnicodeChar function](nf-wdm-rtlupcaseunicodechar.md) | The RtlUpcaseUnicodeChar routine converts the specified Unicode character to uppercase. |
| [ALIGN_UP_POINTER_BY function](nf-wdm-align-up-pointer-by.md) | TBD |
| [RtlStoreUlonglong function](nf-wdm-rtlstoreulonglong.md) | TBD |
| [ClfsLsnRecordSequence function](nf-wdm-clfslsnrecordsequence.md) | The ClfsLsnRecordSequence routine returns the record sequence number contained in a specified LSN. |
| [KeEnterGuardedRegion function](nf-wdm-keenterguardedregion.md) | The KeEnterGuardedRegion routine enters a guarded region, which disables all kernel-mode APC delivery to the current thread. |
| [IMAGE_POLICY_UINT32 function](nf-wdm-image-policy-uint32.md) | TBD |
| [RtlCompareUnicodeStrings function](nf-wdm-rtlcompareunicodestrings.md) | TBD |
| [ClfsScanLogContainers function](nf-wdm-clfsscanlogcontainers.md) | The ClfsScanLogContainers routine retrieves descriptive information for a sequence of containers that belong to a particular CLFS log. |
| [NtCreateResourceManager function](nf-wdm-ntcreateresourcemanager.md) | TBD |
| [READ_REGISTER_ULONG function](nf-wdm-read-register-ulong~r3.md) | The READ_REGISTER_ULONG routine reads a ULONG value from the specified register address. |
| [_bittestandreset64 function](nf-wdm--bittestandreset64.md) | TBD |
| [RtlExtendedMagicDivide function](nf-wdm-rtlextendedmagicdivide~r1.md) | TBD |
| [_InlineBitScanForward64 function](nf-wdm--inlinebitscanforward64.md) | TBD |
| [IoInitializeTimer function](nf-wdm-ioinitializetimer.md) | The IoInitializeTimer routine sets up a driver-supplied IoTimer routine associated with a given device object. |
| [WRITE_PORT_BUFFER_ULONG function](nf-wdm-write-port-buffer-ulong~r3.md) | The WRITE_PORT_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified port address. |
| [IMAGE_POLICY_INT64 function](nf-wdm-image-policy-int64.md) | TBD |
| [READ_REGISTER_NOFENCE_BUFFER_USHORT function](nf-wdm-read-register-nofence-buffer-ushort~r1.md) | TBD |
| [WriteRaw8 function](nf-wdm-writeraw8.md) | TBD |
| [ExInitializeRundownProtectionCacheAwareEx function](nf-wdm-exinitializerundownprotectioncacheawareex.md) | TBD |
| [ZwSetInformationKey function](nf-wdm-zwsetinformationkey.md) | TBD |
| [KeAreApcsDisabled function](nf-wdm-keareapcsdisabled.md) | The KeAreApcsDisabled routine returns whether the calling thread is within a critical region or a guarded region, which disables normal kernel APC delivery. |
| [__incfsdword function](nf-wdm---incfsdword.md) | TBD |
| [InterlockedExchange64 function](nf-wdm-interlockedexchange64.md) | TBD |
| [_InlineInterlockedXor64 function](nf-wdm--inlineinterlockedxor64.md) | TBD |
| [IoFreeErrorLogEntry function](nf-wdm-iofreeerrorlogentry.md) | The IoFreeErrorLogEntry routine frees an unused error log entry. |
| [InterlockedOr function](nf-wdm-interlockedor.md) | The InterlockedOr routine atomically computes a bitwise OR operation. |
| [NT_FRE_ASSERTMSGW function](nf-wdm-nt-fre-assertmsgw.md) | TBD |
| [ReadForWriteAccess function](nf-wdm-readforwriteaccess.md) | TBD |
| [IoUnregisterPlugPlayNotification function](nf-wdm-iounregisterplugplaynotification.md) | This routine is obsolete in Windows 7 and later versions of Windows. For more information, see the following Remarks section.The IoUnregisterPlugPlayNotification routine removes the registration of a driver's callback routine for a PnP event. |
| [FIELD_OFFSET function](nf-wdm-field-offset.md) | The FIELD_OFFSET macro returns the byte offset of a named field in a known structure type. |
| [ZwCreateDirectoryObject function](nf-wdm-zwcreatedirectoryobject.md) | The ZwCreateDirectoryObject routine creates or opens an object-directory object. |
| [RtlLargeIntegerGreaterOrEqualToZero function](nf-wdm-rtllargeintegergreaterorequaltozero.md) | TBD |
| [WRITE_REGISTER_ULONG function](nf-wdm-write-register-ulong~r2.md) | The WRITE_REGISTER_ULONG routine writes a ULONG value to the specified address. |
| [KfRaiseIrql function](nf-wdm-kfraiseirql~r3.md) | TBD |
| [WRITE_REGISTER_BUFFER_ULONG function](nf-wdm-write-register-buffer-ulong~r1.md) | The WRITE_REGISTER_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified register. |
| [ProbeForRead function](nf-wdm-probeforread~r1.md) | The ProbeForRead routine checks that a user-mode buffer actually resides in the user portion of the address space, and is correctly aligned. |
| [DbgPrint function](nf-wdm-dbgprint.md) | The DbgPrint routine sends a message to the kernel debugger. |
| [RtlCheckRegistryKey function](nf-wdm-rtlcheckregistrykey.md) | The RtlCheckRegistryKey routine checks for the existence of a given named key in the registry. |
| [THIRDBYTE function](nf-wdm-thirdbyte.md) | TBD |
| [RtlConvertLongToLargeInteger function](nf-wdm-rtlconvertlongtolargeinteger.md) | The RtlConvertLongToLargeInteger routine converts the input signed integer to a signed large integer. |
| [READ_PORT_BUFFER_UCHAR function](nf-wdm-read-port-buffer-uchar~r3.md) | The READ_PORT_BUFFER_UCHAR routine reads a number of bytes from the specified port address into a buffer. |
| [InterlockedDecrement16 function](nf-wdm-interlockeddecrement16~r1.md) | TBD |
| [ZwWriteFile function](nf-wdm-zwwritefile.md) | The ZwWriteFile routine writes data to an open file. |
| [READ_REGISTER_ULONG function](nf-wdm-read-register-ulong.md) | The READ_REGISTER_ULONG routine reads a ULONG value from the specified register address. |
| [SeSetAuditParameter function](nf-wdm-sesetauditparameter.md) | TBD |
| [__incgsdword function](nf-wdm---incgsdword.md) | TBD |
| [InterlockedXor64 function](nf-wdm-interlockedxor64.md) | TBD |
| [ROUND_TO_PAGES function](nf-wdm-round-to-pages.md) | TBD |
| [RtlFindMostSignificantBit function](nf-wdm-rtlfindmostsignificantbit.md) | The RtlFindMostSignificantBit routine returns the zero-based position of the most significant nonzero bit in its parameter. |
| [KfLowerIrql function](nf-wdm-kflowerirql~r2.md) | TBD |
| [KeSetSystemAffinityThreadEx function](nf-wdm-kesetsystemaffinitythreadex.md) | The KeSetSystemAffinityThreadEx routine sets the system affinity of the current thread. |
| [ExSetResourceOwnerPointerEx function](nf-wdm-exsetresourceownerpointerex.md) | The ExSetResourceOwnerPointerEx routine transfers the ownership of an executive resource from the calling thread to an owner pointer, which is a system address that identifies the resource owner. |
| [READ_PORT_BUFFER_UCHAR function](nf-wdm-read-port-buffer-uchar~r1.md) | The READ_PORT_BUFFER_UCHAR routine reads a number of bytes from the specified port address into a buffer. |
| [ZwCreateTransactionManager function](nf-wdm-zwcreatetransactionmanager.md) | The ZwCreateTransactionManager routine creates a new transaction manager object. |
| [ClfsCloseLogFileObject function](nf-wdm-clfscloselogfileobject.md) | The ClfsCloseLogFileObject routine releases all references to a log file object. |
| [IofCallDriver function](nf-wdm-iofcalldriver.md) | TBD |
| [IoCreateDevice function](nf-wdm-iocreatedevice.md) | The IoCreateDevice routine creates a device object for use by a driver. |
| [WRITE_PORT_BUFFER_USHORT function](nf-wdm-write-port-buffer-ushort~r1.md) | The WRITE_PORT_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified port address. |
| [ZwOpenEvent function](nf-wdm-zwopenevent.md) | The ZwOpenEvent routine opens a handle to an existing named event object with the specified desired access. |
| [RtlLargeIntegerGreaterThanOrEqualTo function](nf-wdm-rtllargeintegergreaterthanorequalto.md) | TBD |
| [ZwQueryValueKey function](nf-wdm-zwqueryvaluekey.md) | The ZwQueryValueKey routine returns a value entry for a registry key. |
| [PoFxCompleteIdleState function](nf-wdm-pofxcompleteidlestate.md) | The PoFxCompleteIdleState routine informs the power management framework (PoFx) that the specified component has completed a pending change to an Fx state. |
| [NtSinglePhaseReject function](nf-wdm-ntsinglephasereject.md) | TBD |
| [RtlUlongByteSwap function](nf-wdm-rtlulongbyteswap~r1.md) | The RtlUlongByteSwap routine reverses the ordering of the four bytes in a 32-bit unsigned integer value. |
| [TmIsTransactionActive function](nf-wdm-tmistransactionactive.md) | The TmIsTransactionActive routine indicates whether a specified transaction is in its active state. |
| [NtOpenTransactionManager function](nf-wdm-ntopentransactionmanager.md) | TBD |
| [ExInitializeNPagedLookasideList_NXPoolOptIn function](nf-wdm-exinitializenpagedlookasidelist-nxpooloptin.md) | TBD |
| [KeSetSystemAffinityThread function](nf-wdm-kesetsystemaffinitythread.md) | The KeSetSystemAffinityThread routine sets the system affinity of the current thread. |
| [__getcallerseflags function](nf-wdm---getcallerseflags.md) | TBD |
| [ExInterlockedExchangeUlong function](nf-wdm-exinterlockedexchangeulong.md) | TBD |
| [IoGetInitialStack function](nf-wdm-iogetinitialstack.md) | The IoGetInitialStack routine returns the base address of the current thread's stack. |
| [ExLocalTimeToSystemTime function](nf-wdm-exlocaltimetosystemtime.md) | The ExLocalTimeToSystemTime routine converts a system time value for the current time zone to an unbiased, GreenGMT value. |
| [WRITE_PORT_UCHAR function](nf-wdm-write-port-uchar~r1.md) | The WRITE_PORT_UCHAR routine writes a byte to the specified port address. |
| [ZwSetInformationTransactionManager function](nf-wdm-zwsetinformationtransactionmanager.md) | TBD |
| [SeLockSubjectContext function](nf-wdm-selocksubjectcontext.md) | TBD |
| [TmRecoverTransactionManager function](nf-wdm-tmrecovertransactionmanager.md) | The TmRecoverTransactionManager routine reconstructs the state of the transaction manager object (including all transactions, enlistments, and resource managers) from the recovery information that is in the log stream. |
| [RtlExtendedLargeIntegerDivide function](nf-wdm-rtlextendedlargeintegerdivide.md) | TBD |
| [ExReleaseSpinLock function](nf-wdm-exreleasespinlock.md) | TBD |
| [READ_REGISTER_USHORT function](nf-wdm-read-register-ushort~r3.md) | The READ_REGISTER_USHORT routine reads a USHORT value from the specified register address. |
| [WRITE_REGISTER_UCHAR function](nf-wdm-write-register-uchar~r2.md) | The WRITE_REGISTER_UCHAR routine writes a byte to the specified address. |
| [IoInitializeIrp function](nf-wdm-ioinitializeirp.md) | The IoInitializeIrp routine initializes a given IRP that was allocated by the caller. |
| [_InlineInterlockedExchangePointer function](nf-wdm--inlineinterlockedexchangepointer.md) | TBD |
| [RtlFillMemory function](nf-wdm-rtlfillmemory.md) | The RtlFillMemory routine fills a block of memory with the specified fill value. |
| [EtwWriteEx function](nf-wdm-etwwriteex.md) | The EtwWriteEx function is a tracing function for publishing events that support filtering in your kernel-mode driver code. |
| [RtlCrc32 function](nf-wdm-rtlcrc32.md) | TBD |
| [IoReleaseRemoveLock function](nf-wdm-ioreleaseremovelock.md) | The IoReleaseRemoveLock routine releases a remove lock acquired with a previous call to IoAcquireRemoveLock. |
| [ObUnRegisterCallbacks function](nf-wdm-obunregistercallbacks.md) | The ObUnRegisterCallbacks routine unregisters a set of callback routines that were registered with the ObRegisterCallbacks routine. |
| [IoWMIOpenBlock function](nf-wdm-iowmiopenblock.md) | The IoWMIOpenBlock routine opens the WMI data block object for the specified WMI class. |
| [InterlockedAnd16 function](nf-wdm-interlockedand16.md) | TBD |
| [ZwRecoverResourceManager function](nf-wdm-zwrecoverresourcemanager.md) | The ZwRecoverResourceManager routine tries to recover the transaction that is associated with each enlistment of a specified resource manager object. |
| [__incfsword function](nf-wdm---incfsword.md) | TBD |
| [WRITE_REGISTER_BUFFER_UCHAR function](nf-wdm-write-register-buffer-uchar~r1.md) | The WRITE_REGISTER_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified register. |
| [WRITE_REGISTER_NOFENCE_UCHAR function](nf-wdm-write-register-nofence-uchar.md) | TBD |
| [KeQueryGroupAffinity function](nf-wdm-kequerygroupaffinity.md) | The KeQueryGroupAffinity routine returns an affinity mask that identifies the active logical processors in a specified group in a multiprocessor system. |
| [ZwClose function](nf-wdm-zwclose.md) | The ZwClose routine closes an object handle. |
| [RtlSetDaclSecurityDescriptor function](nf-wdm-rtlsetdaclsecuritydescriptor.md) | The RtlSetDaclSecurityDescriptor routine sets the DACL information of an absolute-format security descriptor, or if there is already a DACL present in the security descriptor, it is superseded. |
| [InterlockedExchangePointer function](nf-wdm-interlockedexchangepointer.md) | The InterlockedExchangePointer routine performs an atomic operation that sets a pointer to a new value. |
| [InsertHeadList function](nf-wdm-insertheadlist~r1.md) | The InsertHeadList routine inserts an entry at the head of a doubly linked list of LIST_ENTRY structures. |
| [IofCompleteRequest function](nf-wdm-iofcompleterequest.md) | TBD |
| [PrefetchForWrite function](nf-wdm-prefetchforwrite.md) | TBD |
| [ALIGN_DOWN_POINTER_BY function](nf-wdm-align-down-pointer-by.md) | TBD |
| [RtlLargeIntegerLessOrEqualToZero function](nf-wdm-rtllargeintegerlessorequaltozero.md) | TBD |
| [READ_REGISTER_NOFENCE_BUFFER_USHORT function](nf-wdm-read-register-nofence-buffer-ushort.md) | TBD |
| [__movsb function](nf-wdm---movsb.md) | TBD |
| [RtlxAnsiStringToUnicodeSize function](nf-wdm-rtlxansistringtounicodesize.md) | The RtlxAnsiStringToUnicodeSize routine returns the number of bytes that are required for a null-terminated Unicode string that is equivalent to a specified ANSI string. |
| [DEVICE_TYPE_FROM_CTL_CODE function](nf-wdm-device-type-from-ctl-code.md) | TBD |
| [ClfsRemoveLogContainer function](nf-wdm-clfsremovelogcontainer.md) | The ClfsRemoveLogContainer routine removes a container from a CLFS log. |
| [KeQuerySystemTime function](nf-wdm-kequerysystemtime~r1.md) | The KeQuerySystemTime routine obtains the current system time. |
| [RemoveEntryListUnsafe function](nf-wdm-removeentrylistunsafe.md) | TBD |
| [IoCsqInitialize function](nf-wdm-iocsqinitialize.md) | The IoCsqInitialize routine initializes the driver's cancel-safe IRP queue dispatch table. |
| [KeTryToAcquireGuardedMutex function](nf-wdm-ketrytoacquireguardedmutex.md) | The KeTryToAcquireGuardedMutex routine acquires a guarded mutex, if available. |
| [ClfsCreateLogFile function](nf-wdm-clfscreatelogfile.md) | The ClfsCreateLogFile routine creates or opens a CLFS stream. If necessary, ClfsCreateLogFile also creates the underlying physical log that holds the stream's records. |
| [RtlIoDecodeMemIoResource function](nf-wdm-rtliodecodememioresource.md) | The RtlIoDecodeMemIoResource routine provides the address information that is contained in an IO_RESOURCE_DESCRIPTOR structure that describes a range of memory or I/O port addresses. |
| [KeQueryAuxiliaryCounterFrequency function](nf-wdm-kequeryauxiliarycounterfrequency.md) | The KeQueryAuxiliaryCounterFrequency routine returns frequency of the auxiliary counter in units of Hz. |
| [IoGetBootDiskInformationLite function](nf-wdm-iogetbootdiskinformationlite.md) | TBD |
| [KeQueryNodeActiveAffinity function](nf-wdm-kequerynodeactiveaffinity.md) | The KeQueryNodeActiveAffinity routine gets the current processor affinity of a specified node in a multiprocessor system that has a non-uniform memory access (NUMA) architecture. |
| [PsTerminateSystemThread function](nf-wdm-psterminatesystemthread.md) | The PsTerminateSystemThread routine terminates the current system thread. |
| [READ_REGISTER_BUFFER_UCHAR function](nf-wdm-read-register-buffer-uchar.md) | The READ_REGISTER_BUFFER_UCHAR routine reads a number of bytes from the specified register address into a buffer. |
| [WRITE_REGISTER_NOFENCE_BUFFER_ULONG function](nf-wdm-write-register-nofence-buffer-ulong.md) | TBD |
| [ClfsAlignReservedLog function](nf-wdm-clfsalignreservedlog.md) | The ClfsAlignReservedLog routine calculates the size of the space that must be reserved for a specified set of records. The size calculation includes the space required for headers and the space required for sector alignment. |
| [READ_REGISTER_USHORT function](nf-wdm-read-register-ushort~r2.md) | The READ_REGISTER_USHORT routine reads a USHORT value from the specified register address. |
| [ReadAcquire64 function](nf-wdm-readacquire64~r2.md) | TBD |
| [ReadPointerAcquire function](nf-wdm-readpointeracquire~r1.md) | TBD |
| [WRITE_REGISTER_BUFFER_ULONG function](nf-wdm-write-register-buffer-ulong~r3.md) | The WRITE_REGISTER_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified register. |
| [KeSetPriorityThread function](nf-wdm-kesetprioritythread.md) | The KeSetPriorityThread routine sets the run-time priority of a driver-created thread. |
| [ALIGN_DOWN_POINTER function](nf-wdm-align-down-pointer.md) | TBD |
| [__incgsqword function](nf-wdm---incgsqword.md) | TBD |
| [IoConnectInterrupt function](nf-wdm-ioconnectinterrupt.md) | The IoConnectInterrupt routine registers a device driver's InterruptService routine (ISR), so that it will be called when a device interrupts on any of a specified set of processors. |
| [__indwordstring function](nf-wdm---indwordstring.md) | TBD |
| [NtRegisterProtocolAddressInformation function](nf-wdm-ntregisterprotocoladdressinformation.md) | TBD |
| [ExTryAcquireSpinLockExclusiveAtDpcLevel function](nf-wdm-extryacquirespinlockexclusiveatdpclevel.md) | TBD |
| [KeRegisterProcessorChangeCallback function](nf-wdm-keregisterprocessorchangecallback.md) | The KeRegisterProcessorChangeCallback routine registers a callback function with the operating system so that the operating system will notify the driver when a new processor is added to the hardware partition. |
| [SeComputeAutoInheritByObjectType function](nf-wdm-secomputeautoinheritbyobjecttype.md) | TBD |
| [ClfsGetContainerName function](nf-wdm-clfsgetcontainername.md) | The ClfsGetContainerName routine returns the path name of a specified container. |
| [NT_ASSERT_NOASSUME function](nf-wdm-nt-assert-noassume.md) | TBD |
| [RtlLargeIntegerNotEqualTo function](nf-wdm-rtllargeintegernotequalto.md) | TBD |
| [WriteRelease64 function](nf-wdm-writerelease64.md) | TBD |
| [InterlockedIncrement function](nf-wdm-interlockedincrement~r1.md) | The InterlockedIncrement routine increments a caller-supplied variable as an atomic operation. |
| [KeQueryInterruptTimePrecise function](nf-wdm-kequeryinterrupttimeprecise.md) | The KeQueryInterruptTimePrecise routine returns the current value of the system interrupt time count, with accuracy to within a microsecond. |
| [ReadAcquire function](nf-wdm-readacquire~r1.md) | TBD |
| [WriteRelease16 function](nf-wdm-writerelease16.md) | TBD |
| [KeQueryTickCount function](nf-wdm-kequerytickcount.md) | The KeQueryTickCount routine maintains a count of the interval timer interrupts that have occurred since the system was booted. |
| [RtlCmDecodeMemIoResource function](nf-wdm-rtlcmdecodememioresource.md) | The RtlCmDecodeMemIoResource routine provides the starting address and length of a CM_PARTIAL_RESOURCE_DESCRIPTOR structure that describes a range of memory or I/O port addresses. |
| [RtlQueryRegistryValues function](nf-wdm-rtlqueryregistryvalues.md) | The RtlQueryRegistryValues routine allows the caller to query several values from the registry subtree with a single call. |
| [RtlInitUnicodeString function](nf-wdm-rtlinitunicodestring.md) | For more information, see the WdmlibRtlInitUnicodeStringEx function. |
| [MmProtectMdlSystemAddress function](nf-wdm-mmprotectmdlsystemaddress.md) | The MmProtectMdlSystemAddress routine sets the protection type for a memory address range. |
| [IoBuildDeviceIoControlRequest function](nf-wdm-iobuilddeviceiocontrolrequest.md) | The IoBuildDeviceIoControlRequest routine allocates and sets up an IRP for a synchronously processed device control request. |
| [WriteRelease8 function](nf-wdm-writerelease8~r1.md) | TBD |
| [__break function](nf-wdm---break~r1.md) | TBD |
| [WRITE_REGISTER_BUFFER_USHORT function](nf-wdm-write-register-buffer-ushort~r2.md) | The WRITE_REGISTER_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified register. |
| [YieldProcessor function](nf-wdm-yieldprocessor~r1.md) | TBD |
| [ObRegisterCallbacks function](nf-wdm-obregistercallbacks.md) | The ObRegisterCallbacks routine registers a list of callback routines for thread, process, and desktop handle operations. |
| [ExRundownCompleted function](nf-wdm-exrundowncompleted.md) | The ExRundownCompleted routine updates the run-down status of a shared object to indicate that the run down of the object has completed. |
| [PoRegisterPowerSettingCallback function](nf-wdm-poregisterpowersettingcallback.md) | The PoRegisterPowerSettingCallback routine registers a power-setting callback routine to receive notifications of changes in the specified power setting. |
| [ClfsLsnBlockOffset function](nf-wdm-clfslsnblockoffset.md) | The ClfsLsnBlockOffset routine returns the sector-aligned block offset contained in a specified LSN. |
| [MmAllocatePagesForMdl function](nf-wdm-mmallocatepagesformdl.md) | The MmAllocatePagesForMdl routine allocates zero-filled, nonpaged, physical memory pages to an MDL. |
| [InterlockedExchange16 function](nf-wdm-interlockedexchange16~r1.md) | TBD |
| [PoFxSetComponentWake function](nf-wdm-pofxsetcomponentwake.md) | The PoFxSetComponentWake routine indicates whether the driver arms the specified component to wake whenever the component enters the idle condition. |
| [RtlLargeIntegerAnd function](nf-wdm-rtllargeintegerand.md) | TBD |
| [IoSetCancelRoutine function](nf-wdm-iosetcancelroutine.md) | The IoSetCancelRoutine routine sets up a driver-supplied Cancel routine to be called if a given IRP is canceled. |
| [IoReportTargetDeviceChange function](nf-wdm-ioreporttargetdevicechange.md) | The IoReportTargetDeviceChange routine notifies the PnP manager that a custom event has occurred on a device. |
| [PoGetThermalRequestSupport function](nf-wdm-pogetthermalrequestsupport.md) | TBD |
| [ExAllocatePoolWithQuota function](nf-wdm-exallocatepoolwithquota.md) | The ExAllocatePoolWithQuota routine is obsolete, and is exported only for existing driver binaries. Use ExAllocatePoolWithQuotaTag instead.ExAllocatePoolWithQuota allocates pool memory, charging quota against the current process. |
| [WriteNoFence8 function](nf-wdm-writenofence8.md) | TBD |
| [IoAllocateSfioStreamIdentifier function](nf-wdm-ioallocatesfiostreamidentifier.md) | TBD |
| [NtReadOnlyEnlistment function](nf-wdm-ntreadonlyenlistment.md) | TBD |
| [_BitScanForward64 function](nf-wdm--bitscanforward64.md) | TBD |
| [PoSetHiberRange function](nf-wdm-posethiberrange.md) | TBD |
| [READ_REGISTER_BUFFER_UCHAR function](nf-wdm-read-register-buffer-uchar~r2.md) | The READ_REGISTER_BUFFER_UCHAR routine reads a number of bytes from the specified register address into a buffer. |
| [IoBuildPartialMdl function](nf-wdm-iobuildpartialmdl.md) | The IoBuildPartialMdl routine builds a new memory descriptor list (MDL) that represents part of a buffer that is described by an existing MDL. |
| [ExDeletePagedLookasideList function](nf-wdm-exdeletepagedlookasidelist.md) | The ExDeletePagedLookasideList routine destroys a paged lookaside list. |
| [ZwOpenKeyTransactedEx function](nf-wdm-zwopenkeytransactedex.md) | The ZwOpenKeyTransactedEx routine opens an existing registry key and associates the key with a transaction. |
| [WriteNoFence16 function](nf-wdm-writenofence16~r1.md) | TBD |
| [ExReleaseSpinLockShared function](nf-wdm-exreleasespinlockshared.md) | TBD |
| [IoAcquireRemoveLockEx function](nf-wdm-ioacquireremovelockex.md) | TBD |
| [IoIsInitiator32bitProcess function](nf-wdm-ioisinitiator32bitprocess.md) | TBD |
| [ClfsValidTopLevelContext function](nf-wdm-clfsvalidtoplevelcontext.md) | TBD |
| [READ_PORT_ULONG function](nf-wdm-read-port-ulong.md) | The READ_PORT_ULONG routine reads a ULONG value from the specified port address. |
| [ExAcquireResourceSharedLite function](nf-wdm-exacquireresourcesharedlite.md) | The ExAcquireResourceSharedLite routine acquires the given resource for shared access by the calling thread. |
| [KeGetCurrentProcessorIndex function](nf-wdm-kegetcurrentprocessorindex~r1.md) | TBD |
| [KeGetCurrentProcessorIndex function](nf-wdm-kegetcurrentprocessorindex~r3.md) | TBD |
| [RtlStoreUlong function](nf-wdm-rtlstoreulong.md) | TBD |
| [KeFlushIoBuffers function](nf-wdm-keflushiobuffers~r2.md) | The KeFlushIoBuffers routine flushes the memory region described by an MDL from caches of all processors. |
| [ZwCommitComplete function](nf-wdm-zwcommitcomplete.md) | The ZwCommitComplete routine notifies KTM that the calling resource manager has finished committing a transaction's data. |
| [KeInitializeTimer function](nf-wdm-keinitializetimer.md) | The KeInitializeTimer routine initializes a timer object. |
| [InterlockedDecrement function](nf-wdm-interlockeddecrement~r1.md) | The InterlockedDecrement routine decrements a caller-supplied variable of type LONG as an atomic operation. |
| [NtRecoverTransactionManager function](nf-wdm-ntrecovertransactionmanager.md) | TBD |
| [TmEnableCallbacks function](nf-wdm-tmenablecallbacks.md) | The TmEnableCallbacks routine enables a callback routine that receives transaction notifications. |
| [ClfsSetArchiveTail function](nf-wdm-clfssetarchivetail.md) | The ClfsSetArchiveTail routine sets the archive tail of a CLFS log to a specified LSN. |
| [InterlockedXor16 function](nf-wdm-interlockedxor16.md) | TBD |
| [_InterlockedIncrement16 function](nf-wdm--interlockedincrement16.md) | TBD |
| [CmGetBoundTransaction function](nf-wdm-cmgetboundtransaction.md) | The CmGetBoundTransaction routine returns a pointer to the transaction object that represents the transaction, if any, that is associated with a specified registry key object. |
| [EtwWrite function](nf-wdm-etwwrite.md) | The EtwWrite function is a tracing function for publishing events in your kernel-mode driver code. |
| [KeMemoryBarrier function](nf-wdm-kememorybarrier~r2.md) | The KeMemoryBarrier routine creates a barrier at its position in the code&#8212;across which the compiler and the processor cannot move any operations. |
| [KeGetCurrentThread function](nf-wdm-kegetcurrentthread.md) | The KeGetCurrentThread routine identifies the current thread. |
| [ClfsDeleteMarshallingArea function](nf-wdm-clfsdeletemarshallingarea.md) | The ClfsDeleteMarshallingArea routine deletes a marshalling area. |
| [RtlLargeIntegerArithmeticShift function](nf-wdm-rtllargeintegerarithmeticshift.md) | TBD |
| [InsertHeadList function](nf-wdm-insertheadlist.md) | The InsertHeadList routine inserts an entry at the head of a doubly linked list of LIST_ENTRY structures. |
| [IoFreeAdapterChannel function](nf-wdm-iofreeadapterchannel.md) | TBD |
| [__dsb function](nf-wdm---dsb.md) | TBD |
| [WriteUCharNoFence function](nf-wdm-writeucharnofence.md) | TBD |
| [DbgPrintEx function](nf-wdm-dbgprintex.md) | The DbgPrintEx routine sends a string to the kernel debugger if the conditions you specify are met. |
| [WriteBooleanNoFence function](nf-wdm-writebooleannofence.md) | TBD |
| [KeGetProcessorIndexFromNumber function](nf-wdm-kegetprocessorindexfromnumber.md) | The KeGetProcessorIndexFromNumber routine converts a group number and a group-relative processor number to a systemwide processor index. |
| [ZwOpenTransactionManager function](nf-wdm-zwopentransactionmanager.md) | The ZwOpenTransactionManager routine obtains a handle to an existing transaction manager object. |
| [KeFlushIoBuffers function](nf-wdm-keflushiobuffers.md) | The KeFlushIoBuffers routine flushes the memory region described by an MDL from caches of all processors. |
| [RtlClearBit function](nf-wdm-rtlclearbit.md) | The RtlClearBit routine sets the specified bit in a bitmap to zero. |
| [ExSetTimer function](nf-wdm-exsettimer.md) | The ExSetTimer routine starts a timer operation and sets the timer to expire at the specified due time. |
| [RemoveTailList function](nf-wdm-removetaillist.md) | The RemoveTailList routine removes an entry from the end of a doubly linked list of LIST_ENTRY structures. |
| [CmRegisterCallback function](nf-wdm-cmregistercallback.md) | The CmRegisterCallback routine is obsolete for Windows Vista and later operating system versions. Use CmRegisterCallbackEx instead.The CmRegisterCallback routine registers a RegistryCallback routine. |
| [InterlockedOr function](nf-wdm-interlockedor~r1.md) | The InterlockedOr routine atomically computes a bitwise OR operation. |
| [ZwOpenKey function](nf-wdm-zwopenkey.md) | The ZwOpenKey routine opens an existing registry key. |
| [READ_REGISTER_UCHAR function](nf-wdm-read-register-uchar~r2.md) | The READ_REGISTER_UCHAR routine reads a byte from the specified register address. |
| [_ReadWriteBarrier function](nf-wdm--readwritebarrier~r1.md) | TBD |
| [WRITE_PORT_ULONG function](nf-wdm-write-port-ulong~r2.md) | The WRITE_PORT_ULONG routine writes a ULONG value to the specified port address. |
| [MmFreeMappingAddress function](nf-wdm-mmfreemappingaddress.md) | The MmFreeMappingAddress routine frees a range of virtual memory reserved by the MmAllocateMappingAddress routine. |
| [PoFxPowerOnCrashdumpDevice function](nf-wdm-pofxpoweroncrashdumpdevice.md) | TBD |
| [WriteNoFence64 function](nf-wdm-writenofence64~r1.md) | TBD |
| [WRITE_REGISTER_NOFENCE_BUFFER_UCHAR function](nf-wdm-write-register-nofence-buffer-uchar.md) | TBD |
| [ClfsFlushToLsn function](nf-wdm-clfsflushtolsn.md) | The ClfsFlushToLsn routine forces, to stable storage, all records that have an LSN less than or equal to a specified LSN. |
| [IS_DISPATCHING function](nf-wdm-is-dispatching.md) | TBD |
| [ExAcquireRundownProtectionCacheAware function](nf-wdm-exacquirerundownprotectioncacheaware.md) | TBD |
| [WriteRaw64 function](nf-wdm-writeraw64.md) | TBD |
| [RtlxQueryRegistryValues function](nf-wdm-rtlxqueryregistryvalues.md) | TBD |
| [RtlEqualUnicodeString function](nf-wdm-rtlequalunicodestring.md) | The RtlEqualUnicodeString routine compares two Unicode strings to determine whether they are equal. |
| [IMAGE_POLICY_INT16 function](nf-wdm-image-policy-int16.md) | TBD |
| [DbgRaiseAssertionFailure function](nf-wdm-dbgraiseassertionfailure.md) | TBD |
| [MmQuerySystemSize function](nf-wdm-mmquerysystemsize.md) | The MmQuerySystemSize routine returns an estimate of the amount of memory in the system. |
| [KeInitializeDpc function](nf-wdm-keinitializedpc.md) | The KeInitializeDpc routine initializes a DPC object, and registers a CustomDpc routine for that object. |
| [KeGetCurrentIrql function](nf-wdm-kegetcurrentirql~r1.md) | The KeGetCurrentIrql routine returns the current IRQL. |
| [_BitScanReverse function](nf-wdm--bitscanreverse.md) | TBD |
| [READ_PORT_ULONG function](nf-wdm-read-port-ulong~r1.md) | The READ_PORT_ULONG routine reads a ULONG value from the specified port address. |
| [ExFlushLookasideListEx function](nf-wdm-exflushlookasidelistex.md) | The ExFlushLookasideListEx routine flushes all entries from the specified lookaside list and frees the allocated storage for each entry. |
| [IoInvalidateDeviceState function](nf-wdm-ioinvalidatedevicestate.md) | The IoInvalidateDeviceState routine notifies the PnP manager that some aspect of the PnP state of a device has changed. |
| [_InterlockedOr16 function](nf-wdm--interlockedor16.md) | TBD |
| [KeConvertPerformanceCounterToAuxiliaryCounter function](nf-wdm-keconvertperformancecountertoauxiliarycounter.md) | The KeConvertPerformanceCounterToAuxiliaryCounter routine converts the specified performance counter value into an auxiliary counter value. |
| [ExRundownCompletedCacheAware function](nf-wdm-exrundowncompletedcacheaware.md) | TBD |
| [WRITE_REGISTER_BUFFER_ULONG function](nf-wdm-write-register-buffer-ulong.md) | The WRITE_REGISTER_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified register. |
| [PoFxIssueComponentPerfStateChange function](nf-wdm-pofxissuecomponentperfstatechange.md) | The PoFxIssueComponentPerfStateChange routine submits a request to place a device component in a particular performance state. |
| [KeSaveExtendedProcessorState function](nf-wdm-kesaveextendedprocessorstate.md) | The KeSaveExtendedProcessorState routine saves extended processor state information. |
| [LOOKASIDE_CHECK function](nf-wdm-lookaside-check.md) | TBD |
| [ClfsFinalize function](nf-wdm-clfsfinalize.md) | TBD |
| [RtlPrefetchMemoryNonTemporal function](nf-wdm-rtlprefetchmemorynontemporal.md) | The RtlPrefetchMemoryNonTemporal routine provides a hint to the processor that a buffer should be temporarily moved into the processor cache. |
| [KeReadStateMutex function](nf-wdm-kereadstatemutex.md) | The KeReadStateMutex routine returns the current state, signaled or not-signaled, of the specified mutex object. |
| [PoQueryWatchdogTime function](nf-wdm-poquerywatchdogtime.md) | The PoQueryWatchdogTime routine indicates whether the power manager has enabled a watchdog time-out counter for any power IRP that is currently assigned to the device stack. |
| [_m_prefetchw function](nf-wdm--m-prefetchw.md) | TBD |
| [CmRegisterCallbackEx function](nf-wdm-cmregistercallbackex.md) | The CmRegisterCallbackEx routine registers a RegistryCallback routine. |
| [MmGetMdlByteCount function](nf-wdm-mmgetmdlbytecount.md) | TBD |
| [RtlUlonglongByteSwap function](nf-wdm-rtlulonglongbyteswap~r1.md) | The RtlUlonglongByteSwap routine reverses the ordering of the eight bytes in a 64-bit unsigned integer value. |
| [MmGetMdlPfnArray function](nf-wdm-mmgetmdlpfnarray.md) | TBD |
| [RtlCheckBit function](nf-wdm-rtlcheckbit~r1.md) | The RtlCheckBit routine determines whether a particular bit in a given bitmap variable is clear or set. |
| [IoGetDriverObjectExtension function](nf-wdm-iogetdriverobjectextension.md) | The IoGetDriverObjectExtension routine retrieves a previously allocated per-driver context area. |
| [RtlAreBitsClear function](nf-wdm-rtlarebitsclear.md) | The RtlAreBitsClear routine determines whether a given range of bits within a bitmap variable is clear. |
| [MmAllocateContiguousMemorySpecifyCacheNode function](nf-wdm-mmallocatecontiguousmemoryspecifycachenode.md) | TBD |
| [IoGetDeviceNumaNode function](nf-wdm-iogetdevicenumanode.md) | The IoGetDeviceNumaNode routine gets the node number of a device. |
| [__readgsbyte function](nf-wdm---readgsbyte.md) | TBD |
| [InterlockedOr8 function](nf-wdm-interlockedor8.md) | TBD |
| [ARM64_PMXEVCNTRn_EL0 function](nf-wdm-arm64-pmxevcntrn-el0.md) | TBD |
| [IoInitializeRemoveLockEx function](nf-wdm-ioinitializeremovelockex.md) | TBD |
| [NtSetInformationTransactionManager function](nf-wdm-ntsetinformationtransactionmanager.md) | TBD |
| [PushEntryList function](nf-wdm-pushentrylist.md) | The PushEntryList routine inserts an entry at the beginning of a singly linked list of SINGLE_LIST_ENTRY structures. |
| [ExAllocateFromLookasideListEx function](nf-wdm-exallocatefromlookasidelistex.md) | The ExAllocateFromLookasideListEx routine removes the first entry from the specified lookaside list, or, if the list is empty, dynamically allocates the storage for a new entry. |
| [MmGetSystemRoutineAddress function](nf-wdm-mmgetsystemroutineaddress~r1.md) | The MmGetSystemRoutineAddress routine returns a pointer to a function specified by SystemRoutineName. |
| [ClfsMgmtSetLogFileSizeAsClient function](nf-wdm-clfsmgmtsetlogfilesizeasclient.md) | TBD |
| [ReadAcquire16 function](nf-wdm-readacquire16~r2.md) | TBD |
| [ClfsAddLogContainerSet function](nf-wdm-clfsaddlogcontainerset.md) | The ClfsAddLogContainerSet routine atomically adds a set of containers to a CLFS log. |
| [MmAllocatePagesForMdlEx function](nf-wdm-mmallocatepagesformdlex.md) | The MmAllocatePagesForMdlEx routine allocates nonpaged, physical memory pages to an MDL. |
| [ReadNoFence64 function](nf-wdm-readnofence64.md) | TBD |
| [KeSetTimer function](nf-wdm-kesettimer.md) | The KeSetTimer routine sets the absolute or relative interval at which a timer object is to be set to a signaled state and, optionally, supplies a CustomTimerDpc routine to be executed when that interval expires. |
| [_InterlockedCompareExchange16 function](nf-wdm--interlockedcompareexchange16.md) | TBD |
| [NT_ASSERTMSG_ACTION function](nf-wdm-nt-assertmsg-action.md) | TBD |
| [RtlAppendUnicodeStringToString function](nf-wdm-rtlappendunicodestringtostring.md) | The RtlAppendUnicodeStringToString routine concatenates two Unicode strings. |
| [ZwGetNotificationResourceManager function](nf-wdm-zwgetnotificationresourcemanager.md) | The ZwGetNotificationResourceManager routine retrieves the next transaction notification from a specified resource manager's notification queue. |
| [ReadNoFence function](nf-wdm-readnofence~r1.md) | TBD |
| [PoFxIdleComponent function](nf-wdm-pofxidlecomponent.md) | The PoFxIdleComponent routine decrements the activation reference count on the specified component. |
| [IMAGE_POLICY_UINT16 function](nf-wdm-image-policy-uint16.md) | TBD |
| [IoCsqInsertIrp function](nf-wdm-iocsqinsertirp.md) | The IoCsqInsertIrp routine inserts an IRP in the driver's cancel-safe IRP queue. |
| [IoCsqRemoveNextIrp function](nf-wdm-iocsqremovenextirp.md) | The IoCsqRemoveNextIrp routine removes the next matching IRP in the queue. |
| [ExInterlockedPopEntryList function](nf-wdm-exinterlockedpopentrylist.md) | The ExInterlockedPopEntryList routine atomically removes an entry from the beginning of a singly linked list of SINGLE_LIST_ENTRY structures. |
| [KeInitializeCrashDumpHeader function](nf-wdm-keinitializecrashdumpheader.md) | The KeInitializeCrashDumpHeader routine supplies the header information the system requires for a crash dump file. |
| [_byteswap_uint64 function](nf-wdm--byteswap-uint64.md) | TBD |
| [ZwRollbackComplete function](nf-wdm-zwrollbackcomplete.md) | The ZwRollbackComplete routine notifies KTM that the calling resource manager has finished rolling back a transaction's data. |
| [PoFxIssueComponentPerfStateChangeMultiple function](nf-wdm-pofxissuecomponentperfstatechangemultiple.md) | The PoFxIssueComponentPerfStateChangeMultiple routine submits a request to change the performance states in multiple performance state sets simultaneously for a device component. |
| [ZwSaveKey function](nf-wdm-zwsavekey.md) | TBD |
| [LOOKASIDE_CHECK function](nf-wdm-lookaside-check~r3.md) | TBD |
| [READ_REGISTER_BUFFER_USHORT function](nf-wdm-read-register-buffer-ushort.md) | The READ_REGISTER_BUFFER_USHORT routine reads a number of USHORT values from the specified register address into a buffer. |
| [RtlLargeIntegerShiftRight function](nf-wdm-rtllargeintegershiftright.md) | TBD |
| [WRITE_PORT_BUFFER_USHORT function](nf-wdm-write-port-buffer-ushort~r2.md) | The WRITE_PORT_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified port address. |
| [RTL_SOFT_VERIFY function](nf-wdm-rtl-soft-verify.md) | TBD |
| [InterlockedExchangeAdd function](nf-wdm-interlockedexchangeadd.md) | The InterlockedExchangeAdd routine adds a value to a given integer as an atomic operation and returns the original value of the given integer. |
| [WRITE_PORT_BUFFER_ULONG function](nf-wdm-write-port-buffer-ulong~r1.md) | The WRITE_PORT_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified port address. |
| [InterlockedXor function](nf-wdm-interlockedxor~r1.md) | The InterlockedOr routine atomically computes a bitwise exclusive OR operation. |
| [MmGetProcedureAddress function](nf-wdm-mmgetprocedureaddress.md) | TBD |
| [ExDeleteNPagedLookasideList function](nf-wdm-exdeletenpagedlookasidelist.md) | The ExDeleteNPagedLookasideList routine destroys a nonpaged lookaside list. |
| [KeAreAllApcsDisabled function](nf-wdm-keareallapcsdisabled.md) | The KeAreAllApcsDisabled routine indicates whether the calling thread is inside a guarded region or running at IRQL &gt;= APC_LEVEL, which disables all APC delivery. |
| [FIELD_SIZE function](nf-wdm-field-size.md) | TBD |
| [NtSetInformationResourceManager function](nf-wdm-ntsetinformationresourcemanager.md) | TBD |
| [WriteULong64Release function](nf-wdm-writeulong64release.md) | TBD |
| [ZwCreateSection function](nf-wdm-zwcreatesection.md) | The ZwCreateSection routine creates a section object. |
| [ObReferenceObjectSafe function](nf-wdm-obreferenceobjectsafe.md) | TBD |
| [RemoveTailList function](nf-wdm-removetaillist~r1.md) | The RemoveTailList routine removes an entry from the end of a doubly linked list of LIST_ENTRY structures. |
| [KfLowerIrql function](nf-wdm-kflowerirql~r1.md) | TBD |
| [ZwCommitRegistryTransaction function](nf-wdm-zwcommitregistrytransaction.md) | TBD |
| [READ_REGISTER_UCHAR function](nf-wdm-read-register-uchar~r1.md) | The READ_REGISTER_UCHAR routine reads a byte from the specified register address. |
| [__writegsqword function](nf-wdm---writegsqword.md) | TBD |
| [ExSetResourceOwnerPointer function](nf-wdm-exsetresourceownerpointer.md) | The ExSetResourceOwnerPointer routine sets the owner thread pointer for an executive resource. |
| [InterlockedDecrement16 function](nf-wdm-interlockeddecrement16.md) | TBD |
| [KeInsertDeviceQueue function](nf-wdm-keinsertdevicequeue.md) | The KeInsertDeviceQueue routine acquires the spin lock for the specified device queue object and, if the device queue is set to a busy state, queues the specified entry. |
| [LOOKASIDE_CHECK function](nf-wdm-lookaside-check~r1.md) | TBD |
| [__readgsdword function](nf-wdm---readgsdword.md) | TBD |
| [RtlTestBit function](nf-wdm-rtltestbit.md) | The RtlTestBit routine returns the value of a bit in a bitmap. |
| [IoReleaseRemoveLockAndWait function](nf-wdm-ioreleaseremovelockandwait.md) | The IoReleaseRemoveLockAndWait routine releases a remove lock that the driver acquired in a previous call to IoAcquireRemoveLock, and waits until all acquisitions of the lock have been released. |
| [RtlIsUntrustedObject function](nf-wdm-rtlisuntrustedobject.md) | TBD |
| [WRITE_REGISTER_NOFENCE_BUFFER_USHORT function](nf-wdm-write-register-nofence-buffer-ushort~r1.md) | TBD |
| [__addfsword function](nf-wdm---addfsword.md) | TBD |
| [_interlockedbittestandset function](nf-wdm--interlockedbittestandset.md) | TBD |
| [IoInitializeDpcRequest function](nf-wdm-ioinitializedpcrequest.md) | The IoInitializeDpcRequest routine registers a driver-supplied DpcForIsr routine. |
| [KeRemoveQueueDpcEx function](nf-wdm-keremovequeuedpcex.md) | TBD |
| [ExInitializeDriverRuntime function](nf-wdm-exinitializedriverruntime.md) | TBD |
| [__incgsbyte function](nf-wdm---incgsbyte.md) | TBD |
| [WRITE_PORT_ULONG function](nf-wdm-write-port-ulong~r1.md) | The WRITE_PORT_ULONG routine writes a ULONG value to the specified port address. |
| [MmMapMdl function](nf-wdm-mmmapmdl.md) | This function maps physical pages described by a memory descriptor list (MDL) into the system virtual address space. |
| [RtlInterlockedXorBits function](nf-wdm-rtlinterlockedxorbits.md) | TBD |
| [RtlInitStringEx function](nf-wdm-rtlinitstringex.md) | The RtlInitStringEx routine initializes a counted string of 8-bit characters. |
| [READ_REGISTER_BUFFER_USHORT function](nf-wdm-read-register-buffer-ushort~r2.md) | The READ_REGISTER_BUFFER_USHORT routine reads a number of USHORT values from the specified register address into a buffer. |
| [RtlFindClosestEncodableLength function](nf-wdm-rtlfindclosestencodablelength.md) | TBD |
| [IoRegisterShutdownNotification function](nf-wdm-ioregistershutdownnotification.md) | The IoRegisterShutdownNotification routine registers the driver to receive an IRP_MJ_SHUTDOWN IRP when the system is shut down. |
| [IoReleaseRemoveLockAndWaitEx function](nf-wdm-ioreleaseremovelockandwaitex.md) | TBD |
| [RtlCopyMemoryNonTemporal function](nf-wdm-rtlcopymemorynontemporal.md) | TBD |
| [NT_VERIFY function](nf-wdm-nt-verify.md) | TBD |
| [RtlFindLongestRunClear function](nf-wdm-rtlfindlongestrunclear.md) | The RtlFindLongestRunClear routine searches for the largest contiguous range of clear bits within a given bitmap. |
| [_InlineBitScanReverse64 function](nf-wdm--inlinebitscanreverse64.md) | TBD |
| [ExReleaseSpinLockFromDpcLevel function](nf-wdm-exreleasespinlockfromdpclevel.md) | TBD |
| [InterlockedDecrementSizeT function](nf-wdm-interlockeddecrementsizet.md) | TBD |
| [NtRecoverEnlistment function](nf-wdm-ntrecoverenlistment.md) | TBD |
| [IoSetTopLevelIrp function](nf-wdm-iosettoplevelirp.md) | TBD |
| [ASSERT_DPC function](nf-wdm-assert-dpc.md) | TBD |
| [KeSynchronizeExecution function](nf-wdm-kesynchronizeexecution.md) | The KeSynchronizeExecution routine synchronizes the execution of the specified routine with the interrupt service routine (ISR) that is assigned to a set of one or more interrupt objects. |
| [MmMapLockedPagesSpecifyCache function](nf-wdm-mmmaplockedpagesspecifycache.md) | The MmMapLockedPagesSpecifyCache routine maps the physical pages that are described by an MDL to a virtual address, and enables the caller to specify the cache attribute that is used to create the mapping. |
| [WRITE_REGISTER_NOFENCE_BUFFER_ULONG function](nf-wdm-write-register-nofence-buffer-ulong~r1.md) | TBD |
| [WriteUShortNoFence function](nf-wdm-writeushortnofence.md) | TBD |
| [NtOpenTransaction function](nf-wdm-ntopentransaction.md) | TBD |
| [NtOpenEnlistment function](nf-wdm-ntopenenlistment.md) | TBD |
| [NtRollbackTransaction function](nf-wdm-ntrollbacktransaction.md) | TBD |
| [MmAddVerifierSpecialThunks function](nf-wdm-mmaddverifierspecialthunks.md) | TBD |
| [InvalidatePage function](nf-wdm-invalidatepage.md) | TBD |
| [KeInitializeGuardedMutex function](nf-wdm-keinitializeguardedmutex.md) | The KeInitializeGuardedMutex routine initializes a guarded mutex. |
| [ReadUShortNoFence function](nf-wdm-readushortnofence.md) | TBD |
| [ZwUnmapViewOfSection function](nf-wdm-zwunmapviewofsection.md) | The ZwUnmapViewOfSection routine unmaps a view of a section from the virtual address space of a subject process. |
| [IoWMIQuerySingleInstance function](nf-wdm-iowmiquerysingleinstance.md) | The IoWMIQuerySingleInstance routine returns the specified instance of a WMI data block. |
| [KeMemoryBarrier function](nf-wdm-kememorybarrier~r1.md) | The KeMemoryBarrier routine creates a barrier at its position in the code&#8212;across which the compiler and the processor cannot move any operations. |
| [ReadPointerRaw function](nf-wdm-readpointerraw~r1.md) | TBD |
| [ObGetFilterVersion function](nf-wdm-obgetfilterversion.md) | TBD |
| [WRITE_REGISTER_NOFENCE_ULONG64 function](nf-wdm-write-register-nofence-ulong64.md) | TBD |
| [KeQueryLogicalProcessorRelationship function](nf-wdm-kequerylogicalprocessorrelationship.md) | The KeQueryLogicalProcessorRelationship routine gets information about the relationships of one or more processors to the other processors in a multiprocessor system. |
| [ExFreePoolWithTag function](nf-wdm-exfreepoolwithtag.md) | The ExFreePoolWithTag routine deallocates a block of pool memory allocated with the specified tag. |
| [READ_PORT_BUFFER_USHORT function](nf-wdm-read-port-buffer-ushort~r1.md) | The READ_PORT_BUFFER_USHORT routine reads a number of USHORT values from the specified port address into a buffer. |
| [PcwCreateInstance function](nf-wdm-pcwcreateinstance.md) | The PcwCreateInstance function creates a new instance for the specified registered counter set. |
| [NtOpenRegistryTransaction function](nf-wdm-ntopenregistrytransaction.md) | TBD |
| [ExAcquireResourceExclusiveLite function](nf-wdm-exacquireresourceexclusivelite.md) | The ExAcquireResourceExclusiveLite routine acquires the given resource for exclusive access by the calling thread. |
| [ZwSetInformationTransaction function](nf-wdm-zwsetinformationtransaction.md) | The ZwSetInformationTransaction routine sets information for a specified transaction. |
| [WritePointerRaw function](nf-wdm-writepointerraw.md) | TBD |
| [ExFreePool function](nf-wdm-exfreepool.md) | The ExFreePool routine deallocates a block of pool memory. |
| [ZwRecoverEnlistment function](nf-wdm-zwrecoverenlistment.md) | The ZwRecoverEnlistment routine initiates a recovery operation for the transaction that is associated with a specified enlistment. |
| [WriteRelease function](nf-wdm-writerelease~r2.md) | TBD |
| [ExNotifyCallback function](nf-wdm-exnotifycallback.md) | The ExNotifyCallback routine causes all callback routines registered for the given object to be called. |
| [RtlValidSecurityDescriptor function](nf-wdm-rtlvalidsecuritydescriptor.md) | The RtlValidSecurityDescriptor routine checks a given security descriptor's validity. |
| [NtRecoverResourceManager function](nf-wdm-ntrecoverresourcemanager.md) | TBD |
| [ExWaitForRundownProtectionRelease function](nf-wdm-exwaitforrundownprotectionrelease.md) | The ExWaitForRundownProtectionRelease routine waits until all drivers that have already been granted run-down protection complete their accesses of the shared object. |
| [ExQueueWorkItem function](nf-wdm-exqueueworkitem.md) | ExQueueWorkItem inserts a given work item into a queue from which a system worker thread removes the item and gives control to the routine that the caller supplied to ExInitializeWorkItem. |
| [RtlNumberOfClearBits function](nf-wdm-rtlnumberofclearbits.md) | The RtlNumberOfClearBits routine returns a count of the clear bits in a given bitmap variable. |
| [ExReleaseRundownProtectionCacheAware function](nf-wdm-exreleaserundownprotectioncacheaware.md) | TBD |
| [IS_VALIDATION_ENABLED function](nf-wdm-is-validation-enabled.md) | TBD |
| [PoCreateThermalRequest function](nf-wdm-pocreatethermalrequest.md) | TBD |
| [ExpInterlockedFlushSList function](nf-wdm-expinterlockedflushslist.md) | TBD |
| [IoFreeSfioStreamIdentifier function](nf-wdm-iofreesfiostreamidentifier.md) | TBD |
| [WRITE_PORT_BUFFER_UCHAR function](nf-wdm-write-port-buffer-uchar~r1.md) | The WRITE_PORT_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified port. |
| [IoFreeMdl function](nf-wdm-iofreemdl.md) | The IoFreeMdl routine releases a caller-allocated memory descriptor list (MDL). |
| [ClfsAllocReservedLog function](nf-wdm-clfsallocreservedlog.md) | The ClfsAllocReservedLog routine reserves space in a marshalling area for a set of records. |
| [ExInterlockedPopEntrySList function](nf-wdm-exinterlockedpopentryslist~r2.md) | The ExInterlockedPopEntrySList routine atomically removes the first entry from a sequenced singly linked list. |
| [KeFlushIoBuffers function](nf-wdm-keflushiobuffers~r4.md) | The KeFlushIoBuffers routine flushes the memory region described by an MDL from caches of all processors. |
| [KeRestoreFloatingPointState function](nf-wdm-kerestorefloatingpointstate~r3.md) | The KeRestoreFloatingPointState routine restores the nonvolatile floating-point context saved by the preceding call to KeSaveFloatingPointState. |
| [IoGetRelatedDeviceObject function](nf-wdm-iogetrelateddeviceobject.md) | Given a file object, the IoGetRelatedDeviceObject routine returns a pointer to the corresponding device object. |
| [DbgRaiseAssertionFailure function](nf-wdm-dbgraiseassertionfailure~r1.md) | TBD |
| [ExUnregisterCallback function](nf-wdm-exunregistercallback.md) | The ExUnregisterCallback routine removes a callback routine previously registered with a callback object from the list of routines to be called during the notification process. |
| [KeFlushIoBuffers function](nf-wdm-keflushiobuffers~r1.md) | The KeFlushIoBuffers routine flushes the memory region described by an MDL from caches of all processors. |
| [ExReinitializeResourceLite function](nf-wdm-exreinitializeresourcelite.md) | The ExReinitializeResourceLite routine reinitializes an existing resource variable. |
| [WritePointerRelease function](nf-wdm-writepointerrelease.md) | TBD |
| [KeFlushQueuedDpcs function](nf-wdm-keflushqueueddpcs.md) | The KeFlushQueuedDpcs routine returns after all queued DPCs on all processors have executed. |
| [RtlFreeAnsiString function](nf-wdm-rtlfreeansistring.md) | The RtlFreeAnsiString routine releases storage that was allocated by RtlUnicodeStringToAnsiString. |
| [AppendTailList function](nf-wdm-appendtaillist~r1.md) | The AppendTailList routine appends a doubly linked list of LIST_ENTRY structures to the tail of another doubly linked list of LIST_ENTRY structures. |
| [KeSaveFloatingPointState function](nf-wdm-kesavefloatingpointstate~r2.md) | The KeSaveFloatingPointState routine saves the nonvolatile floating-point context so the caller can carry out floating-point operations. |
| [ExInitializeRundownProtectionCacheAware function](nf-wdm-exinitializerundownprotectioncacheaware.md) | TBD |
| [RtlInt64ToUnicodeString function](nf-wdm-rtlint64tounicodestring.md) | The RtlInt64ToUnicodeString routine converts a specified unsigned 64-bit integer value to a Unicode string that represents the value in a specified base. |
| [MmBuildMdlForNonPagedPool function](nf-wdm-mmbuildmdlfornonpagedpool.md) | The MmBuildMdlForNonPagedPool routine receives an MDL that specifies a nonpaged virtual memory buffer, and updates it to describe the underlying physical pages. |
| [IoGetIoAttributionHandle function](nf-wdm-iogetioattributionhandle.md) | TBD |
| [__writegsword function](nf-wdm---writegsword.md) | TBD |
| [KeQuerySystemTime function](nf-wdm-kequerysystemtime.md) | The KeQuerySystemTime routine obtains the current system time. |
| [PoSetSystemState function](nf-wdm-posetsystemstate.md) | Drivers call the PoSetSystemState routine to indicate that the system is active. |
| [RtlCreateSecurityDescriptor function](nf-wdm-rtlcreatesecuritydescriptor.md) | The RtlCreateSecurityDescriptor routine initializes a new absolute-format security descriptor. On return, the security descriptor is initialized with no system ACL, no discretionary ACL, no owner, no primary group, and all control flags set to zero. |
| [MmMdlPageContentsState function](nf-wdm-mmmdlpagecontentsstate.md) | TBD |
| [_interlockedbittestandset64 function](nf-wdm--interlockedbittestandset64.md) | TBD |
| [RtlInitAnsiString function](nf-wdm-rtlinitansistring.md) | The RtlInitAnsiString routine initializes a counted string of ANSI characters. |
| [ReadNoFence64 function](nf-wdm-readnofence64~r2.md) | TBD |
| [MmGetSystemRoutineAddress function](nf-wdm-mmgetsystemroutineaddress.md) | The MmGetSystemRoutineAddress routine returns a pointer to a function specified by SystemRoutineName. |
| [IoQueueWorkItem function](nf-wdm-ioqueueworkitem.md) | The IoQueueWorkItem routine associates a WorkItem routine with a work item, and it inserts the work item into a queue for later processing by a system worker thread. |
| [ExRegisterCallback function](nf-wdm-exregistercallback.md) | The ExRegisterCallback routine registers a given callback routine with a given callback object. |
| [WRITE_PORT_BUFFER_UCHAR function](nf-wdm-write-port-buffer-uchar~r3.md) | The WRITE_PORT_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified port. |
| [operator== function](nf-wdm-operator==.md) | TBD |
| [READ_REGISTER_UCHAR function](nf-wdm-read-register-uchar.md) | The READ_REGISTER_UCHAR routine reads a byte from the specified register address. |
| [ClfsMgmtInstallPolicy function](nf-wdm-clfsmgmtinstallpolicy.md) | The ClfsMgmtInstallPolicy routine adds a CLFS_MGMT_POLICY structure to a physical log. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [EX_TIMER structure](ns-wdm--ex-timer.md) | TBD |
| [PROCESSOR_RELATIONSHIP structure](ns-wdm--processor-relationship.md) | TBD |
| [FILE_SEGMENT_ELEMENT structure](ns-wdm--file-segment-element.md) | TBD |
| [OB_PRE_OPERATION_PARAMETERS structure](ns-wdm--ob-pre-operation-parameters.md) | The OB_PRE_OPERATION_PARAMETERS union describes the operation-specific parameters for an ObjectPreCallback routine. |
| [OB_OPERATION_REGISTRATION structure](ns-wdm--ob-operation-registration.md) | The OB_OPERATION_REGISTRATION structure specifies ObjectPreCallback and ObjectPostCallback callback routines and the types of operations that the routines are called for. |
| [PCI_PMC structure](ns-wdm--pci-pmc.md) | The PCI_PMC structure is used to report the contents of the power management capabilities register. |
| [PCI_EXPRESS_ERROR_SOURCE_ID structure](ns-wdm--pci-express-error-source-id.md) | The PCI_EXPRESS_ERROR_SOURCE_ID structure describes the identifiers of the first correctable error and the first uncorrectable error that are reported in the PCI Express (PCIe) root error status register. |
| [EXCEPTION_RECORD32 structure](ns-wdm--exception-record32.md) | TBD |
| [DEVICE_RESET_INTERFACE_STANDARD structure](ns-wdm--device-reset-interface-standard.md) | The DEVICE_RESET_INTERFACE_STANDARD structure enables function drivers to reset and recover malfunctioning devices. This structure describes the GUID_DEVICE_RESET_INTERFACE_STANDARD interface. |
| [DMA_OPERATIONS structure](ns-wdm--dma-operations.md) | TBD |
| [PCI_EXPRESS_ACS_CONTROL structure](ns-wdm--pci-express-acs-control.md) | TBD |
| [POWER_IDLE_RESILIENCY structure](ns-wdm--power-idle-resiliency.md) | TBD |
| [SYSTEM_LOGICAL_PROCESSOR_INFORMATION structure](ns-wdm--system-logical-processor-information.md) | TBD |
| [CM_Power_Data_s structure](ns-wdm-cm-power-data-s.md) | The CM_POWER_DATA structure contains information about a device's power management state and capabilities. |
| [VIRTUAL_RESOURCE_CAPABILITY structure](ns-wdm--virtual-resource-capability.md) | TBD |
| [Overlay structure](ns-wdm-overlay.md) | TBD |
| [FILE_FULL_EA_INFORMATION structure](ns-wdm--file-full-ea-information.md) | The FILE_FULL_EA_INFORMATION structure provides extended attribute (EA) information. This structure is used primarily by network drivers. |
| [KBUGCHECK_REASON_CALLBACK_RECORD structure](ns-wdm--kbugcheck-reason-callback-record.md) | TBD |
| [REG_QUERY_KEY_SECURITY_INFORMATION structure](ns-wdm--reg-query-key-security-information.md) | The REG_QUERY_KEY_SECURITY_INFORMATION structure receives security information for a registry key object. |
| [OB_CALLBACK_REGISTRATION structure](ns-wdm--ob-callback-registration.md) | The OB_CALLBACK_REGISTRATION structure specifies the parameters when the ObRegisterCallbacks routine registers ObjectPreCallback and ObjectPostCallback callback routines. |
| [RTL_BITMAP_RUN structure](ns-wdm--rtl-bitmap-run.md) | TBD |
| [REG_UNLOAD_KEY_INFORMATION structure](ns-wdm--reg-unload-key-information.md) | The REG_UNLOAD_KEY_INFORMATION structure contains information that a driver's RegistryCallback routine can use when a registry hive is unloaded. |
| [PCW_COUNTER_DESCRIPTOR structure](ns-wdm--pcw-counter-descriptor.md) | The PCW_COUNTER_DESCRIPTOR structure supplies details about the notification to send. |
| [ENLISTMENT_BASIC_INFORMATION structure](ns-wdm--enlistment-basic-information.md) | The ENLISTMENT_BASIC_INFORMATION structure contains information about an enlistment object. |
| [REG_SET_INFORMATION_KEY_INFORMATION structure](ns-wdm--reg-set-information-key-information.md) | The REG_SET_INFORMATION_KEY_INFORMATION structure describes a new setting for a key's metadata. |
| [PRIVILEGE_SET structure](ns-wdm--privilege-set.md) | The PRIVILEGE_SET structure specifies a set of security privileges. For more information, see the reference page for PRIVILEGE_SET in the Microsoft Windows SDK documentation. |
| [KEY_SET_VIRTUALIZATION_INFORMATION structure](ns-wdm--key-set-virtualization-information.md) | TBD |
| [POWER_SESSION_WINLOGON structure](ns-wdm--power-session-winlogon.md) | TBD |
| [FAST_MUTEX structure](ns-wdm--fast-mutex.md) | TBD |
| [SCSI_REQUEST_BLOCK structure](ns-wdm--scsi-request-block.md) | TBD |
| [EX_RUNDOWN_REF_CACHE_AWARE structure](ns-wdm--ex-rundown-ref-cache-aware.md) | TBD |
| [INTEL_CACHE_INFO_EBX structure](ns-wdm-intel-cache-info-ebx.md) | TBD |
| [ADAPTER_OBJECT structure](ns-wdm--adapter-object.md) | TBD |
| [DEVICE_OBJECT structure](ns-wdm--device-object~r3.md) | TBD |
| [FUNCTION_LEVEL_DEVICE_RESET_PARAMETERS structure](ns-wdm--function-level-device-reset-parameters.md) | The FUNCTION_LEVEL_DEVICE_RESET_PARAMETER structure is used as an argument to the DeviceReset routine of the GUID_DEVICE_RESET_INTERFACE_STANDARD interface. |
| [SE_ADT_CLAIMS structure](ns-wdm--se-adt-claims.md) | TBD |
| [ENLISTMENT_CRM_INFORMATION structure](ns-wdm--enlistment-crm-information.md) | TBD |
| [TRANSACTIONMANAGER_RECOVERY_INFORMATION structure](ns-wdm--transactionmanager-recovery-information.md) | The TRANSACTIONMANAGER_RECOVERY_INFORMATION structure contains information about a transaction manager object. |
| [ACCESS_STATE structure](ns-wdm--access-state.md) | The ACCESS_STATE structure describes the state of an access in progress. |
| [REG_SAVE_KEY_INFORMATION structure](ns-wdm--reg-save-key-information.md) | The REG_SAVE_KEY_INFORMATION structure contains the information for a registry key that is about to be saved. |
| [PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER structure](ns-wdm--pci-express-enhanced-capability-header.md) | The PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER structure describes the header for a PCI Express (PCIe) extended capability structure. |
| [TRANSACTION_BIND_INFORMATION structure](ns-wdm--transaction-bind-information.md) | TBD |
| [POWER_USER_PRESENCE structure](ns-wdm--power-user-presence.md) | TBD |
| [PCI_DEVICE_PRESENT_INTERFACE structure](ns-wdm--pci-device-present-interface.md) | The PCI_DEVICE_PRESENT_INTERFACE structure is reserved for system use. |
| [EXCEPTION_RECORD64 structure](ns-wdm--exception-record64.md) | TBD |
| [PCI_PM_CAPABILITY structure](ns-wdm--pci-pm-capability.md) | The PCI_PM_CAPABILITY structure reports the power management capabilities of the device. |
| [RESOURCEMANAGER_COMPLETION_INFORMATION structure](ns-wdm--resourcemanager-completion-information.md) | The RESOURCEMANAGER_COMPLETION_INFORMATION structure is not used. |
| [DPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK structure](ns-wdm--dpc-watchdog-global-triage-block.md) | TBD |
| [KDEVICE_QUEUE structure](ns-wdm--kdevice-queue.md) | TBD |
| [REENUMERATE_SELF_INTERFACE_STANDARD structure](ns-wdm--reenumerate-self-interface-standard.md) | The REENUMERATE_SELF_INTERFACE_STANDARD interface structure enables a driver to request that its parent bus driver reenumerate the driver's device. This structure defines the GUID_REENUMERATE_SELF_INTERFACE_STANDARD interface. |
| [FILE_IOSTATUSBLOCK_RANGE_INFORMATION structure](ns-wdm--file-iostatusblock-range-information.md) | TBD |
| [PCI_PMCSR_BSE structure](ns-wdm--pci-pmcsr-bse.md) | The PCI_PMCSR_BSE structure is used to report the contents of the power management control status register for PCI bridge support extensions. |
| [DRIVE_LAYOUT_INFORMATION structure](ns-wdm--drive-layout-information.md) | TBD |
| [REG_REPLACE_KEY_INFORMATION structure](ns-wdm--reg-replace-key-information.md) | The REG_REPLACE_KEY_INFORMATION structure describes the metadata that is about to be replaced for a key. |
| [IO_CONNECT_INTERRUPT_FULLY_SPECIFIED_PARAMETERS structure](ns-wdm--io-connect-interrupt-fully-specified-parameters.md) | TBD |
| [DEVICE_DESCRIPTION structure](ns-wdm--device-description.md) | TBD |
| [KLOCK_QUEUE_HANDLE structure](ns-wdm--klock-queue-handle.md) | TBD |
| [SYSTEM_CPU_SET_INFORMATION structure](ns-wdm--system-cpu-set-information~r1.md) | TBD |
| [PNP_REPLACE_DRIVER_INTERFACE structure](ns-wdm--pnp-replace-driver-interface~r1.md) | TBD |
| [TARGET_DEVICE_CUSTOM_NOTIFICATION structure](ns-wdm--target-device-custom-notification.md) | The TARGET_DEVICE_CUSTOM_NOTIFICATION structure describes a custom device event. |
| [PCI_EXPRESS_VENDOR_SPECIFIC_CAPABILITY structure](ns-wdm--pci-express-vendor-specific-capability.md) | TBD |
| [PCW_INSTANCE structure](ns-wdm--pcw-instance.md) | TBD |
| [TRANSACTIONMANAGER_LOGPATH_INFORMATION structure](ns-wdm--transactionmanager-logpath-information.md) | The TRANSACTIONMANAGER_LOGPATH_INFORMATION structure contains information about a transaction manager object. |
| [REG_CREATE_KEY_INFORMATION_V1 structure](ns-wdm--reg-create-key-information-v1.md) | The REG_OPEN_KEY_INFORMATION_V1 structure contains information that a filter driver's RegistryCallback routine can use when a registry key is being opened. |
| [DEVOBJ_EXTENSION structure](ns-wdm--devobj-extension.md) | TBD |
| [VIRTUAL_CHANNEL_CONTROL structure](ns-wdm--virtual-channel-control.md) | TBD |
| [DEVICE_DESCRIPTION structure](ns-wdm--device-description~r1.md) | The DEVICE_DESCRIPTION structure describes the attributes of the physical device for which a driver is requesting a DMA adapter. |
| [DRIVER_OBJECT structure](ns-wdm--driver-object~r2.md) | TBD |
| [TARGET_DEVICE_REMOVAL_NOTIFICATION structure](ns-wdm--target-device-removal-notification.md) | The TARGET_DEVICE_REMOVAL_NOTIFICATION structure describes a device-removal event. The PnP manager sends this structure to a driver that registered a callback routine for notification of EventCategoryTargetDeviceChange events. |
| [PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_SEVERITY structure](ns-wdm--pci-express-sec-uncorrectable-error-severity.md) | TBD |
| [DMA_ADAPTER structure](ns-wdm--dma-adapter~r3.md) | TBD |
| [EISA_PORT_CONFIGURATION structure](ns-wdm--eisa-port-configuration.md) | TBD |
| [RTL_BITMAP structure](ns-wdm--rtl-bitmap.md) | TBD |
| [PCI_DEVICE_PRESENCE_PARAMETERS structure](ns-wdm--pci-device-presence-parameters.md) | TBD |
| [PCI_EXPRESS_BRIDGE_AER_CAPABILITY structure](ns-wdm--pci-express-bridge-aer-capability.md) | The PCI_EXPRESS_BRIDGE_AER_CAPABILITY structure describes a PCI Express (PCIe) advanced error reporting capability structure for a PCIe bridge device. |
| [KEY_VALUE_LAYER_INFORMATION structure](ns-wdm--key-value-layer-information.md) | TBD |
| [PO_FX_PERF_STATE_CHANGE structure](ns-wdm--po-fx-perf-state-change.md) | The PO_FX_PERF_STATE_CHANGE structure contains information about a change to a performance state that is being requested by calling the PoFxIssueComponentPerfStateChange or PoFxIssueComponentPerfStateChangeMultiple routine. |
| [GENERAL_LOOKASIDE_POOL structure](ns-wdm--general-lookaside-pool.md) | TBD |
| [PCW_COUNTER_INFORMATION structure](ns-wdm--pcw-counter-information.md) | The PCW_COUNTER_INFORMATION structure describes attributes that identify a specific instance of a counter set. |
| [PCI_EXPRESS_PASID_CAPABILITY structure](ns-wdm--pci-express-pasid-capability.md) | TBD |
| [POWER_SEQUENCE structure](ns-wdm--power-sequence.md) | TBD |
| [PCI_EXPRESS_PASID_CAPABILITY_REGISTER structure](ns-wdm--pci-express-pasid-capability-register.md) | TBD |
| [PCW_REGISTRATION_INFORMATION structure](ns-wdm--pcw-registration-information.md) | The PCW_REGISTRATION_INFORMATION structure supplies details about the provider and the counter set. |
| [OB_POST_OPERATION_INFORMATION structure](ns-wdm--ob-post-operation-information.md) | The OB_POST_OPERATION_INFORMATION structure provides information about a process or thread handle operation to an ObjectPostCallback routine. |
| [OBJECT_NAME_INFORMATION structure](ns-wdm--object-name-information.md) | TBD |
| [SECTION_OBJECT_POINTERS structure](ns-wdm--section-object-pointers.md) | The SECTION_OBJECT_POINTERS structure, allocated by a file system or a redirector driver, is used by the memory manager and cache manager to store file-mapping and cache-related information for a file stream. |
| [IO_CONNECT_INTERRUPT_LINE_BASED_PARAMETERS structure](ns-wdm--io-connect-interrupt-line-based-parameters.md) | TBD |
| [PCI_VIRTUALIZATION_INTERFACE structure](ns-wdm--pci-virtualization-interface.md) | The PCI_VIRTUALIZATION_INTERFACE structure enables drivers to manage and configure the PCI Express (PCIe) configuration space for a virtual function (VF). |
| [SHARE_ACCESS structure](ns-wdm--share-access.md) | TBD |
| [FILE_STANDARD_INFORMATION structure](ns-wdm--file-standard-information.md) | The FILE_STANDARD_INFORMATION structure is used as an argument to routines that query or set file information. |
| [HWPROFILE_CHANGE_NOTIFICATION structure](ns-wdm--hwprofile-change-notification.md) | The HWPROFILE_CHANGE_NOTIFICATION structure describes an event related to a hardware profile configuration change. |
| [KEY_TRUST_INFORMATION structure](ns-wdm--key-trust-information.md) | TBD |
| [FILE_STANDARD_INFORMATION_EX structure](ns-wdm--file-standard-information-ex.md) | The FILE_STANDARD_INFORMATION_EX structure is used as an argument to routines that query or set file information. |
| [PNP_REPLACE_PARAMETERS structure](ns-wdm--pnp-replace-parameters.md) | TBD |
| [DMA_CONFIGURATION_BYTE0 structure](ns-wdm--dma-configuration-byte0.md) | TBD |
| [CLFS_MGMT_NOTIFICATION structure](ns-wdm--clfs-mgmt-notification.md) | TBD |
| [HeaderArm64 structure](ns-wdm-headerarm64.md) | TBD |
| [AMD_L1_CACHE_INFO structure](ns-wdm--amd-l1-cache-info.md) | TBD |
| [REG_ENUMERATE_VALUE_KEY_INFORMATION structure](ns-wdm--reg-enumerate-value-key-information.md) | The REG_ENUMERATE_VALUE_KEY_INFORMATION structure describes one value entry of a key whose value entries are being enumerated. |
| [VIRTUAL_RESOURCE structure](ns-wdm--virtual-resource.md) | TBD |
| [PCI_PMCSR structure](ns-wdm--pci-pmcsr.md) | The PCI_PMCSR structure is used to report the contents of the device's power management control status register. |
| [DEVICE_OBJECT structure](ns-wdm--device-object.md) | TBD |
| [IO_ATTRIBUTION_INFORMATION structure](ns-wdm--io-attribution-information.md) | TBD |
| [CLS_INFORMATION structure](ns-wdm--cls-information.md) | TBD |
| [PCI_EXPRESS_CORRECTABLE_ERROR_STATUS structure](ns-wdm--pci-express-correctable-error-status.md) | The PCI_EXPRESS_CORRECTABLE_ERROR_STATUS structure describes a PCI Express (PCIe) correctable error status register of a PCIe advanced error reporting capability structure. |
| [BDCB_IMAGE_INFORMATION structure](ns-wdm--bdcb-image-information.md) | TBD |
| [IO_REMOVE_LOCK_DBG_BLOCK structure](ns-wdm--io-remove-lock-dbg-block.md) | TBD |
| [DEVICE_OBJECT structure](ns-wdm--device-object~r1.md) | TBD |
| [PLUGPLAY_NOTIFICATION_HEADER structure](ns-wdm--plugplay-notification-header.md) | A PLUGPLAY_NOTIFICATION_HEADER structure is included at the beginning of each PnP notification structure, such as a DEVICE_INTERFACE_CHANGE_NOTIFICATION structure. |
| [SLIST_HEADER structure](ns-wdm--slist-header.md) | TBD |
| [SECURITY_QUALITY_OF_SERVICE structure](ns-wdm--security-quality-of-service.md) | TBD |
| [PCW_CALLBACK_INFORMATION structure](ns-wdm--pcw-callback-information.md) | The PCW_CALLBACK_INFORMATION union supplies details about the notification to send. A provider passes a pointer to this union as a parameter to the PcwCallback function. |
| [OB_POST_OPERATION_PARAMETERS structure](ns-wdm--ob-post-operation-parameters.md) | The OB_POST_OPERATION_PARAMETERS union describes the operation-specific parameters for an ObjectPostCallback routine. |
| [IO_INTERRUPT_MESSAGE_INFO structure](ns-wdm--io-interrupt-message-info.md) | The IO_INTERRUPT_MESSAGE_INFO structure describes the driver's message-signaled interrupts. |
| [KFLOATING_SAVE structure](ns-wdm--kfloating-save~r3.md) | TBD |
| [OSVERSIONINFOEXA structure](ns-wdm--osversioninfoexa.md) | TBD |
| [ACL structure](ns-wdm--acl.md) | TBD |
| [BOOTDISK_INFORMATION structure](ns-wdm--bootdisk-information.md) | The BOOTDISK_INFORMATION structure contains basic information describing the boot and system disks. |
| [OB_PRE_CREATE_HANDLE_INFORMATION structure](ns-wdm--ob-pre-create-handle-information.md) | The OB_PRE_CREATE_HANDLE_INFORMATION structure provides information to an ObjectPreCallback routine about a thread or process handle that is being opened. |
| [SECURE_DRIVER_INTERFACE structure](ns-wdm--secure-driver-interface.md) | TBD |
| [DEVICE_OBJECT structure](ns-wdm--device-object~r2.md) | TBD |
| [PCI_EXPRESS_AER_CAPABILITIES structure](ns-wdm--pci-express-aer-capabilities.md) | The PCI_EXPRESS_AER_CAPABILITIES structure describes a PCI Express (PCIe) advanced error capabilities and control register of a PCIe advanced error reporting capability structure. |
| [KENLISTMENT structure](ns-wdm--kenlistment.md) | TBD |
| [SE_ADT_ACCESS_REASON structure](ns-wdm--se-adt-access-reason.md) | TBD |
| [KAPC structure](ns-wdm--kapc.md) | TBD |
| [MDL structure](ns-wdm--mdl.md) | An MDL structure is a partially opaque structure that represents a memory descriptor list (MDL). |
| [CM_EISA_SLOT_INFORMATION structure](ns-wdm--cm-eisa-slot-information.md) | The CM_EISA_SLOT_INFORMATION structure defines EISA configuration header information returned by HalGetBusData for the input BusDataType = EisaConfiguration, or by HalGetBusDataByOffset for the inputs BusDataType = EisaConfiguration and Offset = 0, assuming the caller-allocated Buffer is of sufficient Length. |
| [PNP_REPLACE_PROCESSOR_LIST_V1 structure](ns-wdm--pnp-replace-processor-list-v1.md) | TBD |
| [TRANSACTION_LIST_ENTRY structure](ns-wdm--transaction-list-entry.md) | TBD |
| [KGATE structure](ns-wdm--kgate.md) | TBD |
| [TRANSACTIONMANAGER_BASIC_INFORMATION structure](ns-wdm--transactionmanager-basic-information.md) | The TRANSACTIONMANAGER_BASIC_INFORMATION structure contains information about a transaction manager object. |
| [KSEMAPHORE structure](ns-wdm--ksemaphore.md) | TBD |
| [CM_SONIC_DEVICE_DATA structure](ns-wdm--cm-sonic-device-data.md) | TBD |
| [INTERFACE structure](ns-wdm--interface.md) | The INTERFACE structure describes an interface that is exported by a driver for use by other drivers. |
| [PCI_EXPRESS_ROOT_ERROR_COMMAND structure](ns-wdm--pci-express-root-error-command.md) | The PCI_EXPRESS_ROOT_ERROR_COMMAND structure describes a PCI Express (PCIe) root error command register of a PCIe advanced error reporting capability structure. |
| [CM_FLOPPY_DEVICE_DATA structure](ns-wdm--cm-floppy-device-data.md) | The CM_FLOPPY_DEVICE_DATA structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a floppy controller if the system can collect this information during the boot process. |
| [PO_FX_DEVICE_V1 structure](ns-wdm--po-fx-device-v1.md) | TBD |
| [PROCESSOR_GROUP_INFO structure](ns-wdm--processor-group-info.md) | TBD |
| [DRIVER_EXTENSION structure](ns-wdm--driver-extension.md) | TBD |
| [PCW_MASK_INFORMATION structure](ns-wdm--pcw-mask-information.md) | The PCW_MASK_INFORMATION structure supplies details about the notification to send to the provider. This information is passed as part of the Info parameter to the PcwCallback function. This mask information is included in PCW_CALLBACK_INFORMATION. |
| [DMA_ADAPTER_INFO_V1 structure](ns-wdm--dma-adapter-info-v1.md) | The DMA_ADAPTER_INFO_V1 structure describes the capabilities of the system DMA controller that is represented by an adapter object. |
| [KBUGCHECK_SECONDARY_DUMP_DATA_EX structure](ns-wdm--kbugcheck-secondary-dump-data-ex.md) | TBD |
| [IO_COMPLETION_CONTEXT structure](ns-wdm--io-completion-context.md) | TBD |
| [PCI_SLOT_NUMBER structure](ns-wdm--pci-slot-number.md) | The PCI_SLOT_NUMBER structure is obsolete. |
| [PO_FX_COMPONENT_V1 structure](ns-wdm--po-fx-component-v1.md) | TBD |
| [EISA_MEMORY_CONFIGURATION structure](ns-wdm--eisa-memory-configuration.md) | TBD |
| [XSTATE_CONTEXT structure](ns-wdm--xstate-context.md) | TBD |
| [PO_FX_DEVICE_V2 structure](ns-wdm--po-fx-device-v2.md) | TBD |
| [CM_COMPONENT_INFORMATION structure](ns-wdm--cm-component-information.md) | TBD |
| [POWER_PLATFORM_INFORMATION structure](ns-wdm--power-platform-information.md) | The POWER_PLATFORM_INFORMATION structure contains information about the power capabilities of the system. |
| [PCI_COMMON_CONFIG structure](ns-wdm--pci-common-config.md) | The PCI_COMMON_CONFIG structure is obsolete. |
| [FILE_IS_REMOTE_DEVICE_INFORMATION structure](ns-wdm--file-is-remote-device-information.md) | The FILE_IS_REMOTE_DEVICE_INFORMATION structure is used as an argument to the ZwQueryInformationFile routine. |
| [CM_PARTIAL_RESOURCE_LIST structure](ns-wdm--cm-partial-resource-list.md) | The CM_PARTIAL_RESOURCE_LIST structure specifies a set of system hardware resources, of various types, assigned to a device. This structure is contained within a CM_FULL_RESOURCE_DESCRIPTOR structure. |
| [KEY_VALUE_ENTRY structure](ns-wdm--key-value-entry.md) | The KEY_VALUE_ENTRY structure is used by the REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION structure to describe a single value entry for a registry key. |
| [FILE_NETWORK_OPEN_INFORMATION structure](ns-wdm--file-network-open-information.md) | The FILE_NETWORK_OPEN_INFORMATION structure is used as an argument to ZwQueryInformationFile. |
| [PCI_EXPRESS_PASID_CONTROL_REGISTER structure](ns-wdm--pci-express-pasid-control-register.md) | TBD |
| [IO_REMOVE_LOCK_COMMON_BLOCK structure](ns-wdm--io-remove-lock-common-block.md) | TBD |
| [KEY_WOW64_FLAGS_INFORMATION structure](ns-wdm--key-wow64-flags-information.md) | TBD |
| [FILE_OBJECT structure](ns-wdm--file-object~r1.md) | The FILE_OBJECT structure is used by the system to represent a file object. |
| [IO_INTERRUPT_MESSAGE_INFO_ENTRY structure](ns-wdm--io-interrupt-message-info-entry.md) | The IO_INTERRUPT_MESSAGE_INFO_ENTRY structure describes the properties of a single message-signaled interrupt. |
| [LOOKASIDE_LIST_EX structure](ns-wdm--lookaside-list-ex.md) | TBD |
| [KDPC structure](ns-wdm--kdpc.md) | TBD |
| [PCI_EXPRESS_SERIAL_NUMBER_CAPABILITY structure](ns-wdm--pci-express-serial-number-capability.md) | The PCI_EXPRESS_SERIAL_NUMBER_CAPABILITY structure describes a serial number for a PCI Express (PCIe) device. |
| [REG_CREATE_KEY_INFORMATION structure](ns-wdm--reg-create-key-information.md) | The REG_OPEN_KEY_INFORMATION structure contains the name of a registry key that is about to be opened. |
| [DRIVER_OBJECT structure](ns-wdm--driver-object.md) | TBD |
| [IO_WORKITEM structure](ns-wdm--io-workitem.md) | TBD |
| [AMD_L3_CACHE_INFO structure](ns-wdm--amd-l3-cache-info.md) | TBD |
| [FILE_PROCESS_IDS_USING_FILE_INFORMATION structure](ns-wdm--file-process-ids-using-file-information.md) | TBD |
| [RESOURCEMANAGER_BASIC_INFORMATION structure](ns-wdm--resourcemanager-basic-information.md) | The RESOURCEMANAGER_BASIC INFORMATION structure contains information about a resource manager object. |
| [NUMA_NODE_RELATIONSHIP structure](ns-wdm--numa-node-relationship.md) | TBD |
| [KDPC_WATCHDOG_INFORMATION structure](ns-wdm--kdpc-watchdog-information.md) | The KDPC_WATCHDOG_INFORMATION structure holds time-out information about the current deferred procedure call (DPC). |
| [IRP structure](ns-wdm--irp.md) | TBD |
| [VIRTUAL_RESOURCE_CONTROL structure](ns-wdm--virtual-resource-control.md) | TBD |
| [PNP_REPLACE_DRIVER_INTERFACE structure](ns-wdm--pnp-replace-driver-interface.md) | TBD |
| [KTM structure](ns-wdm--ktm.md) | TBD |
| [PCI_EXPRESS_ACS_CAPABILITY structure](ns-wdm--pci-express-acs-capability.md) | TBD |
| [FILE_BASIC_INFORMATION structure](ns-wdm--file-basic-information.md) | The FILE_BASIC_INFORMATION structure is used as an argument to routines that query or set file information. |
| [PO_FX_COMPONENT_PERF_SET structure](ns-wdm--po-fx-component-perf-set.md) | The PO_FX_COMPONENT_PERF_SET structure represents a set of performance states for a single component within a device. |
| [PCI_EXPRESS_SRIOV_CONTROL structure](ns-wdm--pci-express-sriov-control.md) | TBD |
| [EISA_MEMORY_TYPE structure](ns-wdm--eisa-memory-type.md) | TBD |
| [FILE_IO_PRIORITY_HINT_INFORMATION_EX structure](ns-wdm--file-io-priority-hint-information-ex.md) | TBD |
| [VIRTUAL_CHANNEL_CAPABILITIES2 structure](ns-wdm--virtual-channel-capabilities2.md) | TBD |
| [REG_QUERY_KEY_NAME structure](ns-wdm--reg-query-key-name.md) | The REG_QUERY_KEY_NAME structure describes the full registry key name of an object being queried. |
| [OSVERSIONINFOA structure](ns-wdm--osversioninfoa.md) | TBD |
| [FILE_IO_PRIORITY_HINT_INFORMATION structure](ns-wdm--file-io-priority-hint-information.md) | The FILE_IO_PRIORITY_HINT_INFORMATION structure is used by the ZwQueryInformationFile and ZwSetInformationFile routines to query and set the default IRP priority hint for requests on the specified file handle. |
| [KWAIT_CHAIN structure](ns-wdm--kwait-chain.md) | TBD |
| [SDEV_IDENTIFIER_INTERFACE structure](ns-wdm--sdev-identifier-interface.md) | TBD. |
| [SCATTER_GATHER_LIST structure](ns-wdm--scatter-gather-list.md) | TBD |
| [POWER_STATE structure](ns-wdm--power-state.md) | The POWER_STATE union specifies a system power state value or a device power state value. |
| [MM_PHYSICAL_ADDRESS_LIST structure](ns-wdm--mm-physical-address-list.md) | The MM_PHYSICAL_ADDRESS_LIST structure specifies a range of physical addresses. |
| [PBATTERY_REPORTING_SCALE structure](ns-wdm-pbattery-reporting-scale.md) | TBD |
| [PCI_SECURITY_INTERFACE structure](ns-wdm--pci-security-interface.md) | TBD |
| [PCW_DATA structure](ns-wdm--pcw-data.md) | The PCW_DATA structure describes the array of data blocks that are associated with an instance. |
| [TRANSACTION_ENLISTMENT_PAIR structure](ns-wdm--transaction-enlistment-pair.md) | The TRANSACTION_ENLISTMENT_PAIR structure contains information about an enlistment that is associated with a transaction object. |
| [PCI_EXPRESS_ACS_CAPABILITY_REGISTER structure](ns-wdm--pci-express-acs-capability-register.md) | TBD |
| [PCI_EXPRESS_PRI_CAPABILITY structure](ns-wdm--pci-express-pri-capability.md) | TBD |
| [KEY_VALUE_FULL_INFORMATION structure](ns-wdm--key-value-full-information.md) | The KEY_VALUE_FULL_INFORMATION structure defines information available for a value entry of a registry key. |
| [IO_RESOURCE_LIST structure](ns-wdm--io-resource-list.md) | The IO_RESOURCE_LIST structure describes a range of raw hardware resources, of various types, that can be used by a device. |
| [DMA_TRANSFER_INFO structure](ns-wdm--dma-transfer-info.md) | The DMA_TRANSFER_INFO structure is a container for a DMA_TRANSFER_INFO_XXX structure that describes the allocation requirements for a scatter/gather list. |
| [KFLOATING_SAVE structure](ns-wdm--kfloating-save~r1.md) | TBD |
| [IO_STATUS_BLOCK structure](ns-wdm--io-status-block.md) | A driver sets an IRP's I/O status block to indicate the final status of an I/O request, before calling IoCompleteRequest for the IRP. |
| [EISA_DMA_CONFIGURATION structure](ns-wdm--eisa-dma-configuration.md) | TBD |
| [TRANSACTION_BASIC_INFORMATION structure](ns-wdm--transaction-basic-information.md) | The TRANSACTION_BASIC_INFORMATION structure contains information about a transaction object. |
| [VIRTUAL_CHANNEL_CAPABILITIES1 structure](ns-wdm--virtual-channel-capabilities1.md) | TBD |
| [IO_STACK_LOCATION structure](ns-wdm--io-stack-location.md) | The IO_STACK_LOCATION structure defines an I/O stack location, which is an entry in the I/O stack that is associated with each IRP. |
| [PCI_EXPRESS_ATS_CAPABILITY structure](ns-wdm--pci-express-ats-capability.md) | TBD |
| [KTIMER structure](ns-wdm--ktimer.md) | TBD |
| [PNP_BUS_INFORMATION structure](ns-wdm--pnp-bus-information.md) | The PNP_BUS_INFORMATION structure describes a bus. |
| [CLFS_MGMT_CLIENT_REGISTRATION structure](ns-wdm--clfs-mgmt-client-registration.md) | The CLFS_MGMT_CLIENT_REGISTRATION structure is given to CLFS management by clients who manage their own logs. |
| [CM_SCSI_DEVICE_DATA structure](ns-wdm--cm-scsi-device-data.md) | The CM_SCSI_DEVICE_DATA structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a SCSI HBA if the system can collect this information during the boot process. |
| [CLS_IO_STATISTICS_HEADER structure](ns-wdm--cls-io-statistics-header.md) | TBD |
| [DMA_OPERATIONS structure](ns-wdm--dma-operations~r1.md) | The DMA_OPERATIONS structure provides a table of pointers to functions that control the operation of a DMA controller. |
| [SE_ADT_PARAMETER_ARRAY_ENTRY structure](ns-wdm--se-adt-parameter-array-entry.md) | TBD |
| [PCI_EXPRESS_ARI_CONTROL_REGISTER structure](ns-wdm--pci-express-ari-control-register.md) | TBD |
| [SE_ADT_PARAMETER_ARRAY_EX structure](ns-wdm--se-adt-parameter-array-ex.md) | TBD |
| [ACPI_INTERFACE_STANDARD structure](ns-wdm--acpi-interface-standard.md) | TBD |
| [KSYSTEM_TIME structure](ns-wdm--ksystem-time.md) | TBD |
| [DRIVER_OBJECT structure](ns-wdm--driver-object~r4.md) | TBD |
| [IO_CONNECT_INTERRUPT_MESSAGE_BASED_PARAMETERS structure](ns-wdm--io-connect-interrupt-message-based-parameters.md) | TBD |
| [PNOTIFY_USER_POWER_SETTING structure](ns-wdm-pnotify-user-power-setting.md) | TBD |
| [KEY_FULL_INFORMATION structure](ns-wdm--key-full-information.md) | The KEY_FULL_INFORMATION structure defines the information available for a registry key, including information about its subkeys and the maximum length for their names and value entries. |
| [SYSTEM_POWER_STATE_CONTEXT structure](ns-wdm--system-power-state-context.md) | The SYSTEM_POWER_STATE_CONTEXT structure is a partially opaque system structure that contains information about the previous system power states of a computer. |
| [CLS_WRITE_ENTRY structure](ns-wdm--cls-write-entry.md) | TBD |
| [IO_CSQ_IRP_CONTEXT structure](ns-wdm--io-csq-irp-context.md) | TBD |
| [IO_STATUS_BLOCK32 structure](ns-wdm--io-status-block32.md) | TBD |
| [IO_SESSION_CONNECT_INFO structure](ns-wdm--io-session-connect-info.md) | The IO_SESSION_CONNECT_INFO structure provides information about a user session. |
| [POWER_SESSION_TIMEOUTS structure](ns-wdm--power-session-timeouts.md) | TBD |
| [AssociatedIrp structure](ns-wdm-associatedirp.md) | TBD |
| [LOOKASIDE_LIST_EX structure](ns-wdm--lookaside-list-ex~r1.md) | TBD |
| [SCATTER_GATHER_ELEMENT structure](ns-wdm--scatter-gather-element.md) | TBD |
| [CLS_SCAN_CONTEXT structure](ns-wdm--cls-scan-context.md) | TBD |
| [KWAIT_BLOCK structure](ns-wdm--kwait-block.md) | TBD |
| [PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_STATUS structure](ns-wdm--pci-express-sec-uncorrectable-error-status.md) | TBD |
| [SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX structure](ns-wdm--system-logical-processor-information-ex.md) | TBD |
| [BOOTDISK_INFORMATION_EX structure](ns-wdm--bootdisk-information-ex.md) | The BOOTDISK_INFORMATION_EX structure contains extended information describing the boot and system disks. |
| [DMA_ADAPTER structure](ns-wdm--dma-adapter~r1.md) | TBD |
| [KEY_VALUE_PARTIAL_INFORMATION_ALIGN64 structure](ns-wdm--key-value-partial-information-align64.md) | TBD |
| [REG_KEY_HANDLE_CLOSE_INFORMATION structure](ns-wdm--reg-key-handle-close-information.md) | The REG_KEY_HANDLE_CLOSE_INFORMATION structure contains information about a registry key whose handle is about to be closed. |
| [CM_PNP_BIOS_INSTALLATION_CHECK structure](ns-wdm--cm-pnp-bios-installation-check.md) | TBD |
| [REG_ENUMERATE_KEY_INFORMATION structure](ns-wdm--reg-enumerate-key-information.md) | The REG_ENUMERATE_KEY_INFORMATION structure describes one subkey of a key whose subkeys are being enumerated. |
| [REG_RENAME_KEY_INFORMATION structure](ns-wdm--reg-rename-key-information.md) | The REG_RENAME_KEY_INFORMATION structure contains the new name for a registry key whose name is about to be changed. |
| [KBUGCHECK_SECONDARY_DUMP_DATA structure](ns-wdm--kbugcheck-secondary-dump-data.md) | The KBUGCHECK_SECONDARY_DUMP_DATA structure describes a section of driver-supplied data to be written by BugCheckSecondaryDumpDataCallback to the crash dump file. |
| [HeaderX64 structure](ns-wdm-headerx64.md) | TBD |
| [INTEL_CACHE_INFO_EAX structure](ns-wdm-intel-cache-info-eax.md) | TBD |
| [SCATTER_GATHER_LIST structure](ns-wdm--scatter-gather-list~r1.md) | The SCATTER_GATHER_LIST structure describes the scatter/gather list for a DMA operation. |
| [LINK_SHARE_ACCESS structure](ns-wdm--link-share-access.md) | The share access structure used by file systems for only link files. |
| [CM_MONITOR_DEVICE_DATA structure](ns-wdm--cm-monitor-device-data.md) | TBD |
| [KEY_CONTROL_FLAGS_INFORMATION structure](ns-wdm--key-control-flags-information.md) | TBD |
| [OWNER_ENTRY structure](ns-wdm--owner-entry.md) | TBD |
| [EX_RUNDOWN_REF structure](ns-wdm--ex-rundown-ref.md) | TBD |
| [VPB structure](ns-wdm--vpb.md) | The volume parameter block (VPB) structure is used to map a device object that represents a mounted file system volume to a device object that represents a physical or virtual disk device. |
| [RESOURCE_PERFORMANCE_DATA structure](ns-wdm--resource-performance-data.md) | TBD |
| [IO_SESSION_STATE_NOTIFICATION structure](ns-wdm--io-session-state-notification.md) | The IO_SESSION_STATE_NOTIFICATION structure contains information that a kernel-mode driver supplies to the IoRegisterContainerNotification routine when the driver registers to receive notifications of session events. |
| [KEVENT structure](ns-wdm--kevent.md) | TBD |
| [NPAGED_LOOKASIDE_LIST structure](ns-wdm--npaged-lookaside-list.md) | TBD |
| [IO_REMOVE_LOCK_TRACKING_BLOCK structure](ns-wdm--io-remove-lock-tracking-block.md) | TBD |
| [REG_POST_OPERATION_INFORMATION structure](ns-wdm--reg-post-operation-information.md) | The REG_POST_OPERATION_INFORMATION structure contains information about a completed registry operation that a RegistryCallback routine can use. |
| [IO_CONNECT_INTERRUPT_PARAMETERS structure](ns-wdm--io-connect-interrupt-parameters.md) | The IO_CONNECT_INTERRUPT_PARAMETERS structure contains the parameters that a driver supplies to the IoConnectInterruptEx routine to register an interrupt service routine (ISR). |
| [KEY_VALUE_BASIC_INFORMATION structure](ns-wdm--key-value-basic-information.md) | The KEY_VALUE_BASIC_INFORMATION structure defines a subset of the full information available for a value entry of a registry key. |
| [CLFS_NODE_ID structure](ns-wdm--clfs-node-id.md) | TBD |
| [DMA_TRANSFER_INFO_V1 structure](ns-wdm--dma-transfer-info-v1.md) | The DMA_TRANSFER_INFO_V1 structure contains the allocation requirements for a scatter/gather list that describes the I/O data buffer for a DMA transfer. |
| [POWER_MONITOR_INVOCATION structure](ns-wdm--power-monitor-invocation.md) | TBD |
| [IO_RESOURCE_DESCRIPTOR structure](ns-wdm--io-resource-descriptor.md) | The IO_RESOURCE_DESCRIPTOR structure describes a range of raw hardware resources, of one type, that can be used by a device. An array of IO_RESOURCE_DESCRIPTOR structures is contained within each IO_RESOURCE_LIST structure. |
| [PCI_EXPRESS_SRIOV_MIGRATION_STATE_ARRAY structure](ns-wdm--pci-express-sriov-migration-state-array.md) | TBD |
| [SINGLE_LIST_ENTRY structure](ns-wdm--single-list-entry.md) | TBD |
| [KEY_NODE_INFORMATION structure](ns-wdm--key-node-information.md) | The KEY_NODE_INFORMATION structure defines the basic information available for a registry (sub)key. |
| [IO_CSQ structure](ns-wdm--io-csq~r1.md) | TBD |
| [GROUP_RELATIONSHIP structure](ns-wdm--group-relationship.md) | TBD |
| [CLFS_MGMT_POLICY structure](ns-wdm--clfs-mgmt-policy.md) | The CLFS_MGMT_POLICY structure holds a description of a policy for managing a CLFS log. |
| [WORK_QUEUE_ITEM structure](ns-wdm--work-queue-item.md) | The WORK_QUEUE_ITEM structure is used to post a work items to a system work queue. |
| [CRASHDUMP_FUNCTIONS_INTERFACE structure](ns-wdm--crashdump-functions-interface.md) | TBD |
| [Tail structure](ns-wdm-tail.md) | TBD |
| [FAST_IO_DISPATCH structure](ns-wdm--fast-io-dispatch.md) | Contains a set of callback routines that a file system driver or file system filter driver (legacy) provides for fast I/O processing. |
| [ETW_TRACE_SESSION_SETTINGS structure](ns-wdm--etw-trace-session-settings.md) | TBD |
| [PCI_EXPRESS_ROOT_PORT_INTERFACE structure](ns-wdm--pci-express-root-port-interface.md) | TBD |
| [BOOTDISK_INFORMATION_LITE structure](ns-wdm--bootdisk-information-lite~r1.md) | TBD |
| [IO_SESSION_STATE_INFORMATION structure](ns-wdm--io-session-state-information.md) | The IO_SESSION_STATE_INFORMATION structure contains information about the state of a user session. |
| [IMAGE_POLICY_METADATA structure](ns-wdm--image-policy-metadata.md) | TBD |
| [Queue structure](ns-wdm-queue.md) | TBD |
| [CLS_ARCHIVE_DESCRIPTOR structure](ns-wdm--cls-archive-descriptor.md) | TBD |
| [PCI_EXPRESS_SEC_AER_CAPABILITIES structure](ns-wdm--pci-express-sec-aer-capabilities.md) | The PCI_EXPRESS_SEC_AER_CAPABILITIES structure describes a PCI Express (PCIe) secondary error capabilities and control register of a PCIe advanced error reporting capability structure. |
| [REG_POST_CREATE_KEY_INFORMATION structure](ns-wdm--reg-post-create-key-information.md) | The REG_POST_OPEN_KEY_INFORMATION structure contains the result of an attempt to open a registry key. |
| [REG_QUERY_VALUE_KEY_INFORMATION structure](ns-wdm--reg-query-value-key-information.md) | The REG_QUERY_VALUE_KEY_INFORMATION structure contains information about a registry key's value entry that is being queried. |
| [OB_PRE_DUPLICATE_HANDLE_INFORMATION structure](ns-wdm--ob-pre-duplicate-handle-information.md) | The OB_PRE_DUPLICATE_HANDLE_INFORMATION structure provides information to an ObjectPreCallback routine about a thread or process handle that is being duplicated. |
| [KEY_WRITE_TIME_INFORMATION structure](ns-wdm--key-write-time-information.md) | The KEY_WRITE_TIME_INFORMATION structure is used by the system to set the last write time for a registry key. |
| [OSVERSIONINFOEXW structure](ns-wdm--osversioninfoexw.md) | TBD |
| [LOADER_PARTITION_INFORMATION_EX structure](ns-wdm--loader-partition-information-ex.md) | TBD |
| [PCI_COMMON_HEADER structure](ns-wdm--pci-common-header.md) | TBD |
| [PCI_EXPRESS_UNCORRECTABLE_ERROR_MASK structure](ns-wdm--pci-express-uncorrectable-error-mask.md) | The PCI_EXPRESS_UNCORRECTABLE_ERROR_MASK structure describes a PCI Express (PCIe) uncorrectable error mask register of a PCIe advanced error reporting capability structure. |
| [D3COLD_SUPPORT_INTERFACE structure](ns-wdm--d3cold-support-interface.md) | The D3COLD_SUPPORT_INTERFACE interface structure contains pointers to the routines in the GUID_D3COLD_SUPPORT_INTERFACE driver interface. |
| [IO_REPORT_INTERRUPT_ACTIVE_STATE_PARAMETERS structure](ns-wdm--io-report-interrupt-active-state-parameters.md) | TBD |
| [IO_DISCONNECT_INTERRUPT_PARAMETERS structure](ns-wdm--io-disconnect-interrupt-parameters.md) | The IO_DISCONNECT_INTERRUPT_PARAMETERS structure describes the parameters when unregistering an interrupt-handling routine with IoDisconnectInterruptEx. |
| [DRIVER_OBJECT structure](ns-wdm--driver-object~r1.md) | TBD |
| [REG_DELETE_VALUE_KEY_INFORMATION structure](ns-wdm--reg-delete-value-key-information.md) | The REG_DELETE_VALUE_KEY_INFORMATION structure contains information that a driver's RegistryCallback routine can use when a registry key's value is being deleted. |
| [CLS_LSN structure](ns-wdm--cls-lsn.md) | TBD |
| [TIME_FIELDS structure](ns-wdm--time-fields.md) | TBD |
| [OSVERSIONINFOW structure](ns-wdm--osversioninfow.md) | TBD |
| [KTRANSACTION structure](ns-wdm--ktransaction.md) | TBD |
| [CM_ROM_BLOCK structure](ns-wdm--cm-rom-block.md) | TBD |
| [COUNTED_REASON_CONTEXT structure](ns-wdm--counted-reason-context.md) | The COUNTED_REASON_CONTEXT structure contains one or more strings that give reasons for a power request. |
| [POWER_SESSION_RIT_STATE structure](ns-wdm--power-session-rit-state.md) | TBD |
| [KBUGCHECK_REMOVE_PAGES structure](ns-wdm--kbugcheck-remove-pages.md) | TBD |
| [DEVICE_CAPABILITIES structure](ns-wdm--device-capabilities.md) | A DEVICE_CAPABILITIES structure describes PnP and power capabilities of a device. This structure is returned in response to an IRP_MN_QUERY_CAPABILITIES IRP. |
| [IO_ERROR_LOG_MESSAGE structure](ns-wdm--io-error-log-message.md) | TBD |
| [INITIAL_PRIVILEGE_SET structure](ns-wdm--initial-privilege-set.md) | TBD |
| [KTMOBJECT_CURSOR structure](ns-wdm--ktmobject-cursor.md) | The KTMOBJECT_CURSOR structure receives enumeration information about KTM objects when a component calls ZwEnumerateTransactionObject. |
| [PCI_CAPABILITIES_HEADER structure](ns-wdm--pci-capabilities-header.md) | The PCI_CAPABILITIES_HEADER structure defines a header that is present in every PCI capability structure. |
| [PNP_EXTENDED_ADDRESS_INTERFACE structure](ns-wdm--pnp-extended-address-interface.md) | TBD |
| [DEVICE_FLAGS structure](ns-wdm--device-flags.md) | TBD |
| [EXT_DELETE_PARAMETERS structure](ns-wdm--ext-delete-parameters.md) | The EXT_DELETE_PARAMETERS structure contains an extended set of parameters for the ExDeleteTimer routine. |
| [FILE_SFIO_VOLUME_INFORMATION structure](ns-wdm--file-sfio-volume-information.md) | TBD |
| [PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK structure](ns-wdm--pci-express-sec-uncorrectable-error-mask.md) | TBD |
| [FILE_FS_DEVICE_INFORMATION structure](ns-wdm--file-fs-device-information.md) | The FILE_FS_DEVICE_INFORMATION structure provides file system device information about the type of device object associated with a file object. |
| [RESOURCE_HASH_ENTRY structure](ns-wdm--resource-hash-entry.md) | TBD |
| [PCI_EXPRESS_ATS_CAPABILITY_REGISTER structure](ns-wdm--pci-express-ats-capability-register.md) | TBD |
| [OB_PRE_OPERATION_INFORMATION structure](ns-wdm--ob-pre-operation-information.md) | The OB_PRE_OPERATION_INFORMATION structure provides information about a process or thread handle operation to an ObjectPreCallback routine. |
| [CLIENT_ID structure](ns-wdm--client-id.md) | TBD |
| [KE_PROCESSOR_CHANGE_NOTIFY_CONTEXT structure](ns-wdm--ke-processor-change-notify-context.md) | The KE_PROCESSOR_CHANGE_NOTIFY_CONTEXT structure describes the notification context that is passed to a registered callback function when a new processor is dynamically added to a hardware partition. |
| [DRIVER_OBJECT structure](ns-wdm--driver-object~r3.md) | Each driver object represents the image of a loaded kernel-mode driver. |
| [TRANSACTION_SUPERIOR_ENLISTMENT_INFORMATION structure](ns-wdm--transaction-superior-enlistment-information.md) | TBD |
| [FILE_NUMA_NODE_INFORMATION structure](ns-wdm--file-numa-node-information.md) | TBD |
| [CLFS_LOG_NAME_INFORMATION structure](ns-wdm--clfs-log-name-information.md) | The CLFS_LOG_NAME_INFORMATION structure holds the name of a Common Log File System (CLFS) stream or log. |
| [GENERIC_MAPPING structure](ns-wdm--generic-mapping.md) | The GENERIC_MAPPING structure describes the ACCESS_MASK value of specific access rights associated with each type of generic access right. |
| [REG_PRE_CREATE_KEY_INFORMATION structure](ns-wdm--reg-pre-create-key-information.md) | The REG_PRE_OPEN_KEY_INFORMATION structure contains the name of a registry key that is about to be opened. |
| [PPCI_X_CAPABILITY structure](ns-wdm-ppci-x-capability.md) | The PCI_X_CAPABILITY structure reports the contents of the command and status registers of a device that is compliant with the PCI-X Addendum to the PCI Local Bus Specification. |
| [PCI_COMMON_CONFIG structure](ns-wdm--pci-common-config~r1.md) | The PCI_COMMON_CONFIG structure is obsolete. |
| [PO_FX_COMPONENT_PERF_INFO structure](ns-wdm--po-fx-component-perf-info.md) | The PO_FX_COMPONENT_PERF_INFO structure describes all the sets of performance states for a single component within a device. |
| [CM_INT13_DRIVE_PARAMETER structure](ns-wdm--cm-int13-drive-parameter.md) | The CM_INT13_DRIVE_PARAMETER structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a disk controller if the system can collect this information during the boot process. |
| [DMA_ADAPTER_INFO structure](ns-wdm--dma-adapter-info.md) | The DMA_ADAPTER_INFO structure is a container for a DMA_ADAPTER_INFO_XXX structure that describes the capabilities of a system DMA controller. |
| [OBJECT_HANDLE_INFORMATION structure](ns-wdm--object-handle-information.md) | TBD |
| [POWER_SESSION_CONNECT structure](ns-wdm--power-session-connect.md) | TBD |
| [PCI_EXPRESS_SRIOV_CAPS structure](ns-wdm--pci-express-sriov-caps.md) | TBD |
| [SECURITY_SUBJECT_CONTEXT structure](ns-wdm--security-subject-context.md) | TBD |
| [PO_FX_COMPONENT_V2 structure](ns-wdm--po-fx-component-v2.md) | TBD |
| [PCI_EXPRESS_ARI_CAPABILITY structure](ns-wdm--pci-express-ari-capability.md) | TBD |
| [PAGED_LOOKASIDE_LIST structure](ns-wdm--paged-lookaside-list.md) | TBD |
| [CM_SERIAL_DEVICE_DATA structure](ns-wdm--cm-serial-device-data.md) | The CM_SERIAL_DEVICE_DATA structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a serial controller if the system can collect this information during the boot process. |
| [NAMED_PIPE_CREATE_PARAMETERS structure](ns-wdm--named-pipe-create-parameters.md) | TBD |
| [EXT_SET_PARAMETERS_V0 structure](ns-wdm--ext-set-parameters-v0.md) | The EXT_SET_PARAMETERS structure contains an extended set of parameters for the ExSetTimer routine. |
| [PCI_MSIX_TABLE_CONFIG_INTERFACE structure](ns-wdm--pci-msix-table-config-interface.md) | The PCI_MSIX_TABLE_CONFIG_INTERFACE structure enables device drivers to modify their MSI-X interrupt settings. This structure describes the GUID_MSIX_TABLE_CONFIG_INTERFACE interface. |
| [CLS_IO_STATISTICS structure](ns-wdm--cls-io-statistics.md) | TBD |
| [PNP_REPLACE_MEMORY_LIST structure](ns-wdm--pnp-replace-memory-list.md) | TBD |
| [CM_KEYBOARD_DEVICE_DATA structure](ns-wdm--cm-keyboard-device-data.md) | The CM_KEYBOARD_DEVICE_DATA structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a keyboard peripheral if the system can collect this information during the boot process. |
| [FILE_OBJECT structure](ns-wdm--file-object~r2.md) | TBD |
| [CACHE_RELATIONSHIP structure](ns-wdm--cache-relationship.md) | TBD |
| [LEGACY_BUS_INFORMATION structure](ns-wdm--legacy-bus-information.md) | TBD |
| [SYSTEM_CPU_SET_INFORMATION structure](ns-wdm--system-cpu-set-information.md) | TBD |
| [AMD_L2_CACHE_INFO structure](ns-wdm--amd-l2-cache-info.md) | TBD |
| [KSPIN_LOCK_QUEUE structure](ns-wdm--kspin-lock-queue.md) | TBD |
| [SE_IMPERSONATION_STATE structure](ns-wdm--se-impersonation-state.md) | TBD |
| [REG_DELETE_KEY_INFORMATION structure](ns-wdm--reg-delete-key-information.md) | TBD |
| [CM_RESOURCE_LIST structure](ns-wdm--cm-resource-list.md) | The CM_RESOURCE_LIST structure specifies all of the system hardware resources assigned to a device. |
| [SE_ADT_PARAMETER_ARRAY structure](ns-wdm--se-adt-parameter-array.md) | TBD |
| [FILE_IO_COMPLETION_NOTIFICATION_INFORMATION structure](ns-wdm--file-io-completion-notification-information.md) | TBD |
| [PCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY structure](ns-wdm--pci-express-uncorrectable-error-severity.md) | The PCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY structure describes a PCI Express (PCIe) uncorrectable error severity register of a PCIe advanced error reporting capability structure. |
| [PO_FX_COMPONENT_IDLE_STATE structure](ns-wdm--po-fx-component-idle-state.md) | The PO_FX_COMPONENT_IDLE_STATE structure specifies the attributes of an Fx power state of a component in a device. |
| [TRANSACTION_LIST_INFORMATION structure](ns-wdm--transaction-list-information.md) | TBD |
| [REG_SET_KEY_SECURITY_INFORMATION structure](ns-wdm--reg-set-key-security-information.md) | The REG_SET_KEY_SECURITY_INFORMATION structure specifies security information for a registry key object. |
| [TRANSACTIONMANAGER_LOG_INFORMATION structure](ns-wdm--transactionmanager-log-information.md) | The TRANSACTIONMANAGER_LOG_INFORMATION structure contains information about a transaction manager object. |
| [PCI_EXPRESS_ROOT_ERROR_STATUS structure](ns-wdm--pci-express-root-error-status.md) | The PCI_EXPRESS_ROOT_ERROR_STATUS structure describes a PCI Express (PCIe) root error status register of a PCIe advanced error reporting capability structure. |
| [DMA_CONFIGURATION_BYTE1 structure](ns-wdm--dma-configuration-byte1.md) | TBD |
| [KBUGCHECK_CALLBACK_RECORD structure](ns-wdm--kbugcheck-callback-record.md) | TBD |
| [XSTATE_SAVE structure](ns-wdm--xstate-save.md) | TBD |
| [CM_PNP_BIOS_DEVICE_NODE structure](ns-wdm--cm-pnp-bios-device-node.md) | TBD |
| [PCW_REGISTRATION structure](ns-wdm--pcw-registration.md) | TBD |
| [ARM_IDCODE structure](ns-wdm--arm-idcode.md) | TBD |
| [IO_RESOURCE_REQUIREMENTS_LIST structure](ns-wdm--io-resource-requirements-list.md) | The IO_RESOURCE_REQUIREMENTS_LIST structure describes sets of resource configurations that can be used by a device. Each configuration represents a range of raw resources, of various types, that can be used by a device. |
| [EISA_IRQ_DESCRIPTOR structure](ns-wdm--eisa-irq-descriptor.md) | TBD |
| [DMA_ADAPTER structure](ns-wdm--dma-adapter.md) | TBD |
| [GENERAL_LOOKASIDE structure](ns-wdm--general-lookaside.md) | TBD |
| [PCI_EXPRESS_AER_CAPABILITY structure](ns-wdm--pci-express-aer-capability.md) | The PCI_EXPRESS_AER_CAPABILITY structure describes a PCI Express (PCIe) advanced error reporting capability structure. |
| [KFLOATING_SAVE structure](ns-wdm--kfloating-save~r2.md) | TBD |
| [CLFS_PHYSICAL_LSN_INFORMATION structure](ns-wdm--clfs-physical-lsn-information.md) | TBD |
| [OB_POST_CREATE_HANDLE_INFORMATION structure](ns-wdm--ob-post-create-handle-information.md) | The OB_POST_CREATE_HANDLE_INFORMATION structure provides information to a ObjectPostCallback routine about a thread or process handle that has been opened. |
| [CLFS_STREAM_ID_INFORMATION structure](ns-wdm--clfs-stream-id-information.md) | The CLFS_STREAM_ID_INFORMATION structure holds a value that identifies a stream in a Common Log File System (CLFS) log. |
| [PCI_EXPRESS_ARI_CAPABILITY_REGISTER structure](ns-wdm--pci-express-ari-capability-register.md) | TBD |
| [REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION structure](ns-wdm--reg-query-multiple-value-key-information.md) | The REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION structure describes the multiple value entries that are being retrieved for a key. |
| [RESUME_PERFORMANCE structure](ns-wdm--resume-performance.md) | TBD |
| [ARM64_IDCODE structure](ns-wdm--arm64-idcode.md) | TBD |
| [EISA_IRQ_CONFIGURATION structure](ns-wdm--eisa-irq-configuration.md) | TBD |
| [ERESOURCE structure](ns-wdm--eresource.md) | TBD |
| [WAIT_CONTEXT_BLOCK structure](ns-wdm--wait-context-block.md) | TBD |
| [MAILSLOT_CREATE_PARAMETERS structure](ns-wdm--mailslot-create-parameters.md) | TBD |
| [CM_EISA_FUNCTION_INFORMATION structure](ns-wdm--cm-eisa-function-information.md) | The CM_EISA_FUNCTION_INFORMATION structure defines detailed EISA configuration information returned by HalGetBusData for the input BusDataType EisaConfiguration, or by HalGetBusDataByOffset for the input BusDataType EisaConfiguration and the Offset zero, assuming the caller-allocated Buffer is of sufficient Length. |
| [DMA_ADAPTER structure](ns-wdm--dma-adapter~r5.md) | The DMA_ADAPTER structure describes a system-defined interface to a DMA controller for a given device. A driver calls IoGetDmaAdapter to obtain this structure. |
| [DEVICE_INTERFACE_CHANGE_NOTIFICATION structure](ns-wdm--device-interface-change-notification.md) | The DEVICE_INTERFACE_CHANGE_NOTIFICATION structure describes a device interface that has been enabled (arrived) or disabled (removed). |
| [TRANSACTION_ENLISTMENTS_INFORMATION structure](ns-wdm--transaction-enlistments-information.md) | The TRANSACTION_ENLISTMENTS_INFORMATION structure contains information about the enlistments that are associated with a transaction object. |
| [SCATTER_GATHER_LIST structure](ns-wdm--scatter-gather-list~r2.md) | TBD |
| [SCATTER_GATHER_LIST structure](ns-wdm--scatter-gather-list~r3.md) | TBD |
| [KFLOATING_SAVE structure](ns-wdm--kfloating-save.md) | TBD |
| [IO_ERROR_LOG_PACKET structure](ns-wdm--io-error-log-packet.md) | The IO_ERROR_LOG_PACKET structure serves as the header for an error log entry. |
| [KEY_BASIC_INFORMATION structure](ns-wdm--key-basic-information.md) | The KEY_BASIC_INFORMATION structure defines a subset of the full information that is available for a registry key. |
| [PCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS structure](ns-wdm--pci-express-uncorrectable-error-status.md) | The PCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS structure describes a PCI Express (PCIe) uncorrectable error status register of a PCIe advanced error reporting capability structure. |
| [FILE_OBJECT structure](ns-wdm--file-object.md) | TBD |
| [CALLBACK_OBJECT structure](ns-wdm--callback-object.md) | TBD |
| [BUS_INTERFACE_STANDARD structure](ns-wdm--bus-interface-standard.md) | The BUS_INTERFACE_STANDARD interface structure enables device drivers to make direct calls to parent bus driver routines. This structure defines the GUID_BUS_INTERFACE_STANDARD interface. |
| [PO_FX_PERF_STATE structure](ns-wdm--po-fx-perf-state.md) | The PO_FX_PERF_STATE structure represents a performance state for a single component within a device. |
| [CM_VIDEO_DEVICE_DATA structure](ns-wdm--cm-video-device-data.md) | TBD |
| [DEVICE_RELATIONS structure](ns-wdm--device-relations.md) | TBD |
| [PCI_EXPRESS_ROOTPORT_AER_CAPABILITY structure](ns-wdm--pci-express-rootport-aer-capability.md) | The PCI_EXPRESS_ROOTPORT_AER_CAPABILITY structure describes a PCI Express (PCIe) advanced error reporting capability structure for a root port or a root complex event collector. |
| [CACHE_DESCRIPTOR structure](ns-wdm--cache-descriptor.md) | TBD |
| [PCI_EXPRESS_PRI_STATUS_REGISTER structure](ns-wdm--pci-express-pri-status-register.md) | TBD |
| [DISPATCHER_HEADER structure](ns-wdm--dispatcher-header.md) | TBD |
| [FILE_MEMORY_PARTITION_INFORMATION structure](ns-wdm--file-memory-partition-information.md) | Stores information about memory partition. This structure is used by the ZwSetInformationFile function. |
| [REG_SET_VALUE_KEY_INFORMATION structure](ns-wdm--reg-set-value-key-information.md) | The REG_SET_VALUE_INFORMATION structure describes a new setting for a registry key's value entry. |
| [KEY_VALUE_PARTIAL_INFORMATION structure](ns-wdm--key-value-partial-information.md) | The KEY_VALUE_PARTIAL_INFORMATION structure defines a subset of the value information available for a value entry of a registry key. |
| [DMA_ADAPTER structure](ns-wdm--dma-adapter~r4.md) | TBD |
| [PCW_BUFFER structure](ns-wdm--pcw-buffer.md) | TBD |
| [PACPI_INTERFACE_STANDARD2 structure](ns-wdm-pacpi-interface-standard2.md) | TBD |
| [IMAGE_POLICY_ENTRY structure](ns-wdm--image-policy-entry.md) | TBD |
| [FILE_POSITION_INFORMATION structure](ns-wdm--file-position-information.md) | The FILE_POSITION_INFORMATION structure is used as an argument to routines that query or set file information. |
| [BOOTDISK_INFORMATION_LITE structure](ns-wdm--bootdisk-information-lite.md) | TBD |
| [KBUGCHECK_ADD_PAGES structure](ns-wdm--kbugcheck-add-pages.md) | The KBUGCHECK_ADD_PAGES structure describes one or more pages of driver-supplied data to be written by a BugCheckAddPagesCallback callback routine to the crash dump file. |
| [SLIST_HEADER structure](ns-wdm--slist-header~r1.md) | TBD |
| [CM_PARTIAL_RESOURCE_DESCRIPTOR structure](ns-wdm--cm-partial-resource-descriptor.md) | The CM_PARTIAL_RESOURCE_DESCRIPTOR structure specifies one or more system hardware resources, of a single type, assigned to a device. |
| [IO_CSQ structure](ns-wdm--io-csq.md) | TBD |
| [OB_POST_DUPLICATE_HANDLE_INFORMATION structure](ns-wdm--ob-post-duplicate-handle-information.md) | The OB_POST_DUPLICATE_HANDLE_INFORMATION structure provides information to an ObjectPostCallback routine about a thread or process handle that has been duplicated. |
| [FILE_SFIO_RESERVE_INFORMATION structure](ns-wdm--file-sfio-reserve-information.md) | TBD |
| [CM_DISK_GEOMETRY_DEVICE_DATA structure](ns-wdm--cm-disk-geometry-device-data.md) | TBD |
| [REG_CALLBACK_CONTEXT_CLEANUP_INFORMATION structure](ns-wdm--reg-callback-context-cleanup-information.md) | The REG_CALLBACK_CONTEXT_CLEANUP_INFORMATION structure contains information that a driver's RegistryCallback routine can use to free resources that the driver previously allocated for the context that is associated with a registry object. |
| [REG_LOAD_KEY_INFORMATION structure](ns-wdm--reg-load-key-information.md) | The REG_LOAD_KEY_INFORMATION structure contains information about a registry hive that is being loaded. |
| [PCI_EXPRESS_ATS_CONTROL_REGISTER structure](ns-wdm--pci-express-ats-control-register.md) | TBD |
| [VIRTUAL_CHANNEL_STATUS structure](ns-wdm--virtual-channel-status.md) | TBD |
| [EXCEPTION_RECORD structure](ns-wdm--exception-record.md) | TBD |
| [PCI_EXPRESS_SRIOV_STATUS structure](ns-wdm--pci-express-sriov-status.md) | TBD |
| [CM_FULL_RESOURCE_DESCRIPTOR structure](ns-wdm--cm-full-resource-descriptor.md) | The CM_FULL_RESOURCE_DESCRIPTOR structure specifies a set of system hardware resources of various types, assigned to a device that is connected to a specific bus. This structure is contained within a CM_RESOURCE_LIST structure. |
| [PCI_EXPRESS_SRIOV_CAPABILITY structure](ns-wdm--pci-express-sriov-capability.md) | TBD |
| [LUID_AND_ATTRIBUTES structure](ns-wdm--luid-and-attributes.md) | LUID_AND_ATTRIBUTES represents a locally unique identifier (LUID) and its attributes. |
| [IO_SECURITY_CONTEXT structure](ns-wdm--io-security-context.md) | The IO_SECURITY_CONTEXT structure represents the security context of an IRP_MJ_CREATE request. |
| [TRANSACTION_PROPERTIES_INFORMATION structure](ns-wdm--transaction-properties-information.md) | The TRANSACTION_PROPERTIES_INFORMATION structure contains a transaction object's properties. |
| [CM_MCA_POS_DATA structure](ns-wdm--cm-mca-pos-data.md) | The CM_MCA_POS_DATA structure is obsolete. It defines IBM-compatible MCA POS configuration information for a slot. |
| [VIRTUAL_RESOURCE_STATUS structure](ns-wdm--virtual-resource-status.md) | TBD |
| [REG_RESTORE_KEY_INFORMATION structure](ns-wdm--reg-restore-key-information.md) | The REG_RESTORE_KEY_INFORMATION structure contains the information for a registry key that is about to be restored. |
| [EXCEPTION_POINTERS structure](ns-wdm--exception-pointers.md) | TBD |
| [REG_QUERY_KEY_INFORMATION structure](ns-wdm--reg-query-key-information.md) | The REG_QUERY_KEY_INFORMATION structure describes the metadata that is about to be queried for a key. |
| [EISA_PORT_DESCRIPTOR structure](ns-wdm--eisa-port-descriptor.md) | TBD |
| [KDPC structure](ns-wdm--kdpc~r1.md) | TBD |
| [RTL_QUERY_REGISTRY_TABLE structure](ns-wdm--rtl-query-registry-table.md) | TBD |
| [PCI_EXPRESS_VIRTUAL_CHANNEL_CAPABILITY structure](ns-wdm--pci-express-virtual-channel-capability.md) | TBD |
| [SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX structure](ns-wdm--system-logical-processor-information-ex~r1.md) | TBD |
| [KBUGCHECK_DUMP_IO structure](ns-wdm--kbugcheck-dump-io.md) | The KBUGCHECK_DUMP_IO structure describes an I/O operation on the crash dump file. |
| [PCI_EXPRESS_CORRECTABLE_ERROR_MASK structure](ns-wdm--pci-express-correctable-error-mask.md) | The PCI_EXPRESS_CORRECTABLE_ERROR_MASK structure describes a PCI Express (PCIe) correctable error mask register of a PCIe advanced error reporting capability structure. |
| [PNP_REPLACE_PROCESSOR_LIST structure](ns-wdm--pnp-replace-processor-list.md) | TBD |
| [KRESOURCEMANAGER structure](ns-wdm--kresourcemanager.md) | TBD |
| [PSET_POWER_SETTING_VALUE structure](ns-wdm-pset-power-setting-value.md) | TBD |
| [KMUTANT structure](ns-wdm--kmutant.md) | TBD |
| [APPLICATIONLAUNCH_SETTING_VALUE structure](ns-wdm--applicationlaunch-setting-value.md) | TBD |
| [DEVICE_OBJECT_POWER_EXTENSION structure](ns-wdm--device-object-power-extension.md) | TBD |
| [DMA_ADAPTER structure](ns-wdm--dma-adapter~r2.md) | TBD |
| [DISK_PARTITION structure](ns-wdm--disk-partition.md) | TBD |
| [PCI_EXPRESS_PRI_CONTROL_REGISTER structure](ns-wdm--pci-express-pri-control-register.md) | TBD |
| [SE_ADT_OBJECT_TYPE structure](ns-wdm--se-adt-object-type.md) | TBD |
| [KDEVICE_QUEUE_ENTRY structure](ns-wdm--kdevice-queue-entry.md) | TBD |
| [PCI_EXPRESS_LINK_QUIESCENT_INTERFACE structure](ns-wdm--pci-express-link-quiescent-interface.md) | TBD |
| [DEVOBJ_EXTENSION structure](ns-wdm--devobj-extension~r1.md) | TBD |
| [CLS_CONTAINER_INFORMATION structure](ns-wdm--cls-container-information.md) | TBD |
| [IO_REMOVE_LOCK structure](ns-wdm--io-remove-lock.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [DRIVER_RUNTIME_INIT_FLAGS enumeration](ne-wdm--driver-runtime-init-flags.md) | TBD |
| [IO_ALLOCATION_ACTION enumeration](ne-wdm--io-allocation-action.md) | The IO_ALLOCATION_ACTION enumerated type is used to specify return values for AdapterControl and ControllerControl routines. |
| [KBUGCHECK_BUFFER_DUMP_STATE enumeration](ne-wdm--kbugcheck-buffer-dump-state.md) | TBD |
| [CPU_SET_INFORMATION_TYPE enumeration](ne-wdm--cpu-set-information-type.md) | TBD |
| [SE_IMAGE_VERIFICATION_CALLBACK_TYPE enumeration](ne-wdm--se-image-verification-callback-type.md) | TBD |
| [USER_ACTIVITY_PRESENCE enumeration](ne-wdm--user-activity-presence.md) | TBD |
| [SECURITY_OPERATION_CODE enumeration](ne-wdm--security-operation-code.md) | TBD |
| [IO_SESSION_EVENT enumeration](ne-wdm--io-session-event.md) | The IO_SESSION_EVENT enumeration indicates the type of session event for which a driver is receiving notification. |
| [IO_CONTAINER_INFORMATION_CLASS enumeration](ne-wdm--io-container-information-class.md) | The IO_CONTAINER_INFORMATION_CLASS enumeration contains constants that indicate the classes of system information that a kernel-mode driver can request. |
| [INTERFACE_TYPE enumeration](ne-wdm--interface-type.md) | The INTERFACE_TYPE enumeration indicates the bus type. |
| [KINTERRUPT_MODE enumeration](ne-wdm--kinterrupt-mode.md) | The KINTERRUPT_MODE enumeration type indicates whether an interrupt is level-triggered or edge-triggered. |
| [POWER_REQUEST_TYPE enumeration](ne-wdm--power-request-type.md) | The POWER_REQUEST_TYPE enumeration indicates the power request type. |
| [CM_SERVICE_NODE_TYPE enumeration](ne-wdm--cm-service-node-type.md) | TBD |
| [PCW_CALLBACK_TYPE enumeration](ne-wdm--pcw-callback-type.md) | The PCW_CALLBACK_TYPE enumeration defines the notification type to send to the registered provider of the counter set. A provider passes a pointer to this enumeration as a parameter to the PcwCallback function. |
| [SECURITY_IMPERSONATION_LEVEL enumeration](ne-wdm--security-impersonation-level.md) | The SECURITY_IMPERSONATION_LEVEL enumeration type contains values that specify security impersonation levels. Security impersonation levels govern the degree to which a server process can act on behalf of a client process. |
| [PO_FX_PERF_STATE_TYPE enumeration](ne-wdm--po-fx-perf-state-type.md) | The PO_FX_PERF_STATE_TYPE enumeration contains values that describe the type of performance states in a PO_FX_COMPONENT_PERF_SET. |
| [DMA_WIDTH enumeration](ne-wdm--dma-width.md) | TBD |
| [IRQ_DEVICE_POLICY_USHORT enumeration](ne-wdm--irq-device-policy-ushort.md) | TBD |
| [CLFS_CONTEXT_MODE enumeration](ne-wdm--clfs-context-mode.md) | The CLFS_CONTEXT_MODE enumeration indicates the type of sequence that the Common Log File System (CLFS) driver follows when it reads a set of records from a stream. |
| [KD_OPTION enumeration](ne-wdm--kd-option.md) | TBD |
| [SECTION_INHERIT enumeration](ne-wdm--section-inherit.md) | TBD |
| [RESOURCEMANAGER_INFORMATION_CLASS enumeration](ne-wdm--resourcemanager-information-class.md) | The RESOURCEMANAGER_INFORMATION_CLASS enumeration identifies the type of information that the ZwQueryInformationResourceManager routine can retrieve for a resource manager object. |
| [MODE enumeration](ne-wdm--mode.md) | TBD |
| [D3COLD_LAST_TRANSITION_STATUS enumeration](ne-wdm--d3cold-last-transition-status.md) | The D3COLD_LAST_TRANSITION_STATUS enumeration indicates whether the most recent transition to the D3hot device power state was followed by a transition to the D3cold device power state. |
| [PO_FX_PERF_STATE_UNIT enumeration](ne-wdm--po-fx-perf-state-unit.md) | The PO_FX_PERF_STATE_UNIT enumeration contains values that describe the type of unit that is controlled by the performance states in a PO_FX_COMPONENT_PERF_SET. |
| [PROCESSOR_CACHE_TYPE enumeration](ne-wdm--processor-cache-type.md) | TBD |
| [KBUGCHECK_DUMP_IO_TYPE enumeration](ne-wdm--kbugcheck-dump-io-type.md) | The KBUGCHECK_DUMP_IO_TYPE enumeration type identifies the type of a section of data within a crash dump file. |
| [FSINFOCLASS enumeration](ne-wdm--fsinfoclass.md) | TBD |
| [IMAGE_POLICY_ENTRY_TYPE enumeration](ne-wdm--image-policy-entry-type.md) | TBD |
| [CM_SHARE_DISPOSITION enumeration](ne-wdm--cm-share-disposition.md) | TBD |
| [CLFS_IOSTATS_CLASS enumeration](ne-wdm--clfs-iostats-class.md) | TBD |
| [POWER_MONITOR_REQUEST_REASON enumeration](ne-wdm-power-monitor-request-reason.md) | TBD |
| [KPROFILE_SOURCE enumeration](ne-wdm--kprofile-source.md) | TBD |
| [SE_IMAGE_TYPE enumeration](ne-wdm--se-image-type.md) | TBD |
| [CM_SERVICE_LOAD_TYPE enumeration](ne-wdm--cm-service-load-type.md) | TBD |
| [TRANSACTIONMANAGER_INFORMATION_CLASS enumeration](ne-wdm--transactionmanager-information-class.md) | The TRANSACTIONMANAGER_INFORMATION_CLASS enumeration specifies the type of information that the ZwQueryInformationTransactionManager routine can retrieve for a transaction manager object. |
| [KE_PROCESSOR_CHANGE_NOTIFY_STATE enumeration](ne-wdm-ke-processor-change-notify-state.md) | TBD |
| [KEY_INFORMATION_CLASS enumeration](ne-wdm--key-information-class.md) | The KEY_INFORMATION_CLASS enumeration type represents the type of information to supply about a registry key. |
| [SE_ADT_PARAMETER_TYPE enumeration](ne-wdm--se-adt-parameter-type.md) | TBD |
| [CLS_IOSTATS_CLASS enumeration](ne-wdm--cls-iostats-class.md) | TBD |
| [SYSTEM_POWER_CONDITION enumeration](ne-wdm-system-power-condition.md) | TBD |
| [DMA_COMPLETION_STATUS enumeration](ne-wdm-dma-completion-status.md) | The DMA_COMPLETION_STATUS enumeration describes the completion status of a DMA transfer. |
| [DEVICE_RELATION_TYPE enumeration](ne-wdm--device-relation-type.md) | TBD |
| [MM_MDL_PAGE_CONTENTS_STATE enumeration](ne-wdm--mm-mdl-page-contents-state.md) | TBD |
| [TRACE_INFORMATION_CLASS enumeration](ne-wdm--trace-information-class.md) | The TRACE_INFORMATION_CLASS enumeration type is used to indicate types of information associated with a WMI event tracing session. |
| [LOGICAL_PROCESSOR_RELATIONSHIP enumeration](ne-wdm--logical-processor-relationship.md) | TBD |
| [KSPIN_LOCK_QUEUE_NUMBER enumeration](ne-wdm--kspin-lock-queue-number.md) | TBD |
| [IO_ACCESS_MODE enumeration](ne-wdm--io-access-mode.md) | TBD |
| [BOUND_CALLBACK_STATUS enumeration](ne-wdm--bound-callback-status.md) | The BOUND_CALLBACK_STATUS enumeration indicates how a user-mode bounds exception was processed by the BoundCallback function. |
| [FILE_INFORMATION_CLASS enumeration](ne-wdm--file-information-class.md) | A value that specifies which structure to use to query or set information for a file object. |
| [CLFS_LOG_ARCHIVE_MODE enumeration](ne-wdm--clfs-log-archive-mode.md) | TBD |
| [KTMOBJECT_TYPE enumeration](ne-wdm--ktmobject-type.md) | The KTMOBJECT_TYPE enumeration identifies the types of objects that KTM supports. |
| [IO_CONTAINER_NOTIFICATION_CLASS enumeration](ne-wdm--io-container-notification-class.md) | The IO_CONTAINER_NOTIFICATION_CLASS enumeration contains constants that indicate the classes of events for which a kernel-mode driver can register to receive notifications. |
| [CLS_CONTEXT_MODE enumeration](ne-wdm--cls-context-mode.md) | TBD |
| [INTEL_CACHE_TYPE enumeration](ne-wdm--intel-cache-type.md) | TBD |
| [MM_PAGE_PRIORITY enumeration](ne-wdm--mm-page-priority.md) | TBD |
| [FIRMWARE_TYPE enumeration](ne-wdm--firmware-type.md) | TBD |
| [IO_PAGING_PRIORITY enumeration](ne-wdm--io-paging-priority.md) | The IO_PAGING_PRIORITY enumeration describes the priority value for a paging I/O IRP. |
| [KDPC_IMPORTANCE enumeration](ne-wdm--kdpc-importance.md) | TBD |
| [PDEVICE_TEXT_TYPE enumeration](ne-wdm-pdevice-text-type.md) | TBD |
| [DEVICE_REMOVAL_POLICY enumeration](ne-wdm--device-removal-policy.md) | The DEVICE_REMOVAL_POLICY enumeration describes a device's removal policy. |
| [IRQ_GROUP_POLICY enumeration](ne-wdm--irq-group-policy.md) | TBD |
| [MEMORY_CACHING_TYPE enumeration](ne-wdm--memory-caching-type.md) | The MEMORY_CACHING_TYPE enumeration type specifies the permitted caching behavior when allocating or mapping memory. |
| [IO_SESSION_STATE enumeration](ne-wdm--io-session-state.md) | The IO_SESSION_STATE enumeration contains constants that indicate the current state of a user session. |
| [SYSTEM_POWER_STATE enumeration](ne-wdm--system-power-state.md) | The SYSTEM_POWER_STATE enumeration type is used to indicate a system power state. |
| [DRIVER_RUNTIME_INIT_FLAGS enumeration](ne-wdm--driver-runtime-init-flags~r1.md) | TBD |
| [IO_NOTIFICATION_EVENT_CATEGORY enumeration](ne-wdm--io-notification-event-category.md) | TBD |
| [CLFS_MGMT_POLICY_TYPE enumeration](ne-wdm--clfs-mgmt-policy-type.md) | The CLFS_MGMT_POLICY_TYPE enumeration type identifies the type of a CLFS management policy. |
| [PBUS_QUERY_ID_TYPE enumeration](ne-wdm-pbus-query-id-type.md) | TBD |
| [POWER_PLATFORM_ROLE enumeration](ne-wdm--power-platform-role.md) | TBD |
| [CM_ERROR_CONTROL_TYPE enumeration](ne-wdm--cm-error-control-type.md) | TBD |
| [KBUGCHECK_CALLBACK_REASON enumeration](ne-wdm--kbugcheck-callback-reason.md) | The KBUGCHECK_CALLBACK_REASON enumeration type specifies the situations in which a bug-check callback executes. |
| [DMA_SPEED enumeration](ne-wdm--dma-speed.md) | TBD |
| [DIRECTORY_NOTIFY_INFORMATION_CLASS enumeration](ne-wdm--directory-notify-information-class.md) | A value that specifies which structure to use to query or set information for a files in a directory. |
| [OS_DEPLOYEMENT_STATE_VALUES enumeration](ne-wdm--os-deployement-state-values.md) | TBD |
| [POOL_TYPE enumeration](ne-wdm--pool-type.md) | The POOL_TYPE enumeration type specifies the type of system memory to allocate. |
| [KEY_VALUE_INFORMATION_CLASS enumeration](ne-wdm--key-value-information-class.md) | The KEY_VALUE_INFORMATION_CLASS enumeration type specifies the type of information to supply about the value of a registry key. |
| [IMAGE_POLICY_ID enumeration](ne-wdm--image-policy-id.md) | TBD |
| [REG_NOTIFY_CLASS enumeration](ne-wdm--reg-notify-class.md) | TBD |
| [POWER_INFORMATION_LEVEL enumeration](ne-wdm-power-information-level.md) | Indicates power level information. |
| [KWAIT_REASON enumeration](ne-wdm--kwait-reason.md) | TBD |
| [ALTERNATIVE_ARCHITECTURE_TYPE enumeration](ne-wdm--alternative-architecture-type.md) | TBD |
| [KEY_SET_INFORMATION_CLASS enumeration](ne-wdm--key-set-information-class.md) | The KEY_SET_INFORMATION_CLASS enumeration type represents the type of information to set for a registry key. |
| [TRANSACTION_STATE enumeration](ne-wdm--transaction-state.md) | The TRANSACTION_STATE enumeration defines the states that KTM can assign to a transaction. |
| [PPOWER_USER_PRESENCE_TYPE enumeration](ne-wdm-ppower-user-presence-type.md) | TBD |
| [DEVICE_REGISTRY_PROPERTY enumeration](ne-wdm-device-registry-property.md) | TBD |
| [DEVICE_INSTALL_STATE enumeration](ne-wdm--device-install-state.md) | The DEVICE_INSTALL_STATE enumeration describes a device's installation state. |
| [OB_PREOP_CALLBACK_STATUS enumeration](ne-wdm--ob-preop-callback-status.md) | TBD |
| [ENLISTMENT_INFORMATION_CLASS enumeration](ne-wdm--enlistment-information-class.md) | The ENLISTMENT_INFORMATION_CLASS enumeration identifies the type of information that the ZwSetInformationEnlistment routine can set and that the ZwQueryInformationEnlistment routine can retrieve for an enlistment object. |
| [IO_PRIORITY_HINT enumeration](ne-wdm--io-priority-hint.md) | The IO_PRIORITY_HINT enumeration type specifies the priority hint for an IRP. |
| [CREATE_FILE_TYPE enumeration](ne-wdm--create-file-type.md) | TBD |
| [PCI_ACS_BIT enumeration](ne-wdm--pci-acs-bit.md) | TBD |
| [POWER_STATE_TYPE enumeration](ne-wdm--power-state-type.md) | The POWER_STATE_TYPE enumeration type indicates that a power state value is a system power state or a device power state. |
| [IO_ACCESS_TYPE enumeration](ne-wdm--io-access-type.md) | TBD |
| [KINTERRUPT_POLARITY enumeration](ne-wdm--kinterrupt-polarity.md) | The KINTERRUPT_POLARITY enumeration indicates how a device signals an interrupt request on an interrupt line. |
| [TRANSACTION_INFORMATION_CLASS enumeration](ne-wdm--transaction-information-class.md) | The TRANSACTION_INFORMATION_CLASS enumeration specifies the type of information that ZwSetInformationTransaction can set and ZwQueryInformationTransaction can retrieve for a transaction manager object. |
| [IRQ_DEVICE_POLICY enumeration](ne-wdm--irq-device-policy.md) | The IRQ_DEVICE_POLICY enumeration type indicates the policy the operating system can use to assign the interrupts from a device to different processors. |
| [LOCK_OPERATION enumeration](ne-wdm--lock-operation.md) | The LOCK_OPERATION enumeration specifies the type of access that is appropriate for a type of I/O operation. |
| [CLFS_MGMT_NOTIFICATION_TYPE enumeration](ne-wdm--clfs-mgmt-notification-type.md) | TBD |
| [DEVICE_POWER_STATE enumeration](ne-wdm--device-power-state.md) | The DEVICE_POWER_STATE enumeration type indicates a device power state. |
| [EX_POOL_PRIORITY enumeration](ne-wdm--ex-pool-priority.md) | TBD |
| [IRQ_PRIORITY enumeration](ne-wdm--irq-priority.md) | The IRQ_PRIORITY enumeration type indicates the priority the system should give to servicing a device's interrupts. |
| [PPOWER_ACTION enumeration](ne-wdm-ppower-action.md) | TBD |
| [LATENCY_TIME enumeration](ne-wdm-latency-time.md) | TBD |
| [DEVICE_USAGE_NOTIFICATION_TYPE enumeration](ne-wdm--device-usage-notification-type.md) | TBD |
| [MM_SYSTEM_SIZE enumeration](ne-wdm--mm-system-size.md) | TBD |
| [MEMORY_CACHING_TYPE_ORIG enumeration](ne-wdm--memory-caching-type-orig.md) | TBD |
| [DEVICE_WAKE_DEPTH enumeration](ne-wdm--device-wake-depth.md) | The DEVICE_WAKE_DEPTH enumeration specifies the deepest device power state from which a device can trigger a wake signal. |
| [TRANSACTION_OUTCOME enumeration](ne-wdm--transaction-outcome.md) | The TRANSACTION_OUTCOME enumeration defines the outcomes (results) that KTM can assign to a transaction. |
| [POWER_MONITOR_REQUEST_TYPE enumeration](ne-wdm--power-monitor-request-type.md) | TBD |
| [WORK_QUEUE_TYPE enumeration](ne-wdm--work-queue-type.md) | The WORK_QUEUE_TYPE enumeration type indicates the type of system worker thread that handles a work item. |
| [MONITOR_DISPLAY_STATE enumeration](ne-wdm--monitor-display-state.md) | Indicates the power state of the monitor being displayed on. |
| [PO_THERMAL_REQUEST_TYPE enumeration](ne-wdm--po-thermal-request-type.md) | TBD |
| [POOL_TYPE enumeration](ne-wdm--pool-type~r1.md) | The POOL_TYPE enumeration type specifies the type of system memory to allocate. |
| [DEVICE_RESET_TYPE enumeration](ne-wdm--device-reset-type.md) | The DEVICE_RESET_TYPE enumeration specifies the type of device reset that is being requested by a call to the DeviceReset routine of the GUID_DEVICE_RESET_INTERFACE_STANDARD interface. |
| [CLS_LOG_INFORMATION_CLASS enumeration](ne-wdm--cls-log-information-class.md) | TBD |
| [IO_COMPLETION_ROUTINE_RESULT enumeration](ne-wdm--io-completion-routine-result.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PCLFS_CLIENT_LOG_UNPINNED_CALLBACK callback function](nc-wdm-pclfs-client-log-unpinned-callback.md) | TBD |
| [RTL_QUERY_REGISTRY_ROUTINE callback function](nc-wdm-rtl-query-registry-routine.md) | TBD |
| [PBUILD_SCATTER_GATHER_LIST callback function](nc-wdm-pbuild-scatter-gather-list.md) | TBD |
| [PREAD_DMA_COUNTER callback function](nc-wdm-pread-dma-counter.md) | TBD |
| [PPUT_DMA_ADAPTER callback function](nc-wdm-pput-dma-adapter.md) | TBD |
| [PALLOCATE_COMMON_BUFFER_EX callback function](nc-wdm-pallocate-common-buffer-ex.md) | TBD |
| [PGPE_DISCONNECT_VECTOR callback function](nc-wdm-pgpe-disconnect-vector.md) | TBD |
| [KSERVICE_ROUTINE callback function](nc-wdm-kservice-routine.md) | TBD |
| [PPCI_EXPRESS_ROOT_PORT_READ_CONFIG_SPACE callback function](nc-wdm-ppci-express-root-port-read-config-space.md) | TBD |
| [CALLBACK_FUNCTION callback function](nc-wdm-callback-function.md) | TBD |
| [PO_FX_POWER_CONTROL_CALLBACK callback function](nc-wdm-po-fx-power-control-callback.md) | TBD |
| [PREPLACE_BEGIN callback function](nc-wdm-preplace-begin.md) | TBD |
| [PDEVICE_RESET_HANDLER callback function](nc-wdm-pdevice-reset-handler.md) | TBD |
| [PFN_NT_OPEN_TRANSACTION callback function](nc-wdm-pfn-nt-open-transaction.md) | TBD |
| [PGET_DMA_DOMAIN callback function](nc-wdm-pget-dma-domain.md) | TBD |
| [POB_PRE_OPERATION_CALLBACK callback function](nc-wdm-pob-pre-operation-callback.md) | TBD |
| [PREPLACE_MAP_MEMORY callback function](nc-wdm-preplace-map-memory.md) | TBD |
| [PROCESSOR_CALLBACK_FUNCTION callback function](nc-wdm-processor-callback-function.md) | TBD |
| [PCALCULATE_SCATTER_GATHER_LIST_SIZE callback function](nc-wdm-pcalculate-scatter-gather-list-size.md) | TBD |
| [PCLFS_CLIENT_ADVANCE_TAIL_CALLBACK callback function](nc-wdm-pclfs-client-advance-tail-callback.md) | TBD |
| [PINITIALIZE_DMA_TRANSFER_CONTEXT callback function](nc-wdm-pinitialize-dma-transfer-context.md) | TBD |
| [ETWENABLECALLBACK callback function](nc-wdm-etwenablecallback.md) | TBD |
| [PALLOCATE_DOMAIN_COMMON_BUFFER callback function](nc-wdm-pallocate-domain-common-buffer.md) | TBD |
| [PFN_NT_SET_INFORMATION_TRANSACTION callback function](nc-wdm-pfn-nt-set-information-transaction.md) | TBD |
| [PO_FX_DEVICE_POWER_NOT_REQUIRED_CALLBACK callback function](nc-wdm-po-fx-device-power-not-required-callback.md) | TBD |
| [GET_VIRTUAL_FUNCTION_PROBED_BARS callback function](nc-wdm-get-virtual-function-probed-bars.md) | TBD |
| [PIO_CONTAINER_NOTIFICATION_FUNCTION callback function](nc-wdm-pio-container-notification-function.md) | TBD |
| [PO_FX_DEVICE_POWER_REQUIRED_CALLBACK callback function](nc-wdm-po-fx-device-power-required-callback.md) | TBD |
| [PO_FX_COMPONENT_CRITICAL_TRANSITION_CALLBACK callback function](nc-wdm-po-fx-component-critical-transition-callback.md) | TBD |
| [GET_VIRTUAL_DEVICE_RESOURCES callback function](nc-wdm-get-virtual-device-resources.md) | TBD |
| [KMESSAGE_SERVICE_ROUTINE callback function](nc-wdm-kmessage-service-routine.md) | TBD |
| [GET_SET_DEVICE_DATA callback function](nc-wdm-get-set-device-data.md) | TBD |
| [PBUILD_SCATTER_GATHER_LIST_EX callback function](nc-wdm-pbuild-scatter-gather-list-ex.md) | TBD |
| [PGPE_ENABLE_EVENT callback function](nc-wdm-pgpe-enable-event.md) | TBD |
| [GET_VIRTUAL_DEVICE_DATA callback function](nc-wdm-get-virtual-device-data.md) | TBD |
| [ALLOCATE_FUNCTION callback function](nc-wdm-allocate-function.md) | TBD |
| [PLEAVE_DMA_DOMAIN callback function](nc-wdm-pleave-dma-domain.md) | TBD |
| [POWER_SETTING_CALLBACK callback function](nc-wdm-power-setting-callback.md) | TBD |
| [PFLUSH_ADAPTER_BUFFERS callback function](nc-wdm-pflush-adapter-buffers.md) | TBD |
| [KSYNCHRONIZE_ROUTINE callback function](nc-wdm-ksynchronize-routine.md) | TBD |
| [PREPLACE_UNLOAD callback function](nc-wdm-preplace-unload.md) | TBD |
| [PFLUSH_ADAPTER_BUFFERS_EX callback function](nc-wdm-pflush-adapter-buffers-ex.md) | TBD |
| [PGET_SCATTER_GATHER_LIST callback function](nc-wdm-pget-scatter-gather-list.md) | TBD |
| [PCONFIGURE_ADAPTER_CHANNEL callback function](nc-wdm-pconfigure-adapter-channel.md) | TBD |
| [NMI_CALLBACK callback function](nc-wdm-nmi-callback.md) | TBD |
| [PFREE_ADAPTER_OBJECT callback function](nc-wdm-pfree-adapter-object.md) | TBD |
| [PFREE_COMMON_BUFFER callback function](nc-wdm-pfree-common-buffer.md) | TBD |
| [EX_CALLBACK_FUNCTION callback function](nc-wdm-ex-callback-function.md) | TBD |
| [DEVICE_CHANGE_COMPLETE_CALLBACK callback function](nc-wdm-device-change-complete-callback.md) | TBD |
| [GET_D3COLD_LAST_TRANSITION_STATUS callback function](nc-wdm-get-d3cold-last-transition-status.md) | TBD |
| [PGET_SCATTER_GATHER_LIST_EX callback function](nc-wdm-pget-scatter-gather-list-ex.md) | TBD |
| [FWMI_NOTIFICATION_CALLBACK callback function](nc-wdm-fwmi-notification-callback.md) | TBD |
| [SECURE_DRIVER_PROCESS_DEREFERENCE callback function](nc-wdm-secure-driver-process-dereference.md) | TBD |
| [PALLOCATE_ADAPTER_CHANNEL_EX callback function](nc-wdm-pallocate-adapter-channel-ex.md) | TBD |
| [CLFS_BLOCK_DEALLOCATION callback function](nc-wdm-clfs-block-deallocation.md) | TBD |
| [KBUGCHECK_CALLBACK_ROUTINE callback function](nc-wdm-kbugcheck-callback-routine.md) | TBD |
| [PFN_NT_QUERY_INFORMATION_TRANSACTION callback function](nc-wdm-pfn-nt-query-information-transaction.md) | TBD |
| [PFN_RTL_IS_NTDDI_VERSION_AVAILABLE callback function](nc-wdm-pfn-rtl-is-ntddi-version-available.md) | TBD |
| [SET_VIRTUAL_DEVICE_DATA callback function](nc-wdm-set-virtual-device-data.md) | TBD |
| [DEVICE_RESET_COMPLETION callback function](nc-wdm-device-reset-completion.md) | TBD |
| [PREPLACE_MIRROR_PHYSICAL_MEMORY callback function](nc-wdm-preplace-mirror-physical-memory.md) | TBD |
| [PIO_DEVICE_EJECT_CALLBACK callback function](nc-wdm-pio-device-eject-callback.md) | TBD |
| [PQUERYEXTENDEDADDRESS callback function](nc-wdm-pqueryextendedaddress.md) | TBD |
| [FREE_FUNCTION_EX callback function](nc-wdm-free-function-ex.md) | TBD |
| [PCANCEL_MAPPED_TRANSFER callback function](nc-wdm-pcancel-mapped-transfer.md) | TBD |
| [PFREE_ADAPTER_CHANNEL callback function](nc-wdm-pfree-adapter-channel.md) | TBD |
| [PUNREGISTER_FOR_DEVICE_NOTIFICATIONS2 callback function](nc-wdm-punregister-for-device-notifications2.md) | TBD |
| [PGET_DMA_TRANSFER_INFO callback function](nc-wdm-pget-dma-transfer-info.md) | TBD |
| [PPUT_SCATTER_GATHER_LIST callback function](nc-wdm-pput-scatter-gather-list.md) | TBD |
| [KSTART_ROUTINE callback function](nc-wdm-kstart-routine.md) | TBD |
| [PBUILD_MDL_FROM_SCATTER_GATHER_LIST callback function](nc-wdm-pbuild-mdl-from-scatter-gather-list.md) | TBD |
| [PREPLACE_END callback function](nc-wdm-preplace-end.md) | TBD |
| [PMM_DLL_INITIALIZE callback function](nc-wdm-pmm-dll-initialize.md) | TBD |
| [PREPLACE_INITIATE_HARDWARE_MIRROR callback function](nc-wdm-preplace-initiate-hardware-mirror.md) | TBD |
| [FREE_FUNCTION callback function](nc-wdm-free-function.md) | TBD |
| [PCI_SET_ACS callback function](nc-wdm-pci-set-acs.md) | TBD |
| [PREPLACE_MIRROR_PLATFORM_MEMORY callback function](nc-wdm-preplace-mirror-platform-memory.md) | TBD |
| [TRANSLATE_BUS_ADDRESS callback function](nc-wdm-translate-bus-address.md) | TBD |
| [PREGISTER_FOR_DEVICE_NOTIFICATIONS2 callback function](nc-wdm-pregister-for-device-notifications2.md) | TBD |
| [CLFS_BLOCK_ALLOCATION callback function](nc-wdm-clfs-block-allocation.md) | TBD |
| [ENABLE_VIRTUALIZATION callback function](nc-wdm-enable-virtualization.md) | TBD |
| [PGPE_DISCONNECT_VECTOR2 callback function](nc-wdm-pgpe-disconnect-vector2.md) | TBD |
| [PO_FX_COMPONENT_ACTIVE_CONDITION_CALLBACK callback function](nc-wdm-po-fx-component-active-condition-callback.md) | TBD |
| [PREPLACE_ENABLE_DISABLE_HARDWARE_QUIESCE callback function](nc-wdm-preplace-enable-disable-hardware-quiesce.md) | TBD |
| [DRIVER_NOTIFICATION_CALLBACK_ROUTINE callback function](nc-wdm-driver-notification-callback-routine.md) | TBD |
| [PO_FX_DRIPS_WATCHDOG_CALLBACK callback function](nc-wdm-po-fx-drips-watchdog-callback.md) | TBD |
| [PGPE_ENABLE_EVENT2 callback function](nc-wdm-pgpe-enable-event2.md) | TBD |
| [PGET_DMA_ALIGNMENT callback function](nc-wdm-pget-dma-alignment.md) | TBD |
| [KBUGCHECK_REASON_CALLBACK_ROUTINE callback function](nc-wdm-kbugcheck-reason-callback-routine.md) | TBD |
| [PFN_NT_CREATE_TRANSACTION callback function](nc-wdm-pfn-nt-create-transaction.md) | TBD |
| [PGPE_CLEAR_STATUS callback function](nc-wdm-pgpe-clear-status.md) | TBD |
| [PPCI_EXPRESS_ROOT_PORT_WRITE_CONFIG_SPACE callback function](nc-wdm-ppci-express-root-port-write-config-space.md) | TBD |
| [WORKER_THREAD_ROUTINE callback function](nc-wdm-worker-thread-routine.md) | TBD |
| [PINTERFACE_DEREFERENCE callback function](nc-wdm-pinterface-dereference.md) | TBD |
| [PCLFS_SET_LOG_SIZE_COMPLETE_CALLBACK callback function](nc-wdm-pclfs-set-log-size-complete-callback.md) | TBD |
| [PGPE_CONNECT_VECTOR2 callback function](nc-wdm-pgpe-connect-vector2.md) | TBD |
| [PREPLACE_GET_MEMORY_DESTINATION callback function](nc-wdm-preplace-get-memory-destination.md) | TBD |
| [GET_IDLE_WAKE_INFO callback function](nc-wdm-get-idle-wake-info.md) | TBD |
| [REQUEST_POWER_COMPLETE callback function](nc-wdm-request-power-complete.md) | TBD |
| [PTM_PROPAGATE_ROUTINE callback function](nc-wdm-ptm-propagate-routine.md) | TBD |
| [PDEVICE_NOTIFY_CALLBACK2 callback function](nc-wdm-pdevice-notify-callback2.md) | TBD |
| [PCANCEL_ADAPTER_CHANNEL callback function](nc-wdm-pcancel-adapter-channel.md) | TBD |
| [POB_POST_OPERATION_CALLBACK callback function](nc-wdm-pob-post-operation-callback.md) | TBD |
| [PCLFS_CLIENT_LFF_HANDLER_COMPLETE_CALLBACK callback function](nc-wdm-pclfs-client-lff-handler-complete-callback.md) | TBD |
| [PGPE_CONNECT_VECTOR callback function](nc-wdm-pgpe-connect-vector.md) | TBD |
| [PO_FX_COMPONENT_IDLE_STATE_CALLBACK callback function](nc-wdm-po-fx-component-idle-state-callback.md) | TBD |
| [GET_D3COLD_CAPABILITY callback function](nc-wdm-get-d3cold-capability.md) | TBD |
| [PUNREGISTER_FOR_DEVICE_NOTIFICATIONS callback function](nc-wdm-punregister-for-device-notifications.md) | TBD |
| [PJOIN_DMA_DOMAIN callback function](nc-wdm-pjoin-dma-domain.md) | TBD |
| [PFN_RTL_IS_SERVICE_PACK_VERSION_INSTALLED callback function](nc-wdm-pfn-rtl-is-service-pack-version-installed.md) | TBD |
| [PINTERFACE_REFERENCE callback function](nc-wdm-pinterface-reference.md) | TBD |
| [PREENUMERATE_SELF callback function](nc-wdm-preenumerate-self.md) | TBD |
| [PGPE_DISABLE_EVENT2 callback function](nc-wdm-pgpe-disable-event2.md) | TBD |
| [PALLOCATE_COMMON_BUFFER callback function](nc-wdm-pallocate-common-buffer.md) | TBD |
| [PMM_DLL_UNLOAD callback function](nc-wdm-pmm-dll-unload.md) | TBD |
| [PREGISTER_FOR_DEVICE_NOTIFICATIONS callback function](nc-wdm-pregister-for-device-notifications.md) | TBD |
| [PIO_APC_ROUTINE callback function](nc-wdm-pio-apc-routine.md) | TBD |
| [PFREE_MAP_REGISTERS callback function](nc-wdm-pfree-map-registers.md) | TBD |
| [PFN_NT_ROLLBACK_TRANSACTION callback function](nc-wdm-pfn-nt-rollback-transaction.md) | TBD |
| [PMAP_TRANSFER_EX callback function](nc-wdm-pmap-transfer-ex.md) | TBD |
| [PGET_DMA_ADAPTER_INFO callback function](nc-wdm-pget-dma-adapter-info.md) | TBD |
| [PGPE_CLEAR_STATUS2 callback function](nc-wdm-pgpe-clear-status2.md) | TBD |
| [PGPE_SERVICE_ROUTINE2 callback function](nc-wdm-pgpe-service-routine2.md) | TBD |
| [PFN_NT_COMMIT_TRANSACTION callback function](nc-wdm-pfn-nt-commit-transaction.md) | TBD |
| [GET_VIRTUAL_DEVICE_LOCATION callback function](nc-wdm-get-virtual-device-location.md) | TBD |
| [PREPLACE_SWAP callback function](nc-wdm-preplace-swap.md) | TBD |
| [PDEBUG_PRINT_CALLBACK callback function](nc-wdm-pdebug-print-callback.md) | TBD |
| [_os_wowa64_rdtsc callback function](nc-wdm--os-wowa64-rdtsc.md) | TBD |
| [PMAP_TRANSFER callback function](nc-wdm-pmap-transfer.md) | TBD |
| [DRIVER_CONTROL callback function](nc-wdm-driver-control.md) | TBD |
| [PREPLACE_DRIVER_INIT callback function](nc-wdm-preplace-driver-init.md) | TBD |
| [ALLOCATE_FUNCTION_EX callback function](nc-wdm-allocate-function-ex.md) | TBD |
| [PGPE_SERVICE_ROUTINE callback function](nc-wdm-pgpe-service-routine.md) | TBD |
| [KIPI_BROADCAST_WORKER callback function](nc-wdm-kipi-broadcast-worker.md) | TBD |
| [SECURE_DRIVER_PROCESS_REFERENCE callback function](nc-wdm-secure-driver-process-reference.md) | TBD |
| [PCRASHDUMP_POWER_ON callback function](nc-wdm-pcrashdump-power-on.md) | TBD |
| [PFLUSH_DMA_BUFFER callback function](nc-wdm-pflush-dma-buffer.md) | TBD |
| [SE_IMAGE_VERIFICATION_CALLBACK_FUNCTION callback function](nc-wdm-se-image-verification-callback-function.md) | TBD |
| [PGPE_DISABLE_EVENT callback function](nc-wdm-pgpe-disable-event.md) | TBD |
| [SET_D3COLD_SUPPORT callback function](nc-wdm-set-d3cold-support.md) | TBD |
| [PREPLACE_SET_PROCESSOR_ID callback function](nc-wdm-preplace-set-processor-id.md) | TBD |
| [DRIVER_LIST_CONTROL callback function](nc-wdm-driver-list-control.md) | TBD |
| [PTM_RM_NOTIFICATION callback function](nc-wdm-ptm-rm-notification.md) | TBD |
| [PALLOCATE_ADAPTER_CHANNEL callback function](nc-wdm-pallocate-adapter-channel.md) | TBD |
| [PO_FX_COMPONENT_IDLE_CONDITION_CALLBACK callback function](nc-wdm-po-fx-component-idle-condition-callback.md) | TBD |
| [PO_FX_COMPONENT_PERF_STATE_CALLBACK callback function](nc-wdm-po-fx-component-perf-state-callback.md) | TBD |
| [GET_SDEV_IDENTIFIER callback function](nc-wdm-get-sdev-identifier.md) | TBD |
| [PDEVICE_NOTIFY_CALLBACK callback function](nc-wdm-pdevice-notify-callback.md) | TBD |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_CANCEL_DEVICE_WAKE IOCTL](ni-wdm-ioctl-cancel-device-wake.md) | TBD |
| [IOCTL_SET_DEVICE_WAKE IOCTL](ni-wdm-ioctl-set-device-wake.md) | TBD |
| [IOCTL_QUERY_DEVICE_POWER_STATE IOCTL](ni-wdm-ioctl-query-device-power-state.md) | TBD |

This header is used in these topics:

- [kernel](..content/_kernel)
- [PCI](..content/_PCI)
- [devtest](..content/_devtest)
- [ifsk](..content/_ifsk)
