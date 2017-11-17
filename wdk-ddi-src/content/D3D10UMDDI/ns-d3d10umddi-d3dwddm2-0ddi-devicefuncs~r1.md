---
UID: NS.d3d10umddi.D3DWDDM2_0DDI_DEVICEFUNCS~r1
title: D3DWDDM2_0DDI_DEVICEFUNCS
author: windows-driver-content
description: This structure contains the user mode device function table for Windows Display Driver Model (WDDM) 2.0.
old-location: display\d3dwddm2_0ddi_devicefuncs.htm
ms.assetid: 9A41512A-91C4-4053-9C60-5B485E93D14B
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DWDDM2_0DDI_DEVICEFUNCS
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
ms.keywords: D3DWDDM2_0DDI_DEVICEFUNCS, D3DWDDM2_0DDI_DEVICEFUNCS
req.iface: 
---

# D3DWDDM2_0DDI_DEVICEFUNCS structure



## -description
<p>This structure contains the user mode device function table for Windows Display Driver Model (WDDM) 2.0.</p>


## -syntax

````
typedef struct D3DWDDM2_0DDI_DEVICEFUNCS {
  PFND3D11_1DDI_RESOURCEUPDATESUBRESOURCEUP               pfnDefaultConstantBufferUpdateSubresourceUP;
  PFND3D11_1DDI_SETCONSTANTBUFFERS                        pfnVsSetConstantBuffers;
  PFND3D10DDI_SETSHADERRESOURCES                          pfnPsSetShaderResources;
  PFND3D10DDI_SETSHADER                                   pfnPsSetShader;
  PFND3D10DDI_SETSAMPLERS                                 pfnPsSetSamplers;
  PFND3D10DDI_SETSHADER                                   pfnVsSetShader;
  PFND3D10DDI_DRAWINDEXED                                 pfnDrawIndexed;
  PFND3D10DDI_DRAW                                        pfnDraw;
  PFND3D11_1DDI_SETCONSTANTBUFFERS                        pfnPsSetConstantBuffers;
  PFND3D10DDI_SETINPUTLAYOUT                              pfnIaSetInputLayout;
  PFND3D10DDI_IA_SETVERTEXBUFFERS                         pfnIaSetVertexBuffers;
  PFND3D10DDI_IA_SETINDEXBUFFER                           pfnIaSetIndexBuffer;
  PFND3D10DDI_DRAWINDEXEDINSTANCED                        pfnDrawIndexedInstanced;
  PFND3D10DDI_DRAWINSTANCED                               pfnDrawInstanced;
  PFND3D11_1DDI_SETCONSTANTBUFFERS                        pfnGsSetConstantBuffers;
  PFND3D10DDI_SETSHADER                                   pfnGsSetShader;
  PFND3D10DDI_IA_SETTOPOLOGY                              pfnIaSetTopology;
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
  PFND3DWDDM2_0DDI_RELOCATEDEVICEFUNCS                    pfnRelocateDeviceFuncs;
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
  PFND3DWDDM2_0DDI_CALCPRIVATERASTERIZERSTATESIZE         pfnCalcPrivateRasterizerStateSize;
  PFND3DWDDM2_0DDI_CREATERASTERIZERSTATE                  pfnCreateRasterizerState;
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
  PFND3DWDDM1_3DDI_CHECKMULTISAMPLEQUALITYLEVELS          pfnCheckMultisampleQualityLevels;
  PFND3D10DDI_CHECKCOUNTERINFO                            pfnCheckCounterInfo;
  PFND3D10DDI_CHECKCOUNTER                                pfnCheckCounter;
  PFND3D10DDI_DESTROYDEVICE                               pfnDestroyDevice;
  PFND3D10DDI_SETTEXTFILTERSIZE                           pfnSetTextFilterSize;
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
  PFND3D11_1DDI_DISCARD                                   pfnDiscard;
  PFND3D11_1DDI_ASSIGNDEBUGBINARY                         pfnAssignDebugBinary;
  PFND3D11_1DDI_CHECKDIRECTFLIPSUPPORT                    pfnCheckDirectFlipSupport;
  PFND3D11_1DDI_CLEARVIEW                                 pfnClearView;
  PFND3DWDDM1_3DDI_UPDATETILEMAPPINGS                     pfnUpdateTileMappings;
  PFND3DWDDM1_3DDI_COPYTILEMAPPINGS                       pfnCopyTileMappings;
  PFND3DWDDM1_3DDI_COPYTILES                              pfnCopyTiles;
  PFND3DWDDM1_3DDI_UPDATETILES                            pfnUpdateTiles;
  PFND3DWDDM1_3DDI_TILEDRESOURCEBARRIER                   pfnTiledResourceBarrier;
  PFND3DWDDM1_3DDI_GETMIPPACKING                          pfnGetMipPacking;
  PFND3DWDDM1_3DDI_RESIZETILEPOOL                         pfnResizeTilePool;
  PFND3DWDDM1_3DDI_SETMARKER                              pfnSetMarker;
  PFND3DWDDM1_3DDI_SETMARKERMODE                          pfnSetMarkerMode;
  PFND3DWDDM2_0DDI_SETHARDWAREPROTECTION                  pfnSetHardwareProtection;
} D3DWDDM2_0DDI_DEVICEFUNCS;
````


