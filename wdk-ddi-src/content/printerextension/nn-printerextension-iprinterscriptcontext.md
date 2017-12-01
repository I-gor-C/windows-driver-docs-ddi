---
UID: NN.printerextension.IPrinterScriptContext
title: IPrinterScriptContext
author: windows-driver-content
description: Passed to all third-party constraints JavaScript functions, and provides access to relevant objects.
old-location: print\iprinterscriptcontext.htm
old-project: print
ms.assetid: B44B47EA-6848-430E-9C10-F6DD460C2304
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
req.alt-api: IPrinterScriptContext
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

# IPrinterScriptContext interface



## -description
<p>Passed to all third-party constraints JavaScript functions, and provides access to relevant objects.</p>
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrinterScriptContext</b> interface has these properties.</p>
<p>
<a href="print.iprinterscriptcontext_driverproperties">DriverProperties</a>
</p>
<p>Read-only</p>
<p>Provides access to the driver property bag, if the property bag is present.</p>
<p>
<a href="print.iprinterscriptcontext_queueproperties">QueueProperties</a>
</p>
<p>Read-only</p>
<p>Provides access to the queue property bag, if the property bag is present.</p>
<p>
<a href="print.iprinterscriptcontext_userproperties">UserProperties</a>
</p>
<p>Read-only</p>
<p>Provides access to the user property bag, if the property bag is present.</p>
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
<a href="NULL">V4 Printer Driver Property Bags</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterScriptContext interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
