---
UID: NS.d3dumddi._D3DDDI_DEVICEFUNCS
title: D3DDDI_DEVICEFUNCS
author: windows-driver-content
description: The D3DDDI_DEVICEFUNCS structure contains functions that the user-mode display driver can implement to render graphics primitives and process state changes.
old-location: display\d3dddi_devicefuncs.htm
old-project: display
ms.assetid: 7345cd67-c10c-46f0-bd56-6f18929f4aa6
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_DEVICEFUNCS, D3DDDI_DEVICEFUNCS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setrenderstate.md">SetRenderState</a> function that updates the render state.</p>
</dd>

### -field <b>pfnUpdateWInfo</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-updatewinfo.md">UpdateWInfo</a> function that updates the w range for w buffering.</p>
</dd>

### -field <b>pfnValidateDevice</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-validatedevice.md">ValidateDevice</a> function that returns the number of passes in which the hardware can perform the blending operations that are specified in the current state. </p>
</dd>

### -field <b>pfnSetTextureStageState</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-settexturestagestate.md">SetTextureStageState</a> function that updates the state of a texture at a particular stage in a multiple-texture group.</p>
</dd>

### -field <b>pfnSetTexture</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-settexture.md">SetTexture</a> function that sets a texture to a particular stage in a multiple-texture group.</p>
</dd>

### -field <b>pfnSetPixelShader</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setpixelshader.md">SetPixelShader</a> function that sets the current pixel shader.</p>
</dd>

### -field <b>pfnSetPixelShaderConst</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setpixelshaderconst.md">SetPixelShaderConst</a> function that sets one or more pixel shader constant registers with float values.</p>
</dd>

### -field <b>pfnSetStreamSourceUm</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setstreamsourceum.md">SetStreamSourceUM</a> function that binds a vertex stream source to a user memory buffer.</p>
</dd>

### -field <b>pfnSetIndices</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setindices.md">SetIndices</a> function that sets the current index buffer.</p>
</dd>

### -field <b>pfnSetIndicesUm</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setindicesum.md">SetIndicesUM</a> function that binds an index buffer to a user memory buffer.</p>
</dd>

### -field <b>pfnDrawPrimitive</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-drawprimitive.md">DrawPrimitive</a> function that draws nonindexed primitives in which the Microsoft Direct3D runtime has not transformed the vertex data.</p>
</dd>

### -field <b>pfnDrawIndexedPrimitive</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-drawindexedprimitive.md">DrawIndexedPrimitive</a> function that draws indexed primitives in which the Direct3D runtime has not transformed the vertex data.</p>
</dd>

### -field <b>pfnDrawRectPatch</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-drawrectpatch.md">DrawRectPatch</a> function that draws a new or cached rectangular patch or updates the specification of a previously defined patch.</p>
</dd>

### -field <b>pfnDrawTriPatch</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-drawtripatch.md">DrawTriPatch</a> function that draws a new or cached triangular patch or updates the specification of a previously defined patch.</p>
</dd>

### -field <b>pfnDrawPrimitive2</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-drawprimitive2.md">DrawPrimitive2</a> function that draws nonindexed primitives in which the Direct3D runtime has transformed the vertex data.</p>
</dd>

### -field <b>pfnDrawIndexedPrimitive2</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-drawindexedprimitive2.md">DrawIndexedPrimitive2</a> function that draws indexed primitives in which the Direct3D runtime has transformed the vertex data.</p>
</dd>

### -field <b>pfnVolBlt</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-volblt.md">VolBlt</a> function that performs a bit-block transfer (bitblt) from a source volume texture to a destination volume texture.</p>
</dd>

### -field <b>pfnBufBlt</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-bufblt.md">BufBlt</a> function that performs a bitblt from a source vertex or index buffer to a destination vertex or index buffer.</p>
</dd>

### -field <b>pfnTexBlt</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-texblt.md">TexBlt</a> function that performs a bitblt from a source texture to a destination texture.</p>
</dd>

### -field <b>pfnStateSet</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-stateset.md">StateSet</a> function that performs a state-set operation.</p>
</dd>

### -field <b>pfnSetPriority</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setpriority.md">SetPriority</a> function that sets the eviction-from-memory priority for a managed texture.</p>
</dd>

