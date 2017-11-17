---
UID: NF.winppi.GdiGetSpoolFileHandle
title: GdiGetSpoolFileHandle
author: windows-driver-content
description: The GdiGetSpoolFileHandle function returns a handle to a print job's EMF file.
old-location: print\gdigetspoolfilehandle.htm
ms.assetid: c820ee94-29c2-4478-884c-49dd68cd713a
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: winppi.h
req.include-header: Winppi.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GdiGetSpoolFileHandle
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
ms.keywords: GdiGetSpoolFileHandle
req.iface: 
req.product: Windows 10 or later.
---

# GdiGetSpoolFileHandle function



## -description
<p>The <b>GdiGetSpoolFileHandle</b> function returns a handle to a print job's EMF file.</p>


## -syntax

````
HANDLE GdiGetSpoolFileHandle(
   LPWSTR     pwszPrinterName,
   LPDEVMODEW pDevmode,
   LPWSTR     pwszDocName
);
````


## -parameters
<dl>

### -param <i>pwszPrinterName</i> 

<dd>
<p>Caller-supplied pointer to a string representing the name of the target printer. See the following Remarks section.</p>
</dd>

### -param <i>pDevmode</i> 

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure. See the following Remarks section.</p>
</dd>

### -param <i>pwszDocName</i> 

<dd>
<p>Caller-supplied pointer to the print job's document name. See the following Remarks section.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function returns a spool file handle. Otherwise the function returns <b>NULL</b>.</p>

## -remarks
<p>The <b>GdiGetSpoolFileHandle</b> function is exported by gdi32.dll for use within a print processor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff560724">PrintDocumentOnPrintProcessor</a> function.</p>

<p>When a print processor calls <b>GdiGetSpoolFileHandle</b>, it should supply arguments as illustrated in the following table.</p>

<p><i>pwszPrinterName</i></p>

<p>Pointer to the printer name received by the print processor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff559604">OpenPrintProcessor</a> function.</p>

<p><i>pDevmode</i></p>

<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560988">PRINTPROCESSOROPENDATA</a> structure, received by the print processor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff559604">OpenPrintProcessor</a> function.</p>

<p><i>pwszDocName</i></p>

<p>Document name pointer received by the print processor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff560724">PrintDocumentOnPrintProcessor</a> function.</p>

<p> </p>

<p>A print processor must call the <b>GdiGetSpoolFileHandle</b> function before calling any other GDI printing functions, because the returned handle must be passed to the other functions. The function calls OpenPrinter to open a connection to the printer, and CreateDC to create a device context for drawing. The print processor can obtain the device context's handle by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549470">GdiGetDC</a>.</p>

<p>For additional information, see <a href="NULL">Using GDI Functions in Print Processors</a>.</p>

<p>The <b>GdiGetSpoolFileHandle</b> function is exported by gdi32.dll for use within a print processor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff560724">PrintDocumentOnPrintProcessor</a> function.</p>

<p>When a print processor calls <b>GdiGetSpoolFileHandle</b>, it should supply arguments as illustrated in the following table.</p>

<p><i>pwszPrinterName</i></p>

<p>Pointer to the printer name received by the print processor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff559604">OpenPrintProcessor</a> function.</p>

<p><i>pDevmode</i></p>

<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560988">PRINTPROCESSOROPENDATA</a> structure, received by the print processor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff559604">OpenPrintProcessor</a> function.</p>

<p><i>pwszDocName</i></p>

<p>Document name pointer received by the print processor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff560724">PrintDocumentOnPrintProcessor</a> function.</p>

<p> </p>

<p>A print processor must call the <b>GdiGetSpoolFileHandle</b> function before calling any other GDI printing functions, because the returned handle must be passed to the other functions. The function calls OpenPrinter to open a connection to the printer, and CreateDC to create a device context for drawing. The print processor can obtain the device context's handle by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549470">GdiGetDC</a>.</p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549449">GdiDeleteSpoolFileHandle</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20GdiGetSpoolFileHandle function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
