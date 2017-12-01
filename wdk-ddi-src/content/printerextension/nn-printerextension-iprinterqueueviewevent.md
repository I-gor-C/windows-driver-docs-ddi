---
UID: NN.printerextension.IPrinterQueueViewEvent
title: IPrinterQueueViewEvent
author: windows-driver-content
description: Provides the signature of the event handler.
old-location: print\iprinterqueueviewevent.htm
old-project: print
ms.assetid: 23951787-C147-43A6-99D6-71AC037F6A43
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintSchemaTicket2, GetParameterInitializer, IPrintSchemaTicket2::GetParameterInitializer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: printerextension.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrinterQueueViewEvent
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

# IPrinterQueueViewEvent interface



## -description
<p>Provides the signature of the event handler.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrinterQueueViewEvent</b> interface inherits from the <a href="ebbff4bc-36b2-4861-9efa-ffa45e013eb5" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IDispatch</b></a> interface. <b>IPrinterQueueViewEvent</b> also has these types of members:</p>

<p>The <b>IPrinterQueueViewEvent</b> interface has these methods.</p>

<p>Provides an <a href="..\printerextension\nn-printerextension-iprintjobcollection.md">IPrintJobCollection</a> object that provides a snapshot of a range of print jobs in the queue.</p>

<p> </p>

## -members
<p>The <b>IPrinterQueueViewEvent</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterqueueviewevent_onchanged">OnChanged</a>
</td>
<td align="left" width="63%">
<p>Provides an <a href="..\printerextension\nn-printerextension-iprintjobcollection.md">IPrintJobCollection</a> object that provides a snapshot of a range of print jobs in the queue.</p>
</td>
</tr>
</table><p>Provides an <a href="..\printerextension\nn-printerextension-iprintjobcollection.md">IPrintJobCollection</a> object that provides a snapshot of a range of print jobs in the queue.</p>

<p> </p>

## -remarks
<p><b>IPrinterQueueViewEvent</b> also helps to make it possible to perform job management from a UWP device app or from a printer extension. For more information, see <a href="NULL">Job Management</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
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
<a href="NULL">Job Management</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterQueueViewEvent interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
