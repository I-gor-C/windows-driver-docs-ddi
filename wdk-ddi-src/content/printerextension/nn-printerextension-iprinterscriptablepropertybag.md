---
UID: NN.printerextension.IPrinterScriptablePropertyBag
title: IPrinterScriptablePropertyBag
author: windows-driver-content
description: The IPrinterScriptablePropertyBag interface is the property bag interface passed to script clients.
old-location: print\iprinterscriptablepropertybag.htm
old-project: print
ms.assetid: E6F48895-7ED6-479B-BF16-42192461C56D
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
req.alt-api: IPrinterScriptablePropertyBag
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

# IPrinterScriptablePropertyBag interface



## -description
<p>The IPrinterScriptablePropertyBag interface is the property bag interface passed to script clients. </p>
<p>This interface is the same as <a href="..\printerextension\nn-printerextension-iprinterpropertybag.md">IPrinterPropertyBag</a>, except that the GetBytes and SetBytes methods operate on JavaScript arrays and the GetReadStream and GetWriteStream methods operate on <a href="..\printerextension\nn-printerextension-iprinterscriptablestream.md">IPrinterScriptableStream</a> objects.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrinterScriptablePropertyBag</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IPrinterScriptablePropertyBag</b> also has these types of members:</p>

<p>The <b>IPrinterScriptablePropertyBag</b> interface has these methods.</p>

<p>Gets a specified boolean property.</p>

<p>Gets a byte array property.</p>

<p>Gets an integer property.</p>

<p>Gets a read stream and uses it to read  from a property.</p>

<p>Gets a string property.</p>

<p>Gets a stream and uses it  to write to a stream property.</p>

<p>Writes a specified boolean property value.</p>

<p>Writes a byte array property.</p>

<p>Writes an integer property.</p>

<p>Writes a string property.</p>

<p> </p>

## -members
<p>The <b>IPrinterScriptablePropertyBag</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterscriptablepropertybag_getbool">GetBool</a>
</td>
<td align="left" width="63%">
<p>Gets a specified boolean property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterscriptablepropertybag_getbytes">GetBytes</a>
</td>
<td align="left" width="63%">
<p>Gets a byte array property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterscriptablepropertybag_getint32">GetInt32</a>
</td>
<td align="left" width="63%">
<p>Gets an integer property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterscriptablepropertybag_getreadstream">GetReadStream</a>
</td>
<td align="left" width="63%">
<p>Gets a read stream and uses it to read  from a property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterscriptablepropertybag_getstring">GetString</a>
</td>
<td align="left" width="63%">
<p>Gets a string property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterscriptablepropertybag_getwritestream">GetWriteStream</a>
</td>
<td align="left" width="63%">
<p>Gets a stream and uses it  to write to a stream property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterscriptablepropertybag_setbool">SetBool</a>
</td>
<td align="left" width="63%">
<p>Writes a specified boolean property value.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterscriptablepropertybag_setbytes">SetBytes</a>
</td>
<td align="left" width="63%">
<p>Writes a byte array property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterscriptablepropertybag_setint32">SetInt32</a>
</td>
<td align="left" width="63%">
<p>Writes an integer property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterscriptablepropertybag_setstring">SetString</a>
</td>
<td align="left" width="63%">
<p>Writes a string property.</p>
</td>
</tr>
</table><p>Gets a specified boolean property.</p>

<p>Gets a byte array property.</p>

<p>Gets an integer property.</p>

<p>Gets a read stream and uses it to read  from a property.</p>

<p>Gets a string property.</p>

<p>Gets a stream and uses it  to write to a stream property.</p>

<p>Writes a specified boolean property value.</p>

<p>Writes a byte array property.</p>

<p>Writes an integer property.</p>

<p>Writes a string property.</p>

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
<a href="..\printerextension\nn-printerextension-iprinterpropertybag.md">IPrinterPropertyBag</a>
</dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprinterscriptablestream.md">IPrinterScriptableStream</a>
</dt>
<dt>
<a href="print.iprinterscriptcontext_driverproperties">IPrinterScriptContext::DriverProperties</a>
</dt>
<dt>
<a href="print.iprinterscriptcontext_queueproperties">IPrinterScriptContext::QueueProperties</a>
</dt>
<dt>
<a href="print.iprinterscriptcontext_userproperties">IPrinterScriptContext::UserProperties</a>
</dt>
<dt>
<a href="NULL">V4 Printer Driver Property Bags</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterScriptablePropertyBag interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
