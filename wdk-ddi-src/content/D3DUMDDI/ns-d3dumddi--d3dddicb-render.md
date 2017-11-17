---
UID: NS.d3dumddi._D3DDDICB_RENDER
title: D3DDDICB_RENDER
author: windows-driver-content
description: The D3DDDICB_RENDER structure describes the current command buffer to be rendered.
old-location: display\d3dddicb_render.htm
ms.assetid: 7a2bf1a8-d416-46bc-a9ba-9122407ea2a2
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICB_RENDER
req.alt-loc: d3dumddi.h
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
ms.keywords: D3DDDICB_RENDER, D3DDDICB_RENDER
req.iface: 
---

# D3DDDICB_RENDER structure



## -description
<p>The D3DDDICB_RENDER structure describes the current command buffer to be rendered.</p>


## -syntax

````
typedef struct _D3DDDICB_RENDER {
  UINT                     CommandLength;
  UINT                     CommandOffset;
  UINT                     NumAllocations;
  UINT                     NumPatchLocations;
  VOID                     *pNewCommandBuffer;
  UINT                     NewCommandBufferSize;
  D3DDDI_ALLOCATIONLIST    *pNewAllocationList;
  UINT                     NewAllocationListSize;
  D3DDDI_PATCHLOCATIONLIST *pNewPatchLocationList;
  UINT                     NewPatchLocationListSize;
  D3DDDICB_RENDERFLAGS     Flags;
  HANDLE                   hContext;
  UINT                     BroadcastContextCount;
  HANDLE                   BroadcastContext[D3DDDI_MAX_BROADCAST_CONTEXT];
  ULONG                    QueuedBufferCount;
#if (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WIN7)
  D3DGPU_VIRTUAL_ADDRESS   NewCommandBuffer;
  VOID                     *pPrivateDriverData;
  UINT                     PrivateDriverDataSize;
#endif 
} D3DDDICB_RENDER;
````


## -struct-fields
<dl>

### -field <b>CommandLength</b>

<dd>
<p>[in] The size, in bytes, of the command buffer, starting from offset zero.</p>
</dd>

### -field <b>CommandOffset</b>

<dd>
<p>[in] The offset, in bytes, to the first command in the command buffer.</p>
</dd>

### -field <b>NumAllocations</b>

<dd>
<p>[in] The number of elements in the allocation list.</p>
</dd>

### -field <b>NumPatchLocations</b>

<dd>
<p>[in] The number of elements in the patch-location list.</p>
</dd>

### -field <b>pNewCommandBuffer</b>

<dd>
<p>[out] A pointer to a command buffer that the user-mode display driver receives to use in its next call to the <a href="https://msdn.microsoft.com/f242162e-6237-469c-b178-5a51dcf69e32">pfnRenderCb</a> function.</p>
</dd>

### -field <b>NewCommandBufferSize</b>

<dd>
<p>[in/out] The size, in bytes, that the user-mode display driver requests for the next command buffer.</p>
<p>The driver receives the size, in bytes, of the next command buffer to use. </p>
</dd>

### -field <b>pNewAllocationList</b>

<dd>
<p>[out] An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544375">D3DDDI_ALLOCATIONLIST</a> structures that the user-mode display driver receives to use as the allocation list in its next call to the <a href="https://msdn.microsoft.com/f242162e-6237-469c-b178-5a51dcf69e32">pfnRenderCb</a> function.</p>
</dd>

### -field <b>NewAllocationListSize</b>

<dd>
<p>[in/out] The number of elements that the user-mode display driver requests for the next allocation list. </p>
<p>The driver receives the number of elements for the allocation list that will be available when the next command buffer is submitted.</p>
</dd>

### -field <b>pNewPatchLocationList</b>

<dd>
<p>[out] An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544630">D3DDDI_PATCHLOCATIONLIST</a> structures that the user-mode display driver receives to use as the patch-location list in its next call to the <a href="https://msdn.microsoft.com/f242162e-6237-469c-b178-5a51dcf69e32">pfnRenderCb</a> function.</p>
</dd>

### -field <b>NewPatchLocationListSize</b>

<dd>
<p>[in/out] The number of elements that the user-mode display driver requests for the next patch-location list.</p>
<p>The driver receives the number of elements for the patch-location list that will be available when the next command buffer is submitted. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544247">D3DDDICB_RENDERFLAGS</a> structure that indicates information about a command buffer to be rendered.</p>
</dd>

### -field <b>hContext</b>

<dd>
<p>[in] A handle to the context that the driver submits the rendering operation to. The user-mode display driver previously created this context by calling the <a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a> function. </p>
</dd>

### -field <b>BroadcastContextCount</b>

<dd>
<p>[in] The number of additional contexts in the array that the <b>BroadcastContext</b> member specifies.</p>
</dd>

### -field <b>BroadcastContext</b>

<dd>
<p>[in] An array of handles to the additional contexts to broadcast the current command buffer to. The D3DDDI_MAX_BROADCAST_CONTEXT constant, which is defined as 64, defines the maximum number of additional contexts that the user-mode display driver can broadcast the current command buffer to.</p>
<p>The original context that the <b>hContext</b> member specifies and that owns the command buffer is not an element in the <b>BroadcastContext</b> array. For example, if the <b>BroadcastContext</b> array contains one element, the user-mode display driver sends the command buffer to the owning context (<b>hContext</b>) and broadcasts to that one additional context. </p>
</dd>

### -field <b>QueuedBufferCount</b>

<dd>
<p>[out] The number of DMA buffers that are queued to the context that the <b>hContext</b> member specifies after the current submission occurs. </p>
</dd>

### -field <b>NewCommandBuffer</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>This member is available beginning with Windows 7.</p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>[in] This member is reserved and should be set to zero.</p>
<p>This member is available beginning with Windows 7.</p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p>[in] This member is reserved and should be set to zero.</p>
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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544375">D3DDDI_ALLOCATIONLIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544630">D3DDDI_PATCHLOCATIONLIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544247">D3DDDICB_RENDERFLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f242162e-6237-469c-b178-5a51dcf69e32">pfnRenderCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_RENDER structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
