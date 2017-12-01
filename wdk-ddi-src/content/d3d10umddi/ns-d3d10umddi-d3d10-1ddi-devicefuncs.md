---
UID: NS.d3d10umddi.D3D10_1DDI_DEVICEFUNCS
title: D3D10_1DDI_DEVICEFUNCS
author: windows-driver-content
description: The D3D10_1DDI_DEVICEFUNCS structure contains functions that a user-mode display driver that is optimized for the Microsoft Direct3D version 10.1 runtime can implement to render graphics primitives and process state changes.
old-location: display\d3d10_1ddi_devicefuncs.htm
old-project: display
ms.assetid: 6de52d56-deca-4623-81a7-a043b8a85dc5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D10_1DDI_DEVICEFUNCS,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D10_1DDI_DEVICEFUNCS is supported on Windows Vista with Service Pack 1 (SP1) and later versions and Windows Server 2008 and later versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10_1DDI_DEVICEFUNCS
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

# D3D10_1DDI_DEVICEFUNCS structure



## -description
<p>The D3D10_1DDI_DEVICEFUNCS structure contains functions that a user-mode display driver that is optimized for the Microsoft Direct3D version 10.1 runtime can implement to render graphics primitives and process state changes.</p>


## -syntax

````
typedef struct D3D10_1DDI_DEVICEFUNCS {
  PFND3D10DDI_RESOURCEUPDATESUBRESOURCEUP               pfnDefaultConstantBufferUpdateSubresourceUP;
  PFND3D10DDI_SETCONSTANTBUFFERS                        pfnVsSetConstantBuffers;
  PFND3D10DDI_SETSHADERRESOURCES                        pfnPsSetShaderResources;
  PFND3D10DDI_SETSHADER                                 pfnPsSetShader;
  PFND3D10DDI_SETSAMPLERS                               pfnPsSetSamplers;
  PFND3D10DDI_SETSHADER                                 pfnVsSetShader;
  PFND3D10DDI_DRAWINDEXED                               pfnDrawIndexed;
  PFND3D10DDI_DRAW                                      pfnDraw;
  PFND3D10DDI_RESOURCEMAP                               pfnDynamicIABufferMapNoOverwrite;
  PFND3D10DDI_RESOURCEUNMAP                             pfnDynamicIABufferUnmap;
  PFND3D10DDI_RESOURCEMAP                               pfnDynamicConstantBufferMapDiscard;
  PFND3D10DDI_RESOURCEMAP                               pfnDynamicIABufferMapDiscard;
  PFND3D10DDI_RESOURCEUNMAP                             pfnDynamicConstantBufferUnmap;
  PFND3D10DDI_SETCONSTANTBUFFERS                        pfnPsSetConstantBuffers;
  PFND3D10DDI_SETINPUTLAYOUT                            pfnIaSetInputLayout;
  PFND3D10DDI_IA_SETVERTEXBUFFERS                       pfnIaSetVertexBuffers;
  PFND3D10DDI_IA_SETINDEXBUFFER                         pfnIaSetIndexBuffer;
  PFND3D10DDI_DRAWINDEXEDINSTANCED                      pfnDrawIndexedInstanced;
  PFND3D10DDI_DRAWINSTANCED                             pfnDrawInstanced;
  PFND3D10DDI_RESOURCEMAP                               pfnDynamicResourceMapDiscard;
  PFND3D10DDI_RESOURCEUNMAP                             pfnDynamicResourceUnmap;
  PFND3D10DDI_SETCONSTANTBUFFERS                        pfnGsSetConstantBuffers;
  PFND3D10DDI_SETSHADER                                 pfnGsSetShader;
  PFND3D10DDI_IA_SETTOPOLOGY                            pfnIaSetTopology;
  PFND3D10DDI_RESOURCEMAP                               pfnStagingResourceMap;
  PFND3D10DDI_RESOURCEUNMAP                             pfnStagingResourceUnmap;
  PFND3D10DDI_SETSHADERRESOURCES                        pfnVsSetShaderResources;
  PFND3D10DDI_SETSAMPLERS                               pfnVsSetSamplers;
  PFND3D10DDI_SETSHADERRESOURCES                        pfnGsSetShaderResources;
  PFND3D10DDI_SETSAMPLERS                               pfnGsSetSamplers;
  PFND3D10DDI_SETRENDERTARGETS                          pfnSetRenderTargets;
  PFND3D10DDI_SHADERRESOURCEVIEWREADAFTERWRITEHAZARD    pfnShaderResourceViewReadAfterWriteHazard;
  PFND3D10DDI_RESOURCEREADAFTERWRITEHAZARD              pfnResourceReadAfterWriteHazard;
  PFND3D10DDI_SETBLENDSTATE                             pfnSetBlendState;
  PFND3D10DDI_SETDEPTHSTENCILSTATE                      pfnSetDepthStencilState;
  PFND3D10DDI_SETRASTERIZERSTATE                        pfnSetRasterizerState;
  PFND3D10DDI_QUERYEND                                  pfnQueryEnd;
  PFND3D10DDI_QUERYBEGIN                                pfnQueryBegin;
  PFND3D10DDI_RESOURCECOPYREGION                        pfnResourceCopyRegion;
  PFND3D10DDI_RESOURCEUPDATESUBRESOURCEUP               pfnResourceUpdateSubresourceUP;
  PFND3D10DDI_SO_SETTARGETS                             pfnSoSetTargets;
  PFND3D10DDI_DRAWAUTO                                  pfnDrawAuto;
  PFND3D10DDI_SETVIEWPORTS                              pfnSetViewports;
  PFND3D10DDI_SETSCISSORRECTS                           pfnSetScissorRects;
  PFND3D10DDI_CLEARRENDERTARGETVIEW                     pfnClearRenderTargetView;
  PFND3D10DDI_CLEARDEPTHSTENCILVIEW                     pfnClearDepthStencilView;
  PFND3D10DDI_SETPREDICATION                            pfnSetPredication;
  PFND3D10DDI_QUERYGETDATA                              pfnQueryGetData;
  PFND3D10DDI_FLUSH                                     pfnFlush;
  PFND3D10DDI_GENMIPS                                   pfnGenMips;
  PFND3D10DDI_RESOURCECOPY                              pfnResourceCopy;
  PFND3D10DDI_RESOURCERESOLVESUBRESOURCE                pfnResourceResolveSubresource;
  PFND3D10DDI_RESOURCEMAP                               pfnResourceMap;
  PFND3D10DDI_RESOURCEUNMAP                             pfnResourceUnmap;
  PFND3D10DDI_RESOURCEISSTAGINGBUSY                     pfnResourceIsStagingBusy;
  PFND3D10_1DDI_RELOCATEDEVICEFUNCS                     pfnRelocateDeviceFuncs;
  PFND3D10DDI_CALCPRIVATERESOURCESIZE                   pfnCalcPrivateResourceSize;
  PFND3D10DDI_CALCPRIVATEOPENEDRESOURCESIZE             pfnCalcPrivateOpenedResourceSize;
  PFND3D10DDI_CREATERESOURCE                            pfnCreateResource;
  PFND3D10DDI_OPENRESOURCE                              pfnOpenResource;
  PFND3D10DDI_DESTROYRESOURCE                           pfnDestroyResource;
  PFND3D10_1DDI_CALCPRIVATESHADERRESOURCEVIEWSIZE       pfnCalcPrivateShaderResourceViewSize;
  PFND3D10_1DDI_CREATESHADERRESOURCEVIEW                pfnCreateShaderResourceView;
  PFND3D10DDI_DESTROYSHADERRESOURCEVIEW                 pfnDestroyShaderResourceView;
  PFND3D10DDI_CALCPRIVATERENDERTARGETVIEWSIZE           pfnCalcPrivateRenderTargetViewSize;
  PFND3D10DDI_CREATERENDERTARGETVIEW                    pfnCreateRenderTargetView;
  PFND3D10DDI_DESTROYRENDERTARGETVIEW                   pfnDestroyRenderTargetView;
  PFND3D10DDI_CALCPRIVATEDEPTHSTENCILVIEWSIZE           pfnCalcPrivateDepthStencilViewSize;
  PFND3D10DDI_CREATEDEPTHSTENCILVIEW                    pfnCreateDepthStencilView;
  PFND3D10DDI_DESTROYDEPTHSTENCILVIEW                   pfnDestroyDepthStencilView;
  PFND3D10DDI_CALCPRIVATEELEMENTLAYOUTSIZE              pfnCalcPrivateElementLayoutSize;
  PFND3D10DDI_CREATEELEMENTLAYOUT                       pfnCreateElementLayout;
  PFND3D10DDI_DESTROYELEMENTLAYOUT                      pfnDestroyElementLayout;
  PFND3D10_1DDI_CALCPRIVATEBLENDSTATESIZE               pfnCalcPrivateBlendStateSize;
  PFND3D10_1DDI_CREATEBLENDSTATE                        pfnCreateBlendState;
  PFND3D10DDI_DESTROYBLENDSTATE                         pfnDestroyBlendState;
  PFND3D10DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE          pfnCalcPrivateDepthStencilStateSize;
  PFND3D10DDI_CREATEDEPTHSTENCILSTATE                   pfnCreateDepthStencilState;
  PFND3D10DDI_DESTROYDEPTHSTENCILSTATE                  pfnDestroyDepthStencilState;
  PFND3D10DDI_CALCPRIVATERASTERIZERSTATESIZE            pfnCalcPrivateRasterizerStateSize;
  PFND3D10DDI_CREATERASTERIZERSTATE                     pfnCreateRasterizerState;
  PFND3D10DDI_DESTROYRASTERIZERSTATE                    pfnDestroyRasterizerState;
  PFND3D10DDI_CALCPRIVATESHADERSIZE                     pfnCalcPrivateShaderSize;
  PFND3D10DDI_CREATEVERTEXSHADER                        pfnCreateVertexShader;
  PFND3D10DDI_CREATEGEOMETRYSHADER                      pfnCreateGeometryShader;
  PFND3D10DDI_CREATEPIXELSHADER                         pfnCreatePixelShader;
  PFND3D10DDI_CALCPRIVATEGEOMETRYSHADERWITHSTREAMOUTPUT pfnCalcPrivateGeometryShaderWithStreamOutput;
  PFND3D10DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT      pfnCreateGeometryShaderWithStreamOutput;
  PFND3D10DDI_DESTROYSHADER                             pfnDestroyShader;
  PFND3D10DDI_CALCPRIVATESAMPLERSIZE                    pfnCalcPrivateSamplerSize;
  PFND3D10DDI_CREATESAMPLER                             pfnCreateSampler;
  PFND3D10DDI_DESTROYSAMPLER                            pfnDestroySampler;
  PFND3D10DDI_CALCPRIVATEQUERYSIZE                      pfnCalcPrivateQuerySize;
  PFND3D10DDI_CREATEQUERY                               pfnCreateQuery;
  PFND3D10DDI_DESTROYQUERY                              pfnDestroyQuery;
  PFND3D10DDI_CHECKFORMATSUPPORT                        pfnCheckFormatSupport;
  PFND3D10DDI_CHECKMULTISAMPLEQUALITYLEVELS             pfnCheckMultisampleQualityLevels;
  PFND3D10DDI_CHECKCOUNTERINFO                          pfnCheckCounterInfo;
  PFND3D10DDI_CHECKCOUNTER                              pfnCheckCounter;
  PFND3D10DDI_DESTROYDEVICE                             pfnDestroyDevice;
  PFND3D10DDI_SETTEXTFILTERSIZE                         pfnSetTextFilterSize;
  PFND3D10DDI_RESOURCECOPY                              pfnResourceConvert;
  PFND3D10DDI_RESOURCECOPYREGION                        pfnResourceConvertRegion;
} D3D10_1DDI_DEVICEFUNCS;
````


