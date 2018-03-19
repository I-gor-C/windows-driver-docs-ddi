---
UID: NS:d3d10umddi.D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW
title: D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW
author: windows-driver-content
description: Describes the video processor's output view.
old-location: display\d3d11_1ddiarg_createvideoprocessoroutputview.htm
old-project: display
ms.assetid: 3545AE6F-3D9E-4C3B-8C22-B823A18CC700
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW, D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW structure [Display Devices], PD3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW, PD3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW structure pointer [Display Devices], d3d10umddi/D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW, d3d10umddi/PD3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW, display.d3d11_1ddiarg_createvideoprocessoroutputview
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	d3d10umddi.h
api_name:
-	D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW
product: Windows
targetos: Windows
req.typenames: D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW
---

# D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW structure
Describes the video processor's output view.

## Syntax
````
typedef struct _D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW {
  D3D10DDI_HRESOURCE             hDrvResource;
  D3D11_1DDI_HVIDEOPROCESSORENUM hDrvVideoProcessorEnum;
  UINT                           MipSlice;
  UINT                           FirstArraySlice;
  UINT                           ArraySize;
} D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW, *PD3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW;
````

## Members


`hDrvResource`

A handle to the video decoder output resource.

`hDrvVideoProcessorEnum`

A handle to the video processor enumeration.

`MipSlice`

The identifier of the MIP-map slice.

`FirstArraySlice`

The identifier of the first array slice.

`ArraySize`

The number of array slices for the texture.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddiarg_createvideoprocessorinputview.md">D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW</a>