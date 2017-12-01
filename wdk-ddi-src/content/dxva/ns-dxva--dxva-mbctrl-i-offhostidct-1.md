---
UID: NS.dxva._DXVA_MBctrl_I_OffHostIDCT_1
title: DXVA_MBctrl_I_OffHostIDCT_1
author: windows-driver-content
description: The DXVA_MBctrl_I_OffHostIDCT_1 structure is sent once per macroblock by the host decoder to the accelerator to specify macroblock control commands for 4:2:0 intra pictures when using off-host IDCT.
old-location: display\dxva_mbctrl_i_offhostidct_1.htm
old-project: display
ms.assetid: c088a923-0600-48ae-8d3e-95b6bbcb59c7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVA_MBctrl_I_OffHostIDCT_1, DXVA_MBctrl_I_OffHostIDCT_1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_MBctrl_I_OffHostIDCT_1
req.alt-loc: dxva.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# DXVA_MBctrl_I_OffHostIDCT_1 structure



## -description
<p>The DXVA_MBctrl_I_OffHostIDCT_1 structure is sent once per macroblock by the host decoder to the accelerator to specify macroblock control commands for 4:2:0 intra pictures when using off-host IDCT. </p>


## -syntax

````
typedef struct _DXVA_MBctrl_I_OffHostIDCT_1 {
  WORD  wMBaddress;
  WORD  wMBtype;
  DWORD dwMB_SNL;
  WORD  wPatternCode;
  BYTE  bNumCoef[DXVA_NumBlocksPerMB_420];
} DXVA_MBctrl_I_OffHostIDCT_1;
````


## -struct-fields
<dl>

### -field <b>wMBaddress</b>

<dd>
<p>Specifies the macroblock address of the current macroblock in raster scan order. For examples of macroblock addresses see <a href="https://msdn.microsoft.com/f04c5462-db7c-4917-b8ef-22a630c82994">macroblock addresses</a>.</p>
</dd>

### -field <b>wMBtype</b>

<dd>
<p>Specifies the type of macroblock being processed. The following bits define macroblock processing.</p>
<table>
<tr>
<th>Bits</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>15 to 12</p>
</td>
<td>
<p><i>MvertFieldSel_3</i> (bit 15, the most significant bit) through <i>MvertFieldSel_0</i> (bit 12)</p>
<p>Must be zero. </p>
</td>
</tr>
<tr>
<td>
<p>11</p>
</td>
<td>
<p><i>Reserved Bit</i></p>
<p>Must be zero. </p>
</td>
</tr>
<tr>
<td>
<p>10</p>
</td>
<td>
<p><i>HostResidDiff</i></p>
<p>Specifies whether spatial-domain residual difference decoded blocks are sent or whether transform coefficients are sent for off-host IDCT for the current macroblock.</p>
<p>The <i>HostResidDiff </i>flag is always equal to zero in this structure. This flag must be zero if <b>bConfigResidDiffHost</b> is zero. This flag must be 1 if <b>bConfigResidDiffAccelerator</b> is zero. The <b>bConfigResidDiffHost</b> and <b>bConfigResidDiffAccelerator</b> members are contained in the <a href="..\dxva\ns-dxva--dxva-configpicturedecode.md">DXVA_ConfigPictureDecode</a> structure.</p>
</td>
</tr>
<tr>
<td>
<p>9 and 8</p>
</td>
<td>
<p><i>MotionType</i></p>
<p>This does not apply to intra pictures. Both bits must be zero.</p>
</td>
</tr>
<tr>
<td>
<p>7 and 6</p>
</td>
<td>
<p><i>MBscanMethod</i></p>
<p>Specifies the scan method of the macroblock control command. This must be equal to <b>bPicScanMethod</b> if <b>bPicScanFixed</b> is 1. </p>
<p>If <b>bConfigHostInverseScan</b> is zero, <i>MBscanMethod</i> is one of the following values:</p>
<ul>
<li>
<p> Zero âˆ’ zigzag scan (MPEG-2 Figure 7-2)</p>
</li>
<li>
<p> 1 âˆ’ alternate-vertical scan (MPEG-2 Figure 7-3)</p>
</li>
<li>
<p> 2 âˆ’ alternate-horizontal scan (H.263 Figure I.2 Part a)</p>
</li>
</ul>
<p>If <b>bConfigHostInverseScan</b> is 1, <i>MBscanMethod</i> is equal to 3, which is an arbitrary scan with absolute coefficient address.</p>
<p><b>bPicScanMethod</b> and <b>bPicScanFixed</b> are members of <a href="..\dxva\ns-dxva--dxva-pictureparameters.md">DXVA_PictureParameters</a>. <b>bConfigHostInverseScan</b> is a member of DXVA_ConfigPictureDecode.</p>
</td>
</tr>
<tr>
<td>
<p>5</p>
</td>
<td>
<p><i>FieldResidual</i></p>
<p>Indicates whether the residual difference blocks use a field IDCT structure as specified in MPEG-2.</p>
<p>Must be 1 if the <b>bPicStructure</b> member of <a href="..\dxva\ns-dxva--dxva-pictureparameters.md">DXVA_PictureParameters</a> is 1 or 2. When used for MPEG-2, <i>FieldResidual</i> must be zero if the <i>frame_pred_frame_DCT</i> flag in the MPEG-2 syntax is 1, and must be equal to the <i>dct_type</i> element of the MPEG-2 syntax if <i>dct_type</i> is present for the macroblock.</p>
</td>
</tr>
<tr>
<td>
<p>4</p>
</td>
<td>
<p><i>H261LoopFilter</i></p>
<p>Must be zero. </p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p><i>Motion4MV</i></p>
<p>Must be zero. </p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p><i>MotionBackward</i></p>
<p>Must be zero. </p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p><i>MotionForward</i></p>
<p>Must be zero. </p>
</td>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p><i>IntraMacroblock</i></p>
<p>Must be 1. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dwMB_SNL</b>

