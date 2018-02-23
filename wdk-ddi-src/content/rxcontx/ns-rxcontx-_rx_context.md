---
UID: NS:rxcontx._RX_CONTEXT
title: "_RX_CONTEXT"
author: windows-driver-content
description: The RX_CONTEXT structure encapsulates an IRP for use by RDBSS, network mini-redirectors, and the file system.
old-location: ifsk\rx_context.htm
old-project: ifsk
ms.assetid: 5eb83a7a-d6dd-445f-89a8-91cdf67512af
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: RX_CONTEXT structure [Installable File System Drivers], RX_CONTEXT, rxcontx/PRX_CONTEXT, rxcontx/RX_CONTEXT, PRX_CONTEXT structure pointer [Installable File System Drivers], rxstructures_29a918c5-d689-4e7d-84fe-dfd8901ee484.xml, ifsk.rx_context, PRX_CONTEXT, _RX_CONTEXT, *PRX_CONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rxcontx.h
req.include-header: Rx.h, Rxcontx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	rxcontx.h
apiname:
-	RX_CONTEXT
product: Windows
targetos: Windows
req.typenames: RX_CONTEXT, *PRX_CONTEXT
req.product: Windows 10 or later.
---

# _RX_CONTEXT structure
The RX_CONTEXT structure encapsulates an IRP for use by RDBSS, network mini-redirectors, and the file system. The RX_CONTEXT structure describes an IRP while it is being processed by a network mini-redirector and contains state information that allows global resources to be released as the IRP is completed.

## Syntax
````
typedef struct _RX_CONTEXT {
  NODE_TYPE_CODE         NodeTypeCode;
  NODE_BYTE_SIZE         NodeByteSize;
  __volatile ULONG       ReferenceCount;
  LIST_ENTRY             ContextListEntry;
  UCHAR                  MajorFunction;
  UCHAR                  MinorFunction;
  BOOLEAN                PendingReturned;
  BOOLEAN                PostRequest;
  PDEVICE_OBJECT         RealDevice;
  PIRP                   CurrentIrp;
  PIO_STACK_LOCATION     CurrentIrpSp;
  PMRX_FCB               pFcb;
  PMRX_FOBX              pFobx;
  PMRX_SRV_OPEN          pRelevantSrvOpen;
  PNON_PAGED_FCB         NonPagedFcb;
  PRDBSS_DEVICE_OBJECT   RxDeviceObject;
  PETHREAD               OriginalThread;
  PETHREAD               LastExecutionThread;
  __volatile PVOID       LockManagerContext;
  PVOID                  RdbssDbgExtension;
  RX_SCAVENGER_ENTRY     ScavengerEntry;
  ULONG                  SerialNumber;
  ULONG                  FobxSerialNumber;
  ULONG                  Flags;
  BOOLEAN                FcbResourceAcquired;
  BOOLEAN                FcbPagingIoResourceAcquired;
  UCHAR                  MustSucceedDescriptorNumber;
  union {
    struct {
      union {
        NTSTATUS StoredStatus;
        PVOID    StoredStatusAlignment;
      };
      ULONG_PTR InformationToReturn;
    };
    IO_STATUS_BLOCK IoStatusBlock;
  };
  union {
    ULONGLONG ForceLonglongAligmentDummyField;
    PVOID     MRxContext[MRX_CONTEXT_FIELD_COUNT];
  };
  PVOID                  WriteOnlyOpenRetryContext;
  PMRX_CALLDOWN          MRxCancelRoutine;
  PRX_DISPATCH           ResumeRoutine;
  RX_WORK_QUEUE_ITEM     WorkQueueItem;
  LIST_ENTRY             OverflowListEntry;
  KEVENT                 SyncEvent;
  LIST_ENTRY             BlockedOperations;
  PFAST_MUTEX            BlockedOpsMutex;
  LIST_ENTRY             RxContextSerializationQLinks;
  union {
    struct {
      union {
        FS_INFORMATION_CLASS   FsInformationClass;
        FILE_INFORMATION_CLASS FileInformationClass;
      };
      PVOID   Buffer;
      union {
        LONG Length;
        LONG LengthRemaining;
      };
      BOOLEAN ReplaceIfExists;
      BOOLEAN AdvanceOnly;
    } Info;
    struct {
      UNICODE_STRING       SuppliedPathName;
      NET_ROOT_TYPE        NetRootType;
      PIO_SECURITY_CONTEXT pSecurityContext;
    } PrefixClaim;
  };
  union {
    struct {
      NT_CREATE_PARAMETERS NtCreateParameters;
      ULONG                ReturnedCreateInformation;
      PWCH                 CanonicalNameBuffer;
      PRX_PREFIX_ENTRY     NetNamePrefixEntry;
      PMRX_SRV_CALL        pSrvCall;
      PMRX_NET_ROOT        pNetRoot;
      PMRX_V_NET_ROOT      pVNetRoot;
      PVOID                EaBuffer;
      ULONG                EaLength;
      ULONG                SdLength;
      ULONG                PipeType;
      ULONG                PipeReadMode;
      ULONG                PipeCompletionMode;
      USHORT               Flags;
      NET_ROOT_TYPE        Type;
      UCHAR                RdrFlags;
      BOOLEAN              FcbAcquired;
      BOOLEAN              TryForScavengingOnSharingViolation;
      BOOLEAN              ScavengingAlreadyTried;
      BOOLEAN              ThisIsATreeConnectOpen;
      BOOLEAN              TreeConnectOpenDeferred;
      UNICODE_STRING       TransportName;
      UNICODE_STRING       UserName;
      UNICODE_STRING       Password;
      UNICODE_STRING       UserDomainName;
    } Create;
    struct {
      ULONG   FileIndex;
      BOOLEAN RestartScan;
      BOOLEAN ReturnSingleEntry;
      BOOLEAN IndexSpecified;
      BOOLEAN InitialQuery;
    } QueryDirectory;
    struct {
      PMRX_V_NET_ROOT pVNetRoot;
    } NotifyChangeDirectory;
    struct {
      PUCHAR  UserEaList;
      ULONG   UserEaListLength;
      ULONG   UserEaIndex;
      BOOLEAN RestartScan;
      BOOLEAN ReturnSingleEntry;
      BOOLEAN IndexSpecified;
    } QueryEa;
    struct {
      SECURITY_INFORMATION SecurityInformation;
      ULONG                Length;
    } QuerySecurity;
    struct {
      SECURITY_INFORMATION SecurityInformation;
      PSECURITY_DESCRIPTOR SecurityDescriptor;
    } SetSecurity;
    struct {
      ULONG                       Length;
      PSID                        StartSid;
      PFILE_GET_QUOTA_INFORMATION SidList;
      ULONG                       SidListLength;
      BOOLEAN                     RestartScan;
      BOOLEAN                     ReturnSingleEntry;
      BOOLEAN                     IndexSpecified;
    } QueryQuota;
    struct {
      ULONG Length;
    } SetQuota;
    struct {
      PV_NET_ROOT VNetRoot;
      PSRV_CALL   SrvCall;
      PNET_ROOT   NetRoot;
    } DosVolumeFunction;
    struct {
      ULONG         FlagsForLowIo;
      LOWIO_CONTEXT LowIoContext;
    };
    LUID   FsdUid;
  };
  PWCH                   AlsoCanonicalNameBuffer;
  PUNICODE_STRING        LoudCompletionString;
#ifdef RDBSS_TRACKER
  __volatile LONG        AcquireReleaseFcbTrackerX;
  __volatile ULONG       TrackerHistoryPointer;
  RX_FCBTRACKER_CALLINFO TrackerHistory[RDBSS_TRACKER_HISTORY_SIZE];
#endif 
} RX_CONTEXT, *PRX_CONTEXT;
````

