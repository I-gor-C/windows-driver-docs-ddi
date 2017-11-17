---
UID: NS.portabledevicetypes.IPortableDeviceValuesCollectionVtbl
title: IPortableDeviceValuesCollectionVtbl
author: windows-driver-content
description: 
ms.assetid: c7412181-6aa7-4959-93ec-1bbf74ba2521
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPortableDeviceValuesCollectionVtbl, IPortableDeviceValuesCollectionVtbl
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

# IPortableDeviceValuesCollectionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPortableDeviceValuesCollection *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPortableDeviceValuesCollection *This) AddRef			
 	
### -field ULONG(* )(IPortableDeviceValuesCollection *This) Release			
 	
### -field HRESULT(* )(IPortableDeviceValuesCollection *This,DWORD *pcElems) GetCount			
 	
### -field HRESULT(* )(IPortableDeviceValuesCollection *This, const DWORD dwIndex,IPortableDeviceValues **ppValues) GetAt			
 	
### -field HRESULT(* )(IPortableDeviceValuesCollection *This,IPortableDeviceValues *pValues) Add			
 	
### -field HRESULT(* )(IPortableDeviceValuesCollection *This) Clear			
 	
### -field HRESULT(* )(IPortableDeviceValuesCollection *This, const DWORD dwIndex) RemoveAt			
 	
## -remarks

## -see-also