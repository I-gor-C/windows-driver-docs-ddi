---
UID: NS.wudfddi.IQueueCallbackReadVtbl
title: IQueueCallbackReadVtbl
author: windows-driver-content
description: 
ms.assetid: a7dfa4d6-e8c4-4f0f-b442-b1f7af309f90
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IQueueCallbackReadVtbl, IQueueCallbackReadVtbl
req.header: wudfddi.h
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

# IQueueCallbackReadVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IQueueCallbackRead *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IQueueCallbackRead *This) AddRef			
 	
### -field ULONG(* )(IQueueCallbackRead *This) Release			
 	
### -field void(* )(IQueueCallbackRead *This,IWDFIoQueue *pWdfQueue,IWDFIoRequest *pWdfRequest,SIZE_T NumOfBytesToRead) OnRead			
 	
## -remarks

## -see-also