---
UID: NS.dxva._DXVA_PicParams_VP9
title: DXVA_PicParams_VP9
author: windows-driver-content
description: 
ms.assetid: e2763f12-7141-4c70-a2cc-10316e3a3940
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DXVA_PicParams_VP9, DXVA_PicParams_VP9, *LPDXVA_PicParams_VP9
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

# DXVA_PicParams_VP9 structure

## -description



## -struct-fields

### -field union __unnamed_union_0b0c_34			
 	
### -field union __unnamed_union_0b0c_36			
 	
### -field DXVA_PicEntry_VPx CurrPic			
 	
### -field UCHAR profile			
 	
### -field UINT width			
 	
### -field UINT height			
 	
### -field UCHAR BitDepthMinus8Luma			
 	
### -field UCHAR BitDepthMinus8Chroma			
 	
### -field UCHAR interp_filter			
 	
### -field UCHAR Reserved8Bits			
 	
### -field DXVA_PicEntry_VPx [8] ref_frame_map			
 	
### -field UINT [8] ref_frame_coded_width			
 	
### -field UINT [8] ref_frame_coded_height			
 	
### -field DXVA_PicEntry_VPx [3] frame_refs			
 	
### -field CHAR [4] ref_frame_sign_bias			
 	
### -field CHAR filter_level			
 	
### -field CHAR sharpness_level			
 	
### -field CHAR [4] ref_deltas			
 	
### -field CHAR [2] mode_deltas			
 	
### -field SHORT base_qindex			
 	
### -field CHAR y_dc_delta_q			
 	
### -field CHAR uv_dc_delta_q			
 	
### -field CHAR uv_ac_delta_q			
 	
### -field DXVA_segmentation_VP9 stVP9Segments			
 	
### -field UCHAR log2_tile_cols			
 	
### -field UCHAR log2_tile_rows			
 	
### -field USHORT uncompressed_header_size_byte_aligned			
 	
### -field USHORT first_partition_size			
 	
### -field USHORT Reserved16Bits			
 	
### -field UINT Reserved32Bits			
 	
### -field UINT StatusReportFeedbackNumber			
 	
### -field USHORT  : 1 frame_type			
 	
### -field USHORT  : 1 show_frame			
 	
### -field USHORT  : 1 error_resilient_mode			
 	
### -field USHORT  : 1 subsampling_x			
 	
### -field USHORT  : 1 subsampling_y			
 	
### -field USHORT  : 1 extra_plane			
 	
### -field USHORT  : 1 refresh_frame_context			
 	
### -field USHORT  : 1 frame_parallel_decoding_mode			
 	
### -field USHORT  : 1 intra_only			
 	
### -field USHORT  : 2 frame_context_idx			
 	
### -field USHORT  : 2 reset_frame_context			
 	
### -field USHORT  : 1 allow_high_precision_mv			
 	
### -field USHORT  : 2 ReservedFormatInfo2Bits			
 	
### -field USHORT wFormatAndPictureInfoFlags			
 	
### -field UCHAR  : 1 mode_ref_delta_enabled			
 	
### -field UCHAR  : 1 mode_ref_delta_update			
 	
### -field UCHAR  : 1 use_prev_in_find_mv_refs			
 	
### -field UCHAR  : 5 ReservedControlInfo5Bits			
 	
### -field UCHAR wControlInfoFlags			
 	
## -remarks

## -see-also