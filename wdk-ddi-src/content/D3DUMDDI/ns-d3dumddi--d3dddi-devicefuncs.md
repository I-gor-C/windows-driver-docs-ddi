---
UID: NS.d3dumddi._D3DDDI_DEVICEFUNCS
title: D3DDDI_DEVICEFUNCS
author: windows-driver-content
description: The D3DDDI_DEVICEFUNCS structure contains functions that the user-mode display driver can implement to render graphics primitives and process state changes.
old-location: display\d3dddi_devicefuncs.htm
ms.assetid: 7345cd67-c10c-46f0-bd56-6f18929f4aa6
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_DEVICEFUNCS
req.alt-loc: d3dumddi.h
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
ms.keywords: D3DDDI_DEVICEFUNCS, D3DDDI_DEVICEFUNCS
req.iface: 
---

# D3DDDI_DEVICEFUNCS structure



## -description
<p>The D3DDDI_DEVICEFUNCS structure contains functions that the user-mode display driver can implement to render graphics primitives and process state changes.</p>


## -syntax

````
typedef struct _D3DDDI_DEVICEFUNCS {
  PFND3DDDI_SETRENDERSTATE                           pfnSetRenderState;
  PFND3DDDI_UPDATEWINFO                              pfnUpdateWInfo;
  PFND3DDDI_VALIDATEDEVICE                           pfnValidateDevice;
  PFND3DDDI_SETTEXTURESTAGESTATE                     pfnSetTextureStageState;
  PFND3DDDI_SETTEXTURE                               pfnSetTexture;
  PFND3DDDI_SETPIXELSHADER                           pfnSetPixelShader;
  PFND3DDDI_SETPIXELSHADERCONST                      pfnSetPixelShaderConst;
  PFND3DDDI_SETSTREAMSOURCEUM                        pfnSetStreamSourceUm;
  PFND3DDDI_SETINDICES                               pfnSetIndices;
  PFND3DDDI_SETINDICESUM                             pfnSetIndicesUm;
  PFND3DDDI_DRAWPRIMITIVE                            pfnDrawPrimitive;
  PFND3DDDI_DRAWINDEXEDPRIMITIVE                     pfnDrawIndexedPrimitive;
  PFND3DDDI_DRAWRECTPATCH                            pfnDrawRectPatch;
  PFND3DDDI_DRAWTRIPATCH                             pfnDrawTriPatch;
  PFND3DDDI_DRAWPRIMITIVE2                           pfnDrawPrimitive2;
  PFND3DDDI_DRAWINDEXEDPRIMITIVE2                    pfnDrawIndexedPrimitive2;
  PFND3DDDI_VOLBLT                                   pfnVolBlt;
  PFND3DDDI_BUFBLT                                   pfnBufBlt;
  PFND3DDDI_TEXBLT                                   pfnTexBlt;
  PFND3DDDI_STATESET                                 pfnStateSet;
  PFND3DDDI_SETPRIORITY                              pfnSetPriority;
  PFND3DDDI_CLEAR                                    pfnClear;
  PFND3DDDI_UPDATEPALETTE                            pfnUpdatePalette;
  PFND3DDDI_SETPALETTE                               pfnSetPalette;
  PFND3DDDI_SETVERTEXSHADERCONST                     pfnSetVertexShaderConst;
  PFND3DDDI_MULTIPLYTRANSFORM                        pfnMultiplyTransform;
  PFND3DDDI_SETTRANSFORM                             pfnSetTransform;
  PFND3DDDI_SETVIEWPORT                              pfnSetViewport;
  PFND3DDDI_SETZRANGE                                pfnSetZRange;
  PFND3DDDI_SETMATERIAL                              pfnSetMaterial;
  PFND3DDDI_SETLIGHT                                 pfnSetLight;
  PFND3DDDI_CREATELIGHT                              pfnCreateLight;
  PFND3DDDI_DESTROYLIGHT                             pfnDestroyLight;
  PFND3DDDI_SETCLIPPLANE                             pfnSetClipPlane;
  PFND3DDDI_GETINFO                                  pfnGetInfo;
  PFND3DDDI_LOCK                                     pfnLock;
  PFND3DDDI_UNLOCK                                   pfnUnlock;
  PFND3DDDI_CREATERESOURCE                           pfnCreateResource;
  PFND3DDDI_DESTROYRESOURCE                          pfnDestroyResource;
  PFND3DDDI_SETDISPLAYMODE                           pfnSetDisplayMode;
  PFND3DDDI_PRESENT                                  pfnPresent;
  PFND3DDDI_FLUSH                                    pfnFlush;
  PFND3DDDI_CREATEVERTEXSHADERFUNC                   pfnCreateVertexShaderFunc;
  PFND3DDDI_DELETEVERTEXSHADERFUNC                   pfnDeleteVertexShaderFunc;
  PFND3DDDI_SETVERTEXSHADERFUNC                      pfnSetVertexShaderFunc;
  PFND3DDDI_CREATEVERTEXSHADERDECL                   pfnCreateVertexShaderDecl;
  PFND3DDDI_DELETEVERTEXSHADERDECL                   pfnDeleteVertexShaderDecl;
  PFND3DDDI_SETVERTEXSHADERDECL                      pfnSetVertexShaderDecl;
  PFND3DDDI_SETVERTEXSHADERCONSTI                    pfnSetVertexShaderConstI;
  PFND3DDDI_SETVERTEXSHADERCONSTB                    pfnSetVertexShaderConstB;
  PFND3DDDI_SETSCISSORRECT                           pfnSetScissorRect;
  PFND3DDDI_SETSTREAMSOURCE                          pfnSetStreamSource;
  PFND3DDDI_SETSTREAMSOURCEFREQ                      pfnSetStreamSourceFreq;
  PFND3DDDI_SETCONVOLUTIONKERNELMONO                 pfnSetConvolutionKernelMono;
  PFND3DDDI_COMPOSERECTS                             pfnComposeRects;
  PFND3DDDI_BLT                                      pfnBlt;
  PFND3DDDI_COLORFILL                                pfnColorFill;
  PFND3DDDI_DEPTHFILL                                pfnDepthFill;
  PFND3DDDI_CREATEQUERY                              pfnCreateQuery;
  PFND3DDDI_DESTROYQUERY                             pfnDestroyQuery;
  PFND3DDDI_ISSUEQUERY                               pfnIssueQuery;
  PFND3DDDI_GETQUERYDATA                             pfnGetQueryData;
  PFND3DDDI_SETRENDERTARGET                          pfnSetRenderTarget;
  PFND3DDDI_SETDEPTHSTENCIL                          pfnSetDepthStencil;
  PFND3DDDI_GENERATEMIPSUBLEVELS                     pfnGenerateMipSubLevels;
  PFND3DDDI_SETPIXELSHADERCONSTI                     pfnSetPixelShaderConstI;
  PFND3DDDI_SETPIXELSHADERCONSTB                     pfnSetPixelShaderConstB;
  PFND3DDDI_CREATEPIXELSHADER                        pfnCreatePixelShader;
  PFND3DDDI_DELETEPIXELSHADER                        pfnDeletePixelShader;
  PFND3DDDI_CREATEDECODEDEVICE                       pfnCreateDecodeDevice;
  PFND3DDDI_DESTROYDECODEDEVICE                      pfnDestroyDecodeDevice;
  PFND3DDDI_SETDECODERENDERTARGET                    pfnSetDecodeRenderTarget;
  PFND3DDDI_DECODEBEGINFRAME                         pfnDecodeBeginFrame;
  PFND3DDDI_DECODEENDFRAME                           pfnDecodeEndFrame;
  PFND3DDDI_DECODEEXECUTE                            pfnDecodeExecute;
  PFND3DDDI_DECODEEXTENSIONEXECUTE                   pfnDecodeExtensionExecute;
  PFND3DDDI_CREATEVIDEOPROCESSDEVICE                 pfnCreateVideoProcessDevice;
  PFND3DDDI_DESTROYVIDEOPROCESSDEVICE                pfnDestroyVideoProcessDevice;
  PFND3DDDI_VIDEOPROCESSBEGINFRAME                   pfnVideoProcessBeginFrame;
  PFND3DDDI_VIDEOPROCESSENDFRAME                     pfnVideoProcessEndFrame;
  PFND3DDDI_SETVIDEOPROCESSRENDERTARGET              pfnSetVideoProcessRenderTarget;
  PFND3DDDI_VIDEOPROCESSBLT                          pfnVideoProcessBlt;
  PFND3DDDI_CREATEEXTENSIONDEVICE                    pfnCreateExtensionDevice;
  PFND3DDDI_DESTROYEXTENSIONDEVICE                   pfnDestroyExtensionDevice;
  PFND3DDDI_EXTENSIONEXECUTE                         pfnExtensionExecute;
  PFND3DDDI_CREATEOVERLAY                            pfnCreateOverlay;
  PFND3DDDI_UPDATEOVERLAY                            pfnUpdateOverlay;
  PFND3DDDI_FLIPOVERLAY                              pfnFlipOverlay;
  PFND3DDDI_GETOVERLAYCOLORCONTROLS                  pfnGetOverlayColorControls;
  PFND3DDDI_SETOVERLAYCOLORCONTROLS                  pfnSetOverlayColorControls;
  PFND3DDDI_DESTROYOVERLAY                           pfnDestroyOverlay;
  PFND3DDDI_DESTROYDEVICE                            pfnDestroyDevice;
  PFND3DDDI_QUERYRESOURCERESIDENCY                   pfnQueryResourceResidency;
  PFND3DDDI_OPENRESOURCE                             pfnOpenResource;
  PFND3DDDI_GETCAPTUREALLOCATIONHANDLE               pfnGetCaptureAllocationHandle;
  PFND3DDDI_CAPTURETOSYSMEM                          pfnCaptureToSysMem;
  PFND3DDDI_LOCKASYNC                                pfnLockAsync;
  PFND3DDDI_UNLOCKASYNC                              pfnUnlockAsync;
  PFND3DDDI_RENAME                                   pfnRename;
  PFND3DDDI_DXVAHD_CREATEVIDEOPROCESSOR              pfnCreateVideoProcessor;
  PFND3DDDI_DXVAHD_SETVIDEOPROCESSBLTSTATE           pfnSetVideoProcessBltState;
  PFND3DDDI_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE    pfnGetVideoProcessBltStatePrivate;
  PFND3DDDI_DXVAHD_SETVIDEOPROCESSSTREAMSTATE        pfnSetVideoProcessStreamState;
  PFND3DDDI_DXVAHD_GETVIDEOPROCESSSTREAMSTATEPRIVATE pfnGetVideoProcessStreamStatePrivate;
  PFND3DDDI_DXVAHD_VIDEOPROCESSBLTHD                 pfnVideoProcessBltHD;
  PFND3DDDI_DXVAHD_DESTROYVIDEOPROCESSOR             pfnDestroyVideoProcessor;
  PFND3DDDI_CREATEAUTHENTICATEDCHANNEL               pfnCreateAuthenticatedChannel;
  PFND3DDDI_AUTHENTICATEDCHANNELKEYEXCHANGE          pfnAuthenticatedChannelKeyExchange;
  PFND3DDDI_QUERYAUTHENTICATEDCHANNEL                pfnQueryAuthenticatedChannel;
  PFND3DDDI_CONFIGUREAUTHENICATEDCHANNEL             pfnConfigureAuthenticatedChannel;
  PFND3DDDI_DESTROYAUTHENTICATEDCHANNEL              pfnDestroyAuthenticatedChannel;
  PFND3DDDI_CREATECRYPTOSESSION                      pfnCreateCryptoSession;
  PFND3DDDI_CRYPTOSESSIONKEYEXCHANGE                 pfnCryptoSessionKeyExchange;
  PFND3DDDI_DESTROYCRYPTOSESSION                     pfnDestroyCryptoSession;
  PFND3DDDI_ENCRYPTIONBLT                            pfnEncryptionBlt;
  PFND3DDDI_GETPITCH                                 pfnGetPitch;
  PFND3DDDI_STARTSESSIONKEYREFRESH                   pfnStartSessionKeyRefresh;
  PFND3DDDI_FINISHSESSIONKEYREFRESH                  pfnFinishSessionKeyRefresh;
  PFND3DDDI_GETENCRYPTIONBLTKEY                      pfnGetEncryptionBltKey;
  PFND3DDDI_DECRYPTIONBLT                            pfnDecryptionBlt;
  PFND3DDDI_RESOLVESHAREDRESOURCE                    pfnResolveSharedResource;
#if (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WIN8)
  PFND3DDDI_VOLBLT1                                  pfnVolBlt1;
  PFND3DDDI_BUFBLT1                                  pfnBufBlt1;
  PFND3DDDI_TEXBLT1                                  pfnTexBlt1;
  PFND3DDDI_DISCARD                                  pfnDiscard;
  PFND3DDDI_OFFERRESOURCES                           pfnOfferResources;
  PFND3DDDI_RECLAIMRESOURCES                         pfnReclaimResources;
  PFND3DDDI_CHECKDIRECTFLIPSUPPORT                   pfnCheckDirectFlipSupport;
  PFND3DDDI_CREATERESOURCE2                          pfnCreateResource2;
  PFND3DDDI_CHECKMULTIPLANEOVERLAYSUPPORT            pfnCheckMultiPlaneOverlaySupport;
  PFND3DDDI_PRESENTMULTIPLANEOVERLAY                 pfnPresentMultiPlaneOverlay;
#endif 
#if (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM1_3)
  void                                               *pfnReserved1;
  PFND3DDDI_FLUSH1                                   pfnFlush1;
  PFND3DDDI_CHECKCOUNTERINFO                         pfnCheckCounterInfo;
  PFND3DDDI_CHECKCOUNTER                             pfnCheckCounter;
  PFND3DDDI_UPDATESUBRESOURCEUP                      pfnUpdateSubresourceUP;
  PFND3DDDI_PRESENT1                                 pfnPresent1;
  PFND3DDDI_CHECKPRESENTDURATIONSUPPORT              pfnCheckPresentDurationSupport;
#endif 
#if (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM1_3)
  PFND3DDDI_SETMARKER                                pfnSetMarker;
  PFND3DDDI_SETMARKERMODE                            pfnSetMarkerMode;
#endif 
} D3DDDI_DEVICEFUNCS;
````


