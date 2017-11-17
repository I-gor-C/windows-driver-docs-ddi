---
UID: NS.wudfddi.IWDFIoRequest2Vtbl
title: IWDFIoRequest2Vtbl
author: windows-driver-content
description: 
ms.assetid: bf6d104a-3399-4bb8-aaa6-66c445e2ef72
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFIoRequest2Vtbl, IWDFIoRequest2Vtbl
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

# IWDFIoRequest2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFIoRequest2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFIoRequest2 *This) AddRef			
 	
### -field ULONG(* )(IWDFIoRequest2 *This) Release			
 	
### -field HRESULT(* )(IWDFIoRequest2 *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFIoRequest2 *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFIoRequest2 *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFIoRequest2 *This) AcquireLock			
 	
### -field void(* )(IWDFIoRequest2 *This) ReleaseLock			
 	
### -field void(* )(IWDFIoRequest2 *This,HRESULT CompletionStatus,SIZE_T Information) CompleteWithInformation			
 	
### -field void(* )(IWDFIoRequest2 *This,ULONG_PTR Information) SetInformation			
 	
### -field void(* )(IWDFIoRequest2 *This,HRESULT CompletionStatus) Complete			
 	
### -field void(* )(IWDFIoRequest2 *This,IRequestCallbackRequestCompletion *pCompletionCallback, void *pContext) SetCompletionCallback			
 	
### -field WDF_REQUEST_TYPE(* )(IWDFIoRequest2 *This) GetType			
 	
### -field void(* )(IWDFIoRequest2 *This,ULONG *pOptions,USHORT *pFileAttributes,USHORT *pShareAccess) GetCreateParameters			
 	
### -field void(* )(IWDFIoRequest2 *This,SIZE_T *pSizeInBytes,LONGLONG *pullOffset,ULONG *pulKey) GetReadParameters			
 	
### -field void(* )(IWDFIoRequest2 *This,SIZE_T *pSizeInBytes,LONGLONG *pullOffset,ULONG *pulKey) GetWriteParameters			
 	
### -field void(* )(IWDFIoRequest2 *This,ULONG *pControlCode,SIZE_T *pInBufferSize,SIZE_T *pOutBufferSize) GetDeviceIoControlParameters			
 	
### -field void(* )(IWDFIoRequest2 *This,IWDFMemory **ppWdfMemory) GetOutputMemory			
 	
### -field void(* )(IWDFIoRequest2 *This,IWDFMemory **ppWdfMemory) GetInputMemory			
 	
### -field void(* )(IWDFIoRequest2 *This,IRequestCallbackCancel *pCancelCallback) MarkCancelable			
 	
### -field HRESULT(* )(IWDFIoRequest2 *This) UnmarkCancelable			
 	
### -field BOOL(* )(IWDFIoRequest2 *This) CancelSentRequest			
 	
### -field HRESULT(* )(IWDFIoRequest2 *This,IWDFIoQueue *pDestination) ForwardToIoQueue			
 	
### -field HRESULT(* )(IWDFIoRequest2 *This,IWDFIoTarget *pIoTarget,ULONG Flags,LONGLONG Timeout) Send			
 	
### -field void(* )(IWDFIoRequest2 *This,IWDFFile **ppFileObject) GetFileObject			
 	
### -field void(* )(IWDFIoRequest2 *This) FormatUsingCurrentType			
 	
### -field ULONG(* )(IWDFIoRequest2 *This) GetRequestorProcessId			
 	
### -field void(* )(IWDFIoRequest2 *This,IWDFIoQueue **ppWdfIoQueue) GetIoQueue			
 	
### -field HRESULT(* )(IWDFIoRequest2 *This,SECURITY_IMPERSONATION_LEVEL ImpersonationLevel,IImpersonateCallback *pCallback, void *pvCallbackContext) Impersonate			
 	
### -field BOOL(* )(IWDFIoRequest2 *This) IsFrom32BitProcess			
 	
### -field void(* )(IWDFIoRequest2 *This,IWDFRequestCompletionParams **ppCompletionParams) GetCompletionParams			
 	
### -field void(* )(IWDFIoRequest2 *This,HRESULT hrNewStatus) Reuse			
 	
### -field WDF_KPROCESSOR_MODE(* )(IWDFIoRequest2 *This) GetRequestorMode			
 	
### -field BOOL(* )(IWDFIoRequest2 *This) IsFromUserModeDriver			
 	
### -field HRESULT(* )(IWDFIoRequest2 *This,SIZE_T MinimumRequiredCb,PVOID *Buffer,SIZE_T *BufferCb) RetrieveInputBuffer			
 	
### -field HRESULT(* )(IWDFIoRequest2 *This,SIZE_T MinimumRequiredCb,PVOID *Buffer,SIZE_T *BufferCb) RetrieveOutputBuffer			
 	
### -field HRESULT(* )(IWDFIoRequest2 *This,IWDFMemory **Memory) RetrieveInputMemory			
 	
### -field HRESULT(* )(IWDFIoRequest2 *This,IWDFMemory **Memory) RetrieveOutputMemory			
 	
### -field WDF_DEVICE_IO_TYPE(* )(IWDFIoRequest2 *This) GetEffectiveIoType			
 	
### -field void(* )(IWDFIoRequest2 *This,ULONG *pOptions,USHORT *pFileAttributes,USHORT *pShareAccess,ACCESS_MASK *pDesiredAccess) GetCreateParametersEx			
 	
### -field void(* )(IWDFIoRequest2 *This,WDF_FILE_INFORMATION_CLASS *pInformationClass,SIZE_T *pSizeInBytes) GetQueryInformationParameters			
 	
### -field void(* )(IWDFIoRequest2 *This,WDF_FILE_INFORMATION_CLASS *pInformationClass,SIZE_T *pSizeInBytes) GetSetInformationParameters			
 	
### -field BOOL(* )(IWDFIoRequest2 *This) IsCanceled			
 	
### -field HRESULT(* )(IWDFIoRequest2 *This) GetStatus			
 	
### -field void(* )(IWDFIoRequest2 *This,BOOL Requeue) StopAcknowledge			
 	
### -field HRESULT(* )(IWDFIoRequest2 *This) Requeue			
 	
## -remarks

## -see-also