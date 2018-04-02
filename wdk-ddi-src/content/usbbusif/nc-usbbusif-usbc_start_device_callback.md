---
UID: NC:usbbusif.USBC_START_DEVICE_CALLBACK
title: USBC_START_DEVICE_CALLBACK
author: windows-driver-content
description: The USBC_START_DEVICE_CALLBACK routine allows a USB client driver to provide a custom definition of the interface collections on a device.
old-location: buses\usbc_start_device_callback.htm
old-project: usbref
ms.assetid: f9a9510a-b55c-4566-83ce-4ed7ccafb543
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: USBC_START_DEVICE_CALLBACK, UsbcStartDeviceCallback, UsbcStartDeviceCallback callback function [Buses], buses.usbc_start_device_callback, usbbusif/UsbcStartDeviceCallback, usbinterKR_d70617c5-be67-4660-9aa3-76b4c66c2616.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: usbbusif.h
req.include-header: Usbbusif.h
req.target-type: Desktop
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
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	usbbusif.h
api_name:
-	UsbcStartDeviceCallback
product:
- Windows
targetos: Windows
req.typenames: USBD_VERSION_INFORMATION, *PUSBD_VERSION_INFORMATION
req.product: Windows 10 or later.
---


# USBC_START_DEVICE_CALLBACK callback function
The <b>USBC_START_DEVICE_CALLBACK</b> routine allows a USB client driver to provide a custom definition of the interface collections on a device.

## Syntax

```
USBC_START_DEVICE_CALLBACK UsbcStartDeviceCallback;

NTSTATUS UsbcStartDeviceCallback(
  PUSB_DEVICE_DESCRIPTOR DeviceDescriptor,
  PUSB_CONFIGURATION_DESCRIPTOR ConfigurationDescriptor,
  PUSBC_FUNCTION_DESCRIPTOR *FunctionDescriptorBuffer,
  PULONG FunctionDescriptorBufferLength,
  PDEVICE_OBJECT FdoDeviceObject,
  PDEVICE_OBJECT PdoDeviceObject
)
{...}
```

## Parameters

`DeviceDescriptor`

The device descriptor of the device.

`ConfigurationDescriptor`

The configuration of the device.

`*FunctionDescriptorBuffer`

Pointer to a buffer that contains an array of function descriptors (<a href="https://msdn.microsoft.com/library/windows/hardware/ff539001">USBC_FUNCTION_DESCRIPTOR</a>).

`FunctionDescriptorBufferLength`

The length in bytes of the buffer that <i>FunctionDescriptorBuffer</i> points to.

`FdoDeviceObject`

The function device object for the device.

`PdoDeviceObject`

The physical device object for the device.


## Return Value

If the operation succeeds, the vendor-supplied callback routine must return STATUS_SUCCESS.

## Remarks

For a general description of the callback routine mechanism, see <a href="https://msdn.microsoft.com/3cf4e9f2-ea33-491f-94af-62d2afacc899">Customizing Enumeration of Interface Collections for Composite Devices</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | usbbusif.h (include Usbbusif.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff538990">USBC_DEVICE_CONFIGURATION_INTERFACE_V1</a>