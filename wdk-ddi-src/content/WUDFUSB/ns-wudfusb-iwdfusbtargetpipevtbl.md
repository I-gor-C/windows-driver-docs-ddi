---
UID: NS.wudfusb.IWDFUsbTargetPipeVtbl
title: IWDFUsbTargetPipeVtbl
author: windows-driver-content
description: 
ms.assetid: 6d520db6-c210-4876-bc04-ac833fb42a78
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFUsbTargetPipeVtbl, IWDFUsbTargetPipeVtbl
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

# IWDFUsbTargetPipeVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFUsbTargetPipe *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFUsbTargetPipe *This) AddRef			
 	
### -field ULONG(* )(IWDFUsbTargetPipe *This) Release			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFUsbTargetPipe *This) AcquireLock			
 	
### -field void(* )(IWDFUsbTargetPipe *This) ReleaseLock			
 	
### -field void(* )(IWDFUsbTargetPipe *This,IWDFFile **ppWdfFile) GetTargetFile			
 	
### -field void(* )(IWDFUsbTargetPipe *This,IWDFFile *pFile) CancelSentRequestsForFile			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe *This,IWDFIoRequest *pRequest,IWDFFile *pFile,IWDFMemory *pOutputMemory,PWDFMEMORY_OFFSET pOutputMemoryOffset,PLONGLONG DeviceOffset) FormatRequestForRead			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe *This,IWDFIoRequest *pRequest,IWDFFile *pFile,IWDFMemory *pInputMemory,PWDFMEMORY_OFFSET pInputMemoryOffset,PLONGLONG DeviceOffset) FormatRequestForWrite			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe *This,IWDFIoRequest *pRequest,ULONG IoctlCode,IWDFFile *pFile,IWDFMemory *pInputMemory,PWDFMEMORY_OFFSET pInputMemoryOffset,IWDFMemory *pOutputMemory,PWDFMEMORY_OFFSET pOutputMemoryOffset) FormatRequestForIoctl			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe *This) Abort			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe *This) Reset			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe *This) Flush			
 	
### -field void(* )(IWDFUsbTargetPipe *This,PWINUSB_PIPE_INFORMATION pInfo) GetInformation			
 	
### -field BOOL(* )(IWDFUsbTargetPipe *This) IsInEndPoint			
 	
### -field BOOL(* )(IWDFUsbTargetPipe *This) IsOutEndPoint			
 	
### -field USBD_PIPE_TYPE(* )(IWDFUsbTargetPipe *This) GetType			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe *This,ULONG PolicyType,ULONG *ValueLength,PVOID Value) RetrievePipePolicy			
 	
### -field HRESULT(* )(IWDFUsbTargetPipe *This,ULONG PolicyType,ULONG ValueLength,PVOID Value) SetPipePolicy			
 	
## -remarks

## -see-also