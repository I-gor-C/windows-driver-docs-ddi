---
UID: NS.prntfont._GLYPHRUN
title: GLYPHRUN
author: windows-driver-content
description: The GLYPHRUN structure is one of the structures used to define the contents of glyph translation table files (.gtt files).
old-location: print\glyphrun.htm
old-project: print
ms.assetid: 21f6631c-dff1-459f-a83e-7aa1d5d2ab2b
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: GLYPHRUN, GLYPHRUN, *PGLYPHRUN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: prntfont.h
req.include-header: Prntfont.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GLYPHRUN
req.alt-loc: prntfont.h
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
req.product: Windows 10 or later.
---

# GLYPHRUN structure



## -description
<p>The GLYPHRUN structure is one of the structures used to define the contents of <a href="print.customized_font_management#ddk_glyph_translation_table_files_gg#ddk_glyph_translation_table_files_gg">glyph translation table files</a> (.gtt files).</p>


## -syntax

````
typedef struct _GLYPHRUN {
  WCHAR wcLow;
  WORD  wGlyphCount;
} GLYPHRUN, *PGLYPHRUN;
````


## -struct-fields
<dl>

### -field <b>wcLow</b>

<dd>
<p>Specifies a Unicode value representing the first glyph in the glyph run.</p>
</dd>

### -field <b>wGlyphCount</b>

<dd>
<p>Specifies the number of glyphs represented by the glyph run.</p>
</dd>
</dl>

## -remarks
<p>A .gtt (glyph translation table) file contains an array of GLYPHRUN structures. Each structure identifies a set of Unicode values for which the printer provides glyphs. The array is described by the <b>IoRunOffset</b> and <b>dwRunCount</b> members of a .gtt file's <a href="https://msdn.microsoft.com/library/windows/hardware/ff563597">UNI_GLYPHSETDATA</a> structure.</p>

<p>The GLYPHRUN structures must be defined in ascending order, based on the value of <b>wcLow</b>. Unidrv uses the GLYPHRUN array to generate glyph handles. Unidrv stores these glyph handles in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570578">WCRUN</a> array within an <a href="https://msdn.microsoft.com/library/windows/hardware/ff565625">FD_GLYPHSET</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Prntfont.h (include Prntfont.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563597">UNI_GLYPHSETDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570578">WCRUN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565625">FD_GLYPHSET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20GLYPHRUN structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
