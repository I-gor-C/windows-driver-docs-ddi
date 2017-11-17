---
UID: NS.xpsrassvc.IXpsRasterizationFactory1Vtbl
title: IXpsRasterizationFactory1Vtbl
author: windows-driver-content
description: 
ms.assetid: 401b1759-5459-4b44-8c23-6f31ffbbc4eb
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IXpsRasterizationFactory1Vtbl, IXpsRasterizationFactory1Vtbl
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

# IXpsRasterizationFactory1Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IXpsRasterizationFactory1 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IXpsRasterizationFactory1 *This) AddRef			
 	
### -field ULONG(* )(IXpsRasterizationFactory1 *This) Release			
 	
### -field HRESULT(* )(IXpsRasterizationFactory1 *This,IXpsOMPage *xpsPage,FLOAT DPI,XPSRAS_RENDERING_MODE nonTextRenderingMode,XPSRAS_RENDERING_MODE textRenderingMode,XPSRAS_PIXEL_FORMAT pixelFormat,IXpsRasterizer **ppIXPSRasterizer) CreateRasterizer			
 	
## -remarks

## -see-also