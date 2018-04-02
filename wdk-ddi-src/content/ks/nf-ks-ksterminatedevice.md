---
UID: NF:ks.KsTerminateDevice
title: KsTerminateDevice function
author: windows-driver-content
description: The KsTerminateDevice function removes an AVStream device.
old-location: stream\ksterminatedevice.htm
old-project: stream
ms.assetid: 3d6ad381-0bd9-47d8-a4dd-e434b62bf5a1
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: KsTerminateDevice, KsTerminateDevice function [Streaming Media Devices], avfunc_42f55ca4-ed73-4ea2-9f33-462d9d13e3e3.xml, ks/KsTerminateDevice, stream.ksterminatedevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
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
req.lib: Ks.lib
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Ks.lib
-	Ks.dll
api_name:
-	KsTerminateDevice
product: Windows
targetos: Windows
req.typenames: 
---


# KsTerminateDevice function
The<b> KsTerminateDevice </b>function removes an AVStream device.

## Syntax

```
void KsTerminateDevice(
  PDEVICE_OBJECT DeviceObject
);
```

## Parameters

`DeviceObject`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure corresponding to the device for which to remove AVStream support.


## Return Value

None

## Remarks

Normally, AVStream calls <b>KsTerminateDevice</b> upon receipt of a PnP remove device IRP (IRP_MN_REMOVE_DEVICE). Most minidrivers do not call this function directly; however, it can be used to remove AVStream support for the device given in <i>DeviceObject</i>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.  |
| **Target Platform** | Universal |
| **Header** | ks.h (include Ks.h) |
| **Library** | Ks.lib |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560927">KsAddDevice</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561647">KsCreateDevice</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562682">KsInitializeDevice</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562683">KsInitializeDriver</a>