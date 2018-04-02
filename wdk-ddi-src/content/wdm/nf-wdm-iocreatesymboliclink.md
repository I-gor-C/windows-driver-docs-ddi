---
UID: NF:wdm.IoCreateSymbolicLink
title: IoCreateSymbolicLink function
author: windows-driver-content
description: The IoCreateSymbolicLink routine sets up a symbolic link between a device object name and a user-visible name for the device.
old-location: kernel\iocreatesymboliclink.htm
old-project: kernel
ms.assetid: be080007-f88e-4cea-b15d-58dc4ac2cb66
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: IoCreateSymbolicLink, IoCreateSymbolicLink routine [Kernel-Mode Driver Architecture], k104_8311eaf7-a12f-470d-b81f-83a12697ddbe.xml, kernel.iocreatesymboliclink, wdm/IoCreateSymbolicLink
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
req.ddi-compliance: IrqlIoPassive3, PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	IoCreateSymbolicLink
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# IoCreateSymbolicLink function
The <b>IoCreateSymbolicLink</b> routine sets up a symbolic link between a device object name and a user-visible name for the device.

## Syntax

```
NTKERNELAPI NTSTATUS IoCreateSymbolicLink(
  PUNICODE_STRING SymbolicLinkName,
  PUNICODE_STRING DeviceName
);
```

## Parameters

`SymbolicLinkName`

Pointer to a buffered Unicode string that is the user-visible name.

`DeviceName`

Pointer to a buffered Unicode string that is the name of the driver-created device object.


## Return Value

<b>IoCreateSymbolicLink</b> returns STATUS_SUCCESS if the symbolic link object was created.

## Remarks

WDM drivers do not name device objects and therefore should not use this routine. Instead, a WDM driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549506">IoRegisterDeviceInterface</a> to set up a symbolic link. 

For more information about when to use <b>IoCreateSymbolicLink</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff556420">Named Device Objects</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** | IrqlIoPassive3, PowerIrpDDis, HwStorPortProhibitedDDIs |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff548282">IoAssignArcName</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549050">IoCreateUnprotectedSymbolicLink</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549085">IoDeleteSymbolicLink</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549506">IoRegisterDeviceInterface</a>