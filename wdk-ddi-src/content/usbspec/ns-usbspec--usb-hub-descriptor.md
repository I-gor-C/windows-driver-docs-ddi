---
UID: NS.usbspec._USB_HUB_DESCRIPTOR
title: USB_HUB_DESCRIPTOR
author: windows-driver-content
description: The USB_HUB_DESCRIPTOR structure contains a hub descriptor.
old-location: buses\usb_hub_descriptor.htm
old-project: usbref
ms.assetid: 6f5521f4-44da-4470-b649-d98c1d4e4891
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USB_HUB_DESCRIPTOR, USB_HUB_DESCRIPTOR, *PUSB_HUB_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbspec.h
req.include-header: Usbioctl.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USB_HUB_DESCRIPTOR
req.alt-loc: usbspec.h
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

# USB_HUB_DESCRIPTOR structure



## -description
<p>The <b>USB_HUB_DESCRIPTOR</b> structure contains a hub descriptor.</p>


## -syntax

````
typedef struct _USB_HUB_DESCRIPTOR {
  UCHAR  bDescriptorLength;
  UCHAR  bDescriptorType;
  UCHAR  bNumberOfPorts;
  USHORT wHubCharacteristics;
  UCHAR  bPowerOnToPowerGood;
  UCHAR  bHubControlCurrent;
  UCHAR  bRemoveAndPowerMask[64];
} USB_HUB_DESCRIPTOR, *PUSB_HUB_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field bDescriptorLength

<dd>
<p>The length, in bytes, of the descriptor.</p>
</dd>

### -field bDescriptorType

<dd>
<p>The descriptor type. For hub descriptors, this value should be 0x29.</p>
</dd>

### -field bNumberOfPorts

<dd>
<p>The number of ports on the hub.</p>
</dd>

### -field wHubCharacteristics

<dd>
<p>The hub characteristics. For more information about this member, see Universal Serial Bus Specification.</p>
</dd>

### -field bPowerOnToPowerGood

<dd>
<p>The time, in 2-millisecond intervals, that it takes the device to turn on completely. For more information about this member, see Universal Serial Bus Specification.</p>
</dd>

### -field bHubControlCurrent

<dd>
<p>The maximum current requirements, in milliamperes, of the controller component of the hub.</p>
</dd>

### -field bRemoveAndPowerMask

<dd>
<p>Not currently implemented. Do not use this member. </p>
<p>This member implements DeviceRemovable and PortPwrCtrlMask fields of the hub descriptor. For more information about these fields, see Universal Serial Bus Specification. </p>
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
<dt>Usbspec.h (include Usbioctl.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\usbioctl\ns-usbioctl--usb-hub-information.md">USB_HUB_INFORMATION</a>
</dt>
<dt>
<a href="buses.usb_structures_and_enumerations">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_HUB_DESCRIPTOR structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
