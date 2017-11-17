---
UID: NS.mfidl.IMFNetCrossOriginSupportVtbl
title: IMFNetCrossOriginSupportVtbl
author: windows-driver-content
description: 
ms.assetid: 433677ab-d8cf-496c-ad0f-7921bbca5410
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFNetCrossOriginSupportVtbl, IMFNetCrossOriginSupportVtbl
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

# IMFNetCrossOriginSupportVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFNetCrossOriginSupport *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFNetCrossOriginSupport *This) AddRef			
 	
### -field ULONG(* )(IMFNetCrossOriginSupport *This) Release			
 	
### -field HRESULT(* )(IMFNetCrossOriginSupport *This,MF_CROSS_ORIGIN_POLICY *pPolicy) GetCrossOriginPolicy			
 	
### -field HRESULT(* )(IMFNetCrossOriginSupport *This,LPWSTR *wszSourceOrigin) GetSourceOrigin			
 	
### -field HRESULT(* )(IMFNetCrossOriginSupport *This,LPCWSTR wszURL,BOOL *pfIsSameOrigin) IsSameOrigin			
 	
## -remarks

## -see-also