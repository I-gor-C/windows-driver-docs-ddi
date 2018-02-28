---
UID: NF:filterpipeline.IPrintPipelineFilter.StartOperation
title: IPrintPipelineFilter::StartOperation method
author: windows-driver-content
description: The StartOperation method starts the operation of a filter. The filter reads, processes, and writes data in this method.
old-location: print\iprintpipelinefilter_startoperation.htm
old-project: print
ms.assetid: 87139670-9b51-4ced-9624-2ec9f4726a84
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IPrintPipelineFilter, IPrintPipelineFilter interface [Print Devices], StartOperation method, IPrintPipelineFilter::StartOperation, StartOperation method [Print Devices], StartOperation method [Print Devices], IPrintPipelineFilter interface, StartOperation,IPrintPipelineFilter.StartOperation, filterpipeline/IPrintPipelineFilter::StartOperation, filterpipeline_9040ff14-d052-4360-bb31-b171581c14b6.xml, print.iprintpipelinefilter_startoperation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: filterpipeline.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: Filterpipeline.idl
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: filterpipeline.h
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	Filterpipeline.h
api_name:
-	IPrintPipelineFilter.StartOperation
product: Windows
targetos: Windows
req.typenames: EXpsFontRestriction
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

A filter returns the <code>StartOperation</code> call only when the filter processing is complete.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | filterpipeline.h |
| **Library** | filterpipeline.h |