## -struct-fields
<dl>

### -field <b>pfnDefaultConstantBufferUpdateSubresourceUP</b>

<dd>
<p>A pointer to the <a href="display.DefaultConstantBufferUpdateSubresourceUP">DefaultConstantBufferUpdateSubresourceUP</a> function.</p>
</dd>

### -field <b>pfnVsSetConstantBuffers</b>

<dd>
<p>A pointer to the <a href="display.VsSetConstantBuffers">VsSetConstantBuffers</a> function.</p>
</dd>

### -field <b>pfnPsSetShaderResources</b>

<dd>
<p>A pointer to the <a href="display.PsSetShaderResources">PsSetShaderResources</a> function.</p>
</dd>

### -field <b>pfnPsSetShader</b>

<dd>
<p>A pointer to the <a href="display.PsSetShader">PsSetShader</a> function.</p>
</dd>

### -field <b>pfnPsSetSamplers</b>

<dd>
<p>A pointer to the <a href="display.PsSetSamplers">PsSetSamplers</a> function.</p>
</dd>

### -field <b>pfnVsSetShader</b>

<dd>
<p>A pointer to the <a href="display.VsSetShader">VsSetShader</a> function.</p>
</dd>

### -field <b>pfnDrawIndexed</b>

<dd>
<p>A pointer to the <a href="display.DrawIndexed">DrawIndexed</a> function.</p>
</dd>

### -field <b>pfnDraw</b>

<dd>
<p>A pointer to the <a href="display.Draw">Draw</a> function.</p>
</dd>

### -field <b>pfnPsSetConstantBuffers</b>

<dd>
<p>A pointer to the <a href="display.PsSetConstantBuffers">PsSetConstantBuffers</a> function.</p>
</dd>

### -field <b>pfnIaSetInputLayout</b>

<dd>
<p>A pointer to the <a href="display.IaSetInputLayout">IaSetInputLayout</a> function.</p>
</dd>

### -field <b>pfnIaSetVertexBuffers</b>

<dd>
<p>A pointer to the <a href="display.IaSetVertexBuffers">IaSetVertexBuffers</a> function.</p>
</dd>

### -field <b>pfnIaSetIndexBuffer</b>

<dd>
<p>A pointer to the <a href="display.IaSetIndexBuffer">IaSetIndexBuffer</a> function.</p>
</dd>

### -field <b>pfnDrawIndexedInstanced</b>

<dd>
<p>A pointer to the <a href="display.DrawIndexedInstanced">DrawIndexedInstanced</a> function.</p>
</dd>

### -field <b>pfnDrawInstanced</b>

<dd>
<p>A pointer to the <a href="display.DrawInstanced">DrawInstanced</a> function.</p>
</dd>

### -field <b>pfnGsSetConstantBuffers</b>

