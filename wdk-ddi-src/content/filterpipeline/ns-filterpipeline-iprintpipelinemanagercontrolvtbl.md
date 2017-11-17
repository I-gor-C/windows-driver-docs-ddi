---
UID: NS.filterpipeline.IPrintPipelineManagerControlVtbl
title: IPrintPipelineManagerControlVtbl
author: windows-driver-content
description: 
ms.assetid: b09fc02c-7de3-4ad5-bdcb-8bd354302490
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintPipelineManagerControlVtbl, IPrintPipelineManagerControlVtbl
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

# IPrintPipelineManagerControlVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintPipelineManagerControl *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintPipelineManagerControl *This) AddRef			
 	
### -field ULONG(* )(IPrintPipelineManagerControl *This) Release			
 	
### -field HRESULT(* )(IPrintPipelineManagerControl *This,HRESULT hrReason,IImgErrorInfo *pReason) RequestShutdown			
 	
### -field HRESULT(* )(IPrintPipelineManagerControl *This) FilterFinished			
 	
## -remarks

## -see-also