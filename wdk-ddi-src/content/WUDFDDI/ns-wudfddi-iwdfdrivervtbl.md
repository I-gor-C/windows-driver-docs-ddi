---
UID: NS.wudfddi.IWDFDriverVtbl
title: IWDFDriverVtbl
author: windows-driver-content
description: 
ms.assetid: 87e8a02f-65ca-4f5d-b49c-eea754382e6d
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFDriverVtbl, IWDFDriverVtbl
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

# IWDFDriverVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFDriver *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFDriver *This) AddRef			
 	
### -field ULONG(* )(IWDFDriver *This) Release			
 	
### -field HRESULT(* )(IWDFDriver *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFDriver *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFDriver *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFDriver *This) AcquireLock			
 	
### -field void(* )(IWDFDriver *This) ReleaseLock			
 	
### -field HRESULT(* )(IWDFDriver *This,IWDFDeviceInitialize *pDeviceInit,IUnknown *pCallbackInterface,IWDFDevice **ppDevice) CreateDevice			
 	
### -field HRESULT(* )(IWDFDriver *This,IUnknown *pCallbackInterface,IWDFObject *pParentObject,IWDFObject **ppWdfObject) CreateWdfObject			
 	
### -field HRESULT(* )(IWDFDriver *This,BYTE *pBuff,SIZE_T BufferSize,IUnknown *pCallbackInterface,IWDFObject *pParentObject,IWDFMemory **ppWdfMemory) CreatePreallocatedWdfMemory			
 	
### -field HRESULT(* )(IWDFDriver *This,SIZE_T BufferSize,IUnknown *pCallbackInterface,IWDFObject *pParentObject,IWDFMemory **ppWdfMemory) CreateWdfMemory			
 	
### -field BOOL(* )(IWDFDriver *This,UMDF_VERSION_DATA *pMinimumVersion) IsVersionAvailable			
 	
### -field HRESULT(* )(IWDFDriver *This,PWSTR pVersion,DWORD *pdwVersionLength) RetrieveVersionString			
 	
## -remarks

## -see-also