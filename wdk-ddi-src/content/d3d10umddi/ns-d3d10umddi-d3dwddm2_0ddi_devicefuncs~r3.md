---
UID: NS.D3D10UMDDI.D3DWDDM2_0DDI_DEVICEFUNCS~R3
title: D3DWDDM2_0DDI_DEVICEFUNCS
author: windows-driver-content
description: This structure contains the user mode device function table for Windows Display Driver Model (WDDM) 2.0.
old-location: display\d3dwddm2_0ddi_devicefuncs.htm
old-project: display
ms.assetid: 9A41512A-91C4-4053-9C60-5B485E93D14B
ms.author: windowsdriverdev
ms.date: 12/15/2017
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
---

# D3DWDDM2_0DDI_DEVICEFUNCS structure



## -description
This structure contains the user mode device function table for Windows Display Driver Model (WDDM) 2.0.



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

### -field pfnDefaultConstantBufferUpdateSubresourceUP

A pointer to the <a href="display.DefaultConstantBufferUpdateSubresourceUP">DefaultConstantBufferUpdateSubresourceUP</a> function.


### -field pfnVsSetConstantBuffers

A pointer to the <a href="display.VsSetConstantBuffers">VsSetConstantBuffers</a> function.


### -field pfnPsSetShaderResources

A pointer to the <a href="display.PsSetShaderResources">PsSetShaderResources</a> function.


### -field pfnPsSetShader

A pointer to the <a href="display.PsSetShader">PsSetShader</a> function.


### -field pfnPsSetSamplers

A pointer to the <a href="display.PsSetSamplers">PsSetSamplers</a> function.


### -field pfnVsSetShader

A pointer to the <a href="display.VsSetShader">VsSetShader</a> function.


### -field pfnDrawIndexed

A pointer to the <a href="display.DrawIndexed">DrawIndexed</a> function.


### -field pfnDraw

A pointer to the <a href="display.Draw">Draw</a> function.


### -field pfnPsSetConstantBuffers

A pointer to the <a href="display.PsSetConstantBuffers">PsSetConstantBuffers</a> function.


### -field pfnIaSetInputLayout

A pointer to the <a href="display.IaSetInputLayout">IaSetInputLayout</a> function.


### -field pfnIaSetVertexBuffers

A pointer to the <a href="display.IaSetVertexBuffers">IaSetVertexBuffers</a> function.


### -field pfnIaSetIndexBuffer

A pointer to the <a href="display.IaSetIndexBuffer">IaSetIndexBuffer</a> function.


### -field pfnDrawIndexedInstanced

A pointer to the <a href="display.DrawIndexedInstanced">DrawIndexedInstanced</a> function.


### -field pfnDrawInstanced

A pointer to the <a href="display.DrawInstanced">DrawInstanced</a> function.


### -field pfnGsSetConstantBuffers

A pointer to the <a href="display.GsSetConstantBuffers">GsSetConstantBuffers</a> function.


### -field pfnGsSetShader

A pointer to the <a href="display.GsSetShader">GsSetShader</a> function.


### -field pfnIaSetTopology

A pointer to the <a href="display.IaSetTopology">IaSetTopology</a> function.


### -field pfnVsSetShaderResources

A pointer to the <a href="display.VsSetShaderResources">VsSetShaderResources</a> function.


### -field pfnVsSetSamplers

A pointer to the <a href="display.VsSetSamplers">VsSetSamplers</a> function.


### -field pfnGsSetShaderResources

A pointer to the <a href="display.GsSetShaderResources">GsSetShaderResources</a> function.


### -field pfnGsSetSamplers

A pointer to the <a href="display.GsSetSamplers">GsSetSamplers</a> function.


### -field pfnSetRenderTargets

A pointer to the <a href="display.SetRenderTargets">SetRenderTargets</a> function.


### -field pfnShaderResourceViewReadAfterWriteHazard

A pointer to the <a href="display.ShaderResourceViewReadAfterWriteHazard">ShaderResourceViewReadAfterWriteHazard</a> function.


### -field pfnResourceReadAfterWriteHazard

A pointer to the <a href="display.ResourceReadAfterWriteHazard">ResourceReadAfterWriteHazard</a> function.


### -field pfnSetBlendState

A pointer to the <a href="display.SetBlendState">SetBlendState</a> function.


### -field pfnSetDepthStencilState

