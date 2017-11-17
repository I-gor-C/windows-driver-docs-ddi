---
UID: NS.mfidl.IMFSaveJobVtbl
title: IMFSaveJobVtbl
author: windows-driver-content
description: 
ms.assetid: 45fde299-da6c-494b-bba3-cbd4f07d443f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSaveJobVtbl, IMFSaveJobVtbl
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

# IMFSaveJobVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSaveJob *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSaveJob *This) AddRef			
 	
### -field ULONG(* )(IMFSaveJob *This) Release			
 	
### -field HRESULT(* )(IMFSaveJob *This,IMFByteStream *pStream,IMFAsyncCallback *pCallback,IUnknown *pState) BeginSave			
 	
### -field HRESULT(* )(IMFSaveJob *This,IMFAsyncResult *pResult) EndSave			
 	
### -field HRESULT(* )(IMFSaveJob *This) CancelSave			
 	
### -field HRESULT(* )(IMFSaveJob *This,DWORD *pdwPercentComplete) GetProgress			
 	
## -remarks

## -see-also