---
UID: NF.d3dkmthk.D3DKMTCreateBundleObject
title: D3DKMTCreateBundleObject
author: windows-driver-content
description: Used to create a bundle object.
old-location: display\d3dkmtcreatebundleobject.htm
ms.assetid: c4d62ccf-606b-457e-a239-1b5189e42657
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
req.alt-api: D3DKMTCreateBundleObject
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
ms.keywords: D3DKMTCreateBundleObject
req.iface: 
---

# D3DKMTCreateBundleObject function



## -description
<p>
			
            Used to create a bundle object.</p>


## -syntax

````
NTSTATUS  D3DKMTCreateBundleObject(
  _Inout_ D3DKMT_CREATEBUNDLEOBJECT  *D3dkmt_createbundleobject
);
````


## -parameters
<dl>

### -param <i>D3dkmt_createbundleobject</i> [in, out]

<dd>
<p>Holds information to create a bundle object.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the call has been successfully completed.</p>

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