---
UID: NF.winppi.GdiResetDCEMF
title: GdiResetDCEMF
author: windows-driver-content
description: The GdiResetDCEMF function resets a printer's device context during playback of a spooled EMF print job.
old-location: print\gdiresetdcemf.htm
old-project: print
ms.assetid: ea97cc22-6057-427d-90c1-4f23ced932aa
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: GdiResetDCEMF
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winppi.h
req.include-header: Winppi.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GdiResetDCEMF
req.alt-loc: Gdi32.dll,Ext-MS-Win-GDI-Internal-Desktop-L1-1-0.dll,GDI32Full.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Gdi32.Lib
req.dll: Gdi32.dll
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# GdiResetDCEMF function



## -description
<p>The <b>GdiResetDCEMF</b> function resets a printer's device context during playback of a spooled EMF print job.</p>


## -syntax

````
BOOL GdiResetDCEMF(
   HANDLE    SpoolFileHandle,
   PDEVMODEW pCurrDM
);
````


## -parameters
<dl>

### -param <i>SpoolFileHandle</i> 

<dd>
<p>Caller-supplied spool file handle, obtained by a previous call to <a href="..\winppi\nf-winppi-gdigetspoolfilehandle.md">GdiGetSpoolFileHandle</a>.</p>
</dd>

### -param <i>pCurrDM</i> 

<dd>
<p>Caller-supplied pointer to a <a href="display.devmodew">DEVMODEW</a> structure, obtained by a previous call to <a href="..\winppi\nf-winppi-gdigetdevmodeforpage.md">GdiGetDevmodeForPage</a>.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function returns <b>TRUE</b>. Otherwise the function returns <b>FALSE</b>.</p>

## -remarks
<p>The <b>GdiResetDCEMF</b> function is exported by gdi32.dll for use within a print processor's <a href="..\winsplp\nf-winsplp-printdocumentonprintprocessor.md">PrintDocumentOnPrintProcessor</a> function.</p>

<p>Print processors must call <b>GdiResetDCEMF</b> whenever it is necessary to reset the printer's device context. The function must be called whenever the <a href="..\winppi\nf-winppi-gdigetdevmodeforpage.md">GdiGetDevmodeForPage</a> function indicates that the current document page's <a href="display.devmodew">DEVMODEW</a> structure is not identical to that of the previous document page.</p>

<p>For additional information, see <a href="NULL">Using GDI Functions in Print Processors</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winppi.h (include Winppi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Gdi32.Lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Gdi32.dll</dt>
</dl>
</td>
</tr>
</table>