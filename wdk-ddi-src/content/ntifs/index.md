# Ntifs.h header


This header is used by Installable file system, Windows kernel, Networking drivers for Windows Vista and later. For more information, see
- [Installable file system](../_ifsk/index.md)
- [Windows kernel](../_kernel/index.md)
- [Networking drivers for Windows Vista and later](../_netvista/index.md)

Ntifs.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [CcCanIWrite function](nf-ntifs-cccaniwrite.md) | The CcCanIWrite routine determines whether the caller can write to a cached file. |
| [CcCoherencyFlushAndPurgeCache function](nf-ntifs-cccoherencyflushandpurgecache.md) | The CcCoherencyFlushAndPurgeCache routine flushes and/or purges the cache to ensure cache coherency. |
| [CcCopyRead function](nf-ntifs-cccopyread.md) | The CcCopyRead routine copies data from a cached file to a user buffer. |
| [CcCopyReadEx function](nf-ntifs-cccopyreadex.md) | The CcCopyReadEx routine copies data from a cached file to a user buffer. The I/O byte count for the operation is charged to the issuing thread. |
| [CcCopyWrite function](nf-ntifs-cccopywrite.md) | The CcCopyWrite routine copies data from a user buffer to a cached file. |
| [CcCopyWriteEx function](nf-ntifs-cccopywriteex.md) | The CcCopyWriteEx routine copies data from a user buffer to a cached file. The I/O byte count for the operation is charged to the issuing thread. |
| [CcCopyWriteWontFlush function](nf-ntifs-cccopywritewontflush.md) | The CcCopyWriteWontFlush macro determines whether the amount of data to be copied in a call to CcCopyWrite is small enough not to require immediate flushing to disk if CcCopyWrite is called with Wait set to FALSE. |
| [CcCopyWriteWontFlush function](nf-ntifs-cccopywritewontflush~r1.md) | The CcCopyWriteWontFlush macro determines whether the amount of data to be copied in a call to CcCopyWrite is small enough not to require immediate flushing to disk if CcCopyWrite is called with Wait set to FALSE. |
| [CcDeferWrite function](nf-ntifs-ccdeferwrite.md) | The CcDeferWrite routine defers writing to a cached file. |
| [CcFastCopyRead function](nf-ntifs-ccfastcopyread.md) | The CcFastCopyRead routine performs a fast copy read from a cached file to a buffer in memory. |
| [CcFastCopyWrite function](nf-ntifs-ccfastcopywrite.md) | The CcFastCopyWrite routine performs a fast copy write from a buffer in memory to a cached file. |
| [CcFlushCache function](nf-ntifs-ccflushcache.md) | The CcFlushCache routine flushes all or a portion of a cached file to disk. |
| [CcGetDirtyPages function](nf-ntifs-ccgetdirtypages.md) | The CcGetDirtyPages routine searches for dirty pages in all files that match a given log handle. |
| [CcGetFileObjectFromBcb function](nf-ntifs-ccgetfileobjectfrombcb.md) | Given a pointer to a pinned buffer control block (BCB) for a file, the CcGetFileObjectFromBcb routine returns a pointer to the file object that the cache manager is using for that file. |
| [CcGetFileObjectFromSectionPtrs function](nf-ntifs-ccgetfileobjectfromsectionptrs.md) | Given a pointer to the section object pointers for a cached file, the CcGetFileObjectFromSectionPtrs routine returns a pointer to the file object that the cache manager is using for the file. |
| [CcGetFileObjectFromSectionPtrsRef function](nf-ntifs-ccgetfileobjectfromsectionptrsref.md) | When passed a pointer to a SECTION_OBJECT_POINTERS structure for a cached file, the CcGetFileObjectFromSectionPtrsRef routine returns a pointer to the file object that the cache manager is using for the cached file. |
| [CcGetFlushedValidData function](nf-ntifs-ccgetflushedvaliddata.md) | The CcGetFlushedValidData routine determines how much of a cached file has been flushed to disk. |
| [CcInitializeCacheMap function](nf-ntifs-ccinitializecachemap.md) | File systems call the CcInitializeCacheMap routine to cache a file. |
| [CcIsThereDirtyData function](nf-ntifs-ccistheredirtydata.md) | The CcIsThereDirtyData routine determines whether a mounted volume contains any files that have dirty data in the system cache. |
| [CcIsThereDirtyDataEx function](nf-ntifs-ccistheredirtydataex.md) | The CcIsThereDirtyDataEx routine determines whether a volume contains any files that have dirty data in the system cache. |
| [CcMapData function](nf-ntifs-ccmapdata.md) | The CcMapData routine maps a specified byte range of a cached file to a buffer in memory. |
| [CcMapData function](nf-ntifs-ccmapdata~r1.md) | The CcMapData routine maps a specified byte range of a cached file to a buffer in memory. |
| [CcMdlReadComplete function](nf-ntifs-ccmdlreadcomplete.md) | The CcMdlReadComplete routine frees the memory descriptor lists (MDL) created by CcMdlRead for a cached file. |
| [CcMdlWriteAbort function](nf-ntifs-ccmdlwriteabort.md) | The CcMdlWriteAbort routine frees memory descriptor lists (MDL) created by an earlier call to CcPrepareMdlWrite. |
| [CcMdlWriteComplete function](nf-ntifs-ccmdlwritecomplete.md) | The CcMdlWriteComplete routine frees the memory descriptor lists (MDL) created by CcPrepareMdlWrite for a cached file. |
| [CcPinMappedData function](nf-ntifs-ccpinmappeddata.md) | The CcPinMappedData routine pins the specified byte range of a cached file. |
| [CcPinRead function](nf-ntifs-ccpinread.md) | The CcPinRead routine pins the specified byte range of a cached file and reads the pinned data into a buffer in memory. |
| [CcPrepareMdlWrite function](nf-ntifs-ccpreparemdlwrite.md) | The CcPrepareMdlWrite routine provides direct access to cached file memory so that the caller can write data to the file. |
| [CcPreparePinWrite function](nf-ntifs-ccpreparepinwrite.md) | The CcPreparePinWrite routine pins the specified byte range of a cached file for write access. |
| [CcPurgeCacheSection function](nf-ntifs-ccpurgecachesection.md) | The CcPurgeCacheSection routine purges all or a portion of a cached file from the system cache. |
| [CcPurgeCacheSection function](nf-ntifs-ccpurgecachesection~r1.md) | The CcPurgeCacheSection routine purges all or a portion of a cached file from the system cache. |
| [CcRemapBcb function](nf-ntifs-ccremapbcb.md) | The CcRemapBcb routine maps a buffer control block (BCB) an additional time to preserve it through several calls that perform additional maps and unpins. |
| [CcRepinBcb function](nf-ntifs-ccrepinbcb.md) | The CcRepinBcb routine pins a buffer control block (BCB) an additional time to prevent it from being freed by a subsequent call to CcUnpinData. |
| [CcScheduleReadAhead function](nf-ntifs-ccschedulereadahead.md) | The CcScheduleReadAhead routine performs read-ahead (also called &#0034;lazy read&#0034;) on a cached file. CcScheduleReadAhead should never be called directly. The CcReadAhead macro should be called instead. |
| [CcScheduleReadAheadEx function](nf-ntifs-ccschedulereadaheadex.md) | The CcScheduleReadAheadEx routine performs read-ahead (also called &#0034;lazy read&#0034;) on a cached file. The I/O byte count for the operation is charged to the issuing thread. |
| [CcSetAdditionalCacheAttributes function](nf-ntifs-ccsetadditionalcacheattributes.md) | Call the CcSetAdditionalCacheAttributes routine to enable or disable read-ahead (also called &#0034;lazy read&#0034;) or write-behind (also called &#0034;lazy write&#0034;) on a cached file. |
| [CcSetAdditionalCacheAttributesEx function](nf-ntifs-ccsetadditionalcacheattributesex.md) | Call the CcSetAdditionalCacheAttributesEx routine to enable extended cache behavior on a cached file. |
| [CcSetBcbOwnerPointer function](nf-ntifs-ccsetbcbownerpointer.md) | The CcSetBcbOwnerPointer routine sets the owner thread pointer for a pinned buffer control block (BCB). |
| [CcSetDirtyPageThreshold function](nf-ntifs-ccsetdirtypagethreshold.md) | The CcSetDirtyPageThreshold routine sets a per-file dirty page threshold on a cached file. |
| [CcSetDirtyPinnedData function](nf-ntifs-ccsetdirtypinneddata.md) | The CcSetDirtyPinnedData routine marks as dirty the buffer control block (BCB) for a pinned buffer whose contents have been modified. |
| [CcSetFileSizes function](nf-ntifs-ccsetfilesizes.md) | The CcSetFileSizes routine updates the cache maps and section object for a cached file whose size has changed. |
| [CcSetLogHandleForFile function](nf-ntifs-ccsetloghandleforfile.md) | The CcSetLogHandleForFile routine sets a log handle for a file. |
| [CcSetReadAheadGranularity function](nf-ntifs-ccsetreadaheadgranularity.md) | The CcSetReadAheadGranularity routine sets the read-ahead granularity for a cached file. |
| [CcUninitializeCacheMap function](nf-ntifs-ccuninitializecachemap.md) | The CcUninitializeCacheMap routine stops the caching of a cached file. |
| [CcUnpinData function](nf-ntifs-ccunpindata.md) | The CcUnpinData routine releases cached file data that was mapped or pinned by an earlier call to CcMapData, CcPinRead, or CcPreparePinWrite. |
| [CcUnpinDataForThread function](nf-ntifs-ccunpindataforthread.md) | The CcUnpinDataForThread routine releases pages of a cached file whose buffer control block (BCB) was modified by an earlier call to CcSetBcbOwnerPointer. |
| [CcUnpinRepinnedBcb function](nf-ntifs-ccunpinrepinnedbcb.md) | The CcUnpinRepinnedBcb routine unpins a repinned buffer control block (BCB). |
| [CcWaitForCurrentLazyWriterActivity function](nf-ntifs-ccwaitforcurrentlazywriteractivity.md) | The CcWaitForCurrentLazyWriterActivity routine puts the caller into a wait state until the current batch of lazy writer activity is completed. |
| [CcZeroData function](nf-ntifs-cczerodata.md) | The CcZeroData routine zeros the specified range of bytes in a cached or noncached file. |
| [FsRtlAcknowledgeEcp function](nf-ntifs-fsrtlacknowledgeecp.md) | The FsRtlAcknowledgeEcp routine marks an extra create parameter (ECP) context structure as acknowledged. |
| [FsRtlAllocateExtraCreateParameter function](nf-ntifs-fsrtlallocateextracreateparameter.md) | The FsRtlAllocateExtraCreateParameter routine allocates memory for a user-defined extra create parameter (ECP) context structure and generates a pointer to that structure. |
| [FsRtlAllocateExtraCreateParameterFromLookasideList function](nf-ntifs-fsrtlallocateextracreateparameterfromlookasidelist.md) | The FsRtlAllocateExtraCreateParameterFromLookasideList routine allocates memory pool from a given lookaside list for an extra create parameter (ECP) context structure, and generates a pointer to that structure. |
| [FsRtlAllocateExtraCreateParameterList function](nf-ntifs-fsrtlallocateextracreateparameterlist.md) | The FsRtlAllocateExtraCreateParameterList routine allocates paged pool memory for an ECP_LIST structure and generates a pointer to that structure. |
| [FsRtlAllocatePoolWithQuotaTag function](nf-ntifs-fsrtlallocatepoolwithquotatag.md) | The FsRtlAllocatePoolWithQuotaTag routine allocates pool memory, charging quota against the current process. |
| [FsRtlAllocatePoolWithTag function](nf-ntifs-fsrtlallocatepoolwithtag.md) | The FsRtlAllocatePoolWithTag routine allocates pool memory. |
| [FsRtlAreThereCurrentFileLocks function](nf-ntifs-fsrtlaretherecurrentfilelocks.md) | The FsRtlAreThereCurrentFileLocks macro checks whether any byte range locks exist for the specified file. |
| [FsRtlAreVolumeStartupApplicationsComplete function](nf-ntifs-fsrtlarevolumestartupapplicationscomplete.md) | The FsRtlAreVolumeStartupApplicationsComplete function determines whether volume startup applications have completed processing. |
| [FsRtlCancellableWaitForMultipleObjects function](nf-ntifs-fsrtlcancellablewaitformultipleobjects.md) | The FsRtlCancellableWaitForMultipleObjects routine executes a cancelable wait operation (a wait that can be terminated) on one or more dispatcher objects. |
| [FsRtlCancellableWaitForSingleObject function](nf-ntifs-fsrtlcancellablewaitforsingleobject.md) | The FsRtlCancellableWaitForSingleObject routine executes a cancelable wait operation (a wait that can be terminated) on a dispatcher object. |
| [FsRtlChangeBackingFileObject function](nf-ntifs-fsrtlchangebackingfileobject.md) | The FsRtlChangeBackingFileObject routine replaces the current file object with a new file object. |
| [FsRtlCompleteRequest function](nf-ntifs-fsrtlcompleterequest.md) | The FsRtlCompleteRequest macro completes an IRP with the specified status. |
| [FsRtlCreateSectionForDataScan function](nf-ntifs-fsrtlcreatesectionfordatascan.md) | The FsRtlCreateSectionForDataScan routine creates a section object. |
| [FsRtlDeleteExtraCreateParameterLookasideList function](nf-ntifs-fsrtldeleteextracreateparameterlookasidelist.md) | The FsRtlDeleteExtraCreateParameterLookasideList routine frees an extra create parameter (ECP) lookaside list. |
| [FsRtlDeregisterUncProvider function](nf-ntifs-fsrtlderegisteruncprovider.md) | The FsRtlDeregisterUncProvider routine deregisters a redirector that was registered as a Universal Naming Convention (UNC) provider with the multiple UNC provider (MUP). |
| [FsRtlFastLock function](nf-ntifs-fsrtlfastlock.md) | The FsRtlFastLock macro is used by file systems and filter drivers to request a byte-range lock for a file stream. |
| [FsRtlFindExtraCreateParameter function](nf-ntifs-fsrtlfindextracreateparameter.md) | The FsRtlFindExtraCreateParameter routine searches a given ECP list for an ECP context structure of a given type and returns a pointer to this structure if it is found. |
| [FsRtlFreeExtraCreateParameter function](nf-ntifs-fsrtlfreeextracreateparameter.md) | The FsRtlFreeExtraCreateParameter routine frees the memory for an ECP context structure. |
| [FsRtlFreeExtraCreateParameterList function](nf-ntifs-fsrtlfreeextracreateparameterlist.md) | The FsRtlFreeExtraCreateParameterList routine frees an extra create parameter (ECP) list structure. |
| [FsRtlGetEcpListFromIrp function](nf-ntifs-fsrtlgetecplistfromirp.md) | The FsRtlGetEcpListFromIrp routine returns a pointer to an extra create parameter (ECP) context structure list that is associated with a given IRP_MJ_CREATE operation. |
| [FsRtlGetNextExtraCreateParameter function](nf-ntifs-fsrtlgetnextextracreateparameter.md) | The FsRtlGetNextExtraCreateParameter routine returns a pointer to the next (or first) extra create parameter (ECP) context structure in a given ECP list. |
| [FsRtlGetPerStreamContextPointer function](nf-ntifs-fsrtlgetperstreamcontextpointer.md) | The FsRtlGetPerStreamContextPointer macro returns the file system's stream context for a file stream. |
| [FsRtlGetSectorSizeInformation function](nf-ntifs-fsrtlgetsectorsizeinformation.md) | The FsRtlGetSectorSizeInformation routine retrieves the physical and logical sector size information for a storage volume. |
| [FsRtlGetSupportedFeatures function](nf-ntifs-fsrtlgetsupportedfeatures.md) | The FsRtlGetSupportedFeatures routine returns the supported features of a volume attached to the specified device object. |
| [FsRtlIncrementCcFastMdlReadWait function](nf-ntifs-fsrtlincrementccfastmdlreadwait.md) | The FsRtlIncrementCcFastMdlReadWait routine increments the cache manager's CcFastMdlReadWait performance counter member in a processor control block (PRCB) object. |
| [FsRtlIncrementCcFastReadNoWait function](nf-ntifs-fsrtlincrementccfastreadnowait.md) | The FsRtlIncrementCcFastReadNoWait routine increments the CcFastReadNoWait performance counter in a per processor control block of cache manager system counters. |
| [FsRtlIncrementCcFastReadNotPossible function](nf-ntifs-fsrtlincrementccfastreadnotpossible.md) | The FsRtlIncrementCcFastReadNotPossible routine increments the CcFastReadNotPossible performance counter in a per processor control block of cache manager system counters. |
| [FsRtlIncrementCcFastReadResourceMiss function](nf-ntifs-fsrtlincrementccfastreadresourcemiss.md) | The FsRtlIncrementCcFastReadResourceMiss routine increments the CcFastReadNotPossible performance counter in a per processor control block of cache manager system counters. |
| [FsRtlIncrementCcFastReadWait function](nf-ntifs-fsrtlincrementccfastreadwait.md) | The FsRtlIncrementCcFastReadWait routine increments the CcFastReadWait performance counter in a per processor control block of cache manager system counters. |
| [FsRtlInitExtraCreateParameterLookasideList function](nf-ntifs-fsrtlinitextracreateparameterlookasidelist.md) | The FsRtlInitExtraCreateParameterLookasideList routine initializes a paged or nonpaged pool lookaside list used for the allocation of one or more extra create parameter context structures (ECPs) of fixed size. |
| [FsRtlInitPerStreamContext function](nf-ntifs-fsrtlinitperstreamcontext.md) | The FsRtlInitPerStreamContext macro initializes a filter driver context structure. |
| [FsRtlInitializeExtraCreateParameter function](nf-ntifs-fsrtlinitializeextracreateparameter.md) | The FsRtlInitializeExtraCreateParameter routine initializes an extra create parameter (ECP) context structure. |
| [FsRtlInitializeExtraCreateParameterList function](nf-ntifs-fsrtlinitializeextracreateparameterlist.md) | The FsRtlInitializeExtraCreateParameterList routine initializes an extra create parameter (ECP) context structure list. |
| [FsRtlInsertExtraCreateParameter function](nf-ntifs-fsrtlinsertextracreateparameter.md) | The FsRtlInsertExtraCreateParameter routine inserts an extra create parameter (ECP) context structure into an ECP list. |
| [FsRtlInsertPerFileContext function](nf-ntifs-fsrtlinsertperfilecontext.md) | The FsRtlInsertPerFileContext routine associates a FSRTL_PER_FILE_CONTEXT object with a driver-specified context object for a file. |
| [FsRtlInsertPerFileObjectContext function](nf-ntifs-fsrtlinsertperfileobjectcontext.md) | For a &#0034;legacy&#0034; file system filter driver, the FsRtlInsertPerFileObjectContext function associates context information with a file object. |
| [FsRtlInsertPerStreamContext function](nf-ntifs-fsrtlinsertperstreamcontext.md) | The FsRtlInsertPerStreamContext routine associates a file system filter driver's per-stream context structure with a file stream. |
| [FsRtlIsAnsiCharacterLegal function](nf-ntifs-fsrtlisansicharacterlegal.md) | The FsRtlIsAnsiCharacterLegal macro determines whether a character is a legal ANSI character. |
| [FsRtlIsAnsiCharacterLegalFat function](nf-ntifs-fsrtlisansicharacterlegalfat.md) | The FsRtlIsAnsiCharacterLegalFat macro determines whether an ANSI character is legal for FAT file names. |
| [FsRtlIsAnsiCharacterLegalHpfs function](nf-ntifs-fsrtlisansicharacterlegalhpfs.md) | The FsRtlIsAnsiCharacterLegalHpfs macro determines whether an ANSI character is legal for HPFS file names. |
| [FsRtlIsAnsiCharacterLegalNtfs function](nf-ntifs-fsrtlisansicharacterlegalntfs.md) | The FsRtlIsAnsiCharacterLegalNtfs macro determines whether an ANSI character is legal for NTFS file names. |
| [FsRtlIsAnsiCharacterLegalNtfsStream function](nf-ntifs-fsrtlisansicharacterlegalntfsstream.md) | The FsRtlIsAnsiCharacterLegalNtfsStream macro determines whether an ANSI character is legal for NTFS stream names. |
| [FsRtlIsAnsiCharacterWild function](nf-ntifs-fsrtlisansicharacterwild.md) | The FsRtlIsAnsiCharacterWild macro determines whether an ANSI character is a wildcard character. |
| [FsRtlIsDaxVolume function](nf-ntifs-fsrtlisdaxvolume.md) | This routine queries if the specified file is on a direct access (DAX) volume. |
| [FsRtlIsEcpAcknowledged function](nf-ntifs-fsrtlisecpacknowledged.md) | The FsRtlIsEcpAcknowledged routine is used to determine if a given extra create parameter (ECP) context structure has been marked as acknowledged. |
| [FsRtlIsEcpFromUserMode function](nf-ntifs-fsrtlisecpfromusermode.md) | The FsRtlIsEcpFromUserMode routine determines whether an extra create parameter (ECP) context structure originated from user mode. |
| [FsRtlIsLeadDbcsCharacter function](nf-ntifs-fsrtlisleaddbcscharacter.md) | The FsRtlIsLeadDbcsCharacter macro determines whether a character is a lead byte (the first byte of a character) in a double-byte character set (DBCS). |
| [FsRtlIsPagingFile function](nf-ntifs-fsrtlispagingfile.md) | The FsRtlIsPagingFile routine determines whether a given file is a paging file. |
| [FsRtlIsSystemPagingFile function](nf-ntifs-fsrtlissystempagingfile.md) | The FsRtlIsSystemPagingFile routine determines whether a given file is currently a system paging file. |
| [FsRtlIsUnicodeCharacterWild function](nf-ntifs-fsrtlisunicodecharacterwild.md) | The FsRtlIsUnicodeCharacterWild macro determines whether a Unicode character is a wildcard character. |
| [FsRtlIssueDeviceIoControl function](nf-ntifs-fsrtlissuedeviceiocontrol.md) | The FsRtlIssueDeviceIoControl routine sends a synchronous device I/O control request to a target device object. |
| [FsRtlLogCcFlushError function](nf-ntifs-fsrtllogccflusherror.md) | The FsRtlLogCcFlushError routine logs a lost delayed-write error and displays a dialog box to the user. |
| [FsRtlLookupPerFileContext function](nf-ntifs-fsrtllookupperfilecontext.md) | The FsRtlLookupPerFileContext routine returns a pointer to a FSRTL_PER_FILE_CONTEXT object that is associated with a specified file. |
| [FsRtlLookupPerFileObjectContext function](nf-ntifs-fsrtllookupperfileobjectcontext.md) | For a &#0034;legacy&#0034; file system filter driver, the FsRtlLookupPerFileObjectContext function retrieves context information previously associated with a file object. |
| [FsRtlLookupPerStreamContext function](nf-ntifs-fsrtllookupperstreamcontext.md) | The FsRtlLookupPerStreamContext macro retrieves a per-stream context structure for a file stream. |
| [FsRtlMupGetProviderIdFromName function](nf-ntifs-fsrtlmupgetprovideridfromname.md) | The FsRtlMupGetProviderIdFromName routine gets the provider identifier of a network redirector that is registered with the multiple UNC provider (MUP) from the device name of the network redirector. |
| [FsRtlMupGetProviderInfoFromFileObject function](nf-ntifs-fsrtlmupgetproviderinfofromfileobject.md) | The FsRtlMupGetProviderInfoFromFileObject routine gets information about a network redirector that is registered with the multiple UNC provider (MUP) from a file object for a file that is located on a remote file system. |
| [FsRtlPrepareToReuseEcp function](nf-ntifs-fsrtlpreparetoreuseecp.md) | The FsRtlPrepareToReuseEcp routine resets an extra create parameter (ECP) context structure, which prepares it for reuse. |
| [FsRtlQueryCachedVdl function](nf-ntifs-fsrtlquerycachedvdl.md) | The current valid data length (VDL) for a cached file is retrieved with the FsRtlQueryCachedVdl routine. |
| [FsRtlQueryKernelEaFile function](nf-ntifs-fsrtlquerykerneleafile.md) | The routine FsRtlQueryKernelEaFile is used to build an explicit QueryEA request and synchronously wait for it to complete, returning the result. This allows the caller to do this by FileObject instead of a handle. |
| [FsRtlRegisterFileSystemFilterCallbacks function](nf-ntifs-fsrtlregisterfilesystemfiltercallbacks.md) | File system filter drivers and file systems call the FsRtlRegisterFileSystemFilterCallbacks routine to register notification callback routines to be invoked when the underlying file system performs certain operations. |
| [FsRtlRemoveDotsFromPath function](nf-ntifs-fsrtlremovedotsfrompath.md) | The FsRtlRemoveDotsFromPath routine removes unnecessary occurrences of '.' and '..' from the specified path. |
| [FsRtlRemoveExtraCreateParameter function](nf-ntifs-fsrtlremoveextracreateparameter.md) | The FsRtlRemoveExtraCreateParameter routine searches an ECP list for an ECP context structure and, if found, detaches it from the ECP list. |
| [FsRtlRemovePerFileContext function](nf-ntifs-fsrtlremoveperfilecontext.md) | The FsRtlRemovePerFileContext routine returns a pointer to a FSRTL_PER_FILE_CONTEXT object that is associated with a file. |
| [FsRtlRemovePerFileObjectContext function](nf-ntifs-fsrtlremoveperfileobjectcontext.md) | For a &#0034;legacy&#0034; file system filter driver, the FsRtlRemovePerFileObjectContext function unlinks a per-file-object context information structure from the list of per-file-object contexts previously associated with a file object. |
| [FsRtlRemovePerStreamContext function](nf-ntifs-fsrtlremoveperstreamcontext.md) | FsRtlRemovePerStreamContext removes a per-stream context structure from the list of per-stream contexts associated with a file stream. |
| [FsRtlSetEcpListIntoIrp function](nf-ntifs-fsrtlsetecplistintoirp.md) | The FsRtlSetEcpListIntoIrp routine attaches an extra create parameter (ECP) context structure list to an IRP_MJ_CREATE operation. |
| [FsRtlSetKernelEaFile function](nf-ntifs-fsrtlsetkerneleafile.md) | The routine FsRtlQueryKernelEaFile is used to set, modify and/or delete extended attribute (EA) values for a file and synchronously wait for it to complete, returning a result. |
| [FsRtlSetupAdvancedHeader function](nf-ntifs-fsrtlsetupadvancedheader.md) | The FsRtlSetupAdvancedHeader macro is used by file systems to initialize an FSRTL_ADVANCED_FCB_HEADER structure for use with filter contexts. |
| [FsRtlSetupAdvancedHeaderEx function](nf-ntifs-fsrtlsetupadvancedheaderex.md) | The FsRtlSetupAdvancedHeaderEx macro is used by file systems to initialize an FSRTL_ADVANCED_FCB_HEADER structure for use with both stream and file contexts. |
| [FsRtlSupportsPerFileContexts function](nf-ntifs-fsrtlsupportsperfilecontexts.md) | The FsRtlSupportsPerFileContexts macro checks if per file context information is supported by the file system that is associated with a specified FILE_OBJECT. |
| [FsRtlTeardownPerFileContexts function](nf-ntifs-fsrtlteardownperfilecontexts.md) | File systems call theFsRtlTeardownPerFileContexts routine to free FSRTL_PER_FILE_CONTEXT objects that are associated with a file control block (FCB) structure. |
| [FsRtlTeardownPerStreamContexts function](nf-ntifs-fsrtlteardownperstreamcontexts.md) | The FsRtlTeardownPerStreamContexts routine frees all per-stream context structures associated with a given FSRTL_ADVANCED_FCB_HEADER structure. |
| [FsRtlTestAnsiCharacter function](nf-ntifs-fsrtltestansicharacter.md) | The FsRtlTestAnsiCharacter macro determines whether an ANSI or double-byte character set (DBCS) character meets the specified criteria. |
| [FsRtlValidateReparsePointBuffer function](nf-ntifs-fsrtlvalidatereparsepointbuffer.md) | The FsRtlValidateReparsePointBuffer routine verifies that the specified reparse point buffer is valid. |
| [GetSecurityUserInfo function](nf-ntifs-getsecurityuserinfo.md) | The GetSecurityUserInfo function retrieves information about a logon session. |
| [IoAcquireVpbSpinLock function](nf-ntifs-ioacquirevpbspinlock.md) | The IoAcquireVpbSpinLock routine acquires the Volume Parameter Block (VPB) spin lock. |
| [IoCheckEaBufferValidity function](nf-ntifs-iocheckeabuffervalidity.md) | The IoCheckEaBufferValidity routine checks whether the specified extended attribute (EA) buffer is valid. |
| [IoCheckQuotaBufferValidity function](nf-ntifs-iocheckquotabuffervalidity.md) | The IoCheckQuotaBufferValidity routine checks whether the specified quota buffer is valid. |
| [IoCreateStreamFileObject function](nf-ntifs-iocreatestreamfileobject.md) | The IoCreateStreamFileObject routine creates a new stream file object. |
| [IoCreateStreamFileObjectEx function](nf-ntifs-iocreatestreamfileobjectex.md) | The IoCreateStreamFileObjectEx routine creates a new stream file object. |
| [IoCreateStreamFileObjectEx2 function](nf-ntifs-iocreatestreamfileobjectex2.md) | The IoCreateStreamFileObjectEx2 routine creates a new stream file object with create options for a target device object. |
| [IoCreateStreamFileObjectLite function](nf-ntifs-iocreatestreamfileobjectlite.md) | The IoCreateStreamFileObjectLite routine creates a new stream file object, but does not cause an IRP_MJ_CLEANUP request to be sent to the file system driver stack. |
| [IoEnumerateDeviceObjectList function](nf-ntifs-ioenumeratedeviceobjectlist.md) | The IoEnumerateDeviceObjectList routine enumerates a driver's device object list. |
| [IoEnumerateRegisteredFiltersList function](nf-ntifs-ioenumerateregisteredfilterslist.md) | The IoEnumerateRegisteredFiltersList routine enumerates the file system filter drivers that have registered with the system. |
| [IoGetAttachedDevice function](nf-ntifs-iogetattacheddevice.md) | The IoGetAttachedDevice routine returns a pointer to the highest-level device object associated with the specified device. |
| [IoGetAttachedDeviceReference function](nf-ntifs-iogetattacheddevicereference.md) | The IoGetAttachedDeviceReference routine returns a pointer to the highest level device object in a driver stack and increments the reference count on that object. |
| [IoGetDeviceAttachmentBaseRef function](nf-ntifs-iogetdeviceattachmentbaseref.md) | The IoGetDeviceAttachmentBaseRef routine returns a pointer to the lowest-level device object in a file system or device driver stack. |
| [IoGetDeviceToVerify function](nf-ntifs-iogetdevicetoverify.md) | The IoGetDeviceToVerify routine returns a pointer to the device object, representing a removable-media device, that is the target of the given thread's I/O request. |
| [IoGetDiskDeviceObject function](nf-ntifs-iogetdiskdeviceobject.md) | The IoGetDiskDeviceObject routine retrieves a pointer to the disk device object associated with a given file system volume device object. |
| [IoGetLowerDeviceObject function](nf-ntifs-iogetlowerdeviceobject.md) | The IoGetLowerDeviceObject routine returns a pointer to the next-lower-level device object on the driver stack. |
| [IoGetRequestorProcess function](nf-ntifs-iogetrequestorprocess.md) | The IoGetRequestorProcess routine returns a process pointer for the thread that originally requested a given I/O operation. |
| [IoGetRequestorProcessId function](nf-ntifs-iogetrequestorprocessid.md) | The IoGetRequestorProcessId routine returns the unique 32-bit process ID for the thread that originally requested a given I/O operation. |
| [IoGetRequestorSessionId function](nf-ntifs-iogetrequestorsessionid.md) | The IoGetRequestorSessionId routine returns the session ID for the process that originally requested a given I/O operation. |
| [IoGetTopLevelIrp function](nf-ntifs-iogettoplevelirp.md) | The IoGetTopLevelIrp routine returns the value of the TopLevelIrp field of the current thread. |
| [IoInitializePriorityInfo function](nf-ntifs-ioinitializepriorityinfo.md) | The IoInitializePriorityInfo routine initializes a structure of type IO_PRIORITY_INFO. |
| [IoIsOperationSynchronous function](nf-ntifs-ioisoperationsynchronous.md) | The IoIsOperationSynchronous routine determines whether a given IRP represents a synchronous or asynchronous I/O request. |
| [IoIsSystemThread function](nf-ntifs-ioissystemthread.md) | The IoIsSystemThread routine checks whether a given thread is a system thread. |
| [IoQueryFileDosDeviceName function](nf-ntifs-ioqueryfiledosdevicename.md) | The IoQueryFileDosDeviceName routine retrieves an MS-DOS device name for a file. |
| [IoRegisterFileSystem function](nf-ntifs-ioregisterfilesystem.md) | The IoRegisterFileSystem routine adds a file system's control device object to the global file system queue. |
| [IoRegisterFsRegistrationChange function](nf-ntifs-ioregisterfsregistrationchange.md) | The IoRegisterFsRegistrationChange routine registers a file system filter driver's notification routine to be called whenever a file system registers or unregisters itself as an active file system. |
| [IoRegisterFsRegistrationChangeEx function](nf-ntifs-ioregisterfsregistrationchangeex.md) | The IoRegisterFsRegistrationChangeEx routine registers a file system filter driver's notification routine to be called whenever a file system registers or unregisters itself as an active file system. |
| [IoRegisterFsRegistrationChangeMountAware function](nf-ntifs-ioregisterfsregistrationchangemountaware.md) | The IoRegisterFsRegistrationChangeMountAware routine registers a file system filter driver's notification routine. This notification routine is called whenever a file system registers or unregisters itself as an active file system. |
| [IoReleaseVpbSpinLock function](nf-ntifs-ioreleasevpbspinlock.md) | The IoReleaseVpbSpinLock routine releases the Volume Parameter Block (VPB) spin lock. |
| [IoReplaceFileObjectName function](nf-ntifs-ioreplacefileobjectname.md) | The IoReplaceFileObjectName routine replaces the name of a file object. |
| [IoSetDeviceToVerify function](nf-ntifs-iosetdevicetoverify.md) | The IoSetDeviceToVerify routine specifies a device object to be verified. The specified device object represents a removable media device. |
| [IoSetStartIoAttributes function](nf-ntifs-iosetstartioattributes.md) | The IoSetStartIoAttributes routine sets attributes for the driver's StartIo routine. |
| [IoSetTopLevelIrp function](nf-ntifs-iosettoplevelirp.md) | The IoSetTopLevelIrp routine sets the value of the TopLevelIrp field of the current thread. |
| [IoSizeOfIrp function](nf-ntifs-iosizeofirp.md) | The IoSizeOfIrp routine determines the size in bytes for an IRP, given the number of stack locations in the IRP. |
| [IoStartNextPacket function](nf-ntifs-iostartnextpacket.md) | The IoStartNextPacket routine dequeues the next IRP, if any, from the given device object's associated device queue and calls the driver's StartIo routine. |
| [IoStartNextPacketByKey function](nf-ntifs-iostartnextpacketbykey.md) | The IoStartNextPacketByKey routine dequeues the next I/O request packet from the specified device object's associated device queue according to a specified sort-key value and calls the driver's StartIo routine with that IRP. |
| [IoStartPacket function](nf-ntifs-iostartpacket.md) | The IoStartPacket routine calls the driver's StartIo routine with the given IRP or inserts the IRP into the device queue associated with the given device object if the device is already busy. |
| [IoStartTimer function](nf-ntifs-iostarttimer.md) | The IoStartTimer routine enables the timer associated with a given device object so the driver-supplied IoTimer routine is called once per second. |
| [IoStopTimer function](nf-ntifs-iostoptimer.md) | The IoStopTimer routine disables the timer for a specified device object so the driver-supplied IoTimer routine is not called. |
| [IoThreadToProcess function](nf-ntifs-iothreadtoprocess.md) | The IoThreadToProcess routine returns a pointer to the process for the specified thread. |
| [IoUnregisterFileSystem function](nf-ntifs-iounregisterfilesystem.md) | The IoUnregisterFileSystem routine removes a file system's control device object from the global file system queue. |
| [IoUnregisterFsRegistrationChange function](nf-ntifs-iounregisterfsregistrationchange.md) | The IoUnregisterFsRegistrationChange routine unregisters file system filter driver's file system registration change notification routine. |
| [IoVerifyVolume function](nf-ntifs-ioverifyvolume.md) | The IoVerifyVolume routine sends a volume verify request to the given removable-media device. |
| [IoWriteErrorLogEntry function](nf-ntifs-iowriteerrorlogentry.md) | The IoWriteErrorLogEntry routine queues a given error log packet to the system error logging thread. |
| [IsReparseTagMicrosoft function](nf-ntifs-isreparsetagmicrosoft.md) | The IsReparseTagMicrosoft macro determines whether a reparse point tag indicates a Microsoft reparse point. |
| [IsReparseTagNameSurrogate function](nf-ntifs-isreparsetagnamesurrogate.md) | The IsReparseTagNameSurrogate macro determines whether a tag's associated reparse point is a surrogate for another named entity, such as a volume mount point. |
| [KeGetProcessorIndexFromNumber function](nf-ntifs-kegetprocessorindexfromnumber.md) | The KeGetProcessorIndexFromNumber routine converts a group number and a group-relative processor number to a systemwide processor index. |
| [KeInitializeQueue function](nf-ntifs-keinitializequeue.md) | The KeInitializeQueue routine initializes a queue object on which threads can wait for entries. |
| [KeInsertHeadQueue function](nf-ntifs-keinsertheadqueue.md) | The KeInsertHeadQueue routine inserts an entry at the head of the given queue if it cannot immediately use the entry to satisfy a thread wait. |
| [KeInsertQueue function](nf-ntifs-keinsertqueue.md) | The KeInsertQueue routine inserts an entry at the tail of the given queue if it cannot immediately use the entry to satisfy a thread wait. |
| [KeQueryPerformanceCounter function](nf-ntifs-kequeryperformancecounter.md) | The KeQueryPerformanceCounter routine retrieves the current value and frequency of the performance counter.Use KeQueryPerformanceCounter to acquire high resolution (&lt;1us) time stamps for time interval measurements. |
| [KeRemoveQueue function](nf-ntifs-keremovequeue.md) | The KeRemoveQueue routine gives the calling thread a pointer to a dequeued entry from the given queue object or allows the caller to wait, up to an optional timeout interval, on the queue object. |
| [KeRundownQueue function](nf-ntifs-kerundownqueue.md) | The KeRundownQueue routine cleans up a queue object, flushing any queued entries. |
| [KeSetKernelStackSwapEnable function](nf-ntifs-kesetkernelstackswapenable.md) | The KeSetKernelStackSwapEnable routine enables and disables swapping of the caller's stack to disk. |
| [KeStackAttachProcess function](nf-ntifs-kestackattachprocess.md) | The KeStackAttachProcess routine attaches the current thread to the address space of the target process. |
| [KeStallExecutionProcessor function](nf-ntifs-kestallexecutionprocessor.md) | The KeStallExecutionProcessor routine stalls the caller on the current processor for a specified time interval. |
| [KeUnstackDetachProcess function](nf-ntifs-keunstackdetachprocess.md) | The KeUnstackDetachProcess routine detaches the current thread from the address space of a process and restores the previous attach state. |
| [MapSecurityError function](nf-ntifs-mapsecurityerror.md) | The MapSecurityError function maps a security interface SECURITY_STATUS status code to a corresponding NSTATUS status code. |
| [MmCanFileBeTruncated function](nf-ntifs-mmcanfilebetruncated.md) | The MmCanFileBeTruncated routine checks whether a file can be truncated. |
| [MmDoesFileHaveUserWritableReferences function](nf-ntifs-mmdoesfilehaveuserwritablereferences.md) | The MmDoesFileHaveUserWritableReferences function returns the number of writable references for a file object. |
| [MmFlushImageSection function](nf-ntifs-mmflushimagesection.md) | The MmFlushImageSection routine flushes the image section for a file. |
| [MmForceSectionClosed function](nf-ntifs-mmforcesectionclosed.md) | The MmForceSectionClosed routine deletes the data and image sections for a file that is no longer in use. |
| [MmGetMaximumFileSectionSize function](nf-ntifs-mmgetmaximumfilesectionsize.md) | The MmGetMaximumFileSectionSize returns the maximum possible size of a file section for the current version of Windows. |
| [MmIsRecursiveIoFault function](nf-ntifs-mmisrecursiveiofault.md) | The MmIsRecursiveIoFault routine determines whether the current page fault is occurring during an I/O operation. |
| [MmPrefetchPages function](nf-ntifs-mmprefetchpages.md) | The MmPrefetchPages routine reads groups of pages from secondary storage in the optimal fashion. |
| [MmSetAddressRangeModified function](nf-ntifs-mmsetaddressrangemodified.md) | The MmSetAddressRangeModified routine marks currently valid pages in the specified range of the system cache as modified. |
| [NtAllocateVirtualMemory function](nf-ntifs-ntallocatevirtualmemory.md) | The ZwAllocateVirtualMemory routine reserves, commits, or both, a region of pages within the user-mode virtual address space of a specified process. |
| [NtClose function](nf-ntifs-ntclose.md) | The ZwClose routine closes an object handle. |
| [NtCreateFile function](nf-ntifs-ntcreatefile.md) | The ZwCreateFile routine creates a new file or opens an existing file. |
| [NtDeviceIoControlFile function](nf-ntifs-ntdeviceiocontrolfile.md) | The ZwDeviceIoControlFile routine sends a control code directly to a specified device driver, causing the corresponding driver to perform the specified operation. |
| [NtDuplicateToken function](nf-ntifs-ntduplicatetoken.md) | The ZwDuplicateToken function creates a handle to a new access token that duplicates an existing token. This function can create either a primary token or an impersonation token. |
| [NtFlushBuffersFileEx function](nf-ntifs-ntflushbuffersfileex.md) | The ZwFlushBuffersFileEx routine is called by a file system filter driver to send a flush request for a given file to the file system. An optional flush operation flag can be set to control how file data is written to storage. |
| [NtFreeVirtualMemory function](nf-ntifs-ntfreevirtualmemory.md) | The ZwFreeVirtualMemory routine releases, decommits, or both, a region of pages within the virtual address space of a specified process. |
| [NtFsControlFile function](nf-ntifs-ntfscontrolfile.md) | The ZwFsControlFile routine sends a control code directly to a specified file system or file system filter driver, causing the corresponding driver to perform the specified action. |
| [NtLockFile function](nf-ntifs-ntlockfile.md) | The ZwLockFile routine requests a byte-range lock for the specified file. |
| [NtOpenFile function](nf-ntifs-ntopenfile.md) | The ZwOpenFile routine opens an existing file, directory, device, or volume. |
| [NtOpenProcessTokenEx function](nf-ntifs-ntopenprocesstokenex.md) | The ZwOpenProcessTokenEx routine opens the access token associated with a process. |
| [NtOpenThreadTokenEx function](nf-ntifs-ntopenthreadtokenex.md) | The ZwOpenThreadTokenEx routine opens the access token associated with a thread. |
| [NtQueryDirectoryFile function](nf-ntifs-ntquerydirectoryfile.md) | The ZwQueryDirectoryFile routine returns various kinds of information about files in the directory specified by a given file handle. |
| [NtQueryDirectoryFileEx function](nf-ntifs-ntquerydirectoryfileex.md) | The ZwQueryDirectoryFileEx routine returns information about files in the directory specified by the FileHandle parameter. |
| [NtQueryInformationFile function](nf-ntifs-ntqueryinformationfile.md) | The ZwQueryInformationFile routine returns various kinds of information about a file object. |
| [NtQueryInformationToken function](nf-ntifs-ntqueryinformationtoken.md) | The ZwQueryInformationToken routine retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information. |
| [NtQueryObject function](nf-ntifs-ntqueryobject.md) | The ZwQueryObject routine provides information about a supplied object. |
| [NtQueryQuotaInformationFile function](nf-ntifs-ntqueryquotainformationfile.md) | The ZwQueryQuotaInformationFile routine retrieves quota entries associated with the volume specified by the FileHandle parameter. |
| [NtQuerySecurityObject function](nf-ntifs-ntquerysecurityobject.md) | The ZwQuerySecurityObject routine retrieves a copy of an object's security descriptor. |
| [NtQueryVirtualMemory function](nf-ntifs-ntqueryvirtualmemory.md) | The ZwQueryVirtualMemory routine determines the state, protection, and type of a region of pages within the virtual address space of the subject process. |
| [NtQueryVolumeInformationFile function](nf-ntifs-ntqueryvolumeinformationfile.md) | The ZwQueryVolumeInformationFile routine retrieves information about the volume associated with a given file, directory, storage device, or volume. |
| [NtReadFile function](nf-ntifs-ntreadfile.md) | The ZwReadFile routine reads data from an open file. |
| [NtSetInformationFile function](nf-ntifs-ntsetinformationfile.md) | The ZwSetInformationFile routine changes various kinds of information about a file object. |
| [NtSetInformationToken function](nf-ntifs-ntsetinformationtoken.md) | The ZwSetInformationToken routine modifies information in a specified token. The calling process must have appropriate access rights to set the information. |
| [NtSetQuotaInformationFile function](nf-ntifs-ntsetquotainformationfile.md) | The ZwSetQuotaInformationFile routine changes quota entries for the volume associated with the FileHandle parameter. All of the quota entries in the specified buffer are applied to the volume. |
| [NtSetSecurityObject function](nf-ntifs-ntsetsecurityobject.md) | The ZwSetSecurityObject routine sets an object's security state. |
| [NtUnlockFile function](nf-ntifs-ntunlockfile.md) | The ZwUnlockFile routine unlocks a byte-range lock in a file. |
| [NtWriteFile function](nf-ntifs-ntwritefile.md) | The ZwWriteFile routine writes data to an open file. |
| [ObIsKernelHandle function](nf-ntifs-obiskernelhandle.md) | The ObIsKernelHandle routine determines whether the specified handle is a kernel handle. |
| [ObOpenObjectByPointer function](nf-ntifs-obopenobjectbypointer.md) | The ObOpenObjectByPointer function opens an object referenced by a pointer and returns a handle to the object. |
| [ObQueryNameString function](nf-ntifs-obquerynamestring.md) | The ObQueryNameString routine supplies the name, if there is one, of a given object to which the caller has a pointer. |
| [PoCallDriver function](nf-ntifs-pocalldriver.md) | The PoCallDriver routine passes a power IRP to the next-lower driver in the device stack. (Windows Server 2003, Windows XP, and Windows 2000 only.). |
| [PoClearPowerRequest function](nf-ntifs-poclearpowerrequest.md) | The PoClearPowerRequest routine decrements the count for the specified power request type. |
| [PoCreatePowerRequest function](nf-ntifs-pocreatepowerrequest.md) | The PoCreatePowerRequest routine creates a power request object. |
| [PoDeletePowerRequest function](nf-ntifs-podeletepowerrequest.md) | The PoDeletePowerRequest routine deletes a power request object. |
| [PoEndDeviceBusy function](nf-ntifs-poenddevicebusy.md) | The PoEndDeviceBusy routine marks the end of a period of time in which the device is busy. |
| [PoQueryWatchdogTime function](nf-ntifs-poquerywatchdogtime.md) | The PoQueryWatchdogTime routine indicates whether the power manager has enabled a watchdog time-out counter for any power IRP that is currently assigned to the device stack. |
| [PoRegisterDeviceForIdleDetection function](nf-ntifs-poregisterdeviceforidledetection.md) | The PoRegisterDeviceForIdleDetection routine enables or cancels idle detection and sets idle time-out values for a device. |
| [PoRegisterPowerSettingCallback function](nf-ntifs-poregisterpowersettingcallback.md) | The PoRegisterPowerSettingCallback routine registers a power-setting callback routine to receive notifications of changes in the specified power setting. |
| [PoRegisterSystemState function](nf-ntifs-poregistersystemstate.md) | The PoRegisterSystemState routine registers the system as busy due to certain activity. |
| [PoSetDeviceBusyEx function](nf-ntifs-posetdevicebusyex.md) | The PoSetDeviceBusyEx routine notifies the power manager that the device associated with the specified idle counter is busy. |
| [PoSetPowerRequest function](nf-ntifs-posetpowerrequest.md) | The PoSetPowerRequest routine increments the count for the specified power request type. |
| [PoSetPowerState function](nf-ntifs-posetpowerstate.md) | The PoSetPowerState routine notifies the system of a change in the device power state for a device. |
| [PoStartDeviceBusy function](nf-ntifs-postartdevicebusy.md) | The PoStartDeviceBusy routine marks the start of a period of time in which the device is busy. |
| [PoStartNextPowerIrp function](nf-ntifs-postartnextpowerirp.md) | The PoStartNextPowerIrp routine signals the power manager that the driver is ready to handle the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only.). |
| [PoUnregisterPowerSettingCallback function](nf-ntifs-pounregisterpowersettingcallback.md) | The PoUnregisterPowerSettingCallback routine unregisters a power-setting callback routine that a driver previously registered by calling the PoRegisterPowerSettingCallback routine. |
| [PoUnregisterSystemState function](nf-ntifs-pounregistersystemstate.md) | The PoUnregisterSystemState routine cancels a system state registration created by PoRegisterSystemState. |
| [PsChargePoolQuota function](nf-ntifs-pschargepoolquota.md) | The PsChargePoolQuota routine charges pool quota of the specified pool type to the specified process. |
| [PsDereferenceImpersonationToken function](nf-ntifs-psdereferenceimpersonationtoken.md) | The PsDereferenceImpersonationToken routine decrements the reference count of an impersonation token. |
| [PsDereferencePrimaryToken function](nf-ntifs-psdereferenceprimarytoken.md) | The PsDereferencePrimaryToken routine decrements the reference count of a primary token. |
| [PsGetCurrentThread function](nf-ntifs-psgetcurrentthread.md) | The PsGetCurrentThread routine identifies the current thread. |
| [PsGetProcessExitTime function](nf-ntifs-psgetprocessexittime.md) | The PsGetProcessExitTime routine returns the exit time for the current process. |
| [PsImpersonateClient function](nf-ntifs-psimpersonateclient.md) | The PsImpersonateClient routine causes a server thread to impersonate a client. |
| [PsIsDiskCountersEnabled function](nf-ntifs-psisdiskcountersenabled.md) | The enabled state of the per process disk I/O counters is returned by the PsIsDiskCountersEnabled routine. |
| [PsIsSystemThread function](nf-ntifs-psissystemthread.md) | The PsIsSystemThread routine checks whether a given thread is a system thread. |
| [PsIsThreadTerminating function](nf-ntifs-psisthreadterminating.md) | The PsIsThreadTerminating routine checks whether a thread is terminating. |
| [PsLookupProcessByProcessId function](nf-ntifs-pslookupprocessbyprocessid.md) | The PsLookupProcessByProcessId routine accepts the process ID of a process and returns a referenced pointer to EPROCESS structure of the process. |
| [PsLookupThreadByThreadId function](nf-ntifs-pslookupthreadbythreadid.md) | The PsLookupThreadByThreadId routine accepts the thread ID of a thread and returns a referenced pointer to the ETHREAD structure of the thread. |
| [PsReferenceImpersonationToken function](nf-ntifs-psreferenceimpersonationtoken.md) | The PsReferenceImpersonationToken routine increments the reference count of the impersonation token for the specified thread. |
| [PsReferencePrimaryToken function](nf-ntifs-psreferenceprimarytoken.md) | The PsReferencePrimaryToken routine increments the reference count of the primary token for the specified process. |
| [PsReturnPoolQuota function](nf-ntifs-psreturnpoolquota.md) | The PsReturnPoolQuota routine returns pool quota of the specified pool type to the specified process. |
| [PsRevertToSelf function](nf-ntifs-psreverttoself.md) | The PsRevertToSelf routine ends the calling thread's impersonation of a client. |
| [PsUpdateDiskCounters function](nf-ntifs-psupdatediskcounters.md) | The PsUpdateDiskCounters routine updates the disk I/O counters of a given process. |
| [RtlAbsoluteToSelfRelativeSD function](nf-ntifs-rtlabsolutetoselfrelativesd.md) | The RtlAbsoluteToSelfRelativeSD routine creates a new security descriptor in self-relative format by using a security descriptor in absolute format as a template. |
| [RtlAddAccessAllowedAce function](nf-ntifs-rtladdaccessallowedace.md) | The RtlAddAccessAllowedAce routine adds an access-allowed access control entry (ACE) to an access control list (ACL). The access is granted to the specified security identifier (SID). |
| [RtlAddAccessAllowedAceEx function](nf-ntifs-rtladdaccessallowedaceex.md) | The RtlAddAccessAllowedAceEx routine adds an access-allowed access control entry (ACE) with inheritance ACE flags to an access control list (ACL). The access is granted to the specified security identifier (SID). |
| [RtlAddAce function](nf-ntifs-rtladdace.md) | The RtlAddAce routine adds one or more access control entries (ACEs) to a specified access control list (ACL). |
| [RtlAllocateHeap function](nf-ntifs-rtlallocateheap.md) | The RtlAllocateHeap routine allocates a block of memory from a heap. |
| [RtlAppendStringToString function](nf-ntifs-rtlappendstringtostring.md) | The RtlAppendStringToString routine concatenates two counted strings. It copies bytes from the source up to the length of the destination buffer. |
| [RtlCaptureContext function](nf-ntifs-rtlcapturecontext.md) | The RtlCaptureContext function retrieves a context record in the context of the caller. |
| [RtlCaptureStackBackTrace function](nf-ntifs-rtlcapturestackbacktrace.md) | The RtlCaptureStackBackTrace routine captures a stack back trace by walking up the stack and recording the information for each frame. |
| [RtlCompareMemoryUlong function](nf-ntifs-rtlcomparememoryulong.md) | The RtlCompareMemoryUlong routine returns how many bytes in a block of memory match a specified pattern. |
| [RtlCompressBuffer function](nf-ntifs-rtlcompressbuffer.md) | The RtlCompressBuffer function compresses a buffer and can be used by a file system driver to facilitate the implementation of file compression. |
| [RtlConvertSidToUnicodeString function](nf-ntifs-rtlconvertsidtounicodestring.md) | The RtlConvertSidToUnicodeString routine generates a printable Unicode string representation of a security identifier (SID). |
| [RtlCopyLuid function](nf-ntifs-rtlcopyluid.md) | The RtlCopyLuid routine copies a locally unique identifier (LUID) to a buffer. |
| [RtlCopySid function](nf-ntifs-rtlcopysid.md) | The RtlCopySid routine copies the value of a security identifier (SID) to a buffer. |
| [RtlCreateAcl function](nf-ntifs-rtlcreateacl.md) | The RtlCreateAcl routine creates and initializes an access control list (ACL). |
| [RtlCreateHeap function](nf-ntifs-rtlcreateheap.md) | The RtlCreateHeap routine creates a heap object that can be used by the calling process. This routine reserves space in the virtual address space of the process and allocates physical storage for a specified initial portion of this block. |
| [RtlCreateSecurityDescriptorRelative function](nf-ntifs-rtlcreatesecuritydescriptorrelative.md) | The RtlCreateSecurityDescriptorRelative routine initializes a new security descriptor in self-relative format. |
| [RtlCreateSystemVolumeInformationFolder function](nf-ntifs-rtlcreatesystemvolumeinformationfolder.md) | The RtlCreateSystemVolumeInformationFolder routine verifies the existence of the &#0034;System Volume Information&#0034; folder on a file system volume. If the folder is not present, then the folder is created. |
| [RtlCreateUnicodeString function](nf-ntifs-rtlcreateunicodestring.md) | The RtlCreateUnicodeString routine creates a new counted Unicode string. |
| [RtlDecompressBuffer function](nf-ntifs-rtldecompressbuffer.md) | The RtlDecompressBuffer function decompresses an entire compressed buffer. |
| [RtlDecompressBufferEx function](nf-ntifs-rtldecompressbufferex.md) | The RtlDecompressBufferEx function decompresses an entire compressed buffer. |
| [RtlDecompressBufferEx2 function](nf-ntifs-rtldecompressbufferex2.md) | The RtlDecompressBufferEx2 function decompresses an entire compressed buffer, using multiple processors where possible. Multiple processor support is only implemented for kernel mode callers. |
| [RtlDecompressFragment function](nf-ntifs-rtldecompressfragment.md) | The RtlDecompressFragment function is used to decompress part of a compressed buffer (that is, a buffer &#0034;fragment&#0034;). |
| [RtlDecompressFragmentEx function](nf-ntifs-rtldecompressfragmentex.md) | The RtlDecompressFragmentEx function is used to decompress part of a compressed buffer (that is, a buffer &#0034;fragment&#0034;), using multiple processors where possible. |
| [RtlDeleteAce function](nf-ntifs-rtldeleteace.md) | The RtlDeleteAce routine deletes an access control entry (ACE) from a specified access control list (ACL). |
| [RtlDestroyHeap function](nf-ntifs-rtldestroyheap.md) | The RtlDestroyHeap routine destroys the specified heap object. RtlDestroyHeap decommits and releases all the pages of a private heap object, and it invalidates the handle to the heap. |
| [RtlDowncaseUnicodeString function](nf-ntifs-rtldowncaseunicodestring.md) | The RtlDowncaseUnicodeString routine converts the specified Unicode source string to lowercase. The translation conforms to the current system locale information. |
| [RtlEqualPrefixSid function](nf-ntifs-rtlequalprefixsid.md) | The RtlEqualPrefixSid routine determines whether two security-identifier (SID) prefixes are equal. An SID prefix is the entire SID except for the last subauthority value. |
| [RtlEqualSid function](nf-ntifs-rtlequalsid.md) | The RtlEqualSid routine determines whether two security identifier (SID) values are equal. Two SIDs must match exactly to be considered equal. |
| [RtlFillMemoryUlong function](nf-ntifs-rtlfillmemoryulong.md) | The RtlFillMemoryUlong routine fills the specified range of memory with one or more repetitions of a ULONG value. |
| [RtlFillMemoryUlong function](nf-ntifs-rtlfillmemoryulong~r1.md) | The RtlFillMemoryUlong routine fills the specified range of memory with one or more repetitions of a ULONG value. |
| [RtlFillMemoryUlonglong function](nf-ntifs-rtlfillmemoryulonglong.md) | The RtlFillMemoryUlonglong routine fills a given range of memory with one or more repetitions of a given ULONGLONG value. |
| [RtlFillMemoryUlonglong function](nf-ntifs-rtlfillmemoryulonglong~r1.md) | The RtlFillMemoryUlonglong routine fills a given range of memory with one or more repetitions of a given ULONGLONG value. |
| [RtlFindUnicodePrefix function](nf-ntifs-rtlfindunicodeprefix.md) | The RtlFindUnicodePrefix routine searches for the best match for a given Unicode file name in a prefix table. |
| [RtlFreeHeap function](nf-ntifs-rtlfreeheap.md) | The RtlFreeHeap routine frees a memory block that was allocated from a heap by RtlAllocateHeap. |
| [RtlFreeHeap function](nf-ntifs-rtlfreeheap~r1.md) | The RtlFreeHeap routine frees a memory block that was allocated from a heap by RtlAllocateHeap. |
| [RtlFreeOemString function](nf-ntifs-rtlfreeoemstring.md) | The RtlFreeOemString routine releases storage that was allocated by any of the Rtl..ToOemString routines. |
| [RtlGenerate8dot3Name function](nf-ntifs-rtlgenerate8dot3name.md) | The RtlGenerate8dot3Name routine generates a short (8.3) name for the specified long file name. |
| [RtlGenerate8dot3Name function](nf-ntifs-rtlgenerate8dot3name~r1.md) | The RtlGenerate8dot3Name routine generates a short (8.3) name for the specified long file name. |
| [RtlGetAce function](nf-ntifs-rtlgetace.md) | The RtlGetAce routine obtains a pointer to an access control entry (ACE) in an access control list (ACL). |
| [RtlGetCompressionWorkSpaceSize function](nf-ntifs-rtlgetcompressionworkspacesize.md) | The RtlGetCompressionWorkSpaceSize function is used to determine the correct size of the WorkSpace buffer for the RtlCompressBuffer and RtlDecompressFragment functions. |
| [RtlGetDaclSecurityDescriptor function](nf-ntifs-rtlgetdaclsecuritydescriptor.md) | The RtlGetDaclSecurityDescriptor routine returns a pointer to the discretionary ACL (DACL) for a security descriptor. |
| [RtlGetGroupSecurityDescriptor function](nf-ntifs-rtlgetgroupsecuritydescriptor.md) | The RtlGetGroupSecurityDescriptor routine returns the primary group information for a given security descriptor. |
| [RtlGetOwnerSecurityDescriptor function](nf-ntifs-rtlgetownersecuritydescriptor.md) | The RtlGetOwnerSecurityDescriptor routine returns the owner information for a given security descriptor. |
| [RtlGetSaclSecurityDescriptor function](nf-ntifs-rtlgetsaclsecuritydescriptor.md) | The RtlGetSaclSecurityDescriptor routine returns a pointer to the system ACL (SACL) for a security descriptor. |
| [RtlInitStringEx function](nf-ntifs-rtlinitstringex.md) | The RtlInitStringEx routine initializes a counted string of 8-bit characters. |
| [RtlInitializeSid function](nf-ntifs-rtlinitializesid.md) | The RtlInitializeSid routine initializes a security identifier (SID) structure. |
| [RtlInitializeSidEx function](nf-ntifs-rtlinitializesidex.md) | The RtlInitializeSidEx routine initializes a pre-allocated security identifier (SID) structure. |
| [RtlInitializeUnicodePrefix function](nf-ntifs-rtlinitializeunicodeprefix.md) | The RtlInitializeUnicodePrefix routine initializes a prefix table. |
| [RtlInsertUnicodePrefix function](nf-ntifs-rtlinsertunicodeprefix.md) | The RtlInsertUnicodePrefix routine inserts a new element into a Unicode prefix table. |
| [RtlIsCloudFilesPlaceholder function](nf-ntifs-rtliscloudfilesplaceholder.md) | The RtlIsCloudFilesPlaceholder routine determines if a file or a directory is a CloudFiles placeholder, based on the FileAttributes and ReparseTag values of the file. |
| [RtlIsNameLegalDOS8Dot3 function](nf-ntifs-rtlisnamelegaldos8dot3.md) | The RtlIsNameLegalDOS8Dot3 routine determines whether a given name represents a valid short (8.3) file name. |
| [RtlIsPartialPlaceholder function](nf-ntifs-rtlispartialplaceholder.md) | The RtlIsPartialPlaceholder routine determines if a file or a directory is a CloudFiles placeholder, based on the FileAttributes and ReparseTag values of the file. |
| [RtlIsPartialPlaceholderFileHandle function](nf-ntifs-rtlispartialplaceholderfilehandle.md) | The RtlIsPartialPlaceholderFileHandle routine determines if a file is a known type of placeholder, based on a file handle. |
| [RtlIsPartialPlaceholderFileInfo function](nf-ntifs-rtlispartialplaceholderfileinfo.md) | The RtlIsPartialPlaceholderFileInfo routine determines if a file is a known type of placeholder, based on the information returned by NtQueryInformationFile or NtQueryDirectoryFile. |
| [RtlIsValidOemCharacter function](nf-ntifs-rtlisvalidoemcharacter.md) | The RtlIsValidOemCharacter routine determines if the specified Unicode character can be mapped to a valid OEM character. |
| [RtlLengthRequiredSid function](nf-ntifs-rtllengthrequiredsid.md) | The RtlLengthRequiredSid routine returns the length, in bytes, of the buffer required to store a security identifier (SID) with a specified number of subauthorities. |
| [RtlLengthSid function](nf-ntifs-rtllengthsid.md) | The RtlLengthSid routine returns the length, in bytes, of a valid security identifier (SID). |
| [RtlMultiByteToUnicodeN function](nf-ntifs-rtlmultibytetounicoden.md) | The RtlMultiByteToUnicodeN routine translates the specified source string into a Unicode string, using the current system ANSI code page (ACP). The source string is not necessarily from a multibyte character set. |
| [RtlMultiByteToUnicodeSize function](nf-ntifs-rtlmultibytetounicodesize.md) | The RtlMultiByteToUnicodeSize routine determines the number of bytes that are required to store the Unicode translation for the specified source string. |
| [RtlNextUnicodePrefix function](nf-ntifs-rtlnextunicodeprefix.md) | The RtlNextUnicodePrefix routine is used to enumerate the elements in a Unicode prefix table. |
| [RtlNtStatusToDosError function](nf-ntifs-rtlntstatustodoserror.md) | The RtlNtStatusToDosError routine converts the specified NTSTATUS code to its equivalent system error code. |
| [RtlNtStatusToDosErrorNoTeb function](nf-ntifs-rtlntstatustodoserrornoteb.md) | Reserved for system use. |
| [RtlOemStringToCountedUnicodeSize function](nf-ntifs-rtloemstringtocountedunicodesize.md) | The RtlOemStringToCountedUnicodeSize routine determines the size, in bytes, that a given OEM string will be after it is translated into a counted Unicode string. |
| [RtlOemStringToCountedUnicodeString function](nf-ntifs-rtloemstringtocountedunicodestring.md) | The RtlOemStringToCountedUnicodeString routine translates the specified source string into a Unicode string using the current system OEM code page. |
| [RtlOemStringToUnicodeSize function](nf-ntifs-rtloemstringtounicodesize.md) | The RtlOemStringToUnicodeSize routine determines the size, in bytes, that a given OEM string will be after it is translated into a null-terminated Unicode string. |
| [RtlOemStringToUnicodeString function](nf-ntifs-rtloemstringtounicodestring.md) | The RtlOemStringToUnicodeString routine translates a given source string into a null-terminated Unicode string using the current system OEM code page. |
| [RtlOemToUnicodeN function](nf-ntifs-rtloemtounicoden.md) | The RtlOemToUnicodeN routine translates the specified source string into a Unicode string, using the current system OEM code page. |
| [RtlQueryThreadPlaceholderCompatibilityMode function](nf-ntifs-rtlquerythreadplaceholdercompatibilitymode.md) | RtlQueryThreadPlaceholderCompatibilityMode is a routine which returns the placeholder compatibility mode for the current thread. |
| [RtlRandom function](nf-ntifs-rtlrandom.md) | The RtlRandom routine returns a random number that was generated from a given seed value. |
| [RtlRandomEx function](nf-ntifs-rtlrandomex.md) | The RtlRandomEx routine returns a random number that was generated from a given seed value. |
| [RtlRemoveUnicodePrefix function](nf-ntifs-rtlremoveunicodeprefix.md) | The RtlRemoveUnicodePrefix routine removes an element from a prefix table. |
| [RtlSecondsSince1970ToTime function](nf-ntifs-rtlsecondssince1970totime.md) | The RtlSecondsSince1970ToTime routine converts the elapsed time, in seconds, since the beginning of 1970 to an absolute system time value. |
| [RtlSecondsSince1980ToTime function](nf-ntifs-rtlsecondssince1980totime.md) | The RtlSecondsSince1980ToTime routine converts the elapsed time, in seconds, since the beginning of 1980 to an absolute system time value. |
| [RtlSelfRelativeToAbsoluteSD function](nf-ntifs-rtlselfrelativetoabsolutesd.md) | The RtlSelfRelativeToAbsoluteSD routine creates a new security descriptor in absolute format by using a security descriptor in self-relative format as a template. |
| [RtlSetGroupSecurityDescriptor function](nf-ntifs-rtlsetgroupsecuritydescriptor.md) | The RtlSetGroupSecurityDescriptor routine sets the primary group information of an absolute-format security descriptor. It replaces any primary group information that is already present in the security descriptor. |
| [RtlSetOwnerSecurityDescriptor function](nf-ntifs-rtlsetownersecuritydescriptor.md) | The RtlSetOwnerSecurityDescriptor routine sets the owner information of an absolute-format security descriptor. It replaces any owner information that is already present in the security descriptor. |
| [RtlSetThreadPlaceholderCompatibilityMode function](nf-ntifs-rtlsetthreadplaceholdercompatibilitymode.md) | RtlSetThreadPlaceholderCompatibilityMode is a routine which sets the placeholder compatibility mode for the current thread. |
| [RtlSubAuthoritySid function](nf-ntifs-rtlsubauthoritysid.md) | The RtlSubAuthoritySid routine returns a pointer to a specified subauthority of a security identifier (SID). |
| [RtlTimeToSecondsSince1970 function](nf-ntifs-rtltimetosecondssince1970.md) | The RtlTimeToSecondsSince1970 routine converts a given absolute system time value to the elapsed time, in seconds, since the beginning of 1970. |
| [RtlTimeToSecondsSince1980 function](nf-ntifs-rtltimetosecondssince1980.md) | The RtlTimeToSecondsSince1980 routine converts a given absolute system time value to the elapsed time, in seconds, since the beginning of 1980. |
| [RtlUTF8ToUnicodeN function](nf-ntifs-rtlutf8tounicoden.md) | The RtlUTF8ToUnicodeN routine converts a UTF-8 string to a Unicode string. |
| [RtlUnicodeStringToCountedOemString function](nf-ntifs-rtlunicodestringtocountedoemstring.md) | The RtlUnicodeStringToCountedOemString routine translates the specified Unicode source string into a counted OEM string using the current system OEM code page. |
| [RtlUnicodeStringToOemSize function](nf-ntifs-rtlunicodestringtooemsize.md) | The RtlUnicodeStringToOemSize routine determines the size, in bytes, that a given Unicode string will be after it is translated into an OEM string. |
| [RtlUnicodeStringToOemString function](nf-ntifs-rtlunicodestringtooemstring.md) | The RtlUnicodeStringToOemString routine translates a given Unicode source string into an OEM string using the current system OEM code page. |
| [RtlUnicodeToMultiByteN function](nf-ntifs-rtlunicodetomultibyten.md) | The RtlUnicodeToMultiByteN routine translates the specified Unicode string into a new character string, using the current system ANSI code page (ACP). The translated string is not necessarily from a multibyte character set. |
| [RtlUnicodeToMultiByteSize function](nf-ntifs-rtlunicodetomultibytesize.md) | The RtlUnicodeToMultiByteSize routine determines the number of bytes that are required to store the multibyte translation for the specified Unicode string. The translation is assumed to use the current system ANSI code page (ACP). |
| [RtlUnicodeToOemN function](nf-ntifs-rtlunicodetooemn.md) | The RtlUnicodeToOemN routine translates a given Unicode string to an OEM string, using the current system OEM code page. |
| [RtlUnicodeToUTF8N function](nf-ntifs-rtlunicodetoutf8n.md) | The RtlUnicodeToUTF8N routine converts a Unicode string to a UTF-8 string. |
| [RtlUpcaseUnicodeStringToCountedOemString function](nf-ntifs-rtlupcaseunicodestringtocountedoemstring.md) | The RtlUpcaseUnicodeStringToCountedOemString routine translates a given Unicode source string into an uppercase counted OEM string using the current system OEM code page. |
| [RtlUpcaseUnicodeStringToOemString function](nf-ntifs-rtlupcaseunicodestringtooemstring.md) | The RtlUpcaseUnicodeStringToOemString routine translates a given Unicode source string into an uppercase OEM string using the current system OEM code page. |
| [RtlUpcaseUnicodeToMultiByteN function](nf-ntifs-rtlupcaseunicodetomultibyten.md) | The RtlUpcaseUnicodeToMultiByteN routine translates the specified Unicode string into a new uppercase character string, using the current system ANSI code page (ACP). The translated string is not necessarily from a multibyte character set. |
| [RtlUpcaseUnicodeToOemN function](nf-ntifs-rtlupcaseunicodetooemn.md) | The RtlUpcaseUnicodeToOemN routine translates a given Unicode string into an uppercase OEM string, using the current system OEM code page. |
| [RtlValidSid function](nf-ntifs-rtlvalidsid.md) | The RtlValidSid routine validates a security identifier (SID) by verifying that the revision number is within a known range and that the number of subauthorities is less than the maximum. |
| [SeAppendPrivileges function](nf-ntifs-seappendprivileges.md) | The SeAppendPrivileges routine appends additional privileges to the privilege set in an access state structure. |
| [SeAuditingFileEvents function](nf-ntifs-seauditingfileevents.md) | The SeAuditingFileEvents routine determines whether file open events are currently being audited. |
| [SeAuditingFileOrGlobalEvents function](nf-ntifs-seauditingfileorglobalevents.md) | The SeAuditingFileOrGlobalEvents routine determines whether file or global events are currently being audited. |
| [SeCaptureSubjectContext function](nf-ntifs-secapturesubjectcontext.md) | The SeCaptureSubjectContext routine captures the security context of the calling thread for access validation and auditing. |
| [SeCreateClientSecurity function](nf-ntifs-secreateclientsecurity.md) | The SeCreateClientSecurity routine initializes a security client context structure with the information needed to call SeImpersonateClientEx. |
| [SeCreateClientSecurityFromSubjectContext function](nf-ntifs-secreateclientsecurityfromsubjectcontext.md) | The SeCreateClientSecurityFromSubjectContext routine retrieves the access token for a security subject context and uses the result to initialize a security client context with the information needed to call SeImpersonateClientEx. |
| [SeDeleteClientSecurity function](nf-ntifs-sedeleteclientsecurity.md) | The SeDeleteClientSecurity routine deletes a client security context. |
| [SeDeleteObjectAuditAlarm function](nf-ntifs-sedeleteobjectauditalarm.md) | The SeDeleteObjectAuditAlarm routine generates audit and alarm messages for an object that is marked for deletion. |
| [SeFilterToken function](nf-ntifs-sefiltertoken.md) | The SeFilterToken routine creates a new access token that is a restricted version of an existing access token. |
| [SeFreePrivileges function](nf-ntifs-sefreeprivileges.md) | The SeFreePrivileges routine frees a privilege set returned by SeAccessCheck. |
| [SeImpersonateClientEx function](nf-ntifs-seimpersonateclientex.md) | The SeImpersonateClientEx routine causes a thread to impersonate a user. |
| [SeLockSubjectContext function](nf-ntifs-selocksubjectcontext.md) | The SeLockSubjectContext routine locks the primary and impersonation tokens of a captured subject context. |
| [SeMarkLogonSessionForTerminationNotification function](nf-ntifs-semarklogonsessionforterminationnotification.md) | The SeMarkLogonSessionForTerminationNotification routine marks a logon session so that the caller's registered callback routine is called when the logon session terminates. |
| [SeOpenObjectAuditAlarm function](nf-ntifs-seopenobjectauditalarm.md) | The SeOpenObjectAuditAlarm routine generates audit and alarm messages when an attempt is made to open an object. |
| [SeOpenObjectForDeleteAuditAlarm function](nf-ntifs-seopenobjectfordeleteauditalarm.md) | The SeOpenObjectForDeleteAuditAlarm routine generates audit and alarm messages when an attempt is made to open an object for deletion. |
| [SePrivilegeCheck function](nf-ntifs-seprivilegecheck.md) | The SePrivilegeCheck routine determines whether a specified set of privileges is enabled in the subject's access token. |
| [SeQueryAuthenticationIdToken function](nf-ntifs-sequeryauthenticationidtoken.md) | The SeQueryAuthenticationIdToken routine retrieves the authentication ID of an access token. |
| [SeQueryInformationToken function](nf-ntifs-sequeryinformationtoken.md) | The SeQueryInformationToken routine retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information. |
| [SeQuerySecurityDescriptorInfo function](nf-ntifs-sequerysecuritydescriptorinfo.md) | The SeQuerySecurityDescriptorInfo routine retrieves a copy of an object's security descriptor. |
| [SeQuerySubjectContextToken function](nf-ntifs-sequerysubjectcontexttoken.md) | The SeQuerySubjectContextToken macro retrieves the access token for a security subject context. |
| [SeRegisterLogonSessionTerminatedRoutine function](nf-ntifs-seregisterlogonsessionterminatedroutine.md) | The SeRegisterLogonSessionTerminatedRoutine routine registers a callback routine to be called when a logon session terminates. A logon session terminates when the last token referencing the logon session is deleted. |
| [SeReleaseSubjectContext function](nf-ntifs-sereleasesubjectcontext.md) | The SeReleaseSubjectContext routine releases a subject security context captured by an earlier call to SeCaptureSubjectContext. |
| [SeSetAccessStateGenericMapping function](nf-ntifs-sesetaccessstategenericmapping.md) | The SeSetAccessStateGenericMapping routine sets the generic mapping field of an ACCESS_STATE structure. |
| [SeSetSecurityDescriptorInfo function](nf-ntifs-sesetsecuritydescriptorinfo.md) | The SeSetSecurityDescriptorInfo routine sets an object's security descriptor. |
| [SeSetSecurityDescriptorInfoEx function](nf-ntifs-sesetsecuritydescriptorinfoex.md) | The SeSetSecurityDescriptorInfoEx routine modifies an object's security descriptor and specifies whether the object supports automatic inheritance of access control entries (ACE). |
| [SeTokenGetNoChildProcessRestricted function](nf-ntifs-setokengetnochildprocessrestricted.md) | The SeTokenGetNoChildProcessRestricted routine determines the state of the no child process mitigation. It is not possible to be enforced and audit-only at the same time. |
| [SeTokenIsAdmin function](nf-ntifs-setokenisadmin.md) | The SeTokenIsAdmin routine determines whether a token contains the local administrators group. |
| [SeTokenIsNoChildProcessRestrictionEnforced function](nf-ntifs-setokenisnochildprocessrestrictionenforced.md) | The SeTokenIsNoChildProcessRestrictionEnforced routine determines if the token carries the no child process restriction. |
| [SeTokenIsRestricted function](nf-ntifs-setokenisrestricted.md) | The SeTokenIsRestricted routine determines whether a token contains a list of restricting security identifiers (SID). |
| [SeTokenSetNoChildProcessRestricted function](nf-ntifs-setokensetnochildprocessrestricted.md) | The SeTokenSetNoChildProcessRestricted routine sets the TOKEN_AUDIT_NO_CHILD_PROCESS or TOKEN_AUDIT_NO_CHILD_PROCESS flags in the token. |
| [SeUnlockSubjectContext function](nf-ntifs-seunlocksubjectcontext.md) | The SeUnlockSubjectContext routine unlocks the tokens of a captured subject context that were locked by a call to SeLockSubjectContext. |
| [SeUnregisterLogonSessionTerminatedRoutine function](nf-ntifs-seunregisterlogonsessionterminatedroutine.md) | The SeUnregisterLogonSessionTerminatedRoutine routine unregisters a callback routine that was registered by an earlier call to SeRegisterLogonSessionTerminatedRoutine. |
| [SecLookupAccountName function](nf-ntifs-seclookupaccountname.md) | SecLookupAccountName accepts an account as input and retrieves a security identifier (SID) for the account and the name of the domain on which the account was found. |
| [SecLookupAccountSid function](nf-ntifs-seclookupaccountsid.md) | SecLookupAccountSid accepts a security identifier (SID) as input. It retrieves the name of the account for this SID and the name of the first domain on which this SID is found. |
| [SecLookupWellKnownSid function](nf-ntifs-seclookupwellknownsid.md) | SecLookupWellKnownSid accepts a well-known security identifier (SID) type as input and retrieves the local security identifier (SID) for this well known SID. |
| [SecMakeSPN function](nf-ntifs-secmakespn.md) | SecMakeSPN creates a service provider name string that can be used when communicating with specific security service providers. |
| [SecMakeSPNEx function](nf-ntifs-secmakespnex.md) | SecMakeSPNEx creates a service provider name string that can be used when communicating with specific security service providers. |
| [SecMakeSPNEx2 function](nf-ntifs-secmakespnex2.md) | SecMakeSPNEx2 creates a service provider name string that can be used when it communicates with specific security service providers. |
| [ZwAllocateVirtualMemory function](nf-ntifs-zwallocatevirtualmemory.md) | The ZwAllocateVirtualMemory routine reserves, commits, or both, a region of pages within the user-mode virtual address space of a specified process. |
| [ZwCreateEvent function](nf-ntifs-zwcreateevent.md) | The ZwCreateEvent routine creates an event object, sets the initial state of the event to the specified value, and opens a handle to the object with the specified desired access. |
| [ZwDeleteFile function](nf-ntifs-zwdeletefile.md) | The ZwDeleteFile routine deletes the specified file. |
| [ZwDeviceIoControlFile function](nf-ntifs-zwdeviceiocontrolfile.md) | The ZwDeviceIoControlFile routine sends a control code directly to a specified device driver, causing the corresponding driver to perform the specified operation. |
| [ZwDuplicateObject function](nf-ntifs-zwduplicateobject.md) | The ZwDuplicateObject routine creates a handle that is a duplicate of the specified source handle. |
| [ZwDuplicateToken function](nf-ntifs-zwduplicatetoken.md) | The ZwDuplicateToken function creates a handle to a new access token that duplicates an existing token. This function can create either a primary token or an impersonation token. |
| [ZwFlushBuffersFile function](nf-ntifs-zwflushbuffersfile.md) | The ZwFlushBuffersFile routine is called by a file system filter driver to send a flush request for the specified file to the file system. |
| [ZwFlushBuffersFileEx function](nf-ntifs-zwflushbuffersfileex.md) | The ZwFlushBuffersFileEx routine is called by a file system filter driver to send a flush request for a given file to the file system. An optional flush operation flag can be set to control how file data is written to storage. |
| [ZwFlushVirtualMemory function](nf-ntifs-zwflushvirtualmemory.md) | The ZwFlushVirtualMemory routine flushes a range of virtual addresses within the virtual address space of a specified process which map to a data file back out to the data file if they have been modified. |
| [ZwFreeVirtualMemory function](nf-ntifs-zwfreevirtualmemory.md) | The ZwFreeVirtualMemory routine releases, decommits, or both, a region of pages within the virtual address space of a specified process. |
| [ZwFsControlFile function](nf-ntifs-zwfscontrolfile.md) | The ZwFsControlFile routine sends a control code directly to a specified file system or file system filter driver, causing the corresponding driver to perform the specified action. |
| [ZwLockFile function](nf-ntifs-zwlockfile.md) | The ZwLockFile routine requests a byte-range lock for the specified file. |
| [ZwNotifyChangeKey function](nf-ntifs-zwnotifychangekey.md) | The ZwNotifyChangeKey routine allows a driver to request notification when a registry key changes. |
| [ZwOpenDirectoryObject function](nf-ntifs-zwopendirectoryobject.md) | The ZwOpenDirectoryObject routine opens an existing directory object. |
| [ZwOpenProcessTokenEx function](nf-ntifs-zwopenprocesstokenex.md) | The ZwOpenProcessTokenEx routine opens the access token associated with a process. |
| [ZwOpenThreadTokenEx function](nf-ntifs-zwopenthreadtokenex.md) | The ZwOpenThreadTokenEx routine opens the access token associated with a thread. |
| [ZwQueryDirectoryFile function](nf-ntifs-zwquerydirectoryfile.md) | The ZwQueryDirectoryFile routine returns various kinds of information about files in the directory specified by a given file handle. |
| [ZwQueryDirectoryFileEx function](nf-ntifs-zwquerydirectoryfileex.md) | The ZwQueryDirectoryFileEx routine returns information about files in the directory specified by the FileHandle parameter. |
| [ZwQueryEaFile function](nf-ntifs-zwqueryeafile.md) | The ZwQueryEaFile routine returns information about extended-attribute (EA) values for a file. |
| [ZwQueryInformationToken function](nf-ntifs-zwqueryinformationtoken.md) | The ZwQueryInformationToken routine retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information. |
| [ZwQueryObject function](nf-ntifs-zwqueryobject.md) | The ZwQueryObject routine provides information about a supplied object. |
| [ZwQueryQuotaInformationFile function](nf-ntifs-zwqueryquotainformationfile.md) | The ZwQueryQuotaInformationFile routine retrieves quota entries associated with the volume specified by the FileHandle parameter. |
| [ZwQuerySecurityObject function](nf-ntifs-zwquerysecurityobject.md) | The ZwQuerySecurityObject routine retrieves a copy of an object's security descriptor. |
| [ZwQueryVirtualMemory function](nf-ntifs-zwqueryvirtualmemory.md) | The ZwQueryVirtualMemory routine determines the state, protection, and type of a region of pages within the virtual address space of the subject process. |
| [ZwQueryVolumeInformationFile function](nf-ntifs-zwqueryvolumeinformationfile.md) | The ZwQueryVolumeInformationFile routine retrieves information about the volume associated with a given file, directory, storage device, or volume. |
| [ZwSetEaFile function](nf-ntifs-zwseteafile.md) | The ZwSetEaFile routine sets extended-attribute (EA) values for a file. |
| [ZwSetEvent function](nf-ntifs-zwsetevent.md) | The ZwSetEvent routine sets an event object to a Signaled state and attempts to satisfy as many waits as possible. |
| [ZwSetInformationToken function](nf-ntifs-zwsetinformationtoken.md) | The ZwSetInformationToken routine modifies information in a specified token. The calling process must have appropriate access rights to set the information. |
| [ZwSetInformationVirtualMemory function](nf-ntifs-zwsetinformationvirtualmemory.md) | The ZwSetInformationVirtualMemory routine performs an operation on a specified list of address ranges in the user address space of a process. |
| [ZwSetQuotaInformationFile function](nf-ntifs-zwsetquotainformationfile.md) | The ZwSetQuotaInformationFile routine changes quota entries for the volume associated with the FileHandle parameter. All of the quota entries in the specified buffer are applied to the volume. |
| [ZwSetSecurityObject function](nf-ntifs-zwsetsecurityobject.md) | The ZwSetSecurityObject routine sets an object's security state. |
| [ZwSetVolumeInformationFile function](nf-ntifs-zwsetvolumeinformationfile.md) | The ZwSetVolumeInformationFile routine modifies information about the volume associated with a given file, directory, storage device, or volume. |
| [ZwUnlockFile function](nf-ntifs-zwunlockfile.md) | The ZwUnlockFile routine unlocks a byte-range lock in a file. |
| [ZwWaitForSingleObject function](nf-ntifs-zwwaitforsingleobject.md) | The ZwWaitForSingleObject routine waits until the specified object attains a state of Signaled. An optional time-out can also be specified. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [DRIVER_FS_NOTIFICATION callback](nc-ntifs-driver-fs-notification.md) | A PDRIVER_FS_NOTIFICATION-typed routine is called by the operating system when a file system registers or unregisters itself by using IoRegisterFileSystem or IoUnregisterFileSystem. |
| [PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK callback](nc-ntifs-pfsrtl-extra-create-parameter-cleanup-callback.md) | A file system filter driver (legacy filter) or a minifilter driver can register a PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK-typed routine as the filter driver's CleanupCallback callback routine for an extra create parameter (ECP) context structure. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [ACCESS_ALLOWED_ACE structure](ns-ntifs--access-allowed-ace.md) | The ACCESS_ALLOWED_ACE structure defines an access-control entry (ACE) for the discretionary access-control list (DACL) that controls access to an object. |
| [ACCESS_DENIED_ACE structure](ns-ntifs--access-denied-ace.md) | The ACCESS_DENIED_ACE structure defines an access-control entry (ACE) for the discretionary access-control list (DACL) controlling access to an object. |
| [ACE_HEADER structure](ns-ntifs--ace-header.md) | The ACE_HEADER structure describes the type and size of an access-control entry (ACE). |
| [ACL structure](ns-ntifs--acl.md) | The ACL structure is the header of an access-control list (ACL). A complete ACL consists of an ACL structure followed by an ordered list of zero or more access-control entries (ACE). |
| [ATOMIC_CREATE_ECP_CONTEXT structure](ns-ntifs--atomic-create-ecp-context.md) | This structure allows supplemental operations to be performed on a file atomically during create. |
| [BOOT_AREA_INFO structure](ns-ntifs--boot-area-info.md) | The BOOT_AREA_INFO structure contains the output for the FSCTL_GET_BOOT_AREA_INFO control code. |
| [ECP_OPEN_PARAMETERS structure](ns-ntifs--ecp-open-parameters.md) | The ECP_OPEN_PARAMETERS structure allows a caller to specify the purpose of opening of a file without interfering with existing handles and/or oplocks on the file. |
| [FILE_ACCESS_INFORMATION structure](ns-ntifs--file-access-information.md) | The FILE_ACCESS_INFORMATION structure is used to query for or set the access rights of a file. |
| [FILE_ALLOCATION_INFORMATION structure](ns-ntifs--file-allocation-information.md) | The FILE_ALLOCATION_INFORMATION structure is used to set the allocation size for a file. |
| [FILE_ALL_INFORMATION structure](ns-ntifs--file-all-information.md) | The FILE_ALL_INFORMATION structure is a container for several FILE_XXX_INFORMATION structures. |
| [FILE_BOTH_DIR_INFORMATION structure](ns-ntifs--file-both-dir-information.md) | The FILE_BOTH_DIR_INFORMATION structure is used to query detailed information for the files in a directory. |
| [FILE_COMPLETION_INFORMATION structure](ns-ntifs--file-completion-information.md) | The FILE_COMPLETION_INFORMATION structure contains the port handle and key for an I/O completion port created for a file handle. |
| [FILE_COMPRESSION_INFORMATION structure](ns-ntifs--file-compression-information.md) | The FILE_COMPRESSION_INFORMATION structure describes the state of a compressed data buffer. |
| [FILE_DIRECTORY_INFORMATION structure](ns-ntifs--file-directory-information.md) | The FILE_DIRECTORY_INFORMATION structure is used to query detailed information for the files in a directory. |
| [FILE_EA_INFORMATION structure](ns-ntifs--file-ea-information.md) | The FILE_EA_INFORMATION structure is used to query for the size of the extended attributes (EA) for a file. |
| [FILE_FS_ATTRIBUTE_INFORMATION structure](ns-ntifs--file-fs-attribute-information.md) | The FILE_FS_ATTRIBUTE_INFORMATION structure is used to query attribute information for a file system. |
| [FILE_FS_CONTROL_INFORMATION structure](ns-ntifs--file-fs-control-information.md) | The FILE_FS_CONTROL_INFORMATION structure is used to query or set control information for the files in a directory. |
| [FILE_FS_DRIVER_PATH_INFORMATION structure](ns-ntifs--file-fs-driver-path-information.md) | The FILE_FS_DRIVER_PATH_INFORMATION structure is used to query whether a given driver is in the I/O path for a file system volume. |
| [FILE_FS_PERSISTENT_VOLUME_INFORMATION structure](ns-ntifs--file-fs-persistent-volume-information.md) | The FILE_FS_PERSISTENT_VOLUME_INFORMATION structure is used to control persistent settings for a file system volume. Persistent settings persist on a file system volume between reboots of the computer. |
| [FILE_FULL_DIR_INFORMATION structure](ns-ntifs--file-full-dir-information.md) | The FILE_FULL_DIR_INFORMATION structure is used to query detailed information for the files in a directory. |
| [FILE_GET_EA_INFORMATION structure](ns-ntifs--file-get-ea-information.md) | The FILE_GET_EA_INFORMATION structure is used to query for extended-attribute (EA) information. |
| [FILE_GET_QUOTA_INFORMATION structure](ns-ntifs--file-get-quota-information.md) | The FILE_GET_QUOTA_INFORMATION structure is used to query for quota information. |
| [FILE_ID_BOTH_DIR_INFORMATION structure](ns-ntifs--file-id-both-dir-information.md) | The FILE_ID_BOTH_DIR_INFORMATION structure is used to query file reference number information for the files in a directory. |
| [FILE_ID_EXTD_BOTH_DIR_INFORMATION structure](ns-ntifs--file-id-extd-both-dir-information.md) | The FILE_ID_EXTD_BOTH_DIR_INFORMATION structure is used to query file reference number information for the files in a directory. |
| [FILE_ID_FULL_DIR_INFORMATION structure](ns-ntifs--file-id-full-dir-information.md) | The FILE_ID_FULL_DIR_INFORMATION structure is used to query detailed information for the files in a directory. |
| [FILE_ID_GLOBAL_TX_DIR_INFORMATION structure](ns-ntifs--file-id-global-tx-dir-information.md) | The FILE_ID_GLOBAL_TX_DIR_INFORMATION structure contains information about transactional visibility for the files in a directory. |
| [FILE_INTERNAL_INFORMATION structure](ns-ntifs--file-internal-information.md) | The FILE_INTERNAL_INFORMATION structure is used to query for the file system's 8-byte file reference number for a file. |
| [FILE_LEVEL_TRIM structure](ns-ntifs--file-level-trim.md) | The FILE_LEVEL_TRIM structure contains an array of byte ranges to trim for a file. |
| [FILE_LEVEL_TRIM_OUTPUT structure](ns-ntifs--file-level-trim-output.md) | The FILE_LEVEL_TRIM_OUTPUT structure contains the results of a trim operation performed by an FSCTL_FILE_LEVEL_TRIM request. |
| [FILE_LEVEL_TRIM_RANGE structure](ns-ntifs--file-level-trim-range.md) | Contains the offset and length of a trim range for a file. |
| [FILE_LINKS_INFORMATION structure](ns-ntifs--file-links-information.md) | The FILE_LINKS_INFORMATION structure is used to query NTFS hard links to an existing file. |
| [FILE_LINK_ENTRY_INFORMATION structure](ns-ntifs--file-link-entry-information.md) | The FILE_LINK_ENTRY_INFORMATION structure describes a single NTFS hard link to an existing file. |
| [FILE_LINK_INFORMATION structure](ns-ntifs--file-link-information.md) | The FILE_LINK_INFORMATION structure is used to create an NTFS hard link to an existing file. |
| [FILE_MAILSLOT_QUERY_INFORMATION structure](ns-ntifs--file-mailslot-query-information.md) | The FILE_MAILSLOT_QUERY_INFORMATION structure contains information about a mailslot. |
| [FILE_MAILSLOT_SET_INFORMATION structure](ns-ntifs--file-mailslot-set-information.md) | The FILE_MAILSLOT_SET_INFORMATION structure is used to set a value on a mailslot. |
| [FILE_MODE_INFORMATION structure](ns-ntifs--file-mode-information.md) | The FILE_MODE_INFORMATION structure is used to query or set the access mode of a file. |
| [FILE_NAMES_INFORMATION structure](ns-ntifs--file-names-information.md) | A FILE_NAMES_INFORMATION structure used to query detailed information about the names of files in a directory. |
| [FILE_NETWORK_PHYSICAL_NAME_INFORMATION structure](ns-ntifs--file-network-physical-name-information.md) | Contains the full UNC physical pathname for a file or directory on a remote file share. |
| [FILE_OBJECTID_INFORMATION structure](ns-ntifs--file-objectid-information.md) | The FILE_OBJECTID_INFORMATION structure is used to query for object ID information for the files in a directory on an NTFS volume. |
| [FILE_PIPE_INFORMATION structure](ns-ntifs--file-pipe-information.md) | The FILE_PIPE_INFORMATION structure contains information about a named pipe that is not specific to the local or the remote end of the pipe. |
| [FILE_PIPE_LOCAL_INFORMATION structure](ns-ntifs--file-pipe-local-information.md) | The FILE_PIPE_LOCAL_INFORMATION structure contains information about the local end of a named pipe. |
| [FILE_PIPE_REMOTE_INFORMATION structure](ns-ntifs--file-pipe-remote-information.md) | The FILE_PIPE_REMOTE_INFORMATION structure contains information about the remote end of a named pipe. |
| [FILE_PROVIDER_EXTERNAL_INFO_V0 structure](ns-ntifs--file-provider-external-info-v0.md) | This structure may be altered or unavailable. Instead, use FILE_PROVIDER_EXTERNAL_INFO_V1. |
| [FILE_PROVIDER_EXTERNAL_INFO_V1 structure](ns-ntifs--file-provider-external-info-v1.md) | The FILE_PROVIDER_EXTERNAL_INFO_V1 structure defines metadata specific to files provided by WOF_PROVIDER_FILE. |
| [FILE_QUOTA_INFORMATION structure](ns-ntifs--file-quota-information.md) | The FILE_QUOTA_INFORMATION structure is used to query or set per-user quota information for each of the files in a directory. |
| [FILE_RENAME_INFORMATION structure](ns-ntifs--file-rename-information.md) | The FILE_RENAME_INFORMATION structure is used to rename a file. |
| [FILE_REPARSE_POINT_INFORMATION structure](ns-ntifs--file-reparse-point-information.md) | The FILE_REPARSE_POINT_INFORMATION structure is used to query for information about a reparse point. |
| [FILE_STREAM_INFORMATION structure](ns-ntifs--file-stream-information.md) | The FILE_STREAM_INFORMATION structure is used to enumerate the streams for a file. |
| [FILE_TIMESTAMPS structure](ns-ntifs--file-timestamps.md) | The FILE_TIMESTAMPS structure specifies the last recorded instance of specific actions on a file. |
| [FILE_ZERO_DATA_INFORMATION structure](ns-ntifs--file-zero-data-information.md) | Contains a range of a file to set to zeros. |
| [FILE_ZERO_DATA_INFORMATION_EX structure](ns-ntifs--file-zero-data-information-ex.md) | Contains a range of a file to set to zeros. |
| [FSCTL_OFFLOAD_READ_INPUT structure](ns-ntifs--fsctl-offload-read-input.md) | The FSCTL_OFFLOAD_READ_INPUT structure contains the input for the FSCTL_OFFLOAD_READ control code request. |
| [FSCTL_OFFLOAD_READ_OUTPUT structure](ns-ntifs--fsctl-offload-read-output.md) | The FSCTL_OFFLOAD_READ_OUTPUT structure contains the output for the FSCTL_OFFLOAD_READ control code request. |
| [FSCTL_OFFLOAD_WRITE_INPUT structure](ns-ntifs--fsctl-offload-write-input.md) | The FSCTL_OFFLOAD_WRITE_INPUT structure contains the input for the FSCTL_OFFLOAD_WRITE control code request. |
| [FSCTL_OFFLOAD_WRITE_OUTPUT structure](ns-ntifs--fsctl-offload-write-output.md) | The FSCTL_OFFLOAD_WRITE_OUTPUT structure contains the output for the FSCTL_OFFLOAD_WRITE control code request. |
| [FSCTL_QUERY_VOLUME_NUMA_INFO_OUTPUT structure](ns-ntifs--fsctl-query-volume-numa-info-output.md) | The FSCTL_QUERY_VOLUME_NUMA_INFO_OUTPUT structure specifies the Non-Uniform Memory Architecture (NUMA) node the volume resides on. |
| [FSRTL_ADVANCED_FCB_HEADER structure](ns-ntifs--fsrtl-advanced-fcb-header.md) | The FSRTL_ADVANCED_FCB_HEADER structure contains context information that a file system maintains about a file. |
| [FSRTL_COMMON_FCB_HEADER structure](ns-ntifs--fsrtl-common-fcb-header.md) | Do not use the FSRTL_COMMON_FCB_HEADER structure outside of the FSRTL_ADVANCED_FCB_HEADER structure. |
| [FSRTL_PER_FILEOBJECT_CONTEXT structure](ns-ntifs--fsrtl-per-fileobject-context.md) | The opaque FSRTL_PER_FILEOBJECT_CONTEXT structure is used by the operating system to track file system filter-driver-defined context information structures for a file object. |
| [FSRTL_PER_FILE_CONTEXT structure](ns-ntifs--fsrtl-per-file-context.md) | A legacy file system filter driver can use a FSRTL_PER_FILE_CONTEXT structure to associate driver-specific context information to an open file. |
| [FSRTL_PER_STREAM_CONTEXT structure](ns-ntifs--fsrtl-per-stream-context.md) | The FSRTL_PER_STREAM_CONTEXT structure contains context information that a file system filter driver maintains about a file stream. |
| [FS_FILTER_SECTION_SYNC_OUTPUT structure](ns-ntifs--fs-filter-section-sync-output.md) | The FS_FILTER_SECTION_SYNC_OUTPUT structure contains information describing the attributes of the section that is being created. |
| [IO_PRIORITY_INFO structure](ns-ntifs--io-priority-info.md) | The IO_PRIORITY_INFO structure is used to hold thread priority information. |
| [IRP structure](ns-ntifs--irp.md) | The IRP structure is a partially opaque structure that represents an I/O request packet. Drivers can use the following members of the IRP structure. |
| [MEMORY_BASIC_INFORMATION structure](ns-ntifs--memory-basic-information.md) | Contains information about a range of pages in the virtual address space of a process. |
| [NETWORK_APP_INSTANCE_ECP_CONTEXT structure](ns-ntifs--network-app-instance-ecp-context.md) | The NETWORK_APP_INSTANCE_ECP_CONTEXT structure is an Extra Create Parameter (ECP) and contains an application instance identifier to associate with a file. |
| [NETWORK_OPEN_ECP_CONTEXT structure](ns-ntifs--network-open-ecp-context.md) | The NETWORK_OPEN_ECP_CONTEXT structure is used to interpret network ECP contexts on files. |
| [NETWORK_OPEN_ECP_CONTEXT structure](ns-ntifs--network-open-ecp-context~r1.md) | The NETWORK_OPEN_ECP_CONTEXT structure is used to interpret network ECP contexts on files. |
| [NETWORK_OPEN_ECP_CONTEXT_V0 structure](ns-ntifs--network-open-ecp-context-v0.md) | The NETWORK_OPEN_ECP_CONTEXT_V0 structure is used to interpret network ECP contexts on files. |
| [NFS_OPEN_ECP_CONTEXT structure](ns-ntifs--nfs-open-ecp-context.md) | The NFS_OPEN_ECP_CONTEXT structure is used by the Network File System (NFS) server to open files in response to client requests. |
| [OPEN_REPARSE_LIST structure](ns-ntifs--open-reparse-list.md) | Points to a list of OPEN_REPARSE_LIST_ENTRY structures that specify the tag and possibly GUID that should be opened directly without returning STATUS_REPARSE. |
| [OPEN_REPARSE_LIST_ENTRY structure](ns-ntifs--open-reparse-list-entry.md) | This structure supports callers opening specific reparse points without inhibiting reparse behavior for all classes of reparse points. |
| [PMARK_HANDLE_INFO32 structure](ns-ntifs-pmark-handle-info32.md) | Contains information that is used to mark a specified file or directory, and its update sequence number (USN) change journal record with data about changes. |
| [PREFETCH_OPEN_ECP_CONTEXT structure](ns-ntifs--prefetch-open-ecp-context.md) | The PREFETCH_OPEN_ECP_CONTEXT structure communicates whether the prefetcher performs a given open request on a file. |
| [PUBLIC_OBJECT_BASIC_INFORMATION structure](ns-ntifs--public-object-basic-information.md) | The PUBLIC_OBJECT_BASIC_INFORMATION structure holds a subset of the full information that is available for an object. |
| [PUBLIC_OBJECT_TYPE_INFORMATION structure](ns-ntifs---public-object-type-information.md) | The PUBLIC_OBJECT_TYPE_INFORMATION structure holds the type name of the object. |
| [QUERY_FILE_LAYOUT_INPUT structure](ns-ntifs--query-file-layout-input.md) | The QUERY_FILE_LAYOUT_INPUT structure selects which file layout entries are returned from a FSCTL_QUERY_FILE_LAYOUT request. |
| [QUERY_FILE_LAYOUT_OUTPUT structure](ns-ntifs--query-file-layout-output.md) | The QUERY_FILE_LAYOUT_OUTPUT structure serves as a header for the file layout entries that are returned from a FSCTL_QUERY_FILE_LAYOUT request. |
| [REFS_SMR_VOLUME_GC_PARAMETERS structure](ns-ntifs--refs-smr-volume-gc-parameters.md) | The REFS_SMR_VOLUME_GC_PARAMETERS structure. |
| [REFS_SMR_VOLUME_INFO_OUTPUT structure](ns-ntifs--refs-smr-volume-info-output.md) | The REFS_SMR_VOLUME_INFO_OUTPUT structure describes a Shingled Magnetic Recording (SMR) volume's current state on space and garbage collection activities. |
| [REPARSE_DATA_BUFFER structure](ns-ntifs--reparse-data-buffer.md) | The REPARSE_DATA_BUFFER structure contains reparse point data for a Microsoft reparse point. |
| [REPARSE_GUID_DATA_BUFFER structure](ns-ntifs--reparse-guid-data-buffer.md) | The REPARSE_GUID_DATA_BUFFER structure contains reparse point data for a reparse point. |
| [SECURITY_DESCRIPTOR structure](ns-ntifs--security-descriptor.md) | The SECURITY_DESCRIPTOR structure specifies the security information that is associated with an object. For more information, see the reference page for SECURITY_DESCRIPTOR in the Installable File System documentation. |
| [SET_DAX_ALLOC_ALIGNMENT_HINT_INPUT structure](ns-ntifs--set-dax-alloc-alignment-hint-input.md) | This structure is for internal use only and should not be called from your code. |
| [SE_EXPORTS structure](ns-ntifs--se-exports.md) | The SeExports structure is a large external static SE_EXPORTS structure that defines a number of well-known security constants for privilege values and security identifiers. |
| [SE_SID structure](ns-ntifs--se-sid.md) | The SE_SID union holds the maximum-sized valid Security Identifier (SID). The structure occupies 68-bytes and is suitable for stack allocation. |
| [SE_TOKEN_USER structure](ns-ntifs--se-token-user.md) | The SE_TOKEN_USER structure holds the maximum-sized valid user SID that can be returned by SeQueryInformationToken, GetTokenInformation, or ZwQueryInformationToken with the TokenUser information class. This structure is suitable for stack allocation. |
| [SID_AND_ATTRIBUTES structure](ns-ntifs--sid-and-attributes.md) | The SID_AND_ATTRIBUTES structure represents a security identifier (SID) and its attributes. SIDs are used to uniquely identify users or groups. |
| [SID_IDENTIFIER_AUTHORITY structure](ns-ntifs--sid-identifier-authority.md) | The SID_IDENTIFIER_AUTHORITY structure represents the top-level authority of a security identifier (SID). |
| [SRV_OPEN_ECP_CONTEXT structure](ns-ntifs--srv-open-ecp-context.md) | The SRV_OPEN_ECP_CONTEXT structure is used by a server to conditionally open files in response to client requests. |
| [SYSTEM_AUDIT_ACE structure](ns-ntifs--system-audit-ace.md) | The SYSTEM_AUDIT_ACE structure defines an access-control entry (ACE) for the system access-control list (ACL) specifying what types of access cause system-level notifications. |
| [SYSTEM_PROCESS_TRUST_LABEL_ACE structure](ns-ntifs--system-process-trust-label-ace.md) | Reserved. |
| [SYSTEM_RESOURCE_ATTRIBUTE_ACE structure](ns-ntifs--system-resource-attribute-ace.md) | The SYSTEM_RESOURCE_ATTRIBUTE_ACE structure defines an access-control entry (ACE) for the system access-control list (ACL) specifying what rights a particular claim has to a resource. |
| [SYSTEM_SCOPED_POLICY_ID_ACE structure](ns-ntifs--system-scoped-policy-id-ace.md) | The SYSTEM_SCOPED_POLICY_ID_ACE structure defines an access-control entry (ACE) for the system access-control list (ACL) specifying rights for a scoped policy identifer. |
| [TOKEN_CONTROL structure](ns-ntifs--token-control.md) | The TOKEN_CONTROL structure contains information that identifies an access token. |
| [TOKEN_DEFAULT_DACL structure](ns-ntifs--token-default-dacl.md) | The TOKEN_DEFAULT_DACL structure specifies a discretionary access-control list (DACL). |
| [TOKEN_GROUPS structure](ns-ntifs--token-groups.md) | TOKEN_GROUPS contains information about the group security identifiers (SID) in an access token. |
| [TOKEN_GROUPS_AND_PRIVILEGES structure](ns-ntifs--token-groups-and-privileges.md) | TOKEN_GROUPS_AND_PRIVILEGES contains information about the group security identifiers (SIDs) and privileges in an access token. |
| [TOKEN_ORIGIN structure](ns-ntifs--token-origin.md) | The TOKEN_ORIGIN structure contains information about the origin of the logon session. |
| [TOKEN_OWNER structure](ns-ntifs--token-owner.md) | TOKEN_OWNER contains the default owner security identifier (SID) that will be applied to newly created objects. |
| [TOKEN_PRIMARY_GROUP structure](ns-ntifs--token-primary-group.md) | TOKEN_PRIMARY_GROUP specifies a group security identifier (SID) for an access token. |
| [TOKEN_PRIVILEGES structure](ns-ntifs--token-privileges.md) | TOKEN_PRIVILEGES contains information about a set of privileges for an access token. |
| [TOKEN_SOURCE structure](ns-ntifs--token-source.md) | TOKEN_SOURCE identifies the source of an access token. |
| [TOKEN_STATISTICS structure](ns-ntifs--token-statistics.md) | TOKEN_STATISTICS contains information about an access token. A driver can retrieve this information by calling SeQueryInformationToken or ZwQueryInformationToken. |
| [TOKEN_USER structure](ns-ntifs--token-user.md) | TOKEN_USER identifies the user associated with an access token. |
| [WIM_PROVIDER_ADD_OVERLAY_INPUT structure](ns-ntifs--wim-provider-add-overlay-input.md) | A new Windows Image File (WIM) data source is added to the WIM provider with the WIM_PROVIDER_ADD_OVERLAY_INPUT structure. |
| [WIM_PROVIDER_EXTERNAL_INFO structure](ns-ntifs--wim-provider-external-info.md) | The WIM_PROVIDER_EXTERNAL_INFO structure holds the identifier and status information for the Windows Image File (WIM) external backing provider. |
| [WIM_PROVIDER_OVERLAY_ENTRY structure](ns-ntifs--wim-provider-overlay-entry.md) | Contains the a Windows Image Format (WIM) file configuration information for a data source entry. It is used to identify specific WIM file names and indices that supply data to externally backed files on a volume. |
| [WIM_PROVIDER_REMOVE_OVERLAY_INPUT structure](ns-ntifs--wim-provider-remove-overlay-input.md) | A Windows Image File (WIM) data source to remove from the WIM provider is specified in the WIM_PROVIDER_REMOVE_OVERLAY_INPUT structure. |
| [WIM_PROVIDER_SUSPEND_OVERLAY_INPUT structure](ns-ntifs--wim-provider-suspend-overlay-input.md) | A Windows Image File (WIM) data source to suspend from the WIM provider is specified in the WIM_PROVIDER_SUSPEND_OVERLAY_INPUT structure. |
| [WIM_PROVIDER_UPDATE_OVERLAY_INPUT structure](ns-ntifs--wim-provider-update-overlay-input.md) | A current Windows Image File (WIM) data source is updated with a new WIM file using the FSCTL_UPDATE_OVERLAY control request with a WIM_PROVIDER_UPDATE_OVERLAY_INPUT structure. |
| [WOF_EXTERNAL_FILE_ID structure](ns-ntifs--wof-external-file-id.md) | The WOF_EXTERNAL_FILE_ID structure contains a file ID that is used to open a handle to a mini-filter or driver. |
| [WOF_EXTERNAL_INFO structure](ns-ntifs--wof-external-info.md) | The WOF_EXTERNAL_INFO structure identifies a file backing provider and the overlay service version it supports. |
| [WOF_VERSION_INFO structure](ns-ntifs--wof-version-info.md) | The WOF_VERSION_INFO structure contains the version corresponding to the driver supporting a given provider. |
| [sockaddr_storage structure](ns-ntifs-sockaddr-storage.md) | The SOCKADDR_STORAGE structure is a generic structure that specifies a transport address. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_REDIR_QUERY_PATH IOCTL](ni-ntifs-ioctl-redir-query-path.md) | The IOCTL_REDIR_QUERY_PATH control code is sent by the multiple UNC provider (MUP) to network redirectors to determine which provider can handle a specific UNC path in a name-based operation, typically an IRP_MJ_CREATE request. |
| [IOCTL_REDIR_QUERY_PATH_EX IOCTL](ni-ntifs-ioctl-redir-query-path-ex.md) | The IOCTL_REDIR_QUERY_PATH_EX control code is sent by the multiple UNC provider (MUP) on Windows Vista or later to network redirectors to determine which provider can handle a specific UNC path in a name-based operation, typically an IRP_MJ_CREATE request. |
| [IOCTL_VOLSNAP_FLUSH_AND_HOLD_WRITES IOCTL](ni-ntifs-ioctl-volsnap-flush-and-hold-writes.md) | The IOCTL_VOLSNAP_FLUSH_AND_HOLD_WRITES control code is sent to force a flush of a file system before a volume shadow copy occurs. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [FSRTL_CHANGE_BACKING_TYPE enumeration](ne-ntifs--fsrtl-change-backing-type.md) | The FSRTL_CHANGE_BACKING_TYPE enumeration specifies the type of cache or control area that a file object designates. |
| [MEMORY_INFORMATION_CLASS enumeration](ne-ntifs--memory-information-class.md) | Defines classes of memory information that can be retrieved by using the ZwQueryVirtualMemory function. |
| [NETWORK_OPEN_INTEGRITY_QUALIFIER enumeration](ne-ntifs-network-open-integrity-qualifier.md) | The NETWORK_OPEN_INTEGRITY_QUALIFIER enumeration type contains values that identify the kind of integrity restriction to attach to a file. |
| [NETWORK_OPEN_LOCATION_QUALIFIER enumeration](ne-ntifs-network-open-location-qualifier.md) | The NETWORK_OPEN_LOCATION_QUALIFIER enumeration type contains values that identify the kind of location restriction to attach to a file. |
| [OBJECT_INFORMATION_CLASS enumeration](ne-ntifs--object-information-class.md) | The OBJECT_INFORMATION_CLASS enumeration type represents the type of information to supply about an object. |
| [REFS_SMR_VOLUME_GC_ACTION enumeration](ne-ntifs--refs-smr-volume-gc-action.md) | The REFS_SMR_VOLUME_GC_ACTION enum contains the available garbage collection commands for FSCTL_SET_REFS_SMR_VOLUME_GC_PARAMETERS. |
| [REFS_SMR_VOLUME_GC_METHOD enumeration](ne-ntifs--refs-smr-volume-gc-method.md) | The REFS_SMR_VOLUME_GC_METHOD enum specifies the garbage collection method or strategy for FSCTL_SET_REFS_SMR_VOLUME_GC_PARAMETERS. |
| [REFS_SMR_VOLUME_GC_STATE enumeration](ne-ntifs--refs-smr-volume-gc-state.md) | The REFS_SMR_VOLUME_GC_STATE enum specifies the garbage collection's current state. |
| [SID_NAME_USE enumeration](ne-ntifs--sid-name-use.md) | The SID_NAME_USE enumeration type contains values that specify the type of a security identifier (SID). |
| [TOKEN_INFORMATION_CLASS enumeration](ne-ntifs--token-information-class.md) | The TOKEN_INFORMATION_CLASS enumeration type contains values that specify the type of information being assigned to or retrieved from an access token. |
| [TOKEN_TYPE enumeration](ne-ntifs--token-type.md) | The TOKEN_TYPE enumeration type contains values that differentiate between a primary token and an impersonation token. |
