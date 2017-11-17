---
UID: NS.usbioctl._USB_ID_STRING
title: USB_ID_STRING
author: windows-driver-content
description: The USB_ID_STRING structure is used to store a string or multi-string.
old-location: buses\usb_id_string.htm
ms.assetid: e7af07ed-f1a7-4f66-8824-2e12492d037a
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: usbref
req.header: usbioctl.h
req.include-header: Usbioctl.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USB_ID_STRING
req.alt-loc: usbioctl.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: USB_ID_STRING, USB_ID_STRING, *PUSB_ID_STRING
req.iface: 
req.product: Windows 10 or later.
---

# USB_ID_STRING structure



## -description
<p>The <b>USB_ID_STRING</b> structure is used to store a string or multi-string.</p>


## -syntax

````
typedef struct _USB_ID_STRING {
  USHORT  LanguageId;
  ULONG   LengthInBytes;
  PWCHAR  Buffer;
} USB_ID_STRING, *PUSB_ID_STRING;
````


## -struct-fields
<dl>

### -field <b>LanguageId</b>

<dd>
<p>Indicates that language ID of the string.</p>
</dd>

### -field <b>LengthInBytes</b>

<dd>
<p>Indicates the length (in bytes) of the string pointed to by <b>Buffer</b>, including the terminating <b>NULL</b>. </p>
</dd>

### -field <b>Buffer</b>

<dd>
<p>Pointer to a string or multi-string.</p>
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
<p>Available in Windows Vista and later operating systems. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbioctl.h (include Usbioctl.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_ID_STRING structure%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
