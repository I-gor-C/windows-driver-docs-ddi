---
UID: NN.printerextension.IPrintSchemaOption~r1
title: IPrintSchemaOption
author: windows-driver-content
description: Exposes a Print Schema Option object.
old-location: print\iprintschemaoption_interface.htm
old-project: print
ms.assetid: B520875A-7882-43D5-A890-0F82654EFD6C
ms.author: windowsdriverdev
ms.date: 12/9/2017
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
req.product: Windows 10 or later.
---

# IPrintSchemaOption interface



## -description
Exposes a Print Schema Option object.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaOption</b> interface inherits from <a href="..\printerextension\nn-printerextension-iprintschemadisplayableelement.md">IPrintSchemaDisplayableElement</a>. <b>IPrintSchemaOption</b> also has these types of members:

The <b>IPrintSchemaOption</b> interface has these methods.

Gets the XML node for the "value" child element of a "Property"  or a "ScoredProperty" element with the given name.

 

The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaOption</b> interface has these properties.


<a href="print.iprintschemaoption_constrained">Constrained</a>


Read-only

Gets  the constraint setting type for the schema option.


<a href="print.iprintschemaoption_selected">Selected</a>


Read-only

Indicates whether this option is selected.

 


## -members
The <b>IPrintSchemaOption</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprintschemaoption_getpropertyvalue">GetPropertyValue</a>
</td>
<td align="left" width="63%">
Gets the XML node for the "value" child element of a "Property"  or a "ScoredProperty" element with the given name.

</td>
</tr>
</table>Gets the XML node for the "value" child element of a "Property"  or a "ScoredProperty" element with the given name.

 

The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaOption</b> interface has these properties.
<table class="members" id="memberListProperties">
<tr>
<th align="left" width="27%">Property</th>
<th align="left" width="10%">Access type</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">

<a href="print.iprintschemaoption_constrained">Constrained</a>


</td>
<td align="left" width="10%">
Read-only

</td>
<td align="left" width="63%">
Gets  the constraint setting type for the schema option.

</td>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">

<a href="print.iprintschemaoption_selected">Selected</a>


</td>
<td align="left" width="10%">
Read-only

</td>
<td align="left" width="63%">
Indicates whether this option is selected.

</td>
</tr>
</table>
<a href="print.iprintschemaoption_constrained">Constrained</a>


Read-only

Gets  the constraint setting type for the schema option.


<a href="print.iprintschemaoption_selected">Selected</a>


Read-only

Indicates whether this option is selected.

 


## -remarks
You must ensure that each Feature or Option in a PrintTicket or PrintCapabilities XML document has a <i>name</i> attribute specified. This attribute is used to build the <b>IPrintSchemaOption</b> and <a href="..\printerextension\nn-printerextension-iprintschemafeature.md">IPrintSchemaFeature</a> objects. If the <i>name</i> attribute is omitted, the feature or option will not be displayed in the object model, or the Microsoft-provided print preferences experience.


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
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintSchemaOption interface%20 RELEASE:%20(12/9/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

