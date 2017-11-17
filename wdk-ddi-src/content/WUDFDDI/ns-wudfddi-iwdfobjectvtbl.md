---
UID: NS.wudfddi.IWDFObjectVtbl
title: IWDFObjectVtbl
author: windows-driver-content
description: 
ms.assetid: ddbe551a-b110-4c99-aeb7-ea54d84ce2eb
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFObjectVtbl, IWDFObjectVtbl
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

# IWDFObjectVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFObject *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFObject *This) AddRef			
 	
### -field ULONG(* )(IWDFObject *This) Release			
 	
### -field HRESULT(* )(IWDFObject *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFObject *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFObject *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFObject *This) AcquireLock			
 	
### -field void(* )(IWDFObject *This) ReleaseLock			
 	
## -remarks

## -see-also