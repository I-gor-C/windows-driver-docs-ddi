---
UID: NS.wudfddi.IWDFIoTargetVtbl
title: IWDFIoTargetVtbl
author: windows-driver-content
description: 
ms.assetid: e0f6b620-01d7-4d55-8e35-c706d69a4697
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFIoTargetVtbl, IWDFIoTargetVtbl
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

# IWDFIoTargetVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFIoTarget *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFIoTarget *This) AddRef			
 	
### -field ULONG(* )(IWDFIoTarget *This) Release			
 	
### -field HRESULT(* )(IWDFIoTarget *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFIoTarget *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFIoTarget *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFIoTarget *This) AcquireLock			
 	
### -field void(* )(IWDFIoTarget *This) ReleaseLock			
 	
### -field void(* )(IWDFIoTarget *This,IWDFFile **ppWdfFile) GetTargetFile			
 	
### -field void(* )(IWDFIoTarget *This,IWDFFile *pFile) CancelSentRequestsForFile			
 	
### -field HRESULT(* )(IWDFIoTarget *This,IWDFIoRequest *pRequest,IWDFFile *pFile,IWDFMemory *pOutputMemory,PWDFMEMORY_OFFSET pOutputMemoryOffset,PLONGLONG DeviceOffset) FormatRequestForRead			
 	
### -field HRESULT(* )(IWDFIoTarget *This,IWDFIoRequest *pRequest,IWDFFile *pFile,IWDFMemory *pInputMemory,PWDFMEMORY_OFFSET pInputMemoryOffset,PLONGLONG DeviceOffset) FormatRequestForWrite			
 	
### -field HRESULT(* )(IWDFIoTarget *This,IWDFIoRequest *pRequest,ULONG IoctlCode,IWDFFile *pFile,IWDFMemory *pInputMemory,PWDFMEMORY_OFFSET pInputMemoryOffset,IWDFMemory *pOutputMemory,PWDFMEMORY_OFFSET pOutputMemoryOffset) FormatRequestForIoctl			
 	
## -remarks

## -see-also