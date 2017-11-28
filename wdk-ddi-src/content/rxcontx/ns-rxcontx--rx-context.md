---
UID: NS.rxcontx._RX_CONTEXT
title: RX_CONTEXT
author: windows-driver-content
description: The RX_CONTEXT structure encapsulates an IRP for use by RDBSS, network mini-redirectors, and the file system.
old-location: ifsk\rx_context.htm
old-project: ifsk
ms.assetid: 5eb83a7a-d6dd-445f-89a8-91cdf67512af
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RX_CONTEXT, RX_CONTEXT, *PRX_CONTEXT
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
req.alt-api: RX_CONTEXT
req.alt-loc: rxcontx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# RX_CONTEXT structure



## -description
<p>The RX_CONTEXT structure encapsulates an IRP for use by RDBSS, network mini-redirectors, and the file system. The RX_CONTEXT structure describes an IRP while it is being processed by a network mini-redirector and contains state information that allows global resources to be released as the IRP is completed. </p>


## -syntax

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


## -struct-fields
<dl>

### -field <b>NodeTypeCode</b>

<dd>
<p>The unique node type used for an RX_CONTEXT structure. All of the major structure types (RX_CONTEXT, SRV_CALL, NET_ROOT, V_NET_ROOT, SRV_OPEN, FCB, and FOBX, for example) used by RDBSS have a unique two-byte node type code defined in the <i>nodetype.h</i> include file which can be used for debugging. RDBSS sets this member to RDBSS_NTC_RX_CONTEXT when an RX_CONTEXT is initialized in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554502">RxInitializeContext</a> routine. If a network mini-redirector driver initializes an RX_CONTEXT structure using some other method, this member must be set.</p>
<p>RDBSS defines this member as part of a standard header for all structures used by RDBSS. </p>
</dd>

### -field <b>NodeByteSize</b>

<dd>
<p>The size, in bytes, of this structure. RDBSS sets this member to sizeof( RX_CONTEXT) when an RX_CONTEXT is initialized in the <b>RxInitializeContext</b> routine. If a network mini-redirector driver initializes an RX_CONTEXT structure using some other method, this member must be set.</p>
<p>RDBSS defines this member as part of a standard header for all structures used by RDBSS. </p>
</dd>

### -field <b>ReferenceCount</b>

<dd>
<p>The reference count for this structure after it is allocated. RDBSS sets this member to 1 when an RX_CONTEXT is allocated and initialized in the <b>RxInitializeContext</b> routine. If a network mini-redirector driver initializes an RX_CONTEXT structure using some other method, this member must be set.</p>
<p>RDBSS defines this member as part of a standard header for all structures used by RDBSS. </p>
</dd>

### -field <b>ContextListEntry</b>

<dd>
<p>The list entry to connect this RX_CONTEXT to the list of active RX_CONTEXTS.</p>
</dd>

### -field <b>MajorFunction</b>

<dd>
<p>The major function for the IRP encapsulated by this RX_CONTEXT.</p>
</dd>

### -field <b>MinorFunction</b>

<dd>
<p>The minor function for the IRP encapsulated by this RX_CONTEXT.</p>
</dd>

### -field <b>PendingReturned</b>

<dd>
<p>If set to <b>TRUE</b>, this specifies that RDBSS or a driver has marked the IRP pending. Each <a href="https://msdn.microsoft.com/library/windows/hardware/ff548354">IoCompletion</a> routine should check the value of this flag. If the flag is <b>TRUE</b>, and if the <b>IoCompletion</b> routine will not return STATUS_MORE_PROCESSING_REQUIRED, the routine should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549422">IoMarkIrpPending</a> to propagate the pending status to drivers above it in the device stack. This member is similar to the same field in the IRP. </p>
<p>RDBSS always sets this member to <b>TRUE</b> before calling the network mini-redirector driver.</p>
</dd>

### -field <b>PostRequest</b>

<dd>
<p>If set to <b>TRUE</b>, this indicates if the associated request is to be posted to a RDBSS worker thread. A network mini-redirector can set this member to <b>TRUE</b> to indicate that it wants to post this request to the file system process (FSP).</p>
</dd>

### -field <b>RealDevice</b>

<dd>
<p>A pointer to the device object for the target network mini-redirector driver. RDBSS sets this member to the device object for the network mini-redirector driver when an RX_CONTEXT is allocated in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554502">RxInitializeContext</a> routine. This member is copied from the <b>FileObject-&gt;DeviceObject</b> member from the IRP stack. The device object for the network mini-redirector is also stored in the <b>RxDeviceObject</b> structure member.</p>
<p>The <b>RealDevice</b>  member is not currently used by RDBSS, but can be used by network mini-redirectors.</p>
</dd>

