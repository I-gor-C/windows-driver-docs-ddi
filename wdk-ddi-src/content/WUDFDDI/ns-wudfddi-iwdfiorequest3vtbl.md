---
UID: NS.wudfddi.IWDFIoRequest3Vtbl
title: IWDFIoRequest3Vtbl
author: windows-driver-content
description: 
ms.assetid: 60dae4d7-c75a-4ba3-bdde-0b03af8e7a40
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFIoRequest3Vtbl, IWDFIoRequest3Vtbl
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

# IWDFIoRequest3Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFIoRequest3 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFIoRequest3 *This) AddRef			
 	
### -field ULONG(* )(IWDFIoRequest3 *This) Release			
 	
### -field HRESULT(* )(IWDFIoRequest3 *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFIoRequest3 *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFIoRequest3 *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFIoRequest3 *This) AcquireLock			
 	
### -field void(* )(IWDFIoRequest3 *This) ReleaseLock			
 	
### -field void(* )(IWDFIoRequest3 *This,HRESULT CompletionStatus,SIZE_T Information) CompleteWithInformation			
 	
### -field void(* )(IWDFIoRequest3 *This,ULONG_PTR Information) SetInformation			
 	
### -field void(* )(IWDFIoRequest3 *This,HRESULT CompletionStatus) Complete			
 	
### -field void(* )(IWDFIoRequest3 *This,IRequestCallbackRequestCompletion *pCompletionCallback, void *pContext) SetCompletionCallback			
 	
### -field WDF_REQUEST_TYPE(* )(IWDFIoRequest3 *This) GetType			
 	
### -field void(* )(IWDFIoRequest3 *This,ULONG *pOptions,USHORT *pFileAttributes,USHORT *pShareAccess) GetCreateParameters			
 	
### -field void(* )(IWDFIoRequest3 *This,SIZE_T *pSizeInBytes,LONGLONG *pullOffset,ULONG *pulKey) GetReadParameters			
 	
### -field void(* )(IWDFIoRequest3 *This,SIZE_T *pSizeInBytes,LONGLONG *pullOffset,ULONG *pulKey) GetWriteParameters			
 	
### -field void(* )(IWDFIoRequest3 *This,ULONG *pControlCode,SIZE_T *pInBufferSize,SIZE_T *pOutBufferSize) GetDeviceIoControlParameters			
 	
### -field void(* )(IWDFIoRequest3 *This,IWDFMemory **ppWdfMemory) GetOutputMemory			
 	
### -field void(* )(IWDFIoRequest3 *This,IWDFMemory **ppWdfMemory) GetInputMemory			
 	
### -field void(* )(IWDFIoRequest3 *This,IRequestCallbackCancel *pCancelCallback) MarkCancelable			
 	
### -field HRESULT(* )(IWDFIoRequest3 *This) UnmarkCancelable			
 	
### -field BOOL(* )(IWDFIoRequest3 *This) CancelSentRequest			
 	
### -field HRESULT(* )(IWDFIoRequest3 *This,IWDFIoQueue *pDestination) ForwardToIoQueue			
 	
### -field HRESULT(* )(IWDFIoRequest3 *This,IWDFIoTarget *pIoTarget,ULONG Flags,LONGLONG Timeout) Send			
 	
### -field void(* )(IWDFIoRequest3 *This,IWDFFile **ppFileObject) GetFileObject			
 	
### -field void(* )(IWDFIoRequest3 *This) FormatUsingCurrentType			
 	
### -field ULONG(* )(IWDFIoRequest3 *This) GetRequestorProcessId			
 	
### -field void(* )(IWDFIoRequest3 *This,IWDFIoQueue **ppWdfIoQueue) GetIoQueue			
 	
### -field HRESULT(* )(IWDFIoRequest3 *This,SECURITY_IMPERSONATION_LEVEL ImpersonationLevel,IImpersonateCallback *pCallback, void *pvCallbackContext) Impersonate			
 	
### -field BOOL(* )(IWDFIoRequest3 *This) IsFrom32BitProcess			
 	
### -field void(* )(IWDFIoRequest3 *This,IWDFRequestCompletionParams **ppCompletionParams) GetCompletionParams			
 	
### -field void(* )(IWDFIoRequest3 *This,HRESULT hrNewStatus) Reuse			
 	
### -field WDF_KPROCESSOR_MODE(* )(IWDFIoRequest3 *This) GetRequestorMode			
 	
### -field BOOL(* )(IWDFIoRequest3 *This) IsFromUserModeDriver			
 	
### -field HRESULT(* )(IWDFIoRequest3 *This,SIZE_T MinimumRequiredCb,PVOID *Buffer,SIZE_T *BufferCb) RetrieveInputBuffer			
 	
### -field HRESULT(* )(IWDFIoRequest3 *This,SIZE_T MinimumRequiredCb,PVOID *Buffer,SIZE_T *BufferCb) RetrieveOutputBuffer			
 	
### -field HRESULT(* )(IWDFIoRequest3 *This,IWDFMemory **Memory) RetrieveInputMemory			
 	
### -field HRESULT(* )(IWDFIoRequest3 *This,IWDFMemory **Memory) RetrieveOutputMemory			
 	
### -field WDF_DEVICE_IO_TYPE(* )(IWDFIoRequest3 *This) GetEffectiveIoType			
 	
### -field void(* )(IWDFIoRequest3 *This,ULONG *pOptions,USHORT *pFileAttributes,USHORT *pShareAccess,ACCESS_MASK *pDesiredAccess) GetCreateParametersEx			
 	
### -field void(* )(IWDFIoRequest3 *This,WDF_FILE_INFORMATION_CLASS *pInformationClass,SIZE_T *pSizeInBytes) GetQueryInformationParameters			
 	
### -field void(* )(IWDFIoRequest3 *This,WDF_FILE_INFORMATION_CLASS *pInformationClass,SIZE_T *pSizeInBytes) GetSetInformationParameters			
 	
### -field BOOL(* )(IWDFIoRequest3 *This) IsCanceled			
 	
### -field HRESULT(* )(IWDFIoRequest3 *This) GetStatus			
 	
### -field void(* )(IWDFIoRequest3 *This,BOOL Requeue) StopAcknowledge			
 	
### -field HRESULT(* )(IWDFIoRequest3 *This) Requeue			
 	
### -field void(* )(IWDFIoRequest3 *This,BOOL IsUserModeDriverInitiated) SetUserModeDriverInitiatedIo			
 	
### -field BOOL(* )(IWDFIoRequest3 *This) GetUserModeDriverInitiatedIo			
 	
### -field HRESULT(* )(IWDFIoRequest3 *This,LPGUID ActivityId) RetrieveActivityId			
 	
### -field void(* )(IWDFIoRequest3 *This,LPGUID ActivityId) SetActivityId			
 	
## -remarks

## -see-also