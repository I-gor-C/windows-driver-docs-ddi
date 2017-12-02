---
UID: NS.d3d10umddi.D3DWDDM2_0DDI_DEVICEFUNCS~r1
title: D3DWDDM2_0DDI_DEVICEFUNCS
author: windows-driver-content
description: This structure contains the user mode device function table for Windows Display Driver Model (WDDM) 2.0.
old-location: display\d3dwddm2_0ddi_devicefuncs.htm
old-project: display
ms.assetid: 9A41512A-91C4-4053-9C60-5B485E93D14B
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_0DDI_DEVICEFUNCS, D3DWDDM2_0DDI_DEVICEFUNCS
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

### -field pfnDefaultConstantBufferUpdateSubresourceUP

<dd>
<p>A pointer to the <a href="display.DefaultConstantBufferUpdateSubresourceUP">DefaultConstantBufferUpdateSubresourceUP</a> function.</p>
</dd>

### -field pfnVsSetConstantBuffers

<dd>
<p>A pointer to the <a href="display.VsSetConstantBuffers">VsSetConstantBuffers</a> function.</p>
</dd>

### -field pfnPsSetShaderResources

<dd>
<p>A pointer to the <a href="display.PsSetShaderResources">PsSetShaderResources</a> function.</p>
</dd>

### -field pfnPsSetShader

<dd>
<p>A pointer to the <a href="display.PsSetShader">PsSetShader</a> function.</p>
</dd>

### -field pfnPsSetSamplers

<dd>
<p>A pointer to the <a href="display.PsSetSamplers">PsSetSamplers</a> function.</p>
</dd>

### -field pfnVsSetShader

<dd>
<p>A pointer to the <a href="display.VsSetShader">VsSetShader</a> function.</p>
</dd>

### -field pfnDrawIndexed

<dd>
<p>A pointer to the <a href="display.DrawIndexed">DrawIndexed</a> function.</p>
</dd>

### -field pfnDraw

<dd>
<p>A pointer to the <a href="display.Draw">Draw</a> function.</p>
</dd>

### -field pfnPsSetConstantBuffers

<dd>
<p>A pointer to the <a href="display.PsSetConstantBuffers">PsSetConstantBuffers</a> function.</p>
</dd>

### -field pfnIaSetInputLayout

<dd>
<p>A pointer to the <a href="display.IaSetInputLayout">IaSetInputLayout</a> function.</p>
</dd>

### -field pfnIaSetVertexBuffers

<dd>
<p>A pointer to the <a href="display.IaSetVertexBuffers">IaSetVertexBuffers</a> function.</p>
</dd>

### -field pfnIaSetIndexBuffer

<dd>
<p>A pointer to the <a href="display.IaSetIndexBuffer">IaSetIndexBuffer</a> function.</p>
</dd>

### -field pfnDrawIndexedInstanced

<dd>
<p>A pointer to the <a href="display.DrawIndexedInstanced">DrawIndexedInstanced</a> function.</p>
</dd>

### -field pfnDrawInstanced

<dd>
<p>A pointer to the <a href="display.DrawInstanced">DrawInstanced</a> function.</p>
</dd>

### -field pfnGsSetConstantBuffers

<dd>
<p>A pointer to the <a href="display.GsSetConstantBuffers">GsSetConstantBuffers</a> function.</p>
</dd>

### -field pfnGsSetShader

<dd>
<p>A pointer to the <a href="display.GsSetShader">GsSetShader</a> function.</p>
</dd>

### -field pfnIaSetTopology

<dd>
<p>A pointer to the <a href="display.IaSetTopology">IaSetTopology</a> function.</p>
</dd>

### -field pfnVsSetShaderResources

<dd>
<p>A pointer to the <a href="display.VsSetShaderResources">VsSetShaderResources</a> function.</p>
</dd>

### -field pfnVsSetSamplers

<dd>
<p>A pointer to the <a href="display.VsSetSamplers">VsSetSamplers</a> function.</p>
</dd>

