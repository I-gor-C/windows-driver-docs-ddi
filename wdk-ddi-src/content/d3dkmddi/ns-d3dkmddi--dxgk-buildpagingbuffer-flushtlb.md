---
UID: NS.d3dkmddi._DXGK_BUILDPAGINGBUFFER_FLUSHTLB
title: DXGK_BUILDPAGINGBUFFER_FLUSHTLB
author: windows-driver-content
description: DXGK_BUILDPAGINGBUFFER_FLUSHTLB is used as part of a flush translation look-aside buffer (TLB) operation.
old-location: display\dxgk_buildpagingbuffer_flushtlb.htm
old-project: display
ms.assetid: 9FDE47A4-1784-41EB-9F60-76368D6DFEED
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_BUILDPAGINGBUFFER_FLUSHTLB, DXGK_BUILDPAGINGBUFFER_FLUSHTLB
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
req.alt-api: DXGK_BUILDPAGINGBUFFER_FLUSHTLB
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

# DXGK_BUILDPAGINGBUFFER_FLUSHTLB structure



## -description
<p><b>DXGK_BUILDPAGINGBUFFER_FLUSHTLB</b> is used as part of a flush translation look-aside buffer (TLB) operation.</p>


## -syntax

````
typedef struct _DXGK_BUILDPAGINGBUFFER_FLUSHTLB {
  D3DGPU_PHYSICAL_ADDRESS RootPageTableAddress;
  HANDLE                  hProcess;
  D3DGPU_PHYSICAL_ADDRESS StartVirtualAddress;
  D3DGPU_PHYSICAL_ADDRESS EndVirtualAddress;
} DXGK_BUILDPAGINGBUFFER_FLUSHTLB;
````


## -struct-fields
<dl>

### -field <b>RootPageTableAddress</b>

<dd>
<p>Physical address of the root page table being invalidated.</p>
</dd>

### -field <b>hProcess</b>

<dd>
<p>KMD process handle,  returned from <a href="display.dxgkddicreateprocess">DxgkDdiCreateProcess</a>, that the page table belongs to. </p>
</dd>

### -field <b>StartVirtualAddress</b>

<dd>
<p>The start of the affected GPU virtual address range.</p>
</dd>

### -field <b>EndVirtualAddress</b>

<dd>
<p>The end of the affected GPU virtual address range. When both <b>StartVirtualAddress</b> and <b>EndVirtualAddress</b> are zero, the entire GPU virtual address range is affected.</p>
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