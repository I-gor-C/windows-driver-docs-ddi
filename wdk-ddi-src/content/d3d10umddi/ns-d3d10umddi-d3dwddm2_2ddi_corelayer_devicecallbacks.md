---
UID: NS:d3d10umddi.D3DWDDM2_2DDI_CORELAYER_DEVICECALLBACKS
title: D3DWDDM2_2DDI_CORELAYER_DEVICECALLBACKS
author: windows-driver-content
description: Specifies core layer device callback functions.
old-location: display\d3dwddm2_2ddi_corelayer_devicecallbacks.htm
old-project: display
ms.assetid: B42DA194-690F-41A6-AC11-71224887A2E4
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DWDDM2_2DDI_CORELAYER_DEVICECALLBACKS, D3DWDDM2_2DDI_CORELAYER_DEVICECALLBACKS structure [Display Devices], d3d10umddi/D3DWDDM2_2DDI_CORELAYER_DEVICECALLBACKS, display.d3dwddm2_2ddi_corelayer_devicecallbacks
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
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
-	d3d10umddi.h
api_name:
-	D3DWDDM2_2DDI_CORELAYER_DEVICECALLBACKS
product: Windows
targetos: Windows
req.typenames: D3DWDDM2_2DDI_CORELAYER_DEVICECALLBACKS
---

# D3DWDDM2_2DDI_CORELAYER_DEVICECALLBACKS structure
Specifies core layer device callback functions.

## Syntax
```
typedef struct D3DWDDM2_2DDI_CORELAYER_DEVICECALLBACKS {
  PFND3D10DDI_SETERROR_CB                                      pfnSetErrorCb;
  PFND3D10DDI_STATE_VS_CONSTBUF_CB                             pfnStateVsConstBufCb;
  PFND3D10DDI_STATE_PS_SRV_CB                                  pfnStatePsSrvCb;
  PFND3D10DDI_STATE_PS_SHADER_CB                               pfnStatePsShaderCb;
  PFND3D10DDI_STATE_PS_SAMPLER_CB                              pfnStatePsSamplerCb;
  PFND3D10DDI_STATE_VS_SHADER_CB                               pfnStateVsShaderCb;
  PFND3D10DDI_STATE_PS_CONSTBUF_CB                             pfnStatePsConstBufCb;
  PFND3D10DDI_STATE_IA_INPUTLAYOUT_CB                          pfnStateIaInputLayoutCb;
  PFND3D10DDI_STATE_IA_VERTEXBUF_CB                            pfnStateIaVertexBufCb;
  PFND3D10DDI_STATE_IA_INDEXBUF_CB                             pfnStateIaIndexBufCb;
  PFND3D10DDI_STATE_GS_CONSTBUF_CB                             pfnStateGsConstBufCb;
  PFND3D10DDI_STATE_GS_SHADER_CB                               pfnStateGsShaderCb;
  PFND3D10DDI_STATE_IA_PRIMITIVE_TOPOLOGY_CB                   pfnStateIaPrimitiveTopologyCb;
  PFND3D10DDI_STATE_VS_SRV_CB                                  pfnStateVsSrvCb;
  PFND3D10DDI_STATE_VS_SAMPLER_CB                              pfnStateVsSamplerCb;
  PFND3D10DDI_STATE_GS_SRV_CB                                  pfnStateGsSrvCb;
  PFND3D10DDI_STATE_GS_SAMPLER_CB                              pfnStateGsSamplerCb;
  PFND3D10DDI_STATE_OM_RENDERTARGETS_CB                        pfnStateOmRenderTargetsCb;
  PFND3D10DDI_STATE_OM_BLENDSTATE_CB                           pfnStateOmBlendStateCb;
  PFND3D10DDI_STATE_OM_DEPTHSTATE_CB                           pfnStateOmDepthStateCb;
  PFND3D10DDI_STATE_RS_RASTSTATE_CB                            pfnStateRsRastStateCb;
  PFND3D10DDI_STATE_SO_TARGETS_CB                              pfnStateSoTargetsCb;
  PFND3D10DDI_STATE_RS_VIEWPORTS_CB                            pfnStateRsViewportsCb;
  PFND3D10DDI_STATE_RS_SCISSOR_CB                              pfnStateRsScissorCb;
  PFND3D10DDI_DISABLE_DEFERRED_STAGING_RESOURCE_DESTRUCTION_CB pfnDisableDeferredStagingResourceDestruction;
  PFND3D10DDI_STATE_TEXTFILTERSIZE_CB                          pfnStateTextFilterSizeCb;
  PFND3D11DDI_STATE_HS_SRV_CB                                  pfnStateHsSrvCb;
  PFND3D11DDI_STATE_HS_SHADER_CB                               pfnStateHsShaderCb;
  PFND3D11DDI_STATE_HS_SAMPLER_CB                              pfnStateHsSamplerCb;
  PFND3D11DDI_STATE_HS_CONSTBUF_CB                             pfnStateHsConstBufCb;
  PFND3D11DDI_STATE_DS_SRV_CB                                  pfnStateDsSrvCb;
  PFND3D11DDI_STATE_DS_SHADER_CB                               pfnStateDsShaderCb;
  PFND3D11DDI_STATE_DS_SAMPLER_CB                              pfnStateDsSamplerCb;
  PFND3D11DDI_STATE_DS_CONSTBUF_CB                             pfnStateDsConstBufCb;
  PFND3D11DDI_PERFORM_AMORTIZED_PROCESSING_CB                  pfnPerformAmortizedProcessingCb;
  PFND3D11DDI_STATE_CS_SRV_CB                                  pfnStateCsSrvCb;
  PFND3D11DDI_STATE_CS_UAV_CB                                  pfnStateCsUavCb;
  PFND3D11DDI_STATE_CS_SHADER_CB                               pfnStateCsShaderCb;
  PFND3D11DDI_STATE_CS_SAMPLER_CB                              pfnStateCsSamplerCb;
  PFND3D11DDI_STATE_CS_CONSTBUF_CB                             pfnStateCsConstBufCb;
  PFND3DWDDM2_0DDI_CREATECONTEXT_CB                            pfnCreateContextCb;
  PFND3DWDDM2_0DDI_CREATECONTEXTVIRTUAL_CB                     pfnCreateContextVirtualCb;
  PFND3DWDDM2_2DDI_SHADERCACHE_GET_VALUE_CB                    pfnShaderCacheGetValueCb;
  PFND3DWDDM2_2DDI_SHADERCACHE_STORE_VALUE_CB                  pfnShaderCacheStoreValueCb;
  PFND3DWDDM2_2DDI_SHADERCACHE_ADDREF_RELEASE_CB               pfnShaderCacheAddRefCb;
  PFND3DWDDM2_2DDI_SHADERCACHE_ADDREF_RELEASE_CB               pfnShaderCacheReleaseCb;
};
```

