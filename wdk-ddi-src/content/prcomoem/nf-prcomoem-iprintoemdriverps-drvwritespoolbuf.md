---
UID: NF.prcomoem.IPrintOemDriverPS.DrvWriteSpoolBuf
title: IPrintOemDriverPS::DrvWriteSpoolBuf
author: windows-driver-content
description: The IPrintOemDriverPS::DrvWriteSpoolBuf method is provided by the Pscript5 driver so that rendering plug-ins can send printer data to the spooler.
old-location: print\iprintoemdriverps_drvwritespoolbuf.htm
old-project: print
ms.assetid: 91eb36b3-ea05-4a5e-8bba-47c262a4fa4a
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemDriverPS, DrvWriteSpoolBuf, IPrintOemDriverPS::DrvWriteSpoolBuf
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
req.alt-api: IPrintOemDriverPS.DrvWriteSpoolBuf
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
req.iface: IPrintOemDriverPS
req.product: Windows 10 or later.
---

# IPrintOemDriverPS::DrvWriteSpoolBuf method



## -description
<p>The <code>IPrintOemDriverPS::DrvWriteSpoolBuf</code> method is provided by the Pscript5 driver so that <a href="NULL">rendering plug-ins</a> can send printer data to the spooler.</p>


## -syntax

````
HRESULT DrvWriteSpoolBuf(
        PDEVOBJ pdevobj,
        PVOID   pBuffer,
        DWORD   cbSize,
  [out] DWORD   *pdwResult
);
````


## -parameters
<dl>

### -param <i>pdevobj</i> 

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547573">DEVOBJ</a> structure.</p>
</dd>

### -param <i>pBuffer</i> 

<dd>
<p>Caller-supplied pointer to a buffer containing data to be sent to the print spooler.</p>
</dd>

### -param <i>cbSize</i> 

<dd>
<p>Caller-supplied value representing the size, in bytes, of the buffer pointed to by <i>pBuffer</i>.</p>
</dd>

### -param <i>pdwResult</i> [out]

<dd>
<p>Receives a method-supplied value representing the number of bytes sent to the spooler.</p>
</dd>
</dl>

## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

## -remarks
<p>Rendering plug-ins are described in <a href="NULL">Customizing Microsoft's Printer Drivers</a>.</p>

<p>Rendering plug-ins are described in <a href="NULL">Customizing Microsoft's Printer Drivers</a>.</p>

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