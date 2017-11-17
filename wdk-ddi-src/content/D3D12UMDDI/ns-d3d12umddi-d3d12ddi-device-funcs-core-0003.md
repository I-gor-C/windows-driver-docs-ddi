---
UID: NS.d3d12umddi.D3D12DDI_DEVICE_FUNCS_CORE_0003
title: D3D12DDI_DEVICE_FUNCS_CORE_0003
author: windows-driver-content
description: 
ms.assetid: 0a725816-ac0b-4589-b9d4-8286e2090b36
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: D3D12DDI_DEVICE_FUNCS_CORE_0003, D3D12DDI_DEVICE_FUNCS_CORE_0003
req.header: d3d12umddi.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# D3D12DDI_DEVICE_FUNCS_CORE_0003 structure

## -description



## -struct-fields

### -field PFND3D12DDI_CHECKFORMATSUPPORT pfnCheckFormatSupport			
 	
### -field PFND3D12DDI_CHECKMULTISAMPLEQUALITYLEVELS pfnCheckMultisampleQualityLevels			
 	
### -field PFND3D12DDI_GETMIPPACKING pfnGetMipPacking			
 	
### -field PFND3D12DDI_CALCPRIVATEELEMENTLAYOUTSIZE pfnCalcPrivateElementLayoutSize			
 	
### -field PFND3D12DDI_CREATEELEMENTLAYOUT_0003 pfnCreateElementLayout			
 	
### -field PFND3D12DDI_DESTROYELEMENTLAYOUT pfnDestroyElementLayout			
 	
### -field PFND3D12DDI_CALCPRIVATEBLENDSTATESIZE pfnCalcPrivateBlendStateSize			
 	
### -field PFND3D12DDI_CREATEBLENDSTATE_0003 pfnCreateBlendState			
 	
### -field PFND3D12DDI_DESTROYBLENDSTATE pfnDestroyBlendState			
 	
### -field PFND3D12DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE pfnCalcPrivateDepthStencilStateSize			
 	
### -field PFND3D12DDI_CREATEDEPTHSTENCILSTATE_0003 pfnCreateDepthStencilState			
 	
### -field PFND3D12DDI_DESTROYDEPTHSTENCILSTATE pfnDestroyDepthStencilState			
 	
### -field PFND3D12DDI_CALCPRIVATERASTERIZERSTATESIZE pfnCalcPrivateRasterizerStateSize			
 	
### -field PFND3D12DDI_CREATERASTERIZERSTATE_0003 pfnCreateRasterizerState			
 	
### -field PFND3D12DDI_DESTROYRASTERIZERSTATE pfnDestroyRasterizerState			
 	
### -field PFND3D12DDI_CALC_PRIVATE_SHADER_SIZE pfnCalcPrivateShaderSize			
 	
### -field PFND3D12DDI_CREATE_SHADER_0003 pfnCreateVertexShader			
 	
### -field PFND3D12DDI_CREATE_SHADER_0003 pfnCreatePixelShader			
 	
### -field PFND3D12DDI_CREATE_SHADER_0003 pfnCreateGeometryShader			
 	
### -field PFND3D12DDI_CREATE_COMPUTE_SHADER_0003 pfnCreateComputeShader			
 	
### -field PFND3D12DDI_CALC_PRIVATE_GEOMETRY_SHADER_WITH_STREAM_OUTPUT pfnCalcPrivateGeometryShaderWithStreamOutput			
 	
### -field PFND3D12DDI_CREATE_GEOMETRY_SHADER_WITH_STREAM_OUTPUT_0003 pfnCreateGeometryShaderWithStreamOutput			
 	
### -field PFND3D12DDI_CALC_PRIVATE_TESSELLATION_SHADER_SIZE pfnCalcPrivateTessellationShaderSize			
 	
### -field PFND3D12DDI_CREATE_TESS_SHADER_0003 pfnCreateHullShader			
 	
### -field PFND3D12DDI_CREATE_TESS_SHADER_0003 pfnCreateDomainShader			
 	
### -field PFND3D12DDI_DESTROYSHADER pfnDestroyShader			
 	