### -field <b>pfnClear</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/library/windows/hardware/hh406339">Clear</a> function that performs hardware-assisted clearing on the rendering target, depth buffer, or stencil buffer.</p>
</dd>

### -field <b>pfnUpdatePalette</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-updatepalette.md">UpdatePalette</a> function that updates a texture palette.</p>
</dd>

### -field <b>pfnSetPalette</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setpalette.md">SetPalette</a> function that sets the palette for a texture.</p>
</dd>

### -field <b>pfnSetVertexShaderConst</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setvertexshaderconst.md">SetVertexShaderConst</a> function that sets one or more vertex shader constant registers with float values.</p>
</dd>

### -field <b>pfnMultiplyTransform</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-multiplytransform.md">MultiplyTransform</a> function that multiplies a current transform.</p>
</dd>

### -field <b>pfnSetTransform</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-settransform.md">SetTransform</a> function that sets up a transform.</p>
</dd>

### -field <b>pfnSetViewport</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setviewport.md">SetViewport</a> function that informs guard-band aware drivers of the view-clipping rectangle.</p>
</dd>

### -field <b>pfnSetZRange</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setzrange.md">SetZRange</a> function that informs the driver about the range of z values.</p>
</dd>

### -field <b>pfnSetMaterial</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setmaterial.md">SetMaterial</a> function that sets the material properties that devices on the system use to create the required effect during rendering.</p>
</dd>

### -field <b>pfnSetLight</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setlight.md">SetLight</a> function that sets properties for a light source.</p>
</dd>

### -field <b>pfnCreateLight</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createlight.md">CreateLight</a> function that creates a light source.</p>
</dd>

### -field <b>pfnDestroyLight</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroylight.md">DestroyLight</a> function that deactivates a light source.</p>
</dd>

### -field <b>pfnSetClipPlane</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setclipplane.md">SetClipPlane</a> function that sets a clip plane.</p>
</dd>

### -field <b>pfnGetInfo</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/library/windows/hardware/hh451309">GetInfo</a> function that retrieves information about the device.</p>
</dd>

### -field <b>pfnLock</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lock.md">Lock</a> function that locks a resource or a surface within the resource.</p>
</dd>

### -field <b>pfnUnlock</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-unlock.md">Unlock</a> function that unlocks a resource or a surface within the resource that the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lock.md">Lock</a> function previously locked.</p>
</dd>

### -field <b>pfnCreateResource</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createresource.md">CreateResource</a> function that creates a resource.</p>
</dd>

### -field <b>pfnDestroyResource</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroyresource.md">DestroyResource</a> function that releases the resource that the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createresource.md">CreateResource</a> function created.</p>
</dd>

### -field <b>pfnSetDisplayMode</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setdisplaymode.md">SetDisplayMode</a> function that sets a surface for displaying.</p>
</dd>

### -field <b>pfnPresent</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-present.md">Present</a> function that requests that the source surface be displayed by either copying or flipping. </p>
</dd>

### -field <b>pfnFlush</b>

<dd>
<p>A pointer to the user-mode display driver <a href="https://msdn.microsoft.com/library/windows/hardware/hh463886">Flush</a> function that submits outstanding hardware commands that are in the hardware command buffer to the display miniport driver.</p>
</dd>

### -field <b>pfnCreateVertexShaderFunc</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createvertexshaderfunc.md">CreateVertexShaderFunc</a> function that converts the vertex shader code into a hardware-specific format and associates this code with the given shader handle.</p>
</dd>

### -field <b>pfnDeleteVertexShaderFunc</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-deletevertexshaderfunc.md">DeleteVertexShaderFunc</a> function that cleans up driver-side resources that are associated with vertex shader code.</p>
</dd>

### -field <b>pfnSetVertexShaderFunc</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setvertexshaderfunc.md">SetVertexShaderFunc</a> function that sets the vertex shader code so that all of the subsequent drawing operations use that code.</p>
</dd>

### -field <b>pfnCreateVertexShaderDecl</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createvertexshaderdecl.md">CreateVertexShaderDecl</a> function that converts the vertex shader declaration into a hardware-specific format and associates this declaration with the given shader handle.</p>
</dd>

### -field <b>pfnDeleteVertexShaderDecl</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-deletevertexshaderdecl.md">DeleteVertexShaderDecl</a> function that cleans up driver-side resources that are associated with the vertex shader declaration.</p>
</dd>

