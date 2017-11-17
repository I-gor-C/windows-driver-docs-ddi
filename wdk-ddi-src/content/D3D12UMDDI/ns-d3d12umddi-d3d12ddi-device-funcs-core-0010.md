---
UID: NS.d3d12umddi.D3D12DDI_DEVICE_FUNCS_CORE_0010
title: D3D12DDI_DEVICE_FUNCS_CORE_0010
author: windows-driver-content
description: Contains core functions.
old-location: display\d3d12ddi_device_funcs_core_0010.htm
ms.assetid: 87B4873E-DD44-47E9-8E6A-5BA91218188F
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_DEVICE_FUNCS_CORE_0010
req.alt-loc: D3d12umddi.h
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
ms.keywords: D3D12DDI_DEVICE_FUNCS_CORE_0010, D3D12DDI_DEVICE_FUNCS_CORE_0010
req.iface: 
---

# D3D12DDI_DEVICE_FUNCS_CORE_0010 structure



## -description
<p>Contains core functions.</p>


## -syntax

````
typedef struct D3D12DDI_DEVICE_FUNCS_CORE_0010 {
  PFND3D12DDI_CHECKFORMATSUPPORT                                   pfnCheckFormatSupport;
  PFND3D12DDI_CHECKMULTISAMPLEQUALITYLEVELS                        pfnCheckMultisampleQualityLevels;
  PFND3D12DDI_GETMIPPACKING                                        pfnGetMipPacking;
  PFND3D12DDI_CALCPRIVATEELEMENTLAYOUTSIZE_0010                    pfnCalcPrivateElementLayoutSize;
  PFND3D12DDI_CREATEELEMENTLAYOUT_0010                             pfnCreateElementLayout;
  PFND3D12DDI_DESTROYELEMENTLAYOUT                                 pfnDestroyElementLayout;
  PFND3D12DDI_CALCPRIVATEBLENDSTATESIZE_0010                       pfnCalcPrivateBlendStateSize;
  PFND3D12DDI_CREATEBLENDSTATE_0010                                pfnCreateBlendState;
  PFND3D12DDI_DESTROYBLENDSTATE                                    pfnDestroyBlendState;
  PFND3D12DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE_0010                pfnCalcPrivateDepthStencilStateSize;
  PFND3D12DDI_CREATEDEPTHSTENCILSTATE_0010                         pfnCreateDepthStencilState;
  PFND3D12DDI_DESTROYDEPTHSTENCILSTATE                             pfnDestroyDepthStencilState;
  PFND3D12DDI_CALCPRIVATERASTERIZERSTATESIZE_0010                  pfnCalcPrivateRasterizerStateSize;
  PFND3D12DDI_CREATERASTERIZERSTATE_0010                           pfnCreateRasterizerState;
  PFND3D12DDI_DESTROYRASTERIZERSTATE                               pfnDestroyRasterizerState;
  PFND3D12DDI_CALC_PRIVATE_SHADER_SIZE_0010                        pfnCalcPrivateShaderSize;
  PFND3D12DDI_CREATE_SHADER_0010                                   pfnCreateVertexShader;
  PFND3D12DDI_CREATE_SHADER_0010                                   pfnCreatePixelShader;
  PFND3D12DDI_CREATE_SHADER_0010                                   pfnCreateGeometryShader;
  PFND3D12DDI_CREATE_SHADER_0010                                   pfnCreateComputeShader;
  PFND3D12DDI_CALC_PRIVATE_GEOMETRY_SHADER_WITH_STREAM_OUTPUT_0010 pfnCalcPrivateGeometryShaderWithStreamOutput;
  PFND3D12DDI_CREATE_GEOMETRY_SHADER_WITH_STREAM_OUTPUT_0010       pfnCreateGeometryShaderWithStreamOutput;
  PFND3D12DDI_CALC_PRIVATE_SHADER_SIZE_0010                        pfnCalcPrivateTessellationShaderSize;
  PFND3D12DDI_CREATE_SHADER_0010                                   pfnCreateHullShader;
  PFND3D12DDI_CREATE_SHADER_0010                                   pfnCreateDomainShader;
  PFND3D12DDI_DESTROYSHADER                                        pfnDestroyShader;
  PFND3D12DDI_CALCPRIVATECOMMANDQUEUESIZE_0001                     pfnCalcPrivateCommandQueueSize;
  PFND3D12DDI_CREATECOMMANDQUEUE_0001                              pfnCreateCommandQueue;
  PFND3D12DDI_DESTROYCOMMANDQUEUE                                  pfnDestroyCommandQueue;
  PFND3D12DDI_CALCPRIVATECOMMANDALLOCATORSIZE                      pfnCalcPrivateCommandAllocatorSize;
  PFND3D12DDI_CREATECOMMANDALLOCATOR                               pfnCreateCommandAllocator;
  PFND3D12DDI_DESTROYCOMMANDALLOCATOR                              pfnDestroyCommandAllocator;
  PFND3D12DDI_RESETCOMMANDALLOCATOR                                pfnResetCommandAllocator;
  PFND3D12DDI_CALC_PRIVATE_PIPELINE_STATE_SIZE_0010                pfnCalcPrivatePipelineStateSize;
  PFND3D12DDI_CREATE_PIPELINE_STATE_0010                           pfnCreatePipelineState;
  PFND3D12DDI_DESTROY_PIPELINE_STATE                               pfnDestroyPipelineState;
  PFND3D12DDI_CALC_PRIVATE_COMMAND_LIST_SIZE_0001                  pfnCalcPrivateCommandListSize;
  PFND3D12DDI_CREATE_COMMAND_LIST_0001                             pfnCreateCommandList;
  PFND3D12DDI_DESTROYCOMMANDLIST                                   pfnDestroyCommandList;
  PFND3D12DDI_CALCPRIVATEFENCESIZE                                 pfnCalcPrivateFenceSize;
  PFND3D12DDI_CREATEFENCE                                          pfnCreateFence;
  PFND3D12DDI_DESTROYFENCE                                         pfnDestroyFence;
  PFND3D12DDI_CALC_PRIVATE_DESCRIPTOR_HEAP_SIZE_0001               pfnCalcPrivateDescriptorHeapSize;
  PFND3D12DDI_CREATE_DESCRIPTOR_HEAP_0001                          pfnCreateDescriptorHeap;
  PFND3D12DDI_DESTROY_DESCRIPTOR_HEAP                              pfnDestroyDescriptorHeap;
  PFND3D12DDI_GET_DESCRIPTOR_SIZE_IN_BYTES                         pfnGetDescriptorSizeInBytes;
  PFND3D12DDI_GET_CPU_DESCRIPTOR_HANDLE_FOR_HEAP_START             pfnGetCPUDescriptorHandleForHeapStart;
  PFND3D12DDI_GET_GPU_DESCRIPTOR_HANDLE_FOR_HEAP_START             pfnGetGPUDescriptorHandleForHeapStart;
  PFND3D12DDI_CREATE_SHADER_RESOURCE_VIEW_0002                     pfnCreateShaderResourceView;
  PFND3D12DDI_CREATE_CONSTANT_BUFFER_VIEW                          pfnCreateConstantBufferView;
  PFND3D12DDI_CREATE_SAMPLER                                       pfnCreateSampler;
  PFND3D12DDI_CREATE_UNORDERED_ACCESS_VIEW_0002                    pfnCreateUnorderedAccessView;
  PFND3D12DDI_CREATE_RENDER_TARGET_VIEW_0002                       pfnCreateRenderTargetView;
  PFND3D12DDI_CREATE_DEPTH_STENCIL_VIEW                            pfnCreateDepthStencilView;
  PFND3D12DDI_CALC_PRIVATE_ROOT_SIGNATURE_SIZE_0001                pfnCalcPrivateRootSignatureSize;
  PFND3D12DDI_CREATE_ROOT_SIGNATURE_0001                           pfnCreateRootSignature;
  PFND3D12DDI_DESTROY_ROOT_SIGNATURE                               pfnDestroyRootSignature;
  PFND3D12DDI_MAPHEAP                                              pfnMapHeap;
  PFND3D12DDI_UNMAPHEAP                                            pfnUnmapHeap;
  PFND3D12DDI_CALCPRIVATEHEAPANDRESOURCESIZES_0003                 pfnCalcPrivateHeapAndResourceSizes;
  PFND3D12DDI_CREATEHEAPANDRESOURCE_0003                           pfnCreateHeapAndResource;
  PFND3D12DDI_DESTROYHEAPANDRESOURCE                               pfnDestroyHeapAndResource;
  PFND3D12DDI_MAKERESIDENT_0001                                    pfnMakeResident;
  PFND3D12DDI_EVICT2                                               pfnEvict;
  PFND3D12DDI_CALCPRIVATEOPENEDHEAPANDRESOURCESIZES_0003           pfnCalcPrivateOpenedHeapAndResourceSizes;
  PFND3D12DDI_OPENHEAPANDRESOURCE_0003                             pfnOpenHeapAndResource;
  PFND3D12DDI_COPY_DESCRIPTORS_0003                                pfnCopyDescriptors;
  PFND3D12DDI_COPY_DESCRIPTORS_SIMPLE_0003                         pfnCopyDescriptorsSimple;
  PFND3D12DDI_CALC_PRIVATE_QUERY_HEAP_SIZE_0001                    pfnCalcPrivateQueryHeapSize;
  PFND3D12DDI_CREATE_QUERY_HEAP_0001                               pfnCreateQueryHeap;
  PFND3D12DDI_DESTROY_QUERY_HEAP                                   pfnDestroyQueryHeap;
  PFND3D12DDI_CALC_PRIVATE_COMMAND_SIGNATURE_SIZE_0001             pfnCalcPrivateCommandSignatureSize;
  PFND3D12DDI_CREATE_COMMAND_SIGNATURE_0001                        pfnCreateCommandSignature;
  PFND3D12DDI_DESTROY_COMMAND_SIGNATURE                            pfnDestroyCommandSignature;
  PFND3D12DDI_CHECKRESOURCEVIRTUALADDRESS                          pfnCheckResourceVirtualAddress;
  PFND3D12DDI_CHECKRESOURCEALLOCATIONINFO_0003                     pfnCheckResourceAllocationInfo;
  PFND3D12DDI_CHECKSUBRESOURCEINFO                                 pfnCheckSubresourceInfo;
  PFND3D12DDI_CHECKEXISITINGRESOURCEALLOCATIONINFO                 pfnCheckExistingResourceAllocationInfo;
  PFND3D12DDI_OFFERRESOURCES                                       pfnOfferResources;
  PFND3D12DDI_RECLAIMRESOURCES_0001                                pfnReclaimResources;
  PFND3D12DDI_GETIMPLICITPHYSICALADAPTERMASK                       pfnGetImplicitPhysicalAdapterMask;
  PFND3D12DDI_GET_PRESENT_PRIVATE_DRIVER_DATA_SIZE                 pfnGetPresentPrivateDriverDataSize;
  PFND3D12DDI_QUERY_NODE_MAP                                       pfnQueryNodeMap;
  PFND3D12DDI_RETRIEVE_SHADER_COMMENT_0003                         pfnRetrieveShaderComment;
  PFND3D12DDI_CHECKRESOURCEALLOCATIONHANDLE                        pfnCheckResourceAllocationHandle;
  PFND3D12DDI_CALC_PRIVATE_PIPELINE_LIBRARY_SIZE_0010              pfnCalcPrivatePipelineLibrarySize;
  PFND3D12DDI_CREATE_PIPELINE_LIBRARY_0010                         pfnCreatePipelineLibrary;
  PFND3D12DDI_DESTROY_PIPELINE_LIBRARY_0010                        pfnDestroyPipelineLibrary;
  PFND3D12DDI_ADD_PIPELINE_STATE_TO_LIBRARY_0010                   pfnAddPipelineStateToLibrary;
  PFND3D12DDI_CALC_SERIALIZED_LIBRARY_SIZE_0010                    pfnCalcSerializedLibrarySize;
  PFND3D12DDI_SERIALIZE_LIBRARY_0010                               pfnSerializeLibrary;
} D3D12DDI_DEVICE_FUNCS_CORE_0010;
````


