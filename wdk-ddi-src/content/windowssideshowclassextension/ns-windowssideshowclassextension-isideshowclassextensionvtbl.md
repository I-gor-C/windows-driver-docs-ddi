---
UID: NS.windowssideshowclassextension.ISideShowClassExtensionVtbl
title: ISideShowClassExtensionVtbl
author: windows-driver-content
description: 
ms.assetid: efd7e190-acd6-4d11-81c1-010463880ae3
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: ISideShowClassExtensionVtbl, ISideShowClassExtensionVtbl
req.header: windowssideshowclassextension.h
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

# ISideShowClassExtensionVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(ISideShowClassExtension *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(ISideShowClassExtension *This) AddRef			
 	
### -field ULONG(* )(ISideShowClassExtension *This) Release			
 	
### -field HRESULT(* )(ISideShowClassExtension *This,IUnknown *pWdfDeviceUnknown,IUnknown *pSideShowDriverUnknown) Initialize			
 	
### -field HRESULT(* )(ISideShowClassExtension *This,IUnknown *pWdfDeviceUnknown) Uninitialize			
 	
### -field HRESULT(* )(ISideShowClassExtension *This,IWDFIoQueue *pWdfQueue,IWDFIoRequest *pWdfRequest,ULONG ControlCode,SIZE_T InputBufferSizeInBytes,SIZE_T OutputBufferSizeInBytes,DWORD *pcbWritten) OnProcessIoControl			
 	
## -remarks

## -see-also