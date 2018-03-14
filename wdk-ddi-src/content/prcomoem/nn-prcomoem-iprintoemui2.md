---
UID: NN:prcomoem.IPrintOemUI2
title: IPrintOemUI2
author: windows-driver-content
description: This section describes the methods defined for the IPrintOemUI2 COM interface.
old-location: print\iprintoemui2_interface.htm
old-project: print
ms.assetid: 9b7afb56-7abb-4f20-b69d-12a28d7e3617
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintOemUI2, IPrintOemUI2 interface [Print Devices], IPrintOemUI2 interface [Print Devices], described, prcomoem/IPrintOemUI2, print.iprintoemui2_interface, print_unidrv-pscript_ui_838f6394-df99-4045-9059-6ff480212733.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: prcomoem.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
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
-	prcomoem.h
api_name:
-	IPrintOemUI2
product: Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---

# IPrintOemUI2 interface

This section describes the methods defined for the <b>IPrintOemUI2</b> COM interface.

## Methods

<p>The <b>IPrintOemUI2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintOemUI2::DocumentEvent](nf-prcomoem-iprintoemui2-documentevent.md) | The IPrintOemUI2::DocumentEvent method allows a UI plug-in to replace the core driver UI module's default implementation of the DrvDocumentEvent DDI. |
| [IPrintOemUI2::HideStandardUI](nf-prcomoem-iprintoemui2-hidestandardui.md) | The IPrintOemUI2::HideStandardUI method allows a user interface plug-in to specify whether the standard property sheets should be displayed or hidden. |
| [IPrintOemUI2::QueryJobAttributes](nf-prcomoem-iprintoemui2-queryjobattributes.md) | The IPrintOemUI2::QueryJobAttributes method allows a UI plug-in to postprocess the core driver's results after a call to the DrvQueryJobAttributes DDI. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | prcomoem.h |