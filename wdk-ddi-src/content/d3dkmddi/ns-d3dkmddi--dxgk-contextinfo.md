---
UID: NS.d3dkmddi._DXGK_CONTEXTINFO
title: DXGK_CONTEXTINFO
author: windows-driver-content
description: The DXGK_CONTEXTINFO structure describes a device context.
old-location: display\dxgk_contextinfo.htm
old-project: display
ms.assetid: 52c98ca7-8024-42d6-9001-1a7a69d24a95
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CONTEXTINFO, DXGK_CONTEXTINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_CONTEXTINFO
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGK_CONTEXTINFO structure



## -description
<p>The DXGK_CONTEXTINFO structure describes a device context.</p>


## -syntax

````
typedef struct _DXGK_CONTEXTINFO {
  UINT                  DmaBufferSize;
  UINT                  DmaBufferSegmentSet;
  UINT                  DmaBufferPrivateDataSize;
  UINT                  AllocationListSize;
  UINT                  PatchLocationListSize;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN7)
  UINT                  Reserved;
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
  DXGK_CONTEXTINFO_CAPS Caps;
  ULONG                 PagingCompanionNodeId;
#endif 
} DXGK_CONTEXTINFO;
````


## -struct-fields
<dl>

### -field DmaBufferSize

<dd>
<p>The size, in bytes, of the buffer of hardware commands that is sent through direct memory access (DMA) to the graphics processing unit (GPU).</p>
<p>The DMA buffer can grow and shrink after the context is created; however, the DMA buffer can never shrink smaller than the starting size that <b>DmaBufferSize</b> specifies.  </p>
</dd>

### -field DmaBufferSegmentSet

<dd>
<p> The identifiers of the segments where the DMA buffer should be made accessible to the GPU. </p>
</dd>

### -field DmaBufferPrivateDataSize

<dd>
<p>The size, in bytes, of the driver-resident private data structure that is associated with each DMA buffer. Memory for this private data structure is allocated from nonpaged pool. If the driver specifies zero in <b>DmaBufferPrivateDataSize</b>, no memory is allocated for the private data structure.</p>
<p>The private data structure that is associated with a DMA buffer is initialized to zero when the DMA buffer is created. During the lifetime of the DMA buffer, the video memory manager never accesses the private data structure that is associated with the DMA buffer. </p>
</dd>

### -field AllocationListSize

<dd>
<p>The starting number of elements in an array of allocations (that is, an array of <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-allocationlist.md">DXGK_ALLOCATIONLIST</a> structures). This number is the starting number of allocations that the driver requests to be in the <b>pAllocationList</b> members of the <a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-present.md">DXGKARG_PRESENT</a> and <a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-render.md">DXGKARG_RENDER</a> structures in calls to the driver's <a href="display.dxgkddipresent">DxgkDdiPresent</a> and <a href="display.dxgkddirender">DxgkDdiRender</a> functions, respectively.</p>
<p>The allocation list can grow and shrink after the context is created; however, the allocation list can never shrink smaller than the starting size that <b>AllocationListSize</b> specifies.  </p>
<div class="alert"><b>Note</b>  If <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-createcontextflags.md">DXGK_CREATECONTEXTFLAGS</a>.<b>GdiContext</b>  is set to 1, meaning that the context is created as a GDI-specific context,  <b>AllocationListSize</b> must be set to a value of 256.</div>
<div> </div>
</dd>

### -field PatchLocationListSize

<dd>
<p> The starting number of elements in an array of patch locations (that is, an array of <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-patchlocationlist.md">D3DDDI_PATCHLOCATIONLIST</a> structures) for the device in user mode and kernel mode. This number is the starting number of patch locations that the driver requests to be in the <b>pPatchLocationListIn</b> members of the <a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-render.md">DXGKARG_RENDER</a> structures in calls to its <a href="display.dxgkddirender">DxgkDdiRender</a> function.</p>
<p>The patch-location list can grow and shrink after the context is created; however, the patch-location list can never shrink smaller than the starting size that <b>PatchLocationListSize</b> specifies. </p>
</dd>

### -field Reserved

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>This member is available beginning with Windows 7.</p>
</dd>

### -field Caps

<dd>
<p>Describes optional features supported by the context.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field PagingCompanionNodeId

<dd>
<p>Specifies the zero-based engine identifier of the engine to use for this context paging companion.</p>
<p>Supported starting with Windows 10.</p>
</dd>
</dl>

## -remarks
<p>A display miniport driver specifies values for the <b>DmaBufferSize</b> and <b>AllocationListSize</b> members to guarantee that:</p>

<p>The Microsoft DirectX graphics subsystem can use only one direct memory access (DMA) buffer to display (by using the display miniport driver's <a href="display.dxgkddipresent">DxgkDdiPresent</a> function) at least one <a href="display.rect">RECT</a> structure for all scenarios.</p>

<p>The sizes of DMA and allocation-list buffers are large enough to hold at least one command that cannot be split across multiple buffers.</p>

<p>The sizes of DMA and allocation-list buffers are large enough to avoid setup and DMA overhead. </p>

<p>The display miniport driver can specify only aperture segments in the <b>DmaBufferSegmentSet</b> member; if the driver specifies a memory segment, a context-creation failure occurs. </p>

<p>If the driver sets <b>DmaBufferSegmentSet</b> to 0, the video memory manager allocates contiguous paged-locked memory, which is mapped write-combined memory, for the DMA buffers. Therefore, the GPU must access DMA buffers by using PCI cycles on computers where AGP transfers that occur outside the AGP aperture are not permitted.</p>

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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-patchlocationlist.md">D3DDDI_PATCHLOCATIONLIST</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-allocationlist.md">DXGK_ALLOCATIONLIST</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-createcontextflags.md">DXGK_CREATECONTEXTFLAGS</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-createcontext.md">DXGKARG_CREATECONTEXT</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-present.md">DXGKARG_PRESENT</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-render.md">DXGKARG_RENDER</a>
</dt>
<dt>
<a href="display.dxgkddipresent">DxgkDdiPresent</a>
</dt>
<dt>
<a href="display.dxgkddirender">DxgkDdiRender</a>
</dt>
<dt>
<a href="display.rect">RECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_CONTEXTINFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
