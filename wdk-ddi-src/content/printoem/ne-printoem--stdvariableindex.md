---
UID: NE.printoem._STDVARIABLEINDEX
title: STDVARIABLEINDEX
author: windows-driver-content
description: .
old-location: print\stdvariableindex.htm
old-project: print
ms.assetid: 02E54636-0B8D-40FE-8405-0FB130139828
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintSchemaTicket2, GetParameterInitializer, IPrintSchemaTicket2::GetParameterInitializer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: printoem.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STDVARIABLEINDEX
req.alt-loc: Printoem.h
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

# STDVARIABLEINDEX enumeration



## -description
<p></p>


## -syntax

````
typedef enum _STDVARIABLEINDEX { 
  SVI_NUMDATABYTES,
  SVI_WIDTHINBYTES,
  SVI_HEIGHTINPIXELS,
  SVI_COPIES,
  SVI_PRINTDIRECTION,
  SVI_DESTX,
  SVI_DESTY,
  SVI_DESTXREL,
  SVI_DESTYREL,
  SVI_LINEFEEDSPACING,
  SVI_RECTXSIZE,
  SVI_RECTYSIZE,
  SVI_GRAYPERCENT,
  SVI_NEXTFONTID,
  SVI_NEXTGLYPH,
  SVI_PHYSPAPERLENGTH,
  SVI_PHYSPAPERWIDTH,
  SVI_FONTHEIGHT,
  SVI_FONTWIDTH,
  SVI_FONTMAXWIDTH,
  SVI_FONTBOLD,
  SVI_FONTITALIC,
  SVI_FONTUNDERLINE,
  SVI_FONTSTRIKETHRU,
  SVI_CURRENTFONTID,
  SVI_TEXTYRES,
  SVI_TEXTXRES,
  SVI_GRAPHICSYRES,
  SVI_GRAPHICSXRES,
  SVI_ROP3,
  SVI_REDVALUE,
  SVI_GREENVALUE,
  SVI_BLUEVALUE,
  SVI_PALETTEINDEXTOPROGRAM,
  SVI_CURRENTPALETTEINDEX,
  SVI_PATTERNBRUSH_TYPE,
  SVI_PATTERNBRUSH_ID,
  SVI_PATTERNBRUSH_SIZE,
  SVI_CURSORORIGINX,
  SVI_CURSORORIGINY,
  SVI_PAGENUMBER,
  SVI_MAX
} STDVARIABLEINDEX;
````


## -enum-fields
<dl>

### -field <a id="SVI_NUMDATABYTES"></a><a id="svi_numdatabytes"></a><b>SVI_NUMDATABYTES</b>

<dd>
<p>The number of data bytes.</p>
</dd>

### -field <a id="SVI_WIDTHINBYTES"></a><a id="svi_widthinbytes"></a><b>SVI_WIDTHINBYTES</b>

<dd>
<p>The raster data width in bytes.</p>
</dd>

### -field <a id="SVI_HEIGHTINPIXELS"></a><a id="svi_heightinpixels"></a><b>SVI_HEIGHTINPIXELS</b>

<dd>
<p>The raster data height in pixels.</p>
</dd>

### -field <a id="SVI_COPIES"></a><a id="svi_copies"></a><b>SVI_COPIES</b>

<dd>
<p>The number of copies.</p>
</dd>

### -field <a id="SVI_PRINTDIRECTION"></a><a id="svi_printdirection"></a><b>SVI_PRINTDIRECTION</b>

<dd>
<p>The print direction in CC degrees.</p>
</dd>

### -field <a id="SVI_DESTX"></a><a id="svi_destx"></a><b>SVI_DESTX</b>

<dd>
<p>The x destination.</p>
</dd>

### -field <a id="SVI_DESTY"></a><a id="svi_desty"></a><b>SVI_DESTY</b>

<dd>
<p>The y destination.</p>
</dd>

### -field <a id="SVI_DESTXREL"></a><a id="svi_destxrel"></a><b>SVI_DESTXREL</b>

<dd>
<p>The relative x destination.</p>
</dd>

### -field <a id="SVI_DESTYREL"></a><a id="svi_destyrel"></a><b>SVI_DESTYREL</b>

<dd>
<p>The relative y direction.</p>
</dd>

### -field <a id="SVI_LINEFEEDSPACING"></a><a id="svi_linefeedspacing"></a><b>SVI_LINEFEEDSPACING</b>

<dd>
<p>The line feed spacing.</p>
</dd>

### -field <a id="SVI_RECTXSIZE"></a><a id="svi_rectxsize"></a><b>SVI_RECTXSIZE</b>

<dd>
<p>The x rect size.</p>
</dd>

### -field <a id="SVI_RECTYSIZE"></a><a id="svi_rectysize"></a><b>SVI_RECTYSIZE</b>

<dd>
<p>The y rect size.</p>
</dd>

### -field <a id="SVI_GRAYPERCENT"></a><a id="svi_graypercent"></a><b>SVI_GRAYPERCENT</b>

<dd>
<p>The gray percentage.</p>
</dd>

### -field <a id="SVI_NEXTFONTID"></a><a id="svi_nextfontid"></a><b>SVI_NEXTFONTID</b>

<dd>
<p>The next font ID.</p>
</dd>

### -field <a id="SVI_NEXTGLYPH"></a><a id="svi_nextglyph"></a><b>SVI_NEXTGLYPH</b>

<dd>
<p>The next glyph.</p>
</dd>

### -field <a id="SVI_PHYSPAPERLENGTH"></a><a id="svi_physpaperlength"></a><b>SVI_PHYSPAPERLENGTH</b>

<dd>
<p>The physical paper length.</p>
</dd>

