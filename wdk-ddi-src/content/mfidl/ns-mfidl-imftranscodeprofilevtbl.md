---
UID: NS.mfidl.IMFTranscodeProfileVtbl
title: IMFTranscodeProfileVtbl
author: windows-driver-content
description: 
ms.assetid: cc032238-4660-430e-bcf0-231cf847c8ea
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFTranscodeProfileVtbl, IMFTranscodeProfileVtbl
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

# IMFTranscodeProfileVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFTranscodeProfile *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFTranscodeProfile *This) AddRef			
 	
### -field ULONG(* )(IMFTranscodeProfile *This) Release			
 	
### -field HRESULT(* )(IMFTranscodeProfile *This,IMFAttributes *pAttrs) SetAudioAttributes			
 	
### -field HRESULT(* )(IMFTranscodeProfile *This,IMFAttributes **ppAttrs) GetAudioAttributes			
 	
### -field HRESULT(* )(IMFTranscodeProfile *This,IMFAttributes *pAttrs) SetVideoAttributes			
 	
### -field HRESULT(* )(IMFTranscodeProfile *This,IMFAttributes **ppAttrs) GetVideoAttributes			
 	
### -field HRESULT(* )(IMFTranscodeProfile *This,IMFAttributes *pAttrs) SetContainerAttributes			
 	
### -field HRESULT(* )(IMFTranscodeProfile *This,IMFAttributes **ppAttrs) GetContainerAttributes			
 	
## -remarks

## -see-also