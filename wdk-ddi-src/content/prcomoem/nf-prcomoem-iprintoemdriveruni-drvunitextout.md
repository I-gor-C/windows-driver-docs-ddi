---
UID: NF.prcomoem.IPrintOemDriverUni.DrvUniTextOut
title: IPrintOemDriverUni::DrvUniTextOut
author: windows-driver-content
description: The IPrintOemDriverUni::DrvUniTextOut method is provided by the Unidrv driver so that a rendering plug-in using a device-managed drawing surface can easily output text strings.
old-location: print\iprintoemdriveruni_drvunitextout.htm
old-project: print
ms.assetid: f8c21813-9bfd-46a5-abb2-78ac2f2301af
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemDriverUni, DrvUniTextOut, IPrintOemDriverUni::DrvUniTextOut
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemDriverUni.DrvUniTextOut
req.alt-loc: prcomoem.h
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
req.iface: IPrintOemDriverUni
req.product: Windows 10 or later.
---

# IPrintOemDriverUni::DrvUniTextOut method



## -description
<p>The <code>IPrintOemDriverUni::DrvUniTextOut</code> method is provided by the Unidrv driver so that a rendering plug-in using a device-managed drawing surface can easily output text strings.</p>


## -syntax

````
HRESULT DrvUniTextOut(
   SURFOBJ  *pso,
   STROBJ   *pstro,
   FONTOBJ  *pfo,
   CLIPOBJ  *pco,
   RECTL    *prclExtra,
   RECTL    *prclOpaque,
   BRUSHOBJ *pboFore,
   BRUSHOBJ *pboOpaque,
   POINTL   *pptlBrushOrg,
   MIX      mix
);
````


## -parameters
<dl>

### -param <i>pso</i> 

<dd>
<p>Pointer to a <a href="display.surfobj">SURFOBJ</a> structure that describes the surface on which to write. </p>
</dd>

### -param <i>pstro</i> 

<dd>
<p>Pointer to a <a href="display.strobj">STROBJ</a> structure that defines the glyphs to be rendered and the positions in which to place them. </p>
</dd>

### -param <i>pfo</i> 

<dd>
<p>Pointer to a <a href="display.fontobj">FONTOBJ</a> structure from which to retrieve information about the font and its glyphs. </p>
</dd>

### -param <i>pco</i> 

<dd>
<p>Pointer to a <a href="display.clipobj">CLIPOBJ</a> structure that defines the clip region through which all rendering must be done. The driver cannot affect any pixels outside the clip region. </p>
</dd>

### -param <i>prclExtra</i> 

<dd>
<p>Pointer to a RECTL structure. GDI always sets this parameter to <b>NULL</b> in calls to this function. It should be ignored by the driver. </p>
</dd>

### -param <i>prclOpaque</i> 

<dd>
<p>Pointer to a <a href="display.rectl">RECTL</a> structure that represents a single opaque rectangle. This rectangle is bottom-right exclusive. Pixels within this rectangle (those that are not foreground and not clipped) are to be rendered with the opaque brush. This rectangle always bounds the text to be drawn. If this parameter is <b>NULL</b>, no opaque pixels are to be rendered. </p>
</dd>

### -param <i>pboFore</i> 

<dd>
<p>Pointer to a <a href="display.brushobj">BRUSHOBJ</a> structure that represents the brush object to be used for the foreground pixels. This brush will always be a solid color brush.</p>
</dd>

### -param <i>pboOpaque</i> 

<dd>
<p>Pointer to a BRUSHOBJ structure that represents the opaque pixels. Both the foreground and background mix modes for this brush are assumed to be R2_COPYPEN. Unless the driver sets the GCAPS_ARBRUSHOPAQUE capabilities bit in the <b>flGraphicsCaps</b> member of the DEVINFO structure, it will always be called with a solid color brush. </p>
</dd>

### -param <i>pptlBrushOrg</i> 

<dd>
<p>Pointer to a <a href="display.pointl">POINTL</a> structure that defines the brush origin for both brushes.</p>
</dd>

### -param <i>mix</i> 

<dd>
<p>The foreground and background raster operations (mix modes) for <i>pboFore</i>. </p>
</dd>
</dl>

## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

## -remarks
<p>The <code>IPrintOemDriverUni::DrvUniTextOut</code> method is provided by Unidrv for use by rendering plug-ins that support a device-managed drawing surface. Such rendering plug-ins must hook out Unidrv's <a href="display.drvtextout">DrvTextOut</a> function, and the <code>IPrintOemDriverUni::DrvUniTextOut</code> method is meant to be called from that hooking function. The hooking function must perform text region clipping and text rotation operations. It can then call <code>IPrintOemDriverUni::DrvUniTextOut</code> to request Unidrv to create the text string using downloadable fonts (and to perform glyph-based clipping).</p>

<p>If <code>IPrintOemDriverUni::DrvUniTextOut</code> cannot create the text string, either because the font is not available or is rotated, it calls the rendering plug-in's <a href="print.iprintoemuni_textoutasbitmap">IPrintOemUni::TextOutAsBitmap</a> method, which draws the text string as a bitmap.</p>

<p>For more information, see <a href="NULL">Handling Device-Managed Surfaces</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Prcomoem.h (include Prcomoem.h)</dt>
</dl>
</td>
</tr>
</table>