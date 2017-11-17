---
UID: NF.d3dkmthk.D3DKMTDestroyProtectedSession
title: D3DKMTDestroyProtectedSession
author: windows-driver-content
description: Used to destroy a protected session.
old-location: display\d3dkmtdestroyprotectedsession.htm
ms.assetid: e27ab1db-647d-447c-b79d-2553aa088398
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTDestroyProtectedSession
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
ms.keywords: D3DKMTDestroyProtectedSession
req.iface: 
---

# D3DKMTDestroyProtectedSession function



## -description
<p>
			
            Used to destroy a protected session.</p>


## -syntax

````
NTSTATUS  D3DKMTDestroyProtectedSession(
  _Inout_ D3DKMT_DESTROYPROTECTEDSESSION  *D3dkmt_destroyprotectedsession
);
````


## -parameters
<dl>

### -param <i>D3dkmt_destroyprotectedsession</i> [in, out]

<dd>
<p>Holds information to destroy a protected session.</p>
</dd>
</dl>

## -returns
<p>
Returns STATUS_SUCCESS if completed successfully.</p>

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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p></p>
</td>
</tr>
</table>