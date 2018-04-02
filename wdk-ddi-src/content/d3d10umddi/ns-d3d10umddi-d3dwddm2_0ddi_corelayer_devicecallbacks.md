---
UID: NS:d3d10umddi.D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS
title: D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS
author: windows-driver-content
description: This structure contains the function table for the core layer device callback functions.
old-location: display\d3dwddm2_0ddi_corelayer_devicecallbacks.htm
old-project: display
ms.assetid: A8E60BF8-2DFE-479A-9DA9-C3D9B012EBE9
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS, D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS structure [Display Devices], d3d10umddi/D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS, display.d3dwddm2_0ddi_corelayer_devicecallbacks
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
-	D3d10umddi.h
api_name:
-	D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS
product:
- Windows
targetos: Windows
req.typenames: D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS
---

# D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS structure
This structure contains the function table for the core layer device callback functions.

## Syntax
```
typedef struct D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS {
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
};
```

## Members


`pfnSetErrorCb`

A pointer to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function.

`pfnStateVsConstBufCb`

A pointer to the <a href="https://msdn.microsoft.com/43aa7188-d6aa-4890-8eac-1342a984005b">pfnStateVsConstBufCb</a> function.

`pfnStatePsSrvCb`

A pointer to the <a href="https://msdn.microsoft.com/ed49ce47-c56d-4d38-8f2c-562841b8e804">pfnStatePsSrvCb</a> function.

`pfnStatePsShaderCb`

A pointer to the <a href="https://msdn.microsoft.com/0865e79e-7df9-4dc7-a655-4fbd0af72030">pfnStatePsShaderCb</a> function.

`pfnStatePsSamplerCb`

A pointer to the <a href="https://msdn.microsoft.com/8cf25918-1acf-40b6-be51-2c1afc419f2a">pfnStatePsSamplerCb</a> function.

`pfnStateVsShaderCb`

A pointer to the <a href="https://msdn.microsoft.com/f43f7dea-26a6-4e3f-99e2-5e3488a621b0">pfnStateVsShaderCb</a> function.

`pfnStatePsConstBufCb`

A pointer to the <a href="https://msdn.microsoft.com/f4670f69-5154-4f6b-ba98-2b91a16e7b2f">pfnStatePsConstBufCb</a> function.

`pfnStateIaInputLayoutCb`

A pointer to the <a href="https://msdn.microsoft.com/fce49c60-8573-4a28-9d1c-5cf33d260db3">pfnStateIaInputLayoutCb</a> function.

`pfnStateIaVertexBufCb`

A pointer to the <a href="https://msdn.microsoft.com/15068932-b769-4027-986f-195b569a23eb">pfnStateIaVertexBufCb</a> function.

`pfnStateIaIndexBufCb`

A pointer to the <a href="https://msdn.microsoft.com/3925bf83-1900-4d88-8100-1ecaa952dead">pfnStateIaIndexBufCb</a> function.

`pfnStateGsConstBufCb`

A pointer to the <a href="https://msdn.microsoft.com/02468226-f0a4-4f24-a7f9-61a3b67dffb1">pfnStateGsConstBufCb</a> function.

`pfnStateGsShaderCb`

A pointer to the <a href="https://msdn.microsoft.com/2bcdc7bd-4327-4258-ad89-5e028cffd06b">pfnStateGsShaderCb</a> function.

`pfnStateIaPrimitiveTopologyCb`

A pointer to the <a href="https://msdn.microsoft.com/5a394a5b-afbc-41f5-8013-ab228e6284f9">pfnStateIaPrimitiveTopologyCb</a> function.

`pfnStateVsSrvCb`

A pointer to the <a href="https://msdn.microsoft.com/5102104e-b79c-40e5-87de-9ccf848288db">pfnStateVsSrvCb</a> function.

`pfnStateVsSamplerCb`

A pointer to the <a href="https://msdn.microsoft.com/5f5dd2ee-72fb-450c-850a-f5546401cd96">pfnStateVsSamplerCb</a> function.

`pfnStateGsSrvCb`

A pointer to the <a href="https://msdn.microsoft.com/4ab7444f-face-4ad0-a73c-18dd0b59a344">pfnStateGsSrvCb</a> function.

`pfnStateGsSamplerCb`

A pointer to the <a href="https://msdn.microsoft.com/086c565e-2747-4bbe-a9e1-af38373c3232">pfnStateGsSamplerCb</a> function.

`pfnStateOmRenderTargetsCb`

A pointer to the <a href="https://msdn.microsoft.com/d17cd31d-44a1-4f7d-82be-1201c0d5769f">pfnStateOmRenderTargetsCb</a> function.

`pfnStateOmBlendStateCb`

A pointer to the <a href="https://msdn.microsoft.com/3cec9d99-0d15-4c61-9de2-ab203a56441d">pfnStateOmBlendStateCb</a> function.

