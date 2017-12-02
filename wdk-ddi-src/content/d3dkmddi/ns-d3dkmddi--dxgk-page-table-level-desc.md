---
UID: NS.d3dkmddi._DXGK_PAGE_TABLE_LEVEL_DESC
title: DXGK_PAGE_TABLE_LEVEL_DESC
author: windows-driver-content
description: The DXGK_PAGE_TABLE_LEVEL_DESC structure describes capabilities that are applied at the page level.
old-location: display\dxgk_page_table_level_desc.htm
old-project: display
ms.assetid: 45BC190C-8985-4F8A-AC84-4ACBBCE9EB67
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_PAGE_TABLE_LEVEL_DESC, DXGK_PAGE_TABLE_LEVEL_DESC
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
req.alt-api: DXGK_PAGE_TABLE_LEVEL_DESC
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

# DXGK_PAGE_TABLE_LEVEL_DESC structure



## -description
<p>The <b>DXGK_PAGE_TABLE_LEVEL_DESC</b> structure describes capabilities that are applied at the page level.</p>


## -syntax

````
typedef struct _DXGK_PAGE_TABLE_LEVEL_DESC {
  UINT PageTableIndexBitCount;
  UINT PageTableSegmentId;
  UINT PagingProcessPageTableSegmentId;
  UINT PageTableSizeInBytes;
} DXGK_PAGE_TABLE_LEVEL_DESC;
````


## -struct-fields
<dl>

### -field PageTableIndexBitCount

<dd>
<p>The number of bits in the virtual address, which used as an index into the page table entry array. The number of entries in every page table is 2<sup>PageTableIndexBitCount</sup>. The video memory manager  sets up the page table entries, assuming that each entry covers a 4 KB page. When the root page table is resizable, the value for this level should be set to an initial index bit count (it could be set to zero). The corresponding <b>DXGK_PAGE_TABLE_LEVEL_DESC::PageTableSizeInBytes</b> should also be set accordingly.</p>
</dd>

### -field PageTableSegmentId

<dd>
<p>A zero-based memory segment identifier. When the segment identifier points to the system memory, the page table size cannot be more than 4 KB. The value zero is reserved for system memory.</p>
</dd>

### -field PagingProcessPageTableSegmentId

<dd>
<p>A zero-based memory segment identifier for the paging process. When the segment identifier points to the system memory (zero), the page table size cannot be more than 4 KB. The value zero is reserved for system memory.</p>
</dd>

### -field PageTableSizeInBytes

<dd>
<p>The size of a page table in bytes. The number of entries in a page table is equal to 2<sup>PageTableIndexBitCount</sup>. The size must be a multiple of the CPU page size. When the root page table is resizable, the value for this level should be set to an initial page table size (it could be set to zero).</p>
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