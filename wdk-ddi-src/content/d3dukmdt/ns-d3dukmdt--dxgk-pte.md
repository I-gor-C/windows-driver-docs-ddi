---
UID: NS.d3dukmdt._DXGK_PTE
title: DXGK_PTE
author: windows-driver-content
description: A page table entry (PTE) provides a physical address of a page and other attributes. The exact format of PTE depends on hardware implementation.
old-location: display\dxgk_pte.htm
old-project: display
ms.assetid: 2d5c1f3e-69a6-4f7f-9c99-bbaf94e6401b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_PTE, DXGK_PTE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_PTE
req.alt-loc: d3dukmdt.h
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

# DXGK_PTE structure



## -description
<p>A page table entry (PTE) provides a physical address of a page and other attributes. The exact format of PTE depends on hardware implementation. </p>


## -syntax

````
typedef struct _DXGK_PTE {
  union {
    struct {
      ULONGLONG Valid  :1;
      ULONGLONG Zero  :1;
      ULONGLONG CacheCoherent  :1;
      ULONGLONG ReadOnly  :1;
      ULONGLONG NoExecute  :1;
      ULONGLONG Segment  :5;
      ULONGLONG LargePage  :1;
      ULONGLONG PhysicalAdapterIndex  :6;
      ULONGLONG PageTablePageSize  :2;
      ULONGLONG Reserved  :45;
    };
    ULONGLONG Flags;
  };
  union {
    ULONGLONG PageAddress;
    ULONGLONG PageTableAddress;
  };
} DXGK_PTE;
````


## -struct-fields
<dl>

### -field <b>Valid</b>

<dd>
<p>When set, this indicates that the entry is valid. Accessing an invalid entry leads to an unrecoverable address fault, unless the <b>Zero</b> flag is set.</p>
</dd>

### -field <b>Zero</b>

<dd>
<p>When set with <b>Valid</b> = 1, the access to the entry lead to returning the zero value for the memory access. This is used to support tiled resources.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>CacheCoherent</b>

<dd>
<p>When set, this indicates that the memory page is cache coherent between CPU and GPU.</p>
</dd>

### -field <b>ReadOnly</b>

<dd>
<p>When set, this indicates that the memory page is read only.</p>
</dd>

### -field <b>NoExecute</b>

<dd>
<p>When set, this  indicates that the memory page contains data, which should not be treated as executable commands.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>Segment</b>

<dd>
<p>A zero-based GPU memory segment identifier where the corresponding memory page is located. The segment zero is reserved for system memory. </p>
</dd>

### -field <b>LargePage</b>

<dd>
<p>The bit can be set only when the kernel mode driver sets the <a href="display.dxgk_virtualaddresscaps">DXGK_VIRTUALADDRESSCAPS</a>::<b>GpuMmu</b>.<b>LargePageSupported</b> cap. When set the page table address (<b>PageTableAddress</b> + <b>SegmentId</b>) is the memory address of an allocation. The allocation size is equal to the virtual address range, covered by the lower page table level. This flag cannot be set for the leaf page tables.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>PhysicalAdapterIndex</b>

<dd>
<p>Defines a physical adapter index in a linked display adapter configuration. PTEs of page tables on one physical adapter can point to memory on another physical adapter.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>PageTablePageSize</b>

<dd>
<p>For the level 1 page table entry defines the pages size of the leaf page table PTEs. The value is provided by the  <a href="..\d3dukmdt\ne-d3dukmdt--dxgk-pte-page-size.md">DXGK_PTE_PAGE_SIZE</a> enumerator. This value should be ignored  when dual-PTE is supported.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use and will be set to zero.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>The unmasked value of the structure.</p>
</dd>

### -field <b>PageAddress</b>

<dd>
<p>The high 52 bits of the 64 bit physical address of a memory page. The low 12 bits are zero. The address is an offset from the start of the segment, defined by <b>Segment</b>, or a system memory address.</p>
</dd>

### -field <b>PageTableAddress</b>

<dd>
<p>The high 52 bits of the 64 bit physical address of a lower level page table. The low 12 bits are zero. The address is an offset from the start of the segment, defined by <b>Segment</b>, or a system memory address.</p>
<p>Supported starting with Windows 10.</p>
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
<p>Available in Windows 7 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dukmdt.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>