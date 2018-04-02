---
UID: NF:wdm.KeClearEvent
title: KeClearEvent function
author: windows-driver-content
description: The KeClearEvent routine sets an event to a not-signaled state.
old-location: kernel\keclearevent.htm
old-project: kernel
ms.assetid: ded54c88-3da0-42ec-88be-865d3cb87651
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: KeClearEvent, KeClearEvent routine [Kernel-Mode Driver Architecture], k105_1ea5c68a-0b59-48ec-911b-058b6a3e586b.xml, kernel.keclearevent, wdm/KeClearEvent
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
req.ddi-compliance: IoBuildDeviceIoControlSetEvent, IrqlKeDispatchLte, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: "<= DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	KeClearEvent
product:
- Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# KeClearEvent function
The <b>KeClearEvent</b> routine sets an event to a not-signaled state.

## Syntax

```
NTKERNELAPI VOID KeClearEvent(
  PRKEVENT Event
);
```

## Parameters

`Event`

Pointer to an initialized dispatcher object of type event for which the caller supplies the storage.


## Return Value

None

## Remarks

<i>Event</i> is set to a not-signaled state, meaning its value is set to zero.

For better performance, use <b>KeClearEvent</b> unless the caller uses the value returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff553176">KeResetEvent</a> to determine what to do next.

For more information about event objects, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544323">Event Objects</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= DISPATCH_LEVEL" |
| **DDI compliance rules** | IoBuildDeviceIoControlSetEvent, IrqlKeDispatchLte, HwStorPortProhibitedDDIs |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552137">KeInitializeEvent</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553089">KeReadStateEvent</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553176">KeResetEvent</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553253">KeSetEvent</a>