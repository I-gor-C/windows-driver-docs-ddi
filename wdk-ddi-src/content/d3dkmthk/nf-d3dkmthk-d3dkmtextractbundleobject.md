---
UID: NF.d3dkmthk.D3DKMTExtractBundleObject
title: D3DKMTExtractBundleObject
author: windows-driver-content
description: Used to extract the bundle object.
old-location: display\d3dkmtextractbundleobject.htm
old-project: display
ms.assetid: f3193d5b-084f-4df1-9688-26ba5a964cca
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMTExtractBundleObject
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
req.alt-api: D3DKMTExtractBundleObject
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

# D3DKMTExtractBundleObject function



## -description
<p>
			
            Used to extract the bundle object.</p>


## -syntax

````
NTSTATUS  D3DKMTExtractBundleObject(
  _Inout_ D3DKMT_EXTRACTBUNDLEOBJECT  *D3dkmt_extractbundleobject
);
````


## -parameters
<dl>

### -param D3dkmt_extractbundleobject [in, out]

<dd>
<p>Holds information to extract the bundle object.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if completed successfully. </p>

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