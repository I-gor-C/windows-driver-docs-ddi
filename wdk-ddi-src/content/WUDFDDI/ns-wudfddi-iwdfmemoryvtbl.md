---
UID: NS.wudfddi.IWDFMemoryVtbl
title: IWDFMemoryVtbl
author: windows-driver-content
description: 
ms.assetid: c27f9d09-a94a-4b25-8c78-0ee59ab8a130
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFMemoryVtbl, IWDFMemoryVtbl
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

# IWDFMemoryVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFMemory *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFMemory *This) AddRef			
 	
### -field ULONG(* )(IWDFMemory *This) Release			
 	
### -field HRESULT(* )(IWDFMemory *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFMemory *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFMemory *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFMemory *This) AcquireLock			
 	
### -field void(* )(IWDFMemory *This) ReleaseLock			
 	
### -field HRESULT(* )(IWDFMemory *This,IWDFMemory *Source,PWDFMEMORY_OFFSET SourceOffset) CopyFromMemory			
 	
### -field HRESULT(* )(IWDFMemory *This,ULONG_PTR SourceOffset, void *TargetBuffer,SIZE_T NumOfBytesToCopyTo) CopyToBuffer			
 	
### -field HRESULT(* )(IWDFMemory *This,ULONG_PTR DestOffset, void *SourceBuffer,SIZE_T NumOfBytesToCopyFrom) CopyFromBuffer			
 	
### -field SIZE_T(* )(IWDFMemory *This) GetSize			
 	
### -field void *(* )(IWDFMemory *This,SIZE_T *BufferSize) GetDataBuffer			
 	
### -field void(* )(IWDFMemory *This, void *Buffer,SIZE_T BufferSize) SetBuffer			
 	
## -remarks

## -see-also