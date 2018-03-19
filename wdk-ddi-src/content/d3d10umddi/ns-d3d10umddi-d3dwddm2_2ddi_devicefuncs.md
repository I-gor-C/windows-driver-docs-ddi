---
UID: NS:d3d10umddi.D3DWDDM2_2DDI_DEVICEFUNCS
title: D3DWDDM2_2DDI_DEVICEFUNCS
author: windows-driver-content
description: Specifies the callback functions that operate on a shader cache.
old-location: display\d3dwddm2_2ddi_devicefuncs.htm
old-project: display
ms.assetid: 4E082193-70BA-4F36-9001-2A12014F3AC3
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3DWDDM2_2DDI_DEVICEFUNCS, D3DWDDM2_2DDI_DEVICEFUNCS structure [Display Devices], d3d10umddi/D3DWDDM2_2DDI_DEVICEFUNCS, display.d3dwddm2_2ddi_devicefuncs
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
-	D3DWDDM2_2DDI_DEVICEFUNCS
product: Windows
targetos: Windows
req.typenames: D3DWDDM2_2DDI_DEVICEFUNCS
---

# D3DWDDM2_2DDI_DEVICEFUNCS structure
Specifies the callback functions that operate on a shader cache.

## Syntax
````
typedef struct D3DWDDM2_2DDI_DEVICEFUNCS {
  PFND3DWDDM2_2DDI_CALCPRIVATE_SHADERCACHE_SESSION_SIZE pfnCalcPrivateShaderCacheSessionSize;
  PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION           pfnCreateShaderCacheSession;
  PFND3DWDDM2_2DDI_DESTROY_SHADERCACHE_SESSION          pfnDestroyShaderCacheSession;
  PFND3DWDDM2_2DDI_SET_SHADERCACHE_SESSION              pfnSetShaderCacheSession;
} D3DWDDM2_2DDI_DEVICEFUNCS;
````

## Members


`pfnDefaultConstantBufferUpdateSubresourceUP`



`pfnVsSetConstantBuffers`



`pfnPsSetShaderResources`



`pfnPsSetShader`



`pfnPsSetSamplers`



`pfnVsSetShader`



`pfnDrawIndexed`



`pfnDraw`



`pfnDynamicIABufferMapNoOverwrite`



`pfnDynamicIABufferUnmap`



`pfnDynamicConstantBufferMapDiscard`



`pfnDynamicIABufferMapDiscard`



`pfnDynamicConstantBufferUnmap`



`pfnPsSetConstantBuffers`



`pfnIaSetInputLayout`



`pfnIaSetVertexBuffers`



`pfnIaSetIndexBuffer`



`pfnDrawIndexedInstanced`



`pfnDrawInstanced`



`pfnDynamicResourceMapDiscard`



`pfnDynamicResourceUnmap`



`pfnGsSetConstantBuffers`



`pfnGsSetShader`



`pfnIaSetTopology`



`pfnStagingResourceMap`



`pfnStagingResourceUnmap`



`pfnVsSetShaderResources`



`pfnVsSetSamplers`



`pfnGsSetShaderResources`



`pfnGsSetSamplers`



`pfnSetRenderTargets`



`pfnShaderResourceViewReadAfterWriteHazard`



`pfnResourceReadAfterWriteHazard`



`pfnSetBlendState`



`pfnSetDepthStencilState`



`pfnSetRasterizerState`



`pfnQueryEnd`



`pfnQueryBegin`



`pfnResourceCopyRegion`



`pfnResourceUpdateSubresourceUP`



`pfnSoSetTargets`



`pfnDrawAuto`



`pfnSetViewports`



`pfnSetScissorRects`



`pfnClearRenderTargetView`



`pfnClearDepthStencilView`



`pfnSetPredication`



`pfnQueryGetData`



`pfnFlush`



`pfnGenMips`



`pfnResourceCopy`



`pfnResourceResolveSubresource`



`pfnResourceMap`



`pfnResourceUnmap`



`pfnResourceIsStagingBusy`



`pfnRelocateDeviceFuncs`



`pfnCalcPrivateResourceSize`



`pfnCalcPrivateOpenedResourceSize`



`pfnCreateResource`



`pfnOpenResource`



`pfnDestroyResource`



`pfnCalcPrivateShaderResourceViewSize`



`pfnCreateShaderResourceView`



`pfnDestroyShaderResourceView`



`pfnCalcPrivateRenderTargetViewSize`



`pfnCreateRenderTargetView`



`pfnDestroyRenderTargetView`



`pfnCalcPrivateDepthStencilViewSize`



