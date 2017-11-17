---
UID: NS.filterpipeline.IPrintReadStreamFactoryVtbl
title: IPrintReadStreamFactoryVtbl
author: windows-driver-content
description: 
ms.assetid: 55b48b92-63fc-4f91-8467-71a95efb3ca3
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPrintReadStreamFactoryVtbl, IPrintReadStreamFactoryVtbl
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

# IPrintReadStreamFactoryVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPrintReadStreamFactory *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPrintReadStreamFactory *This) AddRef			
 	
### -field ULONG(* )(IPrintReadStreamFactory *This) Release			
 	
### -field HRESULT(* )(IPrintReadStreamFactory *This,IPrintReadStream **ppStream) GetStream			
 	
## -remarks

## -see-also