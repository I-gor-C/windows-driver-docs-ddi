---
UID: NS.d3d12umddi.D3D12DDI_DEVICE_FUNCS_CORE_0033
title: D3D12DDI_DEVICE_FUNCS_CORE_0033
author: windows-driver-content
description: Core device functions.
old-location: display\d3d12ddi-device-funcs-core-0033.htm
old-project: display
ms.assetid: c771f360-3641-4e3e-9536-86b31af97932
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_DEVICE_FUNCS_CORE_0033, D3D12DDI_DEVICE_FUNCS_CORE_0033
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
req.alt-api: D3D12DDI_DEVICE_FUNCS_CORE_0033
req.alt-loc: d3d12umddi.h
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

# D3D12DDI_DEVICE_FUNCS_CORE_0033 structure



## -description
<p>Core device functions.</p>


## -syntax

````
typedef struct _D3D12DDI_DEVICE_FUNCS_CORE_0033 {
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
  PFND3D12DDI_CALC_PRIVATE_PIPELINE_STATE_SIZE_0033                 pfnCalcPrivatePipelineStateSize;
  PFND3D12DDI_CREATE_PIPELINE_STATE_0033                            pfnCreatePipelineState;
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
} D3D12DDI_DEVICE_FUNCS_CORE_0033, D3D12DDI_DEVICE_FUNCS_CORE_0033;
````


## -struct-fields
<dl>

### -field pfnCheckFormatSupport

<dd>
<p>Check format support.</p>
</dd>

### -field pfnCheckMultisampleQualityLevels

<dd>
<p>Check multi sample quality levels.</p>
</dd>

### -field pfnGetMipPacking

<dd>
<p>Get MIP packing.</p>
</dd>

### -field pfnCalcPrivateElementLayoutSize

<dd>
<p>Calculate private element layout size.</p>
</dd>

### -field pfnCreateElementLayout

<dd>
<p>Create element layout.</p>
</dd>

### -field pfnDestroyElementLayout

<dd>
<p>Destroy element layout.</p>
</dd>

### -field pfnCalcPrivateBlendStateSize

<dd>
<p>Calculate private blend state size.</p>
</dd>

### -field pfnCreateBlendState

<dd>
<p>Create blend state.</p>
</dd>

### -field pfnDestroyBlendState

<dd>
<p>Destroy blend state.</p>
</dd>

### -field pfnCalcPrivateDepthStencilStateSize

<dd>
<p>Calculate private depth stencil state size.</p>
</dd>

### -field pfnCreateDepthStencilState

<dd>
<p>Create depth stencil state.</p>
</dd>

### -field pfnDestroyDepthStencilState

<dd>
<p>Destroy depth stencil state.</p>
</dd>

### -field pfnCalcPrivateRasterizerStateSize

<dd>
<p>Calculate private rasterizer state size.</p>
</dd>

### -field pfnCreateRasterizerState

<dd>
<p>Create rasterizer state.</p>
</dd>

### -field pfnDestroyRasterizerState

<dd>
<p>Destroy rasterizer state.</p>
</dd>

### -field pfnCalcPrivateShaderSize

<dd>
<p>Calculate private shader size.</p>
</dd>

### -field pfnCreateVertexShader

<dd>
<p>Create vertex shader.</p>
</dd>

### -field pfnCreatePixelShader

<dd>
<p>Create pixel shader.</p>
</dd>

### -field pfnCreateGeometryShader

<dd>
<p>Create geometry shader.</p>
</dd>

### -field pfnCreateComputeShader

<dd>
<p>Create compute shader.</p>
</dd>

### -field pfnCalcPrivateGeometryShaderWithStreamOutput

<dd>
<p>Calculate private geometry shader with stream output.</p>
</dd>

### -field pfnCreateGeometryShaderWithStreamOutput

<dd>
<p>Create geometry shader with stream output.</p>
</dd>

### -field pfnCalcPrivateTessellationShaderSize

<dd>
<p>Calculate private tessellation shader size.</p>
</dd>

### -field pfnCreateHullShader

<dd>
<p>Create hull shader.</p>
</dd>

### -field pfnCreateDomainShader

<dd>
<p>Create domain shader.</p>
</dd>

### -field pfnDestroyShader

<dd>
<p>Destroy shader.</p>
</dd>

### -field pfnCalcPrivateCommandQueueSize

<dd>
<p>Calculate private command queue size.</p>
</dd>

### -field pfnCreateCommandQueue

<dd>
<p>Create command queue.</p>
</dd>

### -field pfnDestroyCommandQueue

<dd>
<p>Destroy command queue.</p>
</dd>

### -field pfnCalcPrivateCommandAllocatorSize

<dd>
<p>Calculate private command allocator size.</p>
</dd>

### -field pfnCreateCommandAllocator

<dd>
<p>Create command allocator.</p>
</dd>

### -field pfnDestroyCommandAllocator

<dd>
<p>Destroy command allocator.</p>
</dd>

### -field pfnResetCommandAllocator

<dd>
<p>Reset command allocator.</p>
</dd>

### -field pfnCalcPrivatePipelineStateSize

<dd>
<p>Calculate private pipeline state size.</p>
</dd>

### -field pfnCreatePipelineState

<dd>
<p>Create pipeline state.</p>
</dd>

### -field pfnDestroyPipelineState

<dd>
<p>Destroy pipeline state.</p>
</dd>

### -field pfnCalcPrivateCommandListSize

<dd>
<p>Calculate private command list size.</p>
</dd>

### -field pfnCreateCommandList

<dd>
<p>Create command list.</p>
</dd>

### -field pfnDestroyCommandList

<dd>
<p>Destroy command list.</p>
</dd>

### -field pfnCalcPrivateFenceSize

<dd>
<p>Calculate private fence size.</p>
</dd>

