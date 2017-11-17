---
UID: NS.wudfddi.IWDFIoTarget2Vtbl
title: IWDFIoTarget2Vtbl
author: windows-driver-content
description: 
ms.assetid: 9b11f66e-98c1-40ac-b4f7-439a4c5f2fe0
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFIoTarget2Vtbl, IWDFIoTarget2Vtbl
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

# IWDFIoTarget2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFIoTarget2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFIoTarget2 *This) AddRef			
 	
### -field ULONG(* )(IWDFIoTarget2 *This) Release			
 	
### -field HRESULT(* )(IWDFIoTarget2 *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFIoTarget2 *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFIoTarget2 *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFIoTarget2 *This) AcquireLock			
 	
### -field void(* )(IWDFIoTarget2 *This) ReleaseLock			
 	
### -field void(* )(IWDFIoTarget2 *This,IWDFFile **ppWdfFile) GetTargetFile			
 	
### -field void(* )(IWDFIoTarget2 *This,IWDFFile *pFile) CancelSentRequestsForFile			
 	
### -field HRESULT(* )(IWDFIoTarget2 *This,IWDFIoRequest *pRequest,IWDFFile *pFile,IWDFMemory *pOutputMemory,PWDFMEMORY_OFFSET pOutputMemoryOffset,PLONGLONG DeviceOffset) FormatRequestForRead			
 	
### -field HRESULT(* )(IWDFIoTarget2 *This,IWDFIoRequest *pRequest,IWDFFile *pFile,IWDFMemory *pInputMemory,PWDFMEMORY_OFFSET pInputMemoryOffset,PLONGLONG DeviceOffset) FormatRequestForWrite			
 	
### -field HRESULT(* )(IWDFIoTarget2 *This,IWDFIoRequest *pRequest,ULONG IoctlCode,IWDFFile *pFile,IWDFMemory *pInputMemory,PWDFMEMORY_OFFSET pInputMemoryOffset,IWDFMemory *pOutputMemory,PWDFMEMORY_OFFSET pOutputMemoryOffset) FormatRequestForIoctl			
 	
### -field HRESULT(* )(IWDFIoTarget2 *This,IWDFIoRequest *pRequest,IWDFFile *pFile) FormatRequestForFlush			
 	
### -field HRESULT(* )(IWDFIoTarget2 *This,IWDFIoRequest *pRequest,WDF_FILE_INFORMATION_CLASS InformationClass,IWDFFile *pFile,IWDFMemory *pInformationMemory,PWDFMEMORY_OFFSET pInformationMemoryOffset) FormatRequestForSetInformation			
 	
### -field HRESULT(* )(IWDFIoTarget2 *This,IWDFIoRequest *pRequest,WDF_FILE_INFORMATION_CLASS InformationClass,IWDFFile *pFile,IWDFMemory *pInformationMemory,PWDFMEMORY_OFFSET pInformationMemoryOffset) FormatRequestForQueryInformation			
 	
## -remarks

## -see-also