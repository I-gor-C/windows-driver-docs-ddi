---
UID: NS.d3d10umddi.D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS~r1
title: D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS
author: windows-driver-content
description: This structure contains the function table for the core layer device callback functions.
old-location: display\d3dwddm2_0ddi_corelayer_devicecallbacks.htm
old-project: display
ms.assetid: A8E60BF8-2DFE-479A-9DA9-C3D9B012EBE9
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS, D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS
req.alt-loc: D3d10umddi.h
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

# D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS structure



## -description
<p>This structure contains the function table for the core layer device callback functions.</p>


## -syntax

````
typedef struct D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS {
  PFND3D10DDI_SETERROR_CB                                      pfnSetErrorCb;
  PFND3D10DDI_STATE_VS_CONSTBUF_CB                             pfnStateVsConstBufCb;
  PFND3D10DDI_STATE_PS_SRV_CB                                  pfnStatePsSrvCb;
  PFND3D10DDI_STATE_PS_SHADER_CB                               pfnStatePsShaderCb;
  PFND3D10DDI_STATE_PS_SAMPLER_CB                              pfnStatePsSamplerCb;
  PFND3D10DDI_STATE_VS_SHADER_CB                               pfnStateVsShaderCb;
  PFND3D10DDI_STATE_PS_CONSTBUF_CB                             pfnStatePsConstBufCb;
  PFND3D10DDI_STATE_IA_INPUTLAYOUT_CB                          pfnStateIaInputLayoutCb;
  PFND3D10DDI_STATE_IA_VERTEXBUF_CB                            pfnStateIaVertexBufCb;
  PFND3D10DDI_STATE_IA_INDEXBUF_CB                             pfnStateIaIndexBufCb;
  PFND3D10DDI_STATE_GS_CONSTBUF_CB                             pfnStateGsConstBufCb;
  PFND3D10DDI_STATE_GS_SHADER_CB                               pfnStateGsShaderCb;
  PFND3D10DDI_STATE_IA_PRIMITIVE_TOPOLOGY_CB                   pfnStateIaPrimitiveTopologyCb;
  PFND3D10DDI_STATE_VS_SRV_CB                                  pfnStateVsSrvCb;
  PFND3D10DDI_STATE_VS_SAMPLER_CB                              pfnStateVsSamplerCb;
  PFND3D10DDI_STATE_GS_SRV_CB                                  pfnStateGsSrvCb;
  PFND3D10DDI_STATE_GS_SAMPLER_CB                              pfnStateGsSamplerCb;
  PFND3D10DDI_STATE_OM_RENDERTARGETS_CB                        pfnStateOmRenderTargetsCb;
  PFND3D10DDI_STATE_OM_BLENDSTATE_CB                           pfnStateOmBlendStateCb;
  PFND3D10DDI_STATE_OM_DEPTHSTATE_CB                           pfnStateOmDepthStateCb;
  PFND3D10DDI_STATE_RS_RASTSTATE_CB                            pfnStateRsRastStateCb;
  PFND3D10DDI_STATE_SO_TARGETS_CB                              pfnStateSoTargetsCb;
  PFND3D10DDI_STATE_RS_VIEWPORTS_CB                            pfnStateRsViewportsCb;
  PFND3D10DDI_STATE_RS_SCISSOR_CB                              pfnStateRsScissorCb;
  PFND3D10DDI_DISABLE_DEFERRED_STAGING_RESOURCE_DESTRUCTION_CB pfnDisableDeferredStagingResourceDestruction;
  PFND3D10DDI_STATE_TEXTFILTERSIZE_CB                          pfnStateTextFilterSizeCb;
  PFND3D11DDI_STATE_HS_SRV_CB                                  pfnStateHsSrvCb;
  PFND3D11DDI_STATE_HS_SHADER_CB                               pfnStateHsShaderCb;
  PFND3D11DDI_STATE_HS_SAMPLER_CB                              pfnStateHsSamplerCb;
  PFND3D11DDI_STATE_HS_CONSTBUF_CB                             pfnStateHsConstBufCb;
  PFND3D11DDI_STATE_DS_SRV_CB                                  pfnStateDsSrvCb;
  PFND3D11DDI_STATE_DS_SHADER_CB                               pfnStateDsShaderCb;
  PFND3D11DDI_STATE_DS_SAMPLER_CB                              pfnStateDsSamplerCb;
  PFND3D11DDI_STATE_DS_CONSTBUF_CB                             pfnStateDsConstBufCb;
  PFND3D11DDI_PERFORM_AMORTIZED_PROCESSING_CB                  pfnPerformAmortizedProcessingCb;
  PFND3D11DDI_STATE_CS_SRV_CB                                  pfnStateCsSrvCb;
  PFND3D11DDI_STATE_CS_UAV_CB                                  pfnStateCsUavCb;
  PFND3D11DDI_STATE_CS_SHADER_CB                               pfnStateCsShaderCb;
  PFND3D11DDI_STATE_CS_SAMPLER_CB                              pfnStateCsSamplerCb;
  PFND3D11DDI_STATE_CS_CONSTBUF_CB                             pfnStateCsConstBufCb;
  PFND3DWDDM2_0DDI_CREATECONTEXT_CB                            pfnCreateContextCb;
  PFND3DWDDM2_0DDI_CREATECONTEXTVIRTUAL_CB                     pfnCreateContextVirtualCb;
} D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS;
````


## -struct-fields
<dl>

### -field pfnSetErrorCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> function.</p>
</dd>

### -field pfnStateVsConstBufCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-vs-constbuf-cb.md">pfnStateVsConstBufCb</a> function.</p>
</dd>

