---
UID: NS.wudfusb.IUsbTargetPipeContinuousReaderCallbackReadersFailedVtbl
title: IUsbTargetPipeContinuousReaderCallbackReadersFailedVtbl
author: windows-driver-content
description: 
ms.assetid: 54a5a083-57e5-4689-806f-418f5901c778
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IUsbTargetPipeContinuousReaderCallbackReadersFailedVtbl, IUsbTargetPipeContinuousReaderCallbackReadersFailedVtbl
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

# IUsbTargetPipeContinuousReaderCallbackReadersFailedVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IUsbTargetPipeContinuousReaderCallbackReadersFailed *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IUsbTargetPipeContinuousReaderCallbackReadersFailed *This) AddRef			
 	
### -field ULONG(* )(IUsbTargetPipeContinuousReaderCallbackReadersFailed *This) Release			
 	
### -field BOOL(* )(IUsbTargetPipeContinuousReaderCallbackReadersFailed *This,IWDFUsbTargetPipe *pPipe,HRESULT hrStatus) OnReaderFailure			
 	
## -remarks

## -see-also