### -field <b>CurrentIrp</b>

<dd>
<p>A pointer to the originating IRP. This member should not be used by a network mini-redirector driver.</p>
</dd>

### -field <b>CurrentIrpSp</b>

<dd>
<p>A pointer to the IRP stack location.</p>
</dd>

### -field <b>pFcb</b>

<dd>
<p>A pointer to the associated file control block (FCB) for this IRP.</p>
</dd>

### -field <b>pFobx</b>

<dd>
<p>A pointer to the associated file object extension (FOBX) for this IRP.</p>
</dd>

### -field <b>pRelevantSrvOpen</b>

<dd>
<p>A pointer to the associated server open(SRV_OPEN) for this IRP.</p>
</dd>

### -field <b>NonPagedFcb</b>

<dd>
<p>A pointer to the associated non-paged file control block (FCB) for this IRP.</p>
</dd>

### -field <b>RxDeviceObject</b>

<dd>
<p>A pointer to the RDBSS_DEVICE_OBJECT for the target network mini-redirector driver which is required for worker queue algorithms. RDBSS sets this member to the RDBSS_DEVICE_OBJECT for the network mini-redirector when an RX_CONTEXT is initialized in the <b>RxInitializeContext</b> routine. The <b>RxDeviceObject</b> structure includes a <b>DeviceObject</b> member that contains the device object for the network mini-redirector driver which is the same as the <b>RealDevice</b> member of the RX_CONTEXT.</p>
</dd>

### -field <b>OriginalThread</b>

<dd>
<p>A pointer to the original thread in which the request was initiated.</p>
</dd>

### -field <b>LastExecutionThread</b>

<dd>
<p>A pointer to the last thread in which some processing associated with the RX_CONTEXT was done if the thread was posted to the file system process.</p>
</dd>

### -field <b>LockManagerContext</b>

<dd>
<p>A pointer to the lock manager context. This member is reserved for internal use.</p>
</dd>

### -field <b>RdbssDbgExtension</b>

<dd>
<p>A pointer to the context given to RDBSS for debugging information. This member is reserved for internal use.</p>
</dd>

### -field <b>ScavengerEntry</b>

<dd>
<p>A pointer to the list of items to be scavenged. This member is reserved for internal use.</p>
</dd>

### -field <b>SerialNumber</b>

<dd>
<p>The serial number for this RX_CONTEXT structure. Every structure initialized by RDBSS has a serial number assigned when the structure is first initialized. This serial number is a number that is incremented by one before the value is set. RDBSS sets this member when an RX_CONTEXT is initialized in the <b>RxInitializeContext</b> routine. RDBSS </p>
</dd>

### -field <b>FobxSerialNumber</b>

<dd>
<p>The serial number for the associated FOBX structure. Every structure initialized by RDBSS has a serial number assigned when the structure is first initialized. This member can be used by network mini-redirectors to see if multiple calls are part of the same larger operation and are therefore more cacheable.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitmask of flags for this RX_CONTEXT structure. </p>
</dd>

### -field <b>FcbResourceAcquired</b>

<dd>
<p>If set to <b>TRUE</b>, this member specifies that the FCB resource has been acquired for this operation. The FCB resource is one of the locking mechanisms associated with an operation on an FCB.</p>
</dd>

### -field <b>FcbPagingIoResourceAcquired</b>

<dd>
<p>If set to <b>TRUE</b>, this member specifies that the FCB paging I/O resource has been acquired for this operation. The FCB paging I/O resource is one of the locking mechanisms associated with a paging I/O operation on an FCB.</p>
</dd>

### -field <b>MustSucceedDescriptorNumber</b>

<dd>
<p>A member initially set to zero in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554367">RxCreateRxContext</a> routine. This member is not otherwise used by RDBSS, but it may be used by network mini-redirectors.</p>
</dd>

### -field ( <i>unnamed struct</i> )

<dd>
<p> </p>
<dl>

### -field <b>StoredStatus</b>

<dd>
<p>A member of an unnamed union used to return status information by a network mini-redirector driver for low I/O operations. RDBSS also sets this value based on the status returned by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550770">MRxQueryFileInfo</a> routine when the file query operation is not understood by RDBSS.</p>
</dd>

### -field <b>StoredStatusAlignment</b>

<dd>
<p>A member of an unnamed union used to force proper alignment on the <b>StoredStatus</b> member. </p>
</dd>

### -field <b>InformationToReturn</b>

<dd>
<p>A member of an unnamed union used to return status information by a network mini-redirector driver for some low I/O (read, write, FSCTL, etc.) and <b>MrxQueryXXX</b> operations. </p>
</dd>
</dl>
</dd>

### -field <b>IoStatusBlock</b>