## -struct-fields
<dl>

### -field <b>pfnSetRenderState</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/22fb67f7-cc28-4f10-950d-1379769ddf89">SetRenderState</a> function that updates the render state.</p>
</dd>

### -field <b>pfnUpdateWInfo</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/e9cd87b9-3958-4b10-895d-480e03ebea76">UpdateWInfo</a> function that updates the w range for w buffering.</p>
</dd>

### -field <b>pfnValidateDevice</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/058696e0-be4a-45f3-b3e8-55abccdce3ce">ValidateDevice</a> function that returns the number of passes in which the hardware can perform the blending operations that are specified in the current state. </p>
</dd>

### -field <b>pfnSetTextureStageState</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/56b9d7bf-1036-4ad1-a0fb-4d7154b50b27">SetTextureStageState</a> function that updates the state of a texture at a particular stage in a multiple-texture group.</p>
</dd>

### -field <b>pfnSetTexture</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/b2ed86c5-cd4f-4aaa-a062-4c7ae4e088df">SetTexture</a> function that sets a texture to a particular stage in a multiple-texture group.</p>
</dd>

### -field <b>pfnSetPixelShader</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/b7ffd96d-086e-445a-89cf-6f34a5b8a5d4">SetPixelShader</a> function that sets the current pixel shader.</p>
</dd>

