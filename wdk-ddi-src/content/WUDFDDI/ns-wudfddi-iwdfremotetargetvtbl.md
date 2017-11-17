---
UID: NS.wudfddi.IWDFRemoteTargetVtbl
title: IWDFRemoteTargetVtbl
author: windows-driver-content
description: 
ms.assetid: 8287c573-db2c-4b70-972c-db113b33bbb1
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFRemoteTargetVtbl, IWDFRemoteTargetVtbl
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

# IWDFRemoteTargetVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFRemoteTarget *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFRemoteTarget *This) AddRef			
 	
### -field ULONG(* )(IWDFRemoteTarget *This) Release			
 	
### -field HRESULT(* )(IWDFRemoteTarget *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFRemoteTarget *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFRemoteTarget *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFRemoteTarget *This) AcquireLock			
 	
### -field void(* )(IWDFRemoteTarget *This) ReleaseLock			
 	
### -field void(* )(IWDFRemoteTarget *This,IWDFFile **ppWdfFile) GetTargetFile			
 	
### -field void(* )(IWDFRemoteTarget *This,IWDFFile *pFile) CancelSentRequestsForFile			
 	
### -field HRESULT(* )(IWDFRemoteTarget *This,IWDFIoRequest *pRequest,IWDFFile *pFile,IWDFMemory *pOutputMemory,PWDFMEMORY_OFFSET pOutputMemoryOffset,PLONGLONG DeviceOffset) FormatRequestForRead			
 	
### -field HRESULT(* )(IWDFRemoteTarget *This,IWDFIoRequest *pRequest,IWDFFile *pFile,IWDFMemory *pInputMemory,PWDFMEMORY_OFFSET pInputMemoryOffset,PLONGLONG DeviceOffset) FormatRequestForWrite			
 	
### -field HRESULT(* )(IWDFRemoteTarget *This,IWDFIoRequest *pRequest,ULONG IoctlCode,IWDFFile *pFile,IWDFMemory *pInputMemory,PWDFMEMORY_OFFSET pInputMemoryOffset,IWDFMemory *pOutputMemory,PWDFMEMORY_OFFSET pOutputMemoryOffset) FormatRequestForIoctl			
 	
### -field HRESULT(* )(IWDFRemoteTarget *This,IWDFIoRequest *pRequest,IWDFFile *pFile) FormatRequestForFlush			
 	
### -field HRESULT(* )(IWDFRemoteTarget *This,IWDFIoRequest *pRequest,WDF_FILE_INFORMATION_CLASS InformationClass,IWDFFile *pFile,IWDFMemory *pInformationMemory,PWDFMEMORY_OFFSET pInformationMemoryOffset) FormatRequestForSetInformation			
 	
### -field HRESULT(* )(IWDFRemoteTarget *This,IWDFIoRequest *pRequest,WDF_FILE_INFORMATION_CLASS InformationClass,IWDFFile *pFile,IWDFMemory *pInformationMemory,PWDFMEMORY_OFFSET pInformationMemoryOffset) FormatRequestForQueryInformation			
 	
### -field HRESULT(* )(IWDFRemoteTarget *This,IWDFRemoteInterface *pRemoteInterface,PCWSTR pszRelativeFileName,DWORD DesiredAccess,PUMDF_IO_TARGET_OPEN_PARAMS pOpenParams) OpenRemoteInterface			
 	
### -field HRESULT(* )(IWDFRemoteTarget *This,PCWSTR pszFileName,DWORD DesiredAccess,PUMDF_IO_TARGET_OPEN_PARAMS pOpenParams) OpenFileByName			
 	
### -field HRESULT(* )(IWDFRemoteTarget *This) Close			
 	
### -field HRESULT(* )(IWDFRemoteTarget *This) CloseForQueryRemove			
 	
### -field HRESULT(* )(IWDFRemoteTarget *This) Reopen			
 	
### -field WDF_IO_TARGET_STATE(* )(IWDFRemoteTarget *This) GetState			
 	
### -field HRESULT(* )(IWDFRemoteTarget *This) Start			
 	
### -field HRESULT(* )(IWDFRemoteTarget *This,WDF_IO_TARGET_SENT_IO_ACTION Action) Stop			
 	
## -remarks

## -see-also