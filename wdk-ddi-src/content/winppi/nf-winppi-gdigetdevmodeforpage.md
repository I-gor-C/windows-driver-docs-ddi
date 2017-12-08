---
UID: NF.winppi.GdiGetDevmodeForPage
title: GdiGetDevmodeForPage function
author: windows-driver-content
description: The GdiGetDevmodeForPage function returns DEVMODEW structures for the specified and previous pages of a print job.
old-location: print\gdigetdevmodeforpage.htm
old-project: print
ms.assetid: 3410e8b1-820f-4892-8d26-d803e3f943da
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: GdiGetDevmodeForPage
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
req.alt-api: GdiGetDevmodeForPage
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
req.product: Windows 10 or later.
---

# GdiGetDevmodeForPage function



## -description
The <b>GdiGetDevmodeForPage</b> function returns <a href="display.devmodew">DEVMODEW</a> structures for the specified and previous pages of a print job.


## -syntax

````
BOOL GdiGetDevmodeForPage(
   HANDLE    SpoolFileHandle,
   DWORD     dwPageNumber,
   PDEVMODEW *pCurrDM,
   PDEVMODEW *pLastDM
);
````


## -parameters

### -param SpoolFileHandle 

Caller-supplied spool file handle, obtained by a previous call to <a href="print.gdigetspoolfilehandle">GdiGetSpoolFileHandle</a>.

### -param dwPageNumber 

Caller-supplied number of the page for which <a href="display.devmodew">DEVMODEW</a> contents are to be returned.

### -param pCurrDM 

Caller-supplied location to receive a pointer to a DEVMODE structure for the page specified by <i>dwPageNumber</i>.

### -param pLastDM 

Caller-supplied location to receive a pointer to a DEVMODE structure for the page previous to the one specified by <i>dwPageNumber</i>.

## -returns
If the operation succeeds, the function returns <b>TRUE</b>. Otherwise it returns <b>FALSE</b>.

## -remarks
The <b>GdiGetDevmodeForPage</b> function is exported by gdi32.dll for use within a print processor's <a href="print.printdocumentonprintprocessor">PrintDocumentOnPrintProcessor</a> function.

Before calling <a href="print.gdiplaypageemf">GdiPlayPageEMF</a> to execute a page's EMF instructions, a print processor must call <b>GdiGetDevmodeForPage</b> to determine if the DEVMODE structure associated with the page to be printed is the same as that of the last page printed. If the two returned DEVMODE structures are not identical, the print processor must perform the following steps, in order, before calling <b>GdiPlayPageEMF</b> for the page:

Call <a href="print.gdiendpageemf">GdiEndPageEMF</a>.

Call <a href="print.gdiresetdcemf">GdiResetDCEMF</a>, specifying the DEVMODE pointed to by <i>pCurrDM</i>.

Call <a href="print.gdistartpageemf">GdiStartPageEMF</a>.

For additional information, see <a href="https://msdn.microsoft.com/2ad62308-ab42-4475-ac42-f753d5091251">Using GDI Functions in Print Processors</a>.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Winppi.h (include Winppi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Gdi32.Lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>Gdi32.dll</dt>
</dl>
</td>
</tr>
</table>