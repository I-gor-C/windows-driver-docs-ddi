---
UID: NS:d3d10umddi.D3DWDDM2_0DDI_VIDEODEVICEFUNCS
title: D3DWDDM2_0DDI_VIDEODEVICEFUNCS
author: windows-driver-content
description: Specifies the video function table for the Microsoft Direct3D driver device object. Used only by Windows Display Driver Model (WDDM) 2.0 and later drivers.
old-location: display\d3dwddm2_0ddi_videodevicefuncs.htm
old-project: display
ms.assetid: 59D06B73-413B-4595-841E-7E0A696A3AC2
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DWDDM2_0DDI_VIDEODEVICEFUNCS, D3DWDDM2_0DDI_VIDEODEVICEFUNCS structure [Display Devices], d3d10umddi/D3DWDDM2_0DDI_VIDEODEVICEFUNCS, display.d3dwddm2_0ddi_videodevicefuncs
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	D3d10umddi.h
api_name:
-	D3DWDDM2_0DDI_VIDEODEVICEFUNCS
product:
- Windows
targetos: Windows
req.typenames: D3DWDDM2_0DDI_VIDEODEVICEFUNCS
---

# D3DWDDM2_0DDI_VIDEODEVICEFUNCS structure
Specifies the video function table for the  Microsoft Direct3D driver device object. Used only by Windows Display Driver Model (WDDM) 2.0 and later drivers.

