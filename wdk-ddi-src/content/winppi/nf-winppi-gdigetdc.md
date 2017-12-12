---
UID: NF.winppi.GdiGetDC
title: GdiGetDC function
author: windows-driver-content
description: The GdiGetDC function returns a handle to a printer's device context.
old-location: print\gdigetdc.htm
old-project: print
ms.assetid: f8aacb6d-4e8a-4fdb-902c-3d0efbc40f08
ms.author: windowsdriverdev
ms.date: 12/9/2017
ms.keywords: GdiGetDC
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
req.alt-api: GdiGetDC
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

# GdiGetDC function



## -description
The <b>GdiGetDC</b> function returns a handle to a printer's device context.



## -syntax

````
HDC GdiGetDC(
   HANDLE SpoolFileHandle
);
````


## -parameters

### -param SpoolFileHandle 

Caller-supplied spool file handle, obtained by a previous call to <a href="print.gdigetspoolfilehandle">GdiGetSpoolFileHandle</a>.


## -returns
If the operation succeeds, the function returns a device context handle. Otherwise the function returns <b>NULL</b>.


## -remarks
The <b>GdiGetDC</b> function is exported by gdi32.dll for use within a print processor's <a href="print.printdocumentonprintprocessor">PrintDocumentOnPrintProcessor</a> function.

A print processor can call <b>GdiGetDC</b> to obtain a printer's device context handle anytime after calling <a href="print.gdigetspoolfilehandle">GdiGetSpoolFileHandle</a>. The print processor can use the context handle to call Win32 device context functions, in order to perform such operations as applying transformations on the print image.

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