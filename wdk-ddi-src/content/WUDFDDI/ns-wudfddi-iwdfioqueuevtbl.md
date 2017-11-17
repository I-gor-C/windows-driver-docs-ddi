---
UID: NS.wudfddi.IWDFIoQueueVtbl
title: IWDFIoQueueVtbl
author: windows-driver-content
description: 
ms.assetid: 0df32ca7-a3df-45f6-86f3-1581b8211242
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFIoQueueVtbl, IWDFIoQueueVtbl
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

# IWDFIoQueueVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFIoQueue *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFIoQueue *This) AddRef			
 	
### -field ULONG(* )(IWDFIoQueue *This) Release			
 	
### -field HRESULT(* )(IWDFIoQueue *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFIoQueue *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFIoQueue *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFIoQueue *This) AcquireLock			
 	
### -field void(* )(IWDFIoQueue *This) ReleaseLock			
 	
### -field void(* )(IWDFIoQueue *This,IWDFDevice **ppWdfDevice) GetDevice			
 	
### -field HRESULT(* )(IWDFIoQueue *This,WDF_REQUEST_TYPE RequestType,BOOL Forward) ConfigureRequestDispatching			
 	
### -field WDF_IO_QUEUE_STATE(* )(IWDFIoQueue *This,ULONG *pulNumOfRequestsInQueue,ULONG *pulNumOfRequestsInDriver) GetState			
 	
### -field HRESULT(* )(IWDFIoQueue *This,IWDFIoRequest **ppRequest) RetrieveNextRequest			
 	
### -field HRESULT(* )(IWDFIoQueue *This,IWDFFile *pFile,IWDFIoRequest **ppRequest) RetrieveNextRequestByFileObject			
 	
### -field void(* )(IWDFIoQueue *This) Start			
 	
### -field void(* )(IWDFIoQueue *This,IQueueCallbackStateChange *pStopComplete) Stop			
 	
### -field void(* )(IWDFIoQueue *This) StopSynchronously			
 	
### -field void(* )(IWDFIoQueue *This,IQueueCallbackStateChange *pDrainComplete) Drain			
 	
### -field void(* )(IWDFIoQueue *This) DrainSynchronously			
 	
### -field void(* )(IWDFIoQueue *This,IQueueCallbackStateChange *pPurgeComplete) Purge			
 	
### -field void(* )(IWDFIoQueue *This) PurgeSynchronously			
 	
## -remarks

## -see-also