---
UID: NS.d3d10umddi.D3DWDDM2_0DDI_VIDEODEVICEFUNCS
title: D3DWDDM2_0DDI_VIDEODEVICEFUNCS
author: windows-driver-content
description: Specifies the video function table for the Microsoft Direct3D driver device object. Used only by Windows Display Driver Model (WDDM) 2.0 and later drivers.
old-location: display\d3dwddm2_0ddi_videodevicefuncs.htm
old-project: display
ms.assetid: 59D06B73-413B-4595-841E-7E0A696A3AC2
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_0DDI_VIDEODEVICEFUNCS, D3DWDDM2_0DDI_VIDEODEVICEFUNCS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DWDDM2_0DDI_VIDEODEVICEFUNCS
req.alt-loc: D3d10umddi.h
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

# D3DWDDM2_0DDI_VIDEODEVICEFUNCS structure



## -description
<p>Specifies the video function table for the  Microsoft Direct3D driver device object. Used only by Windows Display Driver Model (WDDM) 2.0 and later drivers.</p>


## -syntax

````
typedef struct D3DWDDM2_0DDI_VIDEODEVICEFUNCS {
  PFND3D11_1DDI_GETVIDEODECODERPROFILECOUNT                  pfnGetVideoDecoderProfileCount;
  PFND3D11_1DDI_GETVIDEODECODERPROFILE                       pfnGetVideoDecoderProfile;
  PFND3D11_1DDI_CHECKVIDEODECODERFORMAT                      pfnCheckVideoDecoderFormat;
  PFND3D11_1DDI_GETVIDEODECODERCONFIGCOUNT                   pfnGetVideoDecoderConfigCount;
  PFND3D11_1DDI_GETVIDEODECODERCONFIG                        pfnGetVideoDecoderConfig;
  PFND3D11_1DDI_GETVIDEODECODERBUFFERTYPECOUNT               pfnGetVideoDecoderBufferTypeCount;
  PFND3D11_1DDI_GETVIDEODECODERBUFFERINFO                    pfnGetVideoDecoderBufferInfo;
  PFND3D11_1DDI_CALCPRIVATEVIDEODECODERSIZE                  pfnCalcPrivateVideoDecoderSize;
  PFND3D11_1DDI_CREATEVIDEODECODER                           pfnCreateVideoDecoder;
  PFND3D11_1DDI_DESTROYVIDEODECODER                          pfnDestroyVideoDecoder;
  PFND3D11_1DDI_VIDEODECODEREXTENSION                        pfnVideoDecoderExtension;
  PFND3D11_1DDI_VIDEODECODERBEGINFRAME                       pfnVideoDecoderBeginFrame;
  PFND3D11_1DDI_VIDEODECODERENDFRAME                         pfnVideoDecoderEndFrame;
  PFND3D11_1DDI_VIDEODECODERSUBMITBUFFERS                    pfnVideoDecoderSubmitBuffers;
  PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORENUMSIZE            pfnCalcPrivateVideoProcessorEnumSize;
  PFND3D11_1DDI_CREATEVIDEOPROCESSORENUM                     pfnCreateVideoProcessorEnum;
  PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM                    pfnDestroyVideoProcessorEnum;
  PFND3D11_1DDI_CHECKVIDEOPROCESSORFORMAT                    pfnCheckVideoProcessorFormat;
  PFND3D11_1DDI_GETVIDEOPROCESSORCAPS                        pfnGetVideoProcessorCaps;
  PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS          pfnGetVideoProcessorRateConversionCaps;
  PFND3D11_1DDI_GETVIDEOPROCESSORCUSTOMRATE                  pfnGetVideoProcessorCustomRate;
  PFND3D11_1DDI_GETVIDEOPROCESSORFILTERRANGE                 pfnGetVideoProcessorFilterRange;
  PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORSIZE                pfnCalcPrivateVideoProcessorSize;
  PFND3D11_1DDI_CREATEVIDEOPROCESSOR                         pfnCreateVideoProcessor;
  PFND3D11_1DDI_DESTROYVIDEOPROCESSOR                        pfnDestroyVideoProcessor;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTTARGETRECT            pfnVideoProcessorSetOutputTargetRect;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTBACKGROUNDCOLOR       pfnVideoProcessorSetOutputBackgroundColor;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCOLORSPACE            pfnVideoProcessorSetOutputColorSpace;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE         pfnVideoProcessorSetOutputAlphaFillMode;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCONSTRICTION          pfnVideoProcessorSetOutputConstriction;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTSTEREOMODE            pfnVideoProcessorSetOutputStereoMode;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTEXTENSION             pfnVideoProcessorSetOutputExtension;
  PFND3D11_1DDI_VIDEOPROCESSORGETOUTPUTEXTENSION             pfnVideoProcessorGetOutputExtension;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMFRAMEFORMAT           pfnVideoProcessorSetStreamFrameFormat;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMCOLORSPACE            pfnVideoProcessorSetStreamColorSpace;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMOUTPUTRATE            pfnVideoProcessorSetStreamOutputRate;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSOURCERECT            pfnVideoProcessorSetStreamSourceRect;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMDESTRECT              pfnVideoProcessorSetStreamDestRect;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMALPHA                 pfnVideoProcessorSetStreamAlpha;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPALETTE               pfnVideoProcessorSetStreamPalette;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPIXELASPECTRATIO      pfnVideoProcessorSetStreamPixelAspectRatio;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMLUMAKEY               pfnVideoProcessorSetStreamLumaKey;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSTEREOFORMAT          pfnVideoProcessorSetStreamStereoFormat;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMAUTOPROCESSINGMODE    pfnVideoProcessorSetStreamAutoProcessingMode;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMFILTER                pfnVideoProcessorSetStreamFilter;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMEXTENSION             pfnVideoProcessorSetStreamExtension;
  PFND3D11_1DDI_VIDEOPROCESSORGETSTREAMEXTENSION             pfnVideoProcessorGetStreamExtension;
  PFND3D11_1DDI_VIDEOPROCESSORBLT                            pfnVideoProcessorBlt;
  PFND3D11_1DDI_CALCPRIVATEVIDEODECODEROUTPUTVIEWSIZE        pfnCalcPrivateVideoDecoderOutputViewSize;
  PFND3D11_1DDI_CREATEVIDEODECODEROUTPUTVIEW                 pfnCreateVideoDecoderOutputView;
  PFND3D11_1DDI_DESTROYVIDEODECODEROUTPUTVIEW                pfnDestroyVideoDecoderOutputView;
  PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORINPUTVIEWSIZE       pfnCalcPrivateVideoProcessorInputViewSize;
  PFND3D11_1DDI_CREATEVIDEOPROCESSORINPUTVIEW                pfnCreateVideoProcessorInputView;
  PFND3D11_1DDI_DESTROYVIDEOPROCESSORINPUTVIEW               pfnDestroyVideoProcessorInputView;
  PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSOROUTPUTVIEWSIZE      pfnCalcPrivateVideoProcessorOutputViewSize;
  PFND3D11_1DDI_CREATEVIDEOPROCESSOROUTPUTVIEW               pfnCreateVideoProcessorOutputView;
  PFND3D11_1DDI_DESTROYVIDEOPROCESSOROUTPUTVIEW              pfnDestroyVideoProcessorOutputView;
  PFND3D11_1DDI_VIDEOPROCESSORINPUTVIEWREADAFTERWRITEHAZARD  pfnVideoProcessorInputViewReadAfterWriteHazard;
  PFND3D11_1DDI_GETCONTENTPROTECTIONCAPS                     pfnGetContentProtectionCaps;
  PFND3D11_1DDI_GETCRYPTOKEYEXCHANGETYPE                     pfnGetCryptoKeyExchangeType;
  PFND3D11_1DDI_CALCPRIVATECRYPTOSESSIONSIZE                 pfnCalcPrivateCryptoSessionSize;
  PFND3D11_1DDI_CREATECRYPTOSESSION                          pfnCreateCryptoSession;
  PFND3D11_1DDI_DESTROYCRYPTOSESSION                         pfnDestroyCryptoSession;
  PFND3D11_1DDI_GETCERTIFICATESIZE                           pfnGetCertificateSize;
  PFND3D11_1DDI_GETCERTIFICATE                               pfnGetCertificate;
  PFND3D11_1DDI_NEGOTIATECRYPTOSESSIONKEYESCHANGE            pfnNegotiateCryptoSessionKeyExchange;
  PFND3D11_1DDI_ENCRYPTIONBLT                                pfnEncryptionBlt;
  PFND3D11_1DDI_DECRYPTIONBLT                                pfnDecryptionBlt;
  PFND3D11_1DDI_STARTSESSIONKEYREFRESH                       pfnStartSessionKeyRefresh;
  PFND3D11_1DDI_FINISHSESSIONKEYREFRESH                      pfnFinishSessionKeyRefresh;
  PFND3D11_1DDI_GETENCRYPTIONBLTKEY                          pfnGetEncryptionBltKey;
  PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE          pfnCalcPrivateAuthenticatedChannelSize;
  PFND3D11_1DDI_CREATEAUTHENTICATEDCHANNEL                   pfnCreateAuthenticatedChannel;
  PFND3D11_1DDI_DESTROYAUTHENTICATEDCHANNEL                  pfnDestroyAuthenticatedChannel;
  PFND3D11_1DDI_NEGOTIATEAUTHENTICATEDCHANNELKEYEXCHANGE     pfnNegotiateAuthenticatedChannelKeyExchange;
  PFND3D11_1DDI_QUERYAUTHENTICATEDCHANNEL                    pfnQueryAuthenticatedChannel;
  PFND3D11_1DDI_CONFIGUREAUTHENTICATEDCHANNEL                pfnConfigureAuthenticatedChannel;
  PFND3D11_1DDI_VIDEODECODERGETHANDLE                        pfnVideoDecoderGetHandle;
  PFND3D11_1DDI_CRYPTOSESSIONGETHANDLE                       pfnCryptoSessionGetHandle;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMROTATION              pfnVideoProcessorSetStreamRotation;
  PFND3D11_1DDI_GETCAPTUREHANDLE                             pfnGetCaptureHandle;
  PFND3DWDDM2_0DDI_GETDATAFORNEWHARDWAREKEY                  pfnGetDataForNewHardwareKey;
  PFND3DWDDM2_0DDI_CHECKCRYPTOSESSIONSTATUS                  pfnCheckCryptoSessionStatus;
  PFND3DWDDM2_0DDI_VIDEODECODERSUBMITBUFFERS1                pfnVideoDecoderSubmitBuffers1;
  PFND3DWDDM2_0DDI_QUERYVIDEOCAPABILITIES                    pfnQueryVideoCapabilities;
  PFND3DWDDM2_0DDI_CHECKVIDEOPROCESSORFORMATCONVERSION       pfnCheckVideoProcessorFormatConversion;
  PFND3DWDDM2_0DDI_VIDEODECODERENABLEDOWNSAMPLING            pfnVideoDecoderEnableDownsampling;
  PFND3DWDDM2_0DDI_VIDEODECODERUPDATEDOWNSAMPLING            pfnVideoDecoderUpdateDownsampling;
  PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMMIRROR             pfnVideoProcessorSetStreamMirror;
  PFND3DWDDM2_0DDI_VIDEOPROCESSORSETOUTPUTCOLORSPACE1        pfnVideoProcessorSetOutputColorSpace1;
  PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMCOLORSPACE1        pfnVideoProcessorSetStreamColorSpace1;
  PFND3DWDDM2_0DDI_VIDEOPROCESSORSETOUTPUTSHADERUSAGE        pfnVideoProcessorSetOutputShaderUsage;
  PFND3DWDDM2_0DDI_VIDEOPROCESSORGETBEHAVIORHINTS            pfnVideoProcessorGetBehaviorHints;
  PFND3DWDDM2_0DDI_GETCRYPTOSESSIONPRIVATEDATASIZE           pfnGetCryptoSessionPrivateDataSize        ;
} D3DWDDM2_0DDI_VIDEODEVICEFUNCS;
````


