---
UID: NS.mfidl.IMFRealTimeClientExVtbl
title: IMFRealTimeClientExVtbl
author: windows-driver-content
description: 
ms.assetid: fdab4fa7-5c27-4940-b351-31d6ab2d1de9
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFRealTimeClientExVtbl, IMFRealTimeClientExVtbl
req.header: mfidl.h
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

# IMFRealTimeClientExVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFRealTimeClientEx *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFRealTimeClientEx *This) AddRef			
 	
### -field ULONG(* )(IMFRealTimeClientEx *This) Release			
 	
### -field HRESULT(* )(IMFRealTimeClientEx *This,DWORD *pdwTaskIndex,LPCWSTR wszClassName,LONG lBasePriority) RegisterThreadsEx			
 	
### -field HRESULT(* )(IMFRealTimeClientEx *This) UnregisterThreads			
 	
### -field HRESULT(* )(IMFRealTimeClientEx *This,DWORD dwMultithreadedWorkQueueId,LONG lWorkItemBasePriority) SetWorkQueueEx			
 	
## -remarks

## -see-also