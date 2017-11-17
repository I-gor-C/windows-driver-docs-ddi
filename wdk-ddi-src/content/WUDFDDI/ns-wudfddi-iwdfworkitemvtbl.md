---
UID: NS.wudfddi.IWDFWorkItemVtbl
title: IWDFWorkItemVtbl
author: windows-driver-content
description: 
ms.assetid: 549a6d16-6222-411f-a612-4a1889eab10c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFWorkItemVtbl, IWDFWorkItemVtbl
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

# IWDFWorkItemVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFWorkItem *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFWorkItem *This) AddRef			
 	
### -field ULONG(* )(IWDFWorkItem *This) Release			
 	
### -field HRESULT(* )(IWDFWorkItem *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFWorkItem *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFWorkItem *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFWorkItem *This) AcquireLock			
 	
### -field void(* )(IWDFWorkItem *This) ReleaseLock			
 	
### -field void(* )(IWDFWorkItem *This) Enqueue			
 	
### -field void(* )(IWDFWorkItem *This) Flush			
 	
### -field IWDFObject *(* )(IWDFWorkItem *This) GetParentObject			
 	
## -remarks

## -see-also