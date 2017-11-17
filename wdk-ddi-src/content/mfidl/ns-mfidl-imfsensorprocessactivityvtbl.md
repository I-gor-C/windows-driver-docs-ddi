---
UID: NS.mfidl.IMFSensorProcessActivityVtbl
title: IMFSensorProcessActivityVtbl
author: windows-driver-content
description: 
ms.assetid: cbd25e01-8e32-4770-9361-c68920fae3ab
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSensorProcessActivityVtbl, IMFSensorProcessActivityVtbl
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

# IMFSensorProcessActivityVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSensorProcessActivity *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSensorProcessActivity *This) AddRef			
 	
### -field ULONG(* )(IMFSensorProcessActivity *This) Release			
 	
### -field HRESULT(* )(IMFSensorProcessActivity *This,ULONG *pPID) GetProcessId			
 	
### -field HRESULT(* )(IMFSensorProcessActivity *This,BOOL *pfStreaming) GetStreamingState			
 	
### -field HRESULT(* )(IMFSensorProcessActivity *This,MFSensorDeviceMode *pMode) GetStreamingMode			
 	
### -field HRESULT(* )(IMFSensorProcessActivity *This,FILETIME *pft) GetReportTime			
 	
## -remarks

## -see-also