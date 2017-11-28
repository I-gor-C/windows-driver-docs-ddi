---
UID: NS.d3d12umddi.D3D12DDI_DEVICE_FUNCS_CORE_0030
title: D3D12DDI_DEVICE_FUNCS_CORE_0030
author: windows-driver-content
description: Core device functions.
old-location: display\d3d12ddi-device-funcs-core-0030.htm
old-project: display
ms.assetid: 421e6b72-a771-4b18-9776-0b5e8e7a1e29
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_DEVICE_FUNCS_CORE_0030, D3D12DDI_DEVICE_FUNCS_CORE_0030
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
req.alt-api: D3D12DDI_DEVICE_FUNCS_CORE_0030
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

# D3D12DDI_DEVICE_FUNCS_CORE_0030 structure



## -description
<p>Core device functions.</p>


## -syntax

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


## -struct-fields
<dl>

### -field <b>pfnCheckFormatSupport</b>

<dd>
<p>Check format support.</p>
</dd>

### -field <b>pfnCheckMultisampleQualityLevels</b>

<dd>
<p>Check multi-sample quality levels.</p>
</dd>

### -field <b>pfnGetMipPacking</b>

<dd>
<p>Get MIP packing.</p>
</dd>

### -field <b>pfnCalcPrivateElementLayoutSize</b>

<dd>
<p>Calculate private element layout size.</p>
</dd>

### -field <b>pfnCreateElementLayout</b>

<dd></dd>

### -field <b>pfnDestroyElementLayout</b>

<dd>
<p>Destroy element layout.</p>
</dd>

### -field <b>pfnCalcPrivateBlendStateSize</b>

<dd>
<p>Calculate private blend state size.</p>
</dd>

### -field <b>pfnCreateBlendState</b>

<dd>
<p>Create blend state.</p>
</dd>

### -field <b>pfnDestroyBlendState</b>

<dd>
<p>Destroy blend state.</p>
</dd>

### -field <b>pfnCalcPrivateDepthStencilStateSize</b>

<dd>
<p>Calculate private depth stencil state size.</p>
</dd>

### -field <b>pfnCreateDepthStencilState</b>

<dd>
<p>Create depth stencil state.</p>
</dd>

### -field <b>pfnDestroyDepthStencilState</b>

<dd>
<p>Destroy depth stencil state.</p>
</dd>

### -field <b>pfnCalcPrivateRasterizerStateSize</b>

<dd>
<p>Calculate private rasterizer state size.</p>
</dd>

### -field <b>pfnCreateRasterizerState</b>

<dd>
<p>Create rasterizer state.</p>
</dd>

### -field <b>pfnDestroyRasterizerState</b>

<dd>
<p>Destory rasterizer state.</p>
</dd>

### -field <b>pfnCalcPrivateShaderSize</b>

<dd>
<p>Calculate private shader size.</p>
</dd>

### -field <b>pfnCreateVertexShader</b>

<dd>
<p>Create vertex shader.</p>
</dd>

### -field <b>pfnCreatePixelShader</b>

<dd>
<p>Create pixel shader.</p>
</dd>

### -field <b>pfnCreateGeometryShader</b>

<dd>
<p>Create geometry shader.</p>
</dd>

### -field <b>pfnCreateComputeShader</b>

<dd>
<p>Create compute shader.</p>
</dd>

### -field <b>pfnCalcPrivateGeometryShaderWithStreamOutput</b>

<dd>
<p>Calculate private geometry shader with stream output.</p>
</dd>

### -field <b>pfnCreateGeometryShaderWithStreamOutput</b>

<dd>
<p>Create geometry shader with stream output.</p>
</dd>

### -field <b>pfnCalcPrivateTessellationShaderSize</b>

<dd>
<p>Calculate private tessellation shader size.</p>
</dd>

### -field <b>pfnCreateHullShader</b>

<dd>
<p>Create hull shader.</p>
</dd>

### -field <b>pfnCreateDomainShader</b>

<dd>
<p>Create domain shader.</p>
</dd>

### -field <b>pfnDestroyShader</b>

<dd>
<p>Destroy shader.</p>
</dd>

