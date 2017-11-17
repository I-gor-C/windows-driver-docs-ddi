---
UID: NS.usbioctl._USB_PORT_PROPERTIES
title: USB_PORT_PROPERTIES
author: windows-driver-content
description: The USB_PORT_PROPERTIES union is used to report the capabilities of a Universal Serial Bus (USB) port.The port capabilities are retrieved in the USB_PORT_CONNECTOR_PROPERTIES structure by the IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES I/O control request.
old-location: buses\usb_port_properties.htm
ms.assetid: BCADC907-3770-4FBE-AEB3-96F93502E899
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: usbref
req.header: usbioctl.h
req.include-header: Usbioctl.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USB_PORT_PROPERTIES
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
ms.keywords: USB_PORT_PROPERTIES, USB_PORT_PROPERTIES, *PUSB_PORT_PROPERTIES
req.iface: 
req.product: Windows 10 or later.
---

# USB_PORT_PROPERTIES structure



## -description
<p>The <b>USB_PORT_PROPERTIES</b> union is used to report the capabilities of a Universal Serial Bus (USB) port.</p>
<p>The  port capabilities are retrieved in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406265">USB_PORT_CONNECTOR_PROPERTIES</a> structure by the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450863">IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES</a> I/O control request.</p>


## -syntax

````
typedef union _USB_PORT_PROPERTIES {
  ULONG  ul;
  struct {
    ULONG PortIsUserConnectable  :1;
    ULONG PortIsDebugCapable  :1;
    ULONG ReservedMBZ  :30;
  };
} USB_PORT_PROPERTIES, *PUSB_PORT_PROPERTIES;
````


## -struct-fields
<dl>

### -field <b>ul</b>

<dd>
<p>A bitmask that indicates the properties and capabilities of the port.</p>
</dd>

### -field <b>PortIsUserConnectable</b>

<dd>
<p>If <b>TRUE</b>, the port is visible to the user and a USB device can be attached to or detached from the port.</p>
</dd>

### -field <b>PortIsDebugCapable</b>

<dd>
<p>If <b>TRUE</b>, the port supports debugging over a USB connection.</p>
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
<dt>Usbioctl.h (include Usbioctl.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406265">USB_PORT_CONNECTOR_PROPERTIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450863">IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_PORT_PROPERTIES union%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
