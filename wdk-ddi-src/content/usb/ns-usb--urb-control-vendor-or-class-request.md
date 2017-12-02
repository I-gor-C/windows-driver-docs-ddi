---
UID: NS.usb._URB_CONTROL_VENDOR_OR_CLASS_REQUEST
title: URB_CONTROL_VENDOR_OR_CLASS_REQUEST
author: windows-driver-content
description: The _URB_CONTROL_VENDOR_OR_CLASS_REQUEST structure is used by USB client drivers to issue a vendor or class-specific command to a device, interface, endpoint, or other device-defined target.
old-location: buses\_urb_control_vendor_or_class_request.htm
old-project: usbref
ms.assetid: 3d355489-cc70-4fa1-b08f-08ccf84f5490
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: URB_CONTROL_VENDOR_OR_CLASS_REQUEST,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usb.h
req.include-header: Usb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: _URB_CONTROL_VENDOR_OR_CLASS_REQUEST
req.alt-loc: usb.h
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
req.iface: 
req.product: Windows 10 or later.
---

# URB_CONTROL_VENDOR_OR_CLASS_REQUEST structure



## -description
<p>The <b>_URB_CONTROL_VENDOR_OR_CLASS_REQUEST</b> structure is used by USB client drivers to issue a vendor or class-specific command to a device, interface, endpoint, or other device-defined target.</p>


## -syntax

````
struct _URB_CONTROL_VENDOR_OR_CLASS_REQUEST {
  struct URB_HEADER  Hdr;
  PVOID               Reserved;
  ULONG               TransferFlags;
  ULONG               TransferBufferLength;
  PVOID               TransferBuffer;
  PMDL                TransferBufferMDL;
  struct URB  *UrbLink;
  struct URB_HCD_AREA  hca;
  UCHAR               RequestTypeReservedBits;
  UCHAR               Request;
  USHORT              Value;
  USHORT              Index;
  USHORT              Reserved1;
};
````


## -struct-fields
<dl>

### -field Hdr

<dd>
<p>Pointer to a <a href="buses._urb_header">_URB_HEADER</a> structure that specifies the URB header information. <b>Hdr.Function</b> must be one of URB_FUNCTION_CLASS_XXX or URB_FUNCTION_VENDOR_XXX GET_STATUS, and <b>Hdr.Length</b> must be <code>sizeof(_URB_CONTROL_VENDOR_OR_CLASS_REQUEST)</code>.</p>
</dd>

### -field Reserved

<dd>Reserved. Must be NULL.</dd>

### -field TransferFlags

<dd>
<p>
<p>Specifies zero, one, or a combination of the following flags:</p>
</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="USBD_TRANSFER_DIRECTION_IN"></a><a id="usbd_transfer_direction_in"></a><dl>

### -field USBD_TRANSFER_DIRECTION_IN

</dl>
</td>
<td width="60%">
<p>Is set to request data from a device. To transfer data to a device, this flag must be clear. The flag must be set if the pipe is an interrupt transfer pipe.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="USBD_SHORT_TRANSFER_OK"></a><a id="usbd_short_transfer_ok"></a><dl>

### -field USBD_SHORT_TRANSFER_OK

</dl>
</td>
<td width="60%">
<p>Is set to direct the host controller not to return an error when it receives a packet from the device that is shorter than the maximum packet size for the endpoint. The maximum packet size for the endpoint is reported in the <b>bMaxPacketSize0</b> member  of the <a href="..\usbspec\ns-usbspec--usb-device-descriptor.md">USB_DEVICE_DESCRIPTOR</a> structure (device descriptor) for the default control endpoint. For a non-default control endpoint,  maximum packet size  is set in the <b>wMaxPacketSize</b> member of the <a href="..\usbspec\ns-usbspec--usb-endpoint-descriptor.md">USB_ENDPOINT_DESCRIPTOR</a> structure (endpoint descriptor).</p>
<p>When the host controller receives a packet whose length is shorter than the <b>wMaxPacketSize</b> value on a control endpoint, the behavior is as follows depending on the type of host controller:<ul>
<li>On EHCI host controllers, the host controller proceeds immediately to the status phase of the control transfer.  The transfer completes successfully, regardless of whether USBD_SHORT_TRANSFER_OK is set.

</li>
<li>On UHCI and OHCI host controllers, if USBD_SHORT_TRANSFER_OK is set, the host controller proceeds to the status phase.  If USBD_SHORT_TRANSFER_OK is not set, the host controller abandons the data and status phases of the control transfer and the transfer completes with an error.
</li>
</ul>
</p>
<p>This flag should not be set unless USBD_TRANSFER_DIRECTION_IN is also set.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field TransferBufferLength

<dd>
<p>Specifies the length, in bytes, of the buffer specified in <b>TransferBuffer</b> or described in <b>TransferBufferMDL</b>. The host controller driver returns the number of bytes sent to or read from the pipe in this member.</p>
</dd>

### -field TransferBuffer

<dd>
<p>Pointer to a resident buffer for the transfer or is <b>NULL</b> if an MDL is supplied in <b>TransferBufferMDL</b>. The contents of this buffer depend on the value of <b>TransferFlags</b>. If USBD_TRANSFER_DIRECTION_IN is specified this buffer will contain data read from the device on return from the host controller driver. Otherwise, this buffer contains driver-supplied data for transfer to the device.</p>
</dd>

### -field TransferBufferMDL

<dd>
<p>Pointer to an MDL that describes a resident buffer or is <b>NULL</b> if a buffer is supplied in <b>TransferBuffer</b>. The contents of the buffer depend on the value of <b>TransferFlags</b>. If USBD_TRANSFER_DIRECTION_IN is specified, the described buffer will contain data read from the device on return from the host controller driver. Otherwise, the buffer contains driver-supplied data for transfer to the device. This MDL must be allocated from nonpaged pool.</p>
</dd>

### -field UrbLink

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field hca

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field RequestTypeReservedBits

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field Request

<dd>
<p>Specifies the USB or vendor-defined request code for the device, interface, endpoint, or other device-defined target.</p>
</dd>

### -field Value

<dd>
<p>Specifies a value, specific to <b>Request</b>, that becomes part of the USB-defined setup packet for the target. This value is defined by the creator of the code used in <b>Request</b>.</p>
</dd>

### -field Index

<dd>
<p>Specifies the device-defined index, returned by a successful configuration request, if the request is for an endpoint or interface. Otherwise, <b>Index</b> must be zero.</p>
</dd>

### -field Reserved1

<dd>
<p>Reserved. Do not use.</p>
</dd>
</dl>

## -remarks
<p>Drivers can use the <b>UsbBuildVendorRequest</b> service routine format this URB.</p>

<p>The reserved members of this structure must be treated as opaque and are reserved for system use.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usb.h (include Usb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\usb\ns-usb--urb.md">URB</a>
</dt>
<dt>
<a href="buses._urb_header">_URB_HEADER</a>
</dt>
<dt>
<a href="buses.usb_structures_and_enumerations">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20_URB_CONTROL_VENDOR_OR_CLASS_REQUEST structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
