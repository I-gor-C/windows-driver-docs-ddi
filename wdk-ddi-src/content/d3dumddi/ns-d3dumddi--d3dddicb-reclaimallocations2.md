---
UID: NS.d3dumddi._D3DDDICB_RECLAIMALLOCATIONS2
title: D3DDDICB_RECLAIMALLOCATIONS2
author: windows-driver-content
description: D3DDDICB_RECLAIMALLOCATIONS2 is used with pfnReclaimAllocations2Cb to describe video memory resources, previously offered for reuse by the driver, that are to be reclaimed.
old-location: display\d3dddicb_reclaimallocations2.htm
old-project: display
ms.assetid: 952935E2-3216-40E5-8A4E-AA5D5E584F12
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDICB_RECLAIMALLOCATIONS2, D3DDDICB_RECLAIMALLOCATIONS2
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
req.alt-api: D3DDDICB_RECLAIMALLOCATIONS2
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

# D3DDDICB_RECLAIMALLOCATIONS2 structure



## -description
<p><b>D3DDDICB_RECLAIMALLOCATIONS2</b> is used with <a href="display.pfnreclaimallocations2cb">pfnReclaimAllocations2Cb</a> to describe video memory resources, previously offered for reuse by the driver,  that are to be reclaimed.</p>


## -syntax

````
typedef struct _D3DDDICB_RECLAIMALLOCATIONS2 {
  _In_ D3DKMT_HANDLE                             PagingQueue;
  _In_ UINT                                      NumAllocations;
  _In_reads_(NumAllocations) CONST HANDLE        *pResources;
  _In_reads_(NumAllocations) CONST D3DKMT_HANDLE *HandleList;
  _Out_writes_all_opt_(NumAllocations) BOOL      *pDiscarded;
  _Out_ UINT64                                   PagingFenceValue;
} D3DDDICB_RECLAIMALLOCATIONS2;
````


## -struct-fields
<dl>

### -field <b>PagingQueue</b>

<dd>
<p>[in] The paging queue, supplied by the user-mode driver, to page in the allocation list.</p>
</dd>

### -field <b>NumAllocations</b>

<dd>
<p>[in]  The number of items in <b>pDiscarded</b> and whichever of <b>pResources</b> or <b>HandleList</b> is non-NULL.</p>
</dd>

### -field <b>pResources</b>

<dd>
<p>[in]  An array of Direct3D runtime resource handles.</p>
</dd>

### -field <b>HandleList</b>

<dd>
<p>[in]  An array of allocation handles. If non-NULL, <b>pResources</b> must be NULL.</p>
</dd>

### -field <b>pDiscarded</b>

<dd>
<p>[out] Optional array of boolean values specifying whether each resource or allocation was discarded.</p>
</dd>

### -field <b>PagingFenceValue</b>

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