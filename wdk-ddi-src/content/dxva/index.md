---
UID : NA:dxva
ms.assetid : 250929b4-1810-3b6a-a9b5-69d10f2643a0
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# dxva.h header



dxva.h contains the following programming interfaces:







## Structures
| Title | Description |
| ---- |:---- |
| [_DXVA_AYUVsample2](ns-dxva-_dxva_ayuvsample2.md) | The DXVA_AYUVsample2 structure is sent by the host decoder to the accelerator to specify Y, Cb, Cr color values, and an associated opacity. |
| [_DXVA_BlendCombination](ns-dxva-_dxva_blendcombination.md) | The DXVA_BlendCombination structure is sent by the host decoder to the accelerator to specify how a blended picture is created from a source picture and a graphic image with accompanying alpha-blending information. |
| [_DXVA_BufferDescription](ns-dxva-_dxva_bufferdescription.md) | The DXVA_BufferDescription structure is sent by the host decoder to the accelerator to provide information to the accelerator about the buffer that is currently being passed from the host to the accelerator. |
| [_DXVA_ConfigAlphaCombine](ns-dxva-_dxva_configalphacombine.md) | The DXVA_ConfigAlphaCombine structure is sent by the host decoder to the accelerator to set the configuration for alpha-blending combination operations. |
| [_DXVA_ConfigAlphaLoad](ns-dxva-_dxva_configalphaload.md) | The DXVA_ConfigAlphaLoad structure is sent by the host decoder to the accelerator to set the configuration for alpha-blend, texture-loading operations. |
| [_DXVA_ConfigPictureDecode](ns-dxva-_dxva_configpicturedecode.md) | The DXVA_ConfigPictureDecode structure is sent by the host decoder to the accelerator to set the configuration for compressed picture decoding. |
| [_DXVA_ConnectMode](ns-dxva-_dxva_connectmode.md) | The DXVA_ConnectMode structure is sent by the host decoder to the accelerator to define the restricted profile used within a DirectX VA connection. |
| [_DXVA_COPPCommand](ns-dxva-_dxva_coppcommand.md) | The DXVA_COPPCommand structure describes a command sent to a protected video session that is associated with a COPP DirectX VA device. |
| [_DXVA_COPPSetProtectionLevelCmdData](ns-dxva-_dxva_coppsetprotectionlevelcmddata.md) | The DXVA_COPPSetProtectionLevelCmdData structure describes the protection types and levels to set on the physical connector associated with a COPP DirectX VA device. |
| [_DXVA_COPPSetSignalingCmdData](ns-dxva-_dxva_coppsetsignalingcmddata.md) | The DXVA_COPPSetSignalingCmdData structure describes how to protect the signal that goes through the physical connector associated with the DirectX VA COPP device. |
| [_DXVA_COPPSignature](ns-dxva-_dxva_coppsignature.md) | The DXVA_COPPSignature structure describes a sequence of items concatenated together that starts an active protected video session. |
| [_DXVA_COPPStatusData](ns-dxva-_dxva_coppstatusdata.md) | The DXVA_COPPStatusData structure contains the status information returned from a query on a protected video session that is associated with a DirectX VA COPP device. |
| [_DXVA_COPPStatusDisplayData](ns-dxva-_dxva_coppstatusdisplaydata.md) | The DXVA_COPPStatusDisplayData structure describes the display mode of the signal that is transmitted over the connector associated with a DirectX VA COPP device. |
| [_DXVA_COPPStatusHDCPKeyData](ns-dxva-_dxva_coppstatushdcpkeydata.md) | The DXVA_COPPStatusHDCPKeyData structure describes a High-bandwidth Digital Content Protection (HDCP) receiver or repeater key selection vector (KSV). |
| [_DXVA_COPPStatusInput](ns-dxva-_dxva_coppstatusinput.md) | The DXVA_COPPStatusInput structure describes a request for status on a protected video session that is associated with a DirectX VA COPP device. |
| [_DXVA_COPPStatusOutput](ns-dxva-_dxva_coppstatusoutput.md) | The DXVA_COPPStatusOutput structure describes the status returned from a query on a protected video session that is associated with a DirectX VA COPP device. |
| [_DXVA_COPPStatusSignalingCmdData](ns-dxva-_dxva_coppstatussignalingcmddata.md) | The DXVA_COPPStatusSignalingCmdData structure describes how the signal that goes through the physical connector associated with the DirectX VA COPP device is protected. |
| [_DXVA_DeinterlaceBlt](ns-dxva-_dxva_deinterlaceblt.md) | The DXVA_DeinterlaceBlt structure is sent by the VMR to the accelerator to specify the deinterlace or frame-rate conversion parameters for bit-block transfers. |
| [_DXVA_DeinterlaceBltEx](ns-dxva-_dxva_deinterlacebltex.md) | The DXVA_DeinterlaceBltEx structure describes parameters for deinterlace or frame-rate conversion, for combining the deinterlaced or frame-rate-converted video with any supplied video substreams, and for writing the combined output to a destination surface. |
| [_DXVA_DeinterlaceBltEx32](ns-dxva-_dxva_deinterlacebltex32.md) | The DXVA_DeinterlaceBltEx structure describes parameters for deinterlace or frame-rate conversion, for combining the deinterlaced or frame-rate converted video with any supplied video substreams, and for writing the combined output to a destination surface. It is used for forwarding 32-bit DXVA_DeinterlaceBltEx calls on 64-bit drivers. |
| [_DXVA_DeinterlaceCaps](ns-dxva-_dxva_deinterlacecaps.md) | The DXVA_DeinterlaceCaps structure describes the driver capabilities for a deinterlace mode. |
| [_DXVA_DeinterlaceQueryAvailableModes](ns-dxva-_dxva_deinterlacequeryavailablemodes.md) | The DXVA_DeinterlaceQueryAvailableModes structure describes the available deinterlacing or frame-rate conversion modes for a particular input video format. |
| [_DXVA_DeinterlaceQueryModeCaps](ns-dxva-_dxva_deinterlacequerymodecaps.md) | The DXVA_DeinterlaceQueryModeCaps structure describes a deinterlacing mode. |
| [_DXVA_EncryptProtocolHeader](ns-dxva-_dxva_encryptprotocolheader.md) | The DXVA_EncryptProtocolHeader structure is sent by the host decoder to the accelerator to indicate use of an encryption protocol. |
| [_DXVA_ExtendedFormat](ns-dxva-_dxva_extendedformat.md) | The DXVA_ExtendedFormat structure describes the extended format of the video frame. |
| [_DXVA_Frequency](ns-dxva-_dxva_frequency.md) | The DXVA_Frequency structure is sent by the host decoder to the driver to specify the video frame rate, in Hz. For example, NTSC TV is 60000 over 1001. |
| [_DXVA_Highlight](ns-dxva-_dxva_highlight.md) | The DXVA_Highlight structure is sent by the host decoder to the accelerator to specify a highlighted rectangular area of a subpicture, and to create an alpha-blending surface with DCCMD data and a DPXD surface. |
| [_DXVA_MBctrl_I_HostResidDiff_1](ns-dxva-_dxva_mbctrl_i_hostresiddiff_1.md) | The DXVA_MBctrl_I_HostResidDiff_1 structure is sent once per macroblock by the host decoder to the accelerator to specify macroblock control commands for an intra picture. |
| [_DXVA_MBctrl_I_OffHostIDCT_1](ns-dxva-_dxva_mbctrl_i_offhostidct_1.md) | The DXVA_MBctrl_I_OffHostIDCT_1 structure is sent once per macroblock by the host decoder to the accelerator to specify macroblock control commands for 4:2:0 intra pictures when using off-host IDCT. |
| [_DXVA_MBctrl_P_HostResidDiff_1](ns-dxva-_dxva_mbctrl_p_hostresiddiff_1.md) | The DXVA_MBctrl_P_HostResidDiff_1 structure is sent once per macroblock by the host decoder to the accelerator to specify macroblock control commands for most nonintra picture cases when using host-based IDCT. |
| [_DXVA_MBctrl_P_OffHostIDCT_1](ns-dxva-_dxva_mbctrl_p_offhostidct_1.md) | The DXVA_MBctrl_P_OffHostIDCT_1 structure is sent once per macroblock by the host decoder to the accelerator to specify macroblock control commands for most nonintra pictures using off-host IDCT. |
| [_DXVA_MVvalue](ns-dxva-_dxva_mvvalue.md) | The DXVA_MVvalue structure is sent by the host decoder to the accelerator to specify the two-dimensional motion vector value. |
| [_DXVA_PicResample](ns-dxva-_dxva_picresample.md) | The DXVA_PicResample structure is sent by the host decoder to the accelerator to control the resampling process. This process is invoked when the bDXVA_Func variable is equal to 4. |
| [_DXVA_PictureParameters](ns-dxva-_dxva_pictureparameters.md) | The DXVA_PictureParameters structure is sent by the host decoder to the accelerator to provide the picture-level parameters of a compressed picture for decoding on the accelerator. |
| [_DXVA_ProcAmpControlBlt](ns-dxva-_dxva_procampcontrolblt.md) | The DXVA_ProcAmpControlBlt structure contains the ProcAmp adjustment data that is output to the destination surface. |
| [_DXVA_ProcAmpControlCaps](ns-dxva-_dxva_procampcontrolcaps.md) | The DXVA_ProcAmpControlCaps structure identifies the ProcAmp operations that the hardware supports. |
| [_DXVA_ProcAmpControlQueryRange](ns-dxva-_dxva_procampcontrolqueryrange.md) | The DXVA_ProcAmpControlQueryRange structure contains the minimum, maximum, step size, and default value for each ProcAmp property. |
| [_DXVA_QmatrixData](ns-dxva-_dxva_qmatrixdata.md) | The DXVA_QmatrixData structure is sent by the host decoder to the accelerator to load inverse-quantization matrix data for off-host bitstream compressed video picture decoding. |
| [_DXVA_SliceInfo](ns-dxva-_dxva_sliceinfo.md) | The DXVA_SliceInfo structure is sent by the host decoder to the accelerator to specify the slice-level parameters of a slice of bitstream data for off-host bitstream compressed picture decoding. |
| [_DXVA_TCoef4Group](ns-dxva-_dxva_tcoef4group.md) | The DXVA_TCoef4Group structure is sent by the host decoder to the accelerator to specify the IDCT coefficient values. |
| [_DXVA_TCoefSingle](ns-dxva-_dxva_tcoefsingle.md) | The DXVA_TCoefSingle structure is sent by the host decoder to the accelerator to specify IDCT coefficient values. |
| [_DXVA_VideoDesc](ns-dxva-_dxva_videodesc.md) | The DXVA_VideoDesc structure is sent by the renderer to the driver to specify a description of the video stream on which the deinterlacing or frame-rate conversion operation is to be performed. |
| [_DXVA_VideoPropertyRange](ns-dxva-_dxva_videopropertyrange.md) | The DXVA_VideoPropertyRange structure specifies the range of allowed values for ProcAmp control properties. |
| [_DXVA_VideoSample](ns-dxva-_dxva_videosample.md) | The DXVA_VideoSample structure is sent by the renderer to the driver to specify the format of a video sample. |
| [_DXVA_VideoSample2](ns-dxva-_dxva_videosample2.md) | The DXVA_VideoSample2 structure is sent by the renderer to the driver to specify the format of a video sample. |
| [_DXVA_VideoSample32](ns-dxva-_dxva_videosample32.md) | The DXVA_VideoSample32 structure is used for forwarding 32-bit DXVA_DeinterlaceBltEx calls on 64-bit drivers. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_DXVA_DeinterlaceTech](ne-dxva-_dxva_deinterlacetech.md) | The DXVA_DeinterlaceTech enumeration identifies the underlying technology used to implement a particular deinterlace algorithm. |
| [_DXVA_DestinationFlags](ne-dxva-_dxva_destinationflags.md) | The DXVA_DestinationFlags enumeration type contains a collection of flags that identify changes in the current destination surface from the previous destination surface. |
| [_DXVA_NominalRange](ne-dxva-_dxva_nominalrange.md) | The DXVA_NominalRange enumeration type contains enumerators that identify whether sample data includes headroom (values beyond 1.0 white) and toeroom (superblacks below the reference 0.0 black). |
| [_DXVA_ProcAmpControlProp](ne-dxva-_dxva_procampcontrolprop.md) | The DXVA_ProcAmpControlProp enumeration is used to determine the required ProcAmp control adjustments. |
| [_DXVA_SampleFlags](ne-dxva-_dxva_sampleflags.md) | The DXVA_SampleFlags enumeration type contains a collection of flags that identify changes in the current sample frame from the previous sample frame. |
| [_DXVA_SampleFormat](ne-dxva-_dxva_sampleformat.md) | The DXVA_SampleFormat enumeration type describes the format of data that the input sample contains. |
| [_DXVA_VideoChromaSubsampling](ne-dxva-_dxva_videochromasubsampling.md) | The DXVA_VideoChromaSubsampling enumeration type contains enumerators that identify the chroma encoding scheme for Y'Cb'Cr' data. |
| [_DXVA_VideoLighting](ne-dxva-_dxva_videolighting.md) | The DXVA_VideoLighting enumeration type contains enumerators that identify lighting conditions for viewing video. |
| [_DXVA_VideoPrimaries](ne-dxva-_dxva_videoprimaries.md) | The DXVA_VideoPrimaries enumeration type contains enumerators that identify the color primaries, which state which RGB basis functions are used. |
| [_DXVA_VideoProcessCaps](ne-dxva-_dxva_videoprocesscaps.md) | The DXVA_VideoProcessCaps enumeration identifies operations that can be performed concurrently with the requested deinterlace. |
| [_DXVA_VideoTransferFunction](ne-dxva-_dxva_videotransferfunction.md) | The DXVA_VideoTransferFunction enumeration type contains enumerators that identify the conversion function from R'G'B' to RGB. |
| [_DXVA_VideoTransferMatrix](ne-dxva-_dxva_videotransfermatrix.md) | The DXVA_VideoTransferMatrix enumeration type contains enumerators that identify the conversion matrix from Y'Cb'Cr' to R'G'B'. |