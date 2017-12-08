---
UID: NS.d3d10umddi.D3D11_1DDI_DEVICEFUNCS~r1
title: D3D11_1DDI_DEVICEFUNCS
author: windows-driver-content
description: Contains functions that a user-mode display driver that is optimized for the Microsoft Direct3D version 11.1 runtime can implement to render graphics primitives and process state changes.
old-location: display\d3d11_1ddi_devicefuncs.htm
old-project: display
ms.assetid: 5429D886-4CC0-438D-AC9F-739159802062
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D11_1DDI_DEVICEFUNCS, D3D11_1DDI_DEVICEFUNCS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_DEVICEFUNCS
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

# D3D11_1DDI_DEVICEFUNCS structure



## -description
<p>Contains functions that a user-mode display driver that is optimized for the Microsoft Direct3D version 11.1 runtime can implement to render graphics primitives and process state changes.</p>


## -syntax

````
typedef struct D3D11_1DDI_DEVICEFUNCS {
  PFND3D11_1DDI_RESOURCEUPDATESUBRESOURCEUP               pfnDefaultConstantBufferUpdateSubresourceUP;
  PFND3D11_1DDI_SETCONSTANTBUFFERS                        pfnVsSetConstantBuffers;
  PFND3D10DDI_SETSHADERRESOURCES                          pfnPsSetShaderResources;
  PFND3D10DDI_SETSHADER                                   pfnPsSetShader;
  PFND3D10DDI_SETSAMPLERS                                 pfnPsSetSamplers;
  PFND3D10DDI_SETSHADER                                   pfnVsSetShader;
  PFND3D10DDI_DRAWINDEXED                                 pfnDrawIndexed;
  PFND3D10DDI_DRAW                                        pfnDraw;
  PFND3D10DDI_RESOURCEMAP                                 pfnDynamicIABufferMapNoOverwrite;
  PFND3D10DDI_RESOURCEUNMAP                               pfnDynamicIABufferUnmap;
  PFND3D10DDI_RESOURCEMAP                                 pfnDynamicConstantBufferMapDiscard;
  PFND3D10DDI_RESOURCEMAP                                 pfnDynamicIABufferMapDiscard;
  PFND3D10DDI_RESOURCEUNMAP                               pfnDynamicConstantBufferUnmap;
  PFND3D11_1DDI_SETCONSTANTBUFFERS                        pfnPsSetConstantBuffers;
  PFND3D10DDI_SETINPUTLAYOUT                              pfnIaSetInputLayout;
  PFND3D10DDI_IA_SETVERTEXBUFFERS                         pfnIaSetVertexBuffers;
  PFND3D10DDI_IA_SETINDEXBUFFER                           pfnIaSetIndexBuffer;
  PFND3D10DDI_DRAWINDEXEDINSTANCED                        pfnDrawIndexedInstanced;
  PFND3D10DDI_DRAWINSTANCED                               pfnDrawInstanced;
  PFND3D10DDI_RESOURCEMAP                                 pfnDynamicResourceMapDiscard;
  PFND3D10DDI_RESOURCEUNMAP                               pfnDynamicResourceUnmap;
  PFND3D11_1DDI_SETCONSTANTBUFFERS                        pfnGsSetConstantBuffers;
  PFND3D10DDI_SETSHADER                                   pfnGsSetShader;
  PFND3D10DDI_IA_SETTOPOLOGY                              pfnIaSetTopology;
  PFND3D10DDI_RESOURCEMAP                                 pfnStagingResourceMap;
  PFND3D10DDI_RESOURCEUNMAP                               pfnStagingResourceUnmap;
  PFND3D10DDI_SETSHADERRESOURCES                          pfnVsSetShaderResources;
  PFND3D10DDI_SETSAMPLERS                                 pfnVsSetSamplers;
  PFND3D10DDI_SETSHADERRESOURCES                          pfnGsSetShaderResources;
  PFND3D10DDI_SETSAMPLERS                                 pfnGsSetSamplers;
  PFND3D11DDI_SETRENDERTARGETS                            pfnSetRenderTargets;
  PFND3D10DDI_SHADERRESOURCEVIEWREADAFTERWRITEHAZARD      pfnShaderResourceViewReadAfterWriteHazard;
  PFND3D10DDI_RESOURCEREADAFTERWRITEHAZARD                pfnResourceReadAfterWriteHazard;
  PFND3D10DDI_SETBLENDSTATE                               pfnSetBlendState;
  PFND3D10DDI_SETDEPTHSTENCILSTATE                        pfnSetDepthStencilState;
  PFND3D10DDI_SETRASTERIZERSTATE                          pfnSetRasterizerState;
  PFND3D10DDI_QUERYEND                                    pfnQueryEnd;
  PFND3D10DDI_QUERYBEGIN                                  pfnQueryBegin;
  PFND3D11_1DDI_RESOURCECOPYREGION                        pfnResourceCopyRegion;
  PFND3D11_1DDI_RESOURCEUPDATESUBRESOURCEUP               pfnResourceUpdateSubresourceUP;
  PFND3D10DDI_SO_SETTARGETS                               pfnSoSetTargets;
  PFND3D10DDI_DRAWAUTO                                    pfnDrawAuto;
  PFND3D10DDI_SETVIEWPORTS                                pfnSetViewports;
  PFND3D10DDI_SETSCISSORRECTS                             pfnSetScissorRects;
  PFND3D10DDI_CLEARRENDERTARGETVIEW                       pfnClearRenderTargetView;
  PFND3D10DDI_CLEARDEPTHSTENCILVIEW                       pfnClearDepthStencilView;
  PFND3D10DDI_SETPREDICATION                              pfnSetPredication;
  PFND3D10DDI_QUERYGETDATA                                pfnQueryGetData;
  PFND3D11_1DDI_FLUSH                                     pfnFlush;
  PFND3D10DDI_GENMIPS                                     pfnGenMips;
  PFND3D10DDI_RESOURCECOPY                                pfnResourceCopy;
  PFND3D10DDI_RESOURCERESOLVESUBRESOURCE                  pfnResourceResolveSubresource;
  PFND3D10DDI_RESOURCEMAP                                 pfnResourceMap;
  PFND3D10DDI_RESOURCEUNMAP                               pfnResourceUnmap;
  PFND3D10DDI_RESOURCEISSTAGINGBUSY                       pfnResourceIsStagingBusy;
  PFND3D11_1DDI_RELOCATEDEVICEFUNCS                       pfnRelocateDeviceFuncs;
  PFND3D11DDI_CALCPRIVATERESOURCESIZE                     pfnCalcPrivateResourceSize;
  PFND3D10DDI_CALCPRIVATEOPENEDRESOURCESIZE               pfnCalcPrivateOpenedResourceSize;
  PFND3D11DDI_CREATERESOURCE                              pfnCreateResource;
  PFND3D10DDI_OPENRESOURCE                                pfnOpenResource;
  PFND3D10DDI_DESTROYRESOURCE                             pfnDestroyResource;
  PFND3D11DDI_CALCPRIVATESHADERRESOURCEVIEWSIZE           pfnCalcPrivateShaderResourceViewSize;
  PFND3D11DDI_CREATESHADERRESOURCEVIEW                    pfnCreateShaderResourceView;
  PFND3D10DDI_DESTROYSHADERRESOURCEVIEW                   pfnDestroyShaderResourceView;
  PFND3D10DDI_CALCPRIVATERENDERTARGETVIEWSIZE             pfnCalcPrivateRenderTargetViewSize;
  PFND3D10DDI_CREATERENDERTARGETVIEW                      pfnCreateRenderTargetView;
  PFND3D10DDI_DESTROYRENDERTARGETVIEW                     pfnDestroyRenderTargetView;
  PFND3D11DDI_CALCPRIVATEDEPTHSTENCILVIEWSIZE             pfnCalcPrivateDepthStencilViewSize;
  PFND3D11DDI_CREATEDEPTHSTENCILVIEW                      pfnCreateDepthStencilView;
  PFND3D10DDI_DESTROYDEPTHSTENCILVIEW                     pfnDestroyDepthStencilView;
  PFND3D10DDI_CALCPRIVATEELEMENTLAYOUTSIZE                pfnCalcPrivateElementLayoutSize;
  PFND3D10DDI_CREATEELEMENTLAYOUT                         pfnCreateElementLayout;
  PFND3D10DDI_DESTROYELEMENTLAYOUT                        pfnDestroyElementLayout;
  PFND3D11_1DDI_CALCPRIVATEBLENDSTATESIZE                 pfnCalcPrivateBlendStateSize;
  PFND3D11_1DDI_CREATEBLENDSTATE                          pfnCreateBlendState;
  PFND3D10DDI_DESTROYBLENDSTATE                           pfnDestroyBlendState;
  PFND3D10DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE            pfnCalcPrivateDepthStencilStateSize;
  PFND3D10DDI_CREATEDEPTHSTENCILSTATE                     pfnCreateDepthStencilState;
  PFND3D10DDI_DESTROYDEPTHSTENCILSTATE                    pfnDestroyDepthStencilState;
  PFND3D11_1DDI_CALCPRIVATERASTERIZERSTATESIZE            pfnCalcPrivateRasterizerStateSize;
  PFND3D11_1DDI_CREATERASTERIZERSTATE                     pfnCreateRasterizerState;
  PFND3D10DDI_DESTROYRASTERIZERSTATE                      pfnDestroyRasterizerState;
  PFND3D11_1DDI_CALCPRIVATESHADERSIZE                     pfnCalcPrivateShaderSize;
  PFND3D11_1DDI_CREATEVERTEXSHADER                        pfnCreateVertexShader;
  PFND3D11_1DDI_CREATEGEOMETRYSHADER                      pfnCreateGeometryShader;
  PFND3D11_1DDI_CREATEPIXELSHADER                         pfnCreatePixelShader;
  PFND3D11_1DDI_CALCPRIVATEGEOMETRYSHADERWITHSTREAMOUTPUT pfnCalcPrivateGeometryShaderWithStreamOutput;
  PFND3D11_1DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT      pfnCreateGeometryShaderWithStreamOutput;
  PFND3D10DDI_DESTROYSHADER                               pfnDestroyShader;
  PFND3D10DDI_CALCPRIVATESAMPLERSIZE                      pfnCalcPrivateSamplerSize;
  PFND3D10DDI_CREATESAMPLER                               pfnCreateSampler;
  PFND3D10DDI_DESTROYSAMPLER                              pfnDestroySampler;
  PFND3D10DDI_CALCPRIVATEQUERYSIZE                        pfnCalcPrivateQuerySize;
  PFND3D10DDI_CREATEQUERY                                 pfnCreateQuery;
  PFND3D10DDI_DESTROYQUERY                                pfnDestroyQuery;
  PFND3D10DDI_CHECKFORMATSUPPORT                          pfnCheckFormatSupport;
  PFND3D10DDI_CHECKMULTISAMPLEQUALITYLEVELS               pfnCheckMultisampleQualityLevels;
  PFND3D10DDI_CHECKCOUNTERINFO                            pfnCheckCounterInfo;
  PFND3D10DDI_CHECKCOUNTER                                pfnCheckCounter;
  PFND3D10DDI_DESTROYDEVICE                               pfnDestroyDevice;
  PFND3D10DDI_SETTEXTFILTERSIZE                           pfnSetTextFilterSize;
  PFND3D10DDI_RESOURCECOPY                                pfnResourceConvert;
  PFND3D11_1DDI_RESOURCECOPYREGION                        pfnResourceConvertRegion;
  PFND3D11DDI_DRAWINDEXEDINSTANCEDINDIRECT                pfnDrawIndexedInstancedIndirect;
  PFND3D11DDI_DRAWINSTANCEDINDIRECT                       pfnDrawInstancedIndirect;
  PFND3D11DDI_COMMANDLISTEXECUTE                          pfnCommandListExecute;
  PFND3D10DDI_SETSHADERRESOURCES                          pfnHsSetShaderResources;
  PFND3D10DDI_SETSHADER                                   pfnHsSetShader;
  PFND3D10DDI_SETSAMPLERS                                 pfnHsSetSamplers;
  PFND3D11_1DDI_SETCONSTANTBUFFERS                        pfnHsSetConstantBuffers;
  PFND3D10DDI_SETSHADERRESOURCES                          pfnDsSetShaderResources;
  PFND3D10DDI_SETSHADER                                   pfnDsSetShader;
  PFND3D10DDI_SETSAMPLERS                                 pfnDsSetSamplers;
  PFND3D11_1DDI_SETCONSTANTBUFFERS                        pfnDsSetConstantBuffers;
  PFND3D11_1DDI_CREATEHULLSHADER                          pfnCreateHullShader;
  PFND3D11_1DDI_CREATEDOMAINSHADER                        pfnCreateDomainShader;
  PFND3D11DDI_CHECKDEFERREDCONTEXTHANDLESIZES             pfnCheckDeferredContextHandleSizes;
  PFND3D11DDI_CALCDEFERREDCONTEXTHANDLESIZE               pfnCalcDeferredContextHandleSize;
  PFND3D11DDI_CALCPRIVATEDEFERREDCONTEXTSIZE              pfnCalcPrivateDeferredContextSize;
  PFND3D11DDI_CREATEDEFERREDCONTEXT                       pfnCreateDeferredContext;
  PFND3D11DDI_ABANDONCOMMANDLIST                          pfnAbandonCommandList;
  PFND3D11DDI_CALCPRIVATECOMMANDLISTSIZE                  pfnCalcPrivateCommandListSize;
  PFND3D11DDI_CREATECOMMANDLIST                           pfnCreateCommandList;
  PFND3D11DDI_DESTROYCOMMANDLIST                          pfnDestroyCommandList;
  PFND3D11_1DDI_CALCPRIVATETESSELLATIONSHADERSIZE         pfnCalcPrivateTessellationShaderSize;
  PFND3D11DDI_SETSHADER_WITH_IFACES                       pfnPsSetShaderWithIfaces;
  PFND3D11DDI_SETSHADER_WITH_IFACES                       pfnVsSetShaderWithIfaces;
  PFND3D11DDI_SETSHADER_WITH_IFACES                       pfnGsSetShaderWithIfaces;
  PFND3D11DDI_SETSHADER_WITH_IFACES                       pfnHsSetShaderWithIfaces;
  PFND3D11DDI_SETSHADER_WITH_IFACES                       pfnDsSetShaderWithIfaces;
  PFND3D11DDI_SETSHADER_WITH_IFACES                       pfnCsSetShaderWithIfaces;
  PFND3D11DDI_CREATECOMPUTESHADER                         pfnCreateComputeShader;
  PFND3D10DDI_SETSHADER                                   pfnCsSetShader;
  PFND3D10DDI_SETSHADERRESOURCES                          pfnCsSetShaderResources;
  PFND3D10DDI_SETSAMPLERS                                 pfnCsSetSamplers;
  PFND3D11_1DDI_SETCONSTANTBUFFERS                        pfnCsSetConstantBuffers;
  PFND3D11DDI_CALCPRIVATEUNORDEREDACCESSVIEWSIZE          pfnCalcPrivateUnorderedAccessViewSize;
  PFND3D11DDI_CREATEUNORDEREDACCESSVIEW                   pfnCreateUnorderedAccessView;
  PFND3D11DDI_DESTROYUNORDEREDACCESSVIEW                  pfnDestroyUnorderedAccessView;
  PFND3D11DDI_CLEARUNORDEREDACCESSVIEWUINT                pfnClearUnorderedAccessViewUint;
  PFND3D11DDI_CLEARUNORDEREDACCESSVIEWFLOAT               pfnClearUnorderedAccessViewFloat;
  PFND3D11DDI_SETUNORDEREDACCESSVIEWS                     pfnCsSetUnorderedAccessViews;
  PFND3D11DDI_DISPATCH                                    pfnDispatch;
  PFND3D11DDI_DISPATCHINDIRECT                            pfnDispatchIndirect;
  PFND3D11DDI_SETRESOURCEMINLOD                           pfnSetResourceMinLOD;
  PFND3D11DDI_COPYSTRUCTURECOUNT                          pfnCopyStructureCount;
  PFND3D11DDI_RECYCLECOMMANDLIST                          pfnRecycleCommandList;
  PFND3D11DDI_RECYCLECREATECOMMANDLIST                    pfnRecycleCreateCommandList;
  PFND3D11DDI_RECYCLECREATEDEFERREDCONTEXT                pfnRecycleCreateDeferredContext;
  PFND3D11DDI_DESTROYCOMMANDLIST                          pfnRecycleDestroyCommandList;
  PFND3D11_1DDI_DISCARD                                   pfnDiscard;
  PFND3D11_1DDI_ASSIGNDEBUGBINARY                         pfnAssignDebugBinary;
  PFND3D10DDI_RESOURCEMAP                                 pfnDynamicConstantBufferMapNoOverwrite;
  PFND3D11_1DDI_CHECKDIRECTFLIPSUPPORT                    pfnCheckDirectFlipSupport;
  PFND3D11_1DDI_CLEARVIEW                                 pfnClearView;
} D3D11_1DDI_DEVICEFUNCS;
````


