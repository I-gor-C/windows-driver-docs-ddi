---
UID : NN:filterpipeline.IPrintPipelineProgressReport
title : IPrintPipelineProgressReport
author : windows-driver-content
description : A rendering filter uses the IPrintPipelineProgressReport interface to send progress status to a spooler.
old-location : print\iprintpipelineprogressreport.htm
old-project : print
ms.assetid : 7a2644af-fdfe-4481-8c44-c40244b8a00e
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : print.iprintpipelineprogressreport, IPrintPipelineProgressReport interface [Print Devices], IPrintPipelineProgressReport interface [Print Devices], described, IPrintPipelineProgressReport, filterpipeline/IPrintPipelineProgressReport, filterpipeline_de104fc6-8ac2-4a10-ab09-09596a093835.xml
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
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
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

# IPrintPipelineProgressReport interface

A rendering filter uses the <code>IPrintPipelineProgressReport</code> interface to send progress status to a spooler. 

A rendering filter should search for the <b>XPS_FP_PROGRESS_REPORT</b> property in a property bag, get the progress, and then remove it from the property bag. If there are no rendering filters, the filter pipeline sends the notifications to the spooler. It is very important for a rendering filter to remove the progress and send progress status to the spooler; if progress status is not handled correctly, the spooler may get conflicting progress reports.

## Methods

<p>The <b>IPrintPipelineProgressReport</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [filterpipeline.IPrintPipelineProgressReport.ReportProgress](nf-filterpipeline-iprintpipelineprogressreport-reportprogress.md) | The ReportProgress method reports the progress of the XPS job consumption to the pipeline manager. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | filterpipeline.h (include Filterpipeline.h) |
| **DLL** |  |