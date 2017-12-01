---
UID: NN.printerextension.IPrinterExtensionContextCollection
title: IPrinterExtensionContextCollection
author: windows-driver-content
description: Exposes a collection of IPrinterExtensionContext objects.
old-location: print\iprinterextensioncontextcollection.htm
old-project: print
ms.assetid: 693DAA13-70B3-48A7-9BC2-6369691539FD
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
req.alt-api: IPrinterExtensionContextCollection
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

# IPrinterExtensionContextCollection interface



## -description
<p>Exposes a collection of <a href="..\printerextension\nn-printerextension-iprinterextensioncontext.md">IPrinterExtensionContext</a> objects.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrinterExtensionContextCollection</b> interface inherits from the <a href="ebbff4bc-36b2-4861-9efa-ffa45e013eb5" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IDispatch</b></a> interface. <b>IPrinterExtensionContextCollection</b> also has these types of members:</p>

<p>The <b>IPrinterExtensionContextCollection</b> interface has these methods.</p>

<p>Gets a pointer to an <a href="..\printerextension\nn-printerextension-iprinterextensioncontext.md">IPrinterExtensionContext</a> object.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrinterExtensionContextCollection</b> interface has these properties.</p>

<p>
<a href="print.iprinterextensioncontextcollection_count">Count</a>
</p>

<p>Read-only</p>

<p>Gets a count of the number of <a href="..\printerextension\nn-printerextension-iprinterextensioncontext.md">IPrinterExtensionContext</a> objects in the collection.</p>

<p>
<a href="print.iprinterextensioncontextcollection_newenum">NewEnum</a>
</p>

<p>Read-only</p>

<p>Gets a pointer to the enumerants of <b>IPrinterExtensionContextCollection</b> objects.</p>

<p> </p>

## -members
<p>The <b>IPrinterExtensionContextCollection</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterextensioncontextcollection_getat">GetAt</a>
</td>
<td align="left" width="63%">
<p>Gets a pointer to an <a href="..\printerextension\nn-printerextension-iprinterextensioncontext.md">IPrinterExtensionContext</a> object.</p>
</td>
</tr>
</table><p>Gets a pointer to an <a href="..\printerextension\nn-printerextension-iprinterextensioncontext.md">IPrinterExtensionContext</a> object.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrinterExtensionContextCollection</b> interface has these properties.</p><table class="members" id="memberListProperties">
<tr>
<th align="left" width="27%">Property</th>
<th align="left" width="10%">Access type</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="print.iprinterextensioncontextcollection_count">Count</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets a count of the number of <a href="..\printerextension\nn-printerextension-iprinterextensioncontext.md">IPrinterExtensionContext</a> objects in the collection.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="print.iprinterextensioncontextcollection_newenum">NewEnum</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets a pointer to the enumerants of <b>IPrinterExtensionContextCollection</b> objects.</p>
</td>
</tr>
</table><p>
<a href="print.iprinterextensioncontextcollection_count">Count</a>
</p>

<p>Read-only</p>

<p>Gets a count of the number of <a href="..\printerextension\nn-printerextension-iprinterextensioncontext.md">IPrinterExtensionContext</a> objects in the collection.</p>

<p>
<a href="print.iprinterextensioncontextcollection_newenum">NewEnum</a>
</p>

<p>Read-only</p>

<p>Gets a pointer to the enumerants of <b>IPrinterExtensionContextCollection</b> objects.</p>

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
<a href="automat.idispatch">IDispatch</a>
</dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprinterextensioncontext.md">IPrinterExtensionContext</a>
</dt>
<dt>
<a href="print.iprinterextensionevent_onprinterqueuesenumerated">IPrinterExtensionEvent::OnPrinterQueuesEnumerated</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterExtensionContextCollection interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