<dd>
<p>A pointer to the <a href="display.GsSetConstantBuffers">GsSetConstantBuffers</a> function.</p>
</dd>

### -field <b>pfnGsSetShader</b>

<dd>
<p>A pointer to the <a href="display.GsSetShader">GsSetShader</a> function.</p>
</dd>

### -field <b>pfnIaSetTopology</b>

<dd>
<p>A pointer to the <a href="display.IaSetTopology">IaSetTopology</a> function.</p>
</dd>

### -field <b>pfnVsSetShaderResources</b>

<dd>
<p>A pointer to the <a href="display.VsSetShaderResources">VsSetShaderResources</a> function.</p>
</dd>

### -field <b>pfnVsSetSamplers</b>

<dd>
<p>A pointer to the <a href="display.VsSetSamplers">VsSetSamplers</a> function.</p>
</dd>

### -field <b>pfnGsSetShaderResources</b>

<dd>
<p>A pointer to the <a href="display.GsSetShaderResources">GsSetShaderResources</a> function.</p>
</dd>

### -field <b>pfnGsSetSamplers</b>

<dd>
<p>A pointer to the <a href="display.GsSetSamplers">GsSetSamplers</a> function.</p>
</dd>

### -field <b>pfnSetRenderTargets</b>

<dd>
<p>A pointer to the <a href="display.SetRenderTargets">SetRenderTargets</a> function.</p>
</dd>

### -field <b>pfnShaderResourceViewReadAfterWriteHazard</b>

<dd>
<p>A pointer to the <a href="display.ShaderResourceViewReadAfterWriteHazard">ShaderResourceViewReadAfterWriteHazard</a> function.</p>
</dd>

### -field <b>pfnResourceReadAfterWriteHazard</b>

<dd>
<p>A pointer to the <a href="display.ResourceReadAfterWriteHazard">ResourceReadAfterWriteHazard</a> function.</p>
</dd>

### -field <b>pfnSetBlendState</b>

<dd>
<p>A pointer to the <a href="display.SetBlendState">SetBlendState</a> function.</p>
</dd>

### -field <b>pfnSetDepthStencilState</b>

<dd>
<p>A pointer to the <a href="display.SetDepthStencilState">SetDepthStencilState</a> function.</p>
</dd>

### -field <b>pfnSetRasterizerState</b>

<dd>
<p>A pointer to the <a href="display.SetRasterizerState">SetRasterizerState</a> function.</p>
</dd>

### -field <b>pfnQueryEnd</b>

<dd>
<p>A pointer to the <a href="display.QueryEnd">QueryEnd</a> function.</p>
</dd>

### -field <b>pfnQueryBegin</b>

<dd>
<p>A pointer to the <a href="display.QueryBegin">QueryBegin</a> function.</p>
</dd>

### -field <b>pfnResourceCopyRegion</b>

<dd>
<p>A pointer to the <a href="display.ResourceCopyRegion">ResourceCopyRegion</a> function.</p>
</dd>

### -field <b>pfnResourceUpdateSubresourceUP</b>

<dd>
<p>A pointer to the <a href="display.ResourceUpdateSubresourceUP">ResourceUpdateSubresourceUP</a> function.</p>
</dd>

### -field <b>pfnSoSetTargets</b>

<dd>
<p>A pointer to the <a href="display.SoSetTargets">SoSetTargets</a> function.</p>
</dd>

### -field <b>pfnDrawAuto</b>

<dd>
<p>A pointer to the <a href="display.DrawAuto">DrawAuto</a> function.</p>
</dd>

### -field <b>pfnSetViewports</b>

<dd>
<p>A pointer to the <a href="display.SetViewports">SetViewports</a> function.</p>
</dd>

### -field <b>pfnSetScissorRects</b>

<dd>
<p>A pointer to the <a href="display.SetScissorRects">SetScissorRects</a> function.</p>
</dd>

### -field <b>pfnClearRenderTargetView</b>

<dd>
<p>A pointer to the <a href="display.ClearRenderTargetView">ClearRenderTargetView</a> function.</p>
</dd>

### -field <b>pfnClearDepthStencilView</b>

