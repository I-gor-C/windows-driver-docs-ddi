---
UID: NF:wdm.KeLeaveCriticalRegion
title: KeLeaveCriticalRegion function
author: windows-driver-content
description: The KeLeaveCriticalRegion routine reenables the delivery of normal kernel-mode APCs that were disabled by a preceding call to KeEnterCriticalRegion.
old-location: kernel\keleavecriticalregion.htm
old-project: kernel
ms.assetid: d3e90c3b-5ead-40d1-9143-a2b1fc8c255d
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: KeLeaveCriticalRegion, KeLeaveCriticalRegion routine [Kernel-Mode Driver Architecture], k105_f9344044-a57f-4ee4-800c-a03edcc27196.xml, kernel.keleavecriticalregion, wdm/KeLeaveCriticalRegion
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
req.ddi-compliance: CriticalRegions, IrqlKeApcLte2, WithinCriticalRegion, HwStorPortProhibitedDDIs, WithinCriticalRegion(storport)
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
-	KeLeaveCriticalRegion
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# KeLeaveCriticalRegion function
The <b>KeLeaveCriticalRegion</b> routine reenables the delivery of normal kernel-mode APCs that were disabled by a preceding call to <b>KeEnterCriticalRegion</b>.

## Syntax

```
NTKERNELAPI VOID KeLeaveCriticalRegion(

);
```

## Parameters

This function has no parameters.

## Return Value

None

## Remarks

Highest-level drivers can call this routine while running in the context of the thread that requested the current I/O operation.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= APC_LEVEL" |
| **DDI compliance rules** | CriticalRegions, IrqlKeApcLte2, WithinCriticalRegion, HwStorPortProhibitedDDIs, WithinCriticalRegion(storport) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff551938">KeAreApcsDisabled</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552021">KeEnterCriticalRegion</a>