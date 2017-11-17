---
UID: NS.mfidl.IMFContentEnablerVtbl
title: IMFContentEnablerVtbl
author: windows-driver-content
description: 
ms.assetid: d7046fb6-e2b1-43ed-930d-d86f57b90496
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFContentEnablerVtbl, IMFContentEnablerVtbl
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

# IMFContentEnablerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFContentEnabler *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFContentEnabler *This) AddRef			
 	
### -field ULONG(* )(IMFContentEnabler *This) Release			
 	
### -field HRESULT(* )(IMFContentEnabler *This,GUID *pType) GetEnableType			
 	
### -field HRESULT(* )(IMFContentEnabler *This,LPWSTR *ppwszURL,DWORD *pcchURL,MF_URL_TRUST_STATUS *pTrustStatus) GetEnableURL			
 	
### -field HRESULT(* )(IMFContentEnabler *This,BYTE **ppbData,DWORD *pcbData) GetEnableData			
 	
### -field HRESULT(* )(IMFContentEnabler *This,BOOL *pfAutomatic) IsAutomaticSupported			
 	
### -field HRESULT(* )(IMFContentEnabler *This) AutomaticEnable			
 	
### -field HRESULT(* )(IMFContentEnabler *This) MonitorEnable			
 	
### -field HRESULT(* )(IMFContentEnabler *This) Cancel			
 	
## -remarks

## -see-also