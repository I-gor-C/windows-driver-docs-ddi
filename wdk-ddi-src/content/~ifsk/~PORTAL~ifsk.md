# Declarations in the ifsk technology
This technology  contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxpDereferenceAndFinalizeNetFcb function](..\fcb\nf-fcb-rxpdereferenceandfinalizenetfcb.md) | RxpDereferenceAndFinalizeNetFcb decrements the reference count and finalizes an FCB structure. |
| [RxpReferenceNetFcb function](..\fcb\nf-fcb-rxpreferencenetfcb.md) | RxpReferenceNetFcb increments the reference count on an FCB. |
| [RxpTrackDereference function](..\fcb\nf-fcb-rxptrackdereference.md) | RxpTrackDereference is used in checked builds to track requests to dereference SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures in checked builds. A log of these dereference requests can be accessed by the logging system and WMI. |
| [RxCreateVNetRoot function](..\fcb\nf-fcb-rxcreatevnetroot.md) | RxCreateVNetRoot allocates and initializes a NET_ROOT structure and inserts the name into the net name table on the associated device object. |
| [RxCreateNetFcb function](..\fcb\nf-fcb-rxcreatenetfcb.md) | RxCreateNetFCB allocates, initializes, and inserts a new FCB structure into the in-memory data structures for a V_NET_ROOT that this FCB is being opened on. The structure allocated has space for a SRV_OPEN and an FOBX structure. |
| [RxpTrackReference function](..\fcb\nf-fcb-rxptrackreference.md) | RxpTrackReference tracks requests to reference SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures in checked builds. A log of these reference requests can be accessed by the logging system and WMI. |
| [RxFinalizeNetRoot function](..\fcb\nf-fcb-rxfinalizenetroot.md) | RxFinalizeNetRoot finalizes the given NET_ROOT structure. The caller must have an exclusive lock on the netname table associated with the device object. |
| [RxFinalizeNetFobx function](..\fcb\nf-fcb-rxfinalizenetfobx.md) | RxFinalizeNetFOBX finalizes the given FOBX structure. The caller must have an exclusive lock on the FCB associated with FOBX structure. |
| [RxFinalizeVNetRoot function](..\fcb\nf-fcb-rxfinalizevnetroot.md) | RxFinalizeVNetRoot finalizes the given V_NET_ROOT structure. The caller must have an exclusive lock on the netname table associated with the device object. |
| [RxFinalizeSrvOpen function](..\fcb\nf-fcb-rxfinalizesrvopen.md) | RxFinalizeSrvOpen finalizes the given SRV_OPEN structure. The caller must have an exclusive lock on the FCB associated with the SRV_OPEN and either a shared or exclusive lock on the table lock of the NET_ROOT associated with the FCB. |
| [RxCreateSrvCall function](..\fcb\nf-fcb-rxcreatesrvcall.md) | RxCreateSrvCall builds a SRV_CALL structure and inserts the name into the net name table maintained by RDBSS. |
| [RxCreateNetRoot function](..\fcb\nf-fcb-rxcreatenetroot.md) | RxCreateNetRoot allocates and initializes a NET_ROOT structure and inserts the name into the net name table on the associated device object. |
| [RxpDereferenceNetFcb function](..\fcb\nf-fcb-rxpdereferencenetfcb.md) | RxpDereferenceNetFcb decrements the reference count on an FCB structure. |
| [RxFinishFcbInitialization function](..\fcb\nf-fcb-rxfinishfcbinitialization.md) | RxFinishFcbInitialization is used to finish initializing an FCB after the successful completion of a create operation by the network mini-redirector. |
| [RxCreateNetFobx function](..\fcb\nf-fcb-rxcreatenetfobx.md) | RxCreateNetFobx allocates, initializes, and inserts a new file object extension (FOBX) structure into the in-memory data structures for a FCB that this FOBX is being opened on. |
| [RxInferFileType function](..\fcb\nf-fcb-rxinferfiletype.md) | RxInferFileType tries to infer the file type (directory or non-directory) from a member in the RX_CONTEXT structure. |
| [RxCreateSrvOpen function](..\fcb\nf-fcb-rxcreatesrvopen.md) | RxCreateSrvOpen allocates, initializes, and inserts a new SRV_OPEN structure into the in-memory data structures used by RDBSS. If a new structure has to be allocated, it has space for an FOBX structure. |
| [RxFinalizeSrvCall function](..\fcb\nf-fcb-rxfinalizesrvcall.md) | RxFinalizeSrvCall finalizes the given SRV_CALL structure. The caller must have an exclusive lock on the netname table associated with the device object. |
| [RxGetFileSizeWithLock function](..\fcb\nf-fcb-rxgetfilesizewithlock.md) | RxGetFileSizeWithLock gets the file size in the FCB structure using a lock to ensure that the 64-bit value is read consistently. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [FltOplockIsSharedRequest function](..\fltkernel\nf-fltkernel-fltoplockissharedrequest.md) | The FltOplockIsSharedRequest routine determines if a request for an opportunistic lock (oplock) wants a shared oplock. |
| [FltDoCompletionProcessingWhenSafe function](..\fltkernel\nf-fltkernel-fltdocompletionprocessingwhensafe.md) | If it is safe to do so, the FltDoCompletionProcessingWhenSafe function executes a minifilter driver postoperation callback routine. |
| [FltSetVolumeInformation function](..\fltkernel\nf-fltkernel-fltsetvolumeinformation.md) | FltSetVolumeInformation changes various kinds of information about the volume that the given instance is attached to. |
| [FltObjectDereference function](..\fltkernel\nf-fltkernel-fltobjectdereference.md) | The FltObjectDereference routine removes a rundown reference from an opaque filter, instance, or volume pointer. |
| [FltSetInformationFile function](..\fltkernel\nf-fltkernel-fltsetinformationfile.md) | FltSetInformationFile sets information for a given file. |
| [FltQueryVolumeInformationFile function](..\fltkernel\nf-fltkernel-fltqueryvolumeinformationfile.md) | FltQueryVolumeInformationFile retrieves volume information for a given file, directory, storage device, or volume. |
| [FltRollbackComplete function](..\fltkernel\nf-fltkernel-fltrollbackcomplete.md) | The FltRollbackComplete routine acknowledges a TRANSACTION_NOTIFY_ROLLBACK notification. |
| [FltInitializePushLock function](..\fltkernel\nf-fltkernel-fltinitializepushlock.md) | The FltInitializePushLock routine initializes a push lock variable. |
| [FltSetIoPriorityHintIntoThread function](..\fltkernel\nf-fltkernel-fltsetiopriorityhintintothread.md) | The FltSetIoPriorityHintIntoThread routine is used by a minifilter driver to set the IO priority information in a thread. |
| [FltFreeExtraCreateParameter function](..\fltkernel\nf-fltkernel-fltfreeextracreateparameter.md) | The FltFreeExtraCreateParameter routine frees the memory for an ECP context structure. |
| [FltGetFilterInformation function](..\fltkernel\nf-fltkernel-fltgetfilterinformation.md) | The FltGetFilterInformation routine provides information about a minifilter driver. |
| [FltOplockFsctrl function](..\fltkernel\nf-fltkernel-fltoplockfsctrl.md) | The FltOplockFsctrl routine performs various opportunistic lock (oplock) operations on behalf of a minifilter driver. |
| [FltEnumerateInstanceInformationByVolumeName function](..\fltkernel\nf-fltkernel-fltenumerateinstanceinformationbyvolumename.md) | The FltEnumerateInstanceInformationByVolumeName routine provides information about minifilter driver instances and legacy filter drivers that are attached to the volume with the specified name. |
| [FltInsertExtraCreateParameter function](..\fltkernel\nf-fltkernel-fltinsertextracreateparameter.md) | The FltInsertExtraCreateParameter routine inserts an extra create parameter (ECP) context structure into an ECP list. |
| [FltEnlistInTransaction function](..\fltkernel\nf-fltkernel-fltenlistintransaction.md) | The FltEnlistInTransaction routine enlists a minifilter driver in a given transaction. |
| [FltSetSecurityObject function](..\fltkernel\nf-fltkernel-fltsetsecurityobject.md) | FltSetSecurityObject sets an object's security state. |
| [FltDeleteExtraCreateParameterLookasideList function](..\fltkernel\nf-fltkernel-fltdeleteextracreateparameterlookasidelist.md) | The FltDeleteExtraCreateParameterLookasideList routine frees an extra create parameter (ECP) lookaside list. |
| [FltGetUpperInstance function](..\fltkernel\nf-fltkernel-fltgetupperinstance.md) | The FltGetUpperInstance routine returns an opaque instance pointer for the next higher minifilter driver instance, if there is one, that is attached above a given minifilter driver instance on the same volume. |
| [FltPropagateActivityIdToThread function](..\fltkernel\nf-fltkernel-fltpropagateactivityidtothread.md) | The FltPropagateActivityIdToThread routine associates the activity ID from the IRP in the minifilter's callback data with the current thread. |
| [FltGetNewSystemBufferAddress function](..\fltkernel\nf-fltkernel-fltgetnewsystembufferaddress.md) | The FltGetNewSystemBufferAddress function retrieves the AssociatedIrp.SystemBuffer buffer, which the file system has allocated. A minifilter driver's post-callback routine calls this function. |
| [FltGetTransactionContext function](..\fltkernel\nf-fltkernel-fltgettransactioncontext.md) | The FltGetTransactionContext routine retrieves a context that was set for a transaction by a given minifilter driver. |
| [FltReleasePushLock function](..\fltkernel\nf-fltkernel-fltreleasepushlock.md) | The FltReleasePushLock routine releases a specified push lock owned by the current thread. |
| [FltCurrentBatchOplock function](..\fltkernel\nf-fltkernel-fltcurrentbatchoplock.md) | A minifilter driver calls FltCurrentBatchOplock to determine whether there are any batch or filter opportunistic locks (oplocks) on a file. |
| [FltGetDestinationFileNameInformation function](..\fltkernel\nf-fltkernel-fltgetdestinationfilenameinformation.md) | The FltGetDestinationFileNameInformation routine constructs a full destination path name for a file or directory that is being renamed or for which an NTFS hard link is being created. |
| [FltGetFilterFromName function](..\fltkernel\nf-fltkernel-fltgetfilterfromname.md) | The FltGetFilterFromName routine returns an opaque filter pointer for a registered minifilter driver whose name matches the value in the FilterName parameter. |
| [FltFreeSecurityDescriptor function](..\fltkernel\nf-fltkernel-fltfreesecuritydescriptor.md) | FltFreeSecurityDescriptor frees a security descriptor allocated by the FltBuildDefaultSecurityDescriptor routine. |
| [FltGetFileNameInformation function](..\fltkernel\nf-fltkernel-fltgetfilenameinformation.md) | The FltGetFileNameInformation routine returns name information for a file or directory. |
| [FltAcquirePushLockShared function](..\fltkernel\nf-fltkernel-fltacquirepushlockshared.md) | The FltAcquirePushLockShared routine acquires the given push lock for shared access by the calling thread. |
| [FltObjectReference function](..\fltkernel\nf-fltkernel-fltobjectreference.md) | The FltObjectReference routine adds a rundown reference to an opaque filter, instance, or volume pointer. |
| [FltIs32bitProcess function](..\fltkernel\nf-fltkernel-fltis32bitprocess.md) | The FltIs32bitProcess routine checks whether the originator of the current I/O operation is a 32-bit user-mode application. |
| [FltGetRoutineAddress function](..\fltkernel\nf-fltkernel-fltgetroutineaddress.md) | The FltGetRoutineAddress routine returns a pointer to a routine specified by the FltMgrRoutineName parameter. |
| [FltDeleteTransactionContext function](..\fltkernel\nf-fltkernel-fltdeletetransactioncontext.md) | The FltDeleteTransactionContext routine removes a context from a given transaction and marks the context for deletion. |
| [FltCloseCommunicationPort function](..\fltkernel\nf-fltkernel-fltclosecommunicationport.md) | FltCloseCommunicationPort closes a minifilter driver's communication server port. |
| [FltCloseClientPort function](..\fltkernel\nf-fltkernel-fltcloseclientport.md) | FltCloseClientPort closes a communication client port. |
| [FltWriteFileEx function](..\fltkernel\nf-fltkernel-fltwritefileex.md) | FltWriteFileEx is used to write data to an open file, stream, or device. This function extends FltWriteFile to allow the optional use of an MDL for write data instead of a mapped buffer address. |
| [FltDeleteStreamContext function](..\fltkernel\nf-fltkernel-fltdeletestreamcontext.md) | FltDeleteStreamContext removes a context that a given minifilter driver instance has set for a given stream and marks the context for deletion. |
| [FltCreateMailslotFile function](..\fltkernel\nf-fltkernel-fltcreatemailslotfile.md) | Minifilter drivers call FltCreateMailslotFile to create a new pipe or open an existing mailslot. |
| [FltOplockFsctrlEx function](..\fltkernel\nf-fltkernel-fltoplockfsctrlex.md) | The FltOplockFsctrlEx routine performs various opportunistic lock (oplock) operations on behalf of a minifilter driver. |
| [FltDeviceIoControlFile function](..\fltkernel\nf-fltkernel-fltdeviceiocontrolfile.md) | FltDeviceIoControlFile sends a control code directly to a specified device driver, causing the corresponding driver to perform the specified action. |
| [FltGetIoPriorityHint function](..\fltkernel\nf-fltkernel-fltgetiopriorityhint.md) | The FltGetIoPriorityHint routine is used by a minifilter driver to get IO priority information from Callback Data. |
| [FltFreeGenericWorkItem function](..\fltkernel\nf-fltkernel-fltfreegenericworkitem.md) | The FltFreeGenericWorkItem routine frees a work item allocated by the FltAllocateGenericWorkItem routine. |
| [FltIsCallbackDataDirty function](..\fltkernel\nf-fltkernel-fltiscallbackdatadirty.md) | The FltIsCallbackDataDirty routine tests the FLTFL_CALLBACK_DATA_DIRTY flag in a callback data structure. |
| [FltOplockBreakToNone function](..\fltkernel\nf-fltkernel-fltoplockbreaktonone.md) | The FltOplockBreakToNone routine breaks all opportunistic locks (oplocks) immediately without regard for any oplock key. |
| [FltGetIoPriorityHintFromCallbackData function](..\fltkernel\nf-fltkernel-fltgetiopriorityhintfromcallbackdata.md) | The FltGetIoPriorityHintFromCallbackData routine is used by a minifilter driver to get IO priority information from callback data. |
| [FltPurgeFileNameInformationCache function](..\fltkernel\nf-fltkernel-fltpurgefilenameinformationcache.md) | FltPurgeFileNameInformationCache purges from the Filter Manager's name cache all file name information structures that were generated from names provided by the given minifilter driver instance. |
| [FltIsEcpFromUserMode function](..\fltkernel\nf-fltkernel-fltisecpfromusermode.md) | The FltIsEcpFromUserMode routine is used to determine if an extra create parameter context structure (ECP) originated from user mode. |
| [FltDeleteStreamHandleContext function](..\fltkernel\nf-fltkernel-fltdeletestreamhandlecontext.md) | FltDeleteStreamHandleContext removes a context that a given minifilter driver instance has set for a given stream handle and marks the context for deletion. |
| [FltRemoveOpenReparseEntry function](..\fltkernel\nf-fltkernel-fltremoveopenreparseentry.md) | This routine removes an OPEN_REPARSE_LIST_ENTRY structure (added by FltAddOpenReparseEntry) from a create operation. |
| [FltRequestOperationStatusCallback function](..\fltkernel\nf-fltkernel-fltrequestoperationstatuscallback.md) | FltRequestOperationStatusCallback returns status information for the given I/O operation. |
| [FltReuseCallbackData function](..\fltkernel\nf-fltkernel-fltreusecallbackdata.md) | The FltReuseCallbackData routine reinitializes a callback data structure so that it can be reused. |
| [FltReferenceFileNameInformation function](..\fltkernel\nf-fltkernel-fltreferencefilenameinformation.md) | FltReferenceFileNameInformation increments the reference count on a file name information structure. |
| [FltAcquirePushLockExclusive function](..\fltkernel\nf-fltkernel-fltacquirepushlockexclusive.md) | The FltAcquirePushLockExclusive routine acquires the given push lock for exclusive access by the calling thread. |
| [FltCreateCommunicationPort function](..\fltkernel\nf-fltkernel-fltcreatecommunicationport.md) | FltCreateCommunicationPort creates a communication server port on which a minifilter driver can receive connection requests from user-mode applications. |
| [FltQueueGenericWorkItem function](..\fltkernel\nf-fltkernel-fltqueuegenericworkitem.md) | FltQueueGenericWorkItem posts a work item that is not associated with a specific I/O operation to a work queue. |
| [FltCreateFileEx2 function](..\fltkernel\nf-fltkernel-fltcreatefileex2.md) | Minifilter drivers call FltCreateFileEx2 to create a new file or open an existing file. This routine also includes an optional create context parameter. |
| [FltGetEcpListFromCallbackData function](..\fltkernel\nf-fltkernel-fltgetecplistfromcallbackdata.md) | The FltGetEcpListFromCallbackData routine returns a pointer to an extra create parameter context structure (ECP) list that is associated with a given create operation callback-data object. |
| [FltGetContextsEx function](..\fltkernel\nf-fltkernel-fltgetcontextsex.md) | The FltGetContextsEx routine retrieves a minifilter driver's contexts for the objects related to the current operation. |
| [FltGetVolumeGuidName function](..\fltkernel\nf-fltkernel-fltgetvolumeguidname.md) | The FltGetVolumeGuidName routine returns the volume name for a given volume, in volume globally unique identifier (GUID) format. |
| [FltSetCallbackDataDirty function](..\fltkernel\nf-fltkernel-fltsetcallbackdatadirty.md) | A minifilter driver's preoperation or postoperation callback routine calls FltSetCallbackDataDirty to indicate that it has modified the contents of the callback data structure. |
| [FltLockUserBuffer function](..\fltkernel\nf-fltkernel-fltlockuserbuffer.md) | The FltLockUserBuffer routine locks the user buffer for a given I/O operation. |
| [FltGetFileSystemType function](..\fltkernel\nf-fltkernel-fltgetfilesystemtype.md) | The FltGetFileSystemType function takes a volume or instance object and provides the file system type of the volume. |
| [FltGetBottomInstance function](..\fltkernel\nf-fltkernel-fltgetbottominstance.md) | FltGetBottomInstance returns an opaque instance pointer for the minifilter driver instance, if there is one, that is attached at the bottom of the instance stack for a given volume. |
| [FltIsOperationSynchronous function](..\fltkernel\nf-fltkernel-fltisoperationsynchronous.md) | The FltIsOperationSynchronous routine determines whether a given callback data structure (FLT_CALLBACK_DATA) represents a synchronous or asynchronous I/O operation. |
| [FltFreeFileLock function](..\fltkernel\nf-fltkernel-fltfreefilelock.md) | The FltFreeFileLock routine uninitializes and frees an initialized FILE_LOCK structure. |
| [FltCreateFileEx function](..\fltkernel\nf-fltkernel-fltcreatefileex.md) | Minifilter drivers call FltCreateFileEx to create a new file or open an existing file. |
| [FltDecodeParameters function](..\fltkernel\nf-fltkernel-fltdecodeparameters.md) | FltDecodeParameters returns pointers to the memory descriptor list (MDL) address, buffer pointer, buffer length, and desired access parameters for an I/O operation. |
| [FltGetRequestorProcess function](..\fltkernel\nf-fltkernel-fltgetrequestorprocess.md) | The FltGetRequestorProcess routine returns a process pointer for the thread that requested a given I/O operation. |
| [FltIsIoCanceled function](..\fltkernel\nf-fltkernel-fltisiocanceled.md) | The FltIsIoCanceled routine checks if an IRP-based operation has been canceled. |
| [FltCreateFile function](..\fltkernel\nf-fltkernel-fltcreatefile.md) | Minifilter drivers call FltCreateFile to create a new file or open an existing file. |
| [FltCompletePendedPostOperation function](..\fltkernel\nf-fltkernel-fltcompletependedpostoperation.md) | FltCompletePendedPostOperation resumes completion processing for an I/O operation that was pended in a minifilter driver's postoperation callback routine. |
| [FltClose function](..\fltkernel\nf-fltkernel-fltclose.md) | FltClose closes a file handle that was opened by FltCreateFile or FltCreateFileEx. |
| [FltOplockIsFastIoPossible function](..\fltkernel\nf-fltkernel-fltoplockisfastiopossible.md) | The FltOplockIsFastIoPossible routine checks a file's opportunistic lock (oplock) state to determine whether fast I/O can be performed on the file. |
| [FltSetCancelCompletion function](..\fltkernel\nf-fltkernel-fltsetcancelcompletion.md) | A minifilter driver calls FltSetCancelCompletion to specify a cancel routine to be called if a given I/O operation is canceled. |
| [FltAllocateCallbackDataEx function](..\fltkernel\nf-fltkernel-fltallocatecallbackdataex.md) | The FltAllocateCallbackDataEx routine allocates a callback data structure and can preallocate memory for additional structures that a minifilter driver can use to initiate an I/O request. |
| [FltOplockKeysEqual function](..\fltkernel\nf-fltkernel-fltoplockkeysequal.md) | The FltOplockKeysEqual routine compares the opportunistic lock (oplock) keys that are stored in the file object extensions of two file objects. |
| [FltIsFltMgrVolumeDeviceObject function](..\fltkernel\nf-fltkernel-fltisfltmgrvolumedeviceobject.md) | The FltIsFltMgrVolumeDeviceObject routine determines whether the given device object belongs to filter manager and if the device object is a volume device object. |
| [FltEnumerateInstances function](..\fltkernel\nf-fltkernel-fltenumerateinstances.md) | The FltEnumerateInstances routine enumerates minifilter driver instances for a given minifilter driver or volume. |
| [FltGetVolumeFromDeviceObject function](..\fltkernel\nf-fltkernel-fltgetvolumefromdeviceobject.md) | The FltGetVolumeFromDeviceObject routine returns an opaque pointer for the volume represented by a volume device object (VDO). |
| [FltParseFileName function](..\fltkernel\nf-fltkernel-fltparsefilename.md) | FltParseFileName parses the extension, stream, and final component from a file name string. |
| [FltEnumerateFilters function](..\fltkernel\nf-fltkernel-fltenumeratefilters.md) | The FltEnumerateFilters routine enumerates all registered minifilter drivers in the system. |
| [FltClearCallbackDataDirty function](..\fltkernel\nf-fltkernel-fltclearcallbackdatadirty.md) | The FltClearCallbackDataDirty routine clears the callback dirty flag in a callback data structure. |
| [FltCopyOpenReparseList function](..\fltkernel\nf-fltkernel-fltcopyopenreparselist.md) | This routine copies any open reparse information from a previous create into a new ECP list that can be used to issue a second create. |
| [FltInitializeFileLock function](..\fltkernel\nf-fltkernel-fltinitializefilelock.md) | The FltInitializeFileLock routine initializes an opaque FILE_LOCK structure that the caller has allocated from paged pool. |
| [FltReleaseContextsEx function](..\fltkernel\nf-fltkernel-fltreleasecontextsex.md) | FltReleaseContextsEx releases each context in a given FLT_RELATED_CONTEXTS_EX structure. |
| [FltCheckLockForWriteAccess function](..\fltkernel\nf-fltkernel-fltchecklockforwriteaccess.md) | The FltCheckLockForWriteAccess routine determines whether the caller has write access to a locked byte range of a file. |
| [FltDetachVolume function](..\fltkernel\nf-fltkernel-fltdetachvolume.md) | FltDetachVolume detaches a minifilter driver instance from a volume. |
| [FltAllocateExtraCreateParameterList function](..\fltkernel\nf-fltkernel-fltallocateextracreateparameterlist.md) | The FltAllocateExtraCreateParameterList routine allocates paged pool memory for an extra create parameter (ECP) list structure and generates a pointer to that structure. |
| [FltQueryInformationFile function](..\fltkernel\nf-fltkernel-fltqueryinformationfile.md) | FltQueryInformationFile retrieves information for a given file. |
| [FltReadFileEx function](..\fltkernel\nf-fltkernel-fltreadfileex.md) | FltReadFileEx reads data from an open file, stream, or device. This function extends FltReadFile to allow the optional use of an MDL for read data instead of a mapped buffer address. |
| [FltAllocateExtraCreateParameter function](..\fltkernel\nf-fltkernel-fltallocateextracreateparameter.md) | The FltAllocateExtraCreateParameter routine allocates paged memory pool for a user-defined extra create parameter (ECP) context structure and generates a pointer to that structure. |
| [FltGetVolumeName function](..\fltkernel\nf-fltkernel-fltgetvolumename.md) | The FltGetVolumeName routine gets the volume name for a given volume. |
| [FltReadFile function](..\fltkernel\nf-fltkernel-fltreadfile.md) | FltReadFile reads data from an open file, stream, or device. |
| [FltCreateNamedPipeFile function](..\fltkernel\nf-fltkernel-fltcreatenamedpipefile.md) | Minifilter drivers call FltCreateNamedPipeFile to create a new pipe or open an existing pipe. |
| [FltGetVolumeFromInstance function](..\fltkernel\nf-fltkernel-fltgetvolumefrominstance.md) | The FltGetVolumeFromInstance routine returns an opaque pointer for the volume that a given minifilter driver instance is attached to. |
| [FltReleaseContext function](..\fltkernel\nf-fltkernel-fltreleasecontext.md) | FltReleaseContext decrements the reference count on a context. |
| [FltAllocateExtraCreateParameterFromLookasideList function](..\fltkernel\nf-fltkernel-fltallocateextracreateparameterfromlookasidelist.md) | The FltAllocateExtraCreateParameterFromLookasideList routine allocates memory pool from a given lookaside list for an extra create parameter (ECP) context structure and generates a pointer to that structure. |
| [FltRetainSwappedBufferMdlAddress function](..\fltkernel\nf-fltkernel-fltretainswappedbuffermdladdress.md) | FltRetainSwappedBufferMdlAddress prevents the Filter Manager from freeing the memory descriptor list (MDL) for a buffer that was swapped in by a minifilter driver. |
| [FltNotifyFilterChangeDirectory function](..\fltkernel\nf-fltkernel-fltnotifyfilterchangedirectory.md) | The FltNotifyFilterChangeDirectory routine creates a notify structure for an IRP_MN_NOTIFY_CHANGE_DIRECTORY operation and adds it to the specified notify list. |
| [FltQueryDirectoryFile function](..\fltkernel\nf-fltkernel-fltquerydirectoryfile.md) | The FltQueryDirectoryFile routine returns various kinds of information about files in the directory specified by a given file object. |
| [FltFreeDeferredIoWorkItem function](..\fltkernel\nf-fltkernel-fltfreedeferredioworkitem.md) | The FltFreeDeferredIoWorkItem routine frees a work item allocated by the FltAllocateDeferredIoWorkItem routine. |
| [FltEnumerateVolumeInformation function](..\fltkernel\nf-fltkernel-fltenumeratevolumeinformation.md) | The FltEnumerateVolumeInformation routine provides information about volumes that are known to the filter manager. |
| [FltQueueDeferredIoWorkItem function](..\fltkernel\nf-fltkernel-fltqueuedeferredioworkitem.md) | The FltQueueDeferredIoWorkItem routine posts an IRP-based I/O operation to a work queue. |
| [FltCancelIo function](..\fltkernel\nf-fltkernel-fltcancelio.md) | The FltCancelIo routine cancels an I/O operation. |
| [FltTagFile function](..\fltkernel\nf-fltkernel-flttagfile.md) | FltTagFile sets a reparse tag on a file or directory. |
| [FltIsVolumeWritable function](..\fltkernel\nf-fltkernel-fltisvolumewritable.md) | The FltIsVolumeWritable routine determines whether the disk device that corresponds to a volume or minifilter driver instance is writable. |
| [FltReleaseContexts function](..\fltkernel\nf-fltkernel-fltreleasecontexts.md) | FltReleaseContexts releases each context in a given FLT_RELATED_CONTEXTS structure. |
| [FltCurrentOplockH function](..\fltkernel\nf-fltkernel-fltcurrentoplockh.md) | A minifilter driver calls the FltCurrentOplockH routine to determine whether there are any CACHE_HANDLE_LEVEL opportunistic locks (oplocks) on a file. |
| [FltRetrieveIoPriorityInfo function](..\fltkernel\nf-fltkernel-fltretrieveiopriorityinfo.md) | The FltRetrieveIoPriorityInfo routine is used by a minifilter driver to retrieve priority information from a thread. |
| [FltPerformAsynchronousIo function](..\fltkernel\nf-fltkernel-fltperformasynchronousio.md) | A minifilter driver calls FltPerformAsynchronousIo to initiate an asynchronous I/O operation. |
| [FltGetNextExtraCreateParameter function](..\fltkernel\nf-fltkernel-fltgetnextextracreateparameter.md) | The FltGetNextExtraCreateParameter routine returns a pointer to the next (or first) extra create parameter context structure (ECP) in a given ECP list. |
| [FltDeleteContext function](..\fltkernel\nf-fltkernel-fltdeletecontext.md) | FltDeleteContext marks a specified context for deletion. |
| [FltQueryVolumeInformation function](..\fltkernel\nf-fltkernel-fltqueryvolumeinformation.md) | The FltQueryVolumeInformation routine retrieves information about the volume that the given instance is attached to. |
| [FltCreateSystemVolumeInformationFolder function](..\fltkernel\nf-fltkernel-fltcreatesystemvolumeinformationfolder.md) | FltCreateSystemVolumeInformationFolder verifies the existence of the &#0034;System Volume Information&#0034; folder on a file system volume. If the folder is not present, then the folder is created. |
| [FltReissueSynchronousIo function](..\fltkernel\nf-fltkernel-fltreissuesynchronousio.md) | FltReissueSynchronousIo initiates a new synchronous I/O operation that uses the parameters from a previously synchronized I/O operation. |
| [FltIsIoRedirectionAllowed function](..\fltkernel\nf-fltkernel-fltisioredirectionallowed.md) | The FltIsIoRedirectionAllowed routine determines whether I/O can be redirected from the specified source filter instance to another specified filter instance. |
| [FltFreeExtraCreateParameterList function](..\fltkernel\nf-fltkernel-fltfreeextracreateparameterlist.md) | The FltFreeExtraCreateParameterList routine frees an extra create parameter (ECP) list structure. |
| [FltFindExtraCreateParameter function](..\fltkernel\nf-fltkernel-fltfindextracreateparameter.md) | The FltFindExtraCreateParameter routine searches a given ECP list for an ECP context structure of a given type and returns a pointer to this structure if it is found. |
| [FltUnregisterFilter function](..\fltkernel\nf-fltkernel-fltunregisterfilter.md) | A registered minifilter driver calls FltUnregisterFilter to unregister itself so that the Filter Manager no longer calls it to process I/O operations. |
| [FltQueryEaFile function](..\fltkernel\nf-fltkernel-fltqueryeafile.md) | FltQueryEaFile returns information about extended-attribute (EA) values for a file. |
| [FltGetRequestorSessionId function](..\fltkernel\nf-fltkernel-fltgetrequestorsessionid.md) | The FltGetRequestorSessionId routine returns the session ID of the process that originally requested the specified I/O operation. |
| [FltQueryQuotaInformationFile function](..\fltkernel\nf-fltkernel-fltqueryquotainformationfile.md) | The FltQueryQuotaInformationFile routine retrieves quota entries associated with a file object. |
| [FltSetInstanceContext function](..\fltkernel\nf-fltkernel-fltsetinstancecontext.md) | FltSetInstanceContext sets a context for a minifilter driver instance. |
| [FltAcknowledgeEcp function](..\fltkernel\nf-fltkernel-fltacknowledgeecp.md) | The FltAcknowledgeEcp routine is used to mark an extra create parameter context structure (ECP) as acknowledged. |
| [FltAllocateDeferredIoWorkItem function](..\fltkernel\nf-fltkernel-fltallocatedeferredioworkitem.md) | FltAllocateDeferredIoWorkItem allocates a deferred-I/O work item. |
| [FltAllocateGenericWorkItem function](..\fltkernel\nf-fltkernel-fltallocategenericworkitem.md) | FltAllocateGenericWorkItem allocates a generic work item. |
| [FltEnumerateInstanceInformationByFilter function](..\fltkernel\nf-fltkernel-fltenumerateinstanceinformationbyfilter.md) | The FltEnumerateInstanceInformationByFilter routine provides information about instances of a given minifilter driver. |
| [FltGetStreamContext function](..\fltkernel\nf-fltkernel-fltgetstreamcontext.md) | The FltGetStreamContext routine retrieves a context that was set for a file stream by a given minifilter driver instance. |
| [FltSetFileContext function](..\fltkernel\nf-fltkernel-fltsetfilecontext.md) | The FltSetFileContext routine sets a context for a file. |
| [FltGetRequestorProcessIdEx function](..\fltkernel\nf-fltkernel-fltgetrequestorprocessidex.md) | The FltGetRequestorProcessIdEx routine returns the kernel-mode handle for the process that is associated with the thread that requested a given I/O operation. |
| [FltClearCancelCompletion function](..\fltkernel\nf-fltkernel-fltclearcancelcompletion.md) | FltClearCancelCompletion clears a cancel routine that was specified for an I/O operation. |
| [FltGetLowerInstance function](..\fltkernel\nf-fltkernel-fltgetlowerinstance.md) | The FltGetLowerInstance routine returns an opaque instance pointer for the next lower minifilter driver instance, if there is one, that is attached below a given minifilter driver instance on the same volume. |
| [FltInitExtraCreateParameterLookasideList function](..\fltkernel\nf-fltkernel-fltinitextracreateparameterlookasidelist.md) | The FltInitExtraCreateParameterLookasideList routine initializes a paged or non-paged pool lookaside list used for the allocation of one or more extra create parameter context structures (ECPs) of fixed size. |
| [FltGetVolumeContext function](..\fltkernel\nf-fltkernel-fltgetvolumecontext.md) | The FltGetVolumeContext routine retrieves a context that was set for a volume by a given minifilter driver. |
| [FltSetTransactionContext function](..\fltkernel\nf-fltkernel-fltsettransactioncontext.md) | The FltSetTransactionContext routine sets a context on a transaction. |
| [FltCompareInstanceAltitudes function](..\fltkernel\nf-fltkernel-fltcompareinstancealtitudes.md) | FltCompareInstanceAltitudes compares the altitudes of two minifilter driver instances. |
| [FltSupportsStreamHandleContexts function](..\fltkernel\nf-fltkernel-fltsupportsstreamhandlecontexts.md) | FltSupportsStreamHandleContexts determines whether stream handle contexts are supported on a given file object. |
| [FltOpenVolume function](..\fltkernel\nf-fltkernel-fltopenvolume.md) | The FltOpenVolume routine returns a handle and a file object pointer for the file system volume that a given minifilter driver instance is attached to. |
| [FltBuildDefaultSecurityDescriptor function](..\fltkernel\nf-fltkernel-fltbuilddefaultsecuritydescriptor.md) | FltBuildDefaultSecurityDescriptor builds a default security descriptor for use with FltCreateCommunicationPort. |
| [FltOplockBreakH function](..\fltkernel\nf-fltkernel-fltoplockbreakh.md) | The FltOplockBreakH routine breaks CACHE_HANDLE_LEVEL opportunistic locks (oplocks). |
| [FltDeleteFileContext function](..\fltkernel\nf-fltkernel-fltdeletefilecontext.md) | The FltDeleteFileContext routine retrieves and deletes a file context that a given minifilter driver has set for a given file. |
| [FltIsDirectory function](..\fltkernel\nf-fltkernel-fltisdirectory.md) | A minifilter driver calls the FltIsDirectory routine to determine whether a given file object represents a directory. |
| [FltReferenceContext function](..\fltkernel\nf-fltkernel-fltreferencecontext.md) | FltReferenceContext increments the reference count on a context structure. |
| [FltAllocateCallbackData function](..\fltkernel\nf-fltkernel-fltallocatecallbackdata.md) | FltAllocateCallbackData allocates a callback data structure that a minifilter driver can use to initiate an I/O request. |
| [FltGetFileNameInformationUnsafe function](..\fltkernel\nf-fltkernel-fltgetfilenameinformationunsafe.md) | The FltGetFileNameInformationUnsafe routine returns name information for an open file or directory. |
| [FltDeletePushLock function](..\fltkernel\nf-fltkernel-fltdeletepushlock.md) | The FltDeletePushLock routine deletes a given push lock. |
| [FltGetTunneledName function](..\fltkernel\nf-fltkernel-fltgettunneledname.md) | The FltGetTunneledName routine retrieves the tunneled name for a file, given the normalized name returned for the file by a previous call to FltGetFileNameInformation, FltGetFileNameInformationUnsafe, or FltGetDestinationFileNameInformation. |
| [FltProcessFileLock function](..\fltkernel\nf-fltkernel-fltprocessfilelock.md) | The FltProcessFileLock routine processes and completes a file lock operation. |
| [FltFlushBuffers function](..\fltkernel\nf-fltkernel-fltflushbuffers.md) | The FltFlushBuffers routine is used by the minifilter driver to send a flush request for a given file to the file system. |
| [FltLoadFilter function](..\fltkernel\nf-fltkernel-fltloadfilter.md) | The FltLoadFilter routine dynamically loads a minifilter driver into the currently running system. |
| [FltGetVolumeProperties function](..\fltkernel\nf-fltkernel-fltgetvolumeproperties.md) | The FltGetVolumeProperties routine returns volume property information for the given volume. |
| [FltAdjustDeviceStackSizeForIoRedirection function](..\fltkernel\nf-fltkernel-fltadjustdevicestacksizeforioredirection.md) | The FltAdjustDeviceStackSizeForIoRedirection routine increases the size of the source device stack to allow a minifilter to redirect I/O from a specified source instance to a specified target instance when the target stack is deeper than the source stack. |
| [FltSetQuotaInformationFile function](..\fltkernel\nf-fltkernel-fltsetquotainformationfile.md) | The FltSetQuotaInformationFile routine modifies quota entries for a file object. |
| [FltGetInstanceContext function](..\fltkernel\nf-fltkernel-fltgetinstancecontext.md) | The FltGetInstanceContext routine retrieves a context that was set for an instance by a given minifilter driver. |
| [FltGetSectionContext function](..\fltkernel\nf-fltkernel-fltgetsectioncontext.md) | The FltGetSectionContext routine retrieves a section context that was created for a file stream by a specified minifilter driver instance. |
| [FltStartFiltering function](..\fltkernel\nf-fltkernel-fltstartfiltering.md) | FltStartFiltering starts filtering for a registered minifilter driver. |
| [FltEnumerateInstanceInformationByDeviceObject function](..\fltkernel\nf-fltkernel-fltenumerateinstanceinformationbydeviceobject.md) | The FltEnumerateInstanceInformationByDeviceObject routine provides information about minifilter driver instances and legacy filter drivers that are attached to the volume related to a specified device object. |
| [FltSetStreamHandleContext function](..\fltkernel\nf-fltkernel-fltsetstreamhandlecontext.md) | The FltSetStreamHandleContext routine sets a context for a stream handle. |
| [FltGetVolumeInstanceFromName function](..\fltkernel\nf-fltkernel-fltgetvolumeinstancefromname.md) | The FltGetVolumeInstanceFromName routine returns an opaque instance pointer for the given minifilter driver instance on the given volume. |
| [FltCreateSectionForDataScan function](..\fltkernel\nf-fltkernel-fltcreatesectionfordatascan.md) | The FltCreateSectionForDataScan routine creates a section object for a file. The filter manager can optionally synchronize I/O with the section created. |
| [FltGetDeviceObject function](..\fltkernel\nf-fltkernel-fltgetdeviceobject.md) | The FltGetDeviceObject routine returns a pointer to the Filter Manager's volume device object (VDO) for a given volume. |
| [FltCheckLockForReadAccess function](..\fltkernel\nf-fltkernel-fltchecklockforreadaccess.md) | The FltCheckLockForReadAccess routine determines whether the caller has read access to a locked byte range of a file. |
| [FltSetEcpListIntoCallbackData function](..\fltkernel\nf-fltkernel-fltsetecplistintocallbackdata.md) | The FltSetEcpListIntoCallbackData routine attaches an extra create parameter context structure (ECP) list to a create operation callback-data object. |
| [FltAllocateFileLock function](..\fltkernel\nf-fltkernel-fltallocatefilelock.md) | The FltAllocateFileLock routine allocates and initializes a new FILE_LOCK structure. |
| [FltGetDiskDeviceObject function](..\fltkernel\nf-fltkernel-fltgetdiskdeviceobject.md) | The FltGetDiskDeviceObject routine returns a pointer to the disk device object associated with a given volume. |
| [FltQuerySecurityObject function](..\fltkernel\nf-fltkernel-fltquerysecurityobject.md) | FltQuerySecurityObject retrieves a copy of an object's security descriptor. |
| [FltSetVolumeContext function](..\fltkernel\nf-fltkernel-fltsetvolumecontext.md) | FltSetVolumeContext sets a context for a volume. |
| [FltWriteFile function](..\fltkernel\nf-fltkernel-fltwritefile.md) | FltWriteFile is used to write data to an open file, stream, or device. |
| [FltGetContexts function](..\fltkernel\nf-fltkernel-fltgetcontexts.md) | The FltGetContexts routine retrieves a minifilter driver's contexts for the objects related to the current operation. |
| [FltSetActivityIdCallbackData function](..\fltkernel\nf-fltkernel-fltsetactivityidcallbackdata.md) | The FltSetActivityIdCallbackData routine sets the a activity ID for an IRP in a minifilter's callback data. |
| [FltEnumerateInstanceInformationByVolume function](..\fltkernel\nf-fltkernel-fltenumerateinstanceinformationbyvolume.md) | The FltEnumerateInstanceInformationByVolume routine provides information about minifilter driver instances and legacy filter drivers (Windows Vista only) that are attached to a given volume. |
| [FltGetFilterFromInstance function](..\fltkernel\nf-fltkernel-fltgetfilterfrominstance.md) | The FltGetFilterFromInstance routine returns an opaque filter pointer for the minifilter driver that created the given instance. |
| [FltAttachVolumeAtAltitude function](..\fltkernel\nf-fltkernel-fltattachvolumeataltitude.md) | FltAttachVolumeAtAltitude is a debugging support routine that attaches a minifilter driver instance to a volume at a specified altitude, overriding any settings in the minifilter driver's INF file. |
| [FltGetInstanceInformation function](..\fltkernel\nf-fltkernel-fltgetinstanceinformation.md) | The FltGetInstanceInformation routine returns information about a minifilter driver instance. |
| [FltGetRequestorProcessId function](..\fltkernel\nf-fltkernel-fltgetrequestorprocessid.md) | The FltGetRequestorProcessId routine returns the unique 32-bit process ID for the process associated with the thread that requested a given I/O operation. |
| [FltEnumerateVolumes function](..\fltkernel\nf-fltkernel-fltenumeratevolumes.md) | The FltEnumerateVolumes routine enumerates all volumes in the system. |
| [FltAllocateContext function](..\fltkernel\nf-fltkernel-fltallocatecontext.md) | The FltAllocateContext routine allocates a context structure for a specified context type. |
| [FltGetVolumeInformation function](..\fltkernel\nf-fltkernel-fltgetvolumeinformation.md) | The FltGetVolumeInformation routine provides information about a given volume. |
| [FltCommitFinalizeComplete function](..\fltkernel\nf-fltkernel-fltcommitfinalizecomplete.md) | The FltCommitFinalizeComplete routine acknowledges a TRANSACTION_NOTIFY_COMMIT_FINALIZE notification. |
| [FltRegisterForDataScan function](..\fltkernel\nf-fltkernel-fltregisterfordatascan.md) | The FltRegisterForDataScan routine enables data scanning for the volume attached to the minifilter instance. |
| [FltGetSwappedBufferMdlAddress function](..\fltkernel\nf-fltkernel-fltgetswappedbuffermdladdress.md) | The FltGetSwappedBufferMdlAddress routine returns the memory descriptor list (MDL) address for a buffer that was swapped in by a minifilter driver. |
| [FltCancellableWaitForMultipleObjects function](..\fltkernel\nf-fltkernel-fltcancellablewaitformultipleobjects.md) | The FltCancellableWaitForMultipleObjects executes a cancelable wait operation (a wait that can be terminated) on one or more dispatcher objects. |
| [FltAllocatePoolAlignedWithTag function](..\fltkernel\nf-fltkernel-fltallocatepoolalignedwithtag.md) | FltAllocatePoolAlignedWithTag allocates a device-aligned buffer for use in a noncached I/O operation. |
| [FltCheckOplockEx function](..\fltkernel\nf-fltkernel-fltcheckoplockex.md) | A minifilter driver calls the FltCheckOplockEx routine to synchronize the callback data structure for an IRP-based file I/O operation that has the current opportunistic lock (oplock) state of the file. |
| [FltIsEcpAcknowledged function](..\fltkernel\nf-fltkernel-fltisecpacknowledged.md) | The FltIsEcpAcknowledged routine is used to determine if a given extra create parameter context structure (ECP) has been marked as acknowledged. |
| [FltInitializeOplock function](..\fltkernel\nf-fltkernel-fltinitializeoplock.md) | The FltInitializeOplock routine initializes an opportunistic lock (oplock) pointer. |
| [FltPrepareToReuseEcp function](..\fltkernel\nf-fltkernel-fltpreparetoreuseecp.md) | The FltPrepareToReuseEcp routine resets an extra create parameter (ECP) context structure, which prepares it for reuse. |
| [FltSetStreamContext function](..\fltkernel\nf-fltkernel-fltsetstreamcontext.md) | The FltSetStreamContext routine sets a context for a file stream. |
| [FltCommitComplete function](..\fltkernel\nf-fltkernel-fltcommitcomplete.md) | The FltCommitComplete routine acknowledges a TRANSACTION_NOTIFY_COMMIT notification. |
| [FltFreePoolAlignedWithTag function](..\fltkernel\nf-fltkernel-fltfreepoolalignedwithtag.md) | The FltFreePoolAlignedWithTag routine frees a cache-aligned buffer that was allocated by a previous call to FltAllocatePoolAlignedWithTag. |
| [FltSupportsFileContextsEx function](..\fltkernel\nf-fltkernel-fltsupportsfilecontextsex.md) | The FltSupportsFileContextsEx routine determines whether the file system or the filter manager support file contexts for a given file. |
| [FltFreeCallbackData function](..\fltkernel\nf-fltkernel-fltfreecallbackdata.md) | The FltFreeCallbackData routine frees a callback data structure allocated by the FltAllocateCallbackData routine. |
| [FltIsIoRedirectionAllowedForOperation function](..\fltkernel\nf-fltkernel-fltisioredirectionallowedforoperation.md) | The FltIsIoRedirectionAllowedForOperation routine determines whether I/O can be redirected from the filter instance associated with the specified FLT_CALLBACK_DATA structure to the specified filter instance. |
| [FltCurrentOplock function](..\fltkernel\nf-fltkernel-fltcurrentoplock.md) | A minifilter driver calls the FltCurrentOplock routine to determine whether there are any opportunistic locks (oplocks) on a file. |
| [FltPrepareComplete function](..\fltkernel\nf-fltkernel-fltpreparecomplete.md) | The FltPrepareComplete routine acknowledges a TRANSACTION_NOTIFY_PREPARE notification. |
| [FltCheckAndGrowNameControl function](..\fltkernel\nf-fltkernel-fltcheckandgrownamecontrol.md) | The FltCheckAndGrowNameControl routine checks whether the buffer in a FLT_NAME_CONTROL structure is large enough to hold the specified number of bytes. If not, FltCheckAndGrowNameControl replaces it with a larger system-allocated buffer. |
| [FltUninitializeFileLock function](..\fltkernel\nf-fltkernel-fltuninitializefilelock.md) | The FltUninitializeFileLock routine uninitializes a FILE_LOCK structure. |
| [FltParseFileNameInformation function](..\fltkernel\nf-fltkernel-fltparsefilenameinformation.md) | FltParseFileNameInformation parses the contents of a FLT_FILE_NAME_INFORMATION structure. |
| [FltOplockBreakToNoneEx function](..\fltkernel\nf-fltkernel-fltoplockbreaktononeex.md) | The FltOplockBreakToNoneEx routine breaks all opportunistic locks (oplocks) immediately without regard for any oplock key. |
| [FltRegisterFilter function](..\fltkernel\nf-fltkernel-fltregisterfilter.md) | FltRegisterFilter registers a minifilter driver. |
| [FltSendMessage function](..\fltkernel\nf-fltkernel-fltsendmessage.md) | FltSendMessage sends a message to a waiting user-mode application on behalf of a minifilter driver or a minifilter driver instance. |
| [FltCompletePendedPreOperation function](..\fltkernel\nf-fltkernel-fltcompletependedpreoperation.md) | FltCompletePendedPreOperation resumes processing for an I/O operation that was pended in a minifilter driver's preoperation callback (PFLT_PRE_OPERATION_CALLBACK) routine. |
| [FltReleaseFileNameInformation function](..\fltkernel\nf-fltkernel-fltreleasefilenameinformation.md) | FltReleaseFileNameInformation releases a file name information structure. |
| [FltUntagFile function](..\fltkernel\nf-fltkernel-fltuntagfile.md) | FltUntagFile removes a reparse point from a file or directory. |
| [FltSupportsFileContexts function](..\fltkernel\nf-fltkernel-fltsupportsfilecontexts.md) | The FltSupportsFileContexts routine determines whether the file system supports file contexts for a given file. |
| [FltAddOpenReparseEntry function](..\fltkernel\nf-fltkernel-fltaddopenreparseentry.md) | This routine adds a caller allocated open reparse structure, OPEN_REPARSE_LIST_ENTRY, into a create operation. |
| [FltSetIoPriorityHintIntoFileObject function](..\fltkernel\nf-fltkernel-fltsetiopriorityhintintofileobject.md) | The FltSetIoPriorityHintIntoFileObject routine is used by a minifilter driver to set the I/O priority information in a file object. |
| [FltPerformSynchronousIo function](..\fltkernel\nf-fltkernel-fltperformsynchronousio.md) | A minifilter driver calls FltPerformSynchronousIo to initiate a synchronous I/O operation after calling FltAllocateCallbackData to allocate a callback data structure for the operation. |
| [FltGetIoPriorityHintFromThread function](..\fltkernel\nf-fltkernel-fltgetiopriorityhintfromthread.md) | The FltGetIoPriorityHintFromThread routine is used by a minifilter driver to get IO priority information from a thread. |
| [FltUnloadFilter function](..\fltkernel\nf-fltkernel-fltunloadfilter.md) | A minifilter driver that has loaded a supporting minifilter driver by calling FltLoadFilter can unload the minifilter driver by calling FltUnloadFilter. |
| [FltGetFileContext function](..\fltkernel\nf-fltkernel-fltgetfilecontext.md) | The FltGetFileContext routine retrieves a context that was set for a file by a given minifilter driver instance. |
| [FltAttachVolume function](..\fltkernel\nf-fltkernel-fltattachvolume.md) | FltAttachVolume creates a new minifilter driver instance and attaches it to the given volume. |
| [FltUninitializeOplock function](..\fltkernel\nf-fltkernel-fltuninitializeoplock.md) | FltUninitializeOplock uninitializes an opportunistic lock (oplock) pointer. |
| [FltPrePrepareComplete function](..\fltkernel\nf-fltkernel-fltprepreparecomplete.md) | The FltPrePrepareComplete routine acknowledges a TRANSACTION_NOTIFY_PREPREPARE notification. |
| [FltSetIoPriorityHintIntoCallbackData function](..\fltkernel\nf-fltkernel-fltsetiopriorityhintintocallbackdata.md) | The FltSetIoPriorityHintIntoCallbackData routine is used by a minifilter driver to set the I/O priority information in callback data. |
| [FltDeleteVolumeContext function](..\fltkernel\nf-fltkernel-fltdeletevolumecontext.md) | FltDeleteVolumeContext removes a context that a given minifilter driver has set for a given volume and marks the context for deletion. |
| [FltGetIrpName function](..\fltkernel\nf-fltkernel-fltgetirpname.md) | The FltGetIrpName routine returns the name for a major function code as a printable string. |
| [FltGetVolumeFromFileObject function](..\fltkernel\nf-fltkernel-fltgetvolumefromfileobject.md) | The FltGetVolumeFromFileObject routine returns an opaque pointer for the volume that a given file stream resides on. |
| [FltGetIoPriorityHintFromFileObject function](..\fltkernel\nf-fltkernel-fltgetiopriorityhintfromfileobject.md) | The FltGetIoPriorityHintFromFileObject routine is used by a minifilter driver to get IO priority information from a file object. |
| [FltFreeOpenReparseList function](..\fltkernel\nf-fltkernel-fltfreeopenreparselist.md) | This routine deallocates any information copied into a create operation by a previous call to FltCopyOpenReparseList. |
| [FltApplyPriorityInfoThread function](..\fltkernel\nf-fltkernel-fltapplypriorityinfothread.md) | The FltApplyPriorityInfoThread routine is used by a minifilter driver to apply priority information to a thread. |
| [FltRemoveExtraCreateParameter function](..\fltkernel\nf-fltkernel-fltremoveextracreateparameter.md) | The FltRemoveExtraCreateParameter routine searches an ECP list for an ECP context structure and, if found, detaches it from the ECP list. |
| [FltGetActivityIdCallbackData function](..\fltkernel\nf-fltkernel-fltgetactivityidcallbackdata.md) | The FltGetActivityIdCallbackData routine retrieves the current activity ID associated with a request in a minifilter's callback data. |
| [FltDeleteInstanceContext function](..\fltkernel\nf-fltkernel-fltdeleteinstancecontext.md) | FltDeleteInstanceContext removes a context from a given instance and marks the context for deletion. |
| [FltSetEaFile function](..\fltkernel\nf-fltkernel-fltseteafile.md) | FltSetEaFile sets extended-attribute (EA) values for a file. |
| [FltSupportsStreamContexts function](..\fltkernel\nf-fltkernel-fltsupportsstreamcontexts.md) | FltSupportsStreamContexts determines whether stream contexts are supported on a given file object. |
| [FltCloseSectionForDataScan function](..\fltkernel\nf-fltkernel-fltclosesectionfordatascan.md) | The FltCloseSectionForDataScan routine closes a section object associated with a file stream. |
| [FltCancelFileOpen function](..\fltkernel\nf-fltkernel-fltcancelfileopen.md) | A minifilter driver can use the FltCancelFileOpen routine to close a newly opened or created file. |
| [FltCancellableWaitForSingleObject function](..\fltkernel\nf-fltkernel-fltcancellablewaitforsingleobject.md) | The FltCancellableWaitForSingleObject routine executes a cancelable wait operation (a wait that can be terminated) on a dispatcher object. |
| [FltRollbackEnlistment function](..\fltkernel\nf-fltkernel-fltrollbackenlistment.md) | The FltRollbackEnlistment routine rolls back or aborts a transaction on behalf of a minifilter driver. |
| [FltGetTopInstance function](..\fltkernel\nf-fltkernel-fltgettopinstance.md) | The FltGetTopInstance routine returns an opaque instance pointer for the minifilter driver instance that is attached at the top of the instance stack for a given volume. |
| [FltEnumerateFilterInformation function](..\fltkernel\nf-fltkernel-fltenumeratefilterinformation.md) | The FltEnumerateFilterInformation routine provides information about all the registered filter drivers (including minifilter and legacy filter drivers) in the system. |
| [FltGetStreamHandleContext function](..\fltkernel\nf-fltkernel-fltgetstreamhandlecontext.md) | The FltGetStreamHandleContext routine retrieves a context that was set for a stream handle by a given minifilter driver instance. |
| [FltGetVolumeFromName function](..\fltkernel\nf-fltkernel-fltgetvolumefromname.md) | The FltGetVolumeFromName routine returns an opaque pointer for the volume whose name matches the value of the VolumeName parameter. |
| [FltIsVolumeSnapshot function](..\fltkernel\nf-fltkernel-fltisvolumesnapshot.md) | The FltIsVolumeSnapshot routine determines whether a volume or minifilter driver instance is attached to a snapshot volume. |
| [FltFsControlFile function](..\fltkernel\nf-fltkernel-fltfscontrolfile.md) | The FltFsControlFile routine sends a control code directly to a specified file system or file system filter driver, causing the corresponding driver to perform the specified action. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFLT_INSTANCE_SETUP_CALLBACK callback](..\fltkernel\nc-fltkernel-pflt-instance-setup-callback.md) | A minifilter driver can register a routine of type PFLT_INSTANCE_SETUP_CALLBACK as the minifilter driver's InstanceSetupCallback routine. |
| [PFLT_COMPLETED_ASYNC_IO_CALLBACK callback](..\fltkernel\nc-fltkernel-pflt-completed-async-io-callback.md) | A minifilter driver that initiates an asynchronous I/O operation can specify a routine of type PFLT_COMPLETED_ASYNC_IO_CALLBACK routine to be called when the operation is completed. |
| [PFLT_CONTEXT_FREE_CALLBACK callback](..\fltkernel\nc-fltkernel-pflt-context-free-callback.md) | A minifilter can register a routine of type PFLT_CONTEXT_FREE_CALLBACK as the minifilter driver's ContextFreeCallback routine. |
| [PFLT_CONTEXT_ALLOCATE_CALLBACK callback](..\fltkernel\nc-fltkernel-pflt-context-allocate-callback.md) | A minifilter driver can register a routine of type PFLT_CONTEXT_ALLOCATE_CALLBACK as the minifilter driver's ContextAllocateCallback routine. |
| [PFLT_INSTANCE_TEARDOWN_CALLBACK callback](..\fltkernel\nc-fltkernel-pflt-instance-teardown-callback.md) | A minifilter driver can register two routines of type PFLT_INSTANCE_TEARDOWN_CALLBACK as the minifilter driver's InstanceTeardownStartCallback and InstanceTeardownCompleteCallback routines. |
| [PFLT_NORMALIZE_NAME_COMPONENT callback](..\fltkernel\nc-fltkernel-pflt-normalize-name-component.md) | A minifilter driver that provides file names for the filter manager's name cache can register a routine of type PFLT_NORMALIZE_NAME_COMPONENT as the minifilter driver's NormalizeNameComponentCallback routine. |
| [PFLT_SECTION_CONFLICT_NOTIFICATION_CALLBACK callback](..\fltkernel\nc-fltkernel-pflt-section-conflict-notification-callback.md) | A minifilter driver can optionally register a routine of type PFLT_CONTEXT_ALLOCATE_CALLBACK as the minifilter driver's SectionNotificationCallback routine. |
| [PFLT_INSTANCE_QUERY_TEARDOWN_CALLBACK callback](..\fltkernel\nc-fltkernel-pflt-instance-query-teardown-callback.md) | A minifilter driver can register a routine of type PFLT_INSTANCE_QUERY_TEARDOWN_CALLBACK as the minifilter driver's InstanceQueryTeardownCallback routine. |
| [PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE callback](..\fltkernel\nc-fltkernel-pflt-complete-lock-callback-data-routine.md) | A minifilter driver can register a routine of type PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE as the minifilter driver's CompleteLockCallbackDataRoutine callback routine for a FILE_LOCK structure. |
| [PFLT_GET_OPERATION_STATUS_CALLBACK callback](..\fltkernel\nc-fltkernel-pflt-get-operation-status-callback.md) | A minifilter driver can register a routine of type PFLT_GET_OPERATION_STATUS_CALLBACK as the minifilter driver's OperationStatusCallback routine. |
| [PFLT_PRE_OPERATION_CALLBACK callback](..\fltkernel\nc-fltkernel-pflt-pre-operation-callback.md) | A minifilter driver's PFLT_PRE_OPERATION_CALLBACK routine performs pre-operation processing for I/O operations. |
| [PFLT_NORMALIZE_NAME_COMPONENT_EX callback](..\fltkernel\nc-fltkernel-pflt-normalize-name-component-ex.md) | A minifilter driver that provides file names for the filter manager's name cache can register a routine of type PFLT_NORMALIZE_NAME_COMPONENT_EX as the minifilter driver's NormalizeNameComponentExCallback callback routine. |
| [PFLT_FILTER_UNLOAD_CALLBACK callback](..\fltkernel\nc-fltkernel-pflt-filter-unload-callback.md) | A minifilter driver can register a routine of type PFLT_FILTER_UNLOAD_CALLBACK as the minifilter driver's FilterUnloadCallback routine. |
| [PFLT_TRANSACTION_NOTIFICATION_CALLBACK callback](..\fltkernel\nc-fltkernel-pflt-transaction-notification-callback.md) | A minifilter driver can register a routine of type PFLT_TRANSACTION_NOTIFICATION_CALLBACK as its TransactionNotificationCallback routine. |
| [PFLT_NORMALIZE_CONTEXT_CLEANUP callback](..\fltkernel\nc-fltkernel-pflt-normalize-context-cleanup.md) | A minifilter driver that provides file names for the filter manager's name cache can register a routine of type PFLT_NORMALIZE_CONTEXT_CLEANUP as the minifilter driver's NormalizeContextCleanupCallback routine. |
| [PFLT_GENERATE_FILE_NAME callback](..\fltkernel\nc-fltkernel-pflt-generate-file-name.md) | A minifilter driver that provides file names for the filter manager's name cache can register a routine of type PFLT_GENERATE_FILE_NAME as the minifilter driver's GenerateFileNameCallback routine. |
| [PFLT_POST_OPERATION_CALLBACK callback](..\fltkernel\nc-fltkernel-pflt-post-operation-callback.md) | A minifilter driver can register one or more routines of type PFLT_POST_OPERATION_CALLBACK to perform completion processing for I/O operations. |
| [PFLT_CONTEXT_CLEANUP_CALLBACK callback](..\fltkernel\nc-fltkernel-pflt-context-cleanup-callback.md) | A minifilter driver can register a routine of type PFLT_CONTEXT_CLEANUP_CALLBACK as the minifilter driver's ContextCleanupCallback routine. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [FLT_FILE_NAME_INFORMATION structure](..\fltkernel\ns-fltkernel--flt-file-name-information.md) | The FLT_FILE_NAME_INFORMATION structure contains file name information. |
| [FLT_PARAMETERS structure](..\fltkernel\ns-fltkernel--flt-parameters.md) | The FLT_PARAMETERS union defines the request-type-specific parameters associated with an I/O operation. |
| [FLT_TAG_DATA_BUFFER structure](..\fltkernel\ns-fltkernel--flt-tag-data-buffer.md) | The FLT_TAG_DATA_BUFFER structure contains information about a reparse point tag. |
| [FLT_VOLUME_PROPERTIES structure](..\fltkernel\ns-fltkernel--flt-volume-properties.md) | The FLT_VOLUME_PROPERTIES structure is passed as a parameter to FltGetVolumeProperties. |
| [FLT_CREATEFILE_TARGET_ECP_CONTEXT structure](..\fltkernel\ns-fltkernel--flt-createfile-target-ecp-context.md) | The FLT_CREATEFILE_TARGET_ECP_CONTEXT structure is an extra create parameter (ECP) used to return reparse target information back to the caller of FltCreateFileEx2. |
| [FLT_RELATED_OBJECTS structure](..\fltkernel\ns-fltkernel--flt-related-objects.md) | The FLT_RELATED_OBJECTS structure contains opaque pointers for the objects associated with an operation. |
| [FLT_CALLBACK_DATA structure](..\fltkernel\ns-fltkernel--flt-callback-data.md) | The FLT_CALLBACK_DATA structure represents an I/O operation. The Filter Manager and minifilters use this structure to initiate and process I/O operations. |
| [FLT_IO_PARAMETER_BLOCK structure](..\fltkernel\ns-fltkernel--flt-io-parameter-block.md) | The FLT_IO_PARAMETER_BLOCK structure contains the parameters for the I/O operation that is represented by a callback data (FLT_CALLBACK_DATA) structure. |
| [FLT_RELATED_CONTEXTS structure](..\fltkernel\ns-fltkernel--flt-related-contexts.md) | The FLT_RELATED_CONTEXTS structure contains a minifilter driver's contexts for the objects associated with an I/O operation. |
| [FLT_RELATED_CONTEXTS_EX structure](..\fltkernel\ns-fltkernel--flt-related-contexts-ex.md) | The FLT_RELATED_CONTEXTS_EX structure contains a minifilter driver's contexts for the objects associated with an I/O operation. |
| [FLT_REGISTRATION structure](..\fltkernel\ns-fltkernel--flt-registration.md) | The FLT_REGISTRATION structure is passed as a parameter to FltRegisterFilter. |
| [FLT_CONTEXT_REGISTRATION structure](..\fltkernel\ns-fltkernel--flt-context-registration.md) | The FLT_CONTEXT_REGISTRATION structure is used to register context types. |
| [FLT_NAME_CONTROL structure](..\fltkernel\ns-fltkernel--flt-name-control.md) | A minifilter that provides file names for the Filter Manager's name cache can use the FLT_NAME_CONTROL structure to manage its name buffers. |
| [FLT_OPERATION_REGISTRATION structure](..\fltkernel\ns-fltkernel--flt-operation-registration.md) | The FLT_OPERATION_REGISTRATION structure is used to register operation callback routines. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [FILTER_REPLY_HEADER structure](..\fltuserstructures\ns-fltuserstructures--filter-reply-header.md) | The FILTER_REPLY_HEADER structure contains message reply header information. |
| [INSTANCE_AGGREGATE_STANDARD_INFORMATION structure](..\fltuserstructures\ns-fltuserstructures--instance-aggregate-standard-information.md) | The caller-allocated INSTANCE_AGGREGATE_STANDARD_INFORMATION structure contains information for either a minifilter driver instance or a legacy filter driver. |
| [FILTER_AGGREGATE_BASIC_INFORMATION structure](..\fltuserstructures\ns-fltuserstructures--filter-aggregate-basic-information.md) | The FILTER_AGGREGATE_BASIC_INFORMATION structure contains basic information for a minifilter or legacy filter driver. |
| [INSTANCE_FULL_INFORMATION structure](..\fltuserstructures\ns-fltuserstructures--instance-full-information.md) | The INSTANCE_FULL_INFORMATION structure contains full information for a minifilter instance. |
| [INSTANCE_PARTIAL_INFORMATION structure](..\fltuserstructures\ns-fltuserstructures--instance-partial-information.md) | The INSTANCE_PARTIAL_INFORMATION structure contains partial information for a minifilter instance. |
| [FILTER_FULL_INFORMATION structure](..\fltuserstructures\ns-fltuserstructures--filter-full-information.md) | The FILTER_FULL_INFORMATION structure contains full information for a minifilter driver. |
| [FILTER_VOLUME_BASIC_INFORMATION structure](..\fltuserstructures\ns-fltuserstructures--filter-volume-basic-information.md) | The caller-allocated FILTER_VOLUME_BASIC_INFORMATION structure contains basic information for a volume. |
| [FILTER_MESSAGE_HEADER structure](..\fltuserstructures\ns-fltuserstructures--filter-message-header.md) | The FILTER_MESSAGE_HEADER structure contains message header information. |
| [FILTER_VOLUME_STANDARD_INFORMATION structure](..\fltuserstructures\ns-fltuserstructures--filter-volume-standard-information.md) | The caller-allocated FILTER_VOLUME_STANDARD_INFORMATION structure contains information for a volume. |
| [FILTER_AGGREGATE_STANDARD_INFORMATION structure](..\fltuserstructures\ns-fltuserstructures--filter-aggregate-standard-information.md) | The FILTER_AGGREGATE_STANDARD_INFORMATION structure contains information about a minifilter or legacy filter driver. |
| [INSTANCE_BASIC_INFORMATION structure](..\fltuserstructures\ns-fltuserstructures--instance-basic-information.md) | The INSTANCE_BASIC_INFORMATION structure contains basic information for a minifilter instance. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [FLT_FILESYSTEM_TYPE enumeration](..\fltuserstructures\ne-fltuserstructures--flt-filesystem-type.md) | The FLT_FILESYSTEM_TYPE enumeration identifies the type of file system being used on a volume. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxLowIoGetBufferAddress function](..\lowio\nf-lowio-rxlowiogetbufferaddress.md) | RxLowIoGetBufferAddress returns the buffer corresponding to the MDL from LowIoContext structure of an RX_CONTEXT structure. |
| [RxLowIoCompletion function](..\lowio\nf-lowio-rxlowiocompletion.md) | RxLowIoCompletion must be called by the network mini-redirector low I/O routines when they complete, if the low I/O routines have initially returned STATUS_PENDING. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxAssociateContextWithMid function](..\midatlax\nf-midatlax-rxassociatecontextwithmid.md) | RxAssociateContextWithMid associates the supplied opaque context with an available multiplex ID (MID) from a MID_ATLAS. |
| [RxCreateMidAtlas function](..\midatlax\nf-midatlax-rxcreatemidatlas.md) | RxCreateMidAtlas allocates a new instance of MID_ATLAS data structure and initializes it. |
| [RxMapMidToContext function](..\midatlax\nf-midatlax-rxmapmidtocontext.md) | RxMapMidToContext maps a Multiplex ID (MID) to its associated context in a MID_ATLAS structure. |
| [RxReassociateMid function](..\midatlax\nf-midatlax-rxreassociatemid.md) | RxReassociateMid reassociates a Multiplex ID (MID) with an alternate context. |
| [RxDestroyMidAtlas function](..\midatlax\nf-midatlax-rxdestroymidatlas.md) | RxDestroyMidAtlas destroys an existing instance of a MID_ATLAS data structure and frees the allocated memory. |
| [RxMapAndDissociateMidFromContext function](..\midatlax\nf-midatlax-rxmapanddissociatemidfromcontext.md) | RxMapAndDissociateMidFromContext maps a Multiplex ID (MID) to its associated context in a MID_ATLAS structure and then disassociates the MID from the context. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxRegisterMinirdr function](..\mrx\nf-mrx-rxregisterminirdr.md) | RxRegisterMinirdr is called by a network mini-redirector driver to register the driver with RDBSS, which adds the registration information to an internal registration table. RDBSS also builds a device object for the network mini-redirector. |
| [RxMakeLateDeviceAvailable function](..\mrx\nf-mrx-rxmakelatedeviceavailable.md) | RxMakeLateDeviceAvailable modifies the device object to make a &#0034;late device&#0034; available. A late device is one that is not created in the driver's load routine. |
| [RxpUnregisterMinirdr function](..\mrx\nf-mrx-rxpunregisterminirdr.md) | RxpUnregisterMinirdr is called by a network mini-redirector driver to de-register the driver with RDBSS and remove the registration information from the internal RDBSS registration table. |
| [RxStopMinirdr function](..\mrx\nf-mrx-rxstopminirdr.md) | RxStopMinirdr is called to stop a network mini-redirector that has previously been started. |
| [RxFsdDispatch function](..\mrx\nf-mrx-rxfsddispatch.md) | RxFsdDispatch implements the file system driver (FSD) dispatch for RDBSS to process an I/O request packet (IRP). |
| [RxStartMinirdr function](..\mrx\nf-mrx-rxstartminirdr.md) | RxStartMinirdr is called to start up a network mini-redirector that has previously called to register with RDBSS. |
| [__RxFillAndInstallFastIoDispatch function](..\mrx\nf-mrx---rxfillandinstallfastiodispatch.md) | RxFillAndInstallFastIoDispatch fills out a fast I/O dispatch vector to be identical with the normal dispatch I/O vector and installs it into the driver object associated with the device object passed. |
| [RxSetDomainForMailslotBroadcast function](..\mrx\nf-mrx-rxsetdomainformailslotbroadcast.md) | RxSetDomainForMailslotBroadcast is called by a network mini-redirector driver to set the domain used for mailslot broadcasts if mailslots are supported by the driver. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxReleaseFcbResourceForThreadInMRx function](..\mrxfcb\nf-mrxfcb-rxreleasefcbresourceforthreadinmrx.md) | RxReleaseFcbResourceForThreadInMRx releases the FCB resource acquired by a network mini-redirector driver with a particular thread ID. |
| [RxReleaseFcbResourceInMRx function](..\mrxfcb\nf-mrxfcb-rxreleasefcbresourceinmrx.md) | RxReleaseFcbResourceInMRx releases the FCB resource acquired by a network mini-redirector driver. |
| [RxAcquireSharedFcbResourceInMRxEx function](..\mrxfcb\nf-mrxfcb-rxacquiresharedfcbresourceinmrxex.md) | RxAcquireSharedFcbResourceInMRxEx acquires the FCB resource for a network mini-redirector driver in shared mode. |
| [RxAcquireExclusiveFcbResourceInMRx function](..\mrxfcb\nf-mrxfcb-rxacquireexclusivefcbresourceinmrx.md) | RxAcquireExclusiveFcbResourceInMRx acquires the FCB resource for a network mini-redirector driver in exclusive mode. |
| [RxAcquireSharedFcbResourceInMRx function](..\mrxfcb\nf-mrxfcb-rxacquiresharedfcbresourceinmrx.md) | RxAcquireSharedFcbResourceInMRx acquires the FCB resource for a network mini-redirector driver in shared mode. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxNameCacheFinalize function](..\namcache\nf-namcache-rxnamecachefinalize.md) | RxNameCacheFinalize releases the storage for all of the NAME_CACHE entries associated with a NAME_CACHE_CONTROL structure. |
| [RxNameCacheActivateEntry function](..\namcache\nf-namcache-rxnamecacheactivateentry.md) | RxNameCacheActivateEntry takes a name cache entry and updates the expiration time and the network mini-redirector context. It then puts the name cache entry on the active list. |
| [RxNameCacheExpireEntryWithShortName function](..\namcache\nf-namcache-rxnamecacheexpireentrywithshortname.md) | RxNameCacheExpireEntryWithShortName expires all of the name cache entries whose name prefix matches the given short file name. |
| [RxNameCacheExpireEntry function](..\namcache\nf-namcache-rxnamecacheexpireentry.md) | RxNameCacheExpireEntry puts a NAME_CACHE entry on the free list for recycling. |
| [RxNameCacheInitialize function](..\namcache\nf-namcache-rxnamecacheinitialize.md) | RxNameCacheInitialize initializes a name cache (NAME_CACHE_CONTROL structure). |
| [RxNameCacheFetchEntry function](..\namcache\nf-namcache-rxnamecachefetchentry.md) | RxNameCacheFetchEntry looks for a match with a specified name string for a NAME_CACHE entry. |
| [RxNameCacheFreeEntry function](..\namcache\nf-namcache-rxnamecachefreeentry.md) | RxNameCacheFreeEntry releases the storage for a NAME_CACHE entry and decrements the count of the NAME_CACHE cache entries associated with a NAME_CACHE_CONTROL structure. |
| [RxNameCacheCreateEntry function](..\namcache\nf-namcache-rxnamecachecreateentry.md) | RxNameCacheCreateEntry allocates and initializes a NAME_CACHE structure with the given name string. |
| [RxNameCacheCheckEntry function](..\namcache\nf-namcache-rxnamecachecheckentry.md) | RxNameCacheCheckEntry checks a name cache entry for validity. A valid entry means that the lifetime has not expired and the MRxContext parameter passes the equality check. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RtlSecondsSince1970ToTime function](..\ntifs\nf-ntifs-rtlsecondssince1970totime.md) | The RtlSecondsSince1970ToTime routine converts the elapsed time, in seconds, since the beginning of 1970 to an absolute system time value. |
| [MmSetAddressRangeModified function](..\ntifs\nf-ntifs-mmsetaddressrangemodified.md) | The MmSetAddressRangeModified routine marks currently valid pages in the specified range of the system cache as modified. |
| [FsRtlAreThereCurrentFileLocks function](..\ntifs\nf-ntifs-fsrtlaretherecurrentfilelocks.md) | The FsRtlAreThereCurrentFileLocks macro checks whether any byte range locks exist for the specified file. |
| [RtlRemoveUnicodePrefix function](..\ntifs\nf-ntifs-rtlremoveunicodeprefix.md) | The RtlRemoveUnicodePrefix routine removes an element from a prefix table. |
| [PsRevertToSelf function](..\ntifs\nf-ntifs-psreverttoself.md) | The PsRevertToSelf routine ends the calling thread's impersonation of a client. |
| [FsRtlIsEcpAcknowledged function](..\ntifs\nf-ntifs-fsrtlisecpacknowledged.md) | The FsRtlIsEcpAcknowledged routine is used to determine if a given extra create parameter (ECP) context structure has been marked as acknowledged. |
| [RtlDecompressBuffer function](..\ntifs\nf-ntifs-rtldecompressbuffer.md) | The RtlDecompressBuffer function decompresses an entire compressed buffer. |
| [MmGetMaximumFileSectionSize function](..\ntifs\nf-ntifs-mmgetmaximumfilesectionsize.md) | The MmGetMaximumFileSectionSize returns the maximum possible size of a file section for the current version of Windows. |
| [KeUnstackDetachProcess function](..\ntifs\nf-ntifs-keunstackdetachprocess.md) | The KeUnstackDetachProcess routine detaches the current thread from the address space of a process and restores the previous attach state. |
| [FsRtlRemoveExtraCreateParameter function](..\ntifs\nf-ntifs-fsrtlremoveextracreateparameter.md) | The FsRtlRemoveExtraCreateParameter routine searches an ECP list for an ECP context structure and, if found, detaches it from the ECP list. |
| [FsRtlValidateReparsePointBuffer function](..\ntifs\nf-ntifs-fsrtlvalidatereparsepointbuffer.md) | The FsRtlValidateReparsePointBuffer routine verifies that the specified reparse point buffer is valid. |
| [FsRtlIncrementCcFastReadResourceMiss function](..\ntifs\nf-ntifs-fsrtlincrementccfastreadresourcemiss.md) | The FsRtlIncrementCcFastReadResourceMiss routine increments the CcFastReadNotPossible performance counter in a per processor control block of cache manager system counters. |
| [FsRtlInitializeExtraCreateParameter function](..\ntifs\nf-ntifs-fsrtlinitializeextracreateparameter.md) | The FsRtlInitializeExtraCreateParameter routine initializes an extra create parameter (ECP) context structure. |
| [CcSetAdditionalCacheAttributesEx function](..\ntifs\nf-ntifs-ccsetadditionalcacheattributesex.md) | Call the CcSetAdditionalCacheAttributesEx routine to enable extended cache behavior on a cached file. |
| [IoSetTopLevelIrp function](..\ntifs\nf-ntifs-iosettoplevelirp.md) | The IoSetTopLevelIrp routine sets the value of the TopLevelIrp field of the current thread. |
| [CcFastCopyRead function](..\ntifs\nf-ntifs-ccfastcopyread.md) | The CcFastCopyRead routine performs a fast copy read from a cached file to a buffer in memory. |
| [RtlAllocateHeap function](..\ntifs\nf-ntifs-rtlallocateheap.md) | The RtlAllocateHeap routine allocates a block of memory from a heap. |
| [FsRtlInsertExtraCreateParameter function](..\ntifs\nf-ntifs-fsrtlinsertextracreateparameter.md) | The FsRtlInsertExtraCreateParameter routine inserts an extra create parameter (ECP) context structure into an ECP list. |
| [CcScheduleReadAhead function](..\ntifs\nf-ntifs-ccschedulereadahead.md) | The CcScheduleReadAhead routine performs read-ahead (also called &#0034;lazy read&#0034;) on a cached file. CcScheduleReadAhead should never be called directly. The CcReadAhead macro should be called instead. |
| [FsRtlGetEcpListFromIrp function](..\ntifs\nf-ntifs-fsrtlgetecplistfromirp.md) | The FsRtlGetEcpListFromIrp routine returns a pointer to an extra create parameter (ECP) context structure list that is associated with a given IRP_MJ_CREATE operation. |
| [PsChargePoolQuota function](..\ntifs\nf-ntifs-pschargepoolquota.md) | The PsChargePoolQuota routine charges pool quota of the specified pool type to the specified process. |
| [SePrivilegeCheck function](..\ntifs\nf-ntifs-seprivilegecheck.md) | The SePrivilegeCheck routine determines whether a specified set of privileges is enabled in the subject's access token. |
| [RtlGetSaclSecurityDescriptor function](..\ntifs\nf-ntifs-rtlgetsaclsecuritydescriptor.md) | The RtlGetSaclSecurityDescriptor routine returns a pointer to the system ACL (SACL) for a security descriptor. |
| [PsImpersonateClient function](..\ntifs\nf-ntifs-psimpersonateclient.md) | The PsImpersonateClient routine causes a server thread to impersonate a client. |
| [FsRtlTeardownPerStreamContexts function](..\ntifs\nf-ntifs-fsrtlteardownperstreamcontexts.md) | The FsRtlTeardownPerStreamContexts routine frees all per-stream context structures associated with a given FSRTL_ADVANCED_FCB_HEADER structure. |
| [IoGetDeviceAttachmentBaseRef function](..\ntifs\nf-ntifs-iogetdeviceattachmentbaseref.md) | The IoGetDeviceAttachmentBaseRef routine returns a pointer to the lowest-level device object in a file system or device driver stack. |
| [RtlGetOwnerSecurityDescriptor function](..\ntifs\nf-ntifs-rtlgetownersecuritydescriptor.md) | The RtlGetOwnerSecurityDescriptor routine returns the owner information for a given security descriptor. |
| [IoIsSystemThread function](..\ntifs\nf-ntifs-ioissystemthread.md) | The IoIsSystemThread routine checks whether a given thread is a system thread. |
| [CcFlushCache function](..\ntifs\nf-ntifs-ccflushcache.md) | The CcFlushCache routine flushes all or a portion of a cached file to disk. |
| [FsRtlInitExtraCreateParameterLookasideList function](..\ntifs\nf-ntifs-fsrtlinitextracreateparameterlookasidelist.md) | The FsRtlInitExtraCreateParameterLookasideList routine initializes a paged or nonpaged pool lookaside list used for the allocation of one or more extra create parameter context structures (ECPs) of fixed size. |
| [CcGetFileObjectFromSectionPtrsRef function](..\ntifs\nf-ntifs-ccgetfileobjectfromsectionptrsref.md) | When passed a pointer to a SECTION_OBJECT_POINTERS structure for a cached file, the CcGetFileObjectFromSectionPtrsRef routine returns a pointer to the file object that the cache manager is using for the cached file. |
| [KeStackAttachProcess function](..\ntifs\nf-ntifs-kestackattachprocess.md) | The KeStackAttachProcess routine attaches the current thread to the address space of the target process. |
| [PsLookupProcessByProcessId function](..\ntifs\nf-ntifs-pslookupprocessbyprocessid.md) | The PsLookupProcessByProcessId routine accepts the process ID of a process and returns a referenced pointer to EPROCESS structure of the process. |
| [CcRepinBcb function](..\ntifs\nf-ntifs-ccrepinbcb.md) | The CcRepinBcb routine pins a buffer control block (BCB) an additional time to prevent it from being freed by a subsequent call to CcUnpinData. |
| [FsRtlIsEcpFromUserMode function](..\ntifs\nf-ntifs-fsrtlisecpfromusermode.md) | The FsRtlIsEcpFromUserMode routine determines whether an extra create parameter (ECP) context structure originated from user mode. |
| [IoGetTopLevelIrp function](..\ntifs\nf-ntifs-iogettoplevelirp.md) | The IoGetTopLevelIrp routine returns the value of the TopLevelIrp field of the current thread. |
| [CcIsThereDirtyData function](..\ntifs\nf-ntifs-ccistheredirtydata.md) | The CcIsThereDirtyData routine determines whether a mounted volume contains any files that have dirty data in the system cache. |
| [RtlLengthSid function](..\ntifs\nf-ntifs-rtllengthsid.md) | The RtlLengthSid routine returns the length, in bytes, of a valid security identifier (SID). |
| [FsRtlSetKernelEaFile function](..\ntifs\nf-ntifs-fsrtlsetkerneleafile.md) | The routine FsRtlQueryKernelEaFile is used to set, modify and/or delete extended attribute (EA) values for a file and synchronously wait for it to complete, returning a result. |
| [CcSetAdditionalCacheAttributes function](..\ntifs\nf-ntifs-ccsetadditionalcacheattributes.md) | Call the CcSetAdditionalCacheAttributes routine to enable or disable read-ahead (also called &#0034;lazy read&#0034;) or write-behind (also called &#0034;lazy write&#0034;) on a cached file. |
| [SeAuditingFileOrGlobalEvents function](..\ntifs\nf-ntifs-seauditingfileorglobalevents.md) | The SeAuditingFileOrGlobalEvents routine determines whether file or global events are currently being audited. |
| [SeTokenGetNoChildProcessRestricted function](..\ntifs\nf-ntifs-setokengetnochildprocessrestricted.md) | The SeTokenGetNoChildProcessRestricted routine determines the state of the no child process mitigation. It is not possible to be enforced and audit-only at the same time. |
| [RtlLengthRequiredSid function](..\ntifs\nf-ntifs-rtllengthrequiredsid.md) | The RtlLengthRequiredSid routine returns the length, in bytes, of the buffer required to store a security identifier (SID) with a specified number of subauthorities. |
| [CcMapData function](..\ntifs\nf-ntifs-ccmapdata.md) | The CcMapData routine maps a specified byte range of a cached file to a buffer in memory. |
| [RtlCompressBuffer function](..\ntifs\nf-ntifs-rtlcompressbuffer.md) | The RtlCompressBuffer function compresses a buffer and can be used by a file system driver to facilitate the implementation of file compression. |
| [IoGetDiskDeviceObject function](..\ntifs\nf-ntifs-iogetdiskdeviceobject.md) | The IoGetDiskDeviceObject routine retrieves a pointer to the disk device object associated with a given file system volume device object. |
| [CcSetFileSizes function](..\ntifs\nf-ntifs-ccsetfilesizes.md) | The CcSetFileSizes routine updates the cache maps and section object for a cached file whose size has changed. |
| [CcCoherencyFlushAndPurgeCache function](..\ntifs\nf-ntifs-cccoherencyflushandpurgecache.md) | The CcCoherencyFlushAndPurgeCache routine flushes and/or purges the cache to ensure cache coherency. |
| [FsRtlIsAnsiCharacterLegal function](..\ntifs\nf-ntifs-fsrtlisansicharacterlegal.md) | The FsRtlIsAnsiCharacterLegal macro determines whether a character is a legal ANSI character. |
| [FsRtlRemovePerStreamContext function](..\ntifs\nf-ntifs-fsrtlremoveperstreamcontext.md) | FsRtlRemovePerStreamContext removes a per-stream context structure from the list of per-stream contexts associated with a file stream. |
| [CcUninitializeCacheMap function](..\ntifs\nf-ntifs-ccuninitializecachemap.md) | The CcUninitializeCacheMap routine stops the caching of a cached file. |
| [RtlDecompressBufferEx function](..\ntifs\nf-ntifs-rtldecompressbufferex.md) | The RtlDecompressBufferEx function decompresses an entire compressed buffer. |
| [FsRtlAllocateExtraCreateParameterList function](..\ntifs\nf-ntifs-fsrtlallocateextracreateparameterlist.md) | The FsRtlAllocateExtraCreateParameterList routine allocates paged pool memory for an ECP_LIST structure and generates a pointer to that structure. |
| [FsRtlIncrementCcFastReadWait function](..\ntifs\nf-ntifs-fsrtlincrementccfastreadwait.md) | The FsRtlIncrementCcFastReadWait routine increments the CcFastReadWait performance counter in a per processor control block of cache manager system counters. |
| [RtlIsNameLegalDOS8Dot3 function](..\ntifs\nf-ntifs-rtlisnamelegaldos8dot3.md) | The RtlIsNameLegalDOS8Dot3 routine determines whether a given name represents a valid short (8.3) file name. |
| [PsReferencePrimaryToken function](..\ntifs\nf-ntifs-psreferenceprimarytoken.md) | The PsReferencePrimaryToken routine increments the reference count of the primary token for the specified process. |
| [FsRtlSetupAdvancedHeader function](..\ntifs\nf-ntifs-fsrtlsetupadvancedheader.md) | The FsRtlSetupAdvancedHeader macro is used by file systems to initialize an FSRTL_ADVANCED_FCB_HEADER structure for use with filter contexts. |
| [CcCopyWrite function](..\ntifs\nf-ntifs-cccopywrite.md) | The CcCopyWrite routine copies data from a user buffer to a cached file. |
| [PsDereferencePrimaryToken function](..\ntifs\nf-ntifs-psdereferenceprimarytoken.md) | The PsDereferencePrimaryToken routine decrements the reference count of a primary token. |
| [CcSetLogHandleForFile function](..\ntifs\nf-ntifs-ccsetloghandleforfile.md) | The CcSetLogHandleForFile routine sets a log handle for a file. |
| [SeQueryInformationToken function](..\ntifs\nf-ntifs-sequeryinformationtoken.md) | The SeQueryInformationToken routine retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information. |
| [IoQueryFileDosDeviceName function](..\ntifs\nf-ntifs-ioqueryfiledosdevicename.md) | The IoQueryFileDosDeviceName routine retrieves an MS-DOS device name for a file. |
| [RtlGenerate8dot3Name function](..\ntifs\nf-ntifs-rtlgenerate8dot3name.md) | The RtlGenerate8dot3Name routine generates a short (8.3) name for the specified long file name. |
| [RtlGetGroupSecurityDescriptor function](..\ntifs\nf-ntifs-rtlgetgroupsecuritydescriptor.md) | The RtlGetGroupSecurityDescriptor routine returns the primary group information for a given security descriptor. |
| [RtlDecompressFragment function](..\ntifs\nf-ntifs-rtldecompressfragment.md) | The RtlDecompressFragment function is used to decompress part of a compressed buffer (that is, a buffer &#0034;fragment&#0034;). |
| [IoGetRequestorSessionId function](..\ntifs\nf-ntifs-iogetrequestorsessionid.md) | The IoGetRequestorSessionId routine returns the session ID for the process that originally requested a given I/O operation. |
| [SeCreateClientSecurity function](..\ntifs\nf-ntifs-secreateclientsecurity.md) | The SeCreateClientSecurity routine initializes a security client context structure with the information needed to call SeImpersonateClientEx. |
| [SecLookupWellKnownSid function](..\ntifs\nf-ntifs-seclookupwellknownsid.md) | SecLookupWellKnownSid accepts a well-known security identifier (SID) type as input and retrieves the local security identifier (SID) for this well known SID. |
| [RtlSetThreadPlaceholderCompatibilityMode function](..\ntifs\nf-ntifs-rtlsetthreadplaceholdercompatibilitymode.md) | RtlSetThreadPlaceholderCompatibilityMode is a routine which sets the placeholder compatibility mode for the current thread. |
| [RtlCreateHeap function](..\ntifs\nf-ntifs-rtlcreateheap.md) | The RtlCreateHeap routine creates a heap object that can be used by the calling process. This routine reserves space in the virtual address space of the process and allocates physical storage for a specified initial portion of this block. |
| [FsRtlTestAnsiCharacter function](..\ntifs\nf-ntifs-fsrtltestansicharacter.md) | The FsRtlTestAnsiCharacter macro determines whether an ANSI or double-byte character set (DBCS) character meets the specified criteria. |
| [RtlFreeHeap function](..\ntifs\nf-ntifs-rtlfreeheap~r1.md) | The RtlFreeHeap routine frees a memory block that was allocated from a heap by RtlAllocateHeap. |
| [IoGetAttachedDevice function](..\ntifs\nf-ntifs-iogetattacheddevice.md) | The IoGetAttachedDevice routine returns a pointer to the highest-level device object associated with the specified device. |
| [PsIsDiskCountersEnabled function](..\ntifs\nf-ntifs-psisdiskcountersenabled.md) | The enabled state of the per process disk I/O counters is returned by the PsIsDiskCountersEnabled routine. |
| [RtlSetOwnerSecurityDescriptor function](..\ntifs\nf-ntifs-rtlsetownersecuritydescriptor.md) | The RtlSetOwnerSecurityDescriptor routine sets the owner information of an absolute-format security descriptor. It replaces any owner information that is already present in the security descriptor. |
| [IsReparseTagNameSurrogate function](..\ntifs\nf-ntifs-isreparsetagnamesurrogate.md) | The IsReparseTagNameSurrogate macro determines whether a tag's associated reparse point is a surrogate for another named entity, such as a volume mount point. |
| [FsRtlRemovePerFileObjectContext function](..\ntifs\nf-ntifs-fsrtlremoveperfileobjectcontext.md) | For a &#0034;legacy&#0034; file system filter driver, the FsRtlRemovePerFileObjectContext function unlinks a per-file-object context information structure from the list of per-file-object contexts previously associated with a file object. |
| [RtlMultiByteToUnicodeN function](..\ntifs\nf-ntifs-rtlmultibytetounicoden.md) | The RtlMultiByteToUnicodeN routine translates the specified source string into a Unicode string, using the current system ANSI code page (ACP). The source string is not necessarily from a multibyte character set. |
| [IoCreateStreamFileObject function](..\ntifs\nf-ntifs-iocreatestreamfileobject.md) | The IoCreateStreamFileObject routine creates a new stream file object. |
| [MmForceSectionClosed function](..\ntifs\nf-ntifs-mmforcesectionclosed.md) | The MmForceSectionClosed routine deletes the data and image sections for a file that is no longer in use. |
| [RtlCreateAcl function](..\ntifs\nf-ntifs-rtlcreateacl.md) | The RtlCreateAcl routine creates and initializes an access control list (ACL). |
| [RtlFindUnicodePrefix function](..\ntifs\nf-ntifs-rtlfindunicodeprefix.md) | The RtlFindUnicodePrefix routine searches for the best match for a given Unicode file name in a prefix table. |
| [RtlCompareMemoryUlong function](..\ntifs\nf-ntifs-rtlcomparememoryulong.md) | The RtlCompareMemoryUlong routine returns how many bytes in a block of memory match a specified pattern. |
| [RtlInitializeSidEx function](..\ntifs\nf-ntifs-rtlinitializesidex.md) | The RtlInitializeSidEx routine initializes a pre-allocated security identifier (SID) structure. |
| [KeRundownQueue function](..\ntifs\nf-ntifs-kerundownqueue.md) | The KeRundownQueue routine cleans up a queue object, flushing any queued entries. |
| [RtlGetAce function](..\ntifs\nf-ntifs-rtlgetace.md) | The RtlGetAce routine obtains a pointer to an access control entry (ACE) in an access control list (ACL). |
| [CcGetFileObjectFromBcb function](..\ntifs\nf-ntifs-ccgetfileobjectfrombcb.md) | Given a pointer to a pinned buffer control block (BCB) for a file, the CcGetFileObjectFromBcb routine returns a pointer to the file object that the cache manager is using for that file. |
| [CcGetFlushedValidData function](..\ntifs\nf-ntifs-ccgetflushedvaliddata.md) | The CcGetFlushedValidData routine determines how much of a cached file has been flushed to disk. |
| [CcPinMappedData function](..\ntifs\nf-ntifs-ccpinmappeddata.md) | The CcPinMappedData routine pins the specified byte range of a cached file. |
| [FsRtlFindExtraCreateParameter function](..\ntifs\nf-ntifs-fsrtlfindextracreateparameter.md) | The FsRtlFindExtraCreateParameter routine searches a given ECP list for an ECP context structure of a given type and returns a pointer to this structure if it is found. |
| [RtlFillMemoryUlonglong function](..\ntifs\nf-ntifs-rtlfillmemoryulonglong~r1.md) | The RtlFillMemoryUlonglong routine fills a given range of memory with one or more repetitions of a given ULONGLONG value. |
| [IoIsOperationSynchronous function](..\ntifs\nf-ntifs-ioisoperationsynchronous.md) | The IoIsOperationSynchronous routine determines whether a given IRP represents a synchronous or asynchronous I/O request. |
| [RtlCreateSecurityDescriptorRelative function](..\ntifs\nf-ntifs-rtlcreatesecuritydescriptorrelative.md) | The RtlCreateSecurityDescriptorRelative routine initializes a new security descriptor in self-relative format. |
| [RtlNtStatusToDosError function](..\ntifs\nf-ntifs-rtlntstatustodoserror.md) | The RtlNtStatusToDosError routine converts the specified NTSTATUS code to its equivalent system error code. |
| [IoRegisterFileSystem function](..\ntifs\nf-ntifs-ioregisterfilesystem.md) | The IoRegisterFileSystem routine adds a file system's control device object to the global file system queue. |
| [MmIsRecursiveIoFault function](..\ntifs\nf-ntifs-mmisrecursiveiofault.md) | The MmIsRecursiveIoFault routine determines whether the current page fault is occurring during an I/O operation. |
| [FsRtlIsSystemPagingFile function](..\ntifs\nf-ntifs-fsrtlissystempagingfile.md) | The FsRtlIsSystemPagingFile routine determines whether a given file is currently a system paging file. |
| [SeAuditingFileEvents function](..\ntifs\nf-ntifs-seauditingfileevents.md) | The SeAuditingFileEvents routine determines whether file open events are currently being audited. |
| [FsRtlIsLeadDbcsCharacter function](..\ntifs\nf-ntifs-fsrtlisleaddbcscharacter.md) | The FsRtlIsLeadDbcsCharacter macro determines whether a character is a lead byte (the first byte of a character) in a double-byte character set (DBCS). |
| [RtlNtStatusToDosErrorNoTeb function](..\ntifs\nf-ntifs-rtlntstatustodoserrornoteb.md) | Reserved for system use. |
| [FsRtlAllocatePoolWithQuotaTag function](..\ntifs\nf-ntifs-fsrtlallocatepoolwithquotatag.md) | The FsRtlAllocatePoolWithQuotaTag routine allocates pool memory, charging quota against the current process. |
| [FsRtlIncrementCcFastMdlReadWait function](..\ntifs\nf-ntifs-fsrtlincrementccfastmdlreadwait.md) | The FsRtlIncrementCcFastMdlReadWait routine increments the cache manager's CcFastMdlReadWait performance counter member in a processor control block (PRCB) object. |
| [ObOpenObjectByPointer function](..\ntifs\nf-ntifs-obopenobjectbypointer.md) | The ObOpenObjectByPointer function opens an object referenced by a pointer and returns a handle to the object. |
| [FsRtlIncrementCcFastReadNotPossible function](..\ntifs\nf-ntifs-fsrtlincrementccfastreadnotpossible.md) | The FsRtlIncrementCcFastReadNotPossible routine increments the CcFastReadNotPossible performance counter in a per processor control block of cache manager system counters. |
| [CcUnpinRepinnedBcb function](..\ntifs\nf-ntifs-ccunpinrepinnedbcb.md) | The CcUnpinRepinnedBcb routine unpins a repinned buffer control block (BCB). |
| [FsRtlLogCcFlushError function](..\ntifs\nf-ntifs-fsrtllogccflusherror.md) | The FsRtlLogCcFlushError routine logs a lost delayed-write error and displays a dialog box to the user. |
| [RtlAbsoluteToSelfRelativeSD function](..\ntifs\nf-ntifs-rtlabsolutetoselfrelativesd.md) | The RtlAbsoluteToSelfRelativeSD routine creates a new security descriptor in self-relative format by using a security descriptor in absolute format as a template. |
| [FsRtlDeregisterUncProvider function](..\ntifs\nf-ntifs-fsrtlderegisteruncprovider.md) | The FsRtlDeregisterUncProvider routine deregisters a redirector that was registered as a Universal Naming Convention (UNC) provider with the multiple UNC provider (MUP). |
| [PsReferenceImpersonationToken function](..\ntifs\nf-ntifs-psreferenceimpersonationtoken.md) | The PsReferenceImpersonationToken routine increments the reference count of the impersonation token for the specified thread. |
| [RtlOemStringToCountedUnicodeString function](..\ntifs\nf-ntifs-rtloemstringtocountedunicodestring.md) | The RtlOemStringToCountedUnicodeString routine translates the specified source string into a Unicode string using the current system OEM code page. |
| [IoGetRequestorProcessId function](..\ntifs\nf-ntifs-iogetrequestorprocessid.md) | The IoGetRequestorProcessId routine returns the unique 32-bit process ID for the thread that originally requested a given I/O operation. |
| [RtlOemStringToUnicodeString function](..\ntifs\nf-ntifs-rtloemstringtounicodestring.md) | The RtlOemStringToUnicodeString routine translates a given source string into a null-terminated Unicode string using the current system OEM code page. |
| [RtlDeleteAce function](..\ntifs\nf-ntifs-rtldeleteace.md) | The RtlDeleteAce routine deletes an access control entry (ACE) from a specified access control list (ACL). |
| [IoCheckQuotaBufferValidity function](..\ntifs\nf-ntifs-iocheckquotabuffervalidity.md) | The IoCheckQuotaBufferValidity routine checks whether the specified quota buffer is valid. |
| [RtlGetCompressionWorkSpaceSize function](..\ntifs\nf-ntifs-rtlgetcompressionworkspacesize.md) | The RtlGetCompressionWorkSpaceSize function is used to determine the correct size of the WorkSpace buffer for the RtlCompressBuffer and RtlDecompressFragment functions. |
| [RtlCaptureContext function](..\ntifs\nf-ntifs-rtlcapturecontext.md) | The RtlCaptureContext function retrieves a context record in the context of the caller. |
| [IoReleaseVpbSpinLock function](..\ntifs\nf-ntifs-ioreleasevpbspinlock.md) | The IoReleaseVpbSpinLock routine releases the Volume Parameter Block (VPB) spin lock. |
| [FsRtlAllocateExtraCreateParameterFromLookasideList function](..\ntifs\nf-ntifs-fsrtlallocateextracreateparameterfromlookasidelist.md) | The FsRtlAllocateExtraCreateParameterFromLookasideList routine allocates memory pool from a given lookaside list for an extra create parameter (ECP) context structure, and generates a pointer to that structure. |
| [CcPurgeCacheSection function](..\ntifs\nf-ntifs-ccpurgecachesection.md) | The CcPurgeCacheSection routine purges all or a portion of a cached file from the system cache. |
| [SeTokenIsRestricted function](..\ntifs\nf-ntifs-setokenisrestricted.md) | The SeTokenIsRestricted routine determines whether a token contains a list of restricting security identifiers (SID). |
| [RtlInitializeUnicodePrefix function](..\ntifs\nf-ntifs-rtlinitializeunicodeprefix.md) | The RtlInitializeUnicodePrefix routine initializes a prefix table. |
| [RtlAddAccessAllowedAceEx function](..\ntifs\nf-ntifs-rtladdaccessallowedaceex.md) | The RtlAddAccessAllowedAceEx routine adds an access-allowed access control entry (ACE) with inheritance ACE flags to an access control list (ACL). The access is granted to the specified security identifier (SID). |
| [FsRtlFreeExtraCreateParameterList function](..\ntifs\nf-ntifs-fsrtlfreeextracreateparameterlist.md) | The FsRtlFreeExtraCreateParameterList routine frees an extra create parameter (ECP) list structure. |
| [RtlAddAccessAllowedAce function](..\ntifs\nf-ntifs-rtladdaccessallowedace.md) | The RtlAddAccessAllowedAce routine adds an access-allowed access control entry (ACE) to an access control list (ACL). The access is granted to the specified security identifier (SID). |
| [KeInitializeQueue function](..\ntifs\nf-ntifs-keinitializequeue.md) | The KeInitializeQueue routine initializes a queue object on which threads can wait for entries. |
| [RtlSubAuthoritySid function](..\ntifs\nf-ntifs-rtlsubauthoritysid.md) | The RtlSubAuthoritySid routine returns a pointer to a specified subauthority of a security identifier (SID). |
| [CcZeroData function](..\ntifs\nf-ntifs-cczerodata.md) | The CcZeroData routine zeros the specified range of bytes in a cached or noncached file. |
| [CcCanIWrite function](..\ntifs\nf-ntifs-cccaniwrite.md) | The CcCanIWrite routine determines whether the caller can write to a cached file. |
| [FsRtlIssueDeviceIoControl function](..\ntifs\nf-ntifs-fsrtlissuedeviceiocontrol.md) | The FsRtlIssueDeviceIoControl routine sends a synchronous device I/O control request to a target device object. |
| [RtlRandom function](..\ntifs\nf-ntifs-rtlrandom.md) | The RtlRandom routine returns a random number that was generated from a given seed value. |
| [RtlIsPartialPlaceholderFileHandle function](..\ntifs\nf-ntifs-rtlispartialplaceholderfilehandle.md) | The RtlIsPartialPlaceholderFileHandle routine determines if a file is a known type of placeholder, based on a file handle. |
| [RtlEqualPrefixSid function](..\ntifs\nf-ntifs-rtlequalprefixsid.md) | The RtlEqualPrefixSid routine determines whether two security-identifier (SID) prefixes are equal. An SID prefix is the entire SID except for the last subauthority value. |
| [SeTokenIsNoChildProcessRestrictionEnforced function](..\ntifs\nf-ntifs-setokenisnochildprocessrestrictionenforced.md) | The SeTokenIsNoChildProcessRestrictionEnforced routine determines if the token carries the no child process restriction. |
| [FsRtlTeardownPerFileContexts function](..\ntifs\nf-ntifs-fsrtlteardownperfilecontexts.md) | File systems call theFsRtlTeardownPerFileContexts routine to free FSRTL_PER_FILE_CONTEXT objects that are associated with a file control block (FCB) structure. |
| [RtlCopySid function](..\ntifs\nf-ntifs-rtlcopysid.md) | The RtlCopySid routine copies the value of a security identifier (SID) to a buffer. |
| [CcCopyRead function](..\ntifs\nf-ntifs-cccopyread.md) | The CcCopyRead routine copies data from a cached file to a user buffer. |
| [FsRtlIsAnsiCharacterLegalFat function](..\ntifs\nf-ntifs-fsrtlisansicharacterlegalfat.md) | The FsRtlIsAnsiCharacterLegalFat macro determines whether an ANSI character is legal for FAT file names. |
| [CcFastCopyWrite function](..\ntifs\nf-ntifs-ccfastcopywrite.md) | The CcFastCopyWrite routine performs a fast copy write from a buffer in memory to a cached file. |
| [CcMdlReadComplete function](..\ntifs\nf-ntifs-ccmdlreadcomplete.md) | The CcMdlReadComplete routine frees the memory descriptor lists (MDL) created by CcMdlRead for a cached file. |
| [FsRtlIsUnicodeCharacterWild function](..\ntifs\nf-ntifs-fsrtlisunicodecharacterwild.md) | The FsRtlIsUnicodeCharacterWild macro determines whether a Unicode character is a wildcard character. |
| [CcSetDirtyPageThreshold function](..\ntifs\nf-ntifs-ccsetdirtypagethreshold.md) | The CcSetDirtyPageThreshold routine sets a per-file dirty page threshold on a cached file. |
| [SeQuerySubjectContextToken function](..\ntifs\nf-ntifs-sequerysubjectcontexttoken.md) | The SeQuerySubjectContextToken macro retrieves the access token for a security subject context. |
| [MmDoesFileHaveUserWritableReferences function](..\ntifs\nf-ntifs-mmdoesfilehaveuserwritablereferences.md) | The MmDoesFileHaveUserWritableReferences function returns the number of writable references for a file object. |
| [FsRtlDeleteExtraCreateParameterLookasideList function](..\ntifs\nf-ntifs-fsrtldeleteextracreateparameterlookasidelist.md) | The FsRtlDeleteExtraCreateParameterLookasideList routine frees an extra create parameter (ECP) lookaside list. |
| [IoEnumerateDeviceObjectList function](..\ntifs\nf-ntifs-ioenumeratedeviceobjectlist.md) | The IoEnumerateDeviceObjectList routine enumerates a driver's device object list. |
| [RtlIsCloudFilesPlaceholder function](..\ntifs\nf-ntifs-rtliscloudfilesplaceholder.md) | The RtlIsCloudFilesPlaceholder routine determines if a file or a directory is a CloudFiles placeholder, based on the FileAttributes and ReparseTag values of the file. |
| [CcRemapBcb function](..\ntifs\nf-ntifs-ccremapbcb.md) | The CcRemapBcb routine maps a buffer control block (BCB) an additional time to preserve it through several calls that perform additional maps and unpins. |
| [RtlCreateUnicodeString function](..\ntifs\nf-ntifs-rtlcreateunicodestring.md) | The RtlCreateUnicodeString routine creates a new counted Unicode string. |
| [RtlEqualSid function](..\ntifs\nf-ntifs-rtlequalsid.md) | The RtlEqualSid routine determines whether two security identifier (SID) values are equal. Two SIDs must match exactly to be considered equal. |
| [KeRemoveQueue function](..\ntifs\nf-ntifs-keremovequeue.md) | The KeRemoveQueue routine gives the calling thread a pointer to a dequeued entry from the given queue object or allows the caller to wait, up to an optional timeout interval, on the queue object. |
| [CcCopyWriteWontFlush function](..\ntifs\nf-ntifs-cccopywritewontflush.md) | The CcCopyWriteWontFlush macro determines whether the amount of data to be copied in a call to CcCopyWrite is small enough not to require immediate flushing to disk if CcCopyWrite is called with Wait set to FALSE. |
| [RtlGenerate8dot3Name function](..\ntifs\nf-ntifs-rtlgenerate8dot3name~r1.md) | The RtlGenerate8dot3Name routine generates a short (8.3) name for the specified long file name. |
| [IoReplaceFileObjectName function](..\ntifs\nf-ntifs-ioreplacefileobjectname.md) | The IoReplaceFileObjectName routine replaces the name of a file object. |
| [RtlGetDaclSecurityDescriptor function](..\ntifs\nf-ntifs-rtlgetdaclsecuritydescriptor.md) | The RtlGetDaclSecurityDescriptor routine returns a pointer to the discretionary ACL (DACL) for a security descriptor. |
| [SeTokenSetNoChildProcessRestricted function](..\ntifs\nf-ntifs-setokensetnochildprocessrestricted.md) | The SeTokenSetNoChildProcessRestricted routine sets the TOKEN_AUDIT_NO_CHILD_PROCESS or TOKEN_AUDIT_NO_CHILD_PROCESS flags in the token. |
| [CcMapData function](..\ntifs\nf-ntifs-ccmapdata~r1.md) | The CcMapData routine maps a specified byte range of a cached file to a buffer in memory. |
| [MapSecurityError function](..\ntifs\nf-ntifs-mapsecurityerror.md) | The MapSecurityError function maps a security interface SECURITY_STATUS status code to a corresponding NSTATUS status code. |
| [FsRtlGetSectorSizeInformation function](..\ntifs\nf-ntifs-fsrtlgetsectorsizeinformation.md) | The FsRtlGetSectorSizeInformation routine retrieves the physical and logical sector size information for a storage volume. |
| [FsRtlGetNextExtraCreateParameter function](..\ntifs\nf-ntifs-fsrtlgetnextextracreateparameter.md) | The FsRtlGetNextExtraCreateParameter routine returns a pointer to the next (or first) extra create parameter (ECP) context structure in a given ECP list. |
| [RtlMultiByteToUnicodeSize function](..\ntifs\nf-ntifs-rtlmultibytetounicodesize.md) | The RtlMultiByteToUnicodeSize routine determines the number of bytes that are required to store the Unicode translation for the specified source string. |
| [RtlNextUnicodePrefix function](..\ntifs\nf-ntifs-rtlnextunicodeprefix.md) | The RtlNextUnicodePrefix routine is used to enumerate the elements in a Unicode prefix table. |
| [SeAppendPrivileges function](..\ntifs\nf-ntifs-seappendprivileges.md) | The SeAppendPrivileges routine appends additional privileges to the privilege set in an access state structure. |
| [IoGetRequestorProcess function](..\ntifs\nf-ntifs-iogetrequestorprocess.md) | The IoGetRequestorProcess routine returns a process pointer for the thread that originally requested a given I/O operation. |
| [MmPrefetchPages function](..\ntifs\nf-ntifs-mmprefetchpages.md) | The MmPrefetchPages routine reads groups of pages from secondary storage in the optimal fashion. |
| [FsRtlMupGetProviderInfoFromFileObject function](..\ntifs\nf-ntifs-fsrtlmupgetproviderinfofromfileobject.md) | The FsRtlMupGetProviderInfoFromFileObject routine gets information about a network redirector that is registered with the multiple UNC provider (MUP) from a file object for a file that is located on a remote file system. |
| [RtlTimeToSecondsSince1970 function](..\ntifs\nf-ntifs-rtltimetosecondssince1970.md) | The RtlTimeToSecondsSince1970 routine converts a given absolute system time value to the elapsed time, in seconds, since the beginning of 1970. |
| [SeReleaseSubjectContext function](..\ntifs\nf-ntifs-sereleasesubjectcontext.md) | The SeReleaseSubjectContext routine releases a subject security context captured by an earlier call to SeCaptureSubjectContext. |
| [CcMdlWriteAbort function](..\ntifs\nf-ntifs-ccmdlwriteabort.md) | The CcMdlWriteAbort routine frees memory descriptor lists (MDL) created by an earlier call to CcPrepareMdlWrite. |
| [FsRtlRemoveDotsFromPath function](..\ntifs\nf-ntifs-fsrtlremovedotsfrompath.md) | The FsRtlRemoveDotsFromPath routine removes unnecessary occurrences of '.' and '..' from the specified path. |
| [RtlSelfRelativeToAbsoluteSD function](..\ntifs\nf-ntifs-rtlselfrelativetoabsolutesd.md) | The RtlSelfRelativeToAbsoluteSD routine creates a new security descriptor in absolute format by using a security descriptor in self-relative format as a template. |
| [CcUnpinData function](..\ntifs\nf-ntifs-ccunpindata.md) | The CcUnpinData routine releases cached file data that was mapped or pinned by an earlier call to CcMapData, CcPinRead, or CcPreparePinWrite. |
| [CcSetBcbOwnerPointer function](..\ntifs\nf-ntifs-ccsetbcbownerpointer.md) | The CcSetBcbOwnerPointer routine sets the owner thread pointer for a pinned buffer control block (BCB). |
| [SeOpenObjectAuditAlarm function](..\ntifs\nf-ntifs-seopenobjectauditalarm.md) | The SeOpenObjectAuditAlarm routine generates audit and alarm messages when an attempt is made to open an object. |
| [FsRtlIsPagingFile function](..\ntifs\nf-ntifs-fsrtlispagingfile.md) | The FsRtlIsPagingFile routine determines whether a given file is a paging file. |
| [RtlIsPartialPlaceholder function](..\ntifs\nf-ntifs-rtlispartialplaceholder.md) | The RtlIsPartialPlaceholder routine determines if a file or a directory is a CloudFiles placeholder, based on the FileAttributes and ReparseTag values of the file. |
| [RtlInitializeSid function](..\ntifs\nf-ntifs-rtlinitializesid.md) | The RtlInitializeSid routine initializes a security identifier (SID) structure. |
| [IoRegisterFsRegistrationChangeEx function](..\ntifs\nf-ntifs-ioregisterfsregistrationchangeex.md) | The IoRegisterFsRegistrationChangeEx routine registers a file system filter driver's notification routine to be called whenever a file system registers or unregisters itself as an active file system. |
| [FsRtlFastLock function](..\ntifs\nf-ntifs-fsrtlfastlock.md) | The FsRtlFastLock macro is used by file systems and filter drivers to request a byte-range lock for a file stream. |
| [SeUnregisterLogonSessionTerminatedRoutine function](..\ntifs\nf-ntifs-seunregisterlogonsessionterminatedroutine.md) | The SeUnregisterLogonSessionTerminatedRoutine routine unregisters a callback routine that was registered by an earlier call to SeRegisterLogonSessionTerminatedRoutine. |
| [RtlInsertUnicodePrefix function](..\ntifs\nf-ntifs-rtlinsertunicodeprefix.md) | The RtlInsertUnicodePrefix routine inserts a new element into a Unicode prefix table. |
| [SeTokenIsAdmin function](..\ntifs\nf-ntifs-setokenisadmin.md) | The SeTokenIsAdmin routine determines whether a token contains the local administrators group. |
| [RtlFillMemoryUlong function](..\ntifs\nf-ntifs-rtlfillmemoryulong~r1.md) | The RtlFillMemoryUlong routine fills the specified range of memory with one or more repetitions of a ULONG value. |
| [RtlDestroyHeap function](..\ntifs\nf-ntifs-rtldestroyheap.md) | The RtlDestroyHeap routine destroys the specified heap object. RtlDestroyHeap decommits and releases all the pages of a private heap object, and it invalidates the handle to the heap. |
| [CcMdlWriteComplete function](..\ntifs\nf-ntifs-ccmdlwritecomplete.md) | The CcMdlWriteComplete routine frees the memory descriptor lists (MDL) created by CcPrepareMdlWrite for a cached file. |
| [RtlOemStringToCountedUnicodeSize function](..\ntifs\nf-ntifs-rtloemstringtocountedunicodesize.md) | The RtlOemStringToCountedUnicodeSize routine determines the size, in bytes, that a given OEM string will be after it is translated into a counted Unicode string. |
| [IoEnumerateRegisteredFiltersList function](..\ntifs\nf-ntifs-ioenumerateregisteredfilterslist.md) | The IoEnumerateRegisteredFiltersList routine enumerates the file system filter drivers that have registered with the system. |
| [IoGetDeviceToVerify function](..\ntifs\nf-ntifs-iogetdevicetoverify.md) | The IoGetDeviceToVerify routine returns a pointer to the device object, representing a removable-media device, that is the target of the given thread's I/O request. |
| [FsRtlQueryKernelEaFile function](..\ntifs\nf-ntifs-fsrtlquerykerneleafile.md) | The routine FsRtlQueryKernelEaFile is used to build an explicit QueryEA request and synchronously wait for it to complete, returning the result. This allows the caller to do this by FileObject instead of a handle. |
| [FsRtlGetSupportedFeatures function](..\ntifs\nf-ntifs-fsrtlgetsupportedfeatures.md) | The FsRtlGetSupportedFeatures routine returns the supported features of a volume attached to the specified device object. |
| [RtlUpcaseUnicodeStringToOemString function](..\ntifs\nf-ntifs-rtlupcaseunicodestringtooemstring.md) | The RtlUpcaseUnicodeStringToOemString routine translates a given Unicode source string into an uppercase OEM string using the current system OEM code page. |
| [FsRtlIncrementCcFastReadNoWait function](..\ntifs\nf-ntifs-fsrtlincrementccfastreadnowait.md) | The FsRtlIncrementCcFastReadNoWait routine increments the CcFastReadNoWait performance counter in a per processor control block of cache manager system counters. |
| [SeFilterToken function](..\ntifs\nf-ntifs-sefiltertoken.md) | The SeFilterToken routine creates a new access token that is a restricted version of an existing access token. |
| [RtlCreateSystemVolumeInformationFolder function](..\ntifs\nf-ntifs-rtlcreatesystemvolumeinformationfolder.md) | The RtlCreateSystemVolumeInformationFolder routine verifies the existence of the &#0034;System Volume Information&#0034; folder on a file system volume. If the folder is not present, then the folder is created. |
| [IoInitializePriorityInfo function](..\ntifs\nf-ntifs-ioinitializepriorityinfo.md) | The IoInitializePriorityInfo routine initializes a structure of type IO_PRIORITY_INFO. |
| [PsDereferenceImpersonationToken function](..\ntifs\nf-ntifs-psdereferenceimpersonationtoken.md) | The PsDereferenceImpersonationToken routine decrements the reference count of an impersonation token. |
| [SeLockSubjectContext function](..\ntifs\nf-ntifs-selocksubjectcontext.md) | The SeLockSubjectContext routine locks the primary and impersonation tokens of a captured subject context. |
| [FsRtlAreVolumeStartupApplicationsComplete function](..\ntifs\nf-ntifs-fsrtlarevolumestartupapplicationscomplete.md) | The FsRtlAreVolumeStartupApplicationsComplete function determines whether volume startup applications have completed processing. |
| [RtlFreeHeap function](..\ntifs\nf-ntifs-rtlfreeheap.md) | The RtlFreeHeap routine frees a memory block that was allocated from a heap by RtlAllocateHeap. |
| [CcWaitForCurrentLazyWriterActivity function](..\ntifs\nf-ntifs-ccwaitforcurrentlazywriteractivity.md) | The CcWaitForCurrentLazyWriterActivity routine puts the caller into a wait state until the current batch of lazy writer activity is completed. |
| [FsRtlLookupPerStreamContext function](..\ntifs\nf-ntifs-fsrtllookupperstreamcontext.md) | The FsRtlLookupPerStreamContext macro retrieves a per-stream context structure for a file stream. |
| [RtlValidSid function](..\ntifs\nf-ntifs-rtlvalidsid.md) | The RtlValidSid routine validates a security identifier (SID) by verifying that the revision number is within a known range and that the number of subauthorities is less than the maximum. |
| [PsReturnPoolQuota function](..\ntifs\nf-ntifs-psreturnpoolquota.md) | The PsReturnPoolQuota routine returns pool quota of the specified pool type to the specified process. |
| [RtlFillMemoryUlong function](..\ntifs\nf-ntifs-rtlfillmemoryulong.md) | The RtlFillMemoryUlong routine fills the specified range of memory with one or more repetitions of a ULONG value. |
| [RtlUpcaseUnicodeStringToCountedOemString function](..\ntifs\nf-ntifs-rtlupcaseunicodestringtocountedoemstring.md) | The RtlUpcaseUnicodeStringToCountedOemString routine translates a given Unicode source string into an uppercase counted OEM string using the current system OEM code page. |
| [CcPinRead function](..\ntifs\nf-ntifs-ccpinread.md) | The CcPinRead routine pins the specified byte range of a cached file and reads the pinned data into a buffer in memory. |
| [FsRtlInsertPerStreamContext function](..\ntifs\nf-ntifs-fsrtlinsertperstreamcontext.md) | The FsRtlInsertPerStreamContext routine associates a file system filter driver's per-stream context structure with a file stream. |
| [SecMakeSPNEx function](..\ntifs\nf-ntifs-secmakespnex.md) | SecMakeSPNEx creates a service provider name string that can be used when communicating with specific security service providers. |
| [RtlUnicodeToOemN function](..\ntifs\nf-ntifs-rtlunicodetooemn.md) | The RtlUnicodeToOemN routine translates a given Unicode string to an OEM string, using the current system OEM code page. |
| [FsRtlIsDaxVolume function](..\ntifs\nf-ntifs-fsrtlisdaxvolume.md) | This routine queries if the specified file is on a direct access (DAX) volume. |
| [KeInsertHeadQueue function](..\ntifs\nf-ntifs-keinsertheadqueue.md) | The KeInsertHeadQueue routine inserts an entry at the head of the given queue if it cannot immediately use the entry to satisfy a thread wait. |
| [SecLookupAccountSid function](..\ntifs\nf-ntifs-seclookupaccountsid.md) | SecLookupAccountSid accepts a security identifier (SID) as input. It retrieves the name of the account for this SID and the name of the first domain on which this SID is found. |
| [RtlOemStringToUnicodeSize function](..\ntifs\nf-ntifs-rtloemstringtounicodesize.md) | The RtlOemStringToUnicodeSize routine determines the size, in bytes, that a given OEM string will be after it is translated into a null-terminated Unicode string. |
| [RtlSetGroupSecurityDescriptor function](..\ntifs\nf-ntifs-rtlsetgroupsecuritydescriptor.md) | The RtlSetGroupSecurityDescriptor routine sets the primary group information of an absolute-format security descriptor. It replaces any primary group information that is already present in the security descriptor. |
| [IoUnregisterFsRegistrationChange function](..\ntifs\nf-ntifs-iounregisterfsregistrationchange.md) | The IoUnregisterFsRegistrationChange routine unregisters file system filter driver's file system registration change notification routine. |
| [PsIsThreadTerminating function](..\ntifs\nf-ntifs-psisthreadterminating.md) | The PsIsThreadTerminating routine checks whether a thread is terminating. |
| [GetSecurityUserInfo function](..\ntifs\nf-ntifs-getsecurityuserinfo.md) | The GetSecurityUserInfo function retrieves information about a logon session. |
| [IoThreadToProcess function](..\ntifs\nf-ntifs-iothreadtoprocess.md) | The IoThreadToProcess routine returns a pointer to the process for the specified thread. |
| [CcPreparePinWrite function](..\ntifs\nf-ntifs-ccpreparepinwrite.md) | The CcPreparePinWrite routine pins the specified byte range of a cached file for write access. |
| [IoCreateStreamFileObjectEx function](..\ntifs\nf-ntifs-iocreatestreamfileobjectex.md) | The IoCreateStreamFileObjectEx routine creates a new stream file object. |
| [SeUnlockSubjectContext function](..\ntifs\nf-ntifs-seunlocksubjectcontext.md) | The SeUnlockSubjectContext routine unlocks the tokens of a captured subject context that were locked by a call to SeLockSubjectContext. |
| [CcCopyWriteWontFlush function](..\ntifs\nf-ntifs-cccopywritewontflush~r1.md) | The CcCopyWriteWontFlush macro determines whether the amount of data to be copied in a call to CcCopyWrite is small enough not to require immediate flushing to disk if CcCopyWrite is called with Wait set to FALSE. |
| [FsRtlChangeBackingFileObject function](..\ntifs\nf-ntifs-fsrtlchangebackingfileobject.md) | The FsRtlChangeBackingFileObject routine replaces the current file object with a new file object. |
| [FsRtlAcknowledgeEcp function](..\ntifs\nf-ntifs-fsrtlacknowledgeecp.md) | The FsRtlAcknowledgeEcp routine marks an extra create parameter (ECP) context structure as acknowledged. |
| [CcSetReadAheadGranularity function](..\ntifs\nf-ntifs-ccsetreadaheadgranularity.md) | The CcSetReadAheadGranularity routine sets the read-ahead granularity for a cached file. |
| [KeInsertQueue function](..\ntifs\nf-ntifs-keinsertqueue.md) | The KeInsertQueue routine inserts an entry at the tail of the given queue if it cannot immediately use the entry to satisfy a thread wait. |
| [IoSetDeviceToVerify function](..\ntifs\nf-ntifs-iosetdevicetoverify.md) | The IoSetDeviceToVerify routine specifies a device object to be verified. The specified device object represents a removable media device. |
| [RtlCaptureStackBackTrace function](..\ntifs\nf-ntifs-rtlcapturestackbacktrace.md) | The RtlCaptureStackBackTrace routine captures a stack back trace by walking up the stack and recording the information for each frame. |
| [RtlUnicodeStringToOemString function](..\ntifs\nf-ntifs-rtlunicodestringtooemstring.md) | The RtlUnicodeStringToOemString routine translates a given Unicode source string into an OEM string using the current system OEM code page. |
| [FsRtlInsertPerFileObjectContext function](..\ntifs\nf-ntifs-fsrtlinsertperfileobjectcontext.md) | For a &#0034;legacy&#0034; file system filter driver, the FsRtlInsertPerFileObjectContext function associates context information with a file object. |
| [PsUpdateDiskCounters function](..\ntifs\nf-ntifs-psupdatediskcounters.md) | The PsUpdateDiskCounters routine updates the disk I/O counters of a given process. |
| [IoAcquireVpbSpinLock function](..\ntifs\nf-ntifs-ioacquirevpbspinlock.md) | The IoAcquireVpbSpinLock routine acquires the Volume Parameter Block (VPB) spin lock. |
| [IoRegisterFsRegistrationChangeMountAware function](..\ntifs\nf-ntifs-ioregisterfsregistrationchangemountaware.md) | The IoRegisterFsRegistrationChangeMountAware routine registers a file system filter driver's notification routine. This notification routine is called whenever a file system registers or unregisters itself as an active file system. |
| [RtlUpcaseUnicodeToOemN function](..\ntifs\nf-ntifs-rtlupcaseunicodetooemn.md) | The RtlUpcaseUnicodeToOemN routine translates a given Unicode string into an uppercase OEM string, using the current system OEM code page. |
| [IoCreateStreamFileObjectEx2 function](..\ntifs\nf-ntifs-iocreatestreamfileobjectex2.md) | The IoCreateStreamFileObjectEx2 routine creates a new stream file object with create options for a target device object. |
| [RtlUpcaseUnicodeToMultiByteN function](..\ntifs\nf-ntifs-rtlupcaseunicodetomultibyten.md) | The RtlUpcaseUnicodeToMultiByteN routine translates the specified Unicode string into a new uppercase character string, using the current system ANSI code page (ACP). The translated string is not necessarily from a multibyte character set. |
| [RtlUnicodeToMultiByteSize function](..\ntifs\nf-ntifs-rtlunicodetomultibytesize.md) | The RtlUnicodeToMultiByteSize routine determines the number of bytes that are required to store the multibyte translation for the specified Unicode string. The translation is assumed to use the current system ANSI code page (ACP). |
| [FsRtlSetupAdvancedHeaderEx function](..\ntifs\nf-ntifs-fsrtlsetupadvancedheaderex.md) | The FsRtlSetupAdvancedHeaderEx macro is used by file systems to initialize an FSRTL_ADVANCED_FCB_HEADER structure for use with both stream and file contexts. |
| [FsRtlGetPerStreamContextPointer function](..\ntifs\nf-ntifs-fsrtlgetperstreamcontextpointer.md) | The FsRtlGetPerStreamContextPointer macro returns the file system's stream context for a file stream. |
| [RtlAddAce function](..\ntifs\nf-ntifs-rtladdace.md) | The RtlAddAce routine adds one or more access control entries (ACEs) to a specified access control list (ACL). |
| [CcUnpinDataForThread function](..\ntifs\nf-ntifs-ccunpindataforthread.md) | The CcUnpinDataForThread routine releases pages of a cached file whose buffer control block (BCB) was modified by an earlier call to CcSetBcbOwnerPointer. |
| [SeQuerySecurityDescriptorInfo function](..\ntifs\nf-ntifs-sequerysecuritydescriptorinfo.md) | The SeQuerySecurityDescriptorInfo routine retrieves a copy of an object's security descriptor. |
| [FsRtlAllocatePoolWithTag function](..\ntifs\nf-ntifs-fsrtlallocatepoolwithtag.md) | The FsRtlAllocatePoolWithTag routine allocates pool memory. |
| [SeCreateClientSecurityFromSubjectContext function](..\ntifs\nf-ntifs-secreateclientsecurityfromsubjectcontext.md) | The SeCreateClientSecurityFromSubjectContext routine retrieves the access token for a security subject context and uses the result to initialize a security client context with the information needed to call SeImpersonateClientEx. |
| [SeDeleteClientSecurity function](..\ntifs\nf-ntifs-sedeleteclientsecurity.md) | The SeDeleteClientSecurity routine deletes a client security context. |
| [CcPurgeCacheSection function](..\ntifs\nf-ntifs-ccpurgecachesection~r1.md) | The CcPurgeCacheSection routine purges all or a portion of a cached file from the system cache. |
| [SeSetSecurityDescriptorInfo function](..\ntifs\nf-ntifs-sesetsecuritydescriptorinfo.md) | The SeSetSecurityDescriptorInfo routine sets an object's security descriptor. |
| [PsLookupThreadByThreadId function](..\ntifs\nf-ntifs-pslookupthreadbythreadid.md) | The PsLookupThreadByThreadId routine accepts the thread ID of a thread and returns a referenced pointer to the ETHREAD structure of the thread. |
| [IoCheckEaBufferValidity function](..\ntifs\nf-ntifs-iocheckeabuffervalidity.md) | The IoCheckEaBufferValidity routine checks whether the specified extended attribute (EA) buffer is valid. |
| [FsRtlIsAnsiCharacterWild function](..\ntifs\nf-ntifs-fsrtlisansicharacterwild.md) | The FsRtlIsAnsiCharacterWild macro determines whether an ANSI character is a wildcard character. |
| [RtlFillMemoryUlonglong function](..\ntifs\nf-ntifs-rtlfillmemoryulonglong.md) | The RtlFillMemoryUlonglong routine fills a given range of memory with one or more repetitions of a given ULONGLONG value. |
| [ObQueryNameString function](..\ntifs\nf-ntifs-obquerynamestring.md) | The ObQueryNameString routine supplies the name, if there is one, of a given object to which the caller has a pointer. |
| [RtlOemToUnicodeN function](..\ntifs\nf-ntifs-rtloemtounicoden.md) | The RtlOemToUnicodeN routine translates the specified source string into a Unicode string, using the current system OEM code page. |
| [FsRtlCreateSectionForDataScan function](..\ntifs\nf-ntifs-fsrtlcreatesectionfordatascan.md) | The FsRtlCreateSectionForDataScan routine creates a section object. |
| [IoCreateStreamFileObjectLite function](..\ntifs\nf-ntifs-iocreatestreamfileobjectlite.md) | The IoCreateStreamFileObjectLite routine creates a new stream file object, but does not cause an IRP_MJ_CLEANUP request to be sent to the file system driver stack. |
| [FsRtlSetEcpListIntoIrp function](..\ntifs\nf-ntifs-fsrtlsetecplistintoirp.md) | The FsRtlSetEcpListIntoIrp routine attaches an extra create parameter (ECP) context structure list to an IRP_MJ_CREATE operation. |
| [RtlIsPartialPlaceholderFileInfo function](..\ntifs\nf-ntifs-rtlispartialplaceholderfileinfo.md) | The RtlIsPartialPlaceholderFileInfo routine determines if a file is a known type of placeholder, based on the information returned by NtQueryInformationFile or NtQueryDirectoryFile. |
| [MmFlushImageSection function](..\ntifs\nf-ntifs-mmflushimagesection.md) | The MmFlushImageSection routine flushes the image section for a file. |
| [RtlCopyLuid function](..\ntifs\nf-ntifs-rtlcopyluid.md) | The RtlCopyLuid routine copies a locally unique identifier (LUID) to a buffer. |
| [FsRtlFreeExtraCreateParameter function](..\ntifs\nf-ntifs-fsrtlfreeextracreateparameter.md) | The FsRtlFreeExtraCreateParameter routine frees the memory for an ECP context structure. |
| [RtlTimeToSecondsSince1980 function](..\ntifs\nf-ntifs-rtltimetosecondssince1980.md) | The RtlTimeToSecondsSince1980 routine converts a given absolute system time value to the elapsed time, in seconds, since the beginning of 1980. |
| [RtlDowncaseUnicodeString function](..\ntifs\nf-ntifs-rtldowncaseunicodestring.md) | The RtlDowncaseUnicodeString routine converts the specified Unicode source string to lowercase. The translation conforms to the current system locale information. |
| [CcGetDirtyPages function](..\ntifs\nf-ntifs-ccgetdirtypages.md) | The CcGetDirtyPages routine searches for dirty pages in all files that match a given log handle. |
| [SeMarkLogonSessionForTerminationNotification function](..\ntifs\nf-ntifs-semarklogonsessionforterminationnotification.md) | The SeMarkLogonSessionForTerminationNotification routine marks a logon session so that the caller's registered callback routine is called when the logon session terminates. |
| [SeQueryAuthenticationIdToken function](..\ntifs\nf-ntifs-sequeryauthenticationidtoken.md) | The SeQueryAuthenticationIdToken routine retrieves the authentication ID of an access token. |
| [IsReparseTagMicrosoft function](..\ntifs\nf-ntifs-isreparsetagmicrosoft.md) | The IsReparseTagMicrosoft macro determines whether a reparse point tag indicates a Microsoft reparse point. |
| [RtlFreeOemString function](..\ntifs\nf-ntifs-rtlfreeoemstring.md) | The RtlFreeOemString routine releases storage that was allocated by any of the Rtl..ToOemString routines. |
| [SeDeleteObjectAuditAlarm function](..\ntifs\nf-ntifs-sedeleteobjectauditalarm.md) | The SeDeleteObjectAuditAlarm routine generates audit and alarm messages for an object that is marked for deletion. |
| [IoGetLowerDeviceObject function](..\ntifs\nf-ntifs-iogetlowerdeviceobject.md) | The IoGetLowerDeviceObject routine returns a pointer to the next-lower-level device object on the driver stack. |
| [FsRtlInsertPerFileContext function](..\ntifs\nf-ntifs-fsrtlinsertperfilecontext.md) | The FsRtlInsertPerFileContext routine associates a FSRTL_PER_FILE_CONTEXT object with a driver-specified context object for a file. |
| [FsRtlCancellableWaitForMultipleObjects function](..\ntifs\nf-ntifs-fsrtlcancellablewaitformultipleobjects.md) | The FsRtlCancellableWaitForMultipleObjects routine executes a cancelable wait operation (a wait that can be terminated) on one or more dispatcher objects. |
| [RtlAppendStringToString function](..\ntifs\nf-ntifs-rtlappendstringtostring.md) | The RtlAppendStringToString routine concatenates two counted strings. It copies bytes from the source up to the length of the destination buffer. |
| [SeOpenObjectForDeleteAuditAlarm function](..\ntifs\nf-ntifs-seopenobjectfordeleteauditalarm.md) | The SeOpenObjectForDeleteAuditAlarm routine generates audit and alarm messages when an attempt is made to open an object for deletion. |
| [CcGetFileObjectFromSectionPtrs function](..\ntifs\nf-ntifs-ccgetfileobjectfromsectionptrs.md) | Given a pointer to the section object pointers for a cached file, the CcGetFileObjectFromSectionPtrs routine returns a pointer to the file object that the cache manager is using for the file. |
| [FsRtlAllocateExtraCreateParameter function](..\ntifs\nf-ntifs-fsrtlallocateextracreateparameter.md) | The FsRtlAllocateExtraCreateParameter routine allocates memory for a user-defined extra create parameter (ECP) context structure and generates a pointer to that structure. |
| [CcCopyReadEx function](..\ntifs\nf-ntifs-cccopyreadex.md) | The CcCopyReadEx routine copies data from a cached file to a user buffer. The I/O byte count for the operation is charged to the issuing thread. |
| [FsRtlCancellableWaitForSingleObject function](..\ntifs\nf-ntifs-fsrtlcancellablewaitforsingleobject.md) | The FsRtlCancellableWaitForSingleObject routine executes a cancelable wait operation (a wait that can be terminated) on a dispatcher object. |
| [RtlUnicodeToMultiByteN function](..\ntifs\nf-ntifs-rtlunicodetomultibyten.md) | The RtlUnicodeToMultiByteN routine translates the specified Unicode string into a new character string, using the current system ANSI code page (ACP). The translated string is not necessarily from a multibyte character set. |
| [FsRtlPrepareToReuseEcp function](..\ntifs\nf-ntifs-fsrtlpreparetoreuseecp.md) | The FsRtlPrepareToReuseEcp routine resets an extra create parameter (ECP) context structure, which prepares it for reuse. |
| [FsRtlInitializeExtraCreateParameterList function](..\ntifs\nf-ntifs-fsrtlinitializeextracreateparameterlist.md) | The FsRtlInitializeExtraCreateParameterList routine initializes an extra create parameter (ECP) context structure list. |
| [FsRtlRemovePerFileContext function](..\ntifs\nf-ntifs-fsrtlremoveperfilecontext.md) | The FsRtlRemovePerFileContext routine returns a pointer to a FSRTL_PER_FILE_CONTEXT object that is associated with a file. |
| [FsRtlIsAnsiCharacterLegalNtfs function](..\ntifs\nf-ntifs-fsrtlisansicharacterlegalntfs.md) | The FsRtlIsAnsiCharacterLegalNtfs macro determines whether an ANSI character is legal for NTFS file names. |
| [CcPrepareMdlWrite function](..\ntifs\nf-ntifs-ccpreparemdlwrite.md) | The CcPrepareMdlWrite routine provides direct access to cached file memory so that the caller can write data to the file. |
| [FsRtlCompleteRequest function](..\ntifs\nf-ntifs-fsrtlcompleterequest.md) | The FsRtlCompleteRequest macro completes an IRP with the specified status. |
| [FsRtlQueryCachedVdl function](..\ntifs\nf-ntifs-fsrtlquerycachedvdl.md) | The current valid data length (VDL) for a cached file is retrieved with the FsRtlQueryCachedVdl routine. |
| [SeRegisterLogonSessionTerminatedRoutine function](..\ntifs\nf-ntifs-seregisterlogonsessionterminatedroutine.md) | The SeRegisterLogonSessionTerminatedRoutine routine registers a callback routine to be called when a logon session terminates. A logon session terminates when the last token referencing the logon session is deleted. |
| [RtlUnicodeStringToCountedOemString function](..\ntifs\nf-ntifs-rtlunicodestringtocountedoemstring.md) | The RtlUnicodeStringToCountedOemString routine translates the specified Unicode source string into a counted OEM string using the current system OEM code page. |
| [PsGetProcessExitTime function](..\ntifs\nf-ntifs-psgetprocessexittime.md) | The PsGetProcessExitTime routine returns the exit time for the current process. |
| [SeSetSecurityDescriptorInfoEx function](..\ntifs\nf-ntifs-sesetsecuritydescriptorinfoex.md) | The SeSetSecurityDescriptorInfoEx routine modifies an object's security descriptor and specifies whether the object supports automatic inheritance of access control entries (ACE). |
| [RtlDecompressBufferEx2 function](..\ntifs\nf-ntifs-rtldecompressbufferex2.md) | The RtlDecompressBufferEx2 function decompresses an entire compressed buffer, using multiple processors where possible. Multiple processor support is only implemented for kernel mode callers. |
| [SecLookupAccountName function](..\ntifs\nf-ntifs-seclookupaccountname.md) | SecLookupAccountName accepts an account as input and retrieves a security identifier (SID) for the account and the name of the domain on which the account was found. |
| [FsRtlLookupPerFileContext function](..\ntifs\nf-ntifs-fsrtllookupperfilecontext.md) | The FsRtlLookupPerFileContext routine returns a pointer to a FSRTL_PER_FILE_CONTEXT object that is associated with a specified file. |
| [SecMakeSPN function](..\ntifs\nf-ntifs-secmakespn.md) | SecMakeSPN creates a service provider name string that can be used when communicating with specific security service providers. |
| [RtlConvertSidToUnicodeString function](..\ntifs\nf-ntifs-rtlconvertsidtounicodestring.md) | The RtlConvertSidToUnicodeString routine generates a printable Unicode string representation of a security identifier (SID). |
| [CcCopyWriteEx function](..\ntifs\nf-ntifs-cccopywriteex.md) | The CcCopyWriteEx routine copies data from a user buffer to a cached file. The I/O byte count for the operation is charged to the issuing thread. |
| [FsRtlIsAnsiCharacterLegalHpfs function](..\ntifs\nf-ntifs-fsrtlisansicharacterlegalhpfs.md) | The FsRtlIsAnsiCharacterLegalHpfs macro determines whether an ANSI character is legal for HPFS file names. |
| [IoRegisterFsRegistrationChange function](..\ntifs\nf-ntifs-ioregisterfsregistrationchange.md) | The IoRegisterFsRegistrationChange routine registers a file system filter driver's notification routine to be called whenever a file system registers or unregisters itself as an active file system. |
| [RtlUnicodeStringToOemSize function](..\ntifs\nf-ntifs-rtlunicodestringtooemsize.md) | The RtlUnicodeStringToOemSize routine determines the size, in bytes, that a given Unicode string will be after it is translated into an OEM string. |
| [FsRtlInitPerStreamContext function](..\ntifs\nf-ntifs-fsrtlinitperstreamcontext.md) | The FsRtlInitPerStreamContext macro initializes a filter driver context structure. |
| [RtlQueryThreadPlaceholderCompatibilityMode function](..\ntifs\nf-ntifs-rtlquerythreadplaceholdercompatibilitymode.md) | RtlQueryThreadPlaceholderCompatibilityMode is a routine which returns the placeholder compatibility mode for the current thread. |
| [ObIsKernelHandle function](..\ntifs\nf-ntifs-obiskernelhandle.md) | The ObIsKernelHandle routine determines whether the specified handle is a kernel handle. |
| [RtlDecompressFragmentEx function](..\ntifs\nf-ntifs-rtldecompressfragmentex.md) | The RtlDecompressFragmentEx function is used to decompress part of a compressed buffer (that is, a buffer &#0034;fragment&#0034;), using multiple processors where possible. |
| [RtlRandomEx function](..\ntifs\nf-ntifs-rtlrandomex.md) | The RtlRandomEx routine returns a random number that was generated from a given seed value. |
| [FsRtlMupGetProviderIdFromName function](..\ntifs\nf-ntifs-fsrtlmupgetprovideridfromname.md) | The FsRtlMupGetProviderIdFromName routine gets the provider identifier of a network redirector that is registered with the multiple UNC provider (MUP) from the device name of the network redirector. |
| [RtlIsValidOemCharacter function](..\ntifs\nf-ntifs-rtlisvalidoemcharacter.md) | The RtlIsValidOemCharacter routine determines if the specified Unicode character can be mapped to a valid OEM character. |
| [FsRtlLookupPerFileObjectContext function](..\ntifs\nf-ntifs-fsrtllookupperfileobjectcontext.md) | For a &#0034;legacy&#0034; file system filter driver, the FsRtlLookupPerFileObjectContext function retrieves context information previously associated with a file object. |
| [CcScheduleReadAheadEx function](..\ntifs\nf-ntifs-ccschedulereadaheadex.md) | The CcScheduleReadAheadEx routine performs read-ahead (also called &#0034;lazy read&#0034;) on a cached file. The I/O byte count for the operation is charged to the issuing thread. |
| [CcInitializeCacheMap function](..\ntifs\nf-ntifs-ccinitializecachemap.md) | File systems call the CcInitializeCacheMap routine to cache a file. |
| [CcSetDirtyPinnedData function](..\ntifs\nf-ntifs-ccsetdirtypinneddata.md) | The CcSetDirtyPinnedData routine marks as dirty the buffer control block (BCB) for a pinned buffer whose contents have been modified. |
| [SeSetAccessStateGenericMapping function](..\ntifs\nf-ntifs-sesetaccessstategenericmapping.md) | The SeSetAccessStateGenericMapping routine sets the generic mapping field of an ACCESS_STATE structure. |
| [FsRtlIsAnsiCharacterLegalNtfsStream function](..\ntifs\nf-ntifs-fsrtlisansicharacterlegalntfsstream.md) | The FsRtlIsAnsiCharacterLegalNtfsStream macro determines whether an ANSI character is legal for NTFS stream names. |
| [FsRtlRegisterFileSystemFilterCallbacks function](..\ntifs\nf-ntifs-fsrtlregisterfilesystemfiltercallbacks.md) | File system filter drivers and file systems call the FsRtlRegisterFileSystemFilterCallbacks routine to register notification callback routines to be invoked when the underlying file system performs certain operations. |
| [SeCaptureSubjectContext function](..\ntifs\nf-ntifs-secapturesubjectcontext.md) | The SeCaptureSubjectContext routine captures the security context of the calling thread for access validation and auditing. |
| [SeImpersonateClientEx function](..\ntifs\nf-ntifs-seimpersonateclientex.md) | The SeImpersonateClientEx routine causes a thread to impersonate a user. |
| [MmCanFileBeTruncated function](..\ntifs\nf-ntifs-mmcanfilebetruncated.md) | The MmCanFileBeTruncated routine checks whether a file can be truncated. |
| [RtlSecondsSince1980ToTime function](..\ntifs\nf-ntifs-rtlsecondssince1980totime.md) | The RtlSecondsSince1980ToTime routine converts the elapsed time, in seconds, since the beginning of 1980 to an absolute system time value. |
| [CcIsThereDirtyDataEx function](..\ntifs\nf-ntifs-ccistheredirtydataex.md) | The CcIsThereDirtyDataEx routine determines whether a volume contains any files that have dirty data in the system cache. |
| [IoUnregisterFileSystem function](..\ntifs\nf-ntifs-iounregisterfilesystem.md) | The IoUnregisterFileSystem routine removes a file system's control device object from the global file system queue. |
| [CcDeferWrite function](..\ntifs\nf-ntifs-ccdeferwrite.md) | The CcDeferWrite routine defers writing to a cached file. |
| [IoVerifyVolume function](..\ntifs\nf-ntifs-ioverifyvolume.md) | The IoVerifyVolume routine sends a volume verify request to the given removable-media device. |
| [SecMakeSPNEx2 function](..\ntifs\nf-ntifs-secmakespnex2.md) | SecMakeSPNEx2 creates a service provider name string that can be used when it communicates with specific security service providers. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_VOLSNAP_FLUSH_AND_HOLD_WRITES IOCTL](..\ntifs\ni-ntifs-ioctl-volsnap-flush-and-hold-writes.md) | The IOCTL_VOLSNAP_FLUSH_AND_HOLD_WRITES control code is sent to force a flush of a file system before a volume shadow copy occurs. |
| [IOCTL_REDIR_QUERY_PATH IOCTL](..\ntifs\ni-ntifs-ioctl-redir-query-path.md) | The IOCTL_REDIR_QUERY_PATH control code is sent by the multiple UNC provider (MUP) to network redirectors to determine which provider can handle a specific UNC path in a name-based operation, typically an IRP_MJ_CREATE request. |
| [IOCTL_REDIR_QUERY_PATH_EX IOCTL](..\ntifs\ni-ntifs-ioctl-redir-query-path-ex.md) | The IOCTL_REDIR_QUERY_PATH_EX control code is sent by the multiple UNC provider (MUP) on Windows Vista or later to network redirectors to determine which provider can handle a specific UNC path in a name-based operation, typically an IRP_MJ_CREATE request. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [TOKEN_SOURCE structure](..\ntifs\ns-ntifs--token-source.md) | TOKEN_SOURCE identifies the source of an access token. |
| [FSCTL_OFFLOAD_WRITE_INPUT structure](..\ntifs\ns-ntifs--fsctl-offload-write-input.md) | The FSCTL_OFFLOAD_WRITE_INPUT structure contains the input for the FSCTL_OFFLOAD_WRITE control code request. |
| [PUBLIC_OBJECT_BASIC_INFORMATION structure](..\ntifs\ns-ntifs--public-object-basic-information.md) | The PUBLIC_OBJECT_BASIC_INFORMATION structure holds a subset of the full information that is available for an object. |
| [QUERY_FILE_LAYOUT_OUTPUT structure](..\ntifs\ns-ntifs--query-file-layout-output.md) | The QUERY_FILE_LAYOUT_OUTPUT structure serves as a header for the file layout entries that are returned from a FSCTL_QUERY_FILE_LAYOUT request. |
| [REFS_SMR_VOLUME_INFO_OUTPUT structure](..\ntifs\ns-ntifs--refs-smr-volume-info-output.md) | The REFS_SMR_VOLUME_INFO_OUTPUT structure describes a Shingled Magnetic Recording (SMR) volume's current state on space and garbage collection activities. |
| [FILE_OBJECTID_INFORMATION structure](..\ntifs\ns-ntifs--file-objectid-information.md) | The FILE_OBJECTID_INFORMATION structure is used to query for object ID information for the files in a directory on an NTFS volume. |
| [FILE_LEVEL_TRIM_OUTPUT structure](..\ntifs\ns-ntifs--file-level-trim-output.md) | The FILE_LEVEL_TRIM_OUTPUT structure contains the results of a trim operation performed by an FSCTL_FILE_LEVEL_TRIM request. |
| [FILE_LINK_ENTRY_INFORMATION structure](..\ntifs\ns-ntifs--file-link-entry-information.md) | The FILE_LINK_ENTRY_INFORMATION structure describes a single NTFS hard link to an existing file. |
| [TOKEN_GROUPS_AND_PRIVILEGES structure](..\ntifs\ns-ntifs--token-groups-and-privileges.md) | TOKEN_GROUPS_AND_PRIVILEGES contains information about the group security identifiers (SIDs) and privileges in an access token. |
| [WIM_PROVIDER_OVERLAY_ENTRY structure](..\ntifs\ns-ntifs--wim-provider-overlay-entry.md) | Contains the a Windows Image Format (WIM) file configuration information for a data source entry. It is used to identify specific WIM file names and indices that supply data to externally backed files on a volume. |
| [TOKEN_STATISTICS structure](..\ntifs\ns-ntifs--token-statistics.md) | TOKEN_STATISTICS contains information about an access token. A driver can retrieve this information by calling SeQueryInformationToken or ZwQueryInformationToken. |
| [OPEN_REPARSE_LIST structure](..\ntifs\ns-ntifs--open-reparse-list.md) | Points to a list of OPEN_REPARSE_LIST_ENTRY structures that specify the tag and possibly GUID that should be opened directly without returning STATUS_REPARSE. |
| [FILE_FS_CONTROL_INFORMATION structure](..\ntifs\ns-ntifs--file-fs-control-information.md) | The FILE_FS_CONTROL_INFORMATION structure is used to query or set control information for the files in a directory. |
| [SYSTEM_AUDIT_ACE structure](..\ntifs\ns-ntifs--system-audit-ace.md) | The SYSTEM_AUDIT_ACE structure defines an access-control entry (ACE) for the system access-control list (ACL) specifying what types of access cause system-level notifications. |
| [ACE_HEADER structure](..\ntifs\ns-ntifs--ace-header.md) | The ACE_HEADER structure describes the type and size of an access-control entry (ACE). |
| [FILE_NETWORK_PHYSICAL_NAME_INFORMATION structure](..\ntifs\ns-ntifs--file-network-physical-name-information.md) | Contains the full UNC physical pathname for a file or directory on a remote file share. |
| [PREFETCH_OPEN_ECP_CONTEXT structure](..\ntifs\ns-ntifs--prefetch-open-ecp-context.md) | The PREFETCH_OPEN_ECP_CONTEXT structure communicates whether the prefetcher performs a given open request on a file. |
| [ACCESS_DENIED_ACE structure](..\ntifs\ns-ntifs--access-denied-ace.md) | The ACCESS_DENIED_ACE structure defines an access-control entry (ACE) for the discretionary access-control list (DACL) controlling access to an object. |
| [FILE_ID_EXTD_BOTH_DIR_INFORMATION structure](..\ntifs\ns-ntifs--file-id-extd-both-dir-information.md) | The FILE_ID_EXTD_BOTH_DIR_INFORMATION structure is used to query file reference number information for the files in a directory. |
| [SE_SID structure](..\ntifs\ns-ntifs--se-sid.md) | The SE_SID union holds the maximum-sized valid Security Identifier (SID). The structure occupies 68-bytes and is suitable for stack allocation. |
| [FSRTL_COMMON_FCB_HEADER structure](..\ntifs\ns-ntifs--fsrtl-common-fcb-header.md) | Do not use the FSRTL_COMMON_FCB_HEADER structure outside of the FSRTL_ADVANCED_FCB_HEADER structure. |
| [NETWORK_OPEN_ECP_CONTEXT_V0 structure](..\ntifs\ns-ntifs--network-open-ecp-context-v0.md) | The NETWORK_OPEN_ECP_CONTEXT_V0 structure is used to interpret network ECP contexts on files. |
| [FILE_ALLOCATION_INFORMATION structure](..\ntifs\ns-ntifs--file-allocation-information.md) | The FILE_ALLOCATION_INFORMATION structure is used to set the allocation size for a file. |
| [FILE_COMPLETION_INFORMATION structure](..\ntifs\ns-ntifs--file-completion-information.md) | The FILE_COMPLETION_INFORMATION structure contains the port handle and key for an I/O completion port created for a file handle. |
| [FSRTL_PER_FILEOBJECT_CONTEXT structure](..\ntifs\ns-ntifs--fsrtl-per-fileobject-context.md) | The opaque FSRTL_PER_FILEOBJECT_CONTEXT structure is used by the operating system to track file system filter-driver-defined context information structures for a file object. |
| [FILE_ZERO_DATA_INFORMATION_EX structure](..\ntifs\ns-ntifs--file-zero-data-information-ex.md) | Contains a range of a file to set to zeros. |
| [TOKEN_PRIVILEGES structure](..\ntifs\ns-ntifs--token-privileges.md) | TOKEN_PRIVILEGES contains information about a set of privileges for an access token. |
| [REPARSE_DATA_BUFFER structure](..\ntifs\ns-ntifs--reparse-data-buffer.md) | The REPARSE_DATA_BUFFER structure contains reparse point data for a Microsoft reparse point. |
| [FILE_QUOTA_INFORMATION structure](..\ntifs\ns-ntifs--file-quota-information.md) | The FILE_QUOTA_INFORMATION structure is used to query or set per-user quota information for each of the files in a directory. |
| [FILE_PIPE_LOCAL_INFORMATION structure](..\ntifs\ns-ntifs--file-pipe-local-information.md) | The FILE_PIPE_LOCAL_INFORMATION structure contains information about the local end of a named pipe. |
| [WIM_PROVIDER_REMOVE_OVERLAY_INPUT structure](..\ntifs\ns-ntifs--wim-provider-remove-overlay-input.md) | A Windows Image File (WIM) data source to remove from the WIM provider is specified in the WIM_PROVIDER_REMOVE_OVERLAY_INPUT structure. |
| [IO_PRIORITY_INFO structure](..\ntifs\ns-ntifs--io-priority-info.md) | The IO_PRIORITY_INFO structure is used to hold thread priority information. |
| [WIM_PROVIDER_EXTERNAL_INFO structure](..\ntifs\ns-ntifs--wim-provider-external-info.md) | The WIM_PROVIDER_EXTERNAL_INFO structure holds the identifier and status information for the Windows Image File (WIM) external backing provider. |
| [ACCESS_ALLOWED_ACE structure](..\ntifs\ns-ntifs--access-allowed-ace.md) | The ACCESS_ALLOWED_ACE structure defines an access-control entry (ACE) for the discretionary access-control list (DACL) that controls access to an object. |
| [FILE_RENAME_INFORMATION structure](..\ntifs\ns-ntifs--file-rename-information.md) | The FILE_RENAME_INFORMATION structure is used to rename a file. |
| [TOKEN_PRIMARY_GROUP structure](..\ntifs\ns-ntifs--token-primary-group.md) | TOKEN_PRIMARY_GROUP specifies a group security identifier (SID) for an access token. |
| [WIM_PROVIDER_ADD_OVERLAY_INPUT structure](..\ntifs\ns-ntifs--wim-provider-add-overlay-input.md) | A new Windows Image File (WIM) data source is added to the WIM provider with the WIM_PROVIDER_ADD_OVERLAY_INPUT structure. |
| [SYSTEM_SCOPED_POLICY_ID_ACE structure](..\ntifs\ns-ntifs--system-scoped-policy-id-ace.md) | The SYSTEM_SCOPED_POLICY_ID_ACE structure defines an access-control entry (ACE) for the system access-control list (ACL) specifying rights for a scoped policy identifer. |
| [WIM_PROVIDER_UPDATE_OVERLAY_INPUT structure](..\ntifs\ns-ntifs--wim-provider-update-overlay-input.md) | A current Windows Image File (WIM) data source is updated with a new WIM file using the FSCTL_UPDATE_OVERLAY control request with a WIM_PROVIDER_UPDATE_OVERLAY_INPUT structure. |
| [FILE_MAILSLOT_QUERY_INFORMATION structure](..\ntifs\ns-ntifs--file-mailslot-query-information.md) | The FILE_MAILSLOT_QUERY_INFORMATION structure contains information about a mailslot. |
| [FILE_LINK_INFORMATION structure](..\ntifs\ns-ntifs--file-link-information.md) | The FILE_LINK_INFORMATION structure is used to create an NTFS hard link to an existing file. |
| [NETWORK_OPEN_ECP_CONTEXT structure](..\ntifs\ns-ntifs--network-open-ecp-context.md) | The NETWORK_OPEN_ECP_CONTEXT structure is used to interpret network ECP contexts on files. |
| [TOKEN_USER structure](..\ntifs\ns-ntifs--token-user.md) | TOKEN_USER identifies the user associated with an access token. |
| [ECP_OPEN_PARAMETERS structure](..\ntifs\ns-ntifs--ecp-open-parameters.md) | The ECP_OPEN_PARAMETERS structure allows a caller to specify the purpose of opening of a file without interfering with existing handles and/or oplocks on the file. |
| [FILE_COMPRESSION_INFORMATION structure](..\ntifs\ns-ntifs--file-compression-information.md) | The FILE_COMPRESSION_INFORMATION structure describes the state of a compressed data buffer. |
| [FILE_PIPE_REMOTE_INFORMATION structure](..\ntifs\ns-ntifs--file-pipe-remote-information.md) | The FILE_PIPE_REMOTE_INFORMATION structure contains information about the remote end of a named pipe. |
| [SET_DAX_ALLOC_ALIGNMENT_HINT_INPUT structure](..\ntifs\ns-ntifs--set-dax-alloc-alignment-hint-input.md) | This structure is for internal use only and should not be called from your code. |
| [FILE_ID_FULL_DIR_INFORMATION structure](..\ntifs\ns-ntifs--file-id-full-dir-information.md) | The FILE_ID_FULL_DIR_INFORMATION structure is used to query detailed information for the files in a directory. |
| [FILE_FS_DRIVER_PATH_INFORMATION structure](..\ntifs\ns-ntifs--file-fs-driver-path-information.md) | The FILE_FS_DRIVER_PATH_INFORMATION structure is used to query whether a given driver is in the I/O path for a file system volume. |
| [FILE_REPARSE_POINT_INFORMATION structure](..\ntifs\ns-ntifs--file-reparse-point-information.md) | The FILE_REPARSE_POINT_INFORMATION structure is used to query for information about a reparse point. |
| [FSRTL_PER_FILE_CONTEXT structure](..\ntifs\ns-ntifs--fsrtl-per-file-context.md) | A legacy file system filter driver can use a FSRTL_PER_FILE_CONTEXT structure to associate driver-specific context information to an open file. |
| [FS_FILTER_SECTION_SYNC_OUTPUT structure](..\ntifs\ns-ntifs--fs-filter-section-sync-output.md) | The FS_FILTER_SECTION_SYNC_OUTPUT structure contains information describing the attributes of the section that is being created. |
| [FILE_DIRECTORY_INFORMATION structure](..\ntifs\ns-ntifs--file-directory-information.md) | The FILE_DIRECTORY_INFORMATION structure is used to query detailed information for the files in a directory. |
| [FILE_BOTH_DIR_INFORMATION structure](..\ntifs\ns-ntifs--file-both-dir-information.md) | The FILE_BOTH_DIR_INFORMATION structure is used to query detailed information for the files in a directory. |
| [FSRTL_PER_STREAM_CONTEXT structure](..\ntifs\ns-ntifs--fsrtl-per-stream-context.md) | The FSRTL_PER_STREAM_CONTEXT structure contains context information that a file system filter driver maintains about a file stream. |
| [TOKEN_GROUPS structure](..\ntifs\ns-ntifs--token-groups.md) | TOKEN_GROUPS contains information about the group security identifiers (SID) in an access token. |
| [FILE_FS_PERSISTENT_VOLUME_INFORMATION structure](..\ntifs\ns-ntifs--file-fs-persistent-volume-information.md) | The FILE_FS_PERSISTENT_VOLUME_INFORMATION structure is used to control persistent settings for a file system volume. Persistent settings persist on a file system volume between reboots of the computer. |
| [FILE_PIPE_INFORMATION structure](..\ntifs\ns-ntifs--file-pipe-information.md) | The FILE_PIPE_INFORMATION structure contains information about a named pipe that is not specific to the local or the remote end of the pipe. |
| [FILE_GET_EA_INFORMATION structure](..\ntifs\ns-ntifs--file-get-ea-information.md) | The FILE_GET_EA_INFORMATION structure is used to query for extended-attribute (EA) information. |
| [WIM_PROVIDER_SUSPEND_OVERLAY_INPUT structure](..\ntifs\ns-ntifs--wim-provider-suspend-overlay-input.md) | A Windows Image File (WIM) data source to suspend from the WIM provider is specified in the WIM_PROVIDER_SUSPEND_OVERLAY_INPUT structure. |
| [FILE_ID_GLOBAL_TX_DIR_INFORMATION structure](..\ntifs\ns-ntifs--file-id-global-tx-dir-information.md) | The FILE_ID_GLOBAL_TX_DIR_INFORMATION structure contains information about transactional visibility for the files in a directory. |
| [FSCTL_OFFLOAD_WRITE_OUTPUT structure](..\ntifs\ns-ntifs--fsctl-offload-write-output.md) | The FSCTL_OFFLOAD_WRITE_OUTPUT structure contains the output for the FSCTL_OFFLOAD_WRITE control code request. |
| [REPARSE_GUID_DATA_BUFFER structure](..\ntifs\ns-ntifs--reparse-guid-data-buffer.md) | The REPARSE_GUID_DATA_BUFFER structure contains reparse point data for a reparse point. |
| [FILE_ID_BOTH_DIR_INFORMATION structure](..\ntifs\ns-ntifs--file-id-both-dir-information.md) | The FILE_ID_BOTH_DIR_INFORMATION structure is used to query file reference number information for the files in a directory. |
| [BOOT_AREA_INFO structure](..\ntifs\ns-ntifs--boot-area-info.md) | The BOOT_AREA_INFO structure contains the output for the FSCTL_GET_BOOT_AREA_INFO control code. |
| [WOF_EXTERNAL_INFO structure](..\ntifs\ns-ntifs--wof-external-info.md) | The WOF_EXTERNAL_INFO structure identifies a file backing provider and the overlay service version it supports. |
| [FILE_LINKS_INFORMATION structure](..\ntifs\ns-ntifs--file-links-information.md) | The FILE_LINKS_INFORMATION structure is used to query NTFS hard links to an existing file. |
| [SRV_OPEN_ECP_CONTEXT structure](..\ntifs\ns-ntifs--srv-open-ecp-context.md) | The SRV_OPEN_ECP_CONTEXT structure is used by a server to conditionally open files in response to client requests. |
| [FILE_LEVEL_TRIM structure](..\ntifs\ns-ntifs--file-level-trim.md) | The FILE_LEVEL_TRIM structure contains an array of byte ranges to trim for a file. |
| [FILE_FULL_DIR_INFORMATION structure](..\ntifs\ns-ntifs--file-full-dir-information.md) | The FILE_FULL_DIR_INFORMATION structure is used to query detailed information for the files in a directory. |
| [FILE_TIMESTAMPS structure](..\ntifs\ns-ntifs--file-timestamps.md) | The FILE_TIMESTAMPS structure specifies the last recorded instance of specific actions on a file. |
| [QUERY_FILE_LAYOUT_INPUT structure](..\ntifs\ns-ntifs--query-file-layout-input.md) | The QUERY_FILE_LAYOUT_INPUT structure selects which file layout entries are returned from a FSCTL_QUERY_FILE_LAYOUT request. |
| [FSCTL_OFFLOAD_READ_OUTPUT structure](..\ntifs\ns-ntifs--fsctl-offload-read-output.md) | The FSCTL_OFFLOAD_READ_OUTPUT structure contains the output for the FSCTL_OFFLOAD_READ control code request. |
| [FILE_ZERO_DATA_INFORMATION structure](..\ntifs\ns-ntifs--file-zero-data-information.md) | Contains a range of a file to set to zeros. |
| [NETWORK_OPEN_ECP_CONTEXT structure](..\ntifs\ns-ntifs--network-open-ecp-context~r1.md) | The NETWORK_OPEN_ECP_CONTEXT structure is used to interpret network ECP contexts on files. |
| [NETWORK_APP_INSTANCE_ECP_CONTEXT structure](..\ntifs\ns-ntifs--network-app-instance-ecp-context.md) | The NETWORK_APP_INSTANCE_ECP_CONTEXT structure is an Extra Create Parameter (ECP) and contains an application instance identifier to associate with a file. |
| [FSRTL_ADVANCED_FCB_HEADER structure](..\ntifs\ns-ntifs--fsrtl-advanced-fcb-header.md) | The FSRTL_ADVANCED_FCB_HEADER structure contains context information that a file system maintains about a file. |
| [FILE_STREAM_INFORMATION structure](..\ntifs\ns-ntifs--file-stream-information.md) | The FILE_STREAM_INFORMATION structure is used to enumerate the streams for a file. |
| [WOF_VERSION_INFO structure](..\ntifs\ns-ntifs--wof-version-info.md) | The WOF_VERSION_INFO structure contains the version corresponding to the driver supporting a given provider. |
| [SE_TOKEN_USER structure](..\ntifs\ns-ntifs--se-token-user.md) | The SE_TOKEN_USER structure holds the maximum-sized valid user SID that can be returned by SeQueryInformationToken, GetTokenInformation, or ZwQueryInformationToken with the TokenUser information class. This structure is suitable for stack allocation. |
| [TOKEN_OWNER structure](..\ntifs\ns-ntifs--token-owner.md) | TOKEN_OWNER contains the default owner security identifier (SID) that will be applied to newly created objects. |
| [TOKEN_ORIGIN structure](..\ntifs\ns-ntifs--token-origin.md) | The TOKEN_ORIGIN structure contains information about the origin of the logon session. |
| [REFS_SMR_VOLUME_GC_PARAMETERS structure](..\ntifs\ns-ntifs--refs-smr-volume-gc-parameters.md) | The REFS_SMR_VOLUME_GC_PARAMETERS structure. |
| [FILE_NAMES_INFORMATION structure](..\ntifs\ns-ntifs--file-names-information.md) | A FILE_NAMES_INFORMATION structure used to query detailed information about the names of files in a directory. |
| [PUBLIC_OBJECT_TYPE_INFORMATION structure](..\ntifs\ns-ntifs---public-object-type-information.md) | The PUBLIC_OBJECT_TYPE_INFORMATION structure holds the type name of the object. |
| [SID_AND_ATTRIBUTES structure](..\ntifs\ns-ntifs--sid-and-attributes.md) | The SID_AND_ATTRIBUTES structure represents a security identifier (SID) and its attributes. SIDs are used to uniquely identify users or groups. |
| [SYSTEM_PROCESS_TRUST_LABEL_ACE structure](..\ntifs\ns-ntifs--system-process-trust-label-ace.md) | Reserved. |
| [TOKEN_CONTROL structure](..\ntifs\ns-ntifs--token-control.md) | The TOKEN_CONTROL structure contains information that identifies an access token. |
| [SYSTEM_RESOURCE_ATTRIBUTE_ACE structure](..\ntifs\ns-ntifs--system-resource-attribute-ace.md) | The SYSTEM_RESOURCE_ATTRIBUTE_ACE structure defines an access-control entry (ACE) for the system access-control list (ACL) specifying what rights a particular claim has to a resource. |
| [SID_IDENTIFIER_AUTHORITY structure](..\ntifs\ns-ntifs--sid-identifier-authority.md) | The SID_IDENTIFIER_AUTHORITY structure represents the top-level authority of a security identifier (SID). |
| [FSCTL_OFFLOAD_READ_INPUT structure](..\ntifs\ns-ntifs--fsctl-offload-read-input.md) | The FSCTL_OFFLOAD_READ_INPUT structure contains the input for the FSCTL_OFFLOAD_READ control code request. |
| [NFS_OPEN_ECP_CONTEXT structure](..\ntifs\ns-ntifs--nfs-open-ecp-context.md) | The NFS_OPEN_ECP_CONTEXT structure is used by the Network File System (NFS) server to open files in response to client requests. |
| [FILE_FS_ATTRIBUTE_INFORMATION structure](..\ntifs\ns-ntifs--file-fs-attribute-information.md) | The FILE_FS_ATTRIBUTE_INFORMATION structure is used to query attribute information for a file system. |
| [FILE_GET_QUOTA_INFORMATION structure](..\ntifs\ns-ntifs--file-get-quota-information.md) | The FILE_GET_QUOTA_INFORMATION structure is used to query for quota information. |
| [TOKEN_DEFAULT_DACL structure](..\ntifs\ns-ntifs--token-default-dacl.md) | The TOKEN_DEFAULT_DACL structure specifies a discretionary access-control list (DACL). |
| [ATOMIC_CREATE_ECP_CONTEXT structure](..\ntifs\ns-ntifs--atomic-create-ecp-context.md) | This structure allows supplemental operations to be performed on a file atomically during create. |
| [FILE_MAILSLOT_SET_INFORMATION structure](..\ntifs\ns-ntifs--file-mailslot-set-information.md) | The FILE_MAILSLOT_SET_INFORMATION structure is used to set a value on a mailslot. |
| [FILE_LEVEL_TRIM_RANGE structure](..\ntifs\ns-ntifs--file-level-trim-range.md) | Contains the offset and length of a trim range for a file. |
| [PMARK_HANDLE_INFO32 structure](..\ntifs\ns-ntifs-pmark-handle-info32.md) | Contains information that is used to mark a specified file or directory, and its update sequence number (USN) change journal record with data about changes. |
| [FILE_INTERNAL_INFORMATION structure](..\ntifs\ns-ntifs--file-internal-information.md) | The FILE_INTERNAL_INFORMATION structure is used to query for the file system's 8-byte file reference number for a file. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [TOKEN_INFORMATION_CLASS enumeration](..\ntifs\ne-ntifs--token-information-class.md) | The TOKEN_INFORMATION_CLASS enumeration type contains values that specify the type of information being assigned to or retrieved from an access token. |
| [REFS_SMR_VOLUME_GC_ACTION enumeration](..\ntifs\ne-ntifs--refs-smr-volume-gc-action.md) | The REFS_SMR_VOLUME_GC_ACTION enum contains the available garbage collection commands for FSCTL_SET_REFS_SMR_VOLUME_GC_PARAMETERS. |
| [NETWORK_OPEN_INTEGRITY_QUALIFIER enumeration](..\ntifs\ne-ntifs-network-open-integrity-qualifier.md) | The NETWORK_OPEN_INTEGRITY_QUALIFIER enumeration type contains values that identify the kind of integrity restriction to attach to a file. |
| [REFS_SMR_VOLUME_GC_STATE enumeration](..\ntifs\ne-ntifs--refs-smr-volume-gc-state.md) | The REFS_SMR_VOLUME_GC_STATE enum specifies the garbage collection's current state. |
| [SID_NAME_USE enumeration](..\ntifs\ne-ntifs--sid-name-use.md) | The SID_NAME_USE enumeration type contains values that specify the type of a security identifier (SID). |
| [OBJECT_INFORMATION_CLASS enumeration](..\ntifs\ne-ntifs--object-information-class.md) | The OBJECT_INFORMATION_CLASS enumeration type represents the type of information to supply about an object. |
| [REFS_SMR_VOLUME_GC_METHOD enumeration](..\ntifs\ne-ntifs--refs-smr-volume-gc-method.md) | The REFS_SMR_VOLUME_GC_METHOD enum specifies the garbage collection method or strategy for FSCTL_SET_REFS_SMR_VOLUME_GC_PARAMETERS. |
| [TOKEN_TYPE enumeration](..\ntifs\ne-ntifs--token-type.md) | The TOKEN_TYPE enumeration type contains values that differentiate between a primary token and an impersonation token. |
| [FSRTL_CHANGE_BACKING_TYPE enumeration](..\ntifs\ne-ntifs--fsrtl-change-backing-type.md) | The FSRTL_CHANGE_BACKING_TYPE enumeration specifies the type of cache or control area that a file object designates. |
| [NETWORK_OPEN_LOCATION_QUALIFIER enumeration](..\ntifs\ne-ntifs-network-open-location-qualifier.md) | The NETWORK_OPEN_LOCATION_QUALIFIER enumeration type contains values that identify the kind of location restriction to attach to a file. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK callback](..\ntifs\nc-ntifs-pfsrtl-extra-create-parameter-cleanup-callback.md) | A file system filter driver (legacy filter) or a minifilter driver can register a PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK-typed routine as the filter driver's CleanupCallback callback routine for an extra create parameter (ECP) context structure. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxpAcquirePrefixTableLockShared function](..\prefix\nf-prefix-rxpacquireprefixtablelockshared.md) | RxpAcquirePrefixTableLockShared acquires the prefix table lock shared. |
| [RxpReleasePrefixTableLock function](..\prefix\nf-prefix-rxpreleaseprefixtablelock.md) | RxpReleasePrefixTableLock releases a previously acquired shared or exclusive prefix table lock. |
| [RxpAcquirePrefixTableLockExclusive function](..\prefix\nf-prefix-rxpacquireprefixtablelockexclusive.md) | RxpAcquirePrefixTableLockExclusive acquires the prefix table lock exclusively. |
| [RxPrefixTableLookupName function](..\prefix\nf-prefix-rxprefixtablelookupname.md) | RxPrefixTableLookupName looks up a name in a prefix table used to catalog SRV_CALL, NET_ROOT, and V_NET_ROOT names and converts the underlying pointer to a structure that contains the name. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxCeBuildTransport function](..\rxce\nf-rxce-rxcebuildtransport.md) | RxCeBuildTransport binds an RDBSS transport object to a specified transport name. |
| [RxCeFreeIrp function](..\rxce\nf-rxce-rxcefreeirp.md) | RxCeFreeIrp frees an IRP. |
| [RxCeSendDatagram function](..\rxce\nf-rxce-rxcesenddatagram.md) | RxCeSendDatagram sends a transport service data unit (TSDU) along the specified connection on a virtual circuit. |
| [RxCeBuildAddress function](..\rxce\nf-rxce-rxcebuildaddress.md) | RxCeBuildAddress associates a transport address with a transport binding. |
| [RxCeCancelConnectRequest function](..\rxce\nf-rxce-rxcecancelconnectrequest.md) | RxCeCancelConnectRequest cancels a previously issued connection request. Note that this routine is not currently implemented. |
| [RxCeBuildConnection function](..\rxce\nf-rxce-rxcebuildconnection.md) | RxCeBuildConnection establishes a connection between a local RDBSS connection address and a given remote address. |
| [RxCeBuildConnectionOverMultipleTransports function](..\rxce\nf-rxce-rxcebuildconnectionovermultipletransports.md) | RxCeBuildConnectionOverMultipleTransports establishes a connection between a local RDBSS connection address and a given remote address and supports multiple transports. |
| [RxCeAllocateIrpWithMDL function](..\rxce\nf-rxce-rxceallocateirpwithmdl.md) | RxCeAllocateIrpWithMDL allocates an IRP and associates it with an existing memory descriptor list. |
| [RxCeSend function](..\rxce\nf-rxce-rxcesend.md) | RxCeSend sends a transport service data unit (TSDU) along the specified connection on a virtual circuit. |
| [RxCeTearDownAddress function](..\rxce\nf-rxce-rxceteardownaddress.md) | RxCeTearDownAddress deregisters a transport address from a transport binding. |
| [RxCeTearDownVC function](..\rxce\nf-rxce-rxceteardownvc.md) | RxCeTearDownVC deregisters a virtual circuit from a specified RDBSS connection. |
| [RxCeBuildVC function](..\rxce\nf-rxce-rxcebuildvc.md) | RxCeBuildVC adds a virtual circuit to a specified RDBSS connection.. |
| [RxCeQueryAdapterStatus function](..\rxce\nf-rxce-rxcequeryadapterstatus.md) | RxCeQueryAdapterStatus returns the ADAPTER_STATUS structure for a given transport in a caller-allocated buffer. |
| [RxCeInitiateVCDisconnect function](..\rxce\nf-rxce-rxceinitiatevcdisconnect.md) | RxCeInitiateVCDisconnect initiates a disconnect on the virtual circuit. |
| [RxCeQueryTransportInformation function](..\rxce\nf-rxce-rxcequerytransportinformation.md) | RxCeQueryTransportInformation queries transport information for a given transport. |
| [RxCeTearDownConnection function](..\rxce\nf-rxce-rxceteardownconnection.md) | RxCeTearDownConnection tears down a given connection between a local RDBSS connection address and a remote address. |
| [RxCeTearDownTransport function](..\rxce\nf-rxce-rxceteardowntransport.md) | RxCeTearDownTransport unbinds an RDBSS transport object. |
| [RxCeQueryInformation function](..\rxce\nf-rxce-rxcequeryinformation.md) | RxCeQueryInformation queries information about a connection in a caller-allocated buffer. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [RX_CONTEXT structure](..\rxcontx\ns-rxcontx--rx-context.md) | The RX_CONTEXT structure encapsulates an IRP for use by RDBSS, network mini-redirectors, and the file system. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxDereferenceAndDeleteRxContext_Real function](..\rxcontx\nf-rxcontx-rxdereferenceanddeleterxcontext-real.md) | RxDereferenceAndDeleteRxContext_Real dereferences an RX_CONTEXT data structure and if the ReferenceCount member goes to zero, then it deallocates and removes the specified RX_CONTEXT structure from the RDBSS in-memory data structures. |
| [RxInitializeContext function](..\rxcontx\nf-rxcontx-rxinitializecontext.md) | RxInitializeContext initializes an existing RX_CONTEXT data structure. |
| [RxPrepareContextForReuse function](..\rxcontx\nf-rxcontx-rxpreparecontextforreuse.md) | RxPrepareContextForReuse prepares an RX_CONTEXT data structure for reuse by resetting all of the operation-specific allocations and acquisitions that have been made (the ReferenceCount member to the RX_CONTEXT structure is set to zero). |
| [__RxSynchronizeBlockingOperations function](..\rxcontx\nf-rxcontx---rxsynchronizeblockingoperations.md) | __RxSynchronizeBlockingOperations synchronizes blocking I/O requests to the same work queue. |
| [RxSetMinirdrCancelRoutine function](..\rxcontx\nf-rxcontx-rxsetminirdrcancelroutine.md) | RxSetMinirdrCancelRoutine is called by a network mini-redirector driver to set up a network mini-redirector cancel routine for an RX_CONTEXT structure. |
| [RxCreateRxContext function](..\rxcontx\nf-rxcontx-rxcreaterxcontext.md) | RxCreateRxContext allocates a new RX_CONTEXT structure and initializes the data structure. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxLog function](..\rxlog\nf-rxlog-rxlog.md) | _RxLog takes a format string and variable number of parameters and formats an output string for recording as an I/O error log entry if logging is enabled. |
| [_RxLog function](..\rxlog\nf-rxlog--rxlog.md) | _RxLog takes a format string and variable number of parameters and formats an output string for recording as an I/O error log entry if logging is enabled. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxFinalizeConnection function](..\rxprocs\nf-rxprocs-rxfinalizeconnection.md) | RxFinalizeConnection deletes a connection to a share. |
| [RxFsdPostRequest function](..\rxprocs\nf-rxprocs-rxfsdpostrequest.md) | RxFsdPostRequest queues the I/O request packet (IRP) specified by an RX_CONTEXT structure to the worker queue for processing by the file system process (FSP). |
| [RxIndicateChangeOfBufferingState function](..\rxprocs\nf-rxprocs-rxindicatechangeofbufferingstate.md) | RxIndicateChangeOfBufferingState is called to register a change buffering state request (an oplock break indication, for example) for later processing. If necessary, worker thread routines for further processing are activated. |
| [RxLogEventWithAnnotation function](..\rxprocs\nf-rxprocs-rxlogeventwithannotation.md) | RxLogEventWithAnnotation allocates an I/O error log structure, fills it in with information, and writes the entry to the I/O error log. |
| [RxLogEventWithBufferDirect function](..\rxprocs\nf-rxprocs-rxlogeventwithbufferdirect.md) | RxLogEventWithBufferDirect allocates an I/O error log structure, fills it in with information, and writes the entry to the I/O error log. |
| [RxReference function](..\rxprocs\nf-rxprocs-rxreference.md) | RxReference increments the NodeReferenceCount member of a structure by one for several of the reference counted data structures used by RDBSS. |
| [RxSetSrvCallDomainName function](..\rxprocs\nf-rxprocs-rxsetsrvcalldomainname.md) | RxSetSrvCallDomainName is called by a network mini-redirector driver to set the domain name associated with any given server (SRV_CALL structure). |
| [RxDriverEntry function](..\rxprocs\nf-rxprocs-rxdriverentry.md) | RxDriverEntry is called by a monolithic network mini-redirector driver from its DriverEntry routine to initialize the RDBSS static library. |
| [RxForceFinalizeAllVNetRoots function](..\rxprocs\nf-rxprocs-rxforcefinalizeallvnetroots.md) | RxForceFinalizeAllVNetRoots force finalizes all the V_NET_ROOT structures associated with a given NET_ROOT structure. The caller must have an exclusive lock on the netname table associated with the device object. |
| [RxCompleteRequest function](..\rxprocs\nf-rxprocs-rxcompleterequest.md) | RxCompleteRequest completes the IRP request associated with an RX_CONTEXT structure. |
| [RxFinalizeNetFcb function](..\rxprocs\nf-rxprocs-rxfinalizenetfcb.md) | RxFinalizeNetFCB finalizes the given FCB structure. The caller must have an exclusive lock on the NET_ROOT associated with FCB. |
| [RxPurgeAllFobxs function](..\rxprocs\nf-rxprocs-rxpurgeallfobxs.md) | RxPurgeAllFobxs purges all of the FOBX structures associated with a network mini-redirector. |
| [RxChangeBufferingState function](..\rxprocs\nf-rxprocs-rxchangebufferingstate.md) | RxChangeBufferingState is called to process a buffering state change request. |
| [RxLogEventDirect function](..\rxprocs\nf-rxprocs-rxlogeventdirect.md) | RxLogEventDirect is called to log an error to the I/O error log. It is recommended that the RXLogEvent macro or the RxLogFailure macro be used instead of calling this routine directly. |
| [RxDereference function](..\rxprocs\nf-rxprocs-rxdereference.md) | RxDereference decrements the NodeReferenceCount member of a structure by one for several reference counted data structures used by RDBSS. |
| [RxPrepareToReparseSymbolicLink function](..\rxprocs\nf-rxprocs-rxpreparetoreparsesymboliclink.md) | RxPrepareToReparseSymbolicLink sets up the file object name to facilitate a reparse. This routine is used by the network mini-redirectors to traverse symbolic links. |
| [RxLockEnumerator function](..\rxprocs\nf-rxprocs-rxlockenumerator.md) | RxLockEnumerator is called from a network mini-redirector to enumerate the file locks on an FCB. |
| [RxIndicateChangeOfBufferingStateForSrvOpen function](..\rxprocs\nf-rxprocs-rxindicatechangeofbufferingstateforsrvopen.md) | RxIndicateChangeOfBufferingStateForSrvOpen is called to register a change buffering state request (an oplock break indication, for example) for later processing. If the necessary preconditions are satisfied, the oplock is processed further. |
| [RxIsThisACscAgentOpen function](..\rxprocs\nf-rxprocs-rxisthisacscagentopen.md) | RxIsThisACscAgentOpen determines if a file open was made by a user-mode client-side caching agent. |
| [RxMapSystemBuffer function](..\rxprocs\nf-rxprocs-rxmapsystembuffer.md) | RxMapSystemBuffer returns the system buffer address from the IRP. |
| [RxCompleteRequest_Real function](..\rxprocs\nf-rxprocs-rxcompleterequest-real.md) | RxCompleteRequest_Real completes the IRP request associated with an RX_CONTEXT structure. |
| [RxScavengeAllFobxs function](..\rxprocs\nf-rxprocs-rxscavengeallfobxs.md) | RxScavengeAllFobxs scavenges all of the FOBX structures associated with a network mini-redirector device object. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxGetRDBSSProcess function](..\rxstruc\nf-rxstruc-rxgetrdbssprocess.md) | RxGetRDBSSProcess returns a pointer to the process of the main thread used by the RDBSS kernel process. |
| [RxUnregisterMinirdr function](..\rxstruc\nf-rxstruc-rxunregisterminirdr.md) | RxUnregisterMinirdr is an inline routine called by a network mini-redirector driver to de-register the driver with RDBSS and remove the registration information from the internal RDBSS registration table. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxPostOneShotTimerRequest function](..\rxtimer\nf-rxtimer-rxpostoneshottimerrequest.md) | RxPostOneShotTimerRequest initializes a one-shot timer entry. The passed-in pointer to a worker thread routine is called once when the timer expires. |
| [RxPostRecurrentTimerRequest function](..\rxtimer\nf-rxtimer-rxpostrecurrenttimerrequest.md) | RxPostRecurrentTimerRequest initializes a recurrent timer request. The passed in pointer to a worker thread routine is called at regular intervals when the recurrent timer fires based on the input parameters to this routine. |
| [RxCancelTimerRequest function](..\rxtimer\nf-rxtimer-rxcanceltimerrequest.md) | RxCancelTimerRequest cancels a recurrent timer request. The request to be canceled is identified by the worker thread routine and associated context. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxPostToWorkerThread function](..\rxworkq\nf-rxworkq-rxposttoworkerthread.md) | RxPostToWorkerThread invokes a routine passed as a parameter in the context of a worker thread. Memory for the WORK_QUEUE_ITEM must be allocated by the caller. |
| [RxDispatchToWorkerThread function](..\rxworkq\nf-rxworkq-rxdispatchtoworkerthread.md) | RxDispatchToWorkerThread invokes a routine in the context of a worker thread. The memory for the WORK_QUEUE_ITEM is allocated by this routine. |
| [RxSpinDownMRxDispatcher function](..\rxworkq\nf-rxworkq-rxspindownmrxdispatcher.md) | RxSpinDownMRxDispatcher tears down the dispatcher context for a network mini-redirector. |


