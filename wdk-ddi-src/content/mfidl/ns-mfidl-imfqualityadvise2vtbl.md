---
UID: NS.mfidl.IMFQualityAdvise2Vtbl
title: IMFQualityAdvise2Vtbl
author: windows-driver-content
description: 
ms.assetid: 0a76a8f1-9860-4032-bef1-00ec8d56318a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFQualityAdvise2Vtbl, IMFQualityAdvise2Vtbl
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

# IMFQualityAdvise2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFQualityAdvise2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFQualityAdvise2 *This) AddRef			
 	
### -field ULONG(* )(IMFQualityAdvise2 *This) Release			
 	
### -field HRESULT(* )(IMFQualityAdvise2 *This,MF_QUALITY_DROP_MODE eDropMode) SetDropMode			
 	
### -field HRESULT(* )(IMFQualityAdvise2 *This,MF_QUALITY_LEVEL eQualityLevel) SetQualityLevel			
 	
### -field HRESULT(* )(IMFQualityAdvise2 *This,MF_QUALITY_DROP_MODE *peDropMode) GetDropMode			
 	
### -field HRESULT(* )(IMFQualityAdvise2 *This,MF_QUALITY_LEVEL *peQualityLevel) GetQualityLevel			
 	
### -field HRESULT(* )(IMFQualityAdvise2 *This,LONGLONG hnsAmountToDrop) DropTime			
 	
### -field HRESULT(* )(IMFQualityAdvise2 *This,IMFMediaEvent *pEvent,DWORD *pdwFlags) NotifyQualityEvent			
 	
## -remarks

## -see-also