### -field pfnGsSetShaderResources

<dd>
<p>A pointer to the <a href="display.GsSetShaderResources">GsSetShaderResources</a> function.</p>
</dd>

### -field pfnGsSetSamplers

<dd>
<p>A pointer to the <a href="display.GsSetSamplers">GsSetSamplers</a> function.</p>
</dd>

### -field pfnSetRenderTargets

<dd>
<p>A pointer to the <a href="display.SetRenderTargets">SetRenderTargets</a> function.</p>
</dd>

### -field pfnShaderResourceViewReadAfterWriteHazard

<dd>
<p>A pointer to the <a href="display.ShaderResourceViewReadAfterWriteHazard">ShaderResourceViewReadAfterWriteHazard</a> function.</p>
</dd>

### -field pfnResourceReadAfterWriteHazard

<dd>
<p>A pointer to the <a href="display.ResourceReadAfterWriteHazard">ResourceReadAfterWriteHazard</a> function.</p>
</dd>

### -field pfnSetBlendState

<dd>
<p>A pointer to the <a href="display.SetBlendState">SetBlendState</a> function.</p>
</dd>

### -field pfnSetDepthStencilState

<dd>
<p>A pointer to the <a href="display.SetDepthStencilState">SetDepthStencilState</a> function.</p>
</dd>

### -field pfnSetRasterizerState

<dd>
<p>A pointer to the <a href="display.SetRasterizerState">SetRasterizerState</a> function.</p>
</dd>

### -field pfnQueryEnd

<dd>
<p>A pointer to the <a href="display.QueryEnd">QueryEnd</a> function.</p>
</dd>

### -field pfnQueryBegin

<dd>
<p>A pointer to the <a href="display.QueryBegin">QueryBegin</a> function.</p>
</dd>

### -field pfnResourceCopyRegion

<dd>
<p>A pointer to the <a href="display.ResourceCopyRegion">ResourceCopyRegion</a> function.</p>
</dd>

### -field pfnResourceUpdateSubresourceUP

<dd>
<p>A pointer to the <a href="display.ResourceUpdateSubresourceUP">ResourceUpdateSubresourceUP</a> function.</p>
</dd>

### -field pfnSoSetTargets

<dd>
<p>A pointer to the <a href="display.SoSetTargets">SoSetTargets</a> function.</p>
</dd>

### -field pfnDrawAuto

<dd>
<p>A pointer to the <a href="display.DrawAuto">DrawAuto</a> function.</p>
</dd>

### -field pfnSetViewports

<dd>
<p>A pointer to the <a href="display.SetViewports">SetViewports</a> function.</p>
</dd>

### -field pfnSetScissorRects

<dd>
<p>A pointer to the <a href="display.SetScissorRects">SetScissorRects</a> function.</p>
</dd>

### -field pfnClearRenderTargetView

<dd>
<p>A pointer to the <a href="display.ClearRenderTargetView">ClearRenderTargetView</a> function.</p>
</dd>

### -field pfnClearDepthStencilView

<dd>
<p>A pointer to the <a href="display.ClearDepthStencilView">ClearDepthStencilView</a> function.</p>
</dd>

### -field pfnSetPredication

<dd>
<p>A pointer to the <a href="display.SetPredication">SetPredication</a> function.</p>
</dd>

### -field pfnQueryGetData

<dd>
<p>A pointer to the <a href="display.QueryGetData">QueryGetData</a> function.</p>
</dd>

### -field pfnFlush

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh463886">Flush</a> function.</p>
</dd>

### -field pfnGenMips

<dd>
<p>A pointer to the <a href="display.GenMips">GenMips</a> function.</p>
</dd>

### -field pfnResourceCopy

<dd>
<p>A pointer to the <a href="display.ResourceCopy">ResourceCopy</a> function.</p>
</dd>

### -field pfnResourceResolveSubresource

<dd>
<p>A pointer to the <a href="display.ResourceResolveSubresource">ResourceResolveSubresource</a> function.</p>
</dd>

