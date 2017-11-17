---
UID: NC.d3d12umddi.PFND3D12DDI_RESOLVE_QUERY_DATA
title: PFND3D12DDI_RESOLVE_QUERY_DATA
author: windows-driver-content
description: The pfnResolveQueryData callback function transforms a previously stored query into an API defined format.
old-location: display\pfnd3d12ddi_resolve_query_data.htm
ms.assetid: 981053FF-9928-442F-B3B3-3B89AC61EEE4
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnResolveQueryData
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
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
req.iface: 
---

# PFND3D12DDI_RESOLVE_QUERY_DATA callback



## -description
<p>The <i>pfnResolveQueryData</i> callback function transforms a previously stored query into an API defined format.</p>


## -prototype

````
PFND3D12DDI_RESOLVE_QUERY_DATA pfnResolveQueryData;

VOID APIENTRY* pfnResolveQueryData(
   D3D12DDI_HCOMMANDLIST hCommandList,
   D3D12DDI_HQUERYHEAP   hQueryHeap,
   D3D12DDI_QUERY_TYPE   QueryType,
   UINT                  StartElement,
   UINT                  ElementCount,
   D3D12DDI_HRESOURCE    hDrvDestinationBuffer,
   UINT64                DestinationOffset
)
{ ... }
````


## -parameters
<dl>

### -param <i>hCommandList</i> 

<dd>
<p>The handle of a command list.</p>
</dd>

### -param <i>hQueryHeap</i> 

<dd>
<p>The handle of a query heap.</p>
</dd>

### -param <i>QueryType</i> 

<dd>
<p>A query type.</p>
</dd>

### -param <i>StartElement</i> 

<dd>
<p>The value of the start element.</p>
</dd>

### -param <i>ElementCount</i> 

<dd>
<p>The element count.</p>
</dd>

### -param <i>hDrvDestinationBuffer</i> 

<dd>
<p>The handle of a destination buffer.</p>
</dd>

### -param <i>DestinationOffset</i> 

<dd>
<p>The destination offset.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>Resolve functionality is used by applications to transform a query result previously stored in a query heap into the API defined format.  The resolved data is stored in a buffer.  The results can then be consumed by a shader, predication, or mapped and read on the CPU.</p>

<p>Resolve functionality is used by applications to transform a query result previously stored in a query heap into the API defined format.  The resolved data is stored in a buffer.  The results can then be consumed by a shader, predication, or mapped and read on the CPU.</p>

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