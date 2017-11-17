---
UID: NS.mfidl.IMFNetResourceFilterVtbl
title: IMFNetResourceFilterVtbl
author: windows-driver-content
description: 
ms.assetid: 51df7056-2e38-48d1-9128-8333f102e0f7
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFNetResourceFilterVtbl, IMFNetResourceFilterVtbl
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

# IMFNetResourceFilterVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFNetResourceFilter *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFNetResourceFilter *This) AddRef			
 	
### -field ULONG(* )(IMFNetResourceFilter *This) Release			
 	
### -field HRESULT(* )(IMFNetResourceFilter *This,LPCWSTR pszUrl,VARIANT_BOOL *pvbCancel) OnRedirect			
 	
### -field HRESULT(* )(IMFNetResourceFilter *This,LPCWSTR pszUrl) OnSendingRequest			
 	
## -remarks

## -see-also