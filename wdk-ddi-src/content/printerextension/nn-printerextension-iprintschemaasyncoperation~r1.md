---
UID: NN.printerextension.IPrintSchemaAsyncOperation~r1
title: IPrintSchemaAsyncOperation
author: windows-driver-content
description: Represents an asynchronous operation context for validation, merge or commit operations.
old-location: print\iprintschemaasyncoperation_interface.htm
old-project: print
ms.assetid: CEA80412-4B19-493B-A85E-625915D77CA5
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
req.alt-api: IPrintSchemaAsyncOperation
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

# IPrintSchemaAsyncOperation interface



## -description
<p>Represents an asynchronous operation context for validation, merge or commit operations.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaAsyncOperation</b> interface inherits from the <a href="ebbff4bc-36b2-4861-9efa-ffa45e013eb5" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IDispatch</b></a> interface. <b>IPrintSchemaAsyncOperation</b> also has these types of members:</p>

<p>The <b>IPrintSchemaAsyncOperation</b> interface has these methods.</p>

<p>Cancels the asynchronous PrintSchema operation.</p>

<p>Starts the asynchronous PrintSchema operation.</p>

<p> </p>

## -members
<p>The <b>IPrintSchemaAsyncOperation</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406716">Cancel</a>
</td>
<td align="left" width="63%">
<p>Cancels the asynchronous PrintSchema operation.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh973223">Start</a>
</td>
<td align="left" width="63%">
<p>Starts the asynchronous PrintSchema operation.</p>
</td>
</tr>
</table><p>Cancels the asynchronous PrintSchema operation.</p>

<p>Starts the asynchronous PrintSchema operation.</p>

<p> </p>

## -remarks
<p>Any event sink that implements <a href="https://msdn.microsoft.com/library/windows/hardware/hh451211">IPrintSchemaAsyncOperationEvent</a> is connected to the associated event source, <b>IPrintSchemaAsyncOperation</b>, via the <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/ms694318(v=vs.85).aspx">IConnectionPoint</a> mechanism. You must retrieve a pointer to the <b>IConnectionPoint</b> interface by invoking <b>QueryInterface</b> on the <b>IPrinterQueue</b> object.</p>

<p>Any event sink that implements <a href="https://msdn.microsoft.com/library/windows/hardware/hh451211">IPrintSchemaAsyncOperationEvent</a> is connected to the associated event source, <b>IPrintSchemaAsyncOperation</b>, via the <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/ms694318(v=vs.85).aspx">IConnectionPoint</a> mechanism. You must retrieve a pointer to the <b>IConnectionPoint</b> interface by invoking <b>QueryInterface</b> on the <b>IPrinterQueue</b> object.</p>

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
<dt><a href="http://msdn.microsoft.com/en-us/library/windows/desktop/ms694318(v=vs.85).aspx">IConnectionPoint</a></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451211">IPrintSchemaAsyncOperationEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintSchemaAsyncOperation interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
