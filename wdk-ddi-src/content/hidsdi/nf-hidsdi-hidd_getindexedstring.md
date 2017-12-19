---
UID: NF.hidsdi.HidD_GetIndexedString
title: HidD_GetIndexedString function
author: windows-driver-content
description: The HidD_GetIndexedString routine returns a specified embedded string from a top-level collection.
old-location: hid\hidd_getindexedstring.htm
old-project: hid
ms.assetid: 4d500597-8ac7-41ea-aa2a-6e8d559e0282
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: HidD_GetIndexedString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: hidsdi.h
req.include-header: Hidsdi.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HidD_GetIndexedString
req.alt-loc: Hid.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hid.lib
req.dll: Hid.dll
req.irql: 
---

# HidD_GetIndexedString function



## -description
The <b>HidD_GetIndexedString</b> routine returns a specified embedded string from a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection</a>.



## -syntax

````
BOOLEAN __stdcall HidD_GetIndexedString(
  _In_  HANDLE HidDeviceObject,
  _In_  ULONG  StringIndex,
  _Out_ PVOID  Buffer,
  _In_  ULONG  BufferLength
);
````


## -parameters

### -param HidDeviceObject [in]

Specifies an open handle to a top-level collection.


### -param StringIndex [in]

Specifies the device-specific index of an embedded string.


### -param Buffer [out]

Pointer to a caller-allocated buffer that the routine uses to return the embedded string specified by <i>StringIndex</i>. The routine returns a NULL-terminated wide character string in a human-readable format.


### -param BufferLength [in]

Specifies the length, in bytes, of a caller-allocated buffer provided at <i>Buffer</i>. If the buffer is not large enough to return the entire NULL-terminated embedded string, the routine returns nothing in the buffer.


## -returns
<b>HidD_GetIndexedString</b> returns <b>TRUE</b> if it successfully returns the entire NULL-terminated embedded string. Otherwise, the routine returns <b>FALSE</b>.


## -remarks
Only user-mode applications can call <b>HidD_GetIndexedString</b>. Kernel-mode drivers can use an <a href="..\hidclass\ni-hidclass-ioctl_hid_get_indexed_string.md">IOCTL_HID_GET_INDEXED_STRING</a> request.

The maximum possible number of characters in an embedded string is device specific. For USB devices, the maximum string length is 126 wide characters (not including the terminating NULL character). 

The <b>iProduct</b> member of a <a href="buses.usb_device_descriptor">USB_DEVICE_DESCRIPTOR</a> structure for a particular interface is set by the <a href="buses.usb_common_class_generic_parent_driver">USB common class generic parent driver</a> based on the following rules:

If the <b>iInterface</b> member of the <a href="buses.usb_interface_descriptor">USB_INTERFACE_DESCRIPTOR</a> structure for the interface is nonzero, the <b>iProduct</b> member of the USB_DEVICE_DESCRIPTOR structure for the interface is set to the <b>iInterface</b> member of the USB_INTERFACE_DESCRIPTOR structure.

If the interface is grouped by a <a href="buses.usb_interface_association_descriptor">USB interface association descriptor</a>, and the <b>iFunction</b> member of the interface association descriptor for the interface is nonzero, the <b>iProduct</b> member of the USB_DEVICE_DESCRIPTOR structure for the interface is set to the <b>iFunction</b> member of the interface association descriptor.

For more information, see <a href="https://msdn.microsoft.com/2d3efb38-4eba-43db-8cff-9fac30209952">HID Collections</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows 2000 and later versions of Windows.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Hidsdi.h (include Hidsdi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Hid.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Hid.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="hid.hidd_getmanufacturerstring">HidD_GetManufacturerString</a>
</dt>
<dt>
<a href="hid.hidd_getphysicaldescriptor">HidD_GetPhysicalDescriptor</a>
</dt>
<dt>
<a href="hid.hidd_getproductstring">HidD_GetProductString</a>
</dt>
<dt>
<a href="hid.hidd_getserialnumberstring">HidD_GetSerialNumberString</a>
</dt>
<dt>
<a href="..\hidclass\ni-hidclass-ioctl_hid_get_indexed_string.md">IOCTL_HID_GET_INDEXED_STRING</a>
</dt>
<dt>
<a href="..\hidclass\ni-hidclass-ioctl_hid_get_manufacturer_string.md">IOCTL_HID_GET_MANUFACTURER_STRING</a>
</dt>
<dt>
<a href="..\hidclass\ni-hidclass-ioctl_hid_get_product_string.md">IOCTL_HID_GET_PRODUCT_STRING</a>
</dt>
<dt>
<a href="..\hidclass\ni-hidclass-ioctl_hid_get_serialnumber_string.md">IOCTL_HID_GET_SERIALNUMBER_STRING</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HidD_GetIndexedString routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

