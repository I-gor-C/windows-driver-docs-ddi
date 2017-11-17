---
UID: NF.d3dkmthk.D3DKMTSetMonitorColorSpaceTransform
title: D3DKMTSetMonitorColorSpaceTransform
author: windows-driver-content
description: Used to set the color space transform for the selected monitor.
old-location: display\d3dkmtsetmonitorcolorspacetransform.htm
ms.assetid: cb831371-4684-4756-bc01-6c42e5af7e1b
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
req.alt-api: D3DKMTSetMonitorColorSpaceTransform
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
ms.keywords: D3DKMTSetMonitorColorSpaceTransform
req.iface: 
---

# D3DKMTSetMonitorColorSpaceTransform function



## -description
<p>
			
            Used to set the color space transform for the selected monitor.</p>


## -syntax

````
NTSTATUS  D3DKMTSetMonitorColorSpaceTransform(
   D3DKMT_SET_COLORSPACE_TRANSFORM  D3dkmt_set_colorspace_transform
);
````


## -parameters
<dl>

### -param <i>D3dkmt_set_colorspace_transform</i> 

<dd>
<p>Used to set the colorspace transform.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if completed successfully.</p>

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