---
UID: NS.d3dkmthk._D3DKMT_RENDER
title: D3DKMT_RENDER
author: windows-driver-content
description: The D3DKMT_RENDER structure describes the current command buffer to be rendered.
old-location: display\d3dkmt_render.htm
ms.assetid: 8e45c4cb-3635-403b-8a91-71af6605c3be
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_RENDER
req.alt-loc: d3dkmthk.h
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
ms.keywords: D3DKMT_RENDER, D3DKMT_RENDER
req.iface: 
---

# D3DKMT_RENDER structure



## -description
<p>The D3DKMT_RENDER structure describes the current command buffer to be rendered.</p>


## -syntax

````
typedef struct _D3DKMT_RENDER {
  union {
    D3DKMT_HANDLE hDevice;
    D3DKMT_HANDLE hContext;
  };
  UINT                     CommandOffset;
  UINT                     CommandLength;
  UINT                     AllocationCount;
  UINT                     PatchLocationCount;
  VOID                     *pNewCommandBuffer;
  UINT                     NewCommandBufferSize;
  D3DDDI_ALLOCATIONLIST    *pNewAllocationList;
  UINT                     NewAllocationListSize;
  D3DDDI_PATCHLOCATIONLIST *pNewPatchLocationList;
  UINT                     NewPatchLocationListSize;
  D3DKMT_RENDERFLAGS       Flags;
  ULONGLONG                PresentHistoryToken;
  ULONG                    BroadcastContextCount;
  D3DKMT_HANDLE            BroadcastContext[D3DDDI_MAX_BROADCAST_CONTEXT];
  ULONG                    QueuedBufferCount;
  D3DGPU_VIRTUAL_ADDRESS   NewCommandBuffer;
  VOID                     *pPrivateDriverData;
  UINT                     PrivateDriverDataSize;
} D3DKMT_RENDER;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the device that the command buffer is rendered to. A device handle is supplied to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547145">D3DKMTRender</a> function in the union that D3DKMT_RENDER contains for compatibility with Microsoft Direct3D version 10.</p>
</dd>

### -field <b>hContext</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the device context that the command buffer is rendered to.</p>
</dd>

### -field <b>CommandOffset</b>

<dd>
<p>[in] The offset, in bytes, to the first command in the command buffer.</p>
</dd>

### -field <b>CommandLength</b>

<dd>
<p>[in] The size, in bytes, of the command buffer starting from offset zero.</p>
</dd>

### -field <b>AllocationCount</b>

<dd>
<p>[in] The number of elements in the submitted allocation list.</p>
</dd>

### -field <b>PatchLocationCount</b>

<dd>
<p>[in] The number of elements in the submitted patch-location list.</p>
</dd>

### -field <b>pNewCommandBuffer</b>

<dd>
<p>[out] A pointer to a command buffer that the OpenGL ICD receives to use in its next call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547145">D3DKMTRender</a> function. The driver must always update its pointer to the command buffer after any call to <b>D3DKMTRender</b> regardless of whether the call is successful.</p>
<p>Supported in Windows 7 and later versions:</p>
<p>[in] A pointer to the command buffer to be rendered if the <b>RenderKm</b> flag is set in the <b>Flags</b> member. </p>
</dd>

### -field <b>NewCommandBufferSize</b>

<dd>
<p>[in/out] The size, in bytes, that the OpenGL ICD requests for the next command buffer if the <b>ResizeCommandBuffer</b> bit-field flag is specified in the <b>Flags</b> member. If <b>ResizeCommandBuffer</b> is not specified, the value in <b>NewCommandBufferSize</b> is ignored. On output, the driver receives the size, in bytes, of the next command buffer to use.</p>
<p>Depending on current memory conditions the output size might not match the input size. </p>
</dd>

### -field <b>pNewAllocationList</b>

<dd>
<p>[out] An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544375">D3DDDI_ALLOCATIONLIST</a> structures that the OpenGL ICD receives to use as the allocation list in its next call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547145">D3DKMTRender</a> function. The driver must always update its pointer to the allocation list after any call to <b>D3DKMTRender</b> regardless of whether the call is successful.</p>
<p>Supported in Windows 7 and later versions:</p>
<p>[in] A pointer to the allocation list to be rendered if the <b>RenderKm</b> flag is set in the <b>Flags</b> member. </p>
</dd>

