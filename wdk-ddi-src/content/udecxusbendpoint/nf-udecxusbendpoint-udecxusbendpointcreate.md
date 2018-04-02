---
UID: NF:udecxusbendpoint.UdecxUsbEndpointCreate
title: UdecxUsbEndpointCreate function
author: windows-driver-content
description: Creates a UDE endpoint object.
old-location: buses\udecxusbendpointcreate.htm
old-project: usbref
ms.assetid: F97642A2-FE77-41D0-A194-8DE6F9B17BB0
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: UdecxUsbEndpointCreate, UdecxUsbEndpointCreate function [Buses], buses.udecxusbendpointcreate, udecxusbendpoint/UdecxUsbEndpointCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: udecxusbendpoint.h
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
-	UdecxUsbEndpointCreate
product: Windows
targetos: Windows
req.typenames: UDECX_USB_ENDPOINT_INIT_AND_METADATA, *PUDECX_USB_ENDPOINT_INIT_AND_METADATA
req.product: Windows 10 or later.
---


# UdecxUsbEndpointCreate function
Creates a UDE endpoint object.

## Syntax

```
NTSTATUS UdecxUsbEndpointCreate(
  PUDECXUSBENDPOINT_INIT *EndpointInit,
  PWDF_OBJECT_ATTRIBUTES Attributes,
  UDECXUSBENDPOINT       *UdecxUsbEndpoint
);
```

## Parameters

`EndpointInit`

TBD

`Attributes`

A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure that specifies attributes for the USB device object.

`UdecxUsbEndpoint`

A pointer to a variable that receives a handle to the new UDE endpoint object that represents the simple endpoint on the  USB device.


## Return Value

The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.15 |
| **Header** | udecxusbendpoint.h (include Udecx.h) |
| **Library** | Udecxstub.lib |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt595932">Architecture: USB Device Emulation (UDE)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt627989">UdecxUsbSimpleEndpointInitAllocate</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt595939">Write a UDE client driver</a>