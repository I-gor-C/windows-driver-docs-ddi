---
UID: NS.wudfddi.IRequestCallbackCancelVtbl
title: IRequestCallbackCancelVtbl
author: windows-driver-content
description: 
ms.assetid: 0367e21b-c4d0-4e0e-a1de-5d40b12c1201
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IRequestCallbackCancelVtbl, IRequestCallbackCancelVtbl
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

# IRequestCallbackCancelVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IRequestCallbackCancel *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IRequestCallbackCancel *This) AddRef			
 	
### -field ULONG(* )(IRequestCallbackCancel *This) Release			
 	
### -field void(* )(IRequestCallbackCancel *This,IWDFIoRequest *pWdfRequest) OnCancel			
 	
## -remarks

## -see-also