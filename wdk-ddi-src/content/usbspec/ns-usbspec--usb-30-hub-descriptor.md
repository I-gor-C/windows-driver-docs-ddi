---
UID: NS.usbspec._USB_30_HUB_DESCRIPTOR
title: USB_30_HUB_DESCRIPTOR
author: windows-driver-content
description: The USB_30_HUB_DESCRIPTOR structure contains a SuperSpeed hub descriptor. For information about the structure members, see Universal Serial Bus Revision 3.0 Specification, 10.13.2.1 Hub Descriptor, Table 10-3. SuperSpeed Hub Descriptor.
old-location: buses\usb_30_hub_descriptor.htm
old-project: usbref
ms.assetid: 5B910D0B-0D1D-45D8-B418-13DC00B3398A
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USB_30_HUB_DESCRIPTOR, USB_30_HUB_DESCRIPTOR, *PUSB_30_HUB_DESCRIPTOR
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
req.alt-api: USB_30_HUB_DESCRIPTOR
req.alt-loc: Usbspec.h
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
req.iface: 
req.product: Windows 10 or later.
---

# USB_30_HUB_DESCRIPTOR structure



## -description
<p>The <b>USB_30_HUB_DESCRIPTOR</b> structure contains  a SuperSpeed hub descriptor. For information about the structure  members, see <a href="http://www.usb.org/developers/docs/">Universal Serial Bus Revision 3.0 Specification</a>, 10.13.2.1 Hub Descriptor, Table 10-3. SuperSpeed Hub Descriptor.</p>


## -syntax

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


## -struct-fields
<dl>

### -field bLength

<dd>
<p>The length, in bytes, of the descriptor.</p>
</dd>

### -field bDescriptorType

<dd>
<p>    The descriptor type. For SuperSpeed hub descriptors, the value must be USB_30_HUB_DESCRIPTOR_TYPE (0x2A).

</p>
</dd>

### -field bNumberOfPorts

<dd>
<p>    The number of ports on the hub.</p>
</dd>

### -field wHubCharacteristics

<dd>
<p>    The hub characteristics. </p>
</dd>

### -field bPowerOnToPowerGood

<dd>
<p>    The time, in 2-millisecond intervals, that it takes the device to turn on completely.</p>
</dd>

### -field bHubControlCurrent

<dd>
<p>The maximum current requirements, in milliamperes, of the controller component of the hub.</p>
</dd>

### -field bHubHdrDecLat

<dd>
<p>The    hub packet header decode latency.</p>
</dd>

### -field wHubDelay

<dd>
<p>    The average delay, in nanoseconds, that is introduced by the hub.</p>
</dd>

### -field DeviceRemovable

<dd>
<p>    Indicates whether a removable device is attached to each port.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbspec.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.usb_structures_and_enumerations">USB Structures</a>
</dt>
<dt>
<a href="..\usbioctl\ns-usbioctl--usb-hub-information-ex.md">USB_HUB_INFORMATION_EX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_30_HUB_DESCRIPTOR structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
