---
UID: NN.printerextension.IPrinterScriptablePropertyBag
title: IPrinterScriptablePropertyBag
author: windows-driver-content
description: The IPrinterScriptablePropertyBag interface is the property bag interface passed to script clients.
old-location: print\iprinterscriptablepropertybag.htm
ms.assetid: E6F48895-7ED6-479B-BF16-42192461C56D
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: print
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
ms.keywords: IPrintSchemaTicket2, GetParameterInitializer, IPrintSchemaTicket2::GetParameterInitializer
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# IPrinterScriptablePropertyBag interface



## -description
<p>The IPrinterScriptablePropertyBag interface is the property bag interface passed to script clients. </p>
<p>This interface is the same as <a href="https://msdn.microsoft.com/library/windows/hardware/hh439547">IPrinterPropertyBag</a>, except that the GetBytes and SetBytes methods operate on JavaScript arrays and the GetReadStream and GetWriteStream methods operate on <a href="https://msdn.microsoft.com/library/windows/hardware/hh973218">IPrinterScriptableStream</a> objects.</p>


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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439647">GetBool</a>
</td>
<td align="left" width="63%">
<p>Gets a specified boolean property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439653">GetBytes</a>
</td>
<td align="left" width="63%">
<p>Gets a byte array property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439658">GetInt32</a>
</td>
<td align="left" width="63%">
<p>Gets an integer property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439535">GetReadStream</a>
</td>
<td align="left" width="63%">
<p>Gets a read stream and uses it to read  from a property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/jj983419">GetString</a>
</td>
<td align="left" width="63%">
<p>Gets a string property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439675">GetWriteStream</a>
</td>
<td align="left" width="63%">
<p>Gets a stream and uses it  to write to a stream property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439552">SetBool</a>
</td>
<td align="left" width="63%">
<p>Writes a specified boolean property value.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439606">SetBytes</a>
</td>
<td align="left" width="63%">
<p>Writes a byte array property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439610">SetInt32</a>
</td>
<td align="left" width="63%">
<p>Writes an integer property.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/jj983427">SetString</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439547">IPrinterPropertyBag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh973218">IPrinterScriptableStream</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/73BE6E2A-0C46-4C3F-8888-5FE8386A1F50">IPrinterScriptContext::DriverProperties</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/EEC61313-5796-42BC-84BF-CF29F8BE0C96">IPrinterScriptContext::QueueProperties</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6F181350-41A3-4592-BB72-1E3AD6FEC748">IPrinterScriptContext::UserProperties</a>
</dt>
<dt>
<a href="NULL">V4 Printer Driver Property Bags</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterScriptablePropertyBag interface%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
