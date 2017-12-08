---
UID: NS.d3d12umddi.D3D12DDIARG_CREATE_PIPELINE_STATE_0033
title: D3D12DDIARG_CREATE_PIPELINE_STATE_0033
author: windows-driver-content
description: Creates a pipeline state.
old-location: display\d3d12ddiarg-create-pipeline-state-0033.htm
old-project: display
ms.assetid: 2a9108ab-5852-4053-9a7a-266ae1b1dced
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDIARG_CREATE_PIPELINE_STATE_0033, D3D12DDIARG_CREATE_PIPELINE_STATE_0033
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
req.alt-api: D3D12DDIARG_CREATE_PIPELINE_STATE_0033
req.alt-loc: d3d12umddi.h
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

# D3D12DDIARG_CREATE_PIPELINE_STATE_0033 structure



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>Creates a pipeline state.</p>


## -syntax

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


## -struct-fields
<dl>

### -field hComputeShader

<dd>
<p>The compute shader.</p>
</dd>

### -field hVertexShader

<dd>
<p>The vertex shader.</p>
</dd>

### -field hPixelShader

<dd>
<p>The pixel shader.</p>
</dd>

### -field hDomainShader

<dd>
<p>The domain shader.</p>
</dd>

### -field hHullShader

<dd>
<p>The hull shader.</p>
</dd>

### -field hGeometryShader

<dd>
<p>The geometry shader.</p>
</dd>

### -field hRootSignature

<dd>
<p>The root signature.</p>
</dd>

### -field hBlendState

<dd>
<p>The blend state.</p>
</dd>

### -field SampleMask

<dd>
<p>The sample mask.</p>
</dd>

### -field hRasterizerState

<dd>
<p>The rasterizer state.</p>
</dd>

### -field hDepthStencilState

<dd>
<p>The depth stencil state.</p>
</dd>

### -field hElementLayout

<dd>
<p>The element layout.</p>
</dd>

### -field IBStripCutValue

<dd>
<p>The index buffer strip cut value.</p>
</dd>

### -field PrimitiveTopologyType

<dd>
<p>The primitive topology type.</p>
</dd>

### -field NumRenderTargets

<dd>
<p>The number of render targets.</p>
</dd>

### -field RTVFormats

<dd>
<p>The RTV formats.</p>
</dd>

### -field DSVFormat

<dd>
<p>The DSV format.</p>
</dd>

### -field SampleDesc

<dd>
<p>The sample description.</p>
</dd>

### -field NodeMask

<dd>
<p>Represents the set of nodes.</p>
</dd>

### -field LibraryReference

<dd>
<p>The library reference.</p>
</dd>

### -field ViewInstancingDesc

<dd>
<p>The view instancing description.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>