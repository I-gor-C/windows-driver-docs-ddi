---
UID: NE:usb._USBD_ENDPOINT_OFFLOAD_MODE
title: "_USBD_ENDPOINT_OFFLOAD_MODE"
author: windows-driver-content
description: Defines values for endpoint offloading options in the USB device or host controller.
old-location: buses\usbd_endpoint_offload_mode.htm
old-project: usbref
ms.assetid: 577B2B5E-934E-4354-B6FF-FDFE9D1144D7
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: USBD_ENDPOINT_OFFLOAD_MODE, USBD_ENDPOINT_OFFLOAD_MODE enumeration [Buses], UsbdEndpointOffloadHardwareAssisted, UsbdEndpointOffloadModeNotSupported, UsbdEndpointOffloadSoftwareAssisted, _USBD_ENDPOINT_OFFLOAD_MODE, buses.usbd_endpoint_offload_mode, usb/USBD_ENDPOINT_OFFLOAD_MODE, usb/UsbdEndpointOffloadHardwareAssisted, usb/UsbdEndpointOffloadModeNotSupported, usb/UsbdEndpointOffloadSoftwareAssisted
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: usb.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
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
-	HeaderDef
api_location:
-	Usb.h
api_name:
-	USBD_ENDPOINT_OFFLOAD_MODE
product: Windows
targetos: Windows
req.typenames: USBD_ENDPOINT_OFFLOAD_MODE
req.product: Windows 10 or later.
---

# _USBD_ENDPOINT_OFFLOAD_MODE Enumeration
Defines values for endpoint offloading options in the USB device or host controller.

## Syntax
```
typedef enum _USBD_ENDPOINT_OFFLOAD_MODE {
  UsbdEndpointOffloadModeNotSupported  ,
  UsbdEndpointOffloadSoftwareAssisted  ,
  UsbdEndpointOffloadHardwareAssisted
} USBD_ENDPOINT_OFFLOAD_MODE;
```

## Constants

<table>
            
                <tr>
                    <td>UsbdEndpointOffloadModeNotSupported</td>
                    <td>Endpoint offloading is not supported.</td>
                </tr>
            
                <tr>
                    <td>UsbdEndpointOffloadSoftwareAssisted</td>
                    <td>Endpoint offloading is handled by the software.</td>
                </tr>
            
                <tr>
                    <td>UsbdEndpointOffloadHardwareAssisted</td>
                    <td>Endpoint offloading is handled in the USB device or host controller hardware.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1709 Windows 10, version 1709 |
| **Header** | usb.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh406230">USBD_QueryUsbCapability</a>