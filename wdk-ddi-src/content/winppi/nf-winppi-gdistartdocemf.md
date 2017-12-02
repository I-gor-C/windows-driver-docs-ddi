---
UID: NF.winppi.GdiStartDocEMF
title: GdiStartDocEMF
author: windows-driver-content
description: The GdiStartDocEMF function performs initialization operations for an EMF-formatted print job.
old-location: print\gdistartdocemf.htm
old-project: print
ms.assetid: aca4534a-871e-4d86-b329-cb4f84611a29
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: GdiStartDocEMF
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
req.alt-api: GdiStartDocEMF
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

# GdiStartDocEMF function



## -description
<p>The <b>GdiStartDocEMF</b> function performs initialization operations for an EMF-formatted print job.</p>


## -syntax

````
BOOL GdiStartDocEMF(
   HANDLE   SpoolFileHandle,
   DOCINFOW *pDocInfo
);
````


## -parameters
<dl>

### -param SpoolFileHandle 

<dd>
<p>Caller-supplied spool file handle, obtained by a previous call to <a href="..\winppi\nf-winppi-gdigetspoolfilehandle.md">GdiGetSpoolFileHandle</a>.</p>
</dd>

### -param pDocInfo 

<dd>
<p>Caller-supplied pointer to a DOCINFOW structure (described in the Microsoft Window SDK documentation).</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function returns <b>TRUE</b>. Otherwise the function returns <b>FALSE</b>, and an error code can be obtained by calling <b>GetLastError</b>.</p>

## -remarks
<p>The <b>GdiStartDocEMF</b> function is exported by gdi32.dll for use within a print processor's <a href="..\winsplp\nf-winsplp-printdocumentonprintprocessor.md">PrintDocumentOnPrintProcessor</a> function.</p>

<p>The function performs initializations that must take place before a print job's EMF records can be played. The function calls the spooler's <b>StartDoc</b> function (described in the Window SDK documentation), which in turn calls the printer driver's <a href="display.drvstartdoc">DrvStartDoc</a> function.</p>

<p>The print processor must set the <b>lpszOutput</b> member of the DOCINFOW structure to the output file name contained in the <a href="..\winsplp\ns-winsplp--printprocessoropendata.md">PRINTPROCESSOROPENDATA</a> structure, previously received by the <a href="..\winsplp\nf-winsplp-openprintprocessor.md">OpenPrintProcessor</a> function.</p>

<p>The print processor must set the <b>lpszDocName</b> member of the DOCINFOW structure to the document name pointer, previously received by the <a href="..\winsplp\nf-winsplp-printdocumentonprintprocessor.md">PrintDocumentOnPrintProcessor</a> function.</p>

<p>For additional information, see <a href="https://msdn.microsoft.com/2ad62308-ab42-4475-ac42-f753d5091251">Using GDI Functions in Print Processors</a>.</p>

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

## -see-also
<dl>
<dt>
<a href="..\winppi\nf-winppi-gdienddocemf.md">GdiEndDocEMF</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20GdiStartDocEMF function%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
