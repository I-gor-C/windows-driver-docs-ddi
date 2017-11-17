# Declarations in the ntifs header
This header Ntifs contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [IoIrpHasFsTrackOffsetExtensionType function](nf-ntifs-ioirphasfstrackoffsetextensiontype.md) | TBD |
| [RtlSecondsSince1970ToTime function](nf-ntifs-rtlsecondssince1970totime.md) | The RtlSecondsSince1970ToTime routine converts the elapsed time, in seconds, since the beginning of 1970 to an absolute system time value. |
| [RtlSubAuthorityCountSid function](nf-ntifs-rtlsubauthoritycountsid.md) | TBD |
| [MmSetAddressRangeModified function](nf-ntifs-mmsetaddressrangemodified.md) | The MmSetAddressRangeModified routine marks currently valid pages in the specified range of the system cache as modified. |
| [ZwDuplicateObject function](nf-ntifs-zwduplicateobject.md) | The ZwDuplicateObject routine creates a handle that is a duplicate of the specified source handle. |
| [CcSetParallelFlushFile function](nf-ntifs-ccsetparallelflushfile.md) | TBD |
| [FsRtlAreThereCurrentFileLocks function](nf-ntifs-fsrtlaretherecurrentfilelocks.md) | The FsRtlAreThereCurrentFileLocks macro checks whether any byte range locks exist for the specified file. |
| [IoStartPacket function](nf-ntifs-iostartpacket.md) | The IoStartPacket routine calls the driver's StartIo routine with the given IRP or inserts the IRP into the device queue associated with the given device object if the device is already busy. |
| [SeAuditingHardLinkEvents function](nf-ntifs-seauditinghardlinkevents.md) | TBD |
| [SspiGetAsyncCallStatus function](nf-ntifs-sspigetasynccallstatus.md) | TBD |
| [SeDeleteObjectAuditAlarmWithTransaction function](nf-ntifs-sedeleteobjectauditalarmwithtransaction.md) | TBD |
| [RtlRemoveUnicodePrefix function](nf-ntifs-rtlremoveunicodeprefix.md) | The RtlRemoveUnicodePrefix routine removes an element from a prefix table. |
| [SeOpenObjectAuditAlarmWithTransaction function](nf-ntifs-seopenobjectauditalarmwithtransaction.md) | TBD |
| [PsRevertToSelf function](nf-ntifs-psreverttoself.md) | The PsRevertToSelf routine ends the calling thread's impersonation of a client. |
| [NtAccessCheckByTypeAndAuditAlarm function](nf-ntifs-ntaccesscheckbytypeandauditalarm.md) | TBD |
| [FsRtlIsEcpAcknowledged function](nf-ntifs-fsrtlisecpacknowledged.md) | The FsRtlIsEcpAcknowledged routine is used to determine if a given extra create parameter (ECP) context structure has been marked as acknowledged. |
| [RtlDecompressBuffer function](nf-ntifs-rtldecompressbuffer.md) | The RtlDecompressBuffer function decompresses an entire compressed buffer. |
| [PsDisableImpersonation function](nf-ntifs-psdisableimpersonation.md) | TBD |
| [MmGetMaximumFileSectionSize function](nf-ntifs-mmgetmaximumfilesectionsize.md) | The MmGetMaximumFileSectionSize returns the maximum possible size of a file section for the current version of Windows. |
| [KeUnstackDetachProcess function](nf-ntifs-keunstackdetachprocess.md) | The KeUnstackDetachProcess routine detaches the current thread from the address space of a process and restores the previous attach state. |
| [FsRtlRemoveExtraCreateParameter function](nf-ntifs-fsrtlremoveextracreateparameter.md) | The FsRtlRemoveExtraCreateParameter routine searches an ECP list for an ECP context structure and, if found, detaches it from the ECP list. |
| [RtlDescribeChunk function](nf-ntifs-rtldescribechunk.md) | TBD |
| [FsRtlQueryMaximumVirtualDiskNestingLevel function](nf-ntifs-fsrtlquerymaximumvirtualdisknestinglevel.md) | TBD |
| [FsRtlValidateReparsePointBuffer function](nf-ntifs-fsrtlvalidatereparsepointbuffer.md) | The FsRtlValidateReparsePointBuffer routine verifies that the specified reparse point buffer is valid. |
| [FsRtlIncrementCcFastReadResourceMiss function](nf-ntifs-fsrtlincrementccfastreadresourcemiss.md) | The FsRtlIncrementCcFastReadResourceMiss routine increments the CcFastReadNotPossible performance counter in a per processor control block of cache manager system counters. |
| [FsRtlInitializeExtraCreateParameter function](nf-ntifs-fsrtlinitializeextracreateparameter.md) | The FsRtlInitializeExtraCreateParameter routine initializes an extra create parameter (ECP) context structure. |
| [PoDeletePowerRequest function](nf-ntifs-podeletepowerrequest.md) | The PoDeletePowerRequest routine deletes a power request object. |
| [CcSetAdditionalCacheAttributesEx function](nf-ntifs-ccsetadditionalcacheattributesex.md) | Call the CcSetAdditionalCacheAttributesEx routine to enable extended cache behavior on a cached file. |
| [IoGetBaseFileSystemDeviceObject function](nf-ntifs-iogetbasefilesystemdeviceobject.md) | TBD |
| [NtReadFile function](nf-ntifs-ntreadfile.md) | TBD |
| [SeRegisterLogonSessionTerminatedRoutineEx function](nf-ntifs-seregisterlogonsessionterminatedroutineex.md) | TBD |
| [SeAdjustAccessStateForAccessConstraints function](nf-ntifs-seadjustaccessstateforaccessconstraints.md) | TBD |
| [DeleteSecurityContext function](nf-ntifs-deletesecuritycontext.md) | TBD |
| [IoSetTopLevelIrp function](nf-ntifs-iosettoplevelirp.md) | The IoSetTopLevelIrp routine sets the value of the TopLevelIrp field of the current thread. |
| [CcFastCopyRead function](nf-ntifs-ccfastcopyread.md) | The CcFastCopyRead routine performs a fast copy read from a cached file to a buffer in memory. |
| [SspiDeleteSecurityContextAsync function](nf-ntifs-sspideletesecuritycontextasync.md) | TBD |
| [RtlAllocateHeap function](nf-ntifs-rtlallocateheap.md) | The RtlAllocateHeap routine allocates a block of memory from a heap. |
| [FsRtlInsertExtraCreateParameter function](nf-ntifs-fsrtlinsertextracreateparameter.md) | The FsRtlInsertExtraCreateParameter routine inserts an extra create parameter (ECP) context structure into an ECP list. |
| [CcScheduleReadAhead function](nf-ntifs-ccschedulereadahead.md) | The CcScheduleReadAhead routine performs read-ahead (also called &#0034;lazy read&#0034;) on a cached file. CcScheduleReadAhead should never be called directly. The CcReadAhead macro should be called instead. |
| [SeImpersonateClient function](nf-ntifs-seimpersonateclient.md) | TBD |
| [FsRtlGetEcpListFromIrp function](nf-ntifs-fsrtlgetecplistfromirp.md) | The FsRtlGetEcpListFromIrp routine returns a pointer to an extra create parameter (ECP) context structure list that is associated with a given IRP_MJ_CREATE operation. |
| [PsChargePoolQuota function](nf-ntifs-pschargepoolquota.md) | The PsChargePoolQuota routine charges pool quota of the specified pool type to the specified process. |
| [SePrivilegeCheck function](nf-ntifs-seprivilegecheck.md) | The SePrivilegeCheck routine determines whether a specified set of privileges is enabled in the subject's access token. |
| [RtlGetSaclSecurityDescriptor function](nf-ntifs-rtlgetsaclsecuritydescriptor.md) | The RtlGetSaclSecurityDescriptor routine returns a pointer to the system ACL (SACL) for a security descriptor. |
| [PsImpersonateClient function](nf-ntifs-psimpersonateclient.md) | The PsImpersonateClient routine causes a server thread to impersonate a client. |
| [FsRtlTeardownPerStreamContexts function](nf-ntifs-fsrtlteardownperstreamcontexts.md) | The FsRtlTeardownPerStreamContexts routine frees all per-stream context structures associated with a given FSRTL_ADVANCED_FCB_HEADER structure. |
| [SeAccessCheckFromState function](nf-ntifs-seaccesscheckfromstate.md) | TBD |
| [IoGetDeviceAttachmentBaseRef function](nf-ntifs-iogetdeviceattachmentbaseref.md) | The IoGetDeviceAttachmentBaseRef routine returns a pointer to the lowest-level device object in a file system or device driver stack. |
| [SspiEncodeStringsAsAuthIdentity function](nf-ntifs-sspiencodestringsasauthidentity.md) | TBD |
| [RtlGetOwnerSecurityDescriptor function](nf-ntifs-rtlgetownersecuritydescriptor.md) | The RtlGetOwnerSecurityDescriptor routine returns the owner information for a given security descriptor. |
| [IoIsSystemThread function](nf-ntifs-ioissystemthread.md) | The IoIsSystemThread routine checks whether a given thread is a system thread. |
| [CcFlushCache function](nf-ntifs-ccflushcache.md) | The CcFlushCache routine flushes all or a portion of a cached file to disk. |
| [IsReparseTagValid function](nf-ntifs-isreparsetagvalid.md) | TBD |
| [IoGetFsTrackOffsetState function](nf-ntifs-iogetfstrackoffsetstate.md) | TBD |
| [PfxInsertPrefix function](nf-ntifs-pfxinsertprefix.md) | TBD |
| [FsRtlInitExtraCreateParameterLookasideList function](nf-ntifs-fsrtlinitextracreateparameterlookasidelist.md) | The FsRtlInitExtraCreateParameterLookasideList routine initializes a paged or nonpaged pool lookaside list used for the allocation of one or more extra create parameter context structures (ECPs) of fixed size. |
| [KeGetProcessorIndexFromNumber function](nf-ntifs-kegetprocessorindexfromnumber.md) | The KeGetProcessorIndexFromNumber routine converts a group number and a group-relative processor number to a systemwide processor index. |
| [CcGetFileObjectFromSectionPtrsRef function](nf-ntifs-ccgetfileobjectfromsectionptrsref.md) | When passed a pointer to a SECTION_OBJECT_POINTERS structure for a cached file, the CcGetFileObjectFromSectionPtrsRef routine returns a pointer to the file object that the cache manager is using for the cached file. |
| [NtPrivilegeObjectAuditAlarm function](nf-ntifs-ntprivilegeobjectauditalarm.md) | TBD |
| [NtQueryObject function](nf-ntifs-ntqueryobject.md) | TBD |
| [SeAuditingFileEventsWithContextEx function](nf-ntifs-seauditingfileeventswithcontextex.md) | TBD |
| [ZwQuerySecurityObject function](nf-ntifs-zwquerysecurityobject.md) | The ZwQuerySecurityObject routine retrieves a copy of an object's security descriptor. |
| [KeStackAttachProcess function](nf-ntifs-kestackattachprocess.md) | The KeStackAttachProcess routine attaches the current thread to the address space of the target process. |
| [PsLookupProcessByProcessId function](nf-ntifs-pslookupprocessbyprocessid.md) | The PsLookupProcessByProcessId routine accepts the process ID of a process and returns a referenced pointer to EPROCESS structure of the process. |
| [NtQueryDirectoryFile function](nf-ntifs-ntquerydirectoryfile.md) | TBD |
| [CcRepinBcb function](nf-ntifs-ccrepinbcb.md) | The CcRepinBcb routine pins a buffer control block (BCB) an additional time to prevent it from being freed by a subsequent call to CcUnpinData. |
| [RtlIdnToAscii function](nf-ntifs-rtlidntoascii.md) | TBD |
| [FsRtlIsEcpFromUserMode function](nf-ntifs-fsrtlisecpfromusermode.md) | The FsRtlIsEcpFromUserMode routine determines whether an extra create parameter (ECP) context structure originated from user mode. |
| [IoGetTopLevelIrp function](nf-ntifs-iogettoplevelirp.md) | The IoGetTopLevelIrp routine returns the value of the TopLevelIrp field of the current thread. |
| [SeSetSessionIdToken function](nf-ntifs-sesetsessionidtoken.md) | TBD |
| [SeReportSecurityEventWithSubCategory function](nf-ntifs-sereportsecurityeventwithsubcategory.md) | TBD |
| [IoSetFsZeroingOffsetRequired function](nf-ntifs-iosetfszeroingoffsetrequired~r1.md) | TBD |
| [RtlValidateUnicodeString function](nf-ntifs-rtlvalidateunicodestring.md) | TBD |
| [CcIsThereDirtyData function](nf-ntifs-ccistheredirtydata.md) | The CcIsThereDirtyData routine determines whether a mounted volume contains any files that have dirty data in the system cache. |
| [PsGetThreadProcess function](nf-ntifs-psgetthreadprocess.md) | TBD |
| [RtlLengthSid function](nf-ntifs-rtllengthsid.md) | The RtlLengthSid routine returns the length, in bytes, of a valid security identifier (SID). |
| [FsRtlSetKernelEaFile function](nf-ntifs-fsrtlsetkerneleafile.md) | The routine FsRtlQueryKernelEaFile is used to set, modify and/or delete extended attribute (EA) values for a file and synchronously wait for it to complete, returning a result. |
| [SspiAcquireCredentialsHandleAsyncW function](nf-ntifs-sspiacquirecredentialshandleasyncw.md) | TBD |
| [ZwQueryDirectoryFileEx function](nf-ntifs-zwquerydirectoryfileex.md) | The ZwQueryDirectoryFileEx routine returns information about files in the directory specified by the FileHandle parameter. |
| [SspiExcludePackage function](nf-ntifs-sspiexcludepackage.md) | TBD |
| [CcSetAdditionalCacheAttributes function](nf-ntifs-ccsetadditionalcacheattributes.md) | Call the CcSetAdditionalCacheAttributes routine to enable or disable read-ahead (also called &#0034;lazy read&#0034;) or write-behind (also called &#0034;lazy write&#0034;) on a cached file. |
| [IsVirtualDiskFileShared function](nf-ntifs-isvirtualdiskfileshared.md) | TBD |
| [SeAuditingFileOrGlobalEvents function](nf-ntifs-seauditingfileorglobalevents.md) | The SeAuditingFileOrGlobalEvents routine determines whether file or global events are currently being audited. |
| [FsRtlDecrementLockRequestsInProgress function](nf-ntifs-fsrtldecrementlockrequestsinprogress.md) | TBD |
| [SeTokenGetNoChildProcessRestricted function](nf-ntifs-setokengetnochildprocessrestricted.md) | The SeTokenGetNoChildProcessRestricted routine determines the state of the no child process mitigation. It is not possible to be enforced and audit-only at the same time. |
| [RtlLengthRequiredSid function](nf-ntifs-rtllengthrequiredsid.md) | The RtlLengthRequiredSid routine returns the length, in bytes, of the buffer required to store a security identifier (SID) with a specified number of subauthorities. |
| [FlagOn function](nf-ntifs-flagon.md) | TBD |
| [QUERY_TYPE_ULONG function](nf-ntifs-query-type-ulong.md) | TBD |
| [CcMapData function](nf-ntifs-ccmapdata.md) | The CcMapData routine maps a specified byte range of a cached file to a buffer in memory. |
| [SeMarkLogonSessionForTerminationNotificationEx function](nf-ntifs-semarklogonsessionforterminationnotificationex.md) | TBD |
| [RtlCompressBuffer function](nf-ntifs-rtlcompressbuffer.md) | The RtlCompressBuffer function compresses a buffer and can be used by a file system driver to facilitate the implementation of file compression. |
| [SeExamineGlobalSacl function](nf-ntifs-seexamineglobalsacl.md) | TBD |
| [IoApplyPriorityInfoThread function](nf-ntifs-ioapplypriorityinfothread.md) | TBD |
| [PoStartNextPowerIrp function](nf-ntifs-postartnextpowerirp.md) | The PoStartNextPowerIrp routine signals the power manager that the driver is ready to handle the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only.). |
| [SetFlag function](nf-ntifs-setflag.md) | TBD |
| [IoGetDiskDeviceObject function](nf-ntifs-iogetdiskdeviceobject.md) | The IoGetDiskDeviceObject routine retrieves a pointer to the disk device object associated with a given file system volume device object. |
| [CcSetFileSizes function](nf-ntifs-ccsetfilesizes.md) | The CcSetFileSizes routine updates the cache maps and section object for a cached file whose size has changed. |
| [HEAP_MAKE_TAG_FLAGS function](nf-ntifs-heap-make-tag-flags.md) | TBD |
| [CcCoherencyFlushAndPurgeCache function](nf-ntifs-cccoherencyflushandpurgecache.md) | The CcCoherencyFlushAndPurgeCache routine flushes and/or purges the cache to ensure cache coherency. |
| [FsRtlIsAnsiCharacterLegal function](nf-ntifs-fsrtlisansicharacterlegal.md) | The FsRtlIsAnsiCharacterLegal macro determines whether a character is a legal ANSI character. |
| [QueryContextAttributesExW function](nf-ntifs-querycontextattributesexw.md) | TBD |
| [SspiCopyAuthIdentity function](nf-ntifs-sspicopyauthidentity.md) | TBD |
| [RtlIsNonEmptyDirectoryReparsePointAllowed function](nf-ntifs-rtlisnonemptydirectoryreparsepointallowed.md) | TBD |
| [NtAccessCheckByTypeResultListAndAuditAlarm function](nf-ntifs-ntaccesscheckbytyperesultlistandauditalarm.md) | TBD |
| [FsRtlRemovePerStreamContext function](nf-ntifs-fsrtlremoveperstreamcontext.md) | FsRtlRemovePerStreamContext removes a per-stream context structure from the list of per-stream contexts associated with a file stream. |
| [CcUninitializeCacheMap function](nf-ntifs-ccuninitializecachemap.md) | The CcUninitializeCacheMap routine stops the caching of a cached file. |
| [RtlDecompressBufferEx function](nf-ntifs-rtldecompressbufferex.md) | The RtlDecompressBufferEx function decompresses an entire compressed buffer. |
| [PoRegisterSystemState function](nf-ntifs-poregistersystemstate.md) | The PoRegisterSystemState routine registers the system as busy due to certain activity. |
| [FsRtlAllocateExtraCreateParameterList function](nf-ntifs-fsrtlallocateextracreateparameterlist.md) | The FsRtlAllocateExtraCreateParameterList routine allocates paged pool memory for an ECP_LIST structure and generates a pointer to that structure. |
| [CcInitializeCacheMapEx function](nf-ntifs-ccinitializecachemapex.md) | TBD |
| [InterlockedPushListSList function](nf-ntifs-interlockedpushlistslist.md) | TBD |
| [FsRtlIncrementCcFastReadWait function](nf-ntifs-fsrtlincrementccfastreadwait.md) | The FsRtlIncrementCcFastReadWait routine increments the CcFastReadWait performance counter in a per processor control block of cache manager system counters. |
| [RtlIsNameLegalDOS8Dot3 function](nf-ntifs-rtlisnamelegaldos8dot3.md) | The RtlIsNameLegalDOS8Dot3 routine determines whether a given name represents a valid short (8.3) file name. |
| [FsRtlKernelFsControlFile function](nf-ntifs-fsrtlkernelfscontrolfile.md) | TBD |
| [PsReferencePrimaryToken function](nf-ntifs-psreferenceprimarytoken.md) | The PsReferencePrimaryToken routine increments the reference count of the primary token for the specified process. |
| [SeFreePrivileges function](nf-ntifs-sefreeprivileges.md) | The SeFreePrivileges routine frees a privilege set returned by SeAccessCheck. |
| [FsRtlSetupAdvancedHeader function](nf-ntifs-fsrtlsetupadvancedheader.md) | The FsRtlSetupAdvancedHeader macro is used by file systems to initialize an FSRTL_ADVANCED_FCB_HEADER structure for use with filter contexts. |
| [CcCopyWrite function](nf-ntifs-cccopywrite.md) | The CcCopyWrite routine copies data from a user buffer to a cached file. |
| [NtImpersonateAnonymousToken function](nf-ntifs-ntimpersonateanonymoustoken.md) | TBD |
| [NtClose function](nf-ntifs-ntclose.md) | TBD |
| [PsDereferencePrimaryToken function](nf-ntifs-psdereferenceprimarytoken.md) | The PsDereferencePrimaryToken routine decrements the reference count of a primary token. |
| [NtOpenObjectAuditAlarm function](nf-ntifs-ntopenobjectauditalarm.md) | TBD |
| [CcSetLogHandleForFile function](nf-ntifs-ccsetloghandleforfile.md) | The CcSetLogHandleForFile routine sets a log handle for a file. |
| [PsGetCurrentThread function](nf-ntifs-psgetcurrentthread.md) | The PsGetCurrentThread routine identifies the current thread. |
| [RtlNormalizeString function](nf-ntifs-rtlnormalizestring.md) | TBD |
| [AddCredentialsW function](nf-ntifs-addcredentialsw.md) | TBD |
| [SeQueryInformationToken function](nf-ntifs-sequeryinformationtoken.md) | The SeQueryInformationToken routine retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information. |
| [IoQueryVolumeInformation function](nf-ntifs-ioqueryvolumeinformation.md) | TBD |
| [IoQueryFileDosDeviceName function](nf-ntifs-ioqueryfiledosdevicename.md) | The IoQueryFileDosDeviceName routine retrieves an MS-DOS device name for a file. |
| [RtlGenerate8dot3Name function](nf-ntifs-rtlgenerate8dot3name.md) | The RtlGenerate8dot3Name routine generates a short (8.3) name for the specified long file name. |
| [IoWriteErrorLogEntry function](nf-ntifs-iowriteerrorlogentry.md) | The IoWriteErrorLogEntry routine queues a given error log packet to the system error logging thread. |
| [RtlGetGroupSecurityDescriptor function](nf-ntifs-rtlgetgroupsecuritydescriptor.md) | The RtlGetGroupSecurityDescriptor routine returns the primary group information for a given security descriptor. |
| [FsRtlNotifyStreamFileObject function](nf-ntifs-fsrtlnotifystreamfileobject.md) | TBD |
| [RtlDecompressFragment function](nf-ntifs-rtldecompressfragment.md) | The RtlDecompressFragment function is used to decompress part of a compressed buffer (that is, a buffer &#0034;fragment&#0034;). |
| [IoGetRequestorSessionId function](nf-ntifs-iogetrequestorsessionid.md) | The IoGetRequestorSessionId routine returns the session ID for the process that originally requested a given I/O operation. |
| [SeCreateClientSecurity function](nf-ntifs-secreateclientsecurity.md) | The SeCreateClientSecurity routine initializes a security client context structure with the information needed to call SeImpersonateClientEx. |
| [KeReleaseQueuedSpinLock function](nf-ntifs-kereleasequeuedspinlock.md) | TBD |
| [ImpersonateSecurityContext function](nf-ntifs-impersonatesecuritycontext.md) | TBD |
| [ClearFlag function](nf-ntifs-clearflag.md) | TBD |
| [SecLookupWellKnownSid function](nf-ntifs-seclookupwellknownsid.md) | SecLookupWellKnownSid accepts a well-known security identifier (SID) type as input and retrieves the local security identifier (SID) for this well known SID. |
| [RtlSetThreadPlaceholderCompatibilityMode function](nf-ntifs-rtlsetthreadplaceholdercompatibilitymode.md) | RtlSetThreadPlaceholderCompatibilityMode is a routine which sets the placeholder compatibility mode for the current thread. |
| [RtlCreateHeap function](nf-ntifs-rtlcreateheap.md) | The RtlCreateHeap routine creates a heap object that can be used by the calling process. This routine reserves space in the virtual address space of the process and allocates physical storage for a specified initial portion of this block. |
| [FsRtlTestAnsiCharacter function](nf-ntifs-fsrtltestansicharacter.md) | The FsRtlTestAnsiCharacter macro determines whether an ANSI or double-byte character set (DBCS) character meets the specified criteria. |
| [IoSynchronousPageWrite function](nf-ntifs-iosynchronouspagewrite.md) | TBD |
| [ZwDeleteFile function](nf-ntifs-zwdeletefile.md) | The ZwDeleteFile routine deletes the specified file. |
| [SeAdjustAccessStateForTrustLabel function](nf-ntifs-seadjustaccessstatefortrustlabel.md) | TBD |
| [RtlFreeHeap function](nf-ntifs-rtlfreeheap~r1.md) | The RtlFreeHeap routine frees a memory block that was allocated from a heap by RtlAllocateHeap. |
| [IoGetAttachedDevice function](nf-ntifs-iogetattacheddevice.md) | The IoGetAttachedDevice routine returns a pointer to the highest-level device object associated with the specified device. |
| [NtSetInformationVirtualMemory function](nf-ntifs-ntsetinformationvirtualmemory.md) | TBD |
| [PsIsDiskCountersEnabled function](nf-ntifs-psisdiskcountersenabled.md) | The enabled state of the per process disk I/O counters is returned by the PsIsDiskCountersEnabled routine. |
| [IoSetFsZeroingOffsetRequired function](nf-ntifs-iosetfszeroingoffsetrequired.md) | TBD |
| [RtlInitStringEx function](nf-ntifs-rtlinitstringex.md) | The RtlInitStringEx routine initializes a counted string of 8-bit characters. |
| [ZwFlushBuffersFile function](nf-ntifs-zwflushbuffersfile.md) | The ZwFlushBuffersFile routine is called by a file system filter driver to send a flush request for the specified file to the file system. |
| [RtlSetOwnerSecurityDescriptor function](nf-ntifs-rtlsetownersecuritydescriptor.md) | The RtlSetOwnerSecurityDescriptor routine sets the owner information of an absolute-format security descriptor. It replaces any owner information that is already present in the security descriptor. |
| [IsReparseTagNameSurrogate function](nf-ntifs-isreparsetagnamesurrogate.md) | The IsReparseTagNameSurrogate macro determines whether a tag's associated reparse point is a surrogate for another named entity, such as a volume mount point. |
| [PoQueueShutdownWorkItem function](nf-ntifs-poqueueshutdownworkitem.md) | TBD |
| [NtSetInformationThread function](nf-ntifs-ntsetinformationthread~r1.md) | TBD |
| [PoEndDeviceBusy function](nf-ntifs-poenddevicebusy.md) | The PoEndDeviceBusy routine marks the end of a period of time in which the device is busy. |
| [RtlIdentifierAuthoritySid function](nf-ntifs-rtlidentifierauthoritysid.md) | TBD |
| [FsRtlRemovePerFileObjectContext function](nf-ntifs-fsrtlremoveperfileobjectcontext.md) | For a &#0034;legacy&#0034; file system filter driver, the FsRtlRemovePerFileObjectContext function unlinks a per-file-object context information structure from the list of per-file-object contexts previously associated with a file object. |
| [RtlMultiByteToUnicodeN function](nf-ntifs-rtlmultibytetounicoden.md) | The RtlMultiByteToUnicodeN routine translates the specified source string into a Unicode string, using the current system ANSI code page (ACP). The source string is not necessarily from a multibyte character set. |
| [ZwSetQuotaInformationFile function](nf-ntifs-zwsetquotainformationfile.md) | The ZwSetQuotaInformationFile routine changes quota entries for the volume associated with the FileHandle parameter. All of the quota entries in the specified buffer are applied to the volume. |
| [IoCreateStreamFileObject function](nf-ntifs-iocreatestreamfileobject.md) | The IoCreateStreamFileObject routine creates a new stream file object. |
| [MmForceSectionClosed function](nf-ntifs-mmforcesectionclosed.md) | The MmForceSectionClosed routine deletes the data and image sections for a file that is no longer in use. |
| [PoSetDeviceBusy function](nf-ntifs-posetdevicebusy.md) | TBD |
| [RtlCreateAcl function](nf-ntifs-rtlcreateacl.md) | The RtlCreateAcl routine creates and initializes an access control list (ACL). |
| [RtlFindUnicodePrefix function](nf-ntifs-rtlfindunicodeprefix.md) | The RtlFindUnicodePrefix routine searches for the best match for a given Unicode file name in a prefix table. |
| [RtlCompareMemoryUlong function](nf-ntifs-rtlcomparememoryulong.md) | The RtlCompareMemoryUlong routine returns how many bytes in a block of memory match a specified pattern. |
| [ZwQueryVirtualMemory function](nf-ntifs-zwqueryvirtualmemory.md) | The ZwQueryVirtualMemory routine determines the state, protection, and type of a region of pages within the virtual address space of the subject process. |
| [LsaLogonUser function](nf-ntifs-lsalogonuser.md) | TBD |
| [RtlInitializeSidEx function](nf-ntifs-rtlinitializesidex.md) | The RtlInitializeSidEx routine initializes a pre-allocated security identifier (SID) structure. |
| [KeRundownQueue function](nf-ntifs-kerundownqueue.md) | The KeRundownQueue routine cleans up a queue object, flushing any queued entries. |
| [RtlGetAce function](nf-ntifs-rtlgetace.md) | The RtlGetAce routine obtains a pointer to an access control entry (ACE) in an access control list (ACL). |
| [CcGetFileObjectFromBcb function](nf-ntifs-ccgetfileobjectfrombcb.md) | Given a pointer to a pinned buffer control block (BCB) for a file, the CcGetFileObjectFromBcb routine returns a pointer to the file object that the cache manager is using for that file. |
| [CcGetFlushedValidData function](nf-ntifs-ccgetflushedvaliddata.md) | The CcGetFlushedValidData routine determines how much of a cached file has been flushed to disk. |
| [CcPinMappedData function](nf-ntifs-ccpinmappeddata.md) | The CcPinMappedData routine pins the specified byte range of a cached file. |
| [ZwSetSecurityObject function](nf-ntifs-zwsetsecurityobject.md) | The ZwSetSecurityObject routine sets an object's security state. |
| [ObOpenObjectByPointerWithTag function](nf-ntifs-obopenobjectbypointerwithtag.md) | TBD |
| [FsRtlFindExtraCreateParameter function](nf-ntifs-fsrtlfindextracreateparameter.md) | The FsRtlFindExtraCreateParameter routine searches a given ECP list for an ECP context structure of a given type and returns a pointer to this structure if it is found. |
| [RtlFillMemoryUlonglong function](nf-ntifs-rtlfillmemoryulonglong~r1.md) | The RtlFillMemoryUlonglong routine fills a given range of memory with one or more repetitions of a given ULONGLONG value. |
| [SeShouldCheckForAccessRightsFromParent function](nf-ntifs-seshouldcheckforaccessrightsfromparent.md) | TBD |
| [ZwOpenThreadTokenEx function](nf-ntifs-zwopenthreadtokenex.md) | The ZwOpenThreadTokenEx routine opens the access token associated with a thread. |
| [IoIsOperationSynchronous function](nf-ntifs-ioisoperationsynchronous.md) | The IoIsOperationSynchronous routine determines whether a given IRP represents a synchronous or asynchronous I/O request. |
| [SeAuditingFileEventsWithContext function](nf-ntifs-seauditingfileeventswithcontext.md) | TBD |
| [ZwSetInformationVirtualMemory function](nf-ntifs-zwsetinformationvirtualmemory.md) | TBD |
| [RtlCreateSecurityDescriptorRelative function](nf-ntifs-rtlcreatesecuritydescriptorrelative.md) | The RtlCreateSecurityDescriptorRelative routine initializes a new security descriptor in self-relative format. |
| [RtlNtStatusToDosError function](nf-ntifs-rtlntstatustodoserror.md) | The RtlNtStatusToDosError routine converts the specified NTSTATUS code to its equivalent system error code. |
| [ZwDeviceIoControlFile function](nf-ntifs-zwdeviceiocontrolfile.md) | The ZwDeviceIoControlFile routine sends a control code directly to a specified device driver, causing the corresponding driver to perform the specified operation. |
| [IoSetFsTrackOffsetState function](nf-ntifs-iosetfstrackoffsetstate.md) | TBD |
| [FsRtlSetDriverBacking function](nf-ntifs-fsrtlsetdriverbacking.md) | TBD |
| [KeTryToAcquireQueuedSpinLock function](nf-ntifs-ketrytoacquirequeuedspinlock.md) | TBD |
| [NtDuplicateToken function](nf-ntifs-ntduplicatetoken.md) | TBD |
| [IoRegisterFileSystem function](nf-ntifs-ioregisterfilesystem.md) | The IoRegisterFileSystem routine adds a file system's control device object to the global file system queue. |
| [ZwFlushBuffersFileEx function](nf-ntifs-zwflushbuffersfileex.md) | The ZwFlushBuffersFileEx routine is called by a file system filter driver to send a flush request for a given file to the file system. An optional flush operation flag can be set to control how file data is written to storage. |
| [RtlIdnToUnicode function](nf-ntifs-rtlidntounicode.md) | TBD |
| [IoFastQueryNetworkAttributes function](nf-ntifs-iofastquerynetworkattributes.md) | TBD |
| [MmIsRecursiveIoFault function](nf-ntifs-mmisrecursiveiofault.md) | The MmIsRecursiveIoFault routine determines whether the current page fault is occurring during an I/O operation. |
| [FsRtlIsSystemPagingFile function](nf-ntifs-fsrtlissystempagingfile.md) | The FsRtlIsSystemPagingFile routine determines whether a given file is currently a system paging file. |
| [SeAuditingFileEvents function](nf-ntifs-seauditingfileevents.md) | The SeAuditingFileEvents routine determines whether file open events are currently being audited. |
| [FsRtlIsLeadDbcsCharacter function](nf-ntifs-fsrtlisleaddbcscharacter.md) | The FsRtlIsLeadDbcsCharacter macro determines whether a character is a lead byte (the first byte of a character) in a double-byte character set (DBCS). |
| [RtlNtStatusToDosErrorNoTeb function](nf-ntifs-rtlntstatustodoserrornoteb.md) | Reserved for system use. |
| [ZwSetInformationToken function](nf-ntifs-zwsetinformationtoken.md) | The ZwSetInformationToken routine modifies information in a specified token. The calling process must have appropriate access rights to set the information. |
| [ExportSecurityContext function](nf-ntifs-exportsecuritycontext.md) | TBD |
| [PoRegisterPowerSettingCallback function](nf-ntifs-poregisterpowersettingcallback.md) | The PoRegisterPowerSettingCallback routine registers a power-setting callback routine to receive notifications of changes in the specified power setting. |
| [RtlUnicodeToUTF8N function](nf-ntifs-rtlunicodetoutf8n.md) | The RtlUnicodeToUTF8N routine converts a Unicode string to a UTF-8 string. |
| [FsRtlAllocatePoolWithQuotaTag function](nf-ntifs-fsrtlallocatepoolwithquotatag.md) | The FsRtlAllocatePoolWithQuotaTag routine allocates pool memory, charging quota against the current process. |
| [SspiMarshalAuthIdentity function](nf-ntifs-sspimarshalauthidentity.md) | TBD |
| [ApplyControlToken function](nf-ntifs-applycontroltoken.md) | TBD |
| [FsRtlIncrementCcFastMdlReadWait function](nf-ntifs-fsrtlincrementccfastmdlreadwait.md) | The FsRtlIncrementCcFastMdlReadWait routine increments the cache manager's CcFastMdlReadWait performance counter member in a processor control block (PRCB) object. |
| [ObOpenObjectByPointer function](nf-ntifs-obopenobjectbypointer.md) | The ObOpenObjectByPointer function opens an object referenced by a pointer and returns a handle to the object. |
| [NtQueryVolumeInformationFile function](nf-ntifs-ntqueryvolumeinformationfile.md) | TBD |
| [FsRtlIncrementCcFastReadNotPossible function](nf-ntifs-fsrtlincrementccfastreadnotpossible.md) | The FsRtlIncrementCcFastReadNotPossible routine increments the CcFastReadNotPossible performance counter in a per processor control block of cache manager system counters. |
| [CcUnpinRepinnedBcb function](nf-ntifs-ccunpinrepinnedbcb.md) | The CcUnpinRepinnedBcb routine unpins a repinned buffer control block (BCB). |
| [FreeCredentialsHandle function](nf-ntifs-freecredentialshandle.md) | TBD |
| [NtOpenProcessToken function](nf-ntifs-ntopenprocesstoken.md) | TBD |
| [IoSetInformation function](nf-ntifs-iosetinformation.md) | TBD |
| [SeAuditingAnyFileEventsWithContextEx function](nf-ntifs-seauditinganyfileeventswithcontextex.md) | TBD |
| [NtOpenProcessTokenEx function](nf-ntifs-ntopenprocesstokenex.md) | TBD |
| [FsRtlLogCcFlushError function](nf-ntifs-fsrtllogccflusherror.md) | The FsRtlLogCcFlushError routine logs a lost delayed-write error and displays a dialog box to the user. |
| [RtlCompareAltitudes function](nf-ntifs-rtlcomparealtitudes.md) | TBD |
| [RtlAbsoluteToSelfRelativeSD function](nf-ntifs-rtlabsolutetoselfrelativesd.md) | The RtlAbsoluteToSelfRelativeSD routine creates a new security descriptor in self-relative format by using a security descriptor in absolute format as a template. |
| [FsRtlDeregisterUncProvider function](nf-ntifs-fsrtlderegisteruncprovider.md) | The FsRtlDeregisterUncProvider routine deregisters a redirector that was registered as a Universal Naming Convention (UNC) provider with the multiple UNC provider (MUP). |
| [METHOD_FROM_CTL_CODE function](nf-ntifs-method-from-ctl-code.md) | TBD |
| [ZwAllocateVirtualMemory function](nf-ntifs-zwallocatevirtualmemory.md) | The ZwAllocateVirtualMemory routine reserves, commits, or both, a region of pages within the user-mode virtual address space of a specified process. |
| [RtlIsSandboxedToken function](nf-ntifs-rtlissandboxedtoken.md) | TBD |
| [IoQueryFileInformation function](nf-ntifs-ioqueryfileinformation.md) | TBD |
| [PsReferenceImpersonationToken function](nf-ntifs-psreferenceimpersonationtoken.md) | The PsReferenceImpersonationToken routine increments the reference count of the impersonation token for the specified thread. |
| [RtlOemStringToCountedUnicodeString function](nf-ntifs-rtloemstringtocountedunicodestring.md) | The RtlOemStringToCountedUnicodeString routine translates the specified source string into a Unicode string using the current system OEM code page. |
| [IoGetRequestorProcessId function](nf-ntifs-iogetrequestorprocessid.md) | The IoGetRequestorProcessId routine returns the unique 32-bit process ID for the thread that originally requested a given I/O operation. |
| [RtlOemStringToUnicodeString function](nf-ntifs-rtloemstringtounicodestring.md) | The RtlOemStringToUnicodeString routine translates a given source string into a null-terminated Unicode string using the current system OEM code page. |
| [RtlDeleteAce function](nf-ntifs-rtldeleteace.md) | The RtlDeleteAce routine deletes an access control entry (ACE) from a specified access control list (ACL). |
| [IoCheckQuotaBufferValidity function](nf-ntifs-iocheckquotabuffervalidity.md) | The IoCheckQuotaBufferValidity routine checks whether the specified quota buffer is valid. |
| [RtlGetCompressionWorkSpaceSize function](nf-ntifs-rtlgetcompressionworkspacesize.md) | The RtlGetCompressionWorkSpaceSize function is used to determine the correct size of the WorkSpace buffer for the RtlCompressBuffer and RtlDecompressFragment functions. |
| [SspiLocalFree function](nf-ntifs-sspilocalfree.md) | TBD |
| [ZwUnlockFile function](nf-ntifs-zwunlockfile.md) | The ZwUnlockFile routine unlocks a byte-range lock in a file. |
| [SeMaximumAuditMaskFromGlobalSacl function](nf-ntifs-semaximumauditmaskfromglobalsacl.md) | TBD |
| [CcGetFileSizePointer function](nf-ntifs-ccgetfilesizepointer.md) | TBD |
| [KeReadStateQueue function](nf-ntifs-kereadstatequeue.md) | TBD |
| [NtQueryDirectoryFileEx function](nf-ntifs-ntquerydirectoryfileex.md) | TBD |
| [SeTokenFromAccessInformation function](nf-ntifs-setokenfromaccessinformation.md) | TBD |
| [IoGetConfigurationInformation function](nf-ntifs-iogetconfigurationinformation.md) | TBD |
| [RtlCaptureContext function](nf-ntifs-rtlcapturecontext.md) | The RtlCaptureContext function retrieves a context record in the context of the caller. |
| [FsRtlSupportsPerStreamContexts function](nf-ntifs-fsrtlsupportsperstreamcontexts.md) | TBD |
| [FsRtlIsChecksumError function](nf-ntifs-fsrtlischecksumerror.md) | TBD |
| [FsRtlUpdateDiskCounters function](nf-ntifs-fsrtlupdatediskcounters.md) | TBD |
| [FsRtlSupportsPerFileContexts function](nf-ntifs-fsrtlsupportsperfilecontexts.md) | TBD |
| [IoReleaseVpbSpinLock function](nf-ntifs-ioreleasevpbspinlock.md) | The IoReleaseVpbSpinLock routine releases the Volume Parameter Block (VPB) spin lock. |
| [SspiGetTargetHostName function](nf-ntifs-sspigettargethostname.md) | TBD |
| [FsRtlAllocateExtraCreateParameterFromLookasideList function](nf-ntifs-fsrtlallocateextracreateparameterfromlookasidelist.md) | The FsRtlAllocateExtraCreateParameterFromLookasideList routine allocates memory pool from a given lookaside list for an extra create parameter (ECP) context structure, and generates a pointer to that structure. |
| [CcPurgeCacheSection function](nf-ntifs-ccpurgecachesection.md) | The CcPurgeCacheSection routine purges all or a portion of a cached file from the system cache. |
| [SeTokenIsRestricted function](nf-ntifs-setokenisrestricted.md) | The SeTokenIsRestricted routine determines whether a token contains a list of restricting security identifiers (SID). |
| [RtlInitializeUnicodePrefix function](nf-ntifs-rtlinitializeunicodeprefix.md) | The RtlInitializeUnicodePrefix routine initializes a prefix table. |
| [RtlAddAccessAllowedAceEx function](nf-ntifs-rtladdaccessallowedaceex.md) | The RtlAddAccessAllowedAceEx routine adds an access-allowed access control entry (ACE) with inheritance ACE flags to an access control list (ACL). The access is granted to the specified security identifier (SID). |
| [FsRtlFreeExtraCreateParameterList function](nf-ntifs-fsrtlfreeextracreateparameterlist.md) | The FsRtlFreeExtraCreateParameterList routine frees an extra create parameter (ECP) list structure. |
| [NtOpenThreadToken function](nf-ntifs-ntopenthreadtoken.md) | TBD |
| [RtlAddAccessAllowedAce function](nf-ntifs-rtladdaccessallowedace.md) | The RtlAddAccessAllowedAce routine adds an access-allowed access control entry (ACE) to an access control list (ACL). The access is granted to the specified security identifier (SID). |
| [SspiInitializeSecurityContextAsyncA function](nf-ntifs-sspiinitializesecuritycontextasynca.md) | TBD |
| [KeInitializeQueue function](nf-ntifs-keinitializequeue.md) | The KeInitializeQueue routine initializes a queue object on which threads can wait for entries. |
| [RtlSubAuthoritySid function](nf-ntifs-rtlsubauthoritysid.md) | The RtlSubAuthoritySid routine returns a pointer to a specified subauthority of a security identifier (SID). |
| [CcZeroData function](nf-ntifs-cczerodata.md) | The CcZeroData routine zeros the specified range of bytes in a cached or noncached file. |
| [CcCanIWrite function](nf-ntifs-cccaniwrite.md) | The CcCanIWrite routine determines whether the caller can write to a cached file. |
| [RtlPointerToOffset function](nf-ntifs-rtlpointertooffset.md) | TBD |
| [FsRtlIssueDeviceIoControl function](nf-ntifs-fsrtlissuedeviceiocontrol.md) | The FsRtlIssueDeviceIoControl routine sends a synchronous device I/O control request to a target device object. |
| [RtlRandom function](nf-ntifs-rtlrandom.md) | The RtlRandom routine returns a random number that was generated from a given seed value. |
| [KeReleaseMutant function](nf-ntifs-kereleasemutant.md) | TBD |
| [RtlIsPartialPlaceholderFileHandle function](nf-ntifs-rtlispartialplaceholderfilehandle.md) | The RtlIsPartialPlaceholderFileHandle routine determines if a file is a known type of placeholder, based on a file handle. |
| [ZwFsControlFile function](nf-ntifs-zwfscontrolfile.md) | The ZwFsControlFile routine sends a control code directly to a specified file system or file system filter driver, causing the corresponding driver to perform the specified action. |
| [KeInitializeMutant function](nf-ntifs-keinitializemutant.md) | TBD |
| [RtlEqualPrefixSid function](nf-ntifs-rtlequalprefixsid.md) | The RtlEqualPrefixSid routine determines whether two security-identifier (SID) prefixes are equal. An SID prefix is the entire SID except for the last subauthority value. |
| [SeTokenIsNoChildProcessRestrictionEnforced function](nf-ntifs-setokenisnochildprocessrestrictionenforced.md) | The SeTokenIsNoChildProcessRestrictionEnforced routine determines if the token carries the no child process restriction. |
| [FsRtlTeardownPerFileContexts function](nf-ntifs-fsrtlteardownperfilecontexts.md) | File systems call theFsRtlTeardownPerFileContexts routine to free FSRTL_PER_FILE_CONTEXT objects that are associated with a file control block (FCB) structure. |
| [RtlCopySid function](nf-ntifs-rtlcopysid.md) | The RtlCopySid routine copies the value of a security identifier (SID) to a buffer. |
| [RtlCreateVirtualAccountSid function](nf-ntifs-rtlcreatevirtualaccountsid.md) | TBD |
| [QuerySecurityPackageInfoW function](nf-ntifs-querysecuritypackageinfow.md) | TBD |
| [IoStartNextPacketByKey function](nf-ntifs-iostartnextpacketbykey.md) | The IoStartNextPacketByKey routine dequeues the next I/O request packet from the specified device object's associated device queue according to a specified sort-key value and calls the driver's StartIo routine with that IRP. |
| [CcCopyRead function](nf-ntifs-cccopyread.md) | The CcCopyRead routine copies data from a cached file to a user buffer. |
| [FsRtlIsAnsiCharacterLegalFat function](nf-ntifs-fsrtlisansicharacterlegalfat.md) | The FsRtlIsAnsiCharacterLegalFat macro determines whether an ANSI character is legal for FAT file names. |
| [CcFastCopyWrite function](nf-ntifs-ccfastcopywrite.md) | The CcFastCopyWrite routine performs a fast copy write from a buffer in memory to a cached file. |
| [MmMdlPagesAreZero function](nf-ntifs-mmmdlpagesarezero.md) | TBD |
| [CcMdlReadComplete function](nf-ntifs-ccmdlreadcomplete.md) | The CcMdlReadComplete routine frees the memory descriptor lists (MDL) created by CcMdlRead for a cached file. |
| [FsRtlIsUnicodeCharacterWild function](nf-ntifs-fsrtlisunicodecharacterwild.md) | The FsRtlIsUnicodeCharacterWild macro determines whether a Unicode character is a wildcard character. |
| [CcSetDirtyPageThreshold function](nf-ntifs-ccsetdirtypagethreshold.md) | The CcSetDirtyPageThreshold routine sets a per-file dirty page threshold on a cached file. |
| [NtPrivilegeCheck function](nf-ntifs-ntprivilegecheck.md) | TBD |
| [SeQuerySubjectContextToken function](nf-ntifs-sequerysubjectcontexttoken.md) | The SeQuerySubjectContextToken macro retrieves the access token for a security subject context. |
| [IoSetFsZeroingOffset function](nf-ntifs-iosetfszeroingoffset.md) | TBD |
| [MmDoesFileHaveUserWritableReferences function](nf-ntifs-mmdoesfilehaveuserwritablereferences.md) | The MmDoesFileHaveUserWritableReferences function returns the number of writable references for a file object. |
| [KeStallExecutionProcessor function](nf-ntifs-kestallexecutionprocessor.md) | The KeStallExecutionProcessor routine stalls the caller on the current processor for a specified time interval. |
| [AddCredentialsA function](nf-ntifs-addcredentialsa.md) | TBD |
| [FsRtlDeleteExtraCreateParameterLookasideList function](nf-ntifs-fsrtldeleteextracreateparameterlookasidelist.md) | The FsRtlDeleteExtraCreateParameterLookasideList routine frees an extra create parameter (ECP) lookaside list. |
| [SeTokenType function](nf-ntifs-setokentype.md) | TBD |
| [IoEnumerateDeviceObjectList function](nf-ntifs-ioenumeratedeviceobjectlist.md) | The IoEnumerateDeviceObjectList routine enumerates a driver's device object list. |
| [FsRtlIsMobileOS function](nf-ntifs-fsrtlismobileos.md) | TBD |
| [CcReadAhead function](nf-ntifs-ccreadahead.md) | TBD |
| [RtlIsCloudFilesPlaceholder function](nf-ntifs-rtliscloudfilesplaceholder.md) | The RtlIsCloudFilesPlaceholder routine determines if a file or a directory is a CloudFiles placeholder, based on the FileAttributes and ReparseTag values of the file. |
| [NtAdjustPrivilegesToken function](nf-ntifs-ntadjustprivilegestoken.md) | TBD |
| [RtlUTF8ToUnicodeN function](nf-ntifs-rtlutf8tounicoden.md) | The RtlUTF8ToUnicodeN routine converts a UTF-8 string to a Unicode string. |
| [CcRemapBcb function](nf-ntifs-ccremapbcb.md) | The CcRemapBcb routine maps a buffer control block (BCB) an additional time to preserve it through several calls that perform additional maps and unpins. |
| [RtlCreateUnicodeString function](nf-ntifs-rtlcreateunicodestring.md) | The RtlCreateUnicodeString routine creates a new counted Unicode string. |
| [DecryptMessage function](nf-ntifs-decryptmessage.md) | TBD |
| [RtlEqualSid function](nf-ntifs-rtlequalsid.md) | The RtlEqualSid routine determines whether two security identifier (SID) values are equal. Two SIDs must match exactly to be considered equal. |
| [InitializeSecurityContextW function](nf-ntifs-initializesecuritycontextw.md) | TBD |
| [KeRemoveQueue function](nf-ntifs-keremovequeue.md) | The KeRemoveQueue routine gives the calling thread a pointer to a dequeued entry from the given queue object or allows the caller to wait, up to an optional timeout interval, on the queue object. |
| [CcCopyWriteWontFlush function](nf-ntifs-cccopywritewontflush.md) | The CcCopyWriteWontFlush macro determines whether the amount of data to be copied in a call to CcCopyWrite is small enough not to require immediate flushing to disk if CcCopyWrite is called with Wait set to FALSE. |
| [RtlGenerate8dot3Name function](nf-ntifs-rtlgenerate8dot3name~r1.md) | The RtlGenerate8dot3Name routine generates a short (8.3) name for the specified long file name. |
| [IoReplaceFileObjectName function](nf-ntifs-ioreplacefileobjectname.md) | The IoReplaceFileObjectName routine replaces the name of a file object. |
| [RtlGetDaclSecurityDescriptor function](nf-ntifs-rtlgetdaclsecuritydescriptor.md) | The RtlGetDaclSecurityDescriptor routine returns a pointer to the discretionary ACL (DACL) for a security descriptor. |
| [SeAuditingHardLinkEventsWithContext function](nf-ntifs-seauditinghardlinkeventswithcontext.md) | TBD |
| [NtOpenThreadTokenEx function](nf-ntifs-ntopenthreadtokenex.md) | TBD |
| [NtDeviceIoControlFile function](nf-ntifs-ntdeviceiocontrolfile.md) | TBD |
| [SeTokenSetNoChildProcessRestricted function](nf-ntifs-setokensetnochildprocessrestricted.md) | The SeTokenSetNoChildProcessRestricted routine sets the TOKEN_AUDIT_NO_CHILD_PROCESS or TOKEN_AUDIT_NO_CHILD_PROCESS flags in the token. |
| [LsaRegisterLogonProcess function](nf-ntifs-lsaregisterlogonprocess.md) | TBD |
| [CcMapData function](nf-ntifs-ccmapdata~r1.md) | The CcMapData routine maps a specified byte range of a cached file to a buffer in memory. |
| [MapSecurityError function](nf-ntifs-mapsecurityerror.md) | The MapSecurityError function maps a security interface SECURITY_STATUS status code to a corresponding NSTATUS status code. |
| [ExInitializePushLock function](nf-ntifs-exinitializepushlock.md) | TBD |
| [SspiFreeCredentialsHandleAsync function](nf-ntifs-sspifreecredentialshandleasync.md) | TBD |
| [FsRtlGetSectorSizeInformation function](nf-ntifs-fsrtlgetsectorsizeinformation.md) | The FsRtlGetSectorSizeInformation routine retrieves the physical and logical sector size information for a storage volume. |
| [FsRtlGetNextExtraCreateParameter function](nf-ntifs-fsrtlgetnextextracreateparameter.md) | The FsRtlGetNextExtraCreateParameter routine returns a pointer to the next (or first) extra create parameter (ECP) context structure in a given ECP list. |
| [RtlMultiByteToUnicodeSize function](nf-ntifs-rtlmultibytetounicodesize.md) | The RtlMultiByteToUnicodeSize routine determines the number of bytes that are required to store the Unicode translation for the specified source string. |
| [PoClearPowerRequest function](nf-ntifs-poclearpowerrequest.md) | The PoClearPowerRequest routine decrements the count for the specified power request type. |
| [SspiEncodeAuthIdentityAsStrings function](nf-ntifs-sspiencodeauthidentityasstrings.md) | TBD |
| [RtlInitUnicodeStringEx function](nf-ntifs-rtlinitunicodestringex.md) | TBD |
| [KeGetProcessorNumberFromIndex function](nf-ntifs-kegetprocessornumberfromindex.md) | TBD |
| [RtlNextUnicodePrefix function](nf-ntifs-rtlnextunicodeprefix.md) | The RtlNextUnicodePrefix routine is used to enumerate the elements in a Unicode prefix table. |
| [SspiUnmarshalAuthIdentity function](nf-ntifs-sspiunmarshalauthidentity.md) | TBD |
| [IoSetStartIoAttributes function](nf-ntifs-iosetstartioattributes.md) | The IoSetStartIoAttributes routine sets attributes for the driver's StartIo routine. |
| [CTL_CODE function](nf-ntifs-ctl-code.md) | TBD |
| [SeAppendPrivileges function](nf-ntifs-seappendprivileges.md) | The SeAppendPrivileges routine appends additional privileges to the privilege set in an access state structure. |
| [ChangeAccountPasswordW function](nf-ntifs-changeaccountpasswordw.md) | TBD |
| [ZwQueryInformationToken function](nf-ntifs-zwqueryinformationtoken.md) | The ZwQueryInformationToken routine retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information. |
| [IoGetRequestorProcess function](nf-ntifs-iogetrequestorprocess.md) | The IoGetRequestorProcess routine returns a process pointer for the thread that originally requested a given I/O operation. |
| [MmPrefetchPages function](nf-ntifs-mmprefetchpages.md) | The MmPrefetchPages routine reads groups of pages from secondary storage in the optimal fashion. |
| [FsRtlMupGetProviderInfoFromFileObject function](nf-ntifs-fsrtlmupgetproviderinfofromfileobject.md) | The FsRtlMupGetProviderInfoFromFileObject routine gets information about a network redirector that is registered with the multiple UNC provider (MUP) from a file object for a file that is located on a remote file system. |
| [PsChargeProcessPoolQuota function](nf-ntifs-pschargeprocesspoolquota.md) | TBD |
| [SeCaptureSubjectContextEx function](nf-ntifs-secapturesubjectcontextex.md) | TBD |
| [FsRtlVolumeDeviceToCorrelationId function](nf-ntifs-fsrtlvolumedevicetocorrelationid.md) | TBD |
| [NtDeleteObjectAuditAlarm function](nf-ntifs-ntdeleteobjectauditalarm.md) | TBD |
| [RtlTimeToSecondsSince1970 function](nf-ntifs-rtltimetosecondssince1970.md) | The RtlTimeToSecondsSince1970 routine converts a given absolute system time value to the elapsed time, in seconds, since the beginning of 1970. |
| [SeReleaseSubjectContext function](nf-ntifs-sereleasesubjectcontext.md) | The SeReleaseSubjectContext routine releases a subject security context captured by an earlier call to SeCaptureSubjectContext. |
| [InitSecurityInterfaceW function](nf-ntifs-initsecurityinterfacew.md) | TBD |
| [CcMdlWriteAbort function](nf-ntifs-ccmdlwriteabort.md) | The CcMdlWriteAbort routine frees memory descriptor lists (MDL) created by an earlier call to CcPrepareMdlWrite. |
| [FsRtlRemoveDotsFromPath function](nf-ntifs-fsrtlremovedotsfrompath.md) | The FsRtlRemoveDotsFromPath routine removes unnecessary occurrences of '.' and '..' from the specified path. |
| [RtlSelfRelativeToAbsoluteSD function](nf-ntifs-rtlselfrelativetoabsolutesd.md) | The RtlSelfRelativeToAbsoluteSD routine creates a new security descriptor in absolute format by using a security descriptor in self-relative format as a template. |
| [NtAccessCheckByTypeResultListAndAuditAlarmByHandle function](nf-ntifs-ntaccesscheckbytyperesultlistandauditalarmbyhandle.md) | TBD |
| [IoSetFsZeroingOffset function](nf-ntifs-iosetfszeroingoffset~r1.md) | TBD |
| [CcUnpinData function](nf-ntifs-ccunpindata.md) | The CcUnpinData routine releases cached file data that was mapped or pinned by an earlier call to CcMapData, CcPinRead, or CcPreparePinWrite. |
| [CcSetBcbOwnerPointer function](nf-ntifs-ccsetbcbownerpointer.md) | The CcSetBcbOwnerPointer routine sets the owner thread pointer for a pinned buffer control block (BCB). |
| [SeQueryTokenIntegrity function](nf-ntifs-sequerytokenintegrity.md) | TBD |
| [FsRtlIsNonEmptyDirectoryReparsePointAllowed function](nf-ntifs-fsrtlisnonemptydirectoryreparsepointallowed.md) | TBD |
| [SspiAcquireCredentialsHandleAsyncA function](nf-ntifs-sspiacquirecredentialshandleasynca.md) | TBD |
| [SeOpenObjectAuditAlarm function](nf-ntifs-seopenobjectauditalarm.md) | The SeOpenObjectAuditAlarm routine generates audit and alarm messages when an attempt is made to open an object. |
| [MakeSignature function](nf-ntifs-makesignature.md) | TBD |
| [RtlReserveChunk function](nf-ntifs-rtlreservechunk.md) | TBD |
| [FsRtlIsPagingFile function](nf-ntifs-fsrtlispagingfile.md) | The FsRtlIsPagingFile routine determines whether a given file is a paging file. |
| [RtlOffsetToPointer function](nf-ntifs-rtloffsettopointer.md) | TBD |
| [RtlIsPartialPlaceholder function](nf-ntifs-rtlispartialplaceholder.md) | The RtlIsPartialPlaceholder routine determines if a file or a directory is a CloudFiles placeholder, based on the FileAttributes and ReparseTag values of the file. |
| [SspiAsyncContextRequiresNotify function](nf-ntifs-sspiasynccontextrequiresnotify.md) | TBD |
| [CcMdlRead function](nf-ntifs-ccmdlread.md) | TBD |
| [QueryContextAttributesW function](nf-ntifs-querycontextattributesw.md) | TBD |
| [RtlInitializeSid function](nf-ntifs-rtlinitializesid.md) | The RtlInitializeSid routine initializes a security identifier (SID) structure. |
| [IoRegisterFsRegistrationChangeEx function](nf-ntifs-ioregisterfsregistrationchangeex.md) | The IoRegisterFsRegistrationChangeEx routine registers a file system filter driver's notification routine to be called whenever a file system registers or unregisters itself as an active file system. |
| [PfxRemovePrefix function](nf-ntifs-pfxremoveprefix.md) | TBD |
| [FsRtlFastLock function](nf-ntifs-fsrtlfastlock.md) | The FsRtlFastLock macro is used by file systems and filter drivers to request a byte-range lock for a file stream. |
| [SeUnregisterLogonSessionTerminatedRoutine function](nf-ntifs-seunregisterlogonsessionterminatedroutine.md) | The SeUnregisterLogonSessionTerminatedRoutine routine unregisters a callback routine that was registered by an earlier call to SeRegisterLogonSessionTerminatedRoutine. |
| [RtlInsertUnicodePrefix function](nf-ntifs-rtlinsertunicodeprefix.md) | The RtlInsertUnicodePrefix routine inserts a new element into a Unicode prefix table. |
| [SeTokenIsWriteRestricted function](nf-ntifs-setokeniswriterestricted.md) | TBD |
| [IoQueueThreadIrp function](nf-ntifs-ioqueuethreadirp.md) | TBD |
| [KeQueryPerformanceCounter function](nf-ntifs-kequeryperformancecounter.md) | The KeQueryPerformanceCounter routine retrieves the current value and frequency of the performance counter.Use KeQueryPerformanceCounter to acquire high resolution (&lt;1us) time stamps for time interval measurements. |
| [NtSetInformationToken function](nf-ntifs-ntsetinformationtoken.md) | TBD |
| [SeTokenIsAdmin function](nf-ntifs-setokenisadmin.md) | The SeTokenIsAdmin routine determines whether a token contains the local administrators group. |
| [PsIsSystemThread function](nf-ntifs-psissystemthread.md) | The PsIsSystemThread routine checks whether a given thread is a system thread. |
| [SspiAcceptSecurityContextAsync function](nf-ntifs-sspiacceptsecuritycontextasync.md) | TBD |
| [NtQueryInformationToken function](nf-ntifs-ntqueryinformationtoken.md) | TBD |
| [RtlFillMemoryUlong function](nf-ntifs-rtlfillmemoryulong~r1.md) | The RtlFillMemoryUlong routine fills the specified range of memory with one or more repetitions of a ULONG value. |
| [ZwSetEaFile function](nf-ntifs-zwseteafile.md) | The ZwSetEaFile routine sets extended-attribute (EA) values for a file. |
| [RtlDestroyHeap function](nf-ntifs-rtldestroyheap.md) | The RtlDestroyHeap routine destroys the specified heap object. RtlDestroyHeap decommits and releases all the pages of a private heap object, and it invalidates the handle to the heap. |
| [CcMdlWriteComplete function](nf-ntifs-ccmdlwritecomplete.md) | The CcMdlWriteComplete routine frees the memory descriptor lists (MDL) created by CcPrepareMdlWrite for a cached file. |
| [NtFilterToken function](nf-ntifs-ntfiltertoken.md) | TBD |
| [IoClearFsTrackOffsetState function](nf-ntifs-ioclearfstrackoffsetstate.md) | TBD |
| [RtlxOemStringToUnicodeSize function](nf-ntifs-rtlxoemstringtounicodesize.md) | TBD |
| [RtlOemStringToCountedUnicodeSize function](nf-ntifs-rtloemstringtocountedunicodesize.md) | The RtlOemStringToCountedUnicodeSize routine determines the size, in bytes, that a given OEM string will be after it is translated into a counted Unicode string. |
| [PsAssignImpersonationToken function](nf-ntifs-psassignimpersonationtoken.md) | TBD |
| [IoEnumerateRegisteredFiltersList function](nf-ntifs-ioenumerateregisteredfilterslist.md) | The IoEnumerateRegisteredFiltersList routine enumerates the file system filter drivers that have registered with the system. |
| [NtCreateFile function](nf-ntifs-ntcreatefile.md) | TBD |
| [IoGetDeviceToVerify function](nf-ntifs-iogetdevicetoverify.md) | The IoGetDeviceToVerify routine returns a pointer to the device object, representing a removable-media device, that is the target of the given thread's I/O request. |
| [SeQuerySessionIdToken function](nf-ntifs-sequerysessionidtoken.md) | TBD |
| [SeExamineSacl function](nf-ntifs-seexaminesacl.md) | TBD |
| [FsRtlQueryKernelEaFile function](nf-ntifs-fsrtlquerykerneleafile.md) | The routine FsRtlQueryKernelEaFile is used to build an explicit QueryEA request and synchronously wait for it to complete, returning the result. This allows the caller to do this by FileObject instead of a handle. |
| [SspiCompareAuthIdentities function](nf-ntifs-sspicompareauthidentities.md) | TBD |
| [FsRtlGetSupportedFeatures function](nf-ntifs-fsrtlgetsupportedfeatures.md) | The FsRtlGetSupportedFeatures routine returns the supported features of a volume attached to the specified device object. |
| [SeAccessCheckFromStateEx function](nf-ntifs-seaccesscheckfromstateex.md) | TBD |
| [SeAuditHardLinkCreation function](nf-ntifs-seaudithardlinkcreation.md) | TBD |
| [NtOpenFile function](nf-ntifs-ntopenfile.md) | TBD |
| [IsReparseTagDirectory function](nf-ntifs-isreparsetagdirectory.md) | TBD |
| [RtlUpcaseUnicodeStringToOemString function](nf-ntifs-rtlupcaseunicodestringtooemstring.md) | The RtlUpcaseUnicodeStringToOemString routine translates a given Unicode source string into an uppercase OEM string using the current system OEM code page. |
| [FsRtlIncrementCcFastReadNoWait function](nf-ntifs-fsrtlincrementccfastreadnowait.md) | The FsRtlIncrementCcFastReadNoWait routine increments the CcFastReadNoWait performance counter in a per processor control block of cache manager system counters. |
| [SeFilterToken function](nf-ntifs-sefiltertoken.md) | The SeFilterToken routine creates a new access token that is a restricted version of an existing access token. |
| [RtlCreateSystemVolumeInformationFolder function](nf-ntifs-rtlcreatesystemvolumeinformationfolder.md) | The RtlCreateSystemVolumeInformationFolder routine verifies the existence of the &#0034;System Volume Information&#0034; folder on a file system volume. If the folder is not present, then the folder is created. |
| [SeAuditingAnyFileEventsWithContext function](nf-ntifs-seauditinganyfileeventswithcontext.md) | TBD |
| [IoInitializePriorityInfo function](nf-ntifs-ioinitializepriorityinfo.md) | The IoInitializePriorityInfo routine initializes a structure of type IO_PRIORITY_INFO. |
| [PsDereferenceImpersonationToken function](nf-ntifs-psdereferenceimpersonationtoken.md) | The PsDereferenceImpersonationToken routine decrements the reference count of an impersonation token. |
| [NtPrivilegedServiceAuditAlarm function](nf-ntifs-ntprivilegedserviceauditalarm.md) | TBD |
| [SeLockSubjectContext function](nf-ntifs-selocksubjectcontext.md) | The SeLockSubjectContext routine locks the primary and impersonation tokens of a captured subject context. |
| [FsRtlAreVolumeStartupApplicationsComplete function](nf-ntifs-fsrtlarevolumestartupapplicationscomplete.md) | The FsRtlAreVolumeStartupApplicationsComplete function determines whether volume startup applications have completed processing. |
| [RtlFreeHeap function](nf-ntifs-rtlfreeheap.md) | The RtlFreeHeap routine frees a memory block that was allocated from a heap by RtlAllocateHeap. |
| [PoSetDeviceBusyEx function](nf-ntifs-posetdevicebusyex.md) | The PoSetDeviceBusyEx routine notifies the power manager that the device associated with the specified idle counter is busy. |
| [AcquireCredentialsHandleW function](nf-ntifs-acquirecredentialshandlew.md) | TBD |
| [RtlInitCodePageTable function](nf-ntifs-rtlinitcodepagetable.md) | TBD |
| [IoGetAttachedDeviceReference function](nf-ntifs-iogetattacheddevicereference.md) | The IoGetAttachedDeviceReference routine returns a pointer to the highest level device object in a driver stack and increments the reference count on that object. |
| [ZwQueryObject function](nf-ntifs-zwqueryobject.md) | The ZwQueryObject routine provides information about a supplied object. |
| [CcWaitForCurrentLazyWriterActivity function](nf-ntifs-ccwaitforcurrentlazywriteractivity.md) | The CcWaitForCurrentLazyWriterActivity routine puts the caller into a wait state until the current batch of lazy writer activity is completed. |
| [ZwFlushVirtualMemory function](nf-ntifs-zwflushvirtualmemory.md) | The ZwFlushVirtualMemory routine flushes a range of virtual addresses within the virtual address space of a specified process which map to a data file back out to the data file if they have been modified. |
| [FsRtlLookupPerStreamContext function](nf-ntifs-fsrtllookupperstreamcontext.md) | The FsRtlLookupPerStreamContext macro retrieves a per-stream context structure for a file stream. |
| [RtlValidSid function](nf-ntifs-rtlvalidsid.md) | The RtlValidSid routine validates a security identifier (SID) by verifying that the revision number is within a known range and that the number of subauthorities is less than the maximum. |
| [PsReturnPoolQuota function](nf-ntifs-psreturnpoolquota.md) | The PsReturnPoolQuota routine returns pool quota of the specified pool type to the specified process. |
| [RtlDecompressChunks function](nf-ntifs-rtldecompresschunks.md) | TBD |
| [RtlFillMemoryUlong function](nf-ntifs-rtlfillmemoryulong.md) | The RtlFillMemoryUlong routine fills the specified range of memory with one or more repetitions of a ULONG value. |
| [BooleanFlagOn function](nf-ntifs-booleanflagon.md) | TBD |
| [RtlUpcaseUnicodeStringToCountedOemString function](nf-ntifs-rtlupcaseunicodestringtocountedoemstring.md) | The RtlUpcaseUnicodeStringToCountedOemString routine translates a given Unicode source string into an uppercase counted OEM string using the current system OEM code page. |
| [VerifySignature function](nf-ntifs-verifysignature.md) | TBD |
| [SeAuditFipsCryptoSelftests function](nf-ntifs-seauditfipscryptoselftests.md) | TBD |
| [CcPinRead function](nf-ntifs-ccpinread.md) | The CcPinRead routine pins the specified byte range of a cached file and reads the pinned data into a buffer in memory. |
| [FsRtlInsertPerStreamContext function](nf-ntifs-fsrtlinsertperstreamcontext.md) | The FsRtlInsertPerStreamContext routine associates a file system filter driver's per-stream context structure with a file stream. |
| [RevertSecurityContext function](nf-ntifs-revertsecuritycontext.md) | TBD |
| [SecMakeSPNEx function](nf-ntifs-secmakespnex.md) | SecMakeSPNEx creates a service provider name string that can be used when communicating with specific security service providers. |
| [FsRtlGetVirtualDiskNestingLevel function](nf-ntifs-fsrtlgetvirtualdisknestinglevel.md) | TBD |
| [NtCloseObjectAuditAlarm function](nf-ntifs-ntcloseobjectauditalarm.md) | TBD |
| [RtlUnicodeToOemN function](nf-ntifs-rtlunicodetooemn.md) | The RtlUnicodeToOemN routine translates a given Unicode string to an OEM string, using the current system OEM code page. |
| [FsRtlIsDaxVolume function](nf-ntifs-fsrtlisdaxvolume.md) | This routine queries if the specified file is on a direct access (DAX) volume. |
| [KeInsertHeadQueue function](nf-ntifs-keinsertheadqueue.md) | The KeInsertHeadQueue routine inserts an entry at the head of the given queue if it cannot immediately use the entry to satisfy a thread wait. |
| [IoGetFsZeroingOffset function](nf-ntifs-iogetfszeroingoffset.md) | TBD |
| [RtlIdnToNameprepUnicode function](nf-ntifs-rtlidntonameprepunicode.md) | TBD |
| [SecLookupAccountSid function](nf-ntifs-seclookupaccountsid.md) | SecLookupAccountSid accepts a security identifier (SID) as input. It retrieves the name of the account for this SID and the name of the first domain on which this SID is found. |
| [RtlOemStringToUnicodeSize function](nf-ntifs-rtloemstringtounicodesize.md) | The RtlOemStringToUnicodeSize routine determines the size, in bytes, that a given OEM string will be after it is translated into a null-terminated Unicode string. |
| [QueryCredentialsAttributesExW function](nf-ntifs-querycredentialsattributesexw.md) | TBD |
| [RtlSetGroupSecurityDescriptor function](nf-ntifs-rtlsetgroupsecuritydescriptor.md) | The RtlSetGroupSecurityDescriptor routine sets the primary group information of an absolute-format security descriptor. It replaces any primary group information that is already present in the security descriptor. |
| [NtUnlockFile function](nf-ntifs-ntunlockfile.md) | TBD |
| [IoUnregisterFsRegistrationChange function](nf-ntifs-iounregisterfsregistrationchange.md) | The IoUnregisterFsRegistrationChange routine unregisters file system filter driver's file system registration change notification routine. |
| [PsIsThreadTerminating function](nf-ntifs-psisthreadterminating.md) | The PsIsThreadTerminating routine checks whether a thread is terminating. |
| [GetSecurityUserInfo function](nf-ntifs-getsecurityuserinfo.md) | The GetSecurityUserInfo function retrieves information about a logon session. |
| [PoUnregisterPowerSettingCallback function](nf-ntifs-pounregisterpowersettingcallback.md) | The PoUnregisterPowerSettingCallback routine unregisters a power-setting callback routine that a driver previously registered by calling the PoRegisterPowerSettingCallback routine. |
| [ZwSetEvent function](nf-ntifs-zwsetevent.md) | The ZwSetEvent routine sets an event object to a Signaled state and attempts to satisfy as many waits as possible. |
| [SeOpenObjectForDeleteAuditAlarmWithTransaction function](nf-ntifs-seopenobjectfordeleteauditalarmwithtransaction.md) | TBD |
| [IoThreadToProcess function](nf-ntifs-iothreadtoprocess.md) | The IoThreadToProcess routine returns a pointer to the process for the specified thread. |
| [QueryCredentialsAttributesW function](nf-ntifs-querycredentialsattributesw.md) | TBD |
| [CcPreparePinWrite function](nf-ntifs-ccpreparepinwrite.md) | The CcPreparePinWrite routine pins the specified byte range of a cached file for write access. |
| [IoCreateStreamFileObjectEx function](nf-ntifs-iocreatestreamfileobjectex.md) | The IoCreateStreamFileObjectEx routine creates a new stream file object. |
| [SeUnlockSubjectContext function](nf-ntifs-seunlocksubjectcontext.md) | The SeUnlockSubjectContext routine unlocks the tokens of a captured subject context that were locked by a call to SeLockSubjectContext. |
| [NtCreateSection function](nf-ntifs-ntcreatesection.md) | TBD |
| [AcceptSecurityContext function](nf-ntifs-acceptsecuritycontext.md) | TBD |
| [IoPageRead function](nf-ntifs-iopageread.md) | TBD |
| [CcCopyWriteWontFlush function](nf-ntifs-cccopywritewontflush~r1.md) | The CcCopyWriteWontFlush macro determines whether the amount of data to be copied in a call to CcCopyWrite is small enough not to require immediate flushing to disk if CcCopyWrite is called with Wait set to FALSE. |
| [FsRtlChangeBackingFileObject function](nf-ntifs-fsrtlchangebackingfileobject.md) | The FsRtlChangeBackingFileObject routine replaces the current file object with a new file object. |
| [ZwNotifyChangeKey function](nf-ntifs-zwnotifychangekey.md) | The ZwNotifyChangeKey routine allows a driver to request notification when a registry key changes. |
| [IoIsFileOpenedExclusively function](nf-ntifs-ioisfileopenedexclusively.md) | TBD |
| [FsRtlAcknowledgeEcp function](nf-ntifs-fsrtlacknowledgeecp.md) | The FsRtlAcknowledgeEcp routine marks an extra create parameter (ECP) context structure as acknowledged. |
| [ZwQueryQuotaInformationFile function](nf-ntifs-zwqueryquotainformationfile.md) | The ZwQueryQuotaInformationFile routine retrieves quota entries associated with the volume specified by the FileHandle parameter. |
| [CcSetReadAheadGranularity function](nf-ntifs-ccsetreadaheadgranularity.md) | The CcSetReadAheadGranularity routine sets the read-ahead granularity for a cached file. |
| [KeInsertQueue function](nf-ntifs-keinsertqueue.md) | The KeInsertQueue routine inserts an entry at the tail of the given queue if it cannot immediately use the entry to satisfy a thread wait. |
| [FsRtlIsExtentDangling function](nf-ntifs-fsrtlisextentdangling.md) | TBD |
| [IoSetDeviceToVerify function](nf-ntifs-iosetdevicetoverify.md) | The IoSetDeviceToVerify routine specifies a device object to be verified. The specified device object represents a removable media device. |
| [RtlIsNormalizedString function](nf-ntifs-rtlisnormalizedstring.md) | TBD |
| [RtlCaptureStackBackTrace function](nf-ntifs-rtlcapturestackbacktrace.md) | The RtlCaptureStackBackTrace routine captures a stack back trace by walking up the stack and recording the information for each frame. |
| [RtlUnicodeStringToOemString function](nf-ntifs-rtlunicodestringtooemstring.md) | The RtlUnicodeStringToOemString routine translates a given Unicode source string into an OEM string using the current system OEM code page. |
| [FsRtlInsertPerFileObjectContext function](nf-ntifs-fsrtlinsertperfileobjectcontext.md) | For a &#0034;legacy&#0034; file system filter driver, the FsRtlInsertPerFileObjectContext function associates context information with a file object. |
| [PoCreatePowerRequest function](nf-ntifs-pocreatepowerrequest.md) | The PoCreatePowerRequest routine creates a power request object. |
| [KeAttachProcess function](nf-ntifs-keattachprocess.md) | TBD |
| [KeDetachProcess function](nf-ntifs-kedetachprocess.md) | TBD |
| [PoSetPowerState function](nf-ntifs-posetpowerstate.md) | The PoSetPowerState routine notifies the system of a change in the device power state for a device. |
| [PsUpdateDiskCounters function](nf-ntifs-psupdatediskcounters.md) | The PsUpdateDiskCounters routine updates the disk I/O counters of a given process. |
| [IoAcquireVpbSpinLock function](nf-ntifs-ioacquirevpbspinlock.md) | The IoAcquireVpbSpinLock routine acquires the Volume Parameter Block (VPB) spin lock. |
| [IoRegisterFsRegistrationChangeMountAware function](nf-ntifs-ioregisterfsregistrationchangemountaware.md) | The IoRegisterFsRegistrationChangeMountAware routine registers a file system filter driver's notification routine. This notification routine is called whenever a file system registers or unregisters itself as an active file system. |
| [ExQueryPoolBlockSize function](nf-ntifs-exquerypoolblocksize.md) | TBD |
| [RtlUpcaseUnicodeToOemN function](nf-ntifs-rtlupcaseunicodetooemn.md) | The RtlUpcaseUnicodeToOemN routine translates a given Unicode string into an uppercase OEM string, using the current system OEM code page. |
| [IoCreateStreamFileObjectEx2 function](nf-ntifs-iocreatestreamfileobjectex2.md) | The IoCreateStreamFileObjectEx2 routine creates a new stream file object with create options for a target device object. |
| [KeSetIdealProcessorThread function](nf-ntifs-kesetidealprocessorthread.md) | TBD |
| [SeAuditTransactionStateChange function](nf-ntifs-seaudittransactionstatechange.md) | TBD |
| [RtlUpcaseUnicodeToMultiByteN function](nf-ntifs-rtlupcaseunicodetomultibyten.md) | The RtlUpcaseUnicodeToMultiByteN routine translates the specified Unicode string into a new uppercase character string, using the current system ANSI code page (ACP). The translated string is not necessarily from a multibyte character set. |
| [RtlUnicodeToMultiByteSize function](nf-ntifs-rtlunicodetomultibytesize.md) | The RtlUnicodeToMultiByteSize routine determines the number of bytes that are required to store the multibyte translation for the specified Unicode string. The translation is assumed to use the current system ANSI code page (ACP). |
| [ZwQueryDirectoryFile function](nf-ntifs-zwquerydirectoryfile.md) | The ZwQueryDirectoryFile routine returns various kinds of information about files in the directory specified by a given file handle. |
| [EncryptMessage function](nf-ntifs-encryptmessage.md) | TBD |
| [FsRtlSetupAdvancedHeaderEx function](nf-ntifs-fsrtlsetupadvancedheaderex.md) | The FsRtlSetupAdvancedHeaderEx macro is used by file systems to initialize an FSRTL_ADVANCED_FCB_HEADER structure for use with both stream and file contexts. |
| [PoRegisterDeviceForIdleDetection function](nf-ntifs-poregisterdeviceforidledetection.md) | The PoRegisterDeviceForIdleDetection routine enables or cancels idle detection and sets idle time-out values for a device. |
| [IoStartTimer function](nf-ntifs-iostarttimer.md) | The IoStartTimer routine enables the timer associated with a given device object so the driver-supplied IoTimer routine is called once per second. |
| [FsRtlGetPerStreamContextPointer function](nf-ntifs-fsrtlgetperstreamcontextpointer.md) | The FsRtlGetPerStreamContextPointer macro returns the file system's stream context for a file stream. |
| [NtFsControlFile function](nf-ntifs-ntfscontrolfile.md) | TBD |
| [SetContextAttributesW function](nf-ntifs-setcontextattributesw.md) | TBD |
| [RtlAddAce function](nf-ntifs-rtladdace.md) | The RtlAddAce routine adds one or more access control entries (ACEs) to a specified access control list (ACL). |
| [RtlAllocateAndInitializeSid function](nf-ntifs-rtlallocateandinitializesid.md) | TBD |
| [RtlxUnicodeStringToOemSize function](nf-ntifs-rtlxunicodestringtooemsize.md) | TBD |
| [PoUnregisterSystemState function](nf-ntifs-pounregistersystemstate.md) | The PoUnregisterSystemState routine cancels a system state registration created by PoRegisterSystemState. |
| [CcUnpinDataForThread function](nf-ntifs-ccunpindataforthread.md) | The CcUnpinDataForThread routine releases pages of a cached file whose buffer control block (BCB) was modified by an earlier call to CcSetBcbOwnerPointer. |
| [SeQuerySecurityDescriptorInfo function](nf-ntifs-sequerysecuritydescriptorinfo.md) | The SeQuerySecurityDescriptorInfo routine retrieves a copy of an object's security descriptor. |
| [FsRtlAllocatePoolWithTag function](nf-ntifs-fsrtlallocatepoolwithtag.md) | The FsRtlAllocatePoolWithTag routine allocates pool memory. |
| [SeCreateClientSecurityFromSubjectContext function](nf-ntifs-secreateclientsecurityfromsubjectcontext.md) | The SeCreateClientSecurityFromSubjectContext routine retrieves the access token for a security subject context and uses the result to initialize a security client context with the information needed to call SeImpersonateClientEx. |
| [IoRequestDeviceRemovalForReset function](nf-ntifs-iorequestdeviceremovalforreset.md) | TBD |
| [SeQueryServerSiloToken function](nf-ntifs-sequeryserversilotoken.md) | TBD |
| [SeDeleteClientSecurity function](nf-ntifs-sedeleteclientsecurity.md) | The SeDeleteClientSecurity routine deletes a client security context. |
| [PfxFindPrefix function](nf-ntifs-pfxfindprefix.md) | TBD |
| [KeRemoveQueueEx function](nf-ntifs-keremovequeueex.md) | TBD |
| [CcPurgeCacheSection function](nf-ntifs-ccpurgecachesection~r1.md) | The CcPurgeCacheSection routine purges all or a portion of a cached file from the system cache. |
| [SeSetSecurityDescriptorInfo function](nf-ntifs-sesetsecuritydescriptorinfo.md) | The SeSetSecurityDescriptorInfo routine sets an object's security descriptor. |
| [KeSetKernelStackSwapEnable function](nf-ntifs-kesetkernelstackswapenable.md) | The KeSetKernelStackSwapEnable routine enables and disables swapping of the caller's stack to disk. |
| [NtQuerySecurityObject function](nf-ntifs-ntquerysecurityobject.md) | TBD |
| [PsLookupThreadByThreadId function](nf-ntifs-pslookupthreadbythreadid.md) | The PsLookupThreadByThreadId routine accepts the thread ID of a thread and returns a referenced pointer to the ETHREAD structure of the thread. |
| [RtlDuplicateUnicodeString function](nf-ntifs-rtlduplicateunicodestring.md) | TBD |
| [NtQueryQuotaInformationFile function](nf-ntifs-ntqueryquotainformationfile.md) | TBD |
| [FsRtlInitPerFileObjectContext function](nf-ntifs-fsrtlinitperfileobjectcontext.md) | TBD |
| [RtlCustomCPToUnicodeN function](nf-ntifs-rtlcustomcptounicoden.md) | TBD |
| [IoCheckEaBufferValidity function](nf-ntifs-iocheckeabuffervalidity.md) | The IoCheckEaBufferValidity routine checks whether the specified extended attribute (EA) buffer is valid. |
| [FsRtlIsAnsiCharacterWild function](nf-ntifs-fsrtlisansicharacterwild.md) | The FsRtlIsAnsiCharacterWild macro determines whether an ANSI character is a wildcard character. |
| [NtSetSecurityObject function](nf-ntifs-ntsetsecurityobject.md) | TBD |
| [RtlFillMemoryUlonglong function](nf-ntifs-rtlfillmemoryulonglong.md) | The RtlFillMemoryUlonglong routine fills a given range of memory with one or more repetitions of a given ULONGLONG value. |
| [ChangeAccountPasswordA function](nf-ntifs-changeaccountpassworda.md) | TBD |
| [PsRestoreImpersonation function](nf-ntifs-psrestoreimpersonation.md) | TBD |
| [SeLengthSid function](nf-ntifs-selengthsid.md) | TBD |
| [ObQueryNameString function](nf-ntifs-obquerynamestring.md) | The ObQueryNameString routine supplies the name, if there is one, of a given object to which the caller has a pointer. |
| [RtlOemToUnicodeN function](nf-ntifs-rtloemtounicoden.md) | The RtlOemToUnicodeN routine translates the specified source string into a Unicode string, using the current system OEM code page. |
| [FsRtlCreateSectionForDataScan function](nf-ntifs-fsrtlcreatesectionfordatascan.md) | The FsRtlCreateSectionForDataScan routine creates a section object. |
| [IoCreateStreamFileObjectLite function](nf-ntifs-iocreatestreamfileobjectlite.md) | The IoCreateStreamFileObjectLite routine creates a new stream file object, but does not cause an IRP_MJ_CLEANUP request to be sent to the file system driver stack. |
| [FsRtlSetEcpListIntoIrp function](nf-ntifs-fsrtlsetecplistintoirp.md) | The FsRtlSetEcpListIntoIrp routine attaches an extra create parameter (ECP) context structure list to an IRP_MJ_CREATE operation. |
| [RtlIsPartialPlaceholderFileInfo function](nf-ntifs-rtlispartialplaceholderfileinfo.md) | The RtlIsPartialPlaceholderFileInfo routine determines if a file is a known type of placeholder, based on the information returned by NtQueryInformationFile or NtQueryDirectoryFile. |
| [ZwDuplicateToken function](nf-ntifs-zwduplicatetoken.md) | The ZwDuplicateToken function creates a handle to a new access token that duplicates an existing token. This function can create either a primary token or an impersonation token. |
| [NtSetQuotaInformationFile function](nf-ntifs-ntsetquotainformationfile.md) | TBD |
| [DEVICE_TYPE_FROM_CTL_CODE function](nf-ntifs-device-type-from-ctl-code.md) | TBD |
| [MmFlushImageSection function](nf-ntifs-mmflushimagesection.md) | The MmFlushImageSection routine flushes the image section for a file. |
| [KeReadStateMutant function](nf-ntifs-kereadstatemutant.md) | TBD |
| [IoCheckQuerySetFileInformation function](nf-ntifs-iocheckquerysetfileinformation.md) | TBD |
| [RtlCopyLuid function](nf-ntifs-rtlcopyluid.md) | The RtlCopyLuid routine copies a locally unique identifier (LUID) to a buffer. |
| [FsRtlFreeExtraCreateParameter function](nf-ntifs-fsrtlfreeextracreateparameter.md) | The FsRtlFreeExtraCreateParameter routine frees the memory for an ECP context structure. |
| [RtlTimeToSecondsSince1980 function](nf-ntifs-rtltimetosecondssince1980.md) | The RtlTimeToSecondsSince1980 routine converts a given absolute system time value to the elapsed time, in seconds, since the beginning of 1980. |
| [RtlDowncaseUnicodeString function](nf-ntifs-rtldowncaseunicodestring.md) | The RtlDowncaseUnicodeString routine converts the specified Unicode source string to lowercase. The translation conforms to the current system locale information. |
| [RtlUpcaseUnicodeToCustomCPN function](nf-ntifs-rtlupcaseunicodetocustomcpn.md) | TBD |
| [CcSetFileSizesEx function](nf-ntifs-ccsetfilesizesex.md) | TBD |
| [SeLocateProcessImageName function](nf-ntifs-selocateprocessimagename.md) | TBD |
| [IoSizeOfIrp function](nf-ntifs-iosizeofirp.md) | The IoSizeOfIrp routine determines the size in bytes for an IRP, given the number of stack locations in the IRP. |
| [CcGetDirtyPages function](nf-ntifs-ccgetdirtypages.md) | The CcGetDirtyPages routine searches for dirty pages in all files that match a given log handle. |
| [NtFlushBuffersFileEx function](nf-ntifs-ntflushbuffersfileex.md) | TBD |
| [NtAllocateVirtualMemory function](nf-ntifs-ntallocatevirtualmemory.md) | TBD |
| [SeMarkLogonSessionForTerminationNotification function](nf-ntifs-semarklogonsessionforterminationnotification.md) | The SeMarkLogonSessionForTerminationNotification routine marks a logon session so that the caller's registered callback routine is called when the logon session terminates. |
| [SeQueryAuthenticationIdToken function](nf-ntifs-sequeryauthenticationidtoken.md) | The SeQueryAuthenticationIdToken routine retrieves the authentication ID of an access token. |
| [IsReparseTagMicrosoft function](nf-ntifs-isreparsetagmicrosoft.md) | The IsReparseTagMicrosoft macro determines whether a reparse point tag indicates a Microsoft reparse point. |
| [NtAdjustGroupsToken function](nf-ntifs-ntadjustgroupstoken.md) | TBD |
| [IoStartNextPacket function](nf-ntifs-iostartnextpacket.md) | The IoStartNextPacket routine dequeues the next IRP, if any, from the given device object's associated device queue and calls the driver's StartIo routine. |
| [EnumerateSecurityPackagesW function](nf-ntifs-enumeratesecuritypackagesw.md) | TBD |
| [KeQueryOwnerMutant function](nf-ntifs-kequeryownermutant.md) | TBD |
| [SspiFreeAsyncContext function](nf-ntifs-sspifreeasynccontext.md) | TBD |
| [RtlFreeOemString function](nf-ntifs-rtlfreeoemstring.md) | The RtlFreeOemString routine releases storage that was allocated by any of the Rtl..ToOemString routines. |
| [RtlCompressChunks function](nf-ntifs-rtlcompresschunks.md) | TBD |
| [LsaFreeReturnBuffer function](nf-ntifs-lsafreereturnbuffer.md) | TBD |
| [SeQuerySessionIdTokenEx function](nf-ntifs-sequerysessionidtokenex.md) | TBD |
| [RtlPrefixString function](nf-ntifs-rtlprefixstring.md) | TBD |
| [IoGetFsZeroingOffset function](nf-ntifs-iogetfszeroingoffset~r1.md) | TBD |
| [SeDeleteObjectAuditAlarm function](nf-ntifs-sedeleteobjectauditalarm.md) | The SeDeleteObjectAuditAlarm routine generates audit and alarm messages for an object that is marked for deletion. |
| [RtlCreateServiceSid function](nf-ntifs-rtlcreateservicesid.md) | TBD |
| [SecInvalidateHandle function](nf-ntifs-secinvalidatehandle.md) | TBD |
| [IoGetLowerDeviceObject function](nf-ntifs-iogetlowerdeviceobject.md) | The IoGetLowerDeviceObject routine returns a pointer to the next-lower-level device object on the driver stack. |
| [NtWriteFile function](nf-ntifs-ntwritefile.md) | TBD |
| [RtlReplaceSidInSd function](nf-ntifs-rtlreplacesidinsd.md) | TBD |
| [SspiIsPromptingNeeded function](nf-ntifs-sspiispromptingneeded.md) | TBD |
| [PfxInitialize function](nf-ntifs-pfxinitialize.md) | TBD |
| [QuerySecurityContextToken function](nf-ntifs-querysecuritycontexttoken.md) | TBD |
| [FsRtlInsertPerFileContext function](nf-ntifs-fsrtlinsertperfilecontext.md) | The FsRtlInsertPerFileContext routine associates a FSRTL_PER_FILE_CONTEXT object with a driver-specified context object for a file. |
| [ZwSetVolumeInformationFile function](nf-ntifs-zwsetvolumeinformationfile.md) | The ZwSetVolumeInformationFile routine modifies information about the volume associated with a given file, directory, storage device, or volume. |
| [FsRtlCancellableWaitForMultipleObjects function](nf-ntifs-fsrtlcancellablewaitformultipleobjects.md) | The FsRtlCancellableWaitForMultipleObjects routine executes a cancelable wait operation (a wait that can be terminated) on one or more dispatcher objects. |
| [RtlAppendStringToString function](nf-ntifs-rtlappendstringtostring.md) | The RtlAppendStringToString routine concatenates two counted strings. It copies bytes from the source up to the length of the destination buffer. |
| [SspiFreeAuthIdentity function](nf-ntifs-sspifreeauthidentity.md) | TBD |
| [ZwCreateEvent function](nf-ntifs-zwcreateevent.md) | The ZwCreateEvent routine creates an event object, sets the initial state of the event to the specified value, and opens a handle to the object with the specified desired access. |
| [SeOpenObjectForDeleteAuditAlarm function](nf-ntifs-seopenobjectfordeleteauditalarm.md) | The SeOpenObjectForDeleteAuditAlarm routine generates audit and alarm messages when an attempt is made to open an object for deletion. |
| [NtQueryVirtualMemory function](nf-ntifs-ntqueryvirtualmemory.md) | TBD |
| [PoSetPowerRequest function](nf-ntifs-posetpowerrequest.md) | The PoSetPowerRequest routine increments the count for the specified power request type. |
| [CcGetFileObjectFromSectionPtrs function](nf-ntifs-ccgetfileobjectfromsectionptrs.md) | Given a pointer to the section object pointers for a cached file, the CcGetFileObjectFromSectionPtrs routine returns a pointer to the file object that the cache manager is using for the file. |
| [NtOpenJobObjectToken function](nf-ntifs-ntopenjobobjecttoken.md) | TBD |
| [FsRtlAllocateExtraCreateParameter function](nf-ntifs-fsrtlallocateextracreateparameter.md) | The FsRtlAllocateExtraCreateParameter routine allocates memory for a user-defined extra create parameter (ECP) context structure and generates a pointer to that structure. |
| [NtAccessCheckAndAuditAlarm function](nf-ntifs-ntaccesscheckandauditalarm.md) | TBD |
| [CcCopyReadEx function](nf-ntifs-cccopyreadex.md) | The CcCopyReadEx routine copies data from a cached file to a user buffer. The I/O byte count for the operation is charged to the issuing thread. |
| [ObInsertObject function](nf-ntifs-obinsertobject.md) | TBD |
| [FsRtlCancellableWaitForSingleObject function](nf-ntifs-fsrtlcancellablewaitforsingleobject.md) | The FsRtlCancellableWaitForSingleObject routine executes a cancelable wait operation (a wait that can be terminated) on a dispatcher object. |
| [SspiZeroAuthIdentity function](nf-ntifs-sspizeroauthidentity.md) | TBD |
| [RtlUnicodeToMultiByteN function](nf-ntifs-rtlunicodetomultibyten.md) | The RtlUnicodeToMultiByteN routine translates the specified Unicode string into a new character string, using the current system ANSI code page (ACP). The translated string is not necessarily from a multibyte character set. |
| [FsRtlPrepareToReuseEcp function](nf-ntifs-fsrtlpreparetoreuseecp.md) | The FsRtlPrepareToReuseEcp routine resets an extra create parameter (ECP) context structure, which prepares it for reuse. |
| [FsRtlInitializeExtraCreateParameterList function](nf-ntifs-fsrtlinitializeextracreateparameterlist.md) | The FsRtlInitializeExtraCreateParameterList routine initializes an extra create parameter (ECP) context structure list. |
| [FsRtlRemovePerFileContext function](nf-ntifs-fsrtlremoveperfilecontext.md) | The FsRtlRemovePerFileContext routine returns a pointer to a FSRTL_PER_FILE_CONTEXT object that is associated with a file. |
| [SspiInitializeSecurityContextAsyncW function](nf-ntifs-sspiinitializesecuritycontextasyncw.md) | TBD |
| [FsRtlInitPerFileContext function](nf-ntifs-fsrtlinitperfilecontext.md) | TBD |
| [FsRtlIsAnsiCharacterLegalNtfs function](nf-ntifs-fsrtlisansicharacterlegalntfs.md) | The FsRtlIsAnsiCharacterLegalNtfs macro determines whether an ANSI character is legal for NTFS file names. |
| [FsRtlQueryInformationFile function](nf-ntifs-fsrtlqueryinformationfile.md) | TBD |
| [CcPrepareMdlWrite function](nf-ntifs-ccpreparemdlwrite.md) | The CcPrepareMdlWrite routine provides direct access to cached file memory so that the caller can write data to the file. |
| [FsRtlCompleteRequest function](nf-ntifs-fsrtlcompleterequest.md) | The FsRtlCompleteRequest macro completes an IRP with the specified status. |
| [CcIsFileCached function](nf-ntifs-ccisfilecached.md) | TBD |
| [FsRtlQueryCachedVdl function](nf-ntifs-fsrtlquerycachedvdl.md) | The current valid data length (VDL) for a cached file is retrieved with the FsRtlQueryCachedVdl routine. |
| [SeRegisterLogonSessionTerminatedRoutine function](nf-ntifs-seregisterlogonsessionterminatedroutine.md) | The SeRegisterLogonSessionTerminatedRoutine routine registers a callback routine to be called when a logon session terminates. A logon session terminates when the last token referencing the logon session is deleted. |
| [IoCheckFunctionAccess function](nf-ntifs-iocheckfunctionaccess.md) | TBD |
| [NtSetInformationFile function](nf-ntifs-ntsetinformationfile.md) | TBD |
| [NtFreeVirtualMemory function](nf-ntifs-ntfreevirtualmemory.md) | TBD |
| [RtlUnicodeStringToCountedOemString function](nf-ntifs-rtlunicodestringtocountedoemstring.md) | The RtlUnicodeStringToCountedOemString routine translates the specified Unicode source string into a counted OEM string using the current system OEM code page. |
| [MSV1_0_IUM_SUPPLEMENTAL_CREDENTIAL_SIZE function](nf-ntifs-msv1-0-ium-supplemental-credential-size.md) | TBD |
| [FsRtlLookupPerStreamContextInternal function](nf-ntifs-fsrtllookupperstreamcontextinternal.md) | TBD |
| [CcAsyncCopyRead function](nf-ntifs-ccasynccopyread.md) | TBD |
| [PsGetProcessExitTime function](nf-ntifs-psgetprocessexittime.md) | The PsGetProcessExitTime routine returns the exit time for the current process. |
| [SecIsValidHandle function](nf-ntifs-secisvalidhandle.md) | TBD |
| [SeSetSecurityDescriptorInfoEx function](nf-ntifs-sesetsecuritydescriptorinfoex.md) | The SeSetSecurityDescriptorInfoEx routine modifies an object's security descriptor and specifies whether the object supports automatic inheritance of access control entries (ACE). |
| [RtlDecompressBufferEx2 function](nf-ntifs-rtldecompressbufferex2.md) | The RtlDecompressBufferEx2 function decompresses an entire compressed buffer, using multiple processors where possible. Multiple processor support is only implemented for kernel mode callers. |
| [ObMakeTemporaryObject function](nf-ntifs-obmaketemporaryobject.md) | TBD |
| [RtlUnicodeToCustomCPN function](nf-ntifs-rtlunicodetocustomcpn.md) | TBD |
| [ZwFreeVirtualMemory function](nf-ntifs-zwfreevirtualmemory.md) | The ZwFreeVirtualMemory routine releases, decommits, or both, a region of pages within the virtual address space of a specified process. |
| [LSAP_SE_ADT_PARAMETER_ARRAY_TRUE_SIZE function](nf-ntifs-lsap-se-adt-parameter-array-true-size.md) | TBD |
| [SecLookupAccountName function](nf-ntifs-seclookupaccountname.md) | SecLookupAccountName accepts an account as input and retrieves a security identifier (SID) for the account and the name of the domain on which the account was found. |
| [FsRtlDismountComplete function](nf-ntifs-fsrtldismountcomplete.md) | TBD |
| [FsRtlLookupPerFileContext function](nf-ntifs-fsrtllookupperfilecontext.md) | The FsRtlLookupPerFileContext routine returns a pointer to a FSRTL_PER_FILE_CONTEXT object that is associated with a specified file. |
| [NtQueryInformationFile function](nf-ntifs-ntqueryinformationfile.md) | TBD |
| [SecMakeSPN function](nf-ntifs-secmakespn.md) | SecMakeSPN creates a service provider name string that can be used when communicating with specific security service providers. |
| [RtlConvertSidToUnicodeString function](nf-ntifs-rtlconvertsidtounicodestring.md) | The RtlConvertSidToUnicodeString routine generates a printable Unicode string representation of a security identifier (SID). |
| [CcCopyWriteEx function](nf-ntifs-cccopywriteex.md) | The CcCopyWriteEx routine copies data from a user buffer to a cached file. The I/O byte count for the operation is charged to the issuing thread. |
| [FsRtlIsAnsiCharacterLegalHpfs function](nf-ntifs-fsrtlisansicharacterlegalhpfs.md) | The FsRtlIsAnsiCharacterLegalHpfs macro determines whether an ANSI character is legal for HPFS file names. |
| [IoRegisterFsRegistrationChange function](nf-ntifs-ioregisterfsregistrationchange.md) | The IoRegisterFsRegistrationChange routine registers a file system filter driver's notification routine to be called whenever a file system registers or unregisters itself as an active file system. |
| [IoCheckDesiredAccess function](nf-ntifs-iocheckdesiredaccess.md) | TBD |
| [ZwQueryEaFile function](nf-ntifs-zwqueryeafile.md) | The ZwQueryEaFile routine returns information about extended-attribute (EA) values for a file. |
| [RtlUnicodeStringToOemSize function](nf-ntifs-rtlunicodestringtooemsize.md) | The RtlUnicodeStringToOemSize routine determines the size, in bytes, that a given Unicode string will be after it is translated into an OEM string. |
| [IoSizeOfIrpEx function](nf-ntifs-iosizeofirpex.md) | TBD |
| [PoCallDriver function](nf-ntifs-pocalldriver.md) | The PoCallDriver routine passes a power IRP to the next-lower driver in the device stack. (Windows Server 2003, Windows XP, and Windows 2000 only.). |
| [FsRtlInitPerStreamContext function](nf-ntifs-fsrtlinitperstreamcontext.md) | The FsRtlInitPerStreamContext macro initializes a filter driver context structure. |
| [SspiValidateAuthIdentity function](nf-ntifs-sspivalidateauthidentity.md) | TBD |
| [ZwQueryVolumeInformationFile function](nf-ntifs-zwqueryvolumeinformationfile.md) | The ZwQueryVolumeInformationFile routine retrieves information about the volume associated with a given file, directory, storage device, or volume. |
| [ObQueryObjectAuditingByHandle function](nf-ntifs-obqueryobjectauditingbyhandle.md) | TBD |
| [CompleteAuthToken function](nf-ntifs-completeauthtoken.md) | TBD |
| [RtlQueryThreadPlaceholderCompatibilityMode function](nf-ntifs-rtlquerythreadplaceholdercompatibilitymode.md) | RtlQueryThreadPlaceholderCompatibilityMode is a routine which returns the placeholder compatibility mode for the current thread. |
| [NtSetVolumeInformationFile function](nf-ntifs-ntsetvolumeinformationfile.md) | TBD |
| [PoStartDeviceBusy function](nf-ntifs-postartdevicebusy.md) | The PoStartDeviceBusy routine marks the start of a period of time in which the device is busy. |
| [ZwLockFile function](nf-ntifs-zwlockfile.md) | The ZwLockFile routine requests a byte-range lock for the specified file. |
| [SeUnregisterLogonSessionTerminatedRoutineEx function](nf-ntifs-seunregisterlogonsessionterminatedroutineex.md) | TBD |
| [ObIsKernelHandle function](nf-ntifs-obiskernelhandle.md) | The ObIsKernelHandle routine determines whether the specified handle is a kernel handle. |
| [ImportSecurityContextW function](nf-ntifs-importsecuritycontextw.md) | TBD |
| [RtlDecompressFragmentEx function](nf-ntifs-rtldecompressfragmentex.md) | The RtlDecompressFragmentEx function is used to decompress part of a compressed buffer (that is, a buffer &#0034;fragment&#0034;), using multiple processors where possible. |
| [ZwOpenProcessTokenEx function](nf-ntifs-zwopenprocesstokenex.md) | The ZwOpenProcessTokenEx routine opens the access token associated with a process. |
| [MANDATORY_LEVEL_TO_MANDATORY_RID function](nf-ntifs-mandatory-level-to-mandatory-rid.md) | TBD |
| [IoRetrievePriorityInfo function](nf-ntifs-ioretrievepriorityinfo.md) | TBD |
| [RtlRandomEx function](nf-ntifs-rtlrandomex.md) | The RtlRandomEx routine returns a random number that was generated from a given seed value. |
| [FsRtlMupGetProviderIdFromName function](nf-ntifs-fsrtlmupgetprovideridfromname.md) | The FsRtlMupGetProviderIdFromName routine gets the provider identifier of a network redirector that is registered with the multiple UNC provider (MUP) from the device name of the network redirector. |
| [IoCheckQuerySetVolumeInformation function](nf-ntifs-iocheckquerysetvolumeinformation.md) | TBD |
| [FsRtlIncrementLockRequestsInProgress function](nf-ntifs-fsrtlincrementlockrequestsinprogress.md) | TBD |
| [RtlInitAnsiStringEx function](nf-ntifs-rtlinitansistringex.md) | TBD |
| [RtlIsValidOemCharacter function](nf-ntifs-rtlisvalidoemcharacter.md) | The RtlIsValidOemCharacter routine determines if the specified Unicode character can be mapped to a valid OEM character. |
| [FsRtlLookupPerFileObjectContext function](nf-ntifs-fsrtllookupperfileobjectcontext.md) | For a &#0034;legacy&#0034; file system filter driver, the FsRtlLookupPerFileObjectContext function retrieves context information previously associated with a file object. |
| [RtlAllocateAndInitializeSidEx function](nf-ntifs-rtlallocateandinitializesidex.md) | TBD |
| [CcScheduleReadAheadEx function](nf-ntifs-ccschedulereadaheadex.md) | The CcScheduleReadAheadEx routine performs read-ahead (also called &#0034;lazy read&#0034;) on a cached file. The I/O byte count for the operation is charged to the issuing thread. |
| [CcInitializeCacheMap function](nf-ntifs-ccinitializecachemap.md) | File systems call the CcInitializeCacheMap routine to cache a file. |
| [CcSetDirtyPinnedData function](nf-ntifs-ccsetdirtypinneddata.md) | The CcSetDirtyPinnedData routine marks as dirty the buffer control block (BCB) for a pinned buffer whose contents have been modified. |
| [FreeContextBuffer function](nf-ntifs-freecontextbuffer.md) | TBD |
| [SspiSetAsyncNotifyCallback function](nf-ntifs-sspisetasyncnotifycallback.md) | TBD |
| [SeSetAccessStateGenericMapping function](nf-ntifs-sesetaccessstategenericmapping.md) | The SeSetAccessStateGenericMapping routine sets the generic mapping field of an ACCESS_STATE structure. |
| [SECURITY_SID_SIZE function](nf-ntifs-security-sid-size.md) | TBD |
| [IoIsValidNameGraftingBuffer function](nf-ntifs-ioisvalidnamegraftingbuffer.md) | TBD |
| [FsRtlIsAnsiCharacterLegalNtfsStream function](nf-ntifs-fsrtlisansicharacterlegalntfsstream.md) | The FsRtlIsAnsiCharacterLegalNtfsStream macro determines whether an ANSI character is legal for NTFS stream names. |
| [SetCredentialsAttributesW function](nf-ntifs-setcredentialsattributesw.md) | TBD |
| [GHOSTED_FILE_EXTENTS_OUTPUT_SIZE function](nf-ntifs-ghosted-file-extents-output-size.md) | TBD |
| [IoStopTimer function](nf-ntifs-iostoptimer.md) | The IoStopTimer routine disables the timer for a specified device object so the driver-supplied IoTimer routine is not called. |
| [SspiReinitAsyncContext function](nf-ntifs-sspireinitasynccontext.md) | TBD |
| [ExDisableResourceBoostLite function](nf-ntifs-exdisableresourceboostlite.md) | TBD |
| [FsRtlRegisterFileSystemFilterCallbacks function](nf-ntifs-fsrtlregisterfilesystemfiltercallbacks.md) | File system filter drivers and file systems call the FsRtlRegisterFileSystemFilterCallbacks routine to register notification callback routines to be invoked when the underlying file system performs certain operations. |
| [NtSetInformationThread function](nf-ntifs-ntsetinformationthread.md) | TBD |
| [SeCaptureSubjectContext function](nf-ntifs-secapturesubjectcontext.md) | The SeCaptureSubjectContext routine captures the security context of the calling thread for access validation and auditing. |
| [SeImpersonateClientEx function](nf-ntifs-seimpersonateclientex.md) | The SeImpersonateClientEx routine causes a thread to impersonate a user. |
| [ZwOpenDirectoryObject function](nf-ntifs-zwopendirectoryobject.md) | The ZwOpenDirectoryObject routine opens an existing directory object. |
| [FsRtlRegisterUncProviderEx2 function](nf-ntifs-fsrtlregisteruncproviderex2.md) | TBD |
| [ZwWaitForSingleObject function](nf-ntifs-zwwaitforsingleobject.md) | The ZwWaitForSingleObject routine waits until the specified object attains a state of Signaled. An optional time-out can also be specified. |
| [SeAuditHardLinkCreationWithTransaction function](nf-ntifs-seaudithardlinkcreationwithtransaction.md) | TBD |
| [MmCanFileBeTruncated function](nf-ntifs-mmcanfilebetruncated.md) | The MmCanFileBeTruncated routine checks whether a file can be truncated. |
| [ExAdjustLookasideDepth function](nf-ntifs-exadjustlookasidedepth.md) | TBD |
| [RtlSecondsSince1980ToTime function](nf-ntifs-rtlsecondssince1980totime.md) | The RtlSecondsSince1980ToTime routine converts the elapsed time, in seconds, since the beginning of 1980 to an absolute system time value. |
| [CcIsThereDirtyDataEx function](nf-ntifs-ccistheredirtydataex.md) | The CcIsThereDirtyDataEx routine determines whether a volume contains any files that have dirty data in the system cache. |
| [IoUnregisterFileSystem function](nf-ntifs-iounregisterfilesystem.md) | The IoUnregisterFileSystem routine removes a file system's control device object from the global file system queue. |
| [CcDeferWrite function](nf-ntifs-ccdeferwrite.md) | The CcDeferWrite routine defers writing to a cached file. |
| [PoQueryWatchdogTime function](nf-ntifs-poquerywatchdogtime.md) | The PoQueryWatchdogTime routine indicates whether the power manager has enabled a watchdog time-out counter for any power IRP that is currently assigned to the device stack. |
| [IoVerifyVolume function](nf-ntifs-ioverifyvolume.md) | The IoVerifyVolume routine sends a volume verify request to the given removable-media device. |
| [FsRtlGetPerFileContextPointer function](nf-ntifs-fsrtlgetperfilecontextpointer.md) | TBD |
| [NtLockFile function](nf-ntifs-ntlockfile.md) | TBD |
| [RtlFreeSid function](nf-ntifs-rtlfreesid.md) | TBD |
| [SspiCreateAsyncContext function](nf-ntifs-sspicreateasynccontext.md) | TBD |
| [SecMakeSPNEx2 function](nf-ntifs-secmakespnex2.md) | SecMakeSPNEx2 creates a service provider name string that can be used when it communicates with specific security service providers. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_VOLSNAP_FLUSH_AND_HOLD_WRITES IOCTL](ni-ntifs-ioctl-volsnap-flush-and-hold-writes.md) | The IOCTL_VOLSNAP_FLUSH_AND_HOLD_WRITES control code is sent to force a flush of a file system before a volume shadow copy occurs. |
| [IOCTL_REDIR_QUERY_PATH IOCTL](ni-ntifs-ioctl-redir-query-path.md) | The IOCTL_REDIR_QUERY_PATH control code is sent by the multiple UNC provider (MUP) to network redirectors to determine which provider can handle a specific UNC path in a name-based operation, typically an IRP_MJ_CREATE request. |
| [IOCTL_LMR_ARE_FILE_OBJECTS_ON_SAME_SERVER IOCTL](ni-ntifs-ioctl-lmr-are-file-objects-on-same-server.md) | TBD |
| [IOCTL_REDIR_QUERY_PATH_EX IOCTL](ni-ntifs-ioctl-redir-query-path-ex.md) | The IOCTL_REDIR_QUERY_PATH_EX control code is sent by the multiple UNC provider (MUP) on Windows Vista or later to network redirectors to determine which provider can handle a specific UNC path in a name-based operation, typically an IRP_MJ_CREATE request. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [DECRYPT_MESSAGE_FN callback function](nc-ntifs-decrypt-message-fn.md) | TBD |
| [ENCRYPT_MESSAGE_FN callback function](nc-ntifs-encrypt-message-fn.md) | TBD |
| [FREE_CREDENTIALS_HANDLE_FN callback function](nc-ntifs-free-credentials-handle-fn.md) | TBD |
| [PQUERY_LOG_USAGE callback function](nc-ntifs-pquery-log-usage.md) | TBD |
| [ACQUIRE_CREDENTIALS_HANDLE_FN_W callback function](nc-ntifs-acquire-credentials-handle-fn-w.md) | TBD |
| [PASYNC_READ_COMPLETION_CALLBACK callback function](nc-ntifs-pasync-read-completion-callback.md) | TBD |
| [APPLY_CONTROL_TOKEN_FN callback function](nc-ntifs-apply-control-token-fn.md) | TBD |
| [QUERY_CREDENTIALS_ATTRIBUTES_EX_FN_W callback function](nc-ntifs-query-credentials-attributes-ex-fn-w.md) | TBD |
| [PDIRTY_PAGE_ROUTINE callback function](nc-ntifs-pdirty-page-routine.md) | TBD |
| [QUERY_SECURITY_CONTEXT_TOKEN_FN callback function](nc-ntifs-query-security-context-token-fn.md) | TBD |
| [EXPORT_SECURITY_CONTEXT_FN callback function](nc-ntifs-export-security-context-fn.md) | TBD |
| [SspiAsyncNotifyCallback callback function](nc-ntifs-sspiasyncnotifycallback.md) | TBD |
| [QUERY_CONTEXT_ATTRIBUTES_EX_FN_W callback function](nc-ntifs-query-context-attributes-ex-fn-w.md) | TBD |
| [PIO_IRP_EXT_PROCESS_TRACKED_OFFSET_CALLBACK callback function](nc-ntifs-pio-irp-ext-process-tracked-offset-callback.md) | TBD |
| [PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK callback](nc-ntifs-pfsrtl-extra-create-parameter-cleanup-callback.md) | A file system filter driver (legacy filter) or a minifilter driver can register a PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK-typed routine as the filter driver's CleanupCallback callback routine for an extra create parameter (ECP) context structure. |
| [ENUMERATE_SECURITY_PACKAGES_FN_W callback function](nc-ntifs-enumerate-security-packages-fn-w.md) | TBD |
| [INITIALIZE_SECURITY_CONTEXT_FN_W callback function](nc-ntifs-initialize-security-context-fn-w.md) | TBD |
| [POWER_SETTING_CALLBACK callback function](nc-ntifs-power-setting-callback.md) | TBD |
| [PRELEASE_FROM_READ_AHEAD callback function](nc-ntifs-prelease-from-read-ahead.md) | TBD |
| [CHANGE_PASSWORD_FN_W callback function](nc-ntifs-change-password-fn-w.md) | TBD |
| [VERIFY_SIGNATURE_FN callback function](nc-ntifs-verify-signature-fn.md) | TBD |
| [REVERT_SECURITY_CONTEXT_FN callback function](nc-ntifs-revert-security-context-fn.md) | TBD |
| [PACQUIRE_FOR_LAZY_WRITE callback function](nc-ntifs-pacquire-for-lazy-write.md) | TBD |
| [MAKE_SIGNATURE_FN callback function](nc-ntifs-make-signature-fn.md) | TBD |
| [PFS_FILTER_COMPLETION_CALLBACK callback function](nc-ntifs-pfs-filter-completion-callback.md) | TBD |
| [DELETE_SECURITY_CONTEXT_FN callback function](nc-ntifs-delete-security-context-fn.md) | TBD |
| [IMPORT_SECURITY_CONTEXT_FN_W callback function](nc-ntifs-import-security-context-fn-w.md) | TBD |
| [ACCEPT_SECURITY_CONTEXT_FN callback function](nc-ntifs-accept-security-context-fn.md) | TBD |
| [RTL_FREE_STRING_ROUTINE callback function](nc-ntifs-rtl-free-string-routine.md) | TBD |
| [ADD_CREDENTIALS_FN_A callback function](nc-ntifs-add-credentials-fn-a.md) | TBD |
| [RTL_HEAP_COMMIT_ROUTINE callback function](nc-ntifs-rtl-heap-commit-routine.md) | TBD |
| [QUERY_SECURITY_PACKAGE_INFO_FN_W callback function](nc-ntifs-query-security-package-info-fn-w.md) | TBD |
| [PACQUIRE_FOR_READ_AHEAD callback function](nc-ntifs-pacquire-for-read-ahead.md) | TBD |
| [SET_CONTEXT_ATTRIBUTES_FN_W callback function](nc-ntifs-set-context-attributes-fn-w.md) | TBD |
| [PCC_POST_DEFERRED_WRITE callback function](nc-ntifs-pcc-post-deferred-write.md) | TBD |
| [FREE_CONTEXT_BUFFER_FN callback function](nc-ntifs-free-context-buffer-fn.md) | TBD |
| [QUERY_CONTEXT_ATTRIBUTES_FN_W callback function](nc-ntifs-query-context-attributes-fn-w.md) | TBD |
| [PFN_FSRTLTEARDOWNPERSTREAMCONTEXTS callback function](nc-ntifs-pfn-fsrtlteardownperstreamcontexts.md) | TBD |
| [PFLUSH_TO_LSN callback function](nc-ntifs-pflush-to-lsn.md) | TBD |
| [SET_CREDENTIALS_ATTRIBUTES_FN_W callback function](nc-ntifs-set-credentials-attributes-fn-w.md) | TBD |
| [QUERY_CREDENTIALS_ATTRIBUTES_FN_W callback function](nc-ntifs-query-credentials-attributes-fn-w.md) | TBD |
| [INIT_SECURITY_INTERFACE_W callback function](nc-ntifs-init-security-interface-w.md) | TBD |
| [PFS_FILTER_CALLBACK callback function](nc-ntifs-pfs-filter-callback.md) | TBD |
| [COMPLETE_AUTH_TOKEN_FN callback function](nc-ntifs-complete-auth-token-fn.md) | TBD |
| [CHANGE_PASSWORD_FN_A callback function](nc-ntifs-change-password-fn-a.md) | TBD |
| [ADD_CREDENTIALS_FN_W callback function](nc-ntifs-add-credentials-fn-w.md) | TBD |
| [IMPERSONATE_SECURITY_CONTEXT_FN callback function](nc-ntifs-impersonate-security-context-fn.md) | TBD |
| [PRELEASE_FROM_LAZY_WRITE callback function](nc-ntifs-prelease-from-lazy-write.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [FILE_LINK_ENTRY_FULL_ID_INFORMATION structure](ns-ntifs--file-link-entry-full-id-information.md) | TBD |
| [SCRUB_DATA_OUTPUT structure](ns-ntifs--scrub-data-output.md) | TBD |
| [SecPkgContext_Sizes structure](ns-ntifs--secpkgcontext-sizes.md) | TBD |
| [CSV_QUERY_REDIRECT_STATE structure](ns-ntifs--csv-query-redirect-state.md) | TBD |
| [FSRTL_MUP_PROVIDER_INFO_LEVEL_2 structure](ns-ntifs--fsrtl-mup-provider-info-level-2.md) | TBD |
| [TOKEN_SOURCE structure](ns-ntifs--token-source.md) | TOKEN_SOURCE identifies the source of an access token. |
| [QUERY_PATH_RESPONSE structure](ns-ntifs--query-path-response.md) | TBD |
| [SEC_APPLICATION_PROTOCOL_LIST structure](ns-ntifs--sec-application-protocol-list.md) | TBD |
| [MEMORY_RANGE_ENTRY structure](ns-ntifs--memory-range-entry.md) | TBD |
| [FSCTL_QUERY_GHOSTED_FILE_EXTENTS_INPUT_RANGE structure](ns-ntifs--fsctl-query-ghosted-file-extents-input-range.md) | TBD |
| [TXFS_ROLLFORWARD_REDO_INFORMATION structure](ns-ntifs--txfs-rollforward-redo-information.md) | TBD |
| [CSV_SET_HANDLE_PROPERTIES_ECP_CONTEXT structure](ns-ntifs--csv-set-handle-properties-ecp-context.md) | TBD |
| [FS_FILTER_CALLBACK_DATA structure](ns-ntifs--fs-filter-callback-data.md) | TBD |
| [FSCTL_OFFLOAD_WRITE_INPUT structure](ns-ntifs--fsctl-offload-write-input.md) | The FSCTL_OFFLOAD_WRITE_INPUT structure contains the input for the FSCTL_OFFLOAD_WRITE control code request. |
| [PUBLIC_OBJECT_BASIC_INFORMATION structure](ns-ntifs--public-object-basic-information.md) | The PUBLIC_OBJECT_BASIC_INFORMATION structure holds a subset of the full information that is available for an object. |
| [QUERY_FILE_LAYOUT_OUTPUT structure](ns-ntifs--query-file-layout-output.md) | The QUERY_FILE_LAYOUT_OUTPUT structure serves as a header for the file layout entries that are returned from a FSCTL_QUERY_FILE_LAYOUT request. |
| [TXFS_SAVEPOINT_INFORMATION structure](ns-ntifs--txfs-savepoint-information.md) | TBD |
| [sockaddr_storage structure](ns-ntifs-sockaddr-storage.md) | TBD |
| [TXFS_LIST_TRANSACTIONS_ENTRY structure](ns-ntifs--txfs-list-transactions-entry.md) | TBD |
| [LOOKUP_STREAM_FROM_CLUSTER_INPUT structure](ns-ntifs--lookup-stream-from-cluster-input.md) | TBD |
| [MSV1_0_REMOTE_SUPPLEMENTAL_CREDENTIAL structure](ns-ntifs--msv1-0-remote-supplemental-credential.md) | TBD |
| [VIRTUAL_STORAGE_TYPE structure](ns-ntifs--virtual-storage-type.md) | TBD |
| [READ_LIST structure](ns-ntifs--read-list.md) | TBD |
| [REFS_SMR_VOLUME_INFO_OUTPUT structure](ns-ntifs--refs-smr-volume-info-output.md) | The REFS_SMR_VOLUME_INFO_OUTPUT structure describes a Shingled Magnetic Recording (SMR) volume's current state on space and garbage collection activities. |
| [TOKEN_AUDIT_POLICY structure](ns-ntifs--token-audit-policy.md) | TBD |
| [PREFIX_TABLE_ENTRY structure](ns-ntifs--prefix-table-entry.md) | TBD |
| [FILE_ALL_INFORMATION structure](ns-ntifs--file-all-information.md) | The FILE_ALL_INFORMATION structure is a container for several FILE_XXX_INFORMATION structures. |
| [PUBLIC_BCB structure](ns-ntifs--public-bcb.md) | TBD |
| [MSV1_0_IUM_SUPPLEMENTAL_CREDENTIAL structure](ns-ntifs--msv1-0-ium-supplemental-credential.md) | TBD |
| [SEC_SRTP_MASTER_KEY_IDENTIFIER structure](ns-ntifs--sec-srtp-master-key-identifier.md) | TBD |
| [SecPkgContext_PasswordExpiry structure](ns-ntifs--secpkgcontext-passwordexpiry.md) | TBD |
| [FILE_OBJECTID_INFORMATION structure](ns-ntifs--file-objectid-information.md) | The FILE_OBJECTID_INFORMATION structure is used to query for object ID information for the files in a directory on an NTFS volume. |
| [PNTFS_EXTENDED_VOLUME_DATA structure](ns-ntifs-pntfs-extended-volume-data.md) | TBD |
| [TXFS_START_RM_INFORMATION structure](ns-ntifs--txfs-start-rm-information.md) | TBD |
| [GET_FILTER_FILE_IDENTIFIER_INPUT structure](ns-ntifs--get-filter-file-identifier-input.md) | TBD |
| [SecPkgContext_CredInfo structure](ns-ntifs--secpkgcontext-credinfo.md) | TBD |
| [FILE_LEVEL_TRIM_OUTPUT structure](ns-ntifs--file-level-trim-output.md) | The FILE_LEVEL_TRIM_OUTPUT structure contains the results of a trim operation performed by an FSCTL_FILE_LEVEL_TRIM request. |
| [FILE_LINK_ENTRY_INFORMATION structure](ns-ntifs--file-link-entry-information.md) | The FILE_LINK_ENTRY_INFORMATION structure describes a single NTFS hard link to an existing file. |
| [TOKEN_GROUPS_AND_PRIVILEGES structure](ns-ntifs--token-groups-and-privileges.md) | TOKEN_GROUPS_AND_PRIVILEGES contains information about the group security identifiers (SIDs) and privileges in an access token. |
| [RETRIEVAL_POINTER_BASE structure](ns-ntifs--retrieval-pointer-base.md) | TBD |
| [WIM_PROVIDER_OVERLAY_ENTRY structure](ns-ntifs--wim-provider-overlay-entry.md) | Contains the a Windows Image Format (WIM) file configuration information for a data source entry. It is used to identify specific WIM file names and indices that supply data to externally backed files on a volume. |
| [SD_CHANGE_MACHINE_SID_OUTPUT structure](ns-ntifs--sd-change-machine-sid-output.md) | TBD |
| [TOKEN_STATISTICS structure](ns-ntifs--token-statistics.md) | TOKEN_STATISTICS contains information about an access token. A driver can retrieve this information by calling SeQueryInformationToken or ZwQueryInformationToken. |
| [SD_ENUM_SDS_INPUT structure](ns-ntifs--sd-enum-sds-input.md) | TBD |
| [PUSN_RECORD_V3 structure](ns-ntifs-pusn-record-v3.md) | TBD |
| [STREAM_LAYOUT_ENTRY structure](ns-ntifs--stream-layout-entry.md) | TBD |
| [FILE_FS_VOLUME_FLAGS_INFORMATION structure](ns-ntifs--file-fs-volume-flags-information.md) | TBD |
| [FSCTL_QUERY_REGION_INFO_OUTPUT structure](ns-ntifs--fsctl-query-region-info-output.md) | TBD |
| [FILE_PREFETCH_EX structure](ns-ntifs--file-prefetch-ex.md) | TBD |
| [PUSN_RECORD_COMMON_HEADER structure](ns-ntifs-pusn-record-common-header.md) | TBD |
| [FILE_PREFETCH structure](ns-ntifs--file-prefetch.md) | TBD |
| [REFS_DEALLOCATE_RANGES_RANGE structure](ns-ntifs--refs-deallocate-ranges-range.md) | TBD |
| [MSV1_0_SUPPLEMENTAL_CREDENTIAL_V3 structure](ns-ntifs--msv1-0-supplemental-credential-v3.md) | TBD |
| [OPEN_REPARSE_LIST structure](ns-ntifs--open-reparse-list.md) | Points to a list of OPEN_REPARSE_LIST_ENTRY structures that specify the tag and possibly GUID that should be opened directly without returning STATUS_REPARSE. |
| [SECURITY_OBJECT_AI_PARAMS structure](ns-ntifs--security-object-ai-params.md) | TBD |
| [PFIND_BY_SID_OUTPUT structure](ns-ntifs-pfind-by-sid-output.md) | TBD |
| [PREFS_VOLUME_DATA_BUFFER structure](ns-ntifs-prefs-volume-data-buffer.md) | TBD |
| [ENCRYPTION_BUFFER structure](ns-ntifs--encryption-buffer.md) | TBD |
| [IRP structure](ns-ntifs--irp.md) | TBD |
| [WOF_EXTERNAL_FILE_ID structure](ns-ntifs--wof-external-file-id.md) | TBD |
| [FILE_PIPE_ASSIGN_EVENT_BUFFER structure](ns-ntifs--file-pipe-assign-event-buffer.md) | TBD |
| [FILE_FS_CONTROL_INFORMATION structure](ns-ntifs--file-fs-control-information.md) | The FILE_FS_CONTROL_INFORMATION structure is used to query or set control information for the files in a directory. |
| [SYSTEM_AUDIT_ACE structure](ns-ntifs--system-audit-ace.md) | The SYSTEM_AUDIT_ACE structure defines an access-control entry (ACE) for the system access-control list (ACL) specifying what types of access cause system-level notifications. |
| [TOKEN_MANDATORY_POLICY structure](ns-ntifs--token-mandatory-policy.md) | TBD |
| [ACE_HEADER structure](ns-ntifs--ace-header.md) | The ACE_HEADER structure describes the type and size of an access-control entry (ACE). |
| [FILE_NETWORK_PHYSICAL_NAME_INFORMATION structure](ns-ntifs--file-network-physical-name-information.md) | Contains the full UNC physical pathname for a file or directory on a remote file share. |
| [NETWORK_APP_INSTANCE_EA structure](ns-ntifs--network-app-instance-ea.md) | TBD |
| [FSCTL_QUERY_REGION_INFO_INPUT structure](ns-ntifs--fsctl-query-region-info-input.md) | TBD |
| [FILE_LINKS_FULL_ID_INFORMATION structure](ns-ntifs--file-links-full-id-information.md) | TBD |
| [PREFETCH_OPEN_ECP_CONTEXT structure](ns-ntifs--prefetch-open-ecp-context.md) | The PREFETCH_OPEN_ECP_CONTEXT structure communicates whether the prefetcher performs a given open request on a file. |
| [SID structure](ns-ntifs--sid.md) | TBD |
| [SYSTEM_MANDATORY_LABEL_ACE structure](ns-ntifs--system-mandatory-label-ace.md) | TBD |
| [SecPkgContext_DceInfo structure](ns-ntifs--secpkgcontext-dceinfo.md) | TBD |
| [SecPkgCredentials_KdcProxySettingsW structure](ns-ntifs--secpkgcredentials-kdcproxysettingsw.md) | TBD |
| [ACCESS_DENIED_ACE structure](ns-ntifs--access-denied-ace.md) | The ACCESS_DENIED_ACE structure defines an access-control entry (ACE) for the discretionary access-control list (DACL) controlling access to an object. |
| [SE_ACCESS_REPLY structure](ns-ntifs--se-access-reply.md) | TBD |
| [FILE_SET_SPARSE_BUFFER structure](ns-ntifs--file-set-sparse-buffer.md) | TBD |
| [FILE_ID_EXTD_BOTH_DIR_INFORMATION structure](ns-ntifs--file-id-extd-both-dir-information.md) | The FILE_ID_EXTD_BOTH_DIR_INFORMATION structure is used to query file reference number information for the files in a directory. |
| [SE_SID structure](ns-ntifs--se-sid.md) | The SE_SID union holds the maximum-sized valid Security Identifier (SID). The structure occupies 68-bytes and is suitable for stack allocation. |
| [CSV_NAMESPACE_INFO structure](ns-ntifs--csv-namespace-info.md) | TBD |
| [DEVICE_HANDLER_OBJECT structure](ns-ntifs--device-handler-object.md) | TBD |
| [FILE_SYSTEM_RECOGNITION_INFORMATION structure](ns-ntifs--file-system-recognition-information.md) | TBD |
| [SCRUB_DATA_INPUT structure](ns-ntifs--scrub-data-input.md) | TBD |
| [ECP_HEADER structure](ns-ntifs--ecp-header~r1.md) | TBD |
| [FSRTL_COMMON_FCB_HEADER structure](ns-ntifs--fsrtl-common-fcb-header.md) | Do not use the FSRTL_COMMON_FCB_HEADER structure outside of the FSRTL_ADVANCED_FCB_HEADER structure. |
| [CLUSTER_RANGE structure](ns-ntifs--cluster-range.md) | TBD |
| [FILE_ID_128 structure](ns-ntifs--file-id-128.md) | TBD |
| [SID_AND_ATTRIBUTES_HASH structure](ns-ntifs--sid-and-attributes-hash.md) | TBD |
| [LOOKUP_STREAM_FROM_CLUSTER_OUTPUT structure](ns-ntifs--lookup-stream-from-cluster-output.md) | TBD |
| [FSCTL_UNMAP_SPACE_INPUT_BUFFER structure](ns-ntifs--fsctl-unmap-space-input-buffer.md) | TBD |
| [FILE_PIPE_CREATE_SYMLINK_INPUT structure](ns-ntifs--file-pipe-create-symlink-input.md) | TBD |
| [FILE_LAYOUT_ENTRY structure](ns-ntifs--file-layout-entry.md) | TBD |
| [OBJECT_TYPE_LIST structure](ns-ntifs--object-type-list.md) | TBD |
| [FILE_ACCESS_INFORMATION structure](ns-ntifs--file-access-information.md) | The FILE_ACCESS_INFORMATION structure is used to query for or set the access rights of a file. |
| [FILE_MAKE_COMPATIBLE_BUFFER structure](ns-ntifs--file-make-compatible-buffer.md) | TBD |
| [FILE_QUERY_ON_DISK_VOL_INFO_BUFFER structure](ns-ntifs--file-query-on-disk-vol-info-buffer.md) | TBD |
| [RKF_BYPASS_ECP_CONTEXT structure](ns-ntifs--rkf-bypass-ecp-context.md) | TBD |
| [FILE_REFERENCE_RANGE structure](ns-ntifs--file-reference-range.md) | TBD |
| [FILE_PIPE_EVENT_BUFFER structure](ns-ntifs--file-pipe-event-buffer.md) | TBD |
| [DUPLICATE_EXTENTS_DATA32 structure](ns-ntifs--duplicate-extents-data32.md) | TBD |
| [MSV1_0_SUBAUTH_LOGON structure](ns-ntifs--msv1-0-subauth-logon.md) | TBD |
| [FSCTL_GHOST_FILE_EXTENTS_INPUT_BUFFER structure](ns-ntifs--fsctl-ghost-file-extents-input-buffer.md) | TBD |
| [PNTFS_FILE_RECORD_INPUT_BUFFER structure](ns-ntifs-pntfs-file-record-input-buffer.md) | TBD |
| [PREAD_USN_JOURNAL_DATA_V1 structure](ns-ntifs-pread-usn-journal-data-v1.md) | TBD |
| [NETWORK_OPEN_ECP_CONTEXT_V0 structure](ns-ntifs--network-open-ecp-context-v0.md) | The NETWORK_OPEN_ECP_CONTEXT_V0 structure is used to interpret network ECP contexts on files. |
| [FSRTL_MUP_PROVIDER_INFO_LEVEL_1 structure](ns-ntifs--fsrtl-mup-provider-info-level-1.md) | TBD |
| [LOOKUP_STREAM_FROM_CLUSTER_ENTRY structure](ns-ntifs--lookup-stream-from-cluster-entry.md) | TBD |
| [KINTERRUPT structure](ns-ntifs--kinterrupt.md) | TBD |
| [FILE_ALLOCATION_INFORMATION structure](ns-ntifs--file-allocation-information.md) | The FILE_ALLOCATION_INFORMATION structure is used to set the allocation size for a file. |
| [BUS_HANDLER structure](ns-ntifs--bus-handler.md) | TBD |
| [FILE_COMPLETION_INFORMATION structure](ns-ntifs--file-completion-information.md) | The FILE_COMPLETION_INFORMATION structure contains the port handle and key for an I/O completion port created for a file handle. |
| [FSRTL_PER_FILEOBJECT_CONTEXT structure](ns-ntifs--fsrtl-per-fileobject-context.md) | The opaque FSRTL_PER_FILEOBJECT_CONTEXT structure is used by the operating system to track file system filter-driver-defined context information structures for a file object. |
| [CSV_MGMT_LOCK structure](ns-ntifs--csv-mgmt-lock.md) | TBD |
| [SECURITY_CLIENT_CONTEXT structure](ns-ntifs--security-client-context.md) | TBD |
| [CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE structure](ns-ntifs--claim-security-attribute-octet-string-value.md) | TBD |
| [FILE_PIPE_CLIENT_PROCESS_BUFFER structure](ns-ntifs--file-pipe-client-process-buffer.md) | TBD |
| [SecPkgContext_SessionKey structure](ns-ntifs--secpkgcontext-sessionkey.md) | TBD |
| [FILE_ZERO_DATA_INFORMATION_EX structure](ns-ntifs--file-zero-data-information-ex.md) | Contains a range of a file to set to zeros. |
| [TOKEN_PRIVILEGES structure](ns-ntifs--token-privileges.md) | TOKEN_PRIVILEGES contains information about a set of privileges for an access token. |
| [REPARSE_DATA_BUFFER structure](ns-ntifs--reparse-data-buffer.md) | The REPARSE_DATA_BUFFER structure contains reparse point data for a Microsoft reparse point. |
| [FILE_QUOTA_INFORMATION structure](ns-ntifs--file-quota-information.md) | The FILE_QUOTA_INFORMATION structure is used to query or set per-user quota information for each of the files in a directory. |
| [PATHNAME_BUFFER structure](ns-ntifs--pathname-buffer.md) | TBD |
| [MSV1_0_ENUMUSERS_RESPONSE structure](ns-ntifs--msv1-0-enumusers-response.md) | TBD |
| [SD_GLOBAL_CHANGE_OUTPUT structure](ns-ntifs--sd-global-change-output.md) | TBD |
| [FILE_PIPE_LOCAL_INFORMATION structure](ns-ntifs--file-pipe-local-information.md) | The FILE_PIPE_LOCAL_INFORMATION structure contains information about the local end of a named pipe. |
| [TOKEN_USER_CLAIMS structure](ns-ntifs--token-user-claims.md) | TBD |
| [TXFS_WRITE_BACKUP_INFORMATION structure](ns-ntifs--txfs-write-backup-information.md) | TBD |
| [CC_FILE_SIZES structure](ns-ntifs--cc-file-sizes.md) | TBD |
| [DUPLICATE_EXTENTS_DATA structure](ns-ntifs--duplicate-extents-data.md) | TBD |
| [WIM_PROVIDER_REMOVE_OVERLAY_INPUT structure](ns-ntifs--wim-provider-remove-overlay-input.md) | A Windows Image File (WIM) data source to remove from the WIM provider is specified in the WIM_PROVIDER_REMOVE_OVERLAY_INPUT structure. |
| [PCREATE_USN_JOURNAL_DATA structure](ns-ntifs-pcreate-usn-journal-data.md) | TBD |
| [SecHandle structure](ns-ntifs--sechandle.md) | TBD |
| [STREAMS_QUERY_PARAMETERS_OUTPUT_BUFFER structure](ns-ntifs--streams-query-parameters-output-buffer.md) | TBD |
| [IO_PRIORITY_INFO structure](ns-ntifs--io-priority-info.md) | The IO_PRIORITY_INFO structure is used to hold thread priority information. |
| [FILE_REGION_OUTPUT structure](ns-ntifs--file-region-output.md) | TBD |
| [PLEX_READ_DATA_REQUEST structure](ns-ntifs--plex-read-data-request.md) | TBD |
| [CSV_QUERY_FILE_REVISION structure](ns-ntifs--csv-query-file-revision.md) | TBD |
| [ECP_LIST structure](ns-ntifs--ecp-list~r1.md) | TBD |
| [MSV1_0_LM20_CHALLENGE_RESPONSE structure](ns-ntifs--msv1-0-lm20-challenge-response.md) | TBD |
| [WIM_PROVIDER_EXTERNAL_INFO structure](ns-ntifs--wim-provider-external-info.md) | The WIM_PROVIDER_EXTERNAL_INFO structure holds the identifier and status information for the Windows Image File (WIM) external backing provider. |
| [TOKEN_ACCESS_INFORMATION structure](ns-ntifs--token-access-information.md) | TBD |
| [MSV1_0_ENUMUSERS_REQUEST structure](ns-ntifs--msv1-0-enumusers-request.md) | TBD |
| [PUSN_RECORD_UNION structure](ns-ntifs-pusn-record-union.md) | TBD |
| [FILE_ALLOCATED_RANGE_BUFFER structure](ns-ntifs--file-allocated-range-buffer.md) | TBD |
| [CSV_QUERY_FILE_REVISION_FILE_ID_128 structure](ns-ntifs--csv-query-file-revision-file-id-128.md) | TBD |
| [MSV1_0_GETUSERINFO_REQUEST structure](ns-ntifs--msv1-0-getuserinfo-request.md) | TBD |
| [ACCESS_ALLOWED_ACE structure](ns-ntifs--access-allowed-ace.md) | The ACCESS_ALLOWED_ACE structure defines an access-control entry (ACE) for the discretionary access-control list (DACL) that controls access to an object. |
| [FILE_RENAME_INFORMATION structure](ns-ntifs--file-rename-information.md) | The FILE_RENAME_INFORMATION structure is used to rename a file. |
| [SecPkgContext_UserFlags structure](ns-ntifs--secpkgcontext-userflags.md) | TBD |
| [TXFS_LIST_TRANSACTIONS structure](ns-ntifs--txfs-list-transactions.md) | TBD |
| [FILE_PIPE_WAIT_FOR_BUFFER structure](ns-ntifs--file-pipe-wait-for-buffer.md) | TBD |
| [FILE_REGION_INFO structure](ns-ntifs--file-region-info.md) | TBD |
| [SYSTEM_ALARM_ACE structure](ns-ntifs--system-alarm-ace.md) | TBD |
| [CACHE_UNINITIALIZE_EVENT structure](ns-ntifs--cache-uninitialize-event.md) | TBD |
| [CONTAINER_VOLUME_STATE structure](ns-ntifs--container-volume-state.md) | TBD |
| [CSV_QUERY_MDS_PATH structure](ns-ntifs--csv-query-mds-path.md) | TBD |
| [TOKEN_PRIMARY_GROUP structure](ns-ntifs--token-primary-group.md) | TOKEN_PRIMARY_GROUP specifies a group security identifier (SID) for an access token. |
| [SECURITY_FUNCTION_TABLE_W structure](ns-ntifs--security-function-table-w.md) | TBD |
| [FSCTL_QUERY_GHOSTED_FILE_EXTENTS_OUTPUT structure](ns-ntifs--fsctl-query-ghosted-file-extents-output.md) | TBD |
| [TXFS_TRANSACTION_ACTIVE_INFO structure](ns-ntifs--txfs-transaction-active-info.md) | TBD |
| [CSV_QUERY_VETO_FILE_DIRECT_IO_OUTPUT structure](ns-ntifs--csv-query-veto-file-direct-io-output.md) | TBD |
| [WIM_PROVIDER_ADD_OVERLAY_INPUT structure](ns-ntifs--wim-provider-add-overlay-input.md) | A new Windows Image File (WIM) data source is added to the WIM provider with the WIM_PROVIDER_ADD_OVERLAY_INPUT structure. |
| [FS_FILTER_CALLBACKS structure](ns-ntifs--fs-filter-callbacks.md) | TBD |
| [MSV1_0_GETUSERINFO_RESPONSE structure](ns-ntifs--msv1-0-getuserinfo-response.md) | TBD |
| [SD_ENUM_SDS_ENTRY structure](ns-ntifs--sd-enum-sds-entry.md) | TBD |
| [SYSTEM_SCOPED_POLICY_ID_ACE structure](ns-ntifs--system-scoped-policy-id-ace.md) | The SYSTEM_SCOPED_POLICY_ID_ACE structure defines an access-control entry (ACE) for the system access-control list (ACL) specifying rights for a scoped policy identifer. |
| [WIM_PROVIDER_UPDATE_OVERLAY_INPUT structure](ns-ntifs--wim-provider-update-overlay-input.md) | A current Windows Image File (WIM) data source is updated with a new WIM file using the FSCTL_UPDATE_OVERLAY control request with a WIM_PROVIDER_UPDATE_OVERLAY_INPUT structure. |
| [EXTENT_READ_CACHE_INFO_BUFFER structure](ns-ntifs--extent-read-cache-info-buffer.md) | TBD |
| [PEB structure](ns-ntifs--peb.md) | TBD |
| [CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1 structure](ns-ntifs--claim-security-attribute-relative-v1.md) | TBD |
| [MSV1_0_SUPPLEMENTAL_CREDENTIAL structure](ns-ntifs--msv1-0-supplemental-credential.md) | TBD |
| [SecBufferDesc structure](ns-ntifs--secbufferdesc.md) | TBD |
| [PMOVE_FILE_DATA structure](ns-ntifs-pmove-file-data.md) | TBD |
| [GHOSTED_FILE_EXTENT structure](ns-ntifs--ghosted-file-extent.md) | TBD |
| [OPEN_REPARSE_LIST_ENTRY structure](ns-ntifs--open-reparse-list-entry.md) | TBD |
| [FILE_MAILSLOT_QUERY_INFORMATION structure](ns-ntifs--file-mailslot-query-information.md) | The FILE_MAILSLOT_QUERY_INFORMATION structure contains information about a mailslot. |
| [FILE_ID_EXTD_DIR_INFORMATION structure](ns-ntifs--file-id-extd-dir-information.md) | TBD |
| [SCRUB_PARITY_EXTENT_DATA structure](ns-ntifs--scrub-parity-extent-data.md) | TBD |
| [EXTENDED_ENCRYPTED_DATA_INFO structure](ns-ntifs--extended-encrypted-data-info.md) | TBD |
| [FSCTL_SET_INTEGRITY_INFORMATION_BUFFER_EX structure](ns-ntifs--fsctl-set-integrity-information-buffer-ex.md) | TBD |
| [MSV1_0_LM20_LOGON structure](ns-ntifs--msv1-0-lm20-logon.md) | TBD |
| [STREAM_INFORMATION_ENTRY structure](ns-ntifs--stream-information-entry.md) | TBD |
| [RTL_HEAP_PARAMETERS structure](ns-ntifs--rtl-heap-parameters.md) | TBD |
| [FILE_LINK_INFORMATION structure](ns-ntifs--file-link-information.md) | The FILE_LINK_INFORMATION structure is used to create an NTFS hard link to an existing file. |
| [SecPkgContext_AuthorityW structure](ns-ntifs--secpkgcontext-authorityw.md) | TBD |
| [STORAGE_QUERY_DEPENDENT_VOLUME_RESPONSE structure](ns-ntifs--storage-query-dependent-volume-response.md) | TBD |
| [MM_PREFETCH_FLAGS structure](ns-ntifs--mm-prefetch-flags.md) | TBD |
| [PUSN_JOURNAL_DATA_V2 structure](ns-ntifs-pusn-journal-data-v2.md) | TBD |
| [FILE_DESIRED_STORAGE_CLASS_INFORMATION structure](ns-ntifs--file-desired-storage-class-information.md) | TBD |
| [CSV_DOWN_LEVEL_OPEN_ECP_CONTEXT structure](ns-ntifs--csv-down-level-open-ecp-context.md) | TBD |
| [NETWORK_OPEN_ECP_CONTEXT structure](ns-ntifs--network-open-ecp-context.md) | The NETWORK_OPEN_ECP_CONTEXT structure is used to interpret network ECP contexts on files. |
| [FILE_STORAGE_TIER_REGION structure](ns-ntifs--file-storage-tier-region.md) | TBD |
| [PSTARTING_LCN_INPUT_BUFFER_EX structure](ns-ntifs-pstarting-lcn-input-buffer-ex.md) | TBD |
| [MSV1_0_LM20_CHALLENGE_REQUEST structure](ns-ntifs--msv1-0-lm20-challenge-request.md) | TBD |
| [FILE_PIPE_PEEK_BUFFER structure](ns-ntifs--file-pipe-peek-buffer.md) | TBD |
| [TOKEN_USER structure](ns-ntifs--token-user.md) | TOKEN_USER identifies the user associated with an access token. |
| [MOVE_FILE_DATA32 structure](ns-ntifs--move-file-data32.md) | TBD |
| [OBJECT_TYPE structure](ns-ntifs--object-type.md) | TBD |
| [STREAMS_ASSOCIATE_ID_INPUT_BUFFER structure](ns-ntifs--streams-associate-id-input-buffer.md) | TBD |
| [TXFS_QUERY_RM_INFORMATION structure](ns-ntifs--txfs-query-rm-information.md) | TBD |
| [MSV1_0_LM20_LOGON_PROFILE structure](ns-ntifs--msv1-0-lm20-logon-profile.md) | TBD |
| [RETRIEVAL_POINTERS_BUFFER structure](ns-ntifs-retrieval-pointers-buffer.md) | TBD |
| [FILE_SET_DEFECT_MGMT_BUFFER structure](ns-ntifs--file-set-defect-mgmt-buffer.md) | TBD |
| [MEMORY_BASIC_INFORMATION structure](ns-ntifs--memory-basic-information.md) | Contains information about a range of pages in the virtual address space of a process. |
| [SE_ADT_PARAMETER_ARRAY_EX structure](ns-ntifs--se-adt-parameter-array-ex.md) | TBD |
| [WRITE_USN_REASON_INPUT structure](ns-ntifs--write-usn-reason-input.md) | TBD |
| [ECP_OPEN_PARAMETERS structure](ns-ntifs--ecp-open-parameters.md) | The ECP_OPEN_PARAMETERS structure allows a caller to specify the purpose of opening of a file without interfering with existing handles and/or oplocks on the file. |
| [QUERY_BAD_RANGES_INPUT_RANGE structure](ns-ntifs--query-bad-ranges-input-range.md) | TBD |
| [KPROCESS structure](ns-ntifs--kprocess.md) | TBD |
| [UNICODE_PREFIX_TABLE structure](ns-ntifs--unicode-prefix-table.md) | TBD |
| [VIRTUALIZATION_INSTANCE_INFO_INPUT structure](ns-ntifs--virtualization-instance-info-input.md) | TBD |
| [FILE_LAYOUT_NAME_ENTRY structure](ns-ntifs--file-layout-name-entry.md) | TBD |
| [FILE_COMPRESSION_INFORMATION structure](ns-ntifs--file-compression-information.md) | The FILE_COMPRESSION_INFORMATION structure describes the state of a compressed data buffer. |
| [ECP_HEADER structure](ns-ntifs--ecp-header.md) | TBD |
| [SecPkgInfoW structure](ns-ntifs--secpkginfow.md) | TBD |
| [REPAIR_COPIES_INPUT structure](ns-ntifs--repair-copies-input.md) | TBD |
| [CLAIM_SECURITY_ATTRIBUTES_INFORMATION structure](ns-ntifs--claim-security-attributes-information.md) | TBD |
| [QUERY_BAD_RANGES_OUTPUT structure](ns-ntifs--query-bad-ranges-output.md) | TBD |
| [CSV_IS_OWNED_BY_CSVFS structure](ns-ntifs--csv-is-owned-by-csvfs.md) | TBD |
| [SE_ADT_OBJECT_TYPE structure](ns-ntifs--se-adt-object-type.md) | TBD |
| [CREATE_REDIRECTION_ECP_CONTEXT structure](ns-ntifs--create-redirection-ecp-context.md) | TBD |
| [FILE_PIPE_REMOTE_INFORMATION structure](ns-ntifs--file-pipe-remote-information.md) | The FILE_PIPE_REMOTE_INFORMATION structure contains information about the remote end of a named pipe. |
| [SET_DAX_ALLOC_ALIGNMENT_HINT_INPUT structure](ns-ntifs--set-dax-alloc-alignment-hint-input.md) | This structure is for internal use only and should not be called from your code. |
| [SecPkgContext_NegoPackageInfo structure](ns-ntifs--secpkgcontext-negopackageinfo.md) | TBD |
| [PNTFS_FILE_RECORD_OUTPUT_BUFFER structure](ns-ntifs-pntfs-file-record-output-buffer.md) | TBD |
| [TXFS_LIST_TRANSACTION_LOCKED_FILES structure](ns-ntifs--txfs-list-transaction-locked-files.md) | TBD |
| [SYSTEM_ACCESS_FILTER_ACE structure](ns-ntifs--system-access-filter-ace.md) | TBD |
| [FILE_ID_FULL_DIR_INFORMATION structure](ns-ntifs--file-id-full-dir-information.md) | The FILE_ID_FULL_DIR_INFORMATION structure is used to query detailed information for the files in a directory. |
| [SecPkgContext_CredentialNameW structure](ns-ntifs--secpkgcontext-credentialnamew.md) | TBD |
| [SecPkgContext_ProtoInfoW structure](ns-ntifs--secpkgcontext-protoinfow.md) | TBD |
| [FILE_PIPE_CLIENT_PROCESS_BUFFER_EX structure](ns-ntifs--file-pipe-client-process-buffer-ex.md) | TBD |
| [PMFT_ENUM_DATA_V1 structure](ns-ntifs-pmft-enum-data-v1.md) | TBD |
| [CC_ASYNC_READ_CONTEXT structure](ns-ntifs--cc-async-read-context.md) | TBD |
| [FILE_MOVE_CLUSTER_INFORMATION structure](ns-ntifs--file-move-cluster-information.md) | TBD |
| [SEC_CHANNEL_BINDINGS structure](ns-ntifs--sec-channel-bindings.md) | TBD |
| [MSV1_0_GETCHALLENRESP_REQUEST_V1 structure](ns-ntifs--msv1-0-getchallenresp-request-v1.md) | TBD |
| [TOKEN_SID_INFORMATION structure](ns-ntifs--token-sid-information.md) | TBD |
| [REPARSE_INDEX_KEY structure](ns-ntifs--reparse-index-key.md) | TBD |
| [VCN_RANGE_INPUT_BUFFER structure](ns-ntifs--vcn-range-input-buffer.md) | TBD |
| [TOKEN_ELEVATION structure](ns-ntifs--token-elevation.md) | TBD |
| [FILE_FS_DRIVER_PATH_INFORMATION structure](ns-ntifs--file-fs-driver-path-information.md) | The FILE_FS_DRIVER_PATH_INFORMATION structure is used to query whether a given driver is in the I/O path for a file system volume. |
| [IO_IRP_EXT_TRACK_OFFSET_HEADER structure](ns-ntifs--io-irp-ext-track-offset-header~r1.md) | TBD |
| [SecPkgCredentials_SSIProviderW structure](ns-ntifs--secpkgcredentials-ssiproviderw.md) | TBD |
| [FILE_REPARSE_POINT_INFORMATION structure](ns-ntifs--file-reparse-point-information.md) | The FILE_REPARSE_POINT_INFORMATION structure is used to query for information about a reparse point. |
| [KQUEUE structure](ns-ntifs--kqueue.md) | TBD |
| [CONTAINER_ROOT_INFO_INPUT structure](ns-ntifs--container-root-info-input.md) | TBD |
| [SI_COPYFILE structure](ns-ntifs--si-copyfile.md) | TBD |
| [GENERATE_NAME_CONTEXT structure](ns-ntifs--generate-name-context.md) | TBD |
| [SecPkgContext_NegotiationInfoW structure](ns-ntifs--secpkgcontext-negotiationinfow.md) | TBD |
| [FSRTL_PER_FILE_CONTEXT structure](ns-ntifs--fsrtl-per-file-context.md) | A legacy file system filter driver can use a FSRTL_PER_FILE_CONTEXT structure to associate driver-specific context information to an open file. |
| [KAPC_STATE structure](ns-ntifs--kapc-state.md) | TBD |
| [FS_FILTER_SECTION_SYNC_OUTPUT structure](ns-ntifs--fs-filter-section-sync-output.md) | The FS_FILTER_SECTION_SYNC_OUTPUT structure contains information describing the attributes of the section that is being created. |
| [SecPkgContext_NegoKeys structure](ns-ntifs--secpkgcontext-negokeys.md) | TBD |
| [SEC_SRTP_PROTECTION_PROFILES structure](ns-ntifs--sec-srtp-protection-profiles.md) | TBD |
| [VIRTUALIZATION_INSTANCE_INFO_OUTPUT structure](ns-ntifs--virtualization-instance-info-output.md) | TBD |
| [PVOLUME_BITMAP_BUFFER structure](ns-ntifs-pvolume-bitmap-buffer.md) | TBD |
| [FILE_DIRECTORY_INFORMATION structure](ns-ntifs--file-directory-information.md) | The FILE_DIRECTORY_INFORMATION structure is used to query detailed information for the files in a directory. |
| [SD_GLOBAL_CHANGE_INPUT structure](ns-ntifs--sd-global-change-input.md) | TBD |
| [SE_SECURITY_DESCRIPTOR structure](ns-ntifs--se-security-descriptor.md) | TBD |
| [TXFS_CREATE_MINIVERSION_INFO structure](ns-ntifs--txfs-create-miniversion-info.md) | TBD |
| [SE_AUDIT_INFO structure](ns-ntifs--se-audit-info.md) | TBD |
| [IO_TIMER structure](ns-ntifs--io-timer.md) | TBD |
| [MSV1_0_INTERACTIVE_LOGON structure](ns-ntifs--msv1-0-interactive-logon.md) | TBD |
| [FILE_TYPE_NOTIFICATION_INPUT structure](ns-ntifs--file-type-notification-input.md) | TBD |
| [FILE_MODE_INFORMATION structure](ns-ntifs--file-mode-information.md) | The FILE_MODE_INFORMATION structure is used to query or set the access mode of a file. |
| [FILE_BOTH_DIR_INFORMATION structure](ns-ntifs--file-both-dir-information.md) | The FILE_BOTH_DIR_INFORMATION structure is used to query detailed information for the files in a directory. |
| [SecPkgContext_PackageInfoW structure](ns-ntifs--secpkgcontext-packageinfow.md) | TBD |
| [SecPkgContext_KeyInfoW structure](ns-ntifs--secpkgcontext-keyinfow.md) | TBD |
| [ACL structure](ns-ntifs--acl.md) | TBD |
| [FSRTL_PER_STREAM_CONTEXT structure](ns-ntifs--fsrtl-per-stream-context.md) | The FSRTL_PER_STREAM_CONTEXT structure contains context information that a file system filter driver maintains about a file stream. |
| [ACCESS_REASONS structure](ns-ntifs--access-reasons.md) | TBD |
| [TOKEN_GROUPS structure](ns-ntifs--token-groups.md) | TOKEN_GROUPS contains information about the group security identifiers (SID) in an access token. |
| [FILE_FS_PERSISTENT_VOLUME_INFORMATION structure](ns-ntifs--file-fs-persistent-volume-information.md) | The FILE_FS_PERSISTENT_VOLUME_INFORMATION structure is used to control persistent settings for a file system volume. Persistent settings persist on a file system volume between reboots of the computer. |
| [FILE_PIPE_INFORMATION structure](ns-ntifs--file-pipe-information.md) | The FILE_PIPE_INFORMATION structure contains information about a named pipe that is not specific to the local or the remote end of the pipe. |
| [FILESYSTEM_STATISTICS structure](ns-ntifs--filesystem-statistics.md) | TBD |
| [FILE_STANDARD_LINK_INFORMATION structure](ns-ntifs--file-standard-link-information.md) | TBD |
| [SECURITY_USER_DATA structure](ns-ntifs--security-user-data.md) | TBD |
| [CSV_QUERY_FILE_REVISION_ECP_CONTEXT structure](ns-ntifs--csv-query-file-revision-ecp-context.md) | TBD |
| [TXFS_READ_BACKUP_INFORMATION_OUT structure](ns-ntifs--txfs-read-backup-information-out.md) | TBD |
| [SEC_WINNT_AUTH_IDENTITY_EX2 structure](ns-ntifs--sec-winnt-auth-identity-ex2.md) | TBD |
| [FILE_GET_EA_INFORMATION structure](ns-ntifs--file-get-ea-information.md) | The FILE_GET_EA_INFORMATION structure is used to query for extended-attribute (EA) information. |
| [WIM_PROVIDER_SUSPEND_OVERLAY_INPUT structure](ns-ntifs--wim-provider-suspend-overlay-input.md) | A Windows Image File (WIM) data source to suspend from the WIM provider is specified in the WIM_PROVIDER_SUSPEND_OVERLAY_INPUT structure. |
| [LINK_TRACKING_INFORMATION structure](ns-ntifs--link-tracking-information.md) | TBD |
| [IO_DEVICE_HINT_ECP_CONTEXT structure](ns-ntifs--io-device-hint-ecp-context.md) | TBD |
| [ENCRYPTED_DATA_INFO structure](ns-ntifs--encrypted-data-info.md) | TBD |
| [TXFS_GET_METADATA_INFO_OUT structure](ns-ntifs--txfs-get-metadata-info-out.md) | TBD |
| [PMFT_ENUM_DATA_V0 structure](ns-ntifs-pmft-enum-data-v0.md) | TBD |
| [PUSN_RECORD_V4 structure](ns-ntifs-pusn-record-v4.md) | TBD |
| [FILE_TRACKING_INFORMATION structure](ns-ntifs--file-tracking-information.md) | TBD |
| [FILE_ID_GLOBAL_TX_DIR_INFORMATION structure](ns-ntifs--file-id-global-tx-dir-information.md) | The FILE_ID_GLOBAL_TX_DIR_INFORMATION structure contains information about transactional visibility for the files in a directory. |
| [SecBuffer structure](ns-ntifs--secbuffer.md) | TBD |
| [MSV1_0_GETCHALLENRESP_RESPONSE structure](ns-ntifs--msv1-0-getchallenresp-response.md) | TBD |
| [NETWORK_APP_INSTANCE_VERSION_ECP_CONTEXT structure](ns-ntifs--network-app-instance-version-ecp-context.md) | TBD |
| [CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE structure](ns-ntifs--claim-security-attribute-fqbn-value.md) | TBD |
| [SecPkgContext_Flags structure](ns-ntifs--secpkgcontext-flags.md) | TBD |
| [REQUEST_RAW_ENCRYPTED_DATA structure](ns-ntifs--request-raw-encrypted-data.md) | TBD |
| [FSCTL_QUERY_STORAGE_CLASSES_OUTPUT structure](ns-ntifs--fsctl-query-storage-classes-output.md) | TBD |
| [PUSN_RECORD_V2 structure](ns-ntifs-pusn-record-v2.md) | TBD |
| [SecPkgContext_NegoStatus structure](ns-ntifs--secpkgcontext-negostatus.md) | TBD |
| [CSV_QUERY_FILE_REVISION_ECP_CONTEXT_FILE_ID_128 structure](ns-ntifs--csv-query-file-revision-ecp-context-file-id-128.md) | TBD |
| [PMARK_HANDLE_INFO structure](ns-ntifs-pmark-handle-info.md) | TBD |
| [CSV_CONTROL_PARAM structure](ns-ntifs--csv-control-param.md) | TBD |
| [COMPRESSED_DATA_INFO structure](ns-ntifs--compressed-data-info.md) | TBD |
| [MSV1_0_NTLM3_RESPONSE structure](ns-ntifs--msv1-0-ntlm3-response.md) | TBD |
| [SecPkgContext_NamesW structure](ns-ntifs--secpkgcontext-namesw.md) | TBD |
| [CACHE_MANAGER_CALLBACKS structure](ns-ntifs--cache-manager-callbacks.md) | TBD |
| [FSCTL_OFFLOAD_WRITE_OUTPUT structure](ns-ntifs--fsctl-offload-write-output.md) | The FSCTL_OFFLOAD_WRITE_OUTPUT structure contains the output for the FSCTL_OFFLOAD_WRITE control code request. |
| [REPARSE_GUID_DATA_BUFFER structure](ns-ntifs--reparse-guid-data-buffer.md) | The REPARSE_GUID_DATA_BUFFER structure contains reparse point data for a reparse point. |
| [SecPkgCredentials_NamesW structure](ns-ntifs--secpkgcredentials-namesw.md) | TBD |
| [FILE_ID_BOTH_DIR_INFORMATION structure](ns-ntifs--file-id-both-dir-information.md) | The FILE_ID_BOTH_DIR_INFORMATION structure is used to query file reference number information for the files in a directory. |
| [PUSN_RANGE_TRACK_OUTPUT structure](ns-ntifs-pusn-range-track-output.md) | TBD |
| [DUPLICATE_EXTENTS_DATA_EX structure](ns-ntifs--duplicate-extents-data-ex.md) | TBD |
| [PDELETE_USN_JOURNAL_DATA structure](ns-ntifs-pdelete-usn-journal-data.md) | TBD |
| [SET_PURGE_FAILURE_MODE_INPUT structure](ns-ntifs--set-purge-failure-mode-input.md) | TBD |
| [SspiAsyncContext structure](ns-ntifs--sspiasynccontext.md) | TBD |
| [TOKEN_LINKED_TOKEN structure](ns-ntifs--token-linked-token.md) | TBD |
| [FILE_OBJECTID_BUFFER structure](ns-ntifs--file-objectid-buffer.md) | TBD |
| [FSCTL_UNMAP_SPACE_OUTPUT structure](ns-ntifs--fsctl-unmap-space-output.md) | TBD |
| [BOOT_AREA_INFO structure](ns-ntifs--boot-area-info.md) | The BOOT_AREA_INFO structure contains the output for the FSCTL_GET_BOOT_AREA_INFO control code. |
| [REQUEST_OPLOCK_INPUT_BUFFER structure](ns-ntifs--request-oplock-input-buffer.md) | TBD |
| [FILE_ID_INFORMATION structure](ns-ntifs--file-id-information.md) | TBD |
| [SECURITY_DESCRIPTOR structure](ns-ntifs--security-descriptor.md) | The SECURITY_DESCRIPTOR structure specifies the security information that is associated with an object. For more information, see the reference page for SECURITY_DESCRIPTOR in the Installable File System documentation. |
| [FILE_NOTIFY_INFORMATION structure](ns-ntifs--file-notify-information.md) | TBD |
| [MSV1_0_GETCHALLENRESP_REQUEST structure](ns-ntifs--msv1-0-getchallenresp-request.md) | TBD |
| [SE_ADT_ACCESS_REASON structure](ns-ntifs--se-adt-access-reason.md) | TBD |
| [SEC_WINNT_AUTH_IDENTITY_EXW structure](ns-ntifs--sec-winnt-auth-identity-exw.md) | TBD |
| [READ_AHEAD_PARAMETERS structure](ns-ntifs--read-ahead-parameters.md) | TBD |
| [REMOTE_LINK_TRACKING_INFORMATION_ structure](ns-ntifs--remote-link-tracking-information-.md) | TBD |
| [QUERY_PATH_REQUEST structure](ns-ntifs--query-path-request.md) | TBD |
| [PSTARTING_LCN_INPUT_BUFFER structure](ns-ntifs-pstarting-lcn-input-buffer.md) | TBD |
| [STORAGE_QUERY_DEPENDENT_VOLUME_LEV1_ENTRY structure](ns-ntifs--storage-query-dependent-volume-lev1-entry.md) | TBD |
| [SE_ACCESS_REQUEST structure](ns-ntifs--se-access-request.md) | TBD |
| [SE_EXPORTS structure](ns-ntifs--se-exports.md) | TBD |
| [TOKEN_BNO_ISOLATION_INFORMATION structure](ns-ntifs--token-bno-isolation-information.md) | TBD |
| [WOF_EXTERNAL_INFO structure](ns-ntifs--wof-external-info.md) | The WOF_EXTERNAL_INFO structure identifies a file backing provider and the overlay service version it supports. |
| [FILE_FS_DATA_COPY_INFORMATION structure](ns-ntifs--file-fs-data-copy-information.md) | TBD |
| [STREAM_EXTENT_ENTRY structure](ns-ntifs--stream-extent-entry.md) | TBD |
| [STREAMS_QUERY_ID_OUTPUT_BUFFER structure](ns-ntifs--streams-query-id-output-buffer.md) | TBD |
| [SHRINK_VOLUME_INFORMATION structure](ns-ntifs--shrink-volume-information.md) | TBD |
| [MSV1_0_AV_PAIR structure](ns-ntifs--msv1-0-av-pair.md) | TBD |
| [SCRUB_PARITY_EXTENT structure](ns-ntifs--scrub-parity-extent.md) | TBD |
| [PUSN_JOURNAL_DATA_V0 structure](ns-ntifs-pusn-journal-data-v0.md) | TBD |
| [FILE_LINKS_INFORMATION structure](ns-ntifs--file-links-information.md) | The FILE_LINKS_INFORMATION structure is used to query NTFS hard links to an existing file. |
| [RETRIEVAL_POINTERS_AND_REFCOUNT_BUFFER structure](ns-ntifs-retrieval-pointers-and-refcount-buffer.md) | TBD |
| [REFS_DEALLOCATE_RANGES_INPUT_BUFFER structure](ns-ntifs--refs-deallocate-ranges-input-buffer.md) | TBD |
| [SRV_OPEN_ECP_CONTEXT structure](ns-ntifs--srv-open-ecp-context.md) | The SRV_OPEN_ECP_CONTEXT structure is used by a server to conditionally open files in response to client requests. |
| [FILE_REGION_INPUT structure](ns-ntifs--file-region-input.md) | TBD |
| [TXFS_MODIFY_RM structure](ns-ntifs--txfs-modify-rm.md) | TBD |
| [CSV_QUERY_VOLUME_REDIRECT_STATE structure](ns-ntifs--csv-query-volume-redirect-state.md) | TBD |
| [FILE_LEVEL_TRIM structure](ns-ntifs--file-level-trim.md) | The FILE_LEVEL_TRIM structure contains an array of byte ranges to trim for a file. |
| [FILE_REMOTE_PROTOCOL_INFORMATION structure](ns-ntifs--file-remote-protocol-information.md) | TBD |
| [NTFS_STATISTICS_EX structure](ns-ntifs--ntfs-statistics-ex.md) | TBD |
| [QUERY_BAD_RANGES_OUTPUT_RANGE structure](ns-ntifs--query-bad-ranges-output-range.md) | TBD |
| [FILE_FULL_DIR_INFORMATION structure](ns-ntifs--file-full-dir-information.md) | The FILE_FULL_DIR_INFORMATION structure is used to query detailed information for the files in a directory. |
| [NTFS_STATISTICS structure](ns-ntifs--ntfs-statistics.md) | TBD |
| [FILE_TIMESTAMPS structure](ns-ntifs--file-timestamps.md) | The FILE_TIMESTAMPS structure specifies the last recorded instance of specific actions on a file. |
| [FILESYSTEM_STATISTICS_EX structure](ns-ntifs--filesystem-statistics-ex.md) | TBD |
| [FILE_PROVIDER_EXTERNAL_INFO_V0 structure](ns-ntifs--file-provider-external-info-v0.md) | TBD |
| [QUERY_FILE_LAYOUT_INPUT structure](ns-ntifs--query-file-layout-input.md) | The QUERY_FILE_LAYOUT_INPUT structure selects which file layout entries are returned from a FSCTL_QUERY_FILE_LAYOUT request. |
| [SD_QUERY_STATS_OUTPUT structure](ns-ntifs--sd-query-stats-output.md) | TBD |
| [PREFIX_TABLE structure](ns-ntifs--prefix-table.md) | TBD |
| [FS_FILTER_PARAMETERS structure](ns-ntifs--fs-filter-parameters.md) | TBD |
| [FILE_QUERY_SPARING_BUFFER structure](ns-ntifs--file-query-sparing-buffer.md) | TBD |
| [FILE_STORAGE_TIER structure](ns-ntifs--file-storage-tier.md) | TBD |
| [STORAGE_QUERY_DEPENDENT_VOLUME_LEV2_ENTRY structure](ns-ntifs--storage-query-dependent-volume-lev2-entry.md) | TBD |
| [MSV1_0_INTERACTIVE_PROFILE structure](ns-ntifs--msv1-0-interactive-profile.md) | TBD |
| [FSCTL_OFFLOAD_READ_OUTPUT structure](ns-ntifs--fsctl-offload-read-output.md) | The FSCTL_OFFLOAD_READ_OUTPUT structure contains the output for the FSCTL_OFFLOAD_READ control code request. |
| [EXFAT_STATISTICS structure](ns-ntifs--exfat-statistics.md) | TBD |
| [FILE_ZERO_DATA_INFORMATION structure](ns-ntifs--file-zero-data-information.md) | Contains a range of a file to set to zeros. |
| [PBULK_SECURITY_TEST_DATA structure](ns-ntifs-pbulk-security-test-data.md) | TBD |
| [NETWORK_OPEN_ECP_CONTEXT structure](ns-ntifs--network-open-ecp-context~r1.md) | The NETWORK_OPEN_ECP_CONTEXT structure is used to interpret network ECP contexts on files. |
| [NETWORK_APP_INSTANCE_ECP_CONTEXT structure](ns-ntifs--network-app-instance-ecp-context.md) | The NETWORK_APP_INSTANCE_ECP_CONTEXT structure is an Extra Create Parameter (ECP) and contains an application instance identifier to associate with a file. |
| [SecPkgCredentials_Cert structure](ns-ntifs--secpkgcredentials-cert.md) | TBD |
| [FSRTL_ADVANCED_FCB_HEADER structure](ns-ntifs--fsrtl-advanced-fcb-header.md) | The FSRTL_ADVANCED_FCB_HEADER structure contains context information that a file system maintains about a file. |
| [PHYSICAL_MEMORY_DESCRIPTOR structure](ns-ntifs--physical-memory-descriptor.md) | TBD |
| [CONTAINER_ROOT_INFO_OUTPUT structure](ns-ntifs--container-root-info-output.md) | TBD |
| [SE_ADT_PARAMETER_ARRAY structure](ns-ntifs--se-adt-parameter-array.md) | TBD |
| [SEC_DTLS_MTU structure](ns-ntifs--sec-dtls-mtu.md) | TBD |
| [SD_CHANGE_MACHINE_SID_INPUT structure](ns-ntifs--sd-change-machine-sid-input.md) | TBD |
| [SD_ENUM_SDS_OUTPUT structure](ns-ntifs--sd-enum-sds-output.md) | TBD |
| [MSV1_0_S4U_LOGON structure](ns-ntifs--msv1-0-s4u-logon.md) | TBD |
| [SEC_PRESHAREDKEY_IDENTITY structure](ns-ntifs--sec-presharedkey-identity.md) | TBD |
| [FSCTL_QUERY_FAT_BPB_BUFFER structure](ns-ntifs--fsctl-query-fat-bpb-buffer.md) | TBD |
| [TXFS_LIST_TRANSACTION_LOCKED_FILES_ENTRY structure](ns-ntifs--txfs-list-transaction-locked-files-entry.md) | TBD |
| [TXFS_GET_TRANSACTED_VERSION structure](ns-ntifs--txfs-get-transacted-version.md) | TBD |
| [SECURITY_DESCRIPTOR_RELATIVE structure](ns-ntifs--security-descriptor-relative.md) | TBD |
| [FILE_EA_INFORMATION structure](ns-ntifs--file-ea-information.md) | The FILE_EA_INFORMATION structure is used to query for the size of the extended attributes (EA) for a file. |
| [REPAIR_COPIES_OUTPUT structure](ns-ntifs--repair-copies-output.md) | TBD |
| [FILE_STREAM_INFORMATION structure](ns-ntifs--file-stream-information.md) | The FILE_STREAM_INFORMATION structure is used to enumerate the streams for a file. |
| [FILE_NOTIFY_EXTENDED_INFORMATION structure](ns-ntifs--file-notify-extended-information.md) | TBD |
| [PUSN_TRACK_MODIFIED_RANGES structure](ns-ntifs-pusn-track-modified-ranges.md) | TBD |
| [WOF_VERSION_INFO structure](ns-ntifs--wof-version-info.md) | The WOF_VERSION_INFO structure contains the version corresponding to the driver supporting a given provider. |
| [STORAGE_QUERY_DEPENDENT_VOLUME_REQUEST structure](ns-ntifs--storage-query-dependent-volume-request.md) | TBD |
| [REQUEST_OPLOCK_OUTPUT_BUFFER structure](ns-ntifs--request-oplock-output-buffer.md) | TBD |
| [SEC_WINNT_AUTH_IDENTITY_W structure](ns-ntifs--sec-winnt-auth-identity-w.md) | TBD |
| [VOLUME_REFS_INFO_BUFFER structure](ns-ntifs--volume-refs-info-buffer.md) | TBD |
| [PSTARTING_VCN_INPUT_BUFFER structure](ns-ntifs-pstarting-vcn-input-buffer.md) | TBD |
| [SecPkgContext_StreamSizes structure](ns-ntifs--secpkgcontext-streamsizes.md) | TBD |
| [FSCTL_GET_INTEGRITY_INFORMATION_BUFFER structure](ns-ntifs--fsctl-get-integrity-information-buffer.md) | TBD |
| [TOKEN_MANDATORY_LABEL structure](ns-ntifs--token-mandatory-label.md) | TBD |
| [REFS_VOLUME_COUNTER_INFO_INPUT_BUFFER structure](ns-ntifs--refs-volume-counter-info-input-buffer.md) | TBD |
| [PREAD_USN_JOURNAL_DATA_V0 structure](ns-ntifs-pread-usn-journal-data-v0.md) | TBD |
| [QUERY_PATH_REQUEST_EX structure](ns-ntifs--query-path-request-ex.md) | TBD |
| [FILE_PROVIDER_EXTERNAL_INFO_V1 structure](ns-ntifs--file-provider-external-info-v1.md) | TBD |
| [DECRYPTION_STATUS_BUFFER structure](ns-ntifs--decryption-status-buffer.md) | TBD |
| [GET_FILTER_FILE_IDENTIFIER_OUTPUT structure](ns-ntifs--get-filter-file-identifier-output.md) | TBD |
| [QUERY_BAD_RANGES_INPUT structure](ns-ntifs--query-bad-ranges-input.md) | TBD |
| [IO_CREATE_STREAM_FILE_OPTIONS structure](ns-ntifs--io-create-stream-file-options.md) | TBD |
| [FILE_PIPE_SILO_ARRIVAL_INPUT structure](ns-ntifs--file-pipe-silo-arrival-input.md) | TBD |
| [SE_TOKEN_USER structure](ns-ntifs--se-token-user.md) | The SE_TOKEN_USER structure holds the maximum-sized valid user SID that can be returned by SeQueryInformationToken, GetTokenInformation, or ZwQueryInformationToken with the TokenUser information class. This structure is suitable for stack allocation. |
| [TOKEN_OWNER structure](ns-ntifs--token-owner.md) | TOKEN_OWNER contains the default owner security identifier (SID) that will be applied to newly created objects. |
| [CSV_QUERY_MDS_PATH_V2 structure](ns-ntifs--csv-query-mds-path-v2.md) | TBD |
| [SecPkgContext_SubjectAttributes structure](ns-ntifs--secpkgcontext-subjectattributes.md) | TBD |
| [CALLBACK_OBJECT structure](ns-ntifs--callback-object.md) | TBD |
| [TOKEN_ORIGIN structure](ns-ntifs--token-origin.md) | The TOKEN_ORIGIN structure contains information about the origin of the logon session. |
| [SEC_PRESHAREDKEY structure](ns-ntifs--sec-presharedkey.md) | TBD |
| [REFS_SMR_VOLUME_GC_PARAMETERS structure](ns-ntifs--refs-smr-volume-gc-parameters.md) | The REFS_SMR_VOLUME_GC_PARAMETERS structure. |
| [PHYSICAL_EXTENTS_DESCRIPTOR structure](ns-ntifs--physical-extents-descriptor.md) | TBD |
| [SHARED_VIRTUAL_DISK_SUPPORT structure](ns-ntifs--shared-virtual-disk-support.md) | TBD |
| [KTHREAD structure](ns-ntifs--kthread.md) | TBD |
| [FILE_PIPE_DELETE_SYMLINK_INPUT structure](ns-ntifs--file-pipe-delete-symlink-input.md) | TBD |
| [PHYSICAL_MEMORY_RUN structure](ns-ntifs--physical-memory-run.md) | TBD |
| [FILE_NAMES_INFORMATION structure](ns-ntifs--file-names-information.md) | A FILE_NAMES_INFORMATION structure used to query detailed information about the names of files in a directory. |
| [FSCTL_SET_INTEGRITY_INFORMATION_BUFFER structure](ns-ntifs--fsctl-set-integrity-information-buffer.md) | TBD |
| [TOKEN_APPCONTAINER_INFORMATION structure](ns-ntifs--token-appcontainer-information.md) | TBD |
| [SE_ADT_CLAIMS structure](ns-ntifs--se-adt-claims.md) | TBD |
| [FAT_STATISTICS structure](ns-ntifs--fat-statistics.md) | TBD |
| [PMOVE_FILE_RECORD_DATA structure](ns-ntifs-pmove-file-record-data.md) | TBD |
| [PUBLIC_OBJECT_TYPE_INFORMATION structure](ns-ntifs---public-object-type-information.md) | The PUBLIC_OBJECT_TYPE_INFORMATION structure holds the type name of the object. |
| [SID_AND_ATTRIBUTES structure](ns-ntifs--sid-and-attributes.md) | The SID_AND_ATTRIBUTES structure represents a security identifier (SID) and its attributes. SIDs are used to uniquely identify users or groups. |
| [SecPkgContext_Lifespan structure](ns-ntifs--secpkgcontext-lifespan.md) | TBD |
| [FILE_STAT_INFORMATION structure](ns-ntifs--file-stat-information.md) | TBD |
| [SD_QUERY_STATS_INPUT structure](ns-ntifs--sd-query-stats-input.md) | TBD |
| [SE_ADT_PARAMETER_ARRAY_ENTRY structure](ns-ntifs--se-adt-parameter-array-entry.md) | TBD |
| [PUSN_RECORD_EXTENT structure](ns-ntifs-pusn-record-extent.md) | TBD |
| [MSV1_0_CREDENTIAL_KEY structure](ns-ntifs--msv1-0-credential-key.md) | TBD |
| [SYSTEM_PROCESS_TRUST_LABEL_ACE structure](ns-ntifs--system-process-trust-label-ace.md) | Reserved. |
| [ECP_LIST structure](ns-ntifs--ecp-list.md) | TBD |
| [TOKEN_CONTROL structure](ns-ntifs--token-control.md) | The TOKEN_CONTROL structure contains information that identifies an access token. |
| [SYSTEM_RESOURCE_ATTRIBUTE_ACE structure](ns-ntifs--system-resource-attribute-ace.md) | The SYSTEM_RESOURCE_ATTRIBUTE_ACE structure defines an access-control entry (ACE) for the system access-control list (ACL) specifying what rights a particular claim has to a resource. |
| [FILE_INITIATE_REPAIR_OUTPUT_BUFFER structure](ns-ntifs--file-initiate-repair-output-buffer.md) | TBD |
| [SID_IDENTIFIER_AUTHORITY structure](ns-ntifs--sid-identifier-authority.md) | The SID_IDENTIFIER_AUTHORITY structure represents the top-level authority of a security identifier (SID). |
| [PREAD_FILE_USN_DATA structure](ns-ntifs-pread-file-usn-data.md) | TBD |
| [IO_IRP_EXT_TRACK_OFFSET_HEADER structure](ns-ntifs--io-irp-ext-track-offset-header.md) | TBD |
| [PNTFS_VOLUME_DATA_BUFFER structure](ns-ntifs-pntfs-volume-data-buffer.md) | TBD |
| [SEC_APPLICATION_PROTOCOLS structure](ns-ntifs--sec-application-protocols.md) | TBD |
| [FSCTL_OFFLOAD_READ_INPUT structure](ns-ntifs--fsctl-offload-read-input.md) | The FSCTL_OFFLOAD_READ_INPUT structure contains the input for the FSCTL_OFFLOAD_READ control code request. |
| [NFS_OPEN_ECP_CONTEXT structure](ns-ntifs--nfs-open-ecp-context.md) | The NFS_OPEN_ECP_CONTEXT structure is used by the Network File System (NFS) server to open files in response to client requests. |
| [FILE_FS_ATTRIBUTE_INFORMATION structure](ns-ntifs--file-fs-attribute-information.md) | The FILE_FS_ATTRIBUTE_INFORMATION structure is used to query attribute information for a file system. |
| [FILE_GET_QUOTA_INFORMATION structure](ns-ntifs--file-get-quota-information.md) | The FILE_GET_QUOTA_INFORMATION structure is used to query for quota information. |
| [PFIND_BY_SID_DATA structure](ns-ntifs-pfind-by-sid-data.md) | TBD |
| [TOKEN_DEFAULT_DACL structure](ns-ntifs--token-default-dacl.md) | The TOKEN_DEFAULT_DACL structure specifies a discretionary access-control list (DACL). |
| [MSV1_0_SUPPLEMENTAL_CREDENTIAL_V2 structure](ns-ntifs--msv1-0-supplemental-credential-v2.md) | TBD |
| [PUSN_JOURNAL_DATA_V1 structure](ns-ntifs-pusn-journal-data-v1.md) | TBD |
| [CLAIM_SECURITY_ATTRIBUTE_V1 structure](ns-ntifs--claim-security-attribute-v1.md) | TBD |
| [DUPLICATE_EXTENTS_DATA_EX32 structure](ns-ntifs--duplicate-extents-data-ex32.md) | TBD |
| [ATOMIC_CREATE_ECP_CONTEXT structure](ns-ntifs--atomic-create-ecp-context.md) | This structure allows supplemental operations to be performed on a file atomically during create. |
| [FILE_VOLUME_NAME_INFORMATION structure](ns-ntifs--file-volume-name-information.md) | TBD |
| [TOKEN_DEVICE_CLAIMS structure](ns-ntifs--token-device-claims.md) | TBD |
| [FSCTL_QUERY_VOLUME_NUMA_INFO_OUTPUT structure](ns-ntifs--fsctl-query-volume-numa-info-output.md) | TBD |
| [UNICODE_PREFIX_TABLE_ENTRY structure](ns-ntifs--unicode-prefix-table-entry.md) | TBD |
| [FILE_MAILSLOT_SET_INFORMATION structure](ns-ntifs--file-mailslot-set-information.md) | The FILE_MAILSLOT_SET_INFORMATION structure is used to set a value on a mailslot. |
| [FILE_LEVEL_TRIM_RANGE structure](ns-ntifs--file-level-trim-range.md) | Contains the offset and length of a trim range for a file. |
| [PMARK_HANDLE_INFO32 structure](ns-ntifs-pmark-handle-info32.md) | Contains information that is used to mark a specified file or directory, and its update sequence number (USN) change journal record with data about changes. |
| [SecPkgContext_LogoffTime structure](ns-ntifs--secpkgcontext-logofftime.md) | TBD |
| [SEC_NEGOTIATION_INFO structure](ns-ntifs--sec-negotiation-info.md) | TBD |
| [FILE_INTERNAL_INFORMATION structure](ns-ntifs--file-internal-information.md) | The FILE_INTERNAL_INFORMATION structure is used to query for the file system's 8-byte file reference number for a file. |
| [SEC_TOKEN_BINDING structure](ns-ntifs--sec-token-binding.md) | TBD |
| [FILE_LAYOUT_INFO_ENTRY structure](ns-ntifs--file-layout-info-entry.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [FILE_STORAGE_TIER_MEDIA_TYPE enumeration](ne-ntifs--file-storage-tier-media-type.md) | TBD |
| [TOKEN_INFORMATION_CLASS enumeration](ne-ntifs--token-information-class.md) | The TOKEN_INFORMATION_CLASS enumeration type contains values that specify the type of information being assigned to or retrieved from an access token. |
| [SECURITY_LOGON_TYPE enumeration](ne-ntifs--security-logon-type.md) | TBD |
| [CSVFS_DISK_CONNECTIVITY enumeration](ne-ntifs--csvfs-disk-connectivity.md) | TBD |
| [FS_FILTER_SECTION_SYNC_TYPE enumeration](ne-ntifs--fs-filter-section-sync-type.md) | TBD |
| [SECPKG_CRED_CLASS enumeration](ne-ntifs--secpkg-cred-class.md) | TBD |
| [AUDIT_EVENT_TYPE enumeration](ne-ntifs--audit-event-type.md) | TBD |
| [CSV_CONTROL_OP enumeration](ne-ntifs--csv-control-op.md) | TBD |
| [LINK_TRACKING_INFORMATION_TYPE enumeration](ne-ntifs--link-tracking-information-type.md) | TBD |
| [SE_ADT_PARAMETER_TYPE enumeration](ne-ntifs--se-adt-parameter-type.md) | TBD |
| [MSV1_0_LOGON_SUBMIT_TYPE enumeration](ne-ntifs--msv1-0-logon-submit-type.md) | TBD |
| [FILE_STORAGE_TIER_CLASS enumeration](ne-ntifs--file-storage-tier-class.md) | TBD |
| [TOKEN_ELEVATION_TYPE enumeration](ne-ntifs--token-elevation-type.md) | TBD |
| [MEMORY_INFORMATION_CLASS enumeration](ne-ntifs--memory-information-class.md) | Defines classes of memory information that can be retrieved by using the ZwQueryVirtualMemory function. |
| [MMFLUSH_TYPE enumeration](ne-ntifs--mmflush-type.md) | TBD |
| [SHRINK_VOLUME_REQUEST_TYPES enumeration](ne-ntifs--shrink-volume-request-types.md) | TBD |
| [REFS_SMR_VOLUME_GC_ACTION enumeration](ne-ntifs--refs-smr-volume-gc-action.md) | The REFS_SMR_VOLUME_GC_ACTION enum contains the available garbage collection commands for FSCTL_SET_REFS_SMR_VOLUME_GC_PARAMETERS. |
| [CSV_DOWN_LEVEL_FILE_TYPE enumeration](ne-ntifs--csv-down-level-file-type.md) | TBD |
| [NETWORK_OPEN_INTEGRITY_QUALIFIER enumeration](ne-ntifs-network-open-integrity-qualifier.md) | The NETWORK_OPEN_INTEGRITY_QUALIFIER enumeration type contains values that identify the kind of integrity restriction to attach to a file. |
| [REFS_SMR_VOLUME_GC_STATE enumeration](ne-ntifs--refs-smr-volume-gc-state.md) | The REFS_SMR_VOLUME_GC_STATE enum specifies the garbage collection's current state. |
| [SharedVirtualDiskSupportType enumeration](ne-ntifs--sharedvirtualdisksupporttype.md) | TBD |
| [FS_FILTER_STREAM_FO_NOTIFICATION_TYPE enumeration](ne-ntifs--fs-filter-stream-fo-notification-type.md) | TBD |
| [SID_NAME_USE enumeration](ne-ntifs--sid-name-use.md) | The SID_NAME_USE enumeration type contains values that specify the type of a security identifier (SID). |
| [OBJECT_INFORMATION_CLASS enumeration](ne-ntifs--object-information-class.md) | The OBJECT_INFORMATION_CLASS enumeration type represents the type of information to supply about an object. |
| [MSV1_0_PROTOCOL_MESSAGE_TYPE enumeration](ne-ntifs--msv1-0-protocol-message-type.md) | TBD |
| [ACCESS_REASON_TYPE enumeration](ne-ntifs--access-reason-type.md) | TBD |
| [SRV_INSTANCE_TYPE enumeration](ne-ntifs--srv-instance-type.md) | TBD |
| [VIRTUAL_MEMORY_INFORMATION_CLASS enumeration](ne-ntifs--virtual-memory-information-class.md) | TBD |
| [MANDATORY_LEVEL enumeration](ne-ntifs--mandatory-level.md) | TBD |
| [FAST_IO_POSSIBLE enumeration](ne-ntifs--fast-io-possible.md) | TBD |
| [REFS_SMR_VOLUME_GC_METHOD enumeration](ne-ntifs--refs-smr-volume-gc-method.md) | The REFS_SMR_VOLUME_GC_METHOD enum specifies the garbage collection method or strategy for FSCTL_SET_REFS_SMR_VOLUME_GC_PARAMETERS. |
| [MSV1_0_CREDENTIAL_KEY_TYPE enumeration](ne-ntifs--msv1-0-credential-key-type.md) | TBD |
| [SEC_APPLICATION_PROTOCOL_NEGOTIATION_EXT enumeration](ne-ntifs--sec-application-protocol-negotiation-ext.md) | TBD |
| [MSV1_0_AVID enumeration](ne-ntifs-msv1-0-avid.md) | TBD |
| [TOKEN_TYPE enumeration](ne-ntifs--token-type.md) | The TOKEN_TYPE enumeration type contains values that differentiate between a primary token and an impersonation token. |
| [SharedVirtualDiskHandleState enumeration](ne-ntifs--sharedvirtualdiskhandlestate.md) | TBD |
| [FSRTL_CHANGE_BACKING_TYPE enumeration](ne-ntifs--fsrtl-change-backing-type.md) | The FSRTL_CHANGE_BACKING_TYPE enumeration specifies the type of cache or control area that a file object designates. |
| [SE_AUDIT_OPERATION enumeration](ne-ntifs--se-audit-operation.md) | TBD |
| [MSV1_0_PROFILE_BUFFER_TYPE enumeration](ne-ntifs--msv1-0-profile-buffer-type.md) | TBD |
| [NETWORK_OPEN_LOCATION_QUALIFIER enumeration](ne-ntifs-network-open-location-qualifier.md) | The NETWORK_OPEN_LOCATION_QUALIFIER enumeration type contains values that identify the kind of location restriction to attach to a file. |
| [QUERY_FILE_LAYOUT_FILTER_TYPE enumeration](ne-ntifs--query-file-layout-filter-type.md) | TBD |

This header is used in these topics:

- [ifsk](..content/_ifsk)
- [kernel](..content/_kernel)
