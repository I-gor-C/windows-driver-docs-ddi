---
UID: NS.d3dhal._D3DHAL_DP2VOLUMEBLT
title: D3DHAL_DP2VOLUMEBLT
author: windows-driver-content
description: DirectX 8.0 and later versions only. The D3DHAL_DP2VOLUMEBLT structure is used for volume texture blts when D3dDrawPrimitives2 responds to the D3DDP2OP_VOLUMEBLT command token.
old-location: display\d3dhal_dp2volumeblt.htm
ms.assetid: 6c301643-1e1b-4b0c-8827-8eae988b1e9b
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
ms.keywords: D3DHAL_DP2VOLUMEBLT, D3DHAL_DP2VOLUMEBLT
req.iface: 
---

# D3DHAL_DP2VOLUMEBLT structure



## -description
<p>
   DirectX 8.0 and later versions only.
   </p>
<p>The D3DHAL_DP2VOLUMEBLT structure is used for volume texture blts when <a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a> responds to the D3DDP2OP_VOLUMEBLT command token.</p>


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

### -field <b>dwDDDestSurface</b>

<dd>
<p>Specifies the handle to the destination volume texture.</p>
</dd>

### -field <b>dwDDSrcSurface</b>

<dd>
<p>Specifies the handle to the source volume texture.</p>
</dd>

### -field <b>dwDestX</b>

<dd>
<p>Specify the location in the destination volume texture to copy the defined source subvolume. These members (<b>dwDestX</b>, <b>dwDestY</b>, and <b>dwDestZ</b>) are specified in screen coordinates.</p>
</dd>

### -field <b>dwDestY</b>

<dd>
<p>See <b>dwDestX</b> above.</p>
</dd>

### -field <b>dwDestZ</b>

<dd>
<p>See <b>dwDestX</b> above.</p>
</dd>

### -field <b>srcBox</b>

<dd>
<p>Specifies a subvolume of the source volume texture to copy to the destination.</p>
</dd>

### -field <b>dwFlags</b>

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/dd07e49c-ec1f-4ba6-8b17-80ce6d3c5813">D3dCreateSurfaceEx</a> callback creates the small integer handles to the volume textures that can be used as source and destination volume textures for volume texture blts.</p>

<p>See Remarks for <a href="https://msdn.microsoft.com/library/windows/hardware/ff545869">D3DHAL_DP2TEXBLT</a>.</p>

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
<a href="https://msdn.microsoft.com/dd07e49c-ec1f-4ba6-8b17-80ce6d3c5813">D3dCreateSurfaceEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545869">D3DHAL_DP2TEXBLT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2VOLUMEBLT structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
