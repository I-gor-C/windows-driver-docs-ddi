---
UID: NN:filterpipeline.IPrintPipelineManagerControl
title: IPrintPipelineManagerControl
author: windows-driver-content
description: The IPrintPipelineManagerControl interface is passed to each filter in the IPrintPipelineFilter::InitializeFilter method.
old-location: print\iprintpipelinemanagercontrol.htm
old-project: print
ms.assetid: 82efbe8d-0928-4550-9de1-a806a00791eb
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintPipelineManagerControl, IPrintPipelineManagerControl interface [Print Devices], IPrintPipelineManagerControl interface [Print Devices], described, filterpipeline/IPrintPipelineManagerControl, filterpipeline_5b9732d1-6a75-4059-84fa-1bbbdeb70eb3.xml, print.iprintpipelinemanagercontrol
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
req.lib: filterpipeline.h
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
-	IPrintPipelineManagerControl
product: Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---

# IPrintPipelineManagerControl interface

The <code>IPrintPipelineManagerControl</code> interface is passed to each filter in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554291">IPrintPipelineFilter::InitializeFilter</a> method. Filters use this interface to:
<ul>
<li>
Request shutdown in low-memory situations.

</li>
<li>
Report when the filters are finished processing.

</li>
</ul>

## Methods

<p>The <b>IPrintPipelineManagerControl</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintPipelineManagerControl::FilterFinished](nf-filterpipeline-iprintpipelinemanagercontrol-filterfinished.md) | The FilterFinished method reports that a filter is finished processing. |
| [IPrintPipelineManagerControl::RequestShutdown](nf-filterpipeline-iprintpipelinemanagercontrol-requestshutdown.md) | The RequestShutdown method requests that a pipeline be shut down. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | filterpipeline.h (include Filterpipeline.h) |