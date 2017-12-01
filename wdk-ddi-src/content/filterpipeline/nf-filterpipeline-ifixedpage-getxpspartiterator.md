---
UID: NF.filterpipeline.IFixedPage.GetXpsPartIterator
title: IFixedPage::GetXpsPartIterator
author: windows-driver-content
description: The GetXpsPartIterator method gets an iterator to enumerate all of the parts that are associated with the page.
old-location: print\ifixedpage_getxpspartiterator.htm
old-project: print
ms.assetid: c4605d9c-b12c-4056-bf19-a67df3ef8c8b
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IFixedPage, GetXpsPartIterator, IFixedPage::GetXpsPartIterator
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
req.alt-api: IFixedPage.GetXpsPartIterator
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
req.iface: IFixedPage
---

# IFixedPage::GetXpsPartIterator method



## -description
<p>The <b>GetXpsPartIterator</b> method gets an iterator to enumerate all of the parts that are associated with the page. </p>


## -syntax

````
HRESULT GetXpsPartIterator(
  [out] IXpsPartIterator **pXpsPartIt
);
````


## -parameters
<dl>

### -param <i>pXpsPartIt</i> [out]

<dd>
<p>An iterator that you can use to enumerate all of the parts that are associated with the page.</p>
</dd>
</dl>

## -returns
<p><b>GetXpsPartIterator</b> returns an <b>HRESULT</b> value.</p>

## -remarks
<p>Filters should not add or delete parts while using the iterator that the <b>GetXpsPartIterator</b> method retrieves.</p>

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