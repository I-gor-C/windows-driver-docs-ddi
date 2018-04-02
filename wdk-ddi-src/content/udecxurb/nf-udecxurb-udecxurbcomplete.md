---
UID: NF:udecxurb.UdecxUrbComplete
title: UdecxUrbComplete function
author: windows-driver-content
description: Completes the URB request with a USB-specific completion status code.
old-location: buses\udecxurbcomplete.htm
old-project: usbref
ms.assetid: F0B014F3-AE40-466B-BD9A-0D01DF70DCFF
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: UdecxUrbComplete, UdecxUrbComplete function [Buses], buses.udecxurbcomplete, udecxurb/UdecxUrbComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: udecxurb.h
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
-	UdecxUrbComplete
product: Windows
targetos: Windows
req.typenames: USB_DEVICE_PORT_PATH, *PUSB_DEVICE_PORT_PATH
req.product: Windows 10 or later.
---


# UdecxUrbComplete function
Completes the URB request with a USB-specific completion status code.

## Syntax

```
void UdecxUrbComplete(
  WDFREQUEST  Request,
  USBD_STATUS UsbdStatus
);
```

## Parameters

`Request`

A handle to a framework request object that contains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a> for the transfer.

`UsbdStatus`

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff539136">USBD_STATUS</a>-typed value that indicates the success or failure of the completed URB request.


## Return Value

This function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.15 |
| **Header** | udecxurb.h (include Udecx.h) |
| **Library** | Udecxstub.lib |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt595932">Architecture: USB Device Emulation (UDE)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt595939">Write a UDE client driver</a>