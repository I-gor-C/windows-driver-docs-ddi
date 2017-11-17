---
UID: NS.mfidl.IMFTranscodeSinkInfoProviderVtbl
title: IMFTranscodeSinkInfoProviderVtbl
author: windows-driver-content
description: 
ms.assetid: ff63ecc5-3072-4086-af31-181c0ef234fa
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFTranscodeSinkInfoProviderVtbl, IMFTranscodeSinkInfoProviderVtbl
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

# IMFTranscodeSinkInfoProviderVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFTranscodeSinkInfoProvider *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFTranscodeSinkInfoProvider *This) AddRef			
 	
### -field ULONG(* )(IMFTranscodeSinkInfoProvider *This) Release			
 	
### -field HRESULT(* )(IMFTranscodeSinkInfoProvider *This,LPCWSTR pwszFileName) SetOutputFile			
 	
### -field HRESULT(* )(IMFTranscodeSinkInfoProvider *This,IMFActivate *pByteStreamActivate) SetOutputByteStream			
 	
### -field HRESULT(* )(IMFTranscodeSinkInfoProvider *This,IMFTranscodeProfile *pProfile) SetProfile			
 	
### -field HRESULT(* )(IMFTranscodeSinkInfoProvider *This,MF_TRANSCODE_SINK_INFO *pSinkInfo) GetSinkInfo			
 	
## -remarks

## -see-also