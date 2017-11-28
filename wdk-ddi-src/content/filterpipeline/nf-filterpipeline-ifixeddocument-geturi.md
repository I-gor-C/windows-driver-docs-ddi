---
UID: NF.filterpipeline.IFixedDocument.GetUri
title: IFixedDocument::GetUri
author: windows-driver-content
description: The GetUri method gets the URI of the fixed document.
old-location: print\ifixeddocument_geturi.htm
old-project: print
ms.assetid: ed19deff-ecb3-4c6c-bbf5-a82a27b5934e
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IFixedDocument, GetUri, IFixedDocument::GetUri
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
req.alt-api: IFixedDocument.GetUri
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
req.iface: IFixedDocument
---

# IFixedDocument::GetUri method



## -description
<p>The <b>GetUri</b> method gets the URI of the fixed document.</p>


## -syntax

````
HRESULT GetUri(
  [out] BSTR *uri
);
````


## -parameters
<dl>

### -param <i>uri</i> [out]

<dd>
<p>The URI of the fixed document.</p>
</dd>
</dl>

## -returns
<p><b>GetUri</b> returns an <b>HRESULT</b> value.</p>

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