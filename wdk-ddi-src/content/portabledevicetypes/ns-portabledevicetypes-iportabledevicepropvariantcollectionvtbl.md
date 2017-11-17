---
UID: NS.portabledevicetypes.IPortableDevicePropVariantCollectionVtbl
title: IPortableDevicePropVariantCollectionVtbl
author: windows-driver-content
description: 
ms.assetid: 34ae7a64-31d5-4ce4-9dbb-692d75fe77b8
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPortableDevicePropVariantCollectionVtbl, IPortableDevicePropVariantCollectionVtbl
req.header: portabledevicetypes.h
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

# IPortableDevicePropVariantCollectionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPortableDevicePropVariantCollection *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPortableDevicePropVariantCollection *This) AddRef			
 	
### -field ULONG(* )(IPortableDevicePropVariantCollection *This) Release			
 	
### -field HRESULT(* )(IPortableDevicePropVariantCollection *This,DWORD *pcElems) GetCount			
 	
### -field HRESULT(* )(IPortableDevicePropVariantCollection *This, const DWORD dwIndex,PROPVARIANT *pValue) GetAt			
 	
### -field HRESULT(* )(IPortableDevicePropVariantCollection *This, const PROPVARIANT *pValue) Add			
 	
### -field HRESULT(* )(IPortableDevicePropVariantCollection *This,VARTYPE *pvt) GetType			
 	
### -field HRESULT(* )(IPortableDevicePropVariantCollection *This, const VARTYPE vt) ChangeType			
 	
### -field HRESULT(* )(IPortableDevicePropVariantCollection *This) Clear			
 	
### -field HRESULT(* )(IPortableDevicePropVariantCollection *This, const DWORD dwIndex) RemoveAt			
 	
## -remarks

## -see-also