---
UID: NF:usbdlib.USBD_GetPdoRegistryParameter
title: USBD_GetPdoRegistryParameter function
author: windows-driver-content
description: The USBD_GetPdoRegistryParameter routine retrieves the value from the specified key in the USB device's hardware registry.
old-location: buses\usbd_getpdoregistryparameter.htm
old-project: usbref
ms.assetid: f61be32a-2537-4b7f-8f22-4149b00a15a4
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: USBD_GetPdoRegistryParameter, USBD_GetPdoRegistryParameter routine [Buses], buses.usbd_getpdoregistryparameter, usbdlib/USBD_GetPdoRegistryParameter, usbfunc_b85b350e-68ad-4256-b4df-f61ea0367b62.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: usbdlib.h
req.include-header: 
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	usbd.lib
-	usbd.dll
api_name:
-	USBD_GetPdoRegistryParameter
product:
- Windows
targetos: Windows
req.typenames: USBCAMD_DEVICE_DATA2, *PUSBCAMD_DEVICE_DATA2
req.product: Windows 10 or later.
---


# USBD_GetPdoRegistryParameter function
The <b>USBD_GetPdoRegistryParameter</b> routine retrieves the value from the  specified key in the USB device's hardware registry.

## Syntax

```
NTSTATUS USBD_GetPdoRegistryParameter(
  PDEVICE_OBJECT PhysicalDeviceObject,
  PVOID          ParameterLength,
  ULONG          KeyName,
  PWSTR          KeyNameLength,
  ULONG          Parameter
);
```

## Parameters

`PhysicalDeviceObject`

Specifies the device object for the USB device.

`ParameterLength`

Size, in bytes, of the buffer that is pointed to by <i>Parameter</i>.

`KeyName`

Pointer to a string containing the name of the registry key.

`KeyNameLength`

Size, in bytes, of the buffer that is pointed to by <i>KeyName</i>.

`Parameter`

Pointer to a caller-allocated buffer that receives the registry value.


## Return Value

The <b>USBD_GetPdoRegistryParameter</b> returns STATUS_SUCCESS when the operation succeeds or an appropriate error status when the operation fails.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | usbdlib.h |
| **Library** | Usbd.lib |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540134">USB device driver programming reference</a>