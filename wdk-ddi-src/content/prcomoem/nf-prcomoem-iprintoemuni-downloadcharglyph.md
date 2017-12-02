---
UID: NF.prcomoem.IPrintOemUni.DownloadCharGlyph
title: IPrintOemUni::DownloadCharGlyph
author: windows-driver-content
description: The IPrintOemUni::DownloadCharGlyph method enables a rendering plug-in for Unidrv to send a character glyph for a specified soft font to the printer.
old-location: print\iprintoemuni_downloadcharglyph.htm
old-project: print
ms.assetid: 1ce7ebaa-759e-418a-af07-e530b1102567
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUni, DownloadCharGlyph, IPrintOemUni::DownloadCharGlyph
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
req.alt-api: IPrintOemUni.DownloadCharGlyph
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

# IPrintOemUni::DownloadCharGlyph method



## -description
<p>The <code>IPrintOemUni::DownloadCharGlyph</code> method enables a rendering plug-in for Unidrv to send a character glyph for a specified soft font to the printer.</p>


## -syntax

````
HRESULT DownloadCharGlyph(
        PDEVOBJ     pdevobj,
        PUNIFONTOBJ pUFObj,
        HGLYPH      hGlyph,
        PDWORD      pdwWidth,
  [out] DWORD       *pdwResult
);
````


## -parameters
<dl>

### -param pdevobj 

<dd>
<p>Caller-supplied pointer to a <a href="..\printoem\ns-printoem--devobj.md">DEVOBJ</a> structure.</p>
</dd>

### -param pUFObj 

<dd>
<p>Caller-supplied pointer to a <a href="..\printoem\ns-printoem--unifontobj.md">UNIFONTOBJ</a> structure.</p>
</dd>

### -param hGlyph 

<dd>
<p>Caller-supplied glyph handle.</p>
</dd>

### -param pdwWidth 

<dd>
<p>Caller-supplied pointer to receive the method-supplied width of the character.</p>
</dd>

### -param pdwResult [out]

<dd>
<p>Receives a method-supplied value representing the amount of printer memory, in bytes, required to store the character glyph. If the operation fails, the returned value should be zero.</p>
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
<p>The <code>IPrintOemUni::DownloadCharGlyph</code> method is used for supporting soft fonts on printers that do not accept <a href="wdkgloss.p#wdkgloss.pcl#wdkgloss.pcl"><i>PCL</i></a> commands. Its purpose is to enable a rendering plug-in to send a character glyph to the printer.</p>

<p>If a rendering plug-in implements the  <code>IPrintOemUni::DownloadCharGlyph</code> method, Unidrv calls the method immediately after sending the command string specified by the CmdSetCharCode command entry, which is contained in the printer's <a href="wdkgloss.g#wdkgloss.generic_printer_description__gpd_#wdkgloss.generic_printer_description__gpd_"><i>GPD</i></a> file. (GPD files are described in <a href="https://msdn.microsoft.com/1f5d68a1-3552-44a9-a0c5-b3ec5fe22a22">Microsoft Universal Printer Driver</a>.) The method should do the following:</p>

<p>Call the <a href="print.unifontobj_getinfo">UNIFONTOBJ_GetInfo</a> function to obtain the glyph image specified by <i>hGlyph</i>.</p>

<p>Call <a href="print.iprintoemdriveruni_drvwritespoolbuf">IPrintOemDriverUni::DrvWriteSpoolBuf</a> to send the glyph to the printer.</p>

<p>Call the <a href="print.unifontobj_getinfo">UNIFONTOBJ_GetInfo</a> function again to obtain the glyph's width, then store the width in the address pointed to by <i>pdwWidth</i>. </p>

<p>Return the amount of printer memory required to store the glyph by placing it in the location specified by <i>pdwResult</i>.</p>

<p>The <code>IPrintOemUni::DownloadCharGlyph</code> method is optional. If a rendering plug-in implements this method, the plug-in's <a href="print.iprintoemuni_getimplementedmethod">IPrintOemUni::GetImplementedMethod</a> method must return S_OK when it receives "DownloadCharGlyph" as input.</p>

<p>If you implement the <code>IPrintOemUni::DownloadCharGlyph</code> method, you must also implement the <a href="print.iprintoemuni_downloadfontheader">IPrintOemUni::DownloadFontHeader</a> method.</p>

<p>For additional information see <a href="https://msdn.microsoft.com/6e643703-ace1-4660-990c-3a9ca735829d">Customized Font Management</a>.</p>

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