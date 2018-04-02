---
UID: NF:udecxusbdevice.UdecxUsbDeviceInitAddDescriptorWithIndex
title: UdecxUsbDeviceInitAddDescriptorWithIndex function
author: windows-driver-content
description: Adds a USB descriptor to the initialization parameters used to create a virtual USB device.
old-location: buses\udecxusbdeviceinitadddescriptorwithindex.htm
old-project: usbref
ms.assetid: 96DF01F1-2584-4152-8EB9-D2515CA42B03
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: UdecxUsbDeviceInitAddDescriptorWithIndex, UdecxUsbDeviceInitAddDescriptorWithIndex function [Buses], buses.udecxusbdeviceinitadddescriptorwithindex, udecxusbdevice/UdecxUsbDeviceInitAddDescriptorWithIndex
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
-	UdecxUsbDeviceInitAddDescriptorWithIndex
product: Windows
targetos: Windows
req.typenames: UDECX_USB_DEVICE_WAKE_SETTING, *PUDECX_USB_DEVICE_WAKE_SETTING
req.product: Windows 10 or later.
---


# UdecxUsbDeviceInitAddDescriptorWithIndex function
Adds a USB descriptor to the initialization parameters used to create a virtual USB device.

## Syntax

```
NTSTATUS UdecxUsbDeviceInitAddDescriptorWithIndex(
  PUDECXUSBDEVICE_INIT UdecxUsbDeviceInit,
  PUCHAR               Descriptor,
  USHORT               DescriptorLength,
  UCHAR                DescriptorIndex
);
```

## Parameters

`UdecxUsbDeviceInit`

A pointer to a WDF-allocated structure that contains initialization parameters for the virtual USB device.  The client driver retrieved this pointer in the previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt627968">UdecxUsbDeviceInitAllocate</a>.

`Descriptor`

A caller-allocated buffer that contains the USB descriptor to add to the device.

`DescriptorLength`

The length of the descriptor buffer.

`DescriptorIndex`

The index of the descriptor.


## Return Value

The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.


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



<a href="https://msdn.microsoft.com/library/windows/hardware/ff540156">USB String Descriptors</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt627968">UdecxUsbDeviceInitAllocate</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt595939">Write a UDE client driver</a>