## -struct-fields
<dl>

### -field <b>pfnDefaultConstantBufferUpdateSubresourceUP</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceupdatesubresourceup.md">DefaultConstantBufferUpdateSubresourceUP</a> function.</p>
</dd>

### -field <b>pfnVsSetConstantBuffers</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setconstantbuffers.md">VsSetConstantBuffers</a> function.</p>
</dd>

### -field <b>pfnPsSetShaderResources</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshaderresources.md">PsSetShaderResources</a> function.</p>
</dd>

### -field <b>pfnPsSetShader</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshader.md">PsSetShader</a> function. </p>
</dd>

### -field <b>pfnPsSetSamplers</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setsamplers.md">PsSetSamplers</a> function.</p>
</dd>

### -field <b>pfnVsSetShader</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshader.md">VsSetShader</a> function.</p>
</dd>

### -field <b>pfnDrawIndexed</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-drawindexed.md">DrawIndexed</a> function.</p>
</dd>

### -field <b>pfnDraw</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-draw.md">Draw</a> function.</p>
</dd>

### -field <b>pfnDynamicIABufferMapNoOverwrite</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. For more information about whether to implement a separate <b>DynamicIABufferMapNoOverwrite</b> function or to point to the multipurpose <b>ResourceMap</b>, see the Remarks section of <b>ResourceMap</b>. </p>
</dd>

