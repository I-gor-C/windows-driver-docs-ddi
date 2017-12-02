---
UID: NF.prcomoem.IPrintOemDriverUni.DrvWriteAbortBuf
title: IPrintOemDriverUni::DrvWriteAbortBuf
author: windows-driver-content
description: The IPrintOemDriverUni::DrvWriteAbortBuf method is provided by the Unidrv driver to allow an OEM rendering plug-in to send printer clean-up code after a user terminates a print job.
old-location: print\iprintoemdriveruni_drvwriteabortbuf.htm
old-project: print
ms.assetid: 4f7aff9b-32cf-42a0-ba3b-ddc87ecdb8c3
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemDriverUni, DrvWriteAbortBuf, IPrintOemDriverUni::DrvWriteAbortBuf
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
req.alt-api: IPrintOemDriverUni.DrvWriteAbortBuf
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

# IPrintOemDriverUni::DrvWriteAbortBuf method



## -description
<p>The <code>IPrintOemDriverUni::DrvWriteAbortBuf</code> method is provided by the Unidrv driver to allow an OEM <a href="https://msdn.microsoft.com/e55ca083-2790-4929-9e5b-6fce49eb0404">rendering plug-in</a> to send printer clean-up code after a user terminates a print job.</p>


## -syntax

````
HRESULT DrvWriteAbortBuf(
   PDEVOBJ pdevobj,
   PVOID   pBuffer,
   DWORD   cbSize,
   DWORD   dwWait
);
````


## -parameters
<dl>

### -param pdevobj 

<dd>
<p>Caller-supplied pointer to a <a href="..\printoem\ns-printoem--devobj.md">DEVOBJ</a> structure.</p>
</dd>

### -param pBuffer 

<dd>
<p>Caller-supplied pointer to a buffer containing a code fragment to be sent to the printer.</p>
</dd>

### -param cbSize 

<dd>
<p>Caller-supplied number of bytes in the buffer pointed to by <i>pBuffer</i>.</p>
</dd>

### -param dwWait 

<dd>
<p>Caller-supplied length of time the printer must wait, in milliseconds, before it can start a new print job after the current job is aborted. </p>
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
<p>OEMs use <a href="print.iprintoemdriveruni_drvwritespoolbuf">IPrintOemDriverUni::DrvWriteSpoolBuf</a> to send output to the printer. If a print job is terminated by the user, <code>IPrintOemDriverUni::DrvWriteSpoolBuf</code> returns E_FAIL and can no longer be used to send any data to the printer. When this occurs, certain printers must have a clean-up code fragment sent to them, resetting their states before they can start new print jobs. For these printers, <code>IPrintOemDriverUni::DrvWritetAbortBuf</code> is used to send this code fragment to the printer.</p>

<p><code>IPrintOemDriverUni::DrvWriteAbortBuf</code> can only be called after <code>IPrintOemDriverUni::DrvWriteSpoolBuf</code> has returned E_FAIL. <code>IPrintOemDriverUni::DrvWriteAbortBuf</code> should not be called more than once per job. </p>

<p>Rendering plug-ins are described in <a href="https://msdn.microsoft.com/b7761209-1f6f-4288-af47-4ed855c2e629">Customizing Microsoft's Printer Drivers</a>.</p>

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