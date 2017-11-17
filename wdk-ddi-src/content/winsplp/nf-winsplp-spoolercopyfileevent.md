---
UID: NF.winsplp.SpoolerCopyFileEvent
title: SpoolerCopyFileEvent
author: windows-driver-content
description: A Point and Print DLL's SpoolerCopyFileEvent function receives notifications of events associated with copying print queue-associated files to a print client, when the client connects to a print server.
old-location: print\spoolercopyfileevent.htm
ms.assetid: 39e9b596-7726-439c-8ad9-a987fdfd3860
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: winsplp.h
req.include-header: Winsplp.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SpoolerCopyFileEvent
req.alt-loc: Mscms.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Mscms.lib
req.dll: Mscms.dll
req.irql: 
ms.keywords: SpoolerCopyFileEvent
req.iface: 
req.product: Windows 10 or later.
---

# SpoolerCopyFileEvent function



## -description
<p>A Point and Print DLL's <code>SpoolerCopyFileEvent</code> function receives notifications of events associated with copying print queue-associated files to a print client, when the client connects to a print server.</p>


## -syntax

````
BOOL SpoolerCopyFileEvent(
  _In_ LPWSTR pszPrinterName,
  _In_ LPWSTR pszKey,
  _In_ DWORD  dwCopyFileEvent
);
````


## -parameters
<dl>

### -param <i>pszPrinterName</i> [in]

<dd>
<p>Caller-supplied pointer to a string representing the printer name.</p>
</dd>

### -param <i>pszKey</i> [in]

<dd>
<p>Caller-supplied pointer to a string representing a subkey under the printer's <b>CopyFiles</b> registry key. This subkey identifies the component to which the Point and Print DLL belongs.</p>
</dd>

### -param <i>dwCopyFileEvent</i> [in]

<dd>
<p>Caller-supplied flag that identifies the event being reported. Valid flag values are contained in the following table.</p>
<table>
<tr>
<th>Flag</th>
<th>When Received</th>
<th>Where Received</th>
</tr>
<tr>
<td>
<p>COPYFILE_EVENT_ADD_PRINTER_CONNECTION</p>
</td>
<td>
<p>After a client application has called <b>AddPrinterConnection</b>.</p>
</td>
<td>
<p>Client copy of <code>SpoolerCopyFileEvent</code>. The calling context is the client application.</p>
</td>
</tr>
<tr>
<td>
<p>COPYFILE_EVENT_DELETE_PRINTER</p>
</td>
<td>
<p>After a call to <b>DeletePrinter</b> has been made.</p>
</td>
<td>
<p>Client copy of <code>SpoolerCopyFileEvent</code>. The calling context is the client's spooler.</p>
</td>
</tr>
<tr>
<td>
<p>COPYFILE_EVENT_DELETE_PRINTER_CONNECTION</p>
</td>
<td>
<p>After a client application has called <b>DeletePrinterConnection</b>.</p>
</td>
<td>
<p>Client copy of <code>SpoolerCopyFileEvent</code>. The calling context is the client application.</p>
</td>
</tr>
<tr>
<td>
<p>COPYFILE_EVENT_FILES_CHANGED</p>
</td>
<td>
<p>After the client has downloaded the files specified under the <b>pszKey</b> subkey of the printer's <b>CopyFiles</b> registry key.</p>
</td>
<td>
<p>Client copy of <code>SpoolerCopyFileEvent</code>. The calling context is the client's spooler.</p>
</td>
</tr>
<tr>
<td>
<p>COPYFILE_EVENT_SET_PRINTER_DATAEX</p>
</td>
<td>
<p>After a call to <b>SetPrinterDataEx</b> has been processed on the server.</p>
</td>
<td>
<p>Server copy of <code>SpoolerCopyFileEvent</code>. The calling context is the client application, by impersonation.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>If the function encounters errors, the function should return <b>FALSE</b>. Otherwise, it should return <b>TRUE</b>.</p>

## -remarks
<p>All <a href="NULL">Point and Print DLLs</a> must export a <code>SpoolerCopyFileEvent</code> function, which is called by the print spooler. Its purpose is to allow a Point and Print DLL to be notified of events related to the downloading of print queue-associated files, from a print server to a client system, when an application on the client connects to the server. For a complete description of the steps involved in creating a Point and Print connection, see <a href="NULL">Supporting Point and Print</a>.</p>

<p>A Point and Print DLL executes on both the server and the client. The <code>SpoolerCopyFileEvent</code> function can determine where it is executing by reading the contents of <i>dwCopyFileEvent</i>, which supplies a flag indicating the event. The function should process the event and return. If no processing is necessary, the function should just return <b>TRUE</b>.</p>

<p>If <i>dwCopyFileEvent</i> is COPYFILE_EVENT_ADD_PRINTER_CONNECTION or COPYFILE_EVENT_ADD_PRINTER_CONNECTION, the string supplied by <i>pszPrinterName</i> includes the server name.</p>

<p>All <a href="NULL">Point and Print DLLs</a> must export a <code>SpoolerCopyFileEvent</code> function, which is called by the print spooler. Its purpose is to allow a Point and Print DLL to be notified of events related to the downloading of print queue-associated files, from a print server to a client system, when an application on the client connects to the server. For a complete description of the steps involved in creating a Point and Print connection, see <a href="NULL">Supporting Point and Print</a>.</p>

<p>A Point and Print DLL executes on both the server and the client. The <code>SpoolerCopyFileEvent</code> function can determine where it is executing by reading the contents of <i>dwCopyFileEvent</i>, which supplies a flag indicating the event. The function should process the event and return. If no processing is necessary, the function should just return <b>TRUE</b>.</p>

<p>If <i>dwCopyFileEvent</i> is COPYFILE_EVENT_ADD_PRINTER_CONNECTION or COPYFILE_EVENT_ADD_PRINTER_CONNECTION, the string supplied by <i>pszPrinterName</i> includes the server name.</p>

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
<dt>Mscms.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Mscms.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549896">GenerateCopyFilePaths</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20SpoolerCopyFileEvent function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
