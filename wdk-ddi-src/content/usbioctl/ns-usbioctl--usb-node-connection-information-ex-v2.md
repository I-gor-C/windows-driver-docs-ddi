---
UID: NS.usbioctl._USB_NODE_CONNECTION_INFORMATION_EX_V2
title: USB_NODE_CONNECTION_INFORMATION_EX_V2
author: windows-driver-content
description: The USB_NODE_CONNECTION_INFORMATION_EX_V2 structure is used with the IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX_V2 I/O control request to retrieve speed information about a Universal Serial Bus (USB) device that is attached to a particular port.
old-location: buses\_usb_node_connection_information_ex_v2.htm
ms.assetid: F886F470-BAAB-41C6-8431-01BF99236F81
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
req.alt-api: USB_NODE_CONNECTION_INFORMATION_EX_V2
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
ms.keywords: USB_NODE_CONNECTION_INFORMATION_EX_V2, USB_NODE_CONNECTION_INFORMATION_EX_V2, *PUSB_NODE_CONNECTION_INFORMATION_EX_V2
req.iface: 
req.product: Windows 10 or later.
---

# USB_NODE_CONNECTION_INFORMATION_EX_V2 structure



## -description
<p>The <b>USB_NODE_CONNECTION_INFORMATION_EX_V2</b> structure is used with the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450861">IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX_V2</a> I/O control request to retrieve speed information about a Universal Serial Bus (USB) device that is attached to a particular port.</p>


## -syntax

````
typedef struct _USB_NODE_CONNECTION_INFORMATION_EX_V2 {
  ULONG                                       ConnectionIndex;
  ULONG                                       Length;
  USB_PROTOCOLS                               SupportedUsbProtocols;
  USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS Flags;
} USB_NODE_CONNECTION_INFORMATION_EX_V2, *PUSB_NODE_CONNECTION_INFORMATION_EX_V2;
````


## -struct-fields
<dl>

### -field <b>ConnectionIndex</b>

<dd>
<p>The port number. If there are <i>n</i> ports on the USB hub, the ports are numbered from 1 to <i>n</i>. To get the number of ports, send the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450860">IOCTL_USB_GET_HUB_INFORMATION_EX</a> I/O control request. The request retrieves the highest port number on the hub.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>The number of bytes that are required to hold the <b>USB_NODE_CONNECTION_INFORMATION_EX_V2</b> structure. The value must be set by the caller as input to  the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450861">IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX_V2</a> request.</p>
</dd>

### -field <b>SupportedUsbProtocols</b>

<dd>
<p>The USB signaling protocols that are supported by the port. </p>
<p>In the caller's <a href="https://msdn.microsoft.com/library/windows/hardware/hh450861">IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX_V2</a> request, the caller can set <b>SupportedUsbProtocols</b> to a bitwise <b>OR</b> of one or more flags defined in <a href="https://msdn.microsoft.com/library/windows/hardware/hh406267">USB_PROTOCOLS</a>.</p>
<p>Upon completion of the request, <b>SupportedUsbProtocols</b> contains flags, which indicate the protocols that are actually supported by the port.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitmask that indicates the properties and capabilities of the attached device or  port. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh406264">USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS</a>.</p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_NODE_CONNECTION_INFORMATION_EX_V2 structure%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
