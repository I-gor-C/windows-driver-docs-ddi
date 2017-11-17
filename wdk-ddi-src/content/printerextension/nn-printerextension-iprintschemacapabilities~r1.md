---
UID: NN.printerextension.IPrintSchemaCapabilities~r1
title: IPrintSchemaCapabilities
author: windows-driver-content
description: Provides the primary method to access PrintCapabilities.
old-location: print\iprintschemacapabilities_interface.htm
ms.assetid: A148C1B4-99A3-4AF3-B2D6-73684978425F
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
req.alt-api: IPrintSchemaCapabilities
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

# IPrintSchemaCapabilities interface



## -description
<p>Provides the primary method to access PrintCapabilities.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaCapabilities</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/hh451270">IPrintSchemaElement</a>. <b>IPrintSchemaCapabilities</b> also has these types of members:</p>

<p>The <b>IPrintSchemaCapabilities</b> interface has these methods.</p>

<p>Gets a named feature from the PrintCapabilities, by name and full namespace URI.</p>

<p>Gets a feature from the PrintCapabilities based on a given key name.</p>

<p>Gets all the options of a feature.</p>

<p>Gets the selected option for a feature in <a href="https://msdn.microsoft.com/library/windows/hardware/hh451398">IPrintSchemaTicket</a>.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaCapabilities</b> interface has these properties.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh965533">JobCopiesAllDocumentsMaxValue</a>
</p>

<p>Read-only</p>

<p>Gets the <b>JobCopiesAllDocuments</b> parameter maximum value.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh965534">JobCopiesAllDocumentsMinValue</a>
</p>

<p>Read-only</p>

<p>Gets the <b>JobCopiesAllDocuments</b> parameter minimum value.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971601">PageImageableSize</a>
</p>

<p>Read-only</p>

<p>Gets the imageable area information of the printer.</p>

<p> </p>

## -members
<p>The <b>IPrintSchemaCapabilities</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451385">GetFeature</a>
</td>
<td align="left" width="63%">
<p>Gets a named feature from the PrintCapabilities, by name and full namespace URI.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451388">GetFeatureByKeyName</a>
</td>
<td align="left" width="63%">
<p>Gets a feature from the PrintCapabilities based on a given key name.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451244">GetOptions</a>
</td>
<td align="left" width="63%">
<p>Gets all the options of a feature.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451248">GetSelectedOptionInPrintTicket</a>
</td>
<td align="left" width="63%">
<p>Gets the selected option for a feature in <a href="https://msdn.microsoft.com/library/windows/hardware/hh451398">IPrintSchemaTicket</a>.</p>
</td>
</tr>
</table><p>Gets a named feature from the PrintCapabilities, by name and full namespace URI.</p>

<p>Gets a feature from the PrintCapabilities based on a given key name.</p>

<p>Gets all the options of a feature.</p>

<p>Gets the selected option for a feature in <a href="https://msdn.microsoft.com/library/windows/hardware/hh451398">IPrintSchemaTicket</a>.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaCapabilities</b> interface has these properties.</p><table class="members" id="memberListProperties">
<tr>
<th align="left" width="27%">Property</th>
<th align="left" width="10%">Access type</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh965533">JobCopiesAllDocumentsMaxValue</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets the <b>JobCopiesAllDocuments</b> parameter maximum value.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh965534">JobCopiesAllDocumentsMinValue</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets the <b>JobCopiesAllDocuments</b> parameter minimum value.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971601">PageImageableSize</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets the imageable area information of the printer.</p>
</td>
</tr>
</table><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh965533">JobCopiesAllDocumentsMaxValue</a>
</p>

<p>Read-only</p>

<p>Gets the <b>JobCopiesAllDocuments</b> parameter maximum value.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh965534">JobCopiesAllDocumentsMinValue</a>
</p>

<p>Read-only</p>

<p>Gets the <b>JobCopiesAllDocuments</b> parameter minimum value.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971601">PageImageableSize</a>
</p>

<p>Read-only</p>

<p>Gets the imageable area information of the printer.</p>

<p> </p>

## -remarks
<p>To obtain an IXMLDOMDocument2 object for the PrintCapabilities object, you must first dereference the <i>ppXmlNode</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh969196">XmlNode</a> property (using *ppXmlNode ). This retrieves a pointer to an interface of type <b>IUnknown</b>. Use this pointer to  call the <b>QueryInterface</b> method of the PrintCapabilities object to access the underlying  IXMLDOMDocument2 object.</p>

<p>To obtain an IXMLDOMDocument2 object for the PrintCapabilities object, you must first dereference the <i>ppXmlNode</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh969196">XmlNode</a> property (using *ppXmlNode ). This retrieves a pointer to an interface of type <b>IUnknown</b>. Use this pointer to  call the <b>QueryInterface</b> method of the PrintCapabilities object to access the underlying  IXMLDOMDocument2 object.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451270">IPrintSchemaElement</a>
</dt>
<dt><a href="http://msdn.microsoft.com/en-us/library/windows/hardware/br259124">Developing v4 print drivers</a></dt>
<dt>
<a href="https://msdn.microsoft.com/5E7F2292-1F71-4581-8E34-86F1464EC08F">IPrintSchemaElement::XmlNode</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451398">IPrintSchemaTicket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/5556BD5E-6489-4CCF-8C62-DDA53AD9F368">IPrintSchemaTicket_GetCapabilities</a>
</dt>
<dt>
<a href="NULL">V4 Printer Driver Localization</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintSchemaCapabilities interface%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