### -field <b>pfnSetVertexShaderDecl</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setvertexshaderdecl.md">SetVertexShaderDecl</a> function that sets the vertex shader declaration so that all of the subsequent drawing operations use that declaration.</p>
</dd>

### -field <b>pfnSetVertexShaderConstI</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setvertexshaderconst.md">SetVertexShaderConstI</a> function that sets one or more vertex shader constant registers with integer values.</p>
</dd>

### -field <b>pfnSetVertexShaderConstB</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setvertexshaderconstb.md">SetVertexShaderConstB</a> function that sets one or more vertex shader constant registers with Boolean values.</p>
</dd>

### -field <b>pfnSetScissorRect</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setscissorrect.md">SetScissorRect</a> function that marks a portion of a render target to which rendering is restricted.</p>
</dd>

### -field <b>pfnSetStreamSource</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setstreamsource.md">SetStreamSource</a> function that binds a portion of a vertex stream source to a vertex buffer.</p>
</dd>

### -field <b>pfnSetStreamSourceFreq</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setstreamsourcefreq.md">SetStreamSourceFreq</a> function that sets the frequency divisor of a stream source that is bound to a vertex buffer.</p>
</dd>

### -field <b>pfnSetConvolutionKernelMono</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setconvolutionkernelmono.md">SetConvolutionKernelMono</a> function that sets the monochrome convolution kernel.</p>
</dd>

### -field <b>pfnComposeRects</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-composerects.md">ComposeRects</a> function that composes rectangular areas.</p>
</dd>

### -field <b>pfnBlt</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-blt.md">Blt</a> function that copies the contents of a source surface to a destination surface.</p>
</dd>

### -field <b>pfnColorFill</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-colorfill.md">ColorFill</a> function that fills a rectangular area on a surface with a particular A8R8G8B8 color.</p>
</dd>

### -field <b>pfnDepthFill</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-depthfill.md">DepthFill</a> function that fills a depth buffer with a pixel value that is specified in native format.</p>
</dd>

### -field <b>pfnCreateQuery</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createquery.md">CreateQuery</a> function that creates driver-side resources for a query that the Direct3D runtime subsequently issues for processing.</p>
</dd>

### -field <b>pfnDestroyQuery</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroyquery.md">DestroyQuery</a> function that releases resources for the query that the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createquery.md">CreateQuery</a> function created.</p>
</dd>

### -field <b>pfnIssueQuery</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-issuequery.md">IssueQuery</a> function that processes the query that the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createquery.md">CreateQuery</a> function created.</p>
</dd>

### -field <b>pfnGetQueryData</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getquerydata.md">GetQueryData</a> function that retrieves information about a query.</p>
</dd>

### -field <b>pfnSetRenderTarget</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setrendertarget.md">SetRenderTarget</a> function that sets the render target surface in the driver's context.</p>
</dd>

### -field <b>pfnSetDepthStencil</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setdepthstencil.md">SetDepthStencil</a> function that sets the depth buffer in the driver's context.</p>
</dd>

### -field <b>pfnGenerateMipSubLevels</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-generatemipsublevels.md">GenerateMipSubLevels</a> function that regenerates the sublevels of a MIP-map texture.</p>
</dd>

### -field <b>pfnSetPixelShaderConstI</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setpixelshaderconsti.md">SetPixelShaderConstI</a> function that sets one or more pixel shader constant registers with integer values.</p>
</dd>

### -field <b>pfnSetPixelShaderConstB</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setpixelshaderconstb.md">SetPixelShaderConstB</a> function that sets one or more pixel shader constant registers with Boolean values.</p>
</dd>

### -field <b>pfnCreatePixelShader</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createpixelshader.md">CreatePixelShader</a> function that converts the pixel shader code into a hardware-specific format and associates this code with a shader handle.</p>
</dd>

### -field <b>pfnDeletePixelShader</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-deletepixelshader.md">DeletePixelShader</a> function that cleans up driver-side resources that are associated with pixel shader code.</p>
</dd>

### -field <b>pfnCreateDecodeDevice</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createdecodedevice.md">CreateDecodeDevice</a> function that creates a representation of a Microsoft DirectX Video Acceleration (VA) decode device from supplied parameters.</p>
</dd>

### -field <b>pfnDestroyDecodeDevice</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroydecodedevice.md">DestroyDecodeDevice</a> function that releases resources for a DirectX VA decode device.</p>
</dd>

