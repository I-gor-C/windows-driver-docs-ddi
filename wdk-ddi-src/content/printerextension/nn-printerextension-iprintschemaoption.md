---
UID: NN:printerextension.IPrintSchemaOption
title: IPrintSchemaOption
author: windows-driver-content
description: Exposes a Print Schema Option object.
old-location: print\iprintschemaoption_interface.htm
old-project: print
ms.assetid: B520875A-7882-43D5-A890-0F82654EFD6C
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintSchemaOption, IPrintSchemaOption interface [Print Devices], IPrintSchemaOption interface [Print Devices], described, print.iprintschemaoption_interface, printerextension/IPrintSchemaOption
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	Printerextension.h
api_name:
-	IPrintSchemaOption
product:
- Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrintSchemaOption interface

Exposes a Print Schema Option object.

## Methods

<p>The <b>IPrintSchemaOption</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintSchemaOption::get_Constrained](nf-printerextension-iprintschemaoption-get_constrained.md) | Gets the constraint setting type for the schema option. |
| [IPrintSchemaOption::get_Selected](nf-printerextension-iprintschemaoption-get_selected.md) | Indicates whether this option is selected. |
| [IPrintSchemaOption::GetPropertyValue](nf-printerextension-iprintschemaoption-getpropertyvalue.md) | Gets the XML node for the &#0034;value&#0034; child element of a &#0034;Property&#0034; or a &#0034;ScoredProperty&#0034; element with the given name. |

## Remarks
You must ensure that each Feature or Option in a PrintTicket or PrintCapabilities XML document has a <i>name</i> attribute specified. This attribute is used to build the <b>IPrintSchemaOption</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh451284">IPrintSchemaFeature</a> objects. If the <i>name</i> attribute is omitted, the feature or option will not be displayed in the object model, or the Microsoft-provided print preferences experience.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451262">IPrintSchemaDisplayableElement</a>



<a href="https://msdn.microsoft.com/C9C4E085-1F2A-4610-AF2A-8F87E5CE7BCA">IPrintSchemaFeature::GetOption</a>



<a href="https://msdn.microsoft.com/C22BC037-05D2-4F44-8704-D1D56909B603">IPrintSchemaFeature::SelectedOption</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh846198">IPrintSchemaOptionCollection</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451378">IPrintSchemaPageMediaSizeOption</a>