<dd>
<p>The I/O status block use by a network mini-redirector to return status information. The <b>IoStatusBlock</b> member is a member of an unnamed union used for returning status information.</p>
</dd>

### -field <b>ForceLonglongAligmentDummyField</b>

<dd>
<p>A member of an unnamed union use to force proper alignment on the <b>MRxContext[MRX_CONTEXT_FIELD_COUNT]</b> member. </p>
</dd>

### -field <b>MRxContext</b>

<dd>
<p>A member of an unnamed union that contains an array of four pointers for use by a network mini-redirector driver.</p>
</dd>

### -field <b>WriteOnlyOpenRetryContext</b>

<dd>
<p>A pointer that can be used to store some state for the network mini-redirector. This member is not used by RDBSS, but it can be used by a network mini-redirector driver to indicate that a file is cached on a write-only handle.</p>
</dd>

### -field <b>MRxCancelRoutine</b>

<dd>
<p>A pointer to the cancellation routine that can be set by a network mini-redirector driver.</p>
</dd>

### -field <b>ResumeRoutine</b>

<dd>
<p>This member is reserved for internal use.</p>
</dd>

### -field <b>WorkQueueItem</b>

<dd>
<p>A pointer to a work queue item that can be used by a network mini-redirector driver while processing the RX_CONTEXT.</p>
</dd>

### -field <b>OverflowListEntry</b>

<dd>
<p>A pointer to the list head of operations that are to be released on completion. This member is reserved for internal use.</p>
</dd>

### -field <b>SyncEvent</b>

<dd>
<p>A pointer to a kernel EVENT that can be used by a network mini-redirector driver to wait while processing the RX_CONTEXT.</p>
</dd>

### -field <b>BlockedOperations</b>

<dd>
<p>A pointer to the list head of blocked operations that are to be released on completion. This member is reserved for internal use.</p>
</dd>

### -field <b>BlockedOpsMutex</b>

<dd>
<p>A pointer to a mutex that controls serialization of the blocked operations. This member is reserved for internal use.</p>
</dd>

### -field <b>RxContextSerializationQLinks</b>

<dd>
<p>A pointer to the list entry used to serialize pipe operations on a per-file-object basis. This member is reserved for internal use.</p>
</dd>

### -field <b>Info</b>

<dd>
<p>A structure member of an unnamed union used for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550755">MRxQueryDirectory</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550770">MRxQueryFileInfo</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550782">MRxQueryVolumeInfo</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550790">MRxSetFileInfo</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550796">MRxSetFileInfoAtCleanup</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff550810">MRxSetVolumeInfo</a> routines. RDBSS passes information in the <b>Info</b> structure member to the network mini-redirector and the network mini-redirector returns information to RDBSS in the <b>Info</b> structure member. </p>
<dl>

### -field <b>FsInformationClass</b>

<dd>
<p>A member of an unnamed union used by RDBSS to pass the type of FS_INFORMATION_CLASS that is requested to the network mini-redirector driver. RDBSS passes information in the <b>FsInformationClass</b> member when calling <b>MrxQueryVolumeInfo </b>and <b>MrxSetVolumeInfo</b>. </p>
</dd>

### -field <b>FileInformationClass</b>

<dd>
<p>A member of an unnamed union used by RDBSS to indicate the type of FILE_INFORMATION_CLASS request sent to the network mini-redirector driver. RDBSS passes information in the <b>FileInformationClass</b> member when calling <b>MrxQueryDirectory</b>, <b>MrxQueryFileInfo</b>, and <b>MrxSetFileInfo</b>. </p>
</dd>

### -field <b>Buffer</b>

<dd>
<p>A buffer used to pass data from RDBSS to the network mini-redirector driver and receive responses from the network mini-redirector driver by RDBSS. The <b>Buffer</b> member is used in the <b>MrxQueryDirectory</b>, <b>MrxQueryFileInfo</b>, <b>MrxQueryVolumeInfo</b>, <b>MrxSetFileInfo</b>, <b>MRxSetFileInfoAtCleanup</b>, and <b>MrxSetVolumeInfo</b> routines. </p>
</dd>

### -field <b>Length</b>

<dd>
<p>A member of an unnamed union used to pass the length of the <b>Buffer</b> member from RDBSS to the network mini-redirector driver. The <b>Length</b> member is used in the <b>MrxQueryDirectory</b>, <b>MrxQueryFileInfo</b>, <b>MrxQueryVolumeInfo</b>, <b>MrxSetFileInfo</b>, <b>MRxSetFileInfoAtCleanup</b>, and <b>MrxSetVolumeInfo</b> routines. </p>
</dd>

### -field <b>LengthRemaining</b>

