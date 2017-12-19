---
UID: NS.USBIOCTL._USB_HUB_CAP_FLAGS
title: _USB_HUB_CAP_FLAGS
author: windows-driver-content
description: The USB_HUB_CAP_FLAGS structure is used to report the capabilities of a hub.
old-location: buses\usb_hub_cap_flags.htm
old-project: UsbRef
ms.assetid: 4f3f01f2-d5ef-4b41-8733-ac44952dc9a9
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _USB_HUB_CAP_FLAGS, PUSB_HUB_CAP_FLAGS, USB_HUB_CAP_FLAGS, *PUSB_HUB_CAP_FLAGS
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
req.alt-api: USB_HUB_CAP_FLAGS
req.alt-loc: usbioctl.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# _USB_HUB_CAP_FLAGS structure



## -description
The <b>USB_HUB_CAP_FLAGS</b> structure is used to report the capabilities of a hub.



## -syntax

````
typedef union _USB_HUB_CAP_FLAGS {
  ULONG  ul;
  struct {
    ULONG HubIsHighSpeedCapable  :1;
    ULONG HubIsHighSpeed  :1;
    ULONG HubIsMultiTtCapable  :1;
    ULONG HubIsMultiTt  :1;
    ULONG HubIsRoot  :1;
    ULONG HubIsArmedWakeOnConnect  :1;
    ULONG HubIsBusPowered  :1;
    ULONG ReservedMBZ  :25;
  };
} USB_HUB_CAP_FLAGS, *PUSB_HUB_CAP_FLAGS;
````


## -struct-fields

### -field ul

A bitmask that represents the hub capabilities.


### -field HubIsHighSpeedCapable

If <b>TRUE</b>, the hub is high speed-capable. This capability does not necessarily mean that the hub is operating at high speed


### -field HubIsHighSpeed

If <b>TRUE</b>, the hub is high speed.


### -field HubIsMultiTtCapable

If <b>TRUE</b>, the hub is capable of doing multiple transaction translations simultaneously.


### -field HubIsMultiTt

If <b>TRUE</b>, the hub is configured to perform multiple transaction translations simultaneously.


### -field HubIsRoot

If <b>TRUE</b>, the hub is the root hub.


### -field HubIsArmedWakeOnConnect

If <b>TRUE</b>, the hub is armed to wake when a device is connected to the hub.


### -field HubIsBusPowered

A boolean value that indicates whether the hub is bus-powered. <b>TRUE</b>, the hub is bus-powered; <b>FALSE</b>, the hub is self-powered.


### -field ReservedMBZ

Reserved. Do not use.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Usbioctl.h (include Usbioctl.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.usb_hub_capabilities_ex">USB_HUB_CAPABILITIES_EX</a>
</dt>
<dt>
<a href="buses.usb_structures_and_enumerations">USB Structures</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [UsbRef\buses]:%20USB_HUB_CAP_FLAGS union%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

