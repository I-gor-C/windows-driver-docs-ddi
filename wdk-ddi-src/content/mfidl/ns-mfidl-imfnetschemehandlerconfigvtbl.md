---
UID: NS.mfidl.IMFNetSchemeHandlerConfigVtbl
title: IMFNetSchemeHandlerConfigVtbl
author: windows-driver-content
description: 
ms.assetid: d99a6d73-815a-485f-a6d2-7eb499b448ca
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFNetSchemeHandlerConfigVtbl, IMFNetSchemeHandlerConfigVtbl
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

# IMFNetSchemeHandlerConfigVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFNetSchemeHandlerConfig *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFNetSchemeHandlerConfig *This) AddRef			
 	
### -field ULONG(* )(IMFNetSchemeHandlerConfig *This) Release			
 	
### -field HRESULT(* )(IMFNetSchemeHandlerConfig *This,ULONG *pcProtocols) GetNumberOfSupportedProtocols			
 	
### -field HRESULT(* )(IMFNetSchemeHandlerConfig *This,ULONG nProtocolIndex,MFNETSOURCE_PROTOCOL_TYPE *pnProtocolType) GetSupportedProtocolType			
 	
### -field HRESULT(* )(IMFNetSchemeHandlerConfig *This) ResetProtocolRolloverSettings			
 	
## -remarks

## -see-also