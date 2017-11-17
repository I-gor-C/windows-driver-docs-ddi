---
UID: NS.xpsrassvc.IXpsRasterizerVtbl
title: IXpsRasterizerVtbl
author: windows-driver-content
description: 
ms.assetid: 6e3febc5-adb8-43e2-aaca-c82de61b243b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IXpsRasterizerVtbl, IXpsRasterizerVtbl
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

# IXpsRasterizerVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IXpsRasterizer *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IXpsRasterizer *This) AddRef			
 	
### -field ULONG(* )(IXpsRasterizer *This) Release			
 	
### -field HRESULT(* )(IXpsRasterizer *This,INT x,INT y,INT width,INT height,IXpsRasterizerNotificationCallback *notificationCallback,IWICBitmap **bitmap) RasterizeRect			
 	
### -field HRESULT(* )(IXpsRasterizer *This,INT width) SetMinimalLineWidth			
 	
## -remarks

## -see-also