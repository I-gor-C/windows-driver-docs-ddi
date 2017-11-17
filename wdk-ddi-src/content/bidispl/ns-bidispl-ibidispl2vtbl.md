---
UID: NS.bidispl.IBidiSpl2Vtbl
title: IBidiSpl2Vtbl
author: windows-driver-content
description: 
ms.assetid: 6836c4f5-02ab-41eb-8e22-993f209fc9e6
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IBidiSpl2Vtbl, IBidiSpl2Vtbl
req.header: bidispl.h
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

# IBidiSpl2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IBidiSpl2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IBidiSpl2 *This) AddRef			
 	
### -field ULONG(* )(IBidiSpl2 *This) Release			
 	
### -field HRESULT(* )(IBidiSpl2 *This, const LPCWSTR pszDeviceName, const DWORD dwAccess) BindDevice			
 	
### -field HRESULT(* )(IBidiSpl2 *This) UnbindDevice			
 	
### -field HRESULT(* )(IBidiSpl2 *This,BSTR bstrRequest,BSTR *pbstrResponse) SendRecvXMLString			
 	
### -field HRESULT(* )(IBidiSpl2 *This,IStream *pSRequest,IStream **ppSResponse) SendRecvXMLStream			
 	
## -remarks

## -see-also