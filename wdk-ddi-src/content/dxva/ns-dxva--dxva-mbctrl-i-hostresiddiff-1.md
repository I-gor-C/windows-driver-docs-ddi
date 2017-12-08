---
UID: NS.dxva._DXVA_MBctrl_I_HostResidDiff_1
title: DXVA_MBctrl_I_HostResidDiff_1
author: windows-driver-content
description: The DXVA_MBctrl_I_HostResidDiff_1 structure is sent once per macroblock by the host decoder to the accelerator to specify macroblock control commands for an intra picture.
old-location: display\dxva_mbctrl_i_hostresiddiff_1.htm
old-project: display
ms.assetid: e2318d02-f52e-4b5b-86da-04df7b31b7d3
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVA_MBctrl_I_HostResidDiff_1, DXVA_MBctrl_I_HostResidDiff_1
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
req.alt-api: DXVA_MBctrl_I_HostResidDiff_1
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

# DXVA_MBctrl_I_HostResidDiff_1 structure



## -description
<p>The DXVA_MBctrl_I_HostResidDiff_1 structure is sent once per macroblock by the host decoder to the accelerator to specify macroblock control commands for an <a href="wdkgloss.i#wdkgloss.intra_picture#wdkgloss.intra_picture"><i>intra picture</i></a>.</p>


## -syntax

````
typedef struct _DXVA_MBctrl_I_HostResidDiff_1 {
  WORD  wMBaddress;
  WORD  wMBtype;
  DWORD dwMB_SNL;
  WORD  wPatternCode;
  WORD  wPC_Overflow;
  DWORD dwReservedBits2;
} DXVA_MBctrl_I_HostResidDiff_1;
````


## -struct-fields
<dl>

### -field wMBaddress

<dd>
<p>Specifies the macroblock address of the current macroblock in raster scan order. For examples of macroblock addresses, see <a href="https://msdn.microsoft.com/f04c5462-db7c-4917-b8ef-22a630c82994">macroblock addresses</a>.</p>
</dd>

### -field wMBtype

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
<p><i>MvertFieldSel_</i>3 (bit 15, the most significant bit) through <i>MvertFieldSel</i>_0 (bit 12)</p>
<p>Specifies vertical field selection for corresponding motion vectors sent later in the macroblock control command. For frame-based motion with a frame picture structure (for example, for H.261 and H.263), these bits must all be zero. The bits in <i>MvertFieldSel_0, MvertFieldSel_1, MvertFieldSel_2, </i>and <i>MvertFieldSel_3</i> correspond to the motion_vertical_field_select[r][s] bits in Section 6.3.17.2 of MPEG-2.</p>
</td>
</tr>
<tr>
<td>
<p>11</p>
</td>
<td>
<p><i>Reserved Bit</i></p>
<p>Must be zero.</p>
</td>
</tr>
<tr>
<td>
<p>10</p>
</td>
<td>
<p><i>HostResidDiff</i></p>
<p>Specifies whether spatial-domain residual difference decoded blocks are sent or whether transform coefficients are sent for off-host IDCT for the current macroblock.</p>
<p><i>HostResidDiff </i>is always equal to 1 in this structure. This flag must be zero if <b>bConfigResidDiffHost</b> is zero. This flag must be 1 if <b>bConfigResidDiffAccelerator</b> is zero. The <b>bConfigResidDiffHost</b> and <b>bConfigResidDiffAccelerator</b> members are contained in the <a href="..\dxva\ns-dxva--dxva-configpicturedecode.md">DXVA_ConfigPictureDecode</a> structure.</p>
</td>
</tr>
<tr>
<td>
<p>9 and 8</p>
</td>
<td>
<p><i>MotionType</i></p>
<p>Must be zero.</p>
</td>
</tr>
<tr>
<td>
<p>7 and 6</p>
</td>
<td>
<p><i>MBscanMethod</i></p>
<p>These bits have no meaning and should be set to zero.</p>
</td>
</tr>
<tr>
<td>
<p>5</p>
</td>
<td>
<p><i>FieldResidual</i></p>
<p>Indicates whether the residual difference blocks use a field IDCT structure as specified in MPEG-2.</p>
<p>Must be 1 if the <b>bPicStructure</b> member of DXVA_PictureParameters is 1 or 2. When used for MPEG-2, <i>FieldResidual</i> must be zero if the <i>frame_pred_frame_DCT</i> flag in the MPEG-2 syntax is 1, and must be equal to the <i>dct_type</i> variable of the MPEG-2 syntax if <i>dct_type</i> is present for the macroblock.</p>
</td>
</tr>
<tr>
<td>
<p>4</p>
</td>
<td>
<p><i>H261LoopFilter</i></p>
<p>Must be zero.</p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p><i>Motion4MV</i></p>
<p>Must be zero.</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p><i>MotionBackward</i></p>
<p>Must be zero.</p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p><i>MotionForward</i></p>
<p>Must be zero.</p>
</td>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p><i>IntraMacroblock</i></p>
<p>Must be 1.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field dwMB_SNL