### -field pfnResourceMap

<dd>
<p>A pointer to the <a href="display.ResourceMap">ResourceMap</a> function.</p>
</dd>

### -field pfnResourceUnmap

<dd>
<p>A pointer to the <a href="display.ResourceUnmap">ResourceUnmap</a> function.</p>
</dd>

### -field pfnResourceIsStagingBusy

<dd>
<p>A pointer to the <a href="display.ResourceIsStagingBusy">ResourceIsStagingBusy</a> function.</p>
</dd>

### -field pfnRelocateDeviceFuncs

<dd>
<p>A pointer to the <a href="display.RelocateDeviceFuncs">RelocateDeviceFuncs</a> function.</p>
</dd>

### -field pfnCalcPrivateResourceSize

<dd>
<p>A pointer to the <a href="display.CalcPrivateResourceSize">CalcPrivateResourceSize</a> function.</p>
</dd>

### -field pfnCalcPrivateOpenedResourceSize

<dd>
<p>A pointer to the <a href="display.CalcPrivateOpenedResourceSize">CalcPrivateOpenedResourceSize</a> function.</p>
</dd>

### -field pfnCreateResource

<dd>
<p>A pointer to the <a href="display.CreateResource">CreateResource</a> function.</p>
</dd>

### -field pfnOpenResource

<dd>
<p>A pointer to the <a href="display.OpenResource">OpenResource</a> function.</p>
</dd>

### -field pfnDestroyResource

<dd>
<p>A pointer to the <a href="display.DestroyResource">DestroyResource</a> function.</p>
</dd>

### -field pfnCalcPrivateShaderResourceViewSize

<dd>
<p>A pointer to the <a href="display.CalcPrivateShaderResourceViewSize">CalcPrivateShaderResourceViewSize</a> function.</p>
</dd>

### -field pfnCreateShaderResourceView

<dd>
<p>A pointer to the <a href="display.CreateShaderResourceView">CreateShaderResourceView</a> function.</p>
</dd>

### -field pfnDestroyShaderResourceView

<dd>
<p>A pointer to the <a href="display.DestroyShaderResourceView">DestroyShaderResourceView</a> function.</p>
</dd>

### -field pfnCalcPrivateRenderTargetViewSize

<dd>
<p>A pointer to the <a href="display.CalcPrivateRenderTargetViewSize">CalcPrivateRenderTargetViewSize</a> function.</p>
</dd>

### -field pfnCreateRenderTargetView

<dd>
<p>A pointer to the <a href="display.CreateRenderTargetView">CreateRenderTargetView</a> function.</p>
</dd>

### -field pfnDestroyRenderTargetView

<dd>
<p>A pointer to the <a href="display.DestroyRenderTargetView">DestroyRenderTargetView</a> function.</p>
</dd>

### -field pfnCalcPrivateDepthStencilViewSize

<dd>
<p>A pointer to the <a href="display.CalcPrivateDepthStencilViewSize">CalcPrivateDepthStencilViewSize</a> function.</p>
</dd>

### -field pfnCreateDepthStencilView

<dd>
<p>A pointer to the <a href="display.CreateDepthStencilView">CreateDepthStencilView</a> function.</p>
</dd>

### -field pfnDestroyDepthStencilView

<dd>
<p>A pointer to the <a href="display.DestroyDepthStencilView">DestroyDepthStencilView</a> function.</p>
</dd>

### -field pfnCalcPrivateElementLayoutSize

<dd>
<p>A pointer to the <a href="display.CalcPrivateElementLayoutSize">CalcPrivateElementLayoutSize</a> function.</p>
</dd>

### -field pfnCreateElementLayout

<dd>
<p>A pointer to the <a href="display.CreateElementLayout">CreateElementLayout</a> function.</p>
</dd>

### -field pfnDestroyElementLayout

<dd>
<p>A pointer to the <a href="display.DestroyElementLayout">DestroyElementLayout</a> function.</p>
</dd>

