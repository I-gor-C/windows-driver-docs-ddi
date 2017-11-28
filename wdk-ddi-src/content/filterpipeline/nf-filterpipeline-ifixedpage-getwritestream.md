---
UID: NF.filterpipeline.IFixedPage.GetWriteStream
title: IFixedPage::GetWriteStream
author: windows-driver-content
description: The GetWriteStream method retrieves the stream object to write page markup to read . You can use this stream to change page markup.
old-location: print\ifixedpage_getwritestream.htm
old-project: print
ms.assetid: 1a095d51-b727-4d89-aa7c-f43998db4c2e
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IFixedPage, GetWriteStream, IFixedPage::GetWriteStream
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
req.alt-api: IFixedPage.GetWriteStream
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

# IFixedPage::GetWriteStream method



## -description
<p>The <b>GetWriteStream</b> method retrieves the stream object to write page markup to  read . You can use this stream to change page markup.</p>


## -syntax

````
HRESULT GetWriteStream(
  [out] IPrintWriteStream **ppWriteStream
);
````


## -parameters
<dl>

### -param <i>ppWriteStream</i> [out]

<dd>
<p>The stream that the filter should use to write page markup to send data.</p>
</dd>
</dl>

## -returns
<p><b>GetWriteStream</b> returns an <b>HRESULT</b>.</p>

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