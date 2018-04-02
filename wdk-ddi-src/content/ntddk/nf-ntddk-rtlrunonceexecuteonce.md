---
UID: NF:ntddk.RtlRunOnceExecuteOnce
title: RtlRunOnceExecuteOnce function
author: windows-driver-content
description: The RtlRunOnceExecuteOnce performs a one-time initialization.
old-location: kernel\rtlrunonceexecuteonce.htm
old-project: kernel
ms.assetid: 2769eb2c-33e2-4e3f-a1bf-1ebc9213b224
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: RtlRunOnceExecuteOnce, RtlRunOnceExecuteOnce function [Kernel-Mode Driver Architecture], k109_c1729bff-038f-4714-b422-1b97dd5a9c19.xml, kernel.rtlrunonceexecuteonce, ntddk/RtlRunOnceExecuteOnce
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
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
req.irql: "<= APC_LEVEL (See Remarks section.)"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	RtlRunOnceExecuteOnce
product: Windows
targetos: Windows
req.typenames: WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT
---


# RtlRunOnceExecuteOnce function
The <b>RtlRunOnceExecuteOnce</b> performs a one-time initialization.

## Syntax

```
_Maybe_raises_SEH_exception_ NTSYSAPI NTSTATUS RtlRunOnceExecuteOnce(
  PRTL_RUN_ONCE         RunOnce,
  PRTL_RUN_ONCE_INIT_FN InitFn,
  PVOID                 Context,
  PVOID                 *Parameter
);
```

## Parameters

`RunOnce`

A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563626">RTL_RUN_ONCE</a> one-time initialization structure.

`InitFn`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563635">RunOnceInitialization</a> routine.

`Context`

A pointer to a PVOID variable that receives the initialized data.

`Parameter`

The value to pass as the <i>Parameter</i> parameter to the <i>RunOnceInitialization</i> routine.


## Return Value

<b>RtlRunOnceExecuteOnce</b> returns STATUS_SUCCESS if the operation succeeds, or the appropriate NTSTATUS error code if the operation fails.

## Remarks

For the first call to <b>RtlRunOnceExecuteOnce</b> for a particular <a href="https://msdn.microsoft.com/library/windows/hardware/ff563626">RTL_RUN_ONCE</a> structure, <b>RtlRunOnceExecuteOnce</b> calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563635">RunOnceInitialization</a> routine to initialize the data. Every subsequent call to <b>RtlRunOnceExecuteOnce</b> for that structure supplies the same initialized data. The <i>RunOnceInitialization</i> routine will not be called twice for the same <b>RTL_RUN_ONCE</b> structure.

<b>RtlRunOnceExecuteOnce</b> runs with normal kernel APCs disabled. The routine should not be called within a special kernel APC unless all calls occur at APC_LEVEL.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows Vista.  |
| **Target Platform** | Universal |
| **Header** | ntddk.h (include Ntddk.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= APC_LEVEL (See Remarks section.)" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff563626">RTL_RUN_ONCE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562759">RtlRunOnceBeginInitialize</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562763">RtlRunOnceComplete</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562767">RtlRunOnceInitialize</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563635">RunOnceInitialization</a>