### -field pfnCalcPrivateBlendStateSize

<dd>
<p>A pointer to the <a href="display.CalcPrivateBlendStateSize">CalcPrivateBlendStateSize</a> function.</p>
</dd>

### -field pfnCreateBlendState

<dd>
<p>A pointer to the <a href="display.CreateBlendState">CreateBlendState</a> function.</p>
</dd>

### -field pfnDestroyBlendState

<dd>
<p>A pointer to the <a href="display.DestroyBlendState">DestroyBlendState</a> function.</p>
</dd>

### -field pfnCalcPrivateDepthStencilStateSize

<dd>
<p>A pointer to the <a href="display.CalcPrivateDepthStencilStateSize">CalcPrivateDepthStencilStateSize</a> function.</p>
</dd>

### -field pfnCreateDepthStencilState

<dd>
<p>A pointer to the <a href="display.CreateDepthStencilState">CreateDepthStencilState</a> function.</p>
</dd>

### -field pfnDestroyDepthStencilState

<dd>
<p>A pointer to the <a href="display.DestroyDepthStencilState">DestroyDepthStencilState</a> function.</p>
</dd>

### -field pfnCalcPrivateRasterizerStateSize

<dd>
<p>A pointer to the <a href="display.CalcPrivateRasterizerStateSize">CalcPrivateRasterizerStateSize</a> function.</p>
</dd>

### -field pfnCreateRasterizerState

<dd>
<p>A pointer to the <a href="display.CreateRasterizerState">CreateRasterizerState</a> function.</p>
</dd>

### -field pfnDestroyRasterizerState

<dd>
<p>A pointer to the <a href="display.DestroyRasterizerState">DestroyRasterizerState</a> function.</p>
</dd>

### -field pfnCalcPrivateShaderSize

<dd>
<p>A pointer to the <a href="display.CalcPrivateShaderSize">CalcPrivateShaderSize</a> function.</p>
</dd>

### -field pfnCreateVertexShader

<dd>
<p>A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createvertexshader.md">CreateVertexShader</a> function.</p>
</dd>

### -field pfnCreateGeometryShader

<dd>
<p>A pointer to the <a href="display.CreateGeometryShader">CreateGeometryShader</a> function.</p>
</dd>

### -field pfnCreatePixelShader

<dd>
<p>A pointer to the <a href="display.CreatePixelShader">CreatePixelShader</a> function.</p>
</dd>

### -field pfnCalcPrivateGeometryShaderWithStreamOutput

<dd>
<p>A pointer to the <a href="display.CalcPrivateGeometryShaderWithStreamOutput">CalcPrivateGeometryShaderWithStreamOutput</a> function.</p>
</dd>

### -field pfnCreateGeometryShaderWithStreamOutput

<dd>
<p>A pointer to the <a href="display.CreateGeometryShaderWithStreamOutput">CreateGeometryShaderWithStreamOutput</a> function.</p>
</dd>

### -field pfnDestroyShader

<dd>
<p>A pointer to the <a href="display.DestroyShader">DestroyShader</a> function.</p>
</dd>

### -field pfnCalcPrivateSamplerSize

<dd>
<p>A pointer to the <a href="display.CalcPrivateSamplerSize">CalcPrivateSamplerSize</a> function.</p>
</dd>

### -field pfnCreateSampler

<dd>
<p>A pointer to the <a href="display.CreateSampler">CreateSampler</a> function.</p>
</dd>

### -field pfnDestroySampler

<dd>
<p>A pointer to the <a href="display.DestroySampler">DestroySampler</a> function.</p>
</dd>

### -field pfnCalcPrivateQuerySize

<dd>
<p>A pointer to the <a href="display.CalcPrivateQuerySize">CalcPrivateQuerySize</a> function.</p>
</dd>

### -field pfnCreateQuery

<dd>
<p>A pointer to the <a href="display.CreateQuery">CreateQuery</a> function.</p>
</dd>

### -field pfnDestroyQuery

