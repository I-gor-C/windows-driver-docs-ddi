---
UID: NS.d3dkmthk._D3DKMT_RECLAIMALLOCATIONS2
title: D3DKMT_RECLAIMALLOCATIONS2
author: windows-driver-content
description: D3DKMT_RECLAIMALLOCATIONS2 describes video memory resources that are to be reclaimed and that the driver previously offered for reuse. Used with the D3DKMTReclaimAllocations2 function.
old-location: display\d3dkmt_reclaimallocations2.htm
old-project: display
ms.assetid: 7980F1FD-D7C2-4C74-8652-89FD38BE4D1F
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_RECLAIMALLOCATIONS2, D3DKMT_RECLAIMALLOCATIONS2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_RECLAIMALLOCATIONS2
req.alt-loc: D3dkmthk.h
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

# D3DKMT_RECLAIMALLOCATIONS2 structure



## -description
<p><b>D3DKMT_RECLAIMALLOCATIONS2</b> describes video memory resources that are to be reclaimed and that the driver  previously offered  for reuse. Used with the  <a href="https://msdn.microsoft.com/library/windows/hardware/dn906780">D3DKMTReclaimAllocations2</a> function.</p>


## -syntax

````
typedef struct _D3DKMT_RECLAIMALLOCATIONS2 {
  D3DKMT_HANDLE       hPagingQueue;
  UINT                NumAllocations;
  D3DKMT_HANDLE       *pResources;
  const D3DKMT_HANDLE *HandleList;
  union {
    BOOL                   *pDiscarded;
    D3DDDI_RECLAIM_RESULT* pResults;
  };
  UINT64              PagingFenceValue;
} D3DKMT_RECLAIMALLOCATIONS2;
````


## -struct-fields
<dl>

### -field <b>hPagingQueue</b>

<dd>
<p>[in] A handle to the device that created the allocations.</p>
</dd>

### -field <b>NumAllocations</b>

<dd>
<p>[in] The number of items in the <b>pResources</b>, <b>HandleList</b>, or  <b>pDiscarded</b> members, whichever is not <b>NULL</b>.</p>
</dd>

### -field <b>pResources</b>

<dd>
<p>[in] An array of <b>D3DKMT_HANDLE</b> data types that represent Direct3D runtime resource handles.</p>
</dd>

### -field <b>HandleList</b>

<dd>
<p>[in] An array of <b>D3DKMT_HANDLE</b> data types that represent kernel-mode handles to the allocations that are to be reclaimed.</p>
<p>If <b>HandleList</b> is not <b>NULL</b>, the <b>pResources</b> member must be <b>NULL</b>.</p>
</dd>

### -field <b>pDiscarded</b>

<dd>
<p>[out] Optional array of boolean variables  specifying whether each resource or allocation was discarded.</p>
</dd>

### -field <b>pResults</b>

<dd>
<p>[in] Required array of values specifying whether the surface is valid, discarded, or list commitment.</p>
</dd>

### -field <b>PagingFenceValue</b>

<dd>
<p>The paging fence to synchronize against before submitting work to the GPU which references any of the resources or allocations in the provided arrays.</p>
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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>