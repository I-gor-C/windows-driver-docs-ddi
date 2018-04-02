---
UID: NS:usbioctl._USB_PORT_PROPERTIES
title: "_USB_PORT_PROPERTIES"
author: windows-driver-content
description: The USB_PORT_PROPERTIES union is used to report the capabilities of a Universal Serial Bus (USB) port.The port capabilities are retrieved in the USB_PORT_CONNECTOR_PROPERTIES structure by the IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES I/O control request.
old-location: buses\usb_port_properties.htm
old-project: usbref
ms.assetid: BCADC907-3770-4FBE-AEB3-96F93502E899
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUSB_PORT_PROPERTIES, PUSB_PORT_PROPERTIES, PUSB_PORT_PROPERTIES union pointer [Buses], USB_PORT_PROPERTIES, USB_PORT_PROPERTIES union [Buses], _USB_PORT_PROPERTIES, buses.usb_port_properties, usbioctl/PUSB_PORT_PROPERTIES, usbioctl/USB_PORT_PROPERTIES"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbioctl.h
req.include-header: Usbioctl.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: None supported
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
req.irql: "<=DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	usbioctl.h
api_name:
-	USB_PORT_PROPERTIES
product: Windows
targetos: Windows
req.typenames: USB_PORT_PROPERTIES, *PUSB_PORT_PROPERTIES
req.product: Windows 10 or later.
---

# _USB_PORT_PROPERTIES structure
The <b>USB_PORT_PROPERTIES</b> union is used to report the capabilities of a Universal Serial Bus (USB) port.

The  port capabilities are retrieved in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406265">USB_PORT_CONNECTOR_PROPERTIES</a> structure by the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450863">IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES</a> I/O control request.

## Syntax
```
typedef struct _USB_PORT_PROPERTIES {
  ULONG  ul;
  struct {
    ULONG  : 1  PortConnectorIsTypeC;
    ULONG  : 1  PortHasMultipleCompanions;
    ULONG  : 1  PortIsDebugCapable;
    ULONG  : 1  PortIsUserConnectable;
    ULONG  : 28 ReservedMBZ;
  };
} *PUSB_PORT_PROPERTIES, USB_PORT_PROPERTIES;
```

## Members


`ul`

A bitmask that indicates the properties and capabilities of the port.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | usbioctl.h (include Usbioctl.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh450863">IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh406265">USB_PORT_CONNECTOR_PROPERTIES</a>