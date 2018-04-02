---
UID: NS:usbspec._USB_30_HUB_DESCRIPTOR
title: "_USB_30_HUB_DESCRIPTOR"
author: windows-driver-content
description: The USB_30_HUB_DESCRIPTOR structure contains a SuperSpeed hub descriptor. For information about the structure members, see Universal Serial Bus Revision 3.0 Specification, 10.13.2.1 Hub Descriptor, Table 10-3. SuperSpeed Hub Descriptor.
old-location: buses\usb_30_hub_descriptor.htm
old-project: usbref
ms.assetid: 5B910D0B-0D1D-45D8-B418-13DC00B3398A
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUSB_30_HUB_DESCRIPTOR, PUSB_30_HUB_DESCRIPTOR, PUSB_30_HUB_DESCRIPTOR structure pointer [Buses], USB_30_HUB_DESCRIPTOR, USB_30_HUB_DESCRIPTOR structure [Buses], _USB_30_HUB_DESCRIPTOR, buses.usb_30_hub_descriptor, usbspec/PUSB_30_HUB_DESCRIPTOR, usbspec/USB_30_HUB_DESCRIPTOR"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbspec.h
req.include-header: 
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Usbspec.h
api_name:
-	USB_30_HUB_DESCRIPTOR
product:
- Windows
targetos: Windows
req.typenames: USB_30_HUB_DESCRIPTOR, *PUSB_30_HUB_DESCRIPTOR
req.product: Windows 10 or later.
---

# _USB_30_HUB_DESCRIPTOR structure
The <b>USB_30_HUB_DESCRIPTOR</b> structure contains  a SuperSpeed hub descriptor. For information about the structure  members, see <a href="http://www.usb.org/developers/docs/">Universal Serial Bus Revision 3.0 Specification</a>, 10.13.2.1 Hub Descriptor, Table 10-3. SuperSpeed Hub Descriptor.

## Syntax
```
typedef struct _USB_30_HUB_DESCRIPTOR {
  UCHAR  bLength;
  UCHAR  bDescriptorType;
  UCHAR  bNumberOfPorts;
  USHORT wHubCharacteristics;
  UCHAR  bPowerOnToPowerGood;
  UCHAR  bHubControlCurrent;
  UCHAR  bHubHdrDecLat;
  USHORT wHubDelay;
  USHORT DeviceRemovable;
} *PUSB_30_HUB_DESCRIPTOR, USB_30_HUB_DESCRIPTOR;
```

## Members


`bLength`

The length, in bytes, of the descriptor.

`bDescriptorType`

The descriptor type. For SuperSpeed hub descriptors, the value must be USB_30_HUB_DESCRIPTOR_TYPE (0x2A).

`bNumberOfPorts`

The number of ports on the hub.

`wHubCharacteristics`

The hub characteristics.

`bPowerOnToPowerGood`

The time, in 2-millisecond intervals, that it takes the device to turn on completely.

`bHubControlCurrent`

The maximum current requirements, in milliamperes, of the controller component of the hub.

`bHubHdrDecLat`

The    hub packet header decode latency.

`wHubDelay`

The average delay, in nanoseconds, that is introduced by the hub.

`DeviceRemovable`

Indicates whether a removable device is attached to each port.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | usbspec.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh406262">USB_HUB_INFORMATION_EX</a>