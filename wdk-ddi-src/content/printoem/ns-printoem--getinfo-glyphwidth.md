---
UID: NS.printoem._GETINFO_GLYPHWIDTH
title: GETINFO_GLYPHWIDTH
author: windows-driver-content
description: The GETINFO_GLYPHWIDTH structure is used as input to the UNIFONTOBJ_GetInfo callback function.
old-location: print\getinfo_glyphwidth.htm
old-project: print
ms.assetid: bc01b363-71e9-4c50-ad14-a101abbfe6ec
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: GETINFO_GLYPHWIDTH, GETINFO_GLYPHWIDTH, *PGETINFO_GLYPHWIDTH
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: printoem.h
req.include-header: Printoem.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GETINFO_GLYPHWIDTH
req.alt-loc: printoem.h
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
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# GETINFO_GLYPHWIDTH structure



## -description
<p>The GETINFO_GLYPHWIDTH structure is used as input to the <a href="print.unifontobj_getinfo">UNIFONTOBJ_GetInfo</a> callback function.</p>


## -syntax

````
typedef struct _GETINFO_GLYPHWIDTH {
  DWORD dwSize;
  DWORD dwType;
  DWORD dwCount;
  PVOID pGlyph;
  PLONG plWidth;
} GETINFO_GLYPHWIDTH, *PGETINFO_GLYPHWIDTH;
````


## -struct-fields
<dl>

### -field dwSize

<dd>
<p>Size, in bytes, of the GETINFO_GLYPHWIDTH structure. Supplied by the <a href="print.unifontobj_getinfo">UNIFONTOBJ_GetInfo</a> caller.</p>
</dd>

### -field dwType

<dd>
<p>Specifies the type of the glyph specifier array pointed to by <b>pGlyph</b>. Valid values are:</p>
<dl>
<dd>
<p>TYPE_GLYPHHANDLE</p>
</dd>
<dd>
<p>TYPE_GLYPHID</p>
</dd>
</dl>
<p>Supplied by the <a href="print.unifontobj_getinfo">UNIFONTOBJ_GetInfo</a> caller.</p>
</dd>

### -field dwCount

<dd>
<p>Specifies the number of elements in the array pointed to by <b>pGlyph</b>. Supplied by the <a href="print.unifontobj_getinfo">UNIFONTOBJ_GetInfo</a> caller.</p>
</dd>

### -field pGlyph

<dd>
<p>Pointer to an array of glyph specifiers. The array element type is indicated by <b>dwType</b>. Supplied by the <a href="print.unifontobj_getinfo">UNIFONTOBJ_GetInfo</a> caller.</p>
</dd>

### -field plWidth

<dd>
<p>Pointer to a location into which Unidrv's <a href="print.unifontobj_getinfo">UNIFONTOBJ_GetInfo</a> callback function places the width value. The pointer is supplied by the <i>UNIFONTOBJ_GetInfo</i> caller.</p>
</dd>
</dl>

## -remarks
<p>To obtain the width of a set of glyphs, a rendering plug-in can supply the address of a GETINFO_GLYPHWIDTH structure when calling Unidrv's <a href="print.unifontobj_getinfo">UNIFONTOBJ_GetInfo</a> callback function. The callback function calculates the total width of all the glyphs described by the input array, and places the calculated value in the location pointed to by <b>plWidth</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Printoem.h (include Printoem.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="print.unifontobj_getinfo">UNIFONTOBJ_GetInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20GETINFO_GLYPHWIDTH structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
