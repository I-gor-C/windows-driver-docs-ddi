---
UID: NS.d3d10umddi.D3D11_1DDI_VIDEODEVICEFUNCS
title: D3D11_1DDI_VIDEODEVICEFUNCS
author: windows-driver-content
description: Specifies the video function table for the Microsoft Direct3D driver device object.
old-location: display\d3d11_1ddi_videodevicefuncs.htm
ms.assetid: c843fe5c-19bc-479c-8d8d-a3a6146dfb1c
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_VIDEODEVICEFUNCS
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
ms.keywords: D3D11_1DDI_VIDEODEVICEFUNCS, D3D11_1DDI_VIDEODEVICEFUNCS
req.iface: 
---

# D3D11_1DDI_VIDEODEVICEFUNCS structure



## -description
<p>Specifies the video function table for the  Microsoft Direct3D driver device object.</p>


## -syntax

````
typedef struct D3D11_1DDI_VIDEODEVICEFUNCS {
  PFND3D11_1DDI_GETVIDEODECODERPROFILECOUNT                 pfnGetVideoDecoderProfileCount;
  PFND3D11_1DDI_GETVIDEODECODERPROFILE                      pfnGetVideoDecoderProfile;
  PFND3D11_1DDI_CHECKVIDEODECODERFORMAT                     pfnCheckVideoDecoderFormat;
  PFND3D11_1DDI_GETVIDEODECODERCONFIGCOUNT                  pfnGetVideoDecoderConfigCount;
  PFND3D11_1DDI_GETVIDEODECODERCONFIG                       pfnGetVideoDecoderConfig;
  PFND3D11_1DDI_GETVIDEODECODERBUFFERTYPECOUNT              pfnGetVideoDecoderBufferTypeCount;
  PFND3D11_1DDI_GETVIDEODECODERBUFFERINFO                   pfnGetVideoDecoderBufferInfo;
  PFND3D11_1DDI_CALCPRIVATEVIDEODECODERSIZE                 pfnCalcPrivateVideoDecoderSize;
  PFND3D11_1DDI_CREATEVIDEODECODER                          pfnCreateVideoDecoder;
  PFND3D11_1DDI_DESTROYVIDEODECODER                         pfnDestroyVideoDecoder;
  PFND3D11_1DDI_VIDEODECODEREXTENSION                       pfnVideoDecoderExtension;
  PFND3D11_1DDI_VIDEODECODERBEGINFRAME                      pfnVideoDecoderBeginFrame;
  PFND3D11_1DDI_VIDEODECODERENDFRAME                        pfnVideoDecoderEndFrame;
  PFND3D11_1DDI_VIDEODECODERSUBMITBUFFERS                   pfnVideoDecoderSubmitBuffers;
  PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORENUMSIZE           pfnCalcPrivateVideoProcessorEnumSize;
  PFND3D11_1DDI_CREATEVIDEOPROCESSORENUM                    pfnCreateVideoProcessorEnum;
  PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM                   pfnDestroyVideoProcessorEnum;
  PFND3D11_1DDI_CHECKVIDEOPROCESSORFORMAT                   pfnCheckVideoProcessorFormat;
  PFND3D11_1DDI_GETVIDEOPROCESSORCAPS                       pfnGetVideoProcessorCaps;
  PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS         pfnGetVideoProcessorRateConversionCaps;
  PFND3D11_1DDI_GETVIDEOPROCESSORCUSTOMRATE                 pfnGetVideoProcessorCustomRate;
  PFND3D11_1DDI_GETVIDEOPROCESSORFILTERRANGE                pfnGetVideoProcessorFilterRange;
  PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORSIZE               pfnCalcPrivateVideoProcessorSize;
  PFND3D11_1DDI_CREATEVIDEOPROCESSOR                        pfnCreateVideoProcessor;
  PFND3D11_1DDI_DESTROYVIDEOPROCESSOR                       pfnDestroyVideoProcessor;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTTARGETRECT           pfnVideoProcessorSetOutputTargetRect;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTBACKGROUNDCOLOR      pfnVideoProcessorSetOutputBackgroundColor;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCOLORSPACE           pfnVideoProcessorSetOutputColorSpace;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE        pfnVideoProcessorSetOutputAlphaFillMode;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCONSTRICTION         pfnVideoProcessorSetOutputConstriction;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTSTEREOMODE           pfnVideoProcessorSetOutputStereoMode;
  PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTEXTENSION            pfnVideoProcessorSetOutputExtension;
  PFND3D11_1DDI_VIDEOPROCESSORGETOUTPUTEXTENSION            pfnVideoProcessorGetOutputExtension;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMFRAMEFORMAT          pfnVideoProcessorSetStreamFrameFormat;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMCOLORSPACE           pfnVideoProcessorSetStreamColorSpace;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMOUTPUTRATE           pfnVideoProcessorSetStreamOutputRate;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSOURCERECT           pfnVideoProcessorSetStreamSourceRect;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMDESTRECT             pfnVideoProcessorSetStreamDestRect;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMALPHA                pfnVideoProcessorSetStreamAlpha;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPALETTE              pfnVideoProcessorSetStreamPalette;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPIXELASPECTRATIO     pfnVideoProcessorSetStreamPixelAspectRatio;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMLUMAKEY              pfnVideoProcessorSetStreamLumaKey;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSTEREOFORMAT         pfnVideoProcessorSetStreamStereoFormat;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMAUTOPROCESSINGMODE   pfnVideoProcessorSetStreamAutoProcessingMode;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMFILTER               pfnVideoProcessorSetStreamFilter;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMEXTENSION            pfnVideoProcessorSetStreamExtension;
  PFND3D11_1DDI_VIDEOPROCESSORGETSTREAMEXTENSION            pfnVideoProcessorGetStreamExtension;
  PFND3D11_1DDI_VIDEOPROCESSORBLT                           pfnVideoProcessorBlt;
  PFND3D11_1DDI_CALCPRIVATEVIDEODECODEROUTPUTVIEWSIZE       pfnCalcPrivateVideoDecoderOutputViewSize;
  PFND3D11_1DDI_CREATEVIDEODECODEROUTPUTVIEW                pfnCreateVideoDecoderOutputView;
  PFND3D11_1DDI_DESTROYVIDEODECODEROUTPUTVIEW               pfnDestroyVideoDecoderOutputView;
  PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORINPUTVIEWSIZE      pfnCalcPrivateVideoProcessorInputViewSize;
  PFND3D11_1DDI_CREATEVIDEOPROCESSORINPUTVIEW               pfnCreateVideoProcessorInputView;
  PFND3D11_1DDI_DESTROYVIDEOPROCESSORINPUTVIEW              pfnDestroyVideoProcessorInputView;
  PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSOROUTPUTVIEWSIZE     pfnCalcPrivateVideoProcessorOutputViewSize;
  PFND3D11_1DDI_CREATEVIDEOPROCESSOROUTPUTVIEW              pfnCreateVideoProcessorOutputView;
  PFND3D11_1DDI_DESTROYVIDEOPROCESSOROUTPUTVIEW             pfnDestroyVideoProcessorOutputView;
  PFND3D11_1DDI_VIDEOPROCESSORINPUTVIEWREADAFTERWRITEHAZARD pfnVideoProcessorInputViewReadAfterWriteHazard;
  PFND3D11_1DDI_GETCONTENTPROTECTIONCAPS                    pfnGetContentProtectionCaps;
  PFND3D11_1DDI_GETCRYPTOKEYEXCHANGETYPE                    pfnGetCryptoKeyExchangeType;
  PFND3D11_1DDI_CALCPRIVATECRYPTOSESSIONSIZE                pfnCalcPrivateCryptoSessionSize;
  PFND3D11_1DDI_CREATECRYPTOSESSION                         pfnCreateCryptoSession;
  PFND3D11_1DDI_DESTROYCRYPTOSESSION                        pfnDestroyCryptoSession;
  PFND3D11_1DDI_GETCERTIFICATESIZE                          pfnGetCertificateSize;
  PFND3D11_1DDI_GETCERTIFICATE                              pfnGetCertificate;
  PFND3D11_1DDI_NEGOTIATECRYPTOSESSIONKEYESCHANGE           pfnNegotiateCryptoSessionKeyExchange;
  PFND3D11_1DDI_ENCRYPTIONBLT                               pfnEncryptionBlt;
  PFND3D11_1DDI_DECRYPTIONBLT                               pfnDecryptionBlt;
  PFND3D11_1DDI_STARTSESSIONKEYREFRESH                      pfnStartSessionKeyRefresh;
  PFND3D11_1DDI_FINISHSESSIONKEYREFRESH                     pfnFinishSessionKeyRefresh;
  PFND3D11_1DDI_GETENCRYPTIONBLTKEY                         pfnGetEncryptionBltKey;
  PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE         pfnCalcPrivateAuthenticatedChannelSize;
  PFND3D11_1DDI_CREATEAUTHENTICATEDCHANNEL                  pfnCreateAuthenticatedChannel;
  PFND3D11_1DDI_DESTROYAUTHENTICATEDCHANNEL                 pfnDestroyAuthenticatedChannel;
  PFND3D11_1DDI_NEGOTIATEAUTHENTICATEDCHANNELKEYEXCHANGE    pfnNegotiateAuthenticatedChannelKeyExchange;
  PFND3D11_1DDI_QUERYAUTHENTICATEDCHANNEL                   pfnQueryAuthenticatedChannel;
  PFND3D11_1DDI_CONFIGUREAUTHENTICATEDCHANNEL               pfnConfigureAuthenticatedChannel;
  PFND3D11_1DDI_VIDEODECODERGETHANDLE                       pfnVideoDecoderGetHandle;
  PFND3D11_1DDI_CRYPTOSESSIONGETHANDLE                      pfnCryptoSessionGetHandle;
  PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMROTATION             pfnVideoProcessorSetStreamRotation;
  PFND3D11_1DDI_GETCAPTUREHANDLE                            pfnGetCaptureHandle;
} D3D11_1DDI_VIDEODEVICEFUNCS;
````