## -struct-fields
<dl>

### -field <b>pfnCheckFormatSupport</b>

<dd>
<p>A function that checks format support.</p>
</dd>

### -field <b>pfnCheckMultisampleQualityLevels</b>

<dd>
<p>A function that checks multi-sample quality levels. </p>
</dd>

### -field <b>pfnGetMipPacking</b>

<dd>
<p>A function that gets MIP packing.</p>
</dd>

### -field <b>pfnCalcPrivateElementLayoutSize</b>

<dd>
<p>A function that calculates layout size for a private element. </p>
</dd>

### -field <b>pfnCreateElementLayout</b>

<dd>
<p>A function that creates an element layout. </p>
</dd>

### -field <b>pfnDestroyElementLayout</b>

<dd>
<p>A function that destroys an element layout.</p>
</dd>

### -field <b>pfnCalcPrivateBlendStateSize</b>

<dd>
<p>A function that calculates the size of a private blend state.</p>
</dd>

### -field <b>pfnCreateBlendState</b>

<dd>
<p>A function that creates a blend state.</p>
</dd>

### -field <b>pfnDestroyBlendState</b>

<dd>
<p>A function that destroys a blend state.</p>
</dd>

### -field <b>pfnCalcPrivateDepthStencilStateSize</b>

<dd>
<p>A function that calculates the size of the state of a private depth stencil. </p>
</dd>

