---
UID: NS.wudfddi.IQueueCallbackDefaultIoHandlerVtbl
title: IQueueCallbackDefaultIoHandlerVtbl
author: windows-driver-content
description: 
ms.assetid: b8220141-4591-49da-aa7a-6842fcf6de53
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IQueueCallbackDefaultIoHandlerVtbl, IQueueCallbackDefaultIoHandlerVtbl
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

# IQueueCallbackDefaultIoHandlerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IQueueCallbackDefaultIoHandler *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IQueueCallbackDefaultIoHandler *This) AddRef			
 	
### -field ULONG(* )(IQueueCallbackDefaultIoHandler *This) Release			
 	
### -field void(* )(IQueueCallbackDefaultIoHandler *This,IWDFIoQueue *pWdfQueue,IWDFIoRequest *pWdfRequest) OnDefaultIoHandler			
 	
## -remarks

## -see-also