### -field <b>pfnSetDecodeRenderTarget</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setdecoderendertarget.md">SetDecodeRenderTarget</a> function that sets the render target for decoding. <i>SetDecodeRenderTarget</i> can be called only outside of a <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-decodebeginframe.md">DecodeBeginFrame</a>/<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-decodeendframe.md">DecodeEndFrame</a> block.</p>
</dd>

### -field <b>pfnDecodeBeginFrame</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-decodebeginframe.md">DecodeBeginFrame</a> function that indicates that decoding of a frame can begin.</p>
</dd>

### -field <b>pfnDecodeEndFrame</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-decodeendframe.md">DecodeEndFrame</a> function that indicates that frame decoding operations must be completed.</p>
</dd>

### -field <b>pfnDecodeExecute</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-decodeexecute.md">DecodeExecute</a> function that performs a DirectX VA decode operation. <i>DecodeExecute</i> must be called inside a <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-decodebeginframe.md">DecodeBeginFrame</a>/<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-decodeendframe.md">DecodeEndFrame</a> block.</p>
</dd>

### -field <b>pfnDecodeExtensionExecute</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-decodeextensionexecute.md">DecodeExtensionExecute</a> function that performs a nonstandard DirectX VA decode operation. <i>DecodeExtensionExecute</i> must be called inside a <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-decodebeginframe.md">DecodeBeginFrame</a>/<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-decodeendframe.md">DecodeEndFrame</a> block.</p>
</dd>

### -field <b>pfnCreateVideoProcessDevice</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createvideoprocessdevice.md">CreateVideoProcessDevice</a> function that creates a representation of a DirectX VA video processing device from supplied parameters.</p>
</dd>

### -field <b>pfnDestroyVideoProcessDevice</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroyvideoprocessdevice.md">DestroyVideoProcessDevice</a> function that releases resources for a DirectX VA video processing device.</p>
</dd>

### -field <b>pfnVideoProcessBeginFrame</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-videoprocessbeginframe.md">VideoProcessBeginFrame</a> function that indicates that video processing of a frame can begin.</p>
</dd>

### -field <b>pfnVideoProcessEndFrame</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-videoprocessendframe.md">VideoProcessEndFrame</a> function that indicates that video processing operations must be completed.</p>
</dd>

### -field <b>pfnSetVideoProcessRenderTarget</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setvideoprocessrendertarget.md">SetVideoProcessRenderTarget</a> function that sets the render target for video processing. <i>SetVideoProcessRenderTarget</i> can be called only outside of a <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-videoprocessbeginframe.md">VideoProcessBeginFrame</a>/<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-videoprocessendframe.md">VideoProcessEndFrame</a> block.</p>
</dd>

### -field <b>pfnVideoProcessBlt</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-videoprocessblt.md">VideoProcessBlt</a> function that processes DirectX VA video. <i>VideoProcessBlt</i> must be called inside a <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-videoprocessbeginframe.md">VideoProcessBeginFrame</a>/<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-videoprocessendframe.md">VideoProcessEndFrame</a> block.</p>
</dd>

### -field <b>pfnCreateExtensionDevice</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createextensiondevice.md">CreateExtensionDevice</a> function that creates a representation of a DirectX VA extension device from supplied parameters.</p>
</dd>

### -field <b>pfnDestroyExtensionDevice</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroyextensiondevice.md">DestroyExtensionDevice</a> function that releases resources for a DirectX VA extension device.</p>
</dd>

### -field <b>pfnExtensionExecute</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-extensionexecute.md">ExtensionExecute</a> function that performs an operation that is specific to the given DirectX VA extension device.</p>
</dd>

### -field <b>pfnCreateOverlay</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createoverlay.md">CreateOverlay</a> function that allocates overlay hardware and makes the overlay visible.</p>
</dd>

### -field <b>pfnUpdateOverlay</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-updateoverlay.md">UpdateOverlay</a> function that reconfigures or moves an overlay that is being displayed.</p>
</dd>

### -field <b>pfnFlipOverlay</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-flipoverlay.md">FlipOverlay</a> function that causes the overlay hardware to start displaying the new allocation.</p>
</dd>

### -field <b>pfnGetOverlayColorControls</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getoverlaycolorcontrols.md">GetOverlayColorControls</a> function that retrieves color-control settings for an overlay.</p>
</dd>

