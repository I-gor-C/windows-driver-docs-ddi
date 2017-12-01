---
UID: NS.d3dhal._D3DHAL_DP2BLT
title: D3DHAL_DP2BLT
author: windows-driver-content
description: DirectX 9.0 and later versions only. D3DHAL_DP2BLT is used for two dimensional surface blts when D3dDrawPrimitives2 responds to the D3DDP2OP_BLT command token.
old-location: display\d3dhal_dp2blt.htm
old-project: display
ms.assetid: 2d0cdc50-a194-4eda-8bba-f6e5c06ff32c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DHAL_DP2BLT, D3DHAL_DP2BLT
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
req.alt-api: D3DHAL_DP2BLT
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

# D3DHAL_DP2BLT structure



## -description
<p>
   DirectX 9.0 and later versions only.
   </p>
<p>D3DHAL_DP2BLT is used for two dimensional surface blts when <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a> responds to the D3DDP2OP_BLT command token.</p>


## -syntax

````
typedef struct _D3DHAL_DP2BLT {
  DWORD dwSource;
  RECTL rSource;
  DWORD dwSourceMipLevel;
  DWORD dwDest;
  RECTL rDest;
  DWORD dwDestMipLevel;
  DWORD Flags;
} D3DHAL_DP2BLT, *LPD3DHAL_DP2BLT;
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
<p>Specifies the sublevel of a MIP-map texture that is the source of the blt. </p>
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
<p>Specifies a flag that indicates the type of filtering that the driver must perform. This member is set to zero to indicate that the driver can use its own filtering technique or is set to one of the following flags.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DP2BLT_LINEAR</p>
</td>
<td>
<p>Set for linear filtering.</p>
</td>
</tr>
<tr>
<td>
<p>DP2BLT_POINT</p>
</td>
<td>
<p>Set for point filtering.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
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
<dt>
<a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="..\d3dhal\ns-d3dhal--d3dhal-dp2command.md">D3DHAL_DP2COMMAND</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2BLT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