### -field <b>pfnSetPixelShaderConst</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/02710936-28df-4c8f-aa1e-bdff01155608">SetPixelShaderConst</a> function that sets one or more pixel shader constant registers with float values.</p>
</dd>

### -field <b>pfnSetStreamSourceUm</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/75a70801-0338-45ed-a691-5f84202575d5">SetStreamSourceUM</a> function that binds a vertex stream source to a user memory buffer.</p>
</dd>

### -field <b>pfnSetIndices</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/5348b3f9-78c5-4915-ba68-296d6f9f916c">SetIndices</a> function that sets the current index buffer.</p>
</dd>

### -field <b>pfnSetIndicesUm</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/9ca38004-8953-4416-8552-c76813192561">SetIndicesUM</a> function that binds an index buffer to a user memory buffer.</p>
</dd>

### -field <b>pfnDrawPrimitive</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/1a6de2b0-cab0-4fcf-be1b-a8cc1c1f79e9">DrawPrimitive</a> function that draws nonindexed primitives in which the Microsoft Direct3D runtime has not transformed the vertex data.</p>
</dd>

### -field <b>pfnDrawIndexedPrimitive</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/12bb6274-d042-43bb-b9f5-1417f42da729">DrawIndexedPrimitive</a> function that draws indexed primitives in which the Direct3D runtime has not transformed the vertex data.</p>
</dd>

### -field <b>pfnDrawRectPatch</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/c0e3046c-f2af-4406-ac5a-c3e44f40b1fd">DrawRectPatch</a> function that draws a new or cached rectangular patch or updates the specification of a previously defined patch.</p>
</dd>

### -field <b>pfnDrawTriPatch</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/98e5f2c5-2795-4226-b5c0-9498b37c22df">DrawTriPatch</a> function that draws a new or cached triangular patch or updates the specification of a previously defined patch.</p>
</dd>

### -field <b>pfnDrawPrimitive2</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/a81080f0-fbb3-4616-9324-642b60befcb3">DrawPrimitive2</a> function that draws nonindexed primitives in which the Direct3D runtime has transformed the vertex data.</p>
</dd>