### -field <b>NewAllocationListSize</b>

<dd>
<p>[in/out] The number of elements that the OpenGL ICD requests for the next allocation list if the <b>ResizeAllocationList</b> bit-field flag is specified in the <b>Flags</b> member. If <b>ResizeAllocationList</b> is not specified, the value in <b>NewAllocationListSize</b> is ignored. On output, the driver receives the number of elements that will be available in an array of allocations when the next command buffer is submitted.</p>
<p>Depending on current memory conditions the output size might not match the input size. </p>
</dd>

### -field <b>pNewPatchLocationList</b>

<dd>
<p>[out] An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544630">D3DDDI_PATCHLOCATIONLIST</a> structures that the OpenGL ICD receives to use as the patch-location list in its next call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547145">D3DKMTRender</a> function. The driver must always update its pointer to the patch-location list after any call to <b>D3DKMTRender</b> regardless of whether the call is successful.</p>
</dd>

### -field <b>NewPatchLocationListSize</b>

<dd>
<p>[in/out] The number of elements that the OpenGL ICD requests for the next patch-location list if the <b>ResizePatchLocationList</b> bit-field flag is specified in the <b>Flags</b> member. If <b>ResizePatchLocationList</b> is not specified, the value in <b>NewPatchLocationListSize</b> is ignored. On output, the driver receives the number of elements that will be available in an array of patch locations when the next command buffer is submitted.</p>
<p>Depending on current memory conditions the output size might not match the input size.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff548244">D3DKMT_RENDERFLAGS</a> structure that indicates the type of command buffer, in bit-field flags, to be rendered.</p>
</dd>

### -field <b>PresentHistoryToken</b>

<dd>
<p>[in] The present history token for redirected calls to the display miniport driver's <a href="https://msdn.microsoft.com/1a46b129-1e78-44e6-a609-59eab206692b">DxgkDdiPresent</a> function.</p>
<p>A <i>present history token</i> is a data packet that the rendering app submits to inform the Desktop Window Manager (DWM) that rendering is complete and the swap chain back buffer is ready to be presented.</p>
</dd>

### -field <b>BroadcastContextCount</b>

<dd>
<p>[in] The number of additional contexts in the array that <b>BroadcastContext</b> specifies.</p>
</dd>

### -field <b>BroadcastContext</b>

<dd>
<p>[in] An array of D3DKMT_HANDLE data types that represent kernel-mode handles to the additional contexts to broadcast the current command buffer to. The D3DDDI_MAX_BROADCAST_CONTEXT constant, which is defined as 64, defines the maximum number of contexts that the OpenGL ICD can broadcast the current command buffer to.</p>
<p>The original context that the <b>hContext</b> member specifies and that owns the command buffer is not an element in the <b>BroadcastContext</b> array. For example, if the <b>BroadcastContext</b> array contains one element, the OpenGL ICD sends the command buffer to the owning context (<b>hContext</b>) and broadcasts to that one additional context. </p>
</dd>

### -field <b>QueuedBufferCount</b>

<dd>
<p>[out] The number of DMA buffers that are queued to the context that the <b>hContext</b> member specifies after the submission. </p>
</dd>

### -field <b>NewCommandBuffer</b>

<dd>
<p>[out] A pointer to a command buffer that the OpenGL ICD receives to use in its next call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547145">D3DKMTRender</a> function. The driver must always update its pointer to the command buffer after any call to <b>D3DKMTRender</b> regardless of whether the call is successful.</p>
<p>Supported in Windows 7 and later versions:</p>
<p>[in] A pointer to the command buffer to be rendered if the <b>RenderKm</b> flag is set in the <b>Flags</b> member. </p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>This member is available beginning with Windows 7.</p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>This member is available beginning with Windows 7.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548244">D3DKMT_RENDERFLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547145">D3DKMTRender</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1a46b129-1e78-44e6-a609-59eab206692b">DxgkDdiPresent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_RENDER structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
