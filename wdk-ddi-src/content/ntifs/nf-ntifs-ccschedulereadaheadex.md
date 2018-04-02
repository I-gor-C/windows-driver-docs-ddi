---
UID: NF:ntifs.CcScheduleReadAheadEx
title: CcScheduleReadAheadEx function
author: windows-driver-content
description: The CcScheduleReadAheadEx routine performs read-ahead (also called &#0034;lazy read&#0034;) on a cached file. The I/O byte count for the operation is charged to the issuing thread.
old-location: ifsk\ccschedulereadaheadex.htm
old-project: ifsk
ms.assetid: 8549DAA9-3BD3-4CED-AC2A-EFADF317EF5A
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CcScheduleReadAheadEx, CcScheduleReadAheadEx routine [Installable File System Drivers], ifsk.ccschedulereadaheadex, ntifs/CcScheduleReadAheadEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
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
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: "<= APC_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	CcScheduleReadAheadEx
product: Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# CcScheduleReadAheadEx function
The <b>CcScheduleReadAheadEx</b> routine performs read-ahead (also called "lazy read") on a cached file. The I/O byte count for the operation is charged to the issuing thread.

## Syntax

```
NTKERNELAPI VOID CcScheduleReadAheadEx(
  PFILE_OBJECT   FileObject,
  PLARGE_INTEGER FileOffset,
  ULONG          Length,
  PETHREAD       IoIssuerThread
);
```

## Parameters

`FileObject`

Pointer to a file object for the file on which read-ahead is to be performed.

`FileOffset`

Pointer to a variable that specifies the starting byte offset within the cached file where the last read occurred.

`Length`

Length in bytes of the range that was last read.

`IoIssuerThread`

The thread issuing the read ahead request. For a file system with disk I/O accounting enabled, this is the thread the I/O is charged to. If <i>IoIssuerThread</i> is NULL, the I/O is charged to the current thread.


## Return Value

None

## Remarks

<b>CcScheduleReadAheadEx</b> should be called only when <i>Length</i> &gt;= 256. Measurements have shown that calling <b>CcScheduleReadAheadEx</b> for smaller reads actually decreases performance.

<b>CcScheduleReadAheadEx</b> can only be called after a successful call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539038">CcCopyRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh971560">CcCopyReadEx</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff539067">CcFastCopyRead</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 8.  |
| **Target Platform** | Universal |
| **Header** | ntifs.h (include Ntifs.h, FltKernel.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= APC_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff539038">CcCopyRead</a>



<b>CcCopyReadEx</b>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539067">CcFastCopyRead</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539191">CcReadAhead</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539203">CcSetAdditionalCacheAttributes</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539224">CcSetReadAheadGranularity</a>