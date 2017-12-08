---
UID: NS.usb._USBD_ISO_PACKET_DESCRIPTOR
title: USBD_ISO_PACKET_DESCRIPTOR
author: windows-driver-content
description: The USBD_ISO_PACKET_DESCRIPTOR structure is used by USB client drivers to describe an isochronous transfer packet.
old-location: buses\usbd_iso_packet_descriptor.htm
old-project: usbref
ms.assetid: 45ceff8e-a013-45de-be2e-42c6ca30147e
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBD_ISO_PACKET_DESCRIPTOR, USBD_ISO_PACKET_DESCRIPTOR, *PUSBD_ISO_PACKET_DESCRIPTOR
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
req.alt-api: USBD_ISO_PACKET_DESCRIPTOR
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

# USBD_ISO_PACKET_DESCRIPTOR structure



## -description
<p>The <b>USBD_ISO_PACKET_DESCRIPTOR</b>   structure is used by USB client drivers to describe an isochronous transfer packet.</p>


## -syntax

````
typedef struct _USBD_ISO_PACKET_DESCRIPTOR {
  ULONG       Offset;
  ULONG       Length;
  USBD_STATUS Status;
} USBD_ISO_PACKET_DESCRIPTOR, *PUSBD_ISO_PACKET_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field Offset

<dd>
<p>Specifies the offset, in bytes, of the buffer for this packet from the beginning of the entire isochronous transfer buffer.</p>
</dd>

### -field Length

<dd>
<p> Set by the host controller to indicate the actual number of bytes received from the device for isochronous IN transfers. <b>Length</b> not used for isochronous OUT transfers.</p>
</dd>

### -field Status

<dd>
<p>Contains the status, on return from the host controller driver, of this transfer packet.</p>
</dd>
</dl>

## -remarks
<p>This structure is used as part of an isochronous transfer request to the host controller driver using the <a href="buses._urb_isoch_transfer">_URB_ISOCH_TRANSFER</a> structure. The <b>Offset</b> member contains the offset from the beginning of the <b>TransferBuffer</b> or <b>TransferBufferMDL</b> members of  <b>_URB_ISOCH_TRANSFER</b>.</p>

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
<a href="..\usbdlib\nf-usbdlib-usbd-isochurballocate.md">USBD_IsochUrbAllocate</a>
</dt>
<dt>
<a href="buses._urb_isoch_transfer">_URB_ISOCH_TRANSFER</a>
</dt>
<dt>
<a href="buses.transfer_data_to_isochronous_endpoints">How to Transfer Data to USB Isochronous Endpoints</a>
</dt>
<dt>
<a href="buses.usb_structures_and_enumerations">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBD_ISO_PACKET_DESCRIPTOR structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
