---
UID: NS.wudfddi.IWDFDriverCreatedFileVtbl
title: IWDFDriverCreatedFileVtbl
author: windows-driver-content
description: 
ms.assetid: 1e4b9c84-cd8b-43b1-a2cf-8dc2cde69051
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFDriverCreatedFileVtbl, IWDFDriverCreatedFileVtbl
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

# IWDFDriverCreatedFileVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFDriverCreatedFile *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFDriverCreatedFile *This) AddRef			
 	
### -field ULONG(* )(IWDFDriverCreatedFile *This) Release			
 	
### -field HRESULT(* )(IWDFDriverCreatedFile *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFDriverCreatedFile *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFDriverCreatedFile *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFDriverCreatedFile *This) AcquireLock			
 	
### -field void(* )(IWDFDriverCreatedFile *This) ReleaseLock			
 	
### -field HRESULT(* )(IWDFDriverCreatedFile *This,PWSTR pFileName,DWORD *pdwFileNameLengthInChars) RetrieveFileName			
 	
### -field void(* )(IWDFDriverCreatedFile *This,IWDFDevice **ppWdfDevice) GetDevice			
 	
### -field void(* )(IWDFDriverCreatedFile *This) Close			
 	
## -remarks

## -see-also