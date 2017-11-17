---
UID: NS.mfidl.IMFSequencerSourceVtbl
title: IMFSequencerSourceVtbl
author: windows-driver-content
description: 
ms.assetid: 040635d8-efb9-4172-b268-b6d01788a214
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSequencerSourceVtbl, IMFSequencerSourceVtbl
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

# IMFSequencerSourceVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSequencerSource *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSequencerSource *This) AddRef			
 	
### -field ULONG(* )(IMFSequencerSource *This) Release			
 	
### -field HRESULT(* )(IMFSequencerSource *This,IMFTopology *pTopology,DWORD dwFlags,MFSequencerElementId *pdwId) AppendTopology			
 	
### -field HRESULT(* )(IMFSequencerSource *This,MFSequencerElementId dwId) DeleteTopology			
 	
### -field HRESULT(* )(IMFSequencerSource *This,IMFPresentationDescriptor *pPD,MFSequencerElementId *pId,IMFTopology **ppTopology) GetPresentationContext			
 	
### -field HRESULT(* )(IMFSequencerSource *This,MFSequencerElementId dwId,IMFTopology *pTopology) UpdateTopology			
 	
### -field HRESULT(* )(IMFSequencerSource *This,MFSequencerElementId dwId,DWORD dwFlags) UpdateTopologyFlags			
 	
## -remarks

## -see-also