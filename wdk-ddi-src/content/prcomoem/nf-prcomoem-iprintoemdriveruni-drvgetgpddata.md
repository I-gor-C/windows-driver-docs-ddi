---
UID: NF.prcomoem.IPrintOemDriverUni.DrvGetGPDData
title: IPrintOemDriverUni::DrvGetGPDData
author: windows-driver-content
description: The IPrintOemDriverUni::DrvGetGPDData method is provided by the Unidrv driver so that rendering plug-ins can obtain data defined in a printer's GPD file.
old-location: print\iprintoemdriveruni_drvgetgpddata.htm
old-project: print
ms.assetid: cebe8972-4e5a-4382-ac1b-4c326dea46b1
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemDriverUni, DrvGetGPDData, IPrintOemDriverUni::DrvGetGPDData
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
req.alt-api: IPrintOemDriverUni.DrvGetGPDData
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

# IPrintOemDriverUni::DrvGetGPDData method



## -description
<p>The <code>IPrintOemDriverUni::DrvGetGPDData</code> method is provided by the Unidrv driver so that rendering plug-ins can obtain data defined in a printer's <a href="wdkgloss.g#wdkgloss.generic_printer_description__gpd_#wdkgloss.generic_printer_description__gpd_"><i>GPD</i></a> file.</p>


## -syntax

````
HRESULT DrvGetGPDData(
   PDEVOBJ pdevobj,
   DWORD   dwType,
   PVOID   pInputData,
   PVOID   pBuffer,
   DWORD   cbSize,
   PDWORD  pcbNeeded
);
````


## -parameters
<dl>

### -param pdevobj 

<dd>
<p>Caller-supplied pointer to a <a href="..\printoem\ns-printoem--devobj.md">DEVOBJ</a> structure.</p>
</dd>

### -param dwType 

<dd>
<p>Caller-supplied flag indicating the type of GPD data being requested. Currently, the following flag is the only one defined:</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>GPD_OEMCUSTOMDATA</p>
</td>
<td>
<p>The method returns the string associated with a GPD file's *<b>OEMCustomData</b> entry.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param pInputData 

<dd>
<p>Reserved. Must be zero.</p>
</dd>

### -param pBuffer 

<dd>
<p>Caller-supplied pointer to a buffer to receive the requested information.</p>
</dd>

### -param cbSize 

<dd>
<p>Caller-supplied size, in bytes, of the buffer pointed to by <i>pBuffer</i>.</p>
</dd>

### -param pcbNeeded 

<dd>
<p>Receives the driver-supplied minimum buffer size, in bytes, required to contain the requested information.</p>
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
<p>If the buffer specified by <i>pBuffer</i> and <i>cbSize</i> is too small to receive the requested information, Unidrv supplies the required buffer size in the location pointed to by <i>pcbNeeded</i>, returns E_FAIL, and sets the error code to ERROR_INSUFFICIENT_BUFFER.</p>

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