## Members


`pfnSetErrorCb`



`pfnStateVsConstBufCb`



`pfnStatePsSrvCb`



`pfnStatePsShaderCb`



`pfnStatePsSamplerCb`



`pfnStateVsShaderCb`



`pfnStatePsConstBufCb`



`pfnStateIaInputLayoutCb`



`pfnStateIaVertexBufCb`



`pfnStateIaIndexBufCb`



`pfnStateGsConstBufCb`



`pfnStateGsShaderCb`



`pfnStateIaPrimitiveTopologyCb`



`pfnStateVsSrvCb`



`pfnStateVsSamplerCb`



`pfnStateGsSrvCb`



`pfnStateGsSamplerCb`



`pfnStateOmRenderTargetsCb`



`pfnStateOmBlendStateCb`



`pfnStateOmDepthStateCb`



`pfnStateRsRastStateCb`



`pfnStateSoTargetsCb`



`pfnStateRsViewportsCb`



`pfnStateRsScissorCb`



`pfnDisableDeferredStagingResourceDestruction`



`pfnStateTextFilterSizeCb`



`pfnStateHsSrvCb`



`pfnStateHsShaderCb`



`pfnStateHsSamplerCb`



`pfnStateHsConstBufCb`



`pfnStateDsSrvCb`



`pfnStateDsShaderCb`



`pfnStateDsSamplerCb`



`pfnStateDsConstBufCb`



`pfnPerformAmortizedProcessingCb`



`pfnStateCsSrvCb`



`pfnStateCsUavCb`



`pfnStateCsShaderCb`



`pfnStateCsSamplerCb`



`pfnStateCsConstBufCb`



`pfnCreateContextCb`



`pfnCreateContextVirtualCb`



`pfnShaderCacheGetValueCb`



`pfnShaderCacheStoreValueCb`



`pfnShaderCacheAddRefCb`

A callback function that adds a reference to the shader cache.

`pfnShaderCacheReleaseCb`

A callback function that releases a reference to a cache.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d10umddi.h |