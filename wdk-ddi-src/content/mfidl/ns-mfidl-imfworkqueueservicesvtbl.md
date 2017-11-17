---
UID: NS.mfidl.IMFWorkQueueServicesVtbl
title: IMFWorkQueueServicesVtbl
author: windows-driver-content
description: 
ms.assetid: 9b54bd64-bd34-4bda-8ec5-5bcf31c20081
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFWorkQueueServicesVtbl, IMFWorkQueueServicesVtbl
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

# IMFWorkQueueServicesVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFWorkQueueServices *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFWorkQueueServices *This) AddRef			
 	
### -field ULONG(* )(IMFWorkQueueServices *This) Release			
 	
### -field HRESULT(* )(IMFWorkQueueServices *This,IMFAsyncCallback *pCallback,IUnknown *pState) BeginRegisterTopologyWorkQueuesWithMMCSS			
 	
### -field HRESULT(* )(IMFWorkQueueServices *This,IMFAsyncResult *pResult) EndRegisterTopologyWorkQueuesWithMMCSS			
 	
### -field HRESULT(* )(IMFWorkQueueServices *This,IMFAsyncCallback *pCallback,IUnknown *pState) BeginUnregisterTopologyWorkQueuesWithMMCSS			
 	
### -field HRESULT(* )(IMFWorkQueueServices *This,IMFAsyncResult *pResult) EndUnregisterTopologyWorkQueuesWithMMCSS			
 	
### -field HRESULT(* )(IMFWorkQueueServices *This,DWORD dwTopologyWorkQueueId,LPWSTR pwszClass,DWORD *pcchClass) GetTopologyWorkQueueMMCSSClass			
 	
### -field HRESULT(* )(IMFWorkQueueServices *This,DWORD dwTopologyWorkQueueId,DWORD *pdwTaskId) GetTopologyWorkQueueMMCSSTaskId			
 	
### -field HRESULT(* )(IMFWorkQueueServices *This,DWORD dwPlatformWorkQueue,LPCWSTR wszClass,DWORD dwTaskId,IMFAsyncCallback *pCallback,IUnknown *pState) BeginRegisterPlatformWorkQueueWithMMCSS			
 	
### -field HRESULT(* )(IMFWorkQueueServices *This,IMFAsyncResult *pResult,DWORD *pdwTaskId) EndRegisterPlatformWorkQueueWithMMCSS			
 	
### -field HRESULT(* )(IMFWorkQueueServices *This,DWORD dwPlatformWorkQueue,IMFAsyncCallback *pCallback,IUnknown *pState) BeginUnregisterPlatformWorkQueueWithMMCSS			
 	
### -field HRESULT(* )(IMFWorkQueueServices *This,IMFAsyncResult *pResult) EndUnregisterPlatformWorkQueueWithMMCSS			
 	
### -field HRESULT(* )(IMFWorkQueueServices *This,DWORD dwPlatformWorkQueueId,LPWSTR pwszClass,DWORD *pcchClass) GetPlaftormWorkQueueMMCSSClass			
 	
### -field HRESULT(* )(IMFWorkQueueServices *This,DWORD dwPlatformWorkQueueId,DWORD *pdwTaskId) GetPlatformWorkQueueMMCSSTaskId			
 	
## -remarks

## -see-also