## Members


`AcquireReleaseFcbTrackerX`



`AlsoCanonicalNameBuffer`



`BlockedOperations`

A pointer to the list head of blocked operations that are to be released on completion. This member is reserved for internal use.

`BlockedOpsMutex`

A pointer to a mutex that controls serialization of the blocked operations. This member is reserved for internal use.

`ContextListEntry`

The list entry to connect this RX_CONTEXT to the list of active RX_CONTEXTS.

`CurrentIrp`

A pointer to the originating IRP. This member should not be used by a network mini-redirector driver.

`CurrentIrpSp`

A pointer to the IRP stack location.

`FcbPagingIoResourceAcquired`

If set to <b>TRUE</b>, this member specifies that the FCB paging I/O resource has been acquired for this operation. The FCB paging I/O resource is one of the locking mechanisms associated with a paging I/O operation on an FCB.

`FcbResourceAcquired`

If set to <b>TRUE</b>, this member specifies that the FCB resource has been acquired for this operation. The FCB resource is one of the locking mechanisms associated with an operation on an FCB.

`Flags`

A bitmask of flags for this RX_CONTEXT structure.

`FobxSerialNumber`

The serial number for the associated FOBX structure. Every structure initialized by RDBSS has a serial number assigned when the structure is first initialized. This member can be used by network mini-redirectors to see if multiple calls are part of the same larger operation and are therefore more cacheable.

`LastExecutionThread`

A pointer to the last thread in which some processing associated with the RX_CONTEXT was done if the thread was posted to the file system process.

`LockManagerContext`

A pointer to the lock manager context. This member is reserved for internal use.

`LoudCompletionString`

An unused member of the RX_CONTEXT structure.

`MajorFunction`

The major function for the IRP encapsulated by this RX_CONTEXT.

`MinorFunction`

