---
UID: NS.d3dkmthk._D3DKMT_OUTPUTDUPL_SNAPSHOT
title: D3DKMT_OUTPUTDUPL_SNAPSHOT
author: windows-driver-content
description: Provides information on the current processes in which output duplication is occurring.
old-location: display\d3dkmt_outputdupl_snapshot.htm
ms.assetid: bec6a398-34e8-4c03-ac15-c3f00645eac7
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
req.alt-api: D3DKMT_OUTPUTDUPL_SNAPSHOT
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
ms.keywords: D3DKMT_OUTPUTDUPL_SNAPSHOT, D3DKMT_OUTPUTDUPL_SNAPSHOT
req.iface: 
---

# D3DKMT_OUTPUTDUPL_SNAPSHOT structure



## -description
<p>Provides information on the current processes in which output duplication is occurring.</p>


## -syntax

````
typedef struct _D3DKMT_OUTPUTDUPL_SNAPSHOT {
  UINT                          Size;
  UINT                          SessionProcessCount;
  UINT                          SessionActiveConnectionsCount;
  UINT                          NumVidPnSources;
  UINT                          NumOutputDuplContexts;
  OUTPUTDUPL_CONTEXT_DEBUG_INFO OutputDuplDebugInfos[];
} D3DKMT_OUTPUTDUPL_SNAPSHOT;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>[in/out] The size, in bytes, of the entire structure.</p>
</dd>

### -field <b>SessionProcessCount</b>

<dd>
<p>[out] The number of processes in this session that are currently duplicating output. The value of <b>NumOutputDuplContexts</b> specifies the maximum possible number of processes.</p>
</dd>

### -field <b>SessionActiveConnectionsCount</b>

<dd>
<p>[out] The total number of active contexts in this session. The value may be more than the number of active contexts in the 2-D array, which are per adapter.</p>
</dd>

### -field <b>NumVidPnSources</b>

<dd>
<p>[out] The number of video present network (VidPN) sources.</p>
</dd>

### -field <b>NumOutputDuplContexts</b>

<dd>
<p>[out] The number of contexts in which output duplication is occurring.</p>
</dd>

### -field <b>OutputDuplDebugInfos</b>

<dd>
<p>Reserved for system use. Set to zero.</p>
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