### -field <b>pfnDynamicIABufferUnmap</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceunmap.md">ResourceUnmap</a> function. For more information about whether to implement a separate <b>DynamicIABufferUnmap</b> function or to point to the multipurpose <b>ResourceUnmap</b>, see the Remarks section of <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a>. </p>
</dd>

### -field <b>pfnDynamicConstantBufferMapDiscard</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. For more information about whether to implement a separate <b>DynamicConstantBufferMapDiscard</b> function or to point to the multipurpose <b>ResourceMap</b>, see the Remarks section of <b>ResourceMap</b>. </p>
</dd>

### -field <b>pfnDynamicIABufferMapDiscard</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. For more information about whether to implement a separate <b>DynamicIABufferMapDiscard</b> function or to point to the multipurpose <b>ResourceMap</b>, see the Remarks section of <b>ResourceMap</b>. </p>
</dd>

### -field <b>pfnDynamicConstantBufferUnmap</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceunmap.md">ResourceUnmap</a> function. For more information about whether to implement a separate <b>DynamicConstantBufferUnmap</b> function or to point to the multipurpose <b>ResourceUnmap</b>, see the Remarks section of <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a>. </p>
</dd>

### -field <b>pfnPsSetConstantBuffers</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setconstantbuffers.md">PsSetConstantBuffers</a> function.</p>
</dd>

