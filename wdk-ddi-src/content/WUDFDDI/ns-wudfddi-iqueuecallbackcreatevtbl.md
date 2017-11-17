---
UID: NS.wudfddi.IQueueCallbackCreateVtbl
title: IQueueCallbackCreateVtbl
author: windows-driver-content
description: 
ms.assetid: 26a4c1c0-5895-443c-9282-822c699ebf92
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IQueueCallbackCreateVtbl, IQueueCallbackCreateVtbl
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

# IQueueCallbackCreateVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IQueueCallbackCreate *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IQueueCallbackCreate *This) AddRef			
 	
### -field ULONG(* )(IQueueCallbackCreate *This) Release			
 	
### -field void(* )(IQueueCallbackCreate *This,IWDFIoQueue *pWdfQueue,IWDFIoRequest *pWDFRequest,IWDFFile *pWdfFileObject) OnCreateFile			
 	
## -remarks

## -see-also