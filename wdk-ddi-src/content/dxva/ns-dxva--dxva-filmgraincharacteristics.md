---
UID: NS.dxva._DXVA_FilmGrainCharacteristics
title: DXVA_FilmGrainCharacteristics
author: windows-driver-content
description: 
ms.assetid: 68a543ee-d7d1-403e-a96f-4753cb2125f3
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DXVA_FilmGrainCharacteristics, DXVA_FilmGrainChar_H264, *LPDXVA_FilmGrainChar_H264
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

# DXVA_FilmGrainCharacteristics structure

## -description



## -struct-fields

### -field USHORT wFrameWidthInMbsMinus1			
 	
### -field USHORT wFrameHeightInMbsMinus1			
 	
### -field DXVA_PicEntry_H264 InPic			
 	
### -field DXVA_PicEntry_H264 OutPic			
 	
### -field USHORT PicOrderCnt_offset			
 	
### -field INT CurrPicOrderCnt			
 	
### -field UINT StatusReportFeedbackNumber			
 	
### -field UCHAR model_id			
 	
### -field UCHAR separate_colour_description_present_flag			
 	
### -field UCHAR film_grain_bit_depth_luma_minus8			
 	
### -field UCHAR film_grain_bit_depth_chroma_minus8			
 	
### -field UCHAR film_grain_full_range_flag			
 	
### -field UCHAR film_grain_colour_primaries			
 	
### -field UCHAR film_grain_transfer_characteristics			
 	
### -field UCHAR film_grain_matrix_coefficients			
 	
### -field UCHAR blending_mode_id			
 	
### -field UCHAR log2_scale_factor			
 	
### -field UCHAR [4] comp_model_present_flag			
 	
### -field UCHAR [4] num_intensity_intervals_minus1			
 	
### -field UCHAR [4] num_model_values_minus1			
 	
### -field UCHAR [3][16] intensity_interval_lower_bound			
 	
### -field UCHAR [3][16] intensity_interval_upper_bound			
 	
### -field SHORT [3][16][8] comp_model_value			
 	
## -remarks

## -see-also