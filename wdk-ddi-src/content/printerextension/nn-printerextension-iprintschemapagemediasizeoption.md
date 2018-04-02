---
UID: NN:printerextension.IPrintSchemaPageMediaSizeOption
title: IPrintSchemaPageMediaSizeOption
author: windows-driver-content
description: Exposes a Print Schema PageMediaSize Option element.
old-location: print\iprintschemapagemediasizeoption_interface.htm
old-project: print
ms.assetid: 631F5ECF-EA1E-4483-99F8-67C9A8C42EDF
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintSchemaPageMediaSizeOption, IPrintSchemaPageMediaSizeOption interface [Print Devices], IPrintSchemaPageMediaSizeOption interface [Print Devices], described, print.iprintschemapagemediasizeoption_interface, printerextension/IPrintSchemaPageMediaSizeOption
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
-	IPrintSchemaPageMediaSizeOption
product:
- Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrintSchemaPageMediaSizeOption interface

Exposes a Print Schema PageMediaSize Option element.

## Methods

<p>The <b>IPrintSchemaPageMediaSizeOption</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintSchemaPageMediaSizeOption::get_HeightInMicrons](nf-printerextension-iprintschemapagemediasizeoption-get_heightinmicrons.md) | Gets the height of the page in microns. |
| [IPrintSchemaPageMediaSizeOption::get_WidthInMicrons](nf-printerextension-iprintschemapagemediasizeoption-get_widthinmicrons.md) | Gets the width of the page in microns. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451335">IPrintSchemaOption</a>