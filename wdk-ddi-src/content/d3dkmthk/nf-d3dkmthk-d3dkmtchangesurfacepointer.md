---
UID: NF.d3dkmthk.D3DKMTChangeSurfacePointer
title: D3DKMTChangeSurfacePointer
author: windows-driver-content
description: The D3DKMTChangeSurfacePointer function is for system use only.
old-location: display\d3dkmtchangesurfacepointer.htm
old-project: display
ms.assetid: 3db4e04b-2707-4eb1-a249-2714304246a8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMTChangeSurfacePointer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTChangeSurfacePointer
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

# D3DKMTChangeSurfacePointer function



## -description
<p>The <b>D3DKMTChangeSurfacePointer</b> function is for system use only.</p>


## -syntax

````
NTSTATUS APIENTRY D3DKMTChangeSurfacePointer(
  _In_ const D3DKMT_CHANGESURFACEPOINTER *pData
);
````


## -parameters
<dl>

### -param <i>pData</i> [in]

<dd>
<p>For system use only.</p>
</dd>
</dl>

## -returns
<p>An opaque NTSTATUS value.</p>

## -remarks
<p>This function is for system use only.</p>

<p>This function is for system use only.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
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
</table>