The minor function for the IRP encapsulated by this RX_CONTEXT.

`MRxCancelRoutine`

A pointer to the cancellation routine that can be set by a network mini-redirector driver.

`MustSucceedDescriptorNumber`

A member initially set to zero in the <a href="..\rxcontx\nf-rxcontx-rxcreaterxcontext.md">RxCreateRxContext</a> routine. This member is not otherwise used by RDBSS, but it may be used by network mini-redirectors.

`NodeByteSize`

The size, in bytes, of this structure. RDBSS sets this member to sizeof( RX_CONTEXT) when an RX_CONTEXT is initialized in the <b>RxInitializeContext</b> routine. If a network mini-redirector driver initializes an RX_CONTEXT structure using some other method, this member must be set.

RDBSS defines this member as part of a standard header for all structures used by RDBSS.

`NodeTypeCode`

The unique node type used for an RX_CONTEXT structure. All of the major structure types (RX_CONTEXT, SRV_CALL, NET_ROOT, V_NET_ROOT, SRV_OPEN, FCB, and FOBX, for example) used by RDBSS have a unique two-byte node type code defined in the <i>nodetype.h</i> include file which can be used for debugging. RDBSS sets this member to RDBSS_NTC_RX_CONTEXT when an RX_CONTEXT is initialized in the <a href="..\rxcontx\nf-rxcontx-rxinitializecontext.md">RxInitializeContext</a> routine. If a network mini-redirector driver initializes an RX_CONTEXT structure using some other method, this member must be set.

RDBSS defines this member as part of a standard header for all structures used by RDBSS.

`NonPagedFcb`

A pointer to the associated non-paged file control block (FCB) for this IRP.

`OriginalThread`

A pointer to the original thread in which the request was initiated.

`OverflowListEntry`

A pointer to the list head of operations that are to be released on completion. This member is reserved for internal use.

`PendingReturned`

If set to <b>TRUE</b>, this specifies that RDBSS or a driver has marked the IRP pending. Each <a href="..\wdm\nc-wdm-io_completion_routine.md">IoCompletion</a> routine should check the value of this flag. If the flag is <b>TRUE</b>, and if the <b>IoCompletion</b> routine will not return STATUS_MORE_PROCESSING_REQUIRED, the routine should call <a href="..\wdm\nf-wdm-iomarkirppending.md">IoMarkIrpPending</a> to propagate the pending status to drivers above it in the device stack. This member is similar to the same field in the IRP. 

RDBSS always sets this member to <b>TRUE</b> before calling the network mini-redirector driver.

`pFcb`

A pointer to the associated file control block (FCB) for this IRP.

`pFobx`

A pointer to the associated file object extension (FOBX) for this IRP.

`PostRequest`

If set to <b>TRUE</b>, this indicates if the associated request is to be posted to a RDBSS worker thread. A network mini-redirector can set this member to <b>TRUE</b> to indicate that it wants to post this request to the file system process (FSP).

`pRelevantSrvOpen`

A pointer to the associated server open(SRV_OPEN) for this IRP.

`RdbssDbgExtension`

A pointer to the context given to RDBSS for debugging information. This member is reserved for internal use.

`RealDevice`

A pointer to the device object for the target network mini-redirector driver. RDBSS sets this member to the device object for the network mini-redirector driver when an RX_CONTEXT is allocated in the <a href="..\rxcontx\nf-rxcontx-rxinitializecontext.md">RxInitializeContext</a> routine. This member is copied from the <b>FileObject-&gt;DeviceObject</b> member from the IRP stack. The device object for the network mini-redirector is also stored in the <b>RxDeviceObject</b> structure member.

The <b>RealDevice</b>  member is not currently used by RDBSS, but can be used by network mini-redirectors.

`ReferenceCount`

The reference count for this structure after it is allocated. RDBSS sets this member to 1 when an RX_CONTEXT is allocated and initialized in the <b>RxInitializeContext</b> routine. If a network mini-redirector driver initializes an RX_CONTEXT structure using some other method, this member must be set.

RDBSS defines this member as part of a standard header for all structures used by RDBSS.

`ResumeRoutine`

This member is reserved for internal use.

`RxContextSerializationQLinks`

A pointer to the list entry used to serialize pipe operations on a per-file-object basis. This member is reserved for internal use.

`RxDeviceObject`

A pointer to the RDBSS_DEVICE_OBJECT for the target network mini-redirector driver which is required for worker queue algorithms. RDBSS sets this member to the RDBSS_DEVICE_OBJECT for the network mini-redirector when an RX_CONTEXT is initialized in the <b>RxInitializeContext</b> routine. The <b>RxDeviceObject</b> structure includes a <b>DeviceObject</b> member that contains the device object for the network mini-redirector driver which is the same as the <b>RealDevice</b> member of the RX_CONTEXT.

`ScavengerEntry`