<dd>
<p>A pointer to the <a href="display.DestroyQuery">DestroyQuery</a> function.</p>
</dd>

### -field pfnCheckFormatSupport

<dd>
<p>A pointer to the <a href="display.CheckFormatSupport">CheckFormatSupport</a> function.</p>
</dd>

### -field pfnCheckMultisampleQualityLevels

<dd>
<p>A pointer to the <a href="display.CheckMultisampleQualityLevels">CheckMultisampleQualityLevels</a> function.</p>
</dd>

### -field pfnCheckCounterInfo

<dd>
<p>A pointer to the <a href="display.CheckCounterInfo">CheckCounterInfo</a> function.</p>
</dd>

### -field pfnCheckCounter

<dd>
<p>A pointer to the <a href="display.CheckCounter">CheckCounter</a> function.</p>
</dd>

### -field pfnDestroyDevice

<dd>
<p>A pointer to the <a href="display.DestroyDevice">DestroyDevice</a> function.</p>
</dd>

### -field pfnSetTextFilterSize

<dd>
<p>A pointer to the <a href="display.SetTextFilterSize">SetTextFilterSize</a> function.</p>
</dd>

### -field pfnDrawIndexedInstancedIndirect

<dd>
<p>A pointer to the <a href="display.DrawIndexedInstancedIndirect">DrawIndexedInstancedIndirect</a> function.</p>
</dd>

### -field pfnDrawInstancedIndirect

<dd>
<p>A pointer to the <a href="display.DrawInstancedIndirect">DrawInstancedIndirect</a> function.</p>
</dd>

### -field pfnCommandListExecute

<dd>
<p>A pointer to the <a href="display.CommandListExecute">CommandListExecute</a> function.</p>
</dd>

### -field pfnHsSetShaderResources

<dd>
<p>A pointer to the <a href="display.HsSetShaderResources">HsSetShaderResources</a> function.</p>
</dd>

### -field pfnHsSetShader

<dd>
<p>A pointer to the <a href="display.HsSetShader">HsSetShader</a> function.</p>
</dd>

### -field pfnHsSetSamplers

<dd>
<p>A pointer to the <a href="display.HsSetSamplers">HsSetSamplers</a> function.</p>
</dd>

### -field pfnHsSetConstantBuffers

<dd>
<p>A pointer to the <a href="display.HsSetConstantBuffers">HsSetConstantBuffers</a> function.</p>
</dd>

### -field pfnDsSetShaderResources

<dd>
<p>A pointer to the <a href="display.DsSetShaderResources">DsSetShaderResources</a> function.</p>
</dd>

### -field pfnDsSetShader

<dd>
<p>A pointer to the <a href="display.DsSetShader">DsSetShader</a> function.</p>
</dd>

### -field pfnDsSetSamplers

<dd>
<p>A pointer to the <a href="display.DsSetSamplers">DsSetSamplers</a> function.</p>
</dd>

### -field pfnDsSetConstantBuffers

<dd>
<p>A pointer to the <a href="display.DsSetConstantBuffers">DsSetConstantBuffers</a> function.</p>
</dd>

### -field pfnCreateHullShader

<dd>
<p>A pointer to the <a href="display.CreateHullShader">CreateHullShader</a> function.</p>
</dd>

### -field pfnCreateDomainShader

<dd>
<p>A pointer to the <a href="display.CreateDomainShader">CreateDomainShader</a> function.</p>
</dd>

### -field pfnCheckDeferredContextHandleSizes

<dd>
<p>A pointer to the <a href="display.CheckDeferredContextHandleSizes">CheckDeferredContextHandleSizes</a> function.</p>
</dd>

### -field pfnCalcDeferredContextHandleSize

<dd>
<p>A pointer to the <a href="display.CalcDeferredContextHandleSize">CalcDeferredContextHandleSize</a> function.</p>
</dd>

### -field pfnCalcPrivateDeferredContextSize