### -field pfnCreateFence

<dd>
<p>Create fence.</p>
</dd>

### -field pfnDestroyFence

<dd>
<p>Destroy fence.</p>
</dd>

### -field pfnCalcPrivateDescriptorHeapSize

<dd>
<p>Calculate private descriptor heap size.</p>
</dd>

### -field pfnCreateDescriptorHeap

<dd>
<p>Create descriptor heap.</p>
</dd>

### -field pfnDestroyDescriptorHeap

<dd>
<p>Destroy descriptor heap.</p>
</dd>

### -field pfnGetDescriptorSizeInBytes

<dd>
<p>Get descriptor size in bytes.</p>
</dd>

### -field pfnGetCPUDescriptorHandleForHeapStart

<dd>
<p>Get CPU descriptor handle for heap start.</p>
</dd>

### -field pfnGetGPUDescriptorHandleForHeapStart

<dd>
<p>Get GPU descriptor handle for heap start.</p>
</dd>

### -field pfnCreateShaderResourceView

<dd>
<p>Create shader resource view.</p>
</dd>

### -field pfnCreateConstantBufferView

<dd>
<p>Create constant buffer view.</p>
</dd>

### -field pfnCreateSampler

<dd>
<p>Create sampler.</p>
</dd>

### -field pfnCreateUnorderedAccessView

<dd>
<p>Create unordered access view.</p>
</dd>

### -field pfnCreateRenderTargetView

<dd>
<p>Create render target view.</p>
</dd>

### -field pfnCreateDepthStencilView

<dd>
<p>Create depth stencil view.</p>
</dd>

### -field pfnCalcPrivateRootSignatureSize

<dd>
<p>Calculate private root signature size.</p>
</dd>

### -field pfnCreateRootSignature

<dd>
<p>Create root signature.</p>
</dd>

### -field pfnDestroyRootSignature

<dd>
<p>Destroy root signature.</p>
</dd>

### -field pfnMapHeap

<dd>
<p>Map heap.</p>
</dd>

### -field pfnUnmapHeap

<dd>
<p>Unmap heap.</p>
</dd>

### -field pfnCalcPrivateHeapAndResourceSizes

<dd>
<p>Calculate private heap and resource sizes.</p>
</dd>

### -field pfnCreateHeapAndResource

<dd>
<p>Create heap and resource.</p>
</dd>

### -field pfnDestroyHeapAndResource

<dd>
<p>Destroy heap and resource.</p>
</dd>

### -field pfnMakeResident

<dd>
<p>Make resident.</p>
</dd>

### -field pfnEvict

<dd>
<p>Evict.</p>
</dd>

### -field pfnCalcPrivateOpenedHeapAndResourceSizes

<dd>
<p>Calculate private opened heap and resource sizes.</p>
</dd>

### -field pfnOpenHeapAndResource

<dd>
<p>Open heap and resource.</p>
</dd>

### -field pfnCopyDescriptors

<dd>
<p>Copy descriptors.</p>
</dd>

### -field pfnCopyDescriptorsSimple

<dd>
<p>Copy descriptors sample.</p>
</dd>

### -field pfnCalcPrivateQueryHeapSize

<dd>
<p>Calculate private query heap size.</p>
</dd>

### -field pfnCreateQueryHeap

<dd>
<p>Create query heap.</p>
</dd>

### -field pfnDestroyQueryHeap

<dd>
<p>Destroy query heap.</p>
</dd>

### -field pfnCalcPrivateCommandSignatureSize

<dd>
<p>Calculate private command signature size.</p>
</dd>

### -field pfnCreateCommandSignature

<dd>
<p>Create command signature.</p>
</dd>

### -field pfnDestroyCommandSignature

<dd>
<p>Destroy command signature.</p>
</dd>

### -field pfnCheckResourceVirtualAddress

<dd>
<p>Check resource virtual address.</p>
</dd>

### -field pfnCheckResourceAllocationInfo

<dd>
<p>Check resource allocation info.</p>
</dd>

### -field pfnCheckSubresourceInfo

<dd>
<p>check subresource info.</p>
</dd>

### -field pfnCheckExistingResourceAllocationInfo

<dd>
<p>Check existing resource allocation info.</p>
</dd>

### -field pfnOfferResources

<dd>
<p>Offer resources.</p>
</dd>

### -field pfnReclaimResources

<dd>
<p>Reclaim resources.</p>
</dd>

### -field pfnGetImplicitPhysicalAdapterMask

<dd>
<p>Get implicit physical adapter mask.</p>
</dd>

### -field pfnGetPresentPrivateDriverDataSize

<dd>
<p>Get present private driver data size.</p>
</dd>

### -field pfnQueryNodeMap

<dd>
<p>Query node map.</p>
</dd>

### -field pfnRetrieveShaderComment

<dd>
<p>Retrieve shader comment.</p>
</dd>

### -field pfnCheckResourceAllocationHandle

<dd>
<p>Check resource allocation handle.</p>
</dd>

### -field pfnCalcPrivatePipelineLibrarySize

<dd>
<p>Calculate private pipeline library size.</p>
</dd>

### -field pfnCreatePipelineLibrary

<dd>
<p>Create pipeline library.</p>
</dd>

### -field pfnDestroyPipelineLibrary

<dd>
<p>Destroy pipeline library.</p>
</dd>

### -field pfnAddPipelineStateToLibrary

<dd>
<p>Add pipeline state to library.</p>
</dd>

### -field pfnCalcSerializedLibrarySize

<dd>
<p>Calculate serialized library size.</p>
</dd>

### -field pfnSerializeLibrary

<dd>
<p>Serialize library.</p>
</dd>

### -field pfnGetDebugAllocationInfo

<dd>
<p>Get debug allocation info.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>