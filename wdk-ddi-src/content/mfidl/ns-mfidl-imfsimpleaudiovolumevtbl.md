---
UID: NS.mfidl.IMFSimpleAudioVolumeVtbl
title: IMFSimpleAudioVolumeVtbl
author: windows-driver-content
description: 
ms.assetid: 5ddabf4f-7e0a-46ab-8438-a6b57d44c9fd
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSimpleAudioVolumeVtbl, IMFSimpleAudioVolumeVtbl
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

# IMFSimpleAudioVolumeVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSimpleAudioVolume *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSimpleAudioVolume *This) AddRef			
 	
### -field ULONG(* )(IMFSimpleAudioVolume *This) Release			
 	
### -field HRESULT(* )(IMFSimpleAudioVolume *This, float fLevel) SetMasterVolume			
 	
### -field HRESULT(* )(IMFSimpleAudioVolume *This, float *pfLevel) GetMasterVolume			
 	
### -field HRESULT(* )(IMFSimpleAudioVolume *This, const BOOL bMute) SetMute			
 	
### -field HRESULT(* )(IMFSimpleAudioVolume *This,BOOL *pbMute) GetMute			
 	
## -remarks

## -see-also