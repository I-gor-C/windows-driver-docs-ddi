---
UID: NF.filterpipeline.IPrintPipelineFilter.StartOperation
title: IPrintPipelineFilter::StartOperation
author: windows-driver-content
description: The StartOperation method starts the operation of a filter. The filter reads, processes, and writes data in this method.
old-location: print\iprintpipelinefilter_startoperation.htm
old-project: print
ms.assetid: 87139670-9b51-4ced-9624-2ec9f4726a84
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintPipelineFilter, StartOperation, IPrintPipelineFilter::StartOperation
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
req.alt-api: IPrintPipelineFilter.StartOperation
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
req.iface: IPrintPipelineFilter
---

# IPrintPipelineFilter::StartOperation method



## -description
<p>The <code>StartOperation</code> method starts the operation of a filter. The filter reads, processes, and writes data in this method.</p>


## -syntax

````
HRESULT STDMETHODCALLTYPE StartOperation(
    None
);
````


## -parameters
<dl>

### -param <i>None</i> 

<dd></dd>
</dl>

## -returns
<p><code>StartOperation</code> returns an <b>HRESULT</b> value.</p>

## -remarks
<p>A filter returns the <code>StartOperation</code> call only when the filter processing is complete.</p>

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