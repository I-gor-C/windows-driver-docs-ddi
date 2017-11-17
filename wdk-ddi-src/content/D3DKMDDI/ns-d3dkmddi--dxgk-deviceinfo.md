---
UID: NS.d3dkmddi._DXGK_DEVICEINFO
title: DXGK_DEVICEINFO
author: windows-driver-content
description: The DXGK_DEVICEINFO structure describes parameters that the Microsoft DirectX graphics kernel subsystem requires from the display miniport driver.
old-location: display\dxgk_deviceinfo.htm
ms.assetid: 8d941bee-2473-43f8-a157-002708b247aa
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_DEVICEINFO
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
ms.keywords: DXGK_DEVICEINFO, DXGK_DEVICEINFO
req.iface: 
---

# DXGK_DEVICEINFO structure



## -description
<p>The DXGK_DEVICEINFO structure describes parameters that the Microsoft DirectX graphics kernel subsystem requires from the display miniport driver.</p>


## -syntax

````
typedef struct _DXGK_DEVICEINFO {
  UINT                 DmaBufferSize;
  UINT                 DmaBufferSegmentSet;
  UINT                 DmaBufferPrivateDataSize;
  UINT                 AllocationListSize;
  UINT                 PatchLocationListSize;
  DXGK_DEVICEINFOFLAGS Flags;
} DXGK_DEVICEINFO;
````


## -struct-fields
<dl>

### -field <b>DmaBufferSize</b>

<dd>
<p>[out] The size, in bytes, of the buffer of hardware commands that is sent through direct memory access (DMA) to the hardware.</p>
<p>The DMA buffer can grow and shrink after the device is created; however, the DMA buffer can never shrink smaller than the starting size that <b>DmaBufferSize</b> specifies. </p>
</dd>

### -field <b>DmaBufferSegmentSet</b>

<dd>
<p>[out] The identifiers of the segments where the DMA buffers should be made accessible to the graphics processing unit (GPU). </p>
</dd>

### -field <b>DmaBufferPrivateDataSize</b>

<dd>
<p>[out] The size, in bytes, of the driver-resident private data structure that is associated with each DMA buffer. Memory for this private data structure is allocated from nonpaged pool. If the driver specifies zero in <b>DmaBufferPrivateDataSize</b>, no memory is allocated for the private data structure.</p>
<p>The private data structure that is associated with a DMA buffer is initialized to zero when the DMA buffer is created. During the lifetime of the DMA buffer, the video memory manager never accesses the private data structure that is associated with the DMA buffer.</p>
</dd>

### -field <b>AllocationListSize</b>

<dd>
<p>[out] The starting number of elements in an array of allocations (that is, an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff560975">DXGK_ALLOCATIONLIST</a> structures). This number is the starting number of allocations that the driver requests to be in the <b>pAllocationList</b> members of <a href="https://msdn.microsoft.com/library/windows/hardware/ff557618">DXGKARG_PRESENT</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff557648">DXGKARG_RENDER</a> structures in calls to the driver's <a href="https://msdn.microsoft.com/1a46b129-1e78-44e6-a609-59eab206692b">DxgkDdiPresent</a> and <a href="https://msdn.microsoft.com/fd634768-5e1e-4f40-82fd-5ef69148c3d7">DxgkDdiRender</a> functions. </p>
<p>The allocation list can grow and shrink after the device is created; however, the allocation list can never shrink smaller than the starting size that <b>AllocationListSize</b> specifies. </p>
</dd>

### -field <b>PatchLocationListSize</b>

<dd>
<p>[out] The starting number of elements in an array of patch locations (that is, an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544630">D3DDDI_PATCHLOCATIONLIST</a> structures) for the device in user mode and kernel mode. This number is the starting number of patch locations that the driver requests to be in the <b>pPatchLocationListIn</b> members of <a href="https://msdn.microsoft.com/library/windows/hardware/ff557648">DXGKARG_RENDER</a> structures in calls to its <a href="https://msdn.microsoft.com/fd634768-5e1e-4f40-82fd-5ef69148c3d7">DxgkDdiRender</a> function. </p>
<p>The patch-location list can grow and shrink after the device is created; however, the patch-location list can never shrink smaller than the starting size that <b>PatchLocationListSize</b> specifies. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561049">DXGK_DEVICEINFOFLAGS</a> structure that identifies, in bit-field flags, information about the device.</p>
</dd>
</dl>

## -remarks
<p>The display miniport driver specifies values for the <b>DmaBufferSize</b> and <b>AllocationListSize</b> members to guarantee the following:</p>

<p>The DirectX graphics subsystem can use only one DMA buffer to display (by using the display miniport driver's <a href="https://msdn.microsoft.com/1a46b129-1e78-44e6-a609-59eab206692b">DxgkDdiPresent</a> function) at least one <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure for all scenarios.</p>

<p>The sizes of DMA and allocation-list buffers are large enough to hold at least one command that cannot be split across multiple buffers.</p>

<p>The sizes of DMA and allocation-list buffers are large enough to avoid setup and DMA overhead. </p>

<p>The display miniport driver can specify only aperture segments in the <b>DmaBufferSegmentSet</b> member; if the driver specifies a memory segment, a device-creation failure occurs. </p>

<p>If the driver sets <b>DmaBufferSegmentSet</b> to 0, the video memory manager allocates contiguous paged-locked memory, which is mapped write-combined memory, for the DMA buffers. Therefore, the GPU must access DMA buffers by using PCI cycles on systems where AGP transfers that occur outside the AGP aperture are not permitted.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544630">D3DDDI_PATCHLOCATIONLIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560975">DXGK_ALLOCATIONLIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561049">DXGK_DEVICEINFOFLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557618">DXGKARG_PRESENT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557648">DXGKARG_RENDER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a7027735-0ec4-4fad-81fb-1c3aca4ebf2d">DxgkDdiCreateDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1a46b129-1e78-44e6-a609-59eab206692b">DxgkDdiPresent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fd634768-5e1e-4f40-82fd-5ef69148c3d7">DxgkDdiRender</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_DEVICEINFO structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
