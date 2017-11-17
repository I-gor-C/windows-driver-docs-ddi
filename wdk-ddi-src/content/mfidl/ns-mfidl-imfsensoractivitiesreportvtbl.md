---
UID: NS.mfidl.IMFSensorActivitiesReportVtbl
title: IMFSensorActivitiesReportVtbl
author: windows-driver-content
description: 
ms.assetid: e5df14c8-515e-462b-810d-1a46717203e0
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSensorActivitiesReportVtbl, IMFSensorActivitiesReportVtbl
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

# IMFSensorActivitiesReportVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSensorActivitiesReport *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSensorActivitiesReport *This) AddRef			
 	
### -field ULONG(* )(IMFSensorActivitiesReport *This) Release			
 	
### -field HRESULT(* )(IMFSensorActivitiesReport *This,ULONG *pcCount) GetCount			
 	
### -field HRESULT(* )(IMFSensorActivitiesReport *This,ULONG Index,IMFSensorActivityReport **sensorActivityReport) GetActivityReport			
 	
### -field HRESULT(* )(IMFSensorActivitiesReport *This,LPCWSTR SymbolicName,IMFSensorActivityReport **sensorActivityReport) GetActivityReportByDeviceName			
 	
## -remarks

## -see-also