### -field <b>pfnDrawIndexedPrimitive2</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/f12af70c-a6f2-42da-be62-1cfeb90b6239">DrawIndexedPrimitive2</a> function that draws indexed primitives in which the Direct3D runtime has transformed the vertex data.</p>
</dd>

### -field <b>pfnVolBlt</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/249a55a3-f2cf-4838-8a0f-b7108a17cd78">VolBlt</a> function that performs a bit-block transfer (bitblt) from a source volume texture to a destination volume texture.</p>
</dd>

### -field <b>pfnBufBlt</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/d75f3fad-3bcd-44ad-9bd5-f61f5346cf8d">BufBlt</a> function that performs a bitblt from a source vertex or index buffer to a destination vertex or index buffer.</p>
</dd>

### -field <b>pfnTexBlt</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/1ddfd822-7a43-4976-a153-ba862d6dfd82">TexBlt</a> function that performs a bitblt from a source texture to a destination texture.</p>
</dd>

### -field <b>pfnStateSet</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/2c298de6-a3d9-45c7-ab60-dc9124eed1bb">StateSet</a> function that performs a state-set operation.</p>
</dd>

### -field <b>pfnSetPriority</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/61ac2d28-7aed-4796-8d09-591db936013b">SetPriority</a> function that sets the eviction-from-memory priority for a managed texture.</p>
</dd>

### -field <b>pfnClear</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/library/windows/hardware/hh406339">Clear</a> function that performs hardware-assisted clearing on the rendering target, depth buffer, or stencil buffer.</p>
</dd>

### -field <b>pfnUpdatePalette</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/7c22e0c9-cc24-4398-88b7-c91855cbc731">UpdatePalette</a> function that updates a texture palette.</p>
</dd>

### -field <b>pfnSetPalette</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/5d1c8c2d-7886-4876-b48e-1e6b252ae8f7">SetPalette</a> function that sets the palette for a texture.</p>
</dd>

### -field <b>pfnSetVertexShaderConst</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/2dbde343-b10a-4357-a2b7-d6b1b1b868f2">SetVertexShaderConst</a> function that sets one or more vertex shader constant registers with float values.</p>
</dd>

### -field <b>pfnMultiplyTransform</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/69d94062-5655-4d49-a116-7fa7e2b51a91">MultiplyTransform</a> function that multiplies a current transform.</p>
</dd>

### -field <b>pfnSetTransform</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/0e989ea4-3693-4c0b-86a5-96b865a0193f">SetTransform</a> function that sets up a transform.</p>
</dd>

### -field <b>pfnSetViewport</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/ef0847a3-d4f5-4a9e-a041-1b8f8523fdf7">SetViewport</a> function that informs guard-band aware drivers of the view-clipping rectangle.</p>
</dd>

### -field <b>pfnSetZRange</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/29ccde7c-801c-4e90-bc39-8581f262cc65">SetZRange</a> function that informs the driver about the range of z values.</p>
</dd>

### -field <b>pfnSetMaterial</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/e1273478-a450-44fa-95d5-ee86cb3a46b2">SetMaterial</a> function that sets the material properties that devices on the system use to create the required effect during rendering.</p>
</dd>

### -field <b>pfnSetLight</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/28e3992e-a636-47e2-a5a6-5da06d276b5c">SetLight</a> function that sets properties for a light source.</p>
</dd>

### -field <b>pfnCreateLight</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/4649b1d1-6fd3-48fb-b25f-1228851bb682">CreateLight</a> function that creates a light source.</p>
</dd>

### -field <b>pfnDestroyLight</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/dbc86e4d-a002-4270-a3c4-02d16972c921">DestroyLight</a> function that deactivates a light source.</p>
</dd>

### -field <b>pfnSetClipPlane</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/99edfc35-23a5-41e0-8705-7dffba564c10">SetClipPlane</a> function that sets a clip plane.</p>
</dd>

### -field <b>pfnGetInfo</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/library/windows/hardware/hh451309">GetInfo</a> function that retrieves information about the device.</p>
</dd>

### -field <b>pfnLock</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/e2289073-d46a-4a12-8de7-30400e04cc22">Lock</a> function that locks a resource or a surface within the resource.</p>
</dd>

### -field <b>pfnUnlock</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/23cc9c64-99d4-4602-a1b0-234fe7fcc3da">Unlock</a> function that unlocks a resource or a surface within the resource that the <a href="https://msdn.microsoft.com/e2289073-d46a-4a12-8de7-30400e04cc22">Lock</a> function previously locked.</p>
</dd>

### -field <b>pfnCreateResource</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/5b74c989-1a62-4415-a19a-dd0ba2fcff83">CreateResource</a> function that creates a resource.</p>
</dd>

### -field <b>pfnDestroyResource</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/1af85315-4367-49de-9453-eef62c838c97">DestroyResource</a> function that releases the resource that the <a href="https://msdn.microsoft.com/5b74c989-1a62-4415-a19a-dd0ba2fcff83">CreateResource</a> function created.</p>
</dd>

### -field <b>pfnSetDisplayMode</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/d0e409fe-1c64-4468-b52e-b0ede39f6601">SetDisplayMode</a> function that sets a surface for displaying.</p>
</dd>

### -field <b>pfnPresent</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/e90683b4-64b6-4018-96a5-b50118df3367">Present</a> function that requests that the source surface be displayed by either copying or flipping. </p>
</dd>

### -field <b>pfnFlush</b>

<dd>
<p>A pointer to the user-mode display driver <a href="https://msdn.microsoft.com/library/windows/hardware/hh463886">Flush</a> function that submits outstanding hardware commands that are in the hardware command buffer to the display miniport driver.</p>
</dd>

### -field <b>pfnCreateVertexShaderFunc</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/e986d37a-6039-4bc4-b5e8-6c4d4d7adedd">CreateVertexShaderFunc</a> function that converts the vertex shader code into a hardware-specific format and associates this code with the given shader handle.</p>
</dd>