A pointer to the list of items to be scavenged. This member is reserved for internal use.

`SerialNumber`

The serial number for this RX_CONTEXT structure. Every structure initialized by RDBSS has a serial number assigned when the structure is first initialized. This serial number is a number that is incremented by one before the value is set. RDBSS sets this member when an RX_CONTEXT is initialized in the <b>RxInitializeContext</b> routine. RDBSS

`ShadowCritOwner`



`SyncEvent`

A pointer to a kernel EVENT that can be used by a network mini-redirector driver to wait while processing the RX_CONTEXT.

`TrackerHistory`



`TrackerHistoryPointer`



`WorkQueueItem`

A pointer to a work queue item that can be used by a network mini-redirector driver while processing the RX_CONTEXT.

`WriteOnlyOpenRetryContext`

A pointer that can be used to store some state for the network mini-redirector. This member is not used by RDBSS, but it can be used by a network mini-redirector driver to indicate that a file is cached on a write-only handle.

## Remarks
The RX_CONTEXT structure is one of the fundamental data structures used by RDBSS and network mini-redirectors to manage an I/O request packet (IRP). The RX_CONTEXT data structure encapsulates an IRP for use by RDBSS, network mini-redirectors, and the file system. An RX_CONTEXT structure includes a pointer to a single IRP and all of the context required to process the IRP. 

An RX_CONTEXT structure is sometimes referred to as an IRP Context or RxContext in the Window Driver Kit (WDK) or IFS Kit header files and other resources used for developing network mini-redirector drivers.

The RX_CONTEXT is a data structure to which additional information provided by the various network mini redirectors is attached. The RX_CONTEXT includes fields for over allocating the size of each RX_CONTEXT structure by a pre-specified amount for each network mini redirector, which is then reserved for use by the mini redirector. This approach consists of allocating a pre-specified area, which is the same for all network mini redirectors as part of each RX_CONTEXT. This is an unformatted area on top of which any desired structure can be imposed by the various network mini redirectors. Developers of network mini-redirector drivers should try and define the associated private context to fit into this pre-specified area defined in the RX_CONTEXT data structure. Network mini-redirector drivers that violate this rule will incur a significant performance penalty.

Many RDBSS routines and routines exported by a network mini-redirector make reference to RX_CONTEXT structures in either the initiating thread or in some other thread used by the routine. Thus, allocated RX_CONTEXT structures are reference counted to manage their use for asynchronous operations. When the reference count goes to zero, the allocated RX_CONTEXT structure can be finalized and released on the last dereference operation.

RDBSS provides a number of routines that are used to manipulate an RX_CONTEXT and the associated IRP. These routines are used to allocate, initialize, and delete an RX_CONTEXT. These routines are also used to complete the IRP associated with an RX_CONTEXT and set up a cancel routine for an RX_CONTEXT.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rxcontx.h (include Rx.h, Rxcontx.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550805">MRxSetSdInfo</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550773">MRxQueryQuotaInfo</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550790">MRxSetFileInfo</a>



<a href="..\rxcontx\nf-rxcontx-rxcreaterxcontext.md">RxCreateRxContext</a>



<a href="..\rxcontx\nf-rxcontx-rxinitializecontext.md">RxInitializeContext</a>



<a href="..\ntifs\ni-ntifs-ioctl_redir_query_path_ex.md">IOCTL_REDIR_QUERY_PATH_EX</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550810">MRxSetVolumeInfo</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549862">MRxCreate</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548658">IRP_MJ_DIRECTORY_CONTROL</a>



<a href="..\mrx\nf-mrx-rxstartminirdr.md">RxStartMinirdr</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550755">MRxQueryDirectory</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549293">IRP_MJ_QUERY_QUOTA</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548649">IRP_MJ_DEVICE_CONTROL</a>



<a href="..\mrx\nf-mrx-rxstartminirdr.md">RxStartMinirdr</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550790">MRxSetFileInfo</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549407">IRP_MJ_SET_SECURITY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549298">IRP_MJ_QUERY_SECURITY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549401">IRP_MJ_SET_QUOTA</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550770">MRxQueryFileInfo</a>



<a href="..\wdm\nc-wdm-io_completion_routine.md">IoCompletion</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550796">MRxSetFileInfoAtCleanup</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550721">MRxLowIOSubmit[LOWIO_OP_NOTIFY_CHANGE_DIRECTORY]</a>



<a href="..\ntifs\ni-ntifs-ioctl_redir_query_path.md">IOCTL_REDIR_QUERY_PATH</a>



<a href="..\ntifs\ns-ntifs-_file_get_ea_information.md">FILE_GET_EA_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550759">MRxQueryEaInfo</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549279">IRP_MJ_QUERY_EA</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550776">MRxQuerySdInfo</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RX_CONTEXT structure%20 RELEASE:%20(2/16/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>