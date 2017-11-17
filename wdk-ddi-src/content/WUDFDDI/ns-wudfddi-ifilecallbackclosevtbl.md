---
UID: NS.wudfddi.IFileCallbackCloseVtbl
title: IFileCallbackCloseVtbl
author: windows-driver-content
description: 
ms.assetid: a5dc7ac8-a890-4d3d-a3e4-d28e355674a6
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IFileCallbackCloseVtbl, IFileCallbackCloseVtbl
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

# IFileCallbackCloseVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IFileCallbackClose *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IFileCallbackClose *This) AddRef			
 	
### -field ULONG(* )(IFileCallbackClose *This) Release			
 	
### -field void(* )(IFileCallbackClose *This,IWDFFile *pWdfFileObject) OnCloseFile			
 	
## -remarks

## -see-also