<dd>
<p>A member of an unnamed union used to pass the length of information returned in the <b>Buffer</b> member from the network mini-redirector driver to RDBSS. The <b>LengthRemaining</b> member is used in the <b>MrxQueryDirectory</b>, <b>MrxQueryFileInfo</b>, <b>MrxQueryVolumeInfo</b>, <b>MrxSetFileInfo</b>, <b>MRxSetFileInfoAtCleanup</b>, and <b>MrxSetVolumeInfo</b> routines. </p>
</dd>

### -field <b>ReplaceIfExists</b>

<dd>
<p>A Boolean value that indicates if an existing file should be replaced during a rename operation. The <b>ReplaceIfExists</b> member is used in the <b>MrxSetFileInfo</b> routine.</p>
</dd>

### -field <b>AdvanceOnly</b>

<dd>
<p>This member is reserved for internal use.</p>
</dd>
</dl>
</dd>

### -field <b>PrefixClaim</b>

<dd>
<p>A structure member of an unnamed union used for prefix resolution requests sent from the Multiple UNC Provider (MUP). A prefix claim results from an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548649">IRP_MJ_DEVICE_CONTROL</a> request from MUP to RDBSS for <a href="https://msdn.microsoft.com/library/windows/hardware/ff548313">IOCTL_REDIR_QUERY_PATH</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548320">IOCTL_REDIR_QUERY_PATH_EX</a>. RDBSS passes information in the <b>PrefixClaim</b> structure to the network mini-redirector and the network mini-redirector returns information to RDBSS in the <b>PrefixClaim</b> structure. </p>
<dl>

### -field <b>SuppliedPathName</b>

<dd>
<p>A non-NULL terminated Unicode string specifying the UNC path on which to perform the prefix resolution. </p>
</dd>

### -field <b>NetRootType</b>

<dd>
<p>The type of the NET_ROOT requested. This member is not currently used. RDBSS deduces the type of the NET_ROOT from the <b>SuppliedPathName</b> member.</p>
</dd>

### -field <b>pSecurityContext</b>

<dd>
<p>A pointer to the security context passed in from the request from MUP. </p>
<p>This member is not currently used. The security context is passed in the <b>Create.NtCreateParameters.SecurityContext</b> member of the RX_CONTEXT, not in this member.</p>
</dd>
</dl>
</dd>

### -field <b>Create</b>

<dd>
<p>A structure member of an unnamed union used for handling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a> requests. This member is used for handling file open requests that result in calls to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549862">MRxCreate</a> routine. This member is also used for prefix resolution requests. RDBSS passes information in the <b>Create</b> structure member to the network mini-redirector and the network mini-redirector returns information to RDBSS in the <b>Create</b> structure member. </p>
<dl>

### -field <b>NtCreateParameters</b>

<dd>
<p>The create parameters passed to the user-mode <b>NtCreatefile</b> routine. RDBSS sets the members of the <b>NtCreateParameters</b> structure based on the <b>Parameters.Create</b> members of the IRP.</p>
</dd>

### -field <b>ReturnedCreateInformation</b>

<dd>
<p>A value set by the network mini-redirector on completion of the <b>MRxCreate</b> call.</p>
</dd>

### -field <b>CanonicalNameBuffer</b>

<dd>
<p>A pointer to the Unicode string representing the name of physical file to open if the canonical name is larger than the available buffer. </p>
</dd>

### -field <b>NetNamePrefixEntry</b>

<dd>
<p>A pointer to the NetName table prefix entry. This member is reserved for internal use.</p>
</dd>

### -field <b>pSrvCall</b>

<dd>
<p>A pointer to the associated SRV_CALL structure.</p>
</dd>

### -field <b>pNetRoot</b>

<dd>
<p>A pointer to the associated NET_ROOT structure.</p>
</dd>

### -field <b>pVNetRoot</b>

<dd>
<p>A pointer to the associated V_NET_ROOT structure.</p>
</dd>

### -field <b>EaBuffer</b>

<dd>
<p>A pointer to the extended attributes buffer. This member is optional.</p>
</dd>

### -field <b>EaLength</b>

<dd>
<p>The length of the extended attributes buffer, <b>EaBuffer</b>.</p>
</dd>

### -field <b>SdLength</b>

<dd>
<p>The length of the security descriptor. RDBSS sets this based on the value of the <b>Parameters.Create.SecurityContext</b> member of the IRP. If the <b>SdLength</b> member is nonzero, the security descriptor is passed in the <b>Info.Buffer</b> member to the network mini-redirector.</p>
</dd>

### -field <b>PipeType</b>

<dd>
<p>The type of a pipe. This member is reserved for internal use.</p>
</dd>

### -field <b>PipeReadMode</b>

<dd>
<p>The read mode for a pipe. This member is reserved for internal use.</p>
</dd>

### -field <b>PipeCompletionMode</b>

