---
UID: NF.d3dkmthk.D3DKMTSetMonitorColorSpaceTransform
title: D3DKMTSetMonitorColorSpaceTransform function
author: windows-driver-content
description: Used to set the color space transform for the selected monitor.
old-location: display\d3dkmtsetmonitorcolorspacetransform.htm
old-project: display
ms.assetid: cb831371-4684-4756-bc01-6c42e5af7e1b
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: D3DKMTSetMonitorColorSpaceTransform
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
---

# D3DKMTSetMonitorColorSpaceTransform function



## -description

			
            Used to set the color space transform for the selected monitor.


## -syntax

````
NTSTATUS  D3DKMTSetMonitorColorSpaceTransform(
   D3DKMT_SET_COLORSPACE_TRANSFORM  D3dkmt_set_colorspace_transform
);
````


## -parameters

### -param D3dkmt_set_colorspace_transform 

Used to set the colorspace transform.

## -returns
Returns STATUS_SUCCESS if completed successfully.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 10
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2016
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">

</td>
</tr>
</table>