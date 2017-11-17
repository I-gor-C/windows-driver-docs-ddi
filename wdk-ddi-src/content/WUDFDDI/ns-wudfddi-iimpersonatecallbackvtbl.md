---
UID: NS.wudfddi.IImpersonateCallbackVtbl
title: IImpersonateCallbackVtbl
author: windows-driver-content
description: 
ms.assetid: 55c8dd84-72e3-4256-931a-84d89e5bff3c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IImpersonateCallbackVtbl, IImpersonateCallbackVtbl
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

# IImpersonateCallbackVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IImpersonateCallback *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IImpersonateCallback *This) AddRef			
 	
### -field ULONG(* )(IImpersonateCallback *This) Release			
 	
### -field void(* )(IImpersonateCallback *This, void *Context) OnImpersonate			
 	
## -remarks

## -see-also