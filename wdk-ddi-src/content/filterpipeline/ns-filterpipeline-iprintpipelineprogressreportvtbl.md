---
UID: NS.filterpipeline.IPrintPipelineProgressReportVtbl
title: IPrintPipelineProgressReportVtbl
author: windows-driver-content
description: 
ms.assetid: c6324459-d3bf-40a5-ae54-62b9eed97042
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintPipelineProgressReportVtbl, IPrintPipelineProgressReportVtbl
req.header: filterpipeline.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# IPrintPipelineProgressReportVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintPipelineProgressReport *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintPipelineProgressReport *This) AddRef			
 	
### -field ULONG(* )(IPrintPipelineProgressReport *This) Release			
 	
### -field HRESULT(* )(IPrintPipelineProgressReport *This,EXpsJobConsumption update) ReportProgress			
 	
## -remarks

## -see-also