### -field <b>pfnIaSetInputLayout</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setinputlayout.md">IaSetInputLayout</a> function.</p>
</dd>

### -field <b>pfnIaSetVertexBuffers</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-ia-setvertexbuffers.md">IaSetVertexBuffers</a> function.</p>
</dd>

### -field <b>pfnIaSetIndexBuffer</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-ia-setindexbuffer.md">IaSetIndexBuffer</a> function.</p>
</dd>

### -field <b>pfnDrawIndexedInstanced</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-drawindexedinstanced.md">DrawIndexedInstanced</a> function.</p>
</dd>

### -field <b>pfnDrawInstanced</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-drawinstanced.md">DrawInstanced</a> function.</p>
</dd>

### -field <b>pfnDynamicResourceMapDiscard</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. For more information about whether to implement a separate <b>DynamicResourceMapDiscard</b> function or to point to the multipurpose <b>ResourceMap</b>, see the Remarks section of <b>ResourceMap</b>. </p>
</dd>

### -field <b>pfnDynamicResourceUnmap</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceunmap.md">ResourceUnmap</a> function. For more information about whether to implement a separate <b>DynamicResourceUnmap</b> function or to point to the multipurpose <b>ResourceUnmap</b>, see the Remarks section of <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a>. </p>
</dd>

### -field <b>pfnGsSetConstantBuffers</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setconstantbuffers.md">GsSetConstantBuffers</a> function.</p>
</dd>

