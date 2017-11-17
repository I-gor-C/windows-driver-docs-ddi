---
UID: NS.mfidl.IMFMetadataProviderVtbl
title: IMFMetadataProviderVtbl
author: windows-driver-content
description: 
ms.assetid: dd117430-4bc7-40df-a650-006c6ca2232b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFMetadataProviderVtbl, IMFMetadataProviderVtbl
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

# IMFMetadataProviderVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFMetadataProvider *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFMetadataProvider *This) AddRef			
 	
### -field ULONG(* )(IMFMetadataProvider *This) Release			
 	
### -field HRESULT(* )(IMFMetadataProvider *This,IMFPresentationDescriptor *pPresentationDescriptor,DWORD dwStreamIdentifier,DWORD dwFlags,IMFMetadata **ppMFMetadata) GetMFMetadata			
 	
## -remarks

## -see-also