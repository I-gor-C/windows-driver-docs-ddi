---
UID: NF.ks.KsLoadResource
title: KsLoadResource
author: windows-driver-content
description: Copies (loads) a resource from the given image.
old-location: stream\ksloadresource.htm
ms.assetid: a7b9dcca-ce89-4fde-9e58-3c4a675227bc
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsLoadResource
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
ms.keywords: KsLoadResource
req.iface: 
---

# KsLoadResource function



## -description
<p>Copies (loads) a resource from the given image. </p>


## -syntax

````
NTSTATUS KsLoadResource(
  _In_      PVOID     ImageBase,
  _In_      POOL_TYPE PoolType,
  _In_      ULONG_PTR ResourceName,
  _In_      ULONG     ResourceType,
  _Out_     PVOID     *Resource,
  _Out_opt_ PULONG    ResourceSize
);
````


## -parameters
<dl>

### -param <i>ImageBase</i> [in]

<dd>
<p>Pointer to the image base</p>
</dd>

### -param <i>PoolType</i> [in]

<dd>
<p>Pool type to use when copying resource</p>
</dd>

### -param <i>ResourceName</i> [in]

<dd>
<p>Resource name.</p>
</dd>

### -param <i>ResourceType</i> [in]

<dd>
<p>Resource type</p>
</dd>

### -param <i>Resource</i> [out]

<dd>
<p>Pointer to resultant resource memory.</p>
</dd>

### -param <i>ResourceSize</i> [out, optional]

<dd>
<p>Pointer to ULONG value to receive the size of the resource.</p>
</dd>
</dl>

## -returns
<p>STATUS_SUCCESS if successful, STATUS_INSUFFICIENT_RESOURCES if memory cannot be allocated, otherwise an appropriate error code.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>