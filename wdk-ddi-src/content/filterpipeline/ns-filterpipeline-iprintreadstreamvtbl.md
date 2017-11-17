---
UID: NS.filterpipeline.IPrintReadStreamVtbl
title: IPrintReadStreamVtbl
author: windows-driver-content
description: 
ms.assetid: 5f0ef8a8-34cd-4e98-9d56-9aaf59d1a23a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintReadStreamVtbl, IPrintReadStreamVtbl
req.header: filterpipeline.h
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

# IPrintReadStreamVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintReadStream *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintReadStream *This) AddRef			
 	
### -field ULONG(* )(IPrintReadStream *This) Release			
 	
### -field HRESULT(* )(IPrintReadStream *This,LONGLONG dlibMove,DWORD dwOrigin,ULONGLONG *plibNewPosition) Seek			
 	
### -field HRESULT(* )(IPrintReadStream *This, void *pvBuffer,ULONG cbRequested,ULONG *pcbRead,BOOL *pbEndOfFile) ReadBytes			
 	
## -remarks

## -see-also