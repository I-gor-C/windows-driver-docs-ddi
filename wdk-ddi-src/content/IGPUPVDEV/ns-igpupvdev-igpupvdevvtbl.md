---
UID: NS.igpupvdev.IGPUPVDevVtbl
title: IGPUPVDevVtbl
author: windows-driver-content
description: 
ms.assetid: b768e67d-23ca-4189-826f-36e6574303d1
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IGPUPVDevVtbl, IGPUPVDevVtbl
req.header: igpupvdev.h
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

# IGPUPVDevVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IGPUPVDev *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IGPUPVDev *This) AddRef			
 	
### -field ULONG(* )(IGPUPVDev *This) Release			
 	
### -field HRESULT(* )(IGPUPVDev *This,PLUID DeviceLUID) GetDeviceLuid			
 	
## -remarks

## -see-also