---
UID: NF.filterpipeline.IXpsPartIterator.Current
title: IXpsPartIterator::Current
author: windows-driver-content
description: The Current method provides the current URI and part.
old-location: print\ixpspartiterator_current.htm
old-project: print
ms.assetid: ccc8125a-c571-4267-860a-11fc313e395c
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IXpsPartIterator, Current, IXpsPartIterator::Current
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: filterpipeline.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IXpsPartIterator.Current
req.alt-loc: filterpipeline.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: Filterpipeline.idl
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IXpsPartIterator
---

# IXpsPartIterator::Current method



## -description
<p>The <code>Current</code> method provides the current URI and part.</p>


## -syntax

````
HRESULT Current(
  [out] BSTR     *pUri,
  [out] IUnknown **ppXpsPart
);
````


## -parameters
<dl>

### -param <i>pUri</i> [out]

<dd>
<p>A pointer to the URI of the part. If <b>NULL</b>, the <i>ppXpsPartparameter</i> might still be valid.</p>
</dd>

### -param <i>ppXpsPart</i> [out]

<dd>
<p>The current part in the iterator. If <b>NULL</b>, the <i>pUri</i> parameter might still be valid.</p>
</dd>
</dl>

## -returns
<p><code>Current</code> returns an <b>HRESULT</b> value.</p>

## -remarks
<p>Filters should call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556342">IXpsPartIterator::IsDone</a> method before calling <code>Current</code>. One or both parameters can be <b>NULL</b>.</p>

<p>Filters should call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556342">IXpsPartIterator::IsDone</a> method before calling <code>Current</code>. One or both parameters can be <b>NULL</b>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Filterpipeline.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IDL</p>
</th>
<td width="70%">
<dl>
<dt>Filterpipeline.idl</dt>
</dl>
</td>
</tr>
</table>