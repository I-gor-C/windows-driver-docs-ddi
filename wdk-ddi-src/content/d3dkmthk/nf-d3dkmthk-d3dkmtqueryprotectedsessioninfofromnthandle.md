---
UID: NF.d3dkmthk.D3DKMTQueryProtectedSessionInfoFromNtHandle
title: D3DKMTQueryProtectedSessionInfoFromNtHandle
author: windows-driver-content
description: Used to get information on the protected session.
old-location: display\d3dkmtqueryprotectedsessioninfofromnthandle.htm
old-project: display
ms.assetid: 04eff7e1-1ac3-4622-a837-1ea6aad97329
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMTQueryProtectedSessionInfoFromNtHandle
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTQueryProtectedSessionInfoFromNtHandle
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

# D3DKMTQueryProtectedSessionInfoFromNtHandle function



## -description
<p>Used to get information on the protected session.
			
            </p>


## -syntax

````
NTSTATUS  D3DKMTQueryProtectedSessionInfoFromNtHandle(
   D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE  D3dkmt_queryprotectedsessioninfofromnthandle
);
````


## -parameters
<dl>

### -param <i>D3dkmt_queryprotectedsessioninfofromnthandle</i> 

<dd>
<p>Holds session information from the NT handle.</p>
</dd>
</dl>

## -returns
<p>
Returns STATUS_SUCCESS when completed successfully.</p>

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