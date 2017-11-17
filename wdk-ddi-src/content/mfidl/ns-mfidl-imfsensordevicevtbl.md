---
UID: NS.mfidl.IMFSensorDeviceVtbl
title: IMFSensorDeviceVtbl
author: windows-driver-content
description: 
ms.assetid: cfc1eaf9-b2f1-415c-bf13-943243d871b3
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSensorDeviceVtbl, IMFSensorDeviceVtbl
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

# IMFSensorDeviceVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSensorDevice *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSensorDevice *This) AddRef			
 	
### -field ULONG(* )(IMFSensorDevice *This) Release			
 	
### -field HRESULT(* )(IMFSensorDevice *This,ULONGLONG *pDeviceId) GetDeviceId			
 	
### -field HRESULT(* )(IMFSensorDevice *This,MFSensorDeviceType *pType) GetDeviceType			
 	
### -field HRESULT(* )(IMFSensorDevice *This,ULONGLONG *pFlags) GetFlags			
 	
### -field HRESULT(* )(IMFSensorDevice *This,LPWSTR SymbolicLink,LONG cchSymbolicLink,LONG *pcchWritten) GetSymbolicLink			
 	
### -field HRESULT(* )(IMFSensorDevice *This,IMFAttributes **ppAttributes) GetDeviceAttributes			
 	
### -field HRESULT(* )(IMFSensorDevice *This,MFSensorStreamType eType,DWORD *pdwCount) GetStreamAttributesCount			
 	
### -field HRESULT(* )(IMFSensorDevice *This,MFSensorStreamType eType,DWORD dwIndex,IMFAttributes **ppAttributes) GetStreamAttributes			
 	
### -field HRESULT(* )(IMFSensorDevice *This,MFSensorDeviceMode eMode) SetSensorDeviceMode			
 	
### -field HRESULT(* )(IMFSensorDevice *This,MFSensorDeviceMode *peMode) GetSensorDeviceMode			
 	
## -remarks

## -see-also