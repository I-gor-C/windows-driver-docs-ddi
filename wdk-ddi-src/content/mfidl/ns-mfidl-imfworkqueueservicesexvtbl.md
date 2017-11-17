---
UID: NS.mfidl.IMFWorkQueueServicesExVtbl
title: IMFWorkQueueServicesExVtbl
author: windows-driver-content
description: 
ms.assetid: 50ddae76-a1c9-40fe-8aba-0f8176141e60
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFWorkQueueServicesExVtbl, IMFWorkQueueServicesExVtbl
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

# IMFWorkQueueServicesExVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFWorkQueueServicesEx *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFWorkQueueServicesEx *This) AddRef			
 	
### -field ULONG(* )(IMFWorkQueueServicesEx *This) Release			
 	
### -field HRESULT(* )(IMFWorkQueueServicesEx *This,IMFAsyncCallback *pCallback,IUnknown *pState) BeginRegisterTopologyWorkQueuesWithMMCSS			
 	
### -field HRESULT(* )(IMFWorkQueueServicesEx *This,IMFAsyncResult *pResult) EndRegisterTopologyWorkQueuesWithMMCSS			
 	
### -field HRESULT(* )(IMFWorkQueueServicesEx *This,IMFAsyncCallback *pCallback,IUnknown *pState) BeginUnregisterTopologyWorkQueuesWithMMCSS			
 	
### -field HRESULT(* )(IMFWorkQueueServicesEx *This,IMFAsyncResult *pResult) EndUnregisterTopologyWorkQueuesWithMMCSS			
 	
### -field HRESULT(* )(IMFWorkQueueServicesEx *This,DWORD dwTopologyWorkQueueId,LPWSTR pwszClass,DWORD *pcchClass) GetTopologyWorkQueueMMCSSClass			
 	
### -field HRESULT(* )(IMFWorkQueueServicesEx *This,DWORD dwTopologyWorkQueueId,DWORD *pdwTaskId) GetTopologyWorkQueueMMCSSTaskId			
 	
### -field HRESULT(* )(IMFWorkQueueServicesEx *This,DWORD dwPlatformWorkQueue,LPCWSTR wszClass,DWORD dwTaskId,IMFAsyncCallback *pCallback,IUnknown *pState) BeginRegisterPlatformWorkQueueWithMMCSS			
 	
### -field HRESULT(* )(IMFWorkQueueServicesEx *This,IMFAsyncResult *pResult,DWORD *pdwTaskId) EndRegisterPlatformWorkQueueWithMMCSS			
 	
### -field HRESULT(* )(IMFWorkQueueServicesEx *This,DWORD dwPlatformWorkQueue,IMFAsyncCallback *pCallback,IUnknown *pState) BeginUnregisterPlatformWorkQueueWithMMCSS			
 	
### -field HRESULT(* )(IMFWorkQueueServicesEx *This,IMFAsyncResult *pResult) EndUnregisterPlatformWorkQueueWithMMCSS			
 	
### -field HRESULT(* )(IMFWorkQueueServicesEx *This,DWORD dwPlatformWorkQueueId,LPWSTR pwszClass,DWORD *pcchClass) GetPlaftormWorkQueueMMCSSClass			
 	
### -field HRESULT(* )(IMFWorkQueueServicesEx *This,DWORD dwPlatformWorkQueueId,DWORD *pdwTaskId) GetPlatformWorkQueueMMCSSTaskId			
 	
### -field HRESULT(* )(IMFWorkQueueServicesEx *This,DWORD dwTopologyWorkQueueId,LONG *plPriority) GetTopologyWorkQueueMMCSSPriority			
 	
### -field HRESULT(* )(IMFWorkQueueServicesEx *This,DWORD dwPlatformWorkQueue,LPCWSTR wszClass,DWORD dwTaskId,LONG lPriority,IMFAsyncCallback *pCallback,IUnknown *pState) BeginRegisterPlatformWorkQueueWithMMCSSEx			
 	
### -field HRESULT(* )(IMFWorkQueueServicesEx *This,DWORD dwPlatformWorkQueueId,LONG *plPriority) GetPlatformWorkQueueMMCSSPriority			
 	
## -remarks

## -see-also