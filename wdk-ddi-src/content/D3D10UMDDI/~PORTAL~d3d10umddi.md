# Declarations in the d3d10umddi header
This header D3D10Umddi contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFND3DWDDM2_0DDI_CALCPRIVATESHADERRESOURCEVIEWSIZE callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-calcprivateshaderresourceviewsize.md) | TBD |
| [PFND3D10DDI_STATE_IA_PRIMITIVE_TOPOLOGY_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-ia-primitive-topology-cb.md) | The pfnStateIaPrimitiveTopologyCb function causes the Microsoft Direct3D 10 runtime to refresh the primitive topology state. |
| [PFND3D11_1DDI_NEGOTIATEAUTHENTICATEDCHANNELKEYEXCHANGE callback function](nc-d3d10umddi-pfnd3d11-1ddi-negotiateauthenticatedchannelkeyexchange.md) | TBD |
| [PFND3D11_1DDI_VIDEOPROCESSORBLT callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorblt.md) | TBD |
| [PFND3D10DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE callback](nc-d3d10umddi-pfnd3d10ddi-calcprivatedepthstencilstatesize.md) | The CalcPrivateDepthStencilStateSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a depth stencil state. |
| [PFND3DWDDM1_3DDI_UPDATETILEMAPPINGS callback](nc-d3d10umddi-pfnd3dwddm1-3ddi-updatetilemappings.md) | Updates mappings of tile locations in tiled resources to memory locations in a tile pool. |
| [PFND3D10DDI_STATE_VS_SHADER_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-vs-shader-cb.md) | The pfnStateVsShaderCb function causes the Microsoft Direct3D 10 runtime to refresh the vertex shader stage's shader program. |
| [PFND3D11_1DDI_GETVIDEOPROCESSORCAPS callback function](nc-d3d10umddi-pfnd3d11-1ddi-getvideoprocessorcaps.md) | TBD |
| [PFND3D10DDI_CALCPRIVATERESOURCESIZE callback](nc-d3d10umddi-pfnd3d10ddi-calcprivateresourcesize.md) | The CalcPrivateResourceSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory). |
| [PFND3D11_1DDI_GETVIDEODECODERCONFIGCOUNT callback function](nc-d3d10umddi-pfnd3d11-1ddi-getvideodecoderconfigcount.md) | TBD |
| [PFND3D11_1DDI_CLEARVIEW callback](nc-d3d10umddi-pfnd3d11-1ddi-clearview.md) | Sets all the elements in a resource view to one value. A resource view is a surface descriptor that indicates a format and possibly a subset of the resource. |
| [PFND3D11_1DDI_CHECKDIRECTFLIPSUPPORT callback](nc-d3d10umddi-pfnd3d11-1ddi-checkdirectflipsupport.md) | Called by the Desktop Window Manager (DWM) to verify that the user-mode driver supports Direct Flip operations, in which video memory is seamlessly flipped between an application's managed primary allocations and the DWM's managed primary allocations. |
| [PFND3D11_1DDI_CREATEVIDEODECODER callback](nc-d3d10umddi-pfnd3d11-1ddi-createvideodecoder.md) | Creates a video decoder object. |
| [PFND3D10DDI_RESOURCECOPYREGION callback](nc-d3d10umddi-pfnd3d10ddi-resourcecopyregion.md) | The ResourceCopyRegion function copies a source subresource region to a location on a destination subresource. |
| [PFND3D10DDI_CALCPRIVATEGEOMETRYSHADERWITHSTREAMOUTPUT callback](nc-d3d10umddi-pfnd3d10ddi-calcprivategeometryshaderwithstreamoutput.md) | The CalcPrivateGeometryShaderWithStreamOutput function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a geometry shader with stream output. |
| [PFND3D10DDI_CHECKCOUNTER callback](nc-d3d10umddi-pfnd3d10ddi-checkcounter.md) | The CheckCounter function retrieves information that describes a counter. |
| [PFND3D11_1DDI_CRYPTOSESSIONGETHANDLE callback function](nc-d3d10umddi-pfnd3d11-1ddi-cryptosessiongethandle.md) | TBD |
| [PFND3DWDDM2_0DDI_CREATECONTEXTVIRTUAL_CB callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-createcontextvirtual-cb.md) | TBD |
| [PFND3D11_1DDI_GETCRYPTOKEYEXCHANGETYPE callback](nc-d3d10umddi-pfnd3d11-1ddi-getcryptokeyexchangetype.md) | Queries the type of key exchange that is supported by the cryptographic engine of the display adapter for a specified encryption algorithm and video decoder profile. |
| [PFND3D11_1DDI_NEGOTIATECRYPTOSESSIONKEYESCHANGE callback](nc-d3d10umddi-pfnd3d11-1ddi-negotiatecryptosessionkeyeschange.md) | Establishes a session key for a cryptographic session object. |
| [PFND3D11_1DDI_CREATEBLENDSTATE callback](nc-d3d10umddi-pfnd3d11-1ddi-createblendstate.md) | Creates a blend state. |
| [PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMOUTPUTRATE callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetstreamoutputrate.md) | TBD |
| [PFND3D11_1DDI_ASSIGNDEBUGBINARY callback](nc-d3d10umddi-pfnd3d11-1ddi-assigndebugbinary.md) | Provides the full shader binary that is available after shader creation. The full shader binary lets a driver retrieve debugging information or other shader binary information that would not normally be available to the driver. |
| [PFND3D11_1DDI_CREATECRYPTOSESSION callback function](nc-d3d10umddi-pfnd3d11-1ddi-createcryptosession.md) | TBD |
| [PFND3D10DDI_SETCONSTANTBUFFERS callback](nc-d3d10umddi-pfnd3d10ddi-setconstantbuffers.md) | The CsSetConstantBuffers function sets constant buffers for a compute shader. |
| [PFND3D11_1DDI_GETVIDEODECODERPROFILE callback function](nc-d3d10umddi-pfnd3d11-1ddi-getvideodecoderprofile.md) | TBD |
| [PFND3DWDDM2_2DDI_SHADERCACHE_ADDREF_RELEASE_CB callback function](nc-d3d10umddi-pfnd3dwddm2-2ddi-shadercache-addref-release-cb.md) | TBD |
| [PFND3D10DDI_RELOCATEDEVICEFUNCS callback](nc-d3d10umddi-pfnd3d10ddi-relocatedevicefuncs.md) | The RelocateDeviceFuncs function notifies the user-mode display driver about the new location of the driver function table. |
| [PFND3D10DDI_CREATEELEMENTLAYOUT callback](nc-d3d10umddi-pfnd3d10ddi-createelementlayout.md) | The CreateElementLayout function creates an element layout. |
| [PFND3DWDDM1_3DDI_UPDATETILES callback](nc-d3d10umddi-pfnd3dwddm1-3ddi-updatetiles.md) | Updates tiles by copying from app memory to the tiled resource. |
| [PFND3D10DDI_STATE_SO_TARGETS_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-so-targets-cb.md) | The pfnStateSoTargetsCb function causes the Microsoft Direct3D 10 runtime to refresh the stream-out targets. |
| [PFND3D11DDI_RELOCATEDEVICEFUNCS callback](nc-d3d10umddi-pfnd3d11ddi-relocatedevicefuncs.md) | The RelocateDeviceFuncs(D3D11) function notifies the user-mode display driver about the new location of the driver function table. |
| [PFND3D10DDI_STATE_RS_SCISSOR_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-rs-scissor-cb.md) | The pfnStateRsScissorCb function causes the Microsoft Direct3D 10 runtime to refresh the scissor state. |
| [PFND3D11_1DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT callback](nc-d3d10umddi-pfnd3d11-1ddi-creategeometryshaderwithstreamoutput.md) | Creates a geometry shader with stream output. |
| [PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCONSTRICTION callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetoutputconstriction.md) | TBD |
| [PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORENUMSIZE callback function](nc-d3d10umddi-pfnd3d11-1ddi-calcprivatevideoprocessorenumsize.md) | TBD |
| [PFND3D11DDI_CLEARUNORDEREDACCESSVIEWFLOAT callback](nc-d3d10umddi-pfnd3d11ddi-clearunorderedaccessviewfloat.md) | The ClearUnorderedAccessViewFLOAT function clears the specified unordered-access view by setting it to a constant value. |
| [PFND3DWDDM2_0DDI_SETHARDWAREPROTECTION callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-sethardwareprotection.md) | TBD |
| [PFND3DWDDM2_0DDI_CREATESHADERRESOURCEVIEW callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-createshaderresourceview.md) | TBD |
| [PFND3D10DDI_STATE_OM_RENDERTARGETS_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-om-rendertargets-cb.md) | The pfnStateOmRenderTargetsCb function causes the Microsoft Direct3D 10 runtime to refresh the output merger's bound render targets. |
| [PFND3D10DDI_CHECKFORMATSUPPORT callback](nc-d3d10umddi-pfnd3d10ddi-checkformatsupport.md) | Retrieves the capabilities that the device has with the specified format. |
| [PFND3D10DDI_DRAWINDEXEDINSTANCED callback](nc-d3d10umddi-pfnd3d10ddi-drawindexedinstanced.md) | The DrawIndexedInstanced function draws particular instances of indexed primitives. |
| [PFND3D11_1DDI_CALCPRIVATERASTERIZERSTATESIZE callback](nc-d3d10umddi-pfnd3d11-1ddi-calcprivaterasterizerstatesize.md) | Determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a rasterizer state. |
| [PFND3D11DDI_SETUNORDEREDACCESSVIEWS callback](nc-d3d10umddi-pfnd3d11ddi-setunorderedaccessviews.md) | The CsSetUnorderedAccessViews function sets unordered access view (UAV) objects for a compute shader. |
| [PFND3D10DDI_CREATERENDERTARGETVIEW callback](nc-d3d10umddi-pfnd3d10ddi-createrendertargetview.md) | The CreateRenderTargetView function creates a render target view. |
| [PFND3DWDDM2_0DDI_CALCPRIVATEUNORDEREDACCESSVIEWSIZE callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-calcprivateunorderedaccessviewsize.md) | TBD |
| [PFND3D10DDI_RESOURCEISSTAGINGBUSY callback](nc-d3d10umddi-pfnd3d10ddi-resourceisstagingbusy.md) | The ResourceIsStagingBusy function determines whether a resource is currently being used by the graphics pipeline. |
| [PFND3D11_1DDI_CREATEVIDEODECODEROUTPUTVIEW callback](nc-d3d10umddi-pfnd3d11-1ddi-createvideodecoderoutputview.md) | Creates a resource view for a video decoder. This view defines the output sample for the video decoding operation. |
| [PFND3D11_1DDI_CALCPRIVATESHADERSIZE callback](nc-d3d10umddi-pfnd3d11-1ddi-calcprivateshadersize.md) | Determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a shader. |
| [PFND3DWDDM2_0DDI_CREATEQUERY callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-createquery.md) | TBD |
| [PFND3D11_1DDI_STARTSESSIONKEYREFRESH callback function](nc-d3d10umddi-pfnd3d11-1ddi-startsessionkeyrefresh.md) | TBD |
| [PFND3D11DDI_CREATEDEPTHSTENCILVIEW callback](nc-d3d10umddi-pfnd3d11ddi-createdepthstencilview.md) | The CreateDepthStencilView(D3D11) function creates a depth-stencil view. |
| [PFND3D10DDI_SETDEPTHSTENCILSTATE callback](nc-d3d10umddi-pfnd3d10ddi-setdepthstencilstate.md) | The SetDepthStencilState function sets a depth-stencil state. |
| [PFND3D11DDI_CALCPRIVATERESOURCESIZE callback](nc-d3d10umddi-pfnd3d11ddi-calcprivateresourcesize.md) | The CalcPrivateResourceSize(D3D11) function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory). |
| [PFND3DWDDM2_0DDI_VIDEOPROCESSORGETBEHAVIORHINTS callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-videoprocessorgetbehaviorhints.md) | TBD |
| [PFND3D11_1DDI_CREATEPIXELSHADER callback](nc-d3d10umddi-pfnd3d11-1ddi-createpixelshader.md) | Converts pixel shader code into a hardware-specific format and associates this code with a shader handle. |
| [PFND3D11_1DDI_CHECKVIDEODECODERFORMAT callback function](nc-d3d10umddi-pfnd3d11-1ddi-checkvideodecoderformat.md) | TBD |
| [PFND3D10DDI_CALCPRIVATESAMPLERSIZE callback](nc-d3d10umddi-pfnd3d10ddi-calcprivatesamplersize.md) | The CalcPrivateSamplerSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a sampler. |
| [PFND3D10DDI_DESTROYELEMENTLAYOUT callback](nc-d3d10umddi-pfnd3d10ddi-destroyelementlayout.md) | The DestroyElementLayout function destroys the specified element layout object. The element layout object can be destoyed only if it is not currently bound to a display device. |
| [PFND3D11DDI_CALCPRIVATEDEFERREDCONTEXTSIZE callback](nc-d3d10umddi-pfnd3d11ddi-calcprivatedeferredcontextsize.md) | The CalcPrivateDeferredContextSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a deferred context. |
| [PFND3D10DDI_OPENADAPTER callback](nc-d3d10umddi-pfnd3d10ddi-openadapter.md) | The OpenAdapter10 function creates a graphics adapter object that is referenced in subsequent calls. |
| [PFND3D10DDI_STATE_VS_SAMPLER_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-vs-sampler-cb.md) | The pfnStateVsSamplerCb function causes the Microsoft Direct3D 10 runtime to refresh the vertex shader stage's bound samplers. |
| [PFND3D11DDI_STATE_DS_SAMPLER_CB callback](nc-d3d10umddi-pfnd3d11ddi-state-ds-sampler-cb.md) | The pfnStateDsSamplerCb function causes the Microsoft Direct3D 11 runtime to refresh the domain shader sample state. |
| [PFND3D10DDI_CALCPRIVATEDEPTHSTENCILVIEWSIZE callback](nc-d3d10umddi-pfnd3d10ddi-calcprivatedepthstencilviewsize.md) | The CalcPrivateDepthStencilViewSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a depth stencil view. |
| [PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSOROUTPUTVIEWSIZE callback](nc-d3d10umddi-pfnd3d11-1ddi-calcprivatevideoprocessoroutputviewsize.md) | Returns the number of bytes that the driver requires to store private data for the video processor output view state. |
| [PFND3DWDDM2_0DDI_CALCPRIVATERASTERIZERSTATESIZE callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-calcprivaterasterizerstatesize.md) | TBD |
| [PFND3D10DDI_CLOSEADAPTER callback](nc-d3d10umddi-pfnd3d10ddi-closeadapter.md) | The CloseAdapter(D3D10) function releases resources for a graphics adapter object. |
| [PFND3D10DDI_STATE_GS_SAMPLER_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-gs-sampler-cb.md) | The pfnStateGsSamplerCb function causes the Microsoft Direct3D 10 runtime to refresh the geometry shader sample state. |
| [PFND3D11_1DDI_DECRYPTIONBLT callback](nc-d3d10umddi-pfnd3d11-1ddi-decryptionblt.md) | Writes encrypted data to a protected surface. |
| [PFND3D11_1DDI_CALCPRIVATEGEOMETRYSHADERWITHSTREAMOUTPUT callback](nc-d3d10umddi-pfnd3d11-1ddi-calcprivategeometryshaderwithstreamoutput.md) | Determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a geometry shader with stream output. |
| [PFND3DWDDM2_2DDI_RELOCATEDEVICEFUNCS callback function](nc-d3d10umddi-pfnd3dwddm2-2ddi-relocatedevicefuncs.md) | TBD |
| [PFND3DWDDM2_1DDI_VIDEOPROCESSORSETOUTPUTHDRMETADATA callback function](nc-d3d10umddi-pfnd3dwddm2-1ddi-videoprocessorsetoutputhdrmetadata.md) | TBD |
| [PFND3D11DDI_RECYCLECREATEDEFERREDCONTEXT callback](nc-d3d10umddi-pfnd3d11ddi-recyclecreatedeferredcontext.md) | The RecycleCreateDeferredContext function clears out the pipeline state for a deferred context. |
| [PFND3D11_1DDI_CREATEVIDEOPROCESSORINPUTVIEW callback](nc-d3d10umddi-pfnd3d11-1ddi-createvideoprocessorinputview.md) | Creates a resource view for a video processor. This view defines the input sample for the video processing operation. |
| [PFND3D10DDI_DESTROYRASTERIZERSTATE callback](nc-d3d10umddi-pfnd3d10ddi-destroyrasterizerstate.md) | The DestroyRasterizerState function destroys the specified rasterizer state object. The rasterizer state object can be destoyed only if it is not currently bound to a display device. |
| [PFND3D11DDI_CREATEDOMAINSHADER callback](nc-d3d10umddi-pfnd3d11ddi-createdomainshader.md) | The CreateDomainShader function creates a domain shader. |
| [PFND3D10DDI_CREATEDEPTHSTENCILVIEW callback](nc-d3d10umddi-pfnd3d10ddi-createdepthstencilview.md) | The CreateDepthStencilView function creates a depth stencil view. |
| [PFND3D11DDI_ABANDONCOMMANDLIST callback](nc-d3d10umddi-pfnd3d11ddi-abandoncommandlist.md) | The AbandonCommandList function abandons the command list. |
| [PFND3DWDDM2_0DDI_RETRIEVE_SHADER_COMMENT callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-retrieve-shader-comment.md) | TBD |
| [PFND3D10DDI_CHECKCOUNTERINFO callback](nc-d3d10umddi-pfnd3d10ddi-checkcounterinfo.md) | The CheckCounterInfo function determines global information that is related to manipulating counters. |
| [PFND3D10DDI_CALCPRIVATERASTERIZERSTATESIZE callback](nc-d3d10umddi-pfnd3d10ddi-calcprivaterasterizerstatesize.md) | The CalcPrivateRasterizerStateSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a rasterizer state. |
| [PFND3D11DDI_STATE_CS_SAMPLER_CB callback](nc-d3d10umddi-pfnd3d11ddi-state-cs-sampler-cb.md) | The pfnStateCsSamplerCb function causes the Microsoft Direct3D 11 runtime to refresh the compute shader sample state. |
| [PFND3D10DDI_SETVIEWPORTS callback](nc-d3d10umddi-pfnd3d10ddi-setviewports.md) | The SetViewports function sets viewports. |
| [PFND3D10DDI_STATE_VS_SRV_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-vs-srv-cb.md) | The pfnStateVsSrvCb function causes the Microsoft Direct3D 10 runtime to refresh the vertex shader stage's bound shader resource views. |
| [PFND3D10DDI_IA_SETINDEXBUFFER callback](nc-d3d10umddi-pfnd3d10ddi-ia-setindexbuffer.md) | The IaSetIndexBuffer function sets an index buffer for an input assembler. |
| [PFND3D10DDI_GENMIPS callback](nc-d3d10umddi-pfnd3d10ddi-genmips.md) | The GenMips function generates the lower MIP-map levels on the specified shader-resource view. |
| [PFND3D10DDI_STATE_IA_INDEXBUF_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-ia-indexbuf-cb.md) | The pfnStateIaIndexBufCb function causes the Microsoft Direct3D 10 runtime to refresh the index buffer state. |
| [PFND3D11_1DDI_CALCPRIVATEVIDEODECODEROUTPUTVIEWSIZE callback function](nc-d3d10umddi-pfnd3d11-1ddi-calcprivatevideodecoderoutputviewsize.md) | TBD |
| [PFND3D11_1DDI_CREATEVIDEOPROCESSORENUM callback](nc-d3d10umddi-pfnd3d11-1ddi-createvideoprocessorenum.md) | Creates an enumeration object for the video processor capabilities of the driver. |
| [PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSOURCERECT callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetstreamsourcerect.md) | TBD |
| [PFND3DWDDM1_3DDI_COPYTILEMAPPINGS callback](nc-d3d10umddi-pfnd3dwddm1-3ddi-copytilemappings.md) | Copies mappings from a source tiled resource to a destination tiled resource. |
| [PFND3D10DDI_CREATESAMPLER callback](nc-d3d10umddi-pfnd3d10ddi-createsampler.md) | The CreateSampler function creates a sampler. |
| [PFND3DWDDM1_3DDI_TILEDRESOURCEBARRIER callback](nc-d3d10umddi-pfnd3dwddm1-3ddi-tiledresourcebarrier.md) | Specifies a data access ordering constraint between multiple tiled resources. For more info about this constraint, see Remarks. |
| [PFND3D10DDI_SETERROR_CB callback](nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md) | The pfnSetErrorCb function sets the return error code of a user-mode display driver's function. |
| [PFND3DWDDM1_3DDI_RESIZETILEPOOL callback](nc-d3d10umddi-pfnd3dwddm1-3ddi-resizetilepool.md) | Resizes a tile pool. |
| [PFND3D11_1DDI_FLUSH callback](nc-d3d10umddi-pfnd3d11-1ddi-flush.md) | Submits outstanding hardware commands that are in the hardware command buffer to the display miniport driver. Implemented by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORSIZE callback function](nc-d3d10umddi-pfnd3d11-1ddi-calcprivatevideoprocessorsize.md) | TBD |
| [PFND3D11_1DDI_GETVIDEODECODERCONFIG callback function](nc-d3d10umddi-pfnd3d11-1ddi-getvideodecoderconfig.md) | TBD |
| [PFND3D10DDI_SETRASTERIZERSTATE callback](nc-d3d10umddi-pfnd3d10ddi-setrasterizerstate.md) | The SetRasterizerState function sets the rasterizer state. |
| [PFND3D10DDI_STATE_OM_BLENDSTATE_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-om-blendstate-cb.md) | The pfnStateOmBlendStateCb function causes the Microsoft Direct3D 10 runtime to refresh the output merger blend state. |
| [PFND3D10DDI_SETPREDICATION callback](nc-d3d10umddi-pfnd3d10ddi-setpredication.md) | The SetPredication function specifies whether rendering and resource-manipulation commands that follow are actually performed. |
| [PFND3D10DDI_CALCPRIVATEDEVICESIZE callback](nc-d3d10umddi-pfnd3d10ddi-calcprivatedevicesize.md) | The CalcPrivateDeviceSize function determines the size of a memory region that the user-mode display driver requires from the Microsoft Direct3D runtime to store frequently-accessed data. |
| [PFND3D10DDI_CREATERESOURCE callback](nc-d3d10umddi-pfnd3d10ddi-createresource.md) | Creates a resource. |
| [PFND3D11DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT callback](nc-d3d10umddi-pfnd3d11ddi-creategeometryshaderwithstreamoutput.md) | The CreateGeometryShaderWithStreamOutput(D3D11) function creates a geometry shader with stream output. |
| [PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMDESTRECT callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetstreamdestrect.md) | TBD |
| [PFND3D10DDI_CREATEBLENDSTATE callback](nc-d3d10umddi-pfnd3d10ddi-createblendstate.md) | The CreateBlendState function creates a blend state. |
| [PFND3D11_1DDI_VIDEOPROCESSORGETOUTPUTEXTENSION callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorgetoutputextension.md) | TBD |
| [PFND3DWDDM2_2DDI_SHADERCACHE_GET_VALUE_CB callback function](nc-d3d10umddi-pfnd3dwddm2-2ddi-shadercache-get-value-cb.md) | TBD |
| [PFND3D11_1DDI_VIDEOPROCESSORGETSTREAMEXTENSION callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorgetstreamextension.md) | TBD |
| [PFND3D11DDI_STATE_HS_SAMPLER_CB callback](nc-d3d10umddi-pfnd3d11ddi-state-hs-sampler-cb.md) | The pfnStateHsSamplerCb function causes the Microsoft Direct3D 11 runtime to refresh the hull shader sample state. |
| [PFND3D10DDI_CALCPRIVATESHADERSIZE callback](nc-d3d10umddi-pfnd3d10ddi-calcprivateshadersize.md) | The CalcPrivateShaderSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a shader. |
| [PFND3DWDDM2_0DDI_FLUSH callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-flush.md) | TBD |
| [PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPIXELASPECTRATIO callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetstreampixelaspectratio.md) | TBD |
| [PFND3D10DDI_STATE_GS_SHADER_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-gs-shader-cb.md) | The pfnStateGsShaderCb function causes the Microsoft Direct3D 10 runtime to refresh the geometry shader. |
| [PFND3D10DDI_STATE_IA_VERTEXBUF_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-ia-vertexbuf-cb.md) | The pfnStateIaVertexBufCb function causes the Microsoft Direct3D 10 runtime to refresh the set of vertex buffers that are bound to the input assembler. |
| [PFND3D10DDI_STATE_RS_RASTSTATE_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-rs-raststate-cb.md) | The pfnStateRsRastStateCb function causes the Microsoft Direct3D 10 runtime to refresh the rasterization state. |
| [PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMROTATION callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetstreamrotation.md) | TBD |
| [PFND3D10_1DDI_CREATESHADERRESOURCEVIEW callback](nc-d3d10umddi-pfnd3d10-1ddi-createshaderresourceview.md) | The CreateShaderResourceView(D3D10_1) function creates a shader resource view. |
| [PFND3D11DDI_STATE_DS_CONSTBUF_CB callback](nc-d3d10umddi-pfnd3d11ddi-state-ds-constbuf-cb.md) | The pfnStateDsConstBufCb function causes the Microsoft Direct3D 11 runtime to refresh the domain shader constant buffer state. |
| [PFND3DWDDM2_1DDI_VIDEOPROCESSORSETSTREAMHDRMETADATA callback function](nc-d3d10umddi-pfnd3dwddm2-1ddi-videoprocessorsetstreamhdrmetadata.md) | TBD |
| [PFND3D10DDI_CHECKMULTISAMPLEQUALITYLEVELS callback](nc-d3d10umddi-pfnd3d10ddi-checkmultisamplequalitylevels.md) | The CheckMultisampleQualityLevels function retrieves the number of quality levels that the device supports for the specified number of samples. |
| [PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTEXTENSION callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetoutputextension.md) | TBD |
| [PFND3DWDDM2_0DDI_VIDEOPROCESSORSETOUTPUTSHADERUSAGE callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-videoprocessorsetoutputshaderusage.md) | TBD |
| [PFND3D10DDI_DESTROYRENDERTARGETVIEW callback](nc-d3d10umddi-pfnd3d10ddi-destroyrendertargetview.md) | The DestroyRenderTargetView function destroys the specified render target view object. The render target view object can be destoyed only if it is not currently bound to a display device. |
| [PFND3D11_1DDI_CREATEGEOMETRYSHADER callback](nc-d3d10umddi-pfnd3d11-1ddi-creategeometryshader.md) | Creates a geometry shader. |
| [PFND3D10DDI_DESTROYSAMPLER callback](nc-d3d10umddi-pfnd3d10ddi-destroysampler.md) | The DestroySampler function destroys the specified sampler object. The sampler object can be destoyed only if it is not currently bound to a display device. |
| [PFND3D11_1DDI_CREATEVERTEXSHADER callback](nc-d3d10umddi-pfnd3d11-1ddi-createvertexshader.md) | Creates a vertex shader. |
| [PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION callback function](nc-d3d10umddi-pfnd3dwddm2-2ddi-create-shadercache-session.md) | TBD |
| [PFND3D10_2DDI_GETCAPS callback](nc-d3d10umddi-pfnd3d10-2ddi-getcaps.md) | The GetCaps(D3D10_2) function queries for capabilities of the graphics adapter. |
| [PFND3D11DDI_DISPATCH callback](nc-d3d10umddi-pfnd3d11ddi-dispatch.md) | The Dispatch function executes the compute shader. |
| [PFND3DWDDM2_2DDI_DESTROY_SHADERCACHE_SESSION callback function](nc-d3d10umddi-pfnd3dwddm2-2ddi-destroy-shadercache-session.md) | TBD |
| [PFND3D11_1DDI_GETVIDEODECODERPROFILECOUNT callback function](nc-d3d10umddi-pfnd3d11-1ddi-getvideodecoderprofilecount.md) | TBD |
| [PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMCOLORSPACE callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetstreamcolorspace.md) | TBD |
| [PFND3D10DDI_SETINPUTLAYOUT callback](nc-d3d10umddi-pfnd3d10ddi-setinputlayout.md) | The IaSetInputLayout function sets an input layout for the input assembler. |
| [PFND3D11_1DDI_CALCPRIVATECRYPTOSESSIONSIZE callback](nc-d3d10umddi-pfnd3d11-1ddi-calcprivatecryptosessionsize.md) | Returns the number of bytes that the driver requires to store private data for the cryptographic session state. |
| [PFND3DWDDM1_3DDI_CHECKMULTISAMPLEQUALITYLEVELS callback](nc-d3d10umddi-pfnd3dwddm1-3ddi-checkmultisamplequalitylevels.md) | Retrieves the number of quality levels that the device supports for the specified number of samples. Supported. |
| [PFND3D10DDI_CREATERASTERIZERSTATE callback](nc-d3d10umddi-pfnd3d10ddi-createrasterizerstate.md) | The CreateRasterizerState function creates a rasterizer state. |
| [PFND3D10_1DDI_CALCPRIVATESHADERRESOURCEVIEWSIZE callback](nc-d3d10umddi-pfnd3d10-1ddi-calcprivateshaderresourceviewsize.md) | The CalcPrivateShaderResourceViewSize(D3D10_1) function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a shader resource view. |
| [PFND3D10_1DDI_CALCPRIVATEBLENDSTATESIZE callback](nc-d3d10umddi-pfnd3d10-1ddi-calcprivateblendstatesize.md) | The CalcPrivateBlendStateSize(D3D10_1) function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a blend state. |
| [PFND3D10DDI_SETVERTEXPIPELINEOUTPUT callback function](nc-d3d10umddi-pfnd3d10ddi-setvertexpipelineoutput.md) | TBD |
| [PFND3D11_1DDI_CALCPRIVATEVIDEODECODERSIZE callback function](nc-d3d10umddi-pfnd3d11-1ddi-calcprivatevideodecodersize.md) | TBD |
| [PFND3D11DDI_SETRESOURCEMINLOD callback](nc-d3d10umddi-pfnd3d11ddi-setresourceminlod.md) | The SetResourceMinLOD function sets the minimum level of detail (LOD) for a resource. |
| [PFND3D11DDI_STATE_DS_SRV_CB callback](nc-d3d10umddi-pfnd3d11ddi-state-ds-srv-cb.md) | The pfnStateDsSrvCb function causes the Microsoft Direct3D 11 runtime to refresh the constant shader resource view state for the domain shader. |
| [PFND3D10DDI_CREATESHADERRESOURCEVIEW callback](nc-d3d10umddi-pfnd3d10ddi-createshaderresourceview.md) | The CreateShaderResourceView function creates a shader resource view. |
| [PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPALETTE callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetstreampalette.md) | TBD |
| [PFND3D10DDI_CREATEDEVICE callback](nc-d3d10umddi-pfnd3d10ddi-createdevice.md) | The CreateDevice(D3D10) function creates a graphics context that is referenced in subsequent calls. |
| [PFND3D11DDI_DISPATCHINDIRECT callback](nc-d3d10umddi-pfnd3d11ddi-dispatchindirect.md) | The DispatchIndirect function executes the compute shader. |
| [PFND3DWDDM2_0DDI_CREATECONTEXT_CB callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-createcontext-cb.md) | TBD |
| [PFND3DWDDM2_0DDI_RELOCATEDEVICEFUNCS callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-relocatedevicefuncs.md) | TBD |
| [PFND3D10DDI_DRAWAUTO callback](nc-d3d10umddi-pfnd3d10ddi-drawauto.md) | The DrawAuto function works similarly to the Draw function, except DrawAuto is used for the special case where vertex data is written through the stream-output unit and then recycled as a vertex buffer. |
| [PFND3D11DDI_STATE_HS_SRV_CB callback](nc-d3d10umddi-pfnd3d11ddi-state-hs-srv-cb.md) | The pfnStateHsSrvCb function causes the Microsoft Direct3D 11 runtime to refresh the constant shader resource view state for the hull shader. |
| [PFND3DWDDM2_2DDI_SET_SHADERCACHE_SESSION callback function](nc-d3d10umddi-pfnd3dwddm2-2ddi-set-shadercache-session.md) | TBD |
| [PFND3D10_1DDI_CREATEBLENDSTATE callback](nc-d3d10umddi-pfnd3d10-1ddi-createblendstate.md) | The CreateBlendState(D3D10_1) function creates a blend state. |
| [PFND3D10DDI_STATE_PS_SHADER_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-ps-shader-cb.md) | The pfnStatePsShaderCb function causes the Microsoft Direct3D 10 runtime to refresh the pixel shader stage's shader program. |
| [PFND3DWDDM2_0DDI_SETHARDWAREPROTECTIONSTATE callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-sethardwareprotectionstate.md) | TBD |
| [PFND3D10DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT callback](nc-d3d10umddi-pfnd3d10ddi-creategeometryshaderwithstreamoutput.md) | The CreateGeometryShaderWithStreamOutput function creates a geometry shader with stream output. |
| [PFND3D11DDI_CALCPRIVATEDEPTHSTENCILVIEWSIZE callback](nc-d3d10umddi-pfnd3d11ddi-calcprivatedepthstencilviewsize.md) | The CalcPrivateDepthStencilViewSize(D3D11) function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a depth-stencil view. |
| [PFND3D11DDI_STATE_HS_CONSTBUF_CB callback](nc-d3d10umddi-pfnd3d11ddi-state-hs-constbuf-cb.md) | The pfnStateHsConstBufCb function causes the Microsoft Direct3D 11 runtime to refresh the hull shader constant buffer state. |
| [PFND3D11DDI_DESTROYCOMMANDLIST callback](nc-d3d10umddi-pfnd3d11ddi-destroycommandlist.md) | The DestroyCommandList function destroys a command list. |
| [PFND3D10DDI_CREATEGEOMETRYSHADER callback](nc-d3d10umddi-pfnd3d10ddi-creategeometryshader.md) | The CreateGeometryShader function creates a geometry shader. |
| [PFND3D10DDI_CREATEDEPTHSTENCILSTATE callback](nc-d3d10umddi-pfnd3d10ddi-createdepthstencilstate.md) | The CreateDepthStencilState function creates a depth stencil state. |
| [PFND3D10DDI_QUERYEND callback](nc-d3d10umddi-pfnd3d10ddi-queryend.md) | The QueryEnd function marks the end of a sequence of graphics commands for a query and transitions the query to the &#0034;issued&#0034; state. |
| [PFND3D10DDI_IA_SETVERTEXBUFFERS callback](nc-d3d10umddi-pfnd3d10ddi-ia-setvertexbuffers.md) | The IaSetVertexBuffers function sets vertex buffers for an input assembler. |
| [PFND3D11_1DDI_VIDEODECODERBEGINFRAME callback function](nc-d3d10umddi-pfnd3d11-1ddi-videodecoderbeginframe.md) | TBD |
| [PFND3D10DDI_DESTROYDEPTHSTENCILVIEW callback](nc-d3d10umddi-pfnd3d10ddi-destroydepthstencilview.md) | The DestroyDepthStencilView function destroys the specified depth stencil view object. The depth stencil view object can be destoyed only if it is not currently bound to a display device. |
| [PFND3DWDDM2_1DDI_RELOCATEDEVICEFUNCS callback function](nc-d3d10umddi-pfnd3dwddm2-1ddi-relocatedevicefuncs.md) | TBD |
| [PFND3D10DDI_DESTROYSHADER callback](nc-d3d10umddi-pfnd3d10ddi-destroyshader.md) | The DestroyShader function destroys the specified shader object. The shader object can be destoyed only if it is not currently bound to a display device. |
| [PFND3D10DDI_STATE_PS_SAMPLER_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-ps-sampler-cb.md) | The pfnStatePsSamplerCb function causes the Microsoft Direct3D 10 runtime to refresh the pixel shader stage's bound samplers. |
| [PFND3DWDDM2_0DDI_CHECKVIDEOPROCESSORFORMATCONVERSION callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-checkvideoprocessorformatconversion.md) | TBD |
| [PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMFILTER callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetstreamfilter.md) | TBD |
| [PFND3D10DDI_CLEARRENDERTARGETVIEW callback](nc-d3d10umddi-pfnd3d10ddi-clearrendertargetview.md) | The ClearRenderTargetView function clears the specified render-target view by setting it to a constant value. |
| [PFND3D10DDI_STATE_RS_VIEWPORTS_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-rs-viewports-cb.md) | The pfnStateRsViewportsCb function causes the Microsoft Direct3D 10 runtime to refresh the viewport state. |
| [PFND3D11_1DDI_CALCPRIVATEBLENDSTATESIZE callback](nc-d3d10umddi-pfnd3d11-1ddi-calcprivateblendstatesize.md) | Determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a blend state. |
| [PFND3D10DDI_RESOURCEMAP callback](nc-d3d10umddi-pfnd3d10ddi-resourcemap.md) | The ResourceMap function maps a subresource of a resource. |
| [PFND3D11_1DDI_VIDEODECODERENDFRAME callback function](nc-d3d10umddi-pfnd3d11-1ddi-videodecoderendframe.md) | TBD |
| [PFND3D11DDI_CREATEHULLSHADER callback](nc-d3d10umddi-pfnd3d11ddi-createhullshader.md) | The CreateHullShader function creates a hull shader. |
| [PFND3D10DDI_DISABLE_DEFERRED_STAGING_RESOURCE_DESTRUCTION_CB callback](nc-d3d10umddi-pfnd3d10ddi-disable-deferred-staging-resource-destruction-cb.md) | The pfnDisableDeferredStagingResourceDestruction function disables the deferred destruction of staging resources. |
| [PFND3D11_1DDI_ENCRYPTIONBLT callback](nc-d3d10umddi-pfnd3d11-1ddi-encryptionblt.md) | Reads encrypted data from a protected surface. |
| [PFND3D11_1DDI_RESOURCEUPDATESUBRESOURCEUP callback](nc-d3d10umddi-pfnd3d11-1ddi-resourceupdatesubresourceup.md) | Updates a destination subresource region that stores constant buffers from a source system-memory region. Implemented by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [PFND3DWDDM1_3DDI_SETMARKERMODE callback](nc-d3d10umddi-pfnd3dwddm1-3ddi-setmarkermode.md) | Notifies the user-mode display driver that it should support a type of Event Tracing for Windows (ETW) marker event. Must be implemented by Windows Display Driver Model (WDDM) 1.3 and later drivers. |
| [PFND3DWDDM2_0DDI_CREATEUNORDEREDACCESSVIEW callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-createunorderedaccessview.md) | TBD |
| [PFND3DWDDM2_0DDI_VIDEODECODERENABLEDOWNSAMPLING callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-videodecoderenabledownsampling.md) | TBD |
| [PFND3D10DDI_DESTROYQUERY callback](nc-d3d10umddi-pfnd3d10ddi-destroyquery.md) | The DestroyQuery(D3D10) function destroys the specified query object. The query object can be destoyed only if it is not currently bound to a display device. |
| [PFND3DWDDM2_0DDI_VIDEODECODERSUBMITBUFFERS1 callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-videodecodersubmitbuffers1.md) | TBD |
| [PFND3D10DDI_RESOURCEREADAFTERWRITEHAZARD callback](nc-d3d10umddi-pfnd3d10ddi-resourcereadafterwritehazard.md) | The ResourceReadAfterWriteHazard function informs the user-mode display driver that the specified resource was used as an output from the graphics processing unit (GPU) and that the resource will be used as an input to the GPU. |
| [PFND3D11_1DDI_DESTROYCRYPTOSESSION callback function](nc-d3d10umddi-pfnd3d11-1ddi-destroycryptosession.md) | TBD |
| [PFND3D11_1DDI_GETVIDEODECODERBUFFERINFO callback function](nc-d3d10umddi-pfnd3d11-1ddi-getvideodecoderbufferinfo.md) | TBD |
| [PFND3D10DDI_QUERYGETDATA callback](nc-d3d10umddi-pfnd3d10ddi-querygetdata.md) | The QueryGetData function polls for the state of a query operation. |
| [PFND3D11DDI_DESTROYUNORDEREDACCESSVIEW callback](nc-d3d10umddi-pfnd3d11ddi-destroyunorderedaccessview.md) | Destroys an unordered access view. |
| [PFND3D11DDI_STATE_CS_CONSTBUF_CB callback](nc-d3d10umddi-pfnd3d11ddi-state-cs-constbuf-cb.md) | The pfnStateCsConstBufCb function causes the Microsoft Direct3D 11 runtime to refresh the compute shader constant buffer state. |
| [PFND3D10DDI_DRAW callback](nc-d3d10umddi-pfnd3d10ddi-draw.md) | The Draw function draws nonindexed primitives. |
| [PFND3D10DDI_STATE_PS_CONSTBUF_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-ps-constbuf-cb.md) | The pfnStatePsConstBufCb function causes the Microsoft Direct3D 10 runtime to refresh the pixel shader stage's bound constant buffers. |
| [PFND3DWDDM1_3DDI_RELOCATEDEVICEFUNCS callback](nc-d3d10umddi-pfnd3dwddm1-3ddi-relocatedevicefuncs.md) | Notifies the user-mode display driver about the new location of the driver function table. Implemented by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [PFND3D11_1DDI_DESTROYAUTHENTICATEDCHANNEL callback function](nc-d3d10umddi-pfnd3d11-1ddi-destroyauthenticatedchannel.md) | TBD |
| [PFND3D11_1DDI_GETCERTIFICATE callback function](nc-d3d10umddi-pfnd3d11-1ddi-getcertificate.md) | TBD |
| [PFND3DWDDM2_0DDI_CALCPRIVATEQUERYSIZE callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-calcprivatequerysize.md) | TBD |
| [PFND3D11DDI_CALCPRIVATEUNORDEREDACCESSVIEWSIZE callback](nc-d3d10umddi-pfnd3d11ddi-calcprivateunorderedaccessviewsize.md) | The CalcPrivateUnorderedAccessViewSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for an unordered access view. |
| [PFND3D11DDI_CLEARUNORDEREDACCESSVIEWUINT callback](nc-d3d10umddi-pfnd3d11ddi-clearunorderedaccessviewuint.md) | The ClearUnorderedAccessViewUINT function clears the specified unordered-access view by setting it to a constant value. |
| [PFND3D10DDI_STATE_PS_SRV_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-ps-srv-cb.md) | The pfnStatePsSrvCb function causes the Microsoft Direct3D 10 runtime to refresh the pixel shader stage's bound shader resource views. |
| [PFND3DWDDM2_0DDI_CREATERASTERIZERSTATE callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-createrasterizerstate.md) | TBD |
| [PFND3D10DDI_DESTROYBLENDSTATE callback](nc-d3d10umddi-pfnd3d10ddi-destroyblendstate.md) | The DestroyBlendState function destroys the specified blend state object. The blend state object can be destoyed only if it is not currently bound to a display device. |
| [PFND3D10DDI_STATE_IA_INPUTLAYOUT_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-ia-inputlayout-cb.md) | The pfnStateIaInputLayoutCb function causes the Microsoft Direct3D 10 runtime to refresh the input layout state. |
| [PFND3D10DDI_STATE_OM_DEPTHSTATE_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-om-depthstate-cb.md) | The pfnStateOmDepthStateCb function causes the Microsoft Direct3D 10 runtime to refresh the output merger depth state. |
| [PFND3D10_1DDI_RELOCATEDEVICEFUNCS callback](nc-d3d10umddi-pfnd3d10-1ddi-relocatedevicefuncs.md) | The RelocateDeviceFuncs(D3D10_1) function notifies the user-mode display driver about the new location of the driver function table. |
| [PFND3DWDDM2_0DDI_GETDATAFORNEWHARDWAREKEY callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-getdatafornewhardwarekey.md) | TBD |
| [PFND3D11DDI_STATE_CS_SRV_CB callback](nc-d3d10umddi-pfnd3d11ddi-state-cs-srv-cb.md) | The pfnStateCsSrvCb function causes the Microsoft Direct3D 11 runtime to refresh the constant shader resource view state for the compute shader. |
| [PFND3DWDDM1_3DDI_SETMARKER callback](nc-d3d10umddi-pfnd3dwddm1-3ddi-setmarker.md) | Notifies the user-mode display driver that it must generate a new time stamp if any GPU work has completed since the last call to SetMarker. |
| [PFND3D10DDI_DESTROYDEVICE callback](nc-d3d10umddi-pfnd3d10ddi-destroydevice.md) | The DestroyDevice(D3D10) function destroys the specified device object. |
| [PFND3D10DDI_IA_SETTOPOLOGY callback](nc-d3d10umddi-pfnd3d10ddi-ia-settopology.md) | The IaSetTopology function sets the primitive topology to enable drawing for the input assember. |
| [PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMMIRROR callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-videoprocessorsetstreammirror.md) | TBD |
| [PFND3D11_1DDI_GETCAPTUREHANDLE callback](nc-d3d10umddi-pfnd3d11-1ddi-getcapturehandle.md) | Returns the handle for a specified resource that was allocated by the driver. This function also returns the size and location of specified data within the resource. |
| [PFND3D10DDI_STATE_GS_SRV_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-gs-srv-cb.md) | The pfnStateGsSrvCb function causes the Microsoft Direct3D 10 runtime to refresh the geometry shader constant shader resource view state. |
| [PFND3D11DDI_CREATEDEFERREDCONTEXT callback](nc-d3d10umddi-pfnd3d11ddi-createdeferredcontext.md) | The CreateDeferredContext function creates a deferred context. |
| [PFND3DWDDM1_3DDI_COPYTILES callback](nc-d3d10umddi-pfnd3dwddm1-3ddi-copytiles.md) | Copies tiles from buffer to tiled resource or vice versa. |
| [PFND3D11_1DDI_CREATEAUTHENTICATEDCHANNEL callback](nc-d3d10umddi-pfnd3d11-1ddi-createauthenticatedchannel.md) | Creates an authenticated channel object. Implemented by a Windows Display Driver Model (WDDM) 1.2 or later user-mode display driver. |
| [PFND3DWDDM2_0DDI_VIDEODECODERUPDATEDOWNSAMPLING callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-videodecoderupdatedownsampling.md) | TBD |
| [PFND3D11_1DDI_CREATEHULLSHADER callback](nc-d3d10umddi-pfnd3d11-1ddi-createhullshader.md) | Creates a hull shader. |
| [PFND3D11DDI_CALCDEFERREDCONTEXTHANDLESIZE callback](nc-d3d10umddi-pfnd3d11ddi-calcdeferredcontexthandlesize.md) | The CalcDeferredContextHandleSize function queries for the amount of storage space that the driver requires to satisfy deferred context handles to the given immediate context object. |
| [PFND3D11DDI_CALCPRIVATESHADERRESOURCEVIEWSIZE callback](nc-d3d10umddi-pfnd3d11ddi-calcprivateshaderresourceviewsize.md) | The CalcPrivateShaderResourceViewSize(D3D11) function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a shader resource view. |
| [PFND3D11_1DDI_CONFIGUREAUTHENTICATEDCHANNEL callback](nc-d3d10umddi-pfnd3d11-1ddi-configureauthenticatedchannel.md) | Processes a request from an application to configure an authenticated channel for content protection. Implemented by a Windows Display Driver Model (WDDM) 1.2 or later user-mode display driver. |
| [PFND3D11_1DDI_VIDEODECODERGETHANDLE callback function](nc-d3d10umddi-pfnd3d11-1ddi-videodecodergethandle.md) | TBD |
| [PFND3D10DDI_RESOURCERESOLVESUBRESOURCE callback](nc-d3d10umddi-pfnd3d10ddi-resourceresolvesubresource.md) | The ResourceResolveSubresource function resolves multiple samples to one pixel. |
| [PFND3D10DDI_SETSAMPLERS callback](nc-d3d10umddi-pfnd3d10ddi-setsamplers.md) | The CsSetSamplers function sets samplers for a compute shader. |
| [PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM callback function](nc-d3d10umddi-pfnd3d11-1ddi-destroyvideoprocessorenum.md) | TBD |
| [PFND3D11DDI_SETRENDERTARGETS callback](nc-d3d10umddi-pfnd3d11ddi-setrendertargets.md) | The SetRenderTargets(D3D11) function sets render target surfaces. |
| [PFND3D10DDI_STATE_TEXTFILTERSIZE_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-textfiltersize-cb.md) | The pfnStateTextFilterSizeCb function causes the Microsoft Direct3D 10 runtime to refresh the width and height of the monochrome convolution filter. |
| [PFND3D11_1DDI_VIDEODECODERSUBMITBUFFERS callback function](nc-d3d10umddi-pfnd3d11-1ddi-videodecodersubmitbuffers.md) | TBD |
| [PFND3D11DDI_STATE_DS_SHADER_CB callback](nc-d3d10umddi-pfnd3d11ddi-state-ds-shader-cb.md) | The pfnStateDsShaderCb function causes the Microsoft Direct3D 11 runtime to refresh the domain shader. |
| [PFND3D10DDI_CALCPRIVATEELEMENTLAYOUTSIZE callback](nc-d3d10umddi-pfnd3d10ddi-calcprivateelementlayoutsize.md) | The CalcPrivateElementLayoutSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for an element layout. |
| [PFND3D11_1DDI_FINISHSESSIONKEYREFRESH callback function](nc-d3d10umddi-pfnd3d11-1ddi-finishsessionkeyrefresh.md) | TBD |
| [PFND3D11DDI_CALCPRIVATEGEOMETRYSHADERWITHSTREAMOUTPUT callback](nc-d3d10umddi-pfnd3d11ddi-calcprivategeometryshaderwithstreamoutput.md) | The CalcPrivateGeometryShaderWithStreamOutput(D3D11) function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a geometry shader with stream output. |
| [PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE callback function](nc-d3d10umddi-pfnd3d11-1ddi-calcprivateauthenticatedchannelsize.md) | TBD |
| [PFND3D11_1DDI_GETCONTENTPROTECTIONCAPS callback function](nc-d3d10umddi-pfnd3d11-1ddi-getcontentprotectioncaps.md) | TBD |
| [PFND3D11_1DDI_CREATEDOMAINSHADER callback](nc-d3d10umddi-pfnd3d11-1ddi-createdomainshader.md) | Creates a domain shader. |
| [PFND3D11_1DDI_DESTROYVIDEOPROCESSORINPUTVIEW callback function](nc-d3d10umddi-pfnd3d11-1ddi-destroyvideoprocessorinputview.md) | TBD |
| [PFND3D11_1DDI_VIDEOPROCESSORINPUTVIEWREADAFTERWRITEHAZARD callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorinputviewreadafterwritehazard.md) | TBD |
| [PFND3D10DDI_OPENRESOURCE callback](nc-d3d10umddi-pfnd3d10ddi-openresource.md) | The OpenResource(D3D10) function opens a shared resource. |
| [PFND3D11DDI_STATE_CS_UAV_CB callback](nc-d3d10umddi-pfnd3d11ddi-state-cs-uav-cb.md) | The pfnStateCsUavCb function causes the Microsoft Direct3D 11 runtime to refresh the constant unordered access view state for the compute shader. |
| [PFND3D10DDI_DESTROYSHADERRESOURCEVIEW callback](nc-d3d10umddi-pfnd3d10ddi-destroyshaderresourceview.md) | The DestroyShaderResourceView function destroys the specified shader resource view object. The shader resource view object can be destoyed only if it is not currently bound to a display device. |
| [PFND3D11DDI_CALCPRIVATECOMMANDLISTSIZE callback](nc-d3d10umddi-pfnd3d11ddi-calcprivatecommandlistsize.md) | The CalcPrivateCommandListSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a command list. |
| [PFND3D10DDI_SETSCISSORRECTS callback](nc-d3d10umddi-pfnd3d10ddi-setscissorrects.md) | The SetScissorRects function marks portions of render targets that rendering is confined to. |
| [PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMAUTOPROCESSINGMODE callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetstreamautoprocessingmode.md) | TBD |
| [PFND3D11DDI_CREATERESOURCE callback](nc-d3d10umddi-pfnd3d11ddi-createresource.md) | Creates a resource. |
| [PFND3D11_1DDI_RESOURCECOPYREGION callback](nc-d3d10umddi-pfnd3d11-1ddi-resourcecopyregion.md) | Copies a source subresource region to a location on a destination subresource. |
| [PFND3D11DDI_DRAWINDEXEDINSTANCEDINDIRECT callback](nc-d3d10umddi-pfnd3d11ddi-drawindexedinstancedindirect.md) | The DrawIndexedInstancedIndirect function draws particular instances of indexed primitives. |
| [PFND3D11DDI_COPYSTRUCTURECOUNT callback](nc-d3d10umddi-pfnd3d11ddi-copystructurecount.md) | The CopyStructureCount function copies the number of items in the filled portion (that is, the filled-size value) of an append buffer unordered access view (UAV) to an offset into a destination buffer. |
| [PFND3D11DDI_COMMANDLISTEXECUTE callback](nc-d3d10umddi-pfnd3d11ddi-commandlistexecute.md) | The CommandListExecute function runs a command list. |
| [PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMEXTENSION callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetstreamextension.md) | TBD |
| [PFND3DWDDM2_0DDI_CHECKCRYPTOSESSIONSTATUS callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-checkcryptosessionstatus.md) | TBD |
| [PFND3DWDDM1_3DDI_GETMIPPACKING callback](nc-d3d10umddi-pfnd3dwddm1-3ddi-getmippacking.md) | For a given tiled resource, returns how many mips are packed, and how many tiles are needed to store all the packed mips. |
| [PFND3D10DDI_CALCPRIVATERENDERTARGETVIEWSIZE callback](nc-d3d10umddi-pfnd3d10ddi-calcprivaterendertargetviewsize.md) | The CalcPrivateRenderTargetViewSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a render target view. |
| [PFND3D10DDI_CLEARDEPTHSTENCILVIEW callback](nc-d3d10umddi-pfnd3d10ddi-cleardepthstencilview.md) | The ClearDepthStencilView function clears the specified currently bound depth-stencil view. |
| [PFND3D11_1DDI_CREATEVIDEOPROCESSOROUTPUTVIEW callback](nc-d3d10umddi-pfnd3d11-1ddi-createvideoprocessoroutputview.md) | Creates a resource view for a video processor. This view defines the output sample for the video processing operation. |
| [PFND3D11_1DDI_VIDEODECODEREXTENSION callback function](nc-d3d10umddi-pfnd3d11-1ddi-videodecoderextension.md) | TBD |
| [PFND3DWDDM2_0DDI_VIDEOPROCESSORSETOUTPUTCOLORSPACE1 callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-videoprocessorsetoutputcolorspace1.md) | TBD |
| [PFND3D10DDI_RESOURCEUPDATESUBRESOURCEUP callback](nc-d3d10umddi-pfnd3d10ddi-resourceupdatesubresourceup.md) | The DefaultConstantBufferUpdateSubresourceUP function updates a destination subresource region that stores constant buffers from a source system-memory region. |
| [PFND3DWDDM2_2DDI_CALCPRIVATE_SHADERCACHE_SESSION_SIZE callback function](nc-d3d10umddi-pfnd3dwddm2-2ddi-calcprivate-shadercache-session-size.md) | TBD |
| [PFND3D11DDI_CHECKDEFERREDCONTEXTHANDLESIZES callback](nc-d3d10umddi-pfnd3d11ddi-checkdeferredcontexthandlesizes.md) | The CheckDeferredContextHandleSizes function verifies the sizes of the driver-private memory spaces that hold the handle data of deferred context handles. |
| [PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCOLORSPACE callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetoutputcolorspace.md) | TBD |
| [PFND3D11DDI_CREATEUNORDEREDACCESSVIEW callback](nc-d3d10umddi-pfnd3d11ddi-createunorderedaccessview.md) | The CreateUnorderedAccessView function creates an unordered access view. |
| [PFND3D11_1DDI_CHECKVIDEOPROCESSORFORMAT callback function](nc-d3d10umddi-pfnd3d11-1ddi-checkvideoprocessorformat.md) | TBD |
| [PFND3DWDDM2_0DDI_CALCPRIVATERENDERTARGETVIEWSIZE callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-calcprivaterendertargetviewsize.md) | TBD |
| [PFND3D10DDI_CALCPRIVATESHADERRESOURCEVIEWSIZE callback](nc-d3d10umddi-pfnd3d10ddi-calcprivateshaderresourceviewsize.md) | The CalcPrivateShaderResourceViewSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a shader resource view. |
| [PFND3D11_1DDI_DESTROYVIDEOPROCESSOROUTPUTVIEW callback function](nc-d3d10umddi-pfnd3d11-1ddi-destroyvideoprocessoroutputview.md) | TBD |
| [PFND3D11_1DDI_GETVIDEODECODERBUFFERTYPECOUNT callback function](nc-d3d10umddi-pfnd3d11-1ddi-getvideodecoderbuffertypecount.md) | TBD |
| [PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSTEREOFORMAT callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetstreamstereoformat.md) | TBD |
| [PFND3D10DDI_RESOURCEUNMAP callback](nc-d3d10umddi-pfnd3d10ddi-resourceunmap.md) | The ResourceUnmap function unmaps a subresource of a resource. |
| [PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMFRAMEFORMAT callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetstreamframeformat.md) | TBD |
| [PFND3D11_1DDI_DESTROYVIDEODECODEROUTPUTVIEW callback function](nc-d3d10umddi-pfnd3d11-1ddi-destroyvideodecoderoutputview.md) | TBD |
| [PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMALPHA callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetstreamalpha.md) | TBD |
| [PFND3D11_1DDI_DESTROYVIDEOPROCESSOR callback function](nc-d3d10umddi-pfnd3d11-1ddi-destroyvideoprocessor.md) | TBD |
| [PFND3D10DDI_SETTEXTFILTERSIZE callback](nc-d3d10umddi-pfnd3d10ddi-settextfiltersize.md) | The SetTextFilterSize function sets the width and height of the monochrome convolution filter. |
| [PFND3D11_1DDI_RELOCATEDEVICEFUNCS callback](nc-d3d10umddi-pfnd3d11-1ddi-relocatedevicefuncs.md) | Notifies the user-mode display driver about the new location of the driver function table. |
| [PFND3DWDDM2_0DDI_GETCRYPTOSESSIONPRIVATEDATASIZE callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-getcryptosessionprivatedatasize.md) | TBD |
| [PFND3DWDDM2_1DDI_SYNC_TOKEN callback function](nc-d3d10umddi-pfnd3dwddm2-1ddi-sync-token.md) | TBD |
| [PFND3D10DDI_QUERYBEGIN callback](nc-d3d10umddi-pfnd3d10ddi-querybegin.md) | The QueryBegin function marks the beginning of a sequence of graphics commands for a query and transitions the query to the &#0034;building&#0034; state. |
| [PFND3D10DDI_DESTROYDEPTHSTENCILSTATE callback](nc-d3d10umddi-pfnd3d10ddi-destroydepthstencilstate.md) | The DestroyDepthStencilState function destroys the specified depth stencil state object. The depth stencil state object can be destoyed only if it is not currently bound to a display device. |
| [PFND3D10DDI_DRAWINSTANCED callback](nc-d3d10umddi-pfnd3d10ddi-drawinstanced.md) | The DrawInstanced function draws particular instances of nonindexed primitives. |
| [PFND3D11DDI_CREATECOMPUTESHADER callback](nc-d3d10umddi-pfnd3d11ddi-createcomputeshader.md) | The CreateComputeShader function creates a compute shader. |
| [PFND3D10DDI_STATE_GS_CONSTBUF_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-gs-constbuf-cb.md) | The pfnStateGsConstBufCb function causes the Microsoft Direct3D 10 runtime to refresh the geometry shader constant buffer state. |
| [PFND3D11_1DDI_GETVIDEOPROCESSORCUSTOMRATE callback function](nc-d3d10umddi-pfnd3d11-1ddi-getvideoprocessorcustomrate.md) | TBD |
| [PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORINPUTVIEWSIZE callback](nc-d3d10umddi-pfnd3d11-1ddi-calcprivatevideoprocessorinputviewsize.md) | Returns the number of bytes that the driver requires to store private data for the video processor input view state. |
| [PFND3D10DDI_CREATEPIXELSHADER callback](nc-d3d10umddi-pfnd3d10ddi-createpixelshader.md) | The CreatePixelShader(D3D10) function creates a pixel shader. |
| [PFND3D11_1DDI_GETVIDEOPROCESSORFILTERRANGE callback function](nc-d3d10umddi-pfnd3d11-1ddi-getvideoprocessorfilterrange.md) | TBD |
| [PFND3D10DDI_DESTROYRESOURCE callback](nc-d3d10umddi-pfnd3d10ddi-destroyresource.md) | The DestroyResource(D3D10) function destroys the specified resource object. The resource object can be destoyed only if it is not currently bound to a display device, and if all views that refer to the resource are also destroyed. |
| [PFND3D11_1DDI_CREATERASTERIZERSTATE callback](nc-d3d10umddi-pfnd3d11-1ddi-createrasterizerstate.md) | Creates a rasterizer state. |
| [PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS callback function](nc-d3d10umddi-pfnd3d11-1ddi-getvideoprocessorrateconversioncaps.md) | TBD |
| [PFND3D10DDI_SETRENDERTARGETS callback](nc-d3d10umddi-pfnd3d10ddi-setrendertargets.md) | The SetRenderTargets function sets render target surfaces. |
| [PFND3D11_1DDI_DISCARD callback](nc-d3d10umddi-pfnd3d11-1ddi-discard.md) | Discards (evicts) an allocation from video display memory. Implemented by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [PFND3D11DDI_CREATESHADERRESOURCEVIEW callback](nc-d3d10umddi-pfnd3d11ddi-createshaderresourceview.md) | The CreateShaderResourceView(D3D11) function creates a shader resource view. |
| [PFND3D11_1DDI_GETCERTIFICATESIZE callback function](nc-d3d10umddi-pfnd3d11-1ddi-getcertificatesize.md) | TBD |
| [PFND3D11DDI_STATE_CS_SHADER_CB callback](nc-d3d10umddi-pfnd3d11ddi-state-cs-shader-cb.md) | The pfnStateCsShaderCb function causes the Microsoft Direct3D 11 runtime to refresh the compute shader. |
| [PFND3D11DDI_DRAWINSTANCEDINDIRECT callback](nc-d3d10umddi-pfnd3d11ddi-drawinstancedindirect.md) | The DrawInstancedIndirect function draws particular instances of non-indexed primitives. |
| [PFND3D10DDI_SO_SETTARGETS callback](nc-d3d10umddi-pfnd3d10ddi-so-settargets.md) | The SoSetTargets function sets stream output target resources. |
| [PFND3D11_1DDI_SETCONSTANTBUFFERS callback](nc-d3d10umddi-pfnd3d11-1ddi-setconstantbuffers.md) | Sets constant buffers for a compute shader. |
| [PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTSTEREOMODE callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetoutputstereomode.md) | TBD |
| [PFND3D10DDI_SETSHADER callback](nc-d3d10umddi-pfnd3d10ddi-setshader.md) | The CsSetShader function sets the compute shader code so that all of the subsequent dispatching operations use that code. |
| [PFND3D10DDI_CALCPRIVATEOPENEDRESOURCESIZE callback](nc-d3d10umddi-pfnd3d10ddi-calcprivateopenedresourcesize.md) | The CalcPrivateOpenedResourceSize function determines the size of the user-mode display driver's private shared region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for an opened resource. |
| [PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTBACKGROUNDCOLOR callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetoutputbackgroundcolor.md) | TBD |
| [PFND3D11DDI_SETSHADER_WITH_IFACES callback](nc-d3d10umddi-pfnd3d11ddi-setshader-with-ifaces.md) | The CsSetShaderWithIfaces function sets the compute shader code along with a group of interfaces so that all of the subsequent dispatching operations use that code and those interfaces. |
| [PFND3D10DDI_CALCPRIVATEBLENDSTATESIZE callback](nc-d3d10umddi-pfnd3d10ddi-calcprivateblendstatesize.md) | The CalcPrivateBlendStateSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a blend state. |
| [PFND3D10_2DDI_GETSUPPORTEDVERSIONS callback](nc-d3d10umddi-pfnd3d10-2ddi-getsupportedversions.md) | The GetSupportedVersions function queries for the Direct3D interface versions that the driver supports. |
| [PFND3D10DDI_RESOURCECOPY callback](nc-d3d10umddi-pfnd3d10ddi-resourcecopy.md) | The ResourceCopy function copies an entire source resource to a destination resource. |
| [PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTTARGETRECT callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetoutputtargetrect.md) | TBD |
| [PFND3D10DDI_STATE_VS_CONSTBUF_CB callback](nc-d3d10umddi-pfnd3d10ddi-state-vs-constbuf-cb.md) | The pfnStateVsConstBufCb function causes the Microsoft Direct3D 10 runtime to refresh the vertex shader stage's bound constant buffers. |
| [PFND3D10DDI_CREATEVERTEXSHADER callback](nc-d3d10umddi-pfnd3d10ddi-createvertexshader.md) | The CreateVertexShader(D3D10) function creates a vertex shader. |
| [PFND3D10DDI_SETSHADERRESOURCES callback](nc-d3d10umddi-pfnd3d10ddi-setshaderresources.md) | The CsSetShaderResources function sets resources for a compute shader. |
| [PFND3D10DDI_SHADERRESOURCEVIEWREADAFTERWRITEHAZARD callback](nc-d3d10umddi-pfnd3d10ddi-shaderresourceviewreadafterwritehazard.md) | The ShaderResourceViewReadAfterWriteHazard function informs the user-mode display driver that the specified resource was used as an output from the graphics processing unit (GPU) and that the resource will be used as an input to the GPU. |
| [PFND3DWDDM2_0DDI_CREATERENDERTARGETVIEW callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-createrendertargetview.md) | TBD |
| [PFND3DWDDM2_2DDI_SHADERCACHE_STORE_VALUE_CB callback function](nc-d3d10umddi-pfnd3dwddm2-2ddi-shadercache-store-value-cb.md) | TBD |
| [PFND3DWDDM2_0DDI_QUERYVIDEOCAPABILITIES callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-queryvideocapabilities.md) | TBD |
| [PFND3D10DDI_DRAWINDEXED callback](nc-d3d10umddi-pfnd3d10ddi-drawindexed.md) | The DrawIndexed function draws indexed primitives. |
| [PFND3D10DDI_RETRIEVESUBOBJECT callback](nc-d3d10umddi-pfnd3d10ddi-retrievesubobject.md) | Retrieves subparts of the Microsoft Direct3D driver device object. |
| [PFND3D10DDI_RESETPRIMITIVEID callback function](nc-d3d10umddi-pfnd3d10ddi-resetprimitiveid.md) | TBD |
| [PFND3D11DDI_RECYCLECOMMANDLIST callback](nc-d3d10umddi-pfnd3d11ddi-recyclecommandlist.md) | The RecycleCommandList function recycles a command list. |
| [PFND3D11_1DDI_QUERYAUTHENTICATEDCHANNEL callback](nc-d3d10umddi-pfnd3d11-1ddi-queryauthenticatedchannel.md) | Queries an authenticated channel for capability and state information. Implemented by a Windows Display Driver Model (WDDM) 1.2 or later user-mode display driver. |
| [PFND3D11_1DDI_GETENCRYPTIONBLTKEY callback function](nc-d3d10umddi-pfnd3d11-1ddi-getencryptionbltkey.md) | TBD |
| [PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMCOLORSPACE1 callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-videoprocessorsetstreamcolorspace1.md) | TBD |
| [PFND3D11DDI_CALCPRIVATETESSELLATIONSHADERSIZE callback](nc-d3d10umddi-pfnd3d11ddi-calcprivatetessellationshadersize.md) | The CalcPrivateTessellationShaderSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a hull or domain shader. |
| [PFND3D11DDI_STATE_HS_SHADER_CB callback](nc-d3d10umddi-pfnd3d11ddi-state-hs-shader-cb.md) | The pfnStateHsShaderCb function causes the Microsoft Direct3D 11 runtime to refresh the hull shader. |
| [PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMLUMAKEY callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetstreamlumakey.md) | TBD |
| [PFND3D11_1DDI_CREATEVIDEOPROCESSOR callback](nc-d3d10umddi-pfnd3d11-1ddi-createvideoprocessor.md) | Creates a video processor object. |
| [PFND3D10DDI_FLUSH callback](nc-d3d10umddi-pfnd3d10ddi-flush.md) | The Flush(D3D10) function submits outstanding hardware commands that are in the hardware command buffer to the display miniport driver. |
| [PFND3D10DDI_CREATEQUERY callback](nc-d3d10umddi-pfnd3d10ddi-createquery.md) | The CreateQuery(D3D10) function creates a query. |
| [PFND3D11DDI_PERFORM_AMORTIZED_PROCESSING_CB callback](nc-d3d10umddi-pfnd3d11ddi-perform-amortized-processing-cb.md) | The pfnPerformAmortizedProcessingCb function performs amortized processing. |
| [PFND3D11_1DDI_DESTROYVIDEODECODER callback function](nc-d3d10umddi-pfnd3d11-1ddi-destroyvideodecoder.md) | TBD |
| [PFND3D10DDI_SETBLENDSTATE callback](nc-d3d10umddi-pfnd3d10ddi-setblendstate.md) | The SetBlendState function sets a blend state. |
| [PFND3D11_1DDI_CALCPRIVATETESSELLATIONSHADERSIZE callback function](nc-d3d10umddi-pfnd3d11-1ddi-calcprivatetessellationshadersize.md) | TBD |
| [PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE callback function](nc-d3d10umddi-pfnd3d11-1ddi-videoprocessorsetoutputalphafillmode.md) | TBD |
| [PFND3D11DDI_RECYCLECREATECOMMANDLIST callback](nc-d3d10umddi-pfnd3d11ddi-recyclecreatecommandlist.md) | The RecycleCreateCommandList function creates a command list and makes a previously unused DDI handle completely valid again. |
| [PFND3D11DDI_CREATECOMMANDLIST callback](nc-d3d10umddi-pfnd3d11ddi-createcommandlist.md) | The CreateCommandList function creates a command list. |
| [PFND3D10DDI_CALCPRIVATEQUERYSIZE callback](nc-d3d10umddi-pfnd3d10ddi-calcprivatequerysize.md) | The CalcPrivateQuerySize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a query. |
| [PFND3DWDDM2_0DDI_GETRESOURCELAYOUT callback function](nc-d3d10umddi-pfnd3dwddm2-0ddi-getresourcelayout.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [D3D10DDIARG_INPUT_ELEMENT_DESC structure](ns-d3d10umddi-d3d10ddiarg-input-element-desc.md) | The D3D10DDIARG_INPUT_ELEMENT_DESC structure describes an element of a layout. |
| [D3D11DDI_CORELAYER_DEVICECALLBACKS structure](ns-d3d10umddi-d3d11ddi-corelayer-devicecallbacks~r1.md) | The D3D11DDI_CORELAYER_DEVICECALLBACKS structure contains Microsoft Direct3D 11 runtime callback functions that the user-mode display driver can use. |
| [D3D10DDIARG_TEX2D_DEPTHSTENCILVIEW structure](ns-d3d10umddi-d3d10ddiarg-tex2d-depthstencilview.md) | The D3D10DDIARG_TEX2D_DEPTHSTENCILVIEW structure describes a two-dimensional (2-D) texture that is used to create a depth stencil view in a call to the CreateDepthStencilView function. |
| [D3D11_1DDI_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_COUNT_OUTPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-restricted-shared-resource-process-count-output.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_COUNT. |
| [D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_DATA structure](ns-d3d10umddi-d3dwddm2-0ddi-key-exchange-hw-protection-data.md) | D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_DATA is used with NegotiateCryptoSessionKeyExchange in the implementation of Digital Rights Management (DRM). |
| [D3DWDDM2_0DDI_DEVICEFUNCS structure](ns-d3d10umddi-d3dwddm2-0ddi-devicefuncs~r1.md) | This structure contains the user mode device function table for Windows Display Driver Model (WDDM) 2.0. |
| [D3D10DDIARG_TEXCUBE_SHADERRESOURCEVIEW structure](ns-d3d10umddi-d3d10ddiarg-texcube-shaderresourceview.md) | The D3D10DDIARG_TEXCUBE_SHADERRESOURCEVIEW structure describes a cube texture that is used to create a shader resource view in a call to the CreateShaderResourceView function. |
| [D3DWDDM2_0DDIARG_TEX2D_UNORDEREDACCESSVIEW structure](ns-d3d10umddi-d3dwddm2-0ddiarg-tex2d-unorderedaccessview.md) | TBD |
| [D3D11_1DDI_AUTHENTICATED_QUERY_UNRESTRICTED_PROTECTED_SHARED_RESOURCE_COUNT_OUTPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-unrestricted-protected-shared-resource-count-output.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_QUERY_UNRESTRICTED_PROTECTED_SHARED_RESOURCE_COUNT. |
| [D3D11DDI_HANDLESIZE structure](ns-d3d10umddi-d3d11ddi-handlesize.md) | The D3D11DDI_HANDLESIZE structure describes a handle. |
| [D3D10_DDIARG_CREATE_SAMPLER structure](ns-d3d10umddi-d3d10-ddiarg-create-sampler.md) | TBD |
| [D3D10DDIARG_CREATEDEPTHSTENCILVIEW structure](ns-d3d10umddi-d3d10ddiarg-createdepthstencilview.md) | The D3D10DDIARG_CREATEDEPTHSTENCILVIEW structure describes the depth stencil view to create. |
| [D3D10_2DDIARG_GETCAPS structure](ns-d3d10umddi-d3d10-2ddiarg-getcaps.md) | The D3D10_2DDIARG_GETCAPS structure contains display device capabilities of a particular type. |
| [D3DWDDM2_0DDIARG_CREATEUNORDEREDACCESSVIEW structure](ns-d3d10umddi-d3dwddm2-0ddiarg-createunorderedaccessview.md) | TBD |
| [D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE structure](ns-d3d10umddi-d3dwddm1-3ddi-tiled-resource-coordinate.md) | Specifies the (x, y, z) coordinate values below the index tiles of a tiled resource, along with the respective subresource. Note that the coordinate values do not indicate pixels or bytes. |
| [D3DWDDM1_3DDI_DEVICEFUNCS structure](ns-d3d10umddi-d3dwddm1-3ddi-devicefuncs~r1.md) | Contains functions that a user-mode display driver that is optimized for the Microsoft Direct3D version 11.2 runtime can implement to render graphics primitives and process state changes. |
| [D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING structure](ns-d3d10umddi-d3dwddm2-0ddi-video-capability-decoder-downsampling.md) | D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING describes the details of a video decoder downsampling operation. |
| [D3DWDDM1_3DDI_D3D11_OPTIONS_DATA1 structure](ns-d3d10umddi-d3dwddm1-3ddi-d3d11-options-data1.md) | Specifies the level of support by the hardware and user-mode display driver for tiled resources. |
| [D3D11DDI_SHADER_CAPS structure](ns-d3d10umddi-d3d11ddi-shader-caps.md) | The D3D11DDI_SHADER_CAPS structure contains display device shader capabilities. |
| [D3D10DDIARG_REGISTER_DESC structure](ns-d3d10umddi-d3d10ddiarg-register-desc.md) | TBD |
| [D3D11_1DDI_AUTHENTICATED_PROTECTION_FLAGS structure](ns-d3d10umddi-d3d11-1ddi-authenticated-protection-flags.md) | Specifies the protection level for video content. |
| [D3DWDDM2_0DDIARG_CREATEQUERY structure](ns-d3d10umddi-d3dwddm2-0ddiarg-createquery.md) | TBD |
| [D3D11_1DDI_D3D11_OPTIONS_DATA structure](ns-d3d10umddi-d3d11-1ddi-d3d11-options-data.md) | Specifies options to provide data to the user-mode display driver. |
| [D3D11_1DDI_ENCRYPTED_BLOCK_INFO structure](ns-d3d10umddi-d3d11-1ddi-encrypted-block-info.md) | Specifies which bytes in a video surface are encrypted. |
| [D3D10_DDI_VIEWPORT structure](ns-d3d10umddi-d3d10-ddi-viewport.md) | The D3D10_DDI_VIEWPORT structure describes a viewport. |
| [D3D11_1DDIARG_VIDEODECODEREXTENSION structure](ns-d3d10umddi-d3d11-1ddiarg-videodecoderextension.md) | Specifies driver-specific data for the extended Microsoft DirectX Video Acceleration (DXVA) decoding function that is provided by a call to the VideoDecoderExtension function. |
| [D3D11_1DDI_VIDEO_INPUT structure](ns-d3d10umddi-d3d11-1ddi-video-input.md) | Reserved for system use. Do not use in your driver. |
| [D3D11_1DDIARG_CREATECRYPTOSESSION structure](ns-d3d10umddi-d3d11-1ddiarg-createcryptosession.md) | Specifies the attributes of the cryptographic session to be created by the user-mode driver's CreateCryptoSession function. |
| [D3D11_1DDI_AUTHENTICATED_CONFIGURE_PROTECTION structure](ns-d3d10umddi-d3d11-1ddi-authenticated-configure-protection.md) | Contains input data for a call to the ConfigureAuthenticatedChannel(D3D11_1) function when D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT.ConfigureType has a GUID value of D3D11_AUTHENTICATED_CONFIGURE_PROTECTION. |
| [D3DWDDM2_0DDI_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK structure](ns-d3d10umddi-d3dwddm2-0ddi-video-decoder-sub-sample-mapping-block.md) | D3DWDDM2_0DDI_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK is used with VideoDecoderSubmitBuffers1 to describe the decoder buffer sub sample mapping block size. |
| [D3D11_1DDI_VIDEO_DECODER_DESC structure](ns-d3d10umddi-d3d11-1ddi-video-decoder-desc.md) | Describes a video stream for a Microsoft Direct3D video decoder or video processor. |
| [D3DWDDM2_2DDI_TEXTURE_LAYOUT_CAPS structure](ns-d3d10umddi-d3dwddm2-2ddi-texture-layout-caps.md) | TBD |
| [D3D11DDIARG_POINTERDATA structure](ns-d3d10umddi-d3d11ddiarg-pointerdata.md) | The D3D11DDIARG_POINTERDATA structure describes the location of the data that is reference by a class instance that has been assigned to an interface implementation. |
| [D3D10DDI_MAPPED_SUBRESOURCE structure](ns-d3d10umddi-d3d10ddi-mapped-subresource.md) | The D3D10DDI_MAPPED_SUBRESOURCE structure describes a subresource that the driver maps to through a call to the driver's ResourceMap function. |
| [D3D10DDIARG_VERTEXPIPELINEOUTPUT structure](ns-d3d10umddi-d3d10ddiarg-vertexpipelineoutput.md) | TBD |
| [D3DWDDM2_0DDI_D3D11_OPTIONS2_DATA structure](ns-d3d10umddi-d3dwddm2-0ddi-d3d11-options2-data.md) | TBD |
| [D3D10DDIARG_STAGE_IO_SIGNATURES structure](ns-d3d10umddi-d3d10ddiarg-stage-io-signatures.md) | The D3D10DDIARG_STAGE_IO_SIGNATURES structure describes an I/O signature. |
| [D3DWDDM2_0DDI_VIDEO_INPUT structure](ns-d3d10umddi-d3dwddm2-0ddi-video-input.md) | TBD |
| [D3D11DDIARG_BUFFER_UNORDEREDACCESSVIEW structure](ns-d3d10umddi-d3d11ddiarg-buffer-unorderedaccessview.md) | The D3D11DDIARG_BUFFER_UNORDEREDACCESSVIEW structure describes a buffer that is used to create an unordered access view (UAV) in a call to the CreateUnorderedAccessView function. |
| [D3DWDDM2_2DDI_CORELAYER_DEVICECALLBACKS structure](ns-d3d10umddi-d3dwddm2-2ddi-corelayer-devicecallbacks~r1.md) | Specifies core layer device callback functions. |
| [D3D10DDIARG_CREATEQUERY structure](ns-d3d10umddi-d3d10ddiarg-createquery.md) | The D3D10DDIARG_CREATEQUERY structure describes the query to create. |
| [D3D11_1DDI_VIDEO_PROCESSOR_RATE_CONVERSION_CAPS structure](ns-d3d10umddi-d3d11-1ddi-video-processor-rate-conversion-caps.md) | Defines a group of video processor capabilities that are associated with frame-rate conversion, including deinterlacing and inverse telecine. |
| [D3D11_1DDIARG_CREATEVIDEODECODER structure](ns-d3d10umddi-d3d11-1ddiarg-createvideodecoder.md) | Specifies the attributes of a video decoder object. |
| [D3D11_1DDIARG_SIGNATURE_ENTRY2 structure](ns-d3d10umddi-d3d11-1ddiarg-signature-entry2.md) | TBD |
| [D3DWDDM2_0DDI_VIDEO_OUTPUT structure](ns-d3d10umddi-d3dwddm2-0ddi-video-output.md) | TBD |
| [D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC structure](ns-d3d10umddi-d3dwddm2-2ddi-swizzle-pattern-desc.md) | Describes a swizzle pattern. |
| [D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_CAPS structure](ns-d3d10umddi-d3dwddm2-0ddi-video-capability-decoder-caps.md) | D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_CAPS contains information describing the capabilities of the video decoder. |
| [D3DWDDM2_0DDI_SWIZZLE_PATTERN_DESC structure](ns-d3d10umddi-d3dwddm2-0ddi-swizzle-pattern-desc.md) | TBD |
| [D3D10DDI_MIPINFO structure](ns-d3d10umddi-d3d10ddi-mipinfo.md) | The D3D10DDI_MIPINFO structure describes the MIP-level texture and physical coordinates of a surface. |
| [D3D10_DDI_QUERY_DATA_TIMESTAMP_DISJOINT structure](ns-d3d10umddi-d3d10-ddi-query-data-timestamp-disjoint.md) | The D3D10_DDI_QUERY_DATA_TIMESTAMP_DISJOINT structure describes timestamp-disjoint information that is used in a call to the CreateQuery(D3D10) function to create a D3D10DDI_QUERY_TIMESTAMPDISJOINT query type and in a call to the QueryGetData function to return information about the query. |
| [D3D10DDI_DEVICEFUNCS structure](ns-d3d10umddi-d3d10ddi-devicefuncs.md) | TBD |
| [D3D11DDI_THREADING_CAPS structure](ns-d3d10umddi-d3d11ddi-threading-caps.md) | The D3D11DDI_THREADING_CAPS structure contains display device threading capabilities. |
| [D3D11_1DDI_AUTHENTICATED_QUERY_ACESSIBILITY_OUTPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-acessibility-output.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ATTRIBUTES. |
| [D3DWDDM2_0DDI_GPUVA_CAPS_DATA structure](ns-d3d10umddi-d3dwddm2-0ddi-gpuva-caps-data.md) | TBD |
| [D3D10_DDI_BLEND_DESC structure](ns-d3d10umddi-d3d10-ddi-blend-desc.md) | The D3D10_DDI_BLEND_DESC structure describes a blend state. |
| [D3DWDDM2_0DDIARG_TEX2D_RENDERTARGETVIEW structure](ns-d3d10umddi-d3dwddm2-0ddiarg-tex2d-rendertargetview.md) | TBD |
| [D3D10DDIARG_CREATEELEMENTLAYOUT structure](ns-d3d10umddi-d3d10ddiarg-createelementlayout.md) | The D3D10DDIARG_CREATEELEMENTLAYOUT structure describes the element layout to create. |
| [D3D10DDIARG_TEXCUBE_DEPTHSTENCILVIEW structure](ns-d3d10umddi-d3d10ddiarg-texcube-depthstencilview.md) | The D3D10DDIARG_TEXCUBE_DEPTHSTENCILVIEW structure describes a cube texture that is used to create a depth stencil view in a call to the CreateDepthStencilView function. |
| [D3D10_1DDI_DEVICEFUNCS structure](ns-d3d10umddi-d3d10-1ddi-devicefuncs~r1.md) | The D3D10_1DDI_DEVICEFUNCS structure contains functions that a user-mode display driver that is optimized for the Microsoft Direct3D version 10.1 runtime can implement to render graphics primitives and process state changes. |
| [D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW structure](ns-d3d10umddi-d3d11-1ddiarg-createvideodecoderoutputview.md) | Describes the video decoder's output-view state. |
| [D3D11DDIARG_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT structure](ns-d3d10umddi-d3d11ddiarg-creategeometryshaderwithstreamoutput.md) | The D3D11DDIARG_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT structure describes the geometry shader with stream output to create. |
| [D3D11DDI_DEVICEFUNCS structure](ns-d3d10umddi-d3d11ddi-devicefuncs~r1.md) | The D3D11DDI_DEVICEFUNCS structure contains functions that a user-mode display driver that is optimized for the Microsoft Direct3D version 11 runtime can implement to render graphics primitives and process state changes. |
| [D3D11_DDI_SHADER_MIN_PRECISION_SUPPORT_DATA structure](ns-d3d10umddi-d3d11-ddi-shader-min-precision-support-data.md) | Describes precision support options for shaders in the user-mode display driver. |
| [D3D10_1_DDI_BLEND_DESC structure](ns-d3d10umddi-d3d10-1-ddi-blend-desc.md) | The D3D10_1_DDI_BLEND_DESC structure describes a blend state. |
| [D3D10DDIARG_CREATERENDERTARGETVIEW structure](ns-d3d10umddi-d3d10ddiarg-createrendertargetview.md) | The D3D10DDIARG_CREATERENDERTARGETVIEW structure describes the render target view to create. |
| [D3D11_1DDI_VIDEO_PROCESSOR_CAPS structure](ns-d3d10umddi-d3d11-1ddi-video-processor-caps.md) | Describes the capabilities of a Microsoft Direct3D 11 video processor. |
| [D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-configure-input.md) | Contains input data for the ConfigureAuthenticatedChannel(D3D11_1) function. |
| [D3D11DDIARG_CREATEUNORDEREDACCESSVIEW structure](ns-d3d10umddi-d3d11ddiarg-createunorderedaccessview.md) | The D3D11DDIARG_CREATEUNORDEREDACCESSVIEW structure describes the unordered access view to create. |
| [D3D10DDI_CORELAYER_DEVICECALLBACKS structure](ns-d3d10umddi-d3d10ddi-corelayer-devicecallbacks.md) | The D3D10DDI_CORELAYER_DEVICECALLBACKS structure contains Microsoft Direct3D 10 runtime callback functions that the user-mode display driver can use. |
| [D3D10DDI_ADAPTERFUNCS structure](ns-d3d10umddi-d3d10ddi-adapterfuncs.md) | The D3D10DDI_ADAPTERFUNCS structure contains functions that the user-mode display driver can implement to communicate with a graphics adapter object. |
| [D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT_ID_COUNT_OUTPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-output-id-count-output.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT_ID_COUNT. |
| [D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA structure](ns-d3d10umddi-d3dwddm2-0ddi-key-exchange-hw-protection-output-data.md) | D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA is used with D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_DATA in the implementation of Digital Rights Management (DRM). |
| [D3DWDDM2_0DDI_VIDEODEVICEFUNCS structure](ns-d3d10umddi-d3dwddm2-0ddi-videodevicefuncs.md) | Specifies the video function table for the Microsoft Direct3D driver device object. Used only by Windows Display Driver Model (WDDM) 2.0 and later drivers. |
| [D3DWDDM2_0DDI_DEVICE_DEPENDENT_SWIZZLE_LAYOUT_CAPS structure](ns-d3d10umddi-d3dwddm2-0ddi-device-dependent-swizzle-layout-caps.md) | TBD |
| [D3D11_1DDI_VIDEO_PROCESSOR_CONTENT_DESC structure](ns-d3d10umddi-d3d11-1ddi-video-processor-content-desc.md) | Describes a video stream for a video processor. |
| [D3D10DDIARG_CALCPRIVATEDEVICESIZE structure](ns-d3d10umddi-d3d10ddiarg-calcprivatedevicesize.md) | The D3D10DDIARG_CALCPRIVATEDEVICESIZE structure describes the parameters that the user-mode display driver uses to calculate the size of a memory block that the driver requires to store frequently-accessed data. |
| [D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT_ID_COUNT_INPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-output-id-count-input.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_INPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT_ID_COUNT. |
| [D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO structure](ns-d3d10umddi-d3d11-1ddi-video-decoder-buffer-info.md) | Specifies information about a video decoder buffer. |
| [D3D10DDIARG_OPENADAPTER structure](ns-d3d10umddi-d3d10ddiarg-openadapter.md) | The D3D10DDIARG_OPENADAPTER structure describes the graphics adapter object. |
| [D3D11_1DDI_VIDEO_COLOR_YCbCrA structure](ns-d3d10umddi-d3d11-1ddi-video-color-ycbcra.md) | Specifies a YCbCr color value. |
| [D3D10_DDI_RASTERIZER_DESC structure](ns-d3d10umddi-d3d10-ddi-rasterizer-desc.md) | The D3D10_DDI_RASTERIZER_DESC structure describes a rasterizer state. |
| [D3DWDDM2_1DDI_VIDEO_INPUT structure](ns-d3d10umddi-d3dwddm2-1ddi-video-input.md) | TBD |
| [D3DWDDM2_2DDI_DEVICEFUNCS structure](ns-d3d10umddi-d3dwddm2-2ddi-devicefuncs~r1.md) | Specifies the callback functions that operate on a shader cache. |
| [D3DWDDM2_0DDI_SUBRESOURCE_PRESWIZZLE_OFFSETS structure](ns-d3d10umddi-d3dwddm2-0ddi-subresource-preswizzle-offsets.md) | TBD |
| [D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW structure](ns-d3d10umddi-d3d11-1ddiarg-createvideoprocessoroutputview.md) | Describes the video processor's output view. |
| [D3DWDDM2_0DDI_DEVICEFUNCS structure](ns-d3d10umddi-d3dwddm2-0ddi-devicefuncs~r2.md) | This structure contains the user mode device function table for Windows Display Driver Model (WDDM) 2.0. |
| [D3D11_1_DDI_RASTERIZER_DESC structure](ns-d3d10umddi-d3d11-1-ddi-rasterizer-desc.md) | Describes a rasterizer state. Used by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [D3D11DDIARG_BUFFER_RENDERTARGETVIEW structure](ns-d3d10umddi-d3d11ddiarg-buffer-rendertargetview.md) | The D3D11DDIARG_BUFFER_RENDERTARGETVIEW structure describes a buffer that is used to create a render target view in a call to the CreateRenderTargetView function. |
| [D3D11_1DDI_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_INPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-restricted-shared-resource-process-input.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_INPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS. |
| [D3DWDDM2_0DDI_RASTERIZER_DESC structure](ns-d3d10umddi-d3dwddm2-0ddi-rasterizer-desc.md) | TBD |
| [D3D11_1DDI_ARCHITECTURE_INFO_DATA structure](ns-d3d10umddi-d3d11-1ddi-architecture-info-data.md) | Describes information about display adapter architecture. |
| [D3D11_1DDI_AUTHENTICATED_CONFIGURE_OUTPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-configure-output.md) | Contains output data for the ConfigureAuthenticatedChannel(D3D11_1) function. |
| [D3D11_1DDI_VIDEO_DECODERR_BUFFER_DESC structure](ns-d3d10umddi-d3d11-1ddi-video-decoderr-buffer-desc.md) | Describes a compressed buffer for Microsoft DirectX Video Acceleration (DXVA) decoding. |
| [D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-output.md) | Contains a response from the QueryAuthenticatedChannel(D3D11_1) function. |
| [D3D10DDIARG_SIGNATURE_ENTRY structure](ns-d3d10umddi-d3d10ddiarg-signature-entry.md) | The D3D10DDIARG_SIGNATURE_ENTRY structure describes an entry for a signature. |
| [D3DWDDM2_0DDI_SUBRESOURCE_LAYOUT structure](ns-d3d10umddi-d3dwddm2-0ddi-subresource-layout.md) | TBD |
| [D3D10_DDI_QUERY_DATA_SO_STATISTICS structure](ns-d3d10umddi-d3d10-ddi-query-data-so-statistics.md) | The D3D10_DDI_QUERY_DATA_SO_STATISTICS structure describes stream output statistics that is used in a call to the CreateQuery(D3D10) function to create a D3D10DDI_QUERY_STREAMOUTPUTSTATS query type and in a call to the QueryGetData function to return information about the query. |
| [D3D11_1DDI_VIDEO_PROCESSOR_FILTER_RANGE structure](ns-d3d10umddi-d3d11-1ddi-video-processor-filter-range.md) | Defines the range of supported values for an image filter. |
| [D3D10DDIARG_BUFFER_SHADERRESOURCEVIEW structure](ns-d3d10umddi-d3d10ddiarg-buffer-shaderresourceview.md) | The D3D10DDIARG_BUFFER_SHADERRESOURCEVIEW structure describes a buffer that is used to create a shader resource view in a call to the CreateShaderResourceView function. |
| [D3D11DDIARG_CREATEDEFERREDCONTEXT structure](ns-d3d10umddi-d3d11ddiarg-createdeferredcontext.md) | The D3D11DDIARG_CREATEDEFERREDCONTEXT structure describes the deferred context to create. |
| [D3D10DDIARG_TEX3D_SHADERRESOURCEVIEW structure](ns-d3d10umddi-d3d10ddiarg-tex3d-shaderresourceview.md) | The D3D10DDIARG_TEX3D_SHADERRESOURCEVIEW structure describes a three-dimensional (3-D) texture that is used to create a shader resource view in a call to the CreateShaderResourceView function. |
| [D3D10_DDI_RENDER_TARGET_BLEND_DESC1 structure](ns-d3d10umddi-d3d10-ddi-render-target-blend-desc1.md) | The D3D10_DDI_RENDER_TARGET_BLEND_DESC1 structure describes a blend state for a render target. |
| [D3D11_1DDI_AUTHENTICATED_CONFIGURE_INITIALIZE structure](ns-d3d10umddi-d3d11-1ddi-authenticated-configure-initialize.md) | Contains input data for a call to the ConfigureAuthenticatedChannel(D3D11_1) function when D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT.ConfigureType has a GUID value of D3D11_AUTHENTICATED_CONFIGURE_INITIALIZE. |
| [D3D11_1DDI_AUTHENTICATED_CONFIGURE_CRYPTO_SESSION structure](ns-d3d10umddi-d3d11-1ddi-authenticated-configure-crypto-session.md) | Contains input data for a call to the ConfigureAuthenticatedChannel(D3D11_1) function when D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT.ConfigureType has a GUID value of D3D11_1DDI_AUTHENTICATED_CONFIGURE_CRYPTO_SESSION. |
| [D3D10_1DDIARG_CREATESHADERRESOURCEVIEW structure](ns-d3d10umddi-d3d10-1ddiarg-createshaderresourceview.md) | The D3D10_1DDIARG_CREATESHADERRESOURCEVIEW structure describes the shader resource view to create. |
| [D3D10_DDIARG_SUBRESOURCE_UP structure](ns-d3d10umddi-d3d10-ddiarg-subresource-up.md) | The D3D10_DDIARG_SUBRESOURCE_UP structure describes initialization information about a subresource. |
| [D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW structure](ns-d3d10umddi-d3d11ddiarg-bufferex-shaderresourceview.md) | The D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW structure describes a buffer that is used to create a shader resource view in a call to the CreateShaderResourceView(D3D11) function. |
| [D3DWDDM2_2DDI_SHADERCACHE_HASH structure](ns-d3d10umddi-d3dwddm2-2ddi-shadercache-hash.md) | Contains a hash value for a shader cache. |
| [D3DWDDM1_3DDI_TILE_REGION_SIZE structure](ns-d3d10umddi-d3dwddm1-3ddi-tile-region-size.md) | Specifies a tiled region. |
| [D3D11_1DDIARG_VIDEODECODERBEGINFRAME structure](ns-d3d10umddi-d3d11-1ddiarg-videodecoderbeginframe.md) | Specifies a content key in a call to the VideoDecoderBeginFrame function. |
| [D3D11_1DDI_AUTHENTICATED_QUERY_CURRENT_ACCESSIBILITY_ENCRYPTION_OUTPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-current-accessibility-encryption-output.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_CURRENT_ENCRYPTION_WHEN_ACCESSIBLE. |
| [D3D11DDIARG_CREATERESOURCE structure](ns-d3d10umddi-d3d11ddiarg-createresource.md) | Describes a resource to create. |
| [D3D10DDIARG_TEXCUBE_RENDERTARGETVIEW structure](ns-d3d10umddi-d3d10ddiarg-texcube-rendertargetview.md) | The D3D10DDIARG_TEXCUBE_RENDERTARGETVIEW structure describes a cube texture that is used to create a render target view in a call to the CreateRenderTargetView function. |
| [D3D10DDIARG_TEX1D_SHADERRESOURCEVIEW structure](ns-d3d10umddi-d3d10ddiarg-tex1d-shaderresourceview.md) | The D3D10DDIARG_TEX1D_SHADERRESOURCEVIEW structure describes a one-dimensional (1-D) texture that is used to create a shader resource view in a call to the CreateShaderResourceView function. |
| [D3D11_1DDI_VIDEO_CONTENT_PROTECTION_CAPS structure](ns-d3d10umddi-d3d11-1ddi-video-content-protection-caps.md) | Describes the content-protection capabilities of the user-mode display driver. |
| [D3D11_1DDIARG_SIGNATURE_ENTRY structure](ns-d3d10umddi-d3d11-1ddiarg-signature-entry.md) | Describes an entry for a signature. |
| [D3D11_1DDI_VIDEO_PROCESSOR_CUSTOM_RATE structure](ns-d3d10umddi-d3d11-1ddi-video-processor-custom-rate.md) | Specifies a custom rate for frame-rate conversion or inverse telecine (IVTC). |
| [D3DWDDM2_0DDI_MEMORY_ARCHITECTURE_CAPS structure](ns-d3d10umddi-d3dwddm2-0ddi-memory-architecture-caps.md) | TBD |
| [D3DWDDM2_0DDI_DEVICEFUNCS structure](ns-d3d10umddi-d3dwddm2-0ddi-devicefuncs~r3.md) | This structure contains the user mode device function table for Windows Display Driver Model (WDDM) 2.0. |
| [D3DWDDM2_1DDI_VIDEODEVICEFUNCS structure](ns-d3d10umddi-d3dwddm2-1ddi-videodevicefuncs.md) | TBD |
| [D3DWDDM2_0DDI_D3D11_OPTIONS2_DATA_LEGACY_ASTC structure](ns-d3d10umddi-d3dwddm2-0ddi-d3d11-options2-data-legacy-astc.md) | TBD |
| [D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_OUTPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-accessibility-encryption-guid-output.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_CONFIGURE_ENCRYPTION_WHEN_ACCESSIBLE_GUID. |
| [D3DWDDM2_0DDI_VIDEO_DECODER_BUFFER_DESC1 structure](ns-d3d10umddi-d3dwddm2-0ddi-video-decoder-buffer-desc1.md) | D3DWDDM2_0DDI_VIDEO_DECODER_BUFFER_DESC1 is used with VideoDecoderSubmitBuffers1 to submit one or more buffer for decoding. |
| [D3DWDDM2_0DDI_TEXTURE_LAYOUT_CAPS structure](ns-d3d10umddi-d3dwddm2-0ddi-texture-layout-caps.md) | TBD |
| [D3DWDDM2_1DDI_VIDEO_OUTPUT structure](ns-d3d10umddi-d3dwddm2-1ddi-video-output.md) | TBD |
| [D3D11_1DDI_AUTHENTICATED_QUERY_CRYPTO_SESSION_OUTPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-crypto-session-output.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_QUERY_CRYPTO_SESSION. |
| [D3D11DDIARG_CALCPRIVATEDEFERREDCONTEXTSIZE structure](ns-d3d10umddi-d3d11ddiarg-calcprivatedeferredcontextsize.md) | The D3D11DDIARG_CALCPRIVATEDEFERREDCONTEXTSIZE structure describes the parameters that the user-mode display driver uses to calculate the size of a memory block that the driver requires to store frequently-accessed data. |
| [D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS structure](ns-d3d10umddi-d3d10-ddi-query-data-pipeline-statistics.md) | The D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS structure describes statistics for each stage of the graphics pipeline that is used in a call to the CreateQuery(D3D10) function to create a D3D10DDI_QUERY_PIPELINESTATS query type and in a call to the QueryGetData function to return information about the query. |
| [D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_INPUT_DATA structure](ns-d3d10umddi-d3dwddm2-0ddi-key-exchange-hw-protection-input-data.md) | D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_INPUT_DATA is used with D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_DATA in the implementation of Digital Rights Management (DRM). |
| [D3DWDDM2_0DDI_SWIZZLE_BIT_ENTRY structure](ns-d3d10umddi-d3dwddm2-0ddi-swizzle-bit-entry.md) | TBD |
| [D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_INPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-accessibility-encryption-guid-input.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_INPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_CONFIGURE_ENCRYPTION_WHEN_ACCESSIBLE_GUID. |
| [D3DWDDM2_0DDI_CHECK_VIDEO_PROCESSOR_FORMAT_CONVERSION structure](ns-d3d10umddi-d3dwddm2-0ddi-check-video-processor-format-conversion.md) | D3DWDDM2_0DDI_CHECK_VIDEO_PROCESSOR_FORMAT_CONVERSION is used with CheckVideoProcessorFormatConversion to indicate whether the driver supports a specific format/color space conversion combination. |
| [D3D11DDIARG_CREATEDEPTHSTENCILVIEW structure](ns-d3d10umddi-d3d11ddiarg-createdepthstencilview.md) | The D3D11DDIARG_CREATEDEPTHSTENCILVIEW structure describes the depth-stencil view to create. |
| [D3DWDDM2_0DDIARG_CREATERENDERTARGETVIEW structure](ns-d3d10umddi-d3dwddm2-0ddiarg-createrendertargetview.md) | TBD |
| [D3D11DDIARG_TEX2D_UNORDEREDACCESSVIEW structure](ns-d3d10umddi-d3d11ddiarg-tex2d-unorderedaccessview.md) | The D3D11DDIARG_TEX2D_UNORDEREDACCESSVIEW structure describes a two-dimensional texture (2-D) that is used to create an unordered access view in a call to the CreateUnorderedAccessView function. |
| [D3D10DDIARG_TEX1D_RENDERTARGETVIEW structure](ns-d3d10umddi-d3d10ddiarg-tex1d-rendertargetview.md) | The D3D10DDIARG_TEX1D_RENDERTARGETVIEW structure describes a one-dimensional (1-D) texture that is used to create a render target view in a call to the CreateRenderTargetView function. |
| [D3D10_1DDI_DEVICEFUNCS structure](ns-d3d10umddi-d3d10-1ddi-devicefuncs.md) | TBD |
| [D3D11_1DDIARG_TESSELLATION_IO_SIGNATURES structure](ns-d3d10umddi-d3d11-1ddiarg-tessellation-io-signatures.md) | Describes a tessellation I/O signature. |
| [D3DWDDM2_0DDICB_CREATECONTEXT structure](ns-d3d10umddi-d3dwddm2-0ddicb-createcontext.md) | TBD |
| [D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_COUNT_OUTPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-accessibility-encryption-guid-count-output.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_QUERY_ENCRYPTION_WHEN_ACCESSIBLE_GUID_COUNT. |
| [D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT_ID_OUTPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-output-id-output.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT_ID. |
| [D3D10DDIARG_CREATERESOURCE structure](ns-d3d10umddi-d3d10ddiarg-createresource.md) | Describes a resource to create. |
| [D3D11_DDI_QUERY_DATA_PIPELINE_STATISTICS structure](ns-d3d10umddi-d3d11-ddi-query-data-pipeline-statistics.md) | The D3D11_DDI_QUERY_DATA_PIPELINE_STATISTICS structure describes statistics for each stage of the graphics pipeline that is used in a call to the CreateQuery(D3D10) function to create a D3D10DDI_QUERY_PIPELINESTATS query type and in a call to the QueryGetData function to return information about the query. |
| [D3DWDDM2_0DDI_VIDEO_PROCESSOR_STREAM_BEHAVIOR_HINT structure](ns-d3d10umddi-d3dwddm2-0ddi-video-processor-stream-behavior-hint.md) | D3DWDDM2_0DDI_VIDEO_PROCESSOR_STREAM_BEHAVIOR_HINT is used to describe behavior hints for the stream. |
| [D3D11_1_DDI_RENDER_TARGET_BLEND_DESC structure](ns-d3d10umddi-d3d11-1-ddi-render-target-blend-desc.md) | Describes a blend state for a render target. Used by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [D3D11DDI_3DPIPELINESUPPORT_CAPS structure](ns-d3d10umddi-d3d11ddi-3dpipelinesupport-caps.md) | The D3D11DDI_3DPIPELINESUPPORT_CAPS structure contains display device pipeline capabilities. |
| [D3D11DDIARG_CREATECOMMANDLIST structure](ns-d3d10umddi-d3d11ddiarg-createcommandlist.md) | The D3D11DDIARG_CREATECOMMANDLIST structure contains a handle to the deferred context that was created by the CreateDeferredContext function. |
| [D3D11DDIARG_STREAM_OUTPUT_DECLARATION_ENTRY structure](ns-d3d10umddi-d3d11ddiarg-stream-output-declaration-entry.md) | The D3D11DDIARG_STREAM_OUTPUT_DECLARATION_ENTRY structure describes a portion of the stream output for a geometry shader. |
| [D3D11_1DDI_OMAC structure](ns-d3d10umddi-d3d11-1ddi-omac.md) | Contains a Message Authentication Code (MAC). |
| [D3D10_DDI_BOX structure](ns-d3d10umddi-d3d10-ddi-box.md) | The D3D10_DDI_BOX structure describes a volume. |
| [D3D10DDI_VERTEX_CACHE_DESC structure](ns-d3d10umddi-d3d10ddi-vertex-cache-desc.md) | The D3D10DDI_VERTEX_CACHE_DESC structure describes mesh-optimization data. |
| [D3D11_1DDI_AUTHENTICATED_QUERY_INPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-input.md) | Contains input data for the QueryAuthenticatedChannel(D3D11_1) function. |
| [D3D11_1DDIARG_CREATEVIDEOPROCESSOR structure](ns-d3d10umddi-d3d11-1ddiarg-createvideoprocessor.md) | Specifies the attributes of a video processor object. |
| [D3D10_DDI_DEPTH_STENCIL_DESC structure](ns-d3d10umddi-d3d10-ddi-depth-stencil-desc.md) | The D3D10_DDI_DEPTH_STENCIL_DESC structure describes a depth stencil state. |
| [D3D10DDI_DEVICEFUNCS structure](ns-d3d10umddi-d3d10ddi-devicefuncs~r1.md) | The D3D10DDI_DEVICEFUNCS structure contains functions that the user-mode display driver can implement to render graphics primitives and process state changes. |
| [D3D11_1DDI_AUTHENTICATED_QUERY_PROTECTION_OUTPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-protection-output.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_QUERY_PROTECTION. |
| [D3DWDDM2_0DDICB_CREATECONTEXTVIRTUAL structure](ns-d3d10umddi-d3dwddm2-0ddicb-createcontextvirtual.md) | TBD |
| [D3DWDDM2_0DDI_VIDEO_DECODER_BEGIN_FRAME_CRYPTO_SESSION structure](ns-d3d10umddi-d3dwddm2-0ddi-video-decoder-begin-frame-crypto-session.md) | D3DWDDM2_0DDI_VIDEO_DECODER_BEGIN_FRAME_CRYPTO_SESSION describes the beginning frame of a cryptographic session object. |
| [D3DWDDM2_2DDI_SHADERCACHE_DATA structure](ns-d3d10umddi-d3dwddm2-2ddi-shadercache-data.md) | TBD |
| [D3D10DDIARG_OPENRESOURCE structure](ns-d3d10umddi-d3d10ddiarg-openresource.md) | The D3D10DDIARG_OPENRESOURCE structure contains information for opening a shared resource. |
| [D3D11_1DDI_DEVICEFUNCS structure](ns-d3d10umddi-d3d11-1ddi-devicefuncs~r1.md) | Contains functions that a user-mode display driver that is optimized for the Microsoft Direct3D version 11.1 runtime can implement to render graphics primitives and process state changes. |
| [D3D11_1DDI_AUTHENTICATED_QUERY_DEVICE_HANDLE_OUTPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-device-handle-output.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_QUERY_DEVICE_HANDLE. |
| [D3D11_1DDIARG_CREATEVIDEOPROCESSORENUM structure](ns-d3d10umddi-d3d11-1ddiarg-createvideoprocessorenum.md) | Specifies the attributes of a video processor enumeration object. |
| [D3D10DDIARG_CREATEDEVICE structure](ns-d3d10umddi-d3d10ddiarg-createdevice.md) | The D3D10DDIARG_CREATEDEVICE structure describes the display device to create. |
| [D3D11_1DDI_VIDEO_COLOR_RGBA structure](ns-d3d10umddi-d3d11-1ddi-video-color-rgba.md) | Specifies an RGB color value. |
| [D3D11_1DDIARG_CREATEAUTHENTICATEDCHANNEL structure](ns-d3d10umddi-d3d11-1ddiarg-createauthenticatedchannel.md) | Specifies the attributes of the authenticated channel to be created by the user-mode driver's CreateAuthenticatedChannel(D3D11_1) function. |
| [D3D11DDIARG_TEX1D_UNORDEREDACCESSVIEW structure](ns-d3d10umddi-d3d11ddiarg-tex1d-unorderedaccessview.md) | The D3D11DDIARG_TEX1D_UNORDEREDACCESSVIEW structure describes a one-dimensional texture (1-D) that is used to create an unordered access view in a call to the CreateUnorderedAccessView function. |
| [D3D10_DDI_DEPTH_STENCILOP_DESC structure](ns-d3d10umddi-d3d10-ddi-depth-stencilop-desc.md) | The D3D10_DDI_DEPTH_STENCILOP_DESC structure describes a depth stencil operation. |
| [D3D11DDIARG_CREATESHADERRESOURCEVIEW structure](ns-d3d10umddi-d3d11ddiarg-createshaderresourceview.md) | The D3D11DDIARG_CREATESHADERRESOURCEVIEW structure describes the shader resource view to create. |
| [D3D11_1_DDI_BLEND_DESC structure](ns-d3d10umddi-d3d11-1-ddi-blend-desc.md) | Describes a blend state. Used by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [D3DWDDM2_0DDI_TEXTURE_LAYOUT_SET_CAPS structure](ns-d3d10umddi-d3dwddm2-0ddi-texture-layout-set-caps.md) | TBD |
| [D3D11_1DDI_AES_CTR_IV structure](ns-d3d10umddi-d3d11-1ddi-aes-ctr-iv.md) | Contains an initialization vector (IV) for 128-bit Advanced Encryption Standard CTR mode (AES-CTR) block cipher encryption. |
| [D3D10DDIARG_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT structure](ns-d3d10umddi-d3d10ddiarg-creategeometryshaderwithstreamoutput.md) | The D3D10DDIARG_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT structure describes the geometry shader with stream output to create. |
| [D3D10DDIARG_TEX3D_RENDERTARGETVIEW structure](ns-d3d10umddi-d3d10ddiarg-tex3d-rendertargetview.md) | The D3D10DDIARG_TEX3D_RENDERTARGETVIEW structure describes a three-dimensional (3-D) texture that is used to create a render target view in a call to the CreateRenderTargetView function. |
| [D3D10DDIARG_TEX2D_SHADERRESOURCEVIEW structure](ns-d3d10umddi-d3d10ddiarg-tex2d-shaderresourceview.md) | The D3D10DDIARG_TEX2D_SHADERRESOURCEVIEW structure describes a two-dimensional (2-D) texture that is used to create a shader resource view in a call to the CreateShaderResourceView function. |
| [D3D11_1DDI_VIDEODEVICEFUNCS structure](ns-d3d10umddi-d3d11-1ddi-videodevicefuncs.md) | Specifies the video function table for the Microsoft Direct3D driver device object. |
| [D3D10DDIARG_STREAM_OUTPUT_DECLARATION_ENTRY structure](ns-d3d10umddi-d3d10ddiarg-stream-output-declaration-entry.md) | The D3D10DDIARG_STREAM_OUTPUT_DECLARATION_ENTRY structure describes a portion of the stream output for a geometry shader. |
| [D3D11_1DDI_VIDEO_COLOR structure](ns-d3d10umddi-d3d11-1ddi-video-color.md) | Defines a color value for Microsoft Direct3D 11 video. |
| [D3D11_1DDIARG_STAGE_IO_SIGNATURES structure](ns-d3d10umddi-d3d11-1ddiarg-stage-io-signatures.md) | Describes an I/O signature. |
| [D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT_ID_INPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-output-id-input.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_INPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT_ID. |
| [D3D11_1DDI_VIDEO_DECODER_CONFIG structure](ns-d3d10umddi-d3d11-1ddi-video-decoder-config.md) | Describes the configuration of a Microsoft Direct3D 11 decoder device for Microsoft DirectX Video Acceleration (DXVA). |
| [D3D11_1DDI_AUTHENTICATED_QUERY_CHANNEL_TYPE_OUTPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-channel-type-output.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_QUERY_CHANNEL_TYPE. |
| [D3DWDDM2_1DDI_DEVICEFUNCS structure](ns-d3d10umddi-d3dwddm2-1ddi-devicefuncs~r1.md) | TBD |
| [D3D10DDI_COUNTER_INFO structure](ns-d3d10umddi-d3d10ddi-counter-info.md) | The D3D10DDI_COUNTER_INFO structure describes information to manipulate counters. |
| [D3D11_1DDI_AUTHENTICATED_CONFIGURE_ACCESSIBLE_ENCRYPTION structure](ns-d3d10umddi-d3d11-1ddi-authenticated-configure-accessible-encryption.md) | Contains input data for a call to the ConfigureAuthenticatedChannel(D3D11_1) function when D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT.ConfigureType has a GUID value of D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE. |
| [D3D11_1DDI_VIDEO_PROCESSOR_COLOR_SPACE structure](ns-d3d10umddi-d3d11-1ddi-video-processor-color-space.md) | Specifies the color space for video processing. |
| [D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLE_OUTPUT_FORMAT structure](ns-d3d10umddi-d3dwddm2-0ddi-video-capability-decoder-downsample-output-format.md) | TBD |
| [D3DWDDM2_0DDIARG_CREATESHADERRESOURCEVIEW structure](ns-d3d10umddi-d3dwddm2-0ddiarg-createshaderresourceview.md) | TBD |
| [D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW structure](ns-d3d10umddi-d3d10-1ddiarg-texcube-shaderresourceview.md) | The D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW structure describes cube textures that are used to create a shader resource view in a call to the CreateShaderResourceView(D3D10_1) function. |
| [D3D10_2DDI_ADAPTERFUNCS structure](ns-d3d10umddi-d3d10-2ddi-adapterfuncs.md) | The D3D10_2DDI_ADAPTERFUNCS structure contains functions that the user-mode display driver can implement to communicate with a graphics adapter object. |
| [D3D10DDIARG_CREATESHADERRESOURCEVIEW structure](ns-d3d10umddi-d3d10ddiarg-createshaderresourceview.md) | The D3D10DDIARG_CREATESHADERRESOURCEVIEW structure describes the shader resource view to create. |
| [D3D10DDIARG_TEX2D_RENDERTARGETVIEW structure](ns-d3d10umddi-d3d10ddiarg-tex2d-rendertargetview.md) | The D3D10DDIARG_TEX2D_RENDERTARGETVIEW structure describes a two-dimensional (2-D) texture that is used to create a render target view in a call to the CreateRenderTargetView function. |
| [D3DWDDM2_0DDI_D3D11_OPTIONS3_DATA structure](ns-d3d10umddi-d3dwddm2-0ddi-d3d11-options3-data.md) | TBD |
| [D3DWDDM2_0DDI_SWIZZLE_PATTERN structure](ns-d3d10umddi-d3dwddm2-0ddi-swizzle-pattern.md) | TBD |
| [D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW structure](ns-d3d10umddi-d3d11ddiarg-tex3d-unorderedaccessview.md) | The D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW structure describes a three-dimensional (3-D) texture that is used to create an unordered access view in a call to the CreateUnorderedAccessView function. |
| [D3D10_DDI_SAMPLER_DESC structure](ns-d3d10umddi-d3d10-ddi-sampler-desc.md) | The D3D10_DDI_SAMPLER_DESC structure describes a sampler. |
| [D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS structure](ns-d3d10umddi-d3dwddm2-0ddi-corelayer-devicecallbacks~r1.md) | This structure contains the function table for the core layer device callback functions. |
| [D3D10DDIARG_BUFFER_RENDERTARGETVIEW structure](ns-d3d10umddi-d3d10ddiarg-buffer-rendertargetview.md) | The D3D10DDIARG_BUFFER_RENDERTARGETVIEW structure describes a buffer that is used to create a render target view in a call to the CreateRenderTargetView function. |
| [D3D11_1DDI_GETCAPTUREHANDLEDATA structure](ns-d3d10umddi--d3d11-1ddi-getcapturehandledata.md) | Defines a resource allocation in a call to the GetCaptureHandle function. |
| [D3D11DDIARG_TESSELLATION_IO_SIGNATURES structure](ns-d3d10umddi-d3d11ddiarg-tessellation-io-signatures.md) | The D3D11DDIARG_TESSELLATION_IO_SIGNATURES structure describes a tessellation I/O signature. |
| [D3D10DDIARG_TEX1D_DEPTHSTENCILVIEW structure](ns-d3d10umddi-d3d10ddiarg-tex1d-depthstencilview.md) | The D3D10DDIARG_TEX1D_DEPTHSTENCILVIEW structure describes a one-dimensional texture (1-D) that is used to create a depth stencil view in a call to the CreateDepthStencilView function. |
| [D3D11_1DDI_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_OUTPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-restricted-shared-resource-process-output.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS. |
| [D3D11_1DDI_VIDEO_OUTPUT structure](ns-d3d10umddi-d3d11-1ddi-video-output.md) | Reserved for system use. Do not use in your driver. |
| [D3DWDDM2_0DDI_VIDEO_CAPABILITY_RECOMMEND_DECODER_DOWNSAMPLING structure](ns-d3d10umddi-d3dwddm2-0ddi-video-capability-recommend-decoder-downsampling.md) | D3DWDDM2_0DDI_VIDEO_CAPABILITY_RECOMMEND_DECODER_DOWNSAMPLING is used by the user-mode driver to recommend downsampling parameters that can be used to decode the stream in real-time. |
| [D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE structure](ns-d3d10umddi-d3d11-1ddi-authenticated-configure-shared-resource.md) | Contains input data for a call to the ConfigureAuthenticatedChannel(D3D11_1) function when D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT.ConfigureType has a GUID value of D3D11_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE. |
| [D3D11_1DDI_VIDEO_PROCESSOR_STREAM structure](ns-d3d10umddi-d3d11-1ddi-video-processor-stream.md) | Contains stream-level data for the VideoProcessorBlt function. |
| [D3D11_1DDI_AUTHENTICATED_QUERY_CRYPTO_SESSION_INPUT structure](ns-d3d10umddi-d3d11-1ddi-authenticated-query-crypto-session-input.md) | Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_INPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_QUERY_CRYPTO_SESSION. |
| [D3DWDDM2_0DDI_LEGACY_SWIZZLE_PATTERN_DESC structure](ns-d3d10umddi-d3dwddm2-0ddi-legacy-swizzle-pattern-desc.md) | TBD |
| [D3DWDDM2_0DDIARG_TEX2D_SHADERRESOURCEVIEW structure](ns-d3d10umddi-d3dwddm2-0ddiarg-tex2d-shaderresourceview.md) | TBD |
| [D3D11_1DDI_CERTIFICATE_INFO structure](ns-d3d10umddi-d3d11-1ddi-certificate-info.md) | Specifies a cryptographic session certificate or authenticated channel. |
| [D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW structure](ns-d3d10umddi-d3d11-1ddiarg-createvideoprocessorinputview.md) | Describes the video processor's input view. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [D3D10_DDI_FILL_MODE enumeration](ne-d3d10umddi-d3d10-ddi-fill-mode.md) | TBD |
| [D3D10_DDI_INTERPOLATION_MODE enumeration](ne-d3d10umddi-d3d10-ddi-interpolation-mode.md) | TBD |
| [D3D10_DDI_GET_DATA_FLAG enumeration](ne-d3d10umddi-d3d10-ddi-get-data-flag.md) | TBD |
| [D3D11_1DDI_CONTENT_PROTECTION_CAPS enumeration](ne-d3d10umddi-d3d11-1ddi-content-protection-caps.md) | Describes content-protection capabilities. |
| [D3D11_1DDI_VIDEO_FRAME_FORMAT enumeration](ne-d3d10umddi-d3d11-1ddi-video-frame-format.md) | Describes how a video stream is interlaced. |
| [D3D10_DDI_BLEND enumeration](ne-d3d10umddi-d3d10-ddi-blend.md) | The D3D10_DDI_BLEND enumeration type contains values that identify blend modes in a call to the driver's CreateBlendState function. |
| [D3D10DDI_QUERY enumeration](ne-d3d10umddi-d3d10ddi-query.md) | The D3D10DDI_QUERY enumeration type contains values that identify a query type. |
| [D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FORMAT enumeration](ne-d3d10umddi-d3d11-1ddi-video-processor-stereo-format.md) | Specifies the layout in memory of a stereo 3-D video frame. |
| [D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE enumeration](ne-d3d10umddi-d3d11-1ddi-video-processor-output-rate.md) | Specifies the rate at which the video processor produces output frames from an input stream. |
| [D3D11_1DDI_VIDEO_PROCESSOR_CONVERSION_CAPS enumeration](ne-d3d10umddi-d3d11-1ddi-video-processor-conversion-caps.md) | Specifies video processor-specific capabilities. |
| [D3D10_2DDICAPS_TYPE enumeration](ne-d3d10umddi-d3d10-2ddicaps-type.md) | The D3D10_2DDICAPS_TYPE enumeration type contains values that identify the type of capability information that is retrieved from a call to the driver's GetCaps(D3D10_2) function. |
| [D3D11_1_DDI_LOGIC_OP enumeration](ne-d3d10umddi-d3d11-1-ddi-logic-op.md) | Indicates shader logic operations used in a blend state. |
| [D3D10_DDI_PRIMITIVE_TOPOLOGY enumeration](ne-d3d10umddi-d3d10-ddi-primitive-topology.md) | The D3D10_DDI_PRIMITIVE_TOPOLOGY enumeration type contains values that identify primitive topologies in a call to the driver's IaSetTopology function. |
| [D3DWDDM2_0DDI_CONTEXTTYPE_FLAG enumeration](ne-d3d10umddi-d3dwddm2-0ddi-contexttype-flag.md) | D3DWDDM2_0DDI_CONTEXTTYPE_FLAG describes the type of context being created for interacting with JPEG hardware. |
| [D3DWDDM2_0DDI_SWIZZLE_PATTERN enumeration](ne-d3d10umddi-d3dwddm2-0ddi-swizzle-pattern~r1.md) | TBD |
| [D3DWDDM1_3DDI_CHECK_MULTISAMPLE_QUALITY_LEVELS_FLAG enumeration](ne-d3d10umddi-d3dwddm1-3ddi-check-multisample-quality-levels-flag.md) | Identifies how to check multisample quality levels using the CheckMultisampleQualityLevels(D3D11_2) function. |
| [D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG enumeration](ne-d3d10umddi-d3d11-ddi-createdepthstencilview-flag.md) | The D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG enumeration type contains values that identify the type of depth-stencil view to create through a call to the driver's CreateDepthStencilView(D3D11) function. |
| [D3D10_DDI_INPUT_CLASSIFICATION enumeration](ne-d3d10umddi-d3d10-ddi-input-classification.md) | TBD |
| [D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE enumeration](ne-d3d10umddi-d3d11-1ddi-video-processor-alpha-fill-mode.md) | Specifies the alpha fill mode for video processing. |
| [D3D10_DDI_CPU_ACCESS enumeration](ne-d3d10umddi-d3d10-ddi-cpu-access.md) | TBD |
| [D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE enumeration](ne-d3d10umddi-d3d11-1ddi-video-processor-stereo-flip-mode.md) | For stereo 3-D video, specifies whether the data in frame 0 or frame 1 is flipped, either horizontally or vertically. |
| [D3DWDDM2_0DDI_TEXTURE_LAYOUT enumeration](ne-d3d10umddi-d3dwddm2-0ddi-texture-layout.md) | TBD |
| [D3D11_1DDI_CERTIFICATE_TYPE enumeration](ne-d3d10umddi-d3d11-1ddi-certificate-type.md) | Specifies the type of authenticated certificate that is used to establish trust and perform a key exchange. |
| [D3DWDDM1_3DDI_TILE_RANGE_FLAG enumeration](ne-d3d10umddi-d3dwddm1-3ddi-tile-range-flag.md) | Specifies a range of tile mappings to use with the UpdateTileMappings function. |
| [D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY enumeration](ne-d3d10umddi-d3dwddm2-0ddi-video-capability-query.md) | Describes the video capabilities to query. |
| [D3D10DDI_COUNTER_TYPE enumeration](ne-d3d10umddi-d3d10ddi-counter-type.md) | TBD |
| [D3D11_1DDI_VIDEO_PROCESSOR_DEVICE_CAPS enumeration](ne-d3d10umddi-d3d11-1ddi-video-processor-device-caps.md) | Defines video processing capabilities for a Microsoft Direct3D 11 video processor. |
| [D3D11_1DDI_VIDEO_USAGE enumeration](ne-d3d10umddi-d3d11-1ddi-video-usage.md) | Identifies how the decode device plays video. |
| [D3D10_DDI_FILTER enumeration](ne-d3d10umddi-d3d10-ddi-filter.md) | The D3D10_DDI_FILTER enumeration type contains values that identify filter properties of a sampler in a call to the driver's CreateSampler function. |
| [D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS enumeration](ne-d3d10umddi-d3d11-1ddi-video-processor-format-caps.md) | Defines capabilities related to input formats for a Microsoft Direct3D 11 video processor. |
| [D3D11_1DDI_VIDEO_PROCESSOR_FILTER enumeration](ne-d3d10umddi-d3d11-1ddi-video-processor-filter.md) | Identifies a video processor filter. |
| [D3D10_DDI_COLOR_WRITE_ENABLE enumeration](ne-d3d10umddi-d3d10-ddi-color-write-enable.md) | TBD |
| [D3D10_DDI_FILTER_TYPE enumeration](ne-d3d10umddi-d3d10-ddi-filter-type.md) | TBD |
| [D3D10_DDI_COMPARISON_FUNC enumeration](ne-d3d10umddi-d3d10-ddi-comparison-func.md) | The D3D10_DDI_COMPARISON_FUNC enumeration type contains values that identify the comparison function to perform. |
| [D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS enumeration](ne-d3d10umddi-d3d11-1ddi-video-processor-stereo-caps.md) | Defines stereo 3-D capabilities for a Microsoft Direct3D 11 video processor. |
| [D3DWDDM2_0DDI_CONSERVATIVE_RASTERIZATION_TIER enumeration](ne-d3d10umddi-d3dwddm2-0ddi-conservative-rasterization-tier.md) | TBD |
| [D3DWDDM1_3DDI_FILTER_REDUCTION_TYPE enumeration](ne-d3d10umddi-d3dwddm1-3ddi-filter-reduction-type.md) | TBD |
| [D3D10_DDI_TEXTURECUBE_FACE enumeration](ne-d3d10umddi-d3d10-ddi-texturecube-face.md) | TBD |
| [D3D11DDI_HANDLETYPE enumeration](ne-d3d10umddi-d3d11ddi-handletype.md) | Contains values that identify handle types. |
| [D3DWDDM1_3DDI_TILE_COPY_FLAG enumeration](ne-d3d10umddi-d3dwddm1-3ddi-tile-copy-flag.md) | Identifies how to copy a tile using the CopyTiles function. |
| [D3D11_DDI_SHADER_MIN_PRECISION enumeration](ne-d3d10umddi-d3d11-ddi-shader-min-precision.md) | Specifies minimum precision levels that the user-mode driver supports in shaders. |
| [D3D10_DDI_PRIMITIVE enumeration](ne-d3d10umddi-d3d10-ddi-primitive.md) | TBD |
| [D3D10_DDI_MAP_FLAG enumeration](ne-d3d10umddi-d3d10-ddi-map-flag.md) | The D3D10_DDI_MAP_FLAG enumeration type contains flags that identify how to map to a subresource in a call to the driver's ResourceMap function. |
| [D3D10_DDI_BLEND_OP enumeration](ne-d3d10umddi-d3d10-ddi-blend-op.md) | The D3D10_DDI_BLEND_OP enumeration type contains values that identify blending operations in a call to the driver's CreateBlendState function. |
| [D3D10_DDI_TEXTURE_ADDRESS_MODE enumeration](ne-d3d10umddi-d3d10-ddi-texture-address-mode.md) | The D3D10_DDI_TEXTURE_ADDRESS_MODE enumeration type contains values that identify the texture address mode of a sampler. |
| [D3D10_DDI_RESOURCE_USAGE enumeration](ne-d3d10umddi-d3d10-ddi-resource-usage.md) | The D3D10_DDI_RESOURCE_USAGE enumeration type contains values that identify how a resource is used. |
| [D3D11_1_DDI_COPY_FLAGS enumeration](ne-d3d10umddi-d3d11-1-ddi-copy-flags.md) | Specifies how to handle the existing contents of a resource during a copy or update operation of a region within that resource. Used by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [D3D11_1_DDI_FLUSH_FLAGS enumeration](ne-d3d10umddi-d3d11-1-ddi-flush-flags.md) | In calls to the Flush(D3D11_1) function, indicates whether the driver should continue to submit command buffers. Used by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [D3D11_1DDI_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE enumeration](ne-d3d10umddi-d3d11-1ddi-authenticated-process-identifier-type.md) | Specifies the type of process that is identified in the D3D11_1DDI_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_OUTPUT structure. |
| [D3D11DDI_3DPIPELINELEVEL enumeration](ne-d3d10umddi-d3d11ddi-3dpipelinelevel.md) | The D3D11DDI_3DPIPELINELEVEL enumeration type contains values that identify the pipeline level that the driver supports, which is retrieved from a call to the driver's GetCaps(D3D10_2) function. |
| [D3D10_DDI_MAP enumeration](ne-d3d10umddi-d3d10-ddi-map.md) | The D3D10_DDI_MAP enumeration type contains values that identify the access levels to map to a subresource in a call to the driver's ResourceMap function. |
| [D3DWDDM1_3DDI_TILE_MAPPING_FLAG enumeration](ne-d3d10umddi-d3dwddm1-3ddi-tile-mapping-flag.md) | Indicates how to update a tile mapping. |
| [D3D11_1DDI_VIDEO_PROCESSOR_ITELECINE_CAPS enumeration](ne-d3d10umddi-d3d11-1ddi-video-processor-itelecine-caps.md) | Specifies the inverse telecine (IVTC) capabilities of a video processor. |
| [D3DWDDM2_0DDI_VIDEO_DECODER_CAPS enumeration](ne-d3d10umddi-d3dwddm2-0ddi-video-decoder-caps.md) | Describes the video decoder capabilities. |
| [D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS enumeration](ne-d3d10umddi-d3dwddm2-0ddi-swizzle-pattern-flags.md) | Contains swizzle pattern flag values. |
| [D3D11_1DDI_VIDEO_PROCESSOR_FILTER_CAPS enumeration](ne-d3d10umddi-d3d11-1ddi-video-processor-filter-caps.md) | Identifies video processor capabilities that the user-mode driver supports. |
| [D3D10_DDI_DEPTH_WRITE_MASK enumeration](ne-d3d10umddi-d3d10-ddi-depth-write-mask.md) | TBD |
| [D3D10_DDI_FRONT_WINDING enumeration](ne-d3d10umddi-d3d10-ddi-front-winding.md) | TBD |
| [D3D10_DDI_RESOURCE_MISC_FLAG enumeration](ne-d3d10umddi-d3d10-ddi-resource-misc-flag.md) | Identifies miscellaneous information about a resource. |
| [D3DWDDM1_3DDI_MARKER_TYPE enumeration](ne-d3d10umddi-d3dwddm1-3ddi-marker-type.md) | Indicates the type of marker that the user-mode display driver supports. |
| [D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_SUPPORT enumeration](ne-d3d10umddi-d3d11-1ddi-video-processor-format-support.md) | Specifies how a video format can be used for video processing. |
| [D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS enumeration](ne-d3d10umddi-d3dwddm2-0ddi-video-processor-behavior-hints.md) | Describes operations that the video processor can perform more efficiently than VideoProcessorBlt. |
| [D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS enumeration](ne-d3d10umddi-d3dwddm2-0ddi-crypto-session-status.md) | Provides status information for an existing CryptoSession object. |
| [D3D11_1DDI_BUS_TYPE enumeration](ne-d3d10umddi-d3d11-1ddi-bus-type.md) | Specifies the type of I/O bus that is used by the graphics adapter. |
| [D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE enumeration](ne-d3d10umddi-d3d11-1ddi-video-processor-nominal-range.md) | Indicates the luminance range of YUV data. |
| [D3D11_DDI_VIDEO_DECODER_BUFFER_TYPE enumeration](ne-d3d10umddi-d3d11-ddi-video-decoder-buffer-type.md) | Contains values that indicate the buffer type used by the video decoder. |
| [D3D10_DDI_RESOURCE_BIND_FLAG enumeration](ne-d3d10umddi-d3d10-ddi-resource-bind-flag.md) | Identifies how a resource is bound. |
| [D3D10DDI_SHADERUNITTYPE enumeration](ne-d3d10umddi-d3d10ddi-shaderunittype.md) | TBD |
| [D3D11_1DDI_VIDEO_PROCESSOR_ROTATION enumeration](ne-d3d10umddi-d3d11-1ddi-video-processor-rotation.md) | Specifies the clockwise rotation of the input stream of the video processor. |
| [D3D10_DDI_CLEAR_FLAG enumeration](ne-d3d10umddi-d3d10-ddi-clear-flag.md) | TBD |
| [D3D10_DDI_CULL_MODE enumeration](ne-d3d10umddi-d3d10-ddi-cull-mode.md) | TBD |
| [D3D11_1_DDI_CHECK_DIRECT_FLIP_FLAGS enumeration](ne-d3d10umddi-d3d11-1-ddi-check-direct-flip-flags.md) | Used by the CheckDirectFlipFlags parameter of the CheckDirectFlipSupport(D3D11_1) function to specify seamless flipping of video memory. |
| [D3D11_1DDI_AUTHENTICATED_CHANNEL_TYPE enumeration](ne-d3d10umddi-d3d11-1ddi-authenticated-channel-type.md) | Specifies the type of Microsoft Direct3D authenticated channel. |
| [D3DWDDM2_0DDI_CONSERVATIVE_RASTERIZATION_MODE enumeration](ne-d3d10umddi-d3dwddm2-0ddi-conservative-rasterization-mode.md) | TBD |
| [D3D10_1_DDIARG_STANDARD_MULTISAMPLE_QUALITY_LEVELS enumeration](ne-d3d10umddi-d3d10-1-ddiarg-standard-multisample-quality-levels.md) | The D3D10_1_DDIARG_STANDARD_MULTISAMPLE_QUALITY_LEVELS enumeration type contains values that identify quality levels for multisample patterns. |
| [D3D10_DDI_STENCIL_OP enumeration](ne-d3d10umddi-d3d10-ddi-stencil-op.md) | The D3D10_DDI_STENCIL_OP enumeration type contains values that identify operations on stencil buffers in a call to the driver's CreateDepthStencilState function. |
| [D3DWDDM1_3DDI_TILED_RESOURCES_SUPPORT_FLAG enumeration](ne-d3d10umddi-d3dwddm1-3ddi-tiled-resources-support-flag.md) | Indicates the level of support by the hardware and user-mode display driver for tiled resources. |
| [D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS enumeration](ne-d3d10umddi-d3d11-1ddi-video-processor-auto-stream-caps.md) | Specifies the automatic image processing capabilities of the video processor. |
| [D3D11_1DDI_VIDEO_PROCESSOR_FEATURE_CAPS enumeration](ne-d3d10umddi-d3d11-1ddi-video-processor-feature-caps.md) | Defines features that a Microsoft Direct3D 11 video processor can support. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [IS_DXGI1_4_BASE_FUNCTIONS function](nf-d3d10umddi-is-dxgi1-4-base-functions.md) | TBD |
| [D3DWDDM1_3DDI_DECODE_FILTER_REDUCTION function](nf-d3d10umddi-d3dwddm1-3ddi-decode-filter-reduction.md) | TBD |
| [D3D10_DDI_ENCODE_BASIC_FILTER function](nf-d3d10umddi-d3d10-ddi-encode-basic-filter.md) | TBD |
| [D3D10_DDI_DECODE_MIP_FILTER function](nf-d3d10umddi-d3d10-ddi-decode-mip-filter.md) | TBD |
| [D3D10DDI_HRT function](nf-d3d10umddi-d3d10ddi-hrt.md) | TBD |
| [D3D11DDI_ENCODE_3DPIPELINESUPPORT_CAP function](nf-d3d10umddi-d3d11ddi-encode-3dpipelinesupport-cap.md) | TBD |
| [D3D10_DDI_ENCODE_BASIC_FILTER function](nf-d3d10umddi-d3d10-ddi-encode-basic-filter~r1.md) | TBD |
| [D3D11DDI_HRT function](nf-d3d10umddi-d3d11ddi-hrt.md) | TBD |
| [D3D11DDI_H function](nf-d3d10umddi-d3d11ddi-h.md) | TBD |
| [D3D10_DDI_ENCODE_ANISOTROPIC_FILTER function](nf-d3d10umddi-d3d10-ddi-encode-anisotropic-filter~r1.md) | TBD |
| [IS_DXGI1_1_BASE_FUNCTIONS function](nf-d3d10umddi-is-dxgi1-1-base-functions.md) | TBD |
| [D3D10_DDI_DECODE_IS_ANISOTROPIC_FILTER function](nf-d3d10umddi-d3d10-ddi-decode-is-anisotropic-filter.md) | TBD |
| [D3D10_0_DDI_IS_LINKED_ADAPTER_QFE_PRESENT function](nf-d3d10umddi-d3d10-0-ddi-is-linked-adapter-qfe-present.md) | TBD |
| [D3D10_DDI_DECODE_IS_COMPARISON_FILTER function](nf-d3d10umddi-d3d10-ddi-decode-is-comparison-filter.md) | TBD |
| [D3D10_DDI_ENCODE_ANISOTROPIC_FILTER function](nf-d3d10umddi-d3d10-ddi-encode-anisotropic-filter.md) | TBD |
| [IS_DXGI1_6_1_BASE_FUNCTIONS function](nf-d3d10umddi-is-dxgi1-6-1-base-functions.md) | TBD |
| [D3D10_DDI_DECODE_IS_TEXT_1BIT_FILTER function](nf-d3d10umddi-d3d10-ddi-decode-is-text-1bit-filter.md) | TBD |
| [D3D10_DDI_DECODE_MAG_FILTER function](nf-d3d10umddi-d3d10-ddi-decode-mag-filter.md) | TBD |
| [D3D11DDI_EXTRACT_3DPIPELINELEVEL_FROM_FLAGS function](nf-d3d10umddi-d3d11ddi-extract-3dpipelinelevel-from-flags.md) | TBD |
| [IS_DXGI1_5_BASE_FUNCTIONS function](nf-d3d10umddi-is-dxgi1-5-base-functions.md) | TBD |
| [D3D10DDI_H function](nf-d3d10umddi-d3d10ddi-h.md) | TBD |
| [D3D10DDI_HKM function](nf-d3d10umddi-d3d10ddi-hkm.md) | TBD |
| [IS_D3D11_WIN7_INTERFACE_VERSION function](nf-d3d10umddi-is-d3d11-win7-interface-version.md) | TBD |
| [D3D10_1_DDI_IS_LINKED_ADAPTER_QFE_PRESENT function](nf-d3d10umddi-d3d10-1-ddi-is-linked-adapter-qfe-present.md) | TBD |
| [IS_DXGI1_6_BASE_FUNCTIONS function](nf-d3d10umddi-is-dxgi1-6-base-functions.md) | TBD |
| [IS_D3D10_WIN7_INTERFACE_VERSION function](nf-d3d10umddi-is-d3d10-win7-interface-version.md) | TBD |
| [IS_DXGI1_2_BASE_FUNCTIONS function](nf-d3d10umddi-is-dxgi1-2-base-functions.md) | TBD |
| [D3D10_DDI_DECODE_MIN_FILTER function](nf-d3d10umddi-d3d10-ddi-decode-min-filter.md) | TBD |
| [IS_DXGI1_3_BASE_FUNCTIONS function](nf-d3d10umddi-is-dxgi1-3-base-functions.md) | TBD |
| [IS_DXGI_MULTIPLANE_OVERLAY_FUNCTIONS function](nf-d3d10umddi-is-dxgi-multiplane-overlay-functions.md) | TBD |

This header is used in these topics:

- [display](..content/_display)
