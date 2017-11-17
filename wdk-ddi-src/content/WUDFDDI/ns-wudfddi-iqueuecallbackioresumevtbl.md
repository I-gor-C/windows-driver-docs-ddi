---
UID: NS.wudfddi.IQueueCallbackIoResumeVtbl
title: IQueueCallbackIoResumeVtbl
author: windows-driver-content
description: 
ms.assetid: 04dd38df-8aff-4d8e-895a-8403978aecd3
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IQueueCallbackIoResumeVtbl, IQueueCallbackIoResumeVtbl
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

# IQueueCallbackIoResumeVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IQueueCallbackIoResume *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IQueueCallbackIoResume *This) AddRef			
 	
### -field ULONG(* )(IQueueCallbackIoResume *This) Release			
 	
### -field void(* )(IQueueCallbackIoResume *This,IWDFIoQueue *pWdfQueue,IWDFIoRequest *pWdfRequest) OnIoResume			
 	
## -remarks

## -see-also