---
UID: NF.filterpipeline.IPrintPipelineFilter.InitializeFilter
title: IPrintPipelineFilter::InitializeFilter
author: windows-driver-content
description: The InitializeFilter method initializes a filter.
old-location: print\iprintpipelinefilter_initializefilter.htm
old-project: print
ms.assetid: a28a8ee0-24df-45b5-8850-f3b3984b3b64
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintPipelineFilter, InitializeFilter, IPrintPipelineFilter::InitializeFilter
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
req.alt-api: IPrintPipelineFilter.InitializeFilter
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
req.iface: IPrintPipelineFilter
---

# IPrintPipelineFilter::InitializeFilter method



## -description
<p>The <code>InitializeFilter</code> method initializes a filter.</p>


## -syntax

````
HRESULT InitializeFilter(
  [in] IInterFilterCommunicator     *pICommunicator,
  [in] IPrintPipelinePropertyBag    *pIPropertyBag,
  [in] IPrintPipelineManagerControl *pIPipelineControl
);
````


## -parameters
<dl>

### -param <i>pICommunicator</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551050">IInterFilterCommunicator</a> interface.</p>
</dd>

### -param <i>pIPropertyBag</i> [in]

<dd>
<p>A pointer to the<a href="https://msdn.microsoft.com/library/windows/hardware/ff554320">IPrintPipelinePropertyBag</a> interface.</p>
</dd>

### -param <i>pIPipelineControl</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554303">IPrintPipelineManagerControl</a> interface.</p>
</dd>
</dl>

## -returns
<p><code>InitializeFilter</code> returns an <b>HRESULT</b> value. The method should return a value other than "S_OK" or "S_FALSE" if the necessary operations are not performed inside <code>InitializeFilter</code>.</p>

## -remarks
<p>When the <code>InitializeFilter</code> method is called, the filters should:</p>

<p>Get, add, or delete properties from the property bag.</p>

<p>Get the read and write interfaces.</p>

<p>When the <code>InitializeFilter</code> method is called, the filters should:</p>

<p>Get, add, or delete properties from the property bag.</p>

<p>Get the read and write interfaces.</p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551050">IInterFilterCommunicator</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554303">IPrintPipelineManagerControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554320">IPrintPipelinePropertyBag</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintPipelineFilter::InitializeFilter method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
