---
UID: NS.mfidl.IMFSchemeHandlerVtbl
title: IMFSchemeHandlerVtbl
author: windows-driver-content
description: 
ms.assetid: 5a8601ca-d7c8-4970-8cdb-ad5a3077cd6b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSchemeHandlerVtbl, IMFSchemeHandlerVtbl
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

# IMFSchemeHandlerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSchemeHandler *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSchemeHandler *This) AddRef			
 	
### -field ULONG(* )(IMFSchemeHandler *This) Release			
 	
### -field HRESULT(* )(IMFSchemeHandler *This,LPCWSTR pwszURL,DWORD dwFlags,IPropertyStore *pProps,IUnknown **ppIUnknownCancelCookie,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginCreateObject			
 	
### -field HRESULT(* )(IMFSchemeHandler *This,IMFAsyncResult *pResult,MF_OBJECT_TYPE *pObjectType,IUnknown **ppObject) EndCreateObject			
 	
### -field HRESULT(* )(IMFSchemeHandler *This,IUnknown *pIUnknownCancelCookie) CancelObjectCreation			
 	
## -remarks

## -see-also