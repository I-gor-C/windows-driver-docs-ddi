---
UID: NE:printoem._STDVARIABLEINDEX
title: "_STDVARIABLEINDEX"
author: windows-driver-content
description: "."
old-location: print\stdvariableindex.htm
old-project: print
ms.assetid: 02E54636-0B8D-40FE-8405-0FB130139828
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: STDVARIABLEINDEX, STDVARIABLEINDEX enumeration [Print Devices], SVI_BLUEVALUE, SVI_COPIES, SVI_CURRENTFONTID, SVI_CURRENTPALETTEINDEX, SVI_CURSORORIGINX, SVI_CURSORORIGINY, SVI_DESTX, SVI_DESTXREL, SVI_DESTY, SVI_DESTYREL, SVI_FONTBOLD, SVI_FONTHEIGHT, SVI_FONTITALIC, SVI_FONTMAXWIDTH, SVI_FONTSTRIKETHRU, SVI_FONTUNDERLINE, SVI_FONTWIDTH, SVI_GRAPHICSXRES, SVI_GRAPHICSYRES, SVI_GRAYPERCENT, SVI_GREENVALUE, SVI_HEIGHTINPIXELS, SVI_LINEFEEDSPACING, SVI_MAX, SVI_NEXTFONTID, SVI_NEXTGLYPH, SVI_NUMDATABYTES, SVI_PAGENUMBER, SVI_PALETTEINDEXTOPROGRAM, SVI_PATTERNBRUSH_ID, SVI_PATTERNBRUSH_SIZE, SVI_PATTERNBRUSH_TYPE, SVI_PHYSPAPERLENGTH, SVI_PHYSPAPERWIDTH, SVI_PRINTDIRECTION, SVI_RECTXSIZE, SVI_RECTYSIZE, SVI_REDVALUE, SVI_ROP3, SVI_TEXTXRES, SVI_TEXTYRES, SVI_WIDTHINBYTES, _STDVARIABLEINDEX, print.stdvariableindex, printoem/STDVARIABLEINDEX, printoem/SVI_BLUEVALUE, printoem/SVI_COPIES, printoem/SVI_CURRENTFONTID, printoem/SVI_CURRENTPALETTEINDEX, printoem/SVI_CURSORORIGINX, printoem/SVI_CURSORORIGINY, printoem/SVI_DESTX, printoem/SVI_DESTXREL, printoem/SVI_DESTY, printoem/SVI_DESTYREL, printoem/SVI_FONTBOLD, printoem/SVI_FONTHEIGHT, printoem/SVI_FONTITALIC, printoem/SVI_FONTMAXWIDTH, printoem/SVI_FONTSTRIKETHRU, printoem/SVI_FONTUNDERLINE, printoem/SVI_FONTWIDTH, printoem/SVI_GRAPHICSXRES, printoem/SVI_GRAPHICSYRES, printoem/SVI_GRAYPERCENT, printoem/SVI_GREENVALUE, printoem/SVI_HEIGHTINPIXELS, printoem/SVI_LINEFEEDSPACING, printoem/SVI_MAX, printoem/SVI_NEXTFONTID, printoem/SVI_NEXTGLYPH, printoem/SVI_NUMDATABYTES, printoem/SVI_PAGENUMBER, printoem/SVI_PALETTEINDEXTOPROGRAM, printoem/SVI_PATTERNBRUSH_ID, printoem/SVI_PATTERNBRUSH_SIZE, printoem/SVI_PATTERNBRUSH_TYPE, printoem/SVI_PHYSPAPERLENGTH, printoem/SVI_PHYSPAPERWIDTH, printoem/SVI_PRINTDIRECTION, printoem/SVI_RECTXSIZE, printoem/SVI_RECTYSIZE, printoem/SVI_REDVALUE, printoem/SVI_ROP3, printoem/SVI_TEXTXRES, printoem/SVI_TEXTYRES, printoem/SVI_WIDTHINBYTES
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Printoem.h
api_name:
-	STDVARIABLEINDEX
product: Windows
targetos: Windows
req.typenames: STDVARIABLEINDEX
req.product: Windows 10 or later.
---

# _STDVARIABLEINDEX Enumeration


## Syntax
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

## Constants

