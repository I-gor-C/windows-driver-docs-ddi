---
UID: NF:wdm.PsTerminateSystemThread
title: PsTerminateSystemThread function
author: windows-driver-content
description: The PsTerminateSystemThread routine terminates the current system thread.
old-location: kernel\psterminatesystemthread.htm
old-project: kernel
ms.assetid: 04f9f699-0ca1-4b22-b66f-04fcf53935c4
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: PsTerminateSystemThread, PsTerminateSystemThread routine [Kernel-Mode Driver Architecture], k108_a8e19a60-578c-42a6-b77a-cf6c4098c815.xml, kernel.psterminatesystemthread, wdm/PsTerminateSystemThread
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: IrqlPsPassive, PowerIrpDDis, HwStorPortProhibitedDDIs
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
-	PsTerminateSystemThread
product:
- Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# PsTerminateSystemThread function
The <b>PsTerminateSystemThread</b> routine terminates the current system thread.

## Syntax

```
NTKERNELAPI NTSTATUS PsTerminateSystemThread(
  NTSTATUS ExitStatus
);
```

## Parameters

`ExitStatus`

Specifies the status of the terminating system thread.


## Return Value

<b>PsTerminateSystemThread</b> does not return if it successfully terminates the calling thread. If the routine cannot terminate the thread (for example, if the thread is not a system thread), the routine returns an error NTSTATUS value.

## Remarks

A system thread calls <b>PsTerminateSystemThread</b> to terminate itself. A driver that creates its own threads must ensure that each such thread terminates. The driver must not terminate any threads that the system or other drivers created.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** | IrqlPsPassive, PowerIrpDDis, HwStorPortProhibitedDDIs |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff559932">PsCreateSystemThread</a>