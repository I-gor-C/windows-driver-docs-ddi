---
UID: NF:rxprocs.FsRtlNotifyFullChangeDirectory
title: FsRtlNotifyFullChangeDirectory macro
author: windows-driver-content
description: The FsRtlNotifyFullChangeDirectory routine creates a notify structure for a notification request and adds it to the specified notify list.
old-location: ifsk\fsrtlnotifyfullchangedirectory.htm
old-project: ifsk
ms.assetid: 42e5340e-0be4-49d1-a219-88b7425a41ef
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: FsRtlNotifyFullChangeDirectory, FsRtlNotifyFullChangeDirectory routine [Installable File System Drivers], fsrtlref_551aff27-746f-49a4-b427-fa273249c36e.xml, ifsk.fsrtlnotifyfullchangedirectory, rxprocs/FsRtlNotifyFullChangeDirectory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: rxprocs.h
req.include-header: Ntifs.h
req.target-type: Universal
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
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	FsRtlNotifyFullChangeDirectory
product:
- Windows
targetos: Windows
req.typenames: RX_CONTEXT, *PRX_CONTEXT
req.product: Windows 10 or later.
---


# FsRtlNotifyFullChangeDirectory function
The <b>FsRtlNotifyFullChangeDirectory</b> routine creates a notify structure for a notification request and adds it to the specified notify list.

## Syntax

```
void FsRtlNotifyFullChangeDirectory(
   A1,
   A2,
   A3,
   A4,
   A5,
   A6,
   A7,
   A8,
   A9,
   A10
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


## Return Value

None

## Remarks

<b>FsRtlNotifyFullChangeDirectory</b> is called by a file system that has received a notify change request. This request is received as an IRP with major function code IRP_MJ_DIRECTORY_CONTROL, minor function code IRP_MN_NOTIFY_CHANGE_DIRECTORY. 

If <i>NotifyIrp</i> is <b>NULL</b>, <b>FsRtlNotifyFullChangeDirectory</b> checks whether the notify list contains a pending IRP that refers to this file object and, if so, completes it with STATUS_DELETE_PENDING.

If <i>NotifyIrp</i> is not <b>NULL</b>, <b>FsRtlNotifyFullChangeDirectory</b> does the following:

<ul>
<li>
Checks whether the file object has undergone cleanup. If so, <b>FsRtlNotifyFullChangeDirectory</b> completes the notify IRP with status STATUS_NOTIFY_CLEANUP.

</li>
<li>
If the file object has not undergone cleanup, <b>FsRtlNotifyFullChangeDirectory</b> checks whether the notify list for this volume already contains a notify structure for this change. If so, <b>FsRtlNotifyFullChangeDirectory</b> completes any pending IRPs. If not, <b>FsRtlNotifyFullChangeDirectory</b> marks the notify IRP as pending, creates a notify structure, and inserts it into the list. 

</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | rxprocs.h (include Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff547041">FsRtlNotifyFullReportChange</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548658">IRP_MJ_DIRECTORY_CONTROL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563714">SECURITY_SUBJECT_CONTEXT</a>