### -field <b>pfnDeleteVertexShaderFunc</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/780fc47c-bbb9-400a-a2f3-cdce4a18072f">DeleteVertexShaderFunc</a> function that cleans up driver-side resources that are associated with vertex shader code.</p>
</dd>

### -field <b>pfnSetVertexShaderFunc</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/2cea4812-7eba-4558-9c2e-30de460be21f">SetVertexShaderFunc</a> function that sets the vertex shader code so that all of the subsequent drawing operations use that code.</p>
</dd>

### -field <b>pfnCreateVertexShaderDecl</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/00c53e81-93db-46b8-b65c-c8d62059452a">CreateVertexShaderDecl</a> function that converts the vertex shader declaration into a hardware-specific format and associates this declaration with the given shader handle.</p>
</dd>

### -field <b>pfnDeleteVertexShaderDecl</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/8c16cd27-83f9-4474-9031-edfea0ba665b">DeleteVertexShaderDecl</a> function that cleans up driver-side resources that are associated with the vertex shader declaration.</p>
</dd>

### -field <b>pfnSetVertexShaderDecl</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/6387d632-78e2-4594-a58a-b11b2e831cc0">SetVertexShaderDecl</a> function that sets the vertex shader declaration so that all of the subsequent drawing operations use that declaration.</p>
</dd>

### -field <b>pfnSetVertexShaderConstI</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/c245cfbd-0368-4a49-96a7-ac4cd14e2f5a">SetVertexShaderConstI</a> function that sets one or more vertex shader constant registers with integer values.</p>
</dd>

### -field <b>pfnSetVertexShaderConstB</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/41ca823e-4370-4cba-9129-067e25a43a69">SetVertexShaderConstB</a> function that sets one or more vertex shader constant registers with Boolean values.</p>
</dd>

### -field <b>pfnSetScissorRect</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/779fd7ff-e4d6-45b4-8164-186e9cb89513">SetScissorRect</a> function that marks a portion of a render target to which rendering is restricted.</p>
</dd>

### -field <b>pfnSetStreamSource</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/669dbabc-91fb-40f9-a034-11c3c2e70436">SetStreamSource</a> function that binds a portion of a vertex stream source to a vertex buffer.</p>
</dd>

### -field <b>pfnSetStreamSourceFreq</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/92cb270c-1548-4239-81cd-5b3483769fc8">SetStreamSourceFreq</a> function that sets the frequency divisor of a stream source that is bound to a vertex buffer.</p>
</dd>

### -field <b>pfnSetConvolutionKernelMono</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/b560352f-ca4e-4f03-88ac-13ec080834aa">SetConvolutionKernelMono</a> function that sets the monochrome convolution kernel.</p>
</dd>

### -field <b>pfnComposeRects</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/b6a6b549-7590-4b27-b759-631fa62a76d2">ComposeRects</a> function that composes rectangular areas.</p>
</dd>

### -field <b>pfnBlt</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/e87576c6-0173-4d8e-bbaf-b82e2907140a">Blt</a> function that copies the contents of a source surface to a destination surface.</p>
</dd>

### -field <b>pfnColorFill</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/c120421d-6a10-4d37-b936-98dac75e236b">ColorFill</a> function that fills a rectangular area on a surface with a particular A8R8G8B8 color.</p>
</dd>

### -field <b>pfnDepthFill</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/fc889cc0-d71d-4a81-8fa5-894c676ac110">DepthFill</a> function that fills a depth buffer with a pixel value that is specified in native format.</p>
</dd>

### -field <b>pfnCreateQuery</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/ac63b77b-2704-4d5b-bf1d-9d85e8a1e336">CreateQuery</a> function that creates driver-side resources for a query that the Direct3D runtime subsequently issues for processing.</p>
</dd>

### -field <b>pfnDestroyQuery</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/c4cef278-1771-4903-a5cf-85674463aff8">DestroyQuery</a> function that releases resources for the query that the <a href="https://msdn.microsoft.com/ac63b77b-2704-4d5b-bf1d-9d85e8a1e336">CreateQuery</a> function created.</p>
</dd>

### -field <b>pfnIssueQuery</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/e31b2b6a-3721-472a-8044-6516a8419ad3">IssueQuery</a> function that processes the query that the <a href="https://msdn.microsoft.com/ac63b77b-2704-4d5b-bf1d-9d85e8a1e336">CreateQuery</a> function created.</p>
</dd>

### -field <b>pfnGetQueryData</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/64daec14-8e16-4df3-bb0c-27760223b86c">GetQueryData</a> function that retrieves information about a query.</p>
</dd>

### -field <b>pfnSetRenderTarget</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/067378bd-a2d8-4c83-9436-531519eadaa3">SetRenderTarget</a> function that sets the render target surface in the driver's context.</p>
</dd>

### -field <b>pfnSetDepthStencil</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/7c4b01c8-2376-4956-9b18-649647c19b2b">SetDepthStencil</a> function that sets the depth buffer in the driver's context.</p>
</dd>

### -field <b>pfnGenerateMipSubLevels</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/86567fc1-cf66-4709-a6e1-6b24408df963">GenerateMipSubLevels</a> function that regenerates the sublevels of a MIP-map texture.</p>
</dd>

### -field <b>pfnSetPixelShaderConstI</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/fafc046e-0595-4901-bfb1-70bd980388bc">SetPixelShaderConstI</a> function that sets one or more pixel shader constant registers with integer values.</p>
</dd>

### -field <b>pfnSetPixelShaderConstB</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/6f7c8932-9332-4ff2-89ab-2f9a66783326">SetPixelShaderConstB</a> function that sets one or more pixel shader constant registers with Boolean values.</p>
</dd>

### -field <b>pfnCreatePixelShader</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/b80a1823-6d91-440f-89e4-f7248579cc8f">CreatePixelShader</a> function that converts the pixel shader code into a hardware-specific format and associates this code with a shader handle.</p>
</dd>

