---
UID: NS.dxva._DXVA_PicParams_HEVC
title: DXVA_PicParams_HEVC
author: windows-driver-content
description: 
ms.assetid: ded8f004-8ea2-4ff3-a2ff-ab83d3bf7b2d
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DXVA_PicParams_HEVC, DXVA_PicParams_HEVC, *LPDXVA_PicParams_HEVC
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

# DXVA_PicParams_HEVC structure

## -description



## -struct-fields

### -field union __unnamed_union_0b0c_24			
 	
### -field union __unnamed_union_0b0c_26			
 	
### -field union __unnamed_union_0b0c_28			
 	
### -field USHORT PicWidthInMinCbsY			
 	
### -field USHORT PicHeightInMinCbsY			
 	
### -field DXVA_PicEntry_HEVC CurrPic			
 	
### -field UCHAR sps_max_dec_pic_buffering_minus1			
 	
### -field UCHAR log2_min_luma_coding_block_size_minus3			
 	
### -field UCHAR log2_diff_max_min_luma_coding_block_size			
 	
### -field UCHAR log2_min_transform_block_size_minus2			
 	
### -field UCHAR log2_diff_max_min_transform_block_size			
 	
### -field UCHAR max_transform_hierarchy_depth_inter			
 	
### -field UCHAR max_transform_hierarchy_depth_intra			
 	
### -field UCHAR num_short_term_ref_pic_sets			
 	
### -field UCHAR num_long_term_ref_pics_sps			
 	
### -field UCHAR num_ref_idx_l0_default_active_minus1			
 	
### -field UCHAR num_ref_idx_l1_default_active_minus1			
 	
### -field CHAR init_qp_minus26			
 	
### -field UCHAR ucNumDeltaPocsOfRefRpsIdx			
 	
### -field USHORT wNumBitsForShortTermRPSInSlice			
 	
### -field USHORT ReservedBits2			
 	
### -field CHAR pps_cb_qp_offset			
 	
### -field CHAR pps_cr_qp_offset			
 	
### -field UCHAR num_tile_columns_minus1			
 	
### -field UCHAR num_tile_rows_minus1			
 	
### -field USHORT [19] column_width_minus1			
 	
### -field USHORT [21] row_height_minus1			
 	
### -field UCHAR diff_cu_qp_delta_depth			
 	
### -field CHAR pps_beta_offset_div2			
 	
### -field CHAR pps_tc_offset_div2			
 	
### -field UCHAR log2_parallel_merge_level_minus2			
 	
### -field INT CurrPicOrderCntVal			
 	
### -field DXVA_PicEntry_HEVC [15] RefPicList			
 	
### -field UCHAR ReservedBits5			
 	
### -field INT [15] PicOrderCntValList			
 	
### -field UCHAR [8] RefPicSetStCurrBefore			
 	
### -field UCHAR [8] RefPicSetStCurrAfter			
 	
### -field UCHAR [8] RefPicSetLtCurr			
 	
### -field USHORT ReservedBits6			
 	
### -field USHORT ReservedBits7			
 	
### -field UINT StatusReportFeedbackNumber			
 	
### -field USHORT  : 2 chroma_format_idc			
 	
### -field USHORT  : 1 separate_colour_plane_flag			
 	
### -field USHORT  : 3 bit_depth_luma_minus8			
 	
### -field USHORT  : 3 bit_depth_chroma_minus8			
 	
### -field USHORT  : 4 log2_max_pic_order_cnt_lsb_minus4			
 	
### -field USHORT  : 1 NoPicReorderingFlag			
 	
### -field USHORT  : 1 NoBiPredFlag			
 	
### -field USHORT  : 1 ReservedBits1			
 	
### -field USHORT wFormatAndSequenceInfoFlags			
 	
### -field UINT32  : 1 scaling_list_enabled_flag			
 	
### -field UINT32  : 1 amp_enabled_flag			
 	
### -field UINT32  : 1 sample_adaptive_offset_enabled_flag			
 	
### -field UINT32  : 1 pcm_enabled_flag			
 	
### -field UINT32  : 4 pcm_sample_bit_depth_luma_minus1			
 	
### -field UINT32  : 4 pcm_sample_bit_depth_chroma_minus1			
 	
### -field UINT32  : 2 log2_min_pcm_luma_coding_block_size_minus3			
 	
### -field UINT32  : 2 log2_diff_max_min_pcm_luma_coding_block_size			
 	
### -field UINT32  : 1 pcm_loop_filter_disabled_flag			
 	
### -field UINT32  : 1 long_term_ref_pics_present_flag			
 	
### -field UINT32  : 1 sps_temporal_mvp_enabled_flag			
 	
### -field UINT32  : 1 strong_intra_smoothing_enabled_flag			
 	
### -field UINT32  : 1 dependent_slice_segments_enabled_flag			
 	
### -field UINT32  : 1 output_flag_present_flag			
 	
### -field UINT32  : 3 num_extra_slice_header_bits			
 	
### -field UINT32  : 1 sign_data_hiding_enabled_flag			
 	
### -field UINT32  : 1 cabac_init_present_flag			
 	
### -field UINT32  : 5 ReservedBits3			
 	
### -field UINT32 dwCodingParamToolFlags			
 	
### -field UINT32  : 1 constrained_intra_pred_flag			
 	
### -field UINT32  : 1 transform_skip_enabled_flag			
 	
### -field UINT32  : 1 cu_qp_delta_enabled_flag			
 	
### -field UINT32  : 1 pps_slice_chroma_qp_offsets_present_flag			
 	
### -field UINT32  : 1 weighted_pred_flag			
 	
### -field UINT32  : 1 weighted_bipred_flag			
 	
### -field UINT32  : 1 transquant_bypass_enabled_flag			
 	
### -field UINT32  : 1 tiles_enabled_flag			
 	
### -field UINT32  : 1 entropy_coding_sync_enabled_flag			
 	
### -field UINT32  : 1 uniform_spacing_flag			
 	
### -field UINT32  : 1 loop_filter_across_tiles_enabled_flag			
 	
### -field UINT32  : 1 pps_loop_filter_across_slices_enabled_flag			
 	
### -field UINT32  : 1 deblocking_filter_override_enabled_flag			
 	
### -field UINT32  : 1 pps_deblocking_filter_disabled_flag			
 	
### -field UINT32  : 1 lists_modification_present_flag			
 	
### -field UINT32  : 1 slice_segment_header_extension_present_flag			
 	
### -field UINT32  : 1 IrapPicFlag			
 	
### -field UINT32  : 1 IdrPicFlag			
 	
### -field UINT32  : 1 IntraPicFlag			
 	
### -field UINT32  : 13 ReservedBits4			
 	
### -field UINT32 dwCodingSettingPicturePropertyFlags			
 	
## -remarks

## -see-also