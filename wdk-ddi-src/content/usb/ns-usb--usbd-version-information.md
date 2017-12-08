---
UID: NS.usb._USBD_VERSION_INFORMATION
title: USBD_VERSION_INFORMATION
author: windows-driver-content
description: The USBD_VERSION_INFORMATION structure is used by the GetUSBDIVersion function to report its output data.
old-location: buses\usbd_version_information.htm
old-project: usbref
ms.assetid: 37dc1e94-18cb-48d5-81a2-74d03cef4d5d
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBD_VERSION_INFORMATION, USBD_VERSION_INFORMATION, *PUSBD_VERSION_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usb.h
req.include-header: Usbbusif.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBD_VERSION_INFORMATION
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

# USBD_VERSION_INFORMATION structure



## -description
<p>The <b>USBD_VERSION_INFORMATION</b> structure is used by the <a href="buses.getusbdiversion">GetUSBDIVersion</a> function to report its output data.</p>


## -syntax

````
typedef struct _USBD_VERSION_INFORMATION {
  ULONG USBDI_Version;
  ULONG Supported_USB_Version;
} USBD_VERSION_INFORMATION, *PUSBD_VERSION_INFORMATION;
````


## -struct-fields
<dl>

### -field USBDI_Version

<dd>
<p>Contains a binary-coded decimal USB interface version number. Released interface versions are listed in the following table.</p>
<table>
<tr>
<th>Operating system</th>
<th>Interface version</th>
</tr>
<tr>
<td>
<p>Windows 98 Gold</p>
</td>
<td>
<p>0x00000102</p>
</td>
</tr>
<tr>
<td>
<p>Windows 98 SE</p>
</td>
<td>
<p>0x00000200</p>
</td>
</tr>
<tr>
<td>
<p>Windows 2000</p>
</td>
<td>
<p>0x00000300</p>
</td>
</tr>
<tr>
<td>
<p>Windows Millennium Edition</p>
</td>
<td>
<p>0x00000400</p>
</td>
</tr>
<tr>
<td>
<p>Windows XP</p>
</td>
<td>
<p>0x00000500</p>
</td>
</tr>
<tr>
<td>
<p>Windows Vista</p>
<p>Windows 7</p>
<p>Windows 8</p>
</td>
<td>
<p>0x00000600</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Supported_USB_Version

<dd>
<p>Contains a binary-coded decimal USB specification version number. </p>
</dd>
</dl>

## -remarks
<p>
<a href="buses.getusbdiversion">GetUSBDIVersion</a> is deprecated in Windows 8 and later versions of the operating system. To determine whether a particular  version is supported by the underlying USB driver stack, the client driver must call <a href="..\usbdlib\nf-usbdlib-usbd-isinterfaceversionsupported.md">USBD_IsInterfaceVersionSupported</a>.  </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usb.h (include Usbbusif.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.getusbdiversion">GetUSBDIVersion</a>
</dt>
<dt>
<a href="buses.usb_interfaces">USB Bus Driver Interface (USBDI) Routines</a>
</dt>
<dt>
<a href="buses.usb_structures_and_enumerations">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBD_VERSION_INFORMATION structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
