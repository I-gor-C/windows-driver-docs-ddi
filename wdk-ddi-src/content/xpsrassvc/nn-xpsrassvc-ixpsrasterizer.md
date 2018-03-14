---
UID: NN:xpsrassvc.IXpsRasterizer
title: IXpsRasterizer
author: windows-driver-content
description: The IXpsRasterizer interface represents an XPS rasterizer that can create a bitmap image of an XPS fixed page or of a rectangular region of a fixed page.
old-location: print\ixpsrasterizer_interface.htm
old-project: print
ms.assetid: 1ef99120-2b3b-45aa-bcf7-16bcb9656089
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IXpsRasterizer, IXpsRasterizer interface [Print Devices], IXpsRasterizer interface [Print Devices], described, print.ixpsrasterizer_interface, print_xpsrast_e8c45bd1-2f79-4e4f-b6c4-034c703ff173.xml, xpsrassvc/IXpsRasterizer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: xpsrassvc.h
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
-	xpsrassvc.h
api_name:
-	IXpsRasterizer
product: Windows
targetos: Windows
req.typenames: XPSRAS_BACKGROUND_COLOR
req.product: Windows 10 or later.
---

# IXpsRasterizer interface

The <b>IXpsRasterizer</b> interface represents an XPS rasterizer that can create a bitmap image of an XPS fixed page or of a rectangular region of a fixed page.

A client obtains an <b>IXpsRasterizer</b> interface instance by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556350">IXpsRasterizationFactory::CreateRasterizer</a> method.

## Methods

<p>The <b>IXpsRasterizer</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IXpsRasterizer::RasterizeRect](nf-xpsrassvc-ixpsrasterizer-rasterizerect.md) | The RasterizeRect method rasterizes an axis-aligned, rectangular region of an XPS fixed page. |
| [IXpsRasterizer::SetMinimalLineWidth](nf-xpsrassvc-ixpsrasterizer-setminimallinewidth.md) | The SetMinimalLineWidth method allows the caller to set the minimum thickness (in pixels) of the lines that the device can render. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | xpsrassvc.h |