---
UID: NS:d3d12umddi.D3D12DDI_COMMAND_LIST_FUNCS_3D_0030
title: D3D12DDI_COMMAND_LIST_FUNCS_3D_0030
author: windows-driver-content
description: The command list functions for 3D.
old-location: display\d3d12ddi-command-list-funcs-3d-0030.htm
old-project: display
ms.assetid: ec09b652-a809-48e2-9f34-507df5fd9036
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: d3d12umddi/D3D12DDI_COMMAND_LIST_FUNCS_3D_0030, display.d3d12ddi-command-list-funcs-3d-0030, D3D12DDI_COMMAND_LIST_FUNCS_3D_0030, D3D12DDI_COMMAND_LIST_FUNCS_3D_0030 structure [Display Devices]
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3d12umddi.h
apiname:
-	D3D12DDI_COMMAND_LIST_FUNCS_3D_0030
product: Windows
targetos: Windows
req.typenames: D3D12DDI_COMMAND_LIST_FUNCS_3D_0030
---

# D3D12DDI_COMMAND_LIST_FUNCS_3D_0030 structure
The command list functions for 3D.

## Syntax
````
typedef struct _D3D12DDI_COMMAND_LIST_FUNCS_3D_0030 {
  PFND3D12DDI_CLOSECOMMANDLIST                        pfnCloseCommandList;
  PFND3D12DDI_RESETCOMMANDLIST                        pfnResetCommandList;
  PFND3D12DDI_DRAWINSTANCED                           pfnDrawInstanced;
  PFND3D12DDI_DRAWINDEXEDINSTANCED                    pfnDrawIndexedInstanced;
  PFND3D12DDI_DISPATCH                                pfnDispatch;
  PFND3D12DDI_CLEAR_UNORDERED_ACCESS_VIEW_UINT_0003   pfnClearUnorderedAccessViewUint;
  PFND3D12DDI_CLEAR_UNORDERED_ACCESS_VIEW_FLOAT_0003  pfnClearUnorderedAccessViewFloat;
  PFND3D12DDI_CLEAR_RENDER_TARGET_VIEW_0003           pfnClearRenderTargetView;
  PFND3D12DDI_CLEAR_DEPTH_STENCIL_VIEW_0003           pfnClearDepthStencilView;
  PFND3D12DDI_DISCARD_RESOURCE_0003                   pfnDiscardResource;
  PFND3D12DDI_COPYTEXTUREREGION_0003                  pfnCopyTextureRegion;
  PFND3D12DDI_RESOURCECOPY                            pfnResourceCopy;
  PFND3D12DDI_COPYTILES                               pfnCopyTiles;
  PFND3D12DDI_COPYBUFFERREGION_0003                   pfnCopyBufferRegion;
  PFND3D12DDI_RESOURCERESOLVESUBRESOURCE              pfnResourceResolveSubresource;
  PFND3D12DDI_EXECUTE_BUNDLE                          pfnExecuteBundle;
  PFND3D12DDI_EXECUTE_INDIRECT                        pfnExecuteIndirect;
  PFND3D12DDI_RESOURCEBARRIER_0022                    pfnResourceBarrier;
  PFND3D12DDI_BLT                                     pfnBlt;
  PFND3D12DDI_PRESENT_0028                            pfnPresent;
  PFND3D12DDI_BEGIN_END_QUERY_0003                    pfnBeginQuery;
  PFND3D12DDI_BEGIN_END_QUERY_0003                    pfnEndQuery;
  PFND3D12DDI_RESOLVE_QUERY_DATA                      pfnResolveQueryData;
  PFND3D12DDI_SET_PREDICATION                         pfnSetPredication;
  PFND3D12DDI_IA_SETTOPOLOGY_0003                     pfnIaSetTopology;
  PFND3D12DDI_RS_SETVIEWPORTS_0003                    pfnRsSetViewports;
  PFND3D12DDI_RS_SETSCISSORRECTS_0003                 pfnRsSetScissorRects;
  PFND3D12DDI_OM_SETBLENDFACTOR                       pfnOmSetBlendFactor;
  PFND3D12DDI_OM_SETSTENCILREF                        pfnOmSetStencilRef;
  PFND3D12DDI_SET_PIPELINE_STATE                      pfnSetPipelineState;
  PFND3D12DDI_SET_DESCRIPTOR_HEAPS_0003               pfnSetDescriptorHeaps;
  PFND3D12DDI_SET_ROOT_SIGNATURE                      pfnSetComputeRootSignature;
  PFND3D12DDI_SET_ROOT_SIGNATURE                      pfnSetGraphicsRootSignature;
  PFND3D12DDI_SET_ROOT_DESCRIPTOR_TABLE               pfnSetComputeRootDescriptorTable;
  PFND3D12DDI_SET_ROOT_DESCRIPTOR_TABLE               pfnSetGraphicsRootDescriptorTable;
  PFND3D12DDI_SET_ROOT_32BIT_CONSTANT                 pfnSetComputeRoot32BitConstant;
  PFND3D12DDI_SET_ROOT_32BIT_CONSTANT                 pfnSetGraphicsRoot32BitConstant;
  PFND3D12DDI_SET_ROOT_32BIT_CONSTANTS_0003           pfnSetComputeRoot32BitConstants;
  PFND3D12DDI_SET_ROOT_32BIT_CONSTANTS_0003           pfnSetGraphicsRoot32BitConstants;
  PFND3D12DDI_SET_ROOT_BUFFER_VIEW                    pfnSetComputeRootConstantBufferView;
  PFND3D12DDI_SET_ROOT_BUFFER_VIEW                    pfnSetGraphicsRootConstantBufferView;
  PFND3D12DDI_SET_ROOT_BUFFER_VIEW                    pfnSetComputeRootShaderResourceView;
  PFND3D12DDI_SET_ROOT_BUFFER_VIEW                    pfnSetGraphicsRootShaderResourceView;
  PFND3D12DDI_SET_ROOT_BUFFER_VIEW                    pfnSetComputeRootUnorderedAccessView;
  PFND3D12DDI_SET_ROOT_BUFFER_VIEW                    pfnSetGraphicsRootUnorderedAccessView;
  PFND3D12DDI_IA_SET_INDEX_BUFFER                     pfnIASetIndexBuffer;
  PFND3D12DDI_IA_SET_VERTEX_BUFFERS_0003              pfnIASetVertexBuffers;
  PFND3D12DDI_SO_SET_TARGETS_0003                     pfnSOSetTargets;
  PFND3D12DDI_OM_SET_RENDER_TARGETS_0003              pfnOMSetRenderTargets;
  PFND3D12DDI_SET_MARKER                              pfnSetMarker;
  PFND3D12DDI_CLEAR_ROOT_ARGUMENTS                    pfnClearRootArguments;
  PFND3D12DDI_COPYBUFFERREGION_0003                   pfnAtomicCopyBufferRegion;
  PFND3D12DDI_OM_SETDEPTHBOUNDS_0025                  pfnOMSetDepthBounds;
  PFND3D12DDI_SETSAMPLEPOSITIONS_0027                 pfnSetSamplePositions;
  PFND3D12DDI_RESOURCERESOLVESUBRESOURCEREGION_0027   pfnResourceResolveSubresourceRegion;
  PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030        pfnSetProtectedResourceSession;
} D3D12DDI_COMMAND_LIST_FUNCS_3D_0030, D3D12DDI_COMMAND_LIST_FUNCS_3D_0030;
````

