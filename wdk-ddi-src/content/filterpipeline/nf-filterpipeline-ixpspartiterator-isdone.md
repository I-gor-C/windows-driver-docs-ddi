---
UID: NF.filterpipeline.IXpsPartIterator.IsDone
title: IXpsPartIterator::IsDone
author: windows-driver-content
description: The IsDone method determines whether the iterator has finished the iteration.
old-location: print\ixpspartiterator_isdone.htm
old-project: print
ms.assetid: 80877e8e-378f-4849-a8ce-b0651fdc2755
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IXpsPartIterator, IsDone, IXpsPartIterator::IsDone
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
req.alt-api: IXpsPartIterator.IsDone
req.alt-loc: Filterpipeline.h
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

# IXpsPartIterator::IsDone method



## -description
<p>The <code>IsDone</code> method determines whether the iterator has finished  the iteration.</p>


## -syntax

````
BOOL STDMETHODCALLTYPE IsDone(
    None
);
````


## -parameters
<dl>

### -param <i>None</i> 

<dd></dd>
</dl>

## -returns
<p><code>IsDone</code> returns <b>true</b> if the iterator has finished iterating.</p>

## -remarks


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