`pfnStateOmDepthStateCb`

A pointer to the <a href="https://msdn.microsoft.com/caa8ea5b-7167-444a-9d81-6e4ea9375dd6">pfnStateOmDepthStateCb</a> function.

`pfnStateRsRastStateCb`

A pointer to the <a href="https://msdn.microsoft.com/2ce213a6-8075-4ad9-9f58-204c2f7fd8d9">pfnStateRsRastStateCb</a> function.

`pfnStateSoTargetsCb`

A pointer to the <a href="https://msdn.microsoft.com/9000543b-00ab-4378-9fa5-d4fc7cb05b24">pfnStateSoTargetsCb</a> function.

`pfnStateRsViewportsCb`

A pointer to the <a href="https://msdn.microsoft.com/9390ddca-4658-4853-a45c-9fb306bbdef8">pfnStateRsViewportsCb</a> function.

`pfnStateRsScissorCb`

A pointer to the <a href="https://msdn.microsoft.com/4bb88e3c-2309-42f5-bc22-4c7182358e6e">pfnStateRsScissorCb</a> function.

`pfnDisableDeferredStagingResourceDestruction`

A pointer to the <a href="https://msdn.microsoft.com/f0328782-9b5b-44e6-ac58-7eb72685aa52">pfnDisableDeferredStagingResourceDestruction</a> function.

`pfnStateTextFilterSizeCb`

A pointer to the <a href="https://msdn.microsoft.com/f53f73bf-8297-4c56-81f9-443d10a6b701">pfnStateTextFilterSizeCb</a> function.

`pfnStateHsSrvCb`

A pointer to the <a href="https://msdn.microsoft.com/93a0a6b2-6a1a-4cef-ad7e-c5b606d11c17">pfnStateHsSrvCb</a> function.

`pfnStateHsShaderCb`

A pointer to the <a href="https://msdn.microsoft.com/74b243a2-722b-4eec-b382-936a6f2f990e">pfnStateHsShaderCb</a> function.

`pfnStateHsSamplerCb`

A pointer to the <a href="https://msdn.microsoft.com/95475c7a-874c-45e9-ab92-1c3983315446">pfnStateHsSamplerCb</a> function.

`pfnStateHsConstBufCb`

A pointer to the <a href="https://msdn.microsoft.com/2f817497-7334-47ef-aa9d-d43386aa4751">pfnStateHsConstBufCb</a> function.

`pfnStateDsSrvCb`

A pointer to the <a href="https://msdn.microsoft.com/23f92c9a-7f2c-4340-ad5e-101b13883bea">pfnStateDsSrvCb</a> function.

`pfnStateDsShaderCb`

A pointer to the <a href="https://msdn.microsoft.com/3b50f462-667e-4772-89bb-32d01e1bb7fc">pfnStateDsShaderCb</a> function.

`pfnStateDsSamplerCb`

A pointer to the <a href="https://msdn.microsoft.com/975da57f-c859-46b0-b98f-400aaf99098d">pfnStateDsSamplerCb</a> function.

`pfnStateDsConstBufCb`

A pointer to the <a href="https://msdn.microsoft.com/8170be69-3e75-4e33-a123-3039e3f9d0c0">pfnStateDsConstBufCb</a> function.

`pfnPerformAmortizedProcessingCb`

A pointer to the <a href="https://msdn.microsoft.com/6b9fd47f-c6b6-4541-a014-0cd6604eb3b3">pfnPerformAmortizedProcessingCb</a> function.

`pfnStateCsSrvCb`

A pointer to the <a href="https://msdn.microsoft.com/6bb0b6e7-4195-41a0-b614-b777acf3fd35">pfnStateCsSrvCb</a> function.

`pfnStateCsUavCb`

A pointer to the <a href="https://msdn.microsoft.com/2ff9e226-2981-4670-9164-7138f25528a0">pfnStateCsUavCb</a> function.

`pfnStateCsShaderCb`

A pointer to the <a href="https://msdn.microsoft.com/ae06ffb3-3ed5-4117-8373-e41a45be37d1">pfnStateCsShaderCb</a> function.

`pfnStateCsSamplerCb`

A pointer to the <a href="https://msdn.microsoft.com/f041a99b-73d7-4fc4-8530-c94d6bbd1f03">pfnStateCsSamplerCb</a> function.

`pfnStateCsConstBufCb`

A pointer to the <a href="https://msdn.microsoft.com/13eeceff-e19e-4653-b29d-87567e486c28">pfnStateCsConstBufCb</a> function.

`pfnCreateContextCb`

A pointer to the <a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a> function.

`pfnCreateContextVirtualCb`

A pointer to the <a href="https://msdn.microsoft.com/7787FEDF-E18C-4120-A073-A13933856F57">pfnCreateContextVirtualCb</a> function.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |