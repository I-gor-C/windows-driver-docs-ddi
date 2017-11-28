---
UID: NS.d3dkmddi._DXGK_GPUMMUCAPS
title: DXGK_GPUMMUCAPS
author: windows-driver-content
description: The DXGK_GPUMMUCAPS structure is used by the kernel mode driver to express virtual memory addressing capabilities.
old-location: display\dxgk_gpummucaps.htm
old-project: display
ms.assetid: 999820D0-FDEB-49FD-920A-75FD9886492A
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_GPUMMUCAPS, DXGK_GPUMMUCAPS
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
req.alt-api: DXGK_GPUMMUCAPS
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

# DXGK_GPUMMUCAPS structure



## -description
<p>The <b>DXGK_GPUMMUCAPS</b> structure is used by the kernel mode driver to express virtual memory addressing capabilities.</p>


## -syntax

````
typedef struct _DXGK_GPUMMUCAPS {
  union {
    struct {
      UINT ReadOnlyMemorySupported  :1;
      UINT NoExecuteMemorySupported  :1;
      UINT ZeroInPteSupported  :1;
      UINT ExplicitPageTableInvalidation  :1;
      UINT CacheCoherentMemorySupported  :1;
      UINT PageTableUpdateRequireAddressSpaceIdle  :1;
      UINT LargePageSupported  :1;
      UINT DualPteSupported  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_1)
      UINT AllowNonAlignedLargePageAddress  :1;
      UINT Reserved  :23;
    };
    UINT   Value;
  };
  DXGK_PAGETABLEUPDATEMODE PageTableUpdateMode;
  UINT                     VirtualAddressBitCount;
  UINT                     LeafPageTableSizeFor64KPagesInBytes;
  UINT                     PageTableLevelCount;
  struct {
    UINT SourcePageTableVaInTransfer  :1;
    UINT Reserved  :31;
  } LegacyBehaviors;
} DXGK_GPUMMUCAPS;
````


## -struct-fields
<dl>

### -field <b>ReadOnlyMemorySupported</b>

<dd>
<p>When set to 1, the driver supports read-only protection on memory pages.</p>
</dd>

### -field <b>NoExecuteMemorySupported</b>

<dd>
<p>When set to 1, the driver supports <i>no execute</i> protection on memory pages.</p>
</dd>

### -field <b>ZeroInPteSupported</b>

<dd>
<p>When set to 1, the GPU supports the <i>Zero DXGK_PTE</i> flag. This applies to all page table levels.</p>
</dd>

### -field <b>ExplicitPageTableInvalidation</b>

<dd>
<p>This flag indicates that all entries of a page table or page directory should be put into an invalid state explicitly, through <b>UpdatePageTable</b> before being freed. By default the video memory manager may free a page table, which contain previously valid entries, if these entries are no longer needed (ex. freeing a large GPU virtual address range resulting in the destruction of underlying page tables).
</p>
<div class="alert"><b>Note</b>  This flags is typically used by a software driver that needs to emulate page table and need to keep track of information on a per page table entry basis and require a clear init/deinit pair for all page table entry updates.</div>
<div> </div>
</dd>

### -field <b>CacheCoherentMemorySupported</b>

<dd>
<p>This flag indicates that the driver supports the <i>CacheCoherent</i> bits in the page table entry and can do I/O coherent transfer to system memory. </p>
</dd>

### -field <b>PageTableUpdateRequireAddressSpaceIdle</b>

<dd>
<p>This flag indicates that the GPU doesn’t support updating page table entries or invalidating translation look-aside buffer for an address space that is currently in used by an engine. When this flags is set, video memory manager will ensure that all context sharing the address space are suspended when its page table entries are modified and when translation look-aside buffer is invalidated.</p>
</dd>

### -field <b>LargePageSupported</b>

<dd>
<p>When set to 1, all levels of page tables, except the leaf one, support large pages (<b>LargePage</b> bit in <a href="https://msdn.microsoft.com/library/windows/hardware/ff562008">DXGK_PTE</a>).</p>
</dd>

### -field <b>DualPteSupported</b>

<dd>
<p>When set to 1, the GPU supports two pointers to page tables in the level one page table (4 KB page table and 64 KB page table). </p>
</dd>

### -field <b>AllowNonAlignedLargePageAddress</b>

<dd>
<p>When set to 1, the Operating System is able to set the <b>LargePage</b> flag when the physical address of the large page entry is not aligned to the leaf page table coverage.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should not be used.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>The value of the structure expressed as an integer.</p>
</dd>

### -field <b>PageTableUpdateMode</b>

<dd>
<p>Defines the type of addresses which are used in <a href="display.dxgkddiupdatepagetable">DxgkDdiUpdatePageTable</a> operations. When <b>DXGK_PAGETABLEUPDATE_GPU_VIRTUAL</b> is set, all paging operation will occur in the virtual address space of the system context. When page directories are located in a local GPU memory segment, the update mode cannot be set to <b>DXGK_PAGETABLEUPDATE_CPU_VIRTUAL</b>.</p>
</dd>

### -field <b>VirtualAddressBitCount</b>

<dd>
<p>The number of bits in the GPU virtual address.</p>
</dd>

### -field <b>LeafPageTableSizeFor64KPagesInBytes</b>

<dd>
<p>The size of a leaf page table when 64KB pages are used. The size must be a multiple of CPU page size (4096).</p>
</dd>

### -field <b>PageTableLevelCount</b>

<dd>
<p>The number of page table levels supported. The minimum value is 2 (defined as <b>DXGK_MIN_PAGE_TABLE_LEVEL_COUNT</b>). The maximum value is <b>DXGK_MAX_PAGE_TABLE_LEVEL_COUNT</b>. </p>
<p>When <b>PageTableLevelCount</b> is 2, the root page table is dynamically resizable and the size of the page table is determined through <a href="display.dxgkddigetrootpagetablesize">DxgkDdiGetRootPageTableSize</a>. When <b>PageTableLevelCount</b> is greater than 2, all page table levels have a fixed size, which is described through <a href="https://msdn.microsoft.com/library/windows/hardware/dn906832">DXGK_PAGE_TABLE_LEVEL_DESC</a><b>::PageTableSizeInBytes</b>.</p>
</dd>

### -field <b>LegacyBehaviors</b>

<dd>
<dl>

### -field <b>SourcePageTableVaInTransfer</b>

<dd>
<p>When set to 1, video memory manager sets <b>SourcePageTable</b> address in <b>TransferVirtual</b> during allocation eviction.</p>
</dd>
</dl>
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