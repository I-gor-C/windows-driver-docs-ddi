---
UID: NS.wudfddi.IPnpCallbackSelfManagedIoVtbl
title: IPnpCallbackSelfManagedIoVtbl
author: windows-driver-content
description: 
ms.assetid: 820f93a8-cca9-4b4f-8129-177bb27a812a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPnpCallbackSelfManagedIoVtbl, IPnpCallbackSelfManagedIoVtbl
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

# IPnpCallbackSelfManagedIoVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPnpCallbackSelfManagedIo *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPnpCallbackSelfManagedIo *This) AddRef			
 	
### -field ULONG(* )(IPnpCallbackSelfManagedIo *This) Release			
 	
### -field void(* )(IPnpCallbackSelfManagedIo *This,IWDFDevice *pWdfDevice) OnSelfManagedIoCleanup			
 	
### -field void(* )(IPnpCallbackSelfManagedIo *This,IWDFDevice *pWdfDevice) OnSelfManagedIoFlush			
 	
### -field HRESULT(* )(IPnpCallbackSelfManagedIo *This,IWDFDevice *pWdfDevice) OnSelfManagedIoInit			
 	
### -field HRESULT(* )(IPnpCallbackSelfManagedIo *This,IWDFDevice *pWdfDevice) OnSelfManagedIoSuspend			
 	
### -field HRESULT(* )(IPnpCallbackSelfManagedIo *This,IWDFDevice *pWdfDevice) OnSelfManagedIoRestart			
 	
### -field HRESULT(* )(IPnpCallbackSelfManagedIo *This,IWDFDevice *pWdfDevice) OnSelfManagedIoStop			
 	
## -remarks

## -see-also