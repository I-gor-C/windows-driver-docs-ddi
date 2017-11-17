---
UID: NS.mfidl.IMFByteStreamHandlerVtbl
title: IMFByteStreamHandlerVtbl
author: windows-driver-content
description: 
ms.assetid: 95e4301c-e443-4d67-afac-9bc2c5204215
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFByteStreamHandlerVtbl, IMFByteStreamHandlerVtbl
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

# IMFByteStreamHandlerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFByteStreamHandler *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFByteStreamHandler *This) AddRef			
 	
### -field ULONG(* )(IMFByteStreamHandler *This) Release			
 	
### -field HRESULT(* )(IMFByteStreamHandler *This,IMFByteStream *pByteStream,LPCWSTR pwszURL,DWORD dwFlags,IPropertyStore *pProps,IUnknown **ppIUnknownCancelCookie,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginCreateObject			
 	
### -field HRESULT(* )(IMFByteStreamHandler *This,IMFAsyncResult *pResult,MF_OBJECT_TYPE *pObjectType,IUnknown **ppObject) EndCreateObject			
 	
### -field HRESULT(* )(IMFByteStreamHandler *This,IUnknown *pIUnknownCancelCookie) CancelObjectCreation			
 	
### -field HRESULT(* )(IMFByteStreamHandler *This,QWORD *pqwBytes) GetMaxNumberOfBytesRequiredForResolution			
 	
## -remarks

## -see-also