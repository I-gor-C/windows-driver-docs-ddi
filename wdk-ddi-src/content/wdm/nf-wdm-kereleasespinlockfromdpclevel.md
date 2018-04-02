---
UID: NF:wdm.KeReleaseSpinLockFromDpcLevel
title: KeReleaseSpinLockFromDpcLevel macro
author: windows-driver-content
description: The KeReleaseSpinLockFromDpcLevel routine releases an executive spin lock without changing the IRQL.
old-location: kernel\kereleasespinlockfromdpclevel.htm
old-project: kernel
ms.assetid: 5f7a92ee-ebaf-442f-a197-2fb58dd65a25
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: KeReleaseSpinLockFromDpcLevel, KeReleaseSpinLockFromDpcLevel routine [Kernel-Mode Driver Architecture], KefReleaseSpinLockFromDpcLevel, k105_ed15a49d-6903-4f9f-914c-668242701b1e.xml, kernel.kereleasespinlockfromdpclevel, wdm/KeReleaseSpinLockFromDpcLevel, wdm/KefReleaseSpinLockFromDpcLevel
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: HwStorPortProhibitedDDIs, IrqlDispatch, SpinLockSafe
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: DISPATCH_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	KeReleaseSpinLockFromDpcLevel
-	KefReleaseSpinLockFromDpcLevel
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# KeReleaseSpinLockFromDpcLevel function
The <b>KeReleaseSpinLockFromDpcLevel</b> routine releases an executive spin lock without changing the IRQL.

## Syntax

```
void KeReleaseSpinLockFromDpcLevel(
   a
);
```

## Parameters

`a`

TBD


## Return Value

None

## Remarks

Drivers call <b>KeReleaseSpinLockFromDpcLevel</b> to release a spin lock acquired by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff551921">KeAcquireSpinLockAtDpcLevel</a>.

It is an error to call <b>KeReleaseSpinLockFromDpcLevel</b> if the specified spin lock was acquired by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff551917">KeAcquireSpinLock</a> because the caller's original IRQL is not restored, which can cause deadlocks or fatal page faults.

For more information about spin locks, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563830">Spin Locks</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | DISPATCH_LEVEL |
| **DDI compliance rules** | HwStorPortProhibitedDDIs, IrqlDispatch, SpinLockSafe |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff551917">KeAcquireSpinLock</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff551921">KeAcquireSpinLockAtDpcLevel</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553145">KeReleaseSpinLock</a>