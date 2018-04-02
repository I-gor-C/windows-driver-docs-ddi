---
UID: NS:ntifs._FSRTL_ADVANCED_FCB_HEADER
title: "_FSRTL_ADVANCED_FCB_HEADER"
author: windows-driver-content
description: The FSRTL_ADVANCED_FCB_HEADER structure contains context information that a file system maintains about a file.
old-location: ifsk\fsrtl_advanced_fcb_header.htm
old-project: ifsk
ms.assetid: 7816c937-109c-40a8-8b67-04413b00e5fd
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PFSRTL_ADVANCED_FCB_HEADER, *PFSRTL_UNC_PROVIDER_REGISTRATION, FSRTL_ADVANCED_FCB_HEADER, FSRTL_ADVANCED_FCB_HEADER structure [Installable File System Drivers], FSRTL_UNC_PROVIDER_REGISTRATION, PFSRTL_ADVANCED_FCB_HEADER, PFSRTL_ADVANCED_FCB_HEADER structure pointer [Installable File System Drivers], _FSRTL_ADVANCED_FCB_HEADER, contextstructures_cede2315-2c72-496f-a192-3ef25a8b0516.xml, ifsk.fsrtl_advanced_fcb_header, ntifs/FSRTL_ADVANCED_FCB_HEADER, ntifs/PFSRTL_ADVANCED_FCB_HEADER"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntifs.h
api_name:
-	FSRTL_ADVANCED_FCB_HEADER
product: Windows
targetos: Windows
req.typenames: FSRTL_ADVANCED_FCB_HEADER, FSRTL_UNC_PROVIDER_REGISTRATION, *PFSRTL_UNC_PROVIDER_REGISTRATION
---

# _FSRTL_ADVANCED_FCB_HEADER structure
The <b>FSRTL_ADVANCED_FCB_HEADER</b> structure contains context information that a file system maintains about a file.

## Syntax
```
typedef struct _FSRTL_ADVANCED_FCB_HEADER {
  struct {
    FSRTL_COMMON_FCB_HEADER DUMMYSTRUCTNAME;
    PFAST_MUTEX             FastMutex;
    PVOID                   *FileContextSupportPointer;
    LIST_ENTRY              FilterContexts;
    EX_PUSH_LOCK            PushLock;
    PVOID                   ReservedContext;
    struct {
      OPLOCK Oplock;
      PVOID  ReservedForRemote;
    };
  } _FSRTL_ADVANCED_FCB_HEADER;
  struct {
    LIST_ENTRY EofWaitLinks;
    KEVENT     Event;
  } _EOF_WAIT_BLOCK;
  struct {
    PVOID Buffer;
    ULONG Flags;
    ULONG Length;
    PMDL  Mdl;
  } _FSRTL_AUXILIARY_BUFFER;
  struct {
    LARGE_INTEGER EndingByte;
    BOOLEAN       ExclusiveLock;
    PFILE_OBJECT  FileObject;
    ULONG         Key;
    LARGE_INTEGER Length;
    PVOID         ProcessId;
    LARGE_INTEGER StartingByte;
  } _FILE_LOCK_INFO;
  struct {
    PCOMPLETE_LOCK_IRP_ROUTINE CompleteLockIrpRoutine;
    BOOLEAN                    FastIoIsQuestionable;
    PVOID                      LastReturnedLock;
    FILE_LOCK_INFO             LastReturnedLockInfo;
    PVOID                      LockInformation;
    LONG                       LockRequestsInProgress;
    BOOLEAN                    SpareC[3];
    PUNLOCK_ROUTINE            UnlockRoutine;
  } _FILE_LOCK;
  struct {
    PRTL_SPLAY_LINKS Cache;
    FAST_MUTEX       Mutex;
    USHORT           NumEntries;
    LIST_ENTRY       TimerQueue;
  };
  UCHAR const *LEGAL_ANSI_CHARACTER_ARRAY;
  PUSHORT     NLS_OEM_LEAD_BYTE_INFO;
  struct {
    USHORT Flags;
    PVOID  Mapping;
    ULONG  MaximumPairCount;
    ULONG  PairCount;
    USHORT PoolType;
  } _BASE_MCB;
  struct {
    BASE_MCB        BaseMcb;
    PKGUARDED_MUTEX GuardedMutex;
  } _LARGE_MCB;
  struct {
    LARGE_MCB DummyFieldThatSizesThisStructureCorrectly;
  } _MCB;
  struct {
    GUID  OplockKey;
    ULONG Reserved;
  } _OPLOCK_KEY_ECP_CONTEXT;
  GUID        GUID_ECP_OPLOCK_KEY;
  struct {
    GUID    ParentOplockKey;
    BOOLEAN ParentOplockKeySet;
    GUID    TargetOplockKey;
    BOOLEAN TargetOplockKeySet;
  } _DUAL_OPLOCK_KEY_ECP_CONTEXT;
  GUID        GUID_ECP_DUAL_OPLOCK_KEY;
  struct      _REAL_NOTIFY_SYNC;
  USHORT      Version;
  union {
    FSRTL_UNC_PROVIDER_FLAGS ProviderFlags;
    struct {
      ULONG  : 1 MailslotsSupported;
      ULONG  : 1 CscEnabled;
      ULONG  : 1 DomainSvcAware;
      ULONG  : 1 ContainersAware;
    } DUMMYSTRUCTNAME;
  } DUMMYUNIONNAME;
  union {
    FSRTL_UNC_HARDENING_CAPABILITIES HardeningCapabilities;
    struct {
      ULONG  : 1 SupportsMutualAuth;
      ULONG  : 1 SupportsIntegrity;
      ULONG  : 1 SupportsPrivacy;
    } DUMMYSTRUCTNAME;
  } DUMMYUNIONNAME2;
  base_class  FSRTL_COMMON_FCB_HEADER;
} *PFSRTL_UNC_PROVIDER_REGISTRATION, FSRTL_UNC_PROVIDER_REGISTRATION, FSRTL_ADVANCED_FCB_HEADER;
```

