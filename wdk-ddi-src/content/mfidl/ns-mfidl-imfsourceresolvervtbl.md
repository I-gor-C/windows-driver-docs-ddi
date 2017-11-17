---
UID: NS.mfidl.IMFSourceResolverVtbl
title: IMFSourceResolverVtbl
author: windows-driver-content
description: 
ms.assetid: a1d17190-23dc-40d7-ad09-3c1f1794d08f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSourceResolverVtbl, IMFSourceResolverVtbl
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

# IMFSourceResolverVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSourceResolver *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSourceResolver *This) AddRef			
 	
### -field ULONG(* )(IMFSourceResolver *This) Release			
 	
### -field HRESULT(* )(IMFSourceResolver *This,LPCWSTR pwszURL,DWORD dwFlags,IPropertyStore *pProps,MF_OBJECT_TYPE *pObjectType,IUnknown **ppObject) CreateObjectFromURL			
 	
### -field HRESULT(* )(IMFSourceResolver *This,IMFByteStream *pByteStream,LPCWSTR pwszURL,DWORD dwFlags,IPropertyStore *pProps,MF_OBJECT_TYPE *pObjectType,IUnknown **ppObject) CreateObjectFromByteStream			
 	
### -field HRESULT(* )(IMFSourceResolver *This,LPCWSTR pwszURL,DWORD dwFlags,IPropertyStore *pProps,IUnknown **ppIUnknownCancelCookie,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginCreateObjectFromURL			
 	
### -field HRESULT(* )(IMFSourceResolver *This,IMFAsyncResult *pResult,MF_OBJECT_TYPE *pObjectType,IUnknown **ppObject) EndCreateObjectFromURL			
 	
### -field HRESULT(* )(IMFSourceResolver *This,IMFByteStream *pByteStream,LPCWSTR pwszURL,DWORD dwFlags,IPropertyStore *pProps,IUnknown **ppIUnknownCancelCookie,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginCreateObjectFromByteStream			
 	
### -field HRESULT(* )(IMFSourceResolver *This,IMFAsyncResult *pResult,MF_OBJECT_TYPE *pObjectType,IUnknown **ppObject) EndCreateObjectFromByteStream			
 	
### -field HRESULT(* )(IMFSourceResolver *This,IUnknown *pIUnknownCancelCookie) CancelObjectCreation			
 	
## -remarks

## -see-also