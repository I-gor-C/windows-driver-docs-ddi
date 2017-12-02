---
UID: NS.d3dhal._D3DHAL_DP2VOLUMEBLT
title: D3DHAL_DP2VOLUMEBLT
author: windows-driver-content
description: DirectX 8.0 and later versions only. The D3DHAL_DP2VOLUMEBLT structure is used for volume texture blts when D3dDrawPrimitives2 responds to the D3DDP2OP_VOLUMEBLT command token.
old-location: display\d3dhal_dp2volumeblt.htm
old-project: display
ms.assetid: 6c301643-1e1b-4b0c-8827-8eae988b1e9b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DHAL_DP2VOLUMEBLT, D3DHAL_DP2VOLUMEBLT
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
req.alt-api: D3DHAL_DP2VOLUMEBLT
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

# D3DHAL_DP2VOLUMEBLT structure



## -description
<p>
   DirectX 8.0 and later versions only.
   </p>
<p>The D3DHAL_DP2VOLUMEBLT structure is used for volume texture blts when <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a> responds to the D3DDP2OP_VOLUMEBLT command token.</p>


## -syntax

````
typedef struct _D3DHAL_DP2VOLUMEBLT {
  DWORD  dwDDDestSurface;
  DWORD  dwDDSrcSurface;
  DWORD  dwDestX;
  DWORD  dwDestY;
  DWORD  dwDestZ;
  D3DBOX srcBox;
  DWORD  dwFlags;
} D3DHAL_DP2VOLUMEBLT, *LPD3DHAL_DP2VOLUMEBLT;
````


## -struct-fields
<dl>

### -field dwDDDestSurface

<dd>
<p>Specifies the handle to the destination volume texture.</p>
</dd>

### -field dwDDSrcSurface

<dd>
<p>Specifies the handle to the source volume texture.</p>
</dd>

### -field dwDestX

<dd>
<p>Specify the location in the destination volume texture to copy the defined source subvolume. These members (<b>dwDestX</b>, <b>dwDestY</b>, and <b>dwDestZ</b>) are specified in screen coordinates.</p>
</dd>

### -field dwDestY

<dd>
<p>See <b>dwDestX</b> above.</p>
</dd>

### -field dwDestZ

<dd>
<p>See <b>dwDestX</b> above.</p>
</dd>

### -field srcBox

<dd>
<p>Specifies a subvolume of the source volume texture to copy to the destination.</p>
</dd>

### -field dwFlags

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks
<p>The <a href="display.d3dcreatesurfaceex">D3dCreateSurfaceEx</a> callback creates the small integer handles to the volume textures that can be used as source and destination volume textures for volume texture blts.</p>

<p>See Remarks for <a href="..\d3dhal\ns-d3dhal--d3dhal-dp2texblt.md">D3DHAL_DP2TEXBLT</a>.</p>

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
<dt>D3DDP2OP_VOLUMEBLT</dt>
<dt>
<a href="display.d3dcreatesurfaceex">D3dCreateSurfaceEx</a>
</dt>
<dt>
<a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="..\d3dhal\ns-d3dhal--d3dhal-dp2texblt.md">D3DHAL_DP2TEXBLT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2VOLUMEBLT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
