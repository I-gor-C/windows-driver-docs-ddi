---
UID: NS.d3d10umddi.D3D10DDI_DEVICEFUNCS
title: D3D10DDI_DEVICEFUNCS
author: windows-driver-content
description: The D3D10DDI_DEVICEFUNCS structure contains functions that the user-mode display driver can implement to render graphics primitives and process state changes.
old-location: display\d3d10ddi_devicefuncs.htm
old-project: display
ms.assetid: 005f4fc0-2b22-47bf-a129-59b2dc4ff052
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D10DDI_DEVICEFUNCS,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10DDI_DEVICEFUNCS
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

# D3D10DDI_DEVICEFUNCS structure



## -description
<p>The D3D10DDI_DEVICEFUNCS structure contains functions that the user-mode display driver can implement to render graphics primitives and process state changes.</p>


## -syntax

````
typedef struct D3D10DDI_DEVICEFUNCS {
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
  PFND3D10DDI_RELOCATEDEVICEFUNCS                       pfnRelocateDeviceFuncs;
  PFND3D10DDI_CALCPRIVATERESOURCESIZE                   pfnCalcPrivateResourceSize;
  PFND3D10DDI_CALCPRIVATEOPENEDRESOURCESIZE             pfnCalcPrivateOpenedResourceSize;
  PFND3D10DDI_CREATERESOURCE                            pfnCreateResource;
  PFND3D10DDI_OPENRESOURCE                              pfnOpenResource;
  PFND3D10DDI_DESTROYRESOURCE                           pfnDestroyResource;
  PFND3D10DDI_CALCPRIVATESHADERRESOURCEVIEWSIZE         pfnCalcPrivateShaderResourceViewSize;
  PFND3D10DDI_CREATESHADERRESOURCEVIEW                  pfnCreateShaderResourceView;
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
  PFND3D10DDI_CALCPRIVATEBLENDSTATESIZE                 pfnCalcPrivateBlendStateSize;
  PFND3D10DDI_CREATEBLENDSTATE                          pfnCreateBlendState;
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
} D3D10DDI_DEVICEFUNCS;
````


## -struct-fields
<dl>

### -field pfnDefaultConstantBufferUpdateSubresourceUP

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceupdatesubresourceup.md">DefaultConstantBufferUpdateSubresourceUP</a> function.</p>
</dd>

### -field pfnVsSetConstantBuffers

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setconstantbuffers.md">VsSetConstantBuffers</a> function.</p>
</dd>

### -field pfnPsSetShaderResources

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshaderresources.md">PsSetShaderResources</a> function.</p>
</dd>

### -field pfnPsSetShader

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshader.md">PsSetShader</a> function. </p>
</dd>

### -field pfnPsSetSamplers

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setsamplers.md">PsSetSamplers</a> function.</p>
</dd>

### -field pfnVsSetShader

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshader.md">VsSetShader</a> function.</p>
</dd>

### -field pfnDrawIndexed

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-drawindexed.md">DrawIndexed</a> function.</p>
</dd>

### -field pfnDraw

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-draw.md">Draw</a> function.</p>
</dd>

### -field pfnDynamicIABufferMapNoOverwrite

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. For more information about whether to implement a separate <b>DynamicIABufferMapNoOverwrite</b> function or to point to the multipurpose <b>ResourceMap</b>, see the Remarks section of <b>ResourceMap</b>. </p>
</dd>

### -field pfnDynamicIABufferUnmap

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceunmap.md">ResourceUnmap</a> function. For more information about whether to implement a separate <b>DynamicIABufferUnmap</b> function or to point to the multipurpose <b>ResourceUnmap</b>, see the Remarks section of <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a>. </p>
</dd>

### -field pfnDynamicConstantBufferMapDiscard

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. For more information about whether to implement a separate <b>DynamicConstantBufferMapDiscard</b> function or to point to the multipurpose <b>ResourceMap</b>, see the Remarks section of <b>ResourceMap</b>. </p>
</dd>

### -field pfnDynamicIABufferMapDiscard

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. For more information about whether to implement a separate <b>DynamicIABufferMapDiscard</b> function or to point to the multipurpose <b>ResourceMap</b>, see the Remarks section of <b>ResourceMap</b>. </p>
</dd>

