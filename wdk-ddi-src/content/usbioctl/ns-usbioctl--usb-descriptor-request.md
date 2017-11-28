---
UID: NS.usbioctl._USB_DESCRIPTOR_REQUEST
title: USB_DESCRIPTOR_REQUEST
author: windows-driver-content
description: The USB_DESCRIPTOR_REQUEST structure is used with the IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION I/O control request to retrieve one or more descriptors for the device that is associated with the indicated connection index.
old-location: buses\usb_descriptor_request.htm
old-project: usbref
ms.assetid: d4d51366-4d04-47fe-8c44-09c9c6ccf35f
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USB_DESCRIPTOR_REQUEST, USB_DESCRIPTOR_REQUEST, *PUSB_DESCRIPTOR_REQUEST
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
req.alt-api: USB_DESCRIPTOR_REQUEST
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

# USB_DESCRIPTOR_REQUEST structure



## -description
<p>The <b>USB_DESCRIPTOR_REQUEST</b> structure is used with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537310">IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION</a> I/O control request to retrieve one or more descriptors for the device that is associated with the indicated connection index.</p>


## -syntax

````
typedef struct _USB_DESCRIPTOR_REQUEST {
  ULONG  ConnectionIndex;
  struct {
    UCHAR  bmRequest;
    UCHAR  bRequest;
    USHORT wValue;
    USHORT wIndex;
    USHORT wLength;
  } SetupPacket;
  UCHAR  Data[];
} USB_DESCRIPTOR_REQUEST, *PUSB_DESCRIPTOR_REQUEST;
````


## -struct-fields
<dl>

### -field <b>ConnectionIndex</b>

<dd>
<p>The port whose descriptors are retrieved.</p>
</dd>

### -field <b>SetupPacket</b>

<dd>
<p>The members of the <b>SetupPacket</b> structure are as follows:</p>
<dl>

### -field <b>bmRequest</b>

<dd>
<p>The type of USB device request (standard, class, or vendor), the direction of the data transfer, and the type of data recipient (device, interface, or endpoint). On input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537310">IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION</a> I/O control request, the USB stack ignores the value of <b>bmRequest</b> and inserts a value of 0x80. This value indicates a standard USB device request and a device-to-host data transfer. For more information about this member, see Universal Serial Bus Specification.</p>
</dd>

### -field <b>bRequest</b>

<dd>
<p>The request number. On input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537310">IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION</a> I/O control request, the USB stack ignores the value of <b>bRequest</b> and inserts a value of 0x06. This value indicates a request of <b>GET_DESCRIPTOR</b>. For more information about this member see Universal Serial Bus Specification.</p>
</dd>

### -field <b>wValue</b>

<dd>
<p>On input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537310">IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION</a> I/O control request, the caller should specify the type of descriptor to retrieve in the high byte of <b>wValue</b> and the descriptor index in the low byte. The following table lists the possible descriptor types.</p>
<table>
<tr>
<th>Descriptor type</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>USB_DEVICE_DESCRIPTOR_TYPE</p>
</td>
<td>
<p>Instructs the USB stack to return the device descriptor.</p>
</td>
</tr>
<tr>
<td>
<p>USB_CONFIGURATION_DESCRIPTOR_TYPE</p>
</td>
<td>
<p>Instructs the USB stack to return the configuration descriptor and all interface, endpoint, class-specific, and vendor-specific descriptors associated with the current configuration.. </p>
</td>
</tr>
<tr>
<td>
<p>USB_STRING_DESCRIPTOR_TYPE</p>
</td>
<td>
<p>Instructs the USB stack to return the indicated string descriptor.</p>
</td>
</tr>
<tr>
<td>
<p>USB_INTERFACE_DESCRIPTOR_TYPE</p>
</td>
<td>
<p>Instructs the USB stack to return the indicated interface descriptor.</p>
</td>
</tr>
<tr>
<td>
<p>USB_ENDPOINT_DESCRIPTOR_TYPE</p>
</td>
<td>
<p>Instructs the USB stack to return the indicated endpoint descriptor.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>wIndex</b>

<dd>
<p>The device-specific index of the descriptor that is to be retrieved. For more information about this member, see Universal Serial Bus Specification.</p>
</dd>

### -field <b>wLength</b>

<dd>
<p>The length of the data that is transferred during the second phase of the control transfer. For more information about this member, see Universal Serial Bus Specification.</p>
</dd>
</dl>
</dd>

### -field <b>Data</b>

<dd>
<p>On output from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537310">IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION</a> I/O control request, this member contains the retrieved descriptors.</p>
</dd>
</dl>

## -remarks
<p>If the caller specifies a value of USB_CONFIGURATION_DESCRIPTOR_TYPE in the <b>wValue</b> member, the output buffer must be large enough to hold all of the descriptors that are associated with the current configuration, or the request will fail.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537310">IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_DESCRIPTOR_REQUEST structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
