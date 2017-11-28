---
UID: NS.ks.PKSATTRIBUTE
title: PKSATTRIBUTE
author: windows-driver-content
description: The KSATTRIBUTE structure defines an additional attribute of a data format or data range that is not covered by the KSDATAFORMAT and KSDATARANGE structures or the extended information based on the format and range specifiers.
old-location: stream\ksattribute.htm
old-project: stream
ms.assetid: 985d9f12-11c6-40e6-9cb6-572196bc04f4
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSATTRIBUTE, KSATTRIBUTE, *PKSATTRIBUTE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSATTRIBUTE
req.alt-loc: ks.h
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

# PKSATTRIBUTE structure



## -description
<p>The KSATTRIBUTE structure defines an additional attribute of a data format or data range that is not covered by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561656">KSDATAFORMAT</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a> structures or the extended information based on the format and range specifiers.</p>


## -syntax

````
typedef struct {
  ULONG Size;
  ULONG Flags;
  GUID  Attribute;
} KSATTRIBUTE, *PKSATTRIBUTE;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the size of the attribute. This is at least the size of the KSATTRIBUTE structure and may be more if there is extended information based on the identifying GUID in the <b>Attribute</b> field.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Specifies the flags of the attribute. The only used flag is KSATTRIBUTE_REQUIRED; this flag specifies that an attribute is required. If this flag is not set, the attribute is optional. Note that the topmost bit is reserved for internal use in KS.</p>
</dd>

### -field <b>Attribute</b>

<dd>
<p>Specifies the unique identifier of the attribute.</p>
</dd>
</dl>

## -remarks
<p>Note that KSATTRIBUTE is used in conjunction with data formats and data ranges; attributes on data formats and ranges are taken into consideration when determining if a data format is acceptable to a given pin or if a data range intersects with another data range.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561656">KSDATAFORMAT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSATTRIBUTE structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
