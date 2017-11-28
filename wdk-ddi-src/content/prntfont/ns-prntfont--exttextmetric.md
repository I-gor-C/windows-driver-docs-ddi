---
UID: NS.prntfont._EXTTEXTMETRIC
title: EXTTEXTMETRIC
author: windows-driver-content
description: The EXTTEXTMETRIC structure is used to specify font-specific information within Unidrv font metrics files (.ufm files).
old-location: print\exttextmetric.htm
old-project: print
ms.assetid: d3d2397c-71c3-4904-a1ad-96a94698e50c
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: EXTTEXTMETRIC, EXTTEXTMETRIC, *PEXTTEXTMETRIC
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
req.alt-api: EXTTEXTMETRIC
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

# EXTTEXTMETRIC structure



## -description
<p>The EXTTEXTMETRIC structure is used to specify font-specific information within <a href="print.customized_font_management#ddk_unidrv_font_metrics_files_gg#ddk_unidrv_font_metrics_files_gg">Unidrv font metrics files</a> (.ufm files).</p>


## -syntax

````
typedef struct _EXTTEXTMETRIC {
  short emSize;
  short emPointSize;
  short emOrientation;
  short emMasterHeight;
  short emMinScale;
  short emMaxScale;
  short emMasterUnits;
  short emCapHeight;
  short emXHeight;
  short emLowerCaseAscent;
  short emLowerCaseDescent;
  short emSlant;
  short emSuperScript;
  short emSubScript;
  short emSuperScriptSize;
  short emSubScriptSize;
  short emUnderlineOffset;
  short emUnderlineWidth;
  short emDoubleUpperUnderlineOffset;
  short emDoubleLowerUnderlineOffset;
  short emDoubleUpperUnderlineWidth;
  short emDoubleLowerUnderlineWidth;
  short emStrikeOutOffset;
  short emStrikeOutWidth;
  WORD  emKernPairs;
  WORD  emKernTracks;
} EXTTEXTMETRIC, *PEXTTEXTMETRIC;
````


## -struct-fields
<dl>

### -field <b>emSize</b>

<dd>
<p>Specifies the size of the structure, in bytes.</p>
</dd>

### -field <b>emPointSize</b>

<dd>
<p>Specifies the nominal point size of this font, in twips (1/20 of a point, or 1/1440 inch). This is the intended size of the font; the actual size may differ slightly depending on the resolution of the device.</p>
</dd>

### -field <b>emOrientation</b>

<dd>
<p>Specifies the orientation of the font. The <b>emOrientation</b> member can be any of the following values: </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>Either portrait or landscape orientation </p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>Portrait orientation</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>Landscape orientation</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>emMasterHeight</b>

<dd>
<p>Specifies the font size, in device units, for which the values in this font's extent table are exact.</p>
</dd>

### -field <b>emMinScale</b>

<dd>
<p>Specifies the minimum valid point size for this font. The following equation illustrates how the minimum point size is determined:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>smallest point size = (emMinScale * 72) / dfVertRes </pre>
</td>
</tr>
</table></span></div>
<p>The value 72 represents the number of points per inch. The <i>dfVertRes</i> value is the number of dots per inch.</p>
</dd>

### -field <b>emMaxScale</b>

<dd>
<p>Specifies the maximum valid point size for this font. The following equation illustrates how the maximum point size is determined:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>largest point size = (etmMaxScale * 72) / dfVertRes </pre>
</td>
</tr>
</table></span></div>
<p>The value 72 represents the number of points per inch. The <i>dfVertRes</i> value is the number of dots per inch.</p>
</dd>

### -field <b>emMasterUnits</b>

<dd>
<p>Specifies the integral number of units per em, where an em equals the value of the <b>emMasterHeight</b> member. (That is, <b>emMasterUnits</b> is <b>emMasterHeight</b> expressed in font units instead of device units.)</p>
</dd>

### -field <b>emCapHeight</b>

<dd>
<p>Specifies the height, in font units, of uppercase characters in the font. Typically, this is the height of uppercase H.</p>
</dd>

### -field <b>emXHeight</b>

<dd>
<p>Specifies the height, in font units, of lowercase characters in the font. Typically, this is the height of lowercase x.</p>
</dd>

### -field <b>emLowerCaseAscent</b>

<dd>
<p>Specifies the distance, in font units, that the ascender of lowercase letters extends above the base line. Typically, this is the height of lowercase d.</p>
</dd>

### -field <b>emLowerCaseDescent</b>

<dd>
<p>Specifies the distance, in font units, that the descender of lowercase letters extends below the base line. Typically, this is specified for the descender of lowercase p.</p>
</dd>

### -field <b>emSlant</b>

<dd>
<p>For an italic or slanted font, specifies the angle of the slant measured in tenths of a degree clockwise from the upright version of the font.</p>
</dd>

### -field <b>emSuperScript</b>

<dd>
<p>Specifies the recommended amount, in font units, to offset superscript characters from the base line. This is typically a negative value.</p>
</dd>

### -field <b>emSubScript</b>

<dd>
<p>Specifies the recommended amount, in font units, to offset subscript characters from the base line. This is typically a positive value.</p>
</dd>

### -field <b>emSuperScriptSize</b>

<dd>
<p>Specifies the recommended size, in font units, of superscript characters for this font.</p>
</dd>

### -field <b>emSubScriptSize</b>

<dd>
<p>Specifies the recommended size, in font units, of subscript characters for this font.</p>
</dd>

### -field <b>emUnderlineOffset</b>

<dd>
<p>Specifies the offset, in font units, downward from the base line, where the top of a single underline bar should appear.</p>
</dd>

### -field <b>emUnderlineWidth</b>

<dd>
<p>Specifies the thickness, in font units, of the underline bar.</p>
</dd>

### -field <b>emDoubleUpperUnderlineOffset</b>

<dd>
<p>Specifies the offset, in font units, downward from the base line, where the top of the upper double-underline bar should appear.</p>
</dd>

### -field <b>emDoubleLowerUnderlineOffset</b>

<dd>
<p>Specifies the offset, in font units, downward from the base line, where the top of the lower double-underline bar should appear.</p>
</dd>

### -field <b>emDoubleUpperUnderlineWidth</b>

<dd>
<p>Specifies the thickness, in font units, of the upper underline bar.</p>
</dd>

### -field <b>emDoubleLowerUnderlineWidth</b>

<dd>
<p>Specifies the thickness, in font units, of the lower underline bar.</p>
</dd>

### -field <b>emStrikeOutOffset</b>

<dd>
<p>Specifies the offset, in font units, upward from the base line, where the top of a strikeout bar should appear.</p>
</dd>

### -field <b>emStrikeOutWidth</b>

<dd>
<p>Specifies the thickness, in font units, of the strikeout bar.</p>
</dd>

### -field <b>emKernPairs</b>

<dd>
<p>Specifies the number of character kerning pairs defined for this font.</p>
</dd>

### -field <b>emKernTracks</b>

<dd>
<p>Specifies the number of kerning tracks defined for this font.</p>
</dd>
</dl>

## -remarks


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