### -field <b>pfnCalcPrivateCommandQueueSize</b>

<dd>
<p>Calculate private command queue size.</p>
</dd>

### -field <b>pfnCreateCommandQueue</b>

<dd>
<p>Create command queue.</p>
</dd>

### -field <b>pfnDestroyCommandQueue</b>

<dd>
<p>Destroy command queue.</p>
</dd>

### -field <b>pfnCalcPrivateCommandAllocatorSize</b>

<dd>
<p>Calculate private command allocator size.</p>
</dd>

### -field <b>pfnCreateCommandAllocator</b>

<dd>
<p>Create command allocator.</p>
</dd>

### -field <b>pfnDestroyCommandAllocator</b>

<dd>
<p>Destroy command allocator.</p>
</dd>

### -field <b>pfnResetCommandAllocator</b>

<dd>
<p>Reset command allocator.</p>
</dd>

### -field <b>pfnCalcPrivatePipelineStateSize</b>

<dd>
<p>Calculate private pipeline state size.</p>
</dd>

### -field <b>pfnCreatePipelineState</b>

<dd>
<p>Create pipeline state.</p>
</dd>

### -field <b>pfnDestroyPipelineState</b>

<dd></dd>

### -field <b>pfnCalcPrivateCommandListSize</b>

<dd>
<p>Calculate private command list size.</p>
</dd>

### -field <b>pfnCreateCommandList</b>

<dd>
<p>Create command list.</p>
</dd>

### -field <b>pfnDestroyCommandList</b>

<dd>
<p>Destroy command list.</p>
</dd>

### -field <b>pfnCalcPrivateFenceSize</b>

<dd>
<p>Calculate private fence size.</p>
</dd>

### -field <b>pfnCreateFence</b>

<dd>
<p>Create fence.</p>
</dd>

### -field <b>pfnDestroyFence</b>

<dd>
<p>Destroy fence.</p>
</dd>

### -field <b>pfnCalcPrivateDescriptorHeapSize</b>

<dd>
<p>Calculate private descriptor heap size.</p>
</dd>

### -field <b>pfnCreateDescriptorHeap</b>

<dd>
<p>Create descriptor heap.</p>
</dd>

### -field <b>pfnDestroyDescriptorHeap</b>

<dd>
<p>Destroy descriptor heap.</p>
</dd>

### -field <b>pfnGetDescriptorSizeInBytes</b>

<dd>
<p>Get descriptor size in bytes.</p>
</dd>

### -field <b>pfnGetCPUDescriptorHandleForHeapStart</b>

<dd>
<p>Get CPU descriptor handle for heap start.</p>
</dd>

### -field <b>pfnGetGPUDescriptorHandleForHeapStart</b>

<dd>
<p>Get GPU descriptor handle for heap start.</p>
</dd>

### -field <b>pfnCreateShaderResourceView</b>

<dd>
<p>Create shader resource view.</p>
</dd>

### -field <b>pfnCreateConstantBufferView</b>

<dd>
<p>Create constant buffer view.</p>
</dd>

### -field <b>pfnCreateSampler</b>

<dd>
<p>Create sampler.</p>
</dd>

### -field <b>pfnCreateUnorderedAccessView</b>

<dd>
<p>Create unordered access view.</p>
</dd>

### -field <b>pfnCreateRenderTargetView</b>

<dd>
<p>Create render target view.</p>
</dd>

### -field <b>pfnCreateDepthStencilView</b>

<dd>
<p>Create depth stencil view.</p>
</dd>

### -field <b>pfnCalcPrivateRootSignatureSize</b>

<dd>
<p>Calculate private root signature size.</p>
</dd>

### -field <b>pfnCreateRootSignature</b>

<dd>
<p>Create root signature.</p>
</dd>

### -field <b>pfnDestroyRootSignature</b>

<dd>
<p>Destroy root signature.</p>
</dd>

### -field <b>pfnMapHeap</b>

<dd>
<p>Map heap.</p>
</dd>

### -field <b>pfnUnmapHeap</b>

<dd>
<p>Unmap heap.</p>
</dd>

