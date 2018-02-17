---
UID: NS:d3d10umddi.D3DWDDM2_2DDI_DEVICEFUNCS
title: D3DWDDM2_2DDI_DEVICEFUNCS
author: windows-driver-content
description: Specifies the callback functions that operate on a shader cache.
old-location: display\d3dwddm2_2ddi_devicefuncs.htm
old-project: display
ms.assetid: 4E082193-70BA-4F36-9001-2A12014F3AC3
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: d3d10umddi/D3DWDDM2_2DDI_DEVICEFUNCS, D3DWDDM2_2DDI_DEVICEFUNCS, D3DWDDM2_2DDI_DEVICEFUNCS structure [Display Devices], display.d3dwddm2_2ddi_devicefuncs
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3d10umddi.h
apiname:
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


`pfnAbandonCommandList`



`pfnAcquireResource`



`pfnAssignDebugBinary`



`pfnCalcDeferredContextHandleSize`



`pfnCalcPrivateBlendStateSize`



`pfnCalcPrivateCommandListSize`



`pfnCalcPrivateDeferredContextSize`



`pfnCalcPrivateDepthStencilStateSize`



`pfnCalcPrivateDepthStencilViewSize`



`pfnCalcPrivateElementLayoutSize`



`pfnCalcPrivateGeometryShaderWithStreamOutput`



`pfnCalcPrivateOpenedResourceSize`



`pfnCalcPrivateQuerySize`



`pfnCalcPrivateRasterizerStateSize`



`pfnCalcPrivateRenderTargetViewSize`



`pfnCalcPrivateResourceSize`



`pfnCalcPrivateSamplerSize`



`pfnCalcPrivateShaderCacheSessionSize`

A callback function that returns the size of a private shader cache session.

`pfnCalcPrivateShaderResourceViewSize`



`pfnCalcPrivateShaderSize`



`pfnCalcPrivateTessellationShaderSize`



`pfnCalcPrivateUnorderedAccessViewSize`



`pfnCheckCounter`



`pfnCheckCounterInfo`



`pfnCheckDeferredContextHandleSizes`



`pfnCheckDirectFlipSupport`



`pfnCheckFormatSupport`



`pfnCheckMultisampleQualityLevels`



`pfnClearDepthStencilView`



`pfnClearRenderTargetView`



`pfnClearUnorderedAccessViewFloat`



`pfnClearUnorderedAccessViewUint`



`pfnClearView`



`pfnCommandListExecute`



`pfnCopyStructureCount`



`pfnCopyTileMappings`



`pfnCopyTiles`



`pfnCreateBlendState`



`pfnCreateCommandList`



`pfnCreateComputeShader`



`pfnCreateDeferredContext`



`pfnCreateDepthStencilState`



`pfnCreateDepthStencilView`



`pfnCreateDomainShader`



`pfnCreateElementLayout`



`pfnCreateGeometryShader`



`pfnCreateGeometryShaderWithStreamOutput`



`pfnCreateHullShader`



`pfnCreatePixelShader`



`pfnCreateQuery`



`pfnCreateRasterizerState`



`pfnCreateRenderTargetView`



`pfnCreateResource`



`pfnCreateSampler`



`pfnCreateShaderCacheSession`

A callback function that creates a shader cache session.

`pfnCreateShaderResourceView`



`pfnCreateUnorderedAccessView`



`pfnCreateVertexShader`



`pfnCsSetConstantBuffers`



`pfnCsSetSamplers`



`pfnCsSetShader`



`pfnCsSetShaderResources`



`pfnCsSetShaderWithIfaces`



`pfnCsSetUnorderedAccessViews`



`pfnDefaultConstantBufferUpdateSubresourceUP`



`pfnDestroyBlendState`



`pfnDestroyCommandList`



`pfnDestroyDepthStencilState`



`pfnDestroyDepthStencilView`



`pfnDestroyDevice`



`pfnDestroyElementLayout`



`pfnDestroyQuery`



`pfnDestroyRasterizerState`



`pfnDestroyRenderTargetView`



