---
UID: NF.prcomoem.IPrintOemUni3.GetImplementedMethod
title: IPrintOemUni3::GetImplementedMethod
author: windows-driver-content
description: The IPrintOemUni3::GetImplementedMethod method is used by Unidrv to determine which IPrintOemUni interface methods a rendering plug-in has implemented.
old-location: print\iprintoemuni3_getimplementedmethod.htm
old-project: print
ms.assetid: a1de8e8f-eca1-4630-b689-585027184a08
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUni3, GetImplementedMethod, IPrintOemUni3::GetImplementedMethod
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemUni3.GetImplementedMethod
req.alt-loc: Prcomoem.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IPrintOemUni3
req.product: Windows 10 or later.
---

# IPrintOemUni3::GetImplementedMethod method



## -description
<p>The <code>IPrintOemUni3::GetImplementedMethod</code> method is used by Unidrv to determine which <b>IPrintOemUni</b> interface methods a rendering plug-in has implemented.</p>


## -syntax

````
STDMETHOD GetImplementedMethod(
   PSTR pMethodName
);
````


## -parameters
<dl>

### -param <i>pMethodName</i> 

<dd>
<p>Caller-supplied pointer to a string that represents the name of an <b>IPrintOemUni</b> interface method, such as "ImageProcessing" for <b>IPrintOemUni3::ImageProcessing</b> or "FilterGraphics" for <b>IPrintOemUni3::FilterGraphics</b>.</p>
</dd>
</dl>

## -returns
<p><code>GetImplementedMethod</code> must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded (that is, the specified method is implemented).</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The operation failed (that is, the specified method is not implemented).</p>

<p> </p>

## -remarks
<p>A rendering plug-in for Unidrv must implement the <code>IPrintOemUni3::GetImplementedMethod</code> method, together with several other methods in this interface. For those methods that are optional, <code>IPrintOemUni3::GetImplementedMethod</code> examines the input method name string and returns a value that indicates whether the associated method is implemented within the plug-in. For example, if <code>IPrintOemUni3::GetImplementedMethod</code> is called with the string "ImageProcessing", it should return S_OK if the <b>IPrintOemUni3::ImageProcessing</b> method is implemented and S_FALSE otherwise.  </p>

<p>The <code>IPrintOemUni3::GetImplementedMethod</code> method must recognize the following name strings:</p>

<p>"CommandCallback"</p>

<p>"Compression"</p>

<p>"DownloadCharGlyph"</p>

<p>"DownloadFontHeader"</p>

<p>"DownloadPattern"</p>

<p>"FilterGraphics"</p>

<p>"GetPDEVAdjustment"</p>

<p>"HalftonePattern"</p>

<p>"ImageProcessing"</p>

<p>"MemoryUsage"</p>

<p>"OutputCharStr"</p>

<p>"SendFontCmd"</p>

<p>"SetBandSize"</p>

<p>"TextOutAsBitmap"</p>

<p>"TTDownloadMethod"</p>

<p>"TTYGetInfo"</p>

<p>"WritePrinter"</p>

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
<dt>Prcomoem.h (include Prcomoem.h)</dt>
</dl>
</td>
</tr>
</table>