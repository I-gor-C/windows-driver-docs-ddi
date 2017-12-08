---
UID: NS.d3dumddi._D3D12DDICB_RECLAIMALLOCATIONS2
title: D3D12DDICB_RECLAIMALLOCATIONS2
author: windows-driver-content
description: Describes video memory resources that are to be reclaimed and that the driver previously offered for reuse.
old-location: display\d3d12ddicb_reclaimallocations2.htm
old-project: display
ms.assetid: B5ADCD5D-301C-4B02-A4B2-90A81A5FBBC9
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDICB_RECLAIMALLOCATIONS2, D3D12DDICB_RECLAIMALLOCATIONS2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDICB_RECLAIMALLOCATIONS2
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

# D3D12DDICB_RECLAIMALLOCATIONS2 structure



## -description
<p>Describes video memory resources that are to be reclaimed and that the driver  previously offered  for reuse.</p>


## -syntax

````
typedef struct _D3D12DDICB_RECLAIMALLOCATIONS2 {
  _In_ UINT                                      NumAllocations;
  _In_reads_(NumAllocations) CONST HANDLE        *pResources;
  _In_reads_(NumAllocations) CONST D3DKMT_HANDLE *HandleList;
  _Out_writes_all_opt_(NumAllocations) BOOL      *pDiscarded;
  _Out_ UINT64                                   PagingFenceValue;
} D3D12DDICB_RECLAIMALLOCATIONS2;
````


## -struct-fields
<dl>

### -field NumAllocations

<dd>
<p>[in]  The number of items in <b>pDiscarded</b> and whichever of <b>pResources</b> or <b>HandleList</b> is non-NULL.</p>
</dd>

### -field pResources

<dd>
<p>[in]  An array of Direct3D runtime resource handles.</p>
</dd>

### -field HandleList

<dd>
<p>[in]  An array of allocation handles. If non-NULL, <b>pResources</b> must be NULL.</p>
</dd>

### -field pDiscarded

<dd>
<p>[out] Optional array of boolean values specifying whether each resource or allocation was discarded.</p>
</dd>

### -field PagingFenceValue

<dd>
<p>[out] The paging fence to synchronize against before submitting work to the GPU which
                                                                           references any of the resources or allocations in the provided arrays</p>
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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>