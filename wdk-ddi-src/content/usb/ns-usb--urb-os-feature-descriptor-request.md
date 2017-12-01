---
UID: NS.usb._URB_OS_FEATURE_DESCRIPTOR_REQUEST
title: URB_OS_FEATURE_DESCRIPTOR_REQUEST
author: windows-driver-content
description: The _URB_OS_FEATURE_DESCRIPTOR_REQUEST structure is used by the USB hub driver to retrieve Microsoft OS Feature Descriptors from a USB device or an interface on a USB device.
old-location: buses\_urb_os_feature_descriptor_request.htm
old-project: usbref
ms.assetid: 9ff62523-e9e3-4f32-802f-6fee0082d925
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: URB_OS_FEATURE_DESCRIPTOR_REQUEST,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usb.h
req.include-header: Usb.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows XP and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: _URB_OS_FEATURE_DESCRIPTOR_REQUEST
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

# URB_OS_FEATURE_DESCRIPTOR_REQUEST structure



## -description
<p>The <b>_URB_OS_FEATURE_DESCRIPTOR_REQUEST</b> structure is used by the USB hub driver to retrieve Microsoft OS Feature Descriptors from a USB device or an interface on a USB device.</p>


## -syntax

````
struct _URB_OS_FEATURE_DESCRIPTOR_REQUEST {
  _URB_HEADER  Hdr;
  ULONG       TransferBufferLength;
  PVOID       TransferBuffer;
  PMDL        TransferBufferMDL;
  struct URB  *UrbLink;
  UCHAR       Recipient;
  UCHAR       InterfaceNumber;
  UCHAR       MS_PageIndex;
  USHORT      MS_FeatureDescriptorIndex;
};
````


## -struct-fields
<dl>

### -field <b> Hdr</b>

<dd>
<p>Pointer to a <a href="buses._urb_header">_URB_HEADER</a> structure that specifies the URB header information. <b>Hdr.Function</b> must URB_FUNCTION_GET_MS_FEATURE_DESCRIPTOR.
<b>Hdr.Length</b> must be <code>sizeof(_URB_OS_FEATURE_DESCRIPTOR_REQUEST)</code>.
</p>
</dd>

### -field <b>TransferBufferLength</b>

<dd>
<p>Specifies the length, in bytes, of the buffer specified in <b>TransferBuffer</b> or described in <b>TransferBufferMDL</b>. The host controller driver returns the number of bytes read in this member.  Current implementation of this function limits the maximum MS OS Feature Descriptor size to 4 Kilobytes.</p>
</dd>

### -field <b>TransferBuffer</b>

<dd>
<p>Pointer to a resident buffer for the transfer or is <b>NULL</b> if an MDL is supplied in <b>TransferBufferMDL</b>. </p>
</dd>

### -field <b>TransferBufferMDL</b>

<dd>
<p>Pointer to an MDL that describes a resident buffer or is <b>NULL</b> if a buffer is supplied in <b>TransferBuffer</b>. This MDL must be allocated from nonpaged pool.</p>
</dd>

### -field <b>UrbLink</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>Recipient</b>

<dd>
<p>Specifies whether the recipient is the USB device or an interface on the USB device.  One of the following values must be specified:</p>
<ul>
<li>0 indicates that the USB device is the recipient of the request.
</li>
<li>1 indicates that a USB interface is the recipient of the request. 
</li>
<li>2 indicates that a USB endpoint is the recipient of the request. 
</li>
</ul>
</dd>

### -field <b>InterfaceNumber</b>

<dd>
<p>Indicates the interface number that is the recipient of the request, if the <b>Recipient</b> member value is 1. Must be set to 0 if the USB device is the recipient.</p>
</dd>

### -field <b>MS_PageIndex</b>

<dd>
<p>Must be set to 0. Page index of the 64K page of the MS OS Feature Descriptor to be returned.  Current implementation only supports a maximum descriptor size of 4K.</p>
</dd>

### -field <b>MS_FeatureDescriptorIndex</b>

<dd>
<p>Index for MS OS Feature Descriptor to be requested.</p>
</dd>
</dl>

## -remarks
<p>The reserved members of this structure must be treated as opaque and are reserved for system use.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP and later operating systems.</p>
</td>
</tr>
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
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20_URB_OS_FEATURE_DESCRIPTOR_REQUEST structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
