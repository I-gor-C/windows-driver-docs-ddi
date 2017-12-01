---
UID: NN.printerextension.IPrintSchemaOption
title: IPrintSchemaOption
author: windows-driver-content
description: Exposes a Print Schema Option object.
old-location: print\iprintschemaoption_interface.htm
old-project: print
ms.assetid: B520875A-7882-43D5-A890-0F82654EFD6C
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
req.alt-api: IPrintSchemaOption
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

# IPrintSchemaOption interface



## -description
<p>Exposes a Print Schema Option object.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaOption</b> interface inherits from <a href="..\printerextension\nn-printerextension-iprintschemadisplayableelement.md">IPrintSchemaDisplayableElement</a>. <b>IPrintSchemaOption</b> also has these types of members:</p>

<p>The <b>IPrintSchemaOption</b> interface has these methods.</p>

<p>Gets the XML node for the "value" child element of a "Property"  or a "ScoredProperty" element with the given name.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaOption</b> interface has these properties.</p>

<p>
<a href="print.iprintschemaoption_constrained">Constrained</a>
</p>

<p>Read-only</p>

<p>Gets  the constraint setting type for the schema option.</p>

<p>
<a href="print.iprintschemaoption_selected">Selected</a>
</p>

<p>Read-only</p>

<p>Indicates whether this option is selected.</p>

<p> </p>

## -members
<p>The <b>IPrintSchemaOption</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprintschemaoption_getpropertyvalue">GetPropertyValue</a>
</td>
<td align="left" width="63%">
<p>Gets the XML node for the "value" child element of a "Property"  or a "ScoredProperty" element with the given name.</p>
</td>
</tr>
</table><p>Gets the XML node for the "value" child element of a "Property"  or a "ScoredProperty" element with the given name.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaOption</b> interface has these properties.</p><table class="members" id="memberListProperties">
<tr>
<th align="left" width="27%">Property</th>
<th align="left" width="10%">Access type</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="print.iprintschemaoption_constrained">Constrained</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets  the constraint setting type for the schema option.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="print.iprintschemaoption_selected">Selected</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Indicates whether this option is selected.</p>
</td>
</tr>
</table><p>
<a href="print.iprintschemaoption_constrained">Constrained</a>
</p>

<p>Read-only</p>

<p>Gets  the constraint setting type for the schema option.</p>

<p>
<a href="print.iprintschemaoption_selected">Selected</a>
</p>

<p>Read-only</p>

<p>Indicates whether this option is selected.</p>

<p> </p>

## -remarks
<p>You must ensure that each Feature or Option in a PrintTicket or PrintCapabilities XML document has a <i>name</i> attribute specified. This attribute is used to build the <b>IPrintSchemaOption</b> and <a href="..\printerextension\nn-printerextension-iprintschemafeature.md">IPrintSchemaFeature</a> objects. If the <i>name</i> attribute is omitted, the feature or option will not be displayed in the object model, or the Microsoft-provided print preferences experience.</p>

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
<a href="..\printerextension\nn-printerextension-iprintschemadisplayableelement.md">IPrintSchemaDisplayableElement</a>
</dt>
<dt>
<a href="print.iprintschemafeature_getoption">IPrintSchemaFeature::GetOption</a>
</dt>
<dt>
<a href="print.iprintschemafeature_selectedoption">IPrintSchemaFeature::SelectedOption</a>
</dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprintschemaoptioncollection.md">IPrintSchemaOptionCollection</a>
</dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprintschemapagemediasizeoption.md">IPrintSchemaPageMediaSizeOption</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintSchemaOption interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
