---
UID: NF.winsplp.PrintDocumentOnPrintProcessor
title: PrintDocumentOnPrintProcessor
author: windows-driver-content
description: A print processor's PrintDocumentOnPrintProcessor function converts a print job from a spooled format into raw data that can be sent to a print monitor.
old-location: print\printdocumentonprintprocessor.htm
old-project: print
ms.assetid: 1360a699-e312-40be-bf2f-b73b1419cfc5
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: PrintDocumentOnPrintProcessor
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winsplp.h
req.include-header: Winsplp.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PrintDocumentOnPrintProcessor
req.alt-loc: Nwprint.lib,Nwprint.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Nwprint.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# PrintDocumentOnPrintProcessor function



## -description
<p>A print processor's <code>PrintDocumentOnPrintProcessor</code> function converts a print job from a spooled format into raw data that can be sent to a print monitor.</p>


## -syntax

````
BOOL PrintDocumentOnPrintProcessor(
  _In_ HANDLE hPrintProcessor,
  _In_ LPWSTR pDocumentName
);
````


## -parameters
<dl>

### -param hPrintProcessor [in]

<dd>
<p>Caller-supplied print processor handle. This is the handle returned by a previous call to <a href="..\winsplp\nf-winsplp-openprintprocessor.md">OpenPrintProcessor</a>.</p>
</dd>

### -param pDocumentName [in]

<dd>
<p>Caller-supplied pointer to the document name.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function should return <b>TRUE</b>. If the operation fails, the function should call <b>SetLastError</b> to set an error code, and then return <b>FALSE</b>.</p>

## -remarks
<p>Print processors are required to export a <code>PrintDocumentOnPrintProcessor</code> function. The spooler calls the function after calling <a href="..\winsplp\nf-winsplp-openprintprocessor.md">OpenPrintProcessor</a>. The function's purpose is to read the contents of the file named by <i>pDocumentName</i>, convert (if necessary) the file's data to a data stream that can be read by printer hardware, and to send the data stream back to the spooler. The spooler can then send the data stream to the appropriate <a href="wdkgloss.p#wdkgloss.print_monitor#wdkgloss.print_monitor"><i>print monitor</i></a>.</p>

<p>If the input format is NT-based operating system EMF, the <code>PrintDocumentOnPrintProcessor</code> function can call <a href="print.gdi_functions_for_print_processors">GDI functions for print processors</a>. For more information, see <a href="https://msdn.microsoft.com/c5e291d9-069c-4877-a167-862ba5794368">Processing a Print Job</a>.</p>

<p>The converted data stream must be sent back to the spooler by calling <b>WritePrinter</b>, which is described in the Microsoft Windows SDK documentation. For more information, see <a href="https://msdn.microsoft.com/c5e291d9-069c-4877-a167-862ba5794368">Processing a Print Job</a>.</p>

<p>The <code>PrintDocumentOnPrintProcessor</code> function must be written to handle requests to pause, resume, or cancel the print job. For more information, see <a href="..\winsplp\nf-winsplp-controlprintprocessor.md">ControlPrintProcessor</a>.</p>

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
<dt>Winsplp.h (include Winsplp.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Nwprint.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\winsplp\nf-winsplp-openprintprocessor.md">OpenPrintProcessor</a>
</dt>
<dt>
<a href="..\winsplp\nf-winsplp-controlprintprocessor.md">ControlPrintProcessor</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20PrintDocumentOnPrintProcessor function%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