A pointer to the <a href="display.SetDepthStencilState">SetDepthStencilState</a> function.


### -field pfnSetRasterizerState

A pointer to the <a href="display.SetRasterizerState">SetRasterizerState</a> function.


### -field pfnQueryEnd

A pointer to the <a href="display.QueryEnd">QueryEnd</a> function.


### -field pfnQueryBegin

A pointer to the <a href="display.QueryBegin">QueryBegin</a> function.


### -field pfnResourceCopyRegion

A pointer to the <a href="display.ResourceCopyRegion">ResourceCopyRegion</a> function.


### -field pfnResourceUpdateSubresourceUP

A pointer to the <a href="display.ResourceUpdateSubresourceUP">ResourceUpdateSubresourceUP</a> function.


### -field pfnSoSetTargets

A pointer to the <a href="display.SoSetTargets">SoSetTargets</a> function.


### -field pfnDrawAuto

A pointer to the <a href="display.DrawAuto">DrawAuto</a> function.


### -field pfnSetViewports

A pointer to the <a href="display.SetViewports">SetViewports</a> function.


### -field pfnSetScissorRects

A pointer to the <a href="display.SetScissorRects">SetScissorRects</a> function.


### -field pfnClearRenderTargetView

A pointer to the <a href="display.ClearRenderTargetView">ClearRenderTargetView</a> function.


### -field pfnClearDepthStencilView

A pointer to the <a href="display.ClearDepthStencilView">ClearDepthStencilView</a> function.


### -field pfnSetPredication

A pointer to the <a href="display.SetPredication">SetPredication</a> function.


### -field pfnQueryGetData

A pointer to the <a href="display.QueryGetData">QueryGetData</a> function.


### -field pfnFlush

A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh463886">Flush</a> function.


### -field pfnGenMips

A pointer to the <a href="display.GenMips">GenMips</a> function.


### -field pfnResourceCopy

A pointer to the <a href="display.ResourceCopy">ResourceCopy</a> function.


### -field pfnResourceResolveSubresource

A pointer to the <a href="display.ResourceResolveSubresource">ResourceResolveSubresource</a> function.


### -field pfnResourceMap

A pointer to the <a href="display.ResourceMap">ResourceMap</a> function.


### -field pfnResourceUnmap

A pointer to the <a href="display.ResourceUnmap">ResourceUnmap</a> function.


### -field pfnResourceIsStagingBusy

A pointer to the <a href="display.ResourceIsStagingBusy">ResourceIsStagingBusy</a> function.


### -field pfnRelocateDeviceFuncs

A pointer to the <a href="display.RelocateDeviceFuncs">RelocateDeviceFuncs</a> function.


### -field pfnCalcPrivateResourceSize

A pointer to the <a href="display.CalcPrivateResourceSize">CalcPrivateResourceSize</a> function.


### -field pfnCalcPrivateOpenedResourceSize

A pointer to the <a href="display.CalcPrivateOpenedResourceSize">CalcPrivateOpenedResourceSize</a> function.


### -field pfnCreateResource

A pointer to the <a href="display.CreateResource">CreateResource</a> function.


### -field pfnOpenResource

A pointer to the <a href="display.OpenResource">OpenResource</a> function.


### -field pfnDestroyResource

A pointer to the <a href="display.DestroyResource">DestroyResource</a> function.


### -field pfnCalcPrivateShaderResourceViewSize

A pointer to the <a href="display.CalcPrivateShaderResourceViewSize">CalcPrivateShaderResourceViewSize</a> function.


### -field pfnCreateShaderResourceView

A pointer to the <a href="display.CreateShaderResourceView">CreateShaderResourceView</a> function.


### -field pfnDestroyShaderResourceView

A pointer to the <a href="display.DestroyShaderResourceView">DestroyShaderResourceView</a> function.


### -field pfnCalcPrivateRenderTargetViewSize

A pointer to the <a href="display.CalcPrivateRenderTargetViewSize">CalcPrivateRenderTargetViewSize</a> function.


### -field pfnCreateRenderTargetView

A pointer to the <a href="display.CreateRenderTargetView">CreateRenderTargetView</a> function.


### -field pfnDestroyRenderTargetView

A pointer to the <a href="display.DestroyRenderTargetView">DestroyRenderTargetView</a> function.


### -field pfnCalcPrivateDepthStencilViewSize

A pointer to the <a href="display.CalcPrivateDepthStencilViewSize">CalcPrivateDepthStencilViewSize</a> function.


