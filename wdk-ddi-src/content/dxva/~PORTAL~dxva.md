# Dxva.h header


This header is used by unknown technology.

Dxva.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [DXVA_AYUVsample2 structure](ns-dxva--dxva-ayuvsample2.md) | The DXVA_AYUVsample2 structure is sent by the host decoder to the accelerator to specify Y, Cb, Cr color values, and an associated opacity. |
| [DXVA_BlendCombination structure](ns-dxva--dxva-blendcombination.md) | The DXVA_BlendCombination structure is sent by the host decoder to the accelerator to specify how a blended picture is created from a source picture and a graphic image with accompanying alpha-blending information. |
| [DXVA_BufferDescription structure](ns-dxva--dxva-bufferdescription.md) | The DXVA_BufferDescription structure is sent by the host decoder to the accelerator to provide information to the accelerator about the buffer that is currently being passed from the host to the accelerator. |
| [DXVA_COPPCommand structure](ns-dxva--dxva-coppcommand.md) | The DXVA_COPPCommand structure describes a command sent to a protected video session that is associated with a COPP DirectX VA device. |
| [DXVA_COPPSetProtectionLevelCmdData structure](ns-dxva--dxva-coppsetprotectionlevelcmddata.md) | The DXVA_COPPSetProtectionLevelCmdData structure describes the protection types and levels to set on the physical connector associated with a COPP DirectX VA device. |
| [DXVA_COPPSetSignalingCmdData structure](ns-dxva--dxva-coppsetsignalingcmddata.md) | The DXVA_COPPSetSignalingCmdData structure describes how to protect the signal that goes through the physical connector associated with the DirectX VA COPP device. |
| [DXVA_COPPSignature structure](ns-dxva--dxva-coppsignature.md) | The DXVA_COPPSignature structure describes a sequence of items concatenated together that starts an active protected video session. |
| [DXVA_COPPStatusData structure](ns-dxva--dxva-coppstatusdata.md) | The DXVA_COPPStatusData structure contains the status information returned from a query on a protected video session that is associated with a DirectX VA COPP device. |
| [DXVA_COPPStatusDisplayData structure](ns-dxva--dxva-coppstatusdisplaydata.md) | The DXVA_COPPStatusDisplayData structure describes the display mode of the signal that is transmitted over the connector associated with a DirectX VA COPP device. |
| [DXVA_COPPStatusHDCPKeyData structure](ns-dxva--dxva-coppstatushdcpkeydata.md) | The DXVA_COPPStatusHDCPKeyData structure describes a High-bandwidth Digital Content Protection (HDCP) receiver or repeater key selection vector (KSV). |
| [DXVA_COPPStatusInput structure](ns-dxva--dxva-coppstatusinput.md) | The DXVA_COPPStatusInput structure describes a request for status on a protected video session that is associated with a DirectX VA COPP device. |
| [DXVA_COPPStatusOutput structure](ns-dxva--dxva-coppstatusoutput.md) | The DXVA_COPPStatusOutput structure describes the status returned from a query on a protected video session that is associated with a DirectX VA COPP device. |
| [DXVA_COPPStatusSignalingCmdData structure](ns-dxva--dxva-coppstatussignalingcmddata.md) | The DXVA_COPPStatusSignalingCmdData structure describes how the signal that goes through the physical connector associated with the DirectX VA COPP device is protected. |
| [DXVA_ConfigAlphaCombine structure](ns-dxva--dxva-configalphacombine.md) | The DXVA_ConfigAlphaCombine structure is sent by the host decoder to the accelerator to set the configuration for alpha-blending combination operations. |
| [DXVA_ConfigAlphaLoad structure](ns-dxva--dxva-configalphaload.md) | The DXVA_ConfigAlphaLoad structure is sent by the host decoder to the accelerator to set the configuration for alpha-blend, texture-loading operations. |
| [DXVA_ConfigPictureDecode structure](ns-dxva--dxva-configpicturedecode.md) | The DXVA_ConfigPictureDecode structure is sent by the host decoder to the accelerator to set the configuration for compressed picture decoding. |
| [DXVA_ConnectMode structure](ns-dxva--dxva-connectmode.md) | The DXVA_ConnectMode structure is sent by the host decoder to the accelerator to define the restricted profile used within a DirectX VA connection. |
| [DXVA_DeinterlaceBlt structure](ns-dxva--dxva-deinterlaceblt.md) | The DXVA_DeinterlaceBlt structure is sent by the VMR to the accelerator to specify the deinterlace or frame-rate conversion parameters for bit-block transfers. |
| [DXVA_DeinterlaceBltEx structure](ns-dxva--dxva-deinterlacebltex.md) | The DXVA_DeinterlaceBltEx structure describes parameters for deinterlace or frame-rate conversion, for combining the deinterlaced or frame-rate-converted video with any supplied video substreams, and for writing the combined output to a destination surface. |
| [DXVA_DeinterlaceBltEx32 structure](ns-dxva--dxva-deinterlacebltex32.md) | The DXVA_DeinterlaceBltEx structure describes parameters for deinterlace or frame-rate conversion, for combining the deinterlaced or frame-rate converted video with any supplied video substreams, and for writing the combined output to a destination surface. It is used for forwarding 32-bit DXVA_DeinterlaceBltEx calls on 64-bit drivers. |
| [DXVA_DeinterlaceCaps structure](ns-dxva--dxva-deinterlacecaps.md) | The DXVA_DeinterlaceCaps structure describes the driver capabilities for a deinterlace mode. |
| [DXVA_DeinterlaceQueryAvailableModes structure](ns-dxva--dxva-deinterlacequeryavailablemodes.md) | The DXVA_DeinterlaceQueryAvailableModes structure describes the available deinterlacing or frame-rate conversion modes for a particular input video format. |
| [DXVA_DeinterlaceQueryModeCaps structure](ns-dxva--dxva-deinterlacequerymodecaps.md) | The DXVA_DeinterlaceQueryModeCaps structure describes a deinterlacing mode. |
| [DXVA_EncryptProtocolHeader structure](ns-dxva--dxva-encryptprotocolheader.md) | The DXVA_EncryptProtocolHeader structure is sent by the host decoder to the accelerator to indicate use of an encryption protocol. |
| [DXVA_ExtendedFormat structure](ns-dxva--dxva-extendedformat.md) | The DXVA_ExtendedFormat structure describes the extended format of the video frame. |
| [DXVA_Frequency structure](ns-dxva--dxva-frequency.md) | The DXVA_Frequency structure is sent by the host decoder to the driver to specify the video frame rate, in Hz. For example, NTSC TV is 60000 over 1001. |
| [DXVA_Highlight structure](ns-dxva--dxva-highlight.md) | The DXVA_Highlight structure is sent by the host decoder to the accelerator to specify a highlighted rectangular area of a subpicture, and to create an alpha-blending surface with DCCMD data and a DPXD surface. |
| [DXVA_MBctrl_I_HostResidDiff_1 structure](ns-dxva--dxva-mbctrl-i-hostresiddiff-1.md) | The DXVA_MBctrl_I_HostResidDiff_1 structure is sent once per macroblock by the host decoder to the accelerator to specify macroblock control commands for an intra picture. |
| [DXVA_MBctrl_I_OffHostIDCT_1 structure](ns-dxva--dxva-mbctrl-i-offhostidct-1.md) | The DXVA_MBctrl_I_OffHostIDCT_1 structure is sent once per macroblock by the host decoder to the accelerator to specify macroblock control commands for 4 |
| [DXVA_MBctrl_P_HostResidDiff_1 structure](ns-dxva--dxva-mbctrl-p-hostresiddiff-1.md) | The DXVA_MBctrl_P_HostResidDiff_1 structure is sent once per macroblock by the host decoder to the accelerator to specify macroblock control commands for most nonintra picture cases when using host-based IDCT. |
| [DXVA_MBctrl_P_OffHostIDCT_1 structure](ns-dxva--dxva-mbctrl-p-offhostidct-1.md) | The DXVA_MBctrl_P_OffHostIDCT_1 structure is sent once per macroblock by the host decoder to the accelerator to specify macroblock control commands for most nonintra pictures using off-host IDCT. |
| [DXVA_MVvalue structure](ns-dxva--dxva-mvvalue.md) | The DXVA_MVvalue structure is sent by the host decoder to the accelerator to specify the two-dimensional motion vector value. |
| [DXVA_PicResample structure](ns-dxva--dxva-picresample.md) | The DXVA_PicResample structure is sent by the host decoder to the accelerator to control the resampling process. This process is invoked when the bDXVA_Func variable is equal to 4. |
| [DXVA_PictureParameters structure](ns-dxva--dxva-pictureparameters.md) | The DXVA_PictureParameters structure is sent by the host decoder to the accelerator to provide the picture-level parameters of a compressed picture for decoding on the accelerator. |
| [DXVA_ProcAmpControlBlt structure](ns-dxva--dxva-procampcontrolblt.md) | The DXVA_ProcAmpControlBlt structure contains the ProcAmp adjustment data that is output to the destination surface. |
| [DXVA_ProcAmpControlCaps structure](ns-dxva--dxva-procampcontrolcaps.md) | The DXVA_ProcAmpControlCaps structure identifies the ProcAmp operations that the hardware supports. |
| [DXVA_ProcAmpControlQueryRange structure](ns-dxva--dxva-procampcontrolqueryrange.md) | The DXVA_ProcAmpControlQueryRange structure contains the minimum, maximum, step size, and default value for each ProcAmp property. |
| [DXVA_QmatrixData structure](ns-dxva--dxva-qmatrixdata.md) | The DXVA_QmatrixData structure is sent by the host decoder to the accelerator to load inverse-quantization matrix data for off-host bitstream compressed video picture decoding. |
| [DXVA_SliceInfo structure](ns-dxva--dxva-sliceinfo.md) | The DXVA_SliceInfo structure is sent by the host decoder to the accelerator to specify the slice-level parameters of a slice of bitstream data for off-host bitstream compressed picture decoding. |
| [DXVA_TCoef4Group structure](ns-dxva--dxva-tcoef4group.md) | The DXVA_TCoef4Group structure is sent by the host decoder to the accelerator to specify the IDCT coefficient values. |
| [DXVA_TCoefSingle structure](ns-dxva--dxva-tcoefsingle.md) | The DXVA_TCoefSingle structure is sent by the host decoder to the accelerator to specify IDCT coefficient values. |
| [DXVA_VideoDesc structure](ns-dxva--dxva-videodesc.md) | The DXVA_VideoDesc structure is sent by the renderer to the driver to specify a description of the video stream on which the deinterlacing or frame-rate conversion operation is to be performed. |
| [DXVA_VideoPropertyRange structure](ns-dxva--dxva-videopropertyrange.md) | The DXVA_VideoPropertyRange structure specifies the range of allowed values for ProcAmp control properties. |
| [DXVA_VideoSample structure](ns-dxva--dxva-videosample.md) | The DXVA_VideoSample structure is sent by the renderer to the driver to specify the format of a video sample. |
| [DXVA_VideoSample2 structure](ns-dxva--dxva-videosample2.md) | The DXVA_VideoSample2 structure is sent by the renderer to the driver to specify the format of a video sample. |
| [DXVA_VideoSample32 structure](ns-dxva--dxva-videosample32.md) | The DXVA_VideoSample32 structure is used for forwarding 32-bit DXVA_DeinterlaceBltEx calls on 64-bit drivers. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [DXVA_DeinterlaceTech enumeration](ne-dxva--dxva-deinterlacetech.md) | The DXVA_DeinterlaceTech enumeration identifies the underlying technology used to implement a particular deinterlace algorithm. |
| [DXVA_DestinationFlags enumeration](ne-dxva--dxva-destinationflags.md) | The DXVA_DestinationFlags enumeration type contains a collection of flags that identify changes in the current destination surface from the previous destination surface. |
| [DXVA_NominalRange enumeration](ne-dxva--dxva-nominalrange.md) | The DXVA_NominalRange enumeration type contains enumerators that identify whether sample data includes headroom (values beyond 1.0 white) and toeroom (superblacks below the reference 0.0 black). |
| [DXVA_ProcAmpControlProp enumeration](ne-dxva--dxva-procampcontrolprop.md) | The DXVA_ProcAmpControlProp enumeration is used to determine the required ProcAmp control adjustments. |
| [DXVA_SampleFlags enumeration](ne-dxva--dxva-sampleflags.md) | The DXVA_SampleFlags enumeration type contains a collection of flags that identify changes in the current sample frame from the previous sample frame. |
| [DXVA_SampleFormat enumeration](ne-dxva--dxva-sampleformat.md) | The DXVA_SampleFormat enumeration type describes the format of data that the input sample contains. |
| [DXVA_VideoChromaSubsampling enumeration](ne-dxva--dxva-videochromasubsampling.md) | The DXVA_VideoChromaSubsampling enumeration type contains enumerators that identify the chroma encoding scheme for Y'Cb'Cr' data. |
| [DXVA_VideoLighting enumeration](ne-dxva--dxva-videolighting.md) | The DXVA_VideoLighting enumeration type contains enumerators that identify lighting conditions for viewing video. |
| [DXVA_VideoPrimaries enumeration](ne-dxva--dxva-videoprimaries.md) | The DXVA_VideoPrimaries enumeration type contains enumerators that identify the color primaries, which state which RGB basis functions are used. |
| [DXVA_VideoProcessCaps enumeration](ne-dxva--dxva-videoprocesscaps.md) | The DXVA_VideoProcessCaps enumeration identifies operations that can be performed concurrently with the requested deinterlace. |
| [DXVA_VideoTransferFunction enumeration](ne-dxva--dxva-videotransferfunction.md) | The DXVA_VideoTransferFunction enumeration type contains enumerators that identify the conversion function from R'G'B' to RGB. |
| [DXVA_VideoTransferMatrix enumeration](ne-dxva--dxva-videotransfermatrix.md) | The DXVA_VideoTransferMatrix enumeration type contains enumerators that identify the conversion matrix from Y'Cb'Cr' to R'G'B'. |
