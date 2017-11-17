---
UID: NS.dxva._DXVA_Slice_H264_Long
title: DXVA_Slice_H264_Long
author: windows-driver-content
description: 
ms.assetid: aa1db017-ab3c-4868-b5e6-89537d3c685b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DXVA_Slice_H264_Long, DXVA_Slice_H264_Long, *LPDXVA_Slice_H264_Long
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

# DXVA_Slice_H264_Long structure

## -description



## -struct-fields

### -field UINT BSNALunitDataLocation			
 	
### -field UINT SliceBytesInBuffer			
 	
### -field USHORT wBadSliceChopping			
 	
### -field USHORT first_mb_in_slice			
 	
### -field USHORT NumMbsForSlice			
 	
### -field USHORT BitOffsetToSliceData			
 	
### -field UCHAR slice_type			
 	
### -field UCHAR luma_log2_weight_denom			
 	
### -field UCHAR chroma_log2_weight_denom			
 	
### -field UCHAR num_ref_idx_l0_active_minus1			
 	
### -field UCHAR num_ref_idx_l1_active_minus1			
 	
### -field CHAR slice_alpha_c0_offset_div2			
 	
### -field CHAR slice_beta_offset_div2			
 	
### -field UCHAR Reserved8Bits			
 	
### -field DXVA_PicEntry_H264 [2][32] RefPicList			
 	
### -field SHORT [2][32][3][2] Weights			
 	
### -field CHAR slice_qs_delta			
 	
### -field CHAR slice_qp_delta			
 	
### -field UCHAR redundant_pic_cnt			
 	
### -field UCHAR direct_spatial_mv_pred_flag			
 	
### -field UCHAR cabac_init_idc			
 	
### -field UCHAR disable_deblocking_filter_idc			
 	
### -field USHORT slice_id			
 	
## -remarks

## -see-also