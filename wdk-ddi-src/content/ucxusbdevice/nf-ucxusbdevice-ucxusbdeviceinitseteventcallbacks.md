---
UID: NF:ucxusbdevice.UcxUsbDeviceInitSetEventCallbacks
title: UcxUsbDeviceInitSetEventCallbacks function
author: windows-driver-content
description: Initializes a UCXUSBDEVICE_INIT structure with client driver's event callback functions.
old-location: buses\_ucxusbdeviceinitseteventcallbacks.htm
old-project: usbref
ms.assetid: 913F96FD-9C51-4A45-86A9-8830E1A395EE
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: UcxUsbDeviceInitSetEventCallbacks, UcxUsbDeviceInitSetEventCallbacks method [Buses], buses._ucxusbdeviceinitseteventcallbacks
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucxusbdevice.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	ucxusbdevice.h
api_name:
-	UcxUsbDeviceInitSetEventCallbacks
product: Windows
targetos: Windows
req.typenames: UCX_USBDEVICE_CHARACTERISTIC_TYPE
req.product: Windows 10 or later.
---


# UcxUsbDeviceInitSetEventCallbacks function
Initializes a <b>UCXUSBDEVICE_INIT</b> structure with client driver's event callback functions.

## Syntax

```
void UcxUsbDeviceInitSetEventCallbacks(
  PUCXUSBDEVICE_INIT             UsbDeviceInit,
  PUCX_USBDEVICE_EVENT_CALLBACKS EventCallbacks
);
```

## Parameters

`UsbDeviceInit`

A pointer to a <b>UCXUSBDEVICE_INIT</b> structure that UCX passes when it invokes client driver's <a href="https://msdn.microsoft.com/library/windows/hardware/mt187823">EVT_UCX_CONTROLLER_USBDEVICE_ADD</a> 		event callback function.

`EventCallbacks`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/mt188067">UCX_USBDEVICE_EVENT_CALLBACKS</a> structure that contains function pointer to client driver's event callback functions. The  the client driver initializes the structure  by calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt188068">UCX_USBDEVICE_EVENT_CALLBACKS_INIT</a>.


## Return Value

This method does not return a value.

## Remarks

An initialized <b>UCXUSBDEVICE_INIT</b> structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188052">UcxUsbDeviceCreate</a> method to create a USB device and register the client driver's event callback functions. 

For a code example, see <a href="https://msdn.microsoft.com/library/windows/hardware/mt187823">EVT_UCX_CONTROLLER_USBDEVICE_ADD</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10  |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | ucxusbdevice.h (include Ucxclass.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt188067">UCX_USBDEVICE_EVENT_CALLBACKS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt188052">UcxUsbDeviceCreate</a>