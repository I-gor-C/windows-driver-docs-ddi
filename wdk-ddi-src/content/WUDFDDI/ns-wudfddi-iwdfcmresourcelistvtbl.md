---
UID: NS.wudfddi.IWDFCmResourceListVtbl
title: IWDFCmResourceListVtbl
author: windows-driver-content
description: 
ms.assetid: 22cbbf8a-6dd4-44e5-bf69-ec5b4beb3fd5
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFCmResourceListVtbl, IWDFCmResourceListVtbl
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

# IWDFCmResourceListVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFCmResourceList *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFCmResourceList *This) AddRef			
 	
### -field ULONG(* )(IWDFCmResourceList *This) Release			
 	
### -field HRESULT(* )(IWDFCmResourceList *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFCmResourceList *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFCmResourceList *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFCmResourceList *This) AcquireLock			
 	
### -field void(* )(IWDFCmResourceList *This) ReleaseLock			
 	
### -field ULONG(* )(IWDFCmResourceList *This) GetCount			
 	
### -field PCM_PARTIAL_RESOURCE_DESCRIPTOR(* )(IWDFCmResourceList *This,ULONG Index) GetDescriptor			
 	
## -remarks

## -see-also