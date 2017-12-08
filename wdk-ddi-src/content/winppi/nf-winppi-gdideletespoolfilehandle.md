---
UID: NF.winppi.GdiDeleteSpoolFileHandle
title: GdiDeleteSpoolFileHandle function
author: windows-driver-content
description: The GdiDeleteSpoolFileHandle function releases a spool file handle.
old-location: print\gdideletespoolfilehandle.htm
old-project: print
ms.assetid: ff22498e-404f-42f6-82fd-f0178f6c7789
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: GdiDeleteSpoolFileHandle
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
req.alt-api: GdiDeleteSpoolFileHandle
req.alt-loc: Gdi32.dll,Ext-MS-Win-GDI-Internal-Desktop-L1-1-0.dll,GDI32Full.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Gdi32.lib
req.dll: Gdi32.dll
req.irql: 
req.product: Windows 10 or later.
---

# GdiDeleteSpoolFileHandle function



## -description
The <b>GdiDeleteSpoolFileHandle</b> function releases a spool file handle.


## -syntax

````
BOOL GdiDeleteSpoolFileHandle(
   HANDLE SpoolFileHandle
);
````


## -parameters

### -param SpoolFileHandle 

Caller-supplied spool file handle, obtained by a previous call to <a href="print.gdigetspoolfilehandle">GdiGetSpoolFileHandle</a>.

## -returns
If the operation succeeds, the function returns <b>TRUE</b>. Otherwise the function returns <b>FALSE</b>.

## -remarks
The <b>GdiDeleteSpoolFileHandle</b> function is exported by gdi32.dll for use within a print processor's <a href="print.printdocumentonprintprocessor">PrintDocumentOnPrintProcessor</a> function.

Print processors should call <b>GdiDeleteSpoolFileHandle</b> after calling <a href="print.gdienddocemf">GdiEndDocEMF</a>, when processing a print job's EMF data stream has been completed. The function calls ClosePrinter (described in the Microsoft Window SDK documentation) to close the printer connection.

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
<dt>Gdi32.lib</dt>
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

## -see-also
<dl>
<dt>
<a href="print.gdigetspoolfilehandle">GdiGetSpoolFileHandle</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20GdiDeleteSpoolFileHandle function%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
