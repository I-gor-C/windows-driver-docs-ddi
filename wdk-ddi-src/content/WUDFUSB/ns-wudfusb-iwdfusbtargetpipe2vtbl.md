---
UID: NS.wudfusb.IWDFUsbTargetPipe2Vtbl
title: IWDFUsbTargetPipe2Vtbl
author: windows-driver-content
description: 
ms.assetid: f6991edf-072d-4c34-871a-39e6ad7e3b86
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFUsbTargetPipe2Vtbl, IWDFUsbTargetPipe2Vtbl
req.header: wudfusb.h
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

# IWDFUsbTargetPipe2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFUsbTargetPipe2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFUsbTargetPipe2 *This) AddRef			
 	
### -field ULONG(* )(IWDFUsbTargetPipe2 *This) Release			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe2 *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe2 *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe2 *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFUsbTargetPipe2 *This) AcquireLock			
 	
### -field void(* )(IWDFUsbTargetPipe2 *This) ReleaseLock			
 	
### -field void(* )(IWDFUsbTargetPipe2 *This,IWDFFile **ppWdfFile) GetTargetFile			
 	
### -field void(* )(IWDFUsbTargetPipe2 *This,IWDFFile *pFile) CancelSentRequestsForFile			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe2 *This,IWDFIoRequest *pRequest,IWDFFile *pFile,IWDFMemory *pOutputMemory,PWDFMEMORY_OFFSET pOutputMemoryOffset,PLONGLONG DeviceOffset) FormatRequestForRead			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe2 *This,IWDFIoRequest *pRequest,IWDFFile *pFile,IWDFMemory *pInputMemory,PWDFMEMORY_OFFSET pInputMemoryOffset,PLONGLONG DeviceOffset) FormatRequestForWrite			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe2 *This,IWDFIoRequest *pRequest,ULONG IoctlCode,IWDFFile *pFile,IWDFMemory *pInputMemory,PWDFMEMORY_OFFSET pInputMemoryOffset,IWDFMemory *pOutputMemory,PWDFMEMORY_OFFSET pOutputMemoryOffset) FormatRequestForIoctl			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe2 *This) Abort			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe2 *This) Reset			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe2 *This) Flush			
 	
### -field void(* )(IWDFUsbTargetPipe2 *This,PWINUSB_PIPE_INFORMATION pInfo) GetInformation			
 	
### -field BOOL(* )(IWDFUsbTargetPipe2 *This) IsInEndPoint			
 	
### -field BOOL(* )(IWDFUsbTargetPipe2 *This) IsOutEndPoint			
 	
### -field USBD_PIPE_TYPE(* )(IWDFUsbTargetPipe2 *This) GetType			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe2 *This,ULONG PolicyType,ULONG *ValueLength,PVOID Value) RetrievePipePolicy			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe2 *This,ULONG PolicyType,ULONG ValueLength,PVOID Value) SetPipePolicy			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe2 *This,SIZE_T TransferLength,SIZE_T HeaderLength,SIZE_T TrailerLength,UCHAR NumPendingReads,IUnknown *pMemoryCleanupCallbackInterface,IUsbTargetPipeContinuousReaderCallbackReadComplete *pOnCompletion,PVOID pCompletionContext,IUsbTargetPipeContinuousReaderCallbackReadersFailed *pOnFailure) ConfigureContinuousReader			
 	
## -remarks

## -see-also