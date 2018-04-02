---
UID: NF:udecxusbendpoint.UdecxUsbEndpointInitSetCallbacks
title: UdecxUsbEndpointInitSetCallbacks function
author: windows-driver-content
description: Sets pointers to UDE client driver-implemented callback functions in the initialization parameters of the simple endpoint to create.
old-location: buses\udecxusbendpointinitsetcallbacks.htm
old-project: usbref
ms.assetid: 0F6EBBDA-FA0B-4044-905B-535D4FFEC5D2
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: UdecxUsbEndpointInitSetCallbacks, UdecxUsbEndpointInitSetCallbacks function [Buses], buses.udecxusbendpointinitsetcallbacks, udecxusbendpoint/UdecxUsbEndpointInitSetCallbacks
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
-	UdecxUsbEndpointInitSetCallbacks
product: Windows
targetos: Windows
req.typenames: UDECX_USB_ENDPOINT_INIT_AND_METADATA, *PUDECX_USB_ENDPOINT_INIT_AND_METADATA
req.product: Windows 10 or later.
---


# UdecxUsbEndpointInitSetCallbacks function
Sets pointers to UDE client driver-implemented  callback functions in the initialization parameters of the simple endpoint to create.

## Syntax

```
void UdecxUsbEndpointInitSetCallbacks(
  PUDECXUSBENDPOINT_INIT        UdecxUsbEndpointInit,
  PUDECX_USB_ENDPOINT_CALLBACKS EndpointCallbacks
);
```

## Parameters

`UdecxUsbEndpointInit`

TBD

`EndpointCallbacks`

A pointer to <a href="https://msdn.microsoft.com/library/windows/hardware/mt628005">UDECX_USB_ENDPOINT_CALLBACKS</a> that contains function pointers to event callback functions implemented by the UDE client driver.


## Return Value

This function does not return a value.


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



<a href="https://msdn.microsoft.com/library/windows/hardware/mt627983">UdecxUsbEndpointCreate</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt595939">Write a UDE client driver</a>