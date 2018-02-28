---
UID: NS:d3d12umddi.D3D12DDI_DEVICE_FUNCS_CORE_0030
title: D3D12DDI_DEVICE_FUNCS_CORE_0030
author: windows-driver-content
description: Core device functions.
old-location: display\d3d12ddi-device-funcs-core-0030.htm
old-project: display
ms.assetid: 421e6b72-a771-4b18-9776-0b5e8e7a1e29
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: D3D12DDI_DEVICE_FUNCS_CORE_0030, D3D12DDI_DEVICE_FUNCS_CORE_0030 structure [Display Devices], d3d12umddi/D3D12DDI_DEVICE_FUNCS_CORE_0030, display.d3d12ddi-device-funcs-core-0030
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d12umddi.h
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
-	d3d12umddi.h
api_name:
-	D3D12DDI_DEVICE_FUNCS_CORE_0030
product: Windows
targetos: Windows
req.typenames: D3D12DDI_DEVICE_FUNCS_CORE_0030
---

# D3D12DDI_DEVICE_FUNCS_CORE_0030 structure
Core device functions.

## Syntax
````
typedef struct _D3D12DDI_DEVICE_FUNCS_CORE_0030 {
  PFND3D12DDI_CHECKFORMATSUPPORT                                    pfnCheckFormatSupport;
  PFND3D12DDI_CHECKMULTISAMPLEQUALITYLEVELS                         pfnCheckMultisampleQualityLevels;
  PFND3D12DDI_GETMIPPACKING                                         pfnGetMipPacking;
  PFND3D12DDI_CALCPRIVATEELEMENTLAYOUTSIZE_0010                     pfnCalcPrivateElementLayoutSize;
  PFND3D12DDI_CREATEELEMENTLAYOUT_0010                              pfnCreateElementLayout;
  PFND3D12DDI_DESTROYELEMENTLAYOUT                                  pfnDestroyElementLayout;
  PFND3D12DDI_CALCPRIVATEBLENDSTATESIZE_0010                        pfnCalcPrivateBlendStateSize;
  PFND3D12DDI_CREATEBLENDSTATE_0010                                 pfnCreateBlendState;
  PFND3D12DDI_DESTROYBLENDSTATE                                     pfnDestroyBlendState;
  PFND3D12DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE_0025                 pfnCalcPrivateDepthStencilStateSize;
  PFND3D12DDI_CREATEDEPTHSTENCILSTATE_0025                          pfnCreateDepthStencilState;
  PFND3D12DDI_DESTROYDEPTHSTENCILSTATE                              pfnDestroyDepthStencilState;
  PFND3D12DDI_CALCPRIVATERASTERIZERSTATESIZE_0010                   pfnCalcPrivateRasterizerStateSize;
  PFND3D12DDI_CREATERASTERIZERSTATE_0010                            pfnCreateRasterizerState;
  PFND3D12DDI_DESTROYRASTERIZERSTATE                                pfnDestroyRasterizerState;
  PFND3D12DDI_CALC_PRIVATE_SHADER_SIZE_0026                         pfnCalcPrivateShaderSize;
  PFND3D12DDI_CREATE_SHADER_0026                                    pfnCreateVertexShader;
  PFND3D12DDI_CREATE_SHADER_0026                                    pfnCreatePixelShader;
  PFND3D12DDI_CREATE_SHADER_0026                                    pfnCreateGeometryShader;
  PFND3D12DDI_CREATE_SHADER_0026                                    pfnCreateComputeShader;
  PFND3D12DDI_CALC_PRIVATE_GEOMETRY_SHADER_WITH_STREAM_OUTPUT_0026  pfnCalcPrivateGeometryShaderWithStreamOutput;
  PFND3D12DDI_CREATE_GEOMETRY_SHADER_WITH_STREAM_OUTPUT_0026        pfnCreateGeometryShaderWithStreamOutput;
  PFND3D12DDI_CALC_PRIVATE_SHADER_SIZE_0026                         pfnCalcPrivateTessellationShaderSize;
  PFND3D12DDI_CREATE_SHADER_0026                                    pfnCreateHullShader;
  PFND3D12DDI_CREATE_SHADER_0026                                    pfnCreateDomainShader;
  PFND3D12DDI_DESTROYSHADER                                         pfnDestroyShader;
  PFND3D12DDI_CALCPRIVATECOMMANDQUEUESIZE_0023                      pfnCalcPrivateCommandQueueSize;
  PFND3D12DDI_CREATECOMMANDQUEUE_0023                               pfnCreateCommandQueue;
  PFND3D12DDI_DESTROYCOMMANDQUEUE                                   pfnDestroyCommandQueue;
  PFND3D12DDI_CALCPRIVATECOMMANDALLOCATORSIZE                       pfnCalcPrivateCommandAllocatorSize;
  PFND3D12DDI_CREATECOMMANDALLOCATOR                                pfnCreateCommandAllocator;
  PFND3D12DDI_DESTROYCOMMANDALLOCATOR                               pfnDestroyCommandAllocator;
  PFND3D12DDI_RESETCOMMANDALLOCATOR                                 pfnResetCommandAllocator;
  PFND3D12DDI_CALC_PRIVATE_PIPELINE_STATE_SIZE_0010                 pfnCalcPrivatePipelineStateSize;
  PFND3D12DDI_CREATE_PIPELINE_STATE_0021                            pfnCreatePipelineState;
  PFND3D12DDI_DESTROY_PIPELINE_STATE                                pfnDestroyPipelineState;
  PFND3D12DDI_CALC_PRIVATE_COMMAND_LIST_SIZE_0001                   pfnCalcPrivateCommandListSize;
  PFND3D12DDI_CREATE_COMMAND_LIST_0001                              pfnCreateCommandList;
  PFND3D12DDI_DESTROYCOMMANDLIST                                    pfnDestroyCommandList;
  PFND3D12DDI_CALCPRIVATEFENCESIZE                                  pfnCalcPrivateFenceSize;
  PFND3D12DDI_CREATEFENCE                                           pfnCreateFence;
  PFND3D12DDI_DESTROYFENCE                                          pfnDestroyFence;
  PFND3D12DDI_CALC_PRIVATE_DESCRIPTOR_HEAP_SIZE_0001                pfnCalcPrivateDescriptorHeapSize;
  PFND3D12DDI_CREATE_DESCRIPTOR_HEAP_0001                           pfnCreateDescriptorHeap;
  PFND3D12DDI_DESTROY_DESCRIPTOR_HEAP                               pfnDestroyDescriptorHeap;
  PFND3D12DDI_GET_DESCRIPTOR_SIZE_IN_BYTES                          pfnGetDescriptorSizeInBytes;
  PFND3D12DDI_GET_CPU_DESCRIPTOR_HANDLE_FOR_HEAP_START              pfnGetCPUDescriptorHandleForHeapStart;
  PFND3D12DDI_GET_GPU_DESCRIPTOR_HANDLE_FOR_HEAP_START              pfnGetGPUDescriptorHandleForHeapStart;
  PFND3D12DDI_CREATE_SHADER_RESOURCE_VIEW_0002                      pfnCreateShaderResourceView;
  PFND3D12DDI_CREATE_CONSTANT_BUFFER_VIEW                           pfnCreateConstantBufferView;
  PFND3D12DDI_CREATE_SAMPLER                                        pfnCreateSampler;
  PFND3D12DDI_CREATE_UNORDERED_ACCESS_VIEW_0002                     pfnCreateUnorderedAccessView;
  PFND3D12DDI_CREATE_RENDER_TARGET_VIEW_0002                        pfnCreateRenderTargetView;
  PFND3D12DDI_CREATE_DEPTH_STENCIL_VIEW                             pfnCreateDepthStencilView;
  PFND3D12DDI_CALC_PRIVATE_ROOT_SIGNATURE_SIZE_0013                 pfnCalcPrivateRootSignatureSize;
  PFND3D12DDI_CREATE_ROOT_SIGNATURE_0013                            pfnCreateRootSignature;
  PFND3D12DDI_DESTROY_ROOT_SIGNATURE                                pfnDestroyRootSignature;
  PFND3D12DDI_MAPHEAP                                               pfnMapHeap;
  PFND3D12DDI_UNMAPHEAP                                             pfnUnmapHeap;
  PFND3D12DDI_CALCPRIVATEHEAPANDRESOURCESIZES_0030                  pfnCalcPrivateHeapAndResourceSizes;
  PFND3D12DDI_CREATEHEAPANDRESOURCE_0030                            pfnCreateHeapAndResource;
  PFND3D12DDI_DESTROYHEAPANDRESOURCE                                pfnDestroyHeapAndResource;
  PFND3D12DDI_MAKERESIDENT_0001                                     pfnMakeResident;
  PFND3D12DDI_EVICT2                                                pfnEvict;
  PFND3D12DDI_CALCPRIVATEOPENEDHEAPANDRESOURCESIZES_0003            pfnCalcPrivateOpenedHeapAndResourceSizes;
  PFND3D12DDI_OPENHEAPANDRESOURCE_0003                              pfnOpenHeapAndResource;
  PFND3D12DDI_COPY_DESCRIPTORS_0003                                 pfnCopyDescriptors;
  PFND3D12DDI_COPY_DESCRIPTORS_SIMPLE_0003                          pfnCopyDescriptorsSimple;
  PFND3D12DDI_CALC_PRIVATE_QUERY_HEAP_SIZE_0001                     pfnCalcPrivateQueryHeapSize;
  PFND3D12DDI_CREATE_QUERY_HEAP_0001                                pfnCreateQueryHeap;
  PFND3D12DDI_DESTROY_QUERY_HEAP                                    pfnDestroyQueryHeap;
  PFND3D12DDI_CALC_PRIVATE_COMMAND_SIGNATURE_SIZE_0001              pfnCalcPrivateCommandSignatureSize;
  PFND3D12DDI_CREATE_COMMAND_SIGNATURE_0001                         pfnCreateCommandSignature;
  PFND3D12DDI_DESTROY_COMMAND_SIGNATURE                             pfnDestroyCommandSignature;
  PFND3D12DDI_CHECKRESOURCEVIRTUALADDRESS                           pfnCheckResourceVirtualAddress;
  PFND3D12DDI_CHECKRESOURCEALLOCATIONINFO_0022                      pfnCheckResourceAllocationInfo;
  PFND3D12DDI_CHECKSUBRESOURCEINFO                                  pfnCheckSubresourceInfo;
  PFND3D12DDI_CHECKEXISITINGRESOURCEALLOCATIONINFO_0022             pfnCheckExistingResourceAllocationInfo;
  PFND3D12DDI_OFFERRESOURCES                                        pfnOfferResources;
  PFND3D12DDI_RECLAIMRESOURCES_0001                                 pfnReclaimResources;
  PFND3D12DDI_GETIMPLICITPHYSICALADAPTERMASK                        pfnGetImplicitPhysicalAdapterMask;
  PFND3D12DDI_GET_PRESENT_PRIVATE_DRIVER_DATA_SIZE                  pfnGetPresentPrivateDriverDataSize;
  PFND3D12DDI_QUERY_NODE_MAP                                        pfnQueryNodeMap;
  PFND3D12DDI_RETRIEVE_SHADER_COMMENT_0003                          pfnRetrieveShaderComment;
  PFND3D12DDI_CHECKRESOURCEALLOCATIONHANDLE                         pfnCheckResourceAllocationHandle;
  PFND3D12DDI_CALC_PRIVATE_PIPELINE_LIBRARY_SIZE_0010               pfnCalcPrivatePipelineLibrarySize;
  PFND3D12DDI_CREATE_PIPELINE_LIBRARY_0010                          pfnCreatePipelineLibrary;
  PFND3D12DDI_DESTROY_PIPELINE_LIBRARY_0010                         pfnDestroyPipelineLibrary;
  PFND3D12DDI_ADD_PIPELINE_STATE_TO_LIBRARY_0010                    pfnAddPipelineStateToLibrary;
  PFND3D12DDI_CALC_SERIALIZED_LIBRARY_SIZE_0010                     pfnCalcSerializedLibrarySize;
  PFND3D12DDI_SERIALIZE_LIBRARY_0010                                pfnSerializeLibrary;
  PFND3D12DDI_GET_DEBUG_ALLOCATION_INFO_0014                        pfnGetDebugAllocationInfo;
} D3D12DDI_DEVICE_FUNCS_CORE_0030, D3D12DDI_DEVICE_FUNCS_CORE_0030;
````