### -field pfnCreateDepthStencilView

A pointer to the <a href="display.CreateDepthStencilView">CreateDepthStencilView</a> function.


### -field pfnDestroyDepthStencilView

A pointer to the <a href="display.DestroyDepthStencilView">DestroyDepthStencilView</a> function.


### -field pfnCalcPrivateElementLayoutSize

A pointer to the <a href="display.CalcPrivateElementLayoutSize">CalcPrivateElementLayoutSize</a> function.


### -field pfnCreateElementLayout

A pointer to the <a href="display.CreateElementLayout">CreateElementLayout</a> function.


### -field pfnDestroyElementLayout

A pointer to the <a href="display.DestroyElementLayout">DestroyElementLayout</a> function.


### -field pfnCalcPrivateBlendStateSize

A pointer to the <a href="display.CalcPrivateBlendStateSize">CalcPrivateBlendStateSize</a> function.


### -field pfnCreateBlendState

A pointer to the <a href="display.CreateBlendState">CreateBlendState</a> function.


### -field pfnDestroyBlendState

A pointer to the <a href="display.DestroyBlendState">DestroyBlendState</a> function.


### -field pfnCalcPrivateDepthStencilStateSize

A pointer to the <a href="display.CalcPrivateDepthStencilStateSize">CalcPrivateDepthStencilStateSize</a> function.


### -field pfnCreateDepthStencilState

A pointer to the <a href="display.CreateDepthStencilState">CreateDepthStencilState</a> function.


### -field pfnDestroyDepthStencilState

A pointer to the <a href="display.DestroyDepthStencilState">DestroyDepthStencilState</a> function.


### -field pfnCalcPrivateRasterizerStateSize

A pointer to the <a href="display.CalcPrivateRasterizerStateSize">CalcPrivateRasterizerStateSize</a> function.


### -field pfnCreateRasterizerState

A pointer to the <a href="display.CreateRasterizerState">CreateRasterizerState</a> function.


### -field pfnDestroyRasterizerState

A pointer to the <a href="display.DestroyRasterizerState">DestroyRasterizerState</a> function.


### -field pfnCalcPrivateShaderSize

A pointer to the <a href="display.CalcPrivateShaderSize">CalcPrivateShaderSize</a> function.


### -field pfnCreateVertexShader

A pointer to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvertexshader.md">CreateVertexShader</a> function.


### -field pfnCreateGeometryShader

A pointer to the <a href="display.CreateGeometryShader">CreateGeometryShader</a> function.


### -field pfnCreatePixelShader

A pointer to the <a href="display.CreatePixelShader">CreatePixelShader</a> function.


### -field pfnCalcPrivateGeometryShaderWithStreamOutput

A pointer to the <a href="display.CalcPrivateGeometryShaderWithStreamOutput">CalcPrivateGeometryShaderWithStreamOutput</a> function.


### -field pfnCreateGeometryShaderWithStreamOutput

A pointer to the <a href="display.CreateGeometryShaderWithStreamOutput">CreateGeometryShaderWithStreamOutput</a> function.


### -field pfnDestroyShader

A pointer to the <a href="display.DestroyShader">DestroyShader</a> function.


### -field pfnCalcPrivateSamplerSize

A pointer to the <a href="display.CalcPrivateSamplerSize">CalcPrivateSamplerSize</a> function.


### -field pfnCreateSampler

A pointer to the <a href="display.CreateSampler">CreateSampler</a> function.


### -field pfnDestroySampler

A pointer to the <a href="display.DestroySampler">DestroySampler</a> function.


### -field pfnCalcPrivateQuerySize

A pointer to the <a href="display.CalcPrivateQuerySize">CalcPrivateQuerySize</a> function.


### -field pfnCreateQuery

A pointer to the <a href="display.CreateQuery">CreateQuery</a> function.


### -field pfnDestroyQuery

A pointer to the <a href="display.DestroyQuery">DestroyQuery</a> function.


### -field pfnCheckFormatSupport

A pointer to the <a href="display.CheckFormatSupport">CheckFormatSupport</a> function.


### -field pfnCheckMultisampleQualityLevels

A pointer to the <a href="display.CheckMultisampleQualityLevels">CheckMultisampleQualityLevels</a> function.


### -field pfnCheckCounterInfo

A pointer to the <a href="display.CheckCounterInfo">CheckCounterInfo</a> function.