### -field <a id="SVI_PHYSPAPERWIDTH"></a><a id="svi_physpaperwidth"></a><b>SVI_PHYSPAPERWIDTH</b>

<dd>
<p>The physical paper width.</p>
</dd>

### -field <a id="SVI_FONTHEIGHT"></a><a id="svi_fontheight"></a><b>SVI_FONTHEIGHT</b>

<dd>
<p>The font height.</p>
</dd>

### -field <a id="SVI_FONTWIDTH"></a><a id="svi_fontwidth"></a><b>SVI_FONTWIDTH</b>

<dd>
<p>The font width.</p>
</dd>

### -field <a id="SVI_FONTMAXWIDTH"></a><a id="svi_fontmaxwidth"></a><b>SVI_FONTMAXWIDTH</b>

<dd>
<p>The max font width.</p>
</dd>

### -field <a id="SVI_FONTBOLD"></a><a id="svi_fontbold"></a><b>SVI_FONTBOLD</b>

<dd>
<p>The font is bold.</p>
</dd>

### -field <a id="SVI_FONTITALIC"></a><a id="svi_fontitalic"></a><b>SVI_FONTITALIC</b>

<dd>
<p>The font is italicized.</p>
</dd>

### -field <a id="SVI_FONTUNDERLINE"></a><a id="svi_fontunderline"></a><b>SVI_FONTUNDERLINE</b>

<dd>
<p>The font is underlined.</p>
</dd>

### -field <a id="SVI_FONTSTRIKETHRU"></a><a id="svi_fontstrikethru"></a><b>SVI_FONTSTRIKETHRU</b>

<dd>
<p>The font has the strikethru style applied.</p>
</dd>

### -field <a id="SVI_CURRENTFONTID"></a><a id="svi_currentfontid"></a><b>SVI_CURRENTFONTID</b>

<dd>
<p>The current font ID.</p>
</dd>

### -field <a id="SVI_TEXTYRES"></a><a id="svi_textyres"></a><b>SVI_TEXTYRES</b>

<dd>
<p>The text y resolution.</p>
</dd>

### -field <a id="SVI_TEXTXRES"></a><a id="svi_textxres"></a><b>SVI_TEXTXRES</b>

<dd>
<p>The text x resolution.</p>
</dd>

### -field <a id="SVI_GRAPHICSYRES"></a><a id="svi_graphicsyres"></a><b>SVI_GRAPHICSYRES</b>

<dd>
<p>The graphics y resolution.</p>
</dd>

### -field <a id="SVI_GRAPHICSXRES"></a><a id="svi_graphicsxres"></a><b>SVI_GRAPHICSXRES</b>

<dd>
<p>The graphics x resolution.</p>
</dd>

### -field <a id="SVI_ROP3"></a><a id="svi_rop3"></a><b>SVI_ROP3</b>

<dd>
<p>The rop3.</p>
</dd>

### -field <a id="SVI_REDVALUE"></a><a id="svi_redvalue"></a><b>SVI_REDVALUE</b>

<dd>
<p>The red value.</p>
</dd>

### -field <a id="SVI_GREENVALUE"></a><a id="svi_greenvalue"></a><b>SVI_GREENVALUE</b>

<dd>
<p>The green value.</p>
</dd>

### -field <a id="SVI_BLUEVALUE"></a><a id="svi_bluevalue"></a><b>SVI_BLUEVALUE</b>

<dd>
<p>The blue value.</p>
</dd>

### -field <a id="SVI_PALETTEINDEXTOPROGRAM"></a><a id="svi_paletteindextoprogram"></a><b>SVI_PALETTEINDEXTOPROGRAM</b>

<dd>
<p>The palette index to program.</p>
</dd>

### -field <a id="SVI_CURRENTPALETTEINDEX"></a><a id="svi_currentpaletteindex"></a><b>SVI_CURRENTPALETTEINDEX</b>

<dd>
<p>The current palette index.</p>
</dd>

### -field <a id="SVI_PATTERNBRUSH_TYPE"></a><a id="svi_patternbrush_type"></a><b>SVI_PATTERNBRUSH_TYPE</b>

<dd>
<p>The pattern brush type.</p>
</dd>

### -field <a id="SVI_PATTERNBRUSH_ID"></a><a id="svi_patternbrush_id"></a><b>SVI_PATTERNBRUSH_ID</b>

<dd>
<p>The pattern brush ID.</p>
</dd>

### -field <a id="SVI_PATTERNBRUSH_SIZE"></a><a id="svi_patternbrush_size"></a><b>SVI_PATTERNBRUSH_SIZE</b>

<dd>
<p>The pattern brush size.</p>
</dd>

### -field <a id="SVI_CURSORORIGINX"></a><a id="svi_cursororiginx"></a><b>SVI_CURSORORIGINX</b>

<dd>
<p>The cursor origin x value. This is in master units and in the coordinates of the currently selected orientation. This values is defined as ImageableOrigin minus CursorOrigin.</p>
</dd>

### -field <a id="SVI_CURSORORIGINY"></a><a id="svi_cursororiginy"></a><b>SVI_CURSORORIGINY</b>

<dd>
<p>The cursor origin y value. This is in master units and in the coordinates of the currently selected orientation. This values is defined as ImageableOrigin minus CursorOrigin.</p>
</dd>

### -field <a id="SVI_PAGENUMBER"></a><a id="svi_pagenumber"></a><b>SVI_PAGENUMBER</b>

<dd>
<p>The page number. This value tracks the number of times DrvStartBand has been called since StartDoc.</p>
</dd>

### -field <a id="SVI_MAX"></a><a id="svi_max"></a><b>SVI_MAX</b>

<dd>
<p>Placeholder. Do not use.</p>
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
<dt>Printoem.h</dt>
</dl>
</td>
</tr>
</table>