---
UID: NS.wudfddi.IWDFFile3Vtbl
title: IWDFFile3Vtbl
author: windows-driver-content
description: 
ms.assetid: 1ff7091a-2ba3-43c5-a1d4-d57cecc11b0e
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFFile3Vtbl, IWDFFile3Vtbl
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

# IWDFFile3Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFFile3 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFFile3 *This) AddRef			
 	
### -field ULONG(* )(IWDFFile3 *This) Release			
 	
### -field HRESULT(* )(IWDFFile3 *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFFile3 *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFFile3 *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFFile3 *This) AcquireLock			
 	
### -field void(* )(IWDFFile3 *This) ReleaseLock			
 	
### -field HRESULT(* )(IWDFFile3 *This,PWSTR pFileName,DWORD *pdwFileNameLengthInChars) RetrieveFileName			
 	
### -field void(* )(IWDFFile3 *This,IWDFDevice **ppWdfDevice) GetDevice			
 	
### -field HRESULT(* )(IWDFFile3 *This,WCHAR *pCountedFileName,DWORD *pdwCountedFileNameLengthInChars) RetrieveCountedFileName			
 	
### -field void(* )(IWDFFile3 *This,IWDFFile **ppRelatedFileObj) GetRelatedFileObject			
 	
### -field void(* )(IWDFFile3 *This,DWORD *pdwProcessId) GetInitiatorProcessId			
 	
## -remarks

## -see-also