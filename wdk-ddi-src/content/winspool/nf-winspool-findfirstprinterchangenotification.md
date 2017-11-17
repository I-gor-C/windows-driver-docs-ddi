---
UID: NF.winspool.FindFirstPrinterChangeNotification
title: FindFirstPrinterChangeNotification
author: windows-driver-content
description: Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated.
old-location: print\findfirstprinterchangenotification.htm
ms.assetid: f6d2034a-0906-42ea-a4bd-9cdb1b36c5cf
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: winspool.h
req.include-header: Winspool.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FindFirstPrinterChangeNotification
req.alt-loc: WinSpool.drv
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: WinSpool.lib
req.dll: WinSpool.drv
req.irql: 
ms.keywords: FindFirstPrinterChangeNotification
req.iface: 
req.product: Windows 10 or later.
---

# FindFirstPrinterChangeNotification function



## -description

## -syntax

````
BOOL FindFirstPrinterChangeNotification(
   HANDLE hPrinter,
   DWORD  fdwFlags,
   DWORD  fdwOptions,
   HANDLE hNotify,
   PDWORD pfdwStatus,
   PVOID  pPrinterNotifyOptions,
   PVOID  pPrinterNotifyInit
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> 

<dd>
<p>Caller-supplied printer handle, identifying the printer for which event notification is being requested. This handle must have been previously obtained from OpenPrinter (described in the Microsoft Windows SDK documentation).</p>
</dd>

### -param <i>fdwFlags</i> 

<dd>
<p>One or more caller-supplied PRINTER_CHANGE-prefixed flags. For more information, see the description of <b>FindFirstPrinterChangeNotification</b> in the Windows SDK documentation.</p>
</dd>

### -param <i>fdwOptions</i> 

<dd>
<p>Not used.</p>
</dd>

### -param <i>hNotify</i> 

<dd>
<p>Caller-supplied notification handle. This handle must be saved and used as input to <a href="https://msdn.microsoft.com/library/windows/hardware/ff561959">ReplyPrinterChangeNotification</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff559739">PartialReplyPrinterChangeNotification</a>.</p>
</dd>

### -param <i>pfdwStatus</i> 

<dd>
<p>Caller-supplied pointer to a location to receive provider-specified flags. The following flags are defined.</p>
<p></p>
<dl>

### -param <a id="PRINTER_NOTIFY_STATUS_ENDPOINT_"></a><a id="printer_notify_status_endpoint_"></a>PRINTER_NOTIFY_STATUS_ENDPOINT 

<dd>
<p>If set, the print provider supplies print change notifications, by either the polling or the change notification method. (The notification method is identified by the PRINTER_NOTIFY_STATUS_POLL flag.)</p>
</dd>
</dl>
<p></p>
<dl>

### -param <a id="PRINTER_NOTIFY_STATUS_POLL_"></a><a id="printer_notify_status_poll_"></a>PRINTER_NOTIFY_STATUS_POLL 

<dd>
<p>If set, the print application must poll to detect printer changes.</p>
<p>If clear, the print provider notifies the spooler of changes by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff561930">RefreshPrinterChangeNotification</a>.</p>
<p>(See the following Remarks section.)</p>
</dd>
</dl>
<p></p>
<dl>

### -param <a id="PRINTER_NOTIFY_STATUS_INFO_"></a><a id="printer_notify_status_info_"></a>PRINTER_NOTIFY_STATUS_INFO 

<dd>
<p>Not used.</p>
</dd>
</dl>
</dd>

### -param <i>pPrinterNotifyOptions</i> 

<dd>
<p>Caller-supplied pointer to a PRINTER_NOTIFY_OPTIONS structure (described in the Windows SDK documentation).</p>
</dd>

### -param <i>pPrinterNotifyInit</i> 

<dd>
<p>Not used.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function should return <b>TRUE</b>. Otherwise the function should return <b>FALSE</b>.</p>

## -remarks
<p>When the spooler calls a print provider's <b>FindFirstPrinterChangeNotification</b> function, <i>fdwFlags</i> identifies the printer events for which notification is being requested. Additionally, <i>pPrinterNotifyOptions</i> identifies the types of information that the print provider should send to the spooler when one of the specified events occurs.</p>

<p>For a list of the types of notifications an application can request, and for a list of the types of information that can be used to describe an event, see the Windows SDK documentation's description of <b>FindFirstPrinterChangeNotification</b>. Types of events for which an application might request notification include adding or deleting a print job or form. Types of information an application might request include job or form parameters.</p>

<p>If the print provider does not request polling (that is, it does not set PRINTER_NOTIFY_STATUS_POLL in <i>pfdwStatus</i>), it must notify the spooler when events identified by <i>pfwFlags</i> occur. The print provider must supply the types of information identified by <i>pPrinterNotifyOptions</i>, by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff559739">PartialReplyPrinterChangeNotification</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff561959">ReplyPrinterChangeNotification</a>.</p>

<p>If the provider does request polling (that is, it sets PRINTER_NOTIFY_STATUS_POLL), it should not call <b>ReplyPrinterChangeNotification</b>. Instead, the spooler signals the application at regular intervals.</p>

<p>Both polled and nonpolled print provider must return the current state of all requested information types whenever its <a href="https://msdn.microsoft.com/library/windows/hardware/ff561930">RefreshPrinterChangeNotification</a> function is called.</p>

<p>For additional information, see <a href="NULL">Supporting Printer Change Notifications</a>.</p>

<p>When the spooler calls a print provider's <b>FindFirstPrinterChangeNotification</b> function, <i>fdwFlags</i> identifies the printer events for which notification is being requested. Additionally, <i>pPrinterNotifyOptions</i> identifies the types of information that the print provider should send to the spooler when one of the specified events occurs.</p>

<p>For a list of the types of notifications an application can request, and for a list of the types of information that can be used to describe an event, see the Windows SDK documentation's description of <b>FindFirstPrinterChangeNotification</b>. Types of events for which an application might request notification include adding or deleting a print job or form. Types of information an application might request include job or form parameters.</p>

<p>If the print provider does not request polling (that is, it does not set PRINTER_NOTIFY_STATUS_POLL in <i>pfdwStatus</i>), it must notify the spooler when events identified by <i>pfwFlags</i> occur. The print provider must supply the types of information identified by <i>pPrinterNotifyOptions</i>, by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff559739">PartialReplyPrinterChangeNotification</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff561959">ReplyPrinterChangeNotification</a>.</p>

<p>If the provider does request polling (that is, it sets PRINTER_NOTIFY_STATUS_POLL), it should not call <b>ReplyPrinterChangeNotification</b>. Instead, the spooler signals the application at regular intervals.</p>

<p>Both polled and nonpolled print provider must return the current state of all requested information types whenever its <a href="https://msdn.microsoft.com/library/windows/hardware/ff561930">RefreshPrinterChangeNotification</a> function is called.</p>

<p>For additional information, see <a href="NULL">Supporting Printer Change Notifications</a>.</p>

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
<dt>Winspool.h (include Winspool.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>WinSpool.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WinSpool.drv</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559739">PartialReplyPrinterChangeNotification</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561959">ReplyPrinterChangeNotification</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561930">RefreshPrinterChangeNotification</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20FindFirstPrinterChangeNotification function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
