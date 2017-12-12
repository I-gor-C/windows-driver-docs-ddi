---
UID: NS.D3D10UMDDI.D3DWDDM2_0DDI_VIDEODEVICEFUNCS
title: D3DWDDM2_0DDI_VIDEODEVICEFUNCS
author: windows-driver-content
description: Specifies the video function table for the Microsoft Direct3D driver device object. Used only by Windows Display Driver Model (WDDM) 2.0 and later drivers.
old-location: display\d3dwddm2_0ddi_videodevicefuncs.htm
old-project: display
ms.assetid: 59D06B73-413B-4595-841E-7E0A696A3AC2
ms.author: windowsdriverdev
ms.date: 12/8/2017
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
---

# D3DWDDM2_0DDI_VIDEODEVICEFUNCS structure



## -description
Specifies the video function table for the  Microsoft Direct3D driver device object. Used only by Windows Display Driver Model (WDDM) 2.0 and later drivers.



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

### -field pfnGetVideoDecoderProfileCount

The entry point for the driver's <a href="display.getvideodecoderprofilecount">VideoDecoderProfileCount</a> function.


### -field pfnGetVideoDecoderProfile

The entry point for the driver's <a href="display.getvideodecoderprofile">VideoDecoderProfile</a> function.


### -field pfnCheckVideoDecoderFormat

The entry point for the driver's <a href="display.checkvideodecoderformat">CheckVideoDecoderFormat</a> function.


### -field pfnGetVideoDecoderConfigCount

The entry point for the driver's <a href="display.getvideodecoderconfigcount">GetVideoDecoderConfig</a> function.


### -field pfnGetVideoDecoderConfig

The entry point for the driver's <a href="display.getvideodecoderconfig">GetVideoDecoderConfig</a> function.


### -field pfnGetVideoDecoderBufferTypeCount

The entry point for the driver's <a href="display.getvideodecoderbuffertypecount">GetVideoDecoderBufferTypeCount</a> function.


### -field pfnGetVideoDecoderBufferInfo

The entry point for the driver's <a href="display.getvideodecoderbufferinfo">GetVideoDecoderBufferInfo</a> function.


### -field pfnCalcPrivateVideoDecoderSize

The entry point for the driver's <a href="display.calcprivatevideodecodersize">CalcPrivateVideoDecoderSize</a> function.


### -field pfnCreateVideoDecoder

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideodecoder.md">CreateVideoDecoder</a> function.


### -field pfnDestroyVideoDecoder

The entry point for the driver's <a href="display.destroyvideodecoder">DestroyVideoDecoder</a> function.


### -field pfnVideoDecoderExtension

The entry point for the driver's <a href="display.videodecoderextension">VideoDecoderExtension</a> function.


### -field pfnVideoDecoderBeginFrame

The entry point for the driver's <a href="display.videodecoderbeginframe">VideoDecoderBeginFrame</a> function.


### -field pfnVideoDecoderEndFrame

The entry point for the driver's <a href="display.videodecoderendframe">VideoDecoderEndFrame</a> function.


### -field pfnVideoDecoderSubmitBuffers

The entry point for the driver's <a href="display.videodecodersubmitbuffers">VideoDecoderSubmitBuffers</a> function.


### -field pfnCalcPrivateVideoProcessorEnumSize

The entry point for the driver's <a href="display.calcprivatevideoprocessorenumsize">CalcPrivateVideoProcessorEnumSize</a> function.


### -field pfnCreateVideoProcessorEnum

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessorenum.md">CreateVideoProcessorEnum</a> function.


### -field pfnDestroyVideoProcessorEnum

The entry point for the driver's <a href="display.destroyvideoprocessorenum">DestroyVideoProcessorEnum</a> function.


### -field pfnCheckVideoProcessorFormat

The entry point for the driver's <a href="display.checkvideoprocessorformat">CheckVideoProcessorFormat</a> function.


### -field pfnGetVideoProcessorCaps

The entry point for the driver's <a href="display.getvideoprocessorcaps">GetVideoProcessorCaps</a> function.


### -field pfnGetVideoProcessorRateConversionCaps

The entry point for the driver's <a href="display.getvideoprocessorrateconversioncaps">GetVideoProcessorRateConversionCaps</a> function.


### -field pfnGetVideoProcessorCustomRate