<dd>
<p>The completion mode for a pipe. This member is reserved for internal use.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>The create flags</p>
</dd>

### -field <b>Type</b>

<dd>
<p>The type of the associated NET_ROOT structure. </p>
</dd>

### -field <b>FcbAcquired</b>

<dd>
<p>This member is reserved for internal use.</p>
</dd>

### -field <b>TryForScavengingOnSharingViolation</b>

<dd>
<p>This member is reserved for internal use.</p>
</dd>

### -field <b>ScavengingAlreadyTried</b>

<dd>
<p>This member is reserved for internal use.</p>
</dd>

### -field <b>ThisIsATreeConnectOpen</b>

<dd>
<p>A Boolean value that indicates if this call is a tree connect open request with the FILE_CREATE_TREE_CONNECTION option set in the <b>IrpSp-&gt;Parameters.Create.Options</b> member.</p>
</dd>

### -field <b>TreeConnectOpenDeferred</b>

<dd>
<p>A Boolean value that indicates the network mini-redirector can choose to defer the tree connect open request. </p>
</dd>

### -field <b>TransportName</b>

<dd>
<p>A Unicode string that represents the transport name. This member is set from the tree connect open parameters. </p>
</dd>

### -field <b>UserName</b>

<dd>
<p>A Unicode string that represents the user name responsible for the request. This member is set from the tree connect open parameters. </p>
</dd>

### -field <b>Password</b>

<dd>
<p>A Unicode string that contains the password for this <b>UserName</b> used for authentication and authorization. This member is set from the tree connect open parameters. </p>
</dd>

### -field <b>UserDomainName</b>

<dd>
<p>A Unicode string that contains the domain name for this <b>UserName</b>. </p>
</dd>
</dl>
</dd>

### -field <b>QueryDirectory</b>

<dd>
<p>A structure member of an unnamed union used for handling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548658">IRP_MJ_DIRECTORY_CONTROL</a> requests. This member is used for handling query directory requests that result in calls to the <b>MrxQueryDirectory</b> routine. RDBSS passes information in the <b>QueryDirectory</b> structure member to the network mini-redirector. </p>
<dl>

### -field <b>FileIndex</b>

<dd>
<p>The Index of the entry at which to begin scanning the directory if the <b>IndexSpecified</b> member is set to <b>TRUE</b>. This parameter is set to the <b>IrpSp-&gt;Parameters.QueryDirectory.FileIndex</b> member.</p>
</dd>

### -field <b>RestartScan</b>

<dd>
<p>A Boolean value when set to <b>TRUE</b> indicates that the scan is to start at the first entry in the directory. When this value is set to <b>FALSE</b>, the scan is resuming from a previous call. This parameter must be set to <b>TRUE</b> when calling for the first time. This parameter is set to <b>TRUE</b> if <b>IrpSp-&gt;Flags</b> has the SL_RESTART_SCAN bit on.</p>
</dd>

### -field <b>ReturnSingleEntry</b>

<dd>
<p>A Boolean value set to <b>TRUE</b> indicates that only a single entry should be returned. If this parameter is <b>TRUE</b>, <b>MrxQueryDirectory</b> should return only the first entry that is found. This parameter is set to <b>TRUE</b> if <b>IrpSp-&gt;Flags</b> has the SL_RETURN_SINGLE_ENTRY bit on.</p>
</dd>

### -field <b>IndexSpecified</b>

<dd>
<p>A Boolean value when set to <b>TRUE</b> indicates to begin the scan at the entry in the directory whose index is given by the <b>FileIndex</b> member. This parameter is set to <b>TRUE</b> if <b>IrpSp-&gt;Flags</b> has the SL_INDEX_SPECIFIED bit on.</p>
</dd>

### -field <b>InitialQuery</b>

<dd>
<p>A Boolean value that is set to <b>TRUE</b> when the query is not a wild card query ("*.*", for example). This member is set to <b>TRUE</b> if the <b>UnicodeQueryTemplate.Buffer</b> member of the associated FOBX is <b>NULL</b> and the <b>Flags</b> member of the FOBX does not have the FOBX_FLAG_MATCH_ALL bit on. For a wild card query ("*.*", for example), RDBSS will set the <b>UnicodeQueryTemplate.Buffer</b> member of the associated FOBX to the wild card query passed.</p>
</dd>
</dl>
</dd>

### -field <b>NotifyChangeDirectory</b>

<dd>
<p>A structure member of an unnamed union used for handling IRP_MJ_DIRECTORY_CONTROL requests with a minor function of IRP_MN_NOTIFY_CHANGE_DIRECTORY. This member is used for handling directory change requests that result in calls to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550721">MRxLowIOSubmit[LOWIO_OP_NOTIFY_CHANGE_DIRECTORY]</a> routine. RDBSS passes information in the <b>NotifyChangeDirectory</b> structure member and the <b>pLowIoContext-&gt;ParamsFor.NotifyChangeDirectory</b> structure to the network mini-redirector. </p>
<dl>

