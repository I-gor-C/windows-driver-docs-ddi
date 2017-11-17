---
UID: NS.dxva._DXVA_PicParams_H264_MVC
title: DXVA_PicParams_H264_MVC
author: windows-driver-content
description: 
ms.assetid: b591d59c-c61c-412a-b730-d11c3302e5e8
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DXVA_PicParams_H264_MVC, DXVA_PicParams_H264_MVC, *LPDXVA_PicParams_H264_MVC
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

# DXVA_PicParams_H264_MVC structure

## -description



## -struct-fields

### -field union __unnamed_union_0b0c_14			
 	
### -field USHORT wFrameWidthInMbsMinus1			
 	
### -field USHORT wFrameHeightInMbsMinus1			
 	
### -field DXVA_PicEntry_H264 CurrPic			
 	
### -field UCHAR num_ref_frames			
 	
### -field UCHAR bit_depth_luma_minus8			
 	
### -field UCHAR bit_depth_chroma_minus8			
 	
### -field USHORT Reserved16Bits			
 	
### -field UINT StatusReportFeedbackNumber			
 	
### -field DXVA_PicEntry_H264 [16] RefFrameList			
 	
### -field INT [2] CurrFieldOrderCnt			
 	
### -field INT [16][2] FieldOrderCntList			
 	
### -field CHAR pic_init_qs_minus26			
 	
### -field CHAR chroma_qp_index_offset			
 	
### -field CHAR second_chroma_qp_index_offset			
 	
### -field UCHAR ContinuationFlag			
 	
### -field CHAR pic_init_qp_minus26			
 	
### -field UCHAR num_ref_idx_l0_active_minus1			
 	
### -field UCHAR num_ref_idx_l1_active_minus1			
 	
### -field UCHAR Reserved8BitsA			
 	
### -field USHORT [16] FrameNumList			
 	
### -field UINT UsedForReferenceFlags			
 	
### -field USHORT NonExistingFrameFlags			
 	
### -field USHORT frame_num			
 	
### -field UCHAR log2_max_frame_num_minus4			
 	
### -field UCHAR pic_order_cnt_type			
 	
### -field UCHAR log2_max_pic_order_cnt_lsb_minus4			
 	
### -field UCHAR delta_pic_order_always_zero_flag			
 	
### -field UCHAR direct_8x8_inference_flag			
 	
### -field UCHAR entropy_coding_mode_flag			
 	
### -field UCHAR pic_order_present_flag			
 	
### -field UCHAR num_slice_groups_minus1			
 	
### -field UCHAR slice_group_map_type			
 	
### -field UCHAR deblocking_filter_control_present_flag			
 	
### -field UCHAR redundant_pic_cnt_present_flag			
 	
### -field UCHAR Reserved8BitsB			
 	
### -field USHORT slice_group_change_rate_minus1			
 	
### -field UCHAR num_views_minus1			
 	
### -field USHORT [16] view_id			
 	
### -field UCHAR [16] num_anchor_refs_l0			
 	
### -field USHORT [16][16] anchor_ref_l0			
 	
### -field UCHAR [16] num_anchor_refs_l1			
 	
### -field USHORT [16][16] anchor_ref_l1			
 	
### -field UCHAR [16] num_non_anchor_refs_l0			
 	
### -field USHORT [16][16] non_anchor_ref_l0			
 	
### -field UCHAR [16] num_non_anchor_refs_l1			
 	
### -field USHORT [16][16] non_anchor_ref_l1			
 	
### -field USHORT curr_view_id			
 	
### -field UCHAR anchor_pic_flag			
 	
### -field UCHAR inter_view_flag			
 	
### -field USHORT [16] ViewIDList			
 	
### -field USHORT  : 1 field_pic_flag			
 	
### -field USHORT  : 1 MbaffFrameFlag			
 	
### -field USHORT  : 1 residual_colour_transform_flag			
 	
### -field USHORT  : 1 sp_for_switch_flag			
 	
### -field USHORT  : 2 chroma_format_idc			
 	
### -field USHORT  : 1 RefPicFlag			
 	
### -field USHORT  : 1 constrained_intra_pred_flag			
 	
### -field USHORT  : 1 weighted_pred_flag			
 	
### -field USHORT  : 2 weighted_bipred_idc			
 	
### -field USHORT  : 1 MbsConsecutiveFlag			
 	
### -field USHORT  : 1 frame_mbs_only_flag			
 	
### -field USHORT  : 1 transform_8x8_mode_flag			
 	
### -field USHORT  : 1 MinLumaBipredSize8x8Flag			
 	
### -field USHORT  : 1 IntraPicFlag			
 	
### -field USHORT wBitFields			
 	
## -remarks

## -see-also