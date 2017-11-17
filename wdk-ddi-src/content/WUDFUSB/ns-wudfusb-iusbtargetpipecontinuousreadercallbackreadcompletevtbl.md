---
UID: NS.wudfusb.IUsbTargetPipeContinuousReaderCallbackReadCompleteVtbl
title: IUsbTargetPipeContinuousReaderCallbackReadCompleteVtbl
author: windows-driver-content
description: 
ms.assetid: b8190c40-89cc-4f96-8cd6-ae3e4c97a0c3
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IUsbTargetPipeContinuousReaderCallbackReadCompleteVtbl, IUsbTargetPipeContinuousReaderCallbackReadCompleteVtbl
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

# IUsbTargetPipeContinuousReaderCallbackReadCompleteVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IUsbTargetPipeContinuousReaderCallbackReadComplete *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IUsbTargetPipeContinuousReaderCallbackReadComplete *This) AddRef			
 	
### -field ULONG(* )(IUsbTargetPipeContinuousReaderCallbackReadComplete *This) Release			
 	
### -field void(* )(IUsbTargetPipeContinuousReaderCallbackReadComplete *This,IWDFUsbTargetPipe *pPipe,IWDFMemory *pMemory,SIZE_T NumBytesTransferred,PVOID Context) OnReaderCompletion			
 	
## -remarks

## -see-also