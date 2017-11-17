---
UID: NS.wudfddi.IWDFUnifiedPropertyStoreVtbl
title: IWDFUnifiedPropertyStoreVtbl
author: windows-driver-content
description: 
ms.assetid: b7143f3e-81b4-4410-b58f-99738a26f522
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFUnifiedPropertyStoreVtbl, IWDFUnifiedPropertyStoreVtbl
req.header: wudfddi.h
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

# IWDFUnifiedPropertyStoreVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFUnifiedPropertyStore *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFUnifiedPropertyStore *This) AddRef			
 	
### -field ULONG(* )(IWDFUnifiedPropertyStore *This) Release			
 	
### -field HRESULT(* )(IWDFUnifiedPropertyStore *This, const DEVPROPKEY *PropertyKey,LCID Lcid,ULONG Flags,DEVPROPTYPE PropertyType,ULONG PropertyDataSize,PVOID PropertyData) SetPropertyData			
 	
### -field HRESULT(* )(IWDFUnifiedPropertyStore *This, const DEVPROPKEY *PropertyKey,LCID Lcid,ULONG Flags,ULONG PropertyDataSize,PVOID PropertyData,ULONG *PropertyDataRequiredSize,DEVPROPTYPE *PropertyType) GetPropertyData			
 	
## -remarks

## -see-also