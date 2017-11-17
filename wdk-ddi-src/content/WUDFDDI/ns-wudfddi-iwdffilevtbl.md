---
UID: NS.wudfddi.IWDFFileVtbl
title: IWDFFileVtbl
author: windows-driver-content
description: 
ms.assetid: f5b5ab47-9119-4735-b23b-98a5166f564b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFFileVtbl, IWDFFileVtbl
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

# IWDFFileVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFFile *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFFile *This) AddRef			
 	
### -field ULONG(* )(IWDFFile *This) Release			
 	
### -field HRESULT(* )(IWDFFile *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFFile *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFFile *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFFile *This) AcquireLock			
 	
### -field void(* )(IWDFFile *This) ReleaseLock			
 	
### -field HRESULT(* )(IWDFFile *This,PWSTR pFileName,DWORD *pdwFileNameLengthInChars) RetrieveFileName			
 	
### -field void(* )(IWDFFile *This,IWDFDevice **ppWdfDevice) GetDevice			
 	
## -remarks

## -see-also