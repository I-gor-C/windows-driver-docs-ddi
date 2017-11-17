---
UID: NS.wudfddi.IQueueCallbackWriteVtbl
title: IQueueCallbackWriteVtbl
author: windows-driver-content
description: 
ms.assetid: 2b512330-f28d-4a81-a638-195d7ef2cbdc
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IQueueCallbackWriteVtbl, IQueueCallbackWriteVtbl
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

# IQueueCallbackWriteVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IQueueCallbackWrite *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IQueueCallbackWrite *This) AddRef			
 	
### -field ULONG(* )(IQueueCallbackWrite *This) Release			
 	
### -field void(* )(IQueueCallbackWrite *This,IWDFIoQueue *pWdfQueue,IWDFIoRequest *pWdfRequest,SIZE_T NumOfBytesToWrite) OnWrite			
 	
## -remarks

## -see-also