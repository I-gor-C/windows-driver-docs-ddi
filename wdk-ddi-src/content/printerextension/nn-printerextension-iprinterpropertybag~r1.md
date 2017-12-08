---
UID: NN.printerextension.IPrinterPropertyBag~r1
title: IPrinterPropertyBag
author: windows-driver-content
description: Provides strongly-typed get and set methods.
old-location: print\iprinterpropertybag_interface.htm
old-project: print
ms.assetid: 421397FF-4956-4052-B63D-32F8E79A22D0
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
req.alt-api: IPrinterPropertyBag
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

# IPrinterPropertyBag interface



## -description
Provides strongly-typed <b>get</b> and <b>set</b> methods.
Note that the driver property bag uses the following GUID for its property store format ID:

<dl>
<dd>DEFINE_GUID(FMTID_PrinterPropertyBag, 0x75f9adca, 0x097d, 0x45c3, 0xa6, 0xe4, 0xba, 0xb2, 0x9e, 0x27, 0x6f, 0x3e);</dd>
</dl>

The <b>IPrinterPropertyBag</b> interface is used by all the printer property bags, including driver property bag, user property bag, queue property bag, and DEVMODE property bag.


## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrinterPropertyBag</b> interface inherits from the <a href="ebbff4bc-36b2-4861-9efa-ffa45e013eb5" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IDispatch</b></a> interface. <b>IPrinterPropertyBag</b> also has these types of members:

The <b>IPrinterPropertyBag</b> interface has these methods.

Reads a specified boolean property.

Reads a byte array property.

Reads an integer property.

Gets a stream in order to read from a stream property.

Reads a string property.

Gets a stream in order to write a stream property.

Writes a specified boolean property value.

Writes a byte array property.

Writes an integer property.

Writes a string property.

 

## -members
The <b>IPrinterPropertyBag</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterpropertybag_getbool">GetBool</a>
</td>
<td align="left" width="63%">
Reads a specified boolean property.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterpropertybag_getbytes">GetBytes</a>
</td>
<td align="left" width="63%">
Reads a byte array property.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterpropertybag_getint32">GetInt32</a>
</td>
<td align="left" width="63%">
Reads an integer property.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterpropertybag_getreadstream">GetReadStream</a>
</td>
<td align="left" width="63%">
Gets a stream in order to read from a stream property.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterpropertybag_getstring">GetString</a>
</td>
<td align="left" width="63%">
Reads a string property.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterpropertybag_getwritestream">GetWriteStream</a>
</td>
<td align="left" width="63%">
Gets a stream in order to write a stream property.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterpropertybag_setbool">SetBool</a>
</td>
<td align="left" width="63%">
Writes a specified boolean property value.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterpropertybag_setbytes">SetBytes</a>
</td>
<td align="left" width="63%">
Writes a byte array property.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterpropertybag_setint32">SetInt32</a>
</td>
<td align="left" width="63%">
Writes an integer property.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprinterpropertybag_setstring">SetString</a>
</td>
<td align="left" width="63%">
Writes a string property.
</td>
</tr>
</table>Reads a specified boolean property.

Reads a byte array property.

Reads an integer property.

Gets a stream in order to read from a stream property.

Reads a string property.

Gets a stream in order to write a stream property.

Writes a specified boolean property value.

Writes a byte array property.

Writes an integer property.

Writes a string property.

 

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
<a href="automat.idispatch">IDispatch</a>
</dt>
<dt>
<a href="print.iprinterextensioncontext_driverproperties">IPrinterExtensionContext::DriverProperties</a>
</dt>
<dt>
<a href="print.iprinterextensioncontext_userproperties">IPrinterExtensionContext::UserProperties</a>
</dt>
<dt>
<a href="print.iprinterqueue_getproperties">IPrinterQueue::GetProperties</a>
</dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprinterscriptablepropertybag.md">IPrinterScriptablePropertyBag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4E20303A-BEB3-4928-BA5A-356D978FA2BE">V4 Printer Driver Property Bags</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterPropertyBag interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
