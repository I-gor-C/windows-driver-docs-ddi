---
UID: NS.portabledeviceclassextension.IPortableDeviceClassExtensionVtbl
title: IPortableDeviceClassExtensionVtbl
author: windows-driver-content
description: 
ms.assetid: 97c8112f-1000-420e-9cbd-f481f6583f4f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPortableDeviceClassExtensionVtbl, IPortableDeviceClassExtensionVtbl
req.header: portabledeviceclassextension.h
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

# IPortableDeviceClassExtensionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPortableDeviceClassExtension *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPortableDeviceClassExtension *This) AddRef			
 	
### -field ULONG(* )(IPortableDeviceClassExtension *This) Release			
 	
### -field HRESULT(* )(IPortableDeviceClassExtension *This,IUnknown *pWdfDeviceUnknown,IPortableDeviceValues *pOptions) Initialize			
 	
### -field HRESULT(* )(IPortableDeviceClassExtension *This) Uninitialize			
 	
### -field HRESULT(* )(IPortableDeviceClassExtension *This,IPortableDeviceValues *pParams,IPortableDeviceValues *pResults) ProcessLibraryMessage			
 	
## -remarks

## -see-also