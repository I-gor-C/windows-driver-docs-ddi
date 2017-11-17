---
UID: NS.mfidl.IMFMediaSessionVtbl
title: IMFMediaSessionVtbl
author: windows-driver-content
description: 
ms.assetid: bcbfc265-1625-444f-a3a7-b04485813e63
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFMediaSessionVtbl, IMFMediaSessionVtbl
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

# IMFMediaSessionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFMediaSession *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFMediaSession *This) AddRef			
 	
### -field ULONG(* )(IMFMediaSession *This) Release			
 	
### -field HRESULT(* )(IMFMediaSession *This,DWORD dwFlags,IMFMediaEvent **ppEvent) GetEvent			
 	
### -field HRESULT(* )(IMFMediaSession *This,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginGetEvent			
 	
### -field HRESULT(* )(IMFMediaSession *This,IMFAsyncResult *pResult,IMFMediaEvent **ppEvent) EndGetEvent			
 	
### -field HRESULT(* )(IMFMediaSession *This,MediaEventType met,REFGUID guidExtendedType,HRESULT hrStatus, const PROPVARIANT *pvValue) QueueEvent			
 	
### -field HRESULT(* )(IMFMediaSession *This,DWORD dwSetTopologyFlags,IMFTopology *pTopology) SetTopology			
 	
### -field HRESULT(* )(IMFMediaSession *This) ClearTopologies			
 	
### -field HRESULT(* )(IMFMediaSession *This, const GUID *pguidTimeFormat, const PROPVARIANT *pvarStartPosition) Start			
 	
### -field HRESULT(* )(IMFMediaSession *This) Pause			
 	
### -field HRESULT(* )(IMFMediaSession *This) Stop			
 	
### -field HRESULT(* )(IMFMediaSession *This) Close			
 	
### -field HRESULT(* )(IMFMediaSession *This) Shutdown			
 	
### -field HRESULT(* )(IMFMediaSession *This,IMFClock **ppClock) GetClock			
 	
### -field HRESULT(* )(IMFMediaSession *This,DWORD *pdwCaps) GetSessionCapabilities			
 	
### -field HRESULT(* )(IMFMediaSession *This,DWORD dwGetFullTopologyFlags,TOPOID TopoId,IMFTopology **ppFullTopology) GetFullTopology			
 	
## -remarks

## -see-also