### -field PFND3D12DDI_CALCPRIVATECOMMANDQUEUESIZE_0001 pfnCalcPrivateCommandQueueSize			
 	
### -field PFND3D12DDI_CREATECOMMANDQUEUE_0001 pfnCreateCommandQueue			
 	
### -field PFND3D12DDI_DESTROYCOMMANDQUEUE pfnDestroyCommandQueue			
 	
### -field PFND3D12DDI_CALCPRIVATECOMMANDALLOCATORSIZE pfnCalcPrivateCommandAllocatorSize			
 	
### -field PFND3D12DDI_CREATECOMMANDALLOCATOR pfnCreateCommandAllocator			
 	
### -field PFND3D12DDI_DESTROYCOMMANDALLOCATOR pfnDestroyCommandAllocator			
 	
### -field PFND3D12DDI_RESETCOMMANDALLOCATOR pfnResetCommandAllocator			
 	
### -field PFND3D12DDI_CALC_PRIVATE_PIPELINE_STATE_SIZE_0001 pfnCalcPrivatePipelineStateSize			
 	
### -field PFND3D12DDI_CREATE_PIPELINE_STATE_0001 pfnCreatePipelineState			
 	
### -field PFND3D12DDI_DESTROY_PIPELINE_STATE pfnDestroyPipelineState			
 	
### -field PFND3D12DDI_CALC_PRIVATE_COMMAND_LIST_SIZE_0001 pfnCalcPrivateCommandListSize			
 	
### -field PFND3D12DDI_CREATE_COMMAND_LIST_0001 pfnCreateCommandList			
 	
### -field PFND3D12DDI_DESTROYCOMMANDLIST pfnDestroyCommandList			
 	
### -field PFND3D12DDI_CALCPRIVATEFENCESIZE pfnCalcPrivateFenceSize			
 	
### -field PFND3D12DDI_CREATEFENCE pfnCreateFence			
 	
### -field PFND3D12DDI_DESTROYFENCE pfnDestroyFence			
 	
### -field PFND3D12DDI_CALC_PRIVATE_DESCRIPTOR_HEAP_SIZE_0001 pfnCalcPrivateDescriptorHeapSize			
 	
### -field PFND3D12DDI_CREATE_DESCRIPTOR_HEAP_0001 pfnCreateDescriptorHeap			
 	
### -field PFND3D12DDI_DESTROY_DESCRIPTOR_HEAP pfnDestroyDescriptorHeap			
 	
### -field PFND3D12DDI_GET_DESCRIPTOR_SIZE_IN_BYTES pfnGetDescriptorSizeInBytes			
 	
### -field PFND3D12DDI_GET_CPU_DESCRIPTOR_HANDLE_FOR_HEAP_START pfnGetCPUDescriptorHandleForHeapStart			
 	
### -field PFND3D12DDI_GET_GPU_DESCRIPTOR_HANDLE_FOR_HEAP_START pfnGetGPUDescriptorHandleForHeapStart			
 	
### -field PFND3D12DDI_CREATE_SHADER_RESOURCE_VIEW_0002 pfnCreateShaderResourceView			
 	
### -field PFND3D12DDI_CREATE_CONSTANT_BUFFER_VIEW pfnCreateConstantBufferView			
 	
### -field PFND3D12DDI_CREATE_SAMPLER pfnCreateSampler			
 	
### -field PFND3D12DDI_CREATE_UNORDERED_ACCESS_VIEW_0002 pfnCreateUnorderedAccessView			
 	
### -field PFND3D12DDI_CREATE_RENDER_TARGET_VIEW_0002 pfnCreateRenderTargetView			
 	
### -field PFND3D12DDI_CREATE_DEPTH_STENCIL_VIEW pfnCreateDepthStencilView			
 	
### -field PFND3D12DDI_CALC_PRIVATE_ROOT_SIGNATURE_SIZE_0001 pfnCalcPrivateRootSignatureSize			
 	
### -field PFND3D12DDI_CREATE_ROOT_SIGNATURE_0001 pfnCreateRootSignature			
 	
### -field PFND3D12DDI_DESTROY_ROOT_SIGNATURE pfnDestroyRootSignature			
 	