## Syntax
```
typedef struct D3DWDDM2_0DDI_VIDEODEVICEFUNCS {
  PFND3D11_1DDI_GETVIDEODECODERPROFILECOUNT                 pfnGetVideoDecoderProfileCount;
  PFND3D11_1DDI_GETVIDEODECODERPROFILE                      pfnGetVideoDecoderProfile;
  PFND3D11_1DDI_CHECKVIDEODECODERFORMAT                     pfnCheckVideoDecoderFormat;
  PFND3D11_1DDI_GETVIDEODECODERCONFIGCOUNT                  pfnGetVideoDecoderConfigCount;
  PFND3D11_1DDI_GETVIDEODECODERCONFIG                       pfnGetVideoDecoderConfig;
  PFND3D11_1DDI_GETVIDEODECODERBUFFERTYPECOUNT              pfnGetVideoDecoderBufferTypeCount;
  PFND3D11_1DDI_GETVIDEODECODERBUFFERINFO                   pfnGetVideoDecoderBufferInfo;
  PFND3D11_1DDI_CALCPRIVATEVIDEODECODERSIZE                 pfnCalcPrivateVideoDecoderSize;
  PFND3D11_1DDI_CREATEVIDEODECODER                          pfnCreateVideoDecoder;
  PFND3D11_1DDI_DESTROYVIDEODECODER                         pfnDestroyVideoDecoder;
  PFND3D11_1DDI_VIDEODECODEREXTENSION                       pfnVideoDecoderExtension;
  PFND3D11_1DDI_VIDEODECODERBEGINFRAME                      pfnVideoDecoderBeginFrame;
  PFND3D11_1DDI_VIDEODECODERENDFRAME                        pfnVideoDecoderEndFrame;
  PFND3D11_1DDI_VIDEODECODERSUBMITBUFFERS                   pfnVideoDecoderSubmitBuffers;
  PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORENUMSIZE           pfnCalcPrivateVideoProcessorEnumSize;
  PFND3D11_1DDI_CREATEVIDEOPROCESSORENUM                    pfnCreateVideoProcessorEnum;
  PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM                   pfnDestroyVideoProcessorEnum;
  PFND3D11_1DDI_CHECKVIDEOPROCESSORFORMAT                   pfnCheckVideoProcessorFormat;
  PFND3D11_1DDI_GETVIDEOPROCESSORCAPS                       pfnGetVideoProcessorCaps;
  PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS         pfnGetVideoProcessorRateConversionCaps;
  PFND3D11_1DDI_GETVIDEOPROCESSORCUSTOMRATE                 pfnGetVideoProcessorCustomRate;
  PFND3D11_1DDI_GETVIDEOPROCESSORFILTERRANGE                pfnGetVideoProcessorFilterRange;
  PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORSIZE               pfnCalcPrivateVideoProcessorSize;
  PFND3D11_1DDI_CREATEVIDEOPROCESSOR                        pfnCreateVideoProcessor;
  PFND3D11_1DDI_DESTROYVIDEOPROCESSOR                       pfnDestroyVideoProcessor;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTTARGETRECT           pfnVideoProcessorSetOutputTargetRect;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTBACKGROUNDCOLOR      pfnVideoProcessorSetOutputBackgroundColor;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCOLORSPACE           pfnVideoProcessorSetOutputColorSpace;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE        pfnVideoProcessorSetOutputAlphaFillMode;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCONSTRICTION         pfnVideoProcessorSetOutputConstriction;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTSTEREOMODE           pfnVideoProcessorSetOutputStereoMode;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTEXTENSION            pfnVideoProcessorSetOutputExtension;
  PFND3D11_1DDI_VIDEOPROCESSORGETOUTPUTEXTENSION            pfnVideoProcessorGetOutputExtension;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMFRAMEFORMAT          pfnVideoProcessorSetStreamFrameFormat;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMCOLORSPACE           pfnVideoProcessorSetStreamColorSpace;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMOUTPUTRATE           pfnVideoProcessorSetStreamOutputRate;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSOURCERECT           pfnVideoProcessorSetStreamSourceRect;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMDESTRECT             pfnVideoProcessorSetStreamDestRect;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMALPHA                pfnVideoProcessorSetStreamAlpha;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPALETTE              pfnVideoProcessorSetStreamPalette;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPIXELASPECTRATIO     pfnVideoProcessorSetStreamPixelAspectRatio;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMLUMAKEY              pfnVideoProcessorSetStreamLumaKey;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSTEREOFORMAT         pfnVideoProcessorSetStreamStereoFormat;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMAUTOPROCESSINGMODE   pfnVideoProcessorSetStreamAutoProcessingMode;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMFILTER               pfnVideoProcessorSetStreamFilter;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMEXTENSION            pfnVideoProcessorSetStreamExtension;
  PFND3D11_1DDI_VIDEOPROCESSORGETSTREAMEXTENSION            pfnVideoProcessorGetStreamExtension;
  PFND3D11_1DDI_VIDEOPROCESSORBLT                           pfnVideoProcessorBlt;
  PFND3D11_1DDI_CALCPRIVATEVIDEODECODEROUTPUTVIEWSIZE       pfnCalcPrivateVideoDecoderOutputViewSize;
  PFND3D11_1DDI_CREATEVIDEODECODEROUTPUTVIEW                pfnCreateVideoDecoderOutputView;
  PFND3D11_1DDI_DESTROYVIDEODECODEROUTPUTVIEW               pfnDestroyVideoDecoderOutputView;
  PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORINPUTVIEWSIZE      pfnCalcPrivateVideoProcessorInputViewSize;
  PFND3D11_1DDI_CREATEVIDEOPROCESSORINPUTVIEW               pfnCreateVideoProcessorInputView;
  PFND3D11_1DDI_DESTROYVIDEOPROCESSORINPUTVIEW              pfnDestroyVideoProcessorInputView;
  PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSOROUTPUTVIEWSIZE     pfnCalcPrivateVideoProcessorOutputViewSize;
  PFND3D11_1DDI_CREATEVIDEOPROCESSOROUTPUTVIEW              pfnCreateVideoProcessorOutputView;
  PFND3D11_1DDI_DESTROYVIDEOPROCESSOROUTPUTVIEW             pfnDestroyVideoProcessorOutputView;
  PFND3D11_1DDI_VIDEOPROCESSORINPUTVIEWREADAFTERWRITEHAZARD pfnVideoProcessorInputViewReadAfterWriteHazard;
  PFND3D11_1DDI_GETCONTENTPROTECTIONCAPS                    pfnGetContentProtectionCaps;
  PFND3D11_1DDI_GETCRYPTOKEYEXCHANGETYPE                    pfnGetCryptoKeyExchangeType;
  PFND3D11_1DDI_CALCPRIVATECRYPTOSESSIONSIZE                pfnCalcPrivateCryptoSessionSize;
  PFND3D11_1DDI_CREATECRYPTOSESSION                         pfnCreateCryptoSession;
  PFND3D11_1DDI_DESTROYCRYPTOSESSION                        pfnDestroyCryptoSession;
  PFND3D11_1DDI_GETCERTIFICATESIZE                          pfnGetCertificateSize;
  PFND3D11_1DDI_GETCERTIFICATE                              pfnGetCertificate;
  PFND3D11_1DDI_NEGOTIATECRYPTOSESSIONKEYESCHANGE           pfnNegotiateCryptoSessionKeyExchange;
  PFND3D11_1DDI_ENCRYPTIONBLT                               pfnEncryptionBlt;
  PFND3D11_1DDI_DECRYPTIONBLT                               pfnDecryptionBlt;
  PFND3D11_1DDI_STARTSESSIONKEYREFRESH                      pfnStartSessionKeyRefresh;
  PFND3D11_1DDI_FINISHSESSIONKEYREFRESH                     pfnFinishSessionKeyRefresh;
  PFND3D11_1DDI_GETENCRYPTIONBLTKEY                         pfnGetEncryptionBltKey;
  PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE         pfnCalcPrivateAuthenticatedChannelSize;
  PFND3D11_1DDI_CREATEAUTHENTICATEDCHANNEL                  pfnCreateAuthenticatedChannel;
  PFND3D11_1DDI_DESTROYAUTHENTICATEDCHANNEL                 pfnDestroyAuthenticatedChannel;
  PFND3D11_1DDI_NEGOTIATEAUTHENTICATEDCHANNELKEYEXCHANGE    pfnNegotiateAuthenticatedChannelKeyExchange;
  PFND3D11_1DDI_QUERYAUTHENTICATEDCHANNEL                   pfnQueryAuthenticatedChannel;
  PFND3D11_1DDI_CONFIGUREAUTHENTICATEDCHANNEL               pfnConfigureAuthenticatedChannel;
  PFND3D11_1DDI_VIDEODECODERGETHANDLE                       pfnVideoDecoderGetHandle;
  PFND3D11_1DDI_CRYPTOSESSIONGETHANDLE                      pfnCryptoSessionGetHandle;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMROTATION             pfnVideoProcessorSetStreamRotation;
  PFND3D11_1DDI_GETCAPTUREHANDLE                            pfnGetCaptureHandle;
  PFND3DWDDM2_0DDI_GETDATAFORNEWHARDWAREKEY                 pfnGetDataForNewHardwareKey;
  PFND3DWDDM2_0DDI_CHECKCRYPTOSESSIONSTATUS                 pfnCheckCryptoSessionStatus;
  PFND3DWDDM2_0DDI_VIDEODECODERSUBMITBUFFERS1               pfnVideoDecoderSubmitBuffers1;
  PFND3DWDDM2_0DDI_QUERYVIDEOCAPABILITIES                   pfnQueryVideoCapabilities;
  PFND3DWDDM2_0DDI_CHECKVIDEOPROCESSORFORMATCONVERSION      pfnCheckVideoProcessorFormatConversion;
  PFND3DWDDM2_0DDI_VIDEODECODERENABLEDOWNSAMPLING           pfnVideoDecoderEnableDownsampling;
  PFND3DWDDM2_0DDI_VIDEODECODERUPDATEDOWNSAMPLING           pfnVideoDecoderUpdateDownsampling;
  PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMMIRROR            pfnVideoProcessorSetStreamMirror;
  PFND3DWDDM2_0DDI_VIDEOPROCESSORSETOUTPUTCOLORSPACE1       pfnVideoProcessorSetOutputColorSpace1;
  PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMCOLORSPACE1       pfnVideoProcessorSetStreamColorSpace1;
  PFND3DWDDM2_0DDI_VIDEOPROCESSORSETOUTPUTSHADERUSAGE       pfnVideoProcessorSetOutputShaderUsage;
  PFND3DWDDM2_0DDI_VIDEOPROCESSORGETBEHAVIORHINTS           pfnVideoProcessorGetBehaviorHints;
  PFND3DWDDM2_0DDI_GETCRYPTOSESSIONPRIVATEDATASIZE          pfnGetCryptoSessionPrivateDataSize;
};
```

