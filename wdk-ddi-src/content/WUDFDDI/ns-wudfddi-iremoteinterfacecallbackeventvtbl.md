---
UID: NS.wudfddi.IRemoteInterfaceCallbackEventVtbl
title: IRemoteInterfaceCallbackEventVtbl
author: windows-driver-content
description: 
ms.assetid: 99cf7248-bd96-4f45-927c-a4bc10cd77fd
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IRemoteInterfaceCallbackEventVtbl, IRemoteInterfaceCallbackEventVtbl
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

# IRemoteInterfaceCallbackEventVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IRemoteInterfaceCallbackEvent *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IRemoteInterfaceCallbackEvent *This) AddRef			
 	
### -field ULONG(* )(IRemoteInterfaceCallbackEvent *This) Release			
 	
### -field void(* )(IRemoteInterfaceCallbackEvent *This,IWDFRemoteInterface *pWdfRemoteInterface,REFGUID EventGuid,BYTE *pbData,DWORD cbDataSize,DWORD NameBufferOffset) OnRemoteInterfaceEvent			
 	
## -remarks

## -see-also