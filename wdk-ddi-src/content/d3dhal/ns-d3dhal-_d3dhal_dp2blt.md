---
UID: NS:d3dhal._D3DHAL_DP2BLT
title: "_D3DHAL_DP2BLT"
author: windows-driver-content
description: DirectX 9.0 and later versions only. D3DHAL_DP2BLT is used for two dimensional surface blts when D3dDrawPrimitives2 responds to the D3DDP2OP_BLT command token.
old-location: display\d3dhal_dp2blt.htm
old-project: display
ms.assetid: 2d0cdc50-a194-4eda-8bba-f6e5c06ff32c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*LPD3DHAL_DP2BLT, D3DHAL_DP2BLT, D3DHAL_DP2BLT structure [Display Devices], LPD3DHAL_DP2BLT, LPD3DHAL_DP2BLT structure pointer [Display Devices], _D3DHAL_DP2BLT, d3dhal/D3DHAL_DP2BLT, d3dhal/LPD3DHAL_DP2BLT, d3dstrct_cab5e8b8-ec72-4d7d-8aaa-4a1f6da44a9b.xml, display.d3dhal_dp2blt"
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
-	d3dhal.h
api_name:
-	D3DHAL_DP2BLT
product:
- Windows
targetos: Windows
req.typenames: D3DHAL_DP2BLT
---

# _D3DHAL_DP2BLT structure
DirectX 9.0 and later versions only.
   

D3DHAL_DP2BLT is used for two dimensional surface blts when <a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a> responds to the D3DDP2OP_BLT command token.

## Syntax
```
typedef struct _D3DHAL_DP2BLT {
  DWORD dwSource;
  RECTL rSource;
  DWORD dwSourceMipLevel;
  DWORD dwDest;
  RECTL rDest;
  DWORD dwDestMipLevel;
  DWORD Flags;
} D3DHAL_DP2BLT;
```

## Members


`dwSource`

Specifies the handle to the source surface.

`rSource`

Specifies a RECTL structure that specifies the upper left and lower right points of a rectangle on the source surface. These points define the area of the source blit data and its position on the source surface.

`dwSourceMipLevel`

Specifies the sublevel of a MIP-map texture that is the source of the blt.

`dwDest`

Specifies the handle to the destination surface.

`rDest`

Specifies a RECTL structure that specifies the upper left and lower right points of a rectangle on the destination surface. These points define the area in which the blit should occur and its position on the destination surface.

`dwDestMipLevel`

Specifies the sublevel of a MIP-map texture that is the destination for the blt.

`Flags`

Specifies a flag that indicates the type of filtering that the driver must perform. This member is set to zero to indicate that the driver can use its own filtering technique or is set to one of the following flags.

<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
DP2BLT_LINEAR

</td>
<td>
Set for linear filtering.

</td>
</tr>
<tr>
<td>
DP2BLT_POINT

</td>
<td>
Set for point filtering.

</td>
</tr>
</table>

## Remarks
The <b>dwSource</b> or <b>dwDest</b> member specifies the kernel handle to the top-level surface and the <b>dwSourceMipLevel</b> or <b>dwDestMiplevel</b> member specifies the sublevel for the MIP-map chain where the blt occurs.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dhal.h (include D3dhal.h) |

## See Also

D3DDP2OP_BLT



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545454">D3DHAL_DP2COMMAND</a>



<a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a>