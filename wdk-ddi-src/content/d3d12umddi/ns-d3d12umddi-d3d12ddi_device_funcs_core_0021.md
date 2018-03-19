---
UID: NS:d3d12umddi.D3D12DDI_DEVICE_FUNCS_CORE_0021
title: D3D12DDI_DEVICE_FUNCS_CORE_0021
author: windows-driver-content
description: Specifies core device functions.
old-location: display\d3d12ddi_device_funcs_core_0021.htm
old-project: display
ms.assetid: 4E4C3DB3-9C4C-4BBC-82C4-C5C41C0B818C
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3D12DDI_DEVICE_FUNCS_CORE_0021, D3D12DDI_DEVICE_FUNCS_CORE_0021 structure [Display Devices], d3d12umddi/D3D12DDI_DEVICE_FUNCS_CORE_0021, display.d3d12ddi_device_funcs_core_0021
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
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
-	D3d12umddi.h
api_name:
-	D3D12DDI_DEVICE_FUNCS_CORE_0021
product: Windows
targetos: Windows
req.typenames: D3D12DDI_DEVICE_FUNCS_CORE_0021
---

# D3D12DDI_DEVICE_FUNCS_CORE_0021 structure
Specifies core device functions.

## Syntax
````
typedef struct D3D12DDI_DEVICE_FUNCS_CORE_0021 {
  PFND3D12DDI_CALC_PRIVATE_PIPELINE_STATE_SIZE_0010 pfnCalcPrivatePipelineStateSize;
  PFND3D12DDI_CREATE_PIPELINE_STATE_0021            pfnCreatePipelineState;
  PFND3D12DDI_DESTROY_PIPELINE_STATE                pfnDestroyPipelineState;
} D3D12DDI_DEVICE_FUNCS_CORE_0021;
````

## Members


`pfnCheckFormatSupport`



`pfnCheckMultisampleQualityLevels`



`pfnGetMipPacking`



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



`pfnCreatePixelShader`



`pfnCreateGeometryShader`



`pfnCreateComputeShader`



`pfnCalcPrivateGeometryShaderWithStreamOutput`



`pfnCreateGeometryShaderWithStreamOutput`



`pfnCalcPrivateTessellationShaderSize`



`pfnCreateHullShader`



`pfnCreateDomainShader`



`pfnDestroyShader`



`pfnCalcPrivateCommandQueueSize`



`pfnCreateCommandQueue`



`pfnDestroyCommandQueue`



`pfnCalcPrivateCommandAllocatorSize`



`pfnCreateCommandAllocator`



`pfnDestroyCommandAllocator`



`pfnResetCommandAllocator`



`pfnCalcPrivatePipelineStateSize`

A callback function that calculates the size of a private pipeline state.

`pfnCreatePipelineState`

A callback function that creates a pipeline state.

`pfnDestroyPipelineState`

A callback function that destroys  a pipeline state.

`pfnCalcPrivateCommandListSize`



`pfnCreateCommandList`



`pfnDestroyCommandList`



`pfnCalcPrivateFenceSize`



`pfnCreateFence`



`pfnDestroyFence`



`pfnCalcPrivateDescriptorHeapSize`



`pfnCreateDescriptorHeap`



`pfnDestroyDescriptorHeap`



`pfnGetDescriptorSizeInBytes`



`pfnGetCPUDescriptorHandleForHeapStart`



`pfnGetGPUDescriptorHandleForHeapStart`



`pfnCreateShaderResourceView`



`pfnCreateConstantBufferView`



`pfnCreateSampler`



`pfnCreateUnorderedAccessView`



`pfnCreateRenderTargetView`



`pfnCreateDepthStencilView`



`pfnCalcPrivateRootSignatureSize`



`pfnCreateRootSignature`



`pfnDestroyRootSignature`



`pfnMapHeap`



`pfnUnmapHeap`



`pfnCalcPrivateHeapAndResourceSizes`



`pfnCreateHeapAndResource`



`pfnDestroyHeapAndResource`



`pfnMakeResident`



`pfnEvict`



`pfnCalcPrivateOpenedHeapAndResourceSizes`



`pfnOpenHeapAndResource`



`pfnCopyDescriptors`



`pfnCopyDescriptorsSimple`



`pfnCalcPrivateQueryHeapSize`



`pfnCreateQueryHeap`



`pfnDestroyQueryHeap`



`pfnCalcPrivateCommandSignatureSize`



`pfnCreateCommandSignature`



`pfnDestroyCommandSignature`



`pfnCheckResourceVirtualAddress`



`pfnCheckResourceAllocationInfo`



`pfnCheckSubresourceInfo`



`pfnCheckExistingResourceAllocationInfo`



`pfnOfferResources`



`pfnReclaimResources`



`pfnGetImplicitPhysicalAdapterMask`



`pfnGetPresentPrivateDriverDataSize`



`pfnQueryNodeMap`



`pfnRetrieveShaderComment`



`pfnCheckResourceAllocationHandle`



`pfnCalcPrivatePipelineLibrarySize`



`pfnCreatePipelineLibrary`



`pfnDestroyPipelineLibrary`



`pfnAddPipelineStateToLibrary`



`pfnCalcSerializedLibrarySize`



`pfnSerializeLibrary`



`pfnGetDebugAllocationInfo`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |