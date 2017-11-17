---
UID: NS.sensorsclassextension.ISensorDriverVtbl
title: ISensorDriverVtbl
author: windows-driver-content
description: 
ms.assetid: 194c6470-75c9-4276-8281-e3c92a4df24f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: ISensorDriverVtbl, ISensorDriverVtbl
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

# ISensorDriverVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(ISensorDriver *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(ISensorDriver *This) AddRef			
 	
### -field ULONG(* )(ISensorDriver *This) Release			
 	
### -field HRESULT(* )(ISensorDriver *This,IPortableDeviceValuesCollection **ppSensorObjectCollection) OnGetSupportedSensorObjects			
 	
### -field HRESULT(* )(ISensorDriver *This,LPWSTR pwszSensorID,IPortableDeviceKeyCollection **ppSupportedProperties) OnGetSupportedProperties			
 	
### -field HRESULT(* )(ISensorDriver *This,LPWSTR pwszSensorID,IPortableDeviceKeyCollection **ppSupportedDataFields) OnGetSupportedDataFields			
 	
### -field HRESULT(* )(ISensorDriver *This,LPWSTR pwszSensorID,GUID **ppSupportedEvents,ULONG *pulEventCount) OnGetSupportedEvents			
 	
### -field HRESULT(* )(ISensorDriver *This,IWDFFile *pClientFile,LPWSTR pwszSensorID,IPortableDeviceKeyCollection *pProperties,IPortableDeviceValues **ppPropertyValues) OnGetProperties			
 	
### -field HRESULT(* )(ISensorDriver *This,IWDFFile *pClientFile,LPWSTR pwszSensorID,IPortableDeviceKeyCollection *pDataFields,IPortableDeviceValues **ppDataValues) OnGetDataFields			
 	
### -field HRESULT(* )(ISensorDriver *This,IWDFFile *pClientFile,LPWSTR pwszSensorID,IPortableDeviceValues *pPropertiesToSet,IPortableDeviceValues **ppResults) OnSetProperties			
 	
### -field HRESULT(* )(ISensorDriver *This,IWDFFile *pClientFile,LPWSTR pwszSensorID) OnClientConnect			
 	
### -field HRESULT(* )(ISensorDriver *This,IWDFFile *pClientFile,LPWSTR pwszSensorID) OnClientDisconnect			
 	
### -field HRESULT(* )(ISensorDriver *This,IWDFFile *pClientFile,LPWSTR pwszSensorID) OnClientSubscribeToEvents			
 	
### -field HRESULT(* )(ISensorDriver *This,IWDFFile *pClientFile,LPWSTR pwszSensorID) OnClientUnsubscribeFromEvents			
 	
### -field HRESULT(* )(ISensorDriver *This,IUnknown *pUnkPortableDeviceValuesParams,IUnknown *pUnkPortableDeviceValuesResults) OnProcessWpdMessage			
 	
## -remarks

## -see-also