### -field <b>pfnSetOverlayColorControls</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setoverlaycolorcontrols.md">SetOverlayColorControls</a> function that changes color-control settings for an overlay.</p>
</dd>

### -field <b>pfnDestroyOverlay</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroyoverlay.md">DestroyOverlay</a> function that disables the overlay hardware and frees the overlay handle.</p>
</dd>

### -field <b>pfnDestroyDevice</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroydevice.md">DestroyDevice</a> function that releases resources for the display device.</p>
</dd>

### -field <b>pfnQueryResourceResidency</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-queryresourceresidency.md">QueryResourceResidency</a> function that determines the residency of resources.</p>
</dd>

### -field <b>pfnOpenResource</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-openresource.md">OpenResource</a> function that informs the driver that a shared resource is opened.</p>
</dd>

### -field <b>pfnGetCaptureAllocationHandle</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaptureallocationhandle.md">GetCaptureAllocationHandle</a> function that maps the given capture resource to an allocation.</p>
</dd>

### -field <b>pfnCaptureToSysMem</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-capturetosysmem.md">CaptureToSysMem</a> function that copies a capture buffer to a video memory surface.</p>
</dd>

### -field <b>pfnLockAsync</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lockasync.md">LockAsync</a> function that locks a resource or a surface within the resource.</p>
</dd>

### -field <b>pfnUnlockAsync</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-unlockasync.md">UnlockAsync</a> function that unlocks a resource or a surface within the resource that the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lockasync.md">LockAsync</a> function previously locked.</p>
</dd>

### -field <b>pfnRename</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-rename.md">Rename</a> function that renames, with a new allocation, a resource or a surface within the resource.</p>
</dd>

### -field <b>pfnCreateVideoProcessor</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-dxvahd-createvideoprocessor.md">CreateVideoProcessor</a> function that creates a video processor.</p>
</dd>

### -field <b>pfnSetVideoProcessBltState</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-dxvahd-setvideoprocessbltstate.md">SetVideoProcessBltState</a> function that sets the state of a bitblt for a video processor. </p>
</dd>

### -field <b>pfnGetVideoProcessBltStatePrivate</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-dxvahd-getvideoprocessbltstateprivate.md">GetVideoProcessBltStatePrivate</a> function that retrieves the state data of a private bitblt for a video processor. </p>
</dd>

### -field <b>pfnSetVideoProcessStreamState</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-dxvahd-setvideoprocessstreamstate.md">SetVideoProcessStreamState</a> function that sets the state of a stream for a video processor. </p>
</dd>

### -field <b>pfnGetVideoProcessStreamStatePrivate</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-dxvahd-getvideoprocessstreamstateprivate.md">GetVideoProcessStreamStatePrivate</a> function that retrieves the private stream-state data for a video processor. </p>
</dd>

### -field <b>pfnVideoProcessBltHD</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-dxvahd-videoprocessblthd.md">VideoProcessBltHD</a> function that processes video input streams and composes to an output surface. </p>
</dd>

### -field <b>pfnDestroyVideoProcessor</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/library/windows/hardware/hh451638">DestroyVideoProcessor</a> function that releases resources for a previously created video processor. </p>
</dd>

### -field <b>pfnCreateAuthenticatedChannel</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createauthenticatedchannel.md">CreateAuthenticatedChannel</a> function that creates a channel that the Direct3D runtime and the driver can use to set and query protections. </p>
</dd>

### -field <b>pfnAuthenticatedChannelKeyExchange</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-authenticatedchannelkeyexchange.md">AuthenticatedChannelKeyExchange</a> function that negotiates the session key. </p>
</dd>

### -field <b>pfnQueryAuthenticatedChannel</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-queryauthenticatedchannel.md">QueryAuthenticatedChannel</a> function that queries an authenticated channel for capability and state information. </p>
</dd>

### -field <b>pfnConfigureAuthenticatedChannel</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-configureauthenicatedchannel.md">ConfigureAuthenticatedChannel</a> function that sets the state within an authenticated channel. </p>
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
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-cryptosessionkeyexchange.md">CryptoSessionKeyExchange</a> function that performs a key exchange during an encryption session. </p>
</dd>

### -field <b>pfnDestroyCryptoSession</b>

