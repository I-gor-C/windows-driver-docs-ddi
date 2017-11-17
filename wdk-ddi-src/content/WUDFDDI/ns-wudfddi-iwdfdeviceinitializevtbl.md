---
UID: NS.wudfddi.IWDFDeviceInitializeVtbl
title: IWDFDeviceInitializeVtbl
author: windows-driver-content
description: 
ms.assetid: fe1fe31d-3506-4b91-a870-e17e7df08cf7
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFDeviceInitializeVtbl, IWDFDeviceInitializeVtbl
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

# IWDFDeviceInitializeVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFDeviceInitialize *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFDeviceInitialize *This) AddRef			
 	
### -field ULONG(* )(IWDFDeviceInitialize *This) Release			
 	
### -field void(* )(IWDFDeviceInitialize *This) SetFilter			
 	
### -field void(* )(IWDFDeviceInitialize *This,WDF_CALLBACK_CONSTRAINT LockType) SetLockingConstraint			
 	
### -field HRESULT(* )(IWDFDeviceInitialize *This,PCWSTR pcwszServiceName,WDF_PROPERTY_STORE_RETRIEVE_FLAGS Flags,IWDFNamedPropertyStore **ppPropStore,WDF_PROPERTY_STORE_DISPOSITION *pDisposition) RetrieveDevicePropertyStore			
 	
### -field void(* )(IWDFDeviceInitialize *This,BOOL fTrue) SetPowerPolicyOwnership			
 	
### -field void(* )(IWDFDeviceInitialize *This,WDF_TRI_STATE State) AutoForwardCreateCleanupClose			
 	
### -field HRESULT(* )(IWDFDeviceInitialize *This,PWSTR Buffer,DWORD *pdwSizeInChars) RetrieveDeviceInstanceId			
 	
### -field void(* )(IWDFDeviceInitialize *This,WDF_PNP_CAPABILITY Capability,WDF_TRI_STATE Value) SetPnpCapability			
 	
### -field WDF_TRI_STATE(* )(IWDFDeviceInitialize *This,WDF_PNP_CAPABILITY Capability) GetPnpCapability			
 	
## -remarks

## -see-also