---
UID: NF:wdm.KeReadStateSemaphore
title: KeReadStateSemaphore function
author: windows-driver-content
description: The KeReadStateSemaphore routine returns the current state, signaled or not-signaled, of the specified semaphore object.
old-location: kernel\kereadstatesemaphore.htm
old-project: kernel
ms.assetid: e88c89fb-c308-4c6d-a67d-c8f98d539a43
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: KeReadStateSemaphore, KeReadStateSemaphore routine [Kernel-Mode Driver Architecture], k105_cc608a62-f747-4d8c-a4f8-b6df51a4d5dd.xml, kernel.kereadstatesemaphore, wdm/KeReadStateSemaphore
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
req.ddi-compliance: HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	KeReadStateSemaphore
product:
- Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# KeReadStateSemaphore function
The <b>KeReadStateSemaphore</b> routine returns the current state, signaled or not-signaled, of the specified semaphore object.

## Syntax

```
NTKERNELAPI LONG KeReadStateSemaphore(
  PRKSEMAPHORE Semaphore
);
```

## Parameters

`Semaphore`

Pointer to an initialized semaphore object for which the caller provides the storage.


## Return Value

If the return value is zero, the semaphore object is set to a not-signaled state.

## Remarks

This routine provides an efficient way to poll the signal state of a semaphore. <b>KeReadStateSemaphore</b> reads the state of the semaphore without synchronizing its access to the semaphore. Do not assume that accesses of a semaphore state by <b>KeReadStateSemaphore</b> are mutually exclusive of accesses by routines, such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff553143">KeReleaseSemaphore</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a>, that do synchronize their access to the semaphore state.

For more information about semaphore objects, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563719">Semaphore Objects</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | Any level |
| **DDI compliance rules** | HwStorPortProhibitedDDIs |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552150">KeInitializeSemaphore</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553143">KeReleaseSemaphore</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a>