## -struct-fields
<dl>

### -field pfnDefaultConstantBufferUpdateSubresourceUP

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-resourceupdatesubresourceup.md">DefaultConstantBufferUpdateSubresourceUP(D3D11_1)</a> function.</p>
</dd>

### -field pfnVsSetConstantBuffers

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-setconstantbuffers.md">VsSetConstantBuffers(D3D11_1)</a> function.</p>
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
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. For more information about whether to implement a separate <i>DynamicIABufferMapNoOverwrite</i> function or to point to the multipurpose <i>ResourceMap</i>, see the Remarks section of <i>ResourceMap</i>. </p>
</dd>

### -field pfnDynamicIABufferUnmap

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceunmap.md">ResourceUnmap</a> function. For more information about whether to implement a separate <i>DynamicIABufferUnmap</i> function or to point to the multipurpose <i>ResourceUnmap</i>, see the Remarks section of <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a>. </p>
</dd>

### -field pfnDynamicConstantBufferMapDiscard

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. For more information about whether to implement a separate <i>DynamicConstantBufferMapDiscard</i> function or to point to the multipurpose <i>ResourceMap</i>, see the Remarks section of <i>ResourceMap</i>. </p>
</dd>

### -field pfnDynamicIABufferMapDiscard

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. For more information about whether to implement a separate <i>DynamicIABufferMapDiscard</i> function or to point to the multipurpose <i>ResourceMap</i>, see the Remarks section of <i>ResourceMap</i>. </p>
</dd>

