---
UID: NS.wudfddi.IQueueCallbackStateChangeVtbl
title: IQueueCallbackStateChangeVtbl
author: windows-driver-content
description: 
ms.assetid: ff65a748-f24a-4da7-83da-3a5ce13f35a9
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IQueueCallbackStateChangeVtbl, IQueueCallbackStateChangeVtbl
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

# IQueueCallbackStateChangeVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IQueueCallbackStateChange *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IQueueCallbackStateChange *This) AddRef			
 	
### -field ULONG(* )(IQueueCallbackStateChange *This) Release			
 	
### -field void(* )(IQueueCallbackStateChange *This,IWDFIoQueue *pWdfQueue,WDF_IO_QUEUE_STATE QueueState) OnStateChange			
 	
## -remarks

## -see-also