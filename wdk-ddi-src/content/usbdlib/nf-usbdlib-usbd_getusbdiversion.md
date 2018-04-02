---
UID: NF:usbdlib.USBD_GetUSBDIVersion
title: USBD_GetUSBDIVersion function
author: windows-driver-content
description: The USBD_GetUSBDIVersion routine returns version information about the host controller driver (HCD) that controls the client's USB device.Note  USBD_IsInterfaceVersionSupported replaces the USBD_GetUSBDIVersion routine
old-location: buses\usbd_getusbdiversion.htm
old-project: usbref
ms.assetid: 47e6da4a-fa81-40ee-9bf5-80526dc0b865
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: USBD_GetUSBDIVersion, USBD_GetUSBDIVersion routine [Buses], buses.usbd_getusbdiversion, usbdlib/USBD_GetUSBDIVersion, usbfunc_567ca75b-8d65-412c-aa28-284a01cff650.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: usbdlib.h
req.include-header: Usbdlib.h
req.target-type: Universal
req.target-min-winverclnt: 
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
req.lib: Usbd.lib
req.dll: 
req.irql: "<=DISPATCH_LEVEL (See Remarks)"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Usbd.lib
-	Usbd.dll
api_name:
-	USBD_GetUSBDIVersion
product:
- Windows
targetos: Windows
req.typenames: USBCAMD_DEVICE_DATA2, *PUSBCAMD_DEVICE_DATA2
req.product: Windows 10 or later.
---


# USBD_GetUSBDIVersion function
The <b>USBD_GetUSBDIVersion</b> routine returns version information about the host controller driver (HCD) that controls the client's USB device.
<div class="alert"><b>Note</b>  <a href="https://msdn.microsoft.com/library/windows/hardware/hh406233">USBD_IsInterfaceVersionSupported</a> replaces the <b>USBD_GetUSBDIVersion</b>  routine</div><div> </div>

## Syntax

```
DECLSPEC_IMPORT VOID USBD_GetUSBDIVersion(
  PUSBD_VERSION_INFORMATION VersionInformation
);
```

## Parameters

`VersionInformation`

Pointer to caller-allocated memory for a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539149">USBD_VERSION_INFORMATION</a> structure that on return from the routine, contains version information about the HCD.


## Return Value

This routine does not return a value.

## Remarks

Callers of this routine can be running at IRQL &lt;= DISPATCH_LEVEL if the memory for <i>VersionInformation</i> is allocated from nonpaged pool. Otherwise, callers must be running at IRQL &lt; DISPATCH_LEVEL.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | usbdlib.h (include Usbdlib.h) |
| **Library** | Usbd.lib |
| **IRQL** | "<=DISPATCH_LEVEL (See Remarks)" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540134">USB device driver programming reference</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh406233">USBD_IsInterfaceVersionSupported</a>