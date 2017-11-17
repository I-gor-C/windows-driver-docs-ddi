---
UID: NS.wudfddi.IWDFIoTargetStateManagementVtbl
title: IWDFIoTargetStateManagementVtbl
author: windows-driver-content
description: 
ms.assetid: 1458b006-0422-454d-8b8b-f7f0efaf3c9a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFIoTargetStateManagementVtbl, IWDFIoTargetStateManagementVtbl
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

# IWDFIoTargetStateManagementVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFIoTargetStateManagement *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFIoTargetStateManagement *This) AddRef			
 	
### -field ULONG(* )(IWDFIoTargetStateManagement *This) Release			
 	
### -field WDF_IO_TARGET_STATE(* )(IWDFIoTargetStateManagement *This) GetState			
 	
### -field HRESULT(* )(IWDFIoTargetStateManagement *This) Start			
 	
### -field HRESULT(* )(IWDFIoTargetStateManagement *This,WDF_IO_TARGET_SENT_IO_ACTION Action) Stop			
 	
### -field HRESULT(* )(IWDFIoTargetStateManagement *This,BOOL bIsSurpriseRemove) Remove			
 	
## -remarks

## -see-also