<dd>
<p>A pointer to the <a href="display.CalcPrivateDeferredContextSize">CalcPrivateDeferredContextSize</a> function.</p>
</dd>

### -field pfnCreateDeferredContext

<dd>
<p>A pointer to the <a href="display.CreateDeferredContext">CreateDeferredContext</a> function.</p>
</dd>

### -field pfnAbandonCommandList

<dd>
<p>A pointer to the <a href="display.AbandonCommandList">AbandonCommandList</a> function.</p>
</dd>

### -field pfnCalcPrivateCommandListSize

<dd>
<p>A pointer to the <a href="display.CalcPrivateCommandListSize">CalcPrivateCommandListSize</a> function.</p>
</dd>

### -field pfnCreateCommandList

<dd>
<p>A pointer to the <a href="display.CreateCommandList">CreateCommandList</a> function.</p>
</dd>

### -field pfnDestroyCommandList

<dd>
<p>A pointer to the <a href="display.DestroyCommandList">DestroyCommandList</a> function.</p>
</dd>

### -field pfnCalcPrivateTessellationShaderSize

<dd>
<p>A pointer to the <a href="display.CalcPrivateTessellationShaderSize">CalcPrivateTessellationShaderSize</a> function.</p>
</dd>

### -field pfnPsSetShaderWithIfaces

<dd>
<p>A pointer to the <a href="display.PsSetShaderWithIfaces">PsSetShaderWithIfaces</a> function.</p>
</dd>

### -field pfnVsSetShaderWithIfaces

<dd>
<p>A pointer to the <a href="display.VsSetShaderWithIfaces">VsSetShaderWithIfaces</a> function.</p>
</dd>

### -field pfnGsSetShaderWithIfaces

<dd>
<p>A pointer to the <a href="display.GsSetShaderWithIfaces">GsSetShaderWithIfaces</a> function.</p>
</dd>

### -field pfnHsSetShaderWithIfaces

<dd>
<p>A pointer to the <a href="display.HsSetShaderWithIfaces">HsSetShaderWithIfaces</a> function.</p>
</dd>

### -field pfnDsSetShaderWithIfaces

<dd>
<p>A pointer to the <a href="display.DsSetShaderWithIfaces">DsSetShaderWithIfaces</a> function.</p>
</dd>

### -field pfnCsSetShaderWithIfaces

<dd>
<p>A pointer to the <a href="display.CsSetShaderWithIfaces">CsSetShaderWithIfaces</a> function.</p>
</dd>

### -field pfnCreateComputeShader

<dd>
<p>A pointer to the <a href="display.CreateComputeShader">CreateComputeShader</a> function.</p>
</dd>

### -field pfnCsSetShader

<dd>
<p>A pointer to the <a href="display.CsSetShader">CsSetShader</a> function.</p>
</dd>

### -field pfnCsSetShaderResources

<dd>
<p>A pointer to the <a href="display.CsSetShaderResources">CsSetShaderResources</a> function.</p>
</dd>

### -field pfnCsSetSamplers

<dd>
<p>A pointer to the <a href="display.CsSetSamplers">CsSetSamplers</a> function.</p>
</dd>

### -field pfnCsSetConstantBuffers

<dd>
<p>A pointer to the <a href="display.CsSetConstantBuffers">CsSetConstantBuffers</a> function.</p>
</dd>

### -field pfnCalcPrivateUnorderedAccessViewSize

<dd>
<p>A pointer to the <a href="display.CalcPrivateUnorderedAccessViewSize">CalcPrivateUnorderedAccessViewSize</a> function.</p>
</dd>

### -field pfnCreateUnorderedAccessView

<dd>
<p>A pointer to the <a href="display.CreateUnorderedAccessView">CreateUnorderedAccessView</a> function.</p>
</dd>

### -field pfnDestroyUnorderedAccessView

<dd>
<p>A pointer to the <a href="display.DestroyUnorderedAccessView">DestroyUnorderedAccessView</a> function.</p>
</dd>

### -field pfnClearUnorderedAccessViewUint

