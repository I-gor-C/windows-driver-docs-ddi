---
UID: NN.printerextension.IPrinterExtensionContext
title: IPrinterExtensionContext
author: windows-driver-content
description: Represents the context for the activation of a UWP device app for printers.
old-location: print\iprinterextensioncontext_interface.htm
old-project: print
ms.assetid: DD0B5E6F-8E16-48E1-967B-D188535E1320
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: tagPrintSchemaSelectionType, PrintSchemaSelectionType
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
req.alt-api: IPrinterExtensionContext
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
req.product: Windows 10 or later.
---

# IPrinterExtensionContext interface



## -description
Represents the context for the activation of a UWP device app for printers.


## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrinterExtensionContext</b> interface inherits from the <a href="ebbff4bc-36b2-4861-9efa-ffa45e013eb5" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IDispatch</b></a> interface. <b>IPrinterExtensionContext</b> also has these types of members:

The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrinterExtensionContext</b> interface has these properties.


<a href="print.iprinterextensioncontext_driverproperties">DriverProperties</a>


Read-only

Gets the driver property bag.


<a href="..\printerextension\ns-printerextension-printerqueue~r1.md">PrinterQueue</a>


Read-only

Gets the queue for the printer.


<a href="print.iprinterextensioncontext_printschematicket">PrintSchemaTicket</a>


Read-only

Gets the print ticket that is appropriate for the queue and the activation.


<a href="print.iprinterextensioncontext_userproperties">UserProperties</a>


Read-only

Gets the user property bag for this app.

 

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012
</td>
</tr>
<tr>
<th width="30%">
Header
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
<a href="..\printerextension\nn-printerextension-iprinterextensioncontextcollection.md">IPrinterExtensionContextCollection</a>
</dt>
<dt>
<a href="print.iprinterextensioncontextcollection_count">IPrinterExtensionContextCollection::Count</a>
</dt>
<dt>
<a href="print.iprinterextensioncontextcollection_getat">IPrinterExtensionContextCollection::GetAt</a>
</dt>
<dt>
<a href="print.iprinterextensionevent_onprinterqueuesenumerated">IPrinterExtensionEvent::OnPrinterQueuesEnumerated</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4E20303A-BEB3-4928-BA5A-356D978FA2BE">V4 Printer Driver Property Bags</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterExtensionContext interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