## Members


`pfnAddPipelineStateToLibrary`

Add pipeline state to library.

`pfnCalcPrivateBlendStateSize`

Calculate private blend state size.

`pfnCalcPrivateCommandAllocatorSize`

Calculate private command allocator size.

`pfnCalcPrivateCommandListSize`

Calculate private command list size.

`pfnCalcPrivateCommandQueueSize`

Calculate private command queue size.

`pfnCalcPrivateCommandSignatureSize`

Calculate private command signature size.

`pfnCalcPrivateDepthStencilStateSize`

Calculate private depth stencil state size.

`pfnCalcPrivateDescriptorHeapSize`

Calculate private descriptor heap size.

`pfnCalcPrivateElementLayoutSize`

Calculate private element layout size.

`pfnCalcPrivateFenceSize`

Calculate private fence size.

`pfnCalcPrivateGeometryShaderWithStreamOutput`

Calculate private geometry shader with stream output.

`pfnCalcPrivateHeapAndResourceSizes`

Calculate private heap and resource sizes.

`pfnCalcPrivateOpenedHeapAndResourceSizes`

Calculate private opened heap and resource sizes.

`pfnCalcPrivatePipelineLibrarySize`

Calculate private pipeline library size.

`pfnCalcPrivatePipelineStateSize`

