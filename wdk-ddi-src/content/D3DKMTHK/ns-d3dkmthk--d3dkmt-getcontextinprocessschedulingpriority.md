---
UID: NS.d3dkmthk._D3DKMT_GETCONTEXTINPROCESSSCHEDULINGPRIORITY
title: D3DKMT_GETCONTEXTINPROCESSSCHEDULINGPRIORITY
author: windows-driver-content
description: Describes information that is required for an in-process (in-proc) Microsoft Direct3D composition device to retrieve the scheduling priority for a device context that is in the same process as other device contexts.
old-location: display\d3dkmt_getcontextinprocessschedulingpriority.htm
ms.assetid: a72dd755-efd9-4950-8400-179eb1d63e9a
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_GETCONTEXTINPROCESSSCHEDULINGPRIORITY
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
ms.keywords: D3DKMT_GETCONTEXTINPROCESSSCHEDULINGPRIORITY, D3DKMT_GETCONTEXTINPROCESSSCHEDULINGPRIORITY
req.iface: 
---

# D3DKMT_GETCONTEXTINPROCESSSCHEDULINGPRIORITY structure



## -description
<p>Describes information that is required for an in-process (in-proc) Microsoft Direct3D composition device to retrieve the scheduling priority for a device context that is in the same process as other device contexts.</p>


## -syntax

````
typedef struct _D3DKMT_GETCONTEXTINPROCESSSCHEDULINGPRIORITY {
  D3DKMT_HANDLE hContext;
  INT           Priority;
} D3DKMT_GETCONTEXTINPROCESSSCHEDULINGPRIORITY;
````


## -struct-fields
<dl>

### -field <b>hContext</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents the kernel-mode handle to the device context to retrieve scheduling priority for.</p>
</dd>

### -field <b>Priority</b>

<dd>
<p>[out] The priority level that is retrieved for the device context relative to other device contexts within the same process.</p>
<p>A value of zero indicates that the context is scheduled with the same priority as other contexts within the same process.</p>
<p>A value of 1 indicates that the context is scheduled ahead of other contexts within the same process.</p>
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
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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