### -field pfnDynamicConstantBufferUnmap

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceunmap.md">ResourceUnmap</a> function. For more information about whether to implement a separate <i>DynamicConstantBufferUnmap</i> function or to point to the multipurpose <i>ResourceUnmap</i>, see the Remarks section of <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a>. </p>
</dd>

### -field pfnPsSetConstantBuffers

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-setconstantbuffers.md">PsSetConstantBuffers(D3D11_1)</a> function.</p>
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
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. For more information about whether to implement a separate <i>DynamicResourceMapDiscard</i> function or to point to the multipurpose <i>ResourceMap</i>, see the Remarks section of <i>ResourceMap</i>. </p>
</dd>

### -field pfnDynamicResourceUnmap

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceunmap.md">ResourceUnmap</a> function. For more information about whether to implement a separate <i>DynamicResourceUnmap</i> function or to point to the multipurpose <i>ResourceUnmap</i>, see the Remarks section of <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a>. </p>
</dd>

### -field pfnGsSetConstantBuffers

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-setconstantbuffers.md">GsSetConstantBuffers(D3D11_1)</a> function.</p>
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
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. For more information about whether to implement a separate <i>StagingResourceMap</i> function or to point to the multipurpose <i>ResourceMap</i>, see the Remarks section of <i>ResourceMap</i>. </p>
</dd>

