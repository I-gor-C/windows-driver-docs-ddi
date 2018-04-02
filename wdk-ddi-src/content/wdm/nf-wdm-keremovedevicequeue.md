---
UID: NF:wdm.KeRemoveDeviceQueue
title: KeRemoveDeviceQueue function
author: windows-driver-content
description: The KeRemoveDeviceQueue routine removes an entry from the head of a specified device queue.
old-location: kernel\keremovedevicequeue.htm
old-project: kernel
ms.assetid: 9cad7d89-bcaa-47d6-b3e5-51653cbef318
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: KeRemoveDeviceQueue, KeRemoveDeviceQueue routine [Kernel-Mode Driver Architecture], k105_3e26b41e-7e9c-4fc9-8496-f107f3450dd7.xml, kernel.keremovedevicequeue, wdm/KeRemoveDeviceQueue
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
req.ddi-compliance: IrqlDispatch, HwStorPortProhibitedDDIs, IrqlDispatch(storport)
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
-	KeRemoveDeviceQueue
product:
- Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# KeRemoveDeviceQueue function
The <b>KeRemoveDeviceQueue</b> routine removes an entry from the head of a specified device queue.

## Syntax

```
NTKERNELAPI PKDEVICE_QUEUE_ENTRY KeRemoveDeviceQueue(
  PKDEVICE_QUEUE DeviceQueue
);
```

## Parameters

`DeviceQueue`

Pointer to an initialized device queue object for which the caller provides the storage.


## Return Value

If the device queue is empty but is set to a busy state, <b>KeRemoveDeviceQueue</b> returns <b>NULL</b>.

## Remarks

The specified device queue spin lock is acquired and the state of the device queue is checked. If the device queue is set to a busy state and an IRP is queued, this routine dequeues the entry and returns a pointer to the IRP. A call to <b>KeRemoveDeviceQueue</b> when the device queue object is set to a busy state but no IRPs are queued causes a state change to not-busy. The specified device queue's spin lock is released.

It is an error to call <b>KeRemoveDeviceQueue</b> when the device queue object is set to a not-busy state.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | DISPATCH_LEVEL |
| **DDI compliance rules** | IrqlDispatch, HwStorPortProhibitedDDIs, IrqlDispatch(storport) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552126">KeInitializeDeviceQueue</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552178">KeInsertByKeyDeviceQueue</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552180">KeInsertDeviceQueue</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553152">KeRemoveByKeyDeviceQueue</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553163">KeRemoveEntryDeviceQueue</a>