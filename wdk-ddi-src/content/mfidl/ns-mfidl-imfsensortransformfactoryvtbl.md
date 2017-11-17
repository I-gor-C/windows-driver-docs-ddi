---
UID: NS.mfidl.IMFSensorTransformFactoryVtbl
title: IMFSensorTransformFactoryVtbl
author: windows-driver-content
description: 
ms.assetid: 6f633447-cf6a-47d3-8459-cdedbdc7c05b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSensorTransformFactoryVtbl, IMFSensorTransformFactoryVtbl
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

# IMFSensorTransformFactoryVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSensorTransformFactory *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSensorTransformFactory *This) AddRef			
 	
### -field ULONG(* )(IMFSensorTransformFactory *This) Release			
 	
### -field HRESULT(* )(IMFSensorTransformFactory *This,IMFAttributes **ppAttributes) GetFactoryAttributes			
 	
### -field HRESULT(* )(IMFSensorTransformFactory *This,DWORD dwMaxTransformCount,IMFCollection *pSensorDevices,IMFAttributes *pAttributes) InitializeFactory			
 	
### -field HRESULT(* )(IMFSensorTransformFactory *This,DWORD *pdwCount) GetTransformCount			
 	
### -field HRESULT(* )(IMFSensorTransformFactory *This,DWORD TransformIndex,GUID *pguidTransformId,IMFAttributes **ppAttributes,IMFCollection **ppStreamInformation) GetTransformInformation			
 	
### -field HRESULT(* )(IMFSensorTransformFactory *This,REFGUID guidSensorTransformID,IMFAttributes *pAttributes,IMFDeviceTransform **ppDeviceMFT) CreateTransform			
 	
## -remarks

## -see-also