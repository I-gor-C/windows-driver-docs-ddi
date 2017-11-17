---
UID: NS.sensorsclassextension.ISensorClassExtensionVtbl
title: ISensorClassExtensionVtbl
author: windows-driver-content
description: 
ms.assetid: 8fa3c8f3-25d1-4891-970d-3b327498e5c0
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: ISensorClassExtensionVtbl, ISensorClassExtensionVtbl
req.header: sensorsclassextension.h
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

# ISensorClassExtensionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(ISensorClassExtension *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(ISensorClassExtension *This) AddRef			
 	
### -field ULONG(* )(ISensorClassExtension *This) Release			
 	
### -field HRESULT(* )(ISensorClassExtension *This,IUnknown *pWdfDeviceUnknown,IUnknown *pSensorDriverUnknown) Initialize			
 	
### -field HRESULT(* )(ISensorClassExtension *This) Uninitialize			
 	
### -field HRESULT(* )(ISensorClassExtension *This,IWDFIoRequest *pRequest) ProcessIoControl			
 	
### -field HRESULT(* )(ISensorClassExtension *This,LPWSTR pwszSensorID,IPortableDeviceValuesCollection *pEventCollection) PostEvent			
 	
### -field HRESULT(* )(ISensorClassExtension *This,LPWSTR pwszSensorID,SensorState state) PostStateChange			
 	
### -field HRESULT(* )(ISensorClassExtension *This,IWDFFile *pWdfFile) CleanupFile			
 	
## -remarks

## -see-also