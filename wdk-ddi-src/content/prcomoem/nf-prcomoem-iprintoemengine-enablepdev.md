---
UID: NF.prcomoem.IPrintOemEngine.EnablePDEV
title: IPrintOemEngine::EnablePDEV
author: windows-driver-content
description: TBD.
old-location: print\iprintoemengine_enablepdev.htm
ms.assetid: F84B7A8F-5B75-4E2F-93EB-AFFE24637647
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: prcomoem.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemEngine::EnablePDEV
req.alt-loc: 
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
ms.keywords: IPrintOemEngine, EnablePDEV, IPrintOemEngine::EnablePDEV
req.iface: IPrintOemEngine
req.product: Windows 10 or later.
---

# IPrintOemEngine::EnablePDEV method



## -description
<p>TBD</p>


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

### -param <i>pdevobj</i> 

<dd>
<p>TBD</p>
</dd>

### -param <i>pPrinterName</i> 

<dd>
<p>TBD</p>
</dd>

### -param <i>cPatterns</i> 

<dd>
<p>TBD</p>
</dd>

### -param <i>phsurfPatterns</i> 

<dd>
<p>TBD</p>
</dd>

### -param <i>cjGdiInfo</i> 

<dd>
<p>TBD</p>
</dd>

### -param <i>pGdiInfo</i> 

<dd>
<p>TBD</p>
</dd>

### -param <i>cjDevInfo</i> 

<dd>
<p>TBD</p>
</dd>

### -param <i>pDevInfo</i> 

<dd>
<p>TBD</p>
</dd>

### -param <i>pded</i> 

<dd>
<p>TBD</p>
</dd>

### -param <i>pDevOem</i> 

<dd>
<p>TBD</p>
</dd>
</dl>

## -returns
<p>TBD</p>

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
<a href="https://msdn.microsoft.com/DE86FA8C-2E27-4B39-B52D-6227AF56F399">IPrintOemEngine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemEngine::EnablePDEV method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
