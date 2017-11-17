---
UID: NS.d3dhal._D3DHAL_DP2COLORFILL
title: D3DHAL_DP2COLORFILL
author: windows-driver-content
description: DirectX 9.0 and later versions only. D3DHAL_DP2COLORFILL is used for color-fill operations when D3dDrawPrimitives2 responds to the D3DDP2OP_COLORFILL command token.
old-location: display\d3dhal_dp2colorfill.htm
ms.assetid: 6cec8639-1d5e-4b24-8e02-a7ae62740fea
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
req.alt-api: D3DHAL_DP2COLORFILL
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
ms.keywords: D3DHAL_DP2COLORFILL, D3DHAL_DP2COLORFILL
req.iface: 
---

# D3DHAL_DP2COLORFILL structure



## -description
<p>
   DirectX 9.0 and later versions only.
   </p>
<p>D3DHAL_DP2COLORFILL is used for color-fill operations when <a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a> responds to the D3DDP2OP_COLORFILL command token.</p>


## -syntax

````
typedef struct _D3DHAL_DP2COLORFILL {
  DWORD    dwSurface;
  RECTL    rRect;
  D3DCOLOR Color;
} D3DHAL_DP2COLORFILL, *LPD3DHAL_DP2COLORFILL;
````


## -struct-fields
<dl>

### -field <b>dwSurface</b>

<dd>
<p>Specifies the handle to the surface to be filled.</p>
</dd>

### -field <b>rRect</b>

<dd>
<p>Specifies a RECTL structure that specifies the upper left and lower right points of a rectangle on the surface to be filled. </p>
</dd>

### -field <b>Color</b>

<dd>
<p>Specifies a D3DCOLOR for the color type. </p>
</dd>
</dl>

## -remarks
<p>Because DirectX 9.0 and later drivers are required to support the D3DDP2OP_COLORFILL command token, they are not required to expose a capability bit that indicates such support. </p>

<p>Display drivers must convert input color values for the ARGB and YUV classes of color formats. For color-fill operations, input color values are specified in the <b>Color</b> member. For more information, see <a href="https://msdn.microsoft.com/53ce6be1-14e1-4ee8-ba29-f198dcdacdaa">Handling Color Values for Pixel Formats</a>.</p>

<p>When the runtime calls a driver's <b>DdBlt</b> function to perform a color-fill operation, the runtime converts the D3DCOLOR value to an explicit pixel value if the runtime supports the format of that D3DCOLOR value. If the runtime does not support the format, the D3DCOLOR value is passed directly to the driver. </p>

<p>For more information about D3DCOLOR, see the DirectX SDK documentation.</p>

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
<dt>D3DDP2OP_COLORFILL</dt>
<dt>
<a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/28e0c827-33f1-4b83-9f20-bbb66bc0e14a">DdBlt</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2COLORFILL structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
