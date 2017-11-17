---
UID: NS.mfidl.IMFRateControlVtbl
title: IMFRateControlVtbl
author: windows-driver-content
description: 
ms.assetid: e57c3d8f-c9e6-494c-a89b-ee5837525055
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFRateControlVtbl, IMFRateControlVtbl
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

# IMFRateControlVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFRateControl *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFRateControl *This) AddRef			
 	
### -field ULONG(* )(IMFRateControl *This) Release			
 	
### -field HRESULT(* )(IMFRateControl *This,BOOL fThin, float flRate) SetRate			
 	
### -field HRESULT(* )(IMFRateControl *This,BOOL *pfThin, float *pflRate) GetRate			
 	
## -remarks

## -see-also