---
UID: NF:wdm.IoGetAffinityInterrupt
title: IoGetAffinityInterrupt function
author: windows-driver-content
description: For more information, see the WdmlibIoGetAffinityInterrupt function.#define IoGetAffinityInterrupt WdmlibIoGetAffinityInterrupt
old-location: kernel\iogetaffinityinterrupt.htm
old-project: kernel
ms.assetid: aec1ace6-9945-4e7a-b0f6-81591670ecfe
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: IoGetAffinityInterrupt, IoGetAffinityInterrupt routine [Kernel-Mode Driver Architecture], WdmlibIoGetAffinityInterrupt, k104_39247b69-50e1-4162-b26e-81b5358738de.xml, kernel.iogetaffinityinterrupt, wdm/IoGetAffinityInterrupt, wdm/WdmlibIoGetAffinityInterrupt
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
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
req.irql: Any level
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	IoGetAffinityInterrupt
-	WdmlibIoGetAffinityInterrupt
product:
- Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# IoGetAffinityInterrupt function
For more information, see the <a href="https://msdn.microsoft.com/E9E80EB4-C20B-4025-957B-32DC6FAE7F38">WdmlibIoGetAffinityInterrupt</a> function.

<code>#define IoGetAffinityInterrupt WdmlibIoGetAffinityInterrupt</code>

## Syntax

```
NTKERNELAPI NTSTATUS IoGetAffinityInterrupt(
  PKINTERRUPT     InterruptObject,
  PGROUP_AFFINITY GroupAffinity
);
```

## Parameters

`InterruptObject`

For more information, see the <a href="https://msdn.microsoft.com/E9E80EB4-C20B-4025-957B-32DC6FAE7F38">WdmlibIoGetAffinityInterrupt</a> function.

`GroupAffinity`

For more information, see the <a href="https://msdn.microsoft.com/E9E80EB4-C20B-4025-957B-32DC6FAE7F38">WdmlibIoGetAffinityInterrupt</a> function.


## Return Value

For more information, see the <a href="https://msdn.microsoft.com/E9E80EB4-C20B-4025-957B-32DC6FAE7F38">WdmlibIoGetAffinityInterrupt</a> function.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | Any level |

## See Also

<a href="https://msdn.microsoft.com/E9E80EB4-C20B-4025-957B-32DC6FAE7F38">WdmlibIoGetAffinityInterrupt</a>