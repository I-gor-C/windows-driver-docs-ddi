---
UID : NF:ntifs.FsRtlFastLock
title : FsRtlFastLock macro
author : windows-driver-content
description : The FsRtlFastLock macro is used by file systems and filter drivers to request a byte-range lock for a file stream.
old-location : ifsk\fsrtlfastlock.htm
old-project : ifsk
ms.assetid : c3e209b5-9925-4911-8c42-0f15c1c710be
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : FsRtlFastLock, ifsk.fsrtlfastlock, FsRtlFastLock function [Installable File System Drivers], fsrtlref_c60db87b-ac5a-4c60-83f2-7381e0156806.xml, ntifs/FsRtlFastLock
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : macro
req.header : ntifs.h
req.include-header : Ntifs.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : ntifs.h
req.dll : 
req.irql : <= APC_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : TOKEN_TYPE
---


# FsRtlFastLock function
The <b>FsRtlFastLock</b> macro is used by file systems and filter drivers to request a byte-range lock for a file stream.

## Syntax

````
BOOLEAN FsRtlFastLock(
  _In_  PFILE_LOCK       FileLock,
  _In_  PFILE_OBJECT     FileObject,
  _In_  PLARGE_INTEGER   FileOffset,
  _In_  PLARGE_INTEGER   Length,
  _In_  PEPROCESS        ProcessId,
  _In_  ULONG            Key,
  _In_  BOOLEAN          FailImmediately,
  _In_  BOOLEAN          ExclusiveLock,
  _Out_ PIO_STATUS_BLOCK Iosb,
  _In_  PVOID            Context,
  _In_  BOOLEAN          AlreadySynchronized
);
````

## Parameters

`A1`

TBD

`A2`

TBD

`A3`

TBD

`A4`

TBD

`A5`

TBD

`A6`

TBD

`A7`

TBD

`A8`

TBD

`A9`

TBD

`A10`

TBD

`A11`

TBD


## Return Value

None

## Remarks

The <b>FsRtlFastLock</b> macro causes the caller to acquire a byte-range lock on a region of the specified file.

A return value of <b>TRUE</b> indicates that the IO_STATUS_BLOCK structure pointed to by <i>Iosb</i> received status information about the lock operation. To examine the contents of this structure, use the NT_STATUS macro.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** |  |
| **IRQL** | <= APC_LEVEL |
| **DDI compliance rules** |  |

## See Also

<a href="..\ntifs\nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlallocatefilelock~r1.md">FsRtlAllocateFileLock</a>

<a href="..\ntifs\nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlinitializefilelock~r2.md">FsRtlInitializeFileLock</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlFastLock function%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>