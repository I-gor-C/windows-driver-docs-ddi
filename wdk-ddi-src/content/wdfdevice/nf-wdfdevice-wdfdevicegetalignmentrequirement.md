---
UID: NF:wdfdevice.WdfDeviceGetAlignmentRequirement
title: WdfDeviceGetAlignmentRequirement function
author: windows-driver-content
description: The WdfDeviceGetAlignmentRequirement method retrieves a device's address alignment requirement for memory transfer operations.
old-location: wdf\wdfdevicegetalignmentrequirement.htm
old-project: wdf
ms.assetid: 531f5e99-0e04-47dd-86bb-c35aa549c63a
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DFDeviceObjectGeneralRef_c7135427-9887-44e5-8380-28ebef4174a9.xml, WdfDeviceGetAlignmentRequirement, WdfDeviceGetAlignmentRequirement method, kmdf.wdfdevicegetalignmentrequirement, wdf.wdfdevicegetalignmentrequirement, wdfdevice/WdfDeviceGetAlignmentRequirement
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: "<= DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Wdf01000.sys
-	Wdf01000.sys.dll
api_name:
-	WdfDeviceGetAlignmentRequirement
product:
- Windows
targetos: Windows
req.typenames: WDF_STATE_NOTIFICATION_TYPE
req.product: Windows 10 or later.
---


# WdfDeviceGetAlignmentRequirement function
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDeviceGetAlignmentRequirement</b> method retrieves a device's address alignment requirement for memory transfer operations.

## Syntax

```
ULONG WdfDeviceGetAlignmentRequirement(
  WDFDEVICE Device
);
```

## Parameters

`Device`

A handle to a framework device object.


## Return Value

<b>WdfDeviceGetAlignmentRequirement</b> returns the device's current alignment requirement. This value is one of the FILE_<i>XXXX</i>_ALIGNMENT constants that are defined in <i>wdm.h</i>.

A bug check occurs if the driver supplies an invalid object handle.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Minimum KMDF version** | 1.0 |
| **Header** | wdfdevice.h (include Wdf.h) |
| **Library** | Wdf01000.sys (see Framework Library Versioning.) |
| **IRQL** | "<= DISPATCH_LEVEL" |
| **DDI compliance rules** | DriverCreate, KmdfIrql, KmdfIrql2 |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546861">WdfDeviceSetAlignmentRequirement</a>