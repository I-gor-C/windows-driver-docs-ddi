---
UID: NS:dxgiddi.DXGI_DDI_ARG_BLT
title: DXGI_DDI_ARG_BLT
author: windows-driver-content
description: The DXGI_DDI_ARG_BLT structure describes the parameters of a bit-block transfer (bitblt).
old-location: display\dxgi_ddi_arg_blt.htm
old-project: display
ms.assetid: 695f2aff-cce3-4358-a9e2-48eea43e8ef5
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGI_DDI_ARG_BLT, DXGI_DDI_ARG_BLT structure [Display Devices], UMDisplayDriver_Dx10param_Structs_299fa1c4-8c06-4a7e-a81c-741eb2e8c00a.xml, display.dxgi_ddi_arg_blt, dxgiddi/DXGI_DDI_ARG_BLT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
-	dxgiddi.h
api_name:
-	DXGI_DDI_ARG_BLT
product:
- Windows
targetos: Windows
req.typenames: DXGI_DDI_ARG_BLT
---

# DXGI_DDI_ARG_BLT structure
The <b>DXGI_DDI_ARG_BLT</b> structure describes the parameters of a bit-block transfer (bitblt).

## Syntax
```
typedef struct DXGI_DDI_ARG_BLT {
  DXGI_DDI_HDEVICE       hDevice;
  DXGI_DDI_HRESOURCE     hDstResource;
  UINT                   DstSubresource;
  UINT                   DstLeft;
  UINT                   DstTop;
  UINT                   DstRight;
  UINT                   DstBottom;
  DXGI_DDI_HRESOURCE     hSrcResource;
  UINT                   SrcSubresource;
  DXGI_DDI_ARG_BLT_FLAGS Flags;
  DXGI_DDI_MODE_ROTATION Rotate;
};
```

## Members


`hDevice`

[in] A handle to the display device (graphics context) on which the driver performs the bitblt. The Direct3D runtime passes this handle to the driver in the <b>hDrvDevice</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541664">D3D10DDIARG_CREATEDEVICE</a> structure when the runtime calls the driver's <a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a> function to create the display device.

`hDstResource`

[in] A handle to the destination resource.

`DstSubresource`

[in] The index to the destination surface within the resource.

`DstLeft`

[in] The <i>x</i>-coordinate of the upper-left corner of the destination rectangle.

`DstTop`

[in] The <i>y</i>-coordinate of the upper-left corner of the destination rectangle.

`DstRight`

[in] The <i>x</i>-coordinate of the lower-right corner of the destination rectangle.

`DstBottom`

[in] The <i>y</i>-coordinate of the lower-right corner of the destination rectangle.

`hSrcResource`

[in] A handle to the source resource.

`SrcSubresource`

[in] The index to the source surface within the resource.

`Flags`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff557451">DXGI_DDI_ARG_BLT_FLAGS</a> structure that identifies the type of bitblt to perform.

`Rotate`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff557502">DXGI_DDI_MODE_ROTATION</a>-typed value that identifies the orientation of the display mode.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | dxgiddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff538252">BltDXGI</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557451">DXGI_DDI_ARG_BLT_FLAGS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557502">DXGI_DDI_MODE_ROTATION</a>