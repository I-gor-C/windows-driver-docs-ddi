---
UID: NF:wdfdevice.WdfDeviceWriteToHardware
title: WdfDeviceWriteToHardware function
author: windows-driver-content
description: The WdfDeviceWriteToHardware method is used internally by the framework. Do not use.
old-location: wdf\wdfdevicewritetohardware.htm
old-project: wdf
ms.assetid: D79F1D98-E326-4401-86B8-2C3D071DF27C
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFN_WDFDEVICEWRITETOHARDWARE, WdfDeviceWriteToHardware, WdfDeviceWriteToHardware method, wdf.wdfdevicewritetohardware, wdfdevice/WdfDeviceWriteToHardware, wdfhwaccess/WdfDeviceWriteToHardware
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 2.0
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Wdf01000.sys
-	Wdf01000.sys.dll
api_name:
-	WdfDeviceWriteToHardware
product: Windows
targetos: Windows
req.typenames: WDF_STATE_NOTIFICATION_TYPE
req.product: Windows 10 or later.
---


# WdfDeviceWriteToHardware function
The <b>WdfDeviceWriteToHardware</b> method is used internally by the framework. Do not use.

Instead, use the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265662">WDF Register/Port Access Functions</a>.

## Syntax

```
void WdfDeviceWriteToHardware(
  WDFDEVICE                       Device,
  WDF_DEVICE_HWACCESS_TARGET_TYPE Type,
  WDF_DEVICE_HWACCESS_TARGET_SIZE Size,
  PVOID                           TargetAddress,
  SIZE_T                          Value,
  PVOID                           Buffer,
  ULONG                           Count
);
```

## Parameters

`Device`



`Type`



`Size`



`TargetAddress`



`Value`



`Buffer`



`Count`




## Return Value

This method does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Minimum KMDF version** | 1.11 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfdevice.h (include Wdf.h) |
| **Library** | Wdf01000.sys (see Framework Library Versioning.) |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/55FBE72C-E74E-4116-9602-6D491592350F">WriteToHardware</a>