### -field <b>pfnDeletePixelShader</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/bc987531-d402-4f3b-a4e2-d71fe97f5400">DeletePixelShader</a> function that cleans up driver-side resources that are associated with pixel shader code.</p>
</dd>

### -field <b>pfnCreateDecodeDevice</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/4d9a062a-2fdf-4e55-a335-c03c5d5665ff">CreateDecodeDevice</a> function that creates a representation of a Microsoft DirectX Video Acceleration (VA) decode device from supplied parameters.</p>
</dd>

### -field <b>pfnDestroyDecodeDevice</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/3685e58b-8d67-4b01-a8a0-8a794d653637">DestroyDecodeDevice</a> function that releases resources for a DirectX VA decode device.</p>
</dd>

### -field <b>pfnSetDecodeRenderTarget</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/d522b0f3-ca9c-4e79-96ad-ea9477858ef4">SetDecodeRenderTarget</a> function that sets the render target for decoding. <i>SetDecodeRenderTarget</i> can be called only outside of a <a href="https://msdn.microsoft.com/3e6153aa-7b21-429d-8908-1ff3a4d25e17">DecodeBeginFrame</a>/<a href="https://msdn.microsoft.com/6e8d3280-6ddc-4593-9208-c4f0c9ff254c">DecodeEndFrame</a> block.</p>
</dd>

### -field <b>pfnDecodeBeginFrame</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/3e6153aa-7b21-429d-8908-1ff3a4d25e17">DecodeBeginFrame</a> function that indicates that decoding of a frame can begin.</p>
</dd>

### -field <b>pfnDecodeEndFrame</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/6e8d3280-6ddc-4593-9208-c4f0c9ff254c">DecodeEndFrame</a> function that indicates that frame decoding operations must be completed.</p>
</dd>

### -field <b>pfnDecodeExecute</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/e12496c0-e3e4-437e-9f84-a30ee99b4541">DecodeExecute</a> function that performs a DirectX VA decode operation. <i>DecodeExecute</i> must be called inside a <a href="https://msdn.microsoft.com/3e6153aa-7b21-429d-8908-1ff3a4d25e17">DecodeBeginFrame</a>/<a href="https://msdn.microsoft.com/6e8d3280-6ddc-4593-9208-c4f0c9ff254c">DecodeEndFrame</a> block.</p>
</dd>

### -field <b>pfnDecodeExtensionExecute</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/522a552a-4588-4dd1-b81f-73ccd4a1c0aa">DecodeExtensionExecute</a> function that performs a nonstandard DirectX VA decode operation. <i>DecodeExtensionExecute</i> must be called inside a <a href="https://msdn.microsoft.com/3e6153aa-7b21-429d-8908-1ff3a4d25e17">DecodeBeginFrame</a>/<a href="https://msdn.microsoft.com/6e8d3280-6ddc-4593-9208-c4f0c9ff254c">DecodeEndFrame</a> block.</p>
</dd>

### -field <b>pfnCreateVideoProcessDevice</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/3149c7d9-0bf7-4355-8f15-821cf6b92f0a">CreateVideoProcessDevice</a> function that creates a representation of a DirectX VA video processing device from supplied parameters.</p>
</dd>

### -field <b>pfnDestroyVideoProcessDevice</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/dc0f8dba-afdd-47f4-ba7f-72c510e80052">DestroyVideoProcessDevice</a> function that releases resources for a DirectX VA video processing device.</p>
</dd>

### -field <b>pfnVideoProcessBeginFrame</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/1b7b1774-3144-4929-83d8-c52a7de6936d">VideoProcessBeginFrame</a> function that indicates that video processing of a frame can begin.</p>
</dd>

### -field <b>pfnVideoProcessEndFrame</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/a5be6834-bb27-4da0-8802-25a9ca58c101">VideoProcessEndFrame</a> function that indicates that video processing operations must be completed.</p>
</dd>

### -field <b>pfnSetVideoProcessRenderTarget</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/8aa7e23e-f52e-4252-9f22-56ce523f6cba">SetVideoProcessRenderTarget</a> function that sets the render target for video processing. <i>SetVideoProcessRenderTarget</i> can be called only outside of a <a href="https://msdn.microsoft.com/1b7b1774-3144-4929-83d8-c52a7de6936d">VideoProcessBeginFrame</a>/<a href="https://msdn.microsoft.com/a5be6834-bb27-4da0-8802-25a9ca58c101">VideoProcessEndFrame</a> block.</p>
</dd>

### -field <b>pfnVideoProcessBlt</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/719465dd-4547-491c-ab30-ae63bba1b72c">VideoProcessBlt</a> function that processes DirectX VA video. <i>VideoProcessBlt</i> must be called inside a <a href="https://msdn.microsoft.com/1b7b1774-3144-4929-83d8-c52a7de6936d">VideoProcessBeginFrame</a>/<a href="https://msdn.microsoft.com/a5be6834-bb27-4da0-8802-25a9ca58c101">VideoProcessEndFrame</a> block.</p>
</dd>

### -field <b>pfnCreateExtensionDevice</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/7e6dbb70-2e74-4ddb-a504-2c8145af99d9">CreateExtensionDevice</a> function that creates a representation of a DirectX VA extension device from supplied parameters.</p>
</dd>

### -field <b>pfnDestroyExtensionDevice</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/8c4bcab3-b903-4f39-aab0-7efb3b18d068">DestroyExtensionDevice</a> function that releases resources for a DirectX VA extension device.</p>
</dd>

### -field <b>pfnExtensionExecute</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/a3f73651-bfff-48fa-aa61-477b8af7fa07">ExtensionExecute</a> function that performs an operation that is specific to the given DirectX VA extension device.</p>
</dd>

### -field <b>pfnCreateOverlay</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/761377ff-95a6-426b-8372-3f347870f9c4">CreateOverlay</a> function that allocates overlay hardware and makes the overlay visible.</p>
</dd>

