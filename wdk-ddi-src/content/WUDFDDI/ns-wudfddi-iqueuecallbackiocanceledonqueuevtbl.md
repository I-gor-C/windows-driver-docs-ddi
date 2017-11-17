---
UID: NS.wudfddi.IQueueCallbackIoCanceledOnQueueVtbl
title: IQueueCallbackIoCanceledOnQueueVtbl
author: windows-driver-content
description: 
ms.assetid: 29d840ef-26e6-4ff8-a200-ef57942379ad
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IQueueCallbackIoCanceledOnQueueVtbl, IQueueCallbackIoCanceledOnQueueVtbl
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

# IQueueCallbackIoCanceledOnQueueVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IQueueCallbackIoCanceledOnQueue *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IQueueCallbackIoCanceledOnQueue *This) AddRef			
 	
### -field ULONG(* )(IQueueCallbackIoCanceledOnQueue *This) Release			
 	
### -field void(* )(IQueueCallbackIoCanceledOnQueue *This,IWDFIoQueue *pWdfQueue,IWDFIoRequest *pWdfRequest) OnIoCanceledOnQueue			
 	
## -remarks

## -see-also