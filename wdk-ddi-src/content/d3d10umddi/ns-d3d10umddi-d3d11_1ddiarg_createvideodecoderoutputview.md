---
UID : NS:d3d10umddi.D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW
title : D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW
author : windows-driver-content
description : Describes the video decoder's output-view state.
old-location : display\d3d11_1ddiarg_createvideodecoderoutputview.htm
old-project : display
ms.assetid : 6DD555B1-01E8-48DE-B957-2752671B7EBB
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW, D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Windows
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW
req.alt-loc : d3d10umddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW
---

# D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW structure
Describes the video decoder's output-view state.

## Syntax
````
typedef struct _D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW {
  D3D10DDI_HRESOURCE hDrvResource;
  GUID               DecodeProfile;
  UINT               MipSlice;
  UINT               FirstArraySlice;
  UINT               ArraySize;
} D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW, *PD3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW;
````

## Members

        
            `ArraySize`

            The number of array slices for the texture.
        
            `DecodeProfile`

            The decode profile to be used in conjunction with the encryption.
        
            `FirstArraySlice`

            The identifier of the first array slice.
        
            `hDrvResource`

            A handle to the video decoder output resource.
        
            `MipSlice`

            The identifier of the MIP-map slice.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |