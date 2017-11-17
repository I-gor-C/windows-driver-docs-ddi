---
UID: NS.wudfddi.IQueueCallbackDeviceIoControlVtbl
title: IQueueCallbackDeviceIoControlVtbl
author: windows-driver-content
description: 
ms.assetid: 6a39df2e-0344-41e4-81f3-90dd8c7c39b7
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IQueueCallbackDeviceIoControlVtbl, IQueueCallbackDeviceIoControlVtbl
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

# IQueueCallbackDeviceIoControlVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IQueueCallbackDeviceIoControl *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IQueueCallbackDeviceIoControl *This) AddRef			
 	
### -field ULONG(* )(IQueueCallbackDeviceIoControl *This) Release			
 	
### -field void(* )(IQueueCallbackDeviceIoControl *This,IWDFIoQueue *pWdfQueue,IWDFIoRequest *pWdfRequest,ULONG ControlCode,SIZE_T InputBufferSizeInBytes,SIZE_T OutputBufferSizeInBytes) OnDeviceIoControl			
 	
## -remarks

## -see-also