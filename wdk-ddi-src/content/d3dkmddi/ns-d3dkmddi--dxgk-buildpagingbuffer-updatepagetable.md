---
UID: NS.d3dkmddi._DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE
title: DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE
author: windows-driver-content
description: DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE is used as part of a page table update operation.
old-location: display\dxgk_buildpagingbuffer_updatepagetable.htm
old-project: display
ms.assetid: 734B2E28-75F8-49AE-AAAB-EB0C037C6432
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE, DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE
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
req.alt-api: DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE
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

# DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE structure



## -description
<p><b>DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE</b> is used as part of a page table update operation.</p>


## -syntax

````
typedef struct _DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE {
  UINT                        PageTableLevel;
  HANDLE                      hAllocation;
  DXGK_PAGETABLEUPDATEADDRESS PageTableAddress;
  DXGK_PTE                    *pPageTableEntries;
  UINT                        StartIndex;
  UINT                        NumPageTableEntries;
  UINT                        Reserved0;
  DXGK_UPDATEPAGETABLEFLAGS   Flags;
  UINT64                      DriverProtection;
  UINT64                      AllocationOffsetInBytes;
  HANDLE                      hProcess;
  DXGK_PAGETABLEUPDATEMODE    UpdateMode;
  DXGK_PTE                    *pPageTableEntries64KB;
  D3DGPU_VIRTUAL_ADDRESS      FirstPteVirtualAddress;
} DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE;
````


## -struct-fields
<dl>

### -field PageTableLevel

<dd>
<p>Level of a page table, which is updated.</p>
</dd>

### -field hAllocation

<dd>
<p>Kernel mode driver handle of an allocation, which is mapped by the page table entries. The handle is returned by the kernel mode driver from <a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a>. The handle can be <b>NULL</b> for allocations, which do not have a kernel mode drver   handle (page tables, page directories, etc.).</p>
</dd>

### -field PageTableAddress

<dd>
<p>Address of the page table to update. If <b>DXGK_VIRTUALADDRESSCAPS:: PageTableUpdateMode</b> is <b>DXGK_PAGETABLEUPDATE_CPU_VIRTUAL</b>, the CPU virtual address is in the <b>CpuVirtual</b> field. If <b>DXGK_VIRTUALADDRESSCAPS:: PageTableUpdateMode</b> is <b>DXGK_PAGETABLEUPDATE_GPU_VIRTUAL</b>, the GPU virtual address is in the <b>GpuVirtual</b> field. If <b>DXGK_VIRTUALADDRESSCAPS:: PageTableUpdateMode</b> is <b>DXGK_PAGETABLEUPDATE_GPU_PHYSICAL</b>, the GPU physical address is in the <b>GpuPhysical</b> field.</p>
</dd>

### -field pPageTableEntries

<dd>
<p>The entries which need to be copied. The index zero in the <b>pPageTableEntries</b> array corresponds to the <b>StartIndex</b> in the driver page table entry array.</p>
</dd>

### -field StartIndex

<dd>
<p>The starting index of a page table entry within the page table where the entries should be copied. The page table entry array index is zero-based.</p>
</dd>

### -field NumPageTableEntries

<dd>
<p>The number of entries which need to be copied.</p>
</dd>

### -field Reserved0

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>

### -field Flags

<dd>
<p>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-updatepagetableflags.md">DXGK_UPDATEPAGETABLEFLAGS</a> structure describing the update operation.</p>
</dd>

### -field DriverProtection

<dd>
<p>Passed by UMD in MapGpuVirtualAddressRangeCb.</p>
</dd>

### -field AllocationOffsetInBytes

<dd>
<p>When <b>hAllocation</b> is non-NULL, this field specifies the relative offset, in bytes, from the beginning of the allocation to the first page being targeted by this update operation. If the update target multiple pages from <b>hAllocation</b>, those pages are guaranteed to be sequential. For example, video memory manager may be updating a GPU virtual address to page 4,5,6,7 in <b>hAllocation</b>. There will never be a case where a driver would see a single update operation which target non sequential pages (ex. 4,5,7). Note that although the pages are guaranteed to be sequential from the point of view of the allocation, they may not be physically contiguous in memory.</p>
</dd>

### -field hProcess

<dd>
<p>Kernel mode driver process handle for the process whose page table entries are updated. This is the value returned from <a href="display.dxgkddicreateprocess">DxgkDdiCreateProcess</a>.</p>
</dd>

### -field UpdateMode

<dd>
<p>Defines the meaning of <b>PageTableAddress</b>. When initializing page tables for the paging process, the update mode is always <b>DXGK_PAGETABLEUPDATE_CPU_VIRTUAL</b> and <b>pDmaBuffer</b> is set to <b>NULL</b>. In this case the driver must update page tables immediately. In other cases the <b>UpdateMode</b> is set to the value, which is specified in <b>DXGK_VIRTUALADDRESSCAPS::GpuMmu.PageTableUpdateMode</b>.</p>
<p>When updating page table entries for a leaf page table, video memory manager assumes that each entry covers a 4KB page. If a GPU page is bigger (4 KB * 2n), the video memory manager will provide entries in the array, which point within GPU pages. The kernel mode driver might only need to initialize page table entries, which point to the beginning of GPU pages. The following figure illustrates this for the case when GPU page is 16 KB.</p>
</dd>

### -field pPageTableEntries64KB

<dd>
<p>The entries which need to be copied from the 64KB page tables. The index zero in the <b>pPageTableEntries</b> array corresponds to the <b>StartIndex</b> in the driver page table entry array. The array should be use only when the <b>DXGK_GPUMMUCAPS::DualPteSupported</b> cap is set.</p>
</dd>

### -field FirstPteVirtualAddress

<dd>
<p>The GPU virtual address that is mapped by the first updated page table entry.</p>
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