---
UID: NN.printerextension.IPrinterScriptableStream
title: IPrinterScriptableStream
author: windows-driver-content
description: The IPrinterScriptableStream interface builds on IPrinterScriptableSequentialStream and adds IStream-like semantics.
old-location: print\iprinterscriptablestream.htm
old-project: print
ms.assetid: AD3CDF90-76ED-498B-8DE1-B191504EB415
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
req.alt-api: IPrinterScriptableStream
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

# IPrinterScriptableStream interface



## -description
The IPrinterScriptableStream interface builds on <a href="print.iprinterscriptablesequentialstream_interface">IPrinterScriptableSequentialStream</a> and adds IStream-like semantics.


## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrinterScriptableStream</b> interface inherits from <a href="print.iprinterscriptablesequentialstream_interface">IPrinterScriptableSequentialStream</a>. <b>IPrinterScriptableStream</b> also has these types of members:

The <b>IPrinterScriptableStream</b> interface has these methods.

Commits the operation.

Sets the seek pointer.

Sets the size of the scriptable stream, in bytes.

 

## -members
The <b>IPrinterScriptableStream</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterscriptablestream__commit">Commit</a>
</td>
<td align="left" width="63%">
Commits the operation.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterscriptablestream__seek">Seek</a>
</td>
<td align="left" width="63%">
Sets the seek pointer.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterscriptablestream__setsize">SetSize</a>
</td>
<td align="left" width="63%">
Sets the size of the scriptable stream, in bytes.
</td>
</tr>
</table>Commits the operation.

Sets the seek pointer.

Sets the size of the scriptable stream, in bytes.

 

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
<a href="print.iprinterscriptablesequentialstream_interface">IPrinterScriptableSequentialStream</a>
</dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprinterscriptablepropertybag.md">IPrinterScriptablePropertyBag</a>
</dt>
<dt>
<a href="print.iprinterscriptablepropertybag_getreadstream">IPrinterScriptablePropertyBag::GetReadStream</a>
</dt>
<dt>
<a href="print.iprinterscriptablepropertybag_getwritestream">IPrinterScriptablePropertyBag::GetWriteStream</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterScriptableStream interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
