---
UID: NN.printerextension.IPrintSchemaParameterDefinition~r1
title: IPrintSchemaParameterDefinition
author: windows-driver-content
description: The IPrintSchemaParameterDefinition interface represents a parameter definition, as defined in the Print Schema Specification.
old-location: print\iprintschemaparameterdefinition.htm
old-project: print
ms.assetid: 205A4F09-6FE5-459E-A94A-13B1839AF489
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintSchemaTicket2, GetParameterInitializer, IPrintSchemaTicket2::GetParameterInitializer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: printerextension.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintSchemaParameterDefinition
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

# IPrintSchemaParameterDefinition interface



## -description
<p>The <b>IPrintSchemaParameterDefinition</b> interface represents a parameter definition, as defined in the <a href="http://msdn.microsoft.com/en-us/library/windows/hardware/gg463385.aspx">Print Schema Specification</a>. </p>
<p>For more information about the four data types that you can use with the &lt;psf:ParameterDef&gt; element, see section 2.1.3.1 of the <a href="http://msdn.microsoft.com/en-us/library/windows/hardware/gg463385.aspx">Print Schema Specification</a>.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaParameterDefinition</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/hh451262">IPrintSchemaDisplayableElement</a>. <b>IPrintSchemaParameterDefinition</b> also has these types of members:</p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaParameterDefinition</b> interface has these properties.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn454563">DataType</a>
</p>

<p>Read-only</p>

<p>The <b>DataType</b> property Gets the <a href="https://msdn.microsoft.com/library/windows/hardware/dn454562">PrintSchemaParameterDataType</a> enumerated value that indicates the expected data type for the Print Schema parameter.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn454564">RangeMax</a>
</p>

<p>Read-only</p>

<p>The <b>RangeMax</b> property Gets the maximum value of the allowed data range.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn454565">RangeMin</a>
</p>

<p>Read-only</p>

<p>The <b>RangeMin</b> property Gets the minimum value of the allowed data range.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn454566">UnitType</a>
</p>

<p>Read-only</p>

<p>The <b>UnitType</b> property Gets the unit type.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn454567">UserInputRequired</a>
</p>

<p>Read-only</p>

<p>The <b>UserInputRequired</b> property Gets the Boolean value that indicates whether or not a user input value is required for the Print Schema parameter.</p>

<p> </p>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451262">IPrintSchemaDisplayableElement</a>
</dt>
<dt><a href="http://msdn.microsoft.com/en-us/library/windows/hardware/gg463385.aspx">Print Schema Specification</a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintSchemaParameterDefinition interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
