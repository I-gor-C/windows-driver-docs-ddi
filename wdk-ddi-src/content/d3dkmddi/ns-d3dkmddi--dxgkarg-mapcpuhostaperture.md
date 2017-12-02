---
UID: NS.d3dkmddi._DXGKARG_MAPCPUHOSTAPERTURE
title: DXGKARG_MAPCPUHOSTAPERTURE
author: windows-driver-content
description: The DXGKARG_MAPCPUHOSTAPERTURE structure is used to map an allocation, resident in a local memory segment, into the CPU host aperture in order to make it visible to the CPU.
old-location: display\dxgkarg_mapcpuhostaperture.htm
old-project: display
ms.assetid: ACC0C800-B6E3-4EF2-846C-63BF4564D0FD
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_MAPCPUHOSTAPERTURE, DXGKARG_MAPCPUHOSTAPERTURE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_MAPCPUHOSTAPERTURE
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

# DXGKARG_MAPCPUHOSTAPERTURE structure



## -description
<p>The <b>DXGKARG_MAPCPUHOSTAPERTURE</b> structure is used to map an allocation, resident in a local memory segment, into the CPU host aperture in order to make it visible to the CPU.</p>


## -syntax

````
typedef struct _DXGKARG_MAPCPUHOSTAPERTURE {
  HANDLE hAllocation;
  WORD   SegmentId;
  WORD   PhysicalAdapterIndex;
  UINT64 NumberOfPages;
  UINT32 *pCpuHostAperturePages;
  UINT64 *pMemorySegmentPages;
} DXGKARG_MAPCPUHOSTAPERTURE;
````


## -struct-fields
<dl>

### -field hAllocation

<dd>
<p>Specifies the allocation handle, associated with the allocation being mapped. This is the handle, returned by the kernel mode driver from <a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a> or passed in <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-createcontextallocation.md">DxgkCbCreateContextAllocation</a>. This parameter will be <b>NULL</b> for implicit allocations, such as a page table.</p>
</dd>

### -field SegmentId

<dd>
<p>Specifies the segment identifier of the segment being accessed.</p>
</dd>

### -field PhysicalAdapterIndex

<dd>
<p>A zero-based physical adapter index in a linked display adapter link.
The page size is equal to the segment page size, reported in <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-segmentflags.md">DXGK_SEGMENTFLAGS</a>.
</p>
<div class="alert"><b>Note</b>  The allocation itself might be aligned on 4KB page boundary. When the segment page size is 64 KB, CPU host aperture in this case will map more than the allocation size.
</div>
<div> </div>
</dd>

### -field NumberOfPages

<dd>
<p>Specifies the number of pages being mapped.</p>
</dd>

### -field pCpuHostAperturePages

<dd>
<p>Array of CPU Host Aperture pages to map. This is an array of page indices from the start of the CPU host aperture physical address.</p>
</dd>

### -field pMemorySegmentPages

<dd>
<p>MDL-style array of page indices to the allocation pages that need to be mapped into the CPU host aperture. The page indexes starting from 0. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
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