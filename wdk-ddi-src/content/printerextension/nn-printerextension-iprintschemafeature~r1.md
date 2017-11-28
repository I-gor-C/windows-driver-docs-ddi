---
UID: NN.printerextension.IPrintSchemaFeature~r1
title: IPrintSchemaFeature
author: windows-driver-content
description: Exposes a Print Schema Feature element.
old-location: print\iprintschemafeature_interface.htm
old-project: print
ms.assetid: AAC2A60B-9E70-4809-969A-68783A91B093
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
req.alt-api: IPrintSchemaFeature
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

# IPrintSchemaFeature interface



## -description
<p>Exposes a Print Schema Feature element.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaFeature</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/hh451262">IPrintSchemaDisplayableElement</a>. <b>IPrintSchemaFeature</b> also has these types of members:</p>

<p>The <b>IPrintSchemaFeature</b> interface has these methods.</p>

<p>Gets the option with the given name.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaFeature</b> interface has these properties.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971603">DisplayUI</a>
</p>

<p>Read-only</p>

<p>Gets the setting that indicates whether or not to show the print UI.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971604">SelectedOption</a>
</p>

<p>Read-only</p>

<p>Gets an <a href="https://msdn.microsoft.com/library/windows/hardware/hh451335">IPrintSchemaOption</a> representing the selected option.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971604">SelectedOption</a>
</p>

<p>Write-only</p>

<p>Changes the selected option of the Print Schema Feature element to the specified <a href="https://msdn.microsoft.com/library/windows/hardware/hh451335">IPrintSchemaOption</a> element.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971606">SelectionType</a>
</p>

<p>Read-only</p>

<p>Gets the selection type of the Feature.</p>

<p> </p>

## -members
<p>The <b>IPrintSchemaFeature</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451273">GetOption</a>
</td>
<td align="left" width="63%">
<p>Gets the option with the given name.</p>
</td>
</tr>
</table><p>Gets the option with the given name.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaFeature</b> interface has these properties.</p><table class="members" id="memberListProperties">
<tr>
<th align="left" width="27%">Property</th>
<th align="left" width="10%">Access type</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971603">DisplayUI</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets the setting that indicates whether or not to show the print UI.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971604">SelectedOption</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets an <a href="https://msdn.microsoft.com/library/windows/hardware/hh451335">IPrintSchemaOption</a> representing the selected option.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971604">SelectedOption</a>
</p>
</td>
<td align="left" width="10%">
<p>Write-only</p>
</td>
<td align="left" width="63%">
<p>Changes the selected option of the Print Schema Feature element to the specified <a href="https://msdn.microsoft.com/library/windows/hardware/hh451335">IPrintSchemaOption</a> element.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971606">SelectionType</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets the selection type of the Feature.</p>
</td>
</tr>
</table><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971603">DisplayUI</a>
</p>

<p>Read-only</p>

<p>Gets the setting that indicates whether or not to show the print UI.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971604">SelectedOption</a>
</p>

<p>Read-only</p>

<p>Gets an <a href="https://msdn.microsoft.com/library/windows/hardware/hh451335">IPrintSchemaOption</a> representing the selected option.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971604">SelectedOption</a>
</p>

<p>Write-only</p>

<p>Changes the selected option of the Print Schema Feature element to the specified <a href="https://msdn.microsoft.com/library/windows/hardware/hh451335">IPrintSchemaOption</a> element.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971606">SelectionType</a>
</p>

<p>Read-only</p>

<p>Gets the selection type of the Feature.</p>

<p> </p>

## -remarks
<p>You must ensure that each Feature or Option in a PrintTicket or PrintCapabilities XML document has a <i>name</i> attribute specified. This attribute is used to build the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451335">IPrintSchemaOption</a> and <b>IPrintSchemaFeature</b> objects. If the <i>name</i> attribute is omitted, the feature or option will not be displayed in the object model, or the Microsoft-provided print preferences experience.</p>

<p>You must ensure that each Feature or Option in a PrintTicket or PrintCapabilities XML document has a <i>name</i> attribute specified. This attribute is used to build the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451335">IPrintSchemaOption</a> and <b>IPrintSchemaFeature</b> objects. If the <i>name</i> attribute is omitted, the feature or option will not be displayed in the object model, or the Microsoft-provided print preferences experience.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451262">IPrintSchemaDisplayableElement</a>
</dt>
<dt>
<a href="print.iprintschemacapabilities_getfeature">IPrintSchemaCapabilities::GetFeature</a>
</dt>
<dt>
<a href="print.iprintschematicket_getfeature">IPrintSchemaTicket::GetFeature</a>
</dt>
<dt>
<a href="print.iprintschematicket_getfeaturebykeyname">IPrintSchemaTicket::GetFeatureByKeyName</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintSchemaFeature interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
