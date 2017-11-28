---
UID: NF.filterpipeline.IPrintWriteStream.Close
title: IPrintWriteStream::Close
author: windows-driver-content
description: The Close method closes a stream and ends the writing to that stream. This method is mandatory. You must call this method when the filter is done writing.
old-location: print\iprintwritestream_close.htm
old-project: print
ms.assetid: d3f828bf-854f-4d2d-a869-ee5c002a1728
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintWriteStream, Close, IPrintWriteStream::Close
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
req.alt-api: IPrintWriteStream.Close
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
req.iface: IPrintWriteStream
---

# IPrintWriteStream::Close method



## -description
<p>The <code>Close</code> method closes a stream and ends the writing to that stream. This method is mandatory. You must call this method when the filter is done writing.</p>


## -syntax

````
void STDMETHODCALLTYPE Close(
    None
);
````


## -parameters
<dl>

### -param <i>None</i> 

<dd></dd>
</dl>

## -returns
<p>None</p>

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