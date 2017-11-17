---
UID: NF.d3dkmthk.D3DKMTGetProcessDeviceLostSupport
title: D3DKMTGetProcessDeviceLostSupport
author: windows-driver-content
description: Used to get the indicated process.
old-location: display\d3dkmtgetprocessdevicelostsupport.htm
ms.assetid: 7127b6ff-164b-4645-a602-3969f87a47d0
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
req.alt-api: D3DKMTGetProcessDeviceLostSupport
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
ms.keywords: D3DKMTGetProcessDeviceLostSupport
req.iface: 
---

# D3DKMTGetProcessDeviceLostSupport function



## -description
<p>
			
            Used to get the indicated process.</p>


## -syntax

````
NTSTATUS  D3DKMTGetProcessDeviceLostSupport(
  _Inout_ D3DKMT_GETPROCESSDEVICELOSTSUPPORT  *D3dkmt_getprocessdevicelostsupport
);
````


## -parameters
<dl>

### -param <i>D3dkmt_getprocessdevicelostsupport</i> [in, out]

<dd>
<p>Holds information to get the indicated process.</p>
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