### -field <b>pfnCalcPrivateHeapAndResourceSizes</b>

<dd>
<p>Calculate private heap and resource sizes.</p>
</dd>

### -field <b>pfnCreateHeapAndResource</b>

<dd>
<p>Create heap and resource.</p>
</dd>

### -field <b>pfnDestroyHeapAndResource</b>

<dd>
<p>Destroy heap and resource.</p>
</dd>

### -field <b>pfnMakeResident</b>

<dd>
<p>Make resident.</p>
</dd>

### -field <b>pfnEvict</b>

<dd>
<p>Evict.</p>
</dd>

### -field <b>pfnCalcPrivateOpenedHeapAndResourceSizes</b>

<dd>
<p>Calculate private opened heap and resource sizes.</p>
</dd>

### -field <b>pfnOpenHeapAndResource</b>

<dd>
<p>Open heap and resource.</p>
</dd>

### -field <b>pfnCopyDescriptors</b>

<dd>
<p>Copy descriptors.</p>
</dd>

### -field <b>pfnCopyDescriptorsSimple</b>

<dd>
<p>Copy descriptor sample.</p>
</dd>

### -field <b>pfnCalcPrivateQueryHeapSize</b>

<dd>
<p>Calculate private query heap size.</p>
</dd>

### -field <b>pfnCreateQueryHeap</b>

<dd>
<p>Create query heap.</p>
</dd>

### -field <b>pfnDestroyQueryHeap</b>

<dd>
<p>Destroy query heap.</p>
</dd>

### -field <b>pfnCalcPrivateCommandSignatureSize</b>

<dd>
<p>Calculate private command signature size.</p>
</dd>

### -field <b>pfnCreateCommandSignature</b>

<dd>
<p>Create command signature.</p>
</dd>

### -field <b>pfnDestroyCommandSignature</b>

<dd>
<p>Destroy command signature.</p>
</dd>

### -field <b>pfnCheckResourceVirtualAddress</b>

<dd>
<p>Check resource virtual address.</p>
</dd>

### -field <b>pfnCheckResourceAllocationInfo</b>

<dd>
<p>Check resource allocation info.</p>
</dd>

### -field <b>pfnCheckSubresourceInfo</b>

<dd>
<p>Check sub resource info.</p>
</dd>

### -field <b>pfnCheckExistingResourceAllocationInfo</b>

<dd>
<p>Check existing resource allocation info.</p>
</dd>

### -field <b>pfnOfferResources</b>

<dd>
<p>Offer resources.</p>
</dd>

### -field <b>pfnReclaimResources</b>

<dd>
<p>Reclaim resources.</p>
</dd>

### -field <b>pfnGetImplicitPhysicalAdapterMask</b>

<dd>
<p>Get implicit physical adapter mask.</p>
</dd>

### -field <b>pfnGetPresentPrivateDriverDataSize</b>

<dd>
<p>Get present private driver data size.</p>
</dd>

### -field <b>pfnQueryNodeMap</b>

<dd>
<p>Query node map.</p>
</dd>

### -field <b>pfnRetrieveShaderComment</b>

<dd>
<p>Retrieve shader comment.</p>
</dd>

### -field <b>pfnCheckResourceAllocationHandle</b>

<dd>
<p>Check resource allocation handle.</p>
</dd>

### -field <b>pfnCalcPrivatePipelineLibrarySize</b>

<dd>
<p>Calculate private pipeline library size.</p>
</dd>

### -field <b>pfnCreatePipelineLibrary</b>

<dd>
<p>Create pipeline library.</p>
</dd>

### -field <b>pfnDestroyPipelineLibrary</b>

<dd>
<p>Destroy pipeline library.</p>
</dd>

### -field <b>pfnAddPipelineStateToLibrary</b>

<dd>
<p>Add pipeline state to library.</p>
</dd>

### -field <b>pfnCalcSerializedLibrarySize</b>

<dd>
<p>Calculate serialized library size.</p>
</dd>

### -field <b>pfnSerializeLibrary</b>

<dd>
<p>Serialized libary.</p>
</dd>

### -field <b>pfnGetDebugAllocationInfo</b>

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