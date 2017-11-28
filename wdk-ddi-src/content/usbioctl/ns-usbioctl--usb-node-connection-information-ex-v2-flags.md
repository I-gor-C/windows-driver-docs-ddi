---
UID: NS.usbioctl._USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS
title: USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS
author: windows-driver-content
description: The USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS union is used to indicate the speed at which a USB 3.0 device is currently operating and whether it can operate at higher speed, when attached to a particular port.
old-location: buses\usb_node_connection_information_ex_v2_flags.htm
old-project: usbref
ms.assetid: F066CE0E-3247-4C42-9EF6-8A6EB0C0BC71
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS, USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS, *PUSB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS
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
req.alt-api: USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS
req.alt-loc: Usbioctl.h
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

# USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS structure



## -description
<p>The <b>USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS</b> union is used to indicate the speed at which a USB 3.0  device is currently operating and whether it can operate at higher speed, when attached to a particular port. </p>
<p>Device speed information is obtained in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406295">USB_NODE_CONNECTION_INFORMATION_EX_V2</a> structure by the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450861">IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX_V2</a> I/O control request.</p>
<p>Or: the speed in which a device attached to a port is currently operating and at what speeds it is capable of operating.</p>


## -syntax

````
typedef union _USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS {
  ULONG  ul;
  struct {
    ULONG DeviceIsOperatingAtSuperSpeedOrHigher  :1;
    ULONG DeviceIsSuperSpeedCapableOrHigher  :1;
    ULONG ReservedMBZ  :30;
  };
} USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS, *PUSB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS;
````


## -struct-fields
<dl>

### -field <b>ul</b>

<dd>
<p>A bitmask that indicates the USB speed of the device that is attached to the port.</p>
</dd>

### -field <b>DeviceIsOperatingAtSuperSpeedOrHigher</b>

<dd>
<p>If <b>TRUE</b>, the attached device is currently operating at SuperSpeed or a higher speed that is defined by the official USB specification. </p>
</dd>

### -field <b>DeviceIsSuperSpeedCapableOrHigher</b>

<dd>
<p>If <b>TRUE</b>, the attached device is a USB 3.0 device and is capable of operating at SuperSpeed or a higher speed that is defined by the official USB specification.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406264">USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450861">IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX_V2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS union%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
