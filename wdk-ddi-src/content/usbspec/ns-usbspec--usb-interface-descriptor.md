---
UID: NS.usbspec._USB_INTERFACE_DESCRIPTOR
title: USB_INTERFACE_DESCRIPTOR
author: windows-driver-content
description: The USB_INTERFACE_DESCRIPTOR structure is used by USB client drivers to retrieve a USB-defined interface descriptor.
old-location: buses\usb_interface_descriptor.htm
old-project: usbref
ms.assetid: 12378915-fa3d-4054-bb06-6eb8b292559c
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USB_INTERFACE_DESCRIPTOR, USB_INTERFACE_DESCRIPTOR, *PUSB_INTERFACE_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbspec.h
req.include-header: Usb100.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USB_INTERFACE_DESCRIPTOR
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

# USB_INTERFACE_DESCRIPTOR structure



## -description
<p>The <b>USB_INTERFACE_DESCRIPTOR</b> structure is used by USB client drivers to retrieve a USB-defined interface descriptor.</p>


## -syntax

````
typedef struct _USB_INTERFACE_DESCRIPTOR {
  UCHAR bLength;
  UCHAR bDescriptorType;
  UCHAR bInterfaceNumber;
  UCHAR bAlternateSetting;
  UCHAR bNumEndpoints;
  UCHAR bInterfaceClass;
  UCHAR bInterfaceSubClass;
  UCHAR bInterfaceProtocol;
  UCHAR iInterface;
} USB_INTERFACE_DESCRIPTOR, *PUSB_INTERFACE_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>bLength</b>

<dd>
<p>The length, in bytes, of the descriptor.</p>
</dd>

### -field <b>bDescriptorType</b>

<dd>
<p>The descriptor type. <b>bDescriptor</b> must be set to USB_INTERFACE_DESCRIPTOR_TYPE.</p>
</dd>

### -field <b>bInterfaceNumber</b>

<dd>
<p>The index number of the interface.</p>
</dd>

### -field <b>bAlternateSetting</b>

<dd>
<p>The index number of the alternate setting of the interface.</p>
</dd>

### -field <b>bNumEndpoints</b>

<dd>
<p>The number of endpoints that are used by the interface, excluding the default status endpoint.</p>
</dd>

### -field <b>bInterfaceClass</b>

<dd>
<p>The class code of the device that the USB specification group assigned.</p>
</dd>

### -field <b>bInterfaceSubClass</b>

<dd>
<p>The subclass code of the device that the USB specification group assigned.</p>
</dd>

### -field <b>bInterfaceProtocol</b>

<dd>
<p>The protocol code of the device that the USB specification group assigned.</p>
</dd>

### -field <b>iInterface</b>

<dd>
<p>The index of a string descriptor that describes the interface. For information about this field, see section 9.6.5 in the "Universal Serial Bus Revision 2.0" specification  at <a href="http://www.usb.org/developers/docs/">USB Technology</a>.</p>
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
<dt>Usbspec.h (include Usb100.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538943">UsbBuildGetDescriptorRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540357">_URB_CONTROL_DESCRIPTOR_REQUEST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_INTERFACE_DESCRIPTOR structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