## Members


`pfnGetVideoDecoderProfileCount`

The entry point for the driver's <a href="https://msdn.microsoft.com/ae24bc29-177e-48a1-adf9-ed8c79b7f39c">VideoDecoderProfileCount</a> function.

`pfnGetVideoDecoderProfile`

The entry point for the driver's <a href="https://msdn.microsoft.com/75576152-0afd-4602-b481-bf1d6d9348b3">VideoDecoderProfile</a> function.

`pfnCheckVideoDecoderFormat`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451615">CheckVideoDecoderFormat</a> function.

`pfnGetVideoDecoderConfigCount`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451665">GetVideoDecoderConfig</a> function.

`pfnGetVideoDecoderConfig`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451665">GetVideoDecoderConfig</a> function.

`pfnGetVideoDecoderBufferTypeCount`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451663">GetVideoDecoderBufferTypeCount</a> function.

`pfnGetVideoDecoderBufferInfo`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451661">GetVideoDecoderBufferInfo</a> function.

`pfnCalcPrivateVideoDecoderSize`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451610">CalcPrivateVideoDecoderSize</a> function.

`pfnCreateVideoDecoder`

The entry point for the driver's <a href="https://msdn.microsoft.com/41254f99-1806-428c-8bf3-7e736dbeec84">CreateVideoDecoder</a> function.

