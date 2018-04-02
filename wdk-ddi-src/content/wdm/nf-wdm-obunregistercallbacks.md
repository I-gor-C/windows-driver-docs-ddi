---
UID: NF:wdm.ObUnRegisterCallbacks
title: ObUnRegisterCallbacks function
author: windows-driver-content
description: The ObUnRegisterCallbacks routine unregisters a set of callback routines that were registered with the ObRegisterCallbacks routine.
old-location: kernel\obunregistercallbacks.htm
old-project: kernel
ms.assetid: 01121323-da0c-4ae9-b0c0-f6302583237c
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: ObUnRegisterCallbacks, ObUnRegisterCallbacks routine [Kernel-Mode Driver Architecture], k107_f0c1fdd0-3dcc-466c-a7a1-fab0b38e4e88.xml, kernel.obunregistercallbacks, wdm/ObUnRegisterCallbacks
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista with Service Pack 1 (SP1), Windows Server 2008, and later versions of the Windows operating system.
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
-	ObUnRegisterCallbacks
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# ObUnRegisterCallbacks function
The <b>ObUnRegisterCallbacks</b> routine unregisters a set of callback routines that were registered with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558692">ObRegisterCallbacks</a> routine.

## Syntax

```
NTKERNELAPI VOID ObUnRegisterCallbacks(
  PVOID RegistrationHandle
);
```

## Parameters

`RegistrationHandle`

A value that identifies the set of callback routines to unregister. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff558692">ObRegisterCallbacks</a> routine provides this value when it originally registered the callback routines.


## Return Value

None

## Remarks

A driver that calls the <b>ObRegisterCallbacks</b> routine must call the <b>ObUnRegisterCallbacks</b> routine before the driver is unloaded.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista with Service Pack 1 (SP1), Windows Server 2008, and later versions of the Windows operating system.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= APC_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff558692">ObRegisterCallbacks</a>