### -field pfnStagingResourceUnmap

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceunmap.md">ResourceUnmap</a> function. For more information about whether to implement a separate <i>StagingResourceUnmap</i> function or to point to the multipurpose <i>ResourceUnmap</i>, see the Remarks section of <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a>. </p>
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
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-setrendertargets.md">SetRenderTargets(D3D11)</a> function.</p>
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
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-resourcecopyregion.md">ResourceCopyRegion(D3D11_1)</a> function.</p>
</dd>

### -field pfnResourceUpdateSubresourceUP

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-resourceupdatesubresourceup.md">ResourceUpdateSubresourceUP(D3D11_1)</a> function.</p>
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
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-flush.md">Flush(D3D11_1)</a> function.</p>
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
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-relocatedevicefuncs.md">RelocateDeviceFuncs(D3D11_1)</a> function.</p>
</dd>

### -field pfnCalcPrivateResourceSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-calcprivateresourcesize.md">CalcPrivateResourceSize(D3D11)</a> function.</p>
</dd>

### -field pfnCalcPrivateOpenedResourceSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivateopenedresourcesize.md">CalcPrivateOpenedResourceSize</a> function.</p>
</dd>

### -field pfnCreateResource

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createresource.md">CreateResource(D3D11)</a> function.</p>
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
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-calcprivateshaderresourceviewsize.md">CalcPrivateShaderResourceViewSize(D3D11)</a> function.</p>
</dd>

