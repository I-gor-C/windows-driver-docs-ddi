---
UID: NN:printerextension.IPrintSchemaFeature
title: IPrintSchemaFeature
author: windows-driver-content
description: Exposes a Print Schema Feature element.
old-location: print\iprintschemafeature_interface.htm
old-project: print
ms.assetid: AAC2A60B-9E70-4809-969A-68783A91B093
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintSchemaFeature, IPrintSchemaFeature interface [Print Devices], IPrintSchemaFeature interface [Print Devices], described, print.iprintschemafeature_interface, printerextension/IPrintSchemaFeature
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
-	IPrintSchemaFeature
product:
- Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrintSchemaFeature interface

Exposes a Print Schema Feature element.

## Methods

<p>The <b>IPrintSchemaFeature</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintSchemaFeature::get_DisplayUI](nf-printerextension-iprintschemafeature-get_displayui.md) | Gets the setting that indicates whether or not to show the print UI. |
| [IPrintSchemaFeature::get_SelectedOption](nf-printerextension-iprintschemafeature-get_selectedoption.md) | Gets an IPrintSchemaOption representing the selected option. |
| [IPrintSchemaFeature::get_SelectionType](nf-printerextension-iprintschemafeature-get_selectiontype.md) | Gets the selection type of the Feature. |
| [IPrintSchemaFeature::GetOption](nf-printerextension-iprintschemafeature-getoption.md) | Gets the option with the given name. |
| [IPrintSchemaFeature::put_SelectedOption](nf-printerextension-iprintschemafeature-put_selectedoption.md) | Changes the selected option of the Print Schema Feature element to the specified IPrintSchemaOption element. |

## Remarks
You must ensure that each Feature or Option in a PrintTicket or PrintCapabilities XML document has a <i>name</i> attribute specified. This attribute is used to build the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451335">IPrintSchemaOption</a> and <b>IPrintSchemaFeature</b> objects. If the <i>name</i> attribute is omitted, the feature or option will not be displayed in the object model, or the Microsoft-provided print preferences experience.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/AC6434F5-0892-4426-98BB-BC02AD17917B">IPrintSchemaCapabilities::GetFeature</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451262">IPrintSchemaDisplayableElement</a>



<a href="https://msdn.microsoft.com/2E65BDF2-9539-402B-AF19-8CBC84F9C018">IPrintSchemaTicket::GetFeature</a>



<a href="https://msdn.microsoft.com/3BD7B8D6-B06F-492F-A73E-DA0799387B2A">IPrintSchemaTicket::GetFeatureByKeyName</a>