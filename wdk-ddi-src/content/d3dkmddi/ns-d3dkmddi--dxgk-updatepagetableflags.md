---
UID: NS.d3dkmddi._DXGK_UPDATEPAGETABLEFLAGS
title: DXGK_UPDATEPAGETABLEFLAGS
author: windows-driver-content
description: DXGK_UPDATEPAGETABLEFLAGS is used as part of a page table update operation.
old-location: display\dxgk_updatepagetableflags.htm
old-project: display
ms.assetid: E0E1CDE7-F1BF-44C8-A320-9BD90788679F
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_UPDATEPAGETABLEFLAGS, DXGK_UPDATEPAGETABLEFLAGS
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
req.alt-api: DXGK_UPDATEPAGETABLEFLAGS
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

# DXGK_UPDATEPAGETABLEFLAGS structure



## -description
<p><b>DXGK_UPDATEPAGETABLEFLAGS</b> is used as part of a page table update operation.</p>


## -syntax

````
typedef struct _DXGK_UPDATEPAGETABLEFLAGS {
  UINT Repeat  :1;
  UINT InitialUpdate  :1;
  UINT NotifyEviction  :1;
  UINT Use64KBPages  :1;
  UINT Reserved  :28;
} DXGK_UPDATEPAGETABLEFLAGS;
````


## -struct-fields
<dl>

### -field Repeat

<dd>
<p>When set to <b>TRUE</b>, page table entries will point to a single page table entry value that needs to be replicated to all page table entries being updated.</p>
</dd>

### -field InitialUpdate

<dd>
<p>Indicates that the page table is initialized very first time after being made resident in memory.</p>
</dd>

### -field NotifyEviction

<dd>
<p>Indicates that the page table is about to be evicted. </p>
</dd>

### -field Use64KBPages

<dd>
<p>Indicates that page table entries  point to page tables pointing to 64 KB pages. </p>
</dd>

### -field Reserved

<dd>
<p>This member is reserved and should be set to zero.</p>
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