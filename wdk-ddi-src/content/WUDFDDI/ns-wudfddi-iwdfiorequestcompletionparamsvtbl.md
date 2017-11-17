---
UID: NS.wudfddi.IWDFIoRequestCompletionParamsVtbl
title: IWDFIoRequestCompletionParamsVtbl
author: windows-driver-content
description: 
ms.assetid: 946b15a0-87f8-470a-9f6c-332f4465bf9e
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFIoRequestCompletionParamsVtbl, IWDFIoRequestCompletionParamsVtbl
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

# IWDFIoRequestCompletionParamsVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFIoRequestCompletionParams *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFIoRequestCompletionParams *This) AddRef			
 	
### -field ULONG(* )(IWDFIoRequestCompletionParams *This) Release			
 	
### -field HRESULT(* )(IWDFIoRequestCompletionParams *This) GetCompletionStatus			
 	
### -field ULONG_PTR(* )(IWDFIoRequestCompletionParams *This) GetInformation			
 	
### -field WDF_REQUEST_TYPE(* )(IWDFIoRequestCompletionParams *This) GetCompletedRequestType			
 	
### -field void(* )(IWDFIoRequestCompletionParams *This,IWDFMemory **ppWriteMemory,SIZE_T *pBytesWritten,SIZE_T *pWriteMemoryOffset) GetWriteParameters			
 	
### -field void(* )(IWDFIoRequestCompletionParams *This,IWDFMemory **ppReadMemory,SIZE_T *pBytesRead,SIZE_T *pReadMemoryOffset) GetReadParameters			
 	
### -field void(* )(IWDFIoRequestCompletionParams *This,ULONG *pIoControlCode,IWDFMemory **ppInputMemory,SIZE_T *pInputMemoryOffset,IWDFMemory **ppOutputMemory,SIZE_T *pOutputMemoryOffset,SIZE_T *pOutBytes) GetIoctlParameters			
 	
## -remarks

## -see-also