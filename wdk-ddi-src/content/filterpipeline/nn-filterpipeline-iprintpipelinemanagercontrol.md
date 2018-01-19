---
UID : NN:filterpipeline.IPrintPipelineManagerControl
title : IPrintPipelineManagerControl
author : windows-driver-content
description : The IPrintPipelineManagerControl interface is passed to each filter in the IPrintPipelineFilter::InitializeFilter method.
old-location : print\iprintpipelinemanagercontrol.htm
old-project : print
ms.assetid : 82efbe8d-0928-4550-9de1-a806a00791eb
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : IXpsPartIterator, IXpsPartIterator::Reset, Reset
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : filterpipeline.h
req.include-header : Filterpipeline.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IPrintPipelineManagerControl
req.alt-loc : filterpipeline.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : EXpsFontRestriction
---

# IPrintPipelineManagerControl interface

The <code>IPrintPipelineManagerControl</code> interface is passed to each filter in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554291">IPrintPipelineFilter::InitializeFilter</a> method. Filters use this interface to:

Request shutdown in low-memory situations.

Report when the filters are finished processing.

## Methods

<p>The <b>IPrintPipelineManagerControl</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [filterpipeline.IPrintPipelineManagerControl.FilterFinished](nf-filterpipeline-iprintpipelinemanagercontrol-filterfinished.md) | The FilterFinished method reports that a filter is finished processing. |
| [filterpipeline.IPrintPipelineManagerControl.RequestShutdown](nf-filterpipeline-iprintpipelinemanagercontrol-requestshutdown.md) | The RequestShutdown method requests that a pipeline be shut down. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | filterpipeline.h (include Filterpipeline.h) |
| **DLL** |  |