### -field <b>pVNetRoot</b>

<dd>
<p>A pointer to the V_NET_ROOT structure associated with the directory. This parameter is set to the <b>IrpSp-&gt;FileObject-&gt;FsContext</b> member or the <b>IrpSp-&gt;FileObject-&gt;FsContext2</b> member depending on the node type. </p>
</dd>
</dl>
</dd>

### -field <b>QueryEa</b>

<dd>
<p>A structure member of an unnamed union used for handling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549279">IRP_MJ_QUERY_EA</a> requests. This member is used for handling extended attribute query requests that result in calls to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550759">MRxQueryEaInfo</a> routine. RDBSS passes information in the <b>QueryEa</b> structure member to the network mini-redirector. </p>
<dl>

### -field <b>UserEaList</b>

<dd>
<p>A pointer to a caller-supplied input buffer containing a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540295">FILE_GET_EA_INFORMATION</a> structure specifying the extended attributes to be queried. This parameter is set to <b>IrpSp-&gt;Parameters.QueryEa.EaList</b>.</p>
</dd>

### -field <b>UserEaListLength</b>

<dd>
<p>The length, in bytes, of the buffer pointed to by <b>UserEaList</b> member. This parameter is set to <b>IrpSp-&gt;Parameters.QueryEa.EaListLength</b>.</p>
</dd>

### -field <b>UserEaIndex</b>

<dd>
<p>The Index of the entry at which to begin scanning the extended-attribute list. This parameter should be ignored if the <b>IndexSpecified</b> member is not set to <b>TRUE</b> or if <b>QueryEaList</b> member points to a nonempty list. This parameter is set to <b>IrpSp-&gt;Parameters.QueryEa.EaIndex</b>.</p>
</dd>

### -field <b>RestartScan</b>

<dd>
<p>A Boolean value when set to <b>TRUE</b> indicates that the query is to start at the first extended attribute entry. When this value is set to <b>FALSE</b>, the scan is resuming from a previous call. This parameter must be set to <b>TRUE</b> when calling for the first time. This parameter is set to <b>TRUE if IrpSp-&gt;Flags</b> has the SL_RESTART_SCAN bit on. </p>
</dd>

### -field <b>ReturnSingleEntry</b>

<dd>
<p>A Boolean value when set to <b>TRUE</b> indicates that only a single entry should be returned. If this parameter is <b>TRUE</b>, MrxQueryEaInfo should return only the first entry that is found. This parameter is set to <b>TRUE</b> if <b>IrpSp-&gt;Flags</b> has the SL_RETURN_SINGLE_ENTRY bit on. </p>
</dd>

### -field <b>IndexSpecified</b>

<dd>
<p>A Boolean value when set to <b>TRUE</b> indicates to begin the scan at the entry in the extended attributes whose index is given by the <b>UserEaIndex</b> member. This parameter is set to <b>TRUE</b> if <b>IrpSp-&gt;Flags</b> has the SL_INDEX_SPECIFIED bit on. </p>
</dd>
</dl>
</dd>

### -field <b>QuerySecurity</b>

<dd>
<p>A structure member of an unnamed union used for handling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549298">IRP_MJ_QUERY_SECURITY</a> requests. This member is used for handling query security requests that result in calls to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550776">MRxQuerySdInfo</a> routine. RDBSS passes information in the <b>QuerySecurity</b> structure member to the network mini-redirector. </p>
<dl>

### -field <b>SecurityInformation</b>

<dd>
<p>A pointer to a caller-supplied input buffer containing a SECURITY_INFORMATION structure specifying the operation to be queried. This parameter is set to <b>IrpSp-&gt;Parameters.QuerySecurity.SecurityInformation</b>.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>The length, in bytes, of the buffer pointed to by <b>SecurityInformation</b> member. This parameter is set to <b>IrpSp-&gt;Parameters.QuerySecurity.Length</b>.  </p>
</dd>
</dl>
</dd>

### -field <b>SetSecurity</b>

<dd>
<p>A structure member of an unnamed union used for handling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549407">IRP_MJ_SET_SECURITY</a> requests. This member is used for handling query security requests that result in calls to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550805">MRxSetSdInfo</a> routine. RDBSS passes information in the <b>SetSecurity</b> structure member to the network mini-redirector. </p>
<dl>

### -field <b>SecurityInformation</b>

<dd>
<p>A pointer to a caller-supplied input buffer containing a SECURITY_INFORMATION structure that specifies which security information is to be set in the security descriptor. This parameter is set to <b>IrpSp-&gt;Parameters.SetSecurity.SecurityInformation</b>. 
</p>
</dd>

