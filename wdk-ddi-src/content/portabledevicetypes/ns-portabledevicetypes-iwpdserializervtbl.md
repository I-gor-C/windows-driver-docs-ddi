---
UID: NS.portabledevicetypes.IWpdSerializerVtbl
title: IWpdSerializerVtbl
author: windows-driver-content
description: 
ms.assetid: fc36b05b-fd4e-4d2f-ad5c-dec8829c3f88
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWpdSerializerVtbl, IWpdSerializerVtbl
req.header: portabledevicetypes.h
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

# IWpdSerializerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWpdSerializer *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWpdSerializer *This) AddRef			
 	
### -field ULONG(* )(IWpdSerializer *This) Release			
 	
### -field HRESULT(* )(IWpdSerializer *This,BYTE *pBuffer,DWORD dwInputBufferLength,IPortableDeviceValues **ppParams) GetIPortableDeviceValuesFromBuffer			
 	
### -field HRESULT(* )(IWpdSerializer *This,DWORD dwOutputBufferLength,IPortableDeviceValues *pResults,BYTE *pBuffer,DWORD *pdwBytesWritten) WriteIPortableDeviceValuesToBuffer			
 	
### -field HRESULT(* )(IWpdSerializer *This,IPortableDeviceValues *pSource,BYTE **ppBuffer,DWORD *pdwBufferSize) GetBufferFromIPortableDeviceValues			
 	
### -field HRESULT(* )(IWpdSerializer *This,IPortableDeviceValues *pSource,DWORD *pdwSize) GetSerializedSize			
 	
## -remarks

## -see-also