## -struct-fields
<dl>

### -field <b>pfnGetVideoDecoderProfileCount</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/ae24bc29-177e-48a1-adf9-ed8c79b7f39c">VideoDecoderProfileCount</a> function.</p>
</dd>

### -field <b>pfnGetVideoDecoderProfile</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/75576152-0afd-4602-b481-bf1d6d9348b3">VideoDecoderProfile</a> function.</p>
</dd>

### -field <b>pfnCheckVideoDecoderFormat</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451615">CheckVideoDecoderFormat</a> function.</p>
</dd>

### -field <b>pfnGetVideoDecoderConfigCount</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451665">GetVideoDecoderConfig</a> function.</p>
</dd>

### -field <b>pfnGetVideoDecoderConfig</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451665">GetVideoDecoderConfig</a> function.</p>
</dd>

### -field <b>pfnGetVideoDecoderBufferTypeCount</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451663">GetVideoDecoderBufferTypeCount</a> function.</p>
</dd>

### -field <b>pfnGetVideoDecoderBufferInfo</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451661">GetVideoDecoderBufferInfo</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateVideoDecoderSize</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451610">CalcPrivateVideoDecoderSize</a> function.</p>
</dd>

### -field <b>pfnCreateVideoDecoder</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/41254f99-1806-428c-8bf3-7e736dbeec84">CreateVideoDecoder</a> function.</p>
</dd>

