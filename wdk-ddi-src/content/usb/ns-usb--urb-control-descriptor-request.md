---
UID: NS.usb._URB_CONTROL_DESCRIPTOR_REQUEST
title: URB_CONTROL_DESCRIPTOR_REQUEST
author: windows-driver-content
description: The _URB_CONTROL_DESCRIPTOR_REQUEST structure is used by USB client drivers to get or set descriptors on a USB device.
old-location: buses\_urb_control_descriptor_request.htm
old-project: usbref
ms.assetid: 770659f4-701f-47dc-b20f-e51c85cdee4b
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: URB_CONTROL_DESCRIPTOR_REQUEST,
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
req.alt-api: _URB_CONTROL_DESCRIPTOR_REQUEST
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

# URB_CONTROL_DESCRIPTOR_REQUEST structure



## -description
<p>The <b>_URB_CONTROL_DESCRIPTOR_REQUEST</b> structure is used by USB client drivers to get or set descriptors on a USB device.</p>


## -syntax

````
struct _URB_CONTROL_DESCRIPTOR_REQUEST {
  struct URB_HEADER  Hdr;
  PVOID               Reserved;
  ULONG               Reserved0;
  ULONG               TransferBufferLength;
  PVOID               TransferBuffer;
  PMDL                TransferBufferMDL;
  struct URB  *UrbLink;
  struct URB_HCD_AREA  hca;
  USHORT              Reserved1;
  UCHAR               Index;
  UCHAR               DescriptorType;
  USHORT              LanguageId;
  USHORT              Reserved2;
};
````


## -struct-fields
<dl>

### -field <b>Hdr</b>

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540409">_URB_HEADER</a> structure that specifies the URB header information. <b>Hdr.Function</b> must be one of the following:</p>
<dl>
<dd>URB_FUNCTION_GET_DESCRIPTOR_FROM_DEVICE</dd>
<dd>URB_FUNCTION_GET_DESCRIPTOR_FROM_ENDPOINT</dd>
<dd>URB_FUNCTION_GET_DESCRIPTOR_FROM_INTERFACE</dd>
<dd>URB_FUNCTION_SET_DESCRIPTOR_TO_DEVICE</dd>
<dd>URB_FUNCTION_SET_DESCRIPTOR_TO_ENDPOINT</dd>
<dd>URB_FUNCTION_SET_DESCRIPTOR_TO_INTERFACE</dd>
</dl>
<p><b>Hdr.Length</b> must equal <code>sizeof(_URB_CONTROL_DESCRIPTOR_REQUEST)</code>.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>Reserved0</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>TransferBufferLength</b>

<dd>
<p>Specifies the length, in bytes, of the buffer specified in <b>TransferBuffer</b> or described in <b>TransferBufferMDL</b>. The host controller driver returns the number of bytes sent to or read from the pipe in this member.</p>
</dd>

### -field <b>TransferBuffer</b>

<dd>
<p>Pointer to a resident buffer for the transfer or is <b>NULL</b> if an MDL is supplied in <b>TransferBufferMDL</b>.</p>
</dd>

### -field <b>TransferBufferMDL</b>

<dd>
<p>Pointer to an MDL that describes a resident buffer or is <b>NULL</b> if a buffer is supplied in <b>TransferBuffer</b>. This MDL must be allocated from nonpaged pool.</p>
</dd>

### -field <b>UrbLink</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>hca</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>Index</b>

<dd>
<p>Specifies the device-defined index of the descriptor that is being retrieved or set.</p>
</dd>

### -field <b>DescriptorType</b>

<dd>
<p>Indicates what type of descriptor is being retrieved or set. One of the following values must be specified:</p>
<dl>
<dd>USB_DEVICE_DESCRIPTOR_TYPE</dd>
<dd>USB_CONFIGURATION_DESCRIPTOR_TYPE</dd>
<dd>USB_STRING_DESCRIPTOR_TYPE</dd>
</dl>
</dd>

### -field <b>LanguageId</b>

<dd>
<p>Specifies the language ID of the descriptor to be retrieved when USB_STRING_DESCRIPTOR_TYPE is set in <b>DescriptorType</b>. This member must be set to zero for any other value in <b>DescriptorType</b>.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>
</dl>

## -remarks
<p>Drivers can use the <b>UsbBuildGetDescriptorRequest</b> service routine to format this URB. If the caller passes a buffer too small to hold all of the data, the bus driver truncates the data to fit in the buffer without error.</p>

<p>When the caller requests the device descriptor, the bus driver returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539280">USB_DEVICE_DESCRIPTOR</a> data structure.</p>

<p>When the caller requests a configuration descriptor, the bus driver returns the configuration descriptor in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539241">USB_CONFIGURATION_DESCRIPTOR</a> structure, followed by the interface and endpoint descriptors for that configuration. The driver can access the interface and endpoint descriptors as <a href="https://msdn.microsoft.com/library/windows/hardware/ff540065">USB_INTERFACE_DESCRIPTOR</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff539317">USB_ENDPOINT_DESCRIPTOR</a> structures. The bus driver also returns any class-specific or device-specific descriptors. The system provides the <a href="https://msdn.microsoft.com/library/windows/hardware/ff539102">USBD_ParseConfigurationDescriptorEx</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff539109">USBD_ParseDescriptors</a> service routines to find individual descriptors within the buffer.</p>

<p>When the caller requests a string descriptor, the bus driver returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540147">USB_STRING_DESCRIPTOR</a> structure. The string itself is found in the variable-length <b>bString</b> member of the string descriptor.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540409">_URB_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539241">USB_CONFIGURATION_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539280">USB_DEVICE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539317">USB_ENDPOINT_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540065">USB_INTERFACE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540147">USB_STRING_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20_URB_CONTROL_DESCRIPTOR_REQUEST structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
