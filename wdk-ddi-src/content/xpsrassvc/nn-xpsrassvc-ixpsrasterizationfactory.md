---
UID: NN:xpsrassvc.IXpsRasterizationFactory
title: IXpsRasterizationFactory
author: windows-driver-content
description: The IXpsRasterizationFactory interface represents an object factory for creating XPS rasterizer objects.
old-location: print\ixpsrasterizationfactory_interface.htm
old-project: print
ms.assetid: 559bdc65-282e-42b2-998a-276202376c1e
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IXpsRasterizationFactory, IXpsRasterizationFactory interface [Print Devices], IXpsRasterizationFactory interface [Print Devices], described, print.ixpsrasterizationfactory_interface, print_xpsrast_50eb7bf8-2753-47e1-b63b-81639ac26bb7.xml, xpsrassvc/IXpsRasterizationFactory
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
-	IXpsRasterizationFactory
product: Windows
targetos: Windows
req.typenames: XPSRAS_BACKGROUND_COLOR
req.product: Windows 10 or later.
---

# IXpsRasterizationFactory interface

The <b>IXpsRasterizationFactory</b> interface represents an object factory for creating XPS rasterizer objects. Rasterizer objects created by the factory implement <a href="https://msdn.microsoft.com/1ef99120-2b3b-45aa-bcf7-16bcb9656089">IXpsRasterizer</a> interfaces. An XPSDrv filter uses a rasterizer object to convert an XPS fixed page to one or more bitmap images.

An XPSDrv filter obtains a reference to an <b>IXpsRasterizationFactory</b> interface instance from the property bag received from the print filter pipeline manager. The pipeline manager calls the filter's <a href="https://msdn.microsoft.com/library/windows/hardware/ff554291">IPrintPipelineFilter::InitializeFilter</a> method and passes in an <a href="https://msdn.microsoft.com/library/windows/hardware/ff554320">IPrintPipelinePropertyBag</a> pointer. The interface reference is a VT_UNKNOWN property value that is identified by the property name <b>MS_IXpsRasterizationFactory</b>.

## Methods

<p>The <b>IXpsRasterizationFactory</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IXpsRasterizationFactory::CreateRasterizer](nf-xpsrassvc-ixpsrasterizationfactory-createrasterizer.md) | The CreateRasterize method creates an XPS rasterizer object. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | xpsrassvc.h |