## Members


`pfnAtomicCopyBufferRegion`

Atomic copy buffer region.

`pfnBeginQuery`

Begin query.

`pfnBlt`

Blt.

`pfnClearDepthStencilView`

Clear the depth stencil view.

`pfnClearRenderTargetView`

Clear the render target view.

`pfnClearRootArguments`

Clear root arguments.

`pfnClearUnorderedAccessViewFloat`

Clear the unordered access view of FLOAT values.

`pfnClearUnorderedAccessViewUint`

Clear the unordered access view of UINT values.

`pfnCloseCommandList`

Close the command list.

`pfnCopyBufferRegion`

Copy buffer region.

`pfnCopyTextureRegion`

Copy texture region.

`pfnCopyTiles`

Copy tiles.

`pfnDiscardResource`

Discard resource.

`pfnDispatch`

Dispatch.

`pfnDrawIndexedInstanced`

Draw indexed instanced.

`pfnDrawInstanced`

Draw instanced.

`pfnEndQuery`

End query.

`pfnExecuteBundle`

Execute bundle.

`pfnExecuteIndirect`

Execute indirect.

`pfnIASetIndexBuffer`

Set index buffer.

`pfnIaSetTopology`

Set topology.

`pfnIASetVertexBuffers`

Set vertex buffers.

`pfnOmSetBlendFactor`

Set blend factor.

`pfnOMSetDepthBounds`

Set depth bounds.

`pfnOMSetRenderTargets`

Set render targets.

`pfnOmSetStencilRef`

Set stencil reference.

`pfnPresent`

Present.

`pfnResetCommandList`

Reset the command list.

`pfnResolveQueryData`

Resolve query data.

`pfnResourceBarrier`

Resource barrier.

`pfnResourceCopy`

Resource copy.

`pfnResourceResolveSubresource`

Resource resolve subresource.

`pfnResourceResolveSubresourceRegion`

Resource resolve subresource region.

`pfnRsSetScissorRects`

Set scissor rectangles.

`pfnRsSetViewports`

Set view ports.

`pfnSetComputeRoot32BitConstant`

Set compute root 32-bit constant.

`pfnSetComputeRoot32BitConstants`

Set compute root 32-bit constants.

`pfnSetComputeRootConstantBufferView`

Set compute root constant buffer view.

`pfnSetComputeRootDescriptorTable`

Set compute root descriptor table.

`pfnSetComputeRootShaderResourceView`

Set compute root shader resource view.

`pfnSetComputeRootSignature`

Set compute root signature.

`pfnSetComputeRootUnorderedAccessView`

Set compute root unordered access view.

`pfnSetDescriptorHeaps`

Set descriptor heaps.

`pfnSetGraphicsRoot32BitConstant`

Set graphics root 32-bit constant.

`pfnSetGraphicsRoot32BitConstants`

Set graphics root 32-bit constants.

`pfnSetGraphicsRootConstantBufferView`

Set graphics root constant buffer view.

`pfnSetGraphicsRootDescriptorTable`

Set graphics root descriptor table.

`pfnSetGraphicsRootShaderResourceView`

Set graphics root shader resource view.

`pfnSetGraphicsRootSignature`

Set graphics root signature.

`pfnSetGraphicsRootUnorderedAccessView`

Set graphics root unordered access view.

`pfnSetMarker`

Set marker.

`pfnSetPipelineState`

Set pipeline state.

`pfnSetPredication`

Set predication.

`pfnSetProtectedResourceSession`

Set protected resource session.

`pfnSetSamplePositions`

Set sample positions.

`pfnSOSetTargets`

Set targets.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d12umddi.h |