<dd>
<p>Specifies the number of skipped macroblocks to be generated following the current macroblock, and indicates the location of the residual difference data for the blocks of the current macroblock. This member contains two variables: <i>MBskipsFollowing</i> in the most significant 8 bits, and <i>MBdataLocation</i> in the least significant 24 bits. <i>MBskipsFollowing</i> indicates the number of skipped macroblocks to be generated following the current macroblock. <i>MBdataLocation</i> is an index into the residual difference block data buffer. This index indicates the location of the residual difference data for the blocks of the current macroblock, expressed as a multiple of 32 bits.</p>
</dd>

### -field wPatternCode

<dd>
<p>Indicates whether residual difference data is sent for each block in the macroblock. In an intra picture, residual difference data is sent for every block in the macroblock. The bits in <b>wPatternCode</b> that refer to all blocks of the current macroblock must be 1 in this structure. </p>
<p>Bit (11-<i>i</i>) of <b>wPatternCode</b> (where bit zero is the least significant bit) indicates whether residual difference data is sent for block <i>i</i>, where <i>i</i> is the index of the block within the macroblock as specified in MPEG-2 figures 6-10, 6-11, and 6-12 (raster-scan order for Y, followed by 4:2:0 blocks of Cb in raster-scan order, followed by 4:2:0 blocks of Cr, followed by 4:2:2 blocks of Cb, followed by 4:2:2 blocks of Cr, followed by 4:4:4 blocks of Cb, followed by 4:4:4 blocks of Cr). The data for the coded blocks (those blocks having bit (11<i>i</i>) equal to 1) is found in the residual coding buffer in the same indexing order (increasing <i>i</i>). For 4:2:0 MPEG-2 data, the value of <b>wPatternCode</b> corresponds to shifting the decoded value of the CBP (coded block pattern) to the left by six bit positions (those lower bit positions being used for 4:2:2 and 4:4:4 chroma formats).</p>
<p>If the <b>bConfigSpatialResidInterleaved</b> member of the <a href="..\dxva\ns-dxva--dxva-configpicturedecode.md">DXVA_ConfigPictureDecode</a> structure is 1, host-based residual differences are sent in a chroma-interleaved form matching that of the YUV pixel format in use. In this case, each Cb and spatially corresponding Cr pair of blocks is treated as a single residual difference structure unit. This does not alter the value or meaning of <b>wPatternCode</b>, but it implies that both members of each pair of Cb and Cr data blocks are sent whenever either of these data blocks has the corresponding bit set in <b>wPatternCode</b>. If the bit in <b>wPatternCode</b> for a particular data block is zero, the corresponding residual difference data values must be sent as zero whenever this pairing necessitates sending a residual difference data block for a block with a <b>wPatternCode</b> bit equal to zero.</p>
</dd>

### -field wPC_Overflow

<dd>
<p>Must be zero.</p>
</dd>

### -field dwReservedBits2

<dd>
<p>Reserved bits used for packing and alignment. Must be zero.</p>
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
<a href="..\dxva\ns-dxva--dxva-mbctrl-i-offhostidct-1.md">DXVA_MBctrl_I_OffHostIDCT_1</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_MBctrl_I_HostResidDiff_1 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
