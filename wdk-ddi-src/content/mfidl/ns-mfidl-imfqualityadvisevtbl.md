---
UID: NS.mfidl.IMFQualityAdviseVtbl
title: IMFQualityAdviseVtbl
author: windows-driver-content
description: 
ms.assetid: 88ebb5a3-871b-41db-a30b-01a8e2f42d34
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFQualityAdviseVtbl, IMFQualityAdviseVtbl
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

# IMFQualityAdviseVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFQualityAdvise *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFQualityAdvise *This) AddRef			
 	
### -field ULONG(* )(IMFQualityAdvise *This) Release			
 	
### -field HRESULT(* )(IMFQualityAdvise *This,MF_QUALITY_DROP_MODE eDropMode) SetDropMode			
 	
### -field HRESULT(* )(IMFQualityAdvise *This,MF_QUALITY_LEVEL eQualityLevel) SetQualityLevel			
 	
### -field HRESULT(* )(IMFQualityAdvise *This,MF_QUALITY_DROP_MODE *peDropMode) GetDropMode			
 	
### -field HRESULT(* )(IMFQualityAdvise *This,MF_QUALITY_LEVEL *peQualityLevel) GetQualityLevel			
 	
### -field HRESULT(* )(IMFQualityAdvise *This,LONGLONG hnsAmountToDrop) DropTime			
 	
## -remarks

## -see-also