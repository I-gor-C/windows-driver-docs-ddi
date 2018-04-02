---
UID: NS:d3dhal._D3DHAL_DP2VOLUMEBLT
title: "_D3DHAL_DP2VOLUMEBLT"
author: windows-driver-content
description: DirectX 8.0 and later versions only. The D3DHAL_DP2VOLUMEBLT structure is used for volume texture blts when D3dDrawPrimitives2 responds to the D3DDP2OP_VOLUMEBLT command token.
old-location: display\d3dhal_dp2volumeblt.htm
old-project: display
ms.assetid: 6c301643-1e1b-4b0c-8827-8eae988b1e9b
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*LPD3DHAL_DP2VOLUMEBLT, D3DHAL_DP2VOLUMEBLT, D3DHAL_DP2VOLUMEBLT structure [Display Devices], LPD3DHAL_DP2VOLUMEBLT, LPD3DHAL_DP2VOLUMEBLT structure pointer [Display Devices], _D3DHAL_DP2VOLUMEBLT, d3dhal/D3DHAL_DP2VOLUMEBLT, d3dhal/LPD3DHAL_DP2VOLUMEBLT, d3dstrct_44b31cb6-2a36-4d2d-91a3-c59b07d8815b.xml, display.d3dhal_dp2volumeblt"
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
-	D3DHAL_DP2VOLUMEBLT
product:
- Windows
targetos: Windows
req.typenames: D3DHAL_DP2VOLUMEBLT
---

# _D3DHAL_DP2VOLUMEBLT structure
DirectX 8.0 and later versions only.
   

The D3DHAL_DP2VOLUMEBLT structure is used for volume texture blts when <a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a> responds to the D3DDP2OP_VOLUMEBLT command token.

## Syntax
```
typedef struct _D3DHAL_DP2VOLUMEBLT {
  DWORD  dwDDDestSurface;
  DWORD  dwDDSrcSurface;
  DWORD  dwDestX;
  DWORD  dwDestY;
  DWORD  dwDestZ;
  D3DBOX srcBox;
  DWORD  dwFlags;
} D3DHAL_DP2VOLUMEBLT;
```

## Members


`dwDDDestSurface`

Specifies the handle to the destination volume texture.

`dwDDSrcSurface`

Specifies the handle to the source volume texture.

`dwDestX`

Specify the location in the destination volume texture to copy the defined source subvolume. These members (<b>dwDestX</b>, <b>dwDestY</b>, and <b>dwDestZ</b>) are specified in screen coordinates.

`dwDestY`

See <b>dwDestX</b> above.

`dwDestZ`

See <b>dwDestX</b> above.

`srcBox`

Specifies a subvolume of the source volume texture to copy to the destination.

`dwFlags`

Reserved for system use.

## Remarks
The <a href="https://msdn.microsoft.com/dd07e49c-ec1f-4ba6-8b17-80ce6d3c5813">D3dCreateSurfaceEx</a> callback creates the small integer handles to the volume textures that can be used as source and destination volume textures for volume texture blts.

See Remarks for <a href="https://msdn.microsoft.com/library/windows/hardware/ff545869">D3DHAL_DP2TEXBLT</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dhal.h (include D3dhal.h) |

## See Also

D3DDP2OP_VOLUMEBLT



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545869">D3DHAL_DP2TEXBLT</a>



<a href="https://msdn.microsoft.com/dd07e49c-ec1f-4ba6-8b17-80ce6d3c5813">D3dCreateSurfaceEx</a>



<a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a>