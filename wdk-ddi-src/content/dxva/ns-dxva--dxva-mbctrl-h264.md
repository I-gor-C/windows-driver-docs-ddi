---
UID: NS.dxva._DXVA_MBctrl_H264
title: DXVA_MBctrl_H264
author: windows-driver-content
description: 
ms.assetid: f71e530b-2454-4d66-aaa5-77f5f315757c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DXVA_MBctrl_H264, DXVA_MBctrl_H264, *LPDXVA_MBctrl_H264
req.header: dxva.h
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

# DXVA_MBctrl_H264 structure

## -description



## -struct-fields

### -field union __unnamed_union_0b0c_5			
 	
### -field union __unnamed_union_0b0c_7			
 	
### -field USHORT CurrMbAddr			
 	
### -field USHORT [3] wPatternCode			
 	
### -field UCHAR [3] bQpPrime			
 	
### -field UCHAR bMBresidDataQuantity			
 	
### -field ULONG dwMBdataLocation			
 	
### -field UINT  : 8 bSliceID			
 	
### -field UINT  : 5 MbType5Bits			
 	
### -field UINT  : 1 IntraMbFlag			
 	
### -field UINT  : 1 mb_field_decoding_flag			
 	
### -field UINT  : 1 transform_size_8x8_flag			
 	
### -field UINT  : 1 HostResidDiff			
 	
### -field UINT  : 1 DcBlockCodedCrFlag			
 	
### -field UINT  : 1 DcBlockCodedCbFlag			
 	
### -field UINT  : 1 DcBlockCodedYFlag			
 	
### -field UINT  : 1 FilterInternalEdgesFlag			
 	
### -field UINT  : 1 FilterLeftMbEdgeFlag			
 	
### -field UINT  : 1 FilterTopMbEdgeFlag			
 	
### -field UINT  : 1 ReservedBit			
 	
### -field UINT  : 8 bMvQuantity			
 	
### -field UINT dwMBtype			
 	
### -field union __unnamed_union_0b0c_9			
 	
### -field USHORT [4] LumaIntraPredModes			
 	
### -field UCHAR [3] ReservedIntra24Bits			
 	
### -field UCHAR  : 2 intra_chroma_pred_mode			
 	
### -field UCHAR  : 5 IntraPredAvailFlags			
 	
### -field UCHAR  : 1 ReservedIntraBit			
 	
### -field UCHAR bMbIntraStruct			
 	
### -field UCHAR bSubMbShapes			
 	
### -field UCHAR bSubMbPredModes			
 	
### -field USHORT wMvBuffOffset			
 	
### -field UCHAR [2][4] bRefPicSelect			
 	
## -remarks

## -see-also