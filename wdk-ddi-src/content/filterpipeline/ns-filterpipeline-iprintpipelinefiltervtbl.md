---
UID: NS.filterpipeline.IPrintPipelineFilterVtbl
title: IPrintPipelineFilterVtbl
author: windows-driver-content
description: 
ms.assetid: 6cbbff7b-1ffc-40fc-9882-92817bf346f1
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintPipelineFilterVtbl, IPrintPipelineFilterVtbl
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

# IPrintPipelineFilterVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintPipelineFilter *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintPipelineFilter *This) AddRef			
 	
### -field ULONG(* )(IPrintPipelineFilter *This) Release			
 	
### -field HRESULT(* )(IPrintPipelineFilter *This,IInterFilterCommunicator *pINegotiation,IPrintPipelinePropertyBag *pIPropertyBag,IPrintPipelineManagerControl *pIPipelineControl) InitializeFilter			
 	
### -field HRESULT(* )(IPrintPipelineFilter *This) ShutdownOperation			
 	
### -field HRESULT(* )(IPrintPipelineFilter *This) StartOperation			
 	
## -remarks

## -see-also