### -field <b>pfnGsSetShader</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshader.md">GsSetShader</a> function.</p>
</dd>

### -field <b>pfnIaSetTopology</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-ia-settopology.md">IaSetTopology</a> function.</p>
</dd>

### -field <b>pfnStagingResourceMap</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. For more information about whether to implement a separate <b>StagingResourceMap</b> function or to point to the multipurpose <b>ResourceMap</b>, see the Remarks section of <b>ResourceMap</b>. </p>
</dd>

### -field <b>pfnStagingResourceUnmap</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceunmap.md">ResourceUnmap</a> function. For more information about whether to implement a separate <b>StagingResourceUnmap</b> function or to point to the multipurpose <b>ResourceUnmap</b>, see the Remarks section of <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a>. </p>
</dd>

### -field <b>pfnVsSetShaderResources</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshaderresources.md">VsSetShaderResources</a> function.</p>
</dd>

### -field <b>pfnVsSetSamplers</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setsamplers.md">VsSetSamplers</a> function.</p>
</dd>

### -field <b>pfnGsSetShaderResources</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshaderresources.md">GsSetShaderResources</a> function.</p>
</dd>

### -field <b>pfnGsSetSamplers</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setsamplers.md">GsSetSamplers</a> function.</p>
</dd>

### -field <b>pfnSetRenderTargets</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setrendertargets.md">SetRenderTargets</a> function.</p>
</dd>

### -field <b>pfnShaderResourceViewReadAfterWriteHazard</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-shaderresourceviewreadafterwritehazard.md">ShaderResourceViewReadAfterWriteHazard</a> function.</p>
</dd>

### -field <b>pfnResourceReadAfterWriteHazard</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcereadafterwritehazard.md">ResourceReadAfterWriteHazard</a> function.</p>
</dd>

### -field <b>pfnSetBlendState</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setblendstate.md">SetBlendState</a> function.</p>
</dd>

### -field <b>pfnSetDepthStencilState</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setdepthstencilstate.md">SetDepthStencilState</a> function.</p>
</dd>

### -field <b>pfnSetRasterizerState</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setrasterizerstate.md">SetRasterizerState</a> function.</p>
</dd>

### -field <b>pfnQueryEnd</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-queryend.md">QueryEnd</a> function.</p>
</dd>

### -field <b>pfnQueryBegin</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-querybegin.md">QueryBegin</a> function.</p>
</dd>

### -field <b>pfnResourceCopyRegion</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcecopyregion.md">ResourceCopyRegion</a> function.</p>
</dd>

### -field <b>pfnResourceUpdateSubresourceUP</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceupdatesubresourceup.md">ResourceUpdateSubresourceUP</a> function.</p>
</dd>

### -field <b>pfnSoSetTargets</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-so-settargets.md">SoSetTargets</a> function.</p>
</dd>

### -field <b>pfnDrawAuto</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-drawauto.md">DrawAuto</a> function.</p>
</dd>

### -field <b>pfnSetViewports</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setviewports.md">SetViewports</a> function.</p>
</dd>

### -field <b>pfnSetScissorRects</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setscissorrects.md">SetScissorRects</a> function.</p>
</dd>

### -field <b>pfnClearRenderTargetView</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-clearrendertargetview.md">ClearRenderTargetView</a> function.</p>
</dd>

### -field <b>pfnClearDepthStencilView</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-cleardepthstencilview.md">ClearDepthStencilView</a> function.</p>
</dd>

### -field <b>pfnSetPredication</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setpredication.md">SetPredication</a> function.</p>
</dd>

### -field <b>pfnQueryGetData</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-querygetdata.md">QueryGetData</a> function.</p>
</dd>

### -field <b>pfnFlush</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-flush.md">Flush(D3D10)</a> function.</p>
</dd>

### -field <b>pfnGenMips</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-genmips.md">GenMips</a> function.</p>
</dd>

### -field <b>pfnResourceCopy</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcecopy.md">ResourceCopy</a> function.</p>
</dd>

