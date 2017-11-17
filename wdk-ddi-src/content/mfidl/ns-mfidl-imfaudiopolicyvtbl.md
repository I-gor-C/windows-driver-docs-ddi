---
UID: NS.mfidl.IMFAudioPolicyVtbl
title: IMFAudioPolicyVtbl
author: windows-driver-content
description: 
ms.assetid: d912a51f-9cae-4ecb-808d-9eb719028cf8
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFAudioPolicyVtbl, IMFAudioPolicyVtbl
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

# IMFAudioPolicyVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFAudioPolicy *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFAudioPolicy *This) AddRef			
 	
### -field ULONG(* )(IMFAudioPolicy *This) Release			
 	
### -field HRESULT(* )(IMFAudioPolicy *This,REFGUID rguidClass) SetGroupingParam			
 	
### -field HRESULT(* )(IMFAudioPolicy *This,GUID *pguidClass) GetGroupingParam			
 	
### -field HRESULT(* )(IMFAudioPolicy *This,LPCWSTR pszName) SetDisplayName			
 	
### -field HRESULT(* )(IMFAudioPolicy *This,LPWSTR *pszName) GetDisplayName			
 	
### -field HRESULT(* )(IMFAudioPolicy *This,LPCWSTR pszPath) SetIconPath			
 	
### -field HRESULT(* )(IMFAudioPolicy *This,LPWSTR *pszPath) GetIconPath			
 	
## -remarks

## -see-also