`pfnDestroyVideoDecoder`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451634">DestroyVideoDecoder</a> function.

`pfnVideoDecoderExtension`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451699">VideoDecoderExtension</a> function.

`pfnVideoDecoderBeginFrame`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451697">VideoDecoderBeginFrame</a> function.

`pfnVideoDecoderEndFrame`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451698">VideoDecoderEndFrame</a> function.

`pfnVideoDecoderSubmitBuffers`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451701">VideoDecoderSubmitBuffers</a> function.

`pfnCalcPrivateVideoProcessorEnumSize`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451611">CalcPrivateVideoProcessorEnumSize</a> function.

`pfnCreateVideoProcessorEnum`

The entry point for the driver's <a href="https://msdn.microsoft.com/38c27502-7e8a-45a1-8a7c-315300502480">CreateVideoProcessorEnum</a> function.

`pfnDestroyVideoProcessorEnum`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451639">DestroyVideoProcessorEnum</a> function.

`pfnCheckVideoProcessorFormat`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451616">CheckVideoProcessorFormat</a> function.

`pfnGetVideoProcessorCaps`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451674">GetVideoProcessorCaps</a> function.

`pfnGetVideoProcessorRateConversionCaps`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451690">GetVideoProcessorRateConversionCaps</a> function.

`pfnGetVideoProcessorCustomRate`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451676">GetVideoProcessorCustomRate</a> function.

`pfnGetVideoProcessorFilterRange`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451689">GetVideoProcessorFilterRange</a> function.

`pfnCalcPrivateVideoProcessorSize`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451614">CalcPrivateVideoProcessorSize</a> function.

`pfnCreateVideoProcessor`

The entry point for the driver's <a href="https://msdn.microsoft.com/741045a2-0a91-490a-907d-5f4900a4a0ae">CreateVideoProcessor</a> function.

`pfnDestroyVideoProcessor`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451638">DestroyVideoProcessor</a> function.

`pfnVideoProcessorSetOutputTargetRect`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439790">VideoProcessorSetOutputTargetRect</a> function.

`pfnVideoProcessorSetOutputBackgroundColor`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/dn459003">VideoProcessorSetOutputBackgroundColor</a> function.

`pfnVideoProcessorSetOutputColorSpace`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439782">VideoProcessorSetOutputColorSpace</a> function.

`pfnVideoProcessorSetOutputAlphaFillMode`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439778">VideoProcessorSetOutputAlphaFillMode</a> function.

`pfnVideoProcessorSetOutputConstriction`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439784">VideoProcessorSetOutputConstriction</a> function.

`pfnVideoProcessorSetOutputStereoMode`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439788">VideoProcessorSetOutputStereoMode</a> function.

`pfnVideoProcessorSetOutputExtension`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439786">VideoProcessorSetOutputExtension</a> function.

`pfnVideoProcessorGetOutputExtension`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451705">VideoProcessorGetOutputExtension</a> function.

`pfnVideoProcessorSetStreamFrameFormat`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439804">VideoProcessorSetStreamFrameFormat</a> function.

`pfnVideoProcessorSetStreamColorSpace`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439796">VideoProcessorSetStreamColorSpace</a> function.

`pfnVideoProcessorSetStreamOutputRate`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439807">VideoProcessorSetStreamOutputRate</a> function.

`pfnVideoProcessorSetStreamSourceRect`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439815">VideoProcessorSetStreamSourceRect</a> function.

`pfnVideoProcessorSetStreamDestRect`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/dn459004">VideoProcessorSetStreamDestRect</a> function.

`pfnVideoProcessorSetStreamAlpha`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439792">VideoProcessorSetStreamAlpha</a> function.

`pfnVideoProcessorSetStreamPalette`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439809">VideoProcessorSetStreamPalette</a> function.

`pfnVideoProcessorSetStreamPixelAspectRatio`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439811">VideoProcessorSetStreamPixelAspectRatio</a> function.