<dd>
<p>A pointer to the <a href="display.ClearDepthStencilView">ClearDepthStencilView</a> function.</p>
</dd>

### -field <b>pfnSetPredication</b>

<dd>
<p>A pointer to the <a href="display.SetPredication">SetPredication</a> function.</p>
</dd>

### -field <b>pfnQueryGetData</b>

<dd>
<p>A pointer to the <a href="display.QueryGetData">QueryGetData</a> function.</p>
</dd>

### -field <b>pfnFlush</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh463886">Flush</a> function.</p>
</dd>

### -field <b>pfnGenMips</b>

<dd>
<p>A pointer to the <a href="display.GenMips">GenMips</a> function.</p>
</dd>

### -field <b>pfnResourceCopy</b>

<dd>
<p>A pointer to the <a href="display.ResourceCopy">ResourceCopy</a> function.</p>
</dd>

### -field <b>pfnResourceResolveSubresource</b>

<dd>
<p>A pointer to the <a href="display.ResourceResolveSubresource">ResourceResolveSubresource</a> function.</p>
</dd>

### -field <b>pfnResourceMap</b>

<dd>
<p>A pointer to the <a href="display.ResourceMap">ResourceMap</a> function.</p>
</dd>

### -field <b>pfnResourceUnmap</b>

<dd>
<p>A pointer to the <a href="display.ResourceUnmap">ResourceUnmap</a> function.</p>
</dd>

### -field <b>pfnResourceIsStagingBusy</b>

<dd>
<p>A pointer to the <a href="display.ResourceIsStagingBusy">ResourceIsStagingBusy</a> function.</p>
</dd>

### -field <b>pfnRelocateDeviceFuncs</b>

<dd>
<p>A pointer to the <a href="display.RelocateDeviceFuncs">RelocateDeviceFuncs</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateResourceSize</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateResourceSize">CalcPrivateResourceSize</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateOpenedResourceSize</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateOpenedResourceSize">CalcPrivateOpenedResourceSize</a> function.</p>
</dd>

### -field <b>pfnCreateResource</b>

<dd>
<p>A pointer to the <a href="display.CreateResource">CreateResource</a> function.</p>
</dd>

### -field <b>pfnOpenResource</b>

<dd>
<p>A pointer to the <a href="display.OpenResource">OpenResource</a> function.</p>
</dd>

### -field <b>pfnDestroyResource</b>

<dd>
<p>A pointer to the <a href="display.DestroyResource">DestroyResource</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateShaderResourceViewSize</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateShaderResourceViewSize">CalcPrivateShaderResourceViewSize</a> function.</p>
</dd>

### -field <b>pfnCreateShaderResourceView</b>

<dd>
<p>A pointer to the <a href="display.CreateShaderResourceView">CreateShaderResourceView</a> function.</p>
</dd>

### -field <b>pfnDestroyShaderResourceView</b>

<dd>
<p>A pointer to the <a href="display.DestroyShaderResourceView">DestroyShaderResourceView</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateRenderTargetViewSize</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateRenderTargetViewSize">CalcPrivateRenderTargetViewSize</a> function.</p>
</dd>

### -field <b>pfnCreateRenderTargetView</b>

<dd>
<p>A pointer to the <a href="display.CreateRenderTargetView">CreateRenderTargetView</a> function.</p>
</dd>

### -field <b>pfnDestroyRenderTargetView</b>

<dd>
<p>A pointer to the <a href="display.DestroyRenderTargetView">DestroyRenderTargetView</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateDepthStencilViewSize</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateDepthStencilViewSize">CalcPrivateDepthStencilViewSize</a> function.</p>
</dd>

### -field <b>pfnCreateDepthStencilView</b>

<dd>
<p>A pointer to the <a href="display.CreateDepthStencilView">CreateDepthStencilView</a> function.</p>
</dd>

### -field <b>pfnDestroyDepthStencilView</b>

<dd>
<p>A pointer to the <a href="display.DestroyDepthStencilView">DestroyDepthStencilView</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateElementLayoutSize</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateElementLayoutSize">CalcPrivateElementLayoutSize</a> function.</p>
</dd>

