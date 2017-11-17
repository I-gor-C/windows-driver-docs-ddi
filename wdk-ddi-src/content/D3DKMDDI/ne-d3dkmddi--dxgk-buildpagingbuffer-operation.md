---
UID: NE.d3dkmddi._DXGK_BUILDPAGINGBUFFER_OPERATION
title: DXGK_BUILDPAGINGBUFFER_OPERATION
author: windows-driver-content
description: Indicates the type of memory operation to perform.
old-location: display\dxgk_buildpagingbuffer_operation.htm
ms.assetid: D170D828-A0BC-4CBC-9F3F-E384AAD11FCC
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_BUILDPAGINGBUFFER_OPERATION
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
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
req.iface: 
---

# DXGK_BUILDPAGINGBUFFER_OPERATION enumeration



## -description
<p>Indicates the type of memory operation to perform.</p>


## -syntax

````
typedef enum _DXGK_BUILDPAGINGBUFFER_OPERATION { 
  DXGK_OPERATION_TRANSFER                   = 0,
  DXGK_OPERATION_FILL                       = 1,
  DXGK_OPERATION_DISCARD_CONTENT            = 2,
  DXGK_OPERATION_READ_PHYSICAL              = 3,
  DXGK_OPERATION_WRITE_PHYSICAL             = 4,
  DXGK_OPERATION_MAP_APERTURE_SEGMENT       = 5,
  DXGK_OPERATION_UNMAP_APERTURE_SEGMENT     = 6,
  DXGK_OPERATION_SPECIAL_LOCK_TRANSFER      = 7,
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN7)
  DXGK_OPERATION_VIRTUAL_TRANSFER           = 8,
  DXGK_OPERATION_VIRTUAL_FILL               = 9,
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
  DXGK_OPERATION_INIT_CONTEXT_RESOURCE      = 10,
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
  DXGK_OPERATION_UPDATE_PAGE_TABLE          = 11,
  DXGK_OPERATION_FLUSH_TLB                  = 12,
  DXGK_OPERATION_UPDATE_CONTEXT_ALLOCATION  = 13,
  DXGK_OPERATION_COPY_PAGE_TABLE_ENTRIES    = 14,
  DXGK_OPERATION_NOTIFY_RESIDENCY           = 15,
#endif 
  
} DXGK_BUILDPAGINGBUFFER_OPERATION;
````


## -enum-fields
<dl>

### -field <a id="DXGK_OPERATION_TRANSFER"></a><a id="dxgk_operation_transfer"></a><b>DXGK_OPERATION_TRANSFER</b>

<dd>
<p>Perform a transfer operation that moves the content of an allocation from one location to another.</p>
</dd>

### -field <a id="DXGK_OPERATION_FILL"></a><a id="dxgk_operation_fill"></a><b>DXGK_OPERATION_FILL</b>

<dd>
<p>Fill an allocation with a specified pattern.</p>
</dd>

### -field <a id="DXGK_OPERATION_DISCARD_CONTENT"></a><a id="dxgk_operation_discard_content"></a><b>DXGK_OPERATION_DISCARD_CONTENT</b>

<dd>
<p>Notifies the driver that an allocation is discarded from the allocation's current location in a memory segment (that is, the allocation is evicted and not copied back to system memory).</p>
</dd>

### -field <a id="DXGK_OPERATION_READ_PHYSICAL"></a><a id="dxgk_operation_read_physical"></a><b>DXGK_OPERATION_READ_PHYSICAL</b>

<dd>
<p>Perform a read-physical operation that reads from a specified physical memory address.</p>
</dd>

### -field <a id="DXGK_OPERATION_WRITE_PHYSICAL"></a><a id="dxgk_operation_write_physical"></a><b>DXGK_OPERATION_WRITE_PHYSICAL</b>

<dd>
<p>Perform a write-physical operation that writes to a specified physical memory address.</p>
</dd>

### -field <a id="DXGK_OPERATION_MAP_APERTURE_SEGMENT"></a><a id="dxgk_operation_map_aperture_segment"></a><b>DXGK_OPERATION_MAP_APERTURE_SEGMENT</b>

