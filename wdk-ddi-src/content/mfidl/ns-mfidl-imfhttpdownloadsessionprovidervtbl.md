---
UID: NS.mfidl.IMFHttpDownloadSessionProviderVtbl
title: IMFHttpDownloadSessionProviderVtbl
author: windows-driver-content
description: 
ms.assetid: 9059e708-ee5e-45b0-ab70-8eee07b4b5e2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFHttpDownloadSessionProviderVtbl, IMFHttpDownloadSessionProviderVtbl
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

# IMFHttpDownloadSessionProviderVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFHttpDownloadSessionProvider *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFHttpDownloadSessionProvider *This) AddRef			
 	
### -field ULONG(* )(IMFHttpDownloadSessionProvider *This) Release			
 	
### -field HRESULT(* )(IMFHttpDownloadSessionProvider *This,LPCWSTR wszScheme,IMFHttpDownloadSession **ppDownloadSession) CreateHttpDownloadSession			
 	
## -remarks

## -see-also