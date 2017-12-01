---
UID: NF.prcomoem.IPrintOemUI.PrinterEvent
title: IPrintOemUI::PrinterEvent
author: windows-driver-content
description: The IPrintOemUI::PrinterEvent method allows a user interface plug-in to process printer events.
old-location: print\iprintoemui_printerevent.htm
old-project: print
ms.assetid: 214ea4d8-3bf9-4248-8bfa-7180635769be
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUI, PrinterEvent, IPrintOemUI::PrinterEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemUI.PrinterEvent
req.alt-loc: prcomoem.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IPrintOemUI
req.product: Windows 10 or later.
---

# IPrintOemUI::PrinterEvent method



## -description
<p>The <code>IPrintOemUI::PrinterEvent</code> method allows a user interface plug-in to process printer events.</p>


## -syntax

````
HRESULT PrinterEvent(
   PWSTR  pPrinterName,
   INT    iDriverEvent,
   DWORD  dwFlags,
   LPARAM lParam
);
````


## -parameters
<dl>

### -param <i>pPrinterName</i> 

<dd>
<p>Caller-supplied pointer to a NULL-terminated printer name string. The string can identify a local printer ("<i>PrinterName</i>") or remote printer ("\\<i>Machine</i>\<i>PrinterName</i>").</p>
</dd>

### -param <i>iDriverEvent</i> 

<dd>
<p>Caller-supplied value identifying the event that has occurred. For a list of valid values, see <a href="..\winddiui\nf-winddiui-drvprinterevent.md">DrvPrinterEvent</a>.</p>
</dd>

### -param <i>dwFlags</i> 

<dd>
<p>Caller-supplied flags. For a list of valid flags, see <b>DrvPrinterEvent</b>.</p>
</dd>

### -param <i>lParam</i> 

<dd>
<p>Caller-supplied event-specific parameter. For more information, see <b>DrvPrinterEvent</b>.</p>
</dd>
</dl>

## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

## -remarks
<p>A user interface plug-in's <code>IPrintOemUI::PrinterEvent</code> method performs the same types of operations as the <b>DrvPrinterEvent</b> function that is exported by user-mode printer interface DLLs. For information about printer events and how they should be processed, see the description of the <a href="..\winddiui\nf-winddiui-drvprinterevent.md">DrvPrinterEvent</a> function.</p>

<p>If you provide a user interface plug-in, the printer driver's <b>DrvPrinterEvent</b> function calls the <code>IPrintOemUI::PrinterEvent</code> method. The <b>DrvPrinterEvent</b> function performs its own processing for the specified event, and then calls the <code>IPrintOemUI::PrinterEvent</code> method to handle additional processing of the event.</p>

<p>If <code>IPrintOemUI::PrinterEvent</code> methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation.</p>

<p>For more information about creating and installing user interface plug-ins, see <a href="NULL">Customizing Microsoft's Printer Drivers</a>.</p>

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
<dt>Prcomoem.h (include Prcomoem.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\winddiui\nf-winddiui-drvprinterevent.md">DrvPrinterEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUI::PrinterEvent method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
