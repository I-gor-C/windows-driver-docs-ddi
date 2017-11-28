---
UID: NC.d3d12umddi.PFND3D12DDI_BEGIN_END_QUERY_0003
title: PFND3D12DDI_BEGIN_END_QUERY_0003
author: windows-driver-content
description: The pfnBeginQuery callback function defines the beginning of the portion of a command list to which a query applies.
old-location: display\pfnd3d12ddi_begin_end_query_0003.htm
old-project: display
ms.assetid: 9EBF7E0C-BF6D-4E99-B289-8C6581A2DEA5
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
req.alt-api: pfnBeginQuery
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

# PFND3D12DDI_BEGIN_END_QUERY_0003 callback



## -description
<p>The <i>pfnBeginQuery</i> callback function defines the beginning of the portion of a command list to which a query applies.</p>


## -prototype

````
PFND3D12DDI_BEGIN_END_QUERY_0003 pfnBeginQuery;

VOID  APIENTRY* pfnBeginQuery(
   D3D12DDI_HCOMMANDLIST hCommandList,
   D3D12DDI_HQUERYHEAP   hQueryHeap,
   D3D12DDI_QUERY_TYPE   QueryType,
   UINT                  StartElement
)
{ ... }
````


## -parameters
<dl>

### -param <i>hCommandList</i> 

<dd>
<p>The handle of a command list for which to query. </p>
</dd>

### -param <i>hQueryHeap</i> 

<dd>
<p>The handle of a query heap, which represents an array of query results.</p>
</dd>

### -param <i>QueryType</i> 

<dd>
<p>The type of query.</p>
</dd>

### -param <i>StartElement</i> 

<dd>
<p>The value of the start element.</p>
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