### -field pfnCheckCounter

A pointer to the <a href="display.CheckCounter">CheckCounter</a> function.


### -field pfnDestroyDevice

A pointer to the <a href="display.DestroyDevice">DestroyDevice</a> function.


### -field pfnSetTextFilterSize

A pointer to the <a href="display.SetTextFilterSize">SetTextFilterSize</a> function.


### -field pfnDrawIndexedInstancedIndirect

A pointer to the <a href="display.DrawIndexedInstancedIndirect">DrawIndexedInstancedIndirect</a> function.


### -field pfnDrawInstancedIndirect

A pointer to the <a href="display.DrawInstancedIndirect">DrawInstancedIndirect</a> function.


### -field pfnCommandListExecute

A pointer to the <a href="display.CommandListExecute">CommandListExecute</a> function.


### -field pfnHsSetShaderResources

A pointer to the <a href="display.HsSetShaderResources">HsSetShaderResources</a> function.


### -field pfnHsSetShader

A pointer to the <a href="display.HsSetShader">HsSetShader</a> function.


### -field pfnHsSetSamplers

A pointer to the <a href="display.HsSetSamplers">HsSetSamplers</a> function.


### -field pfnHsSetConstantBuffers

A pointer to the <a href="display.HsSetConstantBuffers">HsSetConstantBuffers</a> function.


### -field pfnDsSetShaderResources

A pointer to the <a href="display.DsSetShaderResources">DsSetShaderResources</a> function.


### -field pfnDsSetShader

A pointer to the <a href="display.DsSetShader">DsSetShader</a> function.


### -field pfnDsSetSamplers

A pointer to the <a href="display.DsSetSamplers">DsSetSamplers</a> function.


### -field pfnDsSetConstantBuffers

A pointer to the <a href="display.DsSetConstantBuffers">DsSetConstantBuffers</a> function.


### -field pfnCreateHullShader

A pointer to the <a href="display.CreateHullShader">CreateHullShader</a> function.


### -field pfnCreateDomainShader

A pointer to the <a href="display.CreateDomainShader">CreateDomainShader</a> function.


### -field pfnCheckDeferredContextHandleSizes

A pointer to the <a href="display.CheckDeferredContextHandleSizes">CheckDeferredContextHandleSizes</a> function.


### -field pfnCalcDeferredContextHandleSize

A pointer to the <a href="display.CalcDeferredContextHandleSize">CalcDeferredContextHandleSize</a> function.


### -field pfnCalcPrivateDeferredContextSize

A pointer to the <a href="display.CalcPrivateDeferredContextSize">CalcPrivateDeferredContextSize</a> function.


### -field pfnCreateDeferredContext

A pointer to the <a href="display.CreateDeferredContext">CreateDeferredContext</a> function.


### -field pfnAbandonCommandList

A pointer to the <a href="display.AbandonCommandList">AbandonCommandList</a> function.


### -field pfnCalcPrivateCommandListSize

A pointer to the <a href="display.CalcPrivateCommandListSize">CalcPrivateCommandListSize</a> function.


### -field pfnCreateCommandList

A pointer to the <a href="display.CreateCommandList">CreateCommandList</a> function.


### -field pfnDestroyCommandList

A pointer to the <a href="display.DestroyCommandList">DestroyCommandList</a> function.


### -field pfnCalcPrivateTessellationShaderSize

A pointer to the <a href="display.CalcPrivateTessellationShaderSize">CalcPrivateTessellationShaderSize</a> function.


### -field pfnPsSetShaderWithIfaces

A pointer to the <a href="display.PsSetShaderWithIfaces">PsSetShaderWithIfaces</a> function.


### -field pfnVsSetShaderWithIfaces

A pointer to the <a href="display.VsSetShaderWithIfaces">VsSetShaderWithIfaces</a> function.


### -field pfnGsSetShaderWithIfaces

A pointer to the <a href="display.GsSetShaderWithIfaces">GsSetShaderWithIfaces</a> function.


### -field pfnHsSetShaderWithIfaces

A pointer to the <a href="display.HsSetShaderWithIfaces">HsSetShaderWithIfaces</a> function.


### -field pfnDsSetShaderWithIfaces

A pointer to the <a href="display.DsSetShaderWithIfaces">DsSetShaderWithIfaces</a> function.


### -field pfnCsSetShaderWithIfaces

