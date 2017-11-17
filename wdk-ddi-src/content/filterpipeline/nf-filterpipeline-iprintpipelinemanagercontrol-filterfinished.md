---
UID: NF.filterpipeline.IPrintPipelineManagerControl.FilterFinished
title: IPrintPipelineManagerControl::FilterFinished
author: windows-driver-content
description: The FilterFinished method reports that a filter is finished processing.
old-location: print\iprintpipelinemanagercontrol_filterfinished.htm
ms.assetid: 6393b959-f67a-42e8-bb2b-e830bcf0d45f
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: filterpipeline.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintPipelineManagerControl.FilterFinished
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
ms.keywords: IPrintPipelineManagerControl, FilterFinished, IPrintPipelineManagerControl::FilterFinished
req.iface: IPrintPipelineManagerControl
---

# IPrintPipelineManagerControl::FilterFinished method



## -description
<p>The <code>FilterFinished</code> method reports that a filter is finished processing.</p>


## -syntax

````
HRESULT STDMETHODCALLTYPE FilterFinished(
    None
);
````


## -parameters
<dl>

### -param <i>None</i> 

<dd></dd>
</dl>

## -returns
<p><code>FilterFinished</code> returns an <b>HRESULT</b>.</p>

## -remarks
<p>The filter does not need to call the <code>FilterFinished</code> method. The filter pipeline assumes the filter has finished when the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554301">IPrintPipelineFilter::StartOperation</a> method returns. <code>FilterFinished</code> is provided for compatibility and, when called, it does nothing but returns.</p>

<p>The filter does not need to call the <code>FilterFinished</code> method. The filter pipeline assumes the filter has finished when the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554301">IPrintPipelineFilter::StartOperation</a> method returns. <code>FilterFinished</code> is provided for compatibility and, when called, it does nothing but returns.</p>

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