---
UID: NS.mfidl.IMFCapturePhotoConfirmationVtbl
title: IMFCapturePhotoConfirmationVtbl
author: windows-driver-content
description: 
ms.assetid: 253e67cd-6785-450c-84ae-c0cb8d0bec15
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFCapturePhotoConfirmationVtbl, IMFCapturePhotoConfirmationVtbl
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

# IMFCapturePhotoConfirmationVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFCapturePhotoConfirmation *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFCapturePhotoConfirmation *This) AddRef			
 	
### -field ULONG(* )(IMFCapturePhotoConfirmation *This) Release			
 	
### -field HRESULT(* )(IMFCapturePhotoConfirmation *This,IMFAsyncCallback *pNotificationCallback) SetPhotoConfirmationCallback			
 	
### -field HRESULT(* )(IMFCapturePhotoConfirmation *This,GUID subtype) SetPixelFormat			
 	
### -field HRESULT(* )(IMFCapturePhotoConfirmation *This,GUID *subtype) GetPixelFormat			
 	
## -remarks

## -see-also