Calculate private pipeline state size.

`pfnCalcPrivateQueryHeapSize`

Calculate private query heap size.

`pfnCalcPrivateRasterizerStateSize`

Calculate private rasterizer state size.

`pfnCalcPrivateRootSignatureSize`

Calculate private root signature size.

`pfnCalcPrivateShaderSize`

Calculate private shader size.

`pfnCalcPrivateTessellationShaderSize`

Calculate private tessellation shader size.

`pfnCalcSerializedLibrarySize`

Calculate serialized library size.

`pfnCheckExistingResourceAllocationInfo`

Check existing resource allocation info.

`pfnCheckFormatSupport`

Check format support.

`pfnCheckMultisampleQualityLevels`

Check multi-sample quality levels.

`pfnCheckResourceAllocationHandle`

Check resource allocation handle.

`pfnCheckResourceAllocationInfo`

Check resource allocation info.

`pfnCheckResourceVirtualAddress`

Check resource virtual address.

`pfnCheckSubresourceInfo`

Check sub resource info.

`pfnCopyDescriptors`

Copy descriptors.

`pfnCopyDescriptorsSimple`

Copy descriptor sample.

`pfnCreateBlendState`

Create blend state.

`pfnCreateCommandAllocator`

Create command allocator.

`pfnCreateCommandList`

