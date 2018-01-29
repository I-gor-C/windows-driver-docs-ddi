---
UID : NF:filterpipeline.IPrintPipelineManagerControl.FilterFinished
title : IPrintPipelineManagerControl::FilterFinished method
author : windows-driver-content
description : The FilterFinished method reports that a filter is finished processing.
old-location : print\iprintpipelinemanagercontrol_filterfinished.htm
old-project : print
ms.assetid : 6393b959-f67a-42e8-bb2b-e830bcf0d45f
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : FilterFinished, print.iprintpipelinemanagercontrol_filterfinished, IPrintPipelineManagerControl interface [Print Devices], FilterFinished method, FilterFinished method [Print Devices], IPrintPipelineManagerControl interface, IPrintPipelineManagerControl, filterpipeline/IPrintPipelineManagerControl::FilterFinished, FilterFinished method [Print Devices], IPrintPipelineManagerControl::FilterFinished, filterpipeline_58038d61-195e-4144-adee-2615a62cef91.xml
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
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : Filterpipeline.idl
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : filterpipeline.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : EXpsFontRestriction
---


# FilterFinished method
The <code>FilterFinished</code> method reports that a filter is finished processing.

## Syntax

````
HRESULT STDMETHODCALLTYPE FilterFinished(
    None
);
````

## Parameters

This function has no parameters.

## Return Value

<code>FilterFinished</code> returns an <b>HRESULT</b>.

## Remarks

The filter does not need to call the <code>FilterFinished</code> method. The filter pipeline assumes the filter has finished when the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554301">IPrintPipelineFilter::StartOperation</a> method returns. <code>FilterFinished</code> is provided for compatibility and, when called, it does nothing but returns.

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