### -field <b>pfnCreateElementLayout</b>

<dd>
<p>A pointer to the <a href="display.CreateElementLayout">CreateElementLayout</a> function.</p>
</dd>

### -field <b>pfnDestroyElementLayout</b>

<dd>
<p>A pointer to the <a href="display.DestroyElementLayout">DestroyElementLayout</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateBlendStateSize</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateBlendStateSize">CalcPrivateBlendStateSize</a> function.</p>
</dd>

### -field <b>pfnCreateBlendState</b>

<dd>
<p>A pointer to the <a href="display.CreateBlendState">CreateBlendState</a> function.</p>
</dd>

### -field <b>pfnDestroyBlendState</b>

<dd>
<p>A pointer to the <a href="display.DestroyBlendState">DestroyBlendState</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateDepthStencilStateSize</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateDepthStencilStateSize">CalcPrivateDepthStencilStateSize</a> function.</p>
</dd>

### -field <b>pfnCreateDepthStencilState</b>

<dd>
<p>A pointer to the <a href="display.CreateDepthStencilState">CreateDepthStencilState</a> function.</p>
</dd>

### -field <b>pfnDestroyDepthStencilState</b>

<dd>
<p>A pointer to the <a href="display.DestroyDepthStencilState">DestroyDepthStencilState</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateRasterizerStateSize</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateRasterizerStateSize">CalcPrivateRasterizerStateSize</a> function.</p>
</dd>

### -field <b>pfnCreateRasterizerState</b>

<dd>
<p>A pointer to the <a href="display.CreateRasterizerState">CreateRasterizerState</a> function.</p>
</dd>

### -field <b>pfnDestroyRasterizerState</b>

<dd>
<p>A pointer to the <a href="display.DestroyRasterizerState">DestroyRasterizerState</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateShaderSize</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateShaderSize">CalcPrivateShaderSize</a> function.</p>
</dd>

### -field <b>pfnCreateVertexShader</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/8da896d3-b80c-409a-a838-99eb71668a93">CreateVertexShader</a> function.</p>
</dd>

### -field <b>pfnCreateGeometryShader</b>

<dd>
<p>A pointer to the <a href="display.CreateGeometryShader">CreateGeometryShader</a> function.</p>
</dd>

### -field <b>pfnCreatePixelShader</b>

<dd>
<p>A pointer to the <a href="display.CreatePixelShader">CreatePixelShader</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateGeometryShaderWithStreamOutput</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateGeometryShaderWithStreamOutput">CalcPrivateGeometryShaderWithStreamOutput</a> function.</p>
</dd>

### -field <b>pfnCreateGeometryShaderWithStreamOutput</b>

<dd>
<p>A pointer to the <a href="display.CreateGeometryShaderWithStreamOutput">CreateGeometryShaderWithStreamOutput</a> function.</p>
</dd>

### -field <b>pfnDestroyShader</b>

<dd>
<p>A pointer to the <a href="display.DestroyShader">DestroyShader</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateSamplerSize</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateSamplerSize">CalcPrivateSamplerSize</a> function.</p>
</dd>

### -field <b>pfnCreateSampler</b>

<dd>
<p>A pointer to the <a href="display.CreateSampler">CreateSampler</a> function.</p>
</dd>

### -field <b>pfnDestroySampler</b>

<dd>
<p>A pointer to the <a href="display.DestroySampler">DestroySampler</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateQuerySize</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateQuerySize">CalcPrivateQuerySize</a> function.</p>
</dd>

### -field <b>pfnCreateQuery</b>

<dd>
<p>A pointer to the <a href="display.CreateQuery">CreateQuery</a> function.</p>
</dd>

### -field <b>pfnDestroyQuery</b>

<dd>
<p>A pointer to the <a href="display.DestroyQuery">DestroyQuery</a> function.</p>
</dd>

### -field <b>pfnCheckFormatSupport</b>

<dd>
<p>A pointer to the <a href="display.CheckFormatSupport">CheckFormatSupport</a> function.</p>
</dd>

### -field <b>pfnCheckMultisampleQualityLevels</b>

<dd>
<p>A pointer to the <a href="display.CheckMultisampleQualityLevels">CheckMultisampleQualityLevels</a> function.</p>
</dd>

### -field <b>pfnCheckCounterInfo</b>

<dd>
<p>A pointer to the <a href="display.CheckCounterInfo">CheckCounterInfo</a> function.</p>
</dd>

### -field <b>pfnCheckCounter</b>

<dd>
<p>A pointer to the <a href="display.CheckCounter">CheckCounter</a> function.</p>
</dd>

### -field <b>pfnDestroyDevice</b>

<dd>
<p>A pointer to the <a href="display.DestroyDevice">DestroyDevice</a> function.</p>
</dd>

### -field <b>pfnSetTextFilterSize</b>

<dd>
<p>A pointer to the <a href="display.SetTextFilterSize">SetTextFilterSize</a> function.</p>
</dd>

### -field <b>pfnDrawIndexedInstancedIndirect</b>

<dd>
<p>A pointer to the <a href="display.DrawIndexedInstancedIndirect">DrawIndexedInstancedIndirect</a> function.</p>
</dd>

### -field <b>pfnDrawInstancedIndirect</b>

<dd>
<p>A pointer to the <a href="display.DrawInstancedIndirect">DrawInstancedIndirect</a> function.</p>
</dd>

### -field <b>pfnCommandListExecute</b>

<dd>
<p>A pointer to the <a href="display.CommandListExecute">CommandListExecute</a> function.</p>
</dd>

### -field <b>pfnHsSetShaderResources</b>

<dd>
<p>A pointer to the <a href="display.HsSetShaderResources">HsSetShaderResources</a> function.</p>
</dd>

### -field <b>pfnHsSetShader</b>

<dd>
<p>A pointer to the <a href="display.HsSetShader">HsSetShader</a> function.</p>
</dd>

### -field <b>pfnHsSetSamplers</b>

<dd>
<p>A pointer to the <a href="display.HsSetSamplers">HsSetSamplers</a> function.</p>
</dd>

### -field <b>pfnHsSetConstantBuffers</b>

<dd>
<p>A pointer to the <a href="display.HsSetConstantBuffers">HsSetConstantBuffers</a> function.</p>
</dd>

### -field <b>pfnDsSetShaderResources</b>

<dd>
<p>A pointer to the <a href="display.DsSetShaderResources">DsSetShaderResources</a> function.</p>
</dd>

### -field <b>pfnDsSetShader</b>

<dd>
<p>A pointer to the <a href="display.DsSetShader">DsSetShader</a> function.</p>
</dd>

### -field <b>pfnDsSetSamplers</b>

<dd>
<p>A pointer to the <a href="display.DsSetSamplers">DsSetSamplers</a> function.</p>
</dd>

### -field <b>pfnDsSetConstantBuffers</b>

<dd>
<p>A pointer to the <a href="display.DsSetConstantBuffers">DsSetConstantBuffers</a> function.</p>
</dd>

### -field <b>pfnCreateHullShader</b>

<dd>
<p>A pointer to the <a href="display.CreateHullShader">CreateHullShader</a> function.</p>
</dd>

### -field <b>pfnCreateDomainShader</b>

<dd>
<p>A pointer to the <a href="display.CreateDomainShader">CreateDomainShader</a> function.</p>
</dd>

### -field <b>pfnCheckDeferredContextHandleSizes</b>

<dd>
<p>A pointer to the <a href="display.CheckDeferredContextHandleSizes">CheckDeferredContextHandleSizes</a> function.</p>
</dd>

### -field <b>pfnCalcDeferredContextHandleSize</b>

<dd>
<p>A pointer to the <a href="display.CalcDeferredContextHandleSize">CalcDeferredContextHandleSize</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateDeferredContextSize</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateDeferredContextSize">CalcPrivateDeferredContextSize</a> function.</p>
</dd>

### -field <b>pfnCreateDeferredContext</b>

