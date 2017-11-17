---
UID: NS.xpsrassvc.IXpsRasterizationFactoryVtbl
title: IXpsRasterizationFactoryVtbl
author: windows-driver-content
description: 
ms.assetid: 5838d002-75b7-44dc-b9e4-bfc484c58760
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IXpsRasterizationFactoryVtbl, IXpsRasterizationFactoryVtbl
req.header: xpsrassvc.h
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

# IXpsRasterizationFactoryVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IXpsRasterizationFactory *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IXpsRasterizationFactory *This) AddRef			
 	
### -field ULONG(* )(IXpsRasterizationFactory *This) Release			
 	
### -field HRESULT(* )(IXpsRasterizationFactory *This,IXpsOMPage *xpsPage,FLOAT DPI,XPSRAS_RENDERING_MODE nonTextRenderingMode,XPSRAS_RENDERING_MODE textRenderingMode,IXpsRasterizer **ppIXPSRasterizer) CreateRasterizer			
 	
## -remarks

## -see-also