### -field <b>pfnCreateDepthStencilState</b>

<dd>
<p>A function that creates a depth stencil state.</p>
</dd>

### -field <b>pfnDestroyDepthStencilState</b>

<dd>
<p>A function that destroys a depth stencil state.</p>
</dd>

### -field <b>pfnCalcPrivateRasterizerStateSize</b>

<dd>
<p>A function that calculates the size of a private rasterizer state. </p>
</dd>

### -field <b>pfnCreateRasterizerState</b>

<dd>
<p>A function that creates a rasterizer state.</p>
</dd>

### -field <b>pfnDestroyRasterizerState</b>

<dd>
<p>A function that destroys a rasterizer state.</p>
</dd>

### -field <b>pfnCalcPrivateShaderSize</b>

<dd>
<p>A function that calculates the size of a private shader. </p>
</dd>

### -field <b>pfnCreateVertexShader</b>

<dd>
<p>A function that creates a vertex shader. </p>
</dd>

### -field <b>pfnCreatePixelShader</b>

<dd>
<p>A function that creates a shader.</p>
</dd>

### -field <b>pfnCreateGeometryShader</b>

<dd>
<p>A function that creates a geometry shader.</p>
</dd>

### -field <b>pfnCreateComputeShader</b>

<dd>
<p>A function that creates a compute shader. </p>
</dd>