### -field pfnDynamicConstantBufferUnmap

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceunmap.md">ResourceUnmap</a> function. For more information about whether to implement a separate <b>DynamicConstantBufferUnmap</b> function or to point to the multipurpose <b>ResourceUnmap</b>, see the Remarks section of <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a>. </p>
</dd>

### -field pfnPsSetConstantBuffers

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setconstantbuffers.md">PsSetConstantBuffers</a> function.</p>
</dd>

### -field pfnIaSetInputLayout

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setinputlayout.md">IaSetInputLayout</a> function.</p>
</dd>

### -field pfnIaSetVertexBuffers

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-ia-setvertexbuffers.md">IaSetVertexBuffers</a> function.</p>
</dd>

### -field pfnIaSetIndexBuffer

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-ia-setindexbuffer.md">IaSetIndexBuffer</a> function.</p>
</dd>

### -field pfnDrawIndexedInstanced

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-drawindexedinstanced.md">DrawIndexedInstanced</a> function.</p>
</dd>

### -field pfnDrawInstanced

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-drawinstanced.md">DrawInstanced</a> function.</p>
</dd>

### -field pfnDynamicResourceMapDiscard

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. For more information about whether to implement a separate <b>DynamicResourceMapDiscard</b> function or to point to the multipurpose <b>ResourceMap</b>, see the Remarks section of <b>ResourceMap</b>. </p>
</dd>

### -field pfnDynamicResourceUnmap

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceunmap.md">ResourceUnmap</a> function. For more information about whether to implement a separate <b>DynamicResourceUnmap</b> function or to point to the multipurpose <b>ResourceUnmap</b>, see the Remarks section of <b>ResourceUnmap</b>. </p>
</dd>

### -field pfnGsSetConstantBuffers

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setconstantbuffers.md">GsSetConstantBuffers</a> function.</p>
</dd>

### -field pfnGsSetShader

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshader.md">GsSetShader</a> function.</p>
</dd>

### -field pfnIaSetTopology

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-ia-settopology.md">IaSetTopology</a> function.</p>
</dd>

### -field pfnStagingResourceMap

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. For more information about whether to implement a separate <b>StagingResourceMap</b> function or to point to the multipurpose <b>ResourceMap</b>, see the Remarks section of <b>ResourceMap</b>. </p>
</dd>

### -field pfnStagingResourceUnmap

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceunmap.md">ResourceUnmap</a> function. For more information about whether to implement a separate <b>StagingResourceUnmap</b> function or to point to the multipurpose <b>ResourceUnmap</b>, see the Remarks section of <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a>. </p>
</dd>

### -field pfnVsSetShaderResources

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshaderresources.md">VsSetShaderResources</a> function.</p>
</dd>

### -field pfnVsSetSamplers

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setsamplers.md">VsSetSamplers</a> function.</p>
</dd>

### -field pfnGsSetShaderResources

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshaderresources.md">GsSetShaderResources</a> function.</p>
</dd>

### -field pfnGsSetSamplers

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setsamplers.md">GsSetSamplers</a> function.</p>
</dd>

### -field pfnSetRenderTargets

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setrendertargets.md">SetRenderTargets</a> function.</p>
</dd>

### -field pfnShaderResourceViewReadAfterWriteHazard

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-shaderresourceviewreadafterwritehazard.md">ShaderResourceViewReadAfterWriteHazard</a> function.</p>
</dd>

### -field pfnResourceReadAfterWriteHazard

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcereadafterwritehazard.md">ResourceReadAfterWriteHazard</a> function.</p>
</dd>

### -field pfnSetBlendState

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setblendstate.md">SetBlendState</a> function.</p>
</dd>

### -field pfnSetDepthStencilState

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setdepthstencilstate.md">SetDepthStencilState</a> function.</p>
</dd>

### -field pfnSetRasterizerState

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setrasterizerstate.md">SetRasterizerState</a> function.</p>
</dd>

### -field pfnQueryEnd

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-queryend.md">QueryEnd</a> function.</p>
</dd>

### -field pfnQueryBegin

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-querybegin.md">QueryBegin</a> function.</p>
</dd>

### -field pfnResourceCopyRegion

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcecopyregion.md">ResourceCopyRegion</a> function.</p>
</dd>

### -field pfnResourceUpdateSubresourceUP

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceupdatesubresourceup.md">ResourceUpdateSubresourceUP</a> function.</p>
</dd>

