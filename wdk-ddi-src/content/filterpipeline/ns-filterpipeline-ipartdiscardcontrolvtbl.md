---
UID: NS.filterpipeline.IPartDiscardControlVtbl
title: IPartDiscardControlVtbl
author: windows-driver-content
description: 
ms.assetid: bf4be72e-dc40-4930-8c40-6a0999b480d9
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPartDiscardControlVtbl, IPartDiscardControlVtbl
req.header: filterpipeline.h
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

# IPartDiscardControlVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPartDiscardControl *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPartDiscardControl *This) AddRef			
 	
### -field ULONG(* )(IPartDiscardControl *This) Release			
 	
### -field HRESULT(* )(IPartDiscardControl *This,BSTR *uriSentinelPage,BSTR *uriPartToDiscard) GetDiscardProperties			
 	
## -remarks

## -see-also