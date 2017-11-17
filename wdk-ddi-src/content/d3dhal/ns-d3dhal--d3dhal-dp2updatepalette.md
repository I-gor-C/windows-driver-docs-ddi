---
UID: NS.d3dhal._D3DHAL_DP2UPDATEPALETTE
title: D3DHAL_DP2UPDATEPALETTE
author: windows-driver-content
description: The D3DHAL_DP2UPDATEPALETTE structure alters the palette that is used for palletized textures.
old-location: display\d3dhal_dp2updatepalette.htm
ms.assetid: 1ab2e4da-1107-4a5b-99e4-9c9ea864f95e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dhal.h
req.include-header: D3dhal.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DHAL_DP2UPDATEPALETTE
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
ms.keywords: D3DHAL_DP2UPDATEPALETTE, D3DHAL_DP2UPDATEPALETTE
req.iface: 
---

# D3DHAL_DP2UPDATEPALETTE structure



## -description
<p>The D3DHAL_DP2UPDATEPALETTE structure alters the palette that is used for palletized textures.</p>


## -syntax

````
typedef struct _D3DHAL_DP2UPDATEPALETTE {
  DWORD dwPaletteHandle;
  WORD  wStartIndex;
  WORD  wNumEntries;
} D3DHAL_DP2UPDATEPALETTE, *LPD3DHAL_DP2UPDATEPALETTE;
````


## -struct-fields
<dl>

### -field <b>dwPaletteHandle</b>

<dd>
<p>Specifies a handle to the palette to be altered.</p>
</dd>

### -field <b>wStartIndex</b>

<dd>
<p>Specifies the index in the palette beyond which data is updated. </p>
</dd>

### -field <b>wNumEntries</b>

<dd>
<p>Specifies the number of PALETTEENTRYs being updated.</p>
</dd>
</dl>

## -remarks
<p>The D3DHAL_DP2UPDATEPALETTE structure is used when responding to the D3DDP2OP_UPDATEPALETTE opcode in <a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a>. </p>

<p>The palette handle attached to a surface is updated with <b>wNumEntries</b> PALETTEENTRYs starting at a specific <b>wStartIndex</b> member of the palette. A PALETTEENTRY (defined in <i>wingdi.h</i> and <i>wtypes.h</i>) is actually a DWORD with an ARGB color for each byte.</p>

<p>After the D3DHAL_DP2UPDATEPALETTE structure in the command stream, the actual palette data follows (without any padding), consisting of one DWORD per palette entry (in ARGB format, with 8 bits for each of the four channels). There is only one D3DHAL_DP2UPDATEPALETTE structure (plus palette data) following the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545454">D3DHAL_DP2COMMAND</a> structure regardless of the value of <b>wStateCount</b> (a member of the D3DHAL_DP2COMMAND structure).</p>

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
<dt>D3DDP2OP_UPDATEPALETTE</dt>
<dt>
<a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545454">D3DHAL_DP2COMMAND</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2UPDATEPALETTE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
