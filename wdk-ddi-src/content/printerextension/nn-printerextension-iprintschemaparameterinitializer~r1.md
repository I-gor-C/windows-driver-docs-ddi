---
UID: NN.printerextension.IPrintSchemaParameterInitializer~r1
title: IPrintSchemaParameterInitializer
author: windows-driver-content
description: The IPrintSchemaParameterInitializer interface represents a parameter initialization value, as defined in the print schema specification.
old-location: print\iprintschemaparameterinitializer.htm
old-project: print
ms.assetid: A4A1C231-3D71-4952-B5FA-0C8275DEF4F1
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: tagPrintSchemaSelectionType, PrintSchemaSelectionType
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
req.alt-api: IPrintSchemaParameterInitializer
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

# IPrintSchemaParameterInitializer interface



## -description
The <b>IPrintSchemaParameterInitializer</b> interface represents a parameter initialization value, as defined in the print schema specification.
For more information about the four data types that you can use with the &lt;psf:ParameterInit&gt; element, see section 2.1.3.2 of the <a href="http://msdn.microsoft.com/en-us/library/windows/hardware/gg463385.aspx">Print Schema Specification</a>.


## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaParameterInitializer</b> interface inherits from <a href="..\printerextension\nn-printerextension-iprintschemaelement.md">IPrintSchemaElement</a>. <b>IPrintSchemaParameterInitializer</b> also has these types of members:

The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaParameterInitializer</b> interface has these properties.


<a href="print.iprintschemaparameterinitializer_getvalue">Value</a>


Read-only

The <b>Value</b> (get_Value) property Gets the current value of the <b>IPrintSchemaParameterInitializer</b> object.


<a href="print.iprintschemaparameterinitializer_putvalue">Value</a>


Write-only

The <b>Value</b> (put_Value) property modifies the value of the <b>IPrintSchemaParameterInitializer</b> object. 

 

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8.1
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012 R2
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
<a href="..\printerextension\nn-printerextension-iprintschemaelement.md">IPrintSchemaElement</a>
</dt>
<dt>
<a href="print.iprintschematicket2_getparameterinitializer">IPrintSchematicket2::GetParameterInitializer</a>
</dt>
<dt><a href="http://msdn.microsoft.com/en-us/library/windows/hardware/gg463385.aspx">Print Schema Specification</a></dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintSchemaParameterInitializer interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>