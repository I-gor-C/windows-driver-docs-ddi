---
UID: NS.mfidl.IMFHttpDownloadSessionVtbl
title: IMFHttpDownloadSessionVtbl
author: windows-driver-content
description: 
ms.assetid: 88485c53-4248-41d9-ab6d-dfb890f4cfae
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFHttpDownloadSessionVtbl, IMFHttpDownloadSessionVtbl
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

# IMFHttpDownloadSessionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFHttpDownloadSession *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFHttpDownloadSession *This) AddRef			
 	
### -field ULONG(* )(IMFHttpDownloadSession *This) Release			
 	
### -field HRESULT(* )(IMFHttpDownloadSession *This,LPCWSTR szServerName,DWORD nPort) SetServer			
 	
### -field HRESULT(* )(IMFHttpDownloadSession *This,LPCWSTR szObjectName,BOOL fBypassProxyCache,BOOL fSecure,LPCWSTR szVerb,LPCWSTR szReferrer,IMFHttpDownloadRequest **ppRequest) CreateRequest			
 	
### -field HRESULT(* )(IMFHttpDownloadSession *This) Close			
 	
## -remarks

## -see-also