### -field pfnCreateShaderResourceView

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createshaderresourceview.md">CreateShaderResourceView(D3D11)</a> function.</p>
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
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-calcprivatedepthstencilviewsize.md">CalcPrivateDepthStencilViewSize(D3D11)</a> function.</p>
</dd>

### -field pfnCreateDepthStencilView

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createdepthstencilview.md">CreateDepthStencilView(D3D11)</a> function.</p>
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
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-calcprivateblendstatesize.md">CalcPrivateBlendStateSize(D3D11_1)</a> function.</p>
</dd>

### -field pfnCreateBlendState

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createblendstate.md">CreateBlendState(D3D11_1)</a> function.</p>
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
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-calcprivaterasterizerstatesize.md">CalcPrivateRasterizerStateSize(D3D11_1)</a> function.</p>
</dd>

### -field pfnCreateRasterizerState

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createrasterizerstate.md">CreateRasterizerState(D3D11_1)</a> function.</p>
</dd>

### -field pfnDestroyRasterizerState

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyrasterizerstate.md">DestroyRasterizerState</a> function.</p>
</dd>

### -field pfnCalcPrivateShaderSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-calcprivateshadersize.md">CalcPrivateShaderSize(D3D11_1)</a> function.</p>
</dd>

### -field pfnCreateVertexShader

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createvertexshader.md">CreateVertexShader(D3D11_1)</a> function.</p>
</dd>

