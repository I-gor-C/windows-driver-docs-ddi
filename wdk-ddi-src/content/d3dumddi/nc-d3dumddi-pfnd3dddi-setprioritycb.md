---
UID: NC.d3dumddi.PFND3DDDI_SETPRIORITYCB
title: PFND3DDDI_SETPRIORITYCB
author: windows-driver-content
description: The pfnSetPriorityCb function sets the priority level of a resource or list of allocations.
old-location: display\pfnsetprioritycb.htm
old-project: display
ms.assetid: 1812cb0f-9232-4813-9c7b-74c9fa4d03cf
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnSetPriorityCb
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
req.iface: 
---

# PFND3DDDI_SETPRIORITYCB callback



## -description
<p>The <i>pfnSetPriorityCb</i> function sets the priority level of a resource or list of allocations.</p>


## -prototype

````
PFND3DDDI_SETPRIORITYCB pfnSetPriorityCb;

__checkReturn HRESULT APIENTRY CALLBACK pfnSetPriorityCb(
  _In_ HANDLE               hDevice,
  _In_ D3DDDICB_SETPRIORITY *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544265">D3DDDICB_SETPRIORITY</a> structure that describes the priority level to set a resource or list of allocations to.</p>
</dd>
</dl>

## -returns
<p><i>pfnSetPriorityCb</i> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The priority level was successfully set.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p>

<p> </p>

<p>This function might also return other HRESULT values.

</p>

## -remarks
<p>The user-mode display driver can call the <i>pfnSetPriorityCb</i> function to set the priority of the underlying resource or list of allocations. If the priority level of a resource is set, all of the allocations that belong to the resource are set to the specified priority level. Typically, the user-mode display driver sets the priority of a resource or list of allocations after the Microsoft Direct3D runtime calls the user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setpriority.md">SetPriority</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff569657">SetResourcePriorityDXGI</a> function to set the eviction-from-memory priority for a resource. However, the user-mode display driver can set the priority of allocations at any time. </p>

<p>After an application requests to set the priority level of a surface, the user-mode display driver should set the appropriate resource or list of allocations to the priority level that is specified by the application. </p>

<p>An allocation priority defines both the likelihood that the allocation remains resident and the likelihood of how hard the video memory manager will try to respect the driver's preference for the placement of the allocation. The following priority levels are defined in the D3dukmdt.h header file:</p>

<p></p><dl>
<dt><a id="D3DDDI_ALLOCATIONPRIORITY_MINIMUM__0x28000000_"></a><a id="d3dddi_allocationpriority_minimum__0x28000000_"></a><a id="D3DDDI_ALLOCATIONPRIORITY_MINIMUM__0X28000000_"></a>D3DDDI_ALLOCATIONPRIORITY_MINIMUM (0x28000000)</dt>
<dd>
<p>Marks the allocation as unused and for eviction immediately. The allocation should be evicted as soon as another allocation requires the resource that the allocation occupies.</p>
<p>If an allocation will not be used for a while, the driver marks the allocation as unused at the soonest opportunity. Note that changing allocation priority is not a queued operation; that is, the change is effective immediately. Changing the priority of an allocation that has a queued reference can cause the video memory manager to evict the allocation, then bring the allocation back, and then evict the allocation again. </p>
</dd>
<dt><a id="D3DDDI_ALLOCATIONPRIORITY_LOW__0x50000000_"></a><a id="d3dddi_allocationpriority_low__0x50000000_"></a><a id="D3DDDI_ALLOCATIONPRIORITY_LOW__0X50000000_"></a>D3DDDI_ALLOCATIONPRIORITY_LOW (0x50000000)</dt>
<dd>
<p>Marks the priority of the allocation as low.</p>
<p>The placement of the allocation is not critical, and the video memory manager performs minimal work to find a location for the allocation. For example, if a GPU can render with a vertex buffer from either local or non-local memory with little difference in performance, the driver should mark that vertex buffer as low priority. Marking the buffer as low priority allows other more critical allocations (for example, allocations for a render target or texture) to occupy the faster memory. </p>
</dd>
<dt><a id="D3DDDI_ALLOCATIONPRIORITY_NORMAL__0x78000000_"></a><a id="d3dddi_allocationpriority_normal__0x78000000_"></a><a id="D3DDDI_ALLOCATIONPRIORITY_NORMAL__0X78000000_"></a>D3DDDI_ALLOCATIONPRIORITY_NORMAL (0x78000000)</dt>
<dd>
<p>Marks the priority of the allocation as normal.</p>
<p>The placement of the allocation is important, but not critical, for performance. The video memory manager should try to place the allocation that is marked as normal in the allocation's preferred location instead of a low-priority allocation. </p>
<p>Typically, textures are marked as normal. </p>
</dd>
<dt><a id="D3DDDI_ALLOCATIONPRIORITY_HIGH__0xa0000000_"></a><a id="d3dddi_allocationpriority_high__0xa0000000_"></a><a id="D3DDDI_ALLOCATIONPRIORITY_HIGH__0XA0000000_"></a>D3DDDI_ALLOCATIONPRIORITY_HIGH (0xa0000000)</dt>
<dd>
<p>Marks the priority of the allocation as high.</p>
<p>The placement of the allocation is critical for performance. The video memory manager should try to place the allocation that is marked as high in the allocation's preferred location instead of a low-priority or normal-priority allocation. </p>
<p>Typically, render targets are marked as high.</p>
<p>Beginning with Windows 8, when the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-createcontextallocation.md">DxgkCbCreateContextAllocation</a>  function is called, the Microsoft DirectX graphics subsystem sets this allocation priority value.</p>
</dd>
<dt><a id="D3DDDI_ALLOCATIONPRIORITY_MAXIMUM__0xc8000000_"></a><a id="d3dddi_allocationpriority_maximum__0xc8000000_"></a><a id="D3DDDI_ALLOCATIONPRIORITY_MAXIMUM__0XC8000000_"></a>D3DDDI_ALLOCATIONPRIORITY_MAXIMUM (0xc8000000)</dt>
<dd>
<p>Marks the priority of the allocation as soft-pinned. A soft-pinned allocation is evicted from memory only if there is no other way of resolving the memory requirement of a DMA buffer. The video memory manager attempts to split a DMA buffer to its minimum size and evict all other nonpinned and non soft-pinned allocations before evicting a soft-pinned allocation. This level of priority should be used only for applications that require no errors.</p>
</dd>
</dl><p>Marks the allocation as unused and for eviction immediately. The allocation should be evicted as soon as another allocation requires the resource that the allocation occupies.</p>

<p>If an allocation will not be used for a while, the driver marks the allocation as unused at the soonest opportunity. Note that changing allocation priority is not a queued operation; that is, the change is effective immediately. Changing the priority of an allocation that has a queued reference can cause the video memory manager to evict the allocation, then bring the allocation back, and then evict the allocation again. </p>

<p>Marks the priority of the allocation as low.</p>

<p>The placement of the allocation is not critical, and the video memory manager performs minimal work to find a location for the allocation. For example, if a GPU can render with a vertex buffer from either local or non-local memory with little difference in performance, the driver should mark that vertex buffer as low priority. Marking the buffer as low priority allows other more critical allocations (for example, allocations for a render target or texture) to occupy the faster memory. </p>

<p>Marks the priority of the allocation as normal.</p>

<p>The placement of the allocation is important, but not critical, for performance. The video memory manager should try to place the allocation that is marked as normal in the allocation's preferred location instead of a low-priority allocation. </p>

<p>Typically, textures are marked as normal. </p>

<p>Marks the priority of the allocation as high.</p>

<p>The placement of the allocation is critical for performance. The video memory manager should try to place the allocation that is marked as high in the allocation's preferred location instead of a low-priority or normal-priority allocation. </p>

<p>Typically, render targets are marked as high.</p>

<p>Beginning with Windows 8, when the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-createcontextallocation.md">DxgkCbCreateContextAllocation</a>  function is called, the Microsoft DirectX graphics subsystem sets this allocation priority value.</p>

<p>Marks the priority of the allocation as soft-pinned. A soft-pinned allocation is evicted from memory only if there is no other way of resolving the memory requirement of a DMA buffer. The video memory manager attempts to split a DMA buffer to its minimum size and evict all other nonpinned and non soft-pinned allocations before evicting a soft-pinned allocation. This level of priority should be used only for applications that require no errors.</p>

<p>The driver can use priority levels other than the preceding defined values when appropriate. For example, marking an allocation with a priority level of 0x78000001 indicates that the allocation is slightly above normal. </p>

<p>The following code example shows how to set priority level.</p>

<p>The user-mode display driver can call the <i>pfnSetPriorityCb</i> function to set the priority of the underlying resource or list of allocations. If the priority level of a resource is set, all of the allocations that belong to the resource are set to the specified priority level. Typically, the user-mode display driver sets the priority of a resource or list of allocations after the Microsoft Direct3D runtime calls the user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setpriority.md">SetPriority</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff569657">SetResourcePriorityDXGI</a> function to set the eviction-from-memory priority for a resource. However, the user-mode display driver can set the priority of allocations at any time. </p>

<p>After an application requests to set the priority level of a surface, the user-mode display driver should set the appropriate resource or list of allocations to the priority level that is specified by the application. </p>

<p>An allocation priority defines both the likelihood that the allocation remains resident and the likelihood of how hard the video memory manager will try to respect the driver's preference for the placement of the allocation. The following priority levels are defined in the D3dukmdt.h header file:</p>

<p></p><dl>
<dt><a id="D3DDDI_ALLOCATIONPRIORITY_MINIMUM__0x28000000_"></a><a id="d3dddi_allocationpriority_minimum__0x28000000_"></a><a id="D3DDDI_ALLOCATIONPRIORITY_MINIMUM__0X28000000_"></a>D3DDDI_ALLOCATIONPRIORITY_MINIMUM (0x28000000)</dt>
<dd>
<p>Marks the allocation as unused and for eviction immediately. The allocation should be evicted as soon as another allocation requires the resource that the allocation occupies.</p>
<p>If an allocation will not be used for a while, the driver marks the allocation as unused at the soonest opportunity. Note that changing allocation priority is not a queued operation; that is, the change is effective immediately. Changing the priority of an allocation that has a queued reference can cause the video memory manager to evict the allocation, then bring the allocation back, and then evict the allocation again. </p>
</dd>
<dt><a id="D3DDDI_ALLOCATIONPRIORITY_LOW__0x50000000_"></a><a id="d3dddi_allocationpriority_low__0x50000000_"></a><a id="D3DDDI_ALLOCATIONPRIORITY_LOW__0X50000000_"></a>D3DDDI_ALLOCATIONPRIORITY_LOW (0x50000000)</dt>
<dd>
<p>Marks the priority of the allocation as low.</p>
<p>The placement of the allocation is not critical, and the video memory manager performs minimal work to find a location for the allocation. For example, if a GPU can render with a vertex buffer from either local or non-local memory with little difference in performance, the driver should mark that vertex buffer as low priority. Marking the buffer as low priority allows other more critical allocations (for example, allocations for a render target or texture) to occupy the faster memory. </p>
</dd>
<dt><a id="D3DDDI_ALLOCATIONPRIORITY_NORMAL__0x78000000_"></a><a id="d3dddi_allocationpriority_normal__0x78000000_"></a><a id="D3DDDI_ALLOCATIONPRIORITY_NORMAL__0X78000000_"></a>D3DDDI_ALLOCATIONPRIORITY_NORMAL (0x78000000)</dt>
<dd>
<p>Marks the priority of the allocation as normal.</p>
<p>The placement of the allocation is important, but not critical, for performance. The video memory manager should try to place the allocation that is marked as normal in the allocation's preferred location instead of a low-priority allocation. </p>
<p>Typically, textures are marked as normal. </p>
</dd>
<dt><a id="D3DDDI_ALLOCATIONPRIORITY_HIGH__0xa0000000_"></a><a id="d3dddi_allocationpriority_high__0xa0000000_"></a><a id="D3DDDI_ALLOCATIONPRIORITY_HIGH__0XA0000000_"></a>D3DDDI_ALLOCATIONPRIORITY_HIGH (0xa0000000)</dt>
<dd>
<p>Marks the priority of the allocation as high.</p>
<p>The placement of the allocation is critical for performance. The video memory manager should try to place the allocation that is marked as high in the allocation's preferred location instead of a low-priority or normal-priority allocation. </p>
<p>Typically, render targets are marked as high.</p>
<p>Beginning with Windows 8, when the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-createcontextallocation.md">DxgkCbCreateContextAllocation</a>  function is called, the Microsoft DirectX graphics subsystem sets this allocation priority value.</p>
</dd>
<dt><a id="D3DDDI_ALLOCATIONPRIORITY_MAXIMUM__0xc8000000_"></a><a id="d3dddi_allocationpriority_maximum__0xc8000000_"></a><a id="D3DDDI_ALLOCATIONPRIORITY_MAXIMUM__0XC8000000_"></a>D3DDDI_ALLOCATIONPRIORITY_MAXIMUM (0xc8000000)</dt>
<dd>
<p>Marks the priority of the allocation as soft-pinned. A soft-pinned allocation is evicted from memory only if there is no other way of resolving the memory requirement of a DMA buffer. The video memory manager attempts to split a DMA buffer to its minimum size and evict all other nonpinned and non soft-pinned allocations before evicting a soft-pinned allocation. This level of priority should be used only for applications that require no errors.</p>
</dd>
</dl><p>Marks the allocation as unused and for eviction immediately. The allocation should be evicted as soon as another allocation requires the resource that the allocation occupies.</p>

<p>If an allocation will not be used for a while, the driver marks the allocation as unused at the soonest opportunity. Note that changing allocation priority is not a queued operation; that is, the change is effective immediately. Changing the priority of an allocation that has a queued reference can cause the video memory manager to evict the allocation, then bring the allocation back, and then evict the allocation again. </p>

<p>Marks the priority of the allocation as low.</p>

<p>The placement of the allocation is not critical, and the video memory manager performs minimal work to find a location for the allocation. For example, if a GPU can render with a vertex buffer from either local or non-local memory with little difference in performance, the driver should mark that vertex buffer as low priority. Marking the buffer as low priority allows other more critical allocations (for example, allocations for a render target or texture) to occupy the faster memory. </p>

<p>Marks the priority of the allocation as normal.</p>

<p>The placement of the allocation is important, but not critical, for performance. The video memory manager should try to place the allocation that is marked as normal in the allocation's preferred location instead of a low-priority allocation. </p>

<p>Typically, textures are marked as normal. </p>

<p>Marks the priority of the allocation as high.</p>

<p>The placement of the allocation is critical for performance. The video memory manager should try to place the allocation that is marked as high in the allocation's preferred location instead of a low-priority or normal-priority allocation. </p>

<p>Typically, render targets are marked as high.</p>

<p>Beginning with Windows 8, when the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-createcontextallocation.md">DxgkCbCreateContextAllocation</a>  function is called, the Microsoft DirectX graphics subsystem sets this allocation priority value.</p>

<p>Marks the priority of the allocation as soft-pinned. A soft-pinned allocation is evicted from memory only if there is no other way of resolving the memory requirement of a DMA buffer. The video memory manager attempts to split a DMA buffer to its minimum size and evict all other nonpinned and non soft-pinned allocations before evicting a soft-pinned allocation. This level of priority should be used only for applications that require no errors.</p>

<p>The driver can use priority levels other than the preceding defined values when appropriate. For example, marking an allocation with a priority level of 0x78000001 indicates that the allocation is slightly above normal. </p>

<p>The following code example shows how to set priority level.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544265">D3DDDICB_SETPRIORITY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544512">D3DDDI_DEVICECALLBACKS</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-createcontextallocation.md">DxgkCbCreateContextAllocation</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setpriority.md">SetPriority</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569657">SetResourcePriorityDXGI</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETPRIORITYCB callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
