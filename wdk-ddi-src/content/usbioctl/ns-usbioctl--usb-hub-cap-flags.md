---
UID: NS.usbioctl._USB_HUB_CAP_FLAGS
title: USB_HUB_CAP_FLAGS
author: windows-driver-content
description: The USB_HUB_CAP_FLAGS structure is used to report the capabilities of a hub.
old-location: buses\usb_hub_cap_flags.htm
old-project: usbref
ms.assetid: 4f3f01f2-d5ef-4b41-8733-ac44952dc9a9
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USB_HUB_CAP_FLAGS, USB_HUB_CAP_FLAGS, *PUSB_HUB_CAP_FLAGS
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
req.iface: 
req.product: Windows 10 or later.
---

# USB_HUB_CAP_FLAGS structure



## -description
<p>The <b>USB_HUB_CAP_FLAGS</b> structure is used to report the capabilities of a hub.</p>


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
<dl>

### -field <b>ul</b>

<dd>
<p>A bitmask that represents the hub capabilities.</p>
</dd>

### -field <b>HubIsHighSpeedCapable</b>

<dd>
<p>If <b>TRUE</b>, the hub is high speed-capable. This capability does not necessarily mean that the hub is operating at high speed</p>
</dd>

### -field <b>HubIsHighSpeed</b>

<dd>
<p>If <b>TRUE</b>, the hub is high speed.</p>
</dd>

### -field <b>HubIsMultiTtCapable</b>

<dd>
<p>If <b>TRUE</b>, the hub is capable of doing multiple transaction translations simultaneously.</p>
</dd>

### -field <b>HubIsMultiTt</b>

<dd>
<p>If <b>TRUE</b>, the hub is configured to perform multiple transaction translations simultaneously.</p>
</dd>

### -field <b>HubIsRoot</b>

<dd>
<p>If <b>TRUE</b>, the hub is the root hub.</p>
</dd>

### -field <b>HubIsArmedWakeOnConnect</b>

<dd>
<p>If <b>TRUE</b>, the hub is armed to wake when a device is connected to the hub.</p>
</dd>

### -field <b>HubIsBusPowered</b>

<dd>
<p>A boolean value that indicates whether the hub is bus-powered. <b>TRUE</b>, the hub is bus-powered; <b>FALSE</b>, the hub is self-powered.</p>
</dd>

### -field <b>ReservedMBZ</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="..\usbioctl\ns-usbioctl--usb-hub-capabilities-ex.md">USB_HUB_CAPABILITIES_EX</a>
</dt>
<dt>
<a href="buses.usb_structures_and_enumerations">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_HUB_CAP_FLAGS union%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