`pfnCreateDepthStencilView`



`pfnDestroyDepthStencilView`



`pfnCalcPrivateElementLayoutSize`



`pfnCreateElementLayout`



`pfnDestroyElementLayout`



`pfnCalcPrivateBlendStateSize`



`pfnCreateBlendState`



`pfnDestroyBlendState`



`pfnCalcPrivateDepthStencilStateSize`



`pfnCreateDepthStencilState`



`pfnDestroyDepthStencilState`



`pfnCalcPrivateRasterizerStateSize`



`pfnCreateRasterizerState`



`pfnDestroyRasterizerState`



`pfnCalcPrivateShaderSize`



`pfnCreateVertexShader`



`pfnCreateGeometryShader`



`pfnCreatePixelShader`



`pfnCalcPrivateGeometryShaderWithStreamOutput`



`pfnCreateGeometryShaderWithStreamOutput`



`pfnDestroyShader`



`pfnCalcPrivateSamplerSize`



`pfnCreateSampler`



`pfnDestroySampler`



`pfnCalcPrivateQuerySize`



`pfnCreateQuery`



`pfnDestroyQuery`



`pfnCheckFormatSupport`



`pfnCheckMultisampleQualityLevels`



`pfnCheckCounterInfo`



`pfnCheckCounter`



`pfnDestroyDevice`



`pfnSetTextFilterSize`



`pfnResourceConvert`



`pfnResourceConvertRegion`



`pfnResetPrimitiveID`



`pfnSetVertexPipelineOutput`



`pfnDrawIndexedInstancedIndirect`



`pfnDrawInstancedIndirect`



`pfnCommandListExecute`



`pfnHsSetShaderResources`



`pfnHsSetShader`



`pfnHsSetSamplers`



`pfnHsSetConstantBuffers`



`pfnDsSetShaderResources`



`pfnDsSetShader`



`pfnDsSetSamplers`



`pfnDsSetConstantBuffers`



`pfnCreateHullShader`



`pfnCreateDomainShader`



`pfnCheckDeferredContextHandleSizes`



`pfnCalcDeferredContextHandleSize`



`pfnCalcPrivateDeferredContextSize`



`pfnCreateDeferredContext`



`pfnAbandonCommandList`



`pfnCalcPrivateCommandListSize`



`pfnCreateCommandList`



`pfnDestroyCommandList`



`pfnCalcPrivateTessellationShaderSize`



`pfnPsSetShaderWithIfaces`



`pfnVsSetShaderWithIfaces`



`pfnGsSetShaderWithIfaces`



`pfnHsSetShaderWithIfaces`



`pfnDsSetShaderWithIfaces`



`pfnCsSetShaderWithIfaces`



`pfnCreateComputeShader`



`pfnCsSetShader`



`pfnCsSetShaderResources`



`pfnCsSetSamplers`



`pfnCsSetConstantBuffers`



`pfnCalcPrivateUnorderedAccessViewSize`



`pfnCreateUnorderedAccessView`



`pfnDestroyUnorderedAccessView`



`pfnClearUnorderedAccessViewUint`



`pfnClearUnorderedAccessViewFloat`



`pfnCsSetUnorderedAccessViews`



`pfnDispatch`



`pfnDispatchIndirect`



`pfnSetResourceMinLOD`



`pfnCopyStructureCount`



`pfnRecycleCommandList`



`pfnRecycleCreateCommandList`



`pfnRecycleCreateDeferredContext`



`pfnRecycleDestroyCommandList`



`pfnDiscard`



`pfnAssignDebugBinary`



`pfnDynamicConstantBufferMapNoOverwrite`



`pfnCheckDirectFlipSupport`



`pfnClearView`



`pfnUpdateTileMappings`



`pfnCopyTileMappings`



`pfnCopyTiles`



`pfnUpdateTiles`



`pfnTiledResourceBarrier`



`pfnGetMipPacking`



`pfnResizeTilePool`



`pfnSetMarker`



`pfnSetMarkerMode`



`pfnSetHardwareProtection`



`pfnGetResourceLayout`



`pfnRetrieveShaderComment`



`pfnSetHardwareProtectionState`



`pfnAcquireResource`



`pfnReleaseResource`



`pfnCalcPrivateShaderCacheSessionSize`

A callback function that returns the size of a private shader cache session.

`pfnCreateShaderCacheSession`

A callback function that creates a shader cache session.

`pfnDestroyShaderCacheSession`

A callback function that destroys a shader cache session.

`pfnSetShaderCacheSession`

A callback function that sets a shader cache session.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d10umddi.h |