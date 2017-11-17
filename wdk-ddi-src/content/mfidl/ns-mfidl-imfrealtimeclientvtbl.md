---
UID: NS.mfidl.IMFRealTimeClientVtbl
title: IMFRealTimeClientVtbl
author: windows-driver-content
description: 
ms.assetid: 40c5328b-a2b6-485d-ba52-70766eaeb943
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFRealTimeClientVtbl, IMFRealTimeClientVtbl
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

# IMFRealTimeClientVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFRealTimeClient *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFRealTimeClient *This) AddRef			
 	
### -field ULONG(* )(IMFRealTimeClient *This) Release			
 	
### -field HRESULT(* )(IMFRealTimeClient *This,DWORD dwTaskIndex,LPCWSTR wszClass) RegisterThreads			
 	
### -field HRESULT(* )(IMFRealTimeClient *This) UnregisterThreads			
 	
### -field HRESULT(* )(IMFRealTimeClient *This,DWORD dwWorkQueueId) SetWorkQueue			
 	
## -remarks

## -see-also