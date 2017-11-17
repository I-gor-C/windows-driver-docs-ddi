---
UID: NS.wudfddi.IQueueCallbackIoStopVtbl
title: IQueueCallbackIoStopVtbl
author: windows-driver-content
description: 
ms.assetid: c4335db9-7ab5-4655-9f89-132513485bcb
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IQueueCallbackIoStopVtbl, IQueueCallbackIoStopVtbl
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

# IQueueCallbackIoStopVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IQueueCallbackIoStop *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IQueueCallbackIoStop *This) AddRef			
 	
### -field ULONG(* )(IQueueCallbackIoStop *This) Release			
 	
### -field void(* )(IQueueCallbackIoStop *This,IWDFIoQueue *pWdfQueue,IWDFIoRequest *pWdfRequest,ULONG ActionFlags) OnIoStop			
 	
## -remarks

## -see-also