`pfnVideoProcessorSetStreamLumaKey`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439805">VideoProcessorSetStreamLumaKey</a> function.

`pfnVideoProcessorSetStreamStereoFormat`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439817">VideoProcessorSetStreamStereoFormat</a> function.

`pfnVideoProcessorSetStreamAutoProcessingMode`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439794">VideoProcessorSetStreamAutoProcessingMode</a> function.

`pfnVideoProcessorSetStreamFilter`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439802">VideoProcessorSetStreamFilter</a> function.

`pfnVideoProcessorSetStreamExtension`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439800">VideoProcessorSetStreamExtension</a> function.

`pfnVideoProcessorGetStreamExtension`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439773">VideoProcessorGetStreamExtension</a> function.

`pfnVideoProcessorBlt`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451703">VideoProcessorBlt</a> function.

`pfnCalcPrivateVideoDecoderOutputViewSize`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451608">CalcPrivateVideoDecoderOutputViewSize</a> function.

`pfnCreateVideoDecoderOutputView`

The entry point for the driver's <a href="https://msdn.microsoft.com/a5a32b4e-799c-4d18-995d-f804e6dff85c">CreateVideoDecoderOutputView</a> function.

`pfnDestroyVideoDecoderOutputView`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451636">DestroyVideoDecoderOutputView</a> function.

`pfnCalcPrivateVideoProcessorInputViewSize`

The entry point for the driver's <a href="https://msdn.microsoft.com/3cdf467c-41f5-4a44-b10a-41aeb76ca815">CalcPrivateVideoProcessorInputViewSize</a> function.

`pfnCreateVideoProcessorInputView`

The entry point for the driver's <a href="https://msdn.microsoft.com/f3942c53-e366-41c5-9f43-d093fa6b6ed6">CreateVideoProcessorInputView</a> function.

`pfnDestroyVideoProcessorInputView`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451642">DestroyVideoProcessorInputView</a> function.

`pfnCalcPrivateVideoProcessorOutputViewSize`

The entry point for the driver's <a href="https://msdn.microsoft.com/2cf09e91-e83b-47ae-bf34-037dc01d7e80">CalcPrivateVideoProcessorOutputViewSize</a> function.

`pfnCreateVideoProcessorOutputView`

The entry point for the driver's <a href="https://msdn.microsoft.com/619695dc-8525-4200-a0c2-8ce0fb1010ed">CreateVideoProcessorOutputView</a> function.

`pfnDestroyVideoProcessorOutputView`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451644">DestroyVideoProcessorOutputView</a> function.

`pfnVideoProcessorInputViewReadAfterWriteHazard`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439775">VideoProcessorInputViewReadAfterWriteHazard</a> function.

`pfnGetContentProtectionCaps`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451656">GetContentProtectionCaps</a> function.

`pfnGetCryptoKeyExchangeType`

The entry point for the driver's <a href="https://msdn.microsoft.com/64870c9f-facf-4344-93d0-12cbcec86e11">GetCryptoKeyExchangeType</a> function.

`pfnCalcPrivateCryptoSessionSize`

The entry point for the driver's <a href="https://msdn.microsoft.com/9ca0fdd5-a724-4d5d-81b2-8885b2aed1ca">CalcPrivateCryptoSessionSize</a> function.

`pfnCreateCryptoSession`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a> function.

`pfnDestroyCryptoSession`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451632">DestroyCryptoSession</a> function.

`pfnGetCertificateSize`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451654">GetCertificateSize</a> function.

`pfnGetCertificate`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451652">GetCertificate</a> function.

`pfnNegotiateCryptoSessionKeyExchange`

The entry point for the driver's <a href="https://msdn.microsoft.com/a48dcbae-3236-4523-bc14-4be694da9a7b">NegotiateCryptoSessionKeyExchange</a> function.

`pfnEncryptionBlt`

The entry point for the driver's <a href="https://msdn.microsoft.com/ea6f1b8c-d65a-4d6d-a7ae-998374bf5bfb">EncryptionBlt(D3D11_1)</a> function.

`pfnDecryptionBlt`

The entry point for the driver's <a href="https://msdn.microsoft.com/36aeb826-251e-404e-8ce3-6b2246ff07bc">DecryptionBlt(D3D11_1)</a> function.

`pfnStartSessionKeyRefresh`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451696">StartSessionKeyRefresh</a> function.

`pfnFinishSessionKeyRefresh`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451648">FinishSessionKeyRefresh</a> function.

`pfnGetEncryptionBltKey`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451660">GetEncryptionBltKey</a> function.