### -field <b>pfnCalcPrivateGeometryShaderWithStreamOutput</b>

<dd>
<p>A function that calculates a private geometry shader with stream output. </p>
</dd>

### -field <b>pfnCreateGeometryShaderWithStreamOutput</b>

<dd>
<p>A function that creates a private geometry shader with stream output. </p>
</dd>

### -field <b>pfnCalcPrivateTessellationShaderSize</b>

<dd>
<p>A function that creates private tessellation shader size. </p>
</dd>

### -field <b>pfnCreateHullShader</b>

<dd>
<p>A function that creates a hull shader.</p>
</dd>

### -field <b>pfnCreateDomainShader</b>

<dd>
<p>A function that creates a domain shader.</p>
</dd>

### -field <b>pfnDestroyShader</b>

<dd>
<p>A function that destroys a shader.</p>
</dd>

### -field <b>pfnCalcPrivateCommandQueueSize</b>

<dd>
<p>A function that calculates the size of a private queue.</p>
</dd>

### -field <b>pfnCreateCommandQueue</b>

<dd>
<p>A function that creates a command queue.</p>
</dd>

### -field <b>pfnDestroyCommandQueue</b>

<dd>
<p>A function that destroys a command queue.</p>
</dd>

### -field <b>pfnCalcPrivateCommandAllocatorSize</b>

<dd>
<p>A function that calculates the size of a private command allocator.</p>
</dd>

### -field <b>pfnCreateCommandAllocator</b>

<dd>
<p>A function that creates a command allocator.</p>
</dd>

