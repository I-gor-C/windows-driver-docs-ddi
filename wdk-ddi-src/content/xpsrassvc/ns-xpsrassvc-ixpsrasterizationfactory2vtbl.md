---
UID: NS.xpsrassvc.IXpsRasterizationFactory2Vtbl
title: IXpsRasterizationFactory2Vtbl
author: windows-driver-content
description: 
ms.assetid: 8b2379ff-b385-41c0-a3ba-36db05ac0539
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IXpsRasterizationFactory2Vtbl, IXpsRasterizationFactory2Vtbl
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

# IXpsRasterizationFactory2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IXpsRasterizationFactory2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IXpsRasterizationFactory2 *This) AddRef			
 	
### -field ULONG(* )(IXpsRasterizationFactory2 *This) Release			
 	
### -field HRESULT(* )(IXpsRasterizationFactory2 *This,IXpsOMPage *xpsPage,FLOAT DPIX,FLOAT DPIY,XPSRAS_RENDERING_MODE nonTextRenderingMode,XPSRAS_RENDERING_MODE textRenderingMode,XPSRAS_PIXEL_FORMAT pixelFormat,XPSRAS_BACKGROUND_COLOR backgroundColor,IXpsRasterizer **ppIXpsRasterizer) CreateRasterizer			
 	
## -remarks

## -see-also