### -field pfnStatePsSrvCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-ps-srv-cb.md">pfnStatePsSrvCb</a> function.</p>
</dd>

### -field pfnStatePsShaderCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-ps-shader-cb.md">pfnStatePsShaderCb</a> function.</p>
</dd>

### -field pfnStatePsSamplerCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-ps-sampler-cb.md">pfnStatePsSamplerCb</a> function.</p>
</dd>

### -field pfnStateVsShaderCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-vs-shader-cb.md">pfnStateVsShaderCb</a> function.</p>
</dd>

### -field pfnStatePsConstBufCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-ps-constbuf-cb.md">pfnStatePsConstBufCb</a> function.</p>
</dd>

### -field pfnStateIaInputLayoutCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-ia-inputlayout-cb.md">pfnStateIaInputLayoutCb</a> function.</p>
</dd>

### -field pfnStateIaVertexBufCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-ia-vertexbuf-cb.md">pfnStateIaVertexBufCb</a> function.</p>
</dd>

### -field pfnStateIaIndexBufCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-ia-indexbuf-cb.md">pfnStateIaIndexBufCb</a> function.</p>
</dd>

### -field pfnStateGsConstBufCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-gs-constbuf-cb.md">pfnStateGsConstBufCb</a> function.</p>
</dd>

### -field pfnStateGsShaderCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-gs-shader-cb.md">pfnStateGsShaderCb</a> function.</p>
</dd>

### -field pfnStateIaPrimitiveTopologyCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-ia-primitive-topology-cb.md">pfnStateIaPrimitiveTopologyCb</a> function.</p>
</dd>

### -field pfnStateVsSrvCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-vs-srv-cb.md">pfnStateVsSrvCb</a> function.</p>
</dd>

### -field pfnStateVsSamplerCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-vs-sampler-cb.md">pfnStateVsSamplerCb</a> function.</p>
</dd>

### -field pfnStateGsSrvCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-gs-srv-cb.md">pfnStateGsSrvCb</a> function.</p>
</dd>

### -field pfnStateGsSamplerCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-gs-sampler-cb.md">pfnStateGsSamplerCb</a> function.</p>
</dd>

### -field pfnStateOmRenderTargetsCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-om-rendertargets-cb.md">pfnStateOmRenderTargetsCb</a> function.</p>
</dd>

### -field pfnStateOmBlendStateCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-om-blendstate-cb.md">pfnStateOmBlendStateCb</a> function.</p>
</dd>

### -field pfnStateOmDepthStateCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-om-depthstate-cb.md">pfnStateOmDepthStateCb</a> function.</p>
</dd>

### -field pfnStateRsRastStateCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-rs-raststate-cb.md">pfnStateRsRastStateCb</a> function.</p>
</dd>

### -field pfnStateSoTargetsCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-so-targets-cb.md">pfnStateSoTargetsCb</a> function.</p>
</dd>

### -field pfnStateRsViewportsCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-rs-viewports-cb.md">pfnStateRsViewportsCb</a> function.</p>
</dd>

### -field pfnStateRsScissorCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-rs-scissor-cb.md">pfnStateRsScissorCb</a> function.</p>
</dd>

### -field pfnDisableDeferredStagingResourceDestruction

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-disable-deferred-staging-resource-destruction-cb.md">pfnDisableDeferredStagingResourceDestruction</a> function.</p>
</dd>

### -field pfnStateTextFilterSizeCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-textfiltersize-cb.md">pfnStateTextFilterSizeCb</a> function.</p>
</dd>

### -field pfnStateHsSrvCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-hs-srv-cb.md">pfnStateHsSrvCb</a> function.</p>
</dd>

### -field pfnStateHsShaderCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-hs-shader-cb.md">pfnStateHsShaderCb</a> function.</p>
</dd>

### -field pfnStateHsSamplerCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-hs-sampler-cb.md">pfnStateHsSamplerCb</a> function.</p>
</dd>

### -field pfnStateHsConstBufCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-hs-constbuf-cb.md">pfnStateHsConstBufCb</a> function.</p>
</dd>

### -field pfnStateDsSrvCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-ds-srv-cb.md">pfnStateDsSrvCb</a> function.</p>
</dd>

### -field pfnStateDsShaderCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-ds-shader-cb.md">pfnStateDsShaderCb</a> function.</p>
</dd>

### -field pfnStateDsSamplerCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-ds-sampler-cb.md">pfnStateDsSamplerCb</a> function.</p>
</dd>

### -field pfnStateDsConstBufCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-ds-constbuf-cb.md">pfnStateDsConstBufCb</a> function.</p>
</dd>

### -field pfnPerformAmortizedProcessingCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-perform-amortized-processing-cb.md">pfnPerformAmortizedProcessingCb</a> function.</p>
</dd>

### -field pfnStateCsSrvCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-cs-srv-cb.md">pfnStateCsSrvCb</a> function.</p>
</dd>

### -field pfnStateCsUavCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-cs-uav-cb.md">pfnStateCsUavCb</a> function.</p>
</dd>

### -field pfnStateCsShaderCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-cs-shader-cb.md">pfnStateCsShaderCb</a> function.</p>
</dd>

### -field pfnStateCsSamplerCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-cs-sampler-cb.md">pfnStateCsSamplerCb</a> function.</p>
</dd>

### -field pfnStateCsConstBufCb

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-cs-constbuf-cb.md">pfnStateCsConstBufCb</a> function.</p>
</dd>

### -field pfnCreateContextCb

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a> function.</p>
</dd>

### -field pfnCreateContextVirtualCb

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createcontextvirtualcb.md">pfnCreateContextVirtualCb</a> function.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>