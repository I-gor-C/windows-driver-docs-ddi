---
UID: NF:ntifs.PoUnregisterSystemState
title: PoUnregisterSystemState function
author: windows-driver-content
description: The PoUnregisterSystemState routine cancels a system state registration created by PoRegisterSystemState.
old-location: kernel\pounregistersystemstate.htm
old-project: kernel
ms.assetid: 5d82342e-c800-44ac-8618-468355d14dd0
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: PoUnregisterSystemState, PoUnregisterSystemState routine [Kernel-Mode Driver Architecture], kernel.pounregistersystemstate, portn_b6118bd0-5fe1-4e75-8c17-e81d1f26814c.xml, wdm/PoUnregisterSystemState
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
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
req.irql: "<=APC_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	PoUnregisterSystemState
product: Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# PoUnregisterSystemState function
The <b>PoUnregisterSystemState</b> routine cancels a system state registration created by <a href="https://msdn.microsoft.com/library/windows/hardware/ff559731">PoRegisterSystemState</a>.

## Syntax

```
NTKERNELAPI VOID PoUnregisterSystemState(
  PVOID StateHandle
);
```

## Parameters

`StateHandle`

A pointer to a handle previously returned by <b>PoRegisterSystemState</b>.


## Return Value

None

## Remarks

This routine cancels a system busy state registration established by <b>PoRegisterSystemState</b> and frees the associated <i>StateHandle</i>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | ntifs.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<=APC_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff559731">PoRegisterSystemState</a>