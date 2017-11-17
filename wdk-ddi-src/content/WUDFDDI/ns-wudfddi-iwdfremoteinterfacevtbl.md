---
UID: NS.wudfddi.IWDFRemoteInterfaceVtbl
title: IWDFRemoteInterfaceVtbl
author: windows-driver-content
description: 
ms.assetid: 971bb09e-09ad-46c6-8ad7-f7daa714d420
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFRemoteInterfaceVtbl, IWDFRemoteInterfaceVtbl
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

# IWDFRemoteInterfaceVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFRemoteInterface *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFRemoteInterface *This) AddRef			
 	
### -field ULONG(* )(IWDFRemoteInterface *This) Release			
 	
### -field HRESULT(* )(IWDFRemoteInterface *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFRemoteInterface *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFRemoteInterface *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFRemoteInterface *This) AcquireLock			
 	
### -field void(* )(IWDFRemoteInterface *This) ReleaseLock			
 	
## -remarks

## -see-also