<table>
            
                <tr>
                    <td>SVI_BLUEVALUE</td>
                    <td>The blue value.</td>
                </tr>
            
                <tr>
                    <td>SVI_COPIES</td>
                    <td>The number of copies.</td>
                </tr>
            
                <tr>
                    <td>SVI_CURRENTFONTID</td>
                    <td>The current font ID.</td>
                </tr>
            
                <tr>
                    <td>SVI_CURRENTPALETTEINDEX</td>
                    <td>The current palette index.</td>
                </tr>
            
                <tr>
                    <td>SVI_CURSORORIGINX</td>
                    <td>The cursor origin x value. This is in master units and in the coordinates of the currently selected orientation. This values is defined as ImageableOrigin minus CursorOrigin.</td>
                </tr>
            
                <tr>
                    <td>SVI_CURSORORIGINY</td>
                    <td>The cursor origin y value. This is in master units and in the coordinates of the currently selected orientation. This values is defined as ImageableOrigin minus CursorOrigin.</td>
                </tr>
            
                <tr>
                    <td>SVI_DESTX</td>
                    <td>The x destination.</td>
                </tr>
            
                <tr>
                    <td>SVI_DESTXREL</td>
                    <td>The relative x destination.</td>
                </tr>
            
                <tr>
                    <td>SVI_DESTY</td>
                    <td>The y destination.</td>
                </tr>
            
                <tr>
                    <td>SVI_DESTYREL</td>
                    <td>The relative y direction.</td>
                </tr>
            
                <tr>
                    <td>SVI_FONTBOLD</td>
                    <td>The font is bold.</td>
                </tr>
            
                <tr>
                    <td>SVI_FONTHEIGHT</td>
                    <td>The font height.</td>
                </tr>
            
                <tr>
                    <td>SVI_FONTITALIC</td>
                    <td>The font is italicized.</td>
                </tr>
            
                <tr>
                    <td>SVI_FONTMAXWIDTH</td>
                    <td>The max font width.</td>
                </tr>
            
                <tr>
                    <td>SVI_FONTSTRIKETHRU</td>
                    <td>The font has the strikethru style applied.</td>
                </tr>
            
                <tr>
                    <td>SVI_FONTUNDERLINE</td>
                    <td>The font is underlined.</td>
                </tr>
            
                <tr>
                    <td>SVI_FONTWIDTH</td>
                    <td>The font width.</td>
                </tr>
            
                <tr>
                    <td>SVI_GRAPHICSXRES</td>
                    <td>The graphics x resolution.</td>
                </tr>
            
                <tr>
                    <td>SVI_GRAPHICSYRES</td>
                    <td>The graphics y resolution.</td>
                </tr>
            
                <tr>
                    <td>SVI_GRAYPERCENT</td>
                    <td>The gray percentage.</td>
                </tr>
            
                <tr>
                    <td>SVI_GREENVALUE</td>
                    <td>The green value.</td>
                </tr>
            
                <tr>
                    <td>SVI_HEIGHTINPIXELS</td>
                    <td>The raster data height in pixels.</td>
                </tr>
            
                <tr>
                    <td>SVI_LINEFEEDSPACING</td>
                    <td>The line feed spacing.</td>
                </tr>
            
                <tr>
                    <td>SVI_MAX</td>
                    <td>Placeholder. Do not use.</td>
                </tr>
            
                <tr>
                    <td>SVI_NEXTFONTID</td>
                    <td>The next font ID.</td>
                </tr>
            
                <tr>
                    <td>SVI_NEXTGLYPH</td>
                    <td>The next glyph.</td>
                </tr>
            
                <tr>
                    <td>SVI_NUMDATABYTES</td>
                    <td>The number of data bytes.</td>
                </tr>
            
                <tr>
                    <td>SVI_PAGENUMBER</td>
                    <td>The page number. This value tracks the number of times DrvStartBand has been called since StartDoc.</td>
                </tr>
            
                <tr>
                    <td>SVI_PALETTEINDEXTOPROGRAM</td>
                    <td>The palette index to program.</td>
                </tr>
            
                <tr>
                    <td>SVI_PATTERNBRUSH_ID</td>
                    <td>The pattern brush ID.</td>
                </tr>
            
                <tr>
                    <td>SVI_PATTERNBRUSH_SIZE</td>
                    <td>The pattern brush size.</td>
                </tr>
            
                <tr>
                    <td>SVI_PATTERNBRUSH_TYPE</td>
                    <td>The pattern brush type.</td>
                </tr>
            
                <tr>
                    <td>SVI_PHYSPAPERLENGTH</td>
                    <td>The physical paper length.</td>
                </tr>
            
                <tr>
                    <td>SVI_PHYSPAPERWIDTH</td>
                    <td>The physical paper width.</td>
                </tr>
            
                <tr>
                    <td>SVI_PRINTDIRECTION</td>
                    <td>The print direction in CC degrees.</td>
                </tr>
            
                <tr>
                    <td>SVI_RECTXSIZE</td>
                    <td>The x rect size.</td>
                </tr>
            
                <tr>
                    <td>SVI_RECTYSIZE</td>
                    <td>The y rect size.</td>
                </tr>
            
                <tr>
                    <td>SVI_REDVALUE</td>
                    <td>The red value.</td>
                </tr>
            
                <tr>
                    <td>SVI_ROP3</td>
                    <td>The rop3.</td>
                </tr>
            
                <tr>
                    <td>SVI_TEXTXRES</td>
                    <td>The text x resolution.</td>
                </tr>
            
                <tr>
                    <td>SVI_TEXTYRES</td>
                    <td>The text y resolution.</td>
                </tr>
            
                <tr>
                    <td>SVI_WIDTHINBYTES</td>
                    <td>The raster data width in bytes.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | printoem.h |