---
UID: NF.filterpipeline.IFixedDocumentSequence.GetUri
title: IFixedDocumentSequence::GetUri
author: windows-driver-content
description: The GetUri method gets the URI of the fixed document sequence.
old-location: print\ifixeddocumentsequence_geturi.htm
old-project: print
ms.assetid: 45017249-2ea5-43f6-9712-787f52cb6e4b
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IFixedDocumentSequence, GetUri, IFixedDocumentSequence::GetUri
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
req.alt-api: IFixedDocumentSequence.GetUri
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
req.iface: IFixedDocumentSequence
---

# IFixedDocumentSequence::GetUri method



## -description
<p>The <b>GetUri</b> method gets the URI of the fixed document sequence.</p>


## -syntax

````
HRESULT GetUri(
  [out] BSTR *uri
);
````


## -parameters
<dl>

### -param uri [out]

<dd>
<p>The URI of the fixed document sequence.</p>
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