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

### -field SVI_NUMDATABYTES

<dd>
<p>The number of data bytes.</p>
</dd>

### -field SVI_WIDTHINBYTES

<dd>
<p>The raster data width in bytes.</p>
</dd>

### -field SVI_HEIGHTINPIXELS

<dd>
<p>The raster data height in pixels.</p>
</dd>

### -field SVI_COPIES

<dd>
<p>The number of copies.</p>
</dd>

### -field SVI_PRINTDIRECTION

<dd>
<p>The print direction in CC degrees.</p>
</dd>

### -field SVI_DESTX

<dd>
<p>The x destination.</p>
</dd>

### -field SVI_DESTY

<dd>
<p>The y destination.</p>
</dd>

### -field SVI_DESTXREL

<dd>
<p>The relative x destination.</p>
</dd>

### -field SVI_DESTYREL

<dd>
<p>The relative y direction.</p>
</dd>

### -field SVI_LINEFEEDSPACING

<dd>
<p>The line feed spacing.</p>
</dd>

### -field SVI_RECTXSIZE

<dd>
<p>The x rect size.</p>
</dd>

### -field SVI_RECTYSIZE

<dd>
<p>The y rect size.</p>
</dd>

### -field SVI_GRAYPERCENT

<dd>
<p>The gray percentage.</p>
</dd>

### -field SVI_NEXTFONTID

<dd>
<p>The next font ID.</p>
</dd>

### -field SVI_NEXTGLYPH

<dd>
<p>The next glyph.</p>
</dd>

### -field SVI_PHYSPAPERLENGTH

<dd>
<p>The physical paper length.</p>
</dd>

### -field SVI_PHYSPAPERWIDTH

<dd>
<p>The physical paper width.</p>
</dd>

### -field SVI_FONTHEIGHT

<dd>
<p>The font height.</p>
</dd>

### -field SVI_FONTWIDTH

<dd>
<p>The font width.</p>
</dd>

### -field SVI_FONTMAXWIDTH

<dd>
<p>The max font width.</p>
</dd>

### -field SVI_FONTBOLD

<dd>
<p>The font is bold.</p>
</dd>

### -field SVI_FONTITALIC

<dd>
<p>The font is italicized.</p>
</dd>

### -field SVI_FONTUNDERLINE

<dd>
<p>The font is underlined.</p>
</dd>

### -field SVI_FONTSTRIKETHRU

<dd>
<p>The font has the strikethru style applied.</p>
</dd>

### -field SVI_CURRENTFONTID

<dd>
<p>The current font ID.</p>
</dd>

### -field SVI_TEXTYRES

<dd>
<p>The text y resolution.</p>
</dd>

### -field SVI_TEXTXRES

<dd>
<p>The text x resolution.</p>
</dd>

### -field SVI_GRAPHICSYRES

<dd>
<p>The graphics y resolution.</p>
</dd>

### -field SVI_GRAPHICSXRES

<dd>
<p>The graphics x resolution.</p>
</dd>

### -field SVI_ROP3

<dd>
<p>The rop3.</p>
</dd>

### -field SVI_REDVALUE

<dd>
<p>The red value.</p>
</dd>

### -field SVI_GREENVALUE

<dd>
<p>The green value.</p>
</dd>

### -field SVI_BLUEVALUE

<dd>
<p>The blue value.</p>
</dd>

### -field SVI_PALETTEINDEXTOPROGRAM

<dd>
<p>The palette index to program.</p>
</dd>

### -field SVI_CURRENTPALETTEINDEX

<dd>
<p>The current palette index.</p>
</dd>

### -field SVI_PATTERNBRUSH_TYPE

<dd>
<p>The pattern brush type.</p>
</dd>

### -field SVI_PATTERNBRUSH_ID

<dd>
<p>The pattern brush ID.</p>
</dd>

### -field SVI_PATTERNBRUSH_SIZE

<dd>
<p>The pattern brush size.</p>
</dd>

### -field SVI_CURSORORIGINX

<dd>
<p>The cursor origin x value. This is in master units and in the coordinates of the currently selected orientation. This values is defined as ImageableOrigin minus CursorOrigin.</p>
</dd>

### -field SVI_CURSORORIGINY

<dd>
<p>The cursor origin y value. This is in master units and in the coordinates of the currently selected orientation. This values is defined as ImageableOrigin minus CursorOrigin.</p>
</dd>

### -field SVI_PAGENUMBER

<dd>
<p>The page number. This value tracks the number of times DrvStartBand has been called since StartDoc.</p>
</dd>

### -field SVI_MAX

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