### -field pfnCreateGeometryShader

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-creategeometryshader.md">CreateGeometryShader(D3D11_1)</a> function.</p>
</dd>

### -field pfnCreatePixelShader

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createpixelshader.md">CreatePixelShader(D3D11_1)</a> function.</p>
</dd>

### -field pfnCalcPrivateGeometryShaderWithStreamOutput

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-calcprivategeometryshaderwithstreamoutput.md">CalcPrivateGeometryShaderWithStreamOutput(D3D11_1)</a> function.</p>
</dd>

### -field pfnCreateGeometryShaderWithStreamOutput

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-creategeometryshaderwithstreamoutput.md">CreateGeometryShaderWithStreamOutput(D3D11_1)</a> function.</p>
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

### -field pfnResourceConvert

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcecopy.md">ResourceCopy</a> function. For more information about whether to implement a separate <i>ResourceConvert</i> function or to point to the multipurpose <i>ResourceCopy</i>, see the Remarks section of <i>ResourceCopy</i>.</p>
</dd>

### -field pfnResourceConvertRegion

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-resourcecopyregion.md">ResourceCopyRegion(D3D11_1)</a> function. For more information about whether to implement a separate <i>ResourceConvertRegion(D3D11_1)</i> function or to point to the multipurpose <i>ResourceCopyRegion(D3D11_1)</i>, see the Remarks section of <i>ResourceCopyRegion(D3D11_1)</i>.</p>
</dd>

### -field pfnDrawIndexedInstancedIndirect

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-drawindexedinstancedindirect.md">DrawIndexedInstancedIndirect</a> function.</p>
</dd>

### -field pfnDrawInstancedIndirect

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-drawinstancedindirect.md">DrawInstancedIndirect</a> function.</p>
</dd>

### -field pfnCommandListExecute

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-commandlistexecute.md">CommandListExecute</a> function. The driver is only required to implement <i>CommandListExecute</i> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability. </p>
</dd>

### -field pfnHsSetShaderResources

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshaderresources.md">HsSetShaderResources</a> function.</p>
</dd>

### -field pfnHsSetShader

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshader.md">HsSetShader</a> function.</p>
</dd>

### -field pfnHsSetSamplers

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setsamplers.md">HsSetSamplers</a> function.</p>
</dd>

