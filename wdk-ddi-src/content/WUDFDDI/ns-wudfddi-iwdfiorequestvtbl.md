---
UID: NS.wudfddi.IWDFIoRequestVtbl
title: IWDFIoRequestVtbl
author: windows-driver-content
description: 
ms.assetid: 918ddb5a-e348-4538-9770-93131e6a485b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFIoRequestVtbl, IWDFIoRequestVtbl
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

# IWDFIoRequestVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFIoRequest *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFIoRequest *This) AddRef			
 	
### -field ULONG(* )(IWDFIoRequest *This) Release			
 	
### -field HRESULT(* )(IWDFIoRequest *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFIoRequest *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFIoRequest *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFIoRequest *This) AcquireLock			
 	
### -field void(* )(IWDFIoRequest *This) ReleaseLock			
 	
### -field void(* )(IWDFIoRequest *This,HRESULT CompletionStatus,SIZE_T Information) CompleteWithInformation			
 	
### -field void(* )(IWDFIoRequest *This,ULONG_PTR Information) SetInformation			
 	
### -field void(* )(IWDFIoRequest *This,HRESULT CompletionStatus) Complete			
 	
### -field void(* )(IWDFIoRequest *This,IRequestCallbackRequestCompletion *pCompletionCallback, void *pContext) SetCompletionCallback			
 	
### -field WDF_REQUEST_TYPE(* )(IWDFIoRequest *This) GetType			
 	
### -field void(* )(IWDFIoRequest *This,ULONG *pOptions,USHORT *pFileAttributes,USHORT *pShareAccess) GetCreateParameters			
 	
### -field void(* )(IWDFIoRequest *This,SIZE_T *pSizeInBytes,LONGLONG *pullOffset,ULONG *pulKey) GetReadParameters			
 	
### -field void(* )(IWDFIoRequest *This,SIZE_T *pSizeInBytes,LONGLONG *pullOffset,ULONG *pulKey) GetWriteParameters			
 	
### -field void(* )(IWDFIoRequest *This,ULONG *pControlCode,SIZE_T *pInBufferSize,SIZE_T *pOutBufferSize) GetDeviceIoControlParameters			
 	
### -field void(* )(IWDFIoRequest *This,IWDFMemory **ppWdfMemory) GetOutputMemory			
 	
### -field void(* )(IWDFIoRequest *This,IWDFMemory **ppWdfMemory) GetInputMemory			
 	
### -field void(* )(IWDFIoRequest *This,IRequestCallbackCancel *pCancelCallback) MarkCancelable			
 	
### -field HRESULT(* )(IWDFIoRequest *This) UnmarkCancelable			
 	
### -field BOOL(* )(IWDFIoRequest *This) CancelSentRequest			
 	
### -field HRESULT(* )(IWDFIoRequest *This,IWDFIoQueue *pDestination) ForwardToIoQueue			
 	
### -field HRESULT(* )(IWDFIoRequest *This,IWDFIoTarget *pIoTarget,ULONG Flags,LONGLONG Timeout) Send			
 	
### -field void(* )(IWDFIoRequest *This,IWDFFile **ppFileObject) GetFileObject			
 	
### -field void(* )(IWDFIoRequest *This) FormatUsingCurrentType			
 	
### -field ULONG(* )(IWDFIoRequest *This) GetRequestorProcessId			
 	
### -field void(* )(IWDFIoRequest *This,IWDFIoQueue **ppWdfIoQueue) GetIoQueue			
 	
### -field HRESULT(* )(IWDFIoRequest *This,SECURITY_IMPERSONATION_LEVEL ImpersonationLevel,IImpersonateCallback *pCallback, void *pvCallbackContext) Impersonate			
 	
### -field BOOL(* )(IWDFIoRequest *This) IsFrom32BitProcess			
 	
### -field void(* )(IWDFIoRequest *This,IWDFRequestCompletionParams **ppCompletionParams) GetCompletionParams			
 	
## -remarks

## -see-also