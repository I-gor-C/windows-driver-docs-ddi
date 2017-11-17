---
UID: NS.d3dhal._D3DHAL_DP2SURFACEBLT
title: D3DHAL_DP2SURFACEBLT
author: windows-driver-content
description: DirectX 9.0 and later versions only. D3DHAL_DP2SURFACEBLT is used for two dimensional system memory to video memory surface blts when D3dDrawPrimitives2 responds to the D3DDP2OP_SURFACEBLT command token.
old-location: display\d3dhal_dp2surfaceblt.htm
ms.assetid: 0720635c-77a2-4391-ba75-b276c0d457d5
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
req.alt-api: D3DHAL_DP2SURFACEBLT
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
ms.keywords: D3DHAL_DP2SURFACEBLT, D3DHAL_DP2SURFACEBLT
req.iface: 
---

# D3DHAL_DP2SURFACEBLT structure



## -description
<p>
   DirectX 9.0 and later versions only.
   </p>
<p>D3DHAL_DP2SURFACEBLT is used for two dimensional system memory to video memory surface blts when <a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a> responds to the D3DDP2OP_SURFACEBLT command token.</p>


## -syntax

````
typedef struct _D3DHAL_DP2SURFACEBLT {
  DWORD dwSource;
  RECTL rSource;
  DWORD dwSourceMipLevel;
  DWORD dwDest;
  RECTL rDest;
  DWORD dwDestMipLevel;
  DWORD Flags;
} D3DHAL_DP2SURFACEBLT, *LPD3DHAL_DP2SURFACEBLT;
````


## -struct-fields
<dl>

### -field <b>dwSource</b>

<dd>
<p>Specifies the handle to the source surface.</p>
</dd>

### -field <b>rSource</b>

<dd>
<p>Specifies a RECTL structure that specifies the upper left and lower right points of a rectangle on the source surface. These points define the area of the source blit data and its position on the source surface.</p>
</dd>

### -field <b>dwSourceMipLevel</b>

<dd>
<p>Specifies the sublevel of a MIP-map texture that is the source of the blt.</p>
</dd>

### -field <b>dwDest</b>

<dd>
<p>Specifies the handle to the destination surface.</p>
</dd>

### -field <b>rDest</b>

<dd>
<p>Specifies a RECTL structure that specifies the upper left and lower right points of a rectangle on the destination surface. These points define the area in which the blit should occur and its position on the destination surface.</p>
</dd>

### -field <b>dwDestMipLevel</b>

<dd>
<p>Specifies the sublevel of a MIP-map texture that is the destination for the blt.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Unused</p>
</dd>
</dl>

## -remarks
<p>The D3DDP2OP_SURFACEBLT operation code is identical to the D3DDP2OP_BLT operation code except that D3DDP2OP_SURFACEBLT is only used to copy system memory to video memory and is never used for stretch blts or color conversion. Because D3DDP2OP_SURFACEBLT is not used for stretch blts, no flags are currently defined.</p>

<p>The <b>dwSource</b> or <b>dwDest</b> member specifies the kernel handle to the top-level surface and the <b>dwSourceMipLevel</b> or <b>dwDestMiplevel</b> member specifies the sublevel for the MIP-map chain where the blt occurs.</p>

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
<dt>D3DDP2OP_BLT</dt>
<dt>D3DDP2OP_SURFACEBLT</dt>
<dt>
<a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545454">D3DHAL_DP2COMMAND</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2SURFACEBLT structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
