---
UID : NF:filterpipeline.IPrintPipelineFilter.StartOperation
title : IPrintPipelineFilter::StartOperation method
author : windows-driver-content
description : The StartOperation method starts the operation of a filter. The filter reads, processes, and writes data in this method.
old-location : print\iprintpipelinefilter_startoperation.htm
old-project : print
ms.assetid : 87139670-9b51-4ced-9624-2ec9f4726a84
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : IPrintPipelineFilter, IPrintPipelineFilter::StartOperation, StartOperation
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : filterpipeline.h
req.include-header : 
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IPrintPipelineFilter.StartOperation
req.alt-loc : Filterpipeline.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : Filterpipeline.idl
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : EXpsFontRestriction
---


# StartOperation method
The <code>StartOperation</code> method starts the operation of a filter. The filter reads, processes, and writes data in this method.

## Syntax

````
HRESULT STDMETHODCALLTYPE StartOperation(
    None
);
````

## Parameters

This function has no parameters.

## Return Value

<code>StartOperation</code> returns an <b>HRESULT</b> value.

## Remarks

A filter returns the <code>StartOperation</code> call only when the filter processing is complete.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | filterpipeline.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |