---
UID: NC.d3d12umddi.PFND3D12DDI_SET_EXTENDED_FEATURE_CALLBACKS_0021
title: PFND3D12DDI_SET_EXTENDED_FEATURE_CALLBACKS_0021
author: windows-driver-content
description: The pfnSetExtendedFeatureCallbacks callback function sets extended feature callbacks.
old-location: display\pfnd3d12ddi_set_extended_feature_callbacks_0021.htm
old-project: display
ms.assetid: 8380C972-D5A0-46D5-B32B-C31D5113BB95
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnSetExtendedFeatureCallbacks
req.alt-loc: D3d12umddi.h
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

# PFND3D12DDI_SET_EXTENDED_FEATURE_CALLBACKS_0021 callback



## -description
<p>The <i>pfnSetExtendedFeatureCallbacks</i> callback function sets extended feature callbacks.</p>


## -prototype

````
PFND3D12DDI_SET_EXTENDED_FEATURE_CALLBACKS_0021 pfnSetExtendedFeatureCallbacks;

VOID APIENTRY* pfnSetExtendedFeatureCallbacks(
       D3D12DDI_HDEVICE              hDevice,
       D3D12DDI_TABLE_TYPE           Table,
  _In_ _reads_(TableSize) const void *pTable,
       SIZE_T                        TableSize
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> 

<dd>
<p>The handle of a device.</p>
</dd>

### -param <i>Table</i> 

<dd>
<p>A value for an implementation of video.</p>
</dd>

### -param <i>pTable</i> [in]

<dd>
<p>A pointer to a table value.</p>
</dd>

### -param <i>TableSize</i> 

<dd>
<p>The size of the table. </p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>