The entry point for the driver's <a href="display.getvideoprocessorcustomrate">GetVideoProcessorCustomRate</a> function.


### -field pfnGetVideoProcessorFilterRange

The entry point for the driver's <a href="display.getvideoprocessorfilterrange">GetVideoProcessorFilterRange</a> function.


### -field pfnCalcPrivateVideoProcessorSize

The entry point for the driver's <a href="display.calcprivatevideoprocessorsize">CalcPrivateVideoProcessorSize</a> function.


### -field pfnCreateVideoProcessor

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessor.md">CreateVideoProcessor</a> function.


### -field pfnDestroyVideoProcessor

The entry point for the driver's <a href="display.destroyvideoprocessor1">DestroyVideoProcessor</a> function.


### -field pfnVideoProcessorSetOutputTargetRect

The entry point for the driver's <a href="display.videoprocessorsetoutputtargetrect">VideoProcessorSetOutputTargetRect</a> function.


### -field pfnVideoProcessorSetOutputBackgroundColor

The entry point for the driver's <a href="display.videoprocessorsetoutputbackgroundcolor">VideoProcessorSetOutputBackgroundColor</a> function.


### -field pfnVideoProcessorSetOutputColorSpace

The entry point for the driver's <a href="display.videoprocessorsetoutputcolorspace">VideoProcessorSetOutputColorSpace</a> function.


### -field pfnVideoProcessorSetOutputAlphaFillMode

The entry point for the driver's <a href="display.videoprocessorsetoutputalphafillmode">VideoProcessorSetOutputAlphaFillMode</a> function.


### -field pfnVideoProcessorSetOutputConstriction

The entry point for the driver's <a href="display.videoprocessorsetoutputconstriction">VideoProcessorSetOutputConstriction</a> function.


### -field pfnVideoProcessorSetOutputStereoMode

The entry point for the driver's <a href="display.videoprocessorsetoutputstereomode">VideoProcessorSetOutputStereoMode</a> function.


### -field pfnVideoProcessorSetOutputExtension

The entry point for the driver's <a href="display.videoprocessorsetoutputextension">VideoProcessorSetOutputExtension</a> function.


### -field pfnVideoProcessorGetOutputExtension

The entry point for the driver's <a href="display.videoprocessorgetoutputextension">VideoProcessorGetOutputExtension</a> function.


### -field pfnVideoProcessorSetStreamFrameFormat

The entry point for the driver's <a href="display.videoprocessorsetstreamframeformat">VideoProcessorSetStreamFrameFormat</a> function.


### -field pfnVideoProcessorSetStreamColorSpace

The entry point for the driver's <a href="display.videoprocessorsetstreamcolorspace">VideoProcessorSetStreamColorSpace</a> function.


### -field pfnVideoProcessorSetStreamOutputRate

The entry point for the driver's <a href="display.videoprocessorsetstreamoutputrate">VideoProcessorSetStreamOutputRate</a> function.


### -field pfnVideoProcessorSetStreamSourceRect

The entry point for the driver's <a href="display.videoprocessorsetstreamsourcerect">VideoProcessorSetStreamSourceRect</a> function.


### -field pfnVideoProcessorSetStreamDestRect

The entry point for the driver's <a href="display.videoprocessorsetstreamdestrect">VideoProcessorSetStreamDestRect</a> function.


### -field pfnVideoProcessorSetStreamAlpha

The entry point for the driver's <a href="display.videoprocessorsetstreamalpha">VideoProcessorSetStreamAlpha</a> function.


### -field pfnVideoProcessorSetStreamPalette

The entry point for the driver's <a href="display.videoprocessorsetstreampalette">VideoProcessorSetStreamPalette</a> function.


### -field pfnVideoProcessorSetStreamPixelAspectRatio

The entry point for the driver's <a href="display.videoprocessorsetstreampixelaspectratio">VideoProcessorSetStreamPixelAspectRatio</a> function.


### -field pfnVideoProcessorSetStreamLumaKey

The entry point for the driver's <a href="display.videoprocessorsetstreamlumakey">VideoProcessorSetStreamLumaKey</a> function.


### -field pfnVideoProcessorSetStreamStereoFormat

The entry point for the driver's <a href="display.videoprocessorsetstreamstereoformat">VideoProcessorSetStreamStereoFormat</a> function.


### -field pfnVideoProcessorSetStreamAutoProcessingMode

