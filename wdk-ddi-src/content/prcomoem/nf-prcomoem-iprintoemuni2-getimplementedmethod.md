---
UID: NF.prcomoem.IPrintOemUni2.GetImplementedMethod
title: IPrintOemUni2::GetImplementedMethod
author: windows-driver-content
description: The IPrintOemUni2::GetImplementedMethod method is used by Unidrv to determine which IPrintOemUni2 interface methods a rendering plug-in has implemented.
old-location: print\iprintoemuni2_getimplementedmethod.htm
ms.assetid: a26f7094-8530-4525-b94a-c94dc9ba9629
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemUni2.GetImplementedMethod
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
ms.keywords: IPrintOemUni2, GetImplementedMethod, IPrintOemUni2::GetImplementedMethod
req.iface: IPrintOemUni2
req.product: Windows 10 or later.
---

# IPrintOemUni2::GetImplementedMethod method



## -description
<p>The <code>IPrintOemUni2::GetImplementedMethod</code> method is used by Unidrv to determine which <b>IPrintOemUni2</b> interface methods a rendering plug-in has implemented.</p>


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
<p>Caller-supplied pointer to a string that represents the name of an <b>IPrintOemUni2</b> interface method, such as "ImageProcessing" for <b>IPrintOemUni2::ImageProcessing</b> or "FilterGraphics" for <b>IPrintOemUni2::FilterGraphics</b>.</p>
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
<p>A rendering plug-in for Unidrv must implement the <code>IPrintOemUni2::GetImplementedMethod</code> method, together with several other methods in this interface. For those methods that are optional, <code>IPrintOemUni2::GetImplementedMethod</code> examines the input method name string and returns a value that indicates whether the associated method is implemented within the plug-in. For example, if <code>IPrintOemUni2::GetImplementedMethod</code> is called with the string "ImageProcessing", it should return S_OK if the <b>IPrintOemUni2::ImageProcessing</b> method is implemented and S_FALSE otherwise.  </p>

<p>The <code>IPrintOemUni2::GetImplementedMethod</code> method must recognize the following name strings:</p><dl>
<dd>
<p>"CommandCallback"</p>
</dd>
<dd>
<p>"Compression"</p>
</dd>
<dd>
<p>"DownloadCharGlyph"</p>
</dd>
<dd>
<p>"DownloadFontHeader"</p>
</dd>
<dd>
<p>"FilterGraphics"</p>
</dd>
<dd>
<p>"HalftonePattern"</p>
</dd>
<dd>
<p>"ImageProcessing"</p>
</dd>
<dd>
<p>"MemoryUsage"</p>
</dd>
<dd>
<p>"OutputCharStr"</p>
</dd>
<dd>
<p>"SendFontCmd"</p>
</dd>
<dd>
<p>"TextOutAsBitmap"</p>
</dd>
<dd>
<p>"TTDownloadMethod"</p>
</dd>
<dd>
<p>"TTYGetInfo"</p>
</dd>
<dd>
<p>"WritePrinter"</p>
</dd>
</dl><p>"CommandCallback"</p>

<p>"Compression"</p>

<p>"DownloadCharGlyph"</p>

<p>"DownloadFontHeader"</p>

<p>"FilterGraphics"</p>

<p>"HalftonePattern"</p>

<p>"ImageProcessing"</p>

<p>"MemoryUsage"</p>

<p>"OutputCharStr"</p>

<p>"SendFontCmd"</p>

<p>"TextOutAsBitmap"</p>

<p>"TTDownloadMethod"</p>

<p>"TTYGetInfo"</p>

<p>"WritePrinter"</p>

<p>A rendering plug-in for Unidrv must implement the <code>IPrintOemUni2::GetImplementedMethod</code> method, together with several other methods in this interface. For those methods that are optional, <code>IPrintOemUni2::GetImplementedMethod</code> examines the input method name string and returns a value that indicates whether the associated method is implemented within the plug-in. For example, if <code>IPrintOemUni2::GetImplementedMethod</code> is called with the string "ImageProcessing", it should return S_OK if the <b>IPrintOemUni2::ImageProcessing</b> method is implemented and S_FALSE otherwise.  </p>

<p>The <code>IPrintOemUni2::GetImplementedMethod</code> method must recognize the following name strings:</p><dl>
<dd>
<p>"CommandCallback"</p>
</dd>
<dd>
<p>"Compression"</p>
</dd>
<dd>
<p>"DownloadCharGlyph"</p>
</dd>
<dd>
<p>"DownloadFontHeader"</p>
</dd>
<dd>
<p>"FilterGraphics"</p>
</dd>
<dd>
<p>"HalftonePattern"</p>
</dd>
<dd>
<p>"ImageProcessing"</p>
</dd>
<dd>
<p>"MemoryUsage"</p>
</dd>
<dd>
<p>"OutputCharStr"</p>
</dd>
<dd>
<p>"SendFontCmd"</p>
</dd>
<dd>
<p>"TextOutAsBitmap"</p>
</dd>
<dd>
<p>"TTDownloadMethod"</p>
</dd>
<dd>
<p>"TTYGetInfo"</p>
</dd>
<dd>
<p>"WritePrinter"</p>
</dd>
</dl><p>"CommandCallback"</p>

<p>"Compression"</p>

<p>"DownloadCharGlyph"</p>

<p>"DownloadFontHeader"</p>

<p>"FilterGraphics"</p>

<p>"HalftonePattern"</p>

<p>"ImageProcessing"</p>

<p>"MemoryUsage"</p>

<p>"OutputCharStr"</p>

<p>"SendFontCmd"</p>

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