### -field pfnSoSetTargets

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-so-settargets.md">SoSetTargets</a> function.</p>
</dd>

### -field pfnDrawAuto

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-drawauto.md">DrawAuto</a> function.</p>
</dd>

### -field pfnSetViewports

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setviewports.md">SetViewports</a> function.</p>
</dd>

### -field pfnSetScissorRects

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setscissorrects.md">SetScissorRects</a> function.</p>
</dd>

### -field pfnClearRenderTargetView

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-clearrendertargetview.md">ClearRenderTargetView</a> function.</p>
</dd>

### -field pfnClearDepthStencilView

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-cleardepthstencilview.md">ClearDepthStencilView</a> function.</p>
</dd>

### -field pfnSetPredication

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setpredication.md">SetPredication</a> function.</p>
</dd>

### -field pfnQueryGetData

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-querygetdata.md">QueryGetData</a> function.</p>
</dd>

### -field pfnFlush

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-flush.md">Flush(D3D10)</a> function.</p>
</dd>

### -field pfnGenMips

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-genmips.md">GenMips</a> function.</p>
</dd>

### -field pfnResourceCopy

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcecopy.md">ResourceCopy</a> function.</p>
</dd>

### -field pfnResourceResolveSubresource

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceresolvesubresource.md">ResourceResolveSubresource</a> function.</p>
</dd>

### -field pfnResourceMap

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function.</p>
</dd>

### -field pfnResourceUnmap

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceunmap.md">ResourceUnmap</a> function.</p>
</dd>

### -field pfnResourceIsStagingBusy

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceisstagingbusy.md">ResourceIsStagingBusy</a> function.</p>
</dd>

### -field pfnRelocateDeviceFuncs

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-relocatedevicefuncs.md">RelocateDeviceFuncs</a> function.</p>
</dd>

### -field pfnCalcPrivateResourceSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivateresourcesize.md">CalcPrivateResourceSize</a> function.</p>
</dd>

### -field pfnCalcPrivateOpenedResourceSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivateopenedresourcesize.md">CalcPrivateOpenedResourceSize</a> function.</p>
</dd>

### -field pfnCreateResource

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createresource.md">CreateResource(D3D10)</a> function.</p>
</dd>

### -field pfnOpenResource

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-openresource.md">OpenResource(D3D10)</a> function.</p>
</dd>

### -field pfnDestroyResource

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyresource.md">DestroyResource(D3D10)</a> function.</p>
</dd>

### -field pfnCalcPrivateShaderResourceViewSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivateshaderresourceviewsize.md">CalcPrivateShaderResourceViewSize</a> function.</p>
</dd>

### -field pfnCreateShaderResourceView

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createshaderresourceview.md">CreateShaderResourceView</a> function.</p>
</dd>

### -field pfnDestroyShaderResourceView

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyshaderresourceview.md">DestroyShaderResourceView</a> function.</p>
</dd>

### -field pfnCalcPrivateRenderTargetViewSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivaterendertargetviewsize.md">CalcPrivateRenderTargetViewSize</a> function.</p>
</dd>

### -field pfnCreateRenderTargetView

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createrendertargetview.md">CreateRenderTargetView</a> function.</p>
</dd>

### -field pfnDestroyRenderTargetView

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyrendertargetview.md">DestroyRenderTargetView</a> function.</p>
</dd>

### -field pfnCalcPrivateDepthStencilViewSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivatedepthstencilviewsize.md">CalcPrivateDepthStencilViewSize</a> function.</p>
</dd>

### -field pfnCreateDepthStencilView

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdepthstencilview.md">CreateDepthStencilView</a> function.</p>
</dd>

### -field pfnDestroyDepthStencilView

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroydepthstencilview.md">DestroyDepthStencilView</a> function.</p>
</dd>

### -field pfnCalcPrivateElementLayoutSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivateelementlayoutsize.md">CalcPrivateElementLayoutSize</a> function.</p>
</dd>

### -field pfnCreateElementLayout

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createelementlayout.md">CreateElementLayout</a> function.</p>
</dd>

### -field pfnDestroyElementLayout

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyelementlayout.md">DestroyElementLayout</a> function.</p>
</dd>

### -field pfnCalcPrivateBlendStateSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivateblendstatesize.md">CalcPrivateBlendStateSize</a> function.</p>
</dd>

