---
UID: NS.portabledevicetypes.IPortableDeviceKeyCollectionVtbl
title: IPortableDeviceKeyCollectionVtbl
author: windows-driver-content
description: 
ms.assetid: 15bf69fc-31fe-48a1-83b2-d11beb625388
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPortableDeviceKeyCollectionVtbl, IPortableDeviceKeyCollectionVtbl
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

# IPortableDeviceKeyCollectionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPortableDeviceKeyCollection *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPortableDeviceKeyCollection *This) AddRef			
 	
### -field ULONG(* )(IPortableDeviceKeyCollection *This) Release			
 	
### -field HRESULT(* )(IPortableDeviceKeyCollection *This,DWORD *pcElems) GetCount			
 	
### -field HRESULT(* )(IPortableDeviceKeyCollection *This, const DWORD dwIndex,PROPERTYKEY *pKey) GetAt			
 	
### -field HRESULT(* )(IPortableDeviceKeyCollection *This,REFPROPERTYKEY Key) Add			
 	
### -field HRESULT(* )(IPortableDeviceKeyCollection *This) Clear			
 	
### -field HRESULT(* )(IPortableDeviceKeyCollection *This, const DWORD dwIndex) RemoveAt			
 	
## -remarks

## -see-also