<dd>
<p></p>
<dl>

### -field <a id="Specifies_the_number_of_skipped_macroblocks_to_be_generated_following_the_current_macroblock__and_indicates_the_location_of_the_residual_difference_data_for_the_blocks_of_the_current_macroblock._This_member_contains_two_variables__MBskipsFollowing_in_the_most_significant_8_bits__and_MBdataLocation_in_the_least_significant_24_bits._MBskipsFollowing_indicates_the_number_of_skipped_macroblocks_to_be_generated_following_the_current_macroblock._MBdataLocation_is_an_index_into_the_residual_difference_block_data_buffer._This_index_indicates_the_location_of_the_residual_difference_data_for_the_blocks_of_the_current_macroblock__expressed_as_a_multiple_of_32_bits."></a><a id="specifies_the_number_of_skipped_macroblocks_to_be_generated_following_the_current_macroblock__and_indicates_the_location_of_the_residual_difference_data_for_the_blocks_of_the_current_macroblock._this_member_contains_two_variables__mbskipsfollowing_in_the_most_significant_8_bits__and_mbdatalocation_in_the_least_significant_24_bits._mbskipsfollowing_indicates_the_number_of_skipped_macroblocks_to_be_generated_following_the_current_macroblock._mbdatalocation_is_an_index_into_the_residual_difference_block_data_buffer._this_index_indicates_the_location_of_the_residual_difference_data_for_the_blocks_of_the_current_macroblock__expressed_as_a_multiple_of_32_bits."></a><a id="SPECIFIES_THE_NUMBER_OF_SKIPPED_MACROBLOCKS_TO_BE_GENERATED_FOLLOWING_THE_CURRENT_MACROBLOCK__AND_INDICATES_THE_LOCATION_OF_THE_RESIDUAL_DIFFERENCE_DATA_FOR_THE_BLOCKS_OF_THE_CURRENT_MACROBLOCK._THIS_MEMBER_CONTAINS_TWO_VARIABLES__MBSKIPSFOLLOWING_IN_THE_MOST_SIGNIFICANT_8_BITS__AND_MBDATALOCATION_IN_THE_LEAST_SIGNIFICANT_24_BITS._MBSKIPSFOLLOWING_INDICATES_THE_NUMBER_OF_SKIPPED_MACROBLOCKS_TO_BE_GENERATED_FOLLOWING_THE_CURRENT_MACROBLOCK._MBDATALOCATION_IS_AN_INDEX_INTO_THE_RESIDUAL_DIFFERENCE_BLOCK_DATA_BUFFER._THIS_INDEX_INDICATES_THE_LOCATION_OF_THE_RESIDUAL_DIFFERENCE_DATA_FOR_THE_BLOCKS_OF_THE_CURRENT_MACROBLOCK__EXPRESSED_AS_A_MULTIPLE_OF_32_BITS."></a>Specifies the number of skipped macroblocks to be generated following the current macroblock, and indicates the location of the residual difference data for the blocks of the current macroblock. This member contains two variables: <i>MBskipsFollowing</i> in the most significant 8 bits, and <i>MBdataLocation</i> in the least significant 24 bits. <i>MBskipsFollowing</i> indicates the number of skipped macroblocks to be generated following the current macroblock. <i>MBdataLocation</i> is an index into the residual difference block data buffer. This index indicates the location of the residual difference data for the blocks of the current macroblock, expressed as a multiple of 32 bits.

