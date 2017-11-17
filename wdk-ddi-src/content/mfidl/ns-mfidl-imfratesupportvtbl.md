---
UID: NS.mfidl.IMFRateSupportVtbl
title: IMFRateSupportVtbl
author: windows-driver-content
description: 
ms.assetid: ab2c3c3c-bdc7-4dd4-ba5c-8e3a90c8c944
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFRateSupportVtbl, IMFRateSupportVtbl
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

# IMFRateSupportVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFRateSupport *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFRateSupport *This) AddRef			
 	
### -field ULONG(* )(IMFRateSupport *This) Release			
 	
### -field HRESULT(* )(IMFRateSupport *This,MFRATE_DIRECTION eDirection,BOOL fThin, float *pflRate) GetSlowestRate			
 	
### -field HRESULT(* )(IMFRateSupport *This,MFRATE_DIRECTION eDirection,BOOL fThin, float *pflRate) GetFastestRate			
 	
### -field HRESULT(* )(IMFRateSupport *This,BOOL fThin, float flRate, float *pflNearestSupportedRate) IsRateSupported			
 	
## -remarks

## -see-also