### -field <b>pfnUpdateOverlay</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/80d7cc5c-51d8-4b91-9581-b073f9b0e68a">UpdateOverlay</a> function that reconfigures or moves an overlay that is being displayed.</p>
</dd>

### -field <b>pfnFlipOverlay</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/8490ebdd-f993-4c77-b6da-d57ef5e5d05f">FlipOverlay</a> function that causes the overlay hardware to start displaying the new allocation.</p>
</dd>

### -field <b>pfnGetOverlayColorControls</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/23b15bb5-4394-406b-8869-f9d1e4e2b539">GetOverlayColorControls</a> function that retrieves color-control settings for an overlay.</p>
</dd>

### -field <b>pfnSetOverlayColorControls</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/c2723c57-44eb-4866-9381-a3a341996989">SetOverlayColorControls</a> function that changes color-control settings for an overlay.</p>
</dd>

### -field <b>pfnDestroyOverlay</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/63004d19-e2cd-462c-8fa5-ea4dd6e29735">DestroyOverlay</a> function that disables the overlay hardware and frees the overlay handle.</p>
</dd>

### -field <b>pfnDestroyDevice</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/a3c158c2-6c0d-4da0-80f4-569971b10673">DestroyDevice</a> function that releases resources for the display device.</p>
</dd>

### -field <b>pfnQueryResourceResidency</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/5b9a2a59-b2d1-468e-998b-902bc2a75cb3">QueryResourceResidency</a> function that determines the residency of resources.</p>
</dd>

### -field <b>pfnOpenResource</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/e3f5cec2-391b-40f9-8a4b-afe6b8de2954">OpenResource</a> function that informs the driver that a shared resource is opened.</p>
</dd>

### -field <b>pfnGetCaptureAllocationHandle</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/fb12a12b-6fb7-46d4-aa71-4c88d34d6ff9">GetCaptureAllocationHandle</a> function that maps the given capture resource to an allocation.</p>
</dd>

### -field <b>pfnCaptureToSysMem</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/ea2b5338-81cf-4114-bb07-16e8ff4d2b95">CaptureToSysMem</a> function that copies a capture buffer to a video memory surface.</p>
</dd>

### -field <b>pfnLockAsync</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/c8f76ebe-947a-45e4-abbc-f6020da929e8">LockAsync</a> function that locks a resource or a surface within the resource.</p>
</dd>

### -field <b>pfnUnlockAsync</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/6af04c22-e559-4328-a20a-034b443fddc6">UnlockAsync</a> function that unlocks a resource or a surface within the resource that the <a href="https://msdn.microsoft.com/c8f76ebe-947a-45e4-abbc-f6020da929e8">LockAsync</a> function previously locked.</p>
</dd>

### -field <b>pfnRename</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/60f733e1-d376-4372-b1cc-39508b3a98e5">Rename</a> function that renames, with a new allocation, a resource or a surface within the resource.</p>
</dd>

### -field <b>pfnCreateVideoProcessor</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/68a7c394-4b0f-4446-a54b-5aee6cf8a913">CreateVideoProcessor</a> function that creates a video processor.</p>
</dd>

### -field <b>pfnSetVideoProcessBltState</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/6796372c-279d-427c-a2a4-9b7c99494f53">SetVideoProcessBltState</a> function that sets the state of a bitblt for a video processor. </p>
</dd>

### -field <b>pfnGetVideoProcessBltStatePrivate</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/bb4c04cf-0125-47bf-8fc8-88d807e7b6ad">GetVideoProcessBltStatePrivate</a> function that retrieves the state data of a private bitblt for a video processor. </p>
</dd>

### -field <b>pfnSetVideoProcessStreamState</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/b48fbe58-056a-4c3b-8e1e-c65515c21ee4">SetVideoProcessStreamState</a> function that sets the state of a stream for a video processor. </p>
</dd>

### -field <b>pfnGetVideoProcessStreamStatePrivate</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/0503b382-8ed3-461e-906f-27953ac5f757">GetVideoProcessStreamStatePrivate</a> function that retrieves the private stream-state data for a video processor. </p>
</dd>

### -field <b>pfnVideoProcessBltHD</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/62451fc4-92cc-4553-80cc-0843cf734a62">VideoProcessBltHD</a> function that processes video input streams and composes to an output surface. </p>
</dd>

### -field <b>pfnDestroyVideoProcessor</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/library/windows/hardware/hh451638">DestroyVideoProcessor</a> function that releases resources for a previously created video processor. </p>
</dd>

### -field <b>pfnCreateAuthenticatedChannel</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/0a565bff-fc6f-41c1-a6fd-3a82dd0d7889">CreateAuthenticatedChannel</a> function that creates a channel that the Direct3D runtime and the driver can use to set and query protections. </p>
</dd>

### -field <b>pfnAuthenticatedChannelKeyExchange</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/627f9689-1059-4f88-9005-9c7600dad686">AuthenticatedChannelKeyExchange</a> function that negotiates the session key. </p>
</dd>

### -field <b>pfnQueryAuthenticatedChannel</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/13b65b5a-9512-4d67-b629-479bdd74674e">QueryAuthenticatedChannel</a> function that queries an authenticated channel for capability and state information. </p>
</dd>

### -field <b>pfnConfigureAuthenticatedChannel</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/95485e96-fa4f-4c88-b88b-97b79f507abd">ConfigureAuthenticatedChannel</a> function that sets the state within an authenticated channel. </p>
</dd>

### -field <b>pfnDestroyAuthenticatedChannel</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/library/windows/hardware/hh451630">DestroyAuthenticatedChannel</a> function that releases resources for an authenticated channel. </p>
</dd>

### -field <b>pfnCreateCryptoSession</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a> function that creates an encryption session. </p>
</dd>

### -field <b>pfnCryptoSessionKeyExchange</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/f8055bb3-b8f1-47f5-9ae0-8e7a26989871">CryptoSessionKeyExchange</a> function that performs a key exchange during an encryption session. </p>
</dd>

