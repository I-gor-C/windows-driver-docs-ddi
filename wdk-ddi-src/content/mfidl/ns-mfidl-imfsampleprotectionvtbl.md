---
UID: NS.mfidl.IMFSampleProtectionVtbl
title: IMFSampleProtectionVtbl
author: windows-driver-content
description: 
ms.assetid: d1f5d443-8334-45ec-96c8-62dd8d6e9bf8
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSampleProtectionVtbl, IMFSampleProtectionVtbl
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

# IMFSampleProtectionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSampleProtection *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSampleProtection *This) AddRef			
 	
### -field ULONG(* )(IMFSampleProtection *This) Release			
 	
### -field HRESULT(* )(IMFSampleProtection *This,DWORD *pdwVersion) GetInputProtectionVersion			
 	
### -field HRESULT(* )(IMFSampleProtection *This,DWORD *pdwVersion) GetOutputProtectionVersion			
 	
### -field HRESULT(* )(IMFSampleProtection *This,DWORD dwVersion,BYTE **ppCert,DWORD *pcbCert) GetProtectionCertificate			
 	
### -field HRESULT(* )(IMFSampleProtection *This,DWORD dwVersion,DWORD dwOutputId,BYTE *pbCert,DWORD cbCert,BYTE **ppbSeed,DWORD *pcbSeed) InitOutputProtection			
 	
### -field HRESULT(* )(IMFSampleProtection *This,DWORD dwVersion,DWORD dwInputId,BYTE *pbSeed,DWORD cbSeed) InitInputProtection			
 	
## -remarks

## -see-also