### -field pfnCreateBlendState

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createblendstate.md">CreateBlendState</a> function.</p>
</dd>

### -field pfnDestroyBlendState

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyblendstate.md">DestroyBlendState</a> function.</p>
</dd>

### -field pfnCalcPrivateDepthStencilStateSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivatedepthstencilstatesize.md">CalcPrivateDepthStencilStateSize</a> function.</p>
</dd>

### -field pfnCreateDepthStencilState

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdepthstencilstate.md">CreateDepthStencilState</a> function.</p>
</dd>

### -field pfnDestroyDepthStencilState

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroydepthstencilstate.md">DestroyDepthStencilState</a> function.</p>
</dd>

### -field pfnCalcPrivateRasterizerStateSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivaterasterizerstatesize.md">CalcPrivateRasterizerStateSize</a> function.</p>
</dd>

### -field pfnCreateRasterizerState

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createrasterizerstate.md">CreateRasterizerState</a> function.</p>
</dd>

### -field pfnDestroyRasterizerState

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyrasterizerstate.md">DestroyRasterizerState</a> function.</p>
</dd>

### -field pfnCalcPrivateShaderSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivateshadersize.md">CalcPrivateShaderSize</a> function.</p>
</dd>

### -field pfnCreateVertexShader

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createvertexshader.md">CreateVertexShader(D3D10)</a> function.</p>
</dd>

### -field pfnCreateGeometryShader

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-creategeometryshader.md">CreateGeometryShader</a> function.</p>
</dd>

### -field pfnCreatePixelShader

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createpixelshader.md">CreatePixelShader(D3D10)</a> function.</p>
</dd>

### -field pfnCalcPrivateGeometryShaderWithStreamOutput

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivategeometryshaderwithstreamoutput.md">CalcPrivateGeometryShaderWithStreamOutput</a> function.</p>
</dd>

### -field pfnCreateGeometryShaderWithStreamOutput

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-creategeometryshaderwithstreamoutput.md">CreateGeometryShaderWithStreamOutput</a> function.</p>
</dd>

### -field pfnDestroyShader

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyshader.md">DestroyShader</a> function.</p>
</dd>

### -field pfnCalcPrivateSamplerSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivatesamplersize.md">CalcPrivateSamplerSize</a> function.</p>
</dd>

### -field pfnCreateSampler

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createsampler.md">CreateSampler</a> function.</p>
</dd>

### -field pfnDestroySampler

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroysampler.md">DestroySampler</a> function.</p>
</dd>

### -field pfnCalcPrivateQuerySize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivatequerysize.md">CalcPrivateQuerySize</a> function.</p>
</dd>

### -field pfnCreateQuery

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createquery.md">CreateQuery(D3D10)</a> function.</p>
</dd>

### -field pfnDestroyQuery

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyquery.md">DestroyQuery(D3D10)</a> function.</p>
</dd>

### -field pfnCheckFormatSupport

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-checkformatsupport.md">CheckFormatSupport</a> function.</p>
</dd>

### -field pfnCheckMultisampleQualityLevels

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-checkmultisamplequalitylevels.md">CheckMultisampleQualityLevels</a> function.</p>
</dd>

### -field pfnCheckCounterInfo

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-checkcounterinfo.md">CheckCounterInfo</a> function.</p>
</dd>

### -field pfnCheckCounter

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-checkcounter.md">CheckCounter</a> function.</p>
</dd>

### -field pfnDestroyDevice

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroydevice.md">DestroyDevice(D3D10)</a> function.</p>
</dd>

### -field pfnSetTextFilterSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-settextfiltersize.md">SetTextFilterSize</a> function.</p>
</dd>
</dl>

## -remarks
<p>The order of user-mode display driver functions (that is, the order of the members of the D3D10DDI_DEVICEFUNCS structure) is in decreasing order of priority (in regard to performance).</p>

<p>The user-mode display driver can use different names for these functions because the address of the function table (this structure) is shared between the Direct3D 10 runtime and the driver through the call to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a> function.</p>

<p>The <b>pfnResetPrimitiveID</b> and  <b>pfnSetVertexPipelineOutput</b> members (not shown here) and their data types are reserved for system use and should not be used in your driver.</p>

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
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-createdevice.md">D3D10DDIARG_CREATEDEVICE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10DDI_DEVICEFUNCS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