### -field <b>pfnDestroyVideoDecoder</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451634">DestroyVideoDecoder</a> function.</p>
</dd>

### -field <b>pfnVideoDecoderExtension</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451699">VideoDecoderExtension</a> function.</p>
</dd>

### -field <b>pfnVideoDecoderBeginFrame</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451697">VideoDecoderBeginFrame</a> function.</p>
</dd>

### -field <b>pfnVideoDecoderEndFrame</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451698">VideoDecoderEndFrame</a> function.</p>
</dd>

### -field <b>pfnVideoDecoderSubmitBuffers</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451701">VideoDecoderSubmitBuffers</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateVideoProcessorEnumSize</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451611">CalcPrivateVideoProcessorEnumSize</a> function.</p>
</dd>

### -field <b>pfnCreateVideoProcessorEnum</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/38c27502-7e8a-45a1-8a7c-315300502480">CreateVideoProcessorEnum</a> function.</p>
</dd>

### -field <b>pfnDestroyVideoProcessorEnum</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451639">DestroyVideoProcessorEnum</a> function.</p>
</dd>

### -field <b>pfnCheckVideoProcessorFormat</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451616">CheckVideoProcessorFormat</a> function.</p>
</dd>

### -field <b>pfnGetVideoProcessorCaps</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451674">GetVideoProcessorCaps</a> function.</p>
</dd>

