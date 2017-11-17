---
UID: NN.printerextension.IPrinterExtensionAsyncOperation
title: IPrinterExtensionAsyncOperation
author: windows-driver-content
description: Provides the context associated with an asynchronous operation.
old-location: print\iprinterextensionasyncoperation.htm
ms.assetid: AA862667-42D6-4A82-9698-1C43E9EEC434
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: print
req.header: printerextension.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrinterExtensionAsyncOperation
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
ms.keywords: IPrintSchemaTicket2, GetParameterInitializer, IPrintSchemaTicket2::GetParameterInitializer
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# IPrinterExtensionAsyncOperation interface



## -description
<p>Provides the context associated with an asynchronous operation.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrinterExtensionAsyncOperation</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IPrinterExtensionAsyncOperation</b> also has these types of members:</p>

<p>The <b>IPrinterExtensionAsyncOperation</b> interface has these methods.</p>

<p>Cancels the asynchronous operation.</p>

<p> </p>

## -members
<p>The <b>IPrinterExtensionAsyncOperation</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406716">Cancel</a>
</td>
<td align="left" width="63%">
<p>Cancels the asynchronous operation.</p>
</td>
</tr>
</table><p>Cancels the asynchronous operation.</p>

<p> </p>

## -remarks
<p><b>IPrinterExtensionAsyncOperation</b> also helps to make it possible to perform device maintenance from a UWP device app or from a printer extension. For more information, see <a href="NULL">Device Maintenance</a>.</p>

<p><b>IPrinterExtensionAsyncOperation</b> also helps to make it possible to perform device maintenance from a UWP device app or from a printer extension. For more information, see <a href="NULL">Device Maintenance</a>.</p>

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
<a href="NULL">Device Maintenance</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265391">SendBidiSetRequestAsync</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterExtensionAsyncOperation interface%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