## -struct-fields
<dl>

### -field <b>pfnGetVideoDecoderProfileCount</b>

<dd>
<p>The entry point for the driver's <a href="display.getvideodecoderprofilecount">VideoDecoderProfileCount</a> function.</p>
</dd>

### -field <b>pfnGetVideoDecoderProfile</b>

<dd>
<p>The entry point for the driver's <a href="display.getvideodecoderprofile">VideoDecoderProfile</a> function.</p>
</dd>

### -field <b>pfnCheckVideoDecoderFormat</b>

<dd>
<p>The entry point for the driver's <a href="display.checkvideodecoderformat">CheckVideoDecoderFormat</a> function.</p>
</dd>

### -field <b>pfnGetVideoDecoderConfigCount</b>

<dd>
<p>The entry point for the driver's <a href="display.getvideodecoderconfigcount">GetVideoDecoderConfig</a> function.</p>
</dd>

### -field <b>pfnGetVideoDecoderConfig</b>

<dd>
<p>The entry point for the driver's <a href="display.getvideodecoderconfig">GetVideoDecoderConfig</a> function.</p>
</dd>

### -field <b>pfnGetVideoDecoderBufferTypeCount</b>

<dd>
<p>The entry point for the driver's <a href="display.getvideodecoderbuffertypecount">GetVideoDecoderBufferTypeCount</a> function.</p>
</dd>