### -field <b>pfnGetVideoProcessorRateConversionCaps</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451690">GetVideoProcessorRateConversionCaps</a> function.</p>
</dd>

### -field <b>pfnGetVideoProcessorCustomRate</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451676">GetVideoProcessorCustomRate</a> function.</p>
</dd>

### -field <b>pfnGetVideoProcessorFilterRange</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451689">GetVideoProcessorFilterRange</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateVideoProcessorSize</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451614">CalcPrivateVideoProcessorSize</a> function.</p>
</dd>

### -field <b>pfnCreateVideoProcessor</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/741045a2-0a91-490a-907d-5f4900a4a0ae">CreateVideoProcessor</a> function.</p>
</dd>

### -field <b>pfnDestroyVideoProcessor</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451638">DestroyVideoProcessor</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetOutputTargetRect</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439790">VideoProcessorSetOutputTargetRect</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetOutputBackgroundColor</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/dn459003">VideoProcessorSetOutputBackgroundColor</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetOutputColorSpace</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439782">VideoProcessorSetOutputColorSpace</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetOutputAlphaFillMode</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439778">VideoProcessorSetOutputAlphaFillMode</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetOutputConstriction</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439784">VideoProcessorSetOutputConstriction</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetOutputStereoMode</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439788">VideoProcessorSetOutputStereoMode</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetOutputExtension</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439786">VideoProcessorSetOutputExtension</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorGetOutputExtension</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451705">VideoProcessorGetOutputExtension</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamFrameFormat</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439804">VideoProcessorSetStreamFrameFormat</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamColorSpace</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439796">VideoProcessorSetStreamColorSpace</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamOutputRate</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439807">VideoProcessorSetStreamOutputRate</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamSourceRect</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439815">VideoProcessorSetStreamSourceRect</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamDestRect</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/dn459004">VideoProcessorSetStreamDestRect</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamAlpha</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439792">VideoProcessorSetStreamAlpha</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamPalette</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439809">VideoProcessorSetStreamPalette</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamPixelAspectRatio</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439811">VideoProcessorSetStreamPixelAspectRatio</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamLumaKey</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439805">VideoProcessorSetStreamLumaKey</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamStereoFormat</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439817">VideoProcessorSetStreamStereoFormat</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamAutoProcessingMode</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439794">VideoProcessorSetStreamAutoProcessingMode</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamFilter</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439802">VideoProcessorSetStreamFilter</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamExtension</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439800">VideoProcessorSetStreamExtension</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorGetStreamExtension</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439773">VideoProcessorGetStreamExtension</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorBlt</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451703">VideoProcessorBlt</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateVideoDecoderOutputViewSize</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451608">CalcPrivateVideoDecoderOutputViewSize</a> function.</p>
</dd>

### -field <b>pfnCreateVideoDecoderOutputView</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/a5a32b4e-799c-4d18-995d-f804e6dff85c">CreateVideoDecoderOutputView</a> function.</p>
</dd>

### -field <b>pfnDestroyVideoDecoderOutputView</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451636">DestroyVideoDecoderOutputView</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateVideoProcessorInputViewSize</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/3cdf467c-41f5-4a44-b10a-41aeb76ca815">CalcPrivateVideoProcessorInputViewSize</a> function.</p>
</dd>

### -field <b>pfnCreateVideoProcessorInputView</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/f3942c53-e366-41c5-9f43-d093fa6b6ed6">CreateVideoProcessorInputView</a> function.</p>
</dd>

### -field <b>pfnDestroyVideoProcessorInputView</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451642">DestroyVideoProcessorInputView</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateVideoProcessorOutputViewSize</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/2cf09e91-e83b-47ae-bf34-037dc01d7e80">CalcPrivateVideoProcessorOutputViewSize</a> function.</p>
</dd>

