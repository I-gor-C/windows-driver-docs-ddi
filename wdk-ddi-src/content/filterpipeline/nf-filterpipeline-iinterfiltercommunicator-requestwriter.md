---
UID: NF.filterpipeline.IInterFilterCommunicator.RequestWriter
title: IInterFilterCommunicator::RequestWriter
author: windows-driver-content
description: The RequestWriter method retrieves the writer interface for an IInterFilterCommunicator object.
old-location: print\iinterfiltercommunicator_requestwriter.htm
old-project: print
ms.assetid: 1f0684f0-e15e-491f-ba09-314f831d7ba9
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IInterFilterCommunicator, RequestWriter, IInterFilterCommunicator::RequestWriter
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: filterpipeline.h
req.include-header: Filterpipeline.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IInterFilterCommunicator.RequestWriter
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
req.iface: IInterFilterCommunicator
---

# IInterFilterCommunicator::RequestWriter method



## -description
<p>The <b>RequestWriter</b> method retrieves the writer interface for an <b>IInterFilterCommunicator</b> object.</p>


## -syntax

````
HRESULT RequestWriter(
  [out] void **ppIWriter
);
````


## -parameters
<dl>

### -param <i>ppIWriter</i> [out]

<dd>
<p>A variable that receives the writer interface object that <b>RequestWriter</b> retrieves.</p>
</dd>
</dl>

## -returns
<p><b>RequestWriter</b> returns an <b>HRESULT</b> value.</p>

## -remarks
<p>The <b>IInterFilterCommunicator</b> object is passed to each filter in the <a href="print.iprintpipelinefilter_initializefilter">IPrintPipelineFilter::InitializeFilter</a> method. The filter uses the <b>RequestWriter</b> method to get the writer interface for the object. The universally unique identifier (UUID) for the object is declared in the <a href="NULL">filter pipeline configuration file</a>.</p>

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
<dt>Filterpipeline.h (include Filterpipeline.h)</dt>
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

## -see-also
<dl>
<dt>
<a href="print.iprintpipelinefilter_initializefilter">IPrintPipelineFilter::InitializeFilter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IInterFilterCommunicator::RequestWriter method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