This technology is in the following headers:


| Header        | 

| [fcb](..\fcb\~PORTAL~fcb.md) | 

| [fcbtable](..\fcbtable\~PORTAL~fcbtable.md) | 

| [fltkernel](..\fltkernel\~PORTAL~fltkernel.md) | 

| [fltsafe](..\fltsafe\~PORTAL~fltsafe.md) | 

| [fltuserstructures](..\fltuserstructures\~PORTAL~fltuserstructures.md) | 

| [lowio](..\lowio\~PORTAL~lowio.md) | 

| [midatlax](..\midatlax\~PORTAL~midatlax.md) | 

| [mrx](..\mrx\~PORTAL~mrx.md) | 

| [mrxfcb](..\mrxfcb\~PORTAL~mrxfcb.md) | 

| [namcache](..\namcache\~PORTAL~namcache.md) | 

| [nodetype](..\nodetype\~PORTAL~nodetype.md) | 

| [ntifs](..\ntifs\~PORTAL~ntifs.md) | 

| [ntrxdef](..\ntrxdef\~PORTAL~ntrxdef.md) | 

| [prefix](..\prefix\~PORTAL~prefix.md) | 

| [rx](..\rx\~PORTAL~rx.md) | 

| [rxce](..\rxce\~PORTAL~rxce.md) | 

| [rxcehdlr](..\rxcehdlr\~PORTAL~rxcehdlr.md) | 

| [rxcontx](..\rxcontx\~PORTAL~rxcontx.md) | 

| [rxdata](..\rxdata\~PORTAL~rxdata.md) | 

| [rxexcept](..\rxexcept\~PORTAL~rxexcept.md) | 

| [rxlog](..\rxlog\~PORTAL~rxlog.md) | 

| [rxpooltg](..\rxpooltg\~PORTAL~rxpooltg.md) | 

| [rxprocs](..\rxprocs\~PORTAL~rxprocs.md) | 

| [rxstruc](..\rxstruc\~PORTAL~rxstruc.md) | 

| [rxtimer](..\rxtimer\~PORTAL~rxtimer.md) | 

| [rxtrace](..\rxtrace\~PORTAL~rxtrace.md) | 

| [rxtypes](..\rxtypes\~PORTAL~rxtypes.md) | 

| [rxworkq](..\rxworkq\~PORTAL~rxworkq.md) | 

| [scavengr](..\scavengr\~PORTAL~scavengr.md) | 

| [struchdr](..\struchdr\~PORTAL~struchdr.md) | 

| [tdi](..\tdi\~PORTAL~tdi.md) | 
