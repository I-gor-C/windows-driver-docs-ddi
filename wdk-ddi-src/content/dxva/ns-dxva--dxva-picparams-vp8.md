---
UID: NS.dxva._DXVA_PicParams_VP8
title: DXVA_PicParams_VP8
author: windows-driver-content
description: 
ms.assetid: 0e0dd1b6-3f5d-42f0-a27e-8a09467fca69
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DXVA_PicParams_VP8, DXVA_PicParams_VP8, *LPDXVA_PicParams_VP8
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

# DXVA_PicParams_VP8 structure

## -description



## -struct-fields

### -field union __unnamed_union_0b0c_40			
 	
### -field UINT first_part_size			
 	
### -field UINT width			
 	
### -field UINT height			
 	
### -field DXVA_PicEntry_VPx CurrPic			
 	
### -field DXVA_segmentation_VP8 stVP8Segments			
 	
### -field UCHAR filter_type			
 	
### -field UCHAR filter_level			
 	
### -field UCHAR sharpness_level			
 	
### -field UCHAR mode_ref_lf_delta_enabled			
 	
### -field UCHAR mode_ref_lf_delta_update			
 	
### -field CHAR [4] ref_lf_deltas			
 	
### -field CHAR [4] mode_lf_deltas			
 	
### -field UCHAR log2_nbr_of_dct_partitions			
 	
### -field UCHAR base_qindex			
 	
### -field CHAR y1dc_delta_q			
 	
### -field CHAR y2dc_delta_q			
 	
### -field CHAR y2ac_delta_q			
 	
### -field CHAR uvdc_delta_q			
 	
### -field CHAR uvac_delta_q			
 	
### -field DXVA_PicEntry_VPx alt_fb_idx			
 	
### -field DXVA_PicEntry_VPx gld_fb_idx			
 	
### -field DXVA_PicEntry_VPx lst_fb_idx			
 	
### -field UCHAR ref_frame_sign_bias_golden			
 	
### -field UCHAR ref_frame_sign_bias_altref			
 	
### -field UCHAR refresh_entropy_probs			
 	
### -field UCHAR [4][8][3][11] vp8_coef_update_probs			
 	
### -field UCHAR mb_no_coeff_skip			
 	
### -field UCHAR prob_skip_false			
 	
### -field UCHAR prob_intra			
 	
### -field UCHAR prob_last			
 	
### -field UCHAR prob_golden			
 	
### -field UCHAR [4] intra_16x16_prob			
 	
### -field UCHAR [3] intra_chroma_prob			
 	
### -field UCHAR [2][19] vp8_mv_update_probs			
 	
### -field USHORT ReservedBits1			
 	
### -field USHORT ReservedBits2			
 	
### -field USHORT ReservedBits3			
 	
### -field UINT StatusReportFeedbackNumber			
 	
### -field UCHAR  : 1 frame_type			
 	
### -field UCHAR  : 3 version			
 	
### -field UCHAR  : 1 show_frame			
 	
### -field UCHAR  : 1 clamp_type			
 	
### -field UCHAR  : 2 ReservedFrameTag3Bits			
 	
### -field UCHAR wFrameTagFlags			
 	
## -remarks

## -see-also