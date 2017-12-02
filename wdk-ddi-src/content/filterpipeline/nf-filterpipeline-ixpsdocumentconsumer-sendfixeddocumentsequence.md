---
UID: NF.filterpipeline.IXpsDocumentConsumer.SendFixedDocumentSequence
title: IXpsDocumentConsumer::SendFixedDocumentSequence
author: windows-driver-content
description: The SendFixedDocumentSequence method sends a fixed document sequence to the pipeline.
old-location: print\ixpsdocumentconsumer_sendfixeddocumentsequence.htm
old-project: print
ms.assetid: e2541943-7e0c-45ca-bdfe-2d48581f62a4
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IXpsDocumentConsumer, SendFixedDocumentSequence, IXpsDocumentConsumer::SendFixedDocumentSequence
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
req.alt-api: IXpsDocumentConsumer.SendFixedDocumentSequence
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
req.iface: IXpsDocumentConsumer
---

# IXpsDocumentConsumer::SendFixedDocumentSequence method



## -description
<p>The <b>SendFixedDocumentSequence</b> method sends a fixed document sequence to the pipeline.</p>


## -syntax

````
HRESULT SendFixedDocumentSequence(
  [in] IFixedDocumentSequence *pIFixedDocumentSequence
);
````


## -parameters
<dl>

### -param pIFixedDocumentSequence [in]

<dd>
<p>A pointer to an XPS fixed document sequence object.</p>
</dd>
</dl>

## -returns
<p><code>SendFixedDocumentSequence</code> returns an <b>HRESULT</b> value.</p>

## -remarks
<p>Only one <a href="print.ifixeddocumentsequence">IFixedDocumentSequence</a> interface can be sent. The <code>SendFixedDocumentSequence</code> method will fail if a filter submits more than one such interface for the same print job.</p>

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