`pfnCalcPrivateAuthenticatedChannelSize`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451604">CalcPrivateAuthenticatedChannelSize</a> function.

`pfnCreateAuthenticatedChannel`

The entry point for the driver's <a href="https://msdn.microsoft.com/90b43bc3-6569-4799-8be3-e4e60f59164f">CreateAuthenticatedChannel(D3D11_1)</a> function.

`pfnDestroyAuthenticatedChannel`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451630">DestroyAuthenticatedChannel</a> function.

`pfnNegotiateAuthenticatedChannelKeyExchange`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451691">NegotiateAuthenticatedChannelKeyExchange</a> function.

`pfnQueryAuthenticatedChannel`

The entry point for the driver's <a href="https://msdn.microsoft.com/bb152e3d-497f-4798-86cc-6f300e24a05c">QueryAuthenticatedChannel(D3D11_1)</a> function.

`pfnConfigureAuthenticatedChannel`

The entry point for the driver's <a href="https://msdn.microsoft.com/28d32813-15f5-4b9c-9bdb-5ad9b47bbe3b">ConfigureAuthenticatedChannel(D3D11_1)</a> function.

`pfnVideoDecoderGetHandle`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451700">VideoDecoderGetHandle</a> function.

`pfnCryptoSessionGetHandle`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451626">CryptoSessionGetHandle</a> function.

`pfnVideoProcessorSetStreamRotation`

The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439813">VideoProcessorSetStreamRotation</a> function.

`pfnGetCaptureHandle`

The entry point for the driver's <a href="https://msdn.microsoft.com/b1ca7cf0-fe63-452f-8360-fdba05875719">GetCaptureHandle</a> function.

`pfnGetDataForNewHardwareKey`

The entry point for the driver's     <a href="https://msdn.microsoft.com/library/windows/hardware/dn906350">GetDataForNewHardwareKey</a> function.

`pfnCheckCryptoSessionStatus`

The entry point for the driver's     <a href="https://msdn.microsoft.com/library/windows/hardware/dn906316">CheckCryptoSessionStatus</a> function.

`pfnVideoDecoderSubmitBuffers1`

The entry point for the driver's     <a href="https://msdn.microsoft.com/library/windows/hardware/dn906377">VideoDecoderSubmitBuffers1</a> function.

`pfnQueryVideoCapabilities`

The entry point for the driver's     <a href="https://msdn.microsoft.com/library/windows/hardware/dn906368">QueryVideoCapabilities</a> function.

`pfnCheckVideoProcessorFormatConversion`

The entry point for the driver's     <a href="https://msdn.microsoft.com/library/windows/hardware/dn906317">CheckVideoProcessorFormatConversion</a> function.

`pfnVideoDecoderEnableDownsampling`

The entry point for the driver's     <a href="https://msdn.microsoft.com/library/windows/hardware/dn906376">VideoDecoderEnableDownsampling</a> function.

`pfnVideoDecoderUpdateDownsampling`

The entry point for the driver's     <a href="https://msdn.microsoft.com/library/windows/hardware/dn906378">VideoDecoderUpdateDownsampling</a> function.

`pfnVideoProcessorSetStreamMirror`

The entry point for the driver's     <a href="https://msdn.microsoft.com/library/windows/hardware/dn906383">VideoProcessorSetStreamMirror</a> function.

`pfnVideoProcessorSetOutputColorSpace1`

The entry point for the driver's     <a href="https://msdn.microsoft.com/library/windows/hardware/dn906380">VideoProcessorSetOutputColorSpace1</a> function.

`pfnVideoProcessorSetStreamColorSpace1`

The entry point for the driver's     <a href="https://msdn.microsoft.com/library/windows/hardware/dn906382">VideoProcessorSetStreamColorSpace1</a> function.

`pfnVideoProcessorSetOutputShaderUsage`

The entry point for the driver's     <a href="https://msdn.microsoft.com/library/windows/hardware/dn906381">VideoProcessorSetOutputShaderUsage</a> function.

`pfnVideoProcessorGetBehaviorHints`

The entry point for the driver's     <a href="https://msdn.microsoft.com/library/windows/hardware/dn906379">VideoProcessorGetBehaviorHints</a> function.

`pfnGetCryptoSessionPrivateDataSize`

The entry point for the driver's     <a href="https://msdn.microsoft.com/library/windows/hardware/dn906349">GetCryptoSessionPrivateDataSize</a> function.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |