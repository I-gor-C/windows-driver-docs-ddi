# Windows kernel

Overview of the Windows kernel technology.

To develop Windows kernel, you need these headers:

 * [aux_klib.h](..\aux_klib\index.md)
 * [d3dkmthk.h](..\d3dkmthk\index.md)
 * [evntrace.h](..\evntrace\index.md)
 * [iointex.h](..\iointex\index.md)
 * [miniport.h](..\miniport\index.md)
 * [ntddk.h](..\ntddk\index.md)
 * [ntddsfio.h](..\ntddsfio\index.md)
 * [ntddsysenv.h](..\ntddsysenv\index.md)
 * [ntifs.h](..\ntifs\index.md)
 * [ntintsafe.h](..\ntintsafe\index.md)
 * [ntnls.h](..\ntnls\index.md)
 * [ntstrsafe.h](..\ntstrsafe\index.md)
 * [pep_x.h](..\pep_x\index.md)
 * [pepfx.h](..\pepfx\index.md)
 * [poclass.h](..\poclass\index.md)
 * [procgrp.h](..\procgrp\index.md)
 * [pwmutil.h](..\pwmutil\index.md)
 * [vpci.h](..\vpci\index.md)
 * [wdm.h](..\wdm\index.md)
 * [wdmsec.h](..\wdmsec\index.md)
 * [wmilib.h](..\wmilib\index.md)
 * [wmistr.h](..\wmistr\index.md)
 * [wudfwdm.h](..\wudfwdm\index.md)

For the programming guide, see [Windows kernel](https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel).

## Functions

| Title   | Description   |
| ---- |:---- |
| [AppendTailList function](..\wdm\nf-wdm-appendtaillist.md) | The AppendTailList routine appends a doubly linked list of LIST_ENTRY structures to the tail of another doubly linked list of LIST_ENTRY structures. |
| [AppendTailList function](..\wdm\nf-wdm-appendtaillist~r1.md) | The AppendTailList routine appends a doubly linked list of LIST_ENTRY structures to the tail of another doubly linked list of LIST_ENTRY structures. |
| [AuxKlibEnumerateSystemFirmwareTables function](..\aux_klib\nf-aux-klib-auxklibenumeratesystemfirmwaretables.md) | The AuxKlibEnumerateSystemFirmwareTables routine enumerates all system firmware tables of the specified type. |
| [AuxKlibGetBugCheckData function](..\aux_klib\nf-aux-klib-auxklibgetbugcheckdata.md) | The AuxKlibGetBugCheckData routine retrieves information about a bug check that has just occurred. |
| [AuxKlibGetImageExportDirectory function](..\aux_klib\nf-aux-klib-auxklibgetimageexportdirectory.md) | The AuxKlibGetImageExportDirectory routine returns an image module's export directory. |
| [AuxKlibGetSystemFirmwareTable function](..\aux_klib\nf-aux-klib-auxklibgetsystemfirmwaretable.md) | The AuxKlibGetSystemFirmwareTable routine retrieves the specified firmware table from the firmware table provider. |
| [AuxKlibInitialize function](..\aux_klib\nf-aux-klib-auxklibinitialize.md) | The AuxKlibInitialize routine initializes the Auxiliary Kernel-Mode Library. |
| [AuxKlibQueryModuleInformation function](..\aux_klib\nf-aux-klib-auxklibquerymoduleinformation.md) | The AuxKlibQueryModuleInformation routine retrieves information about the image modules that the operating system has loaded. |
| [ClfsAddLogContainer function](..\wdm\nf-wdm-clfsaddlogcontainer.md) | The ClfsAddLogContainer routine adds a container to a CLFS log. |
| [ClfsAddLogContainerSet function](..\wdm\nf-wdm-clfsaddlogcontainerset.md) | The ClfsAddLogContainerSet routine atomically adds a set of containers to a CLFS log. |
| [ClfsAdvanceLogBase function](..\wdm\nf-wdm-clfsadvancelogbase.md) | The ClfsAdvanceLogBase routine sets the base LSN of a CLFS stream. |
| [ClfsAlignReservedLog function](..\wdm\nf-wdm-clfsalignreservedlog.md) | The ClfsAlignReservedLog routine calculates the size of the space that must be reserved for a specified set of records. The size calculation includes the space required for headers and the space required for sector alignment. |
| [ClfsAllocReservedLog function](..\wdm\nf-wdm-clfsallocreservedlog.md) | The ClfsAllocReservedLog routine reserves space in a marshalling area for a set of records. |
| [ClfsCloseAndResetLogFile function](..\wdm\nf-wdm-clfscloseandresetlogfile.md) | The ClfsCloseAndResetLogFile routine releases all references to a specified log file object and marks its associated stream for reset. |
| [ClfsCloseLogFileObject function](..\wdm\nf-wdm-clfscloselogfileobject.md) | The ClfsCloseLogFileObject routine releases all references to a log file object. |
| [ClfsCreateLogFile function](..\wdm\nf-wdm-clfscreatelogfile.md) | The ClfsCreateLogFile routine creates or opens a CLFS stream. If necessary, ClfsCreateLogFile also creates the underlying physical log that holds the stream's records. |
| [ClfsCreateMarshallingArea function](..\wdm\nf-wdm-clfscreatemarshallingarea.md) | The ClfsCreateMarshallingArea routine creates a marshalling area for a CLFS stream and returns a pointer to an opaque context that represents the new marshalling area. |
| [ClfsCreateScanContext function](..\wdm\nf-wdm-clfscreatescancontext.md) | The ClfsCreateScanContext routine creates a scan context that can be used to iterate over the containers of a specified CLFS log. |
| [ClfsDeleteLogByPointer function](..\wdm\nf-wdm-clfsdeletelogbypointer.md) | The ClfsDeleteLogByPointer routine marks a CLFS stream for deletion. |
| [ClfsDeleteLogFile function](..\wdm\nf-wdm-clfsdeletelogfile.md) | The ClfsDeleteLogFile routine marks a CLFS stream for deletion. |
| [ClfsDeleteMarshallingArea function](..\wdm\nf-wdm-clfsdeletemarshallingarea.md) | The ClfsDeleteMarshallingArea routine deletes a marshalling area. |
| [ClfsFlushBuffers function](..\wdm\nf-wdm-clfsflushbuffers.md) | The ClfsFlushBuffers routine forces all log I/O blocks in a specified marshalling area to stable storage. |
| [ClfsFlushToLsn function](..\wdm\nf-wdm-clfsflushtolsn.md) | The ClfsFlushToLsn routine forces, to stable storage, all records that have an LSN less than or equal to a specified LSN. |
| [ClfsGetContainerName function](..\wdm\nf-wdm-clfsgetcontainername.md) | The ClfsGetContainerName routine returns the path name of a specified container. |
| [ClfsGetIoStatistics function](..\wdm\nf-wdm-clfsgetiostatistics.md) | The ClfsGetIoStatistics routine returns I/O statistics for a specified CLFS log. |
| [ClfsLsnBlockOffset function](..\wdm\nf-wdm-clfslsnblockoffset.md) | The ClfsLsnBlockOffset routine returns the sector-aligned block offset contained in a specified LSN. |
| [ClfsLsnContainer function](..\wdm\nf-wdm-clfslsncontainer.md) | The ClfsLsnContainer routine returns the logical container identifier contained in a specified LSN. |
| [ClfsLsnCreate function](..\wdm\nf-wdm-clfslsncreate.md) | The ClfsLsnCreate routine creates a log sequence number (LSN), given a container identifier, a block offset, and a record sequence number. |
| [ClfsLsnEqual function](..\wdm\nf-wdm-clfslsnequal.md) | The ClfsLsnEqual routine determines whether two LSNs from the same stream are equal. |
| [ClfsLsnGreater function](..\wdm\nf-wdm-clfslsngreater.md) | The ClfsLsnGreater routine determines whether one LSN is greater than another LSN. The two LSNs must be from the same stream. |
| [ClfsLsnLess function](..\wdm\nf-wdm-clfslsnless.md) | The ClfsLsnLess routine determines whether one LSN is less than another LSN. The two LSNs must be from the same stream. |
| [ClfsLsnNull function](..\wdm\nf-wdm-clfslsnnull.md) | The ClfsLsnNull routine determines whether a specified LSN is equal to the smallest possible LSN, CLFS_LSN_NULL. |
| [ClfsLsnRecordSequence function](..\wdm\nf-wdm-clfslsnrecordsequence.md) | The ClfsLsnRecordSequence routine returns the record sequence number contained in a specified LSN. |
| [ClfsMgmtDeregisterManagedClient function](..\wdm\nf-wdm-clfsmgmtderegistermanagedclient.md) | The ClfsMgmtDeregisterManagedClient routine removes the connection between a client and a log, so that the client no longer manages the log. |
| [ClfsMgmtHandleLogFileFull function](..\wdm\nf-wdm-clfsmgmthandlelogfilefull.md) | The ClfsMgmtHandleLogFileFull routine attempts to make more space available in a log. It might make more space available by adding containers to the log, or it might ask clients to move their log tails. |
| [ClfsMgmtInstallPolicy function](..\wdm\nf-wdm-clfsmgmtinstallpolicy.md) | The ClfsMgmtInstallPolicy routine adds a CLFS_MGMT_POLICY structure to a physical log. |
| [ClfsMgmtQueryPolicy function](..\wdm\nf-wdm-clfsmgmtquerypolicy.md) | The ClfsMgmtQueryPolicy routine retrieves a specific CLFS_MGMT_POLICY structure for a log. |
| [ClfsMgmtRegisterManagedClient function](..\wdm\nf-wdm-clfsmgmtregistermanagedclient.md) | The ClfsMgmtRegisterManagedClient routine creates a client that will manage a CLFS log. |
| [ClfsMgmtRemovePolicy function](..\wdm\nf-wdm-clfsmgmtremovepolicy.md) | The ClfsMgmtRemovePolicy routine resets a log's CLFS_MGMT_POLICY structure to its default value. |
| [ClfsMgmtSetLogFileSize function](..\wdm\nf-wdm-clfsmgmtsetlogfilesize.md) | The ClfsMgmtSetLogFileSize routine adds containers to a log or deletes containers from a log. |
| [ClfsMgmtSetLogFileSizeAsClient function](..\wdm\nf-wdm-clfsmgmtsetlogfilesizeasclient.md) | The ClfsMgmtSetLogFileSizeAsClient routine sets the log file size by adding containers to a client log or deleting containers from a client log. |
| [ClfsMgmtTailAdvanceFailure function](..\wdm\nf-wdm-clfsmgmttailadvancefailure.md) | The ClfsMgmtTailAdvanceFailure routine notifies CLFS management that the client could not advance the log's tail. |
| [ClfsQueryLogFileInformation function](..\wdm\nf-wdm-clfsquerylogfileinformation.md) | The ClfsQueryLogFileInformation routine returns metadata and state information for a specified CLFS stream or its underlying physical log or both. |
| [ClfsReadLogRecord function](..\wdm\nf-wdm-clfsreadlogrecord.md) | The ClfsReadLogRecord routine reads a target record in a CLFS stream and returns a read context that the caller can use to read the records preceding or following it in the stream. |
| [ClfsReadNextLogRecord function](..\wdm\nf-wdm-clfsreadnextlogrecord.md) | The ClfsReadNextLogRecord routine reads the next record in a sequence, relative to the current record in a read context. |
| [ClfsReadPreviousRestartArea function](..\wdm\nf-wdm-clfsreadpreviousrestartarea.md) | The ClfsReadPreviousRestartArea routine reads the previous restart record relative to the current record in a read context. |
| [ClfsReadRestartArea function](..\wdm\nf-wdm-clfsreadrestartarea.md) | The ClfsReadRestartArea routine reads the restart record that was most recently written to a specified CLFS stream. |
| [ClfsRemoveLogContainer function](..\wdm\nf-wdm-clfsremovelogcontainer.md) | The ClfsRemoveLogContainer routine removes a container from a CLFS log. |
| [ClfsRemoveLogContainerSet function](..\wdm\nf-wdm-clfsremovelogcontainerset.md) | The ClfsRemoveLogContainerSet routine atomically removes a set of containers from a CLFS log. |
| [ClfsReserveAndAppendLog function](..\wdm\nf-wdm-clfsreserveandappendlog.md) | The ClfsReserveAndAppendLog routine reserves space in a marshalling area or appends a record to a marshalling area or does both atomically. |
| [ClfsReserveAndAppendLogAligned function](..\wdm\nf-wdm-clfsreserveandappendlogaligned.md) | The ClfsReserveAndAppendLogAligned routine reserves space in a marshalling area or appends a record to a marshalling area or does both atomically. The record's data is aligned on specified boundaries. |
| [ClfsScanLogContainers function](..\wdm\nf-wdm-clfsscanlogcontainers.md) | The ClfsScanLogContainers routine retrieves descriptive information for a sequence of containers that belong to a particular CLFS log. |
| [ClfsSetArchiveTail function](..\wdm\nf-wdm-clfssetarchivetail.md) | The ClfsSetArchiveTail routine sets the archive tail of a CLFS log to a specified LSN. |
| [ClfsSetEndOfLog function](..\wdm\nf-wdm-clfssetendoflog.md) | The ClfsSetEndOfLog routine truncates a CLFS stream. |
| [ClfsSetLogFileInformation function](..\wdm\nf-wdm-clfssetlogfileinformation.md) | The ClfsSetLogFileInformation routine sets metadata and state information for a specified stream and its underlying physical log. |
| [ClfsTerminateReadLog function](..\wdm\nf-wdm-clfsterminatereadlog.md) | The ClfsTerminateReadLog routine invalidates a specified read context after freeing resources associated with the context. |
| [ClfsWriteRestartArea function](..\wdm\nf-wdm-clfswriterestartarea.md) | The ClfsWriteRestartArea routine atomically appends a new restart record to a CLFS stream, flushes the restart record to stable storage, and optionally updates the base LSN of the stream. |
| [CmCallbackGetKeyObjectID function](..\wdm\nf-wdm-cmcallbackgetkeyobjectid.md) | The CmCallbackGetKeyObjectID routine retrieves the unique identifier and object name that are associated with a specified registry key object. |
| [CmCallbackGetKeyObjectIDEx function](..\wdm\nf-wdm-cmcallbackgetkeyobjectidex.md) | The CmCallbackGetKeyObjectIDEx routine retrieves the unique identifier and object name that are associated with a specified registry key object. |
| [CmCallbackReleaseKeyObjectIDEx function](..\wdm\nf-wdm-cmcallbackreleasekeyobjectidex.md) | The CmCallbackReleaseKeyObjectIDEx routine frees an object name string obtained from the CmCallbackGetKeyObjectIDEx routine. |
| [CmGetBoundTransaction function](..\wdm\nf-wdm-cmgetboundtransaction.md) | The CmGetBoundTransaction routine returns a pointer to the transaction object that represents the transaction, if any, that is associated with a specified registry key object. |
| [CmGetCallbackVersion function](..\wdm\nf-wdm-cmgetcallbackversion.md) | The CmGetCallbackVersion routine retrieves the major and minor version numbers for the current version of the configuration manager's registry callback feature. |
| [CmRegisterCallback function](..\wdm\nf-wdm-cmregistercallback.md) | The CmRegisterCallback routine is obsolete for Windows Vista and later operating system versions. Use CmRegisterCallbackEx instead.The CmRegisterCallback routine registers a RegistryCallback routine. |
| [CmRegisterCallbackEx function](..\wdm\nf-wdm-cmregistercallbackex.md) | The CmRegisterCallbackEx routine registers a RegistryCallback routine. |
| [CmSetCallbackObjectContext function](..\wdm\nf-wdm-cmsetcallbackobjectcontext.md) | The CmSetCallbackObjectContext routine associates specified context information with a specified registry object. |
| [CmUnRegisterCallback function](..\wdm\nf-wdm-cmunregistercallback.md) | The CmUnRegisterCallback routine unregisters a RegistryCallback routine that a CmRegisterCallback or CmRegisterCallbackEx routine previously registered. |
| [ExAcquireResourceExclusiveLite function](..\wdm\nf-wdm-exacquireresourceexclusivelite.md) | The ExAcquireResourceExclusiveLite routine acquires the given resource for exclusive access by the calling thread. |
| [ExAcquireResourceSharedLite function](..\wdm\nf-wdm-exacquireresourcesharedlite.md) | The ExAcquireResourceSharedLite routine acquires the given resource for shared access by the calling thread. |
| [ExAcquireRundownProtection function](..\wdm\nf-wdm-exacquirerundownprotection.md) | The ExAcquireRundownProtection routine tries to acquire run-down protection on a shared object so the caller can safely access the object. |
| [ExAcquireRundownProtectionEx function](..\wdm\nf-wdm-exacquirerundownprotectionex.md) | The ExAcquireRundownProtectionEx routine tries to acquire run-down protection on a shared object so the caller can safely access the object. |
| [ExAcquireSharedStarveExclusive function](..\wdm\nf-wdm-exacquiresharedstarveexclusive.md) | The ExAcquireSharedStarveExclusive routine acquires a given resource for shared access without waiting for any pending attempts to acquire exclusive access to the same resource. |
| [ExAcquireSharedWaitForExclusive function](..\wdm\nf-wdm-exacquiresharedwaitforexclusive.md) | The ExAcquireSharedWaitForExclusive routine acquires the given resource for shared access if shared access can be granted and there are no exclusive waiters. |
| [ExAllocateFromLookasideListEx function](..\wdm\nf-wdm-exallocatefromlookasidelistex.md) | The ExAllocateFromLookasideListEx routine removes the first entry from the specified lookaside list, or, if the list is empty, dynamically allocates the storage for a new entry. |
| [ExAllocateFromNPagedLookasideList function](..\wdm\nf-wdm-exallocatefromnpagedlookasidelist.md) | The ExAllocateFromNPagedLookasideList routine returns a pointer to a nonpaged entry from the given lookaside list, or it returns a pointer to a newly allocated nonpaged entry. |
| [ExAllocateFromPagedLookasideList function](..\wdm\nf-wdm-exallocatefrompagedlookasidelist.md) | The ExAllocateFromPagedLookasideList routine returns a pointer to a paged entry from the given lookaside list, or it returns a pointer to a newly allocated paged entry. |
| [ExAllocateFromPagedLookasideList function](..\wdm\nf-wdm-exallocatefrompagedlookasidelist~r1.md) | The ExAllocateFromPagedLookasideList routine returns a pointer to a paged entry from the given lookaside list, or it returns a pointer to a newly allocated paged entry. |
| [ExAllocatePool function](..\wdm\nf-wdm-exallocatepool.md) | The ExAllocatePool routine is obsolete, and is exported only for existing binaries. Use ExAllocatePoolWithTag instead.ExAllocatePool allocates pool memory of the specified type and returns a pointer to the allocated block. |
| [ExAllocatePoolWithQuota function](..\wdm\nf-wdm-exallocatepoolwithquota.md) | The ExAllocatePoolWithQuota routine is obsolete, and is exported only for existing driver binaries. Use ExAllocatePoolWithQuotaTag instead.ExAllocatePoolWithQuota allocates pool memory, charging quota against the current process. |
| [ExAllocatePoolWithQuotaTag function](..\wdm\nf-wdm-exallocatepoolwithquotatag.md) | The ExAllocatePoolWithQuotaTag routine allocates pool memory, charging the quota against the current process. |
| [ExAllocatePoolWithQuotaTag function](..\wdm\nf-wdm-exallocatepoolwithquotatag~r1.md) | The ExAllocatePoolWithQuotaTag routine allocates pool memory, charging the quota against the current process. |
| [ExAllocatePoolWithTag function](..\wdm\nf-wdm-exallocatepoolwithtag.md) | The ExAllocatePoolWithTag routine allocates pool memory of the specified type and returns a pointer to the allocated block. |
| [ExAllocatePoolWithTag function](..\wdm\nf-wdm-exallocatepoolwithtag~r1.md) | The ExAllocatePoolWithTag routine allocates pool memory of the specified type and returns a pointer to the allocated block. |
| [ExAllocatePoolWithTagPriority function](..\wdm\nf-wdm-exallocatepoolwithtagpriority.md) | The ExAllocatePoolWithTagPriority routine allocates pool memory of the specified type. |
| [ExAllocateTimer function](..\wdm\nf-wdm-exallocatetimer.md) | The ExAllocateTimer routine allocates and initializes a timer object. |
| [ExCancelTimer function](..\wdm\nf-wdm-excanceltimer.md) | The ExCancelTimer routine cancels a timer that was set by a previous call to the ExSetTimer routine. |
| [ExConvertExclusiveToSharedLite function](..\wdm\nf-wdm-exconvertexclusivetosharedlite.md) | The ExConvertExclusiveToSharedLite routine converts a given resource from acquired for exclusive access to acquired for shared access. |
| [ExCreateCallback function](..\wdm\nf-wdm-excreatecallback.md) | The ExCreateCallback routine either creates a new callback object or opens an existing callback object on behalf of the caller. |
| [ExDeleteLookasideListEx function](..\wdm\nf-wdm-exdeletelookasidelistex.md) | The ExDeleteLookasideListEx routine deletes a lookaside list. |
| [ExDeleteNPagedLookasideList function](..\wdm\nf-wdm-exdeletenpagedlookasidelist.md) | The ExDeleteNPagedLookasideList routine destroys a nonpaged lookaside list. |
| [ExDeletePagedLookasideList function](..\wdm\nf-wdm-exdeletepagedlookasidelist.md) | The ExDeletePagedLookasideList routine destroys a paged lookaside list. |
| [ExDeleteResourceLite function](..\wdm\nf-wdm-exdeleteresourcelite.md) | The ExDeleteResourceLite routine deletes a given resource from the system's resource list. |
| [ExDeleteTimer function](..\wdm\nf-wdm-exdeletetimer.md) | The ExDeleteTimer routine deletes a timer object that was previously allocated by the ExAllocateTimer routine. |
| [ExFlushLookasideListEx function](..\wdm\nf-wdm-exflushlookasidelistex.md) | The ExFlushLookasideListEx routine flushes all entries from the specified lookaside list and frees the allocated storage for each entry. |
| [ExFreePool function](..\ntddk\nf-ntddk-exfreepool.md) | The ExFreePool routine deallocates a block of pool memory. |
| [ExFreePool function](..\wdm\nf-wdm-exfreepool.md) | The ExFreePool routine deallocates a block of pool memory. |
| [ExFreePoolWithTag function](..\wdm\nf-wdm-exfreepoolwithtag.md) | The ExFreePoolWithTag routine deallocates a block of pool memory allocated with the specified tag. |
| [ExFreeToLookasideListEx function](..\wdm\nf-wdm-exfreetolookasidelistex.md) | The ExFreeToLookasideListEx routine inserts an entry into a lookaside list, or, if the list is full, frees the allocated storage for the entry. |
| [ExFreeToNPagedLookasideList function](..\wdm\nf-wdm-exfreetonpagedlookasidelist.md) | The ExFreeToNPagedLookasideList routine returns a nonpaged entry to the given lookaside list or to nonpaged pool. |
| [ExFreeToPagedLookasideList function](..\wdm\nf-wdm-exfreetopagedlookasidelist.md) | The ExFreeToPagedLookasideList routine returns a pageable entry to the given lookaside list or to paged pool. |
| [ExFreeToPagedLookasideList function](..\wdm\nf-wdm-exfreetopagedlookasidelist~r1.md) | The ExFreeToPagedLookasideList routine returns a pageable entry to the given lookaside list or to paged pool. |
| [ExGetExclusiveWaiterCount function](..\wdm\nf-wdm-exgetexclusivewaitercount.md) | The ExGetExclusiveWaiterCount routine returns the number of waiters on exclusive access to a given resource. |
| [ExGetFirmwareEnvironmentVariable function](..\wdm\nf-wdm-exgetfirmwareenvironmentvariable.md) | The ExGetFirmwareEnvironmentVariable routine gets the value of the specified system firmware environment variable. |
| [ExGetFirmwareType function](..\wdm\nf-wdm-exgetfirmwaretype.md) | Returns the system firmware type. |
| [ExGetPreviousMode function](..\wdm\nf-wdm-exgetpreviousmode.md) | The ExGetPreviousMode routine returns the previous processor mode for the current thread. |
| [ExGetSharedWaiterCount function](..\wdm\nf-wdm-exgetsharedwaitercount.md) | The ExGetSharedWaiterCount routine returns the number of waiters on shared access to a given resource. |
| [ExInitializeDeleteTimerParameters function](..\wdm\nf-wdm-exinitializedeletetimerparameters.md) | The ExInitializeDeleteTimerParameters routine initializes an EXT_DELETE_PARAMETERS structure. |
| [ExInitializeFastMutex function](..\wdm\nf-wdm-exinitializefastmutex.md) | The ExInitializeFastMutex routine initializes a fast mutex variable, used to synchronize mutually exclusive access by a set of threads to a shared resource. |
| [ExInitializeLookasideListEx function](..\wdm\nf-wdm-exinitializelookasidelistex.md) | The ExInitializeLookasideListEx routine initializes a lookaside list. |
| [ExInitializeNPagedLookasideList function](..\wdm\nf-wdm-exinitializenpagedlookasidelist.md) | The ExInitializeNPagedLookasideList routine initializes a lookaside list for nonpaged entries of the specified size. |
| [ExInitializePagedLookasideList function](..\wdm\nf-wdm-exinitializepagedlookasidelist.md) | The ExInitializePagedLookasideList routine initializes a lookaside list for pageable entries of the specified size. |
| [ExInitializeResourceLite function](..\wdm\nf-wdm-exinitializeresourcelite.md) | The ExInitializeResourceLite routine initializes a resource variable. |
| [ExInitializeRundownProtection function](..\wdm\nf-wdm-exinitializerundownprotection.md) | The ExInitializeRundownProtection routine initializes run-down protection on a shared object. |
| [ExInitializeSetTimerParameters function](..\wdm\nf-wdm-exinitializesettimerparameters.md) | The ExInitializeSetTimerParameters routine initializes an EXT_SET_PARAMETERS structure. |
| [ExInterlockedAddLargeInteger function](..\wdm\nf-wdm-exinterlockedaddlargeinteger.md) | The ExInterlockedAddLargeInteger routine adds a large integer value to the specified variable as an atomic operation. |
| [ExInterlockedAddLargeStatistic function](..\wdm\nf-wdm-exinterlockedaddlargestatistic.md) | The ExInterlockedAddLargeStatistic routine performs an interlocked addition of a ULONG increment value to a LARGE_INTEGER variable. |
| [ExInterlockedAddUlong function](..\wdm\nf-wdm-exinterlockedaddulong.md) | The ExInterlockedAddUlong routine adds an unsigned long value to a given unsigned integer as an atomic operation. |
| [ExInterlockedCompareExchange64 function](..\wdm\nf-wdm-exinterlockedcompareexchange64.md) | The ExInterlockedCompareExchange64 routine compares one integer variable to another and, if they are equal, sets the first variable to a caller-supplied value. |
| [ExInterlockedFlushSList function](..\wdm\nf-wdm-exinterlockedflushslist.md) | The ExInterlockedFlushSList routine atomically removes all entries from a sequenced singly linked list. |
| [ExInterlockedFlushSList function](..\wdm\nf-wdm-exinterlockedflushslist~r1.md) | The ExInterlockedFlushSList routine atomically removes all entries from a sequenced singly linked list. |
| [ExInterlockedInsertHeadList function](..\wdm\nf-wdm-exinterlockedinsertheadlist.md) | The ExInterlockedInsertHeadList routine atomically inserts an entry at the beginning of a doubly linked list of LIST_ENTRY structures. |
| [ExInterlockedInsertTailList function](..\wdm\nf-wdm-exinterlockedinserttaillist.md) | The ExInterlockedInsertTailList routine atomically inserts an entry at the end of a doubly linked list of LIST_ENTRY structures. |
| [ExInterlockedPopEntryList function](..\wdm\nf-wdm-exinterlockedpopentrylist.md) | The ExInterlockedPopEntryList routine atomically removes an entry from the beginning of a singly linked list of SINGLE_LIST_ENTRY structures. |
| [ExInterlockedPopEntrySList function](..\wdm\nf-wdm-exinterlockedpopentryslist.md) | The ExInterlockedPopEntrySList routine atomically removes the first entry from a sequenced singly linked list. |
| [ExInterlockedPopEntrySList function](..\wdm\nf-wdm-exinterlockedpopentryslist~r1.md) | The ExInterlockedPopEntrySList routine atomically removes the first entry from a sequenced singly linked list. |
| [ExInterlockedPopEntrySList function](..\wdm\nf-wdm-exinterlockedpopentryslist~r2.md) | The ExInterlockedPopEntrySList routine atomically removes the first entry from a sequenced singly linked list. |
| [ExInterlockedPushEntryList function](..\wdm\nf-wdm-exinterlockedpushentrylist.md) | The ExInterlockedPushEntryList routine atomically inserts an entry at the beginning of a singly linked list of SINGLE_LIST_ENTRY structures. |
| [ExInterlockedPushEntrySList function](..\wdm\nf-wdm-exinterlockedpushentryslist.md) | The ExInterlockedPushEntrySList routine atomically inserts an entry at the beginning of a sequenced singly linked list. |
| [ExInterlockedPushEntrySList function](..\wdm\nf-wdm-exinterlockedpushentryslist~r1.md) | The ExInterlockedPushEntrySList routine atomically inserts an entry at the beginning of a sequenced singly linked list. |
| [ExInterlockedPushEntrySList function](..\wdm\nf-wdm-exinterlockedpushentryslist~r2.md) | The ExInterlockedPushEntrySList routine atomically inserts an entry at the beginning of a sequenced singly linked list. |
| [ExInterlockedRemoveHeadList function](..\wdm\nf-wdm-exinterlockedremoveheadlist.md) | The ExInterlockedRemoveHeadList routine removes an entry from the beginning of a doubly linked list of LIST_ENTRY structures. |
| [ExIsProcessorFeaturePresent function](..\wdm\nf-wdm-exisprocessorfeaturepresent.md) | The ExIsProcessorFeaturePresent routine queries for the existence of a specified processor feature. |
| [ExIsResourceAcquiredExclusiveLite function](..\wdm\nf-wdm-exisresourceacquiredexclusivelite.md) | The ExIsResourceAcquiredExclusiveLite routine returns whether the current thread has exclusive access to a given resource. |
| [ExIsResourceAcquiredSharedLite function](..\wdm\nf-wdm-exisresourceacquiredsharedlite.md) | The ExIsResourceAcquiredSharedLite routine returns whether the current thread has access (either shared or exclusive) to a given resource. |
| [ExIsSoftBoot function](..\wdm\nf-wdm-exissoftboot.md) | Determines whether the system has gone through a soft restart. |
| [ExLocalTimeToSystemTime function](..\wdm\nf-wdm-exlocaltimetosystemtime.md) | The ExLocalTimeToSystemTime routine converts a system time value for the current time zone to an unbiased, GreenGMT value. |
| [ExNotifyCallback function](..\wdm\nf-wdm-exnotifycallback.md) | The ExNotifyCallback routine causes all callback routines registered for the given object to be called. |
| [ExQueryDepthSList function](..\wdm\nf-wdm-exquerydepthslist.md) | The ExQueryDepthSList routine returns the number of entries currently in a given sequenced singly linked list. |
| [ExQueryDepthSList function](..\wdm\nf-wdm-exquerydepthslist~r1.md) | The ExQueryDepthSList routine returns the number of entries currently in a given sequenced singly linked list. |
| [ExQueryDepthSList function](..\wdm\nf-wdm-exquerydepthslist~r2.md) | The ExQueryDepthSList routine returns the number of entries currently in a given sequenced singly linked list. |
| [ExQueryTimerResolution function](..\wdm\nf-wdm-exquerytimerresolution.md) | The ExQueryTimerResolution routine reports the range of timer resolutions that are supported by the system clock. |
| [ExRaiseAccessViolation function](..\ntddk\nf-ntddk-exraiseaccessviolation.md) | The ExRaiseAccessViolation routine can be used with structured exception handling to throw a driver-determined exception for a memory access violation that occurs when a driver processes I/O requests. |
| [ExRaiseDatatypeMisalignment function](..\ntddk\nf-ntddk-exraisedatatypemisalignment.md) | The ExRaiseDatatypeMisalignment routine can be used with structured exception handling to throw a driver-determined exception for a misaligned data type that occurs when a driver processes I/O requests. |
| [ExRaiseStatus function](..\wdm\nf-wdm-exraisestatus.md) | The ExRaiseStatus routine is called by drivers that supply structured exception handlers to handle particular errors that occur while they are processing I/O requests. |
| [ExReInitializeRundownProtection function](..\wdm\nf-wdm-exreinitializerundownprotection.md) | The ExReInitializeRundownProtection routine reinitializes an EX_RUNDOWN_REF structure after the associated object is run down. |
| [ExRegisterCallback function](..\wdm\nf-wdm-exregistercallback.md) | The ExRegisterCallback routine registers a given callback routine with a given callback object. |
| [ExReinitializeResourceLite function](..\wdm\nf-wdm-exreinitializeresourcelite.md) | The ExReinitializeResourceLite routine reinitializes an existing resource variable. |
| [ExReleaseResourceForThreadLite function](..\wdm\nf-wdm-exreleaseresourceforthreadlite.md) | The ExReleaseResourceForThreadLite routine releases the input resource of the indicated thread. |
| [ExReleaseRundownProtection function](..\wdm\nf-wdm-exreleaserundownprotection.md) | The ExReleaseRundownProtection routine releases run-down protection that the caller previously acquired by calling the ExAcquireRundownProtection routine. |
| [ExReleaseRundownProtectionEx function](..\wdm\nf-wdm-exreleaserundownprotectionex.md) | The ExReleaseRundownProtectionEx routine releases run-down protection that the caller previously acquired by calling the ExAcquireRundownProtectionEx routine. |
| [ExReleaseSpinLockExclusive function](..\wdm\nf-wdm-exreleasespinlockexclusive.md) | The ExReleaseSpinLockExclusive routine releases a spin lock that the caller previously acquired for exclusive access, and restores the IRQL to its original value. |
| [ExReleaseSpinLockShared function](..\wdm\nf-wdm-exreleasespinlockshared.md) | The ExReleaseSpinLockShared routine releases ownership of a spin lock that the caller previously acquired for shared access, and restores the IRQL to its original value. |
| [ExRundownCompleted function](..\wdm\nf-wdm-exrundowncompleted.md) | The ExRundownCompleted routine updates the run-down status of a shared object to indicate that the run down of the object has completed. |
| [ExSetFirmwareEnvironmentVariable function](..\wdm\nf-wdm-exsetfirmwareenvironmentvariable.md) | The ExSetFirmwareEnvironmentVariable routine sets the value of the specified system firmware environment variable. |
| [ExSetResourceOwnerPointer function](..\wdm\nf-wdm-exsetresourceownerpointer.md) | The ExSetResourceOwnerPointer routine sets the owner thread pointer for an executive resource. |
| [ExSetResourceOwnerPointerEx function](..\wdm\nf-wdm-exsetresourceownerpointerex.md) | The ExSetResourceOwnerPointerEx routine transfers the ownership of an executive resource from the calling thread to an owner pointer, which is a system address that identifies the resource owner. |
| [ExSetTimer function](..\wdm\nf-wdm-exsettimer.md) | The ExSetTimer routine starts a timer operation and sets the timer to expire at the specified due time. |
| [ExSetTimerResolution function](..\wdm\nf-wdm-exsettimerresolution.md) | The ExSetTimerResolution routine modifies the frequency at which the system clock interrupts. Use this routine with extreme caution (see the following Remarks section). |
| [ExSystemTimeToLocalTime function](..\wdm\nf-wdm-exsystemtimetolocaltime.md) | The ExSystemTimeToLocalTime routine converts a GMT system time value to the local system time for the current time zone. |
| [ExTryConvertSharedSpinLockExclusive function](..\wdm\nf-wdm-extryconvertsharedspinlockexclusive.md) | The ExTryConvertSharedSpinLockExclusive routine attempts to convert the access state of a spin lock from acquired for shared access to exclusive access. |
| [ExUnregisterCallback function](..\wdm\nf-wdm-exunregistercallback.md) | The ExUnregisterCallback routine removes a callback routine previously registered with a callback object from the list of routines to be called during the notification process. |
| [ExUuidCreate function](..\ntddk\nf-ntddk-exuuidcreate.md) | The ExUuidCreate routine initializes a UUID (GUID) structure to a newly generated value. |
| [ExWaitForRundownProtectionRelease function](..\wdm\nf-wdm-exwaitforrundownprotectionrelease.md) | The ExWaitForRundownProtectionRelease routine waits until all drivers that have already been granted run-down protection complete their accesses of the shared object. |
| [FIELD_OFFSET function](..\wdm\nf-wdm-field-offset.md) | The FIELD_OFFSET macro returns the byte offset of a named field in a known structure type. |
| [FirstEntrySList function](..\wdm\nf-wdm-firstentryslist.md) | The FirstEntrySList routine returns the first entry in a sequenced singly linked list. |
| [HalAllocateHardwareCounters function](..\ntddk\nf-ntddk-halallocatehardwarecounters.md) | The HalAllocateHardwareCounters routine allocates a set of hardware performance counters. |
| [HalExamineMBR function](..\ntddk\nf-ntddk-halexaminembr.md) | The HalExamineMBR routine reads the master boot record (MBR) of a disk and returns data from the MBR if the MBR is of the type specified by the caller. |
| [HalFreeHardwareCounters function](..\ntddk\nf-ntddk-halfreehardwarecounters.md) | The HalFreeHardwareCounters routine frees a set of hardware performance counters that was acquired in a previous call to HalAllocateHardwareCounters routine. |
| [InitializeListHead function](..\wdm\nf-wdm-initializelisthead.md) | The InitializeListHead routine initializes a LIST_ENTRY structure that represents the head of a doubly linked list. |
| [InsertHeadList function](..\wdm\nf-wdm-insertheadlist.md) | The InsertHeadList routine inserts an entry at the head of a doubly linked list of LIST_ENTRY structures. |
| [InsertHeadList function](..\wdm\nf-wdm-insertheadlist~r1.md) | The InsertHeadList routine inserts an entry at the head of a doubly linked list of LIST_ENTRY structures. |
| [InsertTailList function](..\wdm\nf-wdm-inserttaillist.md) | The InsertTailList routine inserts an entry at the tail of a doubly linked list of LIST_ENTRY structures. |
| [InsertTailList function](..\wdm\nf-wdm-inserttaillist~r1.md) | The InsertTailList routine inserts an entry at the tail of a doubly linked list of LIST_ENTRY structures. |
| [InterlockedAnd function](..\wdm\nf-wdm-interlockedand.md) | The InterlockedAnd macro atomically computes a bitwise AND operation. |
| [InterlockedAnd function](..\wdm\nf-wdm-interlockedand~r1.md) | The InterlockedAnd macro atomically computes a bitwise AND operation. |
| [InterlockedCompareExchange function](..\wdm\nf-wdm-interlockedcompareexchange.md) | The InterlockedCompareExchange routine performs an atomic operation that compares the input value pointed to by Destination with the value of Comparand. |
| [InterlockedCompareExchange function](..\wdm\nf-wdm-interlockedcompareexchange~r1.md) | The InterlockedCompareExchange routine performs an atomic operation that compares the input value pointed to by Destination with the value of Comparand. |
| [InterlockedCompareExchangePointer function](..\wdm\nf-wdm-interlockedcompareexchangepointer.md) | The InterlockedCompareExchangePointer routine performs an atomic operation that compares the input pointer value pointed to by Destination with the pointer value Comparand. |
| [InterlockedDecrement function](..\wdm\nf-wdm-interlockeddecrement.md) | The InterlockedDecrement routine decrements a caller-supplied variable of type LONG as an atomic operation. |
| [InterlockedDecrement function](..\wdm\nf-wdm-interlockeddecrement~r1.md) | The InterlockedDecrement routine decrements a caller-supplied variable of type LONG as an atomic operation. |
| [InterlockedExchange function](..\wdm\nf-wdm-interlockedexchange.md) | The InterlockedExchange routine sets an integer variable to a given value as an atomic operation. |
| [InterlockedExchange function](..\wdm\nf-wdm-interlockedexchange~r1.md) | The InterlockedExchange routine sets an integer variable to a given value as an atomic operation. |
| [InterlockedExchangeAdd function](..\wdm\nf-wdm-interlockedexchangeadd.md) | The InterlockedExchangeAdd routine adds a value to a given integer as an atomic operation and returns the original value of the given integer. |
| [InterlockedExchangeAdd function](..\wdm\nf-wdm-interlockedexchangeadd~r1.md) | The InterlockedExchangeAdd routine adds a value to a given integer as an atomic operation and returns the original value of the given integer. |
| [InterlockedExchangePointer function](..\wdm\nf-wdm-interlockedexchangepointer.md) | The InterlockedExchangePointer routine performs an atomic operation that sets a pointer to a new value. |
| [InterlockedIncrement function](..\wdm\nf-wdm-interlockedincrement.md) | The InterlockedIncrement routine increments a caller-supplied variable as an atomic operation. |
| [InterlockedIncrement function](..\wdm\nf-wdm-interlockedincrement~r1.md) | The InterlockedIncrement routine increments a caller-supplied variable as an atomic operation. |
| [InterlockedOr function](..\wdm\nf-wdm-interlockedor.md) | The InterlockedOr routine atomically computes a bitwise OR operation. |
| [InterlockedOr function](..\wdm\nf-wdm-interlockedor~r1.md) | The InterlockedOr routine atomically computes a bitwise OR operation. |
| [InterlockedXor function](..\wdm\nf-wdm-interlockedxor.md) | The InterlockedOr routine atomically computes a bitwise exclusive OR operation. |
| [InterlockedXor function](..\wdm\nf-wdm-interlockedxor~r1.md) | The InterlockedOr routine atomically computes a bitwise exclusive OR operation. |
| [IoAcquireRemoveLock function](..\wdm\nf-wdm-ioacquireremovelock.md) | The IoAcquireRemoveLock routine increments the count for a remove lock, indicating that the associated device object should not be detached from the device stack or deleted. |
| [IoAdjustPagingPathCount function](..\wdm\nf-wdm-ioadjustpagingpathcount.md) | The IoAdjustPagingPathCount routine increments or decrements a caller-supplied page-file counter as an atomic operation. |
| [IoAllocateController function](..\ntddk\nf-ntddk-ioallocatecontroller.md) | The IoAllocateController routine sets up the call to a driver-supplied ControllerControl routine as soon as the device controller, represented by the given controller object, is available to carry out an I/O operation for the target device, represented by the given device object. |
| [IoAllocateDriverObjectExtension function](..\wdm\nf-wdm-ioallocatedriverobjectextension.md) | The IoAllocateDriverObjectExtension routine allocates a per-driver context area, called a driver object extension, and assigns a unique identifier to it. |
| [IoAllocateErrorLogEntry function](..\wdm\nf-wdm-ioallocateerrorlogentry.md) | The IoAllocateErrorLogEntry routine allocates an error log entry, and returns a pointer to the packet that the caller uses to supply information about an I/O error. |
| [IoAllocateIrp function](..\wdm\nf-wdm-ioallocateirp.md) | The IoAllocateIrp routine allocates an IRP, given the number of I/O stack locations for each driver layered under the caller, and, optionally, for the caller. |
| [IoAllocateMdl function](..\wdm\nf-wdm-ioallocatemdl.md) | The IoAllocateMdl routine allocates a memory descriptor list (MDL) large enough to map a buffer, given the buffer's starting address and length. Optionally, this routine associates the MDL with an IRP. |
| [IoAllocateWorkItem function](..\wdm\nf-wdm-ioallocateworkitem.md) | The IoAllocateWorkItem routine allocates a work item. |
| [IoAssignArcName function](..\ntddk\nf-ntddk-ioassignarcname.md) | The IoAssignArcName routine creates a symbolic link between the ARC name of a physical device and the name of the corresponding device object when it has been created. |
| [IoAttachDevice function](..\wdm\nf-wdm-ioattachdevice.md) | The IoAttachDevice routine attaches the caller's device object to a named target device object, so that I/O requests bound for the target device are routed first to the caller. |
| [IoAttachDeviceToDeviceStack function](..\wdm\nf-wdm-ioattachdevicetodevicestack.md) | The IoAttachDeviceToDeviceStack routine attaches the caller's device object to the highest device object in the chain and returns a pointer to the previously highest device object. |
| [IoBuildAsynchronousFsdRequest function](..\wdm\nf-wdm-iobuildasynchronousfsdrequest.md) | The IoBuildAsynchronousFsdRequest routine allocates and sets up an IRP to be sent to lower-level drivers. |
| [IoBuildDeviceIoControlRequest function](..\wdm\nf-wdm-iobuilddeviceiocontrolrequest.md) | The IoBuildDeviceIoControlRequest routine allocates and sets up an IRP for a synchronously processed device control request. |
| [IoBuildPartialMdl function](..\wdm\nf-wdm-iobuildpartialmdl.md) | The IoBuildPartialMdl routine builds a new memory descriptor list (MDL) that represents part of a buffer that is described by an existing MDL. |
| [IoBuildSynchronousFsdRequest function](..\wdm\nf-wdm-iobuildsynchronousfsdrequest.md) | The IoBuildSynchronousFsdRequest routine allocates and sets up an IRP for a synchronously processed I/O request. |
| [IoCallDriver function](..\wdm\nf-wdm-iocalldriver.md) | The IoCallDriver routine sends an IRP to the driver associated with a specified device object. |
| [IoCancelIrp function](..\wdm\nf-wdm-iocancelirp.md) | The IoCancelIrp routine sets the cancel bit in a given IRP and calls the cancel routine for the IRP if there is one. |
| [IoCheckLinkShareAccess function](..\wdm\nf-wdm-iochecklinkshareaccess.md) | The IoCheckLinkShareAccess routine is called by file system drivers (FSDs) or other highest-level drivers to check whether link shared access to a file object is permitted. |
| [IoCheckShareAccess function](..\wdm\nf-wdm-iocheckshareaccess.md) | The IoCheckShareAccess routine is called by file system drivers (FSDs) or other highest-level drivers to check whether shared access to a file object is permitted. |
| [IoCheckShareAccessEx function](..\wdm\nf-wdm-iocheckshareaccessex.md) | The IoCheckShareAccessEx routine is called by file system drivers (FSDs) or other highest-level drivers to check whether shared access to a file object is permitted. |
| [IoClearActivityIdThread function](..\ntddk\nf-ntddk-ioclearactivityidthread.md) | The IoClearActivityIdThread routine clears the activity ID of the current thread. |
| [IoCompleteRequest function](..\wdm\nf-wdm-iocompleterequest.md) | The IoCompleteRequest routine indicates that the caller has completed all processing for a given I/O request and is returning the given IRP to the I/O manager. |
| [IoConnectInterrupt function](..\wdm\nf-wdm-ioconnectinterrupt.md) | The IoConnectInterrupt routine registers a device driver's InterruptService routine (ISR), so that it will be called when a device interrupts on any of a specified set of processors. |
| [IoConnectInterruptEx function](..\wdm\nf-wdm-ioconnectinterruptex.md) | For more information, see the WdmlibIoConnectInterruptEx function.#define IoConnectInterruptEx WdmlibIoConnectInterruptEx |
| [IoCopyCurrentIrpStackLocationToNext function](..\wdm\nf-wdm-iocopycurrentirpstacklocationtonext.md) | The IoCopyCurrentIrpStackLocationToNext routine copies the IRP stack parameters from the current I/O stack location to the stack location of the next-lower driver. |
| [IoCreateController function](..\ntddk\nf-ntddk-iocreatecontroller.md) | The IoCreateController routine allocates memory for and initializes a controller object with a controller extension of a driver-determined size. |
| [IoCreateDevice function](..\wdm\nf-wdm-iocreatedevice.md) | The IoCreateDevice routine creates a device object for use by a driver. |
| [IoCreateFile function](..\wdm\nf-wdm-iocreatefile.md) | The IoCreateFile routine either causes a new file or directory to be created, or it opens an existing file, device, directory, or volume, giving the caller a handle for the file object. |
| [IoCreateNotificationEvent function](..\wdm\nf-wdm-iocreatenotificationevent.md) | The IoCreateNotificationEvent routine creates or opens a named notification event used to notify one or more threads of execution that an event has occurred. |
| [IoCreateSymbolicLink function](..\wdm\nf-wdm-iocreatesymboliclink.md) | The IoCreateSymbolicLink routine sets up a symbolic link between a device object name and a user-visible name for the device. |
| [IoCreateSynchronizationEvent function](..\wdm\nf-wdm-iocreatesynchronizationevent.md) | The IoCreateSynchronizationEvent routine creates or opens a named synchronization event for use in serialization of access to hardware between two otherwise unrelated drivers. |
| [IoCreateSystemThread function](..\wdm\nf-wdm-iocreatesystemthread.md) | The IoCreateSystemThread routine creates a system thread that executes in kernel mode, and supplies a handle for the thread. |
| [IoCreateUnprotectedSymbolicLink function](..\wdm\nf-wdm-iocreateunprotectedsymboliclink.md) | The IoCreateUnprotectedSymbolicLink routine sets up an unprotected symbolic link between a device object name and a corresponding Win32-visible name. |
| [IoCsqInitialize function](..\wdm\nf-wdm-iocsqinitialize.md) | The IoCsqInitialize routine initializes the driver's cancel-safe IRP queue dispatch table. |
| [IoCsqInitializeEx function](..\wdm\nf-wdm-iocsqinitializeex.md) | The IoCsqInitializeEx routine initializes the dispatch table for a cancel-safe IRP queue. |
| [IoCsqInsertIrp function](..\wdm\nf-wdm-iocsqinsertirp.md) | The IoCsqInsertIrp routine inserts an IRP in the driver's cancel-safe IRP queue. |
| [IoCsqInsertIrpEx function](..\wdm\nf-wdm-iocsqinsertirpex.md) | The IoCsqInsertIrpEx routine inserts an IRP into the driver's cancel-safe IRP queue. |
| [IoCsqRemoveIrp function](..\wdm\nf-wdm-iocsqremoveirp.md) | The IoCsqRemoveIrp routine removes a particular IRP from the queue. |
| [IoCsqRemoveNextIrp function](..\wdm\nf-wdm-iocsqremovenextirp.md) | The IoCsqRemoveNextIrp routine removes the next matching IRP in the queue. |
| [IoDeassignArcName function](..\ntddk\nf-ntddk-iodeassignarcname.md) | The IoDeassignArcName routine removes a symbolic link between the ARC name for a device and the named device object. |
| [IoDecrementKeepAliveCount function](..\ntddk\nf-ntddk-iodecrementkeepalivecount.md) | The IoDecrementKeepAliveCount routine decrements a reference count associated with an Windows app on a specific device. |
| [IoDeleteController function](..\ntddk\nf-ntddk-iodeletecontroller.md) | The IoDeleteController routine removes a given controller object from the system, for example, when the driver that created it is being unloaded. |
| [IoDeleteDevice function](..\wdm\nf-wdm-iodeletedevice.md) | The IoDeleteDevice routine removes a device object from the system, for example, when the underlying device is removed from the system. |
| [IoDeleteSymbolicLink function](..\wdm\nf-wdm-iodeletesymboliclink.md) | The IoDeleteSymbolicLink routine removes a symbolic link from the system. |
| [IoDetachDevice function](..\wdm\nf-wdm-iodetachdevice.md) | The IoDetachDevice routine releases an attachment between the caller's device object and a lower driver's device object. |
| [IoDisconnectInterrupt function](..\wdm\nf-wdm-iodisconnectinterrupt.md) | The IoDisconnectInterrupt routine releases a device driver's set of interrupt object(s) when the device is paused or removed, or when the driver is being unloaded. |
| [IoDisconnectInterruptEx function](..\wdm\nf-wdm-iodisconnectinterruptex.md) | For more information, see the WdmlibIoDisconnectInterruptEx function.#define IoDisconnectInterruptEx WdmlibIoDisconnectInterruptEx |
| [IoForwardIrpSynchronously function](..\wdm\nf-wdm-ioforwardirpsynchronously.md) | The IoForwardIrpSynchronously routine sends an IRP to a specified driver and waits for that driver to complete the IRP. |
| [IoFreeController function](..\ntddk\nf-ntddk-iofreecontroller.md) | The IoFreeController routine releases a previously allocated controller object when the driver has completed an I/O request. |
| [IoFreeErrorLogEntry function](..\wdm\nf-wdm-iofreeerrorlogentry.md) | The IoFreeErrorLogEntry routine frees an unused error log entry. |
| [IoFreeIrp function](..\wdm\nf-wdm-iofreeirp.md) | The IoFreeIrp routine releases a caller-allocated IRP from the caller's IoCompletion routine. |
| [IoFreeMdl function](..\wdm\nf-wdm-iofreemdl.md) | The IoFreeMdl routine releases a caller-allocated memory descriptor list (MDL). |
| [IoFreeWorkItem function](..\wdm\nf-wdm-iofreeworkitem.md) | The IoFreeWorkItem routine frees a work item that was allocated by IoAllocateWorkItem. |
| [IoGetActivityIdIrp function](..\ntddk\nf-ntddk-iogetactivityidirp.md) | The IoGetActivityIdIrp routine retrieves the current activity ID associated with an IRP. |
| [IoGetActivityIdThread function](..\ntddk\nf-ntddk-iogetactivityidthread.md) | The IoGetActivityIdThread routine returns the activity ID associated with the current thread. |
| [IoGetAffinityInterrupt function](..\wdm\nf-wdm-iogetaffinityinterrupt.md) | For more information, see the WdmlibIoGetAffinityInterrupt function.#define IoGetAffinityInterrupt WdmlibIoGetAffinityInterrupt |
| [IoGetAttachedDeviceReference function](..\ntifs\nf-ntifs-iogetattacheddevicereference.md) | The IoGetAttachedDeviceReference routine returns a pointer to the highest level device object in a driver stack and increments the reference count on that object. |
| [IoGetAttachedDeviceReference function](..\wdm\nf-wdm-iogetattacheddevicereference.md) | The IoGetAttachedDeviceReference routine returns a pointer to the highest level device object in a driver stack and increments the reference count on that object. |
| [IoGetBootDiskInformation function](..\wdm\nf-wdm-iogetbootdiskinformation.md) | The IoGetBootDiskInformation routine returns information describing the boot and system disks. |
| [IoGetConfigurationInformation function](..\ntddk\nf-ntddk-iogetconfigurationinformation.md) | The IoGetConfigurationInformation routine returns a pointer to the I/O manager's global configuration information structure, which contains the current values for how many physical disk, floppy, CD-ROM, tape, SCSI HBA, serial, and parallel devices have device objects created to represent them by drivers as they are loaded. |
| [IoGetContainerInformation function](..\wdm\nf-wdm-iogetcontainerinformation.md) | The IoGetContainerInformation routine provides information about the current state of a user session. |
| [IoGetCurrentIrpStackLocation function](..\wdm\nf-wdm-iogetcurrentirpstacklocation.md) | The IoGetCurrentIrpStackLocation routine returns a pointer to the caller's I/O stack location in the specified IRP. |
| [IoGetCurrentProcess function](..\wdm\nf-wdm-iogetcurrentprocess.md) | The IoGetCurrentProcess routine returns a pointer to the current process. |
| [IoGetDeviceInterfaceAlias function](..\wdm\nf-wdm-iogetdeviceinterfacealias.md) | The IoGetDeviceInterfaceAlias routine returns the alias device interface of the specified device interface instance, if the alias exists. |
| [IoGetDeviceInterfacePropertyData function](..\wdm\nf-wdm-iogetdeviceinterfacepropertydata.md) | The IoGetDeviceInterfacePropertyData routine retrieves the current value of a device interface property. |
| [IoGetDeviceInterfaces function](..\wdm\nf-wdm-iogetdeviceinterfaces.md) | The IoGetDeviceInterfaces routine returns a list of device interface instances of a particular device interface class (such as all devices on the system that support a HID interface). |
| [IoGetDeviceNumaNode function](..\wdm\nf-wdm-iogetdevicenumanode.md) | The IoGetDeviceNumaNode routine gets the node number of a device. |
| [IoGetDeviceObjectPointer function](..\wdm\nf-wdm-iogetdeviceobjectpointer.md) | The IoGetDeviceObjectPointer routine returns a pointer to the top object in the named device object's stack and a pointer to the corresponding file object, if the requested access to the objects can be granted. |
| [IoGetDeviceProperty function](..\wdm\nf-wdm-iogetdeviceproperty.md) | The IoGetDeviceProperty routine retrieves information about a device such as configuration information and the name of its PDO. |
| [IoGetDevicePropertyData function](..\wdm\nf-wdm-iogetdevicepropertydata.md) | The IoGetDevicePropertyData routine retrieves the current setting for a device property. |
| [IoGetDriverObjectExtension function](..\wdm\nf-wdm-iogetdriverobjectextension.md) | The IoGetDriverObjectExtension routine retrieves a previously allocated per-driver context area. |
| [IoGetFileObjectGenericMapping function](..\ntddk\nf-ntddk-iogetfileobjectgenericmapping.md) | The IoGetFileObjectGenericMapping routine returns information about the mapping between each generic access right and the set of specific access rights for file objects. |
| [IoGetFunctionCodeFromCtlCode function](..\wdm\nf-wdm-iogetfunctioncodefromctlcode.md) | The IoGetFunctionCodeFromCtlCode macro returns the value of the function code contained in an I/O control code. |
| [IoGetInitialStack function](..\wdm\nf-wdm-iogetinitialstack.md) | The IoGetInitialStack routine returns the base address of the current thread's stack. |
| [IoGetInitiatorProcess function](..\ntddk\nf-ntddk-iogetinitiatorprocess.md) | The IoGetInitiatorProcess routine retrieves the process which initiated the creation of a file object if different than the process which is issuing the create. |
| [IoGetIoPriorityHint function](..\wdm\nf-wdm-iogetiopriorityhint.md) | The IoGetIoPriorityHint routine gets the priority hint value from an IRP. |
| [IoGetNextIrpStackLocation function](..\wdm\nf-wdm-iogetnextirpstacklocation.md) | The IoGetNextIrpStackLocation routine gives a higher level driver access to the next-lower driver's I/O stack location in an IRP so the caller can set it up for the lower driver. |
| [IoGetPagingIoPriority function](..\ntddk\nf-ntddk-iogetpagingiopriority.md) | The IoGetPagingIoPriority routine indicates the priority level of a paging I/O request. |
| [IoGetRelatedDeviceObject function](..\wdm\nf-wdm-iogetrelateddeviceobject.md) | Given a file object, the IoGetRelatedDeviceObject routine returns a pointer to the corresponding device object. |
| [IoGetRemainingStackSize function](..\wdm\nf-wdm-iogetremainingstacksize.md) | The IoGetRemainingStackSize routine returns the current amount of available kernel-mode stack space. |
| [IoGetStackLimits function](..\wdm\nf-wdm-iogetstacklimits.md) | The IoGetStackLimits routine returns the boundaries of the current thread's stack frame. |
| [IoIncrementKeepAliveCount function](..\ntddk\nf-ntddk-ioincrementkeepalivecount.md) | The IoIncrementKeepAliveCount routine increments a reference count associated with an Windows app process on a specific device. |
| [IoInitializeDpcRequest function](..\wdm\nf-wdm-ioinitializedpcrequest.md) | The IoInitializeDpcRequest routine registers a driver-supplied DpcForIsr routine. |
| [IoInitializeIrp function](..\wdm\nf-wdm-ioinitializeirp.md) | The IoInitializeIrp routine initializes a given IRP that was allocated by the caller. |
| [IoInitializeRemoveLock function](..\wdm\nf-wdm-ioinitializeremovelock.md) | The IoInitializeRemoveLock routine initializes a remove lock for a device object. |
| [IoInitializeTimer function](..\wdm\nf-wdm-ioinitializetimer.md) | The IoInitializeTimer routine sets up a driver-supplied IoTimer routine associated with a given device object. |
| [IoInitializeWorkItem function](..\wdm\nf-wdm-ioinitializeworkitem.md) | The IoInitializeWorkItem routine initializes a work item that the caller has already allocated. |
| [IoInvalidateDeviceRelations function](..\wdm\nf-wdm-ioinvalidatedevicerelations.md) | The IoInvalidateDeviceRelations routine notifies the PnP manager that the relations for a device (such as bus relations, ejection relations, removal relations, and the target device relation) have changed. |
| [IoInvalidateDeviceState function](..\wdm\nf-wdm-ioinvalidatedevicestate.md) | The IoInvalidateDeviceState routine notifies the PnP manager that some aspect of the PnP state of a device has changed. |
| [IoIs32bitProcess function](..\wdm\nf-wdm-iois32bitprocess.md) | The IoIs32bitProcess routine checks whether the originator of the current I/O request is a 32-bit user-mode application. |
| [IoIsErrorUserInduced function](..\wdm\nf-wdm-ioiserroruserinduced.md) | The IoIsErrorUserInduced routine determines whether an I/O error encountered while processing a request to a removable-media device was caused by the user. |
| [IoIsValidIrpStatus function](..\ntddk\nf-ntddk-ioisvalidirpstatus.md) | The IoIsValidIrpStatus routine validates the specified NTSTATUS status code value. |
| [IoIsWdmVersionAvailable function](..\wdm\nf-wdm-ioiswdmversionavailable.md) | The IoIsWdmVersionAvailable routine checks whether a given WDM version is supported by the operating system. |
| [IoMakeAssociatedIrp function](..\ntddk\nf-ntddk-iomakeassociatedirp.md) | This routine is reserved for use by file systems and file system filter drivers. |
| [IoMarkIrpPending function](..\wdm\nf-wdm-iomarkirppending.md) | The IoMarkIrpPending routine marks the specified IRP, indicating that a driver's dispatch routine subsequently returned STATUS_PENDING because further processing is required by other driver routines. |
| [IoOpenDeviceInterfaceRegistryKey function](..\wdm\nf-wdm-ioopendeviceinterfaceregistrykey.md) | The IoOpenDeviceInterfaceRegistryKey routine returns a handle to a registry key for storing information about a particular device interface instance. |
| [IoOpenDeviceRegistryKey function](..\wdm\nf-wdm-ioopendeviceregistrykey.md) | The IoOpenDeviceRegistryKey routine returns a handle to a device-specific or a driver-specific registry key for a particular device instance. |
| [IoPropagateActivityIdToThread function](..\ntddk\nf-ntddk-iopropagateactivityidtothread.md) | The IoPropagateActivityIdToThread routine associates the activity ID from an IRP with the current thread. |
| [IoQueryFullDriverPath function](..\ntddk\nf-ntddk-ioqueryfulldriverpath.md) | The IoQueryFullDriverPath routine retrieves the full path name of the binary file that is loaded for the specified driver object. |
| [IoQueueWorkItem function](..\wdm\nf-wdm-ioqueueworkitem.md) | The IoQueueWorkItem routine associates a WorkItem routine with a work item, and it inserts the work item into a queue for later processing by a system worker thread. |
| [IoQueueWorkItemEx function](..\wdm\nf-wdm-ioqueueworkitemex.md) | The IoQueueWorkItemEx routine associates a WorkItemEx routine with a work item, and it inserts the work item into a queue for later processing by a system worker thread. |
| [IoRaiseHardError function](..\ntddk\nf-ntddk-ioraiseharderror.md) | The IoRaiseHardError routine causes a dialog box to appears that warns the user that a device I/O error has occurred, which might indicate that a physical device is failing. |
| [IoRaiseInformationalHardError function](..\ntddk\nf-ntddk-ioraiseinformationalharderror.md) | The IoRaiseInformationalHardError routine sends a dialog box to the user, warning about a device I/O error that indicates why a user I/O request failed. |
| [IoRegisterBootDriverCallback function](..\ntddk\nf-ntddk-ioregisterbootdrivercallback.md) | The IoRegisterBootDriverCallback routine registers a BOOT_DRIVER_CALLBACK_FUNCTION routine to be called during the initialization of a boot-start driver and its dependent DLLs. |
| [IoRegisterBootDriverReinitialization function](..\ntddk\nf-ntddk-ioregisterbootdriverreinitialization.md) | The IoRegisterBootDriverReinitialization routine is called by a boot driver to register the driver's reinitialization routine with the I/O manager to be called after all devices have been enumerated and started. |
| [IoRegisterContainerNotification function](..\wdm\nf-wdm-ioregistercontainernotification.md) | The IoRegisterContainerNotification routine registers a kernel-mode driver to receive notifications about a specified class of events. |
| [IoRegisterDeviceInterface function](..\wdm\nf-wdm-ioregisterdeviceinterface.md) | The IoRegisterDeviceInterface routine registers a device interface class, if it has not been previously registered, and creates a new instance of the interface class, which a driver can subsequently enable for use by applications or other system components. |
| [IoRegisterDriverReinitialization function](..\ntddk\nf-ntddk-ioregisterdriverreinitialization.md) | The IoRegisterDriverReinitialization routine is called by a driver during its initialization or reinitialization to register its Reinitialize routine to be called again before the driver's and, possibly the system's, initialization is complete. |
| [IoRegisterLastChanceShutdownNotification function](..\wdm\nf-wdm-ioregisterlastchanceshutdownnotification.md) | The IoRegisterLastChanceShutdownNotification routine registers a driver to receive an IRP_MJ_SHUTDOWN IRP when the system is shut down, after all file systems have been flushed. |
| [IoRegisterPlugPlayNotification function](..\wdm\nf-wdm-ioregisterplugplaynotification.md) | The IoRegisterPlugPlayNotification routine registers a Plug and Play (PnP) notification callback routine to be called when a PnP event of the specified category occurs. |
| [IoRegisterShutdownNotification function](..\wdm\nf-wdm-ioregistershutdownnotification.md) | The IoRegisterShutdownNotification routine registers the driver to receive an IRP_MJ_SHUTDOWN IRP when the system is shut down. |
| [IoReleaseRemoveLock function](..\wdm\nf-wdm-ioreleaseremovelock.md) | The IoReleaseRemoveLock routine releases a remove lock acquired with a previous call to IoAcquireRemoveLock. |
| [IoReleaseRemoveLockAndWait function](..\wdm\nf-wdm-ioreleaseremovelockandwait.md) | The IoReleaseRemoveLockAndWait routine releases a remove lock that the driver acquired in a previous call to IoAcquireRemoveLock, and waits until all acquisitions of the lock have been released. |
| [IoRemoveLinkShareAccess function](..\wdm\nf-wdm-ioremovelinkshareaccess.md) | The IoRemoveLinkShareAccess routine removes the access and link share-access information for a given open instance of a file object. |
| [IoRemoveShareAccess function](..\wdm\nf-wdm-ioremoveshareaccess.md) | The IoRemoveShareAccess routine removes the access and share-access information for a given open instance of a file object. |
| [IoReportDetectedDevice function](..\ntddk\nf-ntddk-ioreportdetecteddevice.md) | The IoReportDetectedDevice routine reports a non-PnP device to the PnP manager. |
| [IoReportInterruptActive function](..\wdm\nf-wdm-ioreportinterruptactive.md) | The IoReportInterruptActive routine informs the operating system that a registered interrupt service routine (ISR) is active and ready to handle interrupt requests. |
| [IoReportInterruptInactive function](..\wdm\nf-wdm-ioreportinterruptinactive.md) | The IoReportInterruptInactive routine informs the operating system that a registered interrupt service routine (ISR) is inactive and is not expecting interrupt requests. |
| [IoReportResourceForDetection function](..\ntddk\nf-ntddk-ioreportresourcefordetection.md) | The IoReportResourceForDetection routine claims hardware resources in the configuration registry for a legacy device. |
| [IoReportRootDevice function](..\ntddk\nf-ntddk-ioreportrootdevice.md) | The IoReportRootDevice routine reports a device that cannot be detected by a PnP bus driver to the PnP Manager. IoReportRootDevice allows only one device per driver to be created. |
| [IoReportTargetDeviceChange function](..\wdm\nf-wdm-ioreporttargetdevicechange.md) | The IoReportTargetDeviceChange routine notifies the PnP manager that a custom event has occurred on a device. |
| [IoReportTargetDeviceChangeAsynchronous function](..\wdm\nf-wdm-ioreporttargetdevicechangeasynchronous.md) | The IoReportTargetDeviceChangeAsynchronous routine notifies the PnP manager that a custom event has occurred on a device. |
| [IoRequestDeviceEject function](..\wdm\nf-wdm-iorequestdeviceeject.md) | The IoRequestDeviceEject routine notifies the PnP manager that the device eject button was pressed. |
| [IoRequestDpc function](..\wdm\nf-wdm-iorequestdpc.md) | The IoRequestDpc routine queues a driver-supplied DpcForIsr routine to complete interrupt-driven I/O processing at a lower IRQL. |
| [IoReuseIrp function](..\wdm\nf-wdm-ioreuseirp.md) | The IoReuseIrp routine reinitializes an IRP so that it can be reused. |
| [IoSetActivityIdIrp function](..\ntddk\nf-ntddk-iosetactivityidirp.md) | The IoSetActivityIdIrp routine associates an activity ID with an IRP. |
| [IoSetActivityIdThread function](..\ntddk\nf-ntddk-iosetactivityidthread.md) | The IoSetActivityIdThread routine associates an activity ID with the current thread. Drivers should use this routine when they are tracing aware and are issuing I/O on a worker thread. |
| [IoSetCancelRoutine function](..\wdm\nf-wdm-iosetcancelroutine.md) | The IoSetCancelRoutine routine sets up a driver-supplied Cancel routine to be called if a given IRP is canceled. |
| [IoSetCompletionRoutine function](..\wdm\nf-wdm-iosetcompletionroutine.md) | The IoSetCompletionRoutine routine registers an IoCompletion routine, which will be called when the next-lower-level driver has completed the requested operation for the given IRP. |
| [IoSetCompletionRoutineEx function](..\wdm\nf-wdm-iosetcompletionroutineex.md) | The IoSetCompletionRoutineEx routine registers an IoCompletion routine, which is called when the next-lower-level driver has completed the requested operation for the given IRP. |
| [IoSetDeviceInterfacePropertyData function](..\wdm\nf-wdm-iosetdeviceinterfacepropertydata.md) | The IoSetDeviceInterfacePropertyData routine modifies the current value of a device interface property. |
| [IoSetDeviceInterfaceState function](..\wdm\nf-wdm-iosetdeviceinterfacestate.md) | The IoSetDeviceInterfaceState routine enables or disables an instance of a previously registered device interface class. |
| [IoSetDevicePropertyData function](..\wdm\nf-wdm-iosetdevicepropertydata.md) | The IoSetDevicePropertyData routine modifies the current setting for a device property. |
| [IoSetHardErrorOrVerifyDevice function](..\ntddk\nf-ntddk-iosetharderrororverifydevice.md) | Lower-level drivers call the IoSetHardErrorOrVerifyDevice routine to identify a removable media device that has encountered an error, so that a file system driver can prompt the user to verify that the medium is valid. |
| [IoSetIoPriorityHint function](..\wdm\nf-wdm-iosetiopriorityhint.md) | The IoSetIoPriorityHint routine sets the priority hint value for an IRP. |
| [IoSetLinkShareAccess function](..\wdm\nf-wdm-iosetlinkshareaccess.md) | The IoSetLinkShareAccess routine sets the access rights for link sharing the specified file object. |
| [IoSetMasterIrpStatus function](..\ntddk\nf-ntddk-iosetmasterirpstatus.md) | The IoSetMasterIrpStatus routine conditionally replaces the Status value in an IRP with the specified NTSTATUS value. |
| [IoSetNextIrpStackLocation function](..\wdm\nf-wdm-iosetnextirpstacklocation.md) | The IoSetNextIrpStackLocation routine sets the IRP stack location in a driver-allocated IRP to that of the caller. |
| [IoSetShareAccess function](..\wdm\nf-wdm-iosetshareaccess.md) | The IoSetShareAccess routine sets the access rights for sharing the given file object. |
| [IoSetShareAccessEx function](..\wdm\nf-wdm-iosetshareaccessex.md) | The IoSetShareAccessEx routine sets the access rights for sharing the specified file object. |
| [IoSetStartIoAttributes function](..\ntifs\nf-ntifs-iosetstartioattributes.md) | The IoSetStartIoAttributes routine sets attributes for the driver's StartIo routine. |
| [IoSetStartIoAttributes function](..\wdm\nf-wdm-iosetstartioattributes.md) | The IoSetStartIoAttributes routine sets attributes for the driver's StartIo routine. |
| [IoSetSystemPartition function](..\ntddk\nf-ntddk-iosetsystempartition.md) | The IoSetSystemPartition routine sets the boot partition for the system. |
| [IoSetThreadHardErrorMode function](..\ntddk\nf-ntddk-iosetthreadharderrormode.md) | The IoSetThreadHardErrorMode routine enables or disables hard error reporting for the current thread. |
| [IoSizeOfIrp function](..\ntifs\nf-ntifs-iosizeofirp.md) | The IoSizeOfIrp routine determines the size in bytes for an IRP, given the number of stack locations in the IRP. |
| [IoSizeOfIrp function](..\wdm\nf-wdm-iosizeofirp.md) | The IoSizeOfIrp routine determines the size in bytes for an IRP, given the number of stack locations in the IRP. |
| [IoSizeofWorkItem function](..\wdm\nf-wdm-iosizeofworkitem.md) | The IoSizeofWorkItem routine returns the size, in bytes, of an IO_WORKITEM structure. |
| [IoStartNextPacket function](..\ntifs\nf-ntifs-iostartnextpacket.md) | The IoStartNextPacket routine dequeues the next IRP, if any, from the given device object's associated device queue and calls the driver's StartIo routine. |
| [IoStartNextPacket function](..\wdm\nf-wdm-iostartnextpacket.md) | The IoStartNextPacket routine dequeues the next IRP, if any, from the given device object's associated device queue and calls the driver's StartIo routine. |
| [IoStartNextPacketByKey function](..\ntifs\nf-ntifs-iostartnextpacketbykey.md) | The IoStartNextPacketByKey routine dequeues the next I/O request packet from the specified device object's associated device queue according to a specified sort-key value and calls the driver's StartIo routine with that IRP. |
| [IoStartNextPacketByKey function](..\wdm\nf-wdm-iostartnextpacketbykey.md) | The IoStartNextPacketByKey routine dequeues the next I/O request packet from the specified device object's associated device queue according to a specified sort-key value and calls the driver's StartIo routine with that IRP. |
| [IoStartPacket function](..\ntifs\nf-ntifs-iostartpacket.md) | The IoStartPacket routine calls the driver's StartIo routine with the given IRP or inserts the IRP into the device queue associated with the given device object if the device is already busy. |
| [IoStartPacket function](..\wdm\nf-wdm-iostartpacket.md) | The IoStartPacket routine calls the driver's StartIo routine with the given IRP or inserts the IRP into the device queue associated with the given device object if the device is already busy. |
| [IoStartTimer function](..\ntifs\nf-ntifs-iostarttimer.md) | The IoStartTimer routine enables the timer associated with a given device object so the driver-supplied IoTimer routine is called once per second. |
| [IoStartTimer function](..\wdm\nf-wdm-iostarttimer.md) | The IoStartTimer routine enables the timer associated with a given device object so the driver-supplied IoTimer routine is called once per second. |
| [IoStopTimer function](..\ntifs\nf-ntifs-iostoptimer.md) | The IoStopTimer routine disables the timer for a specified device object so the driver-supplied IoTimer routine is not called. |
| [IoStopTimer function](..\wdm\nf-wdm-iostoptimer.md) | The IoStopTimer routine disables the timer for a specified device object so the driver-supplied IoTimer routine is not called. |
| [IoTransferActivityId function](..\ntddk\nf-ntddk-iotransferactivityid.md) | The IoTransferActivityId routine logs an ETW transfer event using the I/O tracing provider on behalf of the caller. This allows a driver to associate two related activity IDs without requiring a specific provider to be enabled. |
| [IoUninitializeWorkItem function](..\wdm\nf-wdm-iouninitializeworkitem.md) | The IoUninitializeWorkItem routine uninitializes a work item that was initialized by IoInitializeWorkItem. |
| [IoUnregisterBootDriverCallback function](..\ntddk\nf-ntddk-iounregisterbootdrivercallback.md) | The IoUnRegisterBootDriverCallback routine unregisters a previously registered BOOT_DRIVER_CALLBACK_FUNCTION routine. |
| [IoUnregisterContainerNotification function](..\wdm\nf-wdm-iounregistercontainernotification.md) | The IoUnregisterContainerNotification routine cancels a container notification registration that was previously created by the IoRegisterContainerNotification routine. |
| [IoUnregisterPlugPlayNotification function](..\wdm\nf-wdm-iounregisterplugplaynotification.md) | This routine is obsolete in Windows 7 and later versions of Windows. For more information, see the following Remarks section.The IoUnregisterPlugPlayNotification routine removes the registration of a driver's callback routine for a PnP event. |
| [IoUnregisterPlugPlayNotificationEx function](..\wdm\nf-wdm-iounregisterplugplaynotificationex.md) | The IoUnregisterPlugPlayNotificationEx routine cancels the registration of a driver's callback routine for notifications of Plug and Play (PnP) events. |
| [IoUnregisterShutdownNotification function](..\wdm\nf-wdm-iounregistershutdownnotification.md) | The IoUnregisterShutdownNotification routine removes a registered driver from the shutdown notification queue. |
| [IoUpdateLinkShareAccess function](..\wdm\nf-wdm-ioupdatelinkshareaccess.md) | The IoUpdateLinkShareAccess routine updates the share access for the given file object, usually when the file is being opened. |
| [IoUpdateShareAccess function](..\wdm\nf-wdm-ioupdateshareaccess.md) | The IoUpdateShareAccess routine updates the share access for the given file object, usually when the file is being opened. |
| [IoValidateDeviceIoControlAccess function](..\wdm\nf-wdm-iovalidatedeviceiocontrolaccess.md) | For more information, see the WdmlibIoValidateDeviceIoControlAccess function. |
| [IoVerifyPartitionTable function](..\ntddk\nf-ntddk-ioverifypartitiontable.md) | The IoVerifyPartitionTable routine checks the validity of the partition table for a disk. |
| [IoVolumeDeviceToDosName function](..\ntddk\nf-ntddk-iovolumedevicetodosname.md) | The IoVolumeDeviceToDosName routine returns the MS-DOS path for a specified device object that represents a file system volume. |
| [IoWMIAllocateInstanceIds function](..\wdm\nf-wdm-iowmiallocateinstanceids.md) | The IoWMIAllocateInstanceIds routine allocates one or more instance IDs that are unique to the GUID. |
| [IoWMIDeviceObjectToInstanceName function](..\wdm\nf-wdm-iowmideviceobjecttoinstancename.md) | The IoWMIDeviceObjectToInstanceName routine determines the instance name for the WMI class instance implemented by the driver that is specified by a device object. |
| [IoWMIDeviceObjectToProviderId function](..\wdm\nf-wdm-iowmideviceobjecttoproviderid.md) | The IoWMIDeviceObjectToProviderId routine translates the specified device object into the corresponding WMI Provider ID. |
| [IoWMIDeviceObjectToProviderId function](..\wdm\nf-wdm-iowmideviceobjecttoproviderid~r1.md) | The IoWMIDeviceObjectToProviderId routine translates the specified device object into the corresponding WMI Provider ID. |
| [IoWMIExecuteMethod function](..\wdm\nf-wdm-iowmiexecutemethod.md) | The IoWMIExecuteMethod routine runs a WMI class method on the specified WMI data block instance. |
| [IoWMIHandleToInstanceName function](..\wdm\nf-wdm-iowmihandletoinstancename.md) | The IoWMIHandleToInstanceName routine determines the instance name for the WMI class instance implemented by the driver that is specified by a file handle. |
| [IoWMIOpenBlock function](..\wdm\nf-wdm-iowmiopenblock.md) | The IoWMIOpenBlock routine opens the WMI data block object for the specified WMI class. |
| [IoWMIQueryAllData function](..\wdm\nf-wdm-iowmiqueryalldata.md) | The IoWMIQueryAllData routine returns all WMI data blocks that implement a given WMI class. |
| [IoWMIQueryAllDataMultiple function](..\wdm\nf-wdm-iowmiqueryalldatamultiple.md) | The IoWMIQueryAllDataMultiple routine returns all WMI data blocks that implement one of a set of WMI classes. |
| [IoWMIQuerySingleInstance function](..\wdm\nf-wdm-iowmiquerysingleinstance.md) | The IoWMIQuerySingleInstance routine returns the specified instance of a WMI data block. |
| [IoWMIQuerySingleInstanceMultiple function](..\wdm\nf-wdm-iowmiquerysingleinstancemultiple.md) | The IoWMIQuerySingleInstanceMultiple routine returns all WMI data block instances that implement the specified WMI classes with the specified instance names. |
| [IoWMIRegistrationControl function](..\wdm\nf-wdm-iowmiregistrationcontrol.md) | The IoWMIRegistrationControl routine registers or unregisters the caller as a WMI data provider for a specified device object. |
| [IoWMISetNotificationCallback function](..\wdm\nf-wdm-iowmisetnotificationcallback.md) | The IoWMISetNotificationCallback routine registers a notification callback for a WMI event. |
| [IoWMISetSingleInstance function](..\wdm\nf-wdm-iowmisetsingleinstance.md) | The IoWMISetSingleInstance routine sets the values for properties within the data block instance that matches the specified WMI class and instance name. |
| [IoWMISetSingleItem function](..\wdm\nf-wdm-iowmisetsingleitem.md) | The IoWMISetSingleItem routine sets a single property in the data block instance that matches the specified WMI class and instance name. |
| [IoWMISuggestInstanceName function](..\wdm\nf-wdm-iowmisuggestinstancename.md) | The IoWMISuggestInstanceName routine is used to request that WMI suggest a base name which a driver can use to build WMI instance names for the device. |
| [IoWMIWriteEvent function](..\wdm\nf-wdm-iowmiwriteevent.md) | The IoWMIWriteEvent routine delivers a given event to the user-mode WMI components for notification. |
| [IoWithinStackLimits function](..\wdm\nf-wdm-iowithinstacklimits.md) | The IoWithinStackLimits routine determines whether a region of memory is within the stack limit of the current thread. |
| [IoWriteErrorLogEntry function](..\ntifs\nf-ntifs-iowriteerrorlogentry.md) | The IoWriteErrorLogEntry routine queues a given error log packet to the system error logging thread. |
| [IoWriteErrorLogEntry function](..\wdm\nf-wdm-iowriteerrorlogentry.md) | The IoWriteErrorLogEntry routine queues a given error log packet to the system error logging thread. |
| [IsListEmpty function](..\wdm\nf-wdm-islistempty.md) | The IsListEmpty routine indicates whether a doubly linked list of LIST_ENTRY structures is empty. |
| [KeAcquireSpinLock function](..\wdm\nf-wdm-keacquirespinlock.md) | The KeAcquireSpinLock routine acquires a spin lock so the caller can synchronize access to shared data in a multiprocessor-safe way by raising IRQL. |
| [KeAcquireSpinLock function](..\wdm\nf-wdm-keacquirespinlock~r1.md) | The KeAcquireSpinLock routine acquires a spin lock so the caller can synchronize access to shared data in a multiprocessor-safe way by raising IRQL. |
| [KeAcquireSpinLockAtDpcLevel function](..\wdm\nf-wdm-keacquirespinlockatdpclevel.md) | The KeAcquireSpinLockAtDpcLevel routine acquires a spin lock when the caller is already running at IRQL &gt;= DISPATCH_LEVEL. |
| [KeAreAllApcsDisabled function](..\wdm\nf-wdm-keareallapcsdisabled.md) | The KeAreAllApcsDisabled routine indicates whether the calling thread is inside a guarded region or running at IRQL &gt;= APC_LEVEL, which disables all APC delivery. |
| [KeAreApcsDisabled function](..\ntddk\nf-ntddk-keareapcsdisabled.md) | The KeAreApcsDisabled routine returns whether the calling thread is within a critical region or a guarded region, which disables normal kernel APC delivery. |
| [KeAreApcsDisabled function](..\wdm\nf-wdm-keareapcsdisabled.md) | The KeAreApcsDisabled routine returns whether the calling thread is within a critical region or a guarded region, which disables normal kernel APC delivery. |
| [KeBugCheck function](..\ntddk\nf-ntddk-kebugcheck.md) | The KeBugCheck routine brings down the system in a controlled manner when the caller discovers an unrecoverable inconsistency that would corrupt the system if the caller continued to run. |
| [KeBugCheckEx function](..\wdm\nf-wdm-kebugcheckex.md) | The KeBugCheckEx routine brings down the system in a controlled manner when the caller discovers an unrecoverable inconsistency that would corrupt the system if the caller continued to run. |
| [KeCancelTimer function](..\wdm\nf-wdm-kecanceltimer.md) | The KeCancelTimer routine dequeues a timer object before the timer interval, if any was set, expires. |
| [KeClearEvent function](..\wdm\nf-wdm-keclearevent.md) | The KeClearEvent routine sets an event to a not-signaled state. |
| [KeConvertAuxiliaryCounterToPerformanceCounter function](..\wdm\nf-wdm-keconvertauxiliarycountertoperformancecounter.md) | The KeConvertAuxiliaryCounterToPerformanceCounter routine converts the specified auxiliary counter value into a performance counter value. |
| [KeConvertPerformanceCounterToAuxiliaryCounter function](..\wdm\nf-wdm-keconvertperformancecountertoauxiliarycounter.md) | The KeConvertPerformanceCounterToAuxiliaryCounter routine converts the specified performance counter value into an auxiliary counter value. |
| [KeDelayExecutionThread function](..\wdm\nf-wdm-kedelayexecutionthread.md) | The KeDelayExecutionThread routine puts the current thread into an alertable or nonalertable wait state for a specified interval. |
| [KeDeregisterBoundCallback function](..\wdm\nf-wdm-kederegisterboundcallback.md) | The KeDeregisterBoundCallback routine deregisters a user-mode bound exception callback registered by KeRegisterBoundCallback. |
| [KeDeregisterBugCheckCallback function](..\wdm\nf-wdm-kederegisterbugcheckcallback.md) | The KeDeregisterBugCheckCallback routine removes a callback routine that was registered by KeRegisterBugCheckCallback. |
| [KeDeregisterBugCheckReasonCallback function](..\wdm\nf-wdm-kederegisterbugcheckreasoncallback.md) | The KeDeregisterBugCheckReasonCallback routine removes a callback routine that was registered by KeRegisterBugCheckReasonCallback. |
| [KeDeregisterNmiCallback function](..\wdm\nf-wdm-kederegisternmicallback.md) | The KeDeregisterNmiCallback routine deregisters a nonmaskable interrupt (NMI) callback registered by KeRegisterNmiCallback. |
| [KeDeregisterProcessorChangeCallback function](..\wdm\nf-wdm-kederegisterprocessorchangecallback.md) | The KeDeregisterProcessorChangeCallback routine unregisters a callback function that was previously registered with the operating system by calling the KeRegisterProcessorChangeCallback routine. |
| [KeEnterCriticalRegion function](..\ntddk\nf-ntddk-keentercriticalregion.md) | The KeEnterCriticalRegion routine temporarily disables the execution of normal kernel APCs, but does not prevent special kernel APCs from running. |
| [KeEnterCriticalRegion function](..\wdm\nf-wdm-keentercriticalregion.md) | The KeEnterCriticalRegion routine temporarily disables the execution of normal kernel APCs, but does not prevent special kernel APCs from running. |
| [KeEnterGuardedRegion function](..\ntddk\nf-ntddk-keenterguardedregion.md) | The KeEnterGuardedRegion routine enters a guarded region, which disables all kernel-mode APC delivery to the current thread. |
| [KeEnterGuardedRegion function](..\wdm\nf-wdm-keenterguardedregion.md) | The KeEnterGuardedRegion routine enters a guarded region, which disables all kernel-mode APC delivery to the current thread. |
| [KeExpandKernelStackAndCallout function](..\ntddk\nf-ntddk-keexpandkernelstackandcallout.md) | The KeExpandKernelStackAndCallout routine calls a routine with a guaranteed amount of stack space. |
| [KeFlushIoBuffers function](..\wdm\nf-wdm-keflushiobuffers.md) | The KeFlushIoBuffers routine flushes the memory region described by an MDL from caches of all processors. |
| [KeFlushIoBuffers function](..\wdm\nf-wdm-keflushiobuffers~r1.md) | The KeFlushIoBuffers routine flushes the memory region described by an MDL from caches of all processors. |
| [KeFlushIoBuffers function](..\wdm\nf-wdm-keflushiobuffers~r2.md) | The KeFlushIoBuffers routine flushes the memory region described by an MDL from caches of all processors. |
| [KeFlushIoBuffers function](..\wdm\nf-wdm-keflushiobuffers~r3.md) | The KeFlushIoBuffers routine flushes the memory region described by an MDL from caches of all processors. |
| [KeFlushIoBuffers function](..\wdm\nf-wdm-keflushiobuffers~r4.md) | The KeFlushIoBuffers routine flushes the memory region described by an MDL from caches of all processors. |
| [KeFlushQueuedDpcs function](..\wdm\nf-wdm-keflushqueueddpcs.md) | The KeFlushQueuedDpcs routine returns after all queued DPCs on all processors have executed. |
| [KeGetCurrentIrql function](..\wdm\nf-wdm-kegetcurrentirql.md) | The KeGetCurrentIrql routine returns the current IRQL. |
| [KeGetCurrentIrql function](..\wdm\nf-wdm-kegetcurrentirql~r1.md) | The KeGetCurrentIrql routine returns the current IRQL. |
| [KeGetCurrentIrql function](..\wdm\nf-wdm-kegetcurrentirql~r2.md) | The KeGetCurrentIrql routine returns the current IRQL. |
| [KeGetCurrentIrql function](..\wdm\nf-wdm-kegetcurrentirql~r3.md) | The KeGetCurrentIrql routine returns the current IRQL. |
| [KeGetCurrentNodeNumber function](..\ntddk\nf-ntddk-kegetcurrentnodenumber.md) | The KeGetCurrentNodeNumber routine gets the NUMA node number for the logical processor that the caller is running on. |
| [KeGetCurrentNodeNumber function](..\wdm\nf-wdm-kegetcurrentnodenumber.md) | The KeGetCurrentNodeNumber routine gets the NUMA node number for the logical processor that the caller is running on. |
| [KeGetCurrentProcessorNumber function](..\ntddk\nf-ntddk-kegetcurrentprocessornumber.md) | The KeGetCurrentProcessorNumber routine returns the system-assigned number of the current processor on which the caller is running. |
| [KeGetCurrentProcessorNumber function](..\ntddk\nf-ntddk-kegetcurrentprocessornumber~r1.md) | The KeGetCurrentProcessorNumber routine returns the system-assigned number of the current processor on which the caller is running. |
| [KeGetCurrentProcessorNumber function](..\ntddk\nf-ntddk-kegetcurrentprocessornumber~r2.md) | The KeGetCurrentProcessorNumber routine returns the system-assigned number of the current processor on which the caller is running. |
| [KeGetCurrentProcessorNumber function](..\ntddk\nf-ntddk-kegetcurrentprocessornumber~r3.md) | The KeGetCurrentProcessorNumber routine returns the system-assigned number of the current processor on which the caller is running. |
| [KeGetCurrentProcessorNumberEx function](..\ntddk\nf-ntddk-kegetcurrentprocessornumberex.md) | The KeGetCurrentProcessorNumberEx routine gets the processor number of the logical processor that the caller is running on. |
| [KeGetCurrentProcessorNumberEx function](..\wdm\nf-wdm-kegetcurrentprocessornumberex.md) | The KeGetCurrentProcessorNumberEx routine gets the processor number of the logical processor that the caller is running on. |
| [KeGetCurrentThread function](..\wdm\nf-wdm-kegetcurrentthread.md) | The KeGetCurrentThread routine identifies the current thread. |
| [KeGetCurrentThread function](..\wdm\nf-wdm-kegetcurrentthread~r1.md) | The KeGetCurrentThread routine identifies the current thread. |
| [KeGetProcessorIndexFromNumber function](..\ntifs\nf-ntifs-kegetprocessorindexfromnumber.md) | The KeGetProcessorIndexFromNumber routine converts a group number and a group-relative processor number to a systemwide processor index. |
| [KeGetProcessorIndexFromNumber function](..\wdm\nf-wdm-kegetprocessorindexfromnumber.md) | The KeGetProcessorIndexFromNumber routine converts a group number and a group-relative processor number to a systemwide processor index. |
| [KeGetProcessorNumberFromIndex function](..\wdm\nf-wdm-kegetprocessornumberfromindex.md) | The KeGetProcessorNumberFromIndex routine converts a systemwide processor index to a group number and a group-relative processor number. |
| [KeGetRecommendedSharedDataAlignment function](..\wdm\nf-wdm-kegetrecommendedshareddataalignment.md) | The KeGetRecommendedSharedDataAlignment routine returns the preferred alignment for memory structures that can be accessed by more than one processor. |
| [KeInitializeCrashDumpHeader function](..\wdm\nf-wdm-keinitializecrashdumpheader.md) | The KeInitializeCrashDumpHeader routine supplies the header information the system requires for a crash dump file. |
| [KeInitializeDeviceQueue function](..\wdm\nf-wdm-keinitializedevicequeue.md) | The KeInitializeDeviceQueue routine initializes a device queue object to a not-busy state. |
| [KeInitializeDpc function](..\wdm\nf-wdm-keinitializedpc.md) | The KeInitializeDpc routine initializes a DPC object, and registers a CustomDpc routine for that object. |
| [KeInitializeEvent function](..\wdm\nf-wdm-keinitializeevent.md) | The KeInitializeEvent routine initializes an event object as a synchronization (single waiter) or notification type event and sets it to a signaled or not-signaled state. |
| [KeInitializeGuardedMutex function](..\wdm\nf-wdm-keinitializeguardedmutex.md) | The KeInitializeGuardedMutex routine initializes a guarded mutex. |
| [KeInitializeMutex function](..\wdm\nf-wdm-keinitializemutex.md) | The KeInitializeMutex routine initializes a mutex object, setting it to a signaled state. |
| [KeInitializeSemaphore function](..\wdm\nf-wdm-keinitializesemaphore.md) | The KeInitializeSemaphore routine initializes a semaphore object with a specified count and specifies an upper limit that the count can attain. |
| [KeInitializeSpinLock function](..\wdm\nf-wdm-keinitializespinlock.md) | The KeInitializeSpinLock routine initializes a variable of type KSPIN_LOCK. |
| [KeInitializeThreadedDpc function](..\wdm\nf-wdm-keinitializethreadeddpc.md) | The KeInitializeThreadedDpc routine initializes a threaded DPC object, and registers a CustomThreadedDpc routine for that object. |
| [KeInitializeTimer function](..\wdm\nf-wdm-keinitializetimer.md) | The KeInitializeTimer routine initializes a timer object. |
| [KeInitializeTimerEx function](..\wdm\nf-wdm-keinitializetimerex.md) | The KeInitializeTimerEx routine initializes an extended kernel timer object. |
| [KeInsertByKeyDeviceQueue function](..\wdm\nf-wdm-keinsertbykeydevicequeue.md) | The KeInsertByKeyDeviceQueue routine acquires the spin lock for the specified DeviceQueue and queues an entry according to the specified sort-key value if the device queue is set to a busy state. |
| [KeInsertDeviceQueue function](..\wdm\nf-wdm-keinsertdevicequeue.md) | The KeInsertDeviceQueue routine acquires the spin lock for the specified device queue object and, if the device queue is set to a busy state, queues the specified entry. |
| [KeInsertQueueDpc function](..\wdm\nf-wdm-keinsertqueuedpc.md) | The KeInsertQueueDpc routine queues a DPC for execution. |
| [KeInvalidateAllCaches function](..\ntddk\nf-ntddk-keinvalidateallcaches.md) | The KeInvalidateAllCaches routine flushes all processor caches. |
| [KeIpiGenericCall function](..\wdm\nf-wdm-keipigenericcall.md) | The KeIpiGenericCall routine causes the specified routine to run on all processors simultaneously. |
| [KeLeaveCriticalRegion function](..\ntddk\nf-ntddk-keleavecriticalregion.md) | The KeLeaveCriticalRegion routine reenables the delivery of normal kernel-mode APCs that were disabled by a preceding call to KeEnterCriticalRegion. |
| [KeLeaveCriticalRegion function](..\wdm\nf-wdm-keleavecriticalregion.md) | The KeLeaveCriticalRegion routine reenables the delivery of normal kernel-mode APCs that were disabled by a preceding call to KeEnterCriticalRegion. |
| [KeLeaveGuardedRegion function](..\ntddk\nf-ntddk-keleaveguardedregion.md) | The KeLeaveGuardedRegion routine exits a guarded region entered by KeEnterGuardedRegion. |
| [KeLeaveGuardedRegion function](..\wdm\nf-wdm-keleaveguardedregion.md) | The KeLeaveGuardedRegion routine exits a guarded region entered by KeEnterGuardedRegion. |
| [KeLowerIrql function](..\wdm\nf-wdm-kelowerirql.md) | The KeLowerIrql routine restores the IRQL on the current processor to its original value. |
| [KeLowerIrql function](..\wdm\nf-wdm-kelowerirql~r1.md) | The KeLowerIrql routine restores the IRQL on the current processor to its original value. |
| [KeMemoryBarrier function](..\wdm\nf-wdm-kememorybarrier.md) | The KeMemoryBarrier routine creates a barrier at its position in the code&#8212;across which the compiler and the processor cannot move any operations. |
| [KeMemoryBarrier function](..\wdm\nf-wdm-kememorybarrier~r1.md) | The KeMemoryBarrier routine creates a barrier at its position in the code&#8212;across which the compiler and the processor cannot move any operations. |
| [KeMemoryBarrier function](..\wdm\nf-wdm-kememorybarrier~r2.md) | The KeMemoryBarrier routine creates a barrier at its position in the code&#8212;across which the compiler and the processor cannot move any operations. |
| [KeMemoryBarrier function](..\wdm\nf-wdm-kememorybarrier~r3.md) | The KeMemoryBarrier routine creates a barrier at its position in the code&#8212;across which the compiler and the processor cannot move any operations. |
| [KePulseEvent function](..\ntddk\nf-ntddk-kepulseevent.md) | The KePulseEvent routine atomically sets an event object to a signaled state, attempts to satisfy as many waits as possible, and then resets the event object to a not-signaled state. |
| [KeQueryActiveGroupCount function](..\ntddk\nf-ntddk-kequeryactivegroupcount.md) | The KeQueryActiveGroupCount routine returns the number of active processor groups in a multiprocessor system. |
| [KeQueryActiveGroupCount function](..\wdm\nf-wdm-kequeryactivegroupcount.md) | The KeQueryActiveGroupCount routine returns the number of active processor groups in a multiprocessor system. |
| [KeQueryActiveProcessorCount function](..\ntddk\nf-ntddk-kequeryactiveprocessorcount.md) | The KeQueryActiveProcessorCount routine returns the number of currently active processors. |
| [KeQueryActiveProcessorCountEx function](..\ntddk\nf-ntddk-kequeryactiveprocessorcountex.md) | The KeQueryActiveProcessorCountEx routine returns the number of active logical processors in a specified group in a multiprocessor system or in the entire system. |
| [KeQueryActiveProcessorCountEx function](..\wdm\nf-wdm-kequeryactiveprocessorcountex.md) | The KeQueryActiveProcessorCountEx routine returns the number of active logical processors in a specified group in a multiprocessor system or in the entire system. |
| [KeQueryActiveProcessors function](..\ntddk\nf-ntddk-kequeryactiveprocessors.md) | The KeQueryActiveProcessors routine returns a bitmask of the currently active processors. |
| [KeQueryAuxiliaryCounterFrequency function](..\wdm\nf-wdm-kequeryauxiliarycounterfrequency.md) | The KeQueryAuxiliaryCounterFrequency routine returns frequency of the auxiliary counter in units of Hz. |
| [KeQueryDpcWatchdogInformation function](..\wdm\nf-wdm-kequerydpcwatchdoginformation.md) | The KeQueryDpcWatchdogInformation routine returns the deferred procedure call (DPC) watchdog timer values for the current processor. |
| [KeQueryGroupAffinity function](..\ntddk\nf-ntddk-kequerygroupaffinity.md) | The KeQueryGroupAffinity routine returns an affinity mask that identifies the active logical processors in a specified group in a multiprocessor system. |
| [KeQueryGroupAffinity function](..\wdm\nf-wdm-kequerygroupaffinity.md) | The KeQueryGroupAffinity routine returns an affinity mask that identifies the active logical processors in a specified group in a multiprocessor system. |
| [KeQueryHardwareCounterConfiguration function](..\ntddk\nf-ntddk-kequeryhardwarecounterconfiguration.md) | The KeQueryHardwareCounterConfiguration routine queries the operating system for the list of hardware counters to use for thread profiling. |
| [KeQueryHighestNodeNumber function](..\ntddk\nf-ntddk-kequeryhighestnodenumber.md) | The KeQueryHighestNodeNumber routine returns the highest node number in a multiprocessor system that has a non-uniform memory access (NUMA) architecture. |
| [KeQueryHighestNodeNumber function](..\wdm\nf-wdm-kequeryhighestnodenumber.md) | The KeQueryHighestNodeNumber routine returns the highest node number in a multiprocessor system that has a non-uniform memory access (NUMA) architecture. |
| [KeQueryInterruptTime function](..\wdm\nf-wdm-kequeryinterrupttime.md) | The KeQueryInterruptTime routine returns the current value of the system interrupt time count, with accuracy to within system clock tick. |
| [KeQueryInterruptTimePrecise function](..\wdm\nf-wdm-kequeryinterrupttimeprecise.md) | The KeQueryInterruptTimePrecise routine returns the current value of the system interrupt time count, with accuracy to within a microsecond. |
| [KeQueryLogicalProcessorRelationship function](..\ntddk\nf-ntddk-kequerylogicalprocessorrelationship.md) | The KeQueryLogicalProcessorRelationship routine gets information about the relationships of one or more processors to the other processors in a multiprocessor system. |
| [KeQueryLogicalProcessorRelationship function](..\wdm\nf-wdm-kequerylogicalprocessorrelationship.md) | The KeQueryLogicalProcessorRelationship routine gets information about the relationships of one or more processors to the other processors in a multiprocessor system. |
| [KeQueryMaximumGroupCount function](..\ntddk\nf-ntddk-kequerymaximumgroupcount.md) | The KeQueryMaximumGroupCount routine returns the maximum number of groups in a multiprocessor system. |
| [KeQueryMaximumGroupCount function](..\wdm\nf-wdm-kequerymaximumgroupcount.md) | The KeQueryMaximumGroupCount routine returns the maximum number of groups in a multiprocessor system. |
| [KeQueryMaximumProcessorCount function](..\ntddk\nf-ntddk-kequerymaximumprocessorcount.md) | The KeQueryMaximumProcessorCount routine returns the maximum number of processors. |
| [KeQueryMaximumProcessorCountEx function](..\ntddk\nf-ntddk-kequerymaximumprocessorcountex.md) | The KeQueryMaximumProcessorCountEx routine returns the maximum number of logical processors in a specified group in a multiprocessor system. |
| [KeQueryMaximumProcessorCountEx function](..\wdm\nf-wdm-kequerymaximumprocessorcountex.md) | The KeQueryMaximumProcessorCountEx routine returns the maximum number of logical processors in a specified group in a multiprocessor system. |
| [KeQueryNodeActiveAffinity function](..\ntddk\nf-ntddk-kequerynodeactiveaffinity.md) | The KeQueryNodeActiveAffinity routine gets the current processor affinity of a specified node in a multiprocessor system that has a non-uniform memory access (NUMA) architecture. |
| [KeQueryNodeActiveAffinity function](..\wdm\nf-wdm-kequerynodeactiveaffinity.md) | The KeQueryNodeActiveAffinity routine gets the current processor affinity of a specified node in a multiprocessor system that has a non-uniform memory access (NUMA) architecture. |
| [KeQueryNodeMaximumProcessorCount function](..\ntddk\nf-ntddk-kequerynodemaximumprocessorcount.md) | The KeQueryNodeMaximumProcessorCount routine returns the maximum number of logical processors that a specified node in a non-uniform memory access (NUMA) multiprocessor system can contain. |
| [KeQueryNodeMaximumProcessorCount function](..\wdm\nf-wdm-kequerynodemaximumprocessorcount.md) | The KeQueryNodeMaximumProcessorCount routine returns the maximum number of logical processors that a specified node in a non-uniform memory access (NUMA) multiprocessor system can contain. |
| [KeQueryPerformanceCounter function](..\ntifs\nf-ntifs-kequeryperformancecounter.md) | The KeQueryPerformanceCounter routine retrieves the current value and frequency of the performance counter.Use KeQueryPerformanceCounter to acquire high resolution (&lt;1us) time stamps for time interval measurements. |
| [KeQueryPerformanceCounter function](..\wdm\nf-wdm-kequeryperformancecounter.md) | The KeQueryPerformanceCounter routine retrieves the current value and frequency of the performance counter.Use KeQueryPerformanceCounter to acquire high resolution (&lt;1us) time stamps for time interval measurements. |
| [KeQueryPriorityThread function](..\wdm\nf-wdm-kequeryprioritythread.md) | The KeQueryPriorityThread routine returns the current priority of a particular thread. |
| [KeQueryRuntimeThread function](..\wdm\nf-wdm-kequeryruntimethread.md) | The KeQueryRuntimeThread routine reports the accumulated kernel-mode and user-mode run time of a thread, in clock ticks. |
| [KeQuerySystemTime function](..\wdm\nf-wdm-kequerysystemtime.md) | The KeQuerySystemTime routine obtains the current system time. |
| [KeQuerySystemTime function](..\wdm\nf-wdm-kequerysystemtime~r1.md) | The KeQuerySystemTime routine obtains the current system time. |
| [KeQuerySystemTimePrecise function](..\wdm\nf-wdm-kequerysystemtimeprecise.md) | The KeQuerySystemTimePrecise routine retrieves the current system time, and is more precise than the KeQuerySystemTime routine. |
| [KeQueryTickCount function](..\ntddk\nf-ntddk-kequerytickcount.md) | The KeQueryTickCount routine maintains a count of the interval timer interrupts that have occurred since the system was booted. |
| [KeQueryTickCount function](..\ntddk\nf-ntddk-kequerytickcount~r1.md) | The KeQueryTickCount routine maintains a count of the interval timer interrupts that have occurred since the system was booted. |
| [KeQueryTickCount function](..\ntddk\nf-ntddk-kequerytickcount~r2.md) | The KeQueryTickCount routine maintains a count of the interval timer interrupts that have occurred since the system was booted. |
| [KeQueryTickCount function](..\wdm\nf-wdm-kequerytickcount.md) | The KeQueryTickCount routine maintains a count of the interval timer interrupts that have occurred since the system was booted. |
| [KeQueryTimeIncrement function](..\wdm\nf-wdm-kequerytimeincrement.md) | The KeQueryTimeIncrement routine returns the number of 100-nanosecond units that are added to the system time each time the interval clock interrupts. |
| [KeQueryTotalCycleTimeThread function](..\wdm\nf-wdm-kequerytotalcycletimethread.md) | The KeQueryTotalCycleTimeThread routine returns the accumulated cycle time for the specified thread. |
| [KeQueryUnbiasedInterruptTime function](..\wdm\nf-wdm-kequeryunbiasedinterrupttime.md) | The KeQueryUnbiasedInterruptTime routine returns the current value of the system interrupt time count. |
| [KeRaiseIrql function](..\wdm\nf-wdm-keraiseirql.md) | The KeRaiseIrql routine raises the hardware priority to the specified IRQL value, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [KeRaiseIrqlToDpcLevel function](..\ntddk\nf-ntddk-keraiseirqltodpclevel.md) | The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [KeRaiseIrqlToDpcLevel function](..\ntddk\nf-ntddk-keraiseirqltodpclevel~r1.md) | The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [KeRaiseIrqlToDpcLevel function](..\ntddk\nf-ntddk-keraiseirqltodpclevel~r2.md) | The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [KeRaiseIrqlToDpcLevel function](..\ntddk\nf-ntddk-keraiseirqltodpclevel~r3.md) | The KeRaiseIrqlToDpcLevel routine raises the hardware priority to IRQL = DISPATCH_LEVEL, thereby masking off interrupts of equivalent or lower IRQL on the current processor. |
| [KeReadStateEvent function](..\wdm\nf-wdm-kereadstateevent.md) | The KeReadStateEvent routine returns the current state, signaled or not-signaled, of an event object. |
| [KeReadStateMutex function](..\wdm\nf-wdm-kereadstatemutex.md) | The KeReadStateMutex routine returns the current state, signaled or not-signaled, of the specified mutex object. |
| [KeReadStateSemaphore function](..\wdm\nf-wdm-kereadstatesemaphore.md) | The KeReadStateSemaphore routine returns the current state, signaled or not-signaled, of the specified semaphore object. |
| [KeReadStateTimer function](..\wdm\nf-wdm-kereadstatetimer.md) | The KeReadStateTimer routine reads the current state of a timer object. |
| [KeRegisterBoundCallback function](..\wdm\nf-wdm-keregisterboundcallback.md) | The KeRegisterBoundCallback routine registers a routine to be called whenever a user-mode bound exception occurs. |
| [KeRegisterBugCheckCallback function](..\wdm\nf-wdm-keregisterbugcheckcallback.md) | The KeRegisterBugCheckCallback routine registers a BugCheckCallback routine, which executes when the operating system issues a bug check. |
| [KeRegisterBugCheckReasonCallback function](..\wdm\nf-wdm-keregisterbugcheckreasoncallback.md) | The KeRegisterBugCheckReasonCallback routine registers a BugCheckDumpIoCallback, BugCheckSecondaryDumpDataCallback, or BugCheckAddPagesCallback routine, which executes when the operating system issues a bug check. |
| [KeRegisterNmiCallback function](..\wdm\nf-wdm-keregisternmicallback.md) | The KeRegisterNmiCallback routine registers a routine to be called whenever a nonmaskable interrupt (NMI) occurs. |
| [KeRegisterProcessorChangeCallback function](..\wdm\nf-wdm-keregisterprocessorchangecallback.md) | The KeRegisterProcessorChangeCallback routine registers a callback function with the operating system so that the operating system will notify the driver when a new processor is added to the hardware partition. |
| [KeReleaseMutex function](..\wdm\nf-wdm-kereleasemutex.md) | The KeReleaseMutex routine releases a mutex object, and specifies whether the caller is to call one of the KeWaitXxx routines as soon as KeReleaseMutex returns control. |
| [KeReleaseSemaphore function](..\wdm\nf-wdm-kereleasesemaphore.md) | The KeReleaseSemaphore routine releases the specified semaphore object. |
| [KeReleaseSpinLock function](..\wdm\nf-wdm-kereleasespinlock.md) | The KeReleaseSpinLock routine releases a spin lock and restores the original IRQL at which the caller was running. |
| [KeReleaseSpinLockFromDpcLevel function](..\wdm\nf-wdm-kereleasespinlockfromdpclevel.md) | The KeReleaseSpinLockFromDpcLevel routine releases an executive spin lock without changing the IRQL. |
| [KeRemoveByKeyDeviceQueue function](..\wdm\nf-wdm-keremovebykeydevicequeue.md) | The KeRemoveByKeyDeviceQueue routine removes an entry, selected according to a sort key value, from the specified device queue. |
| [KeRemoveDeviceQueue function](..\wdm\nf-wdm-keremovedevicequeue.md) | The KeRemoveDeviceQueue routine removes an entry from the head of a specified device queue. |
| [KeRemoveEntryDeviceQueue function](..\wdm\nf-wdm-keremoveentrydevicequeue.md) | The KeRemoveEntryDeviceQueue routine returns whether the specified entry is in the device queue and removes it, if it was queued, from the device queue. |
| [KeRemoveQueueDpc function](..\wdm\nf-wdm-keremovequeuedpc.md) | The KeRemoveQueueDpc routine removes the specified DPC object from the system DPC queue. |
| [KeResetEvent function](..\wdm\nf-wdm-keresetevent.md) | The KeResetEvent routine resets a specified event object to a not-signaled state and returns the previous state of that event object. |
| [KeRestoreExtendedProcessorState function](..\wdm\nf-wdm-kerestoreextendedprocessorstate.md) | The KeRestoreExtendedProcessorState routine restores extended processor state information that was previously saved. |
| [KeRestoreFloatingPointState function](..\wdm\nf-wdm-kerestorefloatingpointstate.md) | The KeRestoreFloatingPointState routine restores the nonvolatile floating-point context saved by the preceding call to KeSaveFloatingPointState. |
| [KeRestoreFloatingPointState function](..\wdm\nf-wdm-kerestorefloatingpointstate~r1.md) | The KeRestoreFloatingPointState routine restores the nonvolatile floating-point context saved by the preceding call to KeSaveFloatingPointState. |
| [KeRestoreFloatingPointState function](..\wdm\nf-wdm-kerestorefloatingpointstate~r2.md) | The KeRestoreFloatingPointState routine restores the nonvolatile floating-point context saved by the preceding call to KeSaveFloatingPointState. |
| [KeRestoreFloatingPointState function](..\wdm\nf-wdm-kerestorefloatingpointstate~r3.md) | The KeRestoreFloatingPointState routine restores the nonvolatile floating-point context saved by the preceding call to KeSaveFloatingPointState. |
| [KeRevertToUserAffinityThreadEx function](..\wdm\nf-wdm-kereverttouseraffinitythreadex.md) | The KeRevertToUserAffinityThreadEx routine restores the previous affinity of the current thread. |
| [KeRevertToUserGroupAffinityThread function](..\wdm\nf-wdm-kereverttousergroupaffinitythread.md) | The KeRevertToUserGroupAffinityThread routine restores the group affinity of the calling thread to its original value at the time that the thread was created. |
| [KeSaveExtendedProcessorState function](..\wdm\nf-wdm-kesaveextendedprocessorstate.md) | The KeSaveExtendedProcessorState routine saves extended processor state information. |
| [KeSaveFloatingPointState function](..\wdm\nf-wdm-kesavefloatingpointstate.md) | The KeSaveFloatingPointState routine saves the nonvolatile floating-point context so the caller can carry out floating-point operations. |
| [KeSaveFloatingPointState function](..\wdm\nf-wdm-kesavefloatingpointstate~r1.md) | The KeSaveFloatingPointState routine saves the nonvolatile floating-point context so the caller can carry out floating-point operations. |
| [KeSaveFloatingPointState function](..\wdm\nf-wdm-kesavefloatingpointstate~r2.md) | The KeSaveFloatingPointState routine saves the nonvolatile floating-point context so the caller can carry out floating-point operations. |
| [KeSaveFloatingPointState function](..\wdm\nf-wdm-kesavefloatingpointstate~r3.md) | The KeSaveFloatingPointState routine saves the nonvolatile floating-point context so the caller can carry out floating-point operations. |
| [KeSetBasePriorityThread function](..\ntddk\nf-ntddk-kesetbaseprioritythread.md) | The KeSetBasePriorityThread routine sets the run-time priority, relative to the current process, for a given thread. |
| [KeSetCoalescableTimer function](..\wdm\nf-wdm-kesetcoalescabletimer.md) | The KeSetCoalescableTimer routine sets the initial expiration time and period of a timer object and specifies how much delay can be tolerated in the expiration times. |
| [KeSetEvent function](..\wdm\nf-wdm-kesetevent.md) | The KeSetEvent routine sets an event object to a signaled state if the event was not already signaled, and returns the previous state of the event object. |
| [KeSetHardwareCounterConfiguration function](..\ntddk\nf-ntddk-kesethardwarecounterconfiguration.md) | The KeSetHardwareCounterConfiguration routine specifies a list of hardware counters to use for thread profiling. |
| [KeSetImportanceDpc function](..\ntddk\nf-ntddk-kesetimportancedpc.md) | The KeSetImportanceDpc routine specifies how soon the DPC routine is run. |
| [KeSetImportanceDpc function](..\wdm\nf-wdm-kesetimportancedpc.md) | The KeSetImportanceDpc routine specifies how soon the DPC routine is run. |
| [KeSetKernelStackSwapEnable function](..\ntifs\nf-ntifs-kesetkernelstackswapenable.md) | The KeSetKernelStackSwapEnable routine enables and disables swapping of the caller's stack to disk. |
| [KeSetPriorityThread function](..\wdm\nf-wdm-kesetprioritythread.md) | The KeSetPriorityThread routine sets the run-time priority of a driver-created thread. |
| [KeSetSystemAffinityThread function](..\wdm\nf-wdm-kesetsystemaffinitythread.md) | The KeSetSystemAffinityThread routine sets the system affinity of the current thread. |
| [KeSetSystemAffinityThreadEx function](..\wdm\nf-wdm-kesetsystemaffinitythreadex.md) | The KeSetSystemAffinityThreadEx routine sets the system affinity of the current thread. |
| [KeSetSystemGroupAffinityThread function](..\wdm\nf-wdm-kesetsystemgroupaffinitythread.md) | The KeSetSystemGroupAffinityThread routine changes the group number and affinity mask of the calling thread. |
| [KeSetTargetProcessorDpc function](..\ntddk\nf-ntddk-kesettargetprocessordpc.md) | The KeSetTargetProcessorDpc routine specifies the processor that a DPC routine will be run on. |
| [KeSetTargetProcessorDpc function](..\wdm\nf-wdm-kesettargetprocessordpc.md) | The KeSetTargetProcessorDpc routine specifies the processor that a DPC routine will be run on. |
| [KeSetTargetProcessorDpcEx function](..\wdm\nf-wdm-kesettargetprocessordpcex.md) | The KeSetTargetProcessorDpcEx routine specifies the processor that a DPC routine will run on. |
| [KeSetTimer function](..\wdm\nf-wdm-kesettimer.md) | The KeSetTimer routine sets the absolute or relative interval at which a timer object is to be set to a signaled state and, optionally, supplies a CustomTimerDpc routine to be executed when that interval expires. |
| [KeSetTimerEx function](..\wdm\nf-wdm-kesettimerex.md) | The KeSetTimerEx routine sets the absolute or relative interval at which a timer object is to be set to a signaled state, optionally supplies a CustomTimerDpc routine to be executed when that interval expires, and optionally supplies a recurring interval for the timer. |
| [KeStallExecutionProcessor function](..\ntifs\nf-ntifs-kestallexecutionprocessor.md) | The KeStallExecutionProcessor routine stalls the caller on the current processor for a specified time interval. |
| [KeStallExecutionProcessor function](..\wdm\nf-wdm-kestallexecutionprocessor.md) | The KeStallExecutionProcessor routine stalls the caller on the current processor for a specified time interval. |
| [KeSynchronizeExecution function](..\wdm\nf-wdm-kesynchronizeexecution.md) | The KeSynchronizeExecution routine synchronizes the execution of the specified routine with the interrupt service routine (ISR) that is assigned to a set of one or more interrupt objects. |
| [KeTestSpinLock function](..\wdm\nf-wdm-ketestspinlock.md) | The KeTestSpinLock routine tests for the availability of a spin lock. |
| [KeTryToAcquireGuardedMutex function](..\wdm\nf-wdm-ketrytoacquireguardedmutex.md) | The KeTryToAcquireGuardedMutex routine acquires a guarded mutex, if available. |
| [KeTryToAcquireSpinLockAtDpcLevel function](..\wdm\nf-wdm-ketrytoacquirespinlockatdpclevel.md) | The KeTryToAcquireSpinLockAtDpcLevel routine attempts to acquire a spin lock at DISPATCH_LEVEL. |
| [KeWaitForMultipleObjects function](..\wdm\nf-wdm-kewaitformultipleobjects.md) | The KeWaitForMultipleObjects routine puts the current thread into an alertable or nonalertable wait state until any or all of a number of dispatcher objects are set to a signaled state or (optionally) until the wait times out. |
| [KeWaitForSingleObject function](..\wdm\nf-wdm-kewaitforsingleobject.md) | The KeWaitForSingleObject routine puts the current thread into a wait state until the given dispatcher object is set to a signaled state or (optionally) until the wait times out. |
| [MmAdvanceMdl function](..\wdm\nf-wdm-mmadvancemdl.md) | The MmAdvanceMdl routine advances the beginning of an MDL's virtual memory range by the specified number of bytes. |
| [MmAllocateContiguousMemory function](..\ntddk\nf-ntddk-mmallocatecontiguousmemory.md) | The MmAllocateContiguousMemory routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space. |
| [MmAllocateContiguousMemorySpecifyCache function](..\ntddk\nf-ntddk-mmallocatecontiguousmemoryspecifycache.md) | The MmAllocateContiguousMemorySpecifyCache routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space. |
| [MmAllocateContiguousMemorySpecifyCacheNode function](..\ntddk\nf-ntddk-mmallocatecontiguousmemoryspecifycachenode.md) | The MmAllocateContiguousMemorySpecifyCacheNode routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space. |
| [MmAllocateContiguousNodeMemory function](..\wdm\nf-wdm-mmallocatecontiguousnodememory.md) | The MmAllocateContiguousNodeMemory routine allocates a range of contiguous, nonpaged physical memory and maps it to the system address space. |
| [MmAllocateMappingAddress function](..\wdm\nf-wdm-mmallocatemappingaddress.md) | The MmAllocateMappingAddress routine reserves a range of system virtual address space of the specified size. |
| [MmAllocateMdlForIoSpace function](..\wdm\nf-wdm-mmallocatemdlforiospace.md) | The MmAllocateMdlForIoSpace routine allocates an MDL and initializes this MDL to describe a set of physical address ranges in I/O address space. |
| [MmAllocateNodePagesForMdlEx function](..\wdm\nf-wdm-mmallocatenodepagesformdlex.md) | The MmAllocateNodePagesForMdlEx routine allocates nonpaged physical memory from an ideal node, and allocates an MDL structure to describe this memory. |
| [MmAllocateNonCachedMemory function](..\ntddk\nf-ntddk-mmallocatenoncachedmemory.md) | The MmAllocateNonCachedMemory routine allocates a virtual address range of noncached and cache-aligned memory. |
| [MmAllocatePagesForMdl function](..\wdm\nf-wdm-mmallocatepagesformdl.md) | The MmAllocatePagesForMdl routine allocates zero-filled, nonpaged, physical memory pages to an MDL. |
| [MmAllocatePagesForMdlEx function](..\wdm\nf-wdm-mmallocatepagesformdlex.md) | The MmAllocatePagesForMdlEx routine allocates nonpaged, physical memory pages to an MDL. |
| [MmBuildMdlForNonPagedPool function](..\wdm\nf-wdm-mmbuildmdlfornonpagedpool.md) | The MmBuildMdlForNonPagedPool routine receives an MDL that specifies a nonpaged virtual memory buffer, and updates it to describe the underlying physical pages. |
| [MmCopyMemory function](..\ntddk\nf-ntddk-mmcopymemory.md) | The MmCopyMemory routine copies the specified range of virtual or physical memory into the caller-supplied buffer. |
| [MmFreeContiguousMemory function](..\ntddk\nf-ntddk-mmfreecontiguousmemory.md) | The MmFreeContiguousMemory routine releases a range of physically contiguous memory that was allocated by an MmAllocateContiguousMemoryXxx routine. |
| [MmFreeContiguousMemorySpecifyCache function](..\ntddk\nf-ntddk-mmfreecontiguousmemoryspecifycache.md) | The MmFreeContiguousMemorySpecifyCache routine frees a buffer that was allocated by an MmAllocateContiguousMemorySpecifyCacheXxx routine. |
| [MmFreeMappingAddress function](..\wdm\nf-wdm-mmfreemappingaddress.md) | The MmFreeMappingAddress routine frees a range of virtual memory reserved by the MmAllocateMappingAddress routine. |
| [MmFreeNonCachedMemory function](..\ntddk\nf-ntddk-mmfreenoncachedmemory.md) | The MmFreeNonCachedMemory routine releases a range of noncached memory that was allocated by the MmAllocateNonCachedMemory routine. |
| [MmFreePagesFromMdl function](..\wdm\nf-wdm-mmfreepagesfrommdl.md) | The MmFreePagesFromMdl routine frees all the physical pages that are described by an MDL that was created by the MmAllocatePagesForMdl routine. |
| [MmGetPhysicalAddress function](..\ntddk\nf-ntddk-mmgetphysicaladdress.md) | The MmGetPhysicalAddress routine returns the physical address corresponding to a valid nonpaged virtual address. |
| [MmGetSystemAddressForMdl function](..\wdm\nf-wdm-mmgetsystemaddressformdl.md) | The MmGetSystemAddressForMdl routine is obsolete for Windows 2000 and later versions of Windows, and for Windows Me. |
| [MmGetSystemRoutineAddress function](..\wdm\nf-wdm-mmgetsystemroutineaddress.md) | The MmGetSystemRoutineAddress routine returns a pointer to a function specified by SystemRoutineName. |
| [MmGetSystemRoutineAddress function](..\wdm\nf-wdm-mmgetsystemroutineaddress~r1.md) | The MmGetSystemRoutineAddress routine returns a pointer to a function specified by SystemRoutineName. |
| [MmIsAddressValid function](..\ntddk\nf-ntddk-mmisaddressvalid.md) | The MmIsAddressValid routine checks whether a page fault will occur for a read or write operation at a given virtual address.Warning  We do not recommend using this function. |
| [MmIsDriverSuspectForVerifier function](..\wdm\nf-wdm-mmisdriversuspectforverifier.md) | The MmIsDriverSuspectForVerifier routine indicates whether the driver represented by the specified driver object is in the list of drivers that are selected to be verified by Driver Verifier. |
| [MmIsDriverVerifying function](..\wdm\nf-wdm-mmisdriververifying.md) | The MmIsDriverVerifying routine indicates whether the kernel-mode driver that is identified by the specified driver object is being verified or calls a driver that is being verified by Driver Verifier. |
| [MmIsDriverVerifyingByAddress function](..\wdm\nf-wdm-mmisdriververifyingbyaddress.md) | The MmIsDriverVerifyingByAddress routine checks whether the kernel-mode driver that is identified by the specified image address is being verified or calls a driver that is being verified by Driver Verifier. |
| [MmIsThisAnNtAsSystem function](..\ntddk\nf-ntddk-mmisthisanntassystem.md) | The MmIsThisAnNtAsSystem routine is obsolete for Windows XP and later versions of Windows. Use RtlGetVersion or RtlVerifyVersionInfo instead. |
| [MmLockPagableCodeSection function](..\wdm\nf-wdm-mmlockpagablecodesection.md) | The MmLockPagableCodeSection routine locks a section of driver code, containing a set of driver routines marked with a special compiler directive, into system space. |
| [MmLockPagableDataSection function](..\wdm\nf-wdm-mmlockpagabledatasection.md) | The MmLockPagableDataSection routine locks an entire section of driver data into system space. |
| [MmLockPagableSectionByHandle function](..\ntddk\nf-ntddk-mmlockpagablesectionbyhandle.md) | The MmLockPagableSectionByHandle routine locks a pageable code or data section into system memory by incrementing the reference count on the handle to the section. |
| [MmMapIoSpace function](..\wdm\nf-wdm-mmmapiospace.md) | The MmMapIoSpace routine maps the given physical address range to nonpaged system space. |
| [MmMapIoSpaceEx function](..\wdm\nf-wdm-mmmapiospaceex.md) | The MmMapIoSpaceEx routine maps the given physical address range to non-paged system space using the specified page protection. |
| [MmMapLockedPages function](..\wdm\nf-wdm-mmmaplockedpages.md) | The MmMapLockedPages routine is obsolete for Windows 2000 and later versions of Windows, and for Windows Me. |
| [MmMapLockedPagesSpecifyCache function](..\wdm\nf-wdm-mmmaplockedpagesspecifycache.md) | The MmMapLockedPagesSpecifyCache routine maps the physical pages that are described by an MDL to a virtual address, and enables the caller to specify the cache attribute that is used to create the mapping. |
| [MmMapLockedPagesWithReservedMapping function](..\wdm\nf-wdm-mmmaplockedpageswithreservedmapping.md) | The MmMapLockedPagesWithReservedMapping routine maps all or part of an address range that was previously reserved by the MmAllocateMappingAddress routine. |
| [MmMapMdl function](..\wdm\nf-wdm-mmmapmdl.md) | This function maps physical pages described by a memory descriptor list (MDL) into the system virtual address space. |
| [MmPageEntireDriver function](..\wdm\nf-wdm-mmpageentiredriver.md) | The MmPageEntireDriver routine causes all of a driver's code and data to be made pageable, overriding the attributes of the various sections that make up the driver's image. |
| [MmProbeAndLockPages function](..\wdm\nf-wdm-mmprobeandlockpages.md) | The MmProbeAndLockPages routine probes the specified virtual memory pages, makes them resident, and locks them in memory. |
| [MmProbeAndLockSelectedPages function](..\wdm\nf-wdm-mmprobeandlockselectedpages.md) | The MmProbeAndLockSelectedPages routine probes the selected virtual memory pages, makes them resident, and locks them in memory. |
| [MmProtectMdlSystemAddress function](..\wdm\nf-wdm-mmprotectmdlsystemaddress.md) | The MmProtectMdlSystemAddress routine sets the protection type for a memory address range. |
| [MmQuerySystemSize function](..\wdm\nf-wdm-mmquerysystemsize.md) | The MmQuerySystemSize routine returns an estimate of the amount of memory in the system. |
| [MmResetDriverPaging function](..\wdm\nf-wdm-mmresetdriverpaging.md) | The MmResetDriverPaging routine resets the pageable status of a driver's sections to that specified when the driver was compiled. |
| [MmSecureVirtualMemory function](..\ntddk\nf-ntddk-mmsecurevirtualmemory.md) | The MmSecureVirtualMemory routine secures a user-space memory address range so that it cannot be freed and its protection type cannot be made more restrictive. |
| [MmSizeOfMdl function](..\wdm\nf-wdm-mmsizeofmdl.md) | The MmSizeOfMdl routine returns the number of bytes to allocate for an MDL describing a given address range. |
| [MmUnlockPagableImageSection function](..\wdm\nf-wdm-mmunlockpagableimagesection.md) | The MmUnlockPagableImageSection routine releases a section of driver code or driver data, previously locked into system space with MmLockPagableCodeSection, MmLockPagableDataSection or MmLockPagableSectionByHandle, so the section can be paged out again. |
| [MmUnlockPages function](..\wdm\nf-wdm-mmunlockpages.md) | The MmUnlockPages routine unlocks the physical pages that are described by the specified memory descriptor list (MDL). |
| [MmUnmapIoSpace function](..\wdm\nf-wdm-mmunmapiospace.md) | The MmUnmapIoSpace routine unmaps a specified range of physical addresses previously mapped by MmMapIoSpace. |
| [MmUnmapLockedPages function](..\wdm\nf-wdm-mmunmaplockedpages.md) | The MmUnmapLockedPages routine releases a mapping that was set up by a preceding call to the MmMapLockedPages or MmMapLockedPagesSpecifyCache routine. |
| [MmUnmapReservedMapping function](..\wdm\nf-wdm-mmunmapreservedmapping.md) | The MmUnmapReservedMapping routine unmaps a memory buffer that was mapped by the MmMapLockedPagesWithReservedMapping routine. |
| [MmUnsecureVirtualMemory function](..\ntddk\nf-ntddk-mmunsecurevirtualmemory.md) | The MmUnsecureVirtualMemory routine unsecures a memory address range secured by the MmSecureVirtualMemory routine. |
| [NtAllocateVirtualMemory function](..\ntifs\nf-ntifs-ntallocatevirtualmemory.md) | The ZwAllocateVirtualMemory routine reserves, commits, or both, a region of pages within the user-mode virtual address space of a specified process. |
| [NtClose function](..\ntifs\nf-ntifs-ntclose.md) | The ZwClose routine closes an object handle. |
| [NtCommitComplete function](..\wdm\nf-wdm-ntcommitcomplete.md) | The ZwCommitComplete routine notifies KTM that the calling resource manager has finished committing a transaction's data. |
| [NtCommitEnlistment function](..\wdm\nf-wdm-ntcommitenlistment.md) | The ZwCommitEnlistment routine initiates the commit operation for a specified enlistment's transaction. |
| [NtCommitTransaction function](..\wdm\nf-wdm-ntcommittransaction.md) | The ZwCommitTransaction routine initiates a commit operation for a specified transaction. |
| [NtCreateEnlistment function](..\wdm\nf-wdm-ntcreateenlistment.md) | The ZwCreateEnlistment routine creates a new enlistment object for a transaction. |
| [NtCreateFile function](..\ntifs\nf-ntifs-ntcreatefile.md) | The ZwCreateFile routine creates a new file or opens an existing file. |
| [NtCreateResourceManager function](..\wdm\nf-wdm-ntcreateresourcemanager.md) | The ZwCreateResourceManager routine creates a resource manager object. |
| [NtCreateTransaction function](..\wdm\nf-wdm-ntcreatetransaction.md) | The ZwCreateTransaction routine creates a transaction object. |
| [NtCreateTransactionManager function](..\wdm\nf-wdm-ntcreatetransactionmanager.md) | The ZwCreateTransactionManager routine creates a new transaction manager object. |
| [NtDeviceIoControlFile function](..\ntifs\nf-ntifs-ntdeviceiocontrolfile.md) | The ZwDeviceIoControlFile routine sends a control code directly to a specified device driver, causing the corresponding driver to perform the specified operation. |
| [NtDuplicateToken function](..\ntifs\nf-ntifs-ntduplicatetoken.md) | The ZwDuplicateToken function creates a handle to a new access token that duplicates an existing token. This function can create either a primary token or an impersonation token. |
| [NtEnumerateTransactionObject function](..\wdm\nf-wdm-ntenumeratetransactionobject.md) | The ZwEnumerateTransactionObject routine enumerates the KTM objects on a computer. |
| [NtFlushBuffersFileEx function](..\ntifs\nf-ntifs-ntflushbuffersfileex.md) | The ZwFlushBuffersFileEx routine is called by a file system filter driver to send a flush request for a given file to the file system. An optional flush operation flag can be set to control how file data is written to storage. |
| [NtFreeVirtualMemory function](..\ntifs\nf-ntifs-ntfreevirtualmemory.md) | The ZwFreeVirtualMemory routine releases, decommits, or both, a region of pages within the virtual address space of a specified process. |
| [NtFsControlFile function](..\ntifs\nf-ntifs-ntfscontrolfile.md) | The ZwFsControlFile routine sends a control code directly to a specified file system or file system filter driver, causing the corresponding driver to perform the specified action. |
| [NtGetNotificationResourceManager function](..\wdm\nf-wdm-ntgetnotificationresourcemanager.md) | The ZwGetNotificationResourceManager routine retrieves the next transaction notification from a specified resource manager's notification queue. |
| [NtLockFile function](..\ntifs\nf-ntifs-ntlockfile.md) | The ZwLockFile routine requests a byte-range lock for the specified file. |
| [NtOpenEnlistment function](..\wdm\nf-wdm-ntopenenlistment.md) | The ZwOpenEnlistment routine obtains a handle to an existing enlistment object. |
| [NtOpenFile function](..\ntifs\nf-ntifs-ntopenfile.md) | The ZwOpenFile routine opens an existing file, directory, device, or volume. |
| [NtOpenProcess function](..\ntddk\nf-ntddk-ntopenprocess.md) | The ZwOpenProcess routine opens a handle to a process object and sets the access rights to this object. |
| [NtOpenProcessTokenEx function](..\ntifs\nf-ntifs-ntopenprocesstokenex.md) | The ZwOpenProcessTokenEx routine opens the access token associated with a process. |
| [NtOpenResourceManager function](..\wdm\nf-wdm-ntopenresourcemanager.md) | The ZwOpenResourceManager routine returns a handle to an existing resource manager object. |
| [NtOpenThreadTokenEx function](..\ntifs\nf-ntifs-ntopenthreadtokenex.md) | The ZwOpenThreadTokenEx routine opens the access token associated with a thread. |
| [NtOpenTransaction function](..\wdm\nf-wdm-ntopentransaction.md) | The ZwOpenTransaction routine obtains a handle to an existing transaction object. |
| [NtOpenTransactionManager function](..\wdm\nf-wdm-ntopentransactionmanager.md) | The ZwOpenTransactionManager routine obtains a handle to an existing transaction manager object. |
| [NtPrePrepareComplete function](..\wdm\nf-wdm-ntprepreparecomplete.md) | The ZwPrePrepareComplete routine notifies KTM that the calling resource manager has finished preliminary preparation of a transaction's data. |
| [NtPrePrepareEnlistment function](..\wdm\nf-wdm-ntpreprepareenlistment.md) | The ZwPrePrepareEnlistment routine initiates the pre-prepare operation for a specified enlistment's transaction. |
| [NtPrepareComplete function](..\wdm\nf-wdm-ntpreparecomplete.md) | The ZwPrepareComplete routine notifies KTM that the calling resource manager has finished preparing a transaction's data. |
| [NtPrepareEnlistment function](..\wdm\nf-wdm-ntprepareenlistment.md) | The ZwPrepareEnlistment routine initiates the prepare operation for a specified enlistment's transaction. |
| [NtQueryDirectoryFile function](..\ntifs\nf-ntifs-ntquerydirectoryfile.md) | The ZwQueryDirectoryFile routine returns various kinds of information about files in the directory specified by a given file handle. |
| [NtQueryDirectoryFileEx function](..\ntifs\nf-ntifs-ntquerydirectoryfileex.md) | The ZwQueryDirectoryFileEx routine returns information about files in the directory specified by the FileHandle parameter. |
| [NtQueryInformationEnlistment function](..\wdm\nf-wdm-ntqueryinformationenlistment.md) | The ZwQueryInformationEnlistment routine retrieves information about a specified enlistment object. |
| [NtQueryInformationFile function](..\ntifs\nf-ntifs-ntqueryinformationfile.md) | The ZwQueryInformationFile routine returns various kinds of information about a file object. |
| [NtQueryInformationResourceManager function](..\wdm\nf-wdm-ntqueryinformationresourcemanager.md) | The ZwQueryInformationResourceManager routine retrieves information about a specified resource manager object. |
| [NtQueryInformationToken function](..\ntifs\nf-ntifs-ntqueryinformationtoken.md) | The ZwQueryInformationToken routine retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information. |
| [NtQueryInformationTransaction function](..\wdm\nf-wdm-ntqueryinformationtransaction.md) | The ZwQueryInformationTransaction routine retrieves information about a specified transaction. |
| [NtQueryInformationTransactionManager function](..\wdm\nf-wdm-ntqueryinformationtransactionmanager.md) | The ZwQueryInformationTransactionManager routine retrieves information about a specified transaction manager object. |
| [NtQueryObject function](..\ntifs\nf-ntifs-ntqueryobject.md) | The ZwQueryObject routine provides information about a supplied object. |
| [NtQueryQuotaInformationFile function](..\ntifs\nf-ntifs-ntqueryquotainformationfile.md) | The ZwQueryQuotaInformationFile routine retrieves quota entries associated with the volume specified by the FileHandle parameter. |
| [NtQuerySecurityObject function](..\ntifs\nf-ntifs-ntquerysecurityobject.md) | The ZwQuerySecurityObject routine retrieves a copy of an object's security descriptor. |
| [NtQueryVirtualMemory function](..\ntifs\nf-ntifs-ntqueryvirtualmemory.md) | The ZwQueryVirtualMemory routine determines the state, protection, and type of a region of pages within the virtual address space of the subject process. |
| [NtQueryVolumeInformationFile function](..\ntifs\nf-ntifs-ntqueryvolumeinformationfile.md) | The ZwQueryVolumeInformationFile routine retrieves information about the volume associated with a given file, directory, storage device, or volume. |
| [NtReadFile function](..\ntifs\nf-ntifs-ntreadfile.md) | The ZwReadFile routine reads data from an open file. |
| [NtReadOnlyEnlistment function](..\wdm\nf-wdm-ntreadonlyenlistment.md) | The ZwReadOnlyEnlistment routine sets a specified enlistment to be read-only. |
| [NtRecoverEnlistment function](..\wdm\nf-wdm-ntrecoverenlistment.md) | The ZwRecoverEnlistment routine initiates a recovery operation for the transaction that is associated with a specified enlistment. |
| [NtRecoverResourceManager function](..\wdm\nf-wdm-ntrecoverresourcemanager.md) | The ZwRecoverResourceManager routine tries to recover the transaction that is associated with each enlistment of a specified resource manager object. |
| [NtRecoverTransactionManager function](..\wdm\nf-wdm-ntrecovertransactionmanager.md) | The ZwRecoverTransactionManager routine reconstructs the state of the transaction manager object (including all transactions, enlistments, and resource managers) from the recovery information that is in the log stream. |
| [NtRollbackComplete function](..\wdm\nf-wdm-ntrollbackcomplete.md) | The ZwRollbackComplete routine notifies KTM that the calling resource manager has finished rolling back a transaction's data. |
| [NtRollbackEnlistment function](..\wdm\nf-wdm-ntrollbackenlistment.md) | The ZwRollbackEnlistment routine rolls back the transaction that is associated with a specified enlistment. |
| [NtRollbackTransaction function](..\wdm\nf-wdm-ntrollbacktransaction.md) | The ZwRollbackTransaction routine initiates a rollback operation for a specified transaction. |
| [NtRollforwardTransactionManager function](..\wdm\nf-wdm-ntrollforwardtransactionmanager.md) | The ZwRollforwardTransactionManager routine initiates recovery operations for all of the in-progress transactions that are assigned to a specified transaction manager. |
| [NtSetInformationEnlistment function](..\wdm\nf-wdm-ntsetinformationenlistment.md) | The ZwSetInformationEnlistment routine sets information for a specified enlistment object. |
| [NtSetInformationFile function](..\ntifs\nf-ntifs-ntsetinformationfile.md) | The ZwSetInformationFile routine changes various kinds of information about a file object. |
| [NtSetInformationResourceManager function](..\wdm\nf-wdm-ntsetinformationresourcemanager.md) | The ZwSetInformationResourceManager routine is not used. |
| [NtSetInformationToken function](..\ntifs\nf-ntifs-ntsetinformationtoken.md) | The ZwSetInformationToken routine modifies information in a specified token. The calling process must have appropriate access rights to set the information. |
| [NtSetInformationTransaction function](..\wdm\nf-wdm-ntsetinformationtransaction.md) | The ZwSetInformationTransaction routine sets information for a specified transaction. |
| [NtSetInformationTransactionManager function](..\wdm\nf-wdm-ntsetinformationtransactionmanager.md) | Do not call this routine from kernel-mode code. |
| [NtSetQuotaInformationFile function](..\ntifs\nf-ntifs-ntsetquotainformationfile.md) | The ZwSetQuotaInformationFile routine changes quota entries for the volume associated with the FileHandle parameter. All of the quota entries in the specified buffer are applied to the volume. |
| [NtSetSecurityObject function](..\ntifs\nf-ntifs-ntsetsecurityobject.md) | The ZwSetSecurityObject routine sets an object's security state. |
| [NtSinglePhaseReject function](..\wdm\nf-wdm-ntsinglephasereject.md) | The ZwSinglePhaseReject routine informs KTM that the calling resource manager will not support single-phase commit operations for a specified enlistment. |
| [NtUnlockFile function](..\ntifs\nf-ntifs-ntunlockfile.md) | The ZwUnlockFile routine unlocks a byte-range lock in a file. |
| [NtWriteFile function](..\ntifs\nf-ntifs-ntwritefile.md) | The ZwWriteFile routine writes data to an open file. |
| [ObCloseHandle function](..\wdm\nf-wdm-obclosehandle.md) | The ObCloseHandle routine closes an object handle. |
| [ObDereferenceObject function](..\wdm\nf-wdm-obdereferenceobject.md) | The ObDereferenceObject routine decrements the given object's reference count and performs retention checks. |
| [ObDereferenceObjectDeferDelete function](..\wdm\nf-wdm-obdereferenceobjectdeferdelete.md) | The ObDereferenceObjectDeferDelete routine decrements the reference count for the given object, checks for object retention, and avoids deadlocks. |
| [ObDereferenceObjectDeferDeleteWithTag function](..\wdm\nf-wdm-obdereferenceobjectdeferdeletewithtag.md) | The ObDereferenceObjectDeferDeleteWithTag routine decrements the reference count for the specified object, defers deletion of the object to avoid deadlocks, and writes a four-byte tag value to the object to support object reference tracing. |
| [ObDereferenceObjectWithTag function](..\wdm\nf-wdm-obdereferenceobjectwithtag.md) | The ObDereferenceObjectWithTag routine decrements the reference count of the specified object, and writes a four-byte tag value to the object to support object reference tracing. |
| [ObGetObjectSecurity function](..\wdm\nf-wdm-obgetobjectsecurity.md) | The ObGetObjectSecurity routine gets the security descriptor for a given object. |
| [ObReferenceObject function](..\wdm\nf-wdm-obreferenceobject.md) | The ObReferenceObject routine increments the reference count to the given object. |
| [ObReferenceObjectByHandle function](..\wdm\nf-wdm-obreferenceobjectbyhandle.md) | The ObReferenceObjectByHandle routine provides access validation on the object handle, and, if access can be granted, returns the corresponding pointer to the object's body. |
| [ObReferenceObjectByHandleWithTag function](..\wdm\nf-wdm-obreferenceobjectbyhandlewithtag.md) | The ObReferenceObjectByHandleWithTag routine increments the reference count of the object that is identified by the specified handle, and writes a four-byte tag value to the object to support object reference tracing. |
| [ObReferenceObjectByPointer function](..\wdm\nf-wdm-obreferenceobjectbypointer.md) | The ObReferenceObjectByPointer routine increments the pointer reference count for a given object. |
| [ObReferenceObjectByPointerWithTag function](..\wdm\nf-wdm-obreferenceobjectbypointerwithtag.md) | The ObReferenceObjectByPointerWithTag routine increments the reference count of the specified object, and writes a four-byte tag value to the object to support object reference tracing. |
| [ObReferenceObjectWithTag function](..\wdm\nf-wdm-obreferenceobjectwithtag.md) | The ObReferenceObjectWithTag routine increments the reference count of the specified object, and writes a four-byte tag value to the object to support object reference tracing. |
| [ObRegisterCallbacks function](..\wdm\nf-wdm-obregistercallbacks.md) | The ObRegisterCallbacks routine registers a list of callback routines for thread, process, and desktop handle operations. |
| [ObReleaseObjectSecurity function](..\wdm\nf-wdm-obreleaseobjectsecurity.md) | The ObReleaseObjectSecurity routine is the reciprocal to ObGetObjectSecurity. |
| [ObUnRegisterCallbacks function](..\wdm\nf-wdm-obunregistercallbacks.md) | The ObUnRegisterCallbacks routine unregisters a set of callback routines that were registered with the ObRegisterCallbacks routine. |
| [ObfReferenceObject function](..\wdm\nf-wdm-obfreferenceobject.md) | The ObReferenceObject routine increments the reference count to the given object. |
| [PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-extended-io-resource.md) | The PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_EXTENDED_ADDRESS structure. |
| [PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-extended-memory-resource.md) | The PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_EXTENDED_ADDRESS structure. |
| [PEP_ACPI_INITIALIZE_GPIO_INT_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-gpio-int-resource.md) | The PEP_ACPI_INITIALIZE_GPIO_INT_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_GPIO_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_GPIO_IO_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-gpio-io-resource.md) | The PEP_ACPI_INITIALIZE_GPIO_IO_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_GPIO_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_INTERRUPT_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-interrupt-resource.md) | The PEP_ACPI_INITIALIZE_INTERRUPT_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_INTERRUPT_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_IOPORT_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-ioport-resource.md) | The PEP_ACPI_INITIALIZE_IOPORT_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_IO_MEMORY_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_MEMORY_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-memory-resource.md) | The PEP_ACPI_INITIALIZE_MEMORY_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_IO_MEMORY_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_SPB_I2C_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-spb-i2c-resource.md) | The PEP_ACPI_INITIALIZE_SPB_I2C_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_SPB_I2C_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_SPB_SPI_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-spb-spi-resource.md) | The PEP_ACPI_INITIALIZE_SPB_SPI_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_SPB_SPI_RESOURCE structure. |
| [PEP_ACPI_INITIALIZE_SPB_UART_RESOURCE function](..\pepfx\nf-pepfx-pep-acpi-initialize-spb-uart-resource.md) | The PEP_ACPI_INITIALIZE_SPB_UART_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_SPB_UART_RESOURCE structure. |
| [PoCallDriver function](..\ntifs\nf-ntifs-pocalldriver.md) | The PoCallDriver routine passes a power IRP to the next-lower driver in the device stack. (Windows Server 2003, Windows XP, and Windows 2000 only.). |
| [PoCallDriver function](..\wdm\nf-wdm-pocalldriver.md) | The PoCallDriver routine passes a power IRP to the next-lower driver in the device stack. (Windows Server 2003, Windows XP, and Windows 2000 only.). |
| [PoClearPowerRequest function](..\ntifs\nf-ntifs-poclearpowerrequest.md) | The PoClearPowerRequest routine decrements the count for the specified power request type. |
| [PoClearPowerRequest function](..\wdm\nf-wdm-poclearpowerrequest.md) | The PoClearPowerRequest routine decrements the count for the specified power request type. |
| [PoCreatePowerRequest function](..\ntifs\nf-ntifs-pocreatepowerrequest.md) | The PoCreatePowerRequest routine creates a power request object. |
| [PoCreatePowerRequest function](..\wdm\nf-wdm-pocreatepowerrequest.md) | The PoCreatePowerRequest routine creates a power request object. |
| [PoDeletePowerRequest function](..\ntifs\nf-ntifs-podeletepowerrequest.md) | The PoDeletePowerRequest routine deletes a power request object. |
| [PoDeletePowerRequest function](..\wdm\nf-wdm-podeletepowerrequest.md) | The PoDeletePowerRequest routine deletes a power request object. |
| [PoEndDeviceBusy function](..\ntifs\nf-ntifs-poenddevicebusy.md) | The PoEndDeviceBusy routine marks the end of a period of time in which the device is busy. |
| [PoEndDeviceBusy function](..\wdm\nf-wdm-poenddevicebusy.md) | The PoEndDeviceBusy routine marks the end of a period of time in which the device is busy. |
| [PoFxActivateComponent function](..\wdm\nf-wdm-pofxactivatecomponent.md) | The PoFxActivateComponent routine increments the activation reference count on the specified component. |
| [PoFxCompleteDevicePowerNotRequired function](..\wdm\nf-wdm-pofxcompletedevicepowernotrequired.md) | The PoFxCompleteDevicePowerNotRequired routine notifies the power management framework (PoFx) that the calling driver has completed its response to a call to the driver's DevicePowerNotRequiredCallback callback routine. |
| [PoFxCompleteIdleCondition function](..\wdm\nf-wdm-pofxcompleteidlecondition.md) | The PoFxCompleteIdleCondition routine informs the power management framework (PoFx) that the specified component has completed a pending change to the idle condition. |
| [PoFxCompleteIdleState function](..\wdm\nf-wdm-pofxcompleteidlestate.md) | The PoFxCompleteIdleState routine informs the power management framework (PoFx) that the specified component has completed a pending change to an Fx state. |
| [PoFxIdleComponent function](..\wdm\nf-wdm-pofxidlecomponent.md) | The PoFxIdleComponent routine decrements the activation reference count on the specified component. |
| [PoFxIssueComponentPerfStateChange function](..\wdm\nf-wdm-pofxissuecomponentperfstatechange.md) | The PoFxIssueComponentPerfStateChange routine submits a request to place a device component in a particular performance state. |
| [PoFxIssueComponentPerfStateChangeMultiple function](..\wdm\nf-wdm-pofxissuecomponentperfstatechangemultiple.md) | The PoFxIssueComponentPerfStateChangeMultiple routine submits a request to change the performance states in multiple performance state sets simultaneously for a device component. |
| [PoFxNotifySurprisePowerOn function](..\wdm\nf-wdm-pofxnotifysurprisepoweron.md) | The PoFxNotifySurprisePowerOn routine notifies the power management framework (PoFx) that a device was turned on as a side effect of supplying power to some other device. |
| [PoFxPowerControl function](..\wdm\nf-wdm-pofxpowercontrol.md) | The PoFxPowerControl routine sends a power control request to the power management framework (PoFx). |
| [PoFxPowerOnCrashdumpDevice function](..\wdm\nf-wdm-pofxpoweroncrashdumpdevice.md) | The PoFxPowerOnCrashdumpDevice routine requests that a crash-dump device be turned on. |
| [PoFxQueryCurrentComponentPerfState function](..\wdm\nf-wdm-pofxquerycurrentcomponentperfstate.md) | The PoFxQueryCurrentComponentPerfState routine retrieves the active performance state in a component's performance state set. |
| [PoFxRegisterComponentPerfStates function](..\wdm\nf-wdm-pofxregistercomponentperfstates.md) | The PoFxRegisterComponentPerfStates routine registers a device component for performance state management by the power management framework (PoFx). |
| [PoFxRegisterCoreDevice function](..\pepfx\nf-pepfx-pofxregistercoredevice.md) | The PoFxRegisterCoreDevice routine registers a new core system resource with the Windows power management framework (PoFx). |
| [PoFxRegisterCrashdumpDevice function](..\wdm\nf-wdm-pofxregistercrashdumpdevice.md) | The PoFxRegisterCrashdumpDevice routine registers a crash-dump device. |
| [PoFxRegisterDevice function](..\wdm\nf-wdm-pofxregisterdevice.md) | The PoFxRegisterDevice routine registers a device with the power management framework (PoFx). |
| [PoFxRegisterPlugin function](..\pepfx\nf-pepfx-pofxregisterplugin.md) | The PoFxRegisterPlugin routine registers a platform extension plug-in (PEP) with the Windows power management framework (PoFx). |
| [PoFxRegisterPluginEx function](..\pepfx\nf-pepfx-pofxregisterpluginex.md) | The PoFxRegisterPluginEx routine registers a platform extension plug-in (PEP) with the Windows power management framework (PoFx). |
| [PoFxReportDevicePoweredOn function](..\wdm\nf-wdm-pofxreportdevicepoweredon.md) | The PoFxReportDevicePoweredOn routine notifies the power management framework (PoFx) that the device completed the requested transition to the D0 (fully on) power state. |
| [PoFxSetComponentLatency function](..\wdm\nf-wdm-pofxsetcomponentlatency.md) | The PoFxSetComponentLatency routine specifies the maximum latency that can be tolerated in the transition from the idle condition to the active condition in the specified component. |
| [PoFxSetComponentResidency function](..\wdm\nf-wdm-pofxsetcomponentresidency.md) | The PoFxSetComponentResidency routine sets the estimated time for how long a component is likely to remain idle after the component enters the idle condition. |
| [PoFxSetComponentWake function](..\wdm\nf-wdm-pofxsetcomponentwake.md) | The PoFxSetComponentWake routine indicates whether the driver arms the specified component to wake whenever the component enters the idle condition. |
| [PoFxSetDeviceIdleTimeout function](..\wdm\nf-wdm-pofxsetdeviceidletimeout.md) | The PoFxSetDeviceIdleTimeout routine specifies the minimum time interval from when the last component of the device enters the idle condition to when the power management framework (PoFx) calls the driver's DevicePowerNotRequiredCallback routine. |
| [PoFxSetTargetDripsDevicePowerState function](..\wdm\nf-wdm-pofxsettargetdripsdevicepowerstate.md) | This routine is called to notify the power manager of the device's target device power state for DRIPS. The driver can override the DRIPS constraint provided by the PEP. |
| [PoFxStartDevicePowerManagement function](..\wdm\nf-wdm-pofxstartdevicepowermanagement.md) | The PoFxStartDevicePowerManagement routine completes the registration of a device with the power management framework (PoFx) and starts device power management. |
| [PoFxUnregisterDevice function](..\wdm\nf-wdm-pofxunregisterdevice.md) | The PoFxUnregisterDevice routine removes the registration of a device from the power management framework (PoFx). |
| [PoGetSystemWake function](..\wdm\nf-wdm-pogetsystemwake.md) | The PoGetSystemWake routine determines whether a specified IRP has been marked as waking the system from a sleeping state. |
| [PoQueryWatchdogTime function](..\ntifs\nf-ntifs-poquerywatchdogtime.md) | The PoQueryWatchdogTime routine indicates whether the power manager has enabled a watchdog time-out counter for any power IRP that is currently assigned to the device stack. |
| [PoQueryWatchdogTime function](..\wdm\nf-wdm-poquerywatchdogtime.md) | The PoQueryWatchdogTime routine indicates whether the power manager has enabled a watchdog time-out counter for any power IRP that is currently assigned to the device stack. |
| [PoRegisterDeviceForIdleDetection function](..\ntifs\nf-ntifs-poregisterdeviceforidledetection.md) | The PoRegisterDeviceForIdleDetection routine enables or cancels idle detection and sets idle time-out values for a device. |
| [PoRegisterDeviceForIdleDetection function](..\wdm\nf-wdm-poregisterdeviceforidledetection.md) | The PoRegisterDeviceForIdleDetection routine enables or cancels idle detection and sets idle time-out values for a device. |
| [PoRegisterPowerSettingCallback function](..\ntifs\nf-ntifs-poregisterpowersettingcallback.md) | The PoRegisterPowerSettingCallback routine registers a power-setting callback routine to receive notifications of changes in the specified power setting. |
| [PoRegisterPowerSettingCallback function](..\wdm\nf-wdm-poregisterpowersettingcallback.md) | The PoRegisterPowerSettingCallback routine registers a power-setting callback routine to receive notifications of changes in the specified power setting. |
| [PoRegisterSystemState function](..\ntifs\nf-ntifs-poregistersystemstate.md) | The PoRegisterSystemState routine registers the system as busy due to certain activity. |
| [PoRegisterSystemState function](..\wdm\nf-wdm-poregistersystemstate.md) | The PoRegisterSystemState routine registers the system as busy due to certain activity. |
| [PoRequestPowerIrp function](..\wdm\nf-wdm-porequestpowerirp.md) | The PoRequestPowerIrp routine allocates a power IRP and sends it to the top driver in the device stack for the specified device. |
| [PoSetDeviceBusyEx function](..\ntifs\nf-ntifs-posetdevicebusyex.md) | The PoSetDeviceBusyEx routine notifies the power manager that the device associated with the specified idle counter is busy. |
| [PoSetDeviceBusyEx function](..\wdm\nf-wdm-posetdevicebusyex.md) | The PoSetDeviceBusyEx routine notifies the power manager that the device associated with the specified idle counter is busy. |
| [PoSetPowerRequest function](..\ntifs\nf-ntifs-posetpowerrequest.md) | The PoSetPowerRequest routine increments the count for the specified power request type. |
| [PoSetPowerRequest function](..\wdm\nf-wdm-posetpowerrequest.md) | The PoSetPowerRequest routine increments the count for the specified power request type. |
| [PoSetPowerState function](..\ntifs\nf-ntifs-posetpowerstate.md) | The PoSetPowerState routine notifies the system of a change in the device power state for a device. |
| [PoSetPowerState function](..\wdm\nf-wdm-posetpowerstate.md) | The PoSetPowerState routine notifies the system of a change in the device power state for a device. |
| [PoSetSystemState function](..\wdm\nf-wdm-posetsystemstate.md) | Drivers call the PoSetSystemState routine to indicate that the system is active. |
| [PoSetSystemWake function](..\wdm\nf-wdm-posetsystemwake.md) | The PoSetSystemWake routine marks the specified IRP as one that contributed to waking the system from a sleep state. |
| [PoStartDeviceBusy function](..\ntifs\nf-ntifs-postartdevicebusy.md) | The PoStartDeviceBusy routine marks the start of a period of time in which the device is busy. |
| [PoStartDeviceBusy function](..\wdm\nf-wdm-postartdevicebusy.md) | The PoStartDeviceBusy routine marks the start of a period of time in which the device is busy. |
| [PoStartNextPowerIrp function](..\ntifs\nf-ntifs-postartnextpowerirp.md) | The PoStartNextPowerIrp routine signals the power manager that the driver is ready to handle the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only.). |
| [PoStartNextPowerIrp function](..\wdm\nf-wdm-postartnextpowerirp.md) | The PoStartNextPowerIrp routine signals the power manager that the driver is ready to handle the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only.). |
| [PoUnregisterPowerSettingCallback function](..\ntifs\nf-ntifs-pounregisterpowersettingcallback.md) | The PoUnregisterPowerSettingCallback routine unregisters a power-setting callback routine that a driver previously registered by calling the PoRegisterPowerSettingCallback routine. |
| [PoUnregisterPowerSettingCallback function](..\wdm\nf-wdm-pounregisterpowersettingcallback.md) | The PoUnregisterPowerSettingCallback routine unregisters a power-setting callback routine that a driver previously registered by calling the PoRegisterPowerSettingCallback routine. |
| [PoUnregisterSystemState function](..\ntifs\nf-ntifs-pounregistersystemstate.md) | The PoUnregisterSystemState routine cancels a system state registration created by PoRegisterSystemState. |
| [PoUnregisterSystemState function](..\wdm\nf-wdm-pounregistersystemstate.md) | The PoUnregisterSystemState routine cancels a system state registration created by PoRegisterSystemState. |
| [PopEntryList function](..\wdm\nf-wdm-popentrylist.md) | The PopEntryList routine removes the first entry from a singly linked list of SINGLE_LIST_ENTRY structures. |
| [ProbeForRead function](..\wdm\nf-wdm-probeforread.md) | The ProbeForRead routine checks that a user-mode buffer actually resides in the user portion of the address space, and is correctly aligned. |
| [ProbeForRead function](..\wdm\nf-wdm-probeforread~r1.md) | The ProbeForRead routine checks that a user-mode buffer actually resides in the user portion of the address space, and is correctly aligned. |
| [ProbeForWrite function](..\wdm\nf-wdm-probeforwrite.md) | The ProbeForWrite routine checks that a user-mode buffer actually resides in the user-mode portion of the address space, is writable, and is correctly aligned. |
| [PsAllocSiloContextSlot function](..\ntddk\nf-ntddk-psallocsilocontextslot.md) | This routine allocates a slot that can be used to insert, retrieve, and delete an object in all silos. . |
| [PsAttachSiloToCurrentThread function](..\ntddk\nf-ntddk-psattachsilotocurrentthread.md) | This routine places a thread temporarily into the specified Silo. |
| [PsCreateSiloContext function](..\ntddk\nf-ntddk-pscreatesilocontext.md) | This routine creates an object that will be inserted in a Silo. |
| [PsCreateSystemThread function](..\wdm\nf-wdm-pscreatesystemthread.md) | The PsCreateSystemThread routine creates a system thread that executes in kernel mode and returns a handle for the thread. |
| [PsDereferenceSiloContext function](..\ntddk\nf-ntddk-psdereferencesilocontext.md) | This routine decrements the reference count on the object. |
| [PsDetachSiloFromCurrentThread function](..\ntddk\nf-ntddk-psdetachsilofromcurrentthread.md) | This routine removes a thread from a silo which was added by an attach. For more info about attaching, see the PsAttachSiloToCurrentThread routine. |
| [PsFreeSiloContextSlot function](..\ntddk\nf-ntddk-psfreesilocontextslot.md) | This routine frees the specified slot and makes it available in the system. It undoes the effects of the PsAllocSiloContextSlot routine. |
| [PsGetCurrentProcessId function](..\ntddk\nf-ntddk-psgetcurrentprocessid.md) | The PsGetCurrentProcessId routine identifies the current thread's process. |
| [PsGetCurrentServerSilo function](..\ntddk\nf-ntddk-psgetcurrentserversilo.md) | This routine returns the effective server silo for the thread. |
| [PsGetCurrentSilo function](..\ntddk\nf-ntddk-psgetcurrentsilo.md) | This routine returns the current silo for the calling thread. First the thread is checked to see if it has been attached to a silo. If not, then the thread is checked to see if it is in a silo. |
| [PsGetCurrentThread function](..\ntddk\nf-ntddk-psgetcurrentthread.md) | The PsGetCurrentThread routine identifies the current thread. |
| [PsGetCurrentThread function](..\ntifs\nf-ntifs-psgetcurrentthread.md) | The PsGetCurrentThread routine identifies the current thread. |
| [PsGetCurrentThread function](..\wdm\nf-wdm-psgetcurrentthread.md) | The PsGetCurrentThread routine identifies the current thread. |
| [PsGetCurrentThreadId function](..\ntddk\nf-ntddk-psgetcurrentthreadid.md) | The PsGetCurrentThreadId routine identifies the current thread. |
| [PsGetCurrentThreadTeb function](..\ntddk\nf-ntddk-psgetcurrentthreadteb.md) | The PsGetCurrentThreadTeb routine returns the Thread Environment Block (TEB) of the current thread. The call must be made in kernel-mode. |
| [PsGetEffectiveServerSilo function](..\ntddk\nf-ntddk-psgeteffectiveserversilo.md) | This routine traverses the parent chain of the Silo until finding the effective server silo or host silo. |
| [PsGetHostSilo function](..\ntddk\nf-ntddk-psgethostsilo.md) | This routine returns the host silo. |
| [PsGetJobServerSilo function](..\ntddk\nf-ntddk-psgetjobserversilo.md) | This routine returns the effective ServerSilo for the job. The returned pointer is valid as long as the supplied Job object remains referenced. |
| [PsGetJobSilo function](..\ntddk\nf-ntddk-psgetjobsilo.md) | This routine returns the first job in the hierarchy that is a Silo. The returned pointer is valid as long as the supplied Job object remains referenced. |
| [PsGetParentSilo function](..\ntddk\nf-ntddk-psgetparentsilo.md) | Retrieves the most immediate parent silo in the hierarchy for a given job object. |
| [PsGetPermanentSiloContext function](..\ntddk\nf-ntddk-psgetpermanentsilocontext.md) | This routine retrieves an object that was inserted in the Silo without incrementing the reference count. |
| [PsGetProcessCreateTimeQuadPart function](..\ntddk\nf-ntddk-psgetprocesscreatetimequadpart.md) | The PsGetProcessCreateTimeQuadPart routine returns a LONGLONG value that represents the time at which the process was created. |
| [PsGetProcessId function](..\ntddk\nf-ntddk-psgetprocessid.md) | The PsGetProcessId routine returns the process identifier (process ID) that is associated with a specified process. |
| [PsGetServerSiloActiveConsoleId function](..\ntddk\nf-ntddk-psgetserversiloactiveconsoleid.md) | Gets the active console for the current server silo context for the supplied thread. |
| [PsGetSiloContext function](..\ntddk\nf-ntddk-psgetsilocontext.md) | This routine retrieves the silo context from the specified silo and slot. |
| [PsGetSiloMonitorContextSlot function](..\ntddk\nf-ntddk-psgetsilomonitorcontextslot.md) | This routine returns the silo context slot that was allocated by the monitor during the registration. |
| [PsGetVersion function](..\wdm\nf-wdm-psgetversion.md) | This function is obsolete in Windows XP and later versions of the Windows operating system. Use RtlGetVersion instead.PsGetVersion returns caller-selected information about the current version of the NT-based operating system. |
| [PsInsertPermanentSiloContext function](..\ntddk\nf-ntddk-psinsertpermanentsilocontext.md) | This routine inserts an object in an empty slot in a Silo. |
| [PsInsertSiloContext function](..\ntddk\nf-ntddk-psinsertsilocontext.md) | This routine inserts an object in an empty slot in a Silo. |
| [PsIsHostSilo function](..\ntddk\nf-ntddk-psishostsilo.md) | This routine will check if the supplied Silo is the host silo. |
| [PsIsSystemThread function](..\ntifs\nf-ntifs-psissystemthread.md) | The PsIsSystemThread routine checks whether a given thread is a system thread. |
| [PsMakeSiloContextPermanent function](..\ntddk\nf-ntddk-psmakesilocontextpermanent.md) | This routine makes the slot in a silo instance read-only, allowing the object in the slot to be retrieved without affecting the reference count on that object. |
| [PsQueryTotalCycleTimeProcess function](..\wdm\nf-wdm-psquerytotalcycletimeprocess.md) | The PsQueryTotalCycleTimeProcess routine returns the accumulated cycle time for the specified process. |
| [PsReferenceSiloContext function](..\ntddk\nf-ntddk-psreferencesilocontext.md) | This routine increments the reference count on the object. |
| [PsRegisterSiloMonitor function](..\ntddk\nf-ntddk-psregistersilomonitor.md) | This routine registers a server silo monitor that can receive notifications about server silo events. |
| [PsRemoveCreateThreadNotifyRoutine function](..\ntddk\nf-ntddk-psremovecreatethreadnotifyroutine.md) | The PsRemoveCreateThreadNotifyRoutine routine removes a callback routine that was registered by the PsSetCreateThreadNotifyRoutine routine. |
| [PsRemoveLoadImageNotifyRoutine function](..\ntddk\nf-ntddk-psremoveloadimagenotifyroutine.md) | The PsRemoveLoadImageNotifyRoutine routine removes a callback routine that was registered by the PsSetLoadImageNotifyRoutine routine. |
| [PsRemoveSiloContext function](..\ntddk\nf-ntddk-psremovesilocontext.md) | This routine removes an object that was inserted in the Silo. |
| [PsReplaceSiloContext function](..\ntddk\nf-ntddk-psreplacesilocontext.md) | This routine inserts an object in a Silo. |
| [PsSetCreateProcessNotifyRoutine function](..\ntddk\nf-ntddk-pssetcreateprocessnotifyroutine.md) | The PsSetCreateProcessNotifyRoutine routine adds a driver-supplied callback routine to, or removes it from, a list of routines to be called whenever a process is created or deleted. |
| [PsSetCreateProcessNotifyRoutineEx function](..\ntddk\nf-ntddk-pssetcreateprocessnotifyroutineex.md) | The PsSetCreateProcessNotifyRoutineEx routine registers or removes a callback routine that notifies the caller when a process is created or exits. |
| [PsSetCreateProcessNotifyRoutineEx2 function](..\ntddk\nf-ntddk-pssetcreateprocessnotifyroutineex2.md) | The PsSetCreateProcessNotifyRoutineEx2 routine registers or removes a callback routine that notifies the caller when a process is created or deleted. |
| [PsSetCreateThreadNotifyRoutine function](..\ntddk\nf-ntddk-pssetcreatethreadnotifyroutine.md) | The PsSetCreateThreadNotifyRoutine routine registers a driver-supplied callback that is subsequently notified when a new thread is created and when such a thread is deleted. |
| [PsSetCreateThreadNotifyRoutineEx function](..\ntddk\nf-ntddk-pssetcreatethreadnotifyroutineex.md) | The PsSetCreateThreadNotifyRoutineEx routine registers a driver-supplied callback that is subsequently notified when a new thread is created and when such a thread is deleted. |
| [PsSetLoadImageNotifyRoutine function](..\ntddk\nf-ntddk-pssetloadimagenotifyroutine.md) | The PsSetLoadImageNotifyRoutine routine registers a driver-supplied callback that is subsequently notified whenever an image is loaded (or mapped into memory). |
| [PsSetLoadImageNotifyRoutineEx function](..\ntddk\nf-ntddk-pssetloadimagenotifyroutineex.md) | The PsSetLoadImageNotifyRoutineEx routine registers a driver-supplied callback that is subsequently notified whenever an image is loaded (or mapped into memory). |
| [PsStartSiloMonitor function](..\ntddk\nf-ntddk-psstartsilomonitor.md) | This routine tries to start the server silo monitor. |
| [PsTerminateServerSilo function](..\ntddk\nf-ntddk-psterminateserversilo.md) | This routine terminates the specified silo. |
| [PsTerminateSystemThread function](..\wdm\nf-wdm-psterminatesystemthread.md) | The PsTerminateSystemThread routine terminates the current system thread. |
| [PsUnregisterSiloMonitor function](..\ntddk\nf-ntddk-psunregistersilomonitor.md) | This routine unregisters a server silo monitor. |
| [PushEntryList function](..\wdm\nf-wdm-pushentrylist.md) | The PushEntryList routine inserts an entry at the beginning of a singly linked list of SINGLE_LIST_ENTRY structures. |
| [PwmParsePinPath function](..\pwmutil\nf-pwmutil-pwmparsepinpath.md) | Parses a pin path under the Pulse Width Modulation (PWM) controller namespace to validate its format and extract the pin number. |
| [READ_PORT_BUFFER_UCHAR function](..\wdm\nf-wdm-read-port-buffer-uchar.md) | The READ_PORT_BUFFER_UCHAR routine reads a number of bytes from the specified port address into a buffer. |
| [READ_PORT_BUFFER_UCHAR function](..\wdm\nf-wdm-read-port-buffer-uchar~r1.md) | The READ_PORT_BUFFER_UCHAR routine reads a number of bytes from the specified port address into a buffer. |
| [READ_PORT_BUFFER_UCHAR function](..\wdm\nf-wdm-read-port-buffer-uchar~r2.md) | The READ_PORT_BUFFER_UCHAR routine reads a number of bytes from the specified port address into a buffer. |
| [READ_PORT_BUFFER_UCHAR function](..\wdm\nf-wdm-read-port-buffer-uchar~r3.md) | The READ_PORT_BUFFER_UCHAR routine reads a number of bytes from the specified port address into a buffer. |
| [READ_PORT_BUFFER_ULONG function](..\wdm\nf-wdm-read-port-buffer-ulong.md) | The READ_PORT_BUFFER_ULONG routine reads a number of ULONG values from the specified port address into a buffer. |
| [READ_PORT_BUFFER_ULONG function](..\wdm\nf-wdm-read-port-buffer-ulong~r1.md) | The READ_PORT_BUFFER_ULONG routine reads a number of ULONG values from the specified port address into a buffer. |
| [READ_PORT_BUFFER_ULONG function](..\wdm\nf-wdm-read-port-buffer-ulong~r2.md) | The READ_PORT_BUFFER_ULONG routine reads a number of ULONG values from the specified port address into a buffer. |
| [READ_PORT_BUFFER_ULONG function](..\wdm\nf-wdm-read-port-buffer-ulong~r3.md) | The READ_PORT_BUFFER_ULONG routine reads a number of ULONG values from the specified port address into a buffer. |
| [READ_PORT_BUFFER_USHORT function](..\wdm\nf-wdm-read-port-buffer-ushort.md) | The READ_PORT_BUFFER_USHORT routine reads a number of USHORT values from the specified port address into a buffer. |
| [READ_PORT_BUFFER_USHORT function](..\wdm\nf-wdm-read-port-buffer-ushort~r1.md) | The READ_PORT_BUFFER_USHORT routine reads a number of USHORT values from the specified port address into a buffer. |
| [READ_PORT_BUFFER_USHORT function](..\wdm\nf-wdm-read-port-buffer-ushort~r2.md) | The READ_PORT_BUFFER_USHORT routine reads a number of USHORT values from the specified port address into a buffer. |
| [READ_PORT_BUFFER_USHORT function](..\wdm\nf-wdm-read-port-buffer-ushort~r3.md) | The READ_PORT_BUFFER_USHORT routine reads a number of USHORT values from the specified port address into a buffer. |
| [READ_PORT_UCHAR function](..\wdm\nf-wdm-read-port-uchar.md) | The READ_PORT_UCHAR routine reads a byte from the specified port address. |
| [READ_PORT_UCHAR function](..\wdm\nf-wdm-read-port-uchar~r1.md) | The READ_PORT_UCHAR routine reads a byte from the specified port address. |
| [READ_PORT_UCHAR function](..\wdm\nf-wdm-read-port-uchar~r2.md) | The READ_PORT_UCHAR routine reads a byte from the specified port address. |
| [READ_PORT_UCHAR function](..\wdm\nf-wdm-read-port-uchar~r3.md) | The READ_PORT_UCHAR routine reads a byte from the specified port address. |
| [READ_PORT_ULONG function](..\wdm\nf-wdm-read-port-ulong.md) | The READ_PORT_ULONG routine reads a ULONG value from the specified port address. |
| [READ_PORT_ULONG function](..\wdm\nf-wdm-read-port-ulong~r1.md) | The READ_PORT_ULONG routine reads a ULONG value from the specified port address. |
| [READ_PORT_ULONG function](..\wdm\nf-wdm-read-port-ulong~r2.md) | The READ_PORT_ULONG routine reads a ULONG value from the specified port address. |
| [READ_PORT_ULONG function](..\wdm\nf-wdm-read-port-ulong~r3.md) | The READ_PORT_ULONG routine reads a ULONG value from the specified port address. |
| [READ_PORT_USHORT function](..\wdm\nf-wdm-read-port-ushort.md) | The READ_PORT_USHORT routine reads a USHORT value from the specified port address. |
| [READ_PORT_USHORT function](..\wdm\nf-wdm-read-port-ushort~r1.md) | The READ_PORT_USHORT routine reads a USHORT value from the specified port address. |
| [READ_PORT_USHORT function](..\wdm\nf-wdm-read-port-ushort~r2.md) | The READ_PORT_USHORT routine reads a USHORT value from the specified port address. |
| [READ_PORT_USHORT function](..\wdm\nf-wdm-read-port-ushort~r3.md) | The READ_PORT_USHORT routine reads a USHORT value from the specified port address. |
| [READ_REGISTER_BUFFER_UCHAR function](..\wdm\nf-wdm-read-register-buffer-uchar.md) | The READ_REGISTER_BUFFER_UCHAR routine reads a number of bytes from the specified register address into a buffer. |
| [READ_REGISTER_BUFFER_UCHAR function](..\wdm\nf-wdm-read-register-buffer-uchar~r1.md) | The READ_REGISTER_BUFFER_UCHAR routine reads a number of bytes from the specified register address into a buffer. |
| [READ_REGISTER_BUFFER_UCHAR function](..\wdm\nf-wdm-read-register-buffer-uchar~r2.md) | The READ_REGISTER_BUFFER_UCHAR routine reads a number of bytes from the specified register address into a buffer. |
| [READ_REGISTER_BUFFER_UCHAR function](..\wdm\nf-wdm-read-register-buffer-uchar~r3.md) | The READ_REGISTER_BUFFER_UCHAR routine reads a number of bytes from the specified register address into a buffer. |
| [READ_REGISTER_BUFFER_ULONG function](..\wdm\nf-wdm-read-register-buffer-ulong.md) | The READ_REGISTER_BUFFER_ULONG routine reads a number of ULONG values from the specified register address into a buffer. |
| [READ_REGISTER_BUFFER_ULONG function](..\wdm\nf-wdm-read-register-buffer-ulong~r1.md) | The READ_REGISTER_BUFFER_ULONG routine reads a number of ULONG values from the specified register address into a buffer. |
| [READ_REGISTER_BUFFER_ULONG function](..\wdm\nf-wdm-read-register-buffer-ulong~r2.md) | The READ_REGISTER_BUFFER_ULONG routine reads a number of ULONG values from the specified register address into a buffer. |
| [READ_REGISTER_BUFFER_ULONG function](..\wdm\nf-wdm-read-register-buffer-ulong~r3.md) | The READ_REGISTER_BUFFER_ULONG routine reads a number of ULONG values from the specified register address into a buffer. |
| [READ_REGISTER_BUFFER_USHORT function](..\wdm\nf-wdm-read-register-buffer-ushort.md) | The READ_REGISTER_BUFFER_USHORT routine reads a number of USHORT values from the specified register address into a buffer. |
| [READ_REGISTER_BUFFER_USHORT function](..\wdm\nf-wdm-read-register-buffer-ushort~r1.md) | The READ_REGISTER_BUFFER_USHORT routine reads a number of USHORT values from the specified register address into a buffer. |
| [READ_REGISTER_BUFFER_USHORT function](..\wdm\nf-wdm-read-register-buffer-ushort~r2.md) | The READ_REGISTER_BUFFER_USHORT routine reads a number of USHORT values from the specified register address into a buffer. |
| [READ_REGISTER_BUFFER_USHORT function](..\wdm\nf-wdm-read-register-buffer-ushort~r3.md) | The READ_REGISTER_BUFFER_USHORT routine reads a number of USHORT values from the specified register address into a buffer. |
| [READ_REGISTER_UCHAR function](..\wdm\nf-wdm-read-register-uchar.md) | The READ_REGISTER_UCHAR routine reads a byte from the specified register address. |
| [READ_REGISTER_UCHAR function](..\wdm\nf-wdm-read-register-uchar~r1.md) | The READ_REGISTER_UCHAR routine reads a byte from the specified register address. |
| [READ_REGISTER_UCHAR function](..\wdm\nf-wdm-read-register-uchar~r2.md) | The READ_REGISTER_UCHAR routine reads a byte from the specified register address. |
| [READ_REGISTER_UCHAR function](..\wdm\nf-wdm-read-register-uchar~r3.md) | The READ_REGISTER_UCHAR routine reads a byte from the specified register address. |
| [READ_REGISTER_ULONG function](..\wdm\nf-wdm-read-register-ulong.md) | The READ_REGISTER_ULONG routine reads a ULONG value from the specified register address. |
| [READ_REGISTER_ULONG function](..\wdm\nf-wdm-read-register-ulong~r1.md) | The READ_REGISTER_ULONG routine reads a ULONG value from the specified register address. |
| [READ_REGISTER_ULONG function](..\wdm\nf-wdm-read-register-ulong~r2.md) | The READ_REGISTER_ULONG routine reads a ULONG value from the specified register address. |
| [READ_REGISTER_ULONG function](..\wdm\nf-wdm-read-register-ulong~r3.md) | The READ_REGISTER_ULONG routine reads a ULONG value from the specified register address. |
| [READ_REGISTER_USHORT function](..\wdm\nf-wdm-read-register-ushort.md) | The READ_REGISTER_USHORT routine reads a USHORT value from the specified register address. |
| [READ_REGISTER_USHORT function](..\wdm\nf-wdm-read-register-ushort~r1.md) | The READ_REGISTER_USHORT routine reads a USHORT value from the specified register address. |
| [READ_REGISTER_USHORT function](..\wdm\nf-wdm-read-register-ushort~r2.md) | The READ_REGISTER_USHORT routine reads a USHORT value from the specified register address. |
| [READ_REGISTER_USHORT function](..\wdm\nf-wdm-read-register-ushort~r3.md) | The READ_REGISTER_USHORT routine reads a USHORT value from the specified register address. |
| [RemoveEntryList function](..\wdm\nf-wdm-removeentrylist.md) | The RemoveEntryList routine removes an entry from a doubly linked list of LIST_ENTRY structures. |
| [RemoveEntryList function](..\wdm\nf-wdm-removeentrylist~r1.md) | The RemoveEntryList routine removes an entry from a doubly linked list of LIST_ENTRY structures. |
| [RemoveHeadList function](..\wdm\nf-wdm-removeheadlist.md) | The RemoveHeadList routine removes an entry from the beginning of a doubly linked list of LIST_ENTRY structures. |
| [RemoveHeadList function](..\wdm\nf-wdm-removeheadlist~r1.md) | The RemoveHeadList routine removes an entry from the beginning of a doubly linked list of LIST_ENTRY structures. |
| [RemoveTailList function](..\wdm\nf-wdm-removetaillist.md) | The RemoveTailList routine removes an entry from the end of a doubly linked list of LIST_ENTRY structures. |
| [RemoveTailList function](..\wdm\nf-wdm-removetaillist~r1.md) | The RemoveTailList routine removes an entry from the end of a doubly linked list of LIST_ENTRY structures. |
| [RtlAnsiStringToUnicodeSize function](..\wdm\nf-wdm-rtlansistringtounicodesize.md) | The RtlAnsiStringToUnicodeSize routine returns the number of bytes required to hold an ANSI string converted into a Unicode string. |
| [RtlAnsiStringToUnicodeString function](..\wdm\nf-wdm-rtlansistringtounicodestring.md) | RtlAnsiStringToUnicodeString converts the given ANSI source string into a Unicode string. |
| [RtlAppendUnicodeStringToString function](..\wdm\nf-wdm-rtlappendunicodestringtostring.md) | The RtlAppendUnicodeStringToString routine concatenates two Unicode strings. |
| [RtlAppendUnicodeToString function](..\wdm\nf-wdm-rtlappendunicodetostring.md) | The RtlAppendUnicodeToString routine concatenates the supplied Unicode string to a buffered Unicode string. |
| [RtlAreBitsClear function](..\wdm\nf-wdm-rtlarebitsclear.md) | The RtlAreBitsClear routine determines whether a given range of bits within a bitmap variable is clear. |
| [RtlAreBitsSet function](..\wdm\nf-wdm-rtlarebitsset.md) | The RtlAreBitsSet routine determines whether a given range of bits within a bitmap variable is set. |
| [RtlByteToChar function](..\ntintsafe\nf-ntintsafe-rtlbytetochar.md) | Converts a value of type BYTE to a value of type CHAR. |
| [RtlByteToInt8 function](..\ntintsafe\nf-ntintsafe-rtlbytetoint8.md) | Converts a value of type BYTE to a value of type INT8. |
| [RtlCharToInteger function](..\ntddk\nf-ntddk-rtlchartointeger.md) | The RtlCharToInteger routine converts a single-byte character string to an integer value in the specified base. |
| [RtlCheckBit function](..\wdm\nf-wdm-rtlcheckbit.md) | The RtlCheckBit routine determines whether a particular bit in a given bitmap variable is clear or set. |
| [RtlCheckBit function](..\wdm\nf-wdm-rtlcheckbit~r1.md) | The RtlCheckBit routine determines whether a particular bit in a given bitmap variable is clear or set. |
| [RtlCheckRegistryKey function](..\wdm\nf-wdm-rtlcheckregistrykey.md) | The RtlCheckRegistryKey routine checks for the existence of a given named key in the registry. |
| [RtlClearAllBits function](..\wdm\nf-wdm-rtlclearallbits.md) | The RtlClearAllBits routine sets all bits in a given bitmap variable to zero. |
| [RtlClearBit function](..\wdm\nf-wdm-rtlclearbit.md) | The RtlClearBit routine sets the specified bit in a bitmap to zero. |
| [RtlClearBits function](..\wdm\nf-wdm-rtlclearbits.md) | The RtlClearBits routine sets all bits in the specified range of bits in the bitmap to zero. |
| [RtlCmDecodeMemIoResource function](..\wdm\nf-wdm-rtlcmdecodememioresource.md) | The RtlCmDecodeMemIoResource routine provides the starting address and length of a CM_PARTIAL_RESOURCE_DESCRIPTOR structure that describes a range of memory or I/O port addresses. |
| [RtlCmEncodeMemIoResource function](..\wdm\nf-wdm-rtlcmencodememioresource.md) | The RtlCmEncodeMemIoResource routine updates a CM_PARTIAL_RESOURCE_DESCRIPTOR structure to describe a range of memory or I/O port addresses. |
| [RtlCompareMemory function](..\wdm\nf-wdm-rtlcomparememory.md) | The RtlCompareMemory routine compares two blocks of memory and returns the number of bytes that match. |
| [RtlCompareString function](..\ntddk\nf-ntddk-rtlcomparestring.md) | The RtlCompareString routine compares two counted strings. |
| [RtlCompareUnicodeString function](..\wdm\nf-wdm-rtlcompareunicodestring.md) | The RtlCompareUnicodeString routine compares two Unicode strings. |
| [RtlConvertLongToLargeInteger function](..\wdm\nf-wdm-rtlconvertlongtolargeinteger.md) | The RtlConvertLongToLargeInteger routine converts the input signed integer to a signed large integer. |
| [RtlConvertLongToLuid function](..\ntddk\nf-ntddk-rtlconvertlongtoluid.md) | The RtlConvertLongToLuid routine converts a long integer to a locally unique identifier (LUID), which is used by the system to represent a security privilege. |
| [RtlConvertUlongToLargeInteger function](..\wdm\nf-wdm-rtlconvertulongtolargeinteger.md) | The RtlConvertUlongToLargeInteger routine converts the input unsigned integer to a signed large integer. For Windows XP and later versions of Windows, do not use this routine; use the native support for __int64. |
| [RtlConvertUlongToLuid function](..\ntddk\nf-ntddk-rtlconvertulongtoluid.md) | The RtlConvertUlongToLuid routine converts an unsigned long integer to a locally unique identifier (LUID), which is used by the system to represent a security privilege. |
| [RtlCopyMemory function](..\wdm\nf-wdm-rtlcopymemory.md) | The RtlCopyMemory routine copies the contents of a source memory block to a destination memory block. |
| [RtlCopyString function](..\ntddk\nf-ntddk-rtlcopystring.md) | The RtlCopyString routine copies a source string to a destination string. |
| [RtlCopyUnicodeString function](..\wdm\nf-wdm-rtlcopyunicodestring.md) | The RtlCopyUnicodeString routine copies a source string to a destination string. |
| [RtlCreateRegistryKey function](..\wdm\nf-wdm-rtlcreateregistrykey.md) | The RtlCreateRegistryKey routine adds a key object in the registry along a given relative path. |
| [RtlCreateSecurityDescriptor function](..\wdm\nf-wdm-rtlcreatesecuritydescriptor.md) | The RtlCreateSecurityDescriptor routine initializes a new absolute-format security descriptor. On return, the security descriptor is initialized with no system ACL, no discretionary ACL, no owner, no primary group, and all control flags set to zero. |
| [RtlDWordPtrAdd function](..\ntintsafe\nf-ntintsafe-rtldwordptradd.md) | Adds two values of type DWORD_PTR. |
| [RtlDWordPtrMult function](..\ntintsafe\nf-ntintsafe-rtldwordptrmult.md) | Multiplies one value of type DWORD_PTR by another. |
| [RtlDWordPtrSub function](..\ntintsafe\nf-ntintsafe-rtldwordptrsub.md) | Subtracts one value of type DWORD_PTR from another. |
| [RtlDeleteRegistryValue function](..\wdm\nf-wdm-rtldeleteregistryvalue.md) | The RtlDeleteRegistryValue routine removes the specified entry name and the associated values from the registry along the given relative path. |
| [RtlDowncaseUnicodeChar function](..\wdm\nf-wdm-rtldowncaseunicodechar.md) | The RtlDowncaseUnicodeChar routine converts the specified Unicode character to lowercase. |
| [RtlEqualMemory function](..\wdm\nf-wdm-rtlequalmemory.md) | The RtlEqualMemory routine compares two blocks of memory to determine whether the specified number of bytes are identical. |
| [RtlEqualString function](..\ntddk\nf-ntddk-rtlequalstring.md) | The RtlEqualString routine compares two counted strings to determine whether they are equal. |
| [RtlEqualUnicodeString function](..\wdm\nf-wdm-rtlequalunicodestring.md) | The RtlEqualUnicodeString routine compares two Unicode strings to determine whether they are equal. |
| [RtlExtendCorrelationVector function](..\ntddk\nf-ntddk-rtlextendcorrelationvector.md) | This routine extends the supplied correlation vector. For a correlation vector of the form X.i, the extended value is X.i.0. |
| [RtlFillMemory function](..\wdm\nf-wdm-rtlfillmemory.md) | The RtlFillMemory routine fills a block of memory with the specified fill value. |
| [RtlFindClearBits function](..\wdm\nf-wdm-rtlfindclearbits.md) | The RtlFindClearBits routine searches for a range of clear bits of a requested size within a bitmap. |
| [RtlFindClearBitsAndSet function](..\wdm\nf-wdm-rtlfindclearbitsandset.md) | The RtlFindClearBitsAndSet routine searches for a range of clear bits of a requested size within a bitmap and sets all bits in the range when it has been located. |
| [RtlFindClearRuns function](..\wdm\nf-wdm-rtlfindclearruns.md) | The RtlFindClearRuns routine finds the specified number of runs of clear bits within a given bitmap. |
| [RtlFindFirstRunClear function](..\wdm\nf-wdm-rtlfindfirstrunclear.md) | The RtlFindFirstRunClear routine searches for the initial contiguous range of clear bits within a given bitmap. |
| [RtlFindLastBackwardRunClear function](..\wdm\nf-wdm-rtlfindlastbackwardrunclear.md) | The RtlFindLastBackwardRunClear routine searches a given bitmap for the preceding clear run of bits, starting from the specified index position. |
| [RtlFindLeastSignificantBit function](..\wdm\nf-wdm-rtlfindleastsignificantbit.md) | The RtlFindLeastSignificantBit routine returns the zero-based position of the least significant nonzero bit in its parameter. |
| [RtlFindLongestRunClear function](..\wdm\nf-wdm-rtlfindlongestrunclear.md) | The RtlFindLongestRunClear routine searches for the largest contiguous range of clear bits within a given bitmap. |
| [RtlFindMostSignificantBit function](..\wdm\nf-wdm-rtlfindmostsignificantbit.md) | The RtlFindMostSignificantBit routine returns the zero-based position of the most significant nonzero bit in its parameter. |
| [RtlFindNextForwardRunClear function](..\wdm\nf-wdm-rtlfindnextforwardrunclear.md) | The RtlFindNextForwardRunClear routine searches a given bitmap variable for the next clear run of bits, starting from the specified index position. |
| [RtlFindSetBits function](..\wdm\nf-wdm-rtlfindsetbits.md) | The RtlFindSetBits routine searches for a range of set bits of a requested size within a bitmap. |
| [RtlFindSetBitsAndClear function](..\wdm\nf-wdm-rtlfindsetbitsandclear.md) | The RtlFindSetBitsAndClear routine searches for a range of set bits of a requested size within a bitmap and clears all bits in the range when it has been located. |
| [RtlFreeAnsiString function](..\wdm\nf-wdm-rtlfreeansistring.md) | The RtlFreeAnsiString routine releases storage that was allocated by RtlUnicodeStringToAnsiString. |
| [RtlFreeUnicodeString function](..\wdm\nf-wdm-rtlfreeunicodestring.md) | The RtlFreeUnicodeString routine releases storage that was allocated by RtlAnsiStringToUnicodeString or RtlUpcaseUnicodeString. |
| [RtlGUIDFromString function](..\wdm\nf-wdm-rtlguidfromstring.md) | The RtlGUIDFromString routine converts the given Unicode string to a GUID in binary format. |
| [RtlGetEnabledExtendedFeatures function](..\ntddk\nf-ntddk-rtlgetenabledextendedfeatures.md) | The RtlGetEnabledExtendedFeatures routine returns a mask of extended processor features that are enabled by the system. |
| [RtlGetVersion function](..\wdm\nf-wdm-rtlgetversion.md) | The RtlGetVersion routine returns version information about the currently running operating system. |
| [RtlHashUnicodeString function](..\wdm\nf-wdm-rtlhashunicodestring.md) | The RtlHashUnicodeString routine creates a hash value from a given Unicode string and hash algorithm. |
| [RtlIncrementCorrelationVector function](..\ntddk\nf-ntddk-rtlincrementcorrelationvector.md) | Increments the specified correlation vector. For a correlation vector of the form X.i, the incremented value is be X.(i+1). |
| [RtlInitAnsiString function](..\wdm\nf-wdm-rtlinitansistring.md) | The RtlInitAnsiString routine initializes a counted string of ANSI characters. |
| [RtlInitString function](..\wdm\nf-wdm-rtlinitstring.md) | The RtlInitString routine initializes a counted string of 8-bit characters. |
| [RtlInitStringEx function](..\ntifs\nf-ntifs-rtlinitstringex.md) | The RtlInitStringEx routine initializes a counted string of 8-bit characters. |
| [RtlInitStringEx function](..\wdm\nf-wdm-rtlinitstringex.md) | The RtlInitStringEx routine initializes a counted string of 8-bit characters. |
| [RtlInitUnicodeString function](..\wdm\nf-wdm-rtlinitunicodestring.md) | For more information, see the WdmlibRtlInitUnicodeStringEx function. |
| [RtlInitializeBitMap function](..\wdm\nf-wdm-rtlinitializebitmap.md) | The RtlInitializeBitMap routine initializes the header of a bitmap variable. |
| [RtlInitializeCorrelationVector function](..\ntddk\nf-ntddk-rtlinitializecorrelationvector.md) | Initializes the specified correlation vector with the supplied GUID. |
| [RtlInt64ToUnicodeString function](..\wdm\nf-wdm-rtlint64tounicodestring.md) | The RtlInt64ToUnicodeString routine converts a specified unsigned 64-bit integer value to a Unicode string that represents the value in a specified base. |
| [RtlInt8Add function](..\ntintsafe\nf-ntintsafe-rtlint8add.md) | Adds two values of type INT8. |
| [RtlInt8Mult function](..\ntintsafe\nf-ntintsafe-rtlint8mult.md) | Multiplies one value of type INT8 by another. |
| [RtlInt8Sub function](..\ntintsafe\nf-ntintsafe-rtlint8sub.md) | Subtracts one value of type INT8 from another. |
| [RtlInt8ToUChar function](..\ntintsafe\nf-ntintsafe-rtlint8touchar.md) | Converts a value of type INT8 to a value of type UCHAR. |
| [RtlInt8ToUInt function](..\ntintsafe\nf-ntintsafe-rtlint8touint.md) | Converts a value of type INT8 to a value of type UINT. |
| [RtlInt8ToUInt8 function](..\ntintsafe\nf-ntintsafe-rtlint8touint8.md) | Converts a value of type INT8 to a value of type UINT8. |
| [RtlInt8ToUIntPtr function](..\ntintsafe\nf-ntintsafe-rtlint8touintptr.md) | Converts a value of type INT8 to a value of type UINT_PTR. |
| [RtlInt8ToULong function](..\ntintsafe\nf-ntintsafe-rtlint8toulong.md) | Converts a value of type INT8 to a value of type ULONG. |
| [RtlInt8ToULongLong function](..\ntintsafe\nf-ntintsafe-rtlint8toulonglong.md) | Converts a value of type INT8 to a value of type ULONGLONG. |
| [RtlInt8ToULongPtr function](..\ntintsafe\nf-ntintsafe-rtlint8toulongptr.md) | Converts a value of type INT8 to a value of type ULONG_PTR. |
| [RtlInt8ToUShort function](..\ntintsafe\nf-ntintsafe-rtlint8toushort.md) | Converts a value of type INT8 to a value of type USHORT. |
| [RtlIntAdd function](..\ntintsafe\nf-ntintsafe-rtlintadd.md) | Adds two values of type INT. |
| [RtlIntMult function](..\ntintsafe\nf-ntintsafe-rtlintmult.md) | Multiplies one value of type INT by another. |
| [RtlIntPtrAdd function](..\ntintsafe\nf-ntintsafe-rtlintptradd.md) | Adds two values of type INT_PTR. |
| [RtlIntPtrMult function](..\ntintsafe\nf-ntintsafe-rtlintptrmult.md) | Multiplies one value of type INT_PTR by another. |
| [RtlIntPtrSub function](..\ntintsafe\nf-ntintsafe-rtlintptrsub.md) | Subtracts one value of type INT_PTR from another. |
| [RtlIntPtrToChar function](..\ntintsafe\nf-ntintsafe-rtlintptrtochar.md) | Converts a value of type INT_PTR to a value of type CHAR. |
| [RtlIntPtrToInt function](..\ntintsafe\nf-ntintsafe-rtlintptrtoint.md) | Converts a value of type INT_PTR to a value of type INT. |
| [RtlIntPtrToInt8 function](..\ntintsafe\nf-ntintsafe-rtlintptrtoint8.md) | Converts a value of type INT_PTR to a value of type INT8. |
| [RtlIntPtrToLong function](..\ntintsafe\nf-ntintsafe-rtlintptrtolong.md) | Converts a value of type INT_PTR to a value of type LONG. |
| [RtlIntPtrToLongPtr function](..\ntintsafe\nf-ntintsafe-rtlintptrtolongptr.md) | Converts a value of type INT_PTR to a value of type LONG_PTR. |
| [RtlIntPtrToShort function](..\ntintsafe\nf-ntintsafe-rtlintptrtoshort.md) | Converts a value of type INT_PTR to a value of type SHORT. |
| [RtlIntPtrToUChar function](..\ntintsafe\nf-ntintsafe-rtlintptrtouchar.md) | Converts a value of type INT_PTR to a value of type UCHAR. |
| [RtlIntPtrToUInt function](..\ntintsafe\nf-ntintsafe-rtlintptrtouint.md) | Converts a value of type INT_PTR to a value of type UINT. |
| [RtlIntPtrToUInt8 function](..\ntintsafe\nf-ntintsafe-rtlintptrtouint8.md) | Converts a value of type INT_PTR to a value of type UINT8. |
| [RtlIntPtrToUIntPtr function](..\ntintsafe\nf-ntintsafe-rtlintptrtouintptr.md) | Converts a value of type INT_PTR to a value of type UINT_PTR. |
| [RtlIntPtrToULong function](..\ntintsafe\nf-ntintsafe-rtlintptrtoulong.md) | Converts a value of type INT_PTR to a value of type ULONG. |
| [RtlIntPtrToULongLong function](..\ntintsafe\nf-ntintsafe-rtlintptrtoulonglong.md) | Converts a value of type INT_PTR to a value of type ULONGLONG. |
| [RtlIntPtrToULongPtr function](..\ntintsafe\nf-ntintsafe-rtlintptrtoulongptr.md) | Converts a value of type INT_PTR to a value of type ULONG_PTR. |
| [RtlIntPtrToUShort function](..\ntintsafe\nf-ntintsafe-rtlintptrtoushort.md) | Converts a value of type INT_PTR to a value of type USHORT. |
| [RtlIntPtrToUnicodeString function](..\wdm\nf-wdm-rtlintptrtounicodestring.md) | The RtlIntPtrToUnicodeString routine converts a specified ULONG_PTR value to a Unicode string that represents the value in a specified base. |
| [RtlIntSub function](..\ntintsafe\nf-ntintsafe-rtlintsub.md) | Subtracts one value of type INT from another. |
| [RtlIntToChar function](..\ntintsafe\nf-ntintsafe-rtlinttochar.md) | Converts a value of type INT to a value of type CHAR. |
| [RtlIntToInt8 function](..\ntintsafe\nf-ntintsafe-rtlinttoint8.md) | Converts a value of type INT to a value of type INT8. |
| [RtlIntToShort function](..\ntintsafe\nf-ntintsafe-rtlinttoshort.md) | Converts a value of type INT to a value of type SHORT. |
| [RtlIntToUChar function](..\ntintsafe\nf-ntintsafe-rtlinttouchar.md) | Converts a value of type INT to a value of type UCHAR. |
| [RtlIntToUInt function](..\ntintsafe\nf-ntintsafe-rtlinttouint.md) | Converts a value of type INT to a value of type UINT. |
| [RtlIntToUInt8 function](..\ntintsafe\nf-ntintsafe-rtlinttouint8.md) | Converts a value of type INT to a value of type UINT8. |
| [RtlIntToULong function](..\ntintsafe\nf-ntintsafe-rtlinttoulong.md) | Converts a value of type INT to a value of type ULONG. |
| [RtlIntToULongLong function](..\ntintsafe\nf-ntintsafe-rtlinttoulonglong.md) | Converts a value of type INT to a value of type ULONGLONG. |
| [RtlIntToUShort function](..\ntintsafe\nf-ntintsafe-rtlinttoushort.md) | Converts a value of type INT to a value of type USHORT. |
| [RtlIntegerToUnicodeString function](..\wdm\nf-wdm-rtlintegertounicodestring.md) | The RtlIntegerToUnicodeString routine converts an unsigned integer value to a null-terminated string of one or more Unicode characters in the specified base. |
| [RtlIoDecodeMemIoResource function](..\wdm\nf-wdm-rtliodecodememioresource.md) | The RtlIoDecodeMemIoResource routine provides the address information that is contained in an IO_RESOURCE_DESCRIPTOR structure that describes a range of memory or I/O port addresses. |
| [RtlIoEncodeMemIoResource function](..\wdm\nf-wdm-rtlioencodememioresource.md) | The RtlIoEncodeMemIoResource routine updates an IO_RESOURCE_DESCRIPTOR structure to describe a range of memory or I/O port addresses. |
| [RtlIsNtDdiVersionAvailable function](..\wdm\nf-wdm-rtlisntddiversionavailable.md) | The RtlIsNtDdiVersionAvailable routine determines if a specified version of the Microsoft Windows device driver interface (DDI) is available. |
| [RtlIsServicePackVersionInstalled function](..\wdm\nf-wdm-rtlisservicepackversioninstalled.md) | The RtlIsServicePackVersionInstalled routine determines if a specified service pack version of the Microsoft Windows device driver interface (DDI) is installed. |
| [RtlIsStateSeparationEnabled function](..\ntddk\nf-ntddk-rtlisstateseparationenabled.md) | Checks if the SKU for the current context supports multiple sessions. |
| [RtlLengthSecurityDescriptor function](..\wdm\nf-wdm-rtllengthsecuritydescriptor.md) | The RtlLengthSecurityDescriptor routine returns the size of a given security descriptor. |
| [RtlLongAdd function](..\ntintsafe\nf-ntintsafe-rtllongadd.md) | Adds two values of type LONG. |
| [RtlLongLongAdd function](..\ntintsafe\nf-ntintsafe-rtllonglongadd.md) | Adds two values of type LONGLONG. |
| [RtlLongLongMult function](..\ntintsafe\nf-ntintsafe-rtllonglongmult.md) | Multiplies one value of type LONGLONG by another. |
| [RtlLongLongSub function](..\ntintsafe\nf-ntintsafe-rtllonglongsub.md) | Subtracts one value of type LONGLONG from another. |
| [RtlLongLongToChar function](..\ntintsafe\nf-ntintsafe-rtllonglongtochar.md) | Converts a value of type LONGLONG to a value of type CHAR. |
| [RtlLongLongToInt function](..\ntintsafe\nf-ntintsafe-rtllonglongtoint.md) | Converts a value of type LONGLONG to a value of type INT. |
| [RtlLongLongToInt8 function](..\ntintsafe\nf-ntintsafe-rtllonglongtoint8.md) | Converts a value of type LONGLONG to a value of type INT8. |
| [RtlLongLongToIntPtr function](..\ntintsafe\nf-ntintsafe-rtllonglongtointptr.md) | Converts a value of type LONGLONG to a value of type INT_PTR. |
| [RtlLongLongToLong function](..\ntintsafe\nf-ntintsafe-rtllonglongtolong.md) | Converts a value of type LONGLONG to a value of type LONG. |
| [RtlLongLongToLongPtr function](..\ntintsafe\nf-ntintsafe-rtllonglongtolongptr.md) | Converts a value of type LONGLONG to a value of type LONG_PTR. |
| [RtlLongLongToShort function](..\ntintsafe\nf-ntintsafe-rtllonglongtoshort.md) | Converts a value of type LONGLONG to a value of type SHORT. |
| [RtlLongLongToUChar function](..\ntintsafe\nf-ntintsafe-rtllonglongtouchar.md) | Converts a value of type LONGLONG to a value of type UCHAR. |
| [RtlLongLongToUInt function](..\ntintsafe\nf-ntintsafe-rtllonglongtouint.md) | Converts a value of type LONGLONG to a value of type UINT. |
| [RtlLongLongToUInt8 function](..\ntintsafe\nf-ntintsafe-rtllonglongtouint8.md) | Converts a value of type LONGLONG to a value of type UNIT8. |
| [RtlLongLongToULong function](..\ntintsafe\nf-ntintsafe-rtllonglongtoulong.md) | Converts a value of type LONGLONG to a value of type ULONG. |
| [RtlLongLongToULongLong function](..\ntintsafe\nf-ntintsafe-rtllonglongtoulonglong.md) | Converts a value of type LONGLONG to a value of type LONGLONG. |
| [RtlLongLongToUShort function](..\ntintsafe\nf-ntintsafe-rtllonglongtoushort.md) | Converts a value of type LONGLONG to a value of type USHORT. |
| [RtlLongMult function](..\ntintsafe\nf-ntintsafe-rtllongmult.md) | Multiplies one value of type LONG by another. |
| [RtlLongPtrAdd function](..\ntintsafe\nf-ntintsafe-rtllongptradd.md) | Adds two values of type LONG_PTR. |
| [RtlLongPtrMult function](..\ntintsafe\nf-ntintsafe-rtllongptrmult.md) | Multiplies one value of type LONG_PTR by another. |
| [RtlLongPtrSub function](..\ntintsafe\nf-ntintsafe-rtllongptrsub.md) | Subtracts one value of type LONG_PTR from another. |
| [RtlLongPtrToChar function](..\ntintsafe\nf-ntintsafe-rtllongptrtochar.md) | Converts a value of type LONG_PTR to a value of type CHAR. |
| [RtlLongPtrToInt function](..\ntintsafe\nf-ntintsafe-rtllongptrtoint.md) | Converts a value of type LONG_PTR to a value of type INT. |
| [RtlLongPtrToInt8 function](..\ntintsafe\nf-ntintsafe-rtllongptrtoint8.md) | Converts a value of type LONG_PTR to a value of type INT8. |
| [RtlLongPtrToIntPtr function](..\ntintsafe\nf-ntintsafe-rtllongptrtointptr.md) | Converts a value of type LONG_PTR to a value of type INT_PTR. |
| [RtlLongPtrToLong function](..\ntintsafe\nf-ntintsafe-rtllongptrtolong.md) | Converts a value of type LONG_PTR to a value of type LONG. |
| [RtlLongPtrToShort function](..\ntintsafe\nf-ntintsafe-rtllongptrtoshort.md) | Converts a value of type LONG_PTR to a value of type SHORT. |
| [RtlLongPtrToUChar function](..\ntintsafe\nf-ntintsafe-rtllongptrtouchar.md) | Converts a value of type LONG_PTR to a value of type UCHAR. |
| [RtlLongPtrToUInt function](..\ntintsafe\nf-ntintsafe-rtllongptrtouint.md) | Converts a value of type LONG_PTR to a value of type UINT. |
| [RtlLongPtrToUInt8 function](..\ntintsafe\nf-ntintsafe-rtllongptrtouint8.md) | Converts a value of type LONG_PTR to a value of type UINT8. |
| [RtlLongPtrToUIntPtr function](..\ntintsafe\nf-ntintsafe-rtllongptrtouintptr.md) | Converts a value of type LONG_PTR to a value of type UINT_PTR. |
| [RtlLongPtrToULong function](..\ntintsafe\nf-ntintsafe-rtllongptrtoulong.md) | Converts a value of type LONG_PTR to a value of type ULONG. |
| [RtlLongPtrToULongLong function](..\ntintsafe\nf-ntintsafe-rtllongptrtoulonglong.md) | Converts a value of type LONG_PTR to a value of type ULONGLONG. |
| [RtlLongPtrToULongPtr function](..\ntintsafe\nf-ntintsafe-rtllongptrtoulongptr.md) | Converts a value of type LONG_PTR to a value of type ULONG_PTR. |
| [RtlLongPtrToUShort function](..\ntintsafe\nf-ntintsafe-rtllongptrtoushort.md) | Converts a value of type LONG_PTR to a value of type USHORT. |
| [RtlLongSub function](..\ntintsafe\nf-ntintsafe-rtllongsub.md) | Subtracts one value of type LONG from another. |
| [RtlLongToChar function](..\ntintsafe\nf-ntintsafe-rtllongtochar.md) | Converts a value of type LONG to a value of type CHAR. |
| [RtlLongToInt function](..\ntintsafe\nf-ntintsafe-rtllongtoint.md) | Converts a value of type LONG to a value of type INT. |
| [RtlLongToInt8 function](..\ntintsafe\nf-ntintsafe-rtllongtoint8.md) | Converts a value of type LONG to a value of type INT8. |
| [RtlLongToIntPtr function](..\ntintsafe\nf-ntintsafe-rtllongtointptr.md) | Converts a value of type LONG to a value of type INT_PTR. |
| [RtlLongToShort function](..\ntintsafe\nf-ntintsafe-rtllongtoshort.md) | Converts a value of type LONG to a value of type SHORT. |
| [RtlLongToUChar function](..\ntintsafe\nf-ntintsafe-rtllongtouchar.md) | Converts a value of type LONG to a value of type UCHAR. |
| [RtlLongToUInt function](..\ntintsafe\nf-ntintsafe-rtllongtouint.md) | Converts a value of type LONG to a value of type UINT. |
| [RtlLongToUInt8 function](..\ntintsafe\nf-ntintsafe-rtllongtouint8.md) | Converts a value of type LONG to a value of type UINT8. |
| [RtlLongToUIntPtr function](..\ntintsafe\nf-ntintsafe-rtllongtouintptr.md) | Converts a value of type LONG to a value of type UINT_PTR. |
| [RtlLongToULong function](..\ntintsafe\nf-ntintsafe-rtllongtoulong.md) | Converts a value of type LONG to a value of type ULONG. |
| [RtlLongToULongLong function](..\ntintsafe\nf-ntintsafe-rtllongtoulonglong.md) | Converts a value of type LONG to a value of type ULONGLONG. |
| [RtlLongToULongPtr function](..\ntintsafe\nf-ntintsafe-rtllongtoulongptr.md) | Converts a value of type LONG to a value of type ULONG_PTR. |
| [RtlLongToUShort function](..\ntintsafe\nf-ntintsafe-rtllongtoushort.md) | Converts a value of type LONG to a value of type USHORT. |
| [RtlMapGenericMask function](..\ntddk\nf-ntddk-rtlmapgenericmask.md) | The RtlMapGenericMask routine determines the nongeneric access rights specified by an ACCESS_MASK. |
| [RtlMoveMemory function](..\wdm\nf-wdm-rtlmovememory.md) | The RtlMoveMemory routine copies the contents of a source memory block to a destination memory block, and supports overlapping source and destination memory blocks. |
| [RtlNumberOfClearBits function](..\wdm\nf-wdm-rtlnumberofclearbits.md) | The RtlNumberOfClearBits routine returns a count of the clear bits in a given bitmap variable. |
| [RtlNumberOfSetBits function](..\wdm\nf-wdm-rtlnumberofsetbits.md) | The RtlNumberOfSetBits routine returns a count of the set bits in a given bitmap variable. |
| [RtlNumberOfSetBitsUlongPtr function](..\wdm\nf-wdm-rtlnumberofsetbitsulongptr.md) | The RtlNumberOfSetBitsUlongPtr routine returns the number of bits in the specified ULONG_PTR integer value that are set to one. |
| [RtlPrefetchMemoryNonTemporal function](..\wdm\nf-wdm-rtlprefetchmemorynontemporal.md) | The RtlPrefetchMemoryNonTemporal routine provides a hint to the processor that a buffer should be temporarily moved into the processor cache. |
| [RtlPrefixUnicodeString function](..\ntddk\nf-ntddk-rtlprefixunicodestring.md) | The RtlPrefixUnicodeString routine compares two Unicode strings to determine whether one string is a prefix of the other. |
| [RtlPtrdiffTAdd function](..\ntintsafe\nf-ntintsafe-rtlptrdifftadd.md) | Adds two values of type PTRDIFF_T. |
| [RtlPtrdiffTMult function](..\ntintsafe\nf-ntintsafe-rtlptrdifftmult.md) | Multiplies one value of type PTRDIFF_T by another. |
| [RtlPtrdiffTSub function](..\ntintsafe\nf-ntintsafe-rtlptrdifftsub.md) | Subtracts one value of type PTRDIFF_T from another. |
| [RtlQueryRegistryValues function](..\wdm\nf-wdm-rtlqueryregistryvalues.md) | The RtlQueryRegistryValues routine allows the caller to query several values from the registry subtree with a single call. |
| [RtlRunOnceBeginInitialize function](..\ntddk\nf-ntddk-rtlrunoncebegininitialize.md) | The RtlRunOnceBeginInitialize routine begins a one-time initialization. |
| [RtlRunOnceComplete function](..\ntddk\nf-ntddk-rtlrunoncecomplete.md) | The RtlRunOnceComplete routine completes the one-time initialization began by RtlRunOnceBeginInitialize. |
| [RtlRunOnceExecuteOnce function](..\ntddk\nf-ntddk-rtlrunonceexecuteonce.md) | The RtlRunOnceExecuteOnce performs a one-time initialization. |
| [RtlRunOnceInitialize function](..\ntddk\nf-ntddk-rtlrunonceinitialize.md) | The RtlRunOnceInitialize routine initializes a RTL_RUN_ONCE structure. |
| [RtlSIZETAdd function](..\ntintsafe\nf-ntintsafe-rtlsizetadd~r1.md) | Adds two values of type SIZE_T. |
| [RtlSIZETMult function](..\ntintsafe\nf-ntintsafe-rtlsizetmult~r1.md) | Multiplies one value of type SIZE_T by another. |
| [RtlSIZETSub function](..\ntintsafe\nf-ntintsafe-rtlsizetsub~r1.md) | Subtracts one value of type SIZE_T from another. |
| [RtlSSIZETAdd function](..\ntintsafe\nf-ntintsafe-rtlssizetadd.md) | Adds two values of type SSIZE_T. |
| [RtlSSIZETMult function](..\ntintsafe\nf-ntintsafe-rtlssizetmult.md) | Multiplies one value of type SSIZE_T by another. |
| [RtlSSIZETSub function](..\ntintsafe\nf-ntintsafe-rtlssizetsub.md) | Subtracts one value of type SSIZE_T from another. |
| [RtlSecureZeroMemory function](..\wdm\nf-wdm-rtlsecurezeromemory.md) | The RtlSecureZeroMemory routine fills a block of memory with zeros in a way that is guaranteed to be secure. |
| [RtlSetAllBits function](..\wdm\nf-wdm-rtlsetallbits.md) | The RtlSetAllBits routine sets all bits in a given bitmap variable. |
| [RtlSetBit function](..\wdm\nf-wdm-rtlsetbit.md) | The RtlSetBit routine sets the specified bit in a bitmap to one. |
| [RtlSetBits function](..\wdm\nf-wdm-rtlsetbits.md) | The RtlSetBits routine sets all bits in a given range of a given bitmap variable. |
| [RtlSetDaclSecurityDescriptor function](..\wdm\nf-wdm-rtlsetdaclsecuritydescriptor.md) | The RtlSetDaclSecurityDescriptor routine sets the DACL information of an absolute-format security descriptor, or if there is already a DACL present in the security descriptor, it is superseded. |
| [RtlShortAdd function](..\ntintsafe\nf-ntintsafe-rtlshortadd.md) | Adds two values of type SHORT. |
| [RtlShortMult function](..\ntintsafe\nf-ntintsafe-rtlshortmult.md) | Multiplies one value of type SHORT by another. |
| [RtlShortSub function](..\ntintsafe\nf-ntintsafe-rtlshortsub.md) | Subtracts one value of type SHORT from another. |
| [RtlShortToChar function](..\ntintsafe\nf-ntintsafe-rtlshorttochar.md) | Converts a value of type SHORT to a value of type CHAR. |
| [RtlShortToDWordPtr function](..\ntintsafe\nf-ntintsafe-rtlshorttodwordptr.md) | Converts a value of type SHORT to a value of type DWORD_PTR. |
| [RtlShortToInt8 function](..\ntintsafe\nf-ntintsafe-rtlshorttoint8.md) | Converts a value of type SHORT to a value of type INT8. |
| [RtlShortToUChar function](..\ntintsafe\nf-ntintsafe-rtlshorttouchar.md) | Converts a value of type SHORT to a value of type UCHAR. |
| [RtlShortToUInt function](..\ntintsafe\nf-ntintsafe-rtlshorttouint.md) | Converts a value of type SHORT to a value of type UINT. |
| [RtlShortToUInt8 function](..\ntintsafe\nf-ntintsafe-rtlshorttouint8.md) | Converts a value of type SHORT to a value of type UINT8. |
| [RtlShortToUIntPtr function](..\ntintsafe\nf-ntintsafe-rtlshorttouintptr.md) | Converts a value of type SHORT to a value of type UINT_PTR. |
| [RtlShortToULong function](..\ntintsafe\nf-ntintsafe-rtlshorttoulong.md) | Converts a value of type SHORT to a value of type ULONG. |
| [RtlShortToULongLong function](..\ntintsafe\nf-ntintsafe-rtlshorttoulonglong.md) | Converts a value of type SHORT to a value of type ULONGLONG. |
| [RtlShortToULongPtr function](..\ntintsafe\nf-ntintsafe-rtlshorttoulongptr.md) | Converts a value of type SHORT to a value of type ULONG_PTR. |
| [RtlShortToUShort function](..\ntintsafe\nf-ntintsafe-rtlshorttoushort.md) | Converts a value of type SHORT to a value of type USHORT. |
| [RtlSizeTAdd function](..\ntintsafe\nf-ntintsafe-rtlsizetadd.md) | Adds two values of type SIZE_T. |
| [RtlSizeTMult function](..\ntintsafe\nf-ntintsafe-rtlsizetmult.md) | Multiplies one value of type SIZE_T by another. |
| [RtlSizeTSub function](..\ntintsafe\nf-ntintsafe-rtlsizetsub.md) | Subtracts one value of type SIZE_T from another. |
| [RtlStringCbCatA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcata.md) | The RtlStringCbCatW and RtlStringCbCatA functions concatenate two byte-counted strings. |
| [RtlStringCbCatExA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcatexa.md) | The RtlStringCbCatExW and RtlStringCbCatExA functions concatenate two byte-counted strings. |
| [RtlStringCbCatExW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcatexw.md) | The RtlStringCbCatExW and RtlStringCbCatExA functions concatenate two byte-counted strings. |
| [RtlStringCbCatNA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcatna.md) | The RtlStringCbCatNW and RtlStringCbCatNA functions concatenate two byte-counted strings while limiting the size of the appended string. |
| [RtlStringCbCatNExA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcatnexa.md) | The RtlStringCbCatNExW and RtlStringCbCatNExA functions concatenate two byte-counted strings while limiting the size of the appended string. |
| [RtlStringCbCatNExW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcatnexw.md) | The RtlStringCbCatNExW and RtlStringCbCatNExA functions concatenate two byte-counted strings while limiting the size of the appended string. |
| [RtlStringCbCatNW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcatnw.md) | The RtlStringCbCatNW and RtlStringCbCatNA functions concatenate two byte-counted strings while limiting the size of the appended string. |
| [RtlStringCbCatW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcatw.md) | The RtlStringCbCatW and RtlStringCbCatA functions concatenate two byte-counted strings. |
| [RtlStringCbCopyA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcopya.md) | The RtlStringCbCopyW and RtlStringCbCopyA functions copy a byte-counted string into a buffer. |
| [RtlStringCbCopyExA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcopyexa.md) | The RtlStringCbCopyExW and RtlStringCbCopyExA functions copy a byte-counted string into a buffer. |
| [RtlStringCbCopyExW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcopyexw.md) | The RtlStringCbCopyExW and RtlStringCbCopyExA functions copy a byte-counted string into a buffer. |
| [RtlStringCbCopyNA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcopyna.md) | The RtlStringCbCopyNW and RtlStringCbCopyNA functions copy a byte-counted string to a buffer while limiting the size of the copied string. |
| [RtlStringCbCopyNExA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcopynexa.md) | The RtlStringCbCopyNExW and RtlStringCbCopyNExA functions copy a byte-counted string to a buffer while limiting the size of the copied string. |
| [RtlStringCbCopyNExW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcopynexw.md) | The RtlStringCbCopyNExW and RtlStringCbCopyNExA functions copy a byte-counted string to a buffer while limiting the size of the copied string. |
| [RtlStringCbCopyNW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcopynw.md) | The RtlStringCbCopyNW and RtlStringCbCopyNA functions copy a byte-counted string to a buffer while limiting the size of the copied string. |
| [RtlStringCbCopyUnicodeString function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcopyunicodestring.md) | The RtlStringCbCopyUnicodeString function copies the contents of a UNICODE_STRING structure to a specified destination. |
| [RtlStringCbCopyUnicodeStringEx function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcopyunicodestringex.md) | The RtlStringCbCopyUnicodeStringEx function copies the contents of a UNICODE_STRING structure to a specified destination. |
| [RtlStringCbCopyW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbcopyw.md) | The RtlStringCbCopyW and RtlStringCbCopyA functions copy a byte-counted string into a buffer. |
| [RtlStringCbLengthA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcblengtha.md) | The RtlStringCbLengthW and RtlStringCbLengthA functions determine the length, in bytes, of a supplied string. |
| [RtlStringCbLengthW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcblengthw.md) | The RtlStringCbLengthW and RtlStringCbLengthA functions determine the length, in bytes, of a supplied string. |
| [RtlStringCbPrintfA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbprintfa.md) | The RtlStringCbPrintfW and RtlStringCbPrintfA functions create a byte-counted text string, with formatting that is based on supplied formatting information. |
| [RtlStringCbPrintfExA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbprintfexa.md) | The RtlStringCbPrintfExW and RtlStringCbPrintfExA functions create a byte-counted text string, with formatting that is based on supplied formatting information. |
| [RtlStringCbPrintfExW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbprintfexw.md) | The RtlStringCbPrintfExW and RtlStringCbPrintfExA functions create a byte-counted text string, with formatting that is based on supplied formatting information. |
| [RtlStringCbPrintfW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbprintfw.md) | The RtlStringCbPrintfW and RtlStringCbPrintfA functions create a byte-counted text string, with formatting that is based on supplied formatting information. |
| [RtlStringCbVPrintfA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbvprintfa.md) | The RtlStringCbVPrintfW and RtlStringCbVPrintfA functions create a byte-counted text string, with formatting that is based on supplied formatting information. |
| [RtlStringCbVPrintfExA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbvprintfexa.md) | The RtlStringCbVPrintfExW and RtlStringCbVPrintfExA functions create a byte-counted text string, with formatting that is based on supplied formatting information. |
| [RtlStringCbVPrintfExW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbvprintfexw.md) | The RtlStringCbVPrintfExW and RtlStringCbVPrintfExA functions create a byte-counted text string, with formatting that is based on supplied formatting information. |
| [RtlStringCbVPrintfW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcbvprintfw.md) | The RtlStringCbVPrintfW and RtlStringCbVPrintfA functions create a byte-counted text string, with formatting that is based on supplied formatting information. |
| [RtlStringCchCatA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcata.md) | The RtlStringCchCatW and RtlStringCchCatA functions concatenate two character-counted strings. |
| [RtlStringCchCatExA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcatexa.md) | The RtlStringCchCatExW and RtlStringCchCatExA functions concatenate two character-counted strings. |
| [RtlStringCchCatExW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcatexw.md) | The RtlStringCchCatExW and RtlStringCchCatExA functions concatenate two character-counted strings. |
| [RtlStringCchCatNA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcatna.md) | The RtlStringCchCatNW and RtlStringCchCatNA functions concatenate two character-counted strings while limiting the size of the appended string. |
| [RtlStringCchCatNExA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcatnexa.md) | The RtlStringCchCatNExW and RtlStringCchCatNExA functions concatenate two character-counted strings while limiting the size of the appended string. |
| [RtlStringCchCatNExW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcatnexw.md) | The RtlStringCchCatNExW and RtlStringCchCatNExA functions concatenate two character-counted strings while limiting the size of the appended string. |
| [RtlStringCchCatNW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcatnw.md) | The RtlStringCchCatNW and RtlStringCchCatNA functions concatenate two character-counted strings while limiting the size of the appended string. |
| [RtlStringCchCatW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcatw.md) | The RtlStringCchCatW and RtlStringCchCatA functions concatenate two character-counted strings. |
| [RtlStringCchCopyA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcopya.md) | The RtlStringCchCopyW and RtlStringCchCopyA functions copy a null-terminated source string into a destination buffer of specified length. |
| [RtlStringCchCopyExA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcopyexa.md) | The RtlStringCchCopyExW and RtlStringCchCopyExA functions copy a character-counted string into a buffer. |
| [RtlStringCchCopyExW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcopyexw.md) | The RtlStringCchCopyExW and RtlStringCchCopyExA functions copy a character-counted string into a buffer. |
| [RtlStringCchCopyNExA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcopynexa.md) | The RtlStringCchCopyNExW and RtlStringCchCopyNExA functions copy a character-counted string to a buffer while limiting the size of the copied string. |
| [RtlStringCchCopyNExW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcopynexw.md) | The RtlStringCchCopyNExW and RtlStringCchCopyNExA functions copy a character-counted string to a buffer while limiting the size of the copied string. |
| [RtlStringCchCopyNW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcopynw.md) | The RtlStringCchCopyNW and RtlStringCchCopyNA functions copy a character-counted string to a buffer while limiting the size of the copied string. |
| [RtlStringCchCopyUnicodeString function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcopyunicodestring.md) | The RtlStringCchCopyUnicodeString function copies the contents of a UNICODE_STRING structure to a specified destination. |
| [RtlStringCchCopyUnicodeStringEx function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcopyunicodestringex.md) | The RtlStringCchCopyUnicodeStringEx function copies the contents of a UNICODE_STRING structure to a specified destination. |
| [RtlStringCchCopyW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchcopyw.md) | The RtlStringCchCopyW and RtlStringCchCopyA functions copy a null-terminated source string into a destination buffer of specified length. |
| [RtlStringCchLengthA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchlengtha.md) | The RtlStringCchLengthW and RtlStringCchLengthA functions determine the length, in characters, of a supplied string. |
| [RtlStringCchLengthW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchlengthw.md) | The RtlStringCchLengthW and RtlStringCchLengthA functions determine the length, in characters, of a supplied string. |
| [RtlStringCchPrintfA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchprintfa.md) | The RtlStringCchPrintfW and RtlStringCchPrintfA functions create a character-counted text string, with formatting that is based on supplied formatting information. |
| [RtlStringCchPrintfExA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchprintfexa.md) | The RtlStringCchPrintfExW and RtlStringCchPrintfExA functions create a character-counted text string, with formatting that is based on supplied formatting information. |
| [RtlStringCchPrintfExW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchprintfexw.md) | The RtlStringCchPrintfExW and RtlStringCchPrintfExA functions create a character-counted text string, with formatting that is based on supplied formatting information. |
| [RtlStringCchPrintfW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchprintfw.md) | The RtlStringCchPrintfW and RtlStringCchPrintfA functions create a character-counted text string, with formatting that is based on supplied formatting information. |
| [RtlStringCchVPrintfA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchvprintfa.md) | The RtlStringCchVPrintfW and RtlStringCchVPrintfA functions create a character-counted text string, with formatting that is based on supplied formatting information. |
| [RtlStringCchVPrintfExA function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchvprintfexa.md) | The RtlStringCchVPrintfExW and RtlStringCchVPrintfExA functions create a character-counted text string, with formatting that is based on supplied formatting information. |
| [RtlStringCchVPrintfExW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchvprintfexw.md) | The RtlStringCchVPrintfExW and RtlStringCchVPrintfExA functions create a character-counted text string, with formatting that is based on supplied formatting information. |
| [RtlStringCchVPrintfW function](..\ntstrsafe\nf-ntstrsafe-rtlstringcchvprintfw.md) | The RtlStringCchVPrintfW and RtlStringCchVPrintfA functions create a character-counted text string, with formatting that is based on supplied formatting information. |
| [RtlStringFromGUID function](..\wdm\nf-wdm-rtlstringfromguid.md) | The RtlStringFromGUID routine converts a given GUID from binary format into a Unicode string. |
| [RtlTestBit function](..\wdm\nf-wdm-rtltestbit.md) | The RtlTestBit routine returns the value of a bit in a bitmap. |
| [RtlTimeFieldsToTime function](..\wdm\nf-wdm-rtltimefieldstotime.md) | The RtlTimeFieldsToTime routine converts TIME_FIELDS information to a system time value. |
| [RtlTimeToTimeFields function](..\wdm\nf-wdm-rtltimetotimefields.md) | The RtlTimeToTimeFields routine converts system time into a TIME_FIELDS structure. |
| [RtlUInt8Add function](..\ntintsafe\nf-ntintsafe-rtluint8add.md) | Adds two values of type UINT8. |
| [RtlUInt8Mult function](..\ntintsafe\nf-ntintsafe-rtluint8mult.md) | Multiplies one value of type UINT8 by another. |
| [RtlUInt8Sub function](..\ntintsafe\nf-ntintsafe-rtluint8sub.md) | The RtlUInt8Sub routine subtracts one value of type UINT8 from another. |
| [RtlUInt8ToChar function](..\ntintsafe\nf-ntintsafe-rtluint8tochar.md) | Converts a value of type UINT8 to a value of type CHAR. |
| [RtlUInt8ToInt8 function](..\ntintsafe\nf-ntintsafe-rtluint8toint8.md) | Converts a value of type UINT8 to a value of type INT8. |
| [RtlUIntAdd function](..\ntintsafe\nf-ntintsafe-rtluintadd.md) | Adds two values of type UINT. |
| [RtlUIntMult function](..\ntintsafe\nf-ntintsafe-rtluintmult.md) | Multiplies one value of type UINT by another. |
| [RtlUIntPtrAdd function](..\ntintsafe\nf-ntintsafe-rtluintptradd.md) | Adds two values of type UINT_PTR. |
| [RtlUIntPtrMult function](..\ntintsafe\nf-ntintsafe-rtluintptrmult.md) | Multiplies one value of type UINT_PTR by another. |
| [RtlUIntPtrSub function](..\ntintsafe\nf-ntintsafe-rtluintptrsub.md) | Subtracts one value of type UINT_PTR from another. |
| [RtlUIntPtrToChar function](..\ntintsafe\nf-ntintsafe-rtluintptrtochar.md) | Converts a value of type UINT_PTR to a value of type CHAR. |
| [RtlUIntPtrToInt function](..\ntintsafe\nf-ntintsafe-rtluintptrtoint.md) | Converts a value of type UINT_PTR to a value of type INT. |
| [RtlUIntPtrToInt16 function](..\ntintsafe\nf-ntintsafe-rtluintptrtoint16.md) | Converts a value of type UINT_PTR to a value of type INT16. |
| [RtlUIntPtrToInt8 function](..\ntintsafe\nf-ntintsafe-rtluintptrtoint8.md) | Converts a value of type UINT_PTR to a value of type INT8. |
| [RtlUIntPtrToIntPtr function](..\ntintsafe\nf-ntintsafe-rtluintptrtointptr.md) | Converts a value of type UINT_PTR to a value of type INT_PTR. |
| [RtlUIntPtrToLong function](..\ntintsafe\nf-ntintsafe-rtluintptrtolong.md) | Converts a value of type UINT_PTR to a value of type LONG. |
| [RtlUIntPtrToLongLong function](..\ntintsafe\nf-ntintsafe-rtluintptrtolonglong.md) | Converts a value of type UINT_PTR to a value of type LONGLONG. |
| [RtlUIntPtrToLongPtr function](..\ntintsafe\nf-ntintsafe-rtluintptrtolongptr.md) | Converts a value of type UINT_PTR to a value of type LONG_PTR. |
| [RtlUIntPtrToShort function](..\ntintsafe\nf-ntintsafe-rtluintptrtoshort.md) | Converts a value of type UINT_PTR to a value of type SHORT. |
| [RtlUIntPtrToUChar function](..\ntintsafe\nf-ntintsafe-rtluintptrtouchar.md) | Converts a value of type UINT_PTR to a value of type UCHAR. |
| [RtlUIntPtrToUInt function](..\ntintsafe\nf-ntintsafe-rtluintptrtouint.md) | Converts a value of type UINT_PTR to a value of type UINT. |
| [RtlUIntPtrToUInt16 function](..\ntintsafe\nf-ntintsafe-rtluintptrtouint16.md) | Converts a value of type UINT_PTR to a value of type UINT16. |
| [RtlUIntPtrToUInt8 function](..\ntintsafe\nf-ntintsafe-rtluintptrtouint8.md) | Converts a value of type UINT_PTR to a value of type UINT8. |
| [RtlUIntPtrToULong function](..\ntintsafe\nf-ntintsafe-rtluintptrtoulong.md) | Converts a value of type UINT_PTR to a value of type LONG. |
| [RtlUIntPtrToUShort function](..\ntintsafe\nf-ntintsafe-rtluintptrtoushort.md) | Converts a value of type UINT_PTR to a value of type USHORT. |
| [RtlUIntSub function](..\ntintsafe\nf-ntintsafe-rtluintsub.md) | Subtracts one value of type UINT from another. |
| [RtlUIntToChar function](..\ntintsafe\nf-ntintsafe-rtluinttochar.md) | Converts a value of type UINT to a value of type CHAR. |
| [RtlUIntToInt function](..\ntintsafe\nf-ntintsafe-rtluinttoint.md) | Converts a value of type UINT to a value of type INT. |
| [RtlUIntToInt8 function](..\ntintsafe\nf-ntintsafe-rtluinttoint8.md) | Converts a value of type UINT to a value of type INT8. |
| [RtlUIntToIntPtr function](..\ntintsafe\nf-ntintsafe-rtluinttointptr.md) | Converts a value of type UINT to a value of type INT_PTR. |
| [RtlUIntToLong function](..\ntintsafe\nf-ntintsafe-rtluinttolong.md) | Converts a value of type UINT to a value of type LONG. |
| [RtlUIntToLongPtr function](..\ntintsafe\nf-ntintsafe-rtluinttolongptr.md) | Converts a value of type UINT to a value of type LONG_PTR. |
| [RtlUIntToShort function](..\ntintsafe\nf-ntintsafe-rtluinttoshort.md) | Converts a value of type UINT to a value of type SHORT. |
| [RtlUIntToUChar function](..\ntintsafe\nf-ntintsafe-rtluinttouchar.md) | Converts a value of type UINT to a value of type UCHAR. |
| [RtlUIntToUInt8 function](..\ntintsafe\nf-ntintsafe-rtluinttouint8.md) | Converts a value of type UINT to a value of type UINT8. |
| [RtlUIntToUShort function](..\ntintsafe\nf-ntintsafe-rtluinttoushort.md) | Converts a value of type UINT to a value of type USHORT. |
| [RtlULongAdd function](..\ntintsafe\nf-ntintsafe-rtlulongadd.md) | Adds two values of type ULONG. |
| [RtlULongLongAdd function](..\ntintsafe\nf-ntintsafe-rtlulonglongadd.md) | Adds two values of type ULONGLONG. |
| [RtlULongLongMult function](..\ntintsafe\nf-ntintsafe-rtlulonglongmult.md) | Multiplies one value of type ULONGLONG by another. |
| [RtlULongLongSub function](..\ntintsafe\nf-ntintsafe-rtlulonglongsub.md) | Subtracts one value of type ULONGLONG from another. |
| [RtlULongLongToChar function](..\ntintsafe\nf-ntintsafe-rtlulonglongtochar.md) | Converts a value of type ULONGLONG to a value of type CHAR. |
| [RtlULongLongToInt function](..\ntintsafe\nf-ntintsafe-rtlulonglongtoint.md) | Converts a value of type ULONGLONG to a value of type INT. |
| [RtlULongLongToInt8 function](..\ntintsafe\nf-ntintsafe-rtlulonglongtoint8.md) | Converts a value of type ULONGLONG to a value of type INT8. |
| [RtlULongLongToLong function](..\ntintsafe\nf-ntintsafe-rtlulonglongtolong.md) | Converts a value of type ULONGLONG to a value of type LONG. |
| [RtlULongLongToLongLong function](..\ntintsafe\nf-ntintsafe-rtlulonglongtolonglong.md) | Converts a value of type ULONGLONG to a value of type LONGLONG. |
| [RtlULongLongToLongPtr function](..\ntintsafe\nf-ntintsafe-rtlulonglongtolongptr.md) | Converts a value of type ULONGLONG to a value of type LONG_PTR. |
| [RtlULongLongToShort function](..\ntintsafe\nf-ntintsafe-rtlulonglongtoshort.md) | Converts a value of type ULONGLONG to a value of type SHORT. |
| [RtlULongLongToUChar function](..\ntintsafe\nf-ntintsafe-rtlulonglongtouchar.md) | Converts a value of type ULONGLONG to a value of type UCHAR. |
| [RtlULongLongToUInt function](..\ntintsafe\nf-ntintsafe-rtlulonglongtouint.md) | Converts a value of type ULONGLONG to a value of type UINT. |
| [RtlULongLongToUInt8 function](..\ntintsafe\nf-ntintsafe-rtlulonglongtouint8.md) | Converts a value of type ULONGLONG to a value of type UINT8. |
| [RtlULongLongToUIntPtr function](..\ntintsafe\nf-ntintsafe-rtlulonglongtouintptr.md) | Converts a value of type ULONGLONG to a value of type UINT_PTR. |
| [RtlULongLongToULong function](..\ntintsafe\nf-ntintsafe-rtlulonglongtoulong.md) | Converts a value of type ULONGLONG to a value of type ULONG. |
| [RtlULongLongToULongPtr function](..\ntintsafe\nf-ntintsafe-rtlulonglongtoulongptr.md) | Converts a value of type ULONGLONG to a value of type ULONG_PTR. |
| [RtlULongLongToUShort function](..\ntintsafe\nf-ntintsafe-rtlulonglongtoushort.md) | Converts a value of type ULONGLONG to a value of type USHORT. |
| [RtlULongMult function](..\ntintsafe\nf-ntintsafe-rtlulongmult.md) | Multiplies one value of type ULONG by another. |
| [RtlULongPtrAdd function](..\ntintsafe\nf-ntintsafe-rtlulongptradd.md) | Adds two values of type ULONG_PTR. |
| [RtlULongPtrMult function](..\ntintsafe\nf-ntintsafe-rtlulongptrmult.md) | Multiplies one value of type ULONG_PTR by another. |
| [RtlULongPtrSub function](..\ntintsafe\nf-ntintsafe-rtlulongptrsub.md) | Subtracts one value of type ULONG_PTR from another. |
| [RtlULongPtrToChar function](..\ntintsafe\nf-ntintsafe-rtlulongptrtochar.md) | Converts a value of type ULONG_PTR to a value of type CHAR. |
| [RtlULongPtrToInt function](..\ntintsafe\nf-ntintsafe-rtlulongptrtoint.md) | Converts a value of type ULONG_PTR to a value of type INT. |
| [RtlULongPtrToInt8 function](..\ntintsafe\nf-ntintsafe-rtlulongptrtoint8.md) | Converts a value of type ULONG_PTR to a value of type INT8. |
| [RtlULongPtrToIntPtr function](..\ntintsafe\nf-ntintsafe-rtlulongptrtointptr.md) | Converts a value of type ULONG_PTR to a value of type INT_PTR. |
| [RtlULongPtrToLong function](..\ntintsafe\nf-ntintsafe-rtlulongptrtolong.md) | Converts a value of type ULONG_PTR to a value of type LONG. |
| [RtlULongPtrToLongLong function](..\ntintsafe\nf-ntintsafe-rtlulongptrtolonglong.md) | Converts a value of type ULONG_PTR to a value of type LONGLONG. |
| [RtlULongPtrToLongPtr function](..\ntintsafe\nf-ntintsafe-rtlulongptrtolongptr.md) | Converts a value of type ULONG_PTR to a value of type LONG_PTR. |
| [RtlULongPtrToShort function](..\ntintsafe\nf-ntintsafe-rtlulongptrtoshort.md) | Converts a value of type ULONG_PTR to a value of type SHORT. |
| [RtlULongPtrToUChar function](..\ntintsafe\nf-ntintsafe-rtlulongptrtouchar.md) | Converts a value of type ULONG_PTR to a value of type UCHAR. |
| [RtlULongPtrToUInt function](..\ntintsafe\nf-ntintsafe-rtlulongptrtouint.md) | Converts a value of type ULONG_PTR to a value of type UINT. |
| [RtlULongPtrToUInt8 function](..\ntintsafe\nf-ntintsafe-rtlulongptrtouint8.md) | Converts a value of type ULONG_PTR to a value of type UINT8. |
| [RtlULongPtrToUIntPtr function](..\ntintsafe\nf-ntintsafe-rtlulongptrtouintptr.md) | Converts a value of type ULONG_PTR to a value of type UINT_PTR. |
| [RtlULongPtrToULong function](..\ntintsafe\nf-ntintsafe-rtlulongptrtoulong.md) | Converts a value of type ULONG_PTR to a value of type ULONG. |
| [RtlULongPtrToUShort function](..\ntintsafe\nf-ntintsafe-rtlulongptrtoushort.md) | Converts a value of type ULONG_PTR to a value of type USHORT. |
| [RtlULongSub function](..\ntintsafe\nf-ntintsafe-rtlulongsub.md) | Subtracts one value of type ULONG from another. |
| [RtlULongToChar function](..\ntintsafe\nf-ntintsafe-rtlulongtochar.md) | Converts a value of type ULONG to a value of type CHAR. |
| [RtlULongToInt function](..\ntintsafe\nf-ntintsafe-rtlulongtoint.md) | Converts a value of type ULONG to a value of type INT. |
| [RtlULongToInt8 function](..\ntintsafe\nf-ntintsafe-rtlulongtoint8.md) | Converts a value of type ULONG to a value of type INT8. |
| [RtlULongToIntPtr function](..\ntintsafe\nf-ntintsafe-rtlulongtointptr.md) | Converts a value of type ULONG to a value of type INT_PTR. |
| [RtlULongToLong function](..\ntintsafe\nf-ntintsafe-rtlulongtolong.md) | Converts a value of type ULONG to a value of type LONG. |
| [RtlULongToLongPtr function](..\ntintsafe\nf-ntintsafe-rtlulongtolongptr.md) | Converts a value of type ULONG to a value of type LONG_PTR. |
| [RtlULongToShort function](..\ntintsafe\nf-ntintsafe-rtlulongtoshort.md) | Converts a value of type ULONG to a value of type SHORT. |
| [RtlULongToUChar function](..\ntintsafe\nf-ntintsafe-rtlulongtouchar.md) | Converts a value of type ULONG to a value of type UCHAR. |
| [RtlULongToUInt function](..\ntintsafe\nf-ntintsafe-rtlulongtouint.md) | Converts a value of type ULONG to a value of type UINT. |
| [RtlULongToUInt8 function](..\ntintsafe\nf-ntintsafe-rtlulongtouint8.md) | Converts a value of type ULONG_PTR to a value of type UINT8. |
| [RtlULongToUIntPtr function](..\ntintsafe\nf-ntintsafe-rtlulongtouintptr.md) | Converts a value of type ULONG_PTR to a value of type UINT_PTR. |
| [RtlULongToUShort function](..\ntintsafe\nf-ntintsafe-rtlulongtoushort.md) | Converts a value of type ULONG to a value of type USHORT. |
| [RtlUShortAdd function](..\ntintsafe\nf-ntintsafe-rtlushortadd.md) | Adds two values of type USHORT. |
| [RtlUShortMult function](..\ntintsafe\nf-ntintsafe-rtlushortmult.md) | Multiplies one value of type USHORT by another. |
| [RtlUShortSub function](..\ntintsafe\nf-ntintsafe-rtlushortsub.md) | Subtracts one value of type USHORT from another. |
| [RtlUShortToChar function](..\ntintsafe\nf-ntintsafe-rtlushorttochar.md) | Converts a value of type USHORT to a value of type CHAR. |
| [RtlUShortToInt8 function](..\ntintsafe\nf-ntintsafe-rtlushorttoint8.md) | Converts a value of type USHORT to a value of type INT8. |
| [RtlUShortToShort function](..\ntintsafe\nf-ntintsafe-rtlushorttoshort.md) | Converts a value of type USHORT to a value of type SHORT. |
| [RtlUShortToUChar function](..\ntintsafe\nf-ntintsafe-rtlushorttouchar.md) | Converts a value of type USHORT to a value of type UCHAR. |
| [RtlUShortToUInt8 function](..\ntintsafe\nf-ntintsafe-rtlushorttouint8.md) | Converts a value of type USHORT to a value of type UINT8. |
| [RtlUTF8ToUnicodeN function](..\ntifs\nf-ntifs-rtlutf8tounicoden.md) | The RtlUTF8ToUnicodeN routine converts a UTF-8 string to a Unicode string. |
| [RtlUTF8ToUnicodeN function](..\wdm\nf-wdm-rtlutf8tounicoden.md) | The RtlUTF8ToUnicodeN routine converts a UTF-8 string to a Unicode string. |
| [RtlUlongByteSwap function](..\wdm\nf-wdm-rtlulongbyteswap.md) | The RtlUlongByteSwap routine reverses the ordering of the four bytes in a 32-bit unsigned integer value. |
| [RtlUlongByteSwap function](..\wdm\nf-wdm-rtlulongbyteswap~r1.md) | The RtlUlongByteSwap routine reverses the ordering of the four bytes in a 32-bit unsigned integer value. |
| [RtlUlonglongByteSwap function](..\wdm\nf-wdm-rtlulonglongbyteswap.md) | The RtlUlonglongByteSwap routine reverses the ordering of the eight bytes in a 64-bit unsigned integer value. |
| [RtlUlonglongByteSwap function](..\wdm\nf-wdm-rtlulonglongbyteswap~r1.md) | The RtlUlonglongByteSwap routine reverses the ordering of the eight bytes in a 64-bit unsigned integer value. |
| [RtlUnalignedStringCbLengthW function](..\ntstrsafe\nf-ntstrsafe-rtlunalignedstringcblengthw.md) | The RtlUnalignedStringCbLengthW function is a version of the RtlStringCbLength function that accepts an unaligned pointer to a string of Unicode characters. |
| [RtlUnalignedStringCchLengthW function](..\ntstrsafe\nf-ntstrsafe-rtlunalignedstringcchlengthw.md) | The RtlUnalignedStringCchLengthW function is a version of the RtlStringCchLength function that accepts an unaligned pointer to a string of Unicode characters. |
| [RtlUnicodeStringCat function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcat.md) | The RtlUnicodeStringCat function concatenates two strings that are contained in UNICODE_STRING structures. |
| [RtlUnicodeStringCatEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcatex.md) | The RtlUnicodeStringCatEx function concatenates two strings that are contained in UNICODE_STRING structures. |
| [RtlUnicodeStringCatString function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcatstring.md) | The RtlUnicodeStringCatString function concatenates two strings when the destination string is contained in a UNICODE_STRING structure. |
| [RtlUnicodeStringCatStringEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcatstringex.md) | The RtlUnicodeStringCatStringEx function concatenates two strings when the destination string is contained in a UNICODE_STRING structure. |
| [RtlUnicodeStringCbCatN function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcbcatn.md) | The RtlUnicodeStringCbCatN function concatenates two strings that are contained in UNICODE_STRING structures while limiting the size of the copied string. |
| [RtlUnicodeStringCbCatNEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcbcatnex.md) | The RtlUnicodeStringCbCatNEx function concatenates two strings that are contained in UNICODE_STRING structures while limiting the size of the copied string. |
| [RtlUnicodeStringCbCatStringN function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcbcatstringn.md) | The RtlUnicodeStringCbCatStringN function concatenates two strings when the destination string is contained in a UNICODE_STRING structure, while limiting the size of the appended string. |
| [RtlUnicodeStringCbCatStringNEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcbcatstringnex.md) | The RtlUnicodeStringCbCatStringNEx function concatenates two strings when the destination string is contained in a UNICODE_STRING structure, while limiting the size of the appended string. |
| [RtlUnicodeStringCbCopyN function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcbcopyn.md) | The RtlUnicodeStringCbCopyN function copies a string from one UNICODE_STRING structure to another while limiting the size of the copied string. |
| [RtlUnicodeStringCbCopyNEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcbcopynex.md) | The RtlUnicodeStringCbCopyNEx function copies a string from one UNICODE_STRING structure to another while limiting the size of the copied string. |
| [RtlUnicodeStringCbCopyStringN function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcbcopystringn.md) | The RtlUnicodeStringCbCopyStringN function copies a string into a UNICODE_STRING structure while limiting the size of the copied string. |
| [RtlUnicodeStringCbCopyStringNEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcbcopystringnex.md) | The RtlUnicodeStringCbCopyStringNEx function copies a string into a UNICODE_STRING structure while limiting the size of the copied string. |
| [RtlUnicodeStringCchCatN function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcchcatn.md) | The RtlUnicodeStringCchCatN function concatenates two strings that are contained in UNICODE_STRING structures while limiting the size of the copied string. |
| [RtlUnicodeStringCchCatNEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcchcatnex.md) | The RtlUnicodeStringCchCatNEx function concatenates two strings that are contained in UNICODE_STRING structures while limiting the size of the copied string. |
| [RtlUnicodeStringCchCatStringN function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcchcatstringn.md) | The RtlUnicodeStringCchCatStringN function concatenates two strings when the destination string is contained in a UNICODE_STRING structure, while limiting the size of the appended string. |
| [RtlUnicodeStringCchCatStringNEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcchcatstringnex.md) | The RtlUnicodeStringCchCatStringNEx function concatenates two strings when the destination string is contained in a UNICODE_STRING structure, while limiting the size of the appended string. |
| [RtlUnicodeStringCchCopyN function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcchcopyn.md) | The RtlUnicodeStringCchCopyN function copies a string from one UNICODE_STRING structure to another while limiting the size of the copied string. |
| [RtlUnicodeStringCchCopyNEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcchcopynex.md) | The RtlUnicodeStringCchCopyNEx function copies a string from one UNICODE_STRING structure to another while limiting the size of the copied string. |
| [RtlUnicodeStringCchCopyStringN function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcchcopystringn.md) | The RtlUnicodeStringCchCopyStringN function copies a string into a UNICODE_STRING structure while limiting the size of the copied string. |
| [RtlUnicodeStringCchCopyStringNEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcchcopystringnex.md) | The RtlUnicodeStringCchCopyStringNEx function copies a string into a UNICODE_STRING structure while limiting the size of the copied string. |
| [RtlUnicodeStringCopy function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcopy.md) | The RtlUnicodeStringCopy function copies a string from one UNICODE_STRING structure to another. |
| [RtlUnicodeStringCopyEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcopyex.md) | The RtlUnicodeStringCopyEx function copies a string from one UNICODE_STRING structure to another. |
| [RtlUnicodeStringCopyString function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcopystring.md) | The RtlUnicodeStringCopyString function copies a string into a UNICODE_STRING structure. |
| [RtlUnicodeStringCopyStringEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringcopystringex.md) | The RtlUnicodeStringCopyStringEx function copies a string into a UNICODE_STRING structure. |
| [RtlUnicodeStringInit function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringinit.md) | The RtlUnicodeStringInit function initializes a UNICODE_STRING structure. |
| [RtlUnicodeStringInitEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringinitex.md) | The RtlUnicodeStringInitEx function initializes a UNICODE_STRING structure. |
| [RtlUnicodeStringPrintf function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringprintf.md) | The RtlUnicodeStringPrintf function creates a text string, with formatting that is based on supplied formatting information, and stores the string in a UNICODE_STRING structure. |
| [RtlUnicodeStringPrintfEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringprintfex.md) | The RtlUnicodeStringPrintfEx function creates a text string, with formatting that is based on supplied formatting information, and stores the string in a UNICODE_STRING structure. |
| [RtlUnicodeStringToAnsiSize function](..\wdm\nf-wdm-rtlunicodestringtoansisize.md) | The RtlUnicodeStringToAnsiSize routine returns the number of bytes required for a null-terminated ANSI string that is equivalent to a specified Unicode string. |
| [RtlUnicodeStringToAnsiString function](..\wdm\nf-wdm-rtlunicodestringtoansistring.md) | The RtlUnicodeStringToAnsiString routine converts a given Unicode string into an ANSI string. |
| [RtlUnicodeStringToInteger function](..\wdm\nf-wdm-rtlunicodestringtointeger.md) | The RtlUnicodeStringToInteger routine converts a Unicode string representation of a number to the equivalent integer value. |
| [RtlUnicodeStringVPrintf function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringvprintf.md) | The RtlUnicodeStringVPrintf function creates a text string, with formatting that is based on supplied formatting information, and stores the string in a UNICODE_STRING structure. |
| [RtlUnicodeStringVPrintfEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringvprintfex.md) | The RtlUnicodeStringVPrintfEx function creates a text string, with formatting that is based on supplied formatting information, and stores the string in a UNICODE_STRING structure. |
| [RtlUnicodeStringValidate function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringvalidate.md) | The RtlUnicodeStringValidate function validates the contents of a UNICODE_STRING structure. |
| [RtlUnicodeStringValidateEx function](..\ntstrsafe\nf-ntstrsafe-rtlunicodestringvalidateex.md) | The RtlUnicodeStringValidateEx function validates the contents of a UNICODE_STRING structure. |
| [RtlUnicodeToUTF8N function](..\ntifs\nf-ntifs-rtlunicodetoutf8n.md) | The RtlUnicodeToUTF8N routine converts a Unicode string to a UTF-8 string. |
| [RtlUnicodeToUTF8N function](..\wdm\nf-wdm-rtlunicodetoutf8n.md) | The RtlUnicodeToUTF8N routine converts a Unicode string to a UTF-8 string. |
| [RtlUpcaseUnicodeChar function](..\wdm\nf-wdm-rtlupcaseunicodechar.md) | The RtlUpcaseUnicodeChar routine converts the specified Unicode character to uppercase. |
| [RtlUpcaseUnicodeString function](..\ntddk\nf-ntddk-rtlupcaseunicodestring.md) | The RtlUpcaseUnicodeString routine converts a copy of the source string to uppercase and writes the converted string in the destination buffer. |
| [RtlUpperChar function](..\ntddk\nf-ntddk-rtlupperchar.md) | The RtlUpperChar routine converts the specified character to uppercase. |
| [RtlUpperString function](..\ntddk\nf-ntddk-rtlupperstring.md) | The RtlUpperString routine copies the given SourceString to the DestinationString buffer, converting it to uppercase. |
| [RtlUshortByteSwap function](..\wdm\nf-wdm-rtlushortbyteswap.md) | The RtlUshortByteSwap routine reverses the ordering of the two bytes in a 16-bit unsigned integer value. |
| [RtlUshortByteSwap function](..\wdm\nf-wdm-rtlushortbyteswap~r1.md) | The RtlUshortByteSwap routine reverses the ordering of the two bytes in a 16-bit unsigned integer value. |
| [RtlValidRelativeSecurityDescriptor function](..\wdm\nf-wdm-rtlvalidrelativesecuritydescriptor.md) | The RtlValidRelativeSecurityDescriptor routine checks the validity of a self-relative security descriptor. |
| [RtlValidSecurityDescriptor function](..\wdm\nf-wdm-rtlvalidsecuritydescriptor.md) | The RtlValidSecurityDescriptor routine checks a given security descriptor's validity. |
| [RtlValidateCorrelationVector function](..\ntddk\nf-ntddk-rtlvalidatecorrelationvector.md) | Validates the specified correlation vector to check whether it conforms to the Correlation Vector Specification (v2). |
| [RtlVerifyVersionInfo function](..\wdm\nf-wdm-rtlverifyversioninfo.md) | The RtlVerifyVersionInfo routine compares a specified set of operating system version requirements to the corresponding attributes of the currently running version of the operating system. |
| [RtlVolumeDeviceToDosName function](..\ntddk\nf-ntddk-rtlvolumedevicetodosname.md) | The RtlVolumeDeviceToDosName routine is obsolete for Windows XP and later versions of Windows. Use IoVolumeDeviceToDosName instead.RtlVolumeDeviceToDosName returns the MS-DOS path for a specified device object that represents a file system volume. |
| [RtlWriteRegistryValue function](..\wdm\nf-wdm-rtlwriteregistryvalue.md) | The RtlWriteRegistryValue routine writes caller-supplied data into the registry along the specified relative path at the given value name. |
| [RtlZeroMemory function](..\wdm\nf-wdm-rtlzeromemory.md) | The RtlZeroMemory routine fills a block of memory with zeros, given a pointer to the block and the length, in bytes, to be filled. |
| [RtlxAnsiStringToUnicodeSize function](..\wdm\nf-wdm-rtlxansistringtounicodesize.md) | The RtlxAnsiStringToUnicodeSize routine returns the number of bytes that are required for a null-terminated Unicode string that is equivalent to a specified ANSI string. |
| [RtlxUnicodeStringToAnsiSize function](..\wdm\nf-wdm-rtlxunicodestringtoansisize.md) | The RtlxUnicodeStringToAnsiSize routine returns the number of bytes required for a null-terminated ANSI string that is equivalent to a specified Unicode string. |
| [SeAccessCheck function](..\wdm\nf-wdm-seaccesscheck.md) | The SeAccessCheck routine determines whether the requested access rights can be granted to an object protected by a security descriptor and an object owner. |
| [SeAssignSecurity function](..\wdm\nf-wdm-seassignsecurity.md) | The SeAssignSecurity routine builds a self-relative security descriptor for a new object, given the security descriptor of its parent directory and any originally requested security for the object. |
| [SeAssignSecurityEx function](..\wdm\nf-wdm-seassignsecurityex.md) | The SeAssignSecurityEx routine builds a self-relative security descriptor for a new object given the following optional parameters |
| [SeDeassignSecurity function](..\wdm\nf-wdm-sedeassignsecurity.md) | The SeDeassignSecurity routine deallocates the memory associated with a security descriptor that was assigned using SeAssignSecurity. |
| [SeFreePrivileges function](..\ntifs\nf-ntifs-sefreeprivileges.md) | The SeFreePrivileges routine frees a privilege set returned by SeAccessCheck. |
| [SeSinglePrivilegeCheck function](..\ntddk\nf-ntddk-sesingleprivilegecheck.md) | The SeSinglePrivilegeCheck routine checks for the passed privilege value in the context of the current thread. |
| [SeValidSecurityDescriptor function](..\wdm\nf-wdm-sevalidsecuritydescriptor.md) | The SeValidSecurityDescriptor routine returns whether a given security descriptor is structurally valid. |
| [TmCommitComplete function](..\wdm\nf-wdm-tmcommitcomplete.md) | The TmCommitComplete routine notifies KTM that the calling resource manager has finished committing a transaction. |
| [TmCommitEnlistment function](..\wdm\nf-wdm-tmcommitenlistment.md) | The TmCommitEnlistment routine initiates the commit operation for a specified enlistment's transaction. |
| [TmCommitTransaction function](..\wdm\nf-wdm-tmcommittransaction.md) | The TmCommitTransaction routine initiates a commit operation for a specified transaction. |
| [TmCreateEnlistment function](..\wdm\nf-wdm-tmcreateenlistment.md) | The TmCreateEnlistment routine creates a new enlistment object for a transaction. |
| [TmDereferenceEnlistmentKey function](..\wdm\nf-wdm-tmdereferenceenlistmentkey.md) | The TmDereferenceEnlistmentKey routine decrements the reference count for the key of a specified enlistment object. |
| [TmEnableCallbacks function](..\wdm\nf-wdm-tmenablecallbacks.md) | The TmEnableCallbacks routine enables a callback routine that receives transaction notifications. |
| [TmGetTransactionId function](..\wdm\nf-wdm-tmgettransactionid.md) | The TmGetTransactionId routine retrieves a transaction object's unit of work (UOW) identifier. |
| [TmInitializeTransactionManager function](..\wdm\nf-wdm-tminitializetransactionmanager.md) | The TmInitializeTransactionManager routine initializes a transaction manager object. |
| [TmIsTransactionActive function](..\wdm\nf-wdm-tmistransactionactive.md) | The TmIsTransactionActive routine indicates whether a specified transaction is in its active state. |
| [TmPrePrepareComplete function](..\wdm\nf-wdm-tmprepreparecomplete.md) | The TmPrePrepareComplete routine notifies KTM that the calling resource manager has finished preliminary preparation of a transaction's data. |
| [TmPrePrepareEnlistment function](..\wdm\nf-wdm-tmpreprepareenlistment.md) | The TmPrePrepareEnlistment routine initiates the pre-prepare operation for a specified enlistment's transaction. |
| [TmPrepareComplete function](..\wdm\nf-wdm-tmpreparecomplete.md) | The TmPrepareComplete routine notifies KTM that the calling resource manager has finished preparing a transaction's data. |
| [TmPrepareEnlistment function](..\wdm\nf-wdm-tmprepareenlistment.md) | The TmPrepareEnlistment routine initiates the prepare operation for a specified enlistment's transaction. |
| [TmReadOnlyEnlistment function](..\wdm\nf-wdm-tmreadonlyenlistment.md) | The TmReadOnlyEnlistment routine sets a specified enlistment to be read-only. |
| [TmRecoverEnlistment function](..\wdm\nf-wdm-tmrecoverenlistment.md) | The TmRecoverEnlistment routine initiates a recovery operation for the transaction that is associated with a specified enlistment. |
| [TmRecoverResourceManager function](..\wdm\nf-wdm-tmrecoverresourcemanager.md) | The TmRecoverResourceManager routine tries to recover the transaction that is associated with each enlistment of a specified resource manager object. |
| [TmRecoverTransactionManager function](..\wdm\nf-wdm-tmrecovertransactionmanager.md) | The TmRecoverTransactionManager routine reconstructs the state of the transaction manager object (including all transactions, enlistments, and resource managers) from the recovery information that is in the log stream. |
| [TmReferenceEnlistmentKey function](..\wdm\nf-wdm-tmreferenceenlistmentkey.md) | The TmReferenceEnlistmentKey routine increments the reference count for the key of a specified enlistment object and retrieves the key. |
| [TmRenameTransactionManager function](..\wdm\nf-wdm-tmrenametransactionmanager.md) | The TmRenameTransactionManager routine changes the identity of the transaction manager object that is stored in the CLFS log file stream contained in the log file name. |
| [TmRequestOutcomeEnlistment function](..\wdm\nf-wdm-tmrequestoutcomeenlistment.md) | The TmRequestOutcomeEnlistment routine asks KTM to try to provide an immediate outcome (commit or rollback) for the transaction that is associated with a specified enlistment. |
| [TmRollbackComplete function](..\wdm\nf-wdm-tmrollbackcomplete.md) | The TmRollbackComplete routine notifies KTM that the calling resource manager has finished rolling back a transaction's data. |
| [TmRollbackEnlistment function](..\wdm\nf-wdm-tmrollbackenlistment.md) | The TmRollbackEnlistment routine rolls back a specified enlistment. |
| [TmRollbackTransaction function](..\wdm\nf-wdm-tmrollbacktransaction.md) | The TmRollbackTransaction routine initiates a rollback operation for a specified transaction. |
| [TmSinglePhaseReject function](..\wdm\nf-wdm-tmsinglephasereject.md) | The TmSinglePhaseReject routine informs KTM that the calling resource manager will not support a single-phase commit operation for a specified enlistment. |
| [WRITE_PORT_BUFFER_UCHAR function](..\wdm\nf-wdm-write-port-buffer-uchar.md) | The WRITE_PORT_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified port. |
| [WRITE_PORT_BUFFER_UCHAR function](..\wdm\nf-wdm-write-port-buffer-uchar~r1.md) | The WRITE_PORT_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified port. |
| [WRITE_PORT_BUFFER_UCHAR function](..\wdm\nf-wdm-write-port-buffer-uchar~r2.md) | The WRITE_PORT_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified port. |
| [WRITE_PORT_BUFFER_UCHAR function](..\wdm\nf-wdm-write-port-buffer-uchar~r3.md) | The WRITE_PORT_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified port. |
| [WRITE_PORT_BUFFER_ULONG function](..\wdm\nf-wdm-write-port-buffer-ulong.md) | The WRITE_PORT_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified port address. |
| [WRITE_PORT_BUFFER_ULONG function](..\wdm\nf-wdm-write-port-buffer-ulong~r1.md) | The WRITE_PORT_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified port address. |
| [WRITE_PORT_BUFFER_ULONG function](..\wdm\nf-wdm-write-port-buffer-ulong~r2.md) | The WRITE_PORT_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified port address. |
| [WRITE_PORT_BUFFER_ULONG function](..\wdm\nf-wdm-write-port-buffer-ulong~r3.md) | The WRITE_PORT_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified port address. |
| [WRITE_PORT_BUFFER_USHORT function](..\wdm\nf-wdm-write-port-buffer-ushort.md) | The WRITE_PORT_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified port address. |
| [WRITE_PORT_BUFFER_USHORT function](..\wdm\nf-wdm-write-port-buffer-ushort~r1.md) | The WRITE_PORT_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified port address. |
| [WRITE_PORT_BUFFER_USHORT function](..\wdm\nf-wdm-write-port-buffer-ushort~r2.md) | The WRITE_PORT_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified port address. |
| [WRITE_PORT_BUFFER_USHORT function](..\wdm\nf-wdm-write-port-buffer-ushort~r3.md) | The WRITE_PORT_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified port address. |
| [WRITE_PORT_UCHAR function](..\wdm\nf-wdm-write-port-uchar.md) | The WRITE_PORT_UCHAR routine writes a byte to the specified port address. |
| [WRITE_PORT_UCHAR function](..\wdm\nf-wdm-write-port-uchar~r1.md) | The WRITE_PORT_UCHAR routine writes a byte to the specified port address. |
| [WRITE_PORT_UCHAR function](..\wdm\nf-wdm-write-port-uchar~r2.md) | The WRITE_PORT_UCHAR routine writes a byte to the specified port address. |
| [WRITE_PORT_UCHAR function](..\wdm\nf-wdm-write-port-uchar~r3.md) | The WRITE_PORT_UCHAR routine writes a byte to the specified port address. |
| [WRITE_PORT_ULONG function](..\wdm\nf-wdm-write-port-ulong.md) | The WRITE_PORT_ULONG routine writes a ULONG value to the specified port address. |
| [WRITE_PORT_ULONG function](..\wdm\nf-wdm-write-port-ulong~r1.md) | The WRITE_PORT_ULONG routine writes a ULONG value to the specified port address. |
| [WRITE_PORT_ULONG function](..\wdm\nf-wdm-write-port-ulong~r2.md) | The WRITE_PORT_ULONG routine writes a ULONG value to the specified port address. |
| [WRITE_PORT_ULONG function](..\wdm\nf-wdm-write-port-ulong~r3.md) | The WRITE_PORT_ULONG routine writes a ULONG value to the specified port address. |
| [WRITE_PORT_USHORT function](..\wdm\nf-wdm-write-port-ushort.md) | The WRITE_PORT_USHORT routine writes a USHORT value to the specified port address. |
| [WRITE_PORT_USHORT function](..\wdm\nf-wdm-write-port-ushort~r1.md) | The WRITE_PORT_USHORT routine writes a USHORT value to the specified port address. |
| [WRITE_PORT_USHORT function](..\wdm\nf-wdm-write-port-ushort~r2.md) | The WRITE_PORT_USHORT routine writes a USHORT value to the specified port address. |
| [WRITE_PORT_USHORT function](..\wdm\nf-wdm-write-port-ushort~r3.md) | The WRITE_PORT_USHORT routine writes a USHORT value to the specified port address. |
| [WRITE_REGISTER_BUFFER_UCHAR function](..\wdm\nf-wdm-write-register-buffer-uchar.md) | The WRITE_REGISTER_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified register. |
| [WRITE_REGISTER_BUFFER_UCHAR function](..\wdm\nf-wdm-write-register-buffer-uchar~r1.md) | The WRITE_REGISTER_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified register. |
| [WRITE_REGISTER_BUFFER_UCHAR function](..\wdm\nf-wdm-write-register-buffer-uchar~r2.md) | The WRITE_REGISTER_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified register. |
| [WRITE_REGISTER_BUFFER_UCHAR function](..\wdm\nf-wdm-write-register-buffer-uchar~r3.md) | The WRITE_REGISTER_BUFFER_UCHAR routine writes a number of bytes from a buffer to the specified register. |
| [WRITE_REGISTER_BUFFER_ULONG function](..\wdm\nf-wdm-write-register-buffer-ulong.md) | The WRITE_REGISTER_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified register. |
| [WRITE_REGISTER_BUFFER_ULONG function](..\wdm\nf-wdm-write-register-buffer-ulong~r1.md) | The WRITE_REGISTER_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified register. |
| [WRITE_REGISTER_BUFFER_ULONG function](..\wdm\nf-wdm-write-register-buffer-ulong~r2.md) | The WRITE_REGISTER_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified register. |
| [WRITE_REGISTER_BUFFER_ULONG function](..\wdm\nf-wdm-write-register-buffer-ulong~r3.md) | The WRITE_REGISTER_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified register. |
| [WRITE_REGISTER_BUFFER_USHORT function](..\wdm\nf-wdm-write-register-buffer-ushort.md) | The WRITE_REGISTER_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified register. |
| [WRITE_REGISTER_BUFFER_USHORT function](..\wdm\nf-wdm-write-register-buffer-ushort~r1.md) | The WRITE_REGISTER_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified register. |
| [WRITE_REGISTER_BUFFER_USHORT function](..\wdm\nf-wdm-write-register-buffer-ushort~r2.md) | The WRITE_REGISTER_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified register. |
| [WRITE_REGISTER_BUFFER_USHORT function](..\wdm\nf-wdm-write-register-buffer-ushort~r3.md) | The WRITE_REGISTER_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified register. |
| [WRITE_REGISTER_UCHAR function](..\wdm\nf-wdm-write-register-uchar.md) | The WRITE_REGISTER_UCHAR routine writes a byte to the specified address. |
| [WRITE_REGISTER_UCHAR function](..\wdm\nf-wdm-write-register-uchar~r1.md) | The WRITE_REGISTER_UCHAR routine writes a byte to the specified address. |
| [WRITE_REGISTER_UCHAR function](..\wdm\nf-wdm-write-register-uchar~r2.md) | The WRITE_REGISTER_UCHAR routine writes a byte to the specified address. |
| [WRITE_REGISTER_UCHAR function](..\wdm\nf-wdm-write-register-uchar~r3.md) | The WRITE_REGISTER_UCHAR routine writes a byte to the specified address. |
| [WRITE_REGISTER_ULONG function](..\wdm\nf-wdm-write-register-ulong.md) | The WRITE_REGISTER_ULONG routine writes a ULONG value to the specified address. |
| [WRITE_REGISTER_ULONG function](..\wdm\nf-wdm-write-register-ulong~r1.md) | The WRITE_REGISTER_ULONG routine writes a ULONG value to the specified address. |
| [WRITE_REGISTER_ULONG function](..\wdm\nf-wdm-write-register-ulong~r2.md) | The WRITE_REGISTER_ULONG routine writes a ULONG value to the specified address. |
| [WRITE_REGISTER_ULONG function](..\wdm\nf-wdm-write-register-ulong~r3.md) | The WRITE_REGISTER_ULONG routine writes a ULONG value to the specified address. |
| [WRITE_REGISTER_USHORT function](..\wdm\nf-wdm-write-register-ushort.md) | The WRITE_REGISTER_USHORT routine writes a USHORT value to the specified address. |
| [WRITE_REGISTER_USHORT function](..\wdm\nf-wdm-write-register-ushort~r1.md) | The WRITE_REGISTER_USHORT routine writes a USHORT value to the specified address. |
| [WRITE_REGISTER_USHORT function](..\wdm\nf-wdm-write-register-ushort~r2.md) | The WRITE_REGISTER_USHORT routine writes a USHORT value to the specified address. |
| [WRITE_REGISTER_USHORT function](..\wdm\nf-wdm-write-register-ushort~r3.md) | The WRITE_REGISTER_USHORT routine writes a USHORT value to the specified address. |
| [WdmlibIoConnectInterruptEx function](..\iointex\nf-iointex-wdmlibioconnectinterruptex.md) | The WdmlibIoConnectInterruptEx function registers an interrupt-handling routine for a device's interrupts. |
| [WdmlibIoCreateDeviceSecure function](..\wdmsec\nf-wdmsec-wdmlibiocreatedevicesecure.md) | The WdmlibIoCreateDeviceSecure function creates a named device object and applies the specified security settings. |
| [WdmlibIoDisconnectInterruptEx function](..\iointex\nf-iointex-wdmlibiodisconnectinterruptex.md) | The WdmlibIoDisconnectInterruptEx function unregisters an interrupt service routine (ISR) that was registered by a previous call to the WdmlibIoConnectInterruptEx function. |
| [WdmlibIoGetAffinityInterrupt function](..\iointex\nf-iointex-wdmlibiogetaffinityinterrupt.md) | The WdmlibIoGetAffinityInterrupt function gets the group affinity of an interrupt object. |
| [WdmlibIoValidateDeviceIoControlAccess function](..\wdmsec\nf-wdmsec-wdmlibiovalidatedeviceiocontrolaccess.md) | The WdmlibIoValidateDeviceIoControlAccess function verifies that the sender of an IRP_MJ_DEVICE_CONTROL or IRP_MJ_FILE_SYSTEM_CONTROL IRP has the specified access to the device object. |
| [WdmlibProcgrpInitialize function](..\procgrp\nf-procgrp-wdmlibprocgrpinitialize.md) | The WdmlibProcgrpInitialize function initializes the Processor Group (ProcGrp) compatibility library. |
| [WdmlibRtlInitUnicodeStringEx function](..\wdmsec\nf-wdmsec-wdmlibrtlinitunicodestringex.md) | The WdmlibRtlInitUnicodeStringEx function initializes a counted string of Unicode characters. |
| [WmiCompleteRequest function](..\wmilib\nf-wmilib-wmicompleterequest.md) | The WmiCompleteRequest routine indicates that a driver has finished processing a WMI request in a DpWmiXxx routine. |
| [WmiFireEvent function](..\wmilib\nf-wmilib-wmifireevent.md) | The WmiFireEvent routine sends an event to WMI for delivery to data consumers that have requested notification of the event. |
| [WmiQueryTraceInformation function](..\wdm\nf-wdm-wmiquerytraceinformation.md) | The WmiQueryTraceInformation routine returns information about a WMI event trace. |
| [WmiSystemControl function](..\wmilib\nf-wmilib-wmisystemcontrol.md) | The WmiSystemControl routine is a dispatch routine for drivers that use WMI library support routines to handle WMI IRPs. |
| [WmiTraceMessage function](..\wdm\nf-wdm-wmitracemessage.md) | The WmiTraceMessage routine adds a message to the output log of a WPP software tracing session. |
| [WmiTraceMessageVa function](..\wdm\nf-wdm-wmitracemessageva.md) | The WmiTraceMessageVa routine adds a message to the output log of a WPP software tracing session. |
| [ZwAllocateLocallyUniqueId function](..\ntddk\nf-ntddk-zwallocatelocallyuniqueid.md) | The ZwAllocateLocallyUniqueId routine allocates a locally unique identifier (LUID). |
| [ZwAllocateVirtualMemory function](..\ntifs\nf-ntifs-zwallocatevirtualmemory.md) | The ZwAllocateVirtualMemory routine reserves, commits, or both, a region of pages within the user-mode virtual address space of a specified process. |
| [ZwClose function](..\wdm\nf-wdm-zwclose.md) | The ZwClose routine closes an object handle. |
| [ZwCommitComplete function](..\wdm\nf-wdm-zwcommitcomplete.md) | The ZwCommitComplete routine notifies KTM that the calling resource manager has finished committing a transaction's data. |
| [ZwCommitEnlistment function](..\wdm\nf-wdm-zwcommitenlistment.md) | The ZwCommitEnlistment routine initiates the commit operation for a specified enlistment's transaction. |
| [ZwCommitTransaction function](..\wdm\nf-wdm-zwcommittransaction.md) | The ZwCommitTransaction routine initiates a commit operation for a specified transaction. |
| [ZwCreateDirectoryObject function](..\wdm\nf-wdm-zwcreatedirectoryobject.md) | The ZwCreateDirectoryObject routine creates or opens an object-directory object. |
| [ZwCreateEnlistment function](..\wdm\nf-wdm-zwcreateenlistment.md) | The ZwCreateEnlistment routine creates a new enlistment object for a transaction. |
| [ZwCreateEvent function](..\ntifs\nf-ntifs-zwcreateevent.md) | The ZwCreateEvent routine creates an event object, sets the initial state of the event to the specified value, and opens a handle to the object with the specified desired access. |
| [ZwCreateFile function](..\wdm\nf-wdm-zwcreatefile.md) | The ZwCreateFile routine creates a new file or opens an existing file. |
| [ZwCreateKey function](..\wdm\nf-wdm-zwcreatekey.md) | The ZwCreateKey routine creates a new registry key or opens an existing one. |
| [ZwCreateKeyTransacted function](..\wdm\nf-wdm-zwcreatekeytransacted.md) | The ZwCreateKeyTransacted routine creates a new registry key or opens an existing one, and it associates the key with a transaction. |
| [ZwCreateResourceManager function](..\wdm\nf-wdm-zwcreateresourcemanager.md) | The ZwCreateResourceManager routine creates a resource manager object. |
| [ZwCreateSection function](..\wdm\nf-wdm-zwcreatesection.md) | The ZwCreateSection routine creates a section object. |
| [ZwCreateTransaction function](..\wdm\nf-wdm-zwcreatetransaction.md) | The ZwCreateTransaction routine creates a transaction object. |
| [ZwCreateTransactionManager function](..\wdm\nf-wdm-zwcreatetransactionmanager.md) | The ZwCreateTransactionManager routine creates a new transaction manager object. |
| [ZwDeleteFile function](..\ntifs\nf-ntifs-zwdeletefile.md) | The ZwDeleteFile routine deletes the specified file. |
| [ZwDeleteKey function](..\wdm\nf-wdm-zwdeletekey.md) | The ZwDeleteKey routine deletes an open key from the registry. |
| [ZwDeleteValueKey function](..\wdm\nf-wdm-zwdeletevaluekey.md) | The ZwDeleteValueKey routine deletes a value entry matching a name from an open key in the registry. If no such entry exists, an error is returned. |
| [ZwDeviceIoControlFile function](..\ntifs\nf-ntifs-zwdeviceiocontrolfile.md) | The ZwDeviceIoControlFile routine sends a control code directly to a specified device driver, causing the corresponding driver to perform the specified operation. |
| [ZwDuplicateObject function](..\ntifs\nf-ntifs-zwduplicateobject.md) | The ZwDuplicateObject routine creates a handle that is a duplicate of the specified source handle. |
| [ZwDuplicateToken function](..\ntifs\nf-ntifs-zwduplicatetoken.md) | The ZwDuplicateToken function creates a handle to a new access token that duplicates an existing token. This function can create either a primary token or an impersonation token. |
| [ZwEnumerateKey function](..\wdm\nf-wdm-zwenumeratekey.md) | The ZwEnumerateKey routine returns information about a subkey of an open registry key. |
| [ZwEnumerateTransactionObject function](..\wdm\nf-wdm-zwenumeratetransactionobject.md) | The ZwEnumerateTransactionObject routine enumerates the KTM objects on a computer. |
| [ZwEnumerateValueKey function](..\wdm\nf-wdm-zwenumeratevaluekey.md) | The ZwEnumerateValueKey routine gets information about the value entries of an open key. |
| [ZwFlushBuffersFile function](..\ntifs\nf-ntifs-zwflushbuffersfile.md) | The ZwFlushBuffersFile routine is called by a file system filter driver to send a flush request for the specified file to the file system. |
| [ZwFlushBuffersFileEx function](..\ntifs\nf-ntifs-zwflushbuffersfileex.md) | The ZwFlushBuffersFileEx routine is called by a file system filter driver to send a flush request for a given file to the file system. An optional flush operation flag can be set to control how file data is written to storage. |
| [ZwFlushKey function](..\wdm\nf-wdm-zwflushkey.md) | The ZwFlushKey routine forces a registry key to be committed to disk. |
| [ZwFlushVirtualMemory function](..\ntifs\nf-ntifs-zwflushvirtualmemory.md) | The ZwFlushVirtualMemory routine flushes a range of virtual addresses within the virtual address space of a specified process which map to a data file back out to the data file if they have been modified. |
| [ZwFreeVirtualMemory function](..\ntifs\nf-ntifs-zwfreevirtualmemory.md) | The ZwFreeVirtualMemory routine releases, decommits, or both, a region of pages within the virtual address space of a specified process. |
| [ZwFsControlFile function](..\ntifs\nf-ntifs-zwfscontrolfile.md) | The ZwFsControlFile routine sends a control code directly to a specified file system or file system filter driver, causing the corresponding driver to perform the specified action. |
| [ZwGetNotificationResourceManager function](..\wdm\nf-wdm-zwgetnotificationresourcemanager.md) | The ZwGetNotificationResourceManager routine retrieves the next transaction notification from a specified resource manager's notification queue. |
| [ZwLoadDriver function](..\wdm\nf-wdm-zwloaddriver.md) | The ZwLoadDriver routine loads a driver into the system. |
| [ZwLockFile function](..\ntifs\nf-ntifs-zwlockfile.md) | The ZwLockFile routine requests a byte-range lock for the specified file. |
| [ZwMakeTemporaryObject function](..\wdm\nf-wdm-zwmaketemporaryobject.md) | The ZwMakeTemporaryObject routine changes the attributes of an object to make it temporary. |
| [ZwMapViewOfSection function](..\wdm\nf-wdm-zwmapviewofsection.md) | The ZwMapViewOfSection routine maps a view of a section into the virtual address space of a subject process. |
| [ZwNotifyChangeKey function](..\ntifs\nf-ntifs-zwnotifychangekey.md) | The ZwNotifyChangeKey routine allows a driver to request notification when a registry key changes. |
| [ZwOpenDirectoryObject function](..\ntifs\nf-ntifs-zwopendirectoryobject.md) | The ZwOpenDirectoryObject routine opens an existing directory object. |
| [ZwOpenEnlistment function](..\wdm\nf-wdm-zwopenenlistment.md) | The ZwOpenEnlistment routine obtains a handle to an existing enlistment object. |
| [ZwOpenEvent function](..\wdm\nf-wdm-zwopenevent.md) | The ZwOpenEvent routine opens a handle to an existing named event object with the specified desired access. |
| [ZwOpenFile function](..\wdm\nf-wdm-zwopenfile.md) | The ZwOpenFile routine opens an existing file, directory, device, or volume. |
| [ZwOpenKey function](..\wdm\nf-wdm-zwopenkey.md) | The ZwOpenKey routine opens an existing registry key. |
| [ZwOpenKeyEx function](..\wdm\nf-wdm-zwopenkeyex.md) | The ZwOpenKeyEx routine opens an existing registry key. |
| [ZwOpenKeyTransacted function](..\wdm\nf-wdm-zwopenkeytransacted.md) | The ZwOpenKeyTransacted routine opens an existing registry key and associates the key with a transaction. |
| [ZwOpenKeyTransactedEx function](..\wdm\nf-wdm-zwopenkeytransactedex.md) | The ZwOpenKeyTransactedEx routine opens an existing registry key and associates the key with a transaction. |
| [ZwOpenProcess function](..\ntddk\nf-ntddk-zwopenprocess.md) | The ZwOpenProcess routine opens a handle to a process object and sets the access rights to this object. |
| [ZwOpenProcessTokenEx function](..\ntifs\nf-ntifs-zwopenprocesstokenex.md) | The ZwOpenProcessTokenEx routine opens the access token associated with a process. |
| [ZwOpenResourceManager function](..\wdm\nf-wdm-zwopenresourcemanager.md) | The ZwOpenResourceManager routine returns a handle to an existing resource manager object. |
| [ZwOpenSection function](..\wdm\nf-wdm-zwopensection.md) | The ZwOpenSection routine opens a handle for an existing section object. |
| [ZwOpenSymbolicLinkObject function](..\wdm\nf-wdm-zwopensymboliclinkobject.md) | The ZwOpenSymbolicLinkObject routine opens an existing symbolic link. |
| [ZwOpenThreadTokenEx function](..\ntifs\nf-ntifs-zwopenthreadtokenex.md) | The ZwOpenThreadTokenEx routine opens the access token associated with a thread. |
| [ZwOpenTransaction function](..\wdm\nf-wdm-zwopentransaction.md) | The ZwOpenTransaction routine obtains a handle to an existing transaction object. |
| [ZwOpenTransactionManager function](..\wdm\nf-wdm-zwopentransactionmanager.md) | The ZwOpenTransactionManager routine obtains a handle to an existing transaction manager object. |
| [ZwPowerInformation function](..\ntddk\nf-ntddk-zwpowerinformation.md) | The ZwPowerInformation routine sets or retrieves system power information. |
| [ZwPrePrepareComplete function](..\wdm\nf-wdm-zwprepreparecomplete.md) | The ZwPrePrepareComplete routine notifies KTM that the calling resource manager has finished preliminary preparation of a transaction's data. |
| [ZwPrePrepareEnlistment function](..\wdm\nf-wdm-zwpreprepareenlistment.md) | The ZwPrePrepareEnlistment routine initiates the pre-prepare operation for a specified enlistment's transaction. |
| [ZwPrepareComplete function](..\wdm\nf-wdm-zwpreparecomplete.md) | The ZwPrepareComplete routine notifies KTM that the calling resource manager has finished preparing a transaction's data. |
| [ZwPrepareEnlistment function](..\wdm\nf-wdm-zwprepareenlistment.md) | The ZwPrepareEnlistment routine initiates the prepare operation for a specified enlistment's transaction. |
| [ZwQueryDirectoryFile function](..\ntifs\nf-ntifs-zwquerydirectoryfile.md) | The ZwQueryDirectoryFile routine returns various kinds of information about files in the directory specified by a given file handle. |
| [ZwQueryDirectoryFileEx function](..\ntifs\nf-ntifs-zwquerydirectoryfileex.md) | The ZwQueryDirectoryFileEx routine returns information about files in the directory specified by the FileHandle parameter. |
| [ZwQueryEaFile function](..\ntifs\nf-ntifs-zwqueryeafile.md) | The ZwQueryEaFile routine returns information about extended-attribute (EA) values for a file. |
| [ZwQueryFullAttributesFile function](..\wdm\nf-wdm-zwqueryfullattributesfile.md) | The ZwQueryFullAttributesFile routine supplies network open information for the specified file. |
| [ZwQueryInformationEnlistment function](..\wdm\nf-wdm-zwqueryinformationenlistment.md) | The ZwQueryInformationEnlistment routine retrieves information about a specified enlistment object. |
| [ZwQueryInformationFile function](..\wdm\nf-wdm-zwqueryinformationfile.md) | The ZwQueryInformationFile routine returns various kinds of information about a file object. |
| [ZwQueryInformationResourceManager function](..\wdm\nf-wdm-zwqueryinformationresourcemanager.md) | The ZwQueryInformationResourceManager routine retrieves information about a specified resource manager object. |
| [ZwQueryInformationToken function](..\ntifs\nf-ntifs-zwqueryinformationtoken.md) | The ZwQueryInformationToken routine retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information. |
| [ZwQueryInformationTransaction function](..\wdm\nf-wdm-zwqueryinformationtransaction.md) | The ZwQueryInformationTransaction routine retrieves information about a specified transaction. |
| [ZwQueryInformationTransactionManager function](..\wdm\nf-wdm-zwqueryinformationtransactionmanager.md) | The ZwQueryInformationTransactionManager routine retrieves information about a specified transaction manager object. |
| [ZwQueryKey function](..\wdm\nf-wdm-zwquerykey.md) | The ZwQueryKey routine provides information about the class of a registry key, and the number and sizes of its subkeys. |
| [ZwQueryObject function](..\ntifs\nf-ntifs-zwqueryobject.md) | The ZwQueryObject routine provides information about a supplied object. |
| [ZwQueryQuotaInformationFile function](..\ntifs\nf-ntifs-zwqueryquotainformationfile.md) | The ZwQueryQuotaInformationFile routine retrieves quota entries associated with the volume specified by the FileHandle parameter. |
| [ZwQuerySecurityObject function](..\ntifs\nf-ntifs-zwquerysecurityobject.md) | The ZwQuerySecurityObject routine retrieves a copy of an object's security descriptor. |
| [ZwQuerySymbolicLinkObject function](..\wdm\nf-wdm-zwquerysymboliclinkobject.md) | The ZwQuerySymbolicLinkObject routine returns a Unicode string that contains the target of a symbolic link. |
| [ZwQueryValueKey function](..\wdm\nf-wdm-zwqueryvaluekey.md) | The ZwQueryValueKey routine returns a value entry for a registry key. |
| [ZwQueryVirtualMemory function](..\ntifs\nf-ntifs-zwqueryvirtualmemory.md) | The ZwQueryVirtualMemory routine determines the state, protection, and type of a region of pages within the virtual address space of the subject process. |
| [ZwQueryVolumeInformationFile function](..\ntifs\nf-ntifs-zwqueryvolumeinformationfile.md) | The ZwQueryVolumeInformationFile routine retrieves information about the volume associated with a given file, directory, storage device, or volume. |
| [ZwReadFile function](..\wdm\nf-wdm-zwreadfile.md) | The ZwReadFile routine reads data from an open file. |
| [ZwReadOnlyEnlistment function](..\wdm\nf-wdm-zwreadonlyenlistment.md) | The ZwReadOnlyEnlistment routine sets a specified enlistment to be read-only. |
| [ZwRecoverEnlistment function](..\wdm\nf-wdm-zwrecoverenlistment.md) | The ZwRecoverEnlistment routine initiates a recovery operation for the transaction that is associated with a specified enlistment. |
| [ZwRecoverResourceManager function](..\wdm\nf-wdm-zwrecoverresourcemanager.md) | The ZwRecoverResourceManager routine tries to recover the transaction that is associated with each enlistment of a specified resource manager object. |
| [ZwRecoverTransactionManager function](..\wdm\nf-wdm-zwrecovertransactionmanager.md) | The ZwRecoverTransactionManager routine reconstructs the state of the transaction manager object (including all transactions, enlistments, and resource managers) from the recovery information that is in the log stream. |
| [ZwRollbackComplete function](..\wdm\nf-wdm-zwrollbackcomplete.md) | The ZwRollbackComplete routine notifies KTM that the calling resource manager has finished rolling back a transaction's data. |
| [ZwRollbackEnlistment function](..\wdm\nf-wdm-zwrollbackenlistment.md) | The ZwRollbackEnlistment routine rolls back the transaction that is associated with a specified enlistment. |
| [ZwRollbackTransaction function](..\wdm\nf-wdm-zwrollbacktransaction.md) | The ZwRollbackTransaction routine initiates a rollback operation for a specified transaction. |
| [ZwRollforwardTransactionManager function](..\wdm\nf-wdm-zwrollforwardtransactionmanager.md) | The ZwRollforwardTransactionManager routine initiates recovery operations for all of the in-progress transactions that are assigned to a specified transaction manager. |
| [ZwSetEaFile function](..\ntifs\nf-ntifs-zwseteafile.md) | The ZwSetEaFile routine sets extended-attribute (EA) values for a file. |
| [ZwSetEvent function](..\ntifs\nf-ntifs-zwsetevent.md) | The ZwSetEvent routine sets an event object to a Signaled state and attempts to satisfy as many waits as possible. |
| [ZwSetInformationEnlistment function](..\wdm\nf-wdm-zwsetinformationenlistment.md) | The ZwSetInformationEnlistment routine sets information for a specified enlistment object. |
| [ZwSetInformationFile function](..\wdm\nf-wdm-zwsetinformationfile.md) | The ZwSetInformationFile routine changes various kinds of information about a file object. |
| [ZwSetInformationResourceManager function](..\wdm\nf-wdm-zwsetinformationresourcemanager.md) | The ZwSetInformationResourceManager routine is not used. |
| [ZwSetInformationThread function](..\ntddk\nf-ntddk-zwsetinformationthread.md) | The ZwSetInformationThread routine sets the priority of a thread. |
| [ZwSetInformationToken function](..\ntifs\nf-ntifs-zwsetinformationtoken.md) | The ZwSetInformationToken routine modifies information in a specified token. The calling process must have appropriate access rights to set the information. |
| [ZwSetInformationTransaction function](..\wdm\nf-wdm-zwsetinformationtransaction.md) | The ZwSetInformationTransaction routine sets information for a specified transaction. |
| [ZwSetInformationVirtualMemory function](..\ntifs\nf-ntifs-zwsetinformationvirtualmemory.md) | The ZwSetInformationVirtualMemory routine performs an operation on a specified list of address ranges in the user address space of a process. |
| [ZwSetQuotaInformationFile function](..\ntifs\nf-ntifs-zwsetquotainformationfile.md) | The ZwSetQuotaInformationFile routine changes quota entries for the volume associated with the FileHandle parameter. All of the quota entries in the specified buffer are applied to the volume. |
| [ZwSetSecurityObject function](..\ntifs\nf-ntifs-zwsetsecurityobject.md) | The ZwSetSecurityObject routine sets an object's security state. |
| [ZwSetValueKey function](..\wdm\nf-wdm-zwsetvaluekey.md) | The ZwSetValueKey routine creates or replaces a registry key's value entry. |
| [ZwSetVolumeInformationFile function](..\ntifs\nf-ntifs-zwsetvolumeinformationfile.md) | The ZwSetVolumeInformationFile routine modifies information about the volume associated with a given file, directory, storage device, or volume. |
| [ZwSinglePhaseReject function](..\wdm\nf-wdm-zwsinglephasereject.md) | The ZwSinglePhaseReject routine informs KTM that the calling resource manager will not support single-phase commit operations for a specified enlistment. |
| [ZwTerminateProcess function](..\ntddk\nf-ntddk-zwterminateprocess.md) | The ZwTerminateProcess routine terminates a process and all of its threads. |
| [ZwUnloadDriver function](..\wdm\nf-wdm-zwunloaddriver.md) | The ZwUnloadDriver routine unloads a driver from the system. |
| [ZwUnlockFile function](..\ntifs\nf-ntifs-zwunlockfile.md) | The ZwUnlockFile routine unlocks a byte-range lock in a file. |
| [ZwUnmapViewOfSection function](..\wdm\nf-wdm-zwunmapviewofsection.md) | The ZwUnmapViewOfSection routine unmaps a view of a section from the virtual address space of a subject process. |
| [ZwWaitForSingleObject function](..\ntifs\nf-ntifs-zwwaitforsingleobject.md) | The ZwWaitForSingleObject routine waits until the specified object attains a state of Signaled. An optional time-out can also be specified. |
| [ZwWriteFile function](..\wdm\nf-wdm-zwwritefile.md) | The ZwWriteFile routine writes data to an open file. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [ALLOCATE_FUNCTION_EX callback](..\wdm\nc-wdm-allocate-function-ex.md) | The LookasideListAllocateEx routine allocates the storage for a new lookaside-list entry when a client requests an entry from a lookaside list that is empty. |
| [DEVICE_ACTIVE_COOLING callback](..\poclass\nc-poclass-device-active-cooling.md) | The ActiveCooling callback routine engages or disengages a device's active-cooling function. |
| [DEVICE_PASSIVE_COOLING callback](..\poclass\nc-poclass-device-passive-cooling.md) | The PassiveCooling callback routine controls the degree to which the device must throttle its performance to meet cooling requirements. |
| [DRIVER_CONTROL callback](..\wdm\nc-wdm-driver-control.md) | The ControllerControl routine starts a data transfer operation. |
| [DRIVER_INITIALIZE callback](..\wdm\nc-wdm-driver-initialize.md) | DriverEntry is the first routine called after a driver is loaded, and is responsible for initializing the driver. |
| [DRIVER_LIST_CONTROL callback](..\wdm\nc-wdm-driver-list-control.md) | The AdapterListControl routine starts a direct memory access (DMA) scatter/gather operation. |
| [DRIVER_REINITIALIZE callback](..\ntddk\nc-ntddk-driver-reinitialize.md) | The Reinitialize routine continues driver and device initialization after the driver's DriverEntry routine returns. |
| [ENABLE_VIRTUALIZATION callback](..\wdm\nc-wdm-enable-virtualization.md) | The EnableVirtualization routine enables or disables virtualization for a PCI Express (PCIe) device that supports the single root I/O virtualization (SR-IOV) interface. |
| [EXPAND_STACK_CALLOUT callback](..\ntddk\nc-ntddk-expand-stack-callout.md) | The ExpandedStackCall routine executes with a guaranteed stack size. |
| [EX_CALLBACK_FUNCTION callback](..\wdm\nc-wdm-ex-callback-function.md) | A filter driver's RegistryCallback routine can monitor, block, or modify a registry operation. |
| [FREE_FUNCTION_EX callback](..\wdm\nc-wdm-free-function-ex.md) | The LookasideListFreeEx routine frees the storage for a lookaside-list entry when a client tries to insert the entry into a lookaside list that is full. |
| [GET_D3COLD_CAPABILITY callback](..\wdm\nc-wdm-get-d3cold-capability.md) | The GetBusDriverD3ColdSupport routine enables the driver for a device to query whether the enumerating bus driver supports the D3cold device power state. |
| [GET_D3COLD_LAST_TRANSITION_STATUS callback](..\wdm\nc-wdm-get-d3cold-last-transition-status.md) | The GetLastTransitionStatus routine enables the driver for a device to query whether the most recent transition to the D3hot substate was followed by a transition to the D3cold substate. |
| [GET_IDLE_WAKE_INFO callback](..\wdm\nc-wdm-get-idle-wake-info.md) | The GetIdleWakeInfo routine enables the driver for a device to discover the device power states from which the device can signal a wake event. |
| [GET_VIRTUAL_DEVICE_DATA callback](..\wdm\nc-wdm-get-virtual-device-data.md) | The GetVirtualFunctionData routine reads data from the PCI Express (PCIe) configuration space of a virtual function (VF) on a device that supports the single root I/O virtualization (SR-IOV) interface. |
| [GET_VIRTUAL_DEVICE_LOCATION callback](..\wdm\nc-wdm-get-virtual-device-location.md) | The GetLocation routine returns the device location of a PCI Express (PCIe) virtual function (VF) on a PCI bus. A device that supports the single root I/O virtualization (SR-IOV) interface can expose one or more VFs on the PCI bus. |
| [GET_VIRTUAL_DEVICE_RESOURCES callback](..\wdm\nc-wdm-get-virtual-device-resources.md) | The GetResources routine returns the resources that the PCI Express (PCIe) physical function (PF) requires in order to enable virtualization on a device that supports the single root I/O virtualization (SR-IOV) interface. |
| [GET_VIRTUAL_FUNCTION_PROBED_BARS callback](..\wdm\nc-wdm-get-virtual-function-probed-bars.md) | The GetVirtualFunctionProbedBars routine returns the values of the PCI Express (PCIe) Base Address Registers (BARs) of a device that supports the single root I/O virtualization (SR-IOV) interface. |
| [IO_COMPLETION_ROUTINE callback](..\wdm\nc-wdm-io-completion-routine.md) | The IoCompletion routine completes the processing of I/O operations. |
| [IO_CSQ_ACQUIRE_LOCK callback](..\wdm\nc-wdm-io-csq-acquire-lock.md) | The CsqAcquireLock routine is used by the system to acquire the lock for a driver-implemented, cancel-safe IRP queue. |
| [IO_CSQ_COMPLETE_CANCELED_IRP callback](..\wdm\nc-wdm-io-csq-complete-canceled-irp.md) | The CsqCompleteCanceledIrp routine is used by the system to signal to the driver that it can complete a canceled IRP. |
| [IO_CSQ_INSERT_IRP callback](..\wdm\nc-wdm-io-csq-insert-irp.md) | The CsqInsertIrp routine is used by the system to insert an IRP into a driver-implemented, cancel-safe IRP queue. |
| [IO_CSQ_INSERT_IRP_EX callback](..\wdm\nc-wdm-io-csq-insert-irp-ex.md) | The CsqInsertIrpEx routine is used by the system to insert an IRP into a driver-implemented, cancel-safe IRP queue. |
| [IO_CSQ_PEEK_NEXT_IRP callback](..\wdm\nc-wdm-io-csq-peek-next-irp.md) | The CsqPeekNextIrp routine is used by the system to find the next matching IRP in a driver-implemented, cancel-safe IRP queue. |
| [IO_CSQ_RELEASE_LOCK callback](..\wdm\nc-wdm-io-csq-release-lock.md) | The CsqReleaseLock routine is used by the system to release the lock that was acquired using CsqAcquireLock. |
| [IO_CSQ_REMOVE_IRP callback](..\wdm\nc-wdm-io-csq-remove-irp.md) | The CsqRemoveIrp routine is used by the system to remove the specified IRP from a driver-implemented, cancel-safe IRP queue. |
| [IO_TIMER_ROUTINE callback](..\wdm\nc-wdm-io-timer-routine.md) | The IoTimer routine is a DPC that, if registered, is called once per second. |
| [KBUGCHECK_CALLBACK_ROUTINE callback](..\wdm\nc-wdm-kbugcheck-callback-routine.md) | The BugCheckCallback routine is executed whenever the system issues a bug check. |
| [KBUGCHECK_REASON_CALLBACK_ROUTINE callback](..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md) | The BugCheckDumpIoCallback routine is executed each time the system writes data to a crash dump file. |
| [KIPI_BROADCAST_WORKER callback](..\wdm\nc-wdm-kipi-broadcast-worker.md) | The IpiGenericCall routine runs simultaneously on all processors. |
| [KMESSAGE_SERVICE_ROUTINE callback](..\wdm\nc-wdm-kmessage-service-routine.md) | An InterruptMessageService routine services a message-signaled interrupt. |
| [KSERVICE_ROUTINE callback](..\wdm\nc-wdm-kservice-routine.md) | The InterruptService routine (ISR) quickly services a device interrupt and schedules post-interrupt processing of received data, if necessary. |
| [KSTART_ROUTINE callback](..\wdm\nc-wdm-kstart-routine.md) | The ThreadStart routine provides an entry point for a driver-created system thread. |
| [KSYNCHRONIZE_ROUTINE callback](..\wdm\nc-wdm-ksynchronize-routine.md) | The SynchCritSection routine is used to access hardware resources or driver data that are shared with a driver's InterruptService routine. |
| [MM_MDL_ROUTINE callback](..\wdm\nc-wdm-mm-mdl-routine.md) | A driver-supplied callback routine that is invoked after a memory descriptor list (MDL) is mapped by calling the MmMapMdl function. |
| [PCI_MSIX_MASKUNMASK_ENTRY callback](..\wdm\nc-wdm-pci-msix-maskunmask-entry.md) | The MaskTableEntry routine masks an interrupt in the MSI-X hardware interrupt table. |
| [PCI_MSIX_SET_ENTRY callback](..\wdm\nc-wdm-pci-msix-set-entry.md) | The SetTableEntry routine sets the message ID for a table entry in the MSI-X hardware interrupt table. |
| [PCREATE_PROCESS_NOTIFY_ROUTINE callback](..\ntddk\nc-ntddk-pcreate-process-notify-routine.md) | Process-creation callback implemented by a driver to track the system-wide creation and deletion of processes against the driver's internal state. |
| [PCREATE_PROCESS_NOTIFY_ROUTINE_EX callback](..\ntddk\nc-ntddk-pcreate-process-notify-routine-ex.md) | A callback routine implemented by a driver to notify the caller when a process is created or exits. |
| [PCREATE_THREAD_NOTIFY_ROUTINE callback](..\ntddk\nc-ntddk-pcreate-thread-notify-routine.md) | A callback routine implemented by a driver to notify the caller when a thread is created or deleted. |
| [PDEVICE_RESET_HANDLER callback](..\wdm\nc-wdm-pdevice-reset-handler.md) | The DeviceReset routine is used to reset and recover a malfunctioning device. |
| [PEPCALLBACKNOTIFYACPI callback](..\pepfx\nc-pepfx-pepcallbacknotifyacpi.md) | An AcceptAcpiNotification event callback routine handles ACPI notifications from the Windows power management framework (PoFx). |
| [PEPCALLBACKNOTIFYDPM callback](..\pepfx\nc-pepfx-pepcallbacknotifydpm.md) | An AcceptDeviceNotification event callback routine handles device power management (DPM) notifications from the Windows power management framework (PoFx). |
| [PEPCALLBACKNOTIFYPPM callback](..\pepfx\nc-pepfx-pepcallbacknotifyppm.md) | An AcceptProcessorNotification event callback routine handles processor power management (PPM) notifications from the Windows power management framework (PoFx). |
| [PEPCALLBACKPOWERONCRASHDUMPDEVICE callback](..\pepfx\nc-pepfx-pepcallbackpoweroncrashdumpdevice.md) | The PowerOnDumpDeviceCallback callback routine turns on the crash-dump device. |
| [PGET_LOCATION_STRING callback](..\ntddk\nc-ntddk-pget-location-string.md) | The PnpGetLocationString routine provides the device-specific part of the device's SPDRP_LOCATION_PATHS property. |
| [PINTERFACE_DEREFERENCE callback](..\wdm\nc-wdm-pinterface-dereference.md) | The InterfaceDereference routine decrements the reference count on a driver-defined interface. |
| [PINTERFACE_REFERENCE callback](..\wdm\nc-wdm-pinterface-reference.md) | The InterfaceReference routine increments the reference count on a driver-defined interface. |
| [PLOAD_IMAGE_NOTIFY_ROUTINE callback](..\ntddk\nc-ntddk-pload-image-notify-routine.md) | Called by the operating system to notify the driver when a driver image or a user image (for example, a DLL or EXE) is mapped into virtual memory. |
| [POFXCALLBACKREQUESTCOMMON callback](..\pepfx\nc-pepfx-pofxcallbackrequestcommon.md) | The RequestCommon routine is a generic request handler. |
| [PO_FX_COMPONENT_ACTIVE_CONDITION_CALLBACK callback](..\wdm\nc-wdm-po-fx-component-active-condition-callback.md) | The ComponentActiveConditionCallback callback routine notifies the driver that the specified component completed a transition from the idle condition to the active condition. |
| [PO_FX_COMPONENT_CRITICAL_TRANSITION_CALLBACK callback](..\wdm\nc-wdm-po-fx-component-critical-transition-callback.md) | The ComponentCriticalTransitionCallback callback routine handles a transition of the specified component between the F0 (fully on) and low-power Fx component power states. |
| [PO_FX_COMPONENT_IDLE_CONDITION_CALLBACK callback](..\wdm\nc-wdm-po-fx-component-idle-condition-callback.md) | The ComponentIdleConditionCallback callback routine notifies the driver that the specified component completed a transition from the active condition to the idle condition. |
| [PO_FX_COMPONENT_IDLE_STATE_CALLBACK callback](..\wdm\nc-wdm-po-fx-component-idle-state-callback.md) | The ComponentIdleStateCallback callback routine notifies the driver of a pending change to the Fx power state of the specified component. |
| [PO_FX_COMPONENT_PERF_STATE_CALLBACK callback](..\wdm\nc-wdm-po-fx-component-perf-state-callback.md) | The ComponentPerfStateCallback callback routine notifies the driver that its request to change the performance state of a component is complete. |
| [PO_FX_DEVICE_POWER_NOT_REQUIRED_CALLBACK callback](..\wdm\nc-wdm-po-fx-device-power-not-required-callback.md) | The DevicePowerNotRequiredCallback callback routine notifies the device driver that the device is not required to stay in the D0 power state. |
| [PO_FX_DEVICE_POWER_REQUIRED_CALLBACK callback](..\wdm\nc-wdm-po-fx-device-power-required-callback.md) | The DevicePowerRequiredCallback callback routine notifies the device driver that the device must enter and remain in the D0 power state. |
| [PO_FX_POWER_CONTROL_CALLBACK callback](..\wdm\nc-wdm-po-fx-power-control-callback.md) | The PowerControlCallback callback routine performs a power control operation that is requested by the power management framework (PoFx). |
| [PPO_ENUMERATE_INTERRUPT_SOURCE_CALLBACK callback](..\pepfx\nc-pepfx-ppo-enumerate-interrupt-source-callback.md) | An EnumerateInterruptSource callback routine supplies a platform extension plug-in (PEP) with information about an interrupt source. |
| [PREENUMERATE_SELF callback](..\wdm\nc-wdm-preenumerate-self.md) | A ReenumerateSelf routine requests that a bus driver reenumerate a child device. |
| [REQUEST_POWER_COMPLETE callback](..\wdm\nc-wdm-request-power-complete.md) | The PowerCompletion callback routine completes the processing of a power IRP. |
| [RTL_QUERY_REGISTRY_ROUTINE callback](..\wdm\nc-wdm-rtl-query-registry-routine.md) | The QueryRoutine routine provides information about a registry value that was requested in a preceding call to the RtlQueryRegistryValues routine. |
| [RTL_RUN_ONCE_INIT_FN callback](..\ntddk\nc-ntddk-rtl-run-once-init-fn.md) | The RunOnceInitialization routine performs a one-time initialization operation. |
| [SET_D3COLD_SUPPORT callback](..\wdm\nc-wdm-set-d3cold-support.md) | The SetD3ColdSupport routine enables or disables transitions to the D3cold device power state. |
| [SET_VIRTUAL_DEVICE_DATA callback](..\wdm\nc-wdm-set-virtual-device-data.md) | The SetVirtualFunctionData routine writes data to the PCI Express (PCIe) configuration space of a virtual function (VF) on a device that supports the single root I/O virtualization (SR-IOV) interface. |
| [SILO_CONTEXT_CLEANUP_CALLBACK callback](..\ntddk\nc-ntddk-silo-context-cleanup-callback.md) | This callback is invoked when the context object reaches a reference count of zero. |
| [SILO_MONITOR_CREATE_CALLBACK callback](..\ntddk\nc-ntddk-silo-monitor-create-callback.md) | This is callback is invoked when a new silo is created. |
| [SILO_MONITOR_TERMINATE_CALLBACK callback](..\ntddk\nc-ntddk-silo-monitor-terminate-callback.md) | This callback is invoked when a silo is terminated. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [AUX_MODULE_BASIC_INFO structure](..\aux_klib\ns-aux-klib--aux-module-basic-info.md) | The AUX_MODULE_BASIC_INFO structure contains basic information about a loaded image module. |
| [AUX_MODULE_EXTENDED_INFO structure](..\aux_klib\ns-aux-klib--aux-module-extended-info.md) | The AUX_MODULE_EXTENDED_INFO structure contains extended information about a loaded image module. |
| [BDCB_IMAGE_INFORMATION structure](..\ntddk\ns-ntddk--bdcb-image-information.md) | The BDCB_IMAGE_INFORMATION structure describes information about a boot-start driver that is about to be initialized, provided by Windows to a boot-start driver's BOOT_DRIVER_CALLBACK_FUNCTION routine. |
| [BDCB_STATUS_UPDATE_CONTEXT structure](..\ntddk\ns-ntddk--bdcb-status-update-context.md) | The BDCB_STATUS_UPDATE_CONTEXT structure describes a status update provided by Windows to a boot-start driver's BOOT_DRIVER_CALLBACK_FUNCTION routine. |
| [BOOTDISK_INFORMATION structure](..\wdm\ns-wdm--bootdisk-information.md) | The BOOTDISK_INFORMATION structure contains basic information describing the boot and system disks. |
| [BOOTDISK_INFORMATION_EX structure](..\wdm\ns-wdm--bootdisk-information-ex.md) | The BOOTDISK_INFORMATION_EX structure contains extended information describing the boot and system disks. |
| [BUS_INTERFACE_STANDARD structure](..\wdm\ns-wdm--bus-interface-standard.md) | The BUS_INTERFACE_STANDARD interface structure enables device drivers to make direct calls to parent bus driver routines. This structure defines the GUID_BUS_INTERFACE_STANDARD interface. |
| [CLFS_LOG_NAME_INFORMATION structure](..\wdm\ns-wdm--clfs-log-name-information.md) | The CLFS_LOG_NAME_INFORMATION structure holds the name of a Common Log File System (CLFS) stream or log. |
| [CLFS_MGMT_CLIENT_REGISTRATION structure](..\wdm\ns-wdm--clfs-mgmt-client-registration.md) | The CLFS_MGMT_CLIENT_REGISTRATION structure is given to CLFS management by clients who manage their own logs. |
| [CLFS_MGMT_POLICY structure](..\wdm\ns-wdm--clfs-mgmt-policy.md) | The CLFS_MGMT_POLICY structure holds a description of a policy for managing a CLFS log. |
| [CLFS_STREAM_ID_INFORMATION structure](..\wdm\ns-wdm--clfs-stream-id-information.md) | The CLFS_STREAM_ID_INFORMATION structure holds a value that identifies a stream in a Common Log File System (CLFS) log. |
| [CM_EISA_FUNCTION_INFORMATION structure](..\wdm\ns-wdm--cm-eisa-function-information.md) | The CM_EISA_FUNCTION_INFORMATION structure defines detailed EISA configuration information returned by HalGetBusData for the input BusDataType EisaConfiguration, or by HalGetBusDataByOffset for the input BusDataType EisaConfiguration and the Offset zero, assuming the caller-allocated Buffer is of sufficient Length. |
| [CM_EISA_SLOT_INFORMATION structure](..\wdm\ns-wdm--cm-eisa-slot-information.md) | The CM_EISA_SLOT_INFORMATION structure defines EISA configuration header information returned by HalGetBusData for the input BusDataType = EisaConfiguration, or by HalGetBusDataByOffset for the inputs BusDataType = EisaConfiguration and Offset = 0, assuming the caller-allocated Buffer is of sufficient Length. |
| [CM_FLOPPY_DEVICE_DATA structure](..\wdm\ns-wdm--cm-floppy-device-data.md) | The CM_FLOPPY_DEVICE_DATA structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a floppy controller if the system can collect this information during the boot process. |
| [CM_FULL_RESOURCE_DESCRIPTOR structure](..\wdm\ns-wdm--cm-full-resource-descriptor.md) | The CM_FULL_RESOURCE_DESCRIPTOR structure specifies a set of system hardware resources of various types, assigned to a device that is connected to a specific bus. This structure is contained within a CM_RESOURCE_LIST structure. |
| [CM_INT13_DRIVE_PARAMETER structure](..\wdm\ns-wdm--cm-int13-drive-parameter.md) | The CM_INT13_DRIVE_PARAMETER structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a disk controller if the system can collect this information during the boot process. |
| [CM_KEYBOARD_DEVICE_DATA structure](..\wdm\ns-wdm--cm-keyboard-device-data.md) | The CM_KEYBOARD_DEVICE_DATA structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a keyboard peripheral if the system can collect this information during the boot process. |
| [CM_MCA_POS_DATA structure](..\wdm\ns-wdm--cm-mca-pos-data.md) | The CM_MCA_POS_DATA structure is obsolete. It defines IBM-compatible MCA POS configuration information for a slot. |
| [CM_PARTIAL_RESOURCE_DESCRIPTOR structure](..\wdm\ns-wdm--cm-partial-resource-descriptor.md) | The CM_PARTIAL_RESOURCE_DESCRIPTOR structure specifies one or more system hardware resources, of a single type, assigned to a device. |
| [CM_PARTIAL_RESOURCE_LIST structure](..\wdm\ns-wdm--cm-partial-resource-list.md) | The CM_PARTIAL_RESOURCE_LIST structure specifies a set of system hardware resources, of various types, assigned to a device. This structure is contained within a CM_FULL_RESOURCE_DESCRIPTOR structure. |
| [CM_Power_Data_s structure](..\wdm\ns-wdm-cm-power-data-s.md) | The CM_POWER_DATA structure contains information about a device's power management state and capabilities. |
| [CM_RESOURCE_LIST structure](..\wdm\ns-wdm--cm-resource-list.md) | The CM_RESOURCE_LIST structure specifies all of the system hardware resources assigned to a device. |
| [CM_SCSI_DEVICE_DATA structure](..\wdm\ns-wdm--cm-scsi-device-data.md) | The CM_SCSI_DEVICE_DATA structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a SCSI HBA if the system can collect this information during the boot process. |
| [CM_SERIAL_DEVICE_DATA structure](..\wdm\ns-wdm--cm-serial-device-data.md) | The CM_SERIAL_DEVICE_DATA structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a serial controller if the system can collect this information during the boot process. |
| [CONTROLLER_OBJECT structure](..\ntddk\ns-ntddk--controller-object.md) | A controller object represents a hardware adapter or controller with homogenous devices that are the actual targets for I/O requests. |
| [CORRELATION_VECTOR structure](..\ntddk\ns-ntddk-correlation-vector.md) | Store the correlation vector that is used to reference events and the generated logs for diagnostic purposes. |
| [COUNTED_REASON_CONTEXT structure](..\wdm\ns-wdm--counted-reason-context.md) | The COUNTED_REASON_CONTEXT structure contains one or more strings that give reasons for a power request. |
| [CPTABLEINFO structure](..\ntnls\ns-ntnls--cptableinfo.md) | Stores the NLS file formats. |
| [D3COLD_SUPPORT_INTERFACE structure](..\wdm\ns-wdm--d3cold-support-interface.md) | The D3COLD_SUPPORT_INTERFACE interface structure contains pointers to the routines in the GUID_D3COLD_SUPPORT_INTERFACE driver interface. |
| [DEVICE_CAPABILITIES structure](..\wdm\ns-wdm--device-capabilities.md) | A DEVICE_CAPABILITIES structure describes PnP and power capabilities of a device. This structure is returned in response to an IRP_MN_QUERY_CAPABILITIES IRP. |
| [DEVICE_DESCRIPTION structure](..\wdm\ns-wdm--device-description.md) | The DEVICE_DESCRIPTION structure describes the attributes of the physical device for which a driver is requesting a DMA adapter. |
| [DEVICE_DESCRIPTION structure](..\wdm\ns-wdm--device-description~r1.md) | The DEVICE_DESCRIPTION structure describes the attributes of the physical device for which a driver is requesting a DMA adapter. |
| [DEVICE_INTERFACE_CHANGE_NOTIFICATION structure](..\wdm\ns-wdm--device-interface-change-notification.md) | The DEVICE_INTERFACE_CHANGE_NOTIFICATION structure describes a device interface that has been enabled (arrived) or disabled (removed). |
| [DEVICE_OBJECT structure](..\wdm\ns-wdm--device-object.md) | A device object represents a logical, virtual, or physical device for which a driver handles I/O requests. |
| [DEVICE_OBJECT structure](..\wdm\ns-wdm--device-object~r1.md) | A device object represents a logical, virtual, or physical device for which a driver handles I/O requests. |
| [DEVICE_OBJECT structure](..\wdm\ns-wdm--device-object~r2.md) | A device object represents a logical, virtual, or physical device for which a driver handles I/O requests. |
| [DEVICE_OBJECT structure](..\wdm\ns-wdm--device-object~r3.md) | A device object represents a logical, virtual, or physical device for which a driver handles I/O requests. |
| [DEVICE_RESET_INTERFACE_STANDARD structure](..\wdm\ns-wdm--device-reset-interface-standard.md) | The DEVICE_RESET_INTERFACE_STANDARD structure enables function drivers to reset and recover malfunctioning devices. This structure describes the GUID_DEVICE_RESET_INTERFACE_STANDARD interface. |
| [DMA_ADAPTER structure](..\ntddk\ns-ntddk--dma-adapter.md) | The DMA_ADAPTER structure describes a system-defined interface to a DMA controller for a given device. A driver calls IoGetDmaAdapter to obtain this structure. |
| [DMA_ADAPTER structure](..\wdm\ns-wdm--dma-adapter.md) | The DMA_ADAPTER structure describes a system-defined interface to a DMA controller for a given device. A driver calls IoGetDmaAdapter to obtain this structure. |
| [DMA_ADAPTER structure](..\wdm\ns-wdm--dma-adapter~r1.md) | The DMA_ADAPTER structure describes a system-defined interface to a DMA controller for a given device. A driver calls IoGetDmaAdapter to obtain this structure. |
| [DMA_ADAPTER structure](..\wdm\ns-wdm--dma-adapter~r2.md) | The DMA_ADAPTER structure describes a system-defined interface to a DMA controller for a given device. A driver calls IoGetDmaAdapter to obtain this structure. |
| [DMA_ADAPTER structure](..\wdm\ns-wdm--dma-adapter~r3.md) | The DMA_ADAPTER structure describes a system-defined interface to a DMA controller for a given device. A driver calls IoGetDmaAdapter to obtain this structure. |
| [DMA_ADAPTER structure](..\wdm\ns-wdm--dma-adapter~r4.md) | The DMA_ADAPTER structure describes a system-defined interface to a DMA controller for a given device. A driver calls IoGetDmaAdapter to obtain this structure. |
| [DMA_ADAPTER structure](..\wdm\ns-wdm--dma-adapter~r5.md) | The DMA_ADAPTER structure describes a system-defined interface to a DMA controller for a given device. A driver calls IoGetDmaAdapter to obtain this structure. |
| [DMA_ADAPTER_INFO structure](..\wdm\ns-wdm--dma-adapter-info.md) | The DMA_ADAPTER_INFO structure is a container for a DMA_ADAPTER_INFO_XXX structure that describes the capabilities of a system DMA controller. |
| [DMA_ADAPTER_INFO_V1 structure](..\wdm\ns-wdm--dma-adapter-info-v1.md) | The DMA_ADAPTER_INFO_V1 structure describes the capabilities of the system DMA controller that is represented by an adapter object. |
| [DMA_OPERATIONS structure](..\wdm\ns-wdm--dma-operations.md) | The DMA_OPERATIONS structure provides a table of pointers to functions that control the operation of a DMA controller. |
| [DMA_OPERATIONS structure](..\wdm\ns-wdm--dma-operations~r1.md) | The DMA_OPERATIONS structure provides a table of pointers to functions that control the operation of a DMA controller. |
| [DMA_TRANSFER_INFO structure](..\wdm\ns-wdm--dma-transfer-info.md) | The DMA_TRANSFER_INFO structure is a container for a DMA_TRANSFER_INFO_XXX structure that describes the allocation requirements for a scatter/gather list. |
| [DMA_TRANSFER_INFO_V1 structure](..\wdm\ns-wdm--dma-transfer-info-v1.md) | The DMA_TRANSFER_INFO_V1 structure contains the allocation requirements for a scatter/gather list that describes the I/O data buffer for a DMA transfer. |
| [DRIVER_OBJECT structure](..\wdm\ns-wdm--driver-object.md) | Each driver object represents the image of a loaded kernel-mode driver. |
| [DRIVER_OBJECT structure](..\wdm\ns-wdm--driver-object~r1.md) | Each driver object represents the image of a loaded kernel-mode driver. |
| [DRIVER_OBJECT structure](..\wdm\ns-wdm--driver-object~r2.md) | Each driver object represents the image of a loaded kernel-mode driver. |
| [DRIVER_OBJECT structure](..\wdm\ns-wdm--driver-object~r3.md) | Each driver object represents the image of a loaded kernel-mode driver. |
| [DRIVER_OBJECT structure](..\wdm\ns-wdm--driver-object~r4.md) | Each driver object represents the image of a loaded kernel-mode driver. |
| [ENLISTMENT_BASIC_INFORMATION structure](..\wdm\ns-wdm--enlistment-basic-information.md) | The ENLISTMENT_BASIC_INFORMATION structure contains information about an enlistment object. |
| [EVENT_TRACE_HEADER structure](..\evntrace\ns-evntrace--event-trace-header.md) | The EVENT_TRACE_HEADER structure is used to pass a WMI event to the WMI event logger. |
| [EXT_DELETE_PARAMETERS structure](..\wdm\ns-wdm--ext-delete-parameters.md) | The EXT_DELETE_PARAMETERS structure contains an extended set of parameters for the ExDeleteTimer routine. |
| [EXT_SET_PARAMETERS_V0 structure](..\wdm\ns-wdm--ext-set-parameters-v0.md) | The EXT_SET_PARAMETERS structure contains an extended set of parameters for the ExSetTimer routine. |
| [FILE_ACCESS_INFORMATION structure](..\ntifs\ns-ntifs--file-access-information.md) | The FILE_ACCESS_INFORMATION structure is used to query for or set the access rights of a file. |
| [FILE_ALIGNMENT_INFORMATION structure](..\ntddk\ns-ntddk--file-alignment-information.md) | The FILE_ALIGNMENT_INFORMATION structure is used as an argument to the ZwQueryInformationFile routine. |
| [FILE_ALL_INFORMATION structure](..\ntifs\ns-ntifs--file-all-information.md) | The FILE_ALL_INFORMATION structure is a container for several FILE_XXX_INFORMATION structures. |
| [FILE_ATTRIBUTE_TAG_INFORMATION structure](..\ntddk\ns-ntddk--file-attribute-tag-information.md) | The FILE_ATTRIBUTE_TAG_INFORMATION structure is used as an argument to ZwQueryInformationFile. |
| [FILE_BASIC_INFORMATION structure](..\wdm\ns-wdm--file-basic-information.md) | The FILE_BASIC_INFORMATION structure is used as an argument to routines that query or set file information. |
| [FILE_DISPOSITION_INFORMATION structure](..\ntddk\ns-ntddk--file-disposition-information.md) | The FILE_DISPOSITION_INFORMATION structure is used as an argument to the ZwSetInformationFile routine. |
| [FILE_EA_INFORMATION structure](..\ntifs\ns-ntifs--file-ea-information.md) | The FILE_EA_INFORMATION structure is used to query for the size of the extended attributes (EA) for a file. |
| [FILE_END_OF_FILE_INFORMATION structure](..\ntddk\ns-ntddk--file-end-of-file-information.md) | The FILE_END_OF_FILE_INFORMATION structure is used as an argument to the ZwSetInformationFile routine. |
| [FILE_FS_DEVICE_INFORMATION structure](..\wdm\ns-wdm--file-fs-device-information.md) | The FILE_FS_DEVICE_INFORMATION structure provides file system device information about the type of device object associated with a file object. |
| [FILE_FULL_EA_INFORMATION structure](..\wdm\ns-wdm--file-full-ea-information.md) | The FILE_FULL_EA_INFORMATION structure provides extended attribute (EA) information. This structure is used primarily by network drivers. |
| [FILE_IO_PRIORITY_HINT_INFORMATION structure](..\wdm\ns-wdm--file-io-priority-hint-information.md) | The FILE_IO_PRIORITY_HINT_INFORMATION structure is used by the ZwQueryInformationFile and ZwSetInformationFile routines to query and set the default IRP priority hint for requests on the specified file handle. |
| [FILE_IS_REMOTE_DEVICE_INFORMATION structure](..\wdm\ns-wdm--file-is-remote-device-information.md) | The FILE_IS_REMOTE_DEVICE_INFORMATION structure is used as an argument to the ZwQueryInformationFile routine. |
| [FILE_MODE_INFORMATION structure](..\ntifs\ns-ntifs--file-mode-information.md) | The FILE_MODE_INFORMATION structure is used to query or set the access mode of a file. |
| [FILE_NAME_INFORMATION structure](..\ntddk\ns-ntddk--file-name-information.md) | The FILE_NAME_INFORMATION structure is used as argument to the ZwQueryInformationFile and ZwSetInformationFile routines. |
| [FILE_NETWORK_OPEN_INFORMATION structure](..\wdm\ns-wdm--file-network-open-information.md) | The FILE_NETWORK_OPEN_INFORMATION structure is used as an argument to ZwQueryInformationFile. |
| [FILE_OBJECT structure](..\wdm\ns-wdm--file-object.md) | The FILE_OBJECT structure is used by the system to represent a file object. |
| [FILE_OBJECT structure](..\wdm\ns-wdm--file-object~r1.md) | The FILE_OBJECT structure is used by the system to represent a file object. |
| [FILE_OBJECT structure](..\wdm\ns-wdm--file-object~r2.md) | The FILE_OBJECT structure is used by the system to represent a file object. |
| [FILE_POSITION_INFORMATION structure](..\wdm\ns-wdm--file-position-information.md) | The FILE_POSITION_INFORMATION structure is used as an argument to routines that query or set file information. |
| [FILE_STANDARD_INFORMATION structure](..\wdm\ns-wdm--file-standard-information.md) | The FILE_STANDARD_INFORMATION structure is used as an argument to routines that query or set file information. |
| [FILE_STANDARD_INFORMATION_EX structure](..\wdm\ns-wdm--file-standard-information-ex.md) | The FILE_STANDARD_INFORMATION_EX structure is used as an argument to routines that query or set file information. |
| [FILE_VALID_DATA_LENGTH_INFORMATION structure](..\ntddk\ns-ntddk--file-valid-data-length-information.md) | The FILE_VALID_DATA_LENGTH_INFORMATION structure is used as an argument to ZwSetInformationFile. |
| [FUNCTION_LEVEL_DEVICE_RESET_PARAMETERS structure](..\wdm\ns-wdm--function-level-device-reset-parameters.md) | The FUNCTION_LEVEL_DEVICE_RESET_PARAMETER structure is used as an argument to the DeviceReset routine of the GUID_DEVICE_RESET_INTERFACE_STANDARD interface. |
| [GENERIC_MAPPING structure](..\wdm\ns-wdm--generic-mapping.md) | The GENERIC_MAPPING structure describes the ACCESS_MASK value of specific access rights associated with each type of generic access right. |
| [GROUP_AFFINITY structure](..\miniport\ns-miniport--group-affinity.md) | The GROUP_AFFINITY structure specifies a group number and the processor affinity within that group. |
| [HARDWARE_COUNTER structure](..\ntddk\ns-ntddk--hardware-counter.md) | The HARDWARE_COUNTER structure contains information about a hardware counter. |
| [HWPROFILE_CHANGE_NOTIFICATION structure](..\wdm\ns-wdm--hwprofile-change-notification.md) | The HWPROFILE_CHANGE_NOTIFICATION structure describes an event related to a hardware profile configuration change. |
| [IMAGE_INFO structure](..\ntddk\ns-ntddk--image-info.md) | Used by driver's load-image routine (PLOAD_IMAGE_NOTIFY_ROUTINE) to specify image information. |
| [IMAGE_INFO_EX structure](..\ntddk\ns-ntddk--image-info-ex.md) | Extended version of the image information structure (see IMAGE_INFO). |
| [INTERFACE structure](..\wdm\ns-wdm--interface.md) | The INTERFACE structure describes an interface that is exported by a driver for use by other drivers. |
| [IO_CONNECT_INTERRUPT_PARAMETERS structure](..\wdm\ns-wdm--io-connect-interrupt-parameters.md) | The IO_CONNECT_INTERRUPT_PARAMETERS structure contains the parameters that a driver supplies to the IoConnectInterruptEx routine to register an interrupt service routine (ISR). |
| [IO_DISCONNECT_INTERRUPT_PARAMETERS structure](..\wdm\ns-wdm--io-disconnect-interrupt-parameters.md) | The IO_DISCONNECT_INTERRUPT_PARAMETERS structure describes the parameters when unregistering an interrupt-handling routine with IoDisconnectInterruptEx. |
| [IO_ERROR_LOG_PACKET structure](..\wdm\ns-wdm--io-error-log-packet.md) | The IO_ERROR_LOG_PACKET structure serves as the header for an error log entry. |
| [IO_INTERRUPT_MESSAGE_INFO structure](..\wdm\ns-wdm--io-interrupt-message-info.md) | The IO_INTERRUPT_MESSAGE_INFO structure describes the driver's message-signaled interrupts. |
| [IO_INTERRUPT_MESSAGE_INFO_ENTRY structure](..\wdm\ns-wdm--io-interrupt-message-info-entry.md) | The IO_INTERRUPT_MESSAGE_INFO_ENTRY structure describes the properties of a single message-signaled interrupt. |
| [IO_REPORT_INTERRUPT_ACTIVE_STATE_PARAMETERS structure](..\wdm\ns-wdm--io-report-interrupt-active-state-parameters.md) | The IO_REPORT_INTERRUPT_ACTIVE_STATE_PARAMETERS structure contains the connection context for a registered interrupt service routine (ISR) that was connected to an interrupt or interrupts by a previous call to the IoConnectInterruptEx routine. |
| [IO_RESOURCE_DESCRIPTOR structure](..\wdm\ns-wdm--io-resource-descriptor.md) | The IO_RESOURCE_DESCRIPTOR structure describes a range of raw hardware resources, of one type, that can be used by a device. An array of IO_RESOURCE_DESCRIPTOR structures is contained within each IO_RESOURCE_LIST structure. |
| [IO_RESOURCE_LIST structure](..\wdm\ns-wdm--io-resource-list.md) | The IO_RESOURCE_LIST structure describes a range of raw hardware resources, of various types, that can be used by a device. |
| [IO_RESOURCE_REQUIREMENTS_LIST structure](..\wdm\ns-wdm--io-resource-requirements-list.md) | The IO_RESOURCE_REQUIREMENTS_LIST structure describes sets of resource configurations that can be used by a device. Each configuration represents a range of raw resources, of various types, that can be used by a device. |
| [IO_SECURITY_CONTEXT structure](..\wdm\ns-wdm--io-security-context.md) | The IO_SECURITY_CONTEXT structure represents the security context of an IRP_MJ_CREATE request. |
| [IO_SESSION_CONNECT_INFO structure](..\wdm\ns-wdm--io-session-connect-info.md) | The IO_SESSION_CONNECT_INFO structure provides information about a user session. |
| [IO_SESSION_STATE_INFORMATION structure](..\wdm\ns-wdm--io-session-state-information.md) | The IO_SESSION_STATE_INFORMATION structure contains information about the state of a user session. |
| [IO_SESSION_STATE_NOTIFICATION structure](..\wdm\ns-wdm--io-session-state-notification.md) | The IO_SESSION_STATE_NOTIFICATION structure contains information that a kernel-mode driver supplies to the IoRegisterContainerNotification routine when the driver registers to receive notifications of session events. |
| [IO_STACK_LOCATION structure](..\wdm\ns-wdm--io-stack-location.md) | The IO_STACK_LOCATION structure defines an I/O stack location, which is an entry in the I/O stack that is associated with each IRP. |
| [IO_STATUS_BLOCK structure](..\wdm\ns-wdm--io-status-block.md) | A driver sets an IRP's I/O status block to indicate the final status of an I/O request, before calling IoCompleteRequest for the IRP. |
| [IRP structure](..\ntifs\ns-ntifs--irp.md) | The IRP structure is a partially opaque structure that represents an I/O request packet. Drivers can use the following members of the IRP structure. |
| [IRP structure](..\wdm\ns-wdm--irp.md) | The IRP structure is a partially opaque structure that represents an I/O request packet. Drivers can use the following members of the IRP structure. |
| [KBUGCHECK_ADD_PAGES structure](..\wdm\ns-wdm--kbugcheck-add-pages.md) | The KBUGCHECK_ADD_PAGES structure describes one or more pages of driver-supplied data to be written by a BugCheckAddPagesCallback callback routine to the crash dump file. |
| [KBUGCHECK_DATA structure](..\aux_klib\ns-aux-klib--kbugcheck-data.md) | The KBUGCHECK_DATA structure contains bug check parameters. |
| [KBUGCHECK_DUMP_IO structure](..\wdm\ns-wdm--kbugcheck-dump-io.md) | The KBUGCHECK_DUMP_IO structure describes an I/O operation on the crash dump file. |
| [KBUGCHECK_SECONDARY_DUMP_DATA structure](..\wdm\ns-wdm--kbugcheck-secondary-dump-data.md) | The KBUGCHECK_SECONDARY_DUMP_DATA structure describes a section of driver-supplied data to be written by BugCheckSecondaryDumpDataCallback to the crash dump file. |
| [KDPC_WATCHDOG_INFORMATION structure](..\wdm\ns-wdm--kdpc-watchdog-information.md) | The KDPC_WATCHDOG_INFORMATION structure holds time-out information about the current deferred procedure call (DPC). |
| [KEY_BASIC_INFORMATION structure](..\wdm\ns-wdm--key-basic-information.md) | The KEY_BASIC_INFORMATION structure defines a subset of the full information that is available for a registry key. |
| [KEY_CACHED_INFORMATION structure](..\ntddk\ns-ntddk--key-cached-information.md) | The KEY_CACHED_INFORMATION structure holds the cached information available for a registry key or subkey. |
| [KEY_FULL_INFORMATION structure](..\wdm\ns-wdm--key-full-information.md) | The KEY_FULL_INFORMATION structure defines the information available for a registry key, including information about its subkeys and the maximum length for their names and value entries. |
| [KEY_NAME_INFORMATION structure](..\ntddk\ns-ntddk--key-name-information.md) | The KEY_NAME_INFORMATION structure holds the name and name length of the key. |
| [KEY_NODE_INFORMATION structure](..\wdm\ns-wdm--key-node-information.md) | The KEY_NODE_INFORMATION structure defines the basic information available for a registry (sub)key. |
| [KEY_VALUE_BASIC_INFORMATION structure](..\wdm\ns-wdm--key-value-basic-information.md) | The KEY_VALUE_BASIC_INFORMATION structure defines a subset of the full information available for a value entry of a registry key. |
| [KEY_VALUE_ENTRY structure](..\wdm\ns-wdm--key-value-entry.md) | The KEY_VALUE_ENTRY structure is used by the REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION structure to describe a single value entry for a registry key. |
| [KEY_VALUE_FULL_INFORMATION structure](..\wdm\ns-wdm--key-value-full-information.md) | The KEY_VALUE_FULL_INFORMATION structure defines information available for a value entry of a registry key. |
| [KEY_VALUE_PARTIAL_INFORMATION structure](..\wdm\ns-wdm--key-value-partial-information.md) | The KEY_VALUE_PARTIAL_INFORMATION structure defines a subset of the value information available for a value entry of a registry key. |
| [KEY_VIRTUALIZATION_INFORMATION structure](..\ntddk\ns-ntddk--key-virtualization-information.md) | The KEY_VIRTUALIZATION_INFORMATION structure defines the basic information that is available for a registry key or subkey. |
| [KEY_WRITE_TIME_INFORMATION structure](..\wdm\ns-wdm--key-write-time-information.md) | The KEY_WRITE_TIME_INFORMATION structure is used by the system to set the last write time for a registry key. |
| [KE_PROCESSOR_CHANGE_NOTIFY_CONTEXT structure](..\wdm\ns-wdm--ke-processor-change-notify-context.md) | The KE_PROCESSOR_CHANGE_NOTIFY_CONTEXT structure describes the notification context that is passed to a registered callback function when a new processor is dynamically added to a hardware partition. |
| [KTMOBJECT_CURSOR structure](..\wdm\ns-wdm--ktmobject-cursor.md) | The KTMOBJECT_CURSOR structure receives enumeration information about KTM objects when a component calls ZwEnumerateTransactionObject. |
| [LINK_SHARE_ACCESS structure](..\wdm\ns-wdm--link-share-access.md) | The share access structure used by file systems for only link files. |
| [MDL structure](..\wdm\ns-wdm--mdl.md) | An MDL structure is a partially opaque structure that represents a memory descriptor list (MDL). |
| [MEMORY_BASIC_INFORMATION structure](..\ntifs\ns-ntifs--memory-basic-information.md) | Contains information about a range of pages in the virtual address space of a process. |
| [MM_COPY_ADDRESS structure](..\ntddk\ns-ntddk--mm-copy-address.md) | The MM_COPY_ADDRESS structure contains either a virtual memory address or a physical memory address. |
| [MM_PHYSICAL_ADDRESS_LIST structure](..\wdm\ns-wdm--mm-physical-address-list.md) | The MM_PHYSICAL_ADDRESS_LIST structure specifies a range of physical addresses. |
| [NLSTABLEINFO structure](..\ntnls\ns-ntnls--nlstableinfo.md) | Stores the NLS file formats . |
| [OBJECT_ATTRIBUTES structure](..\d3dkmthk\ns-d3dkmthk--object-attributes.md) | The OBJECT_ATTRIBUTES structure specifies attributes that can be applied to objects or object handles by routines that create objects and/or return handles to objects. |
| [OB_CALLBACK_REGISTRATION structure](..\wdm\ns-wdm--ob-callback-registration.md) | The OB_CALLBACK_REGISTRATION structure specifies the parameters when the ObRegisterCallbacks routine registers ObjectPreCallback and ObjectPostCallback callback routines. |
| [OB_OPERATION_REGISTRATION structure](..\wdm\ns-wdm--ob-operation-registration.md) | The OB_OPERATION_REGISTRATION structure specifies ObjectPreCallback and ObjectPostCallback callback routines and the types of operations that the routines are called for. |
| [OB_POST_CREATE_HANDLE_INFORMATION structure](..\wdm\ns-wdm--ob-post-create-handle-information.md) | The OB_POST_CREATE_HANDLE_INFORMATION structure provides information to a ObjectPostCallback routine about a thread or process handle that has been opened. |
| [OB_POST_DUPLICATE_HANDLE_INFORMATION structure](..\wdm\ns-wdm--ob-post-duplicate-handle-information.md) | The OB_POST_DUPLICATE_HANDLE_INFORMATION structure provides information to an ObjectPostCallback routine about a thread or process handle that has been duplicated. |
| [OB_POST_OPERATION_INFORMATION structure](..\wdm\ns-wdm--ob-post-operation-information.md) | The OB_POST_OPERATION_INFORMATION structure provides information about a process or thread handle operation to an ObjectPostCallback routine. |
| [OB_POST_OPERATION_PARAMETERS structure](..\wdm\ns-wdm--ob-post-operation-parameters.md) | The OB_POST_OPERATION_PARAMETERS union describes the operation-specific parameters for an ObjectPostCallback routine. |
| [OB_PRE_CREATE_HANDLE_INFORMATION structure](..\wdm\ns-wdm--ob-pre-create-handle-information.md) | The OB_PRE_CREATE_HANDLE_INFORMATION structure provides information to an ObjectPreCallback routine about a thread or process handle that is being opened. |
| [OB_PRE_DUPLICATE_HANDLE_INFORMATION structure](..\wdm\ns-wdm--ob-pre-duplicate-handle-information.md) | The OB_PRE_DUPLICATE_HANDLE_INFORMATION structure provides information to an ObjectPreCallback routine about a thread or process handle that is being duplicated. |
| [OB_PRE_OPERATION_INFORMATION structure](..\wdm\ns-wdm--ob-pre-operation-information.md) | The OB_PRE_OPERATION_INFORMATION structure provides information about a process or thread handle operation to an ObjectPreCallback routine. |
| [OB_PRE_OPERATION_PARAMETERS structure](..\wdm\ns-wdm--ob-pre-operation-parameters.md) | The OB_PRE_OPERATION_PARAMETERS union describes the operation-specific parameters for an ObjectPreCallback routine. |
| [OSVERSIONINFOEXW structure](..\wdm\ns-wdm--osversioninfoexw.md) | The RTL_OSVERSIONINFOEXW structure contains operating system version information. |
| [OSVERSIONINFOW structure](..\wdm\ns-wdm--osversioninfow.md) | The RTL_OSVERSIONINFOW structure contains operating system version information. |
| [PCI_COMMON_CONFIG structure](..\wdm\ns-wdm--pci-common-config.md) | The PCI_COMMON_CONFIG structure is obsolete. |
| [PCI_COMMON_CONFIG structure](..\wdm\ns-wdm--pci-common-config~r1.md) | The PCI_COMMON_CONFIG structure is obsolete. |
| [PCI_MSIX_TABLE_CONFIG_INTERFACE structure](..\wdm\ns-wdm--pci-msix-table-config-interface.md) | The PCI_MSIX_TABLE_CONFIG_INTERFACE structure enables device drivers to modify their MSI-X interrupt settings. This structure describes the GUID_MSIX_TABLE_CONFIG_INTERFACE interface. |
| [PCI_SLOT_NUMBER structure](..\wdm\ns-wdm--pci-slot-number.md) | The PCI_SLOT_NUMBER structure is obsolete. |
| [PCI_VIRTUALIZATION_INTERFACE structure](..\wdm\ns-wdm--pci-virtualization-interface.md) | The PCI_VIRTUALIZATION_INTERFACE structure enables drivers to manage and configure the PCI Express (PCIe) configuration space for a virtual function (VF). |
| [PEP_ABANDON_DEVICE structure](..\pepfx\ns-pepfx--pep-abandon-device.md) | The PEP_ABANDON_DEVICE structure identifies a device that has been abandoned and will no longer be used by the operating system. |
| [PEP_ACPI_ABANDON_DEVICE structure](..\pepfx\ns-pepfx--pep-acpi-abandon-device.md) | The PEP_ACPI_ABANDON_DEVICE structure indicates whether the platform extension plug-in (PEP) accepts ownership of an abandoned device. |
| [PEP_ACPI_ENUMERATE_DEVICE_NAMESPACE structure](..\pepfx\ns-pepfx--pep-acpi-enumerate-device-namespace.md) | The PEP_ACPI_ENUMERATE_DEVICE_NAMESPACE structure contains an enumeration of the objects in the namespace of the device. |
| [PEP_ACPI_EVALUATE_CONTROL_METHOD structure](..\pepfx\ns-pepfx--pep-acpi-evaluate-control-method.md) | The PEP_ACPI_EVALUATE_CONTROL_METHOD structure specifies an ACPI control method to evaluate, an input argument to supply to this method, and an output buffer for the result of the evaluation. |
| [PEP_ACPI_EXTENDED_ADDRESS structure](..\pepfx\ns-pepfx--pep-acpi-extended-address.md) | The PEP_ACPI_EXTENDED_ADDRESS structure is used to report resource usage in the address space such as memory and IO. |
| [PEP_ACPI_GPIO_RESOURCE structure](..\pepfx\ns-pepfx--pep-acpi-gpio-resource.md) | The PEP_ACPI_GPIO_RESOURCE structure describes the ACPI configuration for a general purpose input/output (GPIO) resource. |
| [PEP_ACPI_INTERRUPT_RESOURCE structure](..\pepfx\ns-pepfx--pep-acpi-interrupt-resource.md) | The PEP_ACPI_INTERRUPT_RESOURCE structure describes an ACPI interrupt resource. |
| [PEP_ACPI_IO_MEMORY_RESOURCE structure](..\pepfx\ns-pepfx--pep-acpi-io-memory-resource.md) | The PEP_ACPI_IO_MEMORY_RESOURCE structure describes an ACPI IO port descriptor resource. |
| [PEP_ACPI_OBJECT_NAME structure](..\pepfx\ns-pepfx--pep-acpi-object-name.md) | The PEP_ACPI_OBJECT_NAME union contains the four-character name of an ACPI object. |
| [PEP_ACPI_OBJECT_NAME_WITH_TYPE structure](..\pepfx\ns-pepfx--pep-acpi-object-name-with-type.md) | The PEP_ACPI_OBJECT_NAME_WITH_TYPE structure that specifies both the path-relative name of an ACPI object and the type of this object. |
| [PEP_ACPI_PREPARE_DEVICE structure](..\pepfx\ns-pepfx--pep-acpi-prepare-device.md) | The PEP_ACPI_PREPARE_DEVICE structure indicates whether a platform extension plug-in (PEP) is prepared to provide ACPI services for the specified device. |
| [PEP_ACPI_QUERY_DEVICE_CONTROL_RESOURCES structure](..\pepfx\ns-pepfx--pep-acpi-query-device-control-resources.md) | The PEP_ACPI_QUERY_DEVICE_CONTROL_RESOURCES structure contains a list of raw resources that are needed to control power to the device. |
| [PEP_ACPI_QUERY_OBJECT_INFORMATION structure](..\pepfx\ns-pepfx--pep-acpi-query-object-information.md) | The PEP_ACPI_QUERY_OBJECT_INFORMATION structure contains information about an ACPI object. |
| [PEP_ACPI_REGISTER_DEVICE structure](..\pepfx\ns-pepfx--pep-acpi-register-device.md) | The PEP_ACPI_REGISTER_DEVICE structure contains registration information about a device for which the platform extension plug-in (PEP) is to provide ACPI services. |
| [PEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES structure](..\pepfx\ns-pepfx--pep-acpi-request-convert-to-bios-resources.md) | The PEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES structure is used in the process of converting ACPI resources to BIOS resources by one of the PEP initialization functions. |
| [PEP_ACPI_RESOURCE structure](..\pepfx\ns-pepfx--pep-acpi-resource.md) | The PEP_ACPI_RESOURCE structure contains hardware details for a specific ACPI resource. |
| [PEP_ACPI_RESOURCE_FLAGS structure](..\pepfx\ns-pepfx--pep-acpi-resource-flags.md) | The PEP_ACPI_RESOURCE_FLAGS structure contains flags describing an ACPI resource. |
| [PEP_ACPI_SPB_I2C_RESOURCE structure](..\pepfx\ns-pepfx--pep-acpi-spb-i2c-resource.md) | The PEP_ACPI_SPB_I2C_RESOURCE structure describes an ACPI I2C serial bus resource. |
| [PEP_ACPI_SPB_RESOURCE structure](..\pepfx\ns-pepfx--pep-acpi-spb-resource.md) | The PEP_ACPI_SPB_RESOURCE structure describes an ACPI serial bus connection resource. |
| [PEP_ACPI_SPB_SPI_RESOURCE structure](..\pepfx\ns-pepfx--pep-acpi-spb-spi-resource.md) | The PEP_ACPI_SPB_SPI_RESOURCE structure describes an ACPI SPI serial bus resource. |
| [PEP_ACPI_SPB_UART_RESOURCE structure](..\pepfx\ns-pepfx--pep-acpi-spb-uart-resource.md) | The PEP_ACPI_SPB_UART_RESOURCE structure describes an ACPI UART serial bus resource. |
| [PEP_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES structure](..\pepfx\ns-pepfx--pep-acpi-translated-device-control-resources.md) | The PEP_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES structure contains a list of translated power-control resources for the platform extension plug-in (PEP) to use. |
| [PEP_ACPI_UNREGISTER_DEVICE structure](..\pepfx\ns-pepfx--pep-acpi-unregister-device.md) | The PEP_ACPI_UNREGISTER_DEVICE structure contains information about a device that has been unregistered from ACPI services. |
| [PEP_COMPONENT_ACTIVE structure](..\pep_x\ns-pep-x--pep-component-active.md) | The PEP_COMPONENT_ACTIVE structure identifies a component that is making a transition between the idle condition and the active condition. |
| [PEP_COMPONENT_PERF_INFO structure](..\pepfx\ns-pepfx--pep-component-perf-info.md) | The PEP_COMPONENT_PERF_INFO structure describes the performance states (P-states) of a component. |
| [PEP_COMPONENT_PERF_SET structure](..\pepfx\ns-pepfx--pep-component-perf-set.md) | The PEP_COMPONENT_PERF_SET structure describes the performance states (P-states) in a P-state set. |
| [PEP_COMPONENT_PERF_STATE_REQUEST structure](..\pepfx\ns-pepfx--pep-component-perf-state-request.md) | The PEP_COMPONENT_PERF_STATE_REQUEST structure specifies a performance state (P-state) set and a new performance level to assign to this set. |
| [PEP_COMPONENT_PLATFORM_CONSTRAINTS structure](..\pepfx\ns-pepfx--pep-component-platform-constraints.md) | The PEP_COMPONENT_PLATFORM_CONSTRAINTS structure describes the lowest-powered Fx state of that a component can be in when the platform is in a particular idle state. |
| [PEP_COMPONENT_V2 structure](..\pepfx\ns-pepfx--pep-component-v2.md) | The PEP_COMPONENT_V2 structure specifies the power state attributes of a component in the device. |
| [PEP_COORDINATED_DEPENDENCY_OPTION structure](..\pepfx\ns-pepfx--pep-coordinated-dependency-option.md) | The PEP_COORIDNATED_DEPENDENCY_OPTION structure describes a coordinated idle stateâ€™s dependency to the OS. |
| [PEP_COORDINATED_IDLE_STATE structure](..\pepfx\ns-pepfx--pep-coordinated-idle-state.md) | The PEP_COORIDNATED_IDLE_STATE structure describes a coordinated idle state to the OS. |
| [PEP_CRASHDUMP_INFORMATION structure](..\pepfx\ns-pepfx--pep-crashdump-information.md) | The PEP_CRASHDUMP_INFORMATION structure contains information about a crash-dump device. |
| [PEP_DEBUGGER_TRANSITION_REQUIREMENTS structure](..\pepfx\ns-pepfx--pep-debugger-transition-requirements.md) | The PEP_DEBUGGER_TRANSITION_REQUIREMENTS structure indicates the platform idle states for which the debugger device must be turned on. |
| [PEP_DEVICE_PLATFORM_CONSTRAINTS structure](..\pepfx\ns-pepfx--pep-device-platform-constraints.md) | The PEP_DEVICE_PLATFORM_CONSTRAINTS structure specifies the constraints for entry to the various Dx power states that are supported by a device. |
| [PEP_DEVICE_POWER_STATE structure](..\pepfx\ns-pepfx--pep-device-power-state.md) | The PEP_DEVICE_POWER_STATE structure indicates the status of a transition to a new Dx (device power) state. |
| [PEP_DEVICE_REGISTER_V2 structure](..\pepfx\ns-pepfx--pep-device-register-v2.md) | The PEP_DEVICE_REGISTER structure describes all the components in a particular device. |
| [PEP_DEVICE_STARTED structure](..\pepfx\ns-pepfx--pep-device-started.md) | The PEP_DEVICE_STARTED structure identifies a device whose driver has completed its registration with the Windows power management framework (PoFx). |
| [PEP_INFORMATION structure](..\pepfx\ns-pepfx--pep-information.md) | The PEP_INFORMATION structure specifies the interface that the platform extension plug-in (PEP) uses to receive notifications from the Windows power management framework (PoFx). |
| [PEP_KERNEL_INFORMATION_STRUCT_V3 structure](..\pepfx\ns-pepfx--pep-kernel-information-struct-v3.md) | The PEP_KERNEL_INFORMATION_STRUCT_V3 structure specifies the interface that the power extension plug-in (PEP) uses to request services from the Windows power management framework (PoFx). |
| [PEP_LOW_POWER_EPOCH structure](..\pepfx\ns-pepfx--pep-low-power-epoch.md) | The PEP_LOW_POWER_EPOCH structure is used to provide data for a PEP_DPM_LOW_POWER_EPOCH notification (deprecated). |
| [PEP_NOTIFY_COMPONENT_IDLE_STATE structure](..\pepfx\ns-pepfx--pep-notify-component-idle-state.md) | The PEP_NOTIFY_COMPONENT_IDLE_STATE structure contains status information about a component's pending transition to a new Fx power state. |
| [PEP_PERF_STATE structure](..\pepfx\ns-pepfx--pep-perf-state.md) | The PEP_PERF_STATE structure describes a performance state (P-state) in a P-state set in which the P-states are specified as a list of one or more discrete values. |
| [PEP_PLATFORM_IDLE_STATE structure](..\pepfx\ns-pepfx--pep-platform-idle-state.md) | The PEP_PLATFORM_IDLE_STATE structure specifies the properties of a platform idle state. |
| [PEP_PLATFORM_IDLE_STATE_UPDATE structure](..\pepfx\ns-pepfx--pep-platform-idle-state-update.md) | The PEP_PLATFORM_IDLE_STATE_UPDATE structure contains the updated properties of a platform idle state. |
| [PEP_POWER_CONTROL_COMPLETE structure](..\pepfx\ns-pepfx--pep-power-control-complete.md) | The PEP_POWER_CONTROL_COMPLETE structure contains status information for a power control operation that the PEP previously requested and that the device driver has completed. |
| [PEP_POWER_CONTROL_REQUEST structure](..\pepfx\ns-pepfx--pep-power-control-request.md) | The PEP_POWER_CONTROL_REQUEST structure contains a request from a driver for a power control operation. |
| [PEP_PPM_CONTEXT_QUERY_PARKING_PAGE structure](..\pepfx\ns-pepfx--pep-ppm-context-query-parking-page.md) | The PEP_PPM_CONTEXT_QUERY_PARKING_PAGE structure describes the parking page for a processor. |
| [PEP_PPM_CST_STATE structure](..\pepfx\ns-pepfx--pep-ppm-cst-state.md) | The PEP_PPM_CST_STATE structure specifies the properties of a C state (ACPI processor power state). |
| [PEP_PPM_CST_STATES structure](..\pepfx\ns-pepfx--pep-ppm-cst-states.md) | The PEP_PPM_CST_STATES structure specifies the properties of the C states (ACPI processor power states) that are supported for a processor. |
| [PEP_PPM_ENTER_SYSTEM_STATE structure](..\pepfx\ns-pepfx--pep-ppm-enter-system-state.md) | Used in the PEP_NOTIFY_PPM_ENTER_SYSTEM_STATE notification to notify PEP that the system is about to enter a system power state.  . |
| [PEP_PPM_FEEDBACK_READ structure](..\pepfx\ns-pepfx--pep-ppm-feedback-read.md) | The PEP_PPM_FEEDBACK_READ structure contains the value read from a processor performance feedback counter. |
| [PEP_PPM_IDLE_CANCEL structure](..\pep_x\ns-pep-x--pep-ppm-idle-cancel.md) | The PEP_PPM_IDLE_CANCEL structure indicates why the processor could not enter the previously selected idle state. |
| [PEP_PPM_IDLE_COMPLETE structure](..\pepfx\ns-pepfx--pep-ppm-idle-complete.md) | The PEP_PPM_IDLE_COMPLETE structure describe the idle states from which the processor and hardware platform are waking. |
| [PEP_PPM_IDLE_COMPLETE_V2 structure](..\pepfx\ns-pepfx--pep-ppm-idle-complete-v2.md) | The PEP_PPM_IDLE_COMPLETE_V2 structure describe the idle states from which the processor and hardware platform are waking. |
| [PEP_PPM_IDLE_EXECUTE structure](..\pepfx\ns-pepfx--pep-ppm-idle-execute.md) | The PEP_PPM_IDLE_EXECUTE structure specifies the idle state that the processor is to enter. |
| [PEP_PPM_IDLE_EXECUTE_V2 structure](..\pepfx\ns-pepfx--pep-ppm-idle-execute-v2.md) | The PEP_PPM_IDLE_EXECUTE_V2 structure specifies the idle state that the processor is to enter. |
| [PEP_PPM_IDLE_SELECT structure](..\pep_x\ns-pep-x--pep-ppm-idle-select.md) | The PEP_PPM_IDLE_SELECT structure describes the most energy-efficient idle state that the processor can enter and still satisfy the constraints specified by the operating system. |
| [PEP_PPM_INITIATE_WAKE structure](..\pepfx\ns-pepfx--pep-ppm-initiate-wake.md) | The PEP_PPM_INITIATE_WAKE structure indicates whether a processor requires an interrupt to wake up from an idle state. |
| [PEP_PPM_IS_PROCESSOR_HALTED structure](..\pepfx\ns-pepfx--pep-ppm-is-processor-halted.md) | The PEP_PPM_IS_PROCESSOR_HALTED structure indicates whether the processor is currently halted in its selected idle state. |
| [PEP_PPM_PARK_MASK structure](..\pepfx\ns-pepfx--pep-ppm-park-mask.md) | The PEP_PROCESSOR_PARK_MASK structure contains the current core parking mask. |
| [PEP_PPM_PARK_SELECTION structure](..\pepfx\ns-pepfx--pep-ppm-park-selection.md) | The PEP_PPM_PARK_SELECTION structure indicates the preferences of the operating system and platform extension plug-in (PEP) regarding which processors in the platform should be parked to reduce power consumption. |
| [PEP_PPM_PARK_SELECTION_V2 structure](..\pepfx\ns-pepfx--pep-ppm-park-selection-v2.md) | The PEP_PPM_PARK_SELECTION_V2 structure indicates the preferences of the operating system and platform extension plug-in (PEP) regarding which processors in the platform should be parked to reduce power consumption. |
| [PEP_PPM_PERF_CHECK_COMPLETE structure](..\pepfx\ns-pepfx--pep-ppm-perf-check-complete.md) | The PEP_PPM_PERF_CHECK_COMPLETE structure is used to inform the PEP of details regarding the completion of a periodic performance check evaluation. |
| [PEP_PPM_PERF_SET structure](..\pepfx\ns-pepfx--pep-ppm-perf-set.md) | The PEP_PPM_PERF_SET structure specifies the new performance level that the operating system is requesting for the processor. |
| [PEP_PPM_PERF_SET_STATE structure](..\pepfx\ns-pepfx--pep-ppm-perf-set-state.md) | Used in the PEP_NOTIFY_PPM_PERF_SET notification at runtime to set the current operating performance of the processor.  . |
| [PEP_PPM_PLATFORM_STATE_RESIDENCIES structure](..\pepfx\ns-pepfx--pep-ppm-platform-state-residencies.md) | The PEP_PPM_PLATFORM_STATE_RESIDENCIES structure contains the accumulated residency times and transition counts for the idle states that are supported by the hardware platform. |
| [PEP_PPM_PLATFORM_STATE_RESIDENCY structure](..\pepfx\ns-pepfx--pep-ppm-platform-state-residency.md) | The PEP_PPM_PLATFORM_STATE_RESIDENCY structure specifies the accumulated residency time and transition count for a particular platform idle state. |
| [PEP_PPM_QUERY_CAPABILITIES structure](..\pepfx\ns-pepfx--pep-ppm-query-capabilities.md) | The PEP_PPM_QUERY_CAPABILITIES structure contains information about the processor power management (PPM) capabilities of the platform extension plug-in (PEP). |
| [PEP_PPM_QUERY_COORDINATED_DEPENDENCY structure](..\pepfx\ns-pepfx--pep-ppm-query-coordinated-dependency.md) | The PEP_PPM_QUERY_COORDINATED_DEPENDENCY structure describes dependencies for coordinated idle states. |
| [PEP_PPM_QUERY_COORDINATED_STATES structure](..\pepfx\ns-pepfx--pep-ppm-query-coordinated-states.md) | The PEP_PPM_QUERY_COORDINATED_STATES structure contains information about each coordinated idle state that the platform extension plug-in (PEP) supports. |
| [PEP_PPM_QUERY_DISCRETE_PERF_STATES structure](..\pepfx\ns-pepfx--pep-ppm-query-discrete-perf-states.md) | Used in the PEP_NOTIFY_PPM_QUERY_DISCRETE_PERF_STATES notification that stores the list of discrete performance states that PEP supports, if the PEP_NOTIFY_PPM_QUERY_CAPABILITIES notification indicates support for discrete performance states. . |
| [PEP_PPM_QUERY_DOMAIN_INFO structure](..\pepfx\ns-pepfx--pep-ppm-query-domain-info.md) | Used in the PEP_NOTIFY_PPM_QUERY_DOMAIN_INFO notification that queries for information about a performance domain. . |
| [PEP_PPM_QUERY_FEEDBACK_COUNTERS structure](..\pepfx\ns-pepfx--pep-ppm-query-feedback-counters.md) | The PEP_PPM_QUERY_FEEDBACK_COUNTERS structure describes all the processor performance counters that the platform extension plug-in (PEP) supports for a particular processor. |
| [PEP_PPM_QUERY_IDLE_STATES structure](..\pep_x\ns-pep-x--pep-ppm-query-idle-states.md) | The PEP_PPM_QUERY_IDLE_STATES structure describes the idle states of a particular processor. |
| [PEP_PPM_QUERY_IDLE_STATES_V2 structure](..\pepfx\ns-pepfx--pep-ppm-query-idle-states-v2.md) | The PEP_PPM_QUERY_IDLE_STATES_V2 structure is used during processor initialization to query the platform extension plug-in (PEP) for a list of processor idle states that the processor supports. |
| [PEP_PPM_QUERY_LP_SETTINGS structure](..\pep_x\ns-pep-x--pep-ppm-query-lp-settings.md) | The PEP_PPM_QUERY_LP_SETTINGS structure contains a kernel handle to the registry key that contains the power optimization settings that the platform extension plug-in (PEP) has defined for each power scenario. |
| [PEP_PPM_QUERY_PERF_CAPABILITIES structure](..\pepfx\ns-pepfx--pep-ppm-query-perf-capabilities.md) | The PEP_PPM_QUERY_PERF_CAPABILITIES structure describes the performance capabilities of the processors in the specified processor performance domain. |
| [PEP_PPM_QUERY_PERF_CONSTRAINTS structure](..\pepfx\ns-pepfx--pep-ppm-query-perf-constraints.md) | The PEP_PPM_PERF_CONSTRAINTS structure describes the performance limits to apply to the processor. |
| [PEP_PPM_QUERY_PLATFORM_STATE structure](..\pepfx\ns-pepfx--pep-ppm-query-platform-state.md) | The PEP_PPM_QUERY_PLATFORM_STATE structure contains information about a platform idle state. |
| [PEP_PPM_QUERY_PLATFORM_STATES structure](..\pepfx\ns-pepfx--pep-ppm-query-platform-states.md) | The PEP_PPM_QUERY_PLATFORM_STATES structure specifies the number of platform idle states the hardware platform supports. |
| [PEP_PPM_QUERY_STATE_NAME structure](..\pepfx\ns-pepfx--pep-ppm-query-state-name.md) | The PEP_PPM_QUERY_STATE_NAME structure contains information about a specific coordinated or platform idle state. |
| [PEP_PPM_QUERY_VETO_REASON structure](..\pepfx\ns-pepfx--pep-ppm-query-veto-reason.md) | The PEP_PPM_QUERY_VETO_REASON structure supplies a wide-character, null-terminated string that contains a descriptive, human-readable name for a veto reason. |
| [PEP_PPM_QUERY_VETO_REASONS structure](..\pepfx\ns-pepfx--pep-ppm-query-veto-reasons.md) | The PEP_PPM_QUERY_VETO_REASONS structure specifies the total number of veto reasons that the PEP uses in calls to the ProcessorIdleVeto and PlatformIdleVeto routines. |
| [PEP_PPM_RESUME_FROM_SYSTEM_STATE structure](..\pepfx\ns-pepfx--pep-ppm-resume-from-system-state.md) | Used by the PEP_NOTIFY_PPM_RESUME_FROM_SYSTEM_STATE notification that notifies the PEP that the system has just resumed from a system power state. |
| [PEP_PPM_TEST_IDLE_STATE structure](..\pepfx\ns-pepfx--pep-ppm-test-idle-state.md) | The PEP_PPM_TEST_IDLE_STATE structure contains information about whether the processor can immediately enter a processor idle state. |
| [PEP_PREPARE_DEVICE structure](..\pepfx\ns-pepfx--pep-prepare-device.md) | The PEP_PREPARE_DEVICE structure identifies a device that must be started up in preparation for its use by the operating system. |
| [PEP_PROCESSOR_FEEDBACK_COUNTER structure](..\pepfx\ns-pepfx--pep-processor-feedback-counter.md) | The PEP_PROCESSOR_FEEDBACK_COUNTER structure describes a feedback counter to the operating system. |
| [PEP_PROCESSOR_IDLE_CONSTRAINTS structure](..\pep_x\ns-pep-x--pep-processor-idle-constraints.md) | The PEP_PROCESSOR_IDLE_CONSTRAINTS structure specifies a set of constraints that the PEP uses to select a processor idle state. |
| [PEP_PROCESSOR_IDLE_DEPENDENCY structure](..\pepfx\ns-pepfx--pep-processor-idle-dependency.md) | The PEP_PROCESSOR_IDLE_DEPENDENCY structure specifies the dependencies of a platform idle state on the specified processor. |
| [PEP_PROCESSOR_IDLE_STATE structure](..\pep_x\ns-pep-x--pep-processor-idle-state.md) | The PEP_PROCESSOR_IDLE_STATE structure describes the capabilities of a processor idle state. |
| [PEP_PROCESSOR_IDLE_STATE_UPDATE structure](..\pepfx\ns-pepfx--pep-processor-idle-state-update.md) | The PEP_PROCESSOR_IDLE_STATE_UPDATE structure contains the updated properties of a processor idle state. |
| [PEP_PROCESSOR_IDLE_STATE_V2 structure](..\pepfx\ns-pepfx--pep-processor-idle-state-v2.md) | The PEP_PROCESSOR_IDLE_STATE_V2 structure describes a processor idle state that the platform extension plug-in (PEP) supports. |
| [PEP_PROCESSOR_PARK_PREFERENCE structure](..\pepfx\ns-pepfx--pep-processor-park-preference.md) | The PEP_PROCESSOR_PARK_PREFERENCE structure indicates the preferences of the operating system and platform extension plug-in (PEP) regarding whether the specified processor should be parked to reduce power consumption. |
| [PEP_PROCESSOR_PARK_STATE structure](..\pepfx\ns-pepfx--pep-processor-park-state.md) | The PEP_PROCESSOR_PARK_STATE structure describes the parking state for a single processor. |
| [PEP_PROCESSOR_PERF_STATE structure](..\pepfx\ns-pepfx--pep-processor-perf-state.md) | Use in the PEP_NOTIFY_PPM_QUERY_DISCRETE_PERF_STATES  notification. This structure describes the properties of a single performance state.  . |
| [PEP_QUERY_COMPONENT_PERF_CAPABILITIES structure](..\pepfx\ns-pepfx--pep-query-component-perf-capabilities.md) | The PEP_QUERY_COMPONENT_PERF_CAPABILITIES structure specifies the number of performance state (P-state) sets that are defined for a component. |
| [PEP_QUERY_COMPONENT_PERF_SET structure](..\pepfx\ns-pepfx--pep-query-component-perf-set.md) | The PEP_QUERY_COMPONENT_PERF_SET structure contains query information about a set of performance state values (P-state set) for a component. |
| [PEP_QUERY_COMPONENT_PERF_SET_NAME structure](..\pepfx\ns-pepfx--pep-query-component-perf-set-name.md) | The PEP_QUERY_COMPONENT_PERF_SET_NAME structure contains query information about a set of performance state values (P-state set) for a component. |
| [PEP_QUERY_COMPONENT_PERF_STATES structure](..\pepfx\ns-pepfx--pep-query-component-perf-states.md) | The PEP_QUERY_COMPONENT_PERF_STATES structure contains a list of discrete performance state (P-state) values for the specified P-state set. |
| [PEP_QUERY_CURRENT_COMPONENT_PERF_STATE structure](..\pepfx\ns-pepfx--pep-query-current-component-perf-state.md) | The PEP_QUERY_CURRENT_COMPONENT_PERF_STATE structure contains information about the current P-state in the specified P-state set. |
| [PEP_QUERY_SOC_SUBSYSTEM structure](..\pepfx\ns-pepfx--pep-query-soc-subsystem.md) | The PEP_QUERY_SOC_SUBSYSTEM structure is used by the PEP_DPM_QUERY_SOC_SUBSYSTEM notification to gather basic information about a particular system on a chip (SoC) subsystem. |
| [PEP_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME structure](..\pepfx\ns-pepfx--pep-query-soc-subsystem-blocking-time.md) | The PEP_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME structure is used by the PEP_DPM_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME notification to collect details about the blocking duration for a particular system on a chip (SoC) subsystem. |
| [PEP_QUERY_SOC_SUBSYSTEM_COUNT structure](..\pepfx\ns-pepfx--pep-query-soc-subsystem-count.md) | The PEP_QUERY_SOC_SUBSYSTEM_COUNT structure is used to tell the OS whether the PEP supports system on a chip (SoC) subsystem accounting for a given platform idle state. |
| [PEP_QUERY_SOC_SUBSYSTEM_METADATA structure](..\pepfx\ns-pepfx--pep-query-soc-subsystem-metadata.md) | The PEP_QUERY_SOC_SUBSYSTEM_METADATA structure is used with the PEP_DPM_QUERY_SOC_SUBSYSTEM_METADATA notification to collect optional metadata about the system on a chip (SoC) subsystem whose blocking time has just been queried. |
| [PEP_REGISTER_COMPONENT_PERF_STATES structure](..\pepfx\ns-pepfx--pep-register-component-perf-states.md) | The PEP_REGISTER_COMPONENT_PERF_STATES structure describes the performance states (P-states) of the specified component. |
| [PEP_REGISTER_CRASHDUMP_DEVICE structure](..\pepfx\ns-pepfx--pep-register-crashdump-device.md) | The PEP_REGISTER_CRASHDUMP_DEVICE structure provides a callback routine to turn on a crash-dump device. |
| [PEP_REGISTER_DEBUGGER structure](..\pepfx\ns-pepfx--pep-register-debugger.md) | The PEP_REGISTER_DEBUGGER structure identifies a registered device that is a core system resource that provides debugger transport. |
| [PEP_REGISTER_DEVICE_V2 structure](..\pepfx\ns-pepfx--pep-register-device-v2.md) | The PEP_REGISTER_DEVICE_V2 structure describes a device whose driver stack has just registered with the Windows power management framework (PoFx). |
| [PEP_REQUEST_COMPONENT_PERF_STATE structure](..\pepfx\ns-pepfx--pep-request-component-perf-state.md) | The PEP_REQUEST_COMPONENT_PERF_STATE structure contains a list of performance state (P-state) changes requested by the Windows power management framework (PoFx), plus status information about the handling of these requests by the platform extension plug-in (PEP). |
| [PEP_RESET_SOC_SUBSYSTEM_ACCOUNTING structure](..\pepfx\ns-pepfx--pep-reset-soc-subsystem-accounting.md) | The PEP_RESET_SOC_SUBSYSTEM_ACCOUNTING structure is provided to the platform extension plug-in (PEP) as part of a PEP_DPM_RESET_SOC_SUBSYSTEM_ACCOUNTING notification. |
| [PEP_SOC_SUBSYSTEM_METADATA structure](..\pepfx\ns-pepfx--pep-soc-subsystem-metadata.md) | The PEP_SOC_SUBSYSTEM_METADATA structure contains key-value pairs that contain metadata for a system on a chip (SoC) subsystem. It is used in the context of a PEP_DPM_QUERY_SOC_SUBSYSTEM_METADATA notification sent to a platform extension plug-in (PEP). |
| [PEP_SYSTEM_LATENCY structure](..\pepfx\ns-pepfx--pep-system-latency.md) | The PEP_SYSTEM_LATENCY structure specifies the new value for the system latency tolerance. |
| [PEP_UNMASKED_INTERRUPT_FLAGS structure](..\pepfx\ns-pepfx--pep-unmasked-interrupt-flags.md) | The PEP_UNMASKED_INTERRUPT_FLAGS union indicates whether an unmasked interrupt source is a primary interrupt or a secondary interrupt. |
| [PEP_UNMASKED_INTERRUPT_INFORMATION structure](..\pepfx\ns-pepfx--pep-unmasked-interrupt-information.md) | The PEP_UNMASKED_INTERRUPT_INFORMATION structure contains information about an interrupt source. |
| [PEP_UNREGISTER_DEVICE structure](..\pepfx\ns-pepfx--pep-unregister-device.md) | The PEP_UNREGISTER_DEVICE structure identifies a device whose registration is being removed from the Windows power management framework (PoFx). |
| [PEP_WORK structure](..\pepfx\ns-pepfx--pep-work.md) | The PEP_WORK structure indicates whether the PEP has a work request to submit to the Windows power management framework (PoFx). |
| [PEP_WORK_ACPI_EVALUATE_CONTROL_METHOD_COMPLETE structure](..\pepfx\ns-pepfx--pep-work-acpi-evaluate-control-method-complete.md) | The PEP_WORK_ACPI_EVALUATE_CONTROL_METHOD_COMPLETE structure contains the results of an ACPI control method that was asynchronously evaluated by the platform extension plug-in (PEP). |
| [PEP_WORK_ACPI_NOTIFY structure](..\pepfx\ns-pepfx--pep-work-acpi-notify.md) | The PEP_WORK_ACPI_NOTIFY structure contains the ACPI Notify code for a device that has generated a hardware event. |
| [PEP_WORK_ACTIVE_COMPLETE structure](..\pep_x\ns-pep-x--pep-work-active-complete.md) | The PEP_WORK_ACTIVE_COMPLETE structure identifies a component that is now in the active condition. |
| [PEP_WORK_COMPLETE_IDLE_STATE structure](..\pepfx\ns-pepfx--pep-work-complete-idle-state.md) | The PEP_WORK_COMPLETE_IDLE_STATE structure identifies a component that the platform extension plug-in (PEP) has prepared for a transition to a new Fx power state. |
| [PEP_WORK_COMPLETE_PERF_STATE structure](..\pepfx\ns-pepfx--pep-work-complete-perf-state.md) | The PEP_WORK_COMPLETE_PERF_STATE structure describes the completion status of a previously requested update to the performance values assigned to a list of performance state (P-state) sets. |
| [PEP_WORK_DEVICE_IDLE structure](..\pep_x\ns-pep-x--pep-work-device-idle.md) | The PEP_WORK_DEVICE_IDLE structure indicates whether to ignore the idle time-out for the specified device. |
| [PEP_WORK_DEVICE_POWER structure](..\pep_x\ns-pep-x--pep-work-device-power.md) | The PEP_WORK_DEVICE_POWER structure describes the new power requirements for the specified device. |
| [PEP_WORK_IDLE_STATE structure](..\pep_x\ns-pep-x--pep-work-idle-state.md) | The PEP_WORK_IDLE_STATE structure contains a request to transition a component to an Fx power state. |
| [PEP_WORK_INFORMATION structure](..\pepfx\ns-pepfx--pep-work-information.md) | The PEP_WORK_INFORMATION structure describes a work item that the PEP is submitting to the Windows power management framework (PoFx). |
| [PEP_WORK_POWER_CONTROL structure](..\pepfx\ns-pepfx--pep-work-power-control.md) | The PEP_WORK_POWER_CONTROL structure contains the parameters for a power control request that the platform extension plug-in (PEP) sends directly to a processor driver. |
| [PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structure](..\ntddk\ns-ntddk--physical-counter-resource-descriptor.md) | The PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structure describes the counter resources available on the platform. |
| [PHYSICAL_COUNTER_RESOURCE_LIST structure](..\ntddk\ns-ntddk--physical-counter-resource-list.md) | The PHYSICAL_COUNTER_RESOURCE_LIST structure describes an array of PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structures. |
| [PLUGPLAY_NOTIFICATION_HEADER structure](..\wdm\ns-wdm--plugplay-notification-header.md) | A PLUGPLAY_NOTIFICATION_HEADER structure is included at the beginning of each PnP notification structure, such as a DEVICE_INTERFACE_CHANGE_NOTIFICATION structure. |
| [PNP_BUS_INFORMATION structure](..\wdm\ns-wdm--pnp-bus-information.md) | The PNP_BUS_INFORMATION structure describes a bus. |
| [PNP_LOCATION_INTERFACE structure](..\ntddk\ns-ntddk--pnp-location-interface.md) | The PNP_LOCATION_INTERFACE structure describes the GUID_PNP_LOCATION_INTERFACE interface. |
| [POWER_PLATFORM_INFORMATION structure](..\wdm\ns-wdm--power-platform-information.md) | The POWER_PLATFORM_INFORMATION structure contains information about the power capabilities of the system. |
| [POWER_STATE structure](..\wdm\ns-wdm--power-state.md) | The POWER_STATE union specifies a system power state value or a device power state value. |
| [POWER_THROTTLING_PROCESS_STATE structure](..\ntddk\ns-ntddk--power-throttling-process-state.md) | Stores the throttling policies and how to apply them to a target process when that process is subject to power management. |
| [POWER_THROTTLING_THREAD_STATE structure](..\ntddk\ns-ntddk--power-throttling-thread-state.md) | Stores the throttling policies and how to apply them to a target thread when that thread is subject to power management. |
| [PO_FX_COMPONENT_IDLE_STATE structure](..\wdm\ns-wdm--po-fx-component-idle-state.md) | The PO_FX_COMPONENT_IDLE_STATE structure specifies the attributes of an Fx power state of a component in a device. |
| [PO_FX_COMPONENT_PERF_INFO structure](..\wdm\ns-wdm--po-fx-component-perf-info.md) | The PO_FX_COMPONENT_PERF_INFO structure describes all the sets of performance states for a single component within a device. |
| [PO_FX_COMPONENT_PERF_SET structure](..\wdm\ns-wdm--po-fx-component-perf-set.md) | The PO_FX_COMPONENT_PERF_SET structure represents a set of performance states for a single component within a device. |
| [PO_FX_CORE_DEVICE structure](..\pepfx\ns-pepfx--po-fx-core-device.md) | The PO_FX_CORE_DEVICE structure contains information about the power-state attributes of the components in a core system resource, and provides a software interface for power-managing these components. |
| [PO_FX_PERF_STATE structure](..\wdm\ns-wdm--po-fx-perf-state.md) | The PO_FX_PERF_STATE structure represents a performance state for a single component within a device. |
| [PO_FX_PERF_STATE_CHANGE structure](..\wdm\ns-wdm--po-fx-perf-state-change.md) | The PO_FX_PERF_STATE_CHANGE structure contains information about a change to a performance state that is being requested by calling the PoFxIssueComponentPerfStateChange or PoFxIssueComponentPerfStateChangeMultiple routine. |
| [PRIVILEGE_SET structure](..\wdm\ns-wdm--privilege-set.md) | The PRIVILEGE_SET structure specifies a set of security privileges. For more information, see the reference page for PRIVILEGE_SET in the Microsoft Windows SDK documentation. |
| [PROCESSOR_NUMBER structure](..\miniport\ns-miniport--processor-number.md) | The PROCESSOR_NUMBER structure identifies a processor by its group number and group-relative processor number. |
| [PROCESS_MITIGATION_CHILD_PROCESS_POLICY structure](..\ntddk\ns-ntddk--process-mitigation-child-process-policy.md) | Stores policy information about creating child processes. |
| [PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY structure](..\ntddk\ns-ntddk--process-mitigation-payload-restriction-policy.md) | Stores information about process mitigation policy. |
| [PROCESS_READWRITEVM_LOGGING_INFORMATION structure](..\ntddk\ns-ntddk--process-readwritevm-logging-information.md) | Stores options for read/write access for telemetry per process. |
| [PS_CREATE_NOTIFY_INFO structure](..\ntddk\ns-ntddk--ps-create-notify-info.md) | The PS_CREATE_NOTIFY_INFO structure provides information about a newly created process. |
| [REENUMERATE_SELF_INTERFACE_STANDARD structure](..\wdm\ns-wdm--reenumerate-self-interface-standard.md) | The REENUMERATE_SELF_INTERFACE_STANDARD interface structure enables a driver to request that its parent bus driver reenumerate the driver's device. This structure defines the GUID_REENUMERATE_SELF_INTERFACE_STANDARD interface. |
| [REG_CALLBACK_CONTEXT_CLEANUP_INFORMATION structure](..\wdm\ns-wdm--reg-callback-context-cleanup-information.md) | The REG_CALLBACK_CONTEXT_CLEANUP_INFORMATION structure contains information that a driver's RegistryCallback routine can use to free resources that the driver previously allocated for the context that is associated with a registry object. |
| [REG_CREATE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-create-key-information.md) | The REG_CREATE_KEY_INFORMATION structure contains information that a driver's RegistryCallback routine can use when a registry key that is being created. |
| [REG_CREATE_KEY_INFORMATION_V1 structure](..\wdm\ns-wdm--reg-create-key-information-v1.md) | The REG_CREATE_KEY_INFORMATION_V1 structure contains information that a filter driver's RegistryCallback routine can use when a registry key is being created. |
| [REG_DELETE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-delete-key-information.md) | The REG_DELETE_KEY_INFORMATION structure contains information that a driver's RegistryCallback routine can use when a registry key is being deleted. |
| [REG_DELETE_VALUE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-delete-value-key-information.md) | The REG_DELETE_VALUE_KEY_INFORMATION structure contains information that a driver's RegistryCallback routine can use when a registry key's value is being deleted. |
| [REG_ENUMERATE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-enumerate-key-information.md) | The REG_ENUMERATE_KEY_INFORMATION structure describes one subkey of a key whose subkeys are being enumerated. |
| [REG_ENUMERATE_VALUE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-enumerate-value-key-information.md) | The REG_ENUMERATE_VALUE_KEY_INFORMATION structure describes one value entry of a key whose value entries are being enumerated. |
| [REG_KEY_HANDLE_CLOSE_INFORMATION structure](..\wdm\ns-wdm--reg-key-handle-close-information.md) | The REG_KEY_HANDLE_CLOSE_INFORMATION structure contains information about a registry key whose handle is about to be closed. |
| [REG_LOAD_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-load-key-information.md) | The REG_LOAD_KEY_INFORMATION structure contains information about a registry hive that is being loaded. |
| [REG_POST_CREATE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-post-create-key-information.md) | The REG_POST_CREATE_KEY_INFORMATION structure contains the result of an attempt to create a registry key. |
| [REG_POST_OPERATION_INFORMATION structure](..\wdm\ns-wdm--reg-post-operation-information.md) | The REG_POST_OPERATION_INFORMATION structure contains information about a completed registry operation that a RegistryCallback routine can use. |
| [REG_PRE_CREATE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-pre-create-key-information.md) | The REG_PRE_CREATE_KEY_INFORMATION structure contains the name of a registry key that is about to be created. |
| [REG_QUERY_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-query-key-information.md) | The REG_QUERY_KEY_INFORMATION structure describes the metadata that is about to be queried for a key. |
| [REG_QUERY_KEY_NAME structure](..\wdm\ns-wdm--reg-query-key-name.md) | The REG_QUERY_KEY_NAME structure describes the full registry key name of an object being queried. |
| [REG_QUERY_KEY_SECURITY_INFORMATION structure](..\wdm\ns-wdm--reg-query-key-security-information.md) | The REG_QUERY_KEY_SECURITY_INFORMATION structure receives security information for a registry key object. |
| [REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-query-multiple-value-key-information.md) | The REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION structure describes the multiple value entries that are being retrieved for a key. |
| [REG_QUERY_VALUE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-query-value-key-information.md) | The REG_QUERY_VALUE_KEY_INFORMATION structure contains information about a registry key's value entry that is being queried. |
| [REG_RENAME_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-rename-key-information.md) | The REG_RENAME_KEY_INFORMATION structure contains the new name for a registry key whose name is about to be changed. |
| [REG_REPLACE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-replace-key-information.md) | The REG_REPLACE_KEY_INFORMATION structure describes the metadata that is about to be replaced for a key. |
| [REG_RESTORE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-restore-key-information.md) | The REG_RESTORE_KEY_INFORMATION structure contains the information for a registry key that is about to be restored. |
| [REG_SAVE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-save-key-information.md) | The REG_SAVE_KEY_INFORMATION structure contains the information for a registry key that is about to be saved. |
| [REG_SET_INFORMATION_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-set-information-key-information.md) | The REG_SET_INFORMATION_KEY_INFORMATION structure describes a new setting for a key's metadata. |
| [REG_SET_KEY_SECURITY_INFORMATION structure](..\wdm\ns-wdm--reg-set-key-security-information.md) | The REG_SET_KEY_SECURITY_INFORMATION structure specifies security information for a registry key object. |
| [REG_SET_VALUE_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-set-value-key-information.md) | The REG_SET_VALUE_INFORMATION structure describes a new setting for a registry key's value entry. |
| [REG_UNLOAD_KEY_INFORMATION structure](..\wdm\ns-wdm--reg-unload-key-information.md) | The REG_UNLOAD_KEY_INFORMATION structure contains information that a driver's RegistryCallback routine can use when a registry hive is unloaded. |
| [RESOURCEMANAGER_BASIC_INFORMATION structure](..\wdm\ns-wdm--resourcemanager-basic-information.md) | The RESOURCEMANAGER_BASIC INFORMATION structure contains information about a resource manager object. |
| [RESOURCEMANAGER_COMPLETION_INFORMATION structure](..\wdm\ns-wdm--resourcemanager-completion-information.md) | The RESOURCEMANAGER_COMPLETION_INFORMATION structure is not used. |
| [SCATTER_GATHER_LIST structure](..\wdm\ns-wdm--scatter-gather-list.md) | The SCATTER_GATHER_LIST structure describes the scatter/gather list for a DMA operation. |
| [SCATTER_GATHER_LIST structure](..\wdm\ns-wdm--scatter-gather-list~r1.md) | The SCATTER_GATHER_LIST structure describes the scatter/gather list for a DMA operation. |
| [SCATTER_GATHER_LIST structure](..\wdm\ns-wdm--scatter-gather-list~r2.md) | The SCATTER_GATHER_LIST structure describes the scatter/gather list for a DMA operation. |
| [SCATTER_GATHER_LIST structure](..\wdm\ns-wdm--scatter-gather-list~r3.md) | The SCATTER_GATHER_LIST structure describes the scatter/gather list for a DMA operation. |
| [SDEV_IDENTIFIER_INTERFACE structure](..\wdm\ns-wdm--sdev-identifier-interface.md) | TBD. |
| [SECTION_OBJECT_POINTERS structure](..\wdm\ns-wdm--section-object-pointers.md) | The SECTION_OBJECT_POINTERS structure, allocated by a file system or a redirector driver, is used by the memory manager and cache manager to store file-mapping and cache-related information for a file stream. |
| [SECURITY_DESCRIPTOR structure](..\ntifs\ns-ntifs--security-descriptor.md) | The SECURITY_DESCRIPTOR structure specifies the security information that is associated with an object. For more information, see the reference page for SECURITY_DESCRIPTOR in the Installable File System documentation. |
| [SILO_MONITOR_REGISTRATION structure](..\ntddk\ns-ntddk--silo-monitor-registration.md) | This structure specifies a server silo monitor that can receive notifications about server silo events. |
| [SINGLE_LIST_ENTRY structure](..\wdm\ns-wdm--single-list-entry.md) | A SINGLE_LIST_ENTRY structure describes an entry in a singly linked list, or serves as the header for such a list. |
| [SYSENV_VALUE structure](..\ntddsysenv\ns-ntddsysenv--sysenv-value.md) | Stores the value of a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_GET_VARIABLE request. |
| [SYSENV_VARIABLE structure](..\ntddsysenv\ns-ntddsysenv--sysenv-variable.md) | Stores the name a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_GET_VARIABLE request. |
| [SYSENV_VARIABLE_INFO structure](..\ntddsysenv\ns-ntddsysenv--sysenv-variable-info.md) | Stores the information about a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_QUERY_VARIABLE_INFO request. |
| [SYSTEM_POWER_STATE_CONTEXT structure](..\wdm\ns-wdm--system-power-state-context.md) | The SYSTEM_POWER_STATE_CONTEXT structure is a partially opaque system structure that contains information about the previous system power states of a computer. |
| [TARGET_DEVICE_CUSTOM_NOTIFICATION structure](..\wdm\ns-wdm--target-device-custom-notification.md) | The TARGET_DEVICE_CUSTOM_NOTIFICATION structure describes a custom device event. |
| [TARGET_DEVICE_REMOVAL_NOTIFICATION structure](..\wdm\ns-wdm--target-device-removal-notification.md) | The TARGET_DEVICE_REMOVAL_NOTIFICATION structure describes a device-removal event. The PnP manager sends this structure to a driver that registered a callback routine for notification of EventCategoryTargetDeviceChange events. |
| [THERMAL_COOLING_INTERFACE structure](..\poclass\ns-poclass--thermal-cooling-interface.md) | The THERMAL_COOLING_INTERFACE structure enables the operating system to control the thermal management settings of a device. |
| [TRANSACTIONMANAGER_BASIC_INFORMATION structure](..\wdm\ns-wdm--transactionmanager-basic-information.md) | The TRANSACTIONMANAGER_BASIC_INFORMATION structure contains information about a transaction manager object. |
| [TRANSACTIONMANAGER_LOGPATH_INFORMATION structure](..\wdm\ns-wdm--transactionmanager-logpath-information.md) | The TRANSACTIONMANAGER_LOGPATH_INFORMATION structure contains information about a transaction manager object. |
| [TRANSACTIONMANAGER_LOG_INFORMATION structure](..\wdm\ns-wdm--transactionmanager-log-information.md) | The TRANSACTIONMANAGER_LOG_INFORMATION structure contains information about a transaction manager object. |
| [TRANSACTIONMANAGER_RECOVERY_INFORMATION structure](..\wdm\ns-wdm--transactionmanager-recovery-information.md) | The TRANSACTIONMANAGER_RECOVERY_INFORMATION structure contains information about a transaction manager object. |
| [TRANSACTION_BASIC_INFORMATION structure](..\wdm\ns-wdm--transaction-basic-information.md) | The TRANSACTION_BASIC_INFORMATION structure contains information about a transaction object. |
| [TRANSACTION_ENLISTMENTS_INFORMATION structure](..\wdm\ns-wdm--transaction-enlistments-information.md) | The TRANSACTION_ENLISTMENTS_INFORMATION structure contains information about the enlistments that are associated with a transaction object. |
| [TRANSACTION_ENLISTMENT_PAIR structure](..\wdm\ns-wdm--transaction-enlistment-pair.md) | The TRANSACTION_ENLISTMENT_PAIR structure contains information about an enlistment that is associated with a transaction object. |
| [TRANSACTION_PROPERTIES_INFORMATION structure](..\wdm\ns-wdm--transaction-properties-information.md) | The TRANSACTION_PROPERTIES_INFORMATION structure contains a transaction object's properties. |
| [UNICODE_STRING structure](..\wudfwdm\ns-wudfwdm--unicode-string.md) | The UNICODE_STRING structure is used to define Unicode strings. |
| [VPCI_INVALIDATE_BLOCK_OUTPUT structure](..\vpci\ns-vpci--vpci-invalidate-block-output.md) | The VPCI_INVALIDATE_BLOCK_OUTPUT structure is used in an IOCTL_VPCI_INVALIDATE_BLOCK IOCTL request. |
| [VPCI_READ_BLOCK_INPUT structure](..\vpci\ns-vpci--vpci-read-block-input.md) | The VPCI_READ_BLOCK_INPUT structure is used in an IOCTL_VPCI_READ_BLOCK IOCTL request to read data from a specified configuration block of data for a PCI Express (PCIe) virtual function (VF). |
| [VPCI_WRITE_BLOCK_INPUT structure](..\vpci\ns-vpci--vpci-write-block-input.md) | The VPCI_WRITE_BLOCK_INPUT structure is used in an IOCTL_VPCI_WRITE_BLOCK IOCTL request to write data to a specified configuration block for a PCI Express (PCIe) virtual function (VF). |
| [WMIGUIDREGINFO structure](..\wmilib\ns-wmilib--wmiguidreginfo.md) | The WMIGUIDREGINFO structure contains registration information for a given data block or event block exposed by a driver that uses the WMI library support routines. |
| [WMILIB_CONTEXT structure](..\wmilib\ns-wmilib--wmilib-context.md) | The WMILIB_CONTEXT structure provides registration information for a driver's data blocks and event blocks and defines entry points for the driver's WMI library callback routines. |
| [WNODE_HEADER structure](..\wmistr\ns-wmistr--wnode-header.md) | The WNODE_HEADER structure is the first member of all other WNODE_XXX structures. It contains information common to all such structures. |
| [XVARIABLE_NAME structure](..\ntddsysenv\ns-ntddsysenv--xvariable-name.md) | Stores the name of a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_ENUM_VARIABLES request. |
| [XVARIABLE_NAME_AND_VALUE structure](..\ntddsysenv\ns-ntddsysenv--xvariable-name-and-value.md) | Stores the name and value of a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_ENUM_VARIABLES and IOCTL_SYSENV_SET_VARIABLE requests. |
| [tagWNODE_ALL_DATA structure](..\wmistr\ns-wmistr-tagwnode-all-data.md) | The WNODE_ALL_DATA structure contains data for all instances of a data block or event block. |
| [tagWNODE_EVENT_ITEM structure](..\wmistr\ns-wmistr-tagwnode-event-item.md) | The WNODE_EVENT_ITEM structure contains data generated by a driver for an event. |
| [tagWNODE_EVENT_REFERENCE structure](..\wmistr\ns-wmistr-tagwnode-event-reference.md) | The WNODE_EVENT_REFERENCE structure contains information that WMI can use to query for an event that exceeds the event size limit set in the registry. |
| [tagWNODE_METHOD_ITEM structure](..\wmistr\ns-wmistr-tagwnode-method-item.md) | The WNODE_METHOD_ITEM structure indicates a method associated with an instance of a data block and contains any input data for the method. |
| [tagWNODE_SINGLE_INSTANCE structure](..\wmistr\ns-wmistr-tagwnode-single-instance.md) | The WNODE_SINGLE_INSTANCE structure contains values for all data items in one instance of a data block. |
| [tagWNODE_SINGLE_ITEM structure](..\wmistr\ns-wmistr-tagwnode-single-item.md) | The WNODE_SINGLE_ITEM structure contains the value of a single data item in an instance of a data block. |
| [tagWNODE_TOO_SMALL structure](..\wmistr\ns-wmistr-tagwnode-too-small.md) | The WNODE_TOO_SMALL structure indicates the size of the buffer needed to receive output from a request. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [BDCB_CALLBACK_TYPE enumeration](..\ntddk\ne-ntddk--bdcb-callback-type.md) | The BDCB_CALLBACK_TYPE enumeration specifies whether the callback being passed to a BOOT_DRIVER_CALLBACK_FUNCTION routine is a status update or a boot-start driver initialization notification. |
| [BDCB_CLASSIFICATION enumeration](..\ntddk\ne-ntddk--bdcb-classification.md) | The BDCB_CLASSIFICATION enumeration lists different classifications of boot start images. |
| [BDCB_STATUS_UPDATE_TYPE enumeration](..\ntddk\ne-ntddk--bdcb-status-update-type.md) | The BDCB_STATUS_UPDATE_TYPE enumeration lists the types of boot-driver callback status updates. |
| [BOUND_CALLBACK_STATUS enumeration](..\wdm\ne-wdm--bound-callback-status.md) | The BOUND_CALLBACK_STATUS enumeration indicates how a user-mode bounds exception was processed by the BoundCallback function. |
| [BUS_DATA_TYPE enumeration](..\ntddk\ne-ntddk--bus-data-type.md) | The BUS_DATA_TYPE enumeration indicates the type of bus configuration space. |
| [CLFS_CONTEXT_MODE enumeration](..\wdm\ne-wdm--clfs-context-mode.md) | The CLFS_CONTEXT_MODE enumeration indicates the type of sequence that the Common Log File System (CLFS) driver follows when it reads a set of records from a stream. |
| [CLFS_MGMT_POLICY_TYPE enumeration](..\wdm\ne-wdm--clfs-mgmt-policy-type.md) | The CLFS_MGMT_POLICY_TYPE enumeration type identifies the type of a CLFS management policy. |
| [D3COLD_LAST_TRANSITION_STATUS enumeration](..\wdm\ne-wdm--d3cold-last-transition-status.md) | The D3COLD_LAST_TRANSITION_STATUS enumeration indicates whether the most recent transition to the D3hot device power state was followed by a transition to the D3cold device power state. |
| [DEVICE_INSTALL_STATE enumeration](..\wdm\ne-wdm--device-install-state.md) | The DEVICE_INSTALL_STATE enumeration describes a device's installation state. |
| [DEVICE_POWER_STATE enumeration](..\wdm\ne-wdm--device-power-state.md) | The DEVICE_POWER_STATE enumeration type indicates a device power state. |
| [DEVICE_REGISTRY_PROPERTY enumeration](..\wdm\ne-wdm-device-registry-property.md) | The DEVICE_REGISTRY_PROPERTY enumeration identifies device properties that are stored in the registry. |
| [DEVICE_REMOVAL_POLICY enumeration](..\wdm\ne-wdm--device-removal-policy.md) | The DEVICE_REMOVAL_POLICY enumeration describes a device's removal policy. |
| [DEVICE_RESET_TYPE enumeration](..\wdm\ne-wdm--device-reset-type.md) | The DEVICE_RESET_TYPE enumeration specifies the type of device reset that is being requested by a call to the DeviceReset routine of the GUID_DEVICE_RESET_INTERFACE_STANDARD interface. |
| [DEVICE_WAKE_DEPTH enumeration](..\wdm\ne-wdm--device-wake-depth.md) | The DEVICE_WAKE_DEPTH enumeration specifies the deepest device power state from which a device can trigger a wake signal. |
| [DMA_COMPLETION_STATUS enumeration](..\wdm\ne-wdm-dma-completion-status.md) | The DMA_COMPLETION_STATUS enumeration describes the completion status of a DMA transfer. |
| [ENLISTMENT_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--enlistment-information-class.md) | The ENLISTMENT_INFORMATION_CLASS enumeration identifies the type of information that the ZwSetInformationEnlistment routine can set and that the ZwQueryInformationEnlistment routine can retrieve for an enlistment object. |
| [GPIO_PIN_CONFIG_TYPE enumeration](..\pepfx\ne-pepfx--gpio-pin-config-type.md) | The GPIO_PIN_CONFIG_TYPE enumeration describes a connection IO resource. |
| [GPIO_PIN_IORESTRICTION_TYPE enumeration](..\pepfx\ne-pepfx--gpio-pin-iorestriction-type.md) | The GPIO_PIN_IORESTRICTION_TYPE enumeration describes the functions that a GPIO pin is limited to performing. |
| [HARDWARE_COUNTER_TYPE enumeration](..\ntddk\ne-ntddk--hardware-counter-type.md) | The HARDWARE_COUNTER_TYPE enumeration specifies the type of a hardware counter. |
| [INTERFACE_TYPE enumeration](..\wdm\ne-wdm--interface-type.md) | The INTERFACE_TYPE enumeration indicates the bus type. |
| [IO_ACCESS_MODE enumeration](..\ntddsfio\ne-ntddsfio--io-access-mode.md) | Defines the types of access mode for Scheduled File I/O (SFIO). |
| [IO_ACCESS_TYPE enumeration](..\ntddsfio\ne-ntddsfio--io-access-type.md) | Defines the access rights for Scheduled File I/O (SFIO). |
| [IO_ALLOCATION_ACTION enumeration](..\wdm\ne-wdm--io-allocation-action.md) | The IO_ALLOCATION_ACTION enumerated type is used to specify return values for AdapterControl and ControllerControl routines. |
| [IO_CONTAINER_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--io-container-information-class.md) | The IO_CONTAINER_INFORMATION_CLASS enumeration contains constants that indicate the classes of system information that a kernel-mode driver can request. |
| [IO_CONTAINER_NOTIFICATION_CLASS enumeration](..\wdm\ne-wdm--io-container-notification-class.md) | The IO_CONTAINER_NOTIFICATION_CLASS enumeration contains constants that indicate the classes of events for which a kernel-mode driver can register to receive notifications. |
| [IO_PAGING_PRIORITY enumeration](..\wdm\ne-wdm--io-paging-priority.md) | The IO_PAGING_PRIORITY enumeration describes the priority value for a paging I/O IRP. |
| [IO_PRIORITY_HINT enumeration](..\wdm\ne-wdm--io-priority-hint.md) | The IO_PRIORITY_HINT enumeration type specifies the priority hint for an IRP. |
| [IO_SESSION_EVENT enumeration](..\wdm\ne-wdm--io-session-event.md) | The IO_SESSION_EVENT enumeration indicates the type of session event for which a driver is receiving notification. |
| [IO_SESSION_STATE enumeration](..\wdm\ne-wdm--io-session-state.md) | The IO_SESSION_STATE enumeration contains constants that indicate the current state of a user session. |
| [IRQ_DEVICE_POLICY enumeration](..\wdm\ne-wdm--irq-device-policy.md) | The IRQ_DEVICE_POLICY enumeration type indicates the policy the operating system can use to assign the interrupts from a device to different processors. |
| [IRQ_PRIORITY enumeration](..\wdm\ne-wdm--irq-priority.md) | The IRQ_PRIORITY enumeration type indicates the priority the system should give to servicing a device's interrupts. |
| [KBUGCHECK_CALLBACK_REASON enumeration](..\wdm\ne-wdm--kbugcheck-callback-reason.md) | The KBUGCHECK_CALLBACK_REASON enumeration type specifies the situations in which a bug-check callback executes. |
| [KBUGCHECK_DUMP_IO_TYPE enumeration](..\wdm\ne-wdm--kbugcheck-dump-io-type.md) | The KBUGCHECK_DUMP_IO_TYPE enumeration type identifies the type of a section of data within a crash dump file. |
| [KEY_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--key-information-class.md) | The KEY_INFORMATION_CLASS enumeration type represents the type of information to supply about a registry key. |
| [KEY_SET_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--key-set-information-class.md) | The KEY_SET_INFORMATION_CLASS enumeration type represents the type of information to set for a registry key. |
| [KEY_VALUE_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--key-value-information-class.md) | The KEY_VALUE_INFORMATION_CLASS enumeration type specifies the type of information to supply about the value of a registry key. |
| [KINTERRUPT_MODE enumeration](..\wdm\ne-wdm--kinterrupt-mode.md) | The KINTERRUPT_MODE enumeration type indicates whether an interrupt is level-triggered or edge-triggered. |
| [KINTERRUPT_POLARITY enumeration](..\wdm\ne-wdm--kinterrupt-polarity.md) | The KINTERRUPT_POLARITY enumeration indicates how a device signals an interrupt request on an interrupt line. |
| [KTMOBJECT_TYPE enumeration](..\wdm\ne-wdm--ktmobject-type.md) | The KTMOBJECT_TYPE enumeration identifies the types of objects that KTM supports. |
| [MEMORY_CACHING_TYPE enumeration](..\wdm\ne-wdm--memory-caching-type.md) | The MEMORY_CACHING_TYPE enumeration type specifies the permitted caching behavior when allocating or mapping memory. |
| [MEMORY_INFORMATION_CLASS enumeration](..\ntifs\ne-ntifs--memory-information-class.md) | Defines classes of memory information that can be retrieved by using the ZwQueryVirtualMemory function. |
| [MONITOR_DISPLAY_STATE enumeration](..\wdm\ne-wdm--monitor-display-state.md) | Indicates the power state of the monitor being displayed on. |
| [PEP_ACPI_OBJECT_TYPE enumeration](..\pepfx\ne-pepfx--pep-acpi-object-type.md) | The PEP_ACPI_OBJECT_TYPE enumeration indicates the type of ACPI object. |
| [PEP_ACPI_RESOURCE_TYPE enumeration](..\pepfx\ne-pepfx--pep-acpi-resource-type.md) | The PEP_ACPI_RESOURCE_TYPE enumeration is used to identify the type of ACPI resource that is contained in the PEP_ACPI_RESOURCE union. |
| [PEP_DEVICE_ACCEPTANCE_TYPE enumeration](..\pepfx\ne-pepfx--pep-device-acceptance-type.md) | The PEP_DEVICE_ACCEPTANCE_TYPE enumeration indicates whether a PEP accepts ownership of a device. |
| [PEP_PERF_STATE_TYPE enumeration](..\pepfx\ne-pepfx--pep-perf-state-type.md) | The PEP_PERF_STATE_TYPE enumeration indicates the type of performance information that is specified for a performance state (P-state) of a component. |
| [PEP_PERF_STATE_UNIT enumeration](..\pepfx\ne-pepfx--pep-perf-state-unit.md) | The PEP_PERF_STATE_UNIT enumeration indicates the measurement units in which the performance state (P-state) of a component is specified. |
| [PEP_WORK_TYPE enumeration](..\pepfx\ne-pepfx--pep-work-type.md) | The PEP_WORK_TYPE enumeration describes the type of work that the platform extension plug-in (PEP) is requesting. |
| [PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR_TYPE enumeration](..\ntddk\ne-ntddk--physical-counter-resource-descriptor-type.md) | The PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR_TYPE enumeration contains constants that indicate the type of hardware performance counter resource that is described by a PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structure. |
| [POOL_TYPE enumeration](..\wdm\ne-wdm--pool-type.md) | The POOL_TYPE enumeration type specifies the type of system memory to allocate. |
| [POOL_TYPE enumeration](..\wdm\ne-wdm--pool-type~r1.md) | The POOL_TYPE enumeration type specifies the type of system memory to allocate. |
| [POWER_INFORMATION_LEVEL enumeration](..\wdm\ne-wdm-power-information-level.md) | Indicates power level information. |
| [POWER_REQUEST_TYPE enumeration](..\wdm\ne-wdm--power-request-type.md) | The POWER_REQUEST_TYPE enumeration indicates the power request type. |
| [POWER_STATE_TYPE enumeration](..\wdm\ne-wdm--power-state-type.md) | The POWER_STATE_TYPE enumeration type indicates that a power state value is a system power state or a device power state. |
| [PO_FX_PERF_STATE_TYPE enumeration](..\wdm\ne-wdm--po-fx-perf-state-type.md) | The PO_FX_PERF_STATE_TYPE enumeration contains values that describe the type of performance states in a PO_FX_COMPONENT_PERF_SET. |
| [PO_FX_PERF_STATE_UNIT enumeration](..\wdm\ne-wdm--po-fx-perf-state-unit.md) | The PO_FX_PERF_STATE_UNIT enumeration contains values that describe the type of unit that is controlled by the performance states in a PO_FX_COMPONENT_PERF_SET. |
| [PPEP_PROCESSOR_IDLE_CANCEL_CODE enumeration](..\pep_x\ne-pep-x-ppep-processor-idle-cancel-code.md) | The PEP_PROCESSOR_IDLE_CANCEL_CODE enumeration values indicate reasons why a processor cannot enter an idle state that was previously selected by the platform extension plug-in (PEP). |
| [PPEP_PROCESSOR_IDLE_TYPE enumeration](..\pep_x\ne-pep-x-ppep-processor-idle-type.md) | The PEP_PROCESSOR_IDLE_TYPE enumeration indicates whether idle constraints apply to just the current processor or to all processors in the hardware platform. |
| [PSCREATEPROCESSNOTIFYTYPE enumeration](..\ntddk\ne-ntddk--pscreateprocessnotifytype.md) | Indicates the type of process notification. This enumeration is used in PsSetCreateProcessNotifyRoutineEx2 to register callback notifications. |
| [PSCREATETHREADNOTIFYTYPE enumeration](..\ntddk\ne-ntddk--pscreatethreadnotifytype.md) | Indicates the type of thread notification. This enumeration is used in PsSetCreateThreadNotifyRoutineEx to register callback notifications associated with thread creation or deletion. |
| [REG_NOTIFY_CLASS enumeration](..\wdm\ne-wdm--reg-notify-class.md) | The REG_NOTIFY_CLASS enumeration type specifies the type of registry operation that the configuration manager is passing to a RegistryCallback routine. |
| [RESOURCEMANAGER_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--resourcemanager-information-class.md) | The RESOURCEMANAGER_INFORMATION_CLASS enumeration identifies the type of information that the ZwQueryInformationResourceManager routine can retrieve for a resource manager object. |
| [SUBSYSTEM_INFORMATION_TYPE enumeration](..\ntddk\ne-ntddk--subsystem-information-type.md) | Indicates the type of subsystem for a process or thread. This enumeration is used in NtQueryInformationProcess and NtQueryInformationThread calls. |
| [SYSTEM_POWER_STATE enumeration](..\wdm\ne-wdm--system-power-state.md) | The SYSTEM_POWER_STATE enumeration type is used to indicate a system power state. |
| [TRACE_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--trace-information-class.md) | The TRACE_INFORMATION_CLASS enumeration type is used to indicate types of information associated with a WMI event tracing session. |
| [TRANSACTIONMANAGER_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--transactionmanager-information-class.md) | The TRANSACTIONMANAGER_INFORMATION_CLASS enumeration specifies the type of information that the ZwQueryInformationTransactionManager routine can retrieve for a transaction manager object. |
| [TRANSACTION_INFORMATION_CLASS enumeration](..\wdm\ne-wdm--transaction-information-class.md) | The TRANSACTION_INFORMATION_CLASS enumeration specifies the type of information that ZwSetInformationTransaction can set and ZwQueryInformationTransaction can retrieve for a transaction manager object. |
| [TRANSACTION_OUTCOME enumeration](..\wdm\ne-wdm--transaction-outcome.md) | The TRANSACTION_OUTCOME enumeration defines the outcomes (results) that KTM can assign to a transaction. |
| [TRANSACTION_STATE enumeration](..\wdm\ne-wdm--transaction-state.md) | The TRANSACTION_STATE enumeration defines the states that KTM can assign to a transaction. |
| [WORK_QUEUE_TYPE enumeration](..\wdm\ne-wdm--work-queue-type.md) | The WORK_QUEUE_TYPE enumeration type indicates the type of system worker thread that handles a work item. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_SYSENV_ENUM_VARIABLES IOCTL](..\ntddsysenv\ni-ntddsysenv-ioctl-sysenv-enum-variables.md) | Returns information about system environment variables using SysEnv device. |
| [IOCTL_SYSENV_GET_VARIABLE IOCTL](..\ntddsysenv\ni-ntddsysenv-ioctl-sysenv-get-variable.md) | Gets the value of the specified system environment variables using SysEnv device. |
| [IOCTL_SYSENV_QUERY_VARIABLE_INFO IOCTL](..\ntddsysenv\ni-ntddsysenv-ioctl-sysenv-query-variable-info.md) | Returns information about system environment variables using SysEnv device. |
| [IOCTL_SYSENV_SET_VARIABLE IOCTL](..\ntddsysenv\ni-ntddsysenv-ioctl-sysenv-set-variable.md) | Sets the value of the specified system environment variables using SysEnv device. |
| [IOCTL_VPCI_INVALIDATE_BLOCK IOCTL](..\vpci\ni-vpci-ioctl-vpci-invalidate-block.md) | The driver for a PCI Express (PCIe) virtual function (VF) issues the IOCTL_VPCI_INVALIDATE_BLOCK IOCTL request in order to be notified of changes to data in one or more VF configuration blocks. |
| [IOCTL_VPCI_READ_BLOCK IOCTL](..\vpci\ni-vpci-ioctl-vpci-read-block.md) | The driver for a PCI Express (PCIe) virtual function (VF) issues an IOCTL_VPCI_READ_BLOCK I/O control code (IOCTL) in order to read data from a VF configuration block. The driver issues this IOCTL to the next-lower driver in the driver stack. |
| [IOCTL_VPCI_WRITE_BLOCK IOCTL](..\vpci\ni-vpci-ioctl-vpci-write-block.md) | The driver for a PCI Express (PCIe) virtual function (VF) issues an IOCTL_VPCI_WRITE_BLOCK I/O control code (IOCTL) in order to write data to a VF configuration block. The driver issues this IOCTL to the next-lower driver in the driver stack. |
