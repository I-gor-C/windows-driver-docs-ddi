---
UID: NS.d3dkmthk._D3DKMT_LOCK2
title: D3DKMT_LOCK2
author: windows-driver-content
description: D3DKMT_LOCK2 describes parameters for locking an allocation.
old-location: display\d3dkmt_lock2.htm
old-project: display
ms.assetid: AFDA9D5F-2590-4034-B2CF-07990F4553C8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_LOCK2, D3DKMT_LOCK2
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
req.alt-api: D3DKMT_LOCK2
req.alt-loc: d3dkmthk.h
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

# D3DKMT_LOCK2 structure



## -description
<p><b>D3DKMT_LOCK2</b> describes parameters for locking an allocation.</p>


## -syntax

````
typedef struct _D3DKMT_LOCK2 {
  D3DKMT_HANDLE       hDevice;
  D3DKMT_HANDLE       hAllocation;
  D3DDDICB_LOCK2FLAGS Flags;
  PVOID               pData;
} D3DKMT_LOCK2;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>The handle to the device.</p>
</dd>

### -field <b>hAllocation</b>

<dd>
<p>The handle to the allocation to lock.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A set of flags to pass to the <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtlock2.md">Lock2</a> kernel function which will determine how the allocation is locked. See <a href="..\d3dukmdt\ns-d3dukmdt--d3dddicb-lock2flags.md">D3DDDICB_LOCK2FLAGS</a> for details.</p>
</dd>

### -field <b>pData</b>

<dd>
<p>A CPU virtual address pointing a valid memory location pointing to the CPU backing store or the GPU frame buffer.</p>
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