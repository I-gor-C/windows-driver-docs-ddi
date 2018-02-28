---
UID: NN:prcomoem.IPrintOemUIMXDC
title: IPrintOemUIMXDC
author: windows-driver-content
description: This section describes the methods that are defined for the IPrintOemUIMXDC COM interface.
old-location: print\iprintoemuimxdc_interface.htm
old-project: print
ms.assetid: 4a70c0a7-9de7-48ed-a678-64832f078018
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IPrintOemUIMXDC, IPrintOemUIMXDC interface [Print Devices], IPrintOemUIMXDC interface [Print Devices], described, prcomoem/IPrintOemUIMXDC, print.iprintoemuimxdc_interface, print_unidrv-pscript_ui_120354fc-1e37-41c9-b273-c28fde18079f.xml
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
req.lib: prcomoem.h
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
-	IPrintOemUIMXDC
product: Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---

# IPrintOemUIMXDC interface

This section describes the methods that are defined for the IPrintOemUIMXDC COM interface.

## Methods

<p>The <b>IPrintOemUIMXDC</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintOemUIMXDC::AdjustDPI](nf-prcomoem-iprintoemuimxdc-adjustdpi.md) | The IPrintOemUIMXDC::AdjustDPI method enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of image resolution. |
| [IPrintOemUIMXDC::AdjustImageableArea](nf-prcomoem-iprintoemuimxdc-adjustimageablearea.md) | The IPrintOemUIMXDC::AdjustImageableArea method enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of the printable area, including orientation and direction of rotation. |
| [IPrintOemUIMXDC::AdjustImageCompression](nf-prcomoem-iprintoemuimxdc-adjustimagecompression.md) | The IPrintOemUIMXDC::AdjustImageCompression method allows an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of compression level for JPEG or PNG images. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | prcomoem.h |