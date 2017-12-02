---
UID: NN.printerextension.IPrinterExtensionEventArgs
title: IPrinterExtensionEventArgs
author: windows-driver-content
description: Represents the context for the desktop printer extension activation.
old-location: print\iprinterextensioneventargs.htm
old-project: print
ms.assetid: 77850B5A-4E24-4057-B87F-D964620ABF94
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintSchemaTicket2, GetParameterInitializer, IPrintSchemaTicket2::GetParameterInitializer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: printerextension.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrinterExtensionEventArgs
req.alt-loc: Printerextension.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# IPrinterExtensionEventArgs interface



## -description
<p>Represents the context for the desktop printer extension activation.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrinterExtensionEventArgs</b> interface inherits from <a href="..\printerextension\nn-printerextension-iprinterextensioncontext.md">IPrinterExtensionContext</a>. <b>IPrinterExtensionEventArgs</b> also has these types of members:</p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrinterExtensionEventArgs</b> interface has these properties.</p>

<p>
<a href="print.iprinterextensioneventargs_bidinotification">BidiNotification</a>
</p>

<p>Read-only</p>

<p>Gets the text of the bidirectional communication (Bidi) notification, if applicable.</p>

<p>
<a href="print.iprinterextensioneventargs_detailedreasonid">DetailedReasonId</a>
</p>

<p>Read-only</p>

<p>Gets a more detailed activation reason than what can be retrieved from  <a href="print.iprinterextensioneventargs_reasonid">ReasonId</a>.</p>

<p>
<a href="print.iprinterextensioneventargs_reasonid">ReasonId</a>
</p>

<p>Read-only</p>

<p>Gets the reason why the printer extension was activated.</p>

<p>
<a href="print.iprinterextensioneventargs_request">Request</a>
</p>

<p>Read-only</p>

<p>Gets the <a href="..\printerextension\nn-printerextension-iprinterextensionrequest.md">IPrinterExtensionRequest</a> object for the current event.</p>

<p>
<a href="print.iprinterextensioneventargs_sourceapplication">SourceApplication</a>
</p>

<p>Read-only</p>

<p>Gets the name of the application that invoked the printer extension.</p>

<p>
<a href="print.iprinterextensioneventargs_windowmodal">WindowModal</a>
</p>

<p>Read-only</p>

<p>Gets the run mode parameter that determines whether or not the printer extension should be run as modal.</p>

<p>
<a href="print.iprinterextensioneventargs_windowparent">WindowParent</a>
</p>

<p>Read-only</p>

<p>Gets the handle of the parent window.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Printerextension.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\printerextension\nn-printerextension-iprinterextensioncontext.md">IPrinterExtensionContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4E20303A-BEB3-4928-BA5A-356D978FA2BE">V4 Printer Driver Property Bags</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterExtensionEventArgs interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