### -field <b>pfnDestroyCommandAllocator</b>

<dd>
<p>A function that destroys a command allocator. </p>
</dd>

### -field <b>pfnResetCommandAllocator</b>

<dd>
<p>A function that resets a command allocator. </p>
</dd>

### -field <b>pfnCalcPrivatePipelineStateSize</b>

<dd>
<p>A function that calculate the size of a private pipeline state.</p>
</dd>

### -field <b>pfnCreatePipelineState</b>

<dd>
<p>A function that crates a pipeline state.</p>
</dd>

### -field <b>pfnDestroyPipelineState</b>

<dd>
<p>A function that destroys a pipeline state.</p>
</dd>

### -field <b>pfnCalcPrivateCommandListSize</b>

<dd>
<p>A function that calculate the size of a private command list.</p>
</dd>

### -field <b>pfnCreateCommandList</b>

<dd>
<p>A function that creates a command list.</p>
</dd>

### -field <b>pfnDestroyCommandList</b>

<dd>
<p>A function that destroys a command list. </p>
</dd>

### -field <b>pfnCalcPrivateFenceSize</b>

<dd>
<p>A function that calculates a private fence size. </p>
</dd>

### -field <b>pfnCreateFence</b>

<dd>
<p>A function that creates a fence.</p>
</dd>

### -field <b>pfnDestroyFence</b>

<dd>
<p>A function that destroys a fence. </p>
</dd>

### -field <b>pfnCalcPrivateDescriptorHeapSize</b>

<dd>
<p>A function that calculates the size of a private descriptor heap.</p>
</dd>

### -field <b>pfnCreateDescriptorHeap</b>

<dd>
<p>A function that creates a descriptor heap.</p>
</dd>

### -field <b>pfnDestroyDescriptorHeap</b>

<dd>
<p>A function that destroys a descriptor heap. </p>
</dd>

### -field <b>pfnGetDescriptorSizeInBytes</b>

<dd>
<p>A function that gets the descriptor size, in bytes.</p>
</dd>

### -field <b>pfnGetCPUDescriptorHandleForHeapStart</b>

<dd>
<p>A function that gets a CPU descriptor handle. </p>
</dd>

### -field <b>pfnGetGPUDescriptorHandleForHeapStart</b>

<dd>
<p>A function that gets a GPU descriptor handle.</p>
</dd>

### -field <b>pfnCreateShaderResourceView</b>

<dd>
<p>A function that creates a shader resource view. </p>
</dd>

### -field <b>pfnCreateConstantBufferView</b>

<dd>
<p>A function that creates a constant buffer view. </p>
</dd>

### -field <b>pfnCreateSampler</b>

<dd>
<p>A function that creates a sampler.</p>
</dd>

### -field <b>pfnCreateUnorderedAccessView</b>

<dd>
<p>A function that creates an unordered access view. </p>
</dd>

### -field <b>pfnCreateRenderTargetView</b>

<dd>
<p>A function that creates a render target view. </p>
</dd>

### -field <b>pfnCreateDepthStencilView</b>

<dd>
<p>A function that creates a depth stencil view. </p>
</dd>

### -field <b>pfnCalcPrivateRootSignatureSize</b>

<dd>
<p>A function that calculates the size of a private root signature. </p>
</dd>

### -field <b>pfnCreateRootSignature</b>

<dd>
<p>A function that creates a root signature. </p>
</dd>

### -field <b>pfnDestroyRootSignature</b>

<dd>
<p>A function that destroys a root signature. </p>
</dd>

### -field <b>pfnMapHeap</b>

<dd>
<p>A function that maps a heap.</p>
</dd>

### -field <b>pfnUnmapHeap</b>

<dd>
<p>A function that unmaps a heap.</p>
</dd>

### -field <b>pfnCalcPrivateHeapAndResourceSizes</b>

<dd>
<p>A function that calculates sizes for private heap and resource. </p>
</dd>

### -field <b>pfnCreateHeapAndResource</b>

<dd>
<p>A function that create a heap and resource. </p>
</dd>

### -field <b>pfnDestroyHeapAndResource</b>

<dd>
<p>A function that destroys a heap and resource. </p>
</dd>