### -field <b>pfnResourceResolveSubresource</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceresolvesubresource.md">ResourceResolveSubresource</a> function.</p>
</dd>

### -field <b>pfnResourceMap</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function.</p>
</dd>

### -field <b>pfnResourceUnmap</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceunmap.md">ResourceUnmap</a> function.</p>
</dd>

### -field <b>pfnResourceIsStagingBusy</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceisstagingbusy.md">ResourceIsStagingBusy</a> function.</p>
</dd>

### -field <b>pfnRelocateDeviceFuncs</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-1ddi-relocatedevicefuncs.md">RelocateDeviceFuncs(D3D10_1)</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateResourceSize</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivateresourcesize.md">CalcPrivateResourceSize</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateOpenedResourceSize</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivateopenedresourcesize.md">CalcPrivateOpenedResourceSize</a> function.</p>
</dd>

### -field <b>pfnCreateResource</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createresource.md">CreateResource(D3D10)</a> function.</p>
</dd>

### -field <b>pfnOpenResource</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-openresource.md">OpenResource(D3D10)</a> function.</p>
</dd>

### -field <b>pfnDestroyResource</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyresource.md">DestroyResource(D3D10)</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateShaderResourceViewSize</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-1ddi-calcprivateshaderresourceviewsize.md">CalcPrivateShaderResourceViewSize(D3D10_1)</a> function.</p>
</dd>

### -field <b>pfnCreateShaderResourceView</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-1ddi-createshaderresourceview.md">CreateShaderResourceView(D3D10_1)</a> function.</p>
</dd>

### -field <b>pfnDestroyShaderResourceView</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyshaderresourceview.md">DestroyShaderResourceView</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateRenderTargetViewSize</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivaterendertargetviewsize.md">CalcPrivateRenderTargetViewSize</a> function.</p>
</dd>

### -field <b>pfnCreateRenderTargetView</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createrendertargetview.md">CreateRenderTargetView</a> function.</p>
</dd>

### -field <b>pfnDestroyRenderTargetView</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyrendertargetview.md">DestroyRenderTargetView</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateDepthStencilViewSize</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivatedepthstencilviewsize.md">CalcPrivateDepthStencilViewSize</a> function.</p>
</dd>

### -field <b>pfnCreateDepthStencilView</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdepthstencilview.md">CreateDepthStencilView</a> function.</p>
</dd>

### -field <b>pfnDestroyDepthStencilView</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroydepthstencilview.md">DestroyDepthStencilView</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateElementLayoutSize</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivateelementlayoutsize.md">CalcPrivateElementLayoutSize</a> function.</p>
</dd>

### -field <b>pfnCreateElementLayout</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createelementlayout.md">CreateElementLayout</a> function.</p>
</dd>

### -field <b>pfnDestroyElementLayout</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyelementlayout.md">DestroyElementLayout</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateBlendStateSize</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-1ddi-calcprivateblendstatesize.md">CalcPrivateBlendStateSize(D3D10_1)</a> function.</p>
</dd>

### -field <b>pfnCreateBlendState</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-1ddi-createblendstate.md">CreateBlendState(D3D10_1)</a> function.</p>
</dd>

### -field <b>pfnDestroyBlendState</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyblendstate.md">DestroyBlendState</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateDepthStencilStateSize</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivatedepthstencilstatesize.md">CalcPrivateDepthStencilStateSize</a> function.</p>
</dd>

### -field <b>pfnCreateDepthStencilState</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdepthstencilstate.md">CreateDepthStencilState</a> function.</p>
</dd>

### -field <b>pfnDestroyDepthStencilState</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroydepthstencilstate.md">DestroyDepthStencilState</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateRasterizerStateSize</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivaterasterizerstatesize.md">CalcPrivateRasterizerStateSize</a> function.</p>
</dd>

### -field <b>pfnCreateRasterizerState</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createrasterizerstate.md">CreateRasterizerState</a> function.</p>
</dd>

