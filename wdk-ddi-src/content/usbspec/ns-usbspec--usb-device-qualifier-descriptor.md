---
UID: NS.usbspec._USB_DEVICE_QUALIFIER_DESCRIPTOR
title: USB_DEVICE_QUALIFIER_DESCRIPTOR
author: windows-driver-content
description: The USB_DEVICE_QUALIFIER_DESCRIPTOR structure is used by USB client drivers to retrieve a USB-defined device qualifier descriptor.
old-location: buses\usb_device_qualifier_descriptor.htm
old-project: usbref
ms.assetid: f96e4305-ec07-4df8-8fdf-f840598dd938
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USB_DEVICE_QUALIFIER_DESCRIPTOR, USB_DEVICE_QUALIFIER_DESCRIPTOR, *PUSB_DEVICE_QUALIFIER_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbspec.h
req.include-header: Usb200.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USB_DEVICE_QUALIFIER_DESCRIPTOR
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

# USB_DEVICE_QUALIFIER_DESCRIPTOR structure



## -description
<p>The <b>USB_DEVICE_QUALIFIER_DESCRIPTOR</b> structure is used by USB client drivers to retrieve a USB-defined device qualifier descriptor.</p>


## -syntax

````
typedef struct _USB_DEVICE_QUALIFIER_DESCRIPTOR {
  UCHAR  bLength;
  UCHAR  bDescriptorType;
  USHORT bcdUSB;
  UCHAR  bDeviceClass;
  UCHAR  bDeviceSubClass;
  UCHAR  bDeviceProtocol;
  UCHAR  bMaxPacketSize0;
  UCHAR  bNumConfigurations;
  UCHAR  bReserved;
} USB_DEVICE_QUALIFIER_DESCRIPTOR, *PUSB_DEVICE_QUALIFIER_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>bLength</b>

<dd>
<p>Specifies the length, in bytes, of this descriptor.</p>
</dd>

### -field <b>bDescriptorType</b>

<dd>
<p>Specifies the descriptor type. Must be set to <b>USB_DEVICE_QUALIFIER_DESCRIPTOR_TYPE</b>.</p>
</dd>

### -field <b>bcdUSB</b>

<dd>
<p>Identifies the version of the USB specification that this descriptor structure complies with. This value is a binary-coded decimal number.</p>
</dd>

### -field <b>bDeviceClass</b>

<dd>
<p>Specifies the class code of the device as assigned by the USB specification group.</p>
</dd>

### -field <b>bDeviceSubClass</b>

<dd>
<p>Specifies the subclass code of the device as assigned by the USB specification group.</p>
</dd>

### -field <b>bDeviceProtocol</b>

<dd>
<p>Specifies the protocol code of the device as assigned by the USB specification group.</p>
</dd>

### -field <b>bMaxPacketSize0</b>

<dd>
<p>Specifies the maximum packet size, in bytes, for endpoint zero of the device. The value must be set to 8, 16, 32, or 64.</p>
</dd>

### -field <b>bNumConfigurations</b>

<dd>
<p>Specifies the total number of possible configurations for the device.</p>
</dd>

### -field <b>bReserved</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>

## -remarks
<p>This structure is similar to <a href="..\usbspec\ns-usbspec--usb-device-descriptor.md">USB_DEVICE_DESCRIPTOR</a>, but it contains only those members that can change when the device switches from full-speed operation to high-speed operation or vice versa. If the device is operating at full speed, querying for this descriptor will contain information about how the device would operate at high-speed. If, on the other hand, the device is operating at high-speed, this descriptor will contain information about how the device would operate at full-speed.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbspec.h (include Usb200.h)</dt>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_DEVICE_QUALIFIER_DESCRIPTOR structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
