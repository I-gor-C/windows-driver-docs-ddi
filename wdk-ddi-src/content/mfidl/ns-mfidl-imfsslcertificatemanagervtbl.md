---
UID: NS.mfidl.IMFSSLCertificateManagerVtbl
title: IMFSSLCertificateManagerVtbl
author: windows-driver-content
description: 
ms.assetid: 24d19a8c-9908-4d83-aa09-e37f453640fd
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSSLCertificateManagerVtbl, IMFSSLCertificateManagerVtbl
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

# IMFSSLCertificateManagerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSSLCertificateManager *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSSLCertificateManager *This) AddRef			
 	
### -field ULONG(* )(IMFSSLCertificateManager *This) Release			
 	
### -field HRESULT(* )(IMFSSLCertificateManager *This,LPCWSTR pszURL,BYTE **ppbData,DWORD *pcbData) GetClientCertificate			
 	
### -field HRESULT(* )(IMFSSLCertificateManager *This,LPCWSTR pszURL,IMFAsyncCallback *pCallback,IUnknown *pState) BeginGetClientCertificate			
 	
### -field HRESULT(* )(IMFSSLCertificateManager *This,IMFAsyncResult *pResult,BYTE **ppbData,DWORD *pcbData) EndGetClientCertificate			
 	
### -field HRESULT(* )(IMFSSLCertificateManager *This,LPCWSTR pszURL,BOOL *pfOverrideAutomaticCheck,BOOL *pfClientCertificateAvailable) GetCertificatePolicy			
 	
### -field HRESULT(* )(IMFSSLCertificateManager *This,LPCWSTR pszURL,BYTE *pbData,DWORD cbData,BOOL *pfIsGood) OnServerCertificate			
 	
## -remarks

## -see-also