<dd>
<p>A pointer to the driver <a href="https://msdn.microsoft.com/library/windows/hardware/hh451632">DestroyCryptoSession</a> function that releases resources for an encryption session. </p>
</dd>

### -field <b>pfnEncryptionBlt</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-encryptionblt.md">EncryptionBlt</a> function that performs an encrypted bitblt operation. </p>
</dd>

### -field <b>pfnGetPitch</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getpitch.md">GetPitch</a> function that retrieves the pitch of an encrypted surface. </p>
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
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-decryptionblt.md">DecryptionBlt</a> function that writes data to a protected surface. </p>
</dd>

### -field <b>pfnResolveSharedResource</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-resolvesharedresource.md">ResolveSharedResource</a> function that resolves a shared resource. </p>
</dd>

### -field <b>pfnVolBlt1</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-volblt1.md">VolBlt1</a> function that performs a volume bit-block transfer (bitblt) operation.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnBufBlt1</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-bufblt1.md">BufBlt1</a> function that performs a bit-block transfer (bitblt) operation.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnTexBlt1</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-texblt1.md">TexBlt1</a> function that performs a texture bit-block transfer (bitblt) operation.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnDiscard</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-discard.md">Discard</a>  function that discards (evicts) a set of subresources from video display memory.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnOfferResources</b>

<dd>
<p>A pointer to the driver  <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-offerresources.md">OfferResources</a> function that requests that the user-mode display driver offer video memory resources for reuse.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnReclaimResources</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-reclaimresources.md">ReclaimResources</a> function that's called by the Direct3D runtime to reclaim video memory resources that it previously offered for reuse.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnCheckDirectFlipSupport</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-checkdirectflipsupport.md">CheckDirectFlipSupport</a> function that's called by the DWM to verify that the user-mode driver supports Direct Flip operations.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnCreateResource2</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createresource2.md">CreateResource2</a> function that creates a resource.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnCheckMultiPlaneOverlaySupport</b>

<dd>
<p>A pointer to the driver <a href="display.pfncheckmultiplaneoverlaysupport__d3d_">pfnCheckMultiPlaneOverlaySupport (D3D)</a> function that's called by the Direct3D runtime to check the details on hardware support for multiplane overlays.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnPresentMultiPlaneOverlay</b>

<dd>
<p>A pointer to the driver <a href="display.pfnpresentmultiplaneoverlay__d3d_">pfnPresentMultiplaneOverlay (D3D)</a> function that's called by the Direct3D runtime to notify the user-mode display driver that an application finished rendering and requests that the driver display the source surface by either copying or flipping or that the driver perform a color-fill operation.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnReserved1</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnFlush1</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-flush1.md">pfnFlush1</a>  function that's called by the Direct3D runtime to submit outstanding hardware commands that are in the hardware command buffer to the display miniport driver.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnCheckCounterInfo</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-checkcounterinfo.md">pfnCheckCounterInfo</a>  function that's called by the Direct3D runtime to determine global information that's related to manipulating counters.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnCheckCounter</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-checkcounter.md">pfnCheckCounter</a>  function that's called by the Direct3D runtime to retrieve info that describes a counter.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnUpdateSubresourceUP</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-updatesubresourceup.md">pfnUpdateSubresourceUP</a>  function that's called by the Direct3D runtime to update a destination subresource region from a source system-memory region.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnPresent1</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-present1.md">pfnPresent1(D3D)</a>  function that notifies the user-mode display driver that an application finished rendering and  that all ownership of the shared resource is released, and that  requests that the driver display to the destination surface.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnCheckPresentDurationSupport</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-checkpresentdurationsupport.md">CheckPresentDurationSupport</a> function that's called by the Direct3D runtime to request that the user-mode display driver get hardware device capabilities for seamlessly switching to a new monitor refresh rate.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnSetMarker</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setmarker.md">pfnSetMarker</a> function that notifies the user-mode display driver that it must generate a new time stamp if any GPU work has completed since the last call to <i>pfnSetMarker</i>.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnSetMarkerMode</b>

<dd>
<p>A pointer to the driver <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setmarkermode.md">pfnSetMarkerMode</a> function that notifies the user-mode display driver that it should support a type of Event Tracing for Windows (ETW) marker event.</p>
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
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createdevice.md">CreateDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542931">D3DDDIARG_CREATEDEVICE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_DEVICEFUNCS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