<dd>
<p>Perform a map-aperture-segment operation that maps a memory descriptor list (MDL) into a range of an aperture segment.</p>
</dd>

### -field <a id="DXGK_OPERATION_UNMAP_APERTURE_SEGMENT"></a><a id="dxgk_operation_unmap_aperture_segment"></a><b>DXGK_OPERATION_UNMAP_APERTURE_SEGMENT</b>

<dd>
<p>Perform an unmap-aperture-segment operation that unmaps a previously mapped range of an aperture segment.</p>
</dd>

### -field <a id="DXGK_OPERATION_SPECIAL_LOCK_TRANSFER"></a><a id="dxgk_operation_special_lock_transfer"></a><b>DXGK_OPERATION_SPECIAL_LOCK_TRANSFER</b>

<dd>
<p>Perform a special transfer operation that moves the content of an allocation from one location to another. In this operation, the content of the allocation is transferred from or to the alternate virtual address that was set up for the allocation (that is, when the <a href="https://msdn.microsoft.com/69022797-432a-410b-8cbf-e1ef7111e7ea">pfnLockCb</a> function was called with the <b>UseAlternateVA</b> bit-field flag set).</p>
</dd>

### -field <a id="DXGK_OPERATION_VIRTUAL_TRANSFER"></a><a id="dxgk_operation_virtual_transfer"></a><b>DXGK_OPERATION_VIRTUAL_TRANSFER</b>

<dd>
<p>The operation is used to transfer allocation content between locations in memory. </p>
</dd>

### -field <a id="DXGK_OPERATION_VIRTUAL_FILL"></a><a id="dxgk_operation_virtual_fill"></a><b>DXGK_OPERATION_VIRTUAL_FILL</b>

<dd>
<p>The operation is used to fill an allocation with a pattern.</p>
</dd>

### -field <a id="DXGK_OPERATION_INIT_CONTEXT_RESOURCE"></a><a id="dxgk_operation_init_context_resource"></a><b>DXGK_OPERATION_INIT_CONTEXT_RESOURCE</b>

<dd>
<p>Perform an context initialization operation for a GPU context or device-specific context. This value is supported beginning with Windows 8.
</p>
<div class="alert"><b>Note</b>  The display miniport driver allocates context resources by calling <a href="https://msdn.microsoft.com/b6b142a4-20eb-4368-bd7f-8a25f4fe48ca">DxgkCbCreateContextAllocation</a>.</div>
<div> </div>
</dd>

### -field <a id="DXGK_OPERATION_UPDATE_PAGE_TABLE"></a><a id="dxgk_operation_update_page_table"></a><b>DXGK_OPERATION_UPDATE_PAGE_TABLE</b>

<dd>
<p>The operation is called to allow the kernel mode driver to build a command buffer to update a page table. </p>
</dd>

### -field <a id="DXGK_OPERATION_FLUSH_TLB"></a><a id="dxgk_operation_flush_tlb"></a><b>DXGK_OPERATION_FLUSH_TLB</b>

<dd>
<p>This operation instructs GPU to flush <i>translation look-aside buffer</i> entries, which belong to the given root page table. </p>
</dd>

### -field <a id="DXGK_OPERATION_UPDATE_CONTEXT_ALLOCATION"></a><a id="dxgk_operation_update_context_allocation"></a><b>DXGK_OPERATION_UPDATE_CONTEXT_ALLOCATION</b>

<dd>
<p>This operation is used to update the content of a context or device allocation. </p>
</dd>

### -field <a id="DXGK_OPERATION_COPY_PAGE_TABLE_ENTRIES"></a><a id="dxgk_operation_copy_page_table_entries"></a><b>DXGK_OPERATION_COPY_PAGE_TABLE_ENTRIES</b>

<dd>
<p>This operation is called to copy page table entries from one location to another.</p>
</dd>

### -field <a id="DXGK_OPERATION_NOTIFY_RESIDENCY"></a><a id="dxgk_operation_notify_residency"></a><b>DXGK_OPERATION_NOTIFY_RESIDENCY</b>

<dd>
<p>The paging operation is issued every time an allocation residency is changed (when allocation is evicted or committed).</p>
</dd>

### -field <a id=""></a><b></b>

<dd></dd>
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