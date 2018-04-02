---
UID: NF:ntifs.IoGetAttachedDeviceReference
title: IoGetAttachedDeviceReference function
author: windows-driver-content
description: The IoGetAttachedDeviceReference routine returns a pointer to the highest level device object in a driver stack and increments the reference count on that object.
old-location: kernel\iogetattacheddevicereference.htm
old-project: kernel
ms.assetid: 540a4e5c-8d7b-4ba8-a9a6-6e13d9b85f23
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: IoGetAttachedDeviceReference, IoGetAttachedDeviceReference routine [Kernel-Mode Driver Architecture], k104_f7fa8878-306a-4de2-b418-8102754306f7.xml, kernel.iogetattacheddevicereference, wdm/IoGetAttachedDeviceReference
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
req.ddi-compliance: DanglingDeviceObjectReference, HwStorPortProhibitedDDIs
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
-	IoGetAttachedDeviceReference
product: Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# IoGetAttachedDeviceReference function
The <b>IoGetAttachedDeviceReference</b> routine returns a pointer to the highest level device object in a driver stack and increments the reference count on that object.

## Syntax

```
NTKERNELAPI PDEVICE_OBJECT IoGetAttachedDeviceReference(
  PDEVICE_OBJECT DeviceObject
);
```

## Parameters

`DeviceObject`

Pointer to the device object for which the topmost attached device object is retrieved.


## Return Value

<b>IoGetAttachedDeviceReference</b> returns a pointer to the highest level device object in a stack of attached device objects after incrementing the reference count on the object.

## Remarks

If the device object at <i>DeviceObject</i> has no device objects attached to it, <i>DeviceObject</i> and the returned pointer are equal.

Device driver writers must ensure that when they have completed all operations that required them to make this call, that they call <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a> with the device object pointer returned by this routine. Failure to do so will prevent the system from freeing or deleting the device object because of an outstanding reference count.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | ntifs.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= DISPATCH_LEVEL" |
| **DDI compliance rules** | DanglingDeviceObjectReference, HwStorPortProhibitedDDIs |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a>