### -field <b>SecurityDescriptor</b>

<dd>
<p>A pointer to a SECURITY_DESCRIPTOR structure that contains the values of the security information to be assigned to the object. This parameter is set to <b>IrpSp-&gt;Parameters.SetSecurity.SecurityDescriptor</b>.</p>
</dd>
</dl>
</dd>

### -field <b>QueryQuota</b>

<dd>
<p>A structure member of an unnamed union used for handling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549293">IRP_MJ_QUERY_QUOTA</a> requests. This member is used for handling query security requests that result in calls to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550773">MRxQueryQuotaInfo</a> routine. RDBSS passes information in the <b>QueryQuota</b> structure member to the network mini-redirector. </p>
<dl>

### -field <b>Length</b>

<dd>
<p>The length, in bytes, of the buffer pointed to by <b>StartSid</b> member. This parameter is set to <b>IrpSp-&gt;Parameters.QueryQuota.Length</b>. </p>
</dd>

### -field <b>StartSid</b>

<dd>
<p>An optional pointer to a SID that indicates that the returned information is to start with an entry other than the first entry. This parameter is ignored if the <b>SidList</b> member is specified. This parameter is set to <b>IrpSp-&gt;Parameters.QueryQuota.StartSid</b>.</p>
</dd>

### -field <b>SidList</b>

<dd>
<p>An optional pointer to a list of SIDs whose quota information is to be returned. Each entry in the list is a FILE_GET_QUOTA_INFORMATION structure. This parameter is set to <b>IrpSp-&gt;Parameters.QueryQuota.SidList</b>.</p>
</dd>

### -field <b>SidListLength</b>

<dd>
<p>The length, in bytes, of the list of SIDs in the <b>SidList</b> member, if one is specified. This parameter is set to <b>IrpSp-&gt;Parameters.QueryQuota.SidListLength</b>.</p>
</dd>

### -field <b>RestartScan</b>

<dd>
<p>A Boolean value when set to <b>TRUE</b> indicates that the query is to start at the first entry. When this value is set to <b>FALSE</b>, the scan is resuming from a previous call. This parameter must be set to <b>TRUE</b> when calling for the first time. This parameter is set to <b>TRUE</b> if <b>IrpSp-&gt;Flags</b>has the SL_RESTART_SCAN bit on. </p>
</dd>

### -field <b>ReturnSingleEntry</b>

<dd>
<p>A Boolean value when set to <b>TRUE</b> indicates that only a single entry should be returned. If this parameter is <b>TRUE</b>, MrxQueryQuotaInfo should return only the first entry that is found. This parameter is set to <b>TRUE</b> if <b>IrpSp-&gt;Flags</b> has the SL_RETURN_SINGLE_ENTRY bit on. </p>
</dd>

### -field <b>IndexSpecified</b>

<dd>
<p>A Boolean value when set to <b>TRUE</b> indicates to begin the scan at the entry in the list whose index is given by the <b>StartSid</b> member. This parameter is set to <b>TRUE</b> if <b>IrpSp-&gt;Flags </b>has the SL_INDEX_SPECIFIED bit on. </p>
</dd>
</dl>
</dd>

### -field <b>SetQuota</b>

<dd>
<p>A structure member of an unnamed union used for handling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549401">IRP_MJ_SET_QUOTA</a> requests. This structure is not currently used by RDBSS. </p>
<dl>

### -field <b>Length</b>

<dd>
<p>An unused member of the <b>SetQuota</b> structure. </p>
</dd>
</dl>
</dd>

### -field <b>DosVolumeFunction</b>

<dd>
<p>A structure member of an unnamed union. This structure is not currently used by RDBSS. </p>
<dl>

### -field <b>VNetRoot</b>

<dd>
<p>An unused member of the <b>DosVolumeFunction</b> structure. </p>
</dd>

### -field <b>SrvCall</b>

<dd>
<p>An unused member of the <b>DosVolumeFunction</b> structure. </p>
</dd>

### -field <b>NetRoot</b>

<dd>
<p>An unused member of the <b>DosVolumeFunction</b> structure. </p>
</dd>
</dl>
</dd>

### -field ( <i>unnamed struct</i> )

<dd>
<p>The unique node type used for an RX_CONTEXT structure. All of the major structure types (RX_CONTEXT, SRV_CALL, NET_ROOT, V_NET_ROOT, SRV_OPEN, FCB, and FOBX, for example) used by RDBSS have a unique two-byte node type code defined in the <i>nodetype.h</i> include file which can be used for debugging. RDBSS sets this member to RDBSS_NTC_RX_CONTEXT when an RX_CONTEXT is initialized in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554502">RxInitializeContext</a> routine. If a network mini-redirector driver initializes an RX_CONTEXT structure using some other method, this member must be set.</p>
<p>RDBSS defines this member as part of a standard header for all structures used by RDBSS. </p>
<dl>

