---
UID: NS.hidsdi._HIDD_ATTRIBUTES
title: HIDD_ATTRIBUTES
author: windows-driver-content
description: The HIDD_ATTRIBUTES structure contains vendor information about a HIDClass device.
old-location: hid\hidd_attributes.htm
old-project: hid
ms.assetid: 31bfa863-459f-4fb2-af41-2d40d0396dd7
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HIDD_ATTRIBUTES, HIDD_ATTRIBUTES, *PHIDD_ATTRIBUTES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hidsdi.h
req.include-header: Hidsdi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HIDD_ATTRIBUTES
req.alt-loc: hidsdi.h
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
---

# HIDD_ATTRIBUTES structure



## -description
<p>The HIDD_ATTRIBUTES structure contains vendor information about a HIDClass device.</p>


## -syntax

````
typedef struct _HIDD_ATTRIBUTES {
  ULONG  Size;
  USHORT VendorID;
  USHORT ProductID;
  USHORT VersionNumber;
} HIDD_ATTRIBUTES, *PHIDD_ATTRIBUTES;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>Specifies the size, in bytes, of a HIDD_ATTRIBUTES structure.</p>
</dd>

### -field VendorID

<dd>
<p>Specifies a HID device's vendor ID.</p>
</dd>

### -field ProductID

<dd>
<p>Specifies a HID device's product ID.</p>
</dd>

### -field VersionNumber

<dd>
<p>Specifies the manufacturer's revision number for a HIDClass device.</p>
</dd>
</dl>

## -remarks
<p>A caller of <a href="..\hidsdi\nf-hidsdi-hidd-getattributes.md">HidD_GetAttributes</a>, uses this structure to obtain a device's vendor information.</p>

<p>Before using a HIDD_ATTRIBUTES structure with <a href="hid.hidclass_support_routines">HIDClass support routines</a>, the caller must set the <b>Size</b> member.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hidsdi.h (include Hidsdi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\hidsdi\nf-hidsdi-hidd-getattributes.md">HidD_GetAttributes</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HIDD_ATTRIBUTES structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
