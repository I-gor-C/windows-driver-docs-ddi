---
UID: NF:rxprocs.FsRtlCheckOplock
title: FsRtlCheckOplock macro
author: windows-driver-content
description: The FsRtlCheckOplock routine synchronizes the IRP for a file I/O operation with the file's current opportunistic lock (oplock) state.
old-location: ifsk\fsrtlcheckoplock.htm
old-project: ifsk
ms.assetid: e1430ef2-fb94-4f0d-bdc8-59b423fe9c8c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: FsRtlCheckOplock, FsRtlCheckOplock routine [Installable File System Drivers], fsrtlref_c11dbb80-c7a8-437d-bb6b-661edcf2f24a.xml, ifsk.fsrtlcheckoplock, rxprocs/FsRtlCheckOplock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: rxprocs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available in Microsoft Windows 2000 and later versions of Windows operating systems.
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
-	FsRtlCheckOplock
product: Windows
targetos: Windows
req.typenames: RX_CONTEXT, *PRX_CONTEXT
req.product: Windows 10 or later.
---


# FsRtlCheckOplock function
The <b>FsRtlCheckOplock</b> routine synchronizes the IRP for a file I/O operation with the file's current opportunistic lock (oplock) state.

## Syntax

```
void FsRtlCheckOplock(
   A1,
   A2,
   A3,
   A4,
   A5
);
```

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


## Return Value

None

## Remarks

<b>FsRtlCheckOplock</b> synchronizes the IRP for an I/O operation with the current opportunistic lock state of a file according to the following conditions: 

<ul>
<li>
If the I/O operation will cause the opportunistic lock to break, the opportunistic lock break is initiated. 

</li>
<li>
If the I/O operation cannot continue until the opportunistic lock break is complete, <b>FsRtlCheckOplock</b> returns STATUS_PENDING and calls the callback routine that the <i>PostIrpRoutine</i> parameter points to. 

</li>
</ul>
If a file system or filter driver uses opportunistic locks, it must call <b>FsRtlCheckOplock</b> from any dispatch routines for I/O operations that can cause opportunistic lock breaks. This rule applies to the following types of I/O operations, because these operations can cause opportunistic lock breaks: 

IRP_MJ_CLEANUP

IRP_MJ_CREATE

IRP_MJ_FILE_SYSTEM_CONTROL

IRP_MJ_FLUSH_BUFFERS

IRP_MJ_LOCK_CONTROL

IRP_MJ_READ

IRP_MJ_SET_INFORMATION

IRP_MJ_WRITE

For detailed information about opportunistic locks, see the Microsoft Windows SDK documentation. 

Minifilters should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541844">FltCheckOplock</a> instead of <b>FsRtlCheckOplock</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | This routine is available in Microsoft Windows 2000 and later versions of Windows operating systems.  |
| **Target Platform** | Universal |
| **Header** | rxprocs.h (include FltKernel.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= APC_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff545462">FSCTL_OPBATCH_ACK_CLOSE_PENDING</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545468">FSCTL_OPLOCK_BREAK_ACKNOWLEDGE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545476">FSCTL_OPLOCK_BREAK_ACK_NO_2</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545485">FSCTL_OPLOCK_BREAK_NOTIFY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545510">FSCTL_REQUEST_BATCH_OPLOCK</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545518">FSCTL_REQUEST_FILTER_OPLOCK</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545538">FSCTL_REQUEST_OPLOCK_LEVEL_1</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545546">FSCTL_REQUEST_OPLOCK_LEVEL_2</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541844">FltCheckOplock</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545825">FsRtlCurrentBatchOplock</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546150">FsRtlInitializeOplock</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547112">FsRtlOplockFsctrl</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547120">FsRtlOplockIsFastIoPossible</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547328">FsRtlUninitializeOplock</a>