`pfnDestroyResource`



`pfnDestroySampler`



`pfnDestroyShader`



`pfnDestroyShaderCacheSession`

A callback function that destroys a shader cache session.

`pfnDestroyShaderResourceView`



`pfnDestroyUnorderedAccessView`



`pfnDiscard`



`pfnDispatch`



`pfnDispatchIndirect`



`pfnDraw`



`pfnDrawAuto`



`pfnDrawIndexed`



`pfnDrawIndexedInstanced`



`pfnDrawIndexedInstancedIndirect`



`pfnDrawInstanced`



`pfnDrawInstancedIndirect`



`pfnDsSetConstantBuffers`



`pfnDsSetSamplers`



`pfnDsSetShader`



`pfnDsSetShaderResources`



`pfnDsSetShaderWithIfaces`



`pfnDynamicConstantBufferMapDiscard`



`pfnDynamicConstantBufferMapNoOverwrite`



`pfnDynamicConstantBufferUnmap`



`pfnDynamicIABufferMapDiscard`



`pfnDynamicIABufferMapNoOverwrite`



`pfnDynamicIABufferUnmap`



`pfnDynamicResourceMapDiscard`



`pfnDynamicResourceUnmap`



`pfnFlush`



`pfnGenMips`



`pfnGetMipPacking`



`pfnGetResourceLayout`



`pfnGsSetConstantBuffers`



`pfnGsSetSamplers`



`pfnGsSetShader`



`pfnGsSetShaderResources`



`pfnGsSetShaderWithIfaces`



`pfnHsSetConstantBuffers`



`pfnHsSetSamplers`



`pfnHsSetShader`



`pfnHsSetShaderResources`



`pfnHsSetShaderWithIfaces`



`pfnIaSetIndexBuffer`



`pfnIaSetInputLayout`



`pfnIaSetTopology`



`pfnIaSetVertexBuffers`



`pfnOpenResource`



`pfnPsSetConstantBuffers`



`pfnPsSetSamplers`



`pfnPsSetShader`



`pfnPsSetShaderResources`



`pfnPsSetShaderWithIfaces`



`pfnQueryBegin`



`pfnQueryEnd`



`pfnQueryGetData`



`pfnRecycleCommandList`



`pfnRecycleCreateCommandList`



`pfnRecycleCreateDeferredContext`



`pfnRecycleDestroyCommandList`



`pfnReleaseResource`



`pfnRelocateDeviceFuncs`



`pfnResetPrimitiveID`



`pfnResizeTilePool`



`pfnResourceConvert`



`pfnResourceConvertRegion`



`pfnResourceCopy`



`pfnResourceCopyRegion`



`pfnResourceIsStagingBusy`



`pfnResourceMap`



`pfnResourceReadAfterWriteHazard`



`pfnResourceResolveSubresource`



`pfnResourceUnmap`



`pfnResourceUpdateSubresourceUP`



`pfnRetrieveShaderComment`



`pfnSetBlendState`



`pfnSetDepthStencilState`



`pfnSetHardwareProtection`



`pfnSetHardwareProtectionState`



`pfnSetMarker`



`pfnSetMarkerMode`



`pfnSetPredication`



`pfnSetRasterizerState`



`pfnSetRenderTargets`



`pfnSetResourceMinLOD`



`pfnSetScissorRects`



`pfnSetShaderCacheSession`

A callback function that sets a shader cache session.

`pfnSetTextFilterSize`



`pfnSetVertexPipelineOutput`



`pfnSetViewports`



`pfnShaderResourceViewReadAfterWriteHazard`



`pfnSoSetTargets`



`pfnStagingResourceMap`



`pfnStagingResourceUnmap`



`pfnTiledResourceBarrier`



`pfnUpdateTileMappings`



`pfnUpdateTiles`



`pfnVsSetConstantBuffers`



`pfnVsSetSamplers`



`pfnVsSetShader`



`pfnVsSetShaderResources`



`pfnVsSetShaderWithIfaces`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d10umddi.h |