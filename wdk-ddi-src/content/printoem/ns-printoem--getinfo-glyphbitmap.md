---
UID: NS.printoem._GETINFO_GLYPHBITMAP
title: GETINFO_GLYPHBITMAP
author: windows-driver-content
description: The GETINFO_GLYPHBITMAP structure is used as input to the UNIFONTOBJ_GetInfo callback function.
old-location: print\getinfo_glyphbitmap.htm
old-project: print
ms.assetid: 6a5887fd-0269-4cd1-acf1-f7242016d993
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: GETINFO_GLYPHBITMAP, GETINFO_GLYPHBITMAP, *PGETINFO_GLYPHBITMAP
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
req.alt-api: GETINFO_GLYPHBITMAP
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

# GETINFO_GLYPHBITMAP structure



## -description
<p>The GETINFO_GLYPHBITMAP structure is used as input to the <a href="print.unifontobj_getinfo">UNIFONTOBJ_GetInfo</a> callback function.</p>


## -syntax

````
typedef struct _GETINFO_GLYPHBITMAP {
  DWORD     dwSize;
  HGLYPH    hGlyph;
  GLYPHDATA *pGlyphData;
} GETINFO_GLYPHBITMAP, *PGETINFO_GLYPHBITMAP;
````


## -struct-fields
<dl>

### -field <b>dwSize</b>

<dd>
<p>Specifies the size, in bytes, of the GETINFO_GLYPHBITMAP structure. Supplied by <a href="print.unifontobj_getinfo">UNIFONTOBJ_GetInfo</a> caller.</p>
</dd>

### -field <b>hGlyph</b>

<dd>
<p>Handle to the glyph. See the following Remarks section. Supplied by the <a href="print.unifontobj_getinfo">UNIFONTOBJ_GetInfo</a> caller.</p>
</dd>

### -field <b>pGlyphData</b>

<dd>
<p>Pointer to a <a href="display.glyphdata">GLYPHDATA</a> structure. The structure is filled in by Unidrv's <a href="print.unifontobj_getinfo">UNIFONTOBJ_GetInfo</a> callback function. The pointer is supplied by the <i>UNIFONTOBJ_GetInfo</i> caller.</p>
</dd>
</dl>

## -remarks
<p>To obtain a glyph bitmap, a rendering plug-in can supply the address of a GETINFO_GLYPHBITMAP structure when calling Unidrv's <a href="print.unifontobj_getinfo">UNIFONTOBJ_GetInfo</a> callback function.</p>

<p>The value that a rendering plug-in specifies for the <b>hGlyph</b> member must have been previously received as the <i>hGlyph</i> parameter to the <a href="print.iprintoemuni_downloadcharglyph">IPrintOemUni::DownloadCharGlyph</a> method.</p>

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
<dt>
<a href="display.glyphdata">GLYPHDATA</a>
</dt>
<dt>
<a href="print.iprintoemuni_downloadcharglyph">IPrintOemUni::DownloadCharGlyph</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20GETINFO_GLYPHBITMAP structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
