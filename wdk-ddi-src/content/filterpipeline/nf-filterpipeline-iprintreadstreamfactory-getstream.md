---
UID: NF.filterpipeline.IPrintReadStreamFactory.GetStream
title: IPrintReadStreamFactory::GetStream
author: windows-driver-content
description: The GetStream method gets the stream interface.
old-location: print\iprintreadstreamfactory_getstream.htm
old-project: print
ms.assetid: 47447f00-a57d-4821-b10e-1b2cf7eaad94
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintReadStreamFactory, GetStream, IPrintReadStreamFactory::GetStream
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
req.alt-api: IPrintReadStreamFactory.GetStream
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
req.iface: IPrintReadStreamFactory
---

# IPrintReadStreamFactory::GetStream method



## -description
<p>The <code>GetStream</code> method gets the stream interface.</p>


## -syntax

````
HRESULT GetStream(
  [out] IPrintReadStream **ppStream
);
````


## -parameters
<dl>

### -param <i>ppStream</i> [out]

<dd>
<p>A pointer to an <a href="print.iprintreadstream">IPrintReadStream</a> interface. The filter can use this interface to read the contents of the print ticket.</p>
</dd>
</dl>

## -returns
<p><code>GetStream</code> returns an <b>HRESULT</b> value.</p>

## -remarks
<p>The following code example shows how a filter can use <b>IPrintReadStreamFactory</b> to access the per-user print ticket.</p>

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