<dd></dd>
</dl>
</dd>

### -field <b>wPatternCode</b>

<dd>
<p>Indicates whether residual difference data is sent for each block in the macroblock. In an intra picture, residual difference data is sent for every block in the macroblock. The bits in <b>wPatternCode</b> that refer to all blocks of the current macroblock must be 1 in DXVA_MBctrl_I_OffHostIDCT_1.</p>
<p>Bit (11-<i>i</i>) of <b>wPatternCode</b> (where bit 0 is the least significant bit) indicates whether residual difference data is sent for block <i>i</i>, where <i>i</i> is the index of the block within the macroblock as specified in MPEG-2 figures 6-10, 6-11, and 6-12 (raster scan order for Y, followed by 4:2:0 blocks of Cb in raster scan order, followed by 4:2:0 blocks of Cr, followed by 4:2:2 blocks of Cb, followed by 4:2:2 blocks of Cr, followed by 4:4:4 blocks of Cb, followed by 4:4:4 blocks of Cr). The data for the coded blocks (those blocks having bit (11-<i>i</i>) equal to 1) is found in the residual coding buffer in the same indexing order (increasing <i>i</i>). For 4:2:0 MPEG-2 data, the value of <b>wPatternCode</b> corresponds to shifting the decoded value of CBP (coded block pattern) to the left by six bit positions (those lower-bit positions being used for 4:2:2 and 4:4:4 chroma formats).</p>
</dd>

### -field <b>bNumCoef</b>

<dd>
<p>Each value in the <b>bNumCoef</b> array indicates the number of coefficients in the residual difference data buffer for each block <i>i</i> of the macroblock. </p>
<p>The array subscript <i>i</i> is the index of the block within the macroblock as specified in MPEG-2 video Figures 6-10, 6-11, and 6-12 (raster-scan order for Y, followed by Cb, followed by Cr). </p>
<p>This member is used only when the <i>HostResidDiff</i> flag (bit 10 in <b>wMBtype</b>) is zero, and <b>bChromaFormat</b> is 1 (4:2:0). If used in 4:2:2 or 4:4:4 formats, it would increase the size of typical macroblock control commands past a critical memory alignment boundary. As a result, the <i>TCoefEOB</i> bit within the <a href="..\dxva\ns-dxva--dxva-tcoefsingle.md">DXVA_TCoefSingle</a> structure is used for determining the number of coefficients in each block in non-4:2:0 cases.</p>
<p>The purpose of <b>bNumCoef</b> is to indicate the quantity of data present for each block in the residual difference data buffer, expressed as the number of coefficients present. When the <b>bConfig4GroupedCoefs</b> member of the <a href="..\dxva\ns-dxva--dxva-configpicturedecode.md">DXVA_ConfigPictureDecode</a> structure is 1, <b>bNumCoef</b> may contain either the actual number of coefficients sent for the block or that value rounded up to be a multiple of four. The data for these coefficients is found in the residual difference buffer in the same order.</p>
</dd>
</dl>

## -remarks
<p>Skipped macroblocks are not used by intra pictures, so the <i>MBskipsFollowing</i> variable must be zero. The <i>MBdataLocation</i> variable must be zero for the first macroblock in the macroblock control command buffer. For more information about how skipped macroblocks are generated, see <a href="https://msdn.microsoft.com/98ea004b-347d-4299-a23c-da0a9d0e844f">Generating Skipped Macroblocks</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxva.h (include Dxva.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dxva\ns-dxva--dxva-mbctrl-i-hostresiddiff-1.md">DXVA_MBctrl_I_HostResidDiff_1</a>
</dt>
<dt>
<a href="..\dxva\ns-dxva--dxva-tcoefsingle.md">DXVA_TCoefSingle</a>
</dt>
<dt>
<a href="..\dxva\ns-dxva--dxva-configpicturedecode.md">DXVA_ConfigPictureDecode</a>
</dt>
<dt>
<a href="..\dxva\ns-dxva--dxva-pictureparameters.md">DXVA_PictureParameters</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_MBctrl_I_OffHostIDCT_1 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
