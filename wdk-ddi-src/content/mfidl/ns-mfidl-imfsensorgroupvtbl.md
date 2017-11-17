---
UID: NS.mfidl.IMFSensorGroupVtbl
title: IMFSensorGroupVtbl
author: windows-driver-content
description: 
ms.assetid: fc7e49ac-2834-4294-b307-1065e263c282
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSensorGroupVtbl, IMFSensorGroupVtbl
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

# IMFSensorGroupVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSensorGroup *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSensorGroup *This) AddRef			
 	
### -field ULONG(* )(IMFSensorGroup *This) Release			
 	
### -field HRESULT(* )(IMFSensorGroup *This,LPWSTR SymbolicLink,LONG cchSymbolicLink,LONG *pcchWritten) GetSymbolicLink			
 	
### -field HRESULT(* )(IMFSensorGroup *This,ULONGLONG *pFlags) GetFlags			
 	
### -field HRESULT(* )(IMFSensorGroup *This,IMFAttributes **ppAttributes) GetSensorGroupAttributes			
 	
### -field HRESULT(* )(IMFSensorGroup *This,DWORD *pdwCount) GetSensorDeviceCount			
 	
### -field HRESULT(* )(IMFSensorGroup *This,DWORD dwIndex,IMFSensorDevice **ppDevice) GetSensorDevice			
 	
### -field HRESULT(* )(IMFSensorGroup *This,DWORD dwIndex) SetDefaultSensorDeviceIndex			
 	
### -field HRESULT(* )(IMFSensorGroup *This,DWORD *pdwIndex) GetDefaultSensorDeviceIndex			
 	
### -field HRESULT(* )(IMFSensorGroup *This,IMFMediaSource **ppSource) CreateMediaSource			
 	
## -remarks

## -see-also