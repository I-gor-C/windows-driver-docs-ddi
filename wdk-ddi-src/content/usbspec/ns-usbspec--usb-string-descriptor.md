---
UID: NS.usbspec._USB_STRING_DESCRIPTOR
title: USB_STRING_DESCRIPTOR
author: windows-driver-content
description: The USB_STRING_DESCRIPTOR structure is used by USB client drivers to hold a USB-defined string descriptor.
old-location: buses\usb_string_descriptor.htm
old-project: usbref
ms.assetid: 20d76582-4138-4a45-940b-a8e9207946a5
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USB_STRING_DESCRIPTOR, USB_STRING_DESCRIPTOR, *PUSB_STRING_DESCRIPTOR
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
req.alt-api: USB_STRING_DESCRIPTOR
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

# USB_STRING_DESCRIPTOR structure



## -description
<p>The <b>USB_STRING_DESCRIPTOR</b> structure is used by USB client drivers to hold a USB-defined string descriptor.</p>


## -syntax

````
typedef struct _USB_STRING_DESCRIPTOR {
  UCHAR bLength;
  UCHAR bDescriptorType;
  WCHAR bString[1];
} USB_STRING_DESCRIPTOR, *PUSB_STRING_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>bLength</b>

<dd>
<p>Specifies the length, in bytes, of the descriptor.</p>
</dd>

### -field <b>bDescriptorType</b>

<dd>
<p>Specifies the descriptor type. Must always be USB_STRING_DESCRIPTOR_TYPE.</p>
</dd>

### -field <b>bString</b>

<dd>
<p>Pointer to a client-allocated buffer that contains, on return from the host controller driver, a Unicode string with the requested string descriptor.</p>
</dd>
</dl>

## -remarks
<p>This structure is used to hold a device, configuration, interface, class, vendor, endpoint, or device string descriptor. The string descriptor provides a human-readable description of the component.</p>

<p>Strings returned in <b>bString</b> are in Unicode format and the contents of the strings are device-defined.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538943">UsbBuildGetDescriptorRequest</a>
</dt>
<dt>
<a href="buses._urb_control_descriptor_request">_URB_CONTROL_DESCRIPTOR_REQUEST</a>
</dt>
<dt>
<a href="buses.usb_structures_and_enumerations">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_STRING_DESCRIPTOR structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
