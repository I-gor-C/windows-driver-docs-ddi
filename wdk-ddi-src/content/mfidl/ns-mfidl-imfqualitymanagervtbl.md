---
UID: NS.mfidl.IMFQualityManagerVtbl
title: IMFQualityManagerVtbl
author: windows-driver-content
description: 
ms.assetid: 1a1cbaa7-c3f0-4479-a0da-c3802054b87b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFQualityManagerVtbl, IMFQualityManagerVtbl
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

# IMFQualityManagerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFQualityManager *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFQualityManager *This) AddRef			
 	
### -field ULONG(* )(IMFQualityManager *This) Release			
 	
### -field HRESULT(* )(IMFQualityManager *This,IMFTopology *pTopology) NotifyTopology			
 	
### -field HRESULT(* )(IMFQualityManager *This,IMFPresentationClock *pClock) NotifyPresentationClock			
 	
### -field HRESULT(* )(IMFQualityManager *This,IMFTopologyNode *pNode, long lInputIndex,IMFSample *pSample) NotifyProcessInput			
 	
### -field HRESULT(* )(IMFQualityManager *This,IMFTopologyNode *pNode, long lOutputIndex,IMFSample *pSample) NotifyProcessOutput			
 	
### -field HRESULT(* )(IMFQualityManager *This,IUnknown *pObject,IMFMediaEvent *pEvent) NotifyQualityEvent			
 	
### -field HRESULT(* )(IMFQualityManager *This) Shutdown			
 	
## -remarks

## -see-also