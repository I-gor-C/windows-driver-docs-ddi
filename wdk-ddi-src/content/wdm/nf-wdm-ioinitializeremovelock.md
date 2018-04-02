---
UID: NF:wdm.IoInitializeRemoveLock
title: IoInitializeRemoveLock macro
author: windows-driver-content
description: The IoInitializeRemoveLock routine initializes a remove lock for a device object.
old-location: kernel\ioinitializeremovelock.htm
old-project: kernel
ms.assetid: d85bab78-0e9e-4e71-a09b-40954df81c87
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: IoInitializeRemoveLock, IoInitializeRemoveLock routine [Kernel-Mode Driver Architecture], k104_b9b844b1-4bb4-4a52-8274-c5a3441f6267.xml, kernel.ioinitializeremovelock, wdm/IoInitializeRemoveLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
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
-	IoInitializeRemoveLock
product:
- Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# IoInitializeRemoveLock function
The <b>IoInitializeRemoveLock</b> routine initializes a remove lock for a device object.

## Syntax

```
void IoInitializeRemoveLock(
   Lock,
   Tag,
   Maxmin,
   HighWater
);
```

## Parameters

`Lock`

Pointer to a caller-supplied <b>IO_REMOVE_LOCK</b> structure that this routine initializes with information about the lock, including a counter and a synchronization event. A driver writer must allocate this structure as part of the device object's device extension.

`Tag`

TBD

`Maxmin`

TBD

`HighWater`

TBD


## Return Value

None

## Remarks

A driver can use a remove lock to track outstanding I/O operations on a device and to determine when the driver can delete its device object in response to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551738">IRP_MN_REMOVE_DEVICE</a> request.

Before calling <b>IoInitializeRemoveLock</b>, a driver should allocate an <b>IO_REMOVE_LOCK</b> structure in its <a href="https://msdn.microsoft.com/9ea59994-1112-4ae5-96a8-fa0670694b53">device extension</a>. A driver typically calls <b>IoInitializeRemoveLock</b> in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routine, when the driver initializes the rest of the device extension for a device object.

After the <b>IoReleaseRemoveLockAndWait</b> routine returns, the driver should consider the device to be in a state in which it is ready to be removed and cannot perform I/O operations. Therefore, the driver must not call <b>IoInitializeRemoveLock</b> to re-initialize the remove lock. Violation of this rule while the driver is being verified by <a href="https://msdn.microsoft.com/library/windows/hardware/ff557262">Driver Verifier</a> will result in a bug check.

Because the driver stores the <b>IO_REMOVE_LOCK</b> structure in the device extension of a device object, the remove lock is deleted when the driver deletes the device extension as part of processing an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551738">IRP_MN_REMOVE_DEVICE</a> request.

For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565504">Using Remove Locks</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Desktop |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff548204">IoAcquireRemoveLock</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549324">IoInitializeRemoveLock</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549560">IoReleaseRemoveLock</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549567">IoReleaseRemoveLockAndWait</a>