### -field pfnHsSetConstantBuffers

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-setconstantbuffers.md">HsSetConstantBuffers(D3D11_1)</a> function.</p>
</dd>

### -field pfnDsSetShaderResources

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshaderresources.md">DsSetShaderResources</a> function.</p>
</dd>

### -field pfnDsSetShader

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshader.md">DsSetShader</a> function.</p>
</dd>

### -field pfnDsSetSamplers

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setsamplers.md">DsSetSamplers</a> function.</p>
</dd>

### -field pfnDsSetConstantBuffers

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-setconstantbuffers.md">DsSetConstantBuffers(D3D11_1)</a> function.</p>
</dd>

### -field pfnCreateHullShader

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createhullshader.md">CreateHullShader(D3D11_1)</a> function.</p>
</dd>

### -field pfnCreateDomainShader

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createdomainshader.md">CreateDomainShader(D3D11_1)</a> function.</p>
</dd>

### -field pfnCheckDeferredContextHandleSizes

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-checkdeferredcontexthandlesizes.md">CheckDeferredContextHandleSizes</a> function. The driver is only required to implement <i>CheckDeferredContextHandleSizes</i> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability. </p>
</dd>

### -field pfnCalcDeferredContextHandleSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-calcdeferredcontexthandlesize.md">CalcDeferredContextHandleSize</a> function. The driver is only required to implement <i>CalcDeferredContextHandleSize</i> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability. </p>
</dd>

### -field pfnCalcPrivateDeferredContextSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-calcprivatedeferredcontextsize.md">CalcPrivateDeferredContextSize</a> function. The driver is only required to implement <i>CalcPrivateDeferredContextSize</i> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability. </p>
</dd>

### -field pfnCreateDeferredContext

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createdeferredcontext.md">CreateDeferredContext</a> function. The driver is only required to implement <i>CreateDeferredContext</i> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability. </p>
</dd>

### -field pfnAbandonCommandList

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-abandoncommandlist.md">AbandonCommandList</a> function. The driver is only required to implement <i>AbandonCommandList</i> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability. </p>
</dd>

### -field pfnCalcPrivateCommandListSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-calcprivatecommandlistsize.md">CalcPrivateCommandListSize</a> function. The driver is only required to implement <i>CalcPrivateCommandListSize</i> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability. </p>
</dd>

### -field pfnCreateCommandList

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createcommandlist.md">CreateCommandList</a> function. The driver is only required to implement <i>CreateCommandList</i> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability. </p>
</dd>

### -field pfnDestroyCommandList

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-destroycommandlist.md">DestroyCommandList</a> function. The driver is only required to implement <i>DestroyCommandList</i> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability. </p>
</dd>

### -field pfnCalcPrivateTessellationShaderSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-calcprivatetessellationshadersize.md">CalcPrivateTessellationShaderSize(D3D11_1)</a> function. </p>
</dd>

### -field pfnPsSetShaderWithIfaces

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-setshader-with-ifaces.md">PsSetShaderWithIfaces</a> function. </p>
</dd>

### -field pfnVsSetShaderWithIfaces

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-setshader-with-ifaces.md">VsSetShaderWithIfaces</a> function. </p>
</dd>

### -field pfnGsSetShaderWithIfaces

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-setshader-with-ifaces.md">GsSetShaderWithIfaces</a> function. </p>
</dd>

### -field pfnHsSetShaderWithIfaces

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-setshader-with-ifaces.md">HsSetShaderWithIfaces</a> function. </p>
</dd>

### -field pfnDsSetShaderWithIfaces

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-setshader-with-ifaces.md">DsSetShaderWithIfaces</a> function. </p>
</dd>

### -field pfnCsSetShaderWithIfaces

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-setshader-with-ifaces.md">CsSetShaderWithIfaces</a> function. </p>
</dd>

### -field pfnCreateComputeShader

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createcomputeshader.md">CreateComputeShader</a> function. </p>
</dd>

### -field pfnCsSetShader

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshader.md">CsSetShader</a> function. </p>
</dd>

### -field pfnCsSetShaderResources

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setshaderresources.md">CsSetShaderResources</a> function. </p>
</dd>

