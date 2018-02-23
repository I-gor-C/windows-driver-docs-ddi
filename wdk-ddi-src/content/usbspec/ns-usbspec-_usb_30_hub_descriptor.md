---
UID: NS:usbspec._USB_30_HUB_DESCRIPTOR
title: "_USB_30_HUB_DESCRIPTOR"
author: windows-driver-content
description: The USB_30_HUB_DESCRIPTOR structure contains a SuperSpeed hub descriptor. For information about the structure members, see Universal Serial Bus Revision 3.0 Specification, 10.13.2.1 Hub Descriptor, Table 10-3. SuperSpeed Hub Descriptor.
old-location: buses\usb_30_hub_descriptor.htm
old-project: UsbRef
ms.assetid: 5B910D0B-0D1D-45D8-B418-13DC00B3398A
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: buses.usb_30_hub_descriptor, PUSB_30_HUB_DESCRIPTOR structure pointer [Buses], PUSB_30_HUB_DESCRIPTOR, USB_30_HUB_DESCRIPTOR structure [Buses], USB_30_HUB_DESCRIPTOR, usbspec/PUSB_30_HUB_DESCRIPTOR, usbspec/USB_30_HUB_DESCRIPTOR, _USB_30_HUB_DESCRIPTOR, *PUSB_30_HUB_DESCRIPTOR
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Usbspec.h
apiname:
-	USB_30_HUB_DESCRIPTOR
product: Windows
targetos: Windows
req.typenames: "*PUSB_30_HUB_DESCRIPTOR, USB_30_HUB_DESCRIPTOR"
req.product: Windows 10 or later.
---

# _USB_30_HUB_DESCRIPTOR structure
The <b>USB_30_HUB_DESCRIPTOR</b> structure contains  a SuperSpeed hub descriptor. For information about the structure  members, see <a href="http://www.usb.org/developers/docs/">Universal Serial Bus Revision 3.0 Specification</a>, 10.13.2.1 Hub Descriptor, Table 10-3. SuperSpeed Hub Descriptor.

## Syntax
````
typedef struct _USB_30_HUB_DESCRIPTOR {
  UCHAR  bLength;
  UCHAR  bDescriptorType;
  UCHAR  bNumberOfPorts;
  USHORT wHubCharacteristics;
  UCHAR  bPowerOnToPowerGood;
  UCHAR  bHubControlCurrent;
  UCHAR  bHubHdrDecLat;
  USHORT wHubDelay;
  USHORT DeviceRemovable;
} USB_30_HUB_DESCRIPTOR, *PUSB_30_HUB_DESCRIPTOR;
````

## Members


`bDescriptorType`

The descriptor type. For SuperSpeed hub descriptors, the value must be USB_30_HUB_DESCRIPTOR_TYPE (0x2A).

`bHubControlCurrent`

The maximum current requirements, in milliamperes, of the controller component of the hub.

`bHubHdrDecLat`

The    hub packet header decode latency.

`bLength`

The length, in bytes, of the descriptor.

`bNumberOfPorts`

The number of ports on the hub.

`bPowerOnToPowerGood`

The time, in 2-millisecond intervals, that it takes the device to turn on completely.

`DeviceRemovable`

Indicates whether a removable device is attached to each port.

`wHubCharacteristics`

The hub characteristics.

`wHubDelay`

The average delay, in nanoseconds, that is introduced by the hub.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | usbspec.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>



<a href="..\usbioctl\ns-usbioctl-_usb_hub_information_ex.md">USB_HUB_INFORMATION_EX</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [UsbRef\buses]:%20USB_30_HUB_DESCRIPTOR structure%20 RELEASE:%20(2/15/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>