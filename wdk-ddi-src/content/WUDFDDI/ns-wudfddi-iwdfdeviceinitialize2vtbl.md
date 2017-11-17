---
UID: NS.wudfddi.IWDFDeviceInitialize2Vtbl
title: IWDFDeviceInitialize2Vtbl
author: windows-driver-content
description: 
ms.assetid: d5ec6c3d-6689-4780-99e7-ac1715430fe3
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFDeviceInitialize2Vtbl, IWDFDeviceInitialize2Vtbl
req.header: wudfddi.h
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

# IWDFDeviceInitialize2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFDeviceInitialize2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFDeviceInitialize2 *This) AddRef			
 	
### -field ULONG(* )(IWDFDeviceInitialize2 *This) Release			
 	
### -field void(* )(IWDFDeviceInitialize2 *This) SetFilter			
 	
### -field void(* )(IWDFDeviceInitialize2 *This,WDF_CALLBACK_CONSTRAINT LockType) SetLockingConstraint			
 	
### -field HRESULT(* )(IWDFDeviceInitialize2 *This,PCWSTR pcwszServiceName,WDF_PROPERTY_STORE_RETRIEVE_FLAGS Flags,IWDFNamedPropertyStore **ppPropStore,WDF_PROPERTY_STORE_DISPOSITION *pDisposition) RetrieveDevicePropertyStore			
 	
### -field void(* )(IWDFDeviceInitialize2 *This,BOOL fTrue) SetPowerPolicyOwnership			
 	
### -field void(* )(IWDFDeviceInitialize2 *This,WDF_TRI_STATE State) AutoForwardCreateCleanupClose			
 	
### -field HRESULT(* )(IWDFDeviceInitialize2 *This,PWSTR Buffer,DWORD *pdwSizeInChars) RetrieveDeviceInstanceId			
 	
### -field void(* )(IWDFDeviceInitialize2 *This,WDF_PNP_CAPABILITY Capability,WDF_TRI_STATE Value) SetPnpCapability			
 	
### -field WDF_TRI_STATE(* )(IWDFDeviceInitialize2 *This,WDF_PNP_CAPABILITY Capability) GetPnpCapability			
 	
### -field void(* )(IWDFDeviceInitialize2 *This,WDF_DEVICE_IO_BUFFER_RETRIEVAL RetrievalMode,WDF_DEVICE_IO_TYPE ReadWritePreference,WDF_DEVICE_IO_TYPE IoControlPreference) SetIoTypePreference			
 	
## -remarks

## -see-also