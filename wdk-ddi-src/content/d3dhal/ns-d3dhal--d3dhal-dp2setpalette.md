---
UID: NS.d3dhal._D3DHAL_DP2SETPALETTE
title: D3DHAL_DP2SETPALETTE
author: windows-driver-content
description: The D3DHAL_DP2SETPALETTE structure is used to associate a palette with a texture when a driver responds to D3DDP2OP_SETPALETTE in D3dDrawPrimitives2.
old-location: display\d3dhal_dp2setpalette.htm
old-project: display
ms.assetid: 8c472869-028e-41f5-93df-94e91c47b76e
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DHAL_DP2SETPALETTE, D3DHAL_DP2SETPALETTE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dhal.h
req.include-header: D3dhal.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DHAL_DP2SETPALETTE
req.alt-loc: d3dhal.h
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

# D3DHAL_DP2SETPALETTE structure



## -description
<p>The D3DHAL_DP2SETPALETTE structure is used to associate a palette with a texture when a driver responds to D3DDP2OP_SETPALETTE in <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>. This opcode is used to map an association between a palette handle and a surface handle, and specify the characteristics of the palette.</p>


## -syntax

````
typedef struct _D3DHAL_DP2SETPALETTE {
  DWORD dwPaletteHandle;
  DWORD dwPaletteFlags;
  DWORD dwSurfaceHandle;
} D3DHAL_DP2SETPALETTE, *LPD3DHAL_DP2SETPALETTE;
````


## -struct-fields
<dl>

### -field <b>dwPaletteHandle</b>

<dd>
<p>Specifies a handle to the palette to be set up. If the value is zero, the surface specified by <b>dwSurfaceHandle</b> should be uncoupled from any palette it might have been associated with previously.</p>
</dd>

### -field <b>dwPaletteFlags</b>

<dd>
<p>Specifies a set of flags that specify the attributes of the palette.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DDRAWIPAL_2</p>
</td>
<td>
<p>The palette has 2 entries. Currently unused.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAWIPAL_4</p>
</td>
<td>
<p>The palette has 4 entries. Currently unused.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAWIPAL_16</p>
</td>
<td>
<p>The palette has 16 entries. Currently unused.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAWIPAL_256</p>
</td>
<td>
<p>The palette has 256 entries. Currently unused.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAWIPAL_ALLOW256</p>
</td>
<td>
<p>The palette can be fully updated. Currently unused.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAWIPAL_ALPHA</p>
</td>
<td>
<p>The palette's alpha data channel is valid and should be used.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAWIPAL_DIRTY</p>
</td>
<td>
<p>The palette has been changed so the GDI palette is out of sync. Currently unused.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAWIPAL_EXCLUSIVE</p>
</td>
<td>
<p>The palette is being used in exclusive mode. Currently unused.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAWIPAL_GDI</p>
</td>
<td>
<p>The palette is allocated through GDI. Currently unused.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAWIPAL_INHEL</p>
</td>
<td>
<p>The palette is done in the HEL (hardware emulation layer). Currently unused.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAWIPAL_STORED_8</p>
</td>
<td>
<p>The palette is stored using 8 bpp per entry. Currently unused.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAWIPAL_STORED_16</p>
</td>
<td>
<p>The palette is stored using 16 bpp per entry. Currently unused.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAWIPAL_STORED_24</p>
</td>
<td>
<p>The palette is stored using 24 bpp per entry. Currently unused.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAWIPAL_STORED_8INDEX</p>
</td>
<td>
<p>The palette is stored as an 8-bit index into a destination palette. Currently unused.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dwSurfaceHandle</b>

<dd>
<p>Specifies a handle to the Direct3D surface (texture) that this palette (identified by <b>dwPaletteHandle</b>) is associated to.</p>
</dd>
</dl>

## -remarks
<p>The number of D3DHAL_DP2SETPALETTE structures to follow is specified by the <b>wStateCount</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545454">D3DHAL_DP2COMMAND</a> structure that precedes them in the command stream.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dhal.h (include D3dhal.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>D3DDP2OP_SETPALETTE</dt>
<dt>
<a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545454">D3DHAL_DP2COMMAND</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2SETPALETTE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