### -field <b>FlagsForLowIo</b>

<dd>
<p>A set of options set by RDBSS and passed to low I/O operations sent to the network mini-redirector. <b>FlagsForLowIo</b> is a member of unnamed structure used for low I/O requests to the network mini-redirector.</p>
</dd>

### -field <b>LowIoContext</b>

<dd>
<p>A pointer to a LOWIO_CONTEXT structure passed to the network mini-redirector. <b>LowIoContext</b> is a member of unnamed structure used for low I/O requests sent to the network mini-redirector.</p>
</dd>
</dl>
</dd>

### -field <b>FsdUid</b>

<dd>
<p>The effective user ID if <a href="https://msdn.microsoft.com/library/windows/hardware/ff554736">RxStartMinirdr</a> was called using a user-mode process thread. This member is not used by RDBSS.</p>
</dd>

### -field <b>AlsoCanonicalNameBuffer</b>

<dd></dd>

### -field <b>LoudCompletionString</b>

<dd>
<p>An unused member of the RX_CONTEXT structure.</p>
</dd>

### -field <b>AcquireReleaseFcbTrackerX</b>

<dd></dd>

### -field <b>TrackerHistoryPointer</b>

<dd></dd>

### -field <b>TrackerHistory</b>

<dd></dd>
</dl>

## -remarks
<p>The RX_CONTEXT structure is one of the fundamental data structures used by RDBSS and network mini-redirectors to manage an I/O request packet (IRP). The RX_CONTEXT data structure encapsulates an IRP for use by RDBSS, network mini-redirectors, and the file system. An RX_CONTEXT structure includes a pointer to a single IRP and all of the context required to process the IRP. </p>

<p>An RX_CONTEXT structure is sometimes referred to as an IRP Context or RxContext in the Window Driver Kit (WDK) or IFS Kit header files and other resources used for developing network mini-redirector drivers.</p>

<p>The RX_CONTEXT is a data structure to which additional information provided by the various network mini redirectors is attached. The RX_CONTEXT includes fields for over allocating the size of each RX_CONTEXT structure by a pre-specified amount for each network mini redirector, which is then reserved for use by the mini redirector. This approach consists of allocating a pre-specified area, which is the same for all network mini redirectors as part of each RX_CONTEXT. This is an unformatted area on top of which any desired structure can be imposed by the various network mini redirectors. Developers of network mini-redirector drivers should try and define the associated private context to fit into this pre-specified area defined in the RX_CONTEXT data structure. Network mini-redirector drivers that violate this rule will incur a significant performance penalty.</p>

<p>Many RDBSS routines and routines exported by a network mini-redirector make reference to RX_CONTEXT structures in either the initiating thread or in some other thread used by the routine. Thus, allocated RX_CONTEXT structures are reference counted to manage their use for asynchronous operations. When the reference count goes to zero, the allocated RX_CONTEXT structure can be finalized and released on the last dereference operation.</p>

<p>RDBSS provides a number of routines that are used to manipulate an RX_CONTEXT and the associated IRP. These routines are used to allocate, initialize, and delete an RX_CONTEXT. These routines are also used to complete the IRP associated with an RX_CONTEXT and set up a cancel routine for an RX_CONTEXT. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Rxcontx.h (include Rx.h or Rxcontx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540295">FILE_GET_EA_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548354">IoCompletion</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549422">IoMarkIrpPending</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548313">IOCTL_REDIR_QUERY_PATH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548320">IOCTL_REDIR_QUERY_PATH_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548649">IRP_MJ_DEVICE_CONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548658">IRP_MJ_DIRECTORY_CONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549279">IRP_MJ_QUERY_EA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549293">IRP_MJ_QUERY_QUOTA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549298">IRP_MJ_QUERY_SECURITY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549401">IRP_MJ_SET_QUOTA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549407">IRP_MJ_SET_SECURITY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549862">MRxCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550721">MRxLowIOSubmit[LOWIO_OP_NOTIFY_CHANGE_DIRECTORY]</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550755">MRxQueryDirectory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550759">MRxQueryEaInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550770">MRxQueryFileInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550773">MRxQueryQuotaInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550776">MRxQuerySdInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550782">MRxQueryVolumeInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550790">MRxSetFileInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550796">MRxSetFileInfoAtCleanup</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550805">MRxSetSdInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550810">MRxSetVolumeInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554367">RxCreateRxContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554502">RxInitializeContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554736">RxStartMinirdr</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RX_CONTEXT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
