---
UID: NS:d3d12umddi.D3D12DDIARG_CREATE_PIPELINE_STATE_0033
title: D3D12DDIARG_CREATE_PIPELINE_STATE_0033
author: windows-driver-content
description: Creates a pipeline state.
old-location: display\d3d12ddiarg-create-pipeline-state-0033.htm
old-project: display
ms.assetid: 2a9108ab-5852-4053-9a7a-266ae1b1dced
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: D3D12DDIARG_CREATE_PIPELINE_STATE_0033, D3D12DDIARG_CREATE_PIPELINE_STATE_0033 structure [Display Devices], d3d12umddi/D3D12DDIARG_CREATE_PIPELINE_STATE_0033, display.d3d12ddiarg-create-pipeline-state-0033
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d12umddi.h
req.include-header: 
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
-	d3d12umddi.h
api_name:
-	D3D12DDIARG_CREATE_PIPELINE_STATE_0033
product: Windows
targetos: Windows
req.typenames: D3D12DDIARG_CREATE_PIPELINE_STATE_0033
---

# D3D12DDIARG_CREATE_PIPELINE_STATE_0033 structure
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

Creates a pipeline state.

## Syntax
````
typedef struct _D3D12DDIARG_CREATE_PIPELINE_STATE_0033 {
  D3D12DDI_HSHADER                       hComputeShader;
  D3D12DDI_HSHADER                       hVertexShader;
  D3D12DDI_HSHADER                       hPixelShader;
  D3D12DDI_HSHADER                       hDomainShader;
  D3D12DDI_HSHADER                       hHullShader;
  D3D12DDI_HSHADER                       hGeometryShader;
  D3D12DDI_HROOTSIGNATURE                hRootSignature;
  D3D12DDI_HBLENDSTATE                   hBlendState;
  UINT                                   SampleMask;
  D3D12DDI_HRASTERIZERSTATE              hRasterizerState;
  D3D12DDI_HDEPTHSTENCILSTATE            hDepthStencilState;
  D3D12DDI_HELEMENTLAYOUT                hElementLayout;
  D3D12DDI_INDEX_BUFFER_STRIP_CUT_VALUE  IBStripCutValue;
  D3D12DDI_PRIMITIVE_TOPOLOGY_TYPE       PrimitiveTopologyType;
  UINT                                   NumRenderTargets;
  DXGI_FORMAT [8]                        RTVFormats;
  DXGI_FORMAT                            DSVFormat;
  DXGI_SAMPLE_DESC                       SampleDesc;
  UINT                                   NodeMask;
  D3D12DDI_LIBRARY_REFERENCE_0010        LibraryReference;
  D3D12DDI_VIEW_INSTANCING_DESC          ViewInstancingDesc;
} D3D12DDIARG_CREATE_PIPELINE_STATE_0033, D3D12DDIARG_CREATE_PIPELINE_STATE_0033;
````

## Members


`DSVFormat`

The DSV format.

`hBlendState`

The blend state.

`hComputeShader`

The compute shader.

`hDepthStencilState`

The depth stencil state.

`hDomainShader`

The domain shader.

`hElementLayout`

The element layout.

`hGeometryShader`

The geometry shader.

`hHullShader`

The hull shader.

`hPixelShader`

The pixel shader.

`hRasterizerState`

The rasterizer state.

`hRootSignature`

The root signature.

`hVertexShader`

The vertex shader.

`IBStripCutValue`

The index buffer strip cut value.

`LibraryReference`

The library reference.

`NodeMask`

Represents the set of nodes.

`NumRenderTargets`

The number of render targets.

`PrimitiveTopologyType`

The primitive topology type.

`RTVFormats`

The RTV formats.

`SampleDesc`

The sample description.

`SampleMask`

The sample mask.

`ViewInstancingDesc`

The view instancing description.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d12umddi.h |