### -field PFND3D12DDI_SERIALIZEOBJECT pfnSerializeObject			
 	
### -field PFND3D12DDI_DESTROYOBJECTSERIALIZATION pfnDestroyObjectSerialization			
 	
### -field PFND3D12DDI_CALCPRIVATEDESERIALIZEDOBJECTSIZE pfnCalcPrivateDeserializedObjectSize			
 	
### -field PFND3D12DDI_CREATEDESERIALIZEDOBJECT pfnCreateDeserializedObject			
 	
### -field PFND3D12DDI_MAPHEAP pfnMapHeap			
 	
### -field PFND3D12DDI_UNMAPHEAP pfnUnmapHeap			
 	
### -field PFND3D12DDI_CALCPRIVATEHEAPANDRESOURCESIZES_0003 pfnCalcPrivateHeapAndResourceSizes			
 	
### -field PFND3D12DDI_CREATEHEAPANDRESOURCE_0003 pfnCreateHeapAndResource			
 	
### -field PFND3D12DDI_DESTROYHEAPANDRESOURCE pfnDestroyHeapAndResource			
 	
### -field PFND3D12DDI_MAKERESIDENT_0001 pfnMakeResident			
 	
### -field PFND3D12DDI_EVICT2 pfnEvict			
 	
### -field PFND3D12DDI_CALCPRIVATEOPENEDHEAPANDRESOURCESIZES_0003 pfnCalcPrivateOpenedHeapAndResourceSizes			
 	
### -field PFND3D12DDI_OPENHEAPANDRESOURCE_0003 pfnOpenHeapAndResource			
 	
### -field PFND3D12DDI_COPY_DESCRIPTORS_0003 pfnCopyDescriptors			
 	
### -field PFND3D12DDI_COPY_DESCRIPTORS_SIMPLE_0003 pfnCopyDescriptorsSimple			
 	
### -field PFND3D12DDI_CALC_PRIVATE_QUERY_HEAP_SIZE_0001 pfnCalcPrivateQueryHeapSize			
 	
### -field PFND3D12DDI_CREATE_QUERY_HEAP_0001 pfnCreateQueryHeap			
 	
### -field PFND3D12DDI_DESTROY_QUERY_HEAP pfnDestroyQueryHeap			
 	
### -field PFND3D12DDI_CALC_PRIVATE_COMMAND_SIGNATURE_SIZE_0001 pfnCalcPrivateCommandSignatureSize			
 	
### -field PFND3D12DDI_CREATE_COMMAND_SIGNATURE_0001 pfnCreateCommandSignature			
 	
### -field PFND3D12DDI_DESTROY_COMMAND_SIGNATURE pfnDestroyCommandSignature			
 	
### -field PFND3D12DDI_CHECKRESOURCEVIRTUALADDRESS pfnCheckResourceVirtualAddress			
 	
### -field PFND3D12DDI_CHECKRESOURCEALLOCATIONINFO_0003 pfnCheckResourceAllocationInfo			
 	
### -field PFND3D12DDI_CHECKSUBRESOURCEINFO pfnCheckSubresourceInfo			
 	
### -field PFND3D12DDI_CHECKEXISITINGRESOURCEALLOCATIONINFO pfnCheckExistingResourceAllocationInfo			
 	
### -field PFND3D12DDI_OFFERRESOURCES pfnOfferResources			
 	
### -field PFND3D12DDI_RECLAIMRESOURCES_0001 pfnReclaimResources			
 	
### -field PFND3D12DDI_GETIMPLICITPHYSICALADAPTERMASK pfnGetImplicitPhysicalAdapterMask			
 	
### -field PFND3D12DDI_GET_PRESENT_PRIVATE_DRIVER_DATA_SIZE pfnGetPresentPrivateDriverDataSize			
 	
### -field PFND3D12DDI_QUERY_NODE_MAP pfnQueryNodeMap			
 	
### -field PFND3D12DDI_RETRIEVE_SHADER_COMMENT_0003 pfnRetrieveShaderComment			
 	
### -field PFND3D12DDI_CHECKRESOURCEALLOCATIONHANDLE pfnCheckResourceAllocationHandle			
 	
## -remarks

## -see-also