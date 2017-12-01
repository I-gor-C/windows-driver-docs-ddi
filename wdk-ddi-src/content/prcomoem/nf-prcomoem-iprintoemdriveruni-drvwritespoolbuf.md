---
UID: NF.prcomoem.IPrintOemDriverUni.DrvWriteSpoolBuf
title: IPrintOemDriverUni::DrvWriteSpoolBuf
author: windows-driver-content
description: The IPrintOemDriverUni::DrvWriteSpoolBuf method is provided by the Unidrv driver so that a rendering plug-in can send printer data to the spooler.
old-location: print\iprintoemdriveruni_drvwritespoolbuf.htm
old-project: print
ms.assetid: e019b88a-bffe-44d2-8031-de37b6a1cf1c
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemDriverUni, DrvWriteSpoolBuf, IPrintOemDriverUni::DrvWriteSpoolBuf
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
req.alt-api: IPrintOemDriverUni.DrvWriteSpoolBuf
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
req.iface: IPrintOemDriverUni
req.product: Windows 10 or later.
---

# IPrintOemDriverUni::DrvWriteSpoolBuf method



## -description
<p>The <code>IPrintOemDriverUni::DrvWriteSpoolBuf</code> method is provided by the Unidrv driver so that a <a href="https://msdn.microsoft.com/e55ca083-2790-4929-9e5b-6fce49eb0404">rendering plug-in</a> can send printer data to the spooler.</p>


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
<p>Caller-supplied pointer to a <a href="..\printoem\ns-printoem--devobj.md">DEVOBJ</a> structure.</p>
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
</dl><p>The operation failed.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

## -remarks
<p>OEMs use the Unidrv helper function <code>IPrintOemDriverUni::DrvWriteSpoolBuf</code> to send output to the printer. If a print job is terminated by the user, <code>IPrintOemDriverUni::DrvWriteSpoolBuf</code> returns E_FAIL and can no longer be used to send any data to the printer. When this occurs, certain printers must have a clean-up code fragment sent to them, resetting their states before they can start new print jobs. For these printers, <a href="print.iprintoemdriveruni_drvwriteabortbuf">IPrintOemDriverUni::DrvWriteAbortBuf</a> can be used to send this code fragment to the printer. </p>

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