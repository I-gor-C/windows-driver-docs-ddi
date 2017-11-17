---
UID: NS.mfidl.IMFMediaSourceTopologyProviderVtbl
title: IMFMediaSourceTopologyProviderVtbl
author: windows-driver-content
description: 
ms.assetid: 1f8d63c5-57e1-428d-a3a0-fc1ca2f37762
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFMediaSourceTopologyProviderVtbl, IMFMediaSourceTopologyProviderVtbl
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

# IMFMediaSourceTopologyProviderVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFMediaSourceTopologyProvider *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFMediaSourceTopologyProvider *This) AddRef			
 	
### -field ULONG(* )(IMFMediaSourceTopologyProvider *This) Release			
 	
### -field HRESULT(* )(IMFMediaSourceTopologyProvider *This,IMFPresentationDescriptor *pPresentationDescriptor,IMFTopology **ppTopology) GetMediaSourceTopology			
 	
## -remarks

## -see-also