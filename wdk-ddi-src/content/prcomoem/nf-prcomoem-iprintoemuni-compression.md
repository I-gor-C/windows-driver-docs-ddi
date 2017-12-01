---
UID: NF.prcomoem.IPrintOemUni.Compression
title: IPrintOemUni::Compression
author: windows-driver-content
description: The IPrintOemUni::Compression method can be used with Unidrv-supported printers to provide a customized bitmap compression method.
old-location: print\iprintoemuni_compression.htm
old-project: print
ms.assetid: 02524493-3842-462e-86f6-2ab35998c65e
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUni, Compression, IPrintOemUni::Compression
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
req.alt-api: IPrintOemUni.Compression
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
req.iface: IPrintOemUni
req.product: Windows 10 or later.
---

# IPrintOemUni::Compression method



## -description
<p>The <code>IPrintOemUni::Compression</code> method can be used with Unidrv-supported printers to provide a customized bitmap compression method.</p>


## -syntax

````
HRESULT Compression(
        PDEVOBJ pdevobj,
        PBYTE   pInBuf,
        PBYTE   pOutBuf,
        DWORD   dwInLen,
        DWORD   dwOutLen,
  [out] INT     *piResult
);
````


## -parameters
<dl>

### -param <i>pdevobj</i> 

<dd>
<p>Caller-supplied pointer to a <a href="..\printoem\ns-printoem--devobj.md">DEVOBJ</a> structure.</p>
</dd>

### -param <i>pInBuf</i> 

<dd>
<p>Caller-supplied pointer to input scan line data.</p>
</dd>

### -param <i>pOutBuf</i> 

<dd>
<p>Caller-supplied pointer to an output buffer to receive compressed scan line data.</p>
</dd>

### -param <i>dwInLen</i> 

<dd>
<p>Caller-supplied length of the input data.</p>
</dd>

### -param <i>dwOutLen</i> 

<dd>
<p>Caller-supplied length of the output buffer.</p>
</dd>

### -param <i>piResult</i> [out]

<dd>
<p>Receives a method-supplied result value. If the operation succeeds, this value should be the number of compressed bytes, which must not be larger than the value received for <i>dwOutLen</i>. If an error occurs, or if the method cannot compress, the result value should be -1.</p>
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
<p>The <code>IPrintOemUni::Compression</code> method is used by rendering plug-ins to compress scan line data before it is sent to the print spooler. The method's purpose is to provide support for printer-specific compression methods that are not supported by Unidrv.</p>

<p>If the <code>IPrintOemUni::Compression</code> method is defined, and if the printer's <a href="wdkgloss.g#wdkgloss.generic_printer_description__gpd_#wdkgloss.generic_printer_description__gpd_"><i>GPD</i></a> file contains a CmdEnableOEMComp command entry, Unidrv calls the method each time a scan line is ready to be sent to the print spooler. (For information about the CmdEnableOEMComp command, see <a href="NULL">Raster Data Compression Commands</a>.)</p>

<p>The <i>pInBuf</i> and <i>dwInLen</i> parameter values describe a buffer containing a scan line of image data to be compressed. The <i>pOutBuf</i> and <i>dwOutLen</i> parameter values describe the buffer into which the <code>IPrintOemUni::Compression</code> method should place the compressed data.</p>

<p>Before Unidrv sends a scan line to the print spooler, it tries every enabled compression method to determine which one creates the smallest data stream. After it determines the best compression algorithm (by compressing the data using each method), it spools the printer command that enables the printer to accept the best compressed format, then sends the compressed data to the printer.</p>

<p>Therefore, the <code>IPrintOemUni::Compression</code> method is called for every scan line, whether the compressed data returned by the method is actually used or not. When the method is called, <i>dwOutLen</i> contains the length returned by the best compression method Unidrv has tried up to then. (If no other methods have been tried, <i>dwOutLen</i> contains the uncompressed length.) If the algorithm cannot produce a compressed scan line that is equal to or shorter than <i>dwOutLen</i> bytes, it should return -1 in the location specified by <i>piResult</i>.</p>

<p>If, after Unidrv tries all enabled compression methods, the compressed data returned by <code>IPrintOemUni::Compression</code> has the smallest length, Unidrv sends the buffer to the print spooler, preceded by the command specified by the CmdEnableOEMComp command entry.</p>

<p>If possible, the method's compression algorithm should use the received <i>dwOutLen</i> value to determine whether it can stop the algorithm before completion, to save time if another compression method has already created a better result.</p>

<p>The <code>IPrintOemUni::Compression</code> method is optional. If a rendering plug-in implements this method, the plug-in's <a href="print.iprintoemuni_getimplementedmethod">IPrintOemUni::GetImplementedMethod</a> method must return S_OK when it receives "Compression" as input.</p>

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