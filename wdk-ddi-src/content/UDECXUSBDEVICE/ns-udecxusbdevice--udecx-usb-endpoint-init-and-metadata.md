---
UID: NS.udecxusbdevice._UDECX_USB_ENDPOINT_INIT_AND_METADATA
title: UDECX_USB_ENDPOINT_INIT_AND_METADATA
author: windows-driver-content
description: Contains the descriptors supported by an endpoint of a virtual USB device.
old-location: buses\udecx_usb_endpoint_init_and_metadata.htm
ms.assetid: B68FD95B-E7B8-4748-A1D0-09A1F9763626
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: usbref
req.header: udecxusbdevice.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UDECX_USB_ENDPOINT_INIT_AND_METADATA
req.alt-loc: UdecxUsbDevice.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: UDECX_USB_ENDPOINT_INIT_AND_METADATA, UDECX_USB_ENDPOINT_INIT_AND_METADATA, *PUDECX_USB_ENDPOINT_INIT_AND_METADATA
req.iface: 
req.product: Windows 10 or later.
---

# UDECX_USB_ENDPOINT_INIT_AND_METADATA structure



## -description
<p>Contains the descriptors supported by an endpoint of a virtual USB device.</p>


## -syntax

````
typedef struct _UDECX_USB_ENDPOINT_INIT_AND_METADATA {
  PUDECXUSBENDPOINT_INIT                                                                UdecxUsbEndpointInit;
   _Field_range_(sizeof(USB_ENDPOINT_DESCRIPTOR), 0xff) ULONG                           EndpointDescriptorBufferLength;
  _Notnull_ _Field_size_bytes_(EndpointDescriptorBufferLength) PUSB_ENDPOINT_DESCRIPTOR EndpointDescriptor;
  _Maybenull_ PUSB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR                             SuperSpeedEndpointCompanionDescriptor;
} UDECX_USB_ENDPOINT_INIT_AND_METADATA, *PUDECX_USB_ENDPOINT_INIT_AND_METADATA;
````


## -struct-fields
<dl>

### -field <b>UdecxUsbEndpointInit</b>

<dd>
<p>A pointer to a <b>UDECXUSBDEVICE_INIT</b> structure that contains initialization parameters for the virtual USB device. The client driver retrieved this pointer in the previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt627968">UdecxUsbDeviceInitAllocate</a>.</p>
</dd>

### -field <b>EndpointDescriptorBufferLength</b>

<dd>
<p>The length of the endpoint descriptor.</p>
</dd>

### -field <b>EndpointDescriptor</b>

<dd>
<p>Required. A buffer containing the endpoint descriptor. The descriptor is described in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539317">USB_ENDPOINT_DESCRIPTOR</a> structure.</p>
</dd>

### -field <b>SuperSpeedEndpointCompanionDescriptor</b>

<dd>
<p>Optional. A USB-defined SuperSpeed Endpoint Companion descriptor. For more information, see section 9.6.7 and Table 9-20 in the official USB 3.0 specification. The descriptor is described in a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406269">USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR</a> structure.</p>
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
<dt>UdecxUsbDevice.h (include Udecx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt595914">EVT_UDECX_USB_DEVICE_ENDPOINT_ADD</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UDECX_USB_ENDPOINT_INIT_AND_METADATA structure%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
