---
UID: NS.prntfont._UFF_FONTDIRECTORY
title: UFF_FONTDIRECTORY
author: windows-driver-content
description: The UFF_FONTDIRECTORY structure is used to specify the directory of font descriptions contained in a Unidrv font format file (.uff file).
old-location: print\uff_fontdirectory.htm
old-project: print
ms.assetid: d1cde8a4-f27b-440c-bfb1-c9a564c59c04
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: UFF_FONTDIRECTORY, UFF_FONTDIRECTORY, *PUFF_FONTDIRECTORY
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
req.alt-api: UFF_FONTDIRECTORY
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

# UFF_FONTDIRECTORY structure



## -description
<p>The UFF_FONTDIRECTORY structure is used to specify the directory of font descriptions contained in a Unidrv font format file (.uff file).</p>


## -syntax

````
typedef struct _UFF_FONTDIRECTORY {
  DWORD dwSignature;
  WORD  wSize;
  WORD  wFontID;
  SHORT sGlyphID;
  WORD  wFlags;
  DWORD dwInstallerSig;
  DWORD offFontName;
  DWORD offCartridgeName;
  DWORD offFontData;
  DWORD offGlyphData;
  DWORD offVarData;
} UFF_FONTDIRECTORY, *PUFF_FONTDIRECTORY;
````


## -struct-fields
<dl>

### -field <b>dwSignature</b>

<dd>
<p>Specifies the font metrics record signature. This value must be FONT_REC_SIG.</p>
</dd>

### -field <b>wSize</b>

<dd>
<p>Specifies the size, in bytes, of the UFF_FONTDIRECTORY structure.</p>
</dd>

### -field <b>wFontID</b>

<dd>
<p>Specifies the font identifier. This value must match the <b>wDataID</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547364">DATA_HEADER</a> structure that specifies font metrics information within the .uff file.</p>
</dd>

### -field <b>sGlyphID</b>

<dd>
<p>Specifies the glyph set identifier. This value specifies the glyph set that is to be associated with the font. See the following Remarks section.</p>
</dd>

### -field <b>wFlags</b>

<dd>
<p>Is a set of bit flags. One or more of the following flags can be specified.</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>FONT_FL_DEVICEFONT</p>
</td>
<td>
<p>The font is a device font.</p>
</td>
</tr>
<tr>
<td>
<p>FONT_FL_GLYPHSET_GTT</p>
</td>
<td>
<p>The glyph set is specified in Windows 2000 and later <a href="wdkgloss.g#wdkgloss.glyph_translation_table__gtt_#wdkgloss.glyph_translation_table__gtt_"><i>GTT</i></a> format.</p>
</td>
</tr>
<tr>
<td>
<p>FONT_FL_GLYPHSET_RLE</p>
</td>
<td>
<p>The glyph set is specified in Windows NT 4.0 <a href="wdkgloss.r#wdkgloss.run-length_encoded__rle__bitmap#wdkgloss.run-length_encoded__rle__bitmap"><i>RLE</i></a> format.</p>
</td>
</tr>
<tr>
<td>
<p>FONT_FL_IFI</p>
</td>
<td>
<p>Font metrics are specified in Windows NT 4.0 IFI format.</p>
</td>
</tr>
<tr>
<td>
<p>FONT_FL_PERMANENT_SF</p>
</td>
<td>
<p>The font is a PCL permanent soft font.</p>
</td>
</tr>
<tr>
<td>
<p>FONT_FL_SOFTFONT</p>
</td>
<td>
<p>The font is a <a href="wdkgloss.p#wdkgloss.pcl#wdkgloss.pcl"><i>PCL</i></a> soft font.</p>
</td>
</tr>
<tr>
<td>
<p>FONT_FL_UFM</p>
</td>
<td>
<p>Font metrics are specified in Windows 2000 and later <a href="wdkgloss.u#wdkgloss.unidrv_font_metrics__ufm_#wdkgloss.unidrv_font_metrics__ufm_"><i>UFM</i></a> format.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dwInstallerSig</b>

<dd>
<p>Specifies the signature value of the font installer that installed the font.</p>
</dd>

### -field <b>offFontName</b>

<dd>
<p>Specifies the offset, in bytes, from the beginning of the .uff file to a DWORD-aligned, NULL-terminated, Unicode string representing the name of the font.</p>
</dd>

### -field <b>offCartridgeName</b>

<dd>
<p>Specifies the offset, in bytes, from the beginning of the .uff file to a DWORD-aligned, NULL-terminated, Unicode string representing the name of the font cartridge containing the font. If the font is not contained in a cartridge, this value should be zero.</p>
</dd>

### -field <b>offFontData</b>

<dd>
<p>Specifies the offset, in bytes, from the beginning of the .uff file to a DWORD-aligned <a href="https://msdn.microsoft.com/library/windows/hardware/ff547364">DATA_HEADER</a> structure specifying a font metrics section.</p>
</dd>

### -field <b>offGlyphData</b>

<dd>
<p>Specifies the offset, in bytes, from the beginning of the .uff file to a DWORD-aligned DATA_HEADER structure specifying a glyph set section. If <b>sGlyphID</b> is zero or negative, <b>offGlyphData</b> should be zero.</p>
</dd>

### -field <b>offVarData</b>

<dd>
<p>Specifies the offset, in bytes, from the beginning of the .uff file to a DWORD-aligned <a href="https://msdn.microsoft.com/library/windows/hardware/ff547364">DATA_HEADER</a> structure specifying a data section. If the FONT_FL_PERMANENT_SF flag is set in <b>wFlags</b>, <b>offVarData</b> must be zero.</p>
</dd>
</dl>

## -remarks
<p>If <b>sGlyphID</b> is a greater than zero, it must match the <b>wDataID</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547364">DATA_HEADER</a> structure that specifies a glyph set within the .uff file.</p>

<p>If <b>sGlyphID</b> is less than zero, it must be one of the CC_-prefixed constants defined in prntfont.h, which identify predefined glyph sets.</p>

<p>If <b>sGlyphID</b> is zero, Unidrv uses the glyph set resource identifier contained in the font's UNIFM_HDR structure. The glyph set resource must be contained in the minidriver's resource DLL, or else Unidrv uses the default glyph translation.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547364">DATA_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20UFF_FONTDIRECTORY structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