The entry point for the driver's <a href="display.videoprocessorsetstreamautoprocessingmode">VideoProcessorSetStreamAutoProcessingMode</a> function.


### -field pfnVideoProcessorSetStreamFilter

The entry point for the driver's <a href="display.videoprocessorsetstreamfilter">VideoProcessorSetStreamFilter</a> function.


### -field pfnVideoProcessorSetStreamExtension

The entry point for the driver's <a href="display.videoprocessorsetstreamextension">VideoProcessorSetStreamExtension</a> function.


### -field pfnVideoProcessorGetStreamExtension

The entry point for the driver's <a href="display.videoprocessorgetstreamextension">VideoProcessorGetStreamExtension</a> function.


### -field pfnVideoProcessorBlt

The entry point for the driver's <a href="display.videoprocessorblt">VideoProcessorBlt</a> function.


### -field pfnCalcPrivateVideoDecoderOutputViewSize

The entry point for the driver's <a href="display.calcprivatevideodecoderoutputviewsize">CalcPrivateVideoDecoderOutputViewSize</a> function.


### -field pfnCreateVideoDecoderOutputView

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideodecoderoutputview.md">CreateVideoDecoderOutputView</a> function.


### -field pfnDestroyVideoDecoderOutputView

The entry point for the driver's <a href="display.destroyvideodecoderoutputview">DestroyVideoDecoderOutputView</a> function.


### -field pfnCalcPrivateVideoProcessorInputViewSize

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_calcprivatevideoprocessorinputviewsize.md">CalcPrivateVideoProcessorInputViewSize</a> function.


### -field pfnCreateVideoProcessorInputView

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessorinputview.md">CreateVideoProcessorInputView</a> function.


### -field pfnDestroyVideoProcessorInputView

The entry point for the driver's <a href="display.destroyvideoprocessorinputview">DestroyVideoProcessorInputView</a> function.


### -field pfnCalcPrivateVideoProcessorOutputViewSize

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_calcprivatevideoprocessoroutputviewsize.md">CalcPrivateVideoProcessorOutputViewSize</a> function.


### -field pfnCreateVideoProcessorOutputView

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessoroutputview.md">CreateVideoProcessorOutputView</a> function.


### -field pfnDestroyVideoProcessorOutputView

The entry point for the driver's <a href="display.destroyvideoprocessoroutputview">DestroyVideoProcessorOutputView</a> function.


### -field pfnVideoProcessorInputViewReadAfterWriteHazard

The entry point for the driver's <a href="display.videoprocessorinputviewreadafterwritehazard">VideoProcessorInputViewReadAfterWriteHazard</a> function.


### -field pfnGetContentProtectionCaps

The entry point for the driver's <a href="display.getcontentprotectioncaps">GetContentProtectionCaps</a> function.


### -field pfnGetCryptoKeyExchangeType

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getcryptokeyexchangetype.md">GetCryptoKeyExchangeType</a> function.


### -field pfnCalcPrivateCryptoSessionSize

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_calcprivatecryptosessionsize.md">CalcPrivateCryptoSessionSize</a> function.


### -field pfnCreateCryptoSession

The entry point for the driver's <a href="display.createcryptosession1">CreateCryptoSession</a> function.


### -field pfnDestroyCryptoSession

The entry point for the driver's <a href="display.destroycryptosession1">DestroyCryptoSession</a> function.


### -field pfnGetCertificateSize

The entry point for the driver's <a href="display.getcertificatesize">GetCertificateSize</a> function.


### -field pfnGetCertificate

The entry point for the driver's <a href="display.getcertificate">GetCertificate</a> function.


### -field pfnNegotiateCryptoSessionKeyExchange

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_negotiatecryptosessionkeyeschange.md">NegotiateCryptoSessionKeyExchange</a> function.


### -field pfnEncryptionBlt

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_encryptionblt.md">EncryptionBlt(D3D11_1)</a> function.


### -field pfnDecryptionBlt

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_decryptionblt.md">DecryptionBlt(D3D11_1)</a> function.


### -field pfnStartSessionKeyRefresh

The entry point for the driver's <a href="display.startsessionkeyrefresh1">StartSessionKeyRefresh</a> function.


### -field pfnFinishSessionKeyRefresh

The entry point for the driver's <a href="display.finishsessionkeyrefresh1">FinishSessionKeyRefresh</a> function.


