---
UID: NS.wudfddi.IWDFFile2Vtbl
title: IWDFFile2Vtbl
author: windows-driver-content
description: 
ms.assetid: 101c076a-7de0-4283-b2b8-9f690ee62d0f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFFile2Vtbl, IWDFFile2Vtbl
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

# IWDFFile2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFFile2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFFile2 *This) AddRef			
 	
### -field ULONG(* )(IWDFFile2 *This) Release			
 	
### -field HRESULT(* )(IWDFFile2 *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFFile2 *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFFile2 *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFFile2 *This) AcquireLock			
 	
### -field void(* )(IWDFFile2 *This) ReleaseLock			
 	
### -field HRESULT(* )(IWDFFile2 *This,PWSTR pFileName,DWORD *pdwFileNameLengthInChars) RetrieveFileName			
 	
### -field void(* )(IWDFFile2 *This,IWDFDevice **ppWdfDevice) GetDevice			
 	
### -field HRESULT(* )(IWDFFile2 *This,WCHAR *pCountedFileName,DWORD *pdwCountedFileNameLengthInChars) RetrieveCountedFileName			
 	
### -field void(* )(IWDFFile2 *This,IWDFFile **ppRelatedFileObj) GetRelatedFileObject			
 	
## -remarks

## -see-also