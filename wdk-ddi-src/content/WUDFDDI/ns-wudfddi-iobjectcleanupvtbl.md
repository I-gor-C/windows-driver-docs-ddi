---
UID: NS.wudfddi.IObjectCleanupVtbl
title: IObjectCleanupVtbl
author: windows-driver-content
description: 
ms.assetid: afb8a7ae-3481-432f-98a2-8d24d0253b18
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IObjectCleanupVtbl, IObjectCleanupVtbl
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

# IObjectCleanupVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IObjectCleanup *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IObjectCleanup *This) AddRef			
 	
### -field ULONG(* )(IObjectCleanup *This) Release			
 	
### -field void(* )(IObjectCleanup *This,IWDFObject *pWdfObject) OnCleanup			
 	
## -remarks

## -see-also