---
UID: NS.wudfddi.IFileCallbackCleanupVtbl
title: IFileCallbackCleanupVtbl
author: windows-driver-content
description: 
ms.assetid: 8a2c9645-56b8-4894-a8f2-6149f6f33eda
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IFileCallbackCleanupVtbl, IFileCallbackCleanupVtbl
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

# IFileCallbackCleanupVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IFileCallbackCleanup *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IFileCallbackCleanup *This) AddRef			
 	
### -field ULONG(* )(IFileCallbackCleanup *This) Release			
 	
### -field void(* )(IFileCallbackCleanup *This,IWDFFile *pWdfFileObject) OnCleanupFile			
 	
## -remarks

## -see-also