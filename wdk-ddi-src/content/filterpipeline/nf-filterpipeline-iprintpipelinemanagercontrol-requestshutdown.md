---
UID: NF.filterpipeline.IPrintPipelineManagerControl.RequestShutdown
title: IPrintPipelineManagerControl::RequestShutdown
author: windows-driver-content
description: The RequestShutdown method requests that a pipeline be shut down.
old-location: print\iprintpipelinemanagercontrol_requestshutdown.htm
old-project: print
ms.assetid: dfb0d7d1-4e82-4471-814b-4b8c4929c709
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintPipelineManagerControl, RequestShutdown, IPrintPipelineManagerControl::RequestShutdown
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
req.alt-api: IPrintPipelineManagerControl.RequestShutdown
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
req.iface: IPrintPipelineManagerControl
---

# IPrintPipelineManagerControl::RequestShutdown method



## -description
<p>The <code>RequestShutdown</code> method requests that a pipeline be shut down.</p>


## -syntax

````
HRESULT RequestShutdown(
  [in] HRESULT       hrReason,
  [in] IImgErrorInfo *pReason
);
````


## -parameters
<dl>

### -param <i>hrReason</i> [in]

<dd>
<p>An <b>HRESULT</b> value that indicates the reason for the lack of memory.</p>
</dd>

### -param <i>pReason</i> [in]

<dd>
<p>Not used. Set to <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><code>RequestShutdown</code> returns an <b>HRESULT</b> value.</p>

## -remarks
<p>A filter that uses the <a href="print.ixpsdocumentconsumer">IXpsDocumentConsumer</a> interface must call <code>IPrintPipelineManagerControl::RequestShutdown</code> before it calls <a href="print.ixpsdocumentconsumer_closesender">IXpsDocumentConsumer::CloseSender</a> to shut down the pipeline. Calling <b>IXpsDocumentConsumer::CloseSender</b> first can produce an invalid XPS document and cause an error. </p>

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