<dd>
<p>A pointer to the <a href="display.CreateDeferredContext">CreateDeferredContext</a> function.</p>
</dd>

### -field <b>pfnAbandonCommandList</b>

<dd>
<p>A pointer to the <a href="display.AbandonCommandList">AbandonCommandList</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateCommandListSize</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateCommandListSize">CalcPrivateCommandListSize</a> function.</p>
</dd>

### -field <b>pfnCreateCommandList</b>

<dd>
<p>A pointer to the <a href="display.CreateCommandList">CreateCommandList</a> function.</p>
</dd>

### -field <b>pfnDestroyCommandList</b>

<dd>
<p>A pointer to the <a href="display.DestroyCommandList">DestroyCommandList</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateTessellationShaderSize</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateTessellationShaderSize">CalcPrivateTessellationShaderSize</a> function.</p>
</dd>

### -field <b>pfnPsSetShaderWithIfaces</b>

<dd>
<p>A pointer to the <a href="display.PsSetShaderWithIfaces">PsSetShaderWithIfaces</a> function.</p>
</dd>

### -field <b>pfnVsSetShaderWithIfaces</b>

<dd>
<p>A pointer to the <a href="display.VsSetShaderWithIfaces">VsSetShaderWithIfaces</a> function.</p>
</dd>

### -field <b>pfnGsSetShaderWithIfaces</b>

<dd>
<p>A pointer to the <a href="display.GsSetShaderWithIfaces">GsSetShaderWithIfaces</a> function.</p>
</dd>

### -field <b>pfnHsSetShaderWithIfaces</b>

<dd>
<p>A pointer to the <a href="display.HsSetShaderWithIfaces">HsSetShaderWithIfaces</a> function.</p>
</dd>

### -field <b>pfnDsSetShaderWithIfaces</b>

<dd>
<p>A pointer to the <a href="display.DsSetShaderWithIfaces">DsSetShaderWithIfaces</a> function.</p>
</dd>

### -field <b>pfnCsSetShaderWithIfaces</b>

<dd>
<p>A pointer to the <a href="display.CsSetShaderWithIfaces">CsSetShaderWithIfaces</a> function.</p>
</dd>

### -field <b>pfnCreateComputeShader</b>

<dd>
<p>A pointer to the <a href="display.CreateComputeShader">CreateComputeShader</a> function.</p>
</dd>

### -field <b>pfnCsSetShader</b>

<dd>
<p>A pointer to the <a href="display.CsSetShader">CsSetShader</a> function.</p>
</dd>

### -field <b>pfnCsSetShaderResources</b>

<dd>
<p>A pointer to the <a href="display.CsSetShaderResources">CsSetShaderResources</a> function.</p>
</dd>

### -field <b>pfnCsSetSamplers</b>

<dd>
<p>A pointer to the <a href="display.CsSetSamplers">CsSetSamplers</a> function.</p>
</dd>

### -field <b>pfnCsSetConstantBuffers</b>

<dd>
<p>A pointer to the <a href="display.CsSetConstantBuffers">CsSetConstantBuffers</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateUnorderedAccessViewSize</b>

<dd>
<p>A pointer to the <a href="display.CalcPrivateUnorderedAccessViewSize">CalcPrivateUnorderedAccessViewSize</a> function.</p>
</dd>

### -field <b>pfnCreateUnorderedAccessView</b>

<dd>
<p>A pointer to the <a href="display.CreateUnorderedAccessView">CreateUnorderedAccessView</a> function.</p>
</dd>

### -field <b>pfnDestroyUnorderedAccessView</b>

<dd>
<p>A pointer to the <a href="display.DestroyUnorderedAccessView">DestroyUnorderedAccessView</a> function.</p>
</dd>

### -field <b>pfnClearUnorderedAccessViewUint</b>

<dd>
<p>A pointer to the <a href="display.ClearUnorderedAccessViewUint">ClearUnorderedAccessViewUint</a> function.</p>
</dd>

### -field <b>pfnClearUnorderedAccessViewFloat</b>

