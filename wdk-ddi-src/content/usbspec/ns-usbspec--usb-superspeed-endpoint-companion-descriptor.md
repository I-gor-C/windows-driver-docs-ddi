---
UID: NS.usbspec._USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR
title: USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR
author: windows-driver-content
description: The USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR structure is used by USB client drivers to retrieve a USB-defined SuperSpeed Endpoint Companion descriptor. For more information, see section 9.6.7 and Table 9-20 in the official USB 3.0 specification.
old-location: buses\usb_superspeed_endpoint_companion_descriptor.htm
old-project: usbref
ms.assetid: 725ADCA2-FE86-4131-8D70-2BF63F26F89D
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR, USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR, *PUSB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbspec.h
req.include-header: Usbspec.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR
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

# USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR structure



## -description
<p>The <b>USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR</b> structure is used by USB client drivers to retrieve a USB-defined SuperSpeed Endpoint Companion descriptor.

 For more information, see section 9.6.7 and Table 9-20 in the official USB 3.0 specification.</p>


## -syntax

````
typedef struct _USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR {
  UCHAR  bLength;
  UCHAR  bDescriptorType;
  UCHAR  bMaxBurst;
  union {
    UCHAR  AsUchar;
    struct {
      UCHAR MaxStreams  :5;
      UCHAR Reserved1  :3;
    } Bulk;
    struct {
      UCHAR Mult  :2;
      UCHAR Reserved2  :6;
    } Isochronous;
  } bmAttributes;
  USHORT wBytesPerInterval;
} USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR, *PUSB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>bLength</b>

<dd>
<p>Specifies the length, in bytes, of this descriptor.</p>
</dd>

### -field <b>bDescriptorType</b>

<dd>
<p>Specifies the descriptor type. Must be set to USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR.

</p>
</dd>

### -field <b>bMaxBurst</b>

<dd>
<p>Specifies the maximum number of packets that the endpoint can send or receive as a part of a burst.</p>
</dd>

### -field <b>bmAttributes</b>

<dd>
<dl>

### -field <b>AsUchar</b>

<dd>
<p>Specifies the length of the structures.</p>
</dd>

### -field <b>Bulk</b>

<dd>
<dl>

### -field <b>MaxStreams</b>

<dd>
<p>Specifies the maximum number of streams supported by the bulk endpoint.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>
</dl>
</dd>

### -field <b>Isochronous</b>

<dd>
<dl>

### -field <b>Mult</b>

<dd>
<p>Specifies a zero-based number that determines the maximum number of packets (bMaxBurst *  (Mult + 1)) that can be sent to the endpoint within a service interval.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>
</dl>
</dd>
</dl>
</dd>

### -field <b>wBytesPerInterval</b>

<dd>
<p>Number of bytes per interval.</p>
</dd>
</dl>

## -remarks
<p>A client driver that supports streams associated with a bulk endpoint, uses <b>USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR</b> to get the maximum number of streams supported by the endpoint. That information is required by the client driver in an open-streams request. In the request, the specified value for <b>NumberOfStreams</b> member of the <a href="buses._urb_open_basic_streams">_URB_OPEN_STATIC_STREAMS</a> structure cannot exceed the <b>MaxStreams</b> value reported in <b>USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR</b>. For more information about opening streams, see <a href="buses.how_to_open_streams_in_a_usb_endpoint">How to Open and Close Static Streams in a USB Bulk Endpoint</a>.</p>

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
<dt>Usbspec.h (include Usbspec.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.usb_structures_and_enumerations">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
