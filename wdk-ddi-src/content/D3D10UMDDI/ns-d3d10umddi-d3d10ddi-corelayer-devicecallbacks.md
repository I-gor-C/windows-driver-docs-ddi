---
UID: NS.d3d10umddi.D3D10DDI_CORELAYER_DEVICECALLBACKS
title: D3D10DDI_CORELAYER_DEVICECALLBACKS
author: windows-driver-content
description: The D3D10DDI_CORELAYER_DEVICECALLBACKS structure contains Microsoft Direct3D 10 runtime callback functions that the user-mode display driver can use.
old-location: display\d3d10ddi_corelayer_devicecallbacks.htm
ms.assetid: cced2221-7e8c-432a-9963-3b1de67037a3
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10DDI_CORELAYER_DEVICECALLBACKS
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
ms.keywords: D3D10DDI_CORELAYER_DEVICECALLBACKS, D3D10DDI_CORELAYER_DEVICECALLBACKS
req.iface: 
---

# D3D10DDI_CORELAYER_DEVICECALLBACKS structure



## -description
<p>The D3D10DDI_CORELAYER_DEVICECALLBACKS structure contains Microsoft Direct3D 10 runtime callback functions that the user-mode display driver can use.</p>


## -syntax

````
typedef struct D3D10DDI_CORELAYER_DEVICECALLBACKS {
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
} D3D10DDI_CORELAYER_DEVICECALLBACKS;
````


## -struct-fields
<dl>

### -field <b>pfnSetErrorCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function, which the driver uses to send errors back to the Direct3D 10 runtime because many of the driver's functions (in <a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>) return void.</p>
</dd>

### -field <b>pfnStateVsConstBufCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/43aa7188-d6aa-4890-8eac-1342a984005b">pfnStateVsConstBufCb</a> function.</p>
</dd>

### -field <b>pfnStatePsSrvCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/ed49ce47-c56d-4d38-8f2c-562841b8e804">pfnStatePsSrvCb</a> function.</p>
</dd>

### -field <b>pfnStatePsShaderCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/0865e79e-7df9-4dc7-a655-4fbd0af72030">pfnStatePsShaderCb</a> function.</p>
</dd>

### -field <b>pfnStatePsSamplerCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/8cf25918-1acf-40b6-be51-2c1afc419f2a">pfnStatePsSamplerCb</a> function.</p>
</dd>

### -field <b>pfnStateVsShaderCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/f43f7dea-26a6-4e3f-99e2-5e3488a621b0">pfnStateVsShaderCb</a> function.</p>
</dd>

### -field <b>pfnStatePsConstBufCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/f4670f69-5154-4f6b-ba98-2b91a16e7b2f">pfnStatePsConstBufCb</a> function.</p>
</dd>

### -field <b>pfnStateIaInputLayoutCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/fce49c60-8573-4a28-9d1c-5cf33d260db3">pfnStateIaInputLayoutCb</a> function.</p>
</dd>

### -field <b>pfnStateIaVertexBufCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/15068932-b769-4027-986f-195b569a23eb">pfnStateIaVertexBufCb</a> function. </p>
</dd>

### -field <b>pfnStateIaIndexBufCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/3925bf83-1900-4d88-8100-1ecaa952dead">pfnStateIaIndexBufCb</a> function. </p>
</dd>

### -field <b>pfnStateGsConstBufCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/02468226-f0a4-4f24-a7f9-61a3b67dffb1">pfnStateGsConstBufCb</a> function. </p>
</dd>

### -field <b>pfnStateGsShaderCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/2bcdc7bd-4327-4258-ad89-5e028cffd06b">pfnStateGsShaderCb</a> function. </p>
</dd>

### -field <b>pfnStateIaPrimitiveTopologyCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/5a394a5b-afbc-41f5-8013-ab228e6284f9">pfnStateIaPrimitiveTopologyCb</a> function. </p>
</dd>

### -field <b>pfnStateVsSrvCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/5102104e-b79c-40e5-87de-9ccf848288db">pfnStateVsSrvCb</a> function. </p>
</dd>

### -field <b>pfnStateVsSamplerCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/5f5dd2ee-72fb-450c-850a-f5546401cd96">pfnStateVsSamplerCb</a> function. </p>
</dd>

### -field <b>pfnStateGsSrvCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/4ab7444f-face-4ad0-a73c-18dd0b59a344">pfnStateGsSrvCb</a> function. </p>
</dd>

### -field <b>pfnStateGsSamplerCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/086c565e-2747-4bbe-a9e1-af38373c3232">pfnStateGsSamplerCb</a> function. </p>
</dd>

### -field <b>pfnStateOmRenderTargetsCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/d17cd31d-44a1-4f7d-82be-1201c0d5769f">pfnStateOmRenderTargetsCb</a> function. </p>
</dd>

### -field <b>pfnStateOmBlendStateCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/3cec9d99-0d15-4c61-9de2-ab203a56441d">pfnStateOmBlendStateCb</a> function. </p>
</dd>

### -field <b>pfnStateOmDepthStateCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/caa8ea5b-7167-444a-9d81-6e4ea9375dd6">pfnStateOmDepthStateCb</a> function. </p>
</dd>

### -field <b>pfnStateRsRastStateCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/2ce213a6-8075-4ad9-9f58-204c2f7fd8d9">pfnStateRsRastStateCb</a> function. </p>
</dd>

### -field <b>pfnStateSoTargetsCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/9000543b-00ab-4378-9fa5-d4fc7cb05b24">pfnStateSoTargetsCb</a> function. </p>
</dd>

### -field <b>pfnStateRsViewportsCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/9390ddca-4658-4853-a45c-9fb306bbdef8">pfnStateRsViewportsCb</a> function. </p>
</dd>

### -field <b>pfnStateRsScissorCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/4bb88e3c-2309-42f5-bc22-4c7182358e6e">pfnStateRsScissorCb</a> function. </p>
</dd>

### -field <b>pfnDisableDeferredStagingResourceDestruction</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/f0328782-9b5b-44e6-ac58-7eb72685aa52">pfnDisableDeferredStagingResourceDestruction</a> function. By default, the Direct3D 10 runtime defers the destruction of staging resources until the driver indicates that the hardware no longer requires them. The driver can call this function to disable this feature if the driver does not require the deferred destruction functionality. </p>
</dd>

### -field <b>pfnStateTextFilterSizeCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/f53f73bf-8297-4c56-81f9-443d10a6b701">pfnStateTextFilterSizeCb</a> function. </p>
</dd>
</dl>

## -remarks
<p>Because the Direct3D 10 runtime might change the function pointers dynamically, the user-mode display driver cannot cache the function pointers directly. </p>

<p>The driver uses the functions with "State" in their name to retrieve the current state of the pipeline. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
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
<a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541664">D3D10DDIARG_CREATEDEVICE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10DDI_CORELAYER_DEVICECALLBACKS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