### -field pfnCsSetSamplers

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-setsamplers.md">CsSetSamplers</a> function. </p>
</dd>

### -field pfnCsSetConstantBuffers

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-setconstantbuffers.md">CsSetConstantBuffers(D3D11_1)</a> function. </p>
</dd>

### -field pfnCalcPrivateUnorderedAccessViewSize

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-calcprivateunorderedaccessviewsize.md">CalcPrivateUnorderedAccessViewSize</a> function. </p>
</dd>

### -field pfnCreateUnorderedAccessView

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createunorderedaccessview.md">CreateUnorderedAccessView</a> function. </p>
</dd>

### -field pfnDestroyUnorderedAccessView

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-destroyunorderedaccessview.md">DestroyUnorderedAccessView</a> function. </p>
</dd>

### -field pfnClearUnorderedAccessViewUint

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-clearunorderedaccessviewuint.md">ClearUnorderedAccessViewUINT</a> function. </p>
</dd>

### -field pfnClearUnorderedAccessViewFloat

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-clearunorderedaccessviewfloat.md">ClearUnorderedAccessViewFLOAT</a> function. </p>
</dd>

### -field pfnCsSetUnorderedAccessViews

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-setunorderedaccessviews.md">CsSetUnorderedAccessViews</a> function. </p>
</dd>

### -field pfnDispatch

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-dispatch.md">Dispatch</a> function. </p>
</dd>

### -field pfnDispatchIndirect

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-dispatchindirect.md">DispatchIndirect</a> function. </p>
</dd>

### -field pfnSetResourceMinLOD

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-setresourceminlod.md">SetResourceMinLOD</a> function. </p>
</dd>

### -field pfnCopyStructureCount

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-copystructurecount.md">CopyStructureCount</a> function. </p>
</dd>

### -field pfnRecycleCommandList

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-recyclecommandlist.md">RecycleCommandList</a> function. </p>
</dd>

### -field pfnRecycleCreateCommandList

<dd>
<p>A pointer to the driver's   <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-recyclecreatecommandlist.md">RecycleCreateCommandList</a> function. </p>
</dd>

### -field pfnRecycleCreateDeferredContext

<dd>
<p>A pointer to the driver's  <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-recyclecreatedeferredcontext.md">RecycleCreateDeferredContext</a> function. </p>
</dd>

### -field pfnRecycleDestroyCommandList

<dd>
<p>A pointer to the driver's  <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-destroycommandlist.md">RecycleDestroyCommandList</a> function.</p>
</dd>

### -field pfnDiscard

<dd>
<p>A pointer to the driver's  <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-discard.md">Discard(D3D11_1)</a> function. </p>
</dd>

### -field pfnAssignDebugBinary

<dd>
<p>A pointer to the driver's  <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-assigndebugbinary.md">AssignDebugBinary</a> function.</p>
</dd>

### -field pfnDynamicConstantBufferMapNoOverwrite

<dd>
<p>A pointer to the driver's  <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. </p>
</dd>

### -field pfnCheckDirectFlipSupport

<dd>
<p>A pointer to the driver's  <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-checkdirectflipsupport.md">CheckDirectFlipSupport(D3D11_1)</a> function. </p>
</dd>

### -field pfnClearView

<dd>
<p>A pointer to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-clearview.md">ClearView</a>  function. </p>
</dd>
</dl>

## -remarks
<p>The order of user-mode display driver functions (that is, the order of the members of the <b>D3D11_1DDI_DEVICEFUNCS</b> structure) is in decreasing order of priority (in regard to performance).</p>

<p>The user-mode display driver can use different names for these functions because the address of the function table (this structure) is shared between the Direct3D 11.1 runtime and the driver through the call to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a> function.</p>

<p>The <b>pfnResetPrimitiveID</b> and  <b>pfnSetVertexPipelineOutput</b> members (not shown here) and their data types are reserved for system use and should not be used in your driver.</p>

<p>For a list of the functions that are not leveraged for deferred contexts, see <a href="https://msdn.microsoft.com/f6e7898a-7fb8-4a70-ab2e-3372a28db6f4">Excluding DDI Functions for Deferred Contexts</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi-devicefuncs~r1.md">D3D11DDI_DEVICEFUNCS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDI_DEVICEFUNCS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