### -field <b>pfnGetVideoDecoderBufferInfo</b>

<dd>
<p>The entry point for the driver's <a href="display.getvideodecoderbufferinfo">GetVideoDecoderBufferInfo</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateVideoDecoderSize</b>

<dd>
<p>The entry point for the driver's <a href="display.calcprivatevideodecodersize">CalcPrivateVideoDecoderSize</a> function.</p>
</dd>

### -field <b>pfnCreateVideoDecoder</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createvideodecoder.md">CreateVideoDecoder</a> function.</p>
</dd>

### -field <b>pfnDestroyVideoDecoder</b>

<dd>
<p>The entry point for the driver's <a href="display.destroyvideodecoder">DestroyVideoDecoder</a> function.</p>
</dd>

### -field <b>pfnVideoDecoderExtension</b>

<dd>
<p>The entry point for the driver's <a href="display.videodecoderextension">VideoDecoderExtension</a> function.</p>
</dd>

### -field <b>pfnVideoDecoderBeginFrame</b>

<dd>
<p>The entry point for the driver's <a href="display.videodecoderbeginframe">VideoDecoderBeginFrame</a> function.</p>
</dd>

### -field <b>pfnVideoDecoderEndFrame</b>

<dd>
<p>The entry point for the driver's <a href="display.videodecoderendframe">VideoDecoderEndFrame</a> function.</p>
</dd>

### -field <b>pfnVideoDecoderSubmitBuffers</b>

<dd>
<p>The entry point for the driver's <a href="display.videodecodersubmitbuffers">VideoDecoderSubmitBuffers</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateVideoProcessorEnumSize</b>

<dd>
<p>The entry point for the driver's <a href="display.calcprivatevideoprocessorenumsize">CalcPrivateVideoProcessorEnumSize</a> function.</p>
</dd>

### -field <b>pfnCreateVideoProcessorEnum</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createvideoprocessorenum.md">CreateVideoProcessorEnum</a> function.</p>
</dd>

### -field <b>pfnDestroyVideoProcessorEnum</b>

<dd>
<p>The entry point for the driver's <a href="display.destroyvideoprocessorenum">DestroyVideoProcessorEnum</a> function.</p>
</dd>

### -field <b>pfnCheckVideoProcessorFormat</b>

<dd>
<p>The entry point for the driver's <a href="display.checkvideoprocessorformat">CheckVideoProcessorFormat</a> function.</p>
</dd>

### -field <b>pfnGetVideoProcessorCaps</b>

<dd>
<p>The entry point for the driver's <a href="display.getvideoprocessorcaps">GetVideoProcessorCaps</a> function.</p>
</dd>

### -field <b>pfnGetVideoProcessorRateConversionCaps</b>

<dd>
<p>The entry point for the driver's <a href="display.getvideoprocessorrateconversioncaps">GetVideoProcessorRateConversionCaps</a> function.</p>
</dd>

### -field <b>pfnGetVideoProcessorCustomRate</b>

<dd>
<p>The entry point for the driver's <a href="display.getvideoprocessorcustomrate">GetVideoProcessorCustomRate</a> function.</p>
</dd>

### -field <b>pfnGetVideoProcessorFilterRange</b>

<dd>
<p>The entry point for the driver's <a href="display.getvideoprocessorfilterrange">GetVideoProcessorFilterRange</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateVideoProcessorSize</b>

<dd>
<p>The entry point for the driver's <a href="display.calcprivatevideoprocessorsize">CalcPrivateVideoProcessorSize</a> function.</p>
</dd>

### -field <b>pfnCreateVideoProcessor</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createvideoprocessor.md">CreateVideoProcessor</a> function.</p>
</dd>

### -field <b>pfnDestroyVideoProcessor</b>

<dd>
<p>The entry point for the driver's <a href="display.destroyvideoprocessor1">DestroyVideoProcessor</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetOutputTargetRect</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetoutputtargetrect">VideoProcessorSetOutputTargetRect</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetOutputBackgroundColor</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetoutputbackgroundcolor">VideoProcessorSetOutputBackgroundColor</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetOutputColorSpace</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetoutputcolorspace">VideoProcessorSetOutputColorSpace</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetOutputAlphaFillMode</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetoutputalphafillmode">VideoProcessorSetOutputAlphaFillMode</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetOutputConstriction</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetoutputconstriction">VideoProcessorSetOutputConstriction</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetOutputStereoMode</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetoutputstereomode">VideoProcessorSetOutputStereoMode</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetOutputExtension</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetoutputextension">VideoProcessorSetOutputExtension</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorGetOutputExtension</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorgetoutputextension">VideoProcessorGetOutputExtension</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamFrameFormat</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetstreamframeformat">VideoProcessorSetStreamFrameFormat</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamColorSpace</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetstreamcolorspace">VideoProcessorSetStreamColorSpace</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamOutputRate</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetstreamoutputrate">VideoProcessorSetStreamOutputRate</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamSourceRect</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetstreamsourcerect">VideoProcessorSetStreamSourceRect</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamDestRect</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetstreamdestrect">VideoProcessorSetStreamDestRect</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamAlpha</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetstreamalpha">VideoProcessorSetStreamAlpha</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamPalette</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetstreampalette">VideoProcessorSetStreamPalette</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamPixelAspectRatio</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetstreampixelaspectratio">VideoProcessorSetStreamPixelAspectRatio</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamLumaKey</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetstreamlumakey">VideoProcessorSetStreamLumaKey</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamStereoFormat</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetstreamstereoformat">VideoProcessorSetStreamStereoFormat</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamAutoProcessingMode</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetstreamautoprocessingmode">VideoProcessorSetStreamAutoProcessingMode</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamFilter</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetstreamfilter">VideoProcessorSetStreamFilter</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamExtension</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetstreamextension">VideoProcessorSetStreamExtension</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorGetStreamExtension</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorgetstreamextension">VideoProcessorGetStreamExtension</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorBlt</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorblt">VideoProcessorBlt</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateVideoDecoderOutputViewSize</b>

<dd>
<p>The entry point for the driver's <a href="display.calcprivatevideodecoderoutputviewsize">CalcPrivateVideoDecoderOutputViewSize</a> function.</p>
</dd>

### -field <b>pfnCreateVideoDecoderOutputView</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createvideodecoderoutputview.md">CreateVideoDecoderOutputView</a> function.</p>
</dd>

### -field <b>pfnDestroyVideoDecoderOutputView</b>

<dd>
<p>The entry point for the driver's <a href="display.destroyvideodecoderoutputview">DestroyVideoDecoderOutputView</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateVideoProcessorInputViewSize</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-calcprivatevideoprocessorinputviewsize.md">CalcPrivateVideoProcessorInputViewSize</a> function.</p>
</dd>

### -field <b>pfnCreateVideoProcessorInputView</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createvideoprocessorinputview.md">CreateVideoProcessorInputView</a> function.</p>
</dd>

### -field <b>pfnDestroyVideoProcessorInputView</b>

<dd>
<p>The entry point for the driver's <a href="display.destroyvideoprocessorinputview">DestroyVideoProcessorInputView</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateVideoProcessorOutputViewSize</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-calcprivatevideoprocessoroutputviewsize.md">CalcPrivateVideoProcessorOutputViewSize</a> function.</p>
</dd>

### -field <b>pfnCreateVideoProcessorOutputView</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createvideoprocessoroutputview.md">CreateVideoProcessorOutputView</a> function.</p>
</dd>

### -field <b>pfnDestroyVideoProcessorOutputView</b>

<dd>
<p>The entry point for the driver's <a href="display.destroyvideoprocessoroutputview">DestroyVideoProcessorOutputView</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorInputViewReadAfterWriteHazard</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorinputviewreadafterwritehazard">VideoProcessorInputViewReadAfterWriteHazard</a> function.</p>
</dd>

### -field <b>pfnGetContentProtectionCaps</b>

<dd>
<p>The entry point for the driver's <a href="display.getcontentprotectioncaps">GetContentProtectionCaps</a> function.</p>
</dd>

### -field <b>pfnGetCryptoKeyExchangeType</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-getcryptokeyexchangetype.md">GetCryptoKeyExchangeType</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateCryptoSessionSize</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-calcprivatecryptosessionsize.md">CalcPrivateCryptoSessionSize</a> function.</p>
</dd>

### -field <b>pfnCreateCryptoSession</b>

<dd>
<p>The entry point for the driver's <a href="display.createcryptosession1">CreateCryptoSession</a> function.</p>
</dd>

### -field <b>pfnDestroyCryptoSession</b>

<dd>
<p>The entry point for the driver's <a href="display.destroycryptosession1">DestroyCryptoSession</a> function.</p>
</dd>

### -field <b>pfnGetCertificateSize</b>

<dd>
<p>The entry point for the driver's <a href="display.getcertificatesize">GetCertificateSize</a> function.</p>
</dd>

### -field <b>pfnGetCertificate</b>

<dd>
<p>The entry point for the driver's <a href="display.getcertificate">GetCertificate</a> function.</p>
</dd>

### -field <b>pfnNegotiateCryptoSessionKeyExchange</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-negotiatecryptosessionkeyeschange.md">NegotiateCryptoSessionKeyExchange</a> function.</p>
</dd>

### -field <b>pfnEncryptionBlt</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-encryptionblt.md">EncryptionBlt(D3D11_1)</a> function.</p>
</dd>

### -field <b>pfnDecryptionBlt</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-decryptionblt.md">DecryptionBlt(D3D11_1)</a> function.</p>
</dd>

### -field <b>pfnStartSessionKeyRefresh</b>

<dd>
<p>The entry point for the driver's <a href="display.startsessionkeyrefresh1">StartSessionKeyRefresh</a> function.</p>
</dd>

### -field <b>pfnFinishSessionKeyRefresh</b>

<dd>
<p>The entry point for the driver's <a href="display.finishsessionkeyrefresh1">FinishSessionKeyRefresh</a> function.</p>
</dd>

### -field <b>pfnGetEncryptionBltKey</b>

<dd>
<p>The entry point for the driver's <a href="..\d3dumddi\ns-d3dumddi--getencryptionbltkey.md">GetEncryptionBltKey</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateAuthenticatedChannelSize</b>

<dd>
<p>The entry point for the driver's <a href="display.calcprivateauthenticatedchannelsize">CalcPrivateAuthenticatedChannelSize</a> function.</p>
</dd>

### -field <b>pfnCreateAuthenticatedChannel</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createauthenticatedchannel.md">CreateAuthenticatedChannel(D3D11_1)</a> function.</p>
</dd>

### -field <b>pfnDestroyAuthenticatedChannel</b>

<dd>
<p>The entry point for the driver's <a href="display.destroyauthenticatedchannel1">DestroyAuthenticatedChannel</a> function.</p>
</dd>

### -field <b>pfnNegotiateAuthenticatedChannelKeyExchange</b>

