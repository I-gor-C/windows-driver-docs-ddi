---
UID: NS.ntddmmc._FEATURE_BD_WRITE
title: FEATURE_BD_WRITE
author: windows-driver-content
description: 
ms.assetid: 861b72f9-218a-4997-ae63-2dee7f9b2a04
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: FEATURE_BD_WRITE, FEATURE_BD_WRITE, *PFEATURE_BD_WRITE
req.header: ntddmmc.h
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

# FEATURE_BD_WRITE structure

## -description



## -struct-fields

### -field FEATURE_HEADER Header			
 	
### -field UCHAR  : 1 SupportsVerifyNotRequired			
 	
### -field UCHAR  : 7 Reserved1			
 	
### -field UCHAR [3] Reserved2			
 	
### -field BD_CLASS_SUPPORT_BITMAP Class0BitmapBDREWriteSupport			
 	
### -field BD_CLASS_SUPPORT_BITMAP Class1BitmapBDREWriteSupport			
 	
### -field BD_CLASS_SUPPORT_BITMAP Class2BitmapBDREWriteSupport			
 	
### -field BD_CLASS_SUPPORT_BITMAP Class3BitmapBDREWriteSupport			
 	
### -field BD_CLASS_SUPPORT_BITMAP Class0BitmapBDRWriteSupport			
 	
### -field BD_CLASS_SUPPORT_BITMAP Class1BitmapBDRWriteSupport			
 	
### -field BD_CLASS_SUPPORT_BITMAP Class2BitmapBDRWriteSupport			
 	
### -field BD_CLASS_SUPPORT_BITMAP Class3BitmapBDRWriteSupport			
 	
## -remarks

## -see-also