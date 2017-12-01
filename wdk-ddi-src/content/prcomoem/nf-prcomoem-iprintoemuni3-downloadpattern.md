---
UID: NF.prcomoem.IPrintOemUni3.DownloadPattern
title: IPrintOemUni3::DownloadPattern
author: windows-driver-content
description: The IPrintOemUni3::DownloadPattern method downloads a pattern to a printer.
old-location: print\iprintoemuni3_downloadpattern.htm
old-project: print
ms.assetid: 7604a6df-c73a-4114-916f-1e777a323731
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUni3, DownloadPattern, IPrintOemUni3::DownloadPattern
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
req.alt-api: IPrintOemUni3.DownloadPattern
req.alt-loc: prcomoem.h
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

# IPrintOemUni3::DownloadPattern method



## -description
<p>The <code>IPrintOemUni3::DownloadPattern</code> method downloads a pattern to a printer.</p>


## -syntax

````
HRESULT DownloadPattern(
   PDEVOBJ pdevobj,
   SURFOBJ *psoPattern,
   LONG    lPatternID
);
````


## -parameters
<dl>

### -param <i>pdevobj</i> 

<dd>
<p>A pointer to a <a href="..\printoem\ns-printoem--devobj.md">DEVOBJ</a> structure.</p>
</dd>

### -param <i>psoPattern</i> 

<dd>
<p>A pointer to the <a href="display.surfobj">SURFOBJ</a> structure that contains the pattern to download.</p>
</dd>

### -param <i>lPatternID</i> 

<dd>
<p>The ID of the pattern to download.</p>
</dd>
</dl>

## -returns
<p>If successful, this method should return S_OK. Otherwise, this method should return an appropriate value in the returned HRESULT.</p>

## -remarks
<p>This method is available in Windows Vista and later.</p>

<p>You should implement this method if you want your rendering plug-in, rather than Unidrv, to download a pattern. If implemented, this method is called by <b>DrvRealizeBrush</b> for raster-mode print jobs. This method is not called for vector-mode print jobs.</p>

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

## -see-also
<dl>
<dt>
<a href="display.drvrealizebrush">DrvRealizeBrush</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUni3::DownloadPattern method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
