---
UID: NF.prcomoem.IPrintOemEngine.EnablePDEV
title: IPrintOemEngine::EnablePDEV
author: windows-driver-content
description: .
old-location: print\iprintoemengine_enablepdev.htm
old-project: print
ms.assetid: F84B7A8F-5B75-4E2F-93EB-AFFE24637647
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemEngine, EnablePDEV, IPrintOemEngine::EnablePDEV
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prcomoem.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemEngine.EnablePDEV
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
req.iface: IPrintOemEngine
req.product: Windows 10 or later.
---

# IPrintOemEngine::EnablePDEV method



## -description
<p></p>


## -syntax

````
HRESULT EnablePDEV(
   PDEVOBJ       pdevobj,
   PWSTR         pPrinterName,
   ULONG         cPatterns,
   HSURF         *phsurfPatterns,
   ULONG         cjGdiInfo,
   GDIINFO       *pGdiInfo,
   ULONG         cjDevInfo,
   DEVINFO       *pDevInfo,
   DRVENABLEDATA *pded,
   PDEVOEM       *pDevOem
);
````


## -parameters
<dl>

### -param pdevobj 

<dd></dd>

### -param pPrinterName 

<dd></dd>

### -param cPatterns 

<dd></dd>

### -param phsurfPatterns 

<dd></dd>

### -param cjGdiInfo 

<dd></dd>

### -param pGdiInfo 

<dd></dd>

### -param cjDevInfo 

<dd></dd>

### -param pDevInfo 

<dd></dd>

### -param pded 

<dd></dd>

### -param pDevOem 

<dd></dd>
</dl>

## -returns
<p>If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Prcomoem.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\prcomoem\nn-prcomoem-iprintoemengine.md">IPrintOemEngine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemEngine::EnablePDEV method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