Create command list.

`pfnCreateCommandQueue`

Create command queue.

`pfnCreateCommandSignature`

Create command signature.

`pfnCreateComputeShader`

Create compute shader.

`pfnCreateConstantBufferView`

Create constant buffer view.

`pfnCreateDepthStencilState`

Create depth stencil state.

`pfnCreateDepthStencilView`

Create depth stencil view.

`pfnCreateDescriptorHeap`

Create descriptor heap.

`pfnCreateDomainShader`

Create domain shader.

`pfnCreateElementLayout`



`pfnCreateFence`

Create fence.

`pfnCreateGeometryShader`

Create geometry shader.

`pfnCreateGeometryShaderWithStreamOutput`

Create geometry shader with stream output.

`pfnCreateHeapAndResource`

Create heap and resource.

`pfnCreateHullShader`

Create hull shader.

`pfnCreatePipelineLibrary`

Create pipeline library.

`pfnCreatePipelineState`

Create pipeline state.

`pfnCreatePixelShader`

Create pixel shader.

`pfnCreateQueryHeap`

Create query heap.

`pfnCreateRasterizerState`

Create rasterizer state.

`pfnCreateRenderTargetView`

Create render target view.

`pfnCreateRootSignature`

Create root signature.

`pfnCreateSampler`

Create sampler.

`pfnCreateShaderResourceView`

Create shader resource view.

`pfnCreateUnorderedAccessView`

Create unordered access view.

`pfnCreateVertexShader`

Create vertex shader.

`pfnDestroyBlendState`

Destroy blend state.

`pfnDestroyCommandAllocator`

Destroy command allocator.

`pfnDestroyCommandList`

Destroy command list.

`pfnDestroyCommandQueue`

Destroy command queue.

`pfnDestroyCommandSignature`

Destroy command signature.

`pfnDestroyDepthStencilState`

Destroy depth stencil state.

`pfnDestroyDescriptorHeap`

Destroy descriptor heap.

`pfnDestroyElementLayout`

Destroy element layout.

`pfnDestroyFence`

Destroy fence.

`pfnDestroyHeapAndResource`

Destroy heap and resource.

`pfnDestroyPipelineLibrary`

Destroy pipeline library.

`pfnDestroyPipelineState`



`pfnDestroyQueryHeap`

Destroy query heap.

`pfnDestroyRasterizerState`

Destory rasterizer state.

`pfnDestroyRootSignature`

Destroy root signature.

`pfnDestroyShader`

Destroy shader.

`pfnEvict`

Evict.

`pfnGetCPUDescriptorHandleForHeapStart`

Get CPU descriptor handle for heap start.

`pfnGetDebugAllocationInfo`

Get debug allocation info.

`pfnGetDescriptorSizeInBytes`

Get descriptor size in bytes.

`pfnGetGPUDescriptorHandleForHeapStart`

Get GPU descriptor handle for heap start.

`pfnGetImplicitPhysicalAdapterMask`

Get implicit physical adapter mask.

`pfnGetMipPacking`

Get MIP packing.

`pfnGetPresentPrivateDriverDataSize`

Get present private driver data size.

`pfnMakeResident`

Make resident.

`pfnMapHeap`

Map heap.

`pfnOfferResources`

Offer resources.

`pfnOpenHeapAndResource`

Open heap and resource.

`pfnQueryNodeMap`

Query node map.

`pfnReclaimResources`

Reclaim resources.

`pfnResetCommandAllocator`

Reset command allocator.

`pfnRetrieveShaderComment`

Retrieve shader comment.

`pfnSerializeLibrary`

Serialized libary.

`pfnUnmapHeap`

Unmap heap.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d12umddi.h |