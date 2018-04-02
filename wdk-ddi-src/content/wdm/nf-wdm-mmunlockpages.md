---
UID: NF:wdm.MmUnlockPages
title: MmUnlockPages function
author: windows-driver-content
description: The MmUnlockPages routine unlocks the physical pages that are described by the specified memory descriptor list (MDL).
old-location: kernel\mmunlockpages.htm
old-project: kernel
ms.assetid: 506f5fef-11fa-4d65-a180-c613cd8a8e1e
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: MmUnlockPages, MmUnlockPages routine [Kernel-Mode Driver Architecture], k106_b8d8a984-9e0e-4322-bce1-2dd79e8d3a10.xml, kernel.mmunlockpages, wdm/MmUnlockPages
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
req.irql: "<=DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	MmUnlockPages
product:
- Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# MmUnlockPages function
The <b>MmUnlockPages</b> routine unlocks the physical pages that are described by the specified memory descriptor list (MDL).

## Syntax

```
NTKERNELAPI VOID MmUnlockPages(
  PMDL MemoryDescriptorList
);
```

## Parameters

`MemoryDescriptorList`

A pointer to an MDL.


## Return Value

None

## Remarks

The memory described by the specified MDL must have been locked previously by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff554664">MmProbeAndLockPages</a>. If the specified MDL is mapped to system address space, <b>MmUnlockPages</b> releases this mapping before it unlocks the pages.

For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565421">Using MDLs</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<=DISPATCH_LEVEL" |
| **DDI compliance rules** | HwStorPortProhibitedDDIs |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff554664">MmProbeAndLockPages</a>