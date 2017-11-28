---
UID: NS.d3d10umddi.D3D11DDI_CORELAYER_DEVICECALLBACKS~r1
title: D3D11DDI_CORELAYER_DEVICECALLBACKS
author: windows-driver-content
description: The D3D11DDI_CORELAYER_DEVICECALLBACKS structure contains Microsoft Direct3D 11 runtime callback functions that the user-mode display driver can use.
old-location: display\d3d11ddi_corelayer_devicecallbacks.htm
old-project: display
ms.assetid: 7a10b7e0-b062-4ec9-9883-7042f6e55505
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D11DDI_CORELAYER_DEVICECALLBACKS, D3D11DDI_CORELAYER_DEVICECALLBACKS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D11DDI_CORELAYER_DEVICECALLBACKS is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11DDI_CORELAYER_DEVICECALLBACKS
req.alt-loc: d3d10umddi.h
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

# D3D11DDI_CORELAYER_DEVICECALLBACKS structure



## -description
<p>The D3D11DDI_CORELAYER_DEVICECALLBACKS structure contains Microsoft Direct3D 11 runtime callback functions that the user-mode display driver can use.</p>


## -syntax

````
typedef struct D3D11DDI_CORELAYER_DEVICECALLBACKS {
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
} D3D11DDI_CORELAYER_DEVICECALLBACKS;
````


## -struct-fields
<dl>

### -field <b>pfnSetErrorCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> function, which the driver uses to send errors back to the Direct3D 11 runtime because many of the driver's functions (in <a href="https://msdn.microsoft.com/library/windows/hardware/ff542141">D3D11DDI_DEVICEFUNCS</a>) return void.</p>
</dd>

### -field <b>pfnStateVsConstBufCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-vs-constbuf-cb.md">pfnStateVsConstBufCb</a> function.</p>
</dd>

### -field <b>pfnStatePsSrvCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-ps-srv-cb.md">pfnStatePsSrvCb</a> function.</p>
</dd>

### -field <b>pfnStatePsShaderCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-ps-shader-cb.md">pfnStatePsShaderCb</a> function.</p>
</dd>

### -field <b>pfnStatePsSamplerCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-ps-sampler-cb.md">pfnStatePsSamplerCb</a> function.</p>
</dd>

### -field <b>pfnStateVsShaderCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-vs-shader-cb.md">pfnStateVsShaderCb</a> function.</p>
</dd>

### -field <b>pfnStatePsConstBufCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-ps-constbuf-cb.md">pfnStatePsConstBufCb</a> function.</p>
</dd>

### -field <b>pfnStateIaInputLayoutCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-ia-inputlayout-cb.md">pfnStateIaInputLayoutCb</a> function.</p>
</dd>

### -field <b>pfnStateIaVertexBufCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-ia-vertexbuf-cb.md">pfnStateIaVertexBufCb</a> function. </p>
</dd>

### -field <b>pfnStateIaIndexBufCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-ia-indexbuf-cb.md">pfnStateIaIndexBufCb</a> function. </p>
</dd>

### -field <b>pfnStateGsConstBufCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-gs-constbuf-cb.md">pfnStateGsConstBufCb</a> function. </p>
</dd>

### -field <b>pfnStateGsShaderCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-gs-shader-cb.md">pfnStateGsShaderCb</a> function. </p>
</dd>

### -field <b>pfnStateIaPrimitiveTopologyCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-ia-primitive-topology-cb.md">pfnStateIaPrimitiveTopologyCb</a> function. </p>
</dd>

### -field <b>pfnStateVsSrvCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-vs-srv-cb.md">pfnStateVsSrvCb</a> function. </p>
</dd>

### -field <b>pfnStateVsSamplerCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-vs-sampler-cb.md">pfnStateVsSamplerCb</a> function. </p>
</dd>

### -field <b>pfnStateGsSrvCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-gs-srv-cb.md">pfnStateGsSrvCb</a> function. </p>
</dd>

### -field <b>pfnStateGsSamplerCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-gs-sampler-cb.md">pfnStateGsSamplerCb</a> function. </p>
</dd>

### -field <b>pfnStateOmRenderTargetsCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-om-rendertargets-cb.md">pfnStateOmRenderTargetsCb</a> function. </p>
</dd>

### -field <b>pfnStateOmBlendStateCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-om-blendstate-cb.md">pfnStateOmBlendStateCb</a> function. </p>
</dd>

### -field <b>pfnStateOmDepthStateCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-om-depthstate-cb.md">pfnStateOmDepthStateCb</a> function. </p>
</dd>

### -field <b>pfnStateRsRastStateCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-rs-raststate-cb.md">pfnStateRsRastStateCb</a> function. </p>
</dd>

### -field <b>pfnStateSoTargetsCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-so-targets-cb.md">pfnStateSoTargetsCb</a> function. </p>
</dd>

### -field <b>pfnStateRsViewportsCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-rs-viewports-cb.md">pfnStateRsViewportsCb</a> function. </p>
</dd>

### -field <b>pfnStateRsScissorCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-rs-scissor-cb.md">pfnStateRsScissorCb</a> function. </p>
</dd>

### -field <b>pfnDisableDeferredStagingResourceDestruction</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-disable-deferred-staging-resource-destruction-cb.md">pfnDisableDeferredStagingResourceDestruction</a> function. By default, the Direct3D 10 runtime defers the destruction of staging resources until the driver indicates that the hardware no longer requires them. The driver can call this function to disable this feature if the driver does not require the deferred destruction functionality. </p>
</dd>

### -field <b>pfnStateTextFilterSizeCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-state-textfiltersize-cb.md">pfnStateTextFilterSizeCb</a> function. </p>
<p><b>The following functions are supported beginning with Windows 7:  </b></p>
</dd>

### -field <b>pfnStateHsSrvCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-hs-srv-cb.md">pfnStateHsSrvCb</a> function. </p>
</dd>

### -field <b>pfnStateHsShaderCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-hs-shader-cb.md">pfnStateHsShaderCb</a> function. </p>
</dd>

### -field <b>pfnStateHsSamplerCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-hs-sampler-cb.md">pfnStateHsSamplerCb</a> function. </p>
</dd>

### -field <b>pfnStateHsConstBufCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-hs-constbuf-cb.md">pfnStateHsConstBufCb</a> function. </p>
</dd>

### -field <b>pfnStateDsSrvCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-ds-srv-cb.md">pfnStateDsSrvCb</a> function. </p>
</dd>

### -field <b>pfnStateDsShaderCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-ds-shader-cb.md">pfnStateDsShaderCb</a> function. </p>
</dd>

### -field <b>pfnStateDsSamplerCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-ds-sampler-cb.md">pfnStateDsSamplerCb</a> function. </p>
</dd>

### -field <b>pfnStateDsConstBufCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-ds-constbuf-cb.md">pfnStateDsConstBufCb</a> function. </p>
</dd>

### -field <b>pfnPerformAmortizedProcessingCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-perform-amortized-processing-cb.md">pfnPerformAmortizedProcessingCb</a> function. </p>
</dd>

### -field <b>pfnStateCsSrvCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-cs-srv-cb.md">pfnStateCsSrvCb</a> function. </p>
</dd>

### -field <b>pfnStateCsUavCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-cs-uav-cb.md">pfnStateCsUavCb</a> function. </p>
</dd>

### -field <b>pfnStateCsShaderCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-cs-shader-cb.md">pfnStateCsShaderCb</a> function. </p>
</dd>

### -field <b>pfnStateCsSamplerCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-cs-sampler-cb.md">pfnStateCsSamplerCb</a> function. </p>
</dd>

### -field <b>pfnStateCsConstBufCb</b>

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-state-cs-constbuf-cb.md">pfnStateCsConstBufCb</a> function. </p>
</dd>
</dl>

## -remarks
<p>Because the Direct3D 11 runtime might change the function pointers dynamically, the user-mode display driver cannot cache the function pointers directly. </p>

<p>The driver uses the functions with "State" in their name to retrieve the current state of the pipeline. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3D11DDI_CORELAYER_DEVICECALLBACKS is supported beginning with the Windows 7 operating system. </p>
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

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542141">D3D11DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541664">D3D10DDIARG_CREATEDEVICE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11DDI_CORELAYER_DEVICECALLBACKS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
