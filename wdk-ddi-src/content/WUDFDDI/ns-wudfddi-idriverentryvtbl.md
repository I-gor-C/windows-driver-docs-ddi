---
UID: NS.wudfddi.IDriverEntryVtbl
title: IDriverEntryVtbl
author: windows-driver-content
description: 
ms.assetid: ac38b3c4-cb7f-444c-9d38-d68e27079bf7
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IDriverEntryVtbl, IDriverEntryVtbl
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

# IDriverEntryVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IDriverEntry *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IDriverEntry *This) AddRef			
 	
### -field ULONG(* )(IDriverEntry *This) Release			
 	
### -field HRESULT(* )(IDriverEntry *This,IWDFDriver *pWdfDriver) OnInitialize			
 	
### -field HRESULT(* )(IDriverEntry *This,IWDFDriver *pWdfDriver,IWDFDeviceInitialize *pWdfDeviceInit) OnDeviceAdd			
 	
### -field void(* )(IDriverEntry *This,IWDFDriver *pWdfDriver) OnDeinitialize			
 	
## -remarks

## -see-also