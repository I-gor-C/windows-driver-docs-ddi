---
UID: NF.winppi.GdiGetPageHandle
title: GdiGetPageHandle
author: windows-driver-content
description: The GdiGetPageHandle function returns a handle to the specified page within a print job.
old-location: print\gdigetpagehandle.htm
old-project: print
ms.assetid: 7eaed9d2-20fa-4cf1-b924-fbe1443535e9
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: GdiGetPageHandle
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
req.alt-api: GdiGetPageHandle
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

# GdiGetPageHandle function



## -description
<p>The <b>GdiGetPageHandle</b> function returns a handle to the specified page within a print job.</p>


## -syntax

````
HANDLE GdiGetPageHandle(
   HANDLE  SpoolFileHandle,
   DWORD   Page,
   LPDWORD pdwPageType
);
````


## -parameters
<dl>

### -param <i>SpoolFileHandle</i> 

<dd>
<p>Caller-supplied spool file handle, obtained by a previous call to <a href="..\winppi\nf-winppi-gdigetspoolfilehandle.md">GdiGetSpoolFileHandle</a>.</p>
</dd>

### -param <i>Page</i> 

<dd>
<p>Caller-supplied page number.</p>
</dd>

### -param <i>pdwPageType</i> 

<dd>
<p>Caller-supplied pointer to a location that receives the page type. The possible page types are shown in the following table:</p>
<table>
<tr>
<th>Page Type</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>EMF_PP_FORM</p>
</td>
<td>
<p>The page is a form or has a watermark. (Not currently supported.)</p>
</td>
</tr>
<tr>
<td>
<p>EMF_PP_NORMAL</p>
</td>
<td>
<p>The page is a normal page.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function returns <b>TRUE</b>. Otherwise the function returns <b>FALSE</b>, and an error code can be obtained by calling <b>GetLastError</b>.</p>

## -remarks
<p>The <b>GdiGetPageHandle</b> function is exported by gdi32.dll for use within a print processor's <a href="..\winsplp\nf-winsplp-printdocumentonprintprocessor.md">PrintDocumentOnPrintProcessor</a> function.</p>

<p>Print processors must obtain a page handle before calling <a href="..\winppi\nf-winppi-gdiplaypageemf.md">GdiPlayPageEMF</a> to draw a page. If a Page value is specified that is too large, the function returns ERROR_NO_MORE_ITEMS.</p>

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