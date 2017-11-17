---
UID: NS.d3d12umddi.D3D12DDI_COMMAND_LIST_FUNCS_3D_0033
title: D3D12DDI_COMMAND_LIST_FUNCS_3D_0033
author: windows-driver-content
description: The command list functions for 3D.
old-location: display\d3d12ddi-command-list-funcs-3d-0033.htm
ms.assetid: 421e0623-0679-4068-b8e0-f0278abd2caf
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
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
ms.keywords: D3D12DDI_COMMAND_LIST_FUNCS_3D_0033, D3D12DDI_COMMAND_LIST_FUNCS_3D_0033
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

### -field <b>pfnCloseCommandList</b>

<dd>
<p>Close the command list.</p>
</dd>

### -field <b>pfnResetCommandList</b>

<dd>
<p>Reset the command list.</p>
</dd>

### -field <b>pfnDrawInstanced</b>

<dd>
<p>Draw instanced.</p>
</dd>

### -field <b>pfnDrawIndexedInstanced</b>

<dd>
<p>Draw indexed instanced.</p>
</dd>

### -field <b>pfnDispatch</b>

<dd>
<p>Dispatch.</p>
</dd>

### -field <b>pfnClearUnorderedAccessViewUint</b>

<dd>
<p>Clear unordered access view unit.</p>
</dd>

### -field <b>pfnClearUnorderedAccessViewFloat</b>

<dd>
<p>Clear unordered access view float.</p>
</dd>

### -field <b>pfnClearRenderTargetView</b>

<dd>
<p>Clear render target view.</p>
</dd>

### -field <b>pfnClearDepthStencilView</b>

<dd>
<p>Clear depth stencil view.</p>
</dd>

### -field <b>pfnDiscardResource</b>

<dd>
<p>Discard resource.</p>
</dd>

### -field <b>pfnCopyTextureRegion</b>

<dd>
<p>Copy texture region.</p>
</dd>

### -field <b>pfnResourceCopy</b>

<dd>
<p>Resource copy.</p>
</dd>

### -field <b>pfnCopyTiles</b>

<dd>
<p>Copy tiles.</p>
</dd>

### -field <b>pfnCopyBufferRegion</b>

<dd>
<p>Copy buffer region.</p>
</dd>

### -field <b>pfnResourceResolveSubresource</b>

<dd>
<p>Resource resolve subresource.</p>
</dd>

### -field <b>pfnExecuteBundle</b>

<dd>
<p>Execute bundle.</p>
</dd>

### -field <b>pfnExecuteIndirect</b>

<dd>
<p>Execute indirect.</p>
</dd>

### -field <b>pfnResourceBarrier</b>

<dd>
<p>Resource barrier.</p>
</dd>

### -field <b>pfnBlt</b>

<dd>
<p>Blt.</p>
</dd>

### -field <b>pfnPresent</b>

<dd>
<p>Present.</p>
</dd>

### -field <b>pfnBeginQuery</b>

<dd>
<p>Begin query.</p>
</dd>

### -field <b>pfnEndQuery</b>

<dd>
<p>End query.</p>
</dd>

### -field <b>pfnResolveQueryData</b>

<dd>
<p>Resolve query data.</p>
</dd>

### -field <b>pfnSetPredication</b>

<dd>
<p>Set predication.</p>
</dd>

### -field <b>pfnIaSetTopology</b>

<dd>
<p>Set topology</p>
</dd>

### -field <b>pfnRsSetViewports</b>

<dd>
<p>Set view ports.</p>
</dd>

### -field <b>pfnRsSetScissorRects</b>

<dd>
<p>Set scissor rectangles.</p>
</dd>

### -field <b>pfnOmSetBlendFactor</b>

<dd>
<p>Set blend factor.</p>
</dd>

### -field <b>pfnOmSetStencilRef</b>

<dd>
<p>Set stencil reference.</p>
</dd>

### -field <b>pfnSetPipelineState</b>

<dd>
<p>Set pipeline state.</p>
</dd>

### -field <b>pfnSetDescriptorHeaps</b>

<dd>
<p>Set descriptor heaps.</p>
</dd>

### -field <b>pfnSetComputeRootSignature</b>

<dd>
<p>Set compute root signature.</p>
</dd>

### -field <b>pfnSetGraphicsRootSignature</b>

<dd>
<p>Set graphics root signature.</p>
</dd>

### -field <b>pfnSetComputeRootDescriptorTable</b>

<dd>
<p>Set compute root descriptor table.</p>
</dd>

### -field <b>pfnSetGraphicsRootDescriptorTable</b>

<dd>
<p>Set graphics root descriptor table.</p>
</dd>

### -field <b>pfnSetComputeRoot32BitConstant</b>

<dd>
<p>Set compute root 32-bit constant.</p>
</dd>

### -field <b>pfnSetGraphicsRoot32BitConstant</b>

<dd>
<p>Set graphics root 32-bit constant.</p>
</dd>

### -field <b>pfnSetComputeRoot32BitConstants</b>

<dd>
<p>Set compute root 32-bit constants.</p>
</dd>

### -field <b>pfnSetGraphicsRoot32BitConstants</b>

<dd>
<p>Set graphics root 32-bit constants.</p>
</dd>

### -field <b>pfnSetComputeRootConstantBufferView</b>

<dd>
<p>Set compute root constant buffer view.</p>
</dd>

### -field <b>pfnSetGraphicsRootConstantBufferView</b>

<dd>
<p>Set graphics root constant buffer view.</p>
</dd>

### -field <b>pfnSetComputeRootShaderResourceView</b>

<dd>
<p>Set compute root shader resource view.</p>
</dd>

### -field <b>pfnSetGraphicsRootShaderResourceView</b>

<dd>
<p>Set graphics root shader resource view.</p>
</dd>

### -field <b>pfnSetComputeRootUnorderedAccessView</b>

<dd>
<p>Set compute root unordered access view.</p>
</dd>

### -field <b>pfnSetGraphicsRootUnorderedAccessView</b>

<dd>
<p>Set graphics root unordered access view.</p>
</dd>

### -field <b>pfnIASetIndexBuffer</b>

<dd>
<p>Set index buffer.</p>
</dd>

### -field <b>pfnIASetVertexBuffers</b>

<dd>
<p>Set vertex buffers.</p>
</dd>

### -field <b>pfnSOSetTargets</b>

<dd>
<p>Set targets.</p>
</dd>

### -field <b>pfnOMSetRenderTargets</b>

<dd>
<p>Set render targets.</p>
</dd>

### -field <b>pfnSetMarker</b>

<dd>
<p>Set marker.</p>
</dd>

### -field <b>pfnClearRootArguments</b>

<dd>
<p>Clear root arguments.</p>
</dd>

### -field <b>pfnAtomicCopyBufferRegion</b>

<dd>
<p>Atomic copy buffer region.</p>
</dd>

### -field <b>pfnOMSetDepthBounds</b>

<dd>
<p>Set depth bounds.</p>
</dd>

### -field <b>pfnSetSamplePositions</b>

<dd>
<p>Set sample positions.</p>
</dd>

### -field <b>pfnResourceResolveSubresourceRegion</b>

<dd>
<p>Resource resolve subresource region.</p>
</dd>

### -field <b>pfnSetProtectedResourceSession</b>

<dd>
<p>Set protected resource session.</p>
</dd>

### -field <b>pfnWriteBufferImmediate</b>

<dd>
<p>Write buffer immediate.</p>
</dd>

### -field <b>pfnSetViewInstanceMask</b>

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