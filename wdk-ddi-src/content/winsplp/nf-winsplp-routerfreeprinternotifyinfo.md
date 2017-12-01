---
UID: NF.winsplp.RouterFreePrinterNotifyInfo
title: RouterFreePrinterNotifyInfo
author: windows-driver-content
description: The print spooler's RouterFreePrinterNotifyInfo function deallocates a specified PRINTER_NOTIFY_INFO structure and its associated PRINTER_NOTIFY_INFO_DATA structure array.
old-location: print\routerfreeprinternotifyinfo.htm
old-project: print
ms.assetid: 11beef0b-061a-4d73-b723-d0214f479503
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: RouterFreePrinterNotifyInfo
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
req.alt-api: RouterFreePrinterNotifyInfo
req.alt-loc: Spoolss.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Spoolss.lib
req.dll: Spoolss.dll
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# RouterFreePrinterNotifyInfo function



## -description
<p>The print spooler's <code>RouterFreePrinterNotifyInfo</code> function deallocates a specified PRINTER_NOTIFY_INFO structure and its associated PRINTER_NOTIFY_INFO_DATA structure array. (These structures are described in the Microsoft Windows SDK documentation.)</p>


## -syntax

````
BOOL RouterFreePrinterNotifyInfo(
  _In_opt_ PPRINTER_NOTIFY_INFO pInfo
);
````


## -parameters
<dl>

### -param <i>pInfo</i> [in, optional]

<dd>
<p>Caller-supplied pointer to a PRINTER_NOTIFY_INFO structure (described in the Windows SDK documentation).</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function returns <b>TRUE</b>. Otherwise the function returns <b>FALSE</b>.</p>

## -remarks
<p>A print provider's <a href="print.refreshprinterchangenotification">RefreshPrinterChangeNotification</a> function should call <code>RouterFreePrinterNotifyInfo</code> to deallocate structures previously allocated by <a href="..\winsplp\nf-winsplp-routerallocprinternotifyinfo.md">RouterAllocPrinterNotifyInfo</a>, but only if <b>RefreshPrinterChangeNotification</b> encounters a error. If <b>RefreshPrinterChangeNotification</b> succeeds, you should assume that the client application will deallocate the structures.</p>

<p>Besides deallocating the specified PRINTER_NOTIFY_INFO structure and its associated PRINTER_NOTIFY_INFO_DATA structure array, the function also deallocates buffer space pointed to by <i>pBuf</i> in any element of the PRINTER_NOTIFY_INFO_DATA structure array.</p>

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
<dt>Spoolss.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Spoolss.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="print.refreshprinterchangenotification">RefreshPrinterChangeNotification</a>
</dt>
<dt>
<a href="..\winsplp\nf-winsplp-routerallocprinternotifyinfo.md">RouterAllocPrinterNotifyInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20RouterFreePrinterNotifyInfo function%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