### -field <b>pfnCreateVideoProcessorOutputView</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/619695dc-8525-4200-a0c2-8ce0fb1010ed">CreateVideoProcessorOutputView</a> function.</p>
</dd>

### -field <b>pfnDestroyVideoProcessorOutputView</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451644">DestroyVideoProcessorOutputView</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorInputViewReadAfterWriteHazard</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439775">VideoProcessorInputViewReadAfterWriteHazard</a> function.</p>
</dd>

### -field <b>pfnGetContentProtectionCaps</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451656">GetContentProtectionCaps</a> function.</p>
</dd>

### -field <b>pfnGetCryptoKeyExchangeType</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/64870c9f-facf-4344-93d0-12cbcec86e11">GetCryptoKeyExchangeType</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateCryptoSessionSize</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/9ca0fdd5-a724-4d5d-81b2-8885b2aed1ca">CalcPrivateCryptoSessionSize</a> function.</p>
</dd>

### -field <b>pfnCreateCryptoSession</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a> function.</p>
</dd>

### -field <b>pfnDestroyCryptoSession</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451632">DestroyCryptoSession</a> function.</p>
</dd>

### -field <b>pfnGetCertificateSize</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451654">GetCertificateSize</a> function.</p>
</dd>

### -field <b>pfnGetCertificate</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451652">GetCertificate</a> function.</p>
</dd>

### -field <b>pfnNegotiateCryptoSessionKeyExchange</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/a48dcbae-3236-4523-bc14-4be694da9a7b">NegotiateCryptoSessionKeyExchange</a> function.</p>
</dd>

### -field <b>pfnEncryptionBlt</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/ea6f1b8c-d65a-4d6d-a7ae-998374bf5bfb">EncryptionBlt(D3D11_1)</a> function.</p>
</dd>

### -field <b>pfnDecryptionBlt</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/36aeb826-251e-404e-8ce3-6b2246ff07bc">DecryptionBlt(D3D11_1)</a> function.</p>
</dd>

### -field <b>pfnStartSessionKeyRefresh</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451696">StartSessionKeyRefresh</a> function.</p>
</dd>

### -field <b>pfnFinishSessionKeyRefresh</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451648">FinishSessionKeyRefresh</a> function.</p>
</dd>

### -field <b>pfnGetEncryptionBltKey</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451660">GetEncryptionBltKey</a> function.</p>
</dd>

### -field <b>pfnCalcPrivateAuthenticatedChannelSize</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451604">CalcPrivateAuthenticatedChannelSize</a> function.</p>
</dd>

### -field <b>pfnCreateAuthenticatedChannel</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/90b43bc3-6569-4799-8be3-e4e60f59164f">CreateAuthenticatedChannel(D3D11_1)</a> function.</p>
</dd>

### -field <b>pfnDestroyAuthenticatedChannel</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451630">DestroyAuthenticatedChannel</a> function.</p>
</dd>

### -field <b>pfnNegotiateAuthenticatedChannelKeyExchange</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451691">NegotiateAuthenticatedChannelKeyExchange</a> function.</p>
</dd>

### -field <b>pfnQueryAuthenticatedChannel</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/bb152e3d-497f-4798-86cc-6f300e24a05c">QueryAuthenticatedChannel(D3D11_1)</a> function.</p>
</dd>

### -field <b>pfnConfigureAuthenticatedChannel</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/28d32813-15f5-4b9c-9bdb-5ad9b47bbe3b">ConfigureAuthenticatedChannel(D3D11_1)</a> function.</p>
</dd>

### -field <b>pfnVideoDecoderGetHandle</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451700">VideoDecoderGetHandle</a> function.</p>
</dd>

### -field <b>pfnCryptoSessionGetHandle</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451626">CryptoSessionGetHandle</a> function.</p>
</dd>

### -field <b>pfnVideoProcessorSetStreamRotation</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439813">VideoProcessorSetStreamRotation</a> function.</p>
</dd>

### -field <b>pfnGetCaptureHandle</b>

<dd>
<p>The entry point for the driver's <a href="https://msdn.microsoft.com/b1ca7cf0-fe63-452f-8360-fdba05875719">GetCaptureHandle</a> function.</p>
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
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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