<dd>
<p>The entry point for the driver's <a href="display.negotiateauthenticatedchannelkeyexchange">NegotiateAuthenticatedChannelKeyExchange</a> function.</p>
</dd>

### -field <b>pfnQueryAuthenticatedChannel</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-queryauthenticatedchannel.md">QueryAuthenticatedChannel(D3D11_1)</a> function.</p>
</dd>

### -field <b>pfnConfigureAuthenticatedChannel</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-configureauthenticatedchannel.md">ConfigureAuthenticatedChannel(D3D11_1)</a> function.</p>
</dd>

### -field <b>pfnVideoDecoderGetHandle</b>

<dd>
<p>The entry point for the driver's <a href="display.videodecodergethandle">VideoDecoderGetHandle</a> function.</p>
</dd>

### -field <b>pfnCryptoSessionGetHandle</b>

<dd>
<p>The entry point for the driver's <a href="display.cryptosessiongethandle">CryptoSessionGetHandle</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamRotation</b>

<dd>
<p>The entry point for the driver's <a href="display.videoprocessorsetstreamrotation">VideoProcessorSetStreamRotation</a> function.</p>
</dd>

### -field <b>pfnGetCaptureHandle</b>

<dd>
<p>The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-getcapturehandle.md">GetCaptureHandle</a> function.</p>
</dd>

### -field <b>pfnGetDataForNewHardwareKey</b>

<dd>
<p>The entry point for the driver's     <a href="display.getdatafornewhardwarekey">GetDataForNewHardwareKey</a> function.</p>
</dd>

### -field <b>pfnCheckCryptoSessionStatus</b>

<dd>
<p>The entry point for the driver's     <a href="display.checkcryptosessionstatus">CheckCryptoSessionStatus</a> function.</p>
</dd>

### -field <b>pfnVideoDecoderSubmitBuffers1</b>

<dd>
<p>The entry point for the driver's     <a href="display.videodecodersubmitbuffers1">VideoDecoderSubmitBuffers1</a> function.</p>
</dd>

### -field <b>pfnQueryVideoCapabilities</b>

<dd>
<p>The entry point for the driver's     <a href="display.queryvideocapabilities">QueryVideoCapabilities</a> function.</p>
</dd>

### -field <b>pfnCheckVideoProcessorFormatConversion</b>

<dd>
<p>The entry point for the driver's     <a href="display.checkvideoprocessorformatconversion">CheckVideoProcessorFormatConversion</a> function.</p>
</dd>

### -field <b>pfnVideoDecoderEnableDownsampling</b>

<dd>
<p>The entry point for the driver's     <a href="display.videodecoderenabledownsampling">VideoDecoderEnableDownsampling</a> function.</p>
</dd>

### -field <b>pfnVideoDecoderUpdateDownsampling</b>

<dd>
<p>The entry point for the driver's     <a href="display.videodecoderupdatedownsampling">VideoDecoderUpdateDownsampling</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamMirror</b>

<dd>
<p>The entry point for the driver's     <a href="display.videoprocessorsetstreammirror">VideoProcessorSetStreamMirror</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetOutputColorSpace1</b>

<dd>
<p>The entry point for the driver's     <a href="display.videoprocessorsetoutputcolorspace1">VideoProcessorSetOutputColorSpace1</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamColorSpace1</b>

<dd>
<p>The entry point for the driver's     <a href="display.videoprocessorsetstreamcolorspace1">VideoProcessorSetStreamColorSpace1</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetOutputShaderUsage</b>

<dd>
<p>The entry point for the driver's     <a href="display.videoprocessorsetoutputshaderusage">VideoProcessorSetOutputShaderUsage</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorGetBehaviorHints</b>

<dd>
<p>The entry point for the driver's     <a href="display.videoprocessorgetbehaviorhints">VideoProcessorGetBehaviorHints</a> function.</p>
</dd>

### -field <b>pfnGetCryptoSessionPrivateDataSize        </b>

<dd>
<p>The entry point for the driver's     <a href="display.getcryptosessionprivatedatasize">GetCryptoSessionPrivateDataSize</a> function.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>