### -field pfnGetEncryptionBltKey

The entry point for the driver's <a href="display.getencryptionbltkey1">GetEncryptionBltKey</a> function.


### -field pfnCalcPrivateAuthenticatedChannelSize

The entry point for the driver's <a href="display.calcprivateauthenticatedchannelsize">CalcPrivateAuthenticatedChannelSize</a> function.


### -field pfnCreateAuthenticatedChannel

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createauthenticatedchannel.md">CreateAuthenticatedChannel(D3D11_1)</a> function.


### -field pfnDestroyAuthenticatedChannel

The entry point for the driver's <a href="display.destroyauthenticatedchannel1">DestroyAuthenticatedChannel</a> function.


### -field pfnNegotiateAuthenticatedChannelKeyExchange

The entry point for the driver's <a href="display.negotiateauthenticatedchannelkeyexchange">NegotiateAuthenticatedChannelKeyExchange</a> function.


### -field pfnQueryAuthenticatedChannel

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_queryauthenticatedchannel.md">QueryAuthenticatedChannel(D3D11_1)</a> function.


### -field pfnConfigureAuthenticatedChannel

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_configureauthenticatedchannel.md">ConfigureAuthenticatedChannel(D3D11_1)</a> function.


### -field pfnVideoDecoderGetHandle

The entry point for the driver's <a href="display.videodecodergethandle">VideoDecoderGetHandle</a> function.


### -field pfnCryptoSessionGetHandle

The entry point for the driver's <a href="display.cryptosessiongethandle">CryptoSessionGetHandle</a> function.


### -field pfnVideoProcessorSetStreamRotation

The entry point for the driver's <a href="display.videoprocessorsetstreamrotation">VideoProcessorSetStreamRotation</a> function.


### -field pfnGetCaptureHandle

The entry point for the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getcapturehandle.md">GetCaptureHandle</a> function.


### -field pfnGetDataForNewHardwareKey

The entry point for the driver's     <a href="display.getdatafornewhardwarekey">GetDataForNewHardwareKey</a> function.


### -field pfnCheckCryptoSessionStatus

The entry point for the driver's     <a href="display.checkcryptosessionstatus">CheckCryptoSessionStatus</a> function.


### -field pfnVideoDecoderSubmitBuffers1

The entry point for the driver's     <a href="display.videodecodersubmitbuffers1">VideoDecoderSubmitBuffers1</a> function.


### -field pfnQueryVideoCapabilities

The entry point for the driver's     <a href="display.queryvideocapabilities">QueryVideoCapabilities</a> function.


### -field pfnCheckVideoProcessorFormatConversion

The entry point for the driver's     <a href="display.checkvideoprocessorformatconversion">CheckVideoProcessorFormatConversion</a> function.


### -field pfnVideoDecoderEnableDownsampling

The entry point for the driver's     <a href="display.videodecoderenabledownsampling">VideoDecoderEnableDownsampling</a> function.


### -field pfnVideoDecoderUpdateDownsampling

The entry point for the driver's     <a href="display.videodecoderupdatedownsampling">VideoDecoderUpdateDownsampling</a> function.


### -field pfnVideoProcessorSetStreamMirror

The entry point for the driver's     <a href="display.videoprocessorsetstreammirror">VideoProcessorSetStreamMirror</a> function.


### -field pfnVideoProcessorSetOutputColorSpace1

The entry point for the driver's     <a href="display.videoprocessorsetoutputcolorspace1">VideoProcessorSetOutputColorSpace1</a> function.


### -field pfnVideoProcessorSetStreamColorSpace1

The entry point for the driver's     <a href="display.videoprocessorsetstreamcolorspace1">VideoProcessorSetStreamColorSpace1</a> function.


### -field pfnVideoProcessorSetOutputShaderUsage

The entry point for the driver's     <a href="display.videoprocessorsetoutputshaderusage">VideoProcessorSetOutputShaderUsage</a> function.


### -field pfnVideoProcessorGetBehaviorHints

The entry point for the driver's     <a href="display.videoprocessorgetbehaviorhints">VideoProcessorGetBehaviorHints</a> function.


### -field pfnGetCryptoSessionPrivateDataSize        

The entry point for the driver's     <a href="display.getcryptosessionprivatedatasize">GetCryptoSessionPrivateDataSize</a> function.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>