## Members


`_FSRTL_ADVANCED_FCB_HEADER`



`_EOF_WAIT_BLOCK`



`_FSRTL_AUXILIARY_BUFFER`



`_FILE_LOCK_INFO`



`_FILE_LOCK`



`LEGAL_ANSI_CHARACTER_ARRAY`



`NLS_OEM_LEAD_BYTE_INFO`



`_BASE_MCB`



`_LARGE_MCB`



`_MCB`



`_OPLOCK_KEY_ECP_CONTEXT`



`GUID_ECP_OPLOCK_KEY`



`_DUAL_OPLOCK_KEY_ECP_CONTEXT`



`GUID_ECP_DUAL_OPLOCK_KEY`



`_REAL_NOTIFY_SYNC`



`Version`



`DUMMYUNIONNAME`



`DUMMYUNIONNAME2`



`FSRTL_COMMON_FCB_HEADER`



## Remarks
The <b>FSRTL_ADVANCED_FCB_HEADER</b> structure is a superset of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547343">FSRTL_COMMON_FCB_HEADER</a> structure. File systems (including legacy filter and minifilter drivers, when applicable) must use the <b>FSRTL_ADVANCED_FCB_HEADER</b> structure. 

File systems must use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547257">FsRtlSetupAdvancedHeader</a> macro or the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547263">FsRtlSetupAdvancedHeaderEx</a> macro to initialize an <b>FSRTL_ADVANCED_FCB_HEADER</b> structure.

The following flags are set by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547257">FsRtlSetupAdvancedHeader</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff547263">FsRtlSetupAdvancedHeaderEx</a> macros.

<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
FSRTL_FLAG_ADVANCED_HEADER

</td>
<td>
Set in the <b>Flags</b> member of the  <a href="https://msdn.microsoft.com/library/windows/hardware/ff547343">FSRTL_COMMON_FCB_HEADER</a> structure, this flag indicates file system driver support for <b>FSRTL_ADVANCED_FCB_HEADER</b> structures.  This flag should not be modified.

</td>
</tr>
<tr>
<td>
FSRTL_FLAG2_SUPPORTS_FILTER_CONTEXTS

</td>
<td>
Set in the <b>Flags2</b> member of  <a href="https://msdn.microsoft.com/library/windows/hardware/ff547343">FSRTL_COMMON_FCB_HEADER</a>, this flag indicates support for filter driver contexts.  This flag can only be cleared for paging files (see information after the table).

</td>
</tr>
<tr>
<td>
FSRTL_FCB_HEADER_V1

</td>
<td>
Set in the <b>Version</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff547343">FSRTL_COMMON_FCB_HEADER</a>, this value indicates support for the <b>PushLock</b> and <b>FilterContextPointer</b> members.  This flag should not be modified.

</td>
</tr>
<tr>
<td>
FSRTL_FCB_HEADER_V2

</td>
<td>
Set in the <b>Version</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff547343">FSRTL_COMMON_FCB_HEADER</a>, this value indicates support for the <b>PushLock</b>, <b>FilterContextPointer</b>, <b>Oplock</b>, and <b>ReservedForRemote</b> members.  This flag should not be modified.

</td>
</tr>
</table>
 

File systems must set the <b>FsContext</b> member of every file object to point to an <b>FSRTL_ADVANCED_FCB_HEADER</b> structure. This structure can be embedded inside of a context object structure that is specific to a file-system stream  (the remainder of the structure is file-system–specific). Usually, this structure is a file control block (FCB). However, on some file systems that support multiple data streams, such as NTFS, it is a stream control block (SCB).  Note that FCBs and SCBs for all classes of open requests, including volume open requests, must include this structure.

If the file is a paging file, the <b>FSRTL_ADVANCED_FCB_HEADER</b> structure must be allocated from a nonpaged pool. Otherwise, it can be allocated from a paged or nonpaged pool. 

All Microsoft file systems disable stream context support for paging files by clearing the <b>FSRTL_FLAG2_SUPPORTS_FILTER_CONTEXTS</b> flag in the <b>Flags2</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff547343">FSRTL_COMMON_FCB_HEADER</a> after they call <a href="https://msdn.microsoft.com/library/windows/hardware/ff547257">FsRtlSetupAdvancedHeader</a>. (See the <b>FatCreateFcb</b> function in <i>Strucsup.c</i> for the FASTFAT WDK sample.) You are strongly encouraged to do the same in your file system or systems so that the operating system will behave in a consistent manner across all file systems.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntifs.h (include Ntifs.h, Fltkernel.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff547343">FSRTL_COMMON_FCB_HEADER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547357">FSRTL_PER_STREAM_CONTEXT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546194">FsRtlInsertPerStreamContext</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546945">FsRtlLookupPerStreamContext</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547238">FsRtlRemovePerStreamContext</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547257">FsRtlSetupAdvancedHeader</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547263">FsRtlSetupAdvancedHeaderEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547295">FsRtlTeardownPerStreamContexts</a>