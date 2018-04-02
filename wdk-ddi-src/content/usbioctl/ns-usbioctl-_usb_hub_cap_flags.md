---
UID: NS:usbioctl._USB_HUB_CAP_FLAGS
title: "_USB_HUB_CAP_FLAGS"
author: windows-driver-content
description: The USB_HUB_CAP_FLAGS structure is used to report the capabilities of a hub.
old-location: buses\usb_hub_cap_flags.htm
old-project: usbref
ms.assetid: 4f3f01f2-d5ef-4b41-8733-ac44952dc9a9
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUSB_HUB_CAP_FLAGS, PUSB_HUB_CAP_FLAGS, PUSB_HUB_CAP_FLAGS union pointer [Buses], USB_HUB_CAP_FLAGS, USB_HUB_CAP_FLAGS union [Buses], _USB_HUB_CAP_FLAGS, buses.usb_hub_cap_flags, usbioctl/PUSB_HUB_CAP_FLAGS, usbioctl/USB_HUB_CAP_FLAGS, usbstrct_0c0ca119-db83-4486-9b65-f16c70716c14.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbioctl.h
req.include-header: Usbioctl.h
req.target-type: Windows
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
req.irql: "<=DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	usbioctl.h
api_name:
-	USB_HUB_CAP_FLAGS
product:
- Windows
targetos: Windows
req.typenames: USB_HUB_CAP_FLAGS, *PUSB_HUB_CAP_FLAGS
req.product: Windows 10 or later.
---

# _USB_HUB_CAP_FLAGS structure
The <b>USB_HUB_CAP_FLAGS</b> structure is used to report the capabilities of a hub.

## Syntax
```
typedef struct _USB_HUB_CAP_FLAGS {
  ULONG  ul;
  struct {
    ULONG  : 1  HubIsArmedWakeOnConnect;
    ULONG  : 1  HubIsBusPowered;
    ULONG  : 1  HubIsHighSpeed;
    ULONG  : 1  HubIsHighSpeedCapable;
    ULONG  : 1  HubIsMultiTt;
    ULONG  : 1  HubIsMultiTtCapable;
    ULONG  : 1  HubIsRoot;
    ULONG  : 25 ReservedMBZ;
  };
} USB_HUB_CAP_FLAGS, *PUSB_HUB_CAP_FLAGS;
```

## Members


`ul`

A bitmask that represents the hub capabilities.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usbioctl.h (include Usbioctl.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539329">USB_HUB_CAPABILITIES_EX</a>