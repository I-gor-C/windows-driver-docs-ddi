---
UID: NN:filterpipeline.IPrintPipelineFilter
title: IPrintPipelineFilter
author: windows-driver-content
description: The methods in the IPrintPipelineFilter interface are called for initialization and shutdown. A filter must implement these methods.
old-location: print\iprintpipelinefilter.htm
old-project: print
ms.assetid: e8841091-1d62-4770-aa85-993b49efbd48
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintPipelineFilter, IPrintPipelineFilter interface [Print Devices], IPrintPipelineFilter interface [Print Devices], described, filterpipeline/IPrintPipelineFilter, filterpipeline_67beec81-fbba-43d2-af2f-ddbc32c68fce.xml, print.iprintpipelinefilter
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: filterpipeline.h
req.include-header: Filterpipeline.h
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
-	filterpipeline.h
api_name:
-	IPrintPipelineFilter
product:
- Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---

# IPrintPipelineFilter interface

The methods in the <code>IPrintPipelineFilter</code> interface are called for initialization and shutdown. A filter must implement these methods.

## Methods

<p>The <b>IPrintPipelineFilter</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintPipelineFilter::InitializeFilter](nf-filterpipeline-iprintpipelinefilter-initializefilter.md) | The InitializeFilter method initializes a filter. |
| [IPrintPipelineFilter::ShutdownOperation](nf-filterpipeline-iprintpipelinefilter-shutdownoperation.md) | The Pipeline Manager uses the ShutdownOperation method to shut down a filter if the print job is canceled or an error occurs. |
| [IPrintPipelineFilter::StartOperation](nf-filterpipeline-iprintpipelinefilter-startoperation.md) | The StartOperation method starts the operation of a filter. The filter reads, processes, and writes data in this method. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | filterpipeline.h (include Filterpipeline.h) |