<dd>
<p>A pointer to the <a href="display.ClearUnorderedAccessViewFloat">ClearUnorderedAccessViewFloat</a> function.</p>
</dd>

### -field <b>pfnCsSetUnorderedAccessViews</b>

<dd>
<p>A pointer to the <a href="display.CsSetUnorderedAccessViews">CsSetUnorderedAccessViews</a> function.</p>
</dd>

### -field <b>pfnDispatch</b>

<dd>
<p>A pointer to the <a href="display.Dispatch">Dispatch</a> function.</p>
</dd>

### -field <b>pfnDispatchIndirect</b>

<dd>
<p>A pointer to the <a href="display.DispatchIndirect">DispatchIndirect</a> function.</p>
</dd>

### -field <b>pfnSetResourceMinLOD</b>

<dd>
<p>A pointer to the <a href="display.SetResourceMinLOD">SetResourceMinLOD</a> function.</p>
</dd>

### -field <b>pfnCopyStructureCount</b>

<dd>
<p>A pointer to the <a href="display.CopyStructureCount">CopyStructureCount</a> function.</p>
</dd>

### -field <b>pfnRecycleCommandList</b>

<dd>
<p>A pointer to the <a href="display.RecycleCommandList">RecycleCommandList</a> function.</p>
</dd>

### -field <b>pfnRecycleCreateCommandList</b>

<dd>
<p>A pointer to the <a href="display.RecycleCreateCommandList">RecycleCreateCommandList</a> function.</p>
</dd>

### -field <b>pfnRecycleCreateDeferredContext</b>

<dd>
<p>A pointer to the <a href="display.RecycleCreateDeferredContext">RecycleCreateDeferredContext</a> function.</p>
</dd>

### -field <b>pfnDiscard</b>

<dd>
<p>A pointer to the <a href="display.Discard">Discard</a> function.</p>
</dd>

### -field <b>pfnAssignDebugBinary</b>

<dd>
<p>A pointer to the <a href="display.AssignDebugBinary">AssignDebugBinary</a> function.</p>
</dd>

### -field <b>pfnCheckDirectFlipSupport</b>

<dd>
<p>A pointer to the <a href="display.CheckDirectFlipSupport">CheckDirectFlipSupport</a> function.</p>
</dd>

### -field <b>pfnClearView</b>

<dd>
<p>A pointer to the <a href="display.ClearView">ClearView</a> function.</p>
</dd>

### -field <b>pfnUpdateTileMappings</b>

<dd>
<p>A pointer to the <a href="display.UpdateTileMappings">UpdateTileMappings</a> function.</p>
</dd>

### -field <b>pfnCopyTileMappings</b>

<dd>
<p>A pointer to the <a href="display.CopyTileMappings">CopyTileMappings</a> function.</p>
</dd>

### -field <b>pfnCopyTiles</b>

<dd>
<p>A pointer to the <a href="display.CopyTiles">CopyTiles</a> function.</p>
</dd>

### -field <b>pfnUpdateTiles</b>

<dd>
<p>A pointer to the <a href="display.UpdateTiles">UpdateTiles</a> function.</p>
</dd>

### -field <b>pfnTiledResourceBarrier</b>

<dd>
<p>A pointer to the <a href="display.TiledResourceBarrier">TiledResourceBarrier</a> function.</p>
</dd>

### -field <b>pfnGetMipPacking</b>

<dd>
<p>A pointer to the <a href="display.GetMipPacking">GetMipPacking</a> function.</p>
</dd>

### -field <b>pfnResizeTilePool</b>

<dd>
<p>A pointer to the <a href="display.ResizeTilePool">ResizeTilePool</a> function.</p>
</dd>

### -field <b>pfnSetMarker</b>

<dd>
<p>A pointer to the <a href="display.SetMarker">SetMarker</a> function.</p>
</dd>

### -field <b>pfnSetMarkerMode</b>

<dd>
<p>A pointer to the <a href="display.SetMarkerMode">SetMarkerMode</a> function.</p>
</dd>

### -field <b>pfnSetHardwareProtection</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/dn906369">SetHardwareProtection</a> function.</p>
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