### -field <b>pfnMakeResident</b>

<dd>
<p>A function that makes a resident. </p>
</dd>

### -field <b>pfnEvict</b>

<dd>
<p>A function that evicts. </p>
</dd>

### -field <b>pfnCalcPrivateOpenedHeapAndResourceSizes</b>

<dd>
<p>A function that calculates sizes for private opened heap and resources. </p>
</dd>

### -field <b>pfnOpenHeapAndResource</b>

<dd>
<p>A function that opens a heap and resource. </p>
</dd>

### -field <b>pfnCopyDescriptors</b>

<dd>
<p>A function that copies descriptors. </p>
</dd>

### -field <b>pfnCopyDescriptorsSimple</b>

<dd>
<p>A function that does a simple copy of descriptors. </p>
</dd>

### -field <b>pfnCalcPrivateQueryHeapSize</b>

<dd>
<p>A function that calculates the size of a private query heap.</p>
</dd>

### -field <b>pfnCreateQueryHeap</b>

<dd>
<p>A function that creates a query heap.</p>
</dd>

### -field <b>pfnDestroyQueryHeap</b>

<dd>
<p>A function that destroys a query heap. </p>
</dd>

### -field <b>pfnCalcPrivateCommandSignatureSize</b>

<dd>
<p>A function that calculates the size of a private command signature. </p>
</dd>

### -field <b>pfnCreateCommandSignature</b>

<dd>
<p>A function that creates a command signature. </p>
</dd>

### -field <b>pfnDestroyCommandSignature</b>

<dd>
<p>A function that destroys a command signature. </p>
</dd>

### -field <b>pfnCheckResourceVirtualAddress</b>

<dd>
<p>A function that checks the virtual address of a resource.</p>
</dd>

### -field <b>pfnCheckResourceAllocationInfo</b>

<dd>
<p>A function that checks allocation information of a resource.</p>
</dd>

### -field <b>pfnCheckSubresourceInfo</b>

<dd>
<p>A function that checks information of a subresource. </p>
</dd>

### -field <b>pfnCheckExistingResourceAllocationInfo</b>

<dd>
<p>A function that checks allocation information of an existing resource.</p>
</dd>

### -field <b>pfnOfferResources</b>

<dd>
<p>A function that offers resources.</p>
</dd>

### -field <b>pfnReclaimResources</b>

<dd>
<p>A function that reclaims resources. </p>
</dd>

### -field <b>pfnGetImplicitPhysicalAdapterMask</b>

<dd>
<p>A function that gets an implicit physical adapter mask.</p>
</dd>

### -field <b>pfnGetPresentPrivateDriverDataSize</b>

<dd>
<p>A function that gets the present size of private driver data. </p>
</dd>

### -field <b>pfnQueryNodeMap</b>

<dd>
<p>A function that queries a node map.</p>
</dd>

### -field <b>pfnRetrieveShaderComment</b>

<dd>
<p>A function that retrieves a shader comment. </p>
</dd>

### -field <b>pfnCheckResourceAllocationHandle</b>

<dd>
<p>A function that checks a resource allocation handle. </p>
</dd>

### -field <b>pfnCalcPrivatePipelineLibrarySize</b>

<dd>
<p>A function that calculates the size of a private pipeline library.</p>
</dd>

### -field <b>pfnCreatePipelineLibrary</b>

<dd>
<p>A function that creates a pipeline library.</p>
</dd>

### -field <b>pfnDestroyPipelineLibrary</b>

<dd>
<p>A function that destroys a pipeline library.</p>
</dd>

### -field <b>pfnAddPipelineStateToLibrary</b>

<dd>
<p>A function that adds pipeline state to a library.</p>
</dd>

### -field <b>pfnCalcSerializedLibrarySize</b>

<dd>
<p>A function that calculates the size of a serialized library.</p>
</dd>

### -field <b>pfnSerializeLibrary</b>

<dd>
<p>A function that serializes a library. </p>
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
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/F4C385C8-00A2-44AB-A7E6-4C9AA19CFFB0">D3D12DDI_DEVICE_FUNCS_VIDEO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D12DDI_DEVICE_FUNCS_CORE_0010 structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
