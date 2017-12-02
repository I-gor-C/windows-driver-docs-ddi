---
UID: NS.d3d12umddi.D3D12DDI_COMMAND_LIST_FUNCS_3D_0033
title: D3D12DDI_COMMAND_LIST_FUNCS_3D_0033
author: windows-driver-content
description: The command list functions for 3D.
old-location: display\d3d12ddi-command-list-funcs-3d-0033.htm
old-project: display
ms.assetid: 421e0623-0679-4068-b8e0-f0278abd2caf
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_COMMAND_LIST_FUNCS_3D_0033, D3D12DDI_COMMAND_LIST_FUNCS_3D_0033
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
req.alt-api: D3D12DDI_COMMAND_LIST_FUNCS_3D_0033
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

# D3D12DDI_COMMAND_LIST_FUNCS_3D_0033 structure



## -description
<p>The command list functions for 3D.</p>


## -syntax

````
typedef struct _D3D12DDI_COMMAND_LIST_FUNCS_3D_0033 {
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
  PFND3D12DDI_WRITEBUFFERIMMEDIATE_0032               pfnWriteBufferImmediate;
  PFND3D12DDI_SETVIEWINSTANCEMASK_0033                pfnSetViewInstanceMask;
} D3D12DDI_COMMAND_LIST_FUNCS_3D_0033, D3D12DDI_COMMAND_LIST_FUNCS_3D_0033;
````


## -struct-fields
<dl>

### -field pfnCloseCommandList

<dd>
<p>Close the command list.</p>
</dd>

### -field pfnResetCommandList

<dd>
<p>Reset the command list.</p>
</dd>

### -field pfnDrawInstanced

<dd>
<p>Draw instanced.</p>
</dd>

### -field pfnDrawIndexedInstanced

<dd>
<p>Draw indexed instanced.</p>
</dd>

### -field pfnDispatch

<dd>
<p>Dispatch.</p>
</dd>

### -field pfnClearUnorderedAccessViewUint

<dd>
<p>Clear unordered access view unit.</p>
</dd>

### -field pfnClearUnorderedAccessViewFloat

<dd>
<p>Clear unordered access view float.</p>
</dd>

### -field pfnClearRenderTargetView

<dd>
<p>Clear render target view.</p>
</dd>

### -field pfnClearDepthStencilView

<dd>
<p>Clear depth stencil view.</p>
</dd>

### -field pfnDiscardResource

<dd>
<p>Discard resource.</p>
</dd>

### -field pfnCopyTextureRegion

<dd>
<p>Copy texture region.</p>
</dd>

### -field pfnResourceCopy

<dd>
<p>Resource copy.</p>
</dd>

### -field pfnCopyTiles

<dd>
<p>Copy tiles.</p>
</dd>

### -field pfnCopyBufferRegion

<dd>
<p>Copy buffer region.</p>
</dd>

### -field pfnResourceResolveSubresource

<dd>
<p>Resource resolve subresource.</p>
</dd>

### -field pfnExecuteBundle

<dd>
<p>Execute bundle.</p>
</dd>

### -field pfnExecuteIndirect

<dd>
<p>Execute indirect.</p>
</dd>

### -field pfnResourceBarrier

<dd>
<p>Resource barrier.</p>
</dd>

### -field pfnBlt

<dd>
<p>Blt.</p>
</dd>

### -field pfnPresent

<dd>
<p>Present.</p>
</dd>

### -field pfnBeginQuery

<dd>
<p>Begin query.</p>
</dd>

### -field pfnEndQuery

<dd>
<p>End query.</p>
</dd>

### -field pfnResolveQueryData

<dd>
<p>Resolve query data.</p>
</dd>

### -field pfnSetPredication

<dd>
<p>Set predication.</p>
</dd>

### -field pfnIaSetTopology

<dd>
<p>Set topology</p>
</dd>

### -field pfnRsSetViewports

<dd>
<p>Set view ports.</p>
</dd>

### -field pfnRsSetScissorRects

<dd>
<p>Set scissor rectangles.</p>
</dd>

### -field pfnOmSetBlendFactor

<dd>
<p>Set blend factor.</p>
</dd>

### -field pfnOmSetStencilRef

<dd>
<p>Set stencil reference.</p>
</dd>

### -field pfnSetPipelineState

<dd>
<p>Set pipeline state.</p>
</dd>

### -field pfnSetDescriptorHeaps

<dd>
<p>Set descriptor heaps.</p>
</dd>

### -field pfnSetComputeRootSignature

<dd>
<p>Set compute root signature.</p>
</dd>

### -field pfnSetGraphicsRootSignature

<dd>
<p>Set graphics root signature.</p>
</dd>

### -field pfnSetComputeRootDescriptorTable

<dd>
<p>Set compute root descriptor table.</p>
</dd>

### -field pfnSetGraphicsRootDescriptorTable

<dd>
<p>Set graphics root descriptor table.</p>
</dd>

### -field pfnSetComputeRoot32BitConstant

<dd>
<p>Set compute root 32-bit constant.</p>
</dd>

### -field pfnSetGraphicsRoot32BitConstant

<dd>
<p>Set graphics root 32-bit constant.</p>
</dd>

### -field pfnSetComputeRoot32BitConstants

<dd>
<p>Set compute root 32-bit constants.</p>
</dd>

### -field pfnSetGraphicsRoot32BitConstants

<dd>
<p>Set graphics root 32-bit constants.</p>
</dd>

### -field pfnSetComputeRootConstantBufferView

<dd>
<p>Set compute root constant buffer view.</p>
</dd>

### -field pfnSetGraphicsRootConstantBufferView

<dd>
<p>Set graphics root constant buffer view.</p>
</dd>

### -field pfnSetComputeRootShaderResourceView

<dd>
<p>Set compute root shader resource view.</p>
</dd>

### -field pfnSetGraphicsRootShaderResourceView

<dd>
<p>Set graphics root shader resource view.</p>
</dd>

### -field pfnSetComputeRootUnorderedAccessView

<dd>
<p>Set compute root unordered access view.</p>
</dd>

### -field pfnSetGraphicsRootUnorderedAccessView

<dd>
<p>Set graphics root unordered access view.</p>
</dd>

### -field pfnIASetIndexBuffer

<dd>
<p>Set index buffer.</p>
</dd>

### -field pfnIASetVertexBuffers

<dd>
<p>Set vertex buffers.</p>
</dd>

### -field pfnSOSetTargets

<dd>
<p>Set targets.</p>
</dd>

### -field pfnOMSetRenderTargets

<dd>
<p>Set render targets.</p>
</dd>

### -field pfnSetMarker

<dd>
<p>Set marker.</p>
</dd>

### -field pfnClearRootArguments

<dd>
<p>Clear root arguments.</p>
</dd>

### -field pfnAtomicCopyBufferRegion

<dd>
<p>Atomic copy buffer region.</p>
</dd>

### -field pfnOMSetDepthBounds

<dd>
<p>Set depth bounds.</p>
</dd>

### -field pfnSetSamplePositions

<dd>
<p>Set sample positions.</p>
</dd>

### -field pfnResourceResolveSubresourceRegion

<dd>
<p>Resource resolve subresource region.</p>
</dd>

### -field pfnSetProtectedResourceSession

<dd>
<p>Set protected resource session.</p>
</dd>

### -field pfnWriteBufferImmediate

<dd>
<p>Write buffer immediate.</p>
</dd>

### -field pfnSetViewInstanceMask

<dd>
<p>Set view instance mask.</p>
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