A pointer to the <a href="display.CsSetShaderWithIfaces">CsSetShaderWithIfaces</a> function.


### -field pfnCreateComputeShader

A pointer to the <a href="display.CreateComputeShader">CreateComputeShader</a> function.


### -field pfnCsSetShader

A pointer to the <a href="display.CsSetShader">CsSetShader</a> function.


### -field pfnCsSetShaderResources

A pointer to the <a href="display.CsSetShaderResources">CsSetShaderResources</a> function.


### -field pfnCsSetSamplers

A pointer to the <a href="display.CsSetSamplers">CsSetSamplers</a> function.


### -field pfnCsSetConstantBuffers

A pointer to the <a href="display.CsSetConstantBuffers">CsSetConstantBuffers</a> function.


### -field pfnCalcPrivateUnorderedAccessViewSize

A pointer to the <a href="display.CalcPrivateUnorderedAccessViewSize">CalcPrivateUnorderedAccessViewSize</a> function.


### -field pfnCreateUnorderedAccessView

A pointer to the <a href="display.CreateUnorderedAccessView">CreateUnorderedAccessView</a> function.


### -field pfnDestroyUnorderedAccessView

A pointer to the <a href="display.DestroyUnorderedAccessView">DestroyUnorderedAccessView</a> function.


### -field pfnClearUnorderedAccessViewUint

A pointer to the <a href="display.ClearUnorderedAccessViewUint">ClearUnorderedAccessViewUint</a> function.


### -field pfnClearUnorderedAccessViewFloat

A pointer to the <a href="display.ClearUnorderedAccessViewFloat">ClearUnorderedAccessViewFloat</a> function.


### -field pfnCsSetUnorderedAccessViews

A pointer to the <a href="display.CsSetUnorderedAccessViews">CsSetUnorderedAccessViews</a> function.


### -field pfnDispatch

A pointer to the <a href="display.Dispatch">Dispatch</a> function.


### -field pfnDispatchIndirect

A pointer to the <a href="display.DispatchIndirect">DispatchIndirect</a> function.


### -field pfnSetResourceMinLOD

A pointer to the <a href="display.SetResourceMinLOD">SetResourceMinLOD</a> function.


### -field pfnCopyStructureCount

A pointer to the <a href="display.CopyStructureCount">CopyStructureCount</a> function.


### -field pfnRecycleCommandList

A pointer to the <a href="display.RecycleCommandList">RecycleCommandList</a> function.


### -field pfnRecycleCreateCommandList

A pointer to the <a href="display.RecycleCreateCommandList">RecycleCreateCommandList</a> function.


### -field pfnRecycleCreateDeferredContext

A pointer to the <a href="display.RecycleCreateDeferredContext">RecycleCreateDeferredContext</a> function.


### -field pfnDiscard

A pointer to the <a href="display.Discard">Discard</a> function.


### -field pfnAssignDebugBinary

A pointer to the <a href="display.AssignDebugBinary">AssignDebugBinary</a> function.


### -field pfnCheckDirectFlipSupport

A pointer to the <a href="display.CheckDirectFlipSupport">CheckDirectFlipSupport</a> function.


### -field pfnClearView

A pointer to the <a href="display.ClearView">ClearView</a> function.


### -field pfnUpdateTileMappings

A pointer to the <a href="display.UpdateTileMappings">UpdateTileMappings</a> function.


### -field pfnCopyTileMappings

A pointer to the <a href="display.CopyTileMappings">CopyTileMappings</a> function.


### -field pfnCopyTiles

A pointer to the <a href="display.CopyTiles">CopyTiles</a> function.


### -field pfnUpdateTiles

A pointer to the <a href="display.UpdateTiles">UpdateTiles</a> function.


### -field pfnTiledResourceBarrier

A pointer to the <a href="display.TiledResourceBarrier">TiledResourceBarrier</a> function.


### -field pfnGetMipPacking

A pointer to the <a href="display.GetMipPacking">GetMipPacking</a> function.


### -field pfnResizeTilePool

A pointer to the <a href="display.ResizeTilePool">ResizeTilePool</a> function.


### -field pfnSetMarker

A pointer to the <a href="display.SetMarker">SetMarker</a> function.


### -field pfnSetMarkerMode

A pointer to the <a href="display.SetMarkerMode">SetMarkerMode</a> function.


### -field pfnSetHardwareProtection

A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/dn906369">SetHardwareProtection</a> function.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>