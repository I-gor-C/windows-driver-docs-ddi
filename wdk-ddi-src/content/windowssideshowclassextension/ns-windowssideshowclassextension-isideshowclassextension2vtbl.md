---
UID: NS.windowssideshowclassextension.ISideShowClassExtension2Vtbl
title: ISideShowClassExtension2Vtbl
author: windows-driver-content
description: 
ms.assetid: 560a6a18-98ff-4ab7-86bf-e456300085ec
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: ISideShowClassExtension2Vtbl, ISideShowClassExtension2Vtbl
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

# ISideShowClassExtension2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(ISideShowClassExtension2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(ISideShowClassExtension2 *This) AddRef			
 	
### -field ULONG(* )(ISideShowClassExtension2 *This) Release			
 	
### -field HRESULT(* )(ISideShowClassExtension2 *This,IUnknown *pWdfDeviceUnknown,IUnknown *pSideShowDriverUnknown) Initialize			
 	
### -field HRESULT(* )(ISideShowClassExtension2 *This,IUnknown *pWdfDeviceUnknown) Uninitialize			
 	
### -field HRESULT(* )(ISideShowClassExtension2 *This,IWDFIoQueue *pWdfQueue,IWDFIoRequest *pWdfRequest,ULONG ControlCode,SIZE_T InputBufferSizeInBytes,SIZE_T OutputBufferSizeInBytes,DWORD *pcbWritten) OnProcessIoControl			
 	
### -field HRESULT(* )(ISideShowClassExtension2 *This,IUnknown *pWdfDeviceUnknown,IUnknown *pSideShowDriverUnknown) InitializeAsync			
 	
### -field HRESULT(* )(ISideShowClassExtension2 *This,REFGUID in_EventGuid,SID * const in_pSid,BYTE * const in_pbEventData, const DWORD in_cbEventData) PostEvent			
 	
### -field HRESULT(* )(ISideShowClassExtension2 *This,IWDFFile *pWdfFile) CleanupFile			
 	
## -remarks

## -see-also