---
UID: NF:udecxusbdevice.UdecxUsbDeviceInitAllocate
title: UdecxUsbDeviceInitAllocate function
author: windows-driver-content
description: Allocates memory for a UDECXUSBDEVICE_INIT structure that is used to initialize a virtual USB device.
old-location: buses\udecxusbdeviceinitallocate.htm
old-project: usbref
ms.assetid: 127D132B-6A40-4F6F-BCDA-473F89A1A747
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: UdecxUsbDeviceInitAllocate, UdecxUsbDeviceInitAllocate function [Buses], buses.udecxusbdeviceinitallocate, udecxusbdevice/UdecxUsbDeviceInitAllocate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: udecxusbdevice.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Udecxstub.lib
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Udecxstub.lib
-	Udecxstub.dll
api_name:
-	UdecxUsbDeviceInitAllocate
product: Windows
targetos: Windows
req.typenames: UDECX_USB_DEVICE_WAKE_SETTING, *PUDECX_USB_DEVICE_WAKE_SETTING
req.product: Windows 10 or later.
---


# UdecxUsbDeviceInitAllocate function
Allocates memory for a  <b>UDECXUSBDEVICE_INIT</b> structure that is used to initialize a virtual USB device.

## Syntax

```
PUDECXUSBDEVICE_INIT UdecxUsbDeviceInitAllocate(
  WDFDEVICE UdecxWdfDevice
);
```

## Parameters

`UdecxWdfDevice`

A handle to a framework device object that represents the a USB device. The client driver initialized this object in the previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt627990">UdecxWdfDeviceAddUsbDeviceEmulation</a>.


## Return Value

This method returns a pointer to an opaque <b>UDECXUSBDEVICE_INIT</b> that contains the initialization parameters. The structure is allocated by the USB device emulation  class extension (UdeCx).

## Remarks

The UDE client driver calls this method to allocate parameters for the virtual device that is created by a subsequent call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt595959">UdecxUsbDeviceCreate</a>. If the device is not created or the driver is finished using the resources, the driver must free the resources by calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt627969">UdecxUsbDeviceInitFree</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.15 |
| **Header** | udecxusbdevice.h (include Udecx.h) |
| **Library** | Udecxstub.lib |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt595932">Architecture: USB Device Emulation (UDE)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt595939">Write a UDE client driver</a>