### -field <b>pfnDestroyCryptoSession</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/library/windows/hardware/hh451632">DestroyCryptoSession</a> function that releases resources for an encryption session. </p>
</dd>

### -field <b>pfnEncryptionBlt</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/a92bfff7-8af6-48c3-9e7f-95b9426aaaf2">EncryptionBlt</a> function that performs an encrypted bitblt operation. </p>
</dd>

### -field <b>pfnGetPitch</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/1a5721a3-c03f-4827-9626-c9b6af5059a1">GetPitch</a> function that retrieves the pitch of an encrypted surface. </p>
</dd>

### -field <b>pfnStartSessionKeyRefresh</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/library/windows/hardware/hh451696">StartSessionKeyRefresh</a> function that sets the current video session to protected mode. </p>
</dd>

### -field <b>pfnFinishSessionKeyRefresh</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/library/windows/hardware/hh451648">FinishSessionKeyRefresh</a> function that sets the current video session to unprotected mode. </p>
</dd>

### -field <b>pfnGetEncryptionBltKey</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/library/windows/hardware/hh451660">GetEncryptionBltKey</a> function that retrieves the key of an encrypted bitblt session. </p>
</dd>

### -field <b>pfnDecryptionBlt</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/1bfe2b9c-90f6-48bf-b0b3-30788ef94110">DecryptionBlt</a> function that writes data to a protected surface. </p>
</dd>

### -field <b>pfnResolveSharedResource</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/8ad9130e-bade-4fd2-b345-b6361fd001ef">ResolveSharedResource</a> function that resolves a shared resource. </p>
</dd>

### -field <b>pfnVolBlt1</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/81B9AB74-9CD1-4181-BE13-32D519069FD4">VolBlt1</a> function that performs a volume bit-block transfer (bitblt) operation.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnBufBlt1</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/92F2AED7-935F-4E3E-934F-D6DF9AA87495">BufBlt1</a> function that performs a bit-block transfer (bitblt) operation.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnTexBlt1</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/63EE8130-47E5-4976-8A72-1B11136B1192">TexBlt1</a> function that performs a texture bit-block transfer (bitblt) operation.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnDiscard</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/F3EC7AAE-9DB8-43A1-B756-5F5C91F8372E">Discard</a>  function that discards (evicts) a set of subresources from video display memory.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnOfferResources</b>

<dd>
<p>A pointer to the driver  <a href="https://msdn.microsoft.com/68551AD7-AC0C-4138-948F-33773F02DA41">OfferResources</a> function that requests that the user-mode display driver offer video memory resources for reuse.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnReclaimResources</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/F0533DBB-CB18-4556-9871-2DF4CA719172">ReclaimResources</a> function that's called by the Direct3D runtime to reclaim video memory resources that it previously offered for reuse.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnCheckDirectFlipSupport</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/BB909041-0194-4828-ACA2-E3F6B1974DBB">CheckDirectFlipSupport</a> function that's called by the DWM to verify that the user-mode driver supports Direct Flip operations.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnCreateResource2</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/a8326707-cffc-4a20-ad3d-c7862661f513">CreateResource2</a> function that creates a resource.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnCheckMultiPlaneOverlaySupport</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/A439E695-D374-439A-8A69-6D4E247FF134">pfnCheckMultiPlaneOverlaySupport (D3D)</a> function that's called by the Direct3D runtime to check the details on hardware support for multiplane overlays.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnPresentMultiPlaneOverlay</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/3AC47977-A5F3-44A6-8F89-A1EA5E0BB6E4">pfnPresentMultiplaneOverlay (D3D)</a> function that's called by the Direct3D runtime to notify the user-mode display driver that an application finished rendering and requests that the driver display the source surface by either copying or flipping or that the driver perform a color-fill operation.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnReserved1</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnFlush1</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/6BAC104A-85CE-42FC-AE30-969B2FF6AFEF">pfnFlush1</a>  function that's called by the Direct3D runtime to submit outstanding hardware commands that are in the hardware command buffer to the display miniport driver.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnCheckCounterInfo</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/98B8EE79-18D2-4C57-964B-74DB550C1330">pfnCheckCounterInfo</a>  function that's called by the Direct3D runtime to determine global information that's related to manipulating counters.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnCheckCounter</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/3A8B040D-7B48-4CDB-985B-906AE1762E22">pfnCheckCounter</a>  function that's called by the Direct3D runtime to retrieve info that describes a counter.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnUpdateSubresourceUP</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/5AF55FED-6FD6-41BE-A743-1E9D0EA51C9C">pfnUpdateSubresourceUP</a>  function that's called by the Direct3D runtime to update a destination subresource region from a source system-memory region.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnPresent1</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/8BB8E85F-B081-422E-ACE1-C2312BA28B9F">pfnPresent1(D3D)</a>  function that notifies the user-mode display driver that an application finished rendering and  that all ownership of the shared resource is released, and that  requests that the driver display to the destination surface.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnCheckPresentDurationSupport</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/4D3FC503-A502-41D3-AB76-5A2BEBE4C551">CheckPresentDurationSupport</a> function that's called by the Direct3D runtime to request that the user-mode display driver get hardware device capabilities for seamlessly switching to a new monitor refresh rate.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnSetMarker</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/6D4DB988-D339-4B2F-A9B8-41B4FD21FE66">pfnSetMarker</a> function that notifies the user-mode display driver that it must generate a new time stamp if any GPU work has completed since the last call to <i>pfnSetMarker</i>.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnSetMarkerMode</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/D45750D9-F722-4208-8D00-E14FD9C009CB">pfnSetMarkerMode</a> function that notifies the user-mode display driver that it should support a type of Event Tracing for Windows (ETW) marker event.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>
</dl>

## -remarks
<p>The following code, from D3dumddi.h, shows the function declarations for the functions that the members of <b>D3DDDI_DEVICEFUNCS</b> point to. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/ce35bdac-af90-471f-af93-0e665be6c7f6">CreateDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542931">D3DDDIARG_CREATEDEVICE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_DEVICEFUNCS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