<dd>
<p>A pointer to the <a href="display.ClearUnorderedAccessViewUint">ClearUnorderedAccessViewUint</a> function.</p>
</dd>

### -field pfnClearUnorderedAccessViewFloat

<dd>
<p>A pointer to the <a href="display.ClearUnorderedAccessViewFloat">ClearUnorderedAccessViewFloat</a> function.</p>
</dd>

### -field pfnCsSetUnorderedAccessViews

<dd>
<p>A pointer to the <a href="display.CsSetUnorderedAccessViews">CsSetUnorderedAccessViews</a> function.</p>
</dd>

### -field pfnDispatch

<dd>
<p>A pointer to the <a href="display.Dispatch">Dispatch</a> function.</p>
</dd>

### -field pfnDispatchIndirect

<dd>
<p>A pointer to the <a href="display.DispatchIndirect">DispatchIndirect</a> function.</p>
</dd>

### -field pfnSetResourceMinLOD

<dd>
<p>A pointer to the <a href="display.SetResourceMinLOD">SetResourceMinLOD</a> function.</p>
</dd>

### -field pfnCopyStructureCount

<dd>
<p>A pointer to the <a href="display.CopyStructureCount">CopyStructureCount</a> function.</p>
</dd>

### -field pfnRecycleCommandList

<dd>
<p>A pointer to the <a href="display.RecycleCommandList">RecycleCommandList</a> function.</p>
</dd>

### -field pfnRecycleCreateCommandList

<dd>
<p>A pointer to the <a href="display.RecycleCreateCommandList">RecycleCreateCommandList</a> function.</p>
</dd>

### -field pfnRecycleCreateDeferredContext

<dd>
<p>A pointer to the <a href="display.RecycleCreateDeferredContext">RecycleCreateDeferredContext</a> function.</p>
</dd>

### -field pfnDiscard

<dd>
<p>A pointer to the <a href="display.Discard">Discard</a> function.</p>
</dd>

### -field pfnAssignDebugBinary

<dd>
<p>A pointer to the <a href="display.AssignDebugBinary">AssignDebugBinary</a> function.</p>
</dd>

### -field pfnCheckDirectFlipSupport

<dd>
<p>A pointer to the <a href="display.CheckDirectFlipSupport">CheckDirectFlipSupport</a> function.</p>
</dd>

### -field pfnClearView

<dd>
<p>A pointer to the <a href="display.ClearView">ClearView</a> function.</p>
</dd>

### -field pfnUpdateTileMappings

<dd>
<p>A pointer to the <a href="display.UpdateTileMappings">UpdateTileMappings</a> function.</p>
</dd>

### -field pfnCopyTileMappings

<dd>
<p>A pointer to the <a href="display.CopyTileMappings">CopyTileMappings</a> function.</p>
</dd>

### -field pfnCopyTiles

<dd>
<p>A pointer to the <a href="display.CopyTiles">CopyTiles</a> function.</p>
</dd>

### -field pfnUpdateTiles

<dd>
<p>A pointer to the <a href="display.UpdateTiles">UpdateTiles</a> function.</p>
</dd>

### -field pfnTiledResourceBarrier

<dd>
<p>A pointer to the <a href="display.TiledResourceBarrier">TiledResourceBarrier</a> function.</p>
</dd>

### -field pfnGetMipPacking

<dd>
<p>A pointer to the <a href="display.GetMipPacking">GetMipPacking</a> function.</p>
</dd>

### -field pfnResizeTilePool

<dd>
<p>A pointer to the <a href="display.ResizeTilePool">ResizeTilePool</a> function.</p>
</dd>

### -field pfnSetMarker

<dd>
<p>A pointer to the <a href="display.SetMarker">SetMarker</a> function.</p>
</dd>

### -field pfnSetMarkerMode

<dd>
<p>A pointer to the <a href="display.SetMarkerMode">SetMarkerMode</a> function.</p>
</dd>

### -field pfnSetHardwareProtection

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