### -field <b>pfnDestroyRasterizerState</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyrasterizerstate.md">DestroyRasterizerState</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateShaderSize</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivateshadersize.md">CalcPrivateShaderSize</a> function.</p>
</dd>

### -field <b>pfnCreateVertexShader</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createvertexshader.md">CreateVertexShader(D3D10)</a> function.</p>
</dd>

### -field <b>pfnCreateGeometryShader</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-creategeometryshader.md">CreateGeometryShader</a> function.</p>
</dd>

### -field <b>pfnCreatePixelShader</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createpixelshader.md">CreatePixelShader(D3D10)</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateGeometryShaderWithStreamOutput</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivategeometryshaderwithstreamoutput.md">CalcPrivateGeometryShaderWithStreamOutput</a> function.</p>
</dd>

### -field <b>pfnCreateGeometryShaderWithStreamOutput</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-creategeometryshaderwithstreamoutput.md">CreateGeometryShaderWithStreamOutput</a> function.</p>
</dd>

### -field <b>pfnDestroyShader</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyshader.md">DestroyShader</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateSamplerSize</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivatesamplersize.md">CalcPrivateSamplerSize</a> function.</p>
</dd>

### -field <b>pfnCreateSampler</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createsampler.md">CreateSampler</a> function.</p>
</dd>

### -field <b>pfnDestroySampler</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroysampler.md">DestroySampler</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateQuerySize</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivatequerysize.md">CalcPrivateQuerySize</a> function.</p>
</dd>

### -field <b>pfnCreateQuery</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createquery.md">CreateQuery(D3D10)</a> function.</p>
</dd>

### -field <b>pfnDestroyQuery</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyquery.md">DestroyQuery(D3D10)</a> function.</p>
</dd>

### -field <b>pfnCheckFormatSupport</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-checkformatsupport.md">CheckFormatSupport</a> function.</p>
</dd>

### -field <b>pfnCheckMultisampleQualityLevels</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-checkmultisamplequalitylevels.md">CheckMultisampleQualityLevels</a> function.</p>
</dd>

### -field <b>pfnCheckCounterInfo</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-checkcounterinfo.md">CheckCounterInfo</a> function.</p>
</dd>

### -field <b>pfnCheckCounter</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-checkcounter.md">CheckCounter</a> function.</p>
</dd>

### -field <b>pfnDestroyDevice</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroydevice.md">DestroyDevice(D3D10)</a> function.</p>
</dd>

### -field <b>pfnSetTextFilterSize</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-settextfiltersize.md">SetTextFilterSize</a> function.</p>
</dd>

### -field <b>pfnResourceConvert</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcecopy.md">ResourceCopy</a> function. For more information about whether to implement a separate <b>ResourceConvert</b> function or to point to the multipurpose <b>ResourceCopy</b>, see the Remarks section of <b>ResourceCopy</b>.  </p>
</dd>

### -field <b>pfnResourceConvertRegion</b>

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcecopyregion.md">ResourceCopyRegion</a> function. For more information about whether to implement a separate <b>ResourceConvertRegion</b> function or to point to the multipurpose <b>ResourceCopyRegion</b>, see the Remarks section of <b>ResourceCopyRegion</b>.  </p>
</dd>
</dl>

## -remarks
<p>The order of user-mode display driver functions (that is, the order of the members of the D3D10_1DDI_DEVICEFUNCS structure) is in decreasing order of priority (in regard to performance).</p>

<p>The user-mode display driver can use different names for these functions because the address of the function table (this structure) is shared between the Direct3D 10.1 runtime and the driver through the call to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a> function.</p>

<p>The <b>pfnResetPrimitiveID</b> and  <b>pfnSetVertexPipelineOutput</b> members (not shown here) and their data types are reserved for system use and should not be used in your driver.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3D10_1DDI_DEVICEFUNCS is supported on Windows Vista with Service Pack 1 (SP1) and later versions and Windows Server 2008 and later versions. </p>
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
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-createdevice.md">D3D10DDIARG_CREATEDEVICE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10_1DDI_DEVICEFUNCS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
