---
UID: NS.wudfddi.IRequestCallbackRequestCompletionVtbl
title: IRequestCallbackRequestCompletionVtbl
author: windows-driver-content
description: 
ms.assetid: 6ae5bbd0-7c65-40be-9163-cf07d0cc483f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IRequestCallbackRequestCompletionVtbl, IRequestCallbackRequestCompletionVtbl
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

# IRequestCallbackRequestCompletionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IRequestCallbackRequestCompletion *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IRequestCallbackRequestCompletion *This) AddRef			
 	
### -field ULONG(* )(IRequestCallbackRequestCompletion *This) Release			
 	
### -field void(* )(IRequestCallbackRequestCompletion *This,IWDFIoRequest *pWdfRequest,IWDFIoTarget *pIoTarget,IWDFRequestCompletionParams *pParams, void *pContext) OnCompletion			
 	
## -remarks

## -see-also