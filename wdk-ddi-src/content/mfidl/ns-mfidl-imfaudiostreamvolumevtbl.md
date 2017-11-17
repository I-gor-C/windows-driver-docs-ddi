---
UID: NS.mfidl.IMFAudioStreamVolumeVtbl
title: IMFAudioStreamVolumeVtbl
author: windows-driver-content
description: 
ms.assetid: 34aecb47-d110-42d1-befb-50c4a8860a34
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFAudioStreamVolumeVtbl, IMFAudioStreamVolumeVtbl
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

# IMFAudioStreamVolumeVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFAudioStreamVolume *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFAudioStreamVolume *This) AddRef			
 	
### -field ULONG(* )(IMFAudioStreamVolume *This) Release			
 	
### -field HRESULT(* )(IMFAudioStreamVolume *This,UINT32 *pdwCount) GetChannelCount			
 	
### -field HRESULT(* )(IMFAudioStreamVolume *This,UINT32 dwIndex, const float fLevel) SetChannelVolume			
 	
### -field HRESULT(* )(IMFAudioStreamVolume *This,UINT32 dwIndex, float *pfLevel) GetChannelVolume			
 	
### -field HRESULT(* )(IMFAudioStreamVolume *This,UINT32 dwCount, const float *pfVolumes) SetAllVolumes			
 	
### -field HRESULT(* )(IMFAudioStreamVolume *This,UINT32 dwCount, float *pfVolumes) GetAllVolumes			
 	
## -remarks

## -see-also