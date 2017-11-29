# D3Dumddi.h header


This header is used by Display. For more information, see
- [Display](../_display/index.md)

D3Dumddi.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PFND3DDDICB_LOGSTRINGTABLEENTRY callback](nc-d3dumddi-pfnd3dddicb-logstringtableentry.md) | Locates a string table entry that is used by the LogMarkerStringTable function to log an Event Tracing for Windows (ETW) marker event. Optionally implemented by Windows Display Driver Model (WDDM) 1.3 and later drivers. |
| [PFND3DDDI_ALLOCATECB callback](nc-d3dumddi-pfnd3dddi-allocatecb.md) | The pfnAllocateCb function allocates system or video memory. |
| [PFND3DDDI_AUTHENTICATEDCHANNELKEYEXCHANGE callback](nc-d3dumddi-pfnd3dddi-authenticatedchannelkeyexchange.md) | The AuthenticatedChannelKeyExchange function negotiates the session key. |
| [PFND3DDDI_BLT callback](nc-d3dumddi-pfnd3dddi-blt.md) | The Blt function copies the contents of a source surface to a destination surface. |
| [PFND3DDDI_BUFBLT callback](nc-d3dumddi-pfnd3dddi-bufblt.md) | The BufBlt function performs a bit-block transfer (bitblt) operation from a source vertex or index buffer to a destination vertex or index buffer. |
| [PFND3DDDI_BUFBLT1 callback](nc-d3dumddi-pfnd3dddi-bufblt1.md) | Performs a bit-block transfer (bitblt) operation from a source vertex or index buffer to a destination vertex or index buffer. Implemented by Windows Display Driver Model (WDDM) 1.2 or later user-mode display drivers. |
| [PFND3DDDI_CAPTURETOSYSMEM callback](nc-d3dumddi-pfnd3dddi-capturetosysmem.md) | The CaptureToSysMem function copies the contents of a capture buffer to a destination surface. |
| [PFND3DDDI_CHECKCOUNTER callback](nc-d3dumddi-pfnd3dddi-checkcounter.md) | Called by the Microsoft Direct3D runtime to retrieve info that describes a counter. Must be implemented by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [PFND3DDDI_CHECKCOUNTERINFO callback](nc-d3dumddi-pfnd3dddi-checkcounterinfo.md) | Called by the Microsoft Direct3D runtime to determine global information that's related to manipulating counters. Must be implemented by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [PFND3DDDI_CHECKDIRECTFLIPSUPPORT callback](nc-d3dumddi-pfnd3dddi-checkdirectflipsupport.md) | Called by the Desktop Window Manager (DWM) to verify that the user-mode driver supports Direct Flip operations, in which video memory is seamlessly flipped between an application's managed primary allocations and the DWM's managed primary allocations. |
| [PFND3DDDI_CHECKMULTIPLANEOVERLAYSUPPORT callback](nc-d3dumddi-pfnd3dddi-checkmultiplaneoverlaysupport.md) | Called by the Microsoft Direct3D runtime to check the details on hardware support for multiplane overlays. |
| [PFND3DDDI_CHECKPRESENTDURATIONSUPPORT callback](nc-d3dumddi-pfnd3dddi-checkpresentdurationsupport.md) | Called by the Microsoft Direct3D runtime to request that the user-mode display driver get hardware device capabilities for seamlessly switching to a new monitor refresh rate. |
| [PFND3DDDI_CLEAR callback](nc-d3dumddi-pfnd3dddi-clear.md) | The Clear function performs hardware-assisted clearing on the rendering target, depth buffer, or stencil buffer. |
| [PFND3DDDI_CLOSEADAPTER callback](nc-d3dumddi-pfnd3dddi-closeadapter.md) | The CloseAdapter function releases resources for a graphics adapter object. |
| [PFND3DDDI_COLORFILL callback](nc-d3dumddi-pfnd3dddi-colorfill.md) | The ColorFill function fills a rectangle on the surface with a particular color. |
| [PFND3DDDI_COMPOSERECTS callback](nc-d3dumddi-pfnd3dddi-composerects.md) | The ComposeRects function composes two-dimensional areas from a source surface to a destination surface. |
| [PFND3DDDI_CONFIGUREAUTHENICATEDCHANNEL callback](nc-d3dumddi-pfnd3dddi-configureauthenicatedchannel.md) | The ConfigureAuthenticatedChannel function sets state within an authenticated channel. |
| [PFND3DDDI_CREATEAUTHENTICATEDCHANNEL callback](nc-d3dumddi-pfnd3dddi-createauthenticatedchannel.md) | The CreateAuthenticatedChannel function creates a channel that the Microsoft Direct3D runtime and the driver can use to set and query protections. |
| [PFND3DDDI_CREATECONTEXTVIRTUALCB callback](nc-d3dumddi-pfnd3dddi-createcontextvirtualcb.md) | pfnCreateContextVirtualCb should be used with contexts that support virtual addressing. |
| [PFND3DDDI_CREATECRYPTOSESSION callback](nc-d3dumddi-pfnd3dddi-createcryptosession.md) | The CreateCryptoSession function creates a crypto session that the Direct3D runtime uses to manage a session key and to perform crypto operations into and out of protected memory. |
| [PFND3DDDI_CREATEDECODEDEVICE callback](nc-d3dumddi-pfnd3dddi-createdecodedevice.md) | The CreateDecodeDevice function creates a Microsoft DirectX Video Acceleration (DirectX VA) decode device that is used to decode video. |
| [PFND3DDDI_CREATEDEVICE callback](nc-d3dumddi-pfnd3dddi-createdevice.md) | The CreateDevice function creates a graphics context that is referenced in subsequent calls. |
| [PFND3DDDI_CREATEEXTENSIONDEVICE callback](nc-d3dumddi-pfnd3dddi-createextensiondevice.md) | The CreateExtensionDevice function creates a Microsoft DirectX Video Acceleration (DirectX VA) extension device. |
| [PFND3DDDI_CREATEHWCONTEXTCB callback](nc-d3dumddi-pfnd3dddi-createhwcontextcb.md) | A callback to create a new hardware context. |
| [PFND3DDDI_CREATEHWQUEUECB callback](nc-d3dumddi-pfnd3dddi-createhwqueuecb.md) | A callback to create a new hardware queue. |
| [PFND3DDDI_CREATELIGHT callback](nc-d3dumddi-pfnd3dddi-createlight.md) | The CreateLight function creates a light source. |
| [PFND3DDDI_CREATEOVERLAY callback](nc-d3dumddi-pfnd3dddi-createoverlay.md) | The CreateOverlay function allocates overlay hardware and makes the overlay visible. |
| [PFND3DDDI_CREATEOVERLAYCB callback](nc-d3dumddi-pfnd3dddi-createoverlaycb.md) | The pfnCreateOverlayCb function creates a kernel-mode overlay object and calls the display miniport driver to display the overlay. |
| [PFND3DDDI_CREATEPAGINGQUEUECB callback](nc-d3dumddi-pfnd3dddi-createpagingqueuecb.md) | pfnCreatePagingQueueCb is used to create a device paging queue that can be used to synchronize with video memory management operations for the device, such as making the device resource resident. |
| [PFND3DDDI_CREATEPIXELSHADER callback](nc-d3dumddi-pfnd3dddi-createpixelshader.md) | The CreatePixelShader function converts pixel shader code into a hardware-specific format and associates this code with a shader handle. |
| [PFND3DDDI_CREATEQUERY callback](nc-d3dumddi-pfnd3dddi-createquery.md) | The CreateQuery function creates driver-side resources for a query that the Microsoft Direct3D runtime subsequently issues for processing. |
| [PFND3DDDI_CREATERESOURCE callback](nc-d3dumddi-pfnd3dddi-createresource.md) | The CreateResource function creates a resource. |
| [PFND3DDDI_CREATERESOURCE2 callback](nc-d3dumddi-pfnd3dddi-createresource2.md) | Creates a resource. Implemented by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [PFND3DDDI_CREATESYNCHRONIZATIONOBJECT2CB callback](nc-d3dumddi-pfnd3dddi-createsynchronizationobject2cb.md) | Creates a GPU synchronization object that a device context can signal and wait for. Used by WDDM 1.2 and later user-mode display drivers. |
| [PFND3DDDI_CREATESYNCHRONIZATIONOBJECTCB callback](nc-d3dumddi-pfnd3dddi-createsynchronizationobjectcb.md) | The pfnCreateSynchronizationObjectCb function creates a synchronization object that a device context can signal and wait for. |
| [PFND3DDDI_CREATEVERTEXSHADERDECL callback](nc-d3dumddi-pfnd3dddi-createvertexshaderdecl.md) | The CreateVertexShaderDecl function converts the vertex shader declaration into a hardware-specific format and associates the declaration with a shader handle. |
| [PFND3DDDI_CREATEVERTEXSHADERFUNC callback](nc-d3dumddi-pfnd3dddi-createvertexshaderfunc.md) | The CreateVertexShaderFunc function converts vertex shader code into a hardware-specific format and associates the code with a shader handle. |
| [PFND3DDDI_CREATEVIDEOPROCESSDEVICE callback](nc-d3dumddi-pfnd3dddi-createvideoprocessdevice.md) | The CreateVideoProcessDevice function creates a Microsoft DirectX Video Acceleration (DirectX VA) video processing device that is used to process video (for example, to deinterlace the video and adjust ProcAmp properties of the video). |
| [PFND3DDDI_CRYPTOSESSIONKEYEXCHANGE callback](nc-d3dumddi-pfnd3dddi-cryptosessionkeyexchange.md) | The CryptoSessionKeyExchange function negotiates a session key. |
| [PFND3DDDI_DEALLOCATE2CB callback](nc-d3dumddi-pfnd3dddi-deallocate2cb.md) | The pfnDeallocate2Cb user mode callback function releases allocations for a kernel-mode resource object if the resource object was created. |
| [PFND3DDDI_DEALLOCATECB callback](nc-d3dumddi-pfnd3dddi-deallocatecb.md) | The pfnDeallocateCb callback function releases allocations or a kernel-mode resource object if the resource object was created. |
| [PFND3DDDI_DECODEBEGINFRAME callback](nc-d3dumddi-pfnd3dddi-decodebeginframe.md) | The DecodeBeginFrame function notifies the user-mode display driver that decoding can begin on the specified Microsoft DirectX Video Accelerator (VA) decode device. |
| [PFND3DDDI_DECODEENDFRAME callback](nc-d3dumddi-pfnd3dddi-decodeendframe.md) | The DecodeEndFrame function notifies the user-mode display driver that all of the data that was required to decode the current frame was submitted. |
| [PFND3DDDI_DECODEEXECUTE callback](nc-d3dumddi-pfnd3dddi-decodeexecute.md) | The DecodeExecute function performs a decode operation by using the given Microsoft DirectX Video Accelerator (VA) decode device. |
| [PFND3DDDI_DECODEEXTENSIONEXECUTE callback](nc-d3dumddi-pfnd3dddi-decodeextensionexecute.md) | The DecodeExtensionExecute function performs a decode operation by using the given Microsoft DirectX Video Accelerator (VA) nonstandard decode device. |
| [PFND3DDDI_DECRYPTIONBLT callback](nc-d3dumddi-pfnd3dddi-decryptionblt.md) | The DecryptionBlt function writes data to a protected surface. |
| [PFND3DDDI_DELETEPIXELSHADER callback](nc-d3dumddi-pfnd3dddi-deletepixelshader.md) | The DeletePixelShader function cleans up driver-side resources that are associated with pixel shader code. |
| [PFND3DDDI_DELETEVERTEXSHADERDECL callback](nc-d3dumddi-pfnd3dddi-deletevertexshaderdecl.md) | The DeleteVertexShaderDecl function cleans up driver-side resources that are associated with the vertex shader declaration. |
| [PFND3DDDI_DELETEVERTEXSHADERFUNC callback](nc-d3dumddi-pfnd3dddi-deletevertexshaderfunc.md) | The DeleteVertexShaderFunc function cleans up driver-side resources that are associated with vertex shader code. |
| [PFND3DDDI_DEPTHFILL callback](nc-d3dumddi-pfnd3dddi-depthfill.md) | The DepthFill function fills a depth buffer with a pixel value that is specified in native format. |
| [PFND3DDDI_DESTROYAUTHENTICATEDCHANNEL callback](nc-d3dumddi-pfnd3dddi-destroyauthenticatedchannel.md) | The DestroyAuthenticatedChannel function releases resources for the authenticated channel that the CreateAuthenticatedChannel function creates. |
| [PFND3DDDI_DESTROYCONTEXTCB callback](nc-d3dumddi-pfnd3dddi-destroycontextcb.md) | The pfnDestroyContextCb function destroys the context that was created through a call to the pfnCreateContextCb function. |
| [PFND3DDDI_DESTROYCRYPTOSESSION callback](nc-d3dumddi-pfnd3dddi-destroycryptosession.md) | The DestroyCryptoSession function releases resources for the encryption session that the CreateCryptoSession function creates. |
| [PFND3DDDI_DESTROYDECODEDEVICE callback](nc-d3dumddi-pfnd3dddi-destroydecodedevice.md) | The DestroyDecodeDevice function releases resources for a Microsoft DirectX Video Acceleration (VA) decode device. |
| [PFND3DDDI_DESTROYDEVICE callback](nc-d3dumddi-pfnd3dddi-destroydevice.md) | The DestroyDevice function destroys a graphics context. |
| [PFND3DDDI_DESTROYEXTENSIONDEVICE callback](nc-d3dumddi-pfnd3dddi-destroyextensiondevice.md) | The DestroyExtensionDevice function releases resources for a Microsoft DirectX Video Acceleration (VA) extension device. |
| [PFND3DDDI_DESTROYHWCONTEXTCB callback](nc-d3dumddi-pfnd3dddi-destroyhwcontextcb.md) | A callback to destroy a hardware context. |
| [PFND3DDDI_DESTROYHWQUEUECB callback](nc-d3dumddi-pfnd3dddi-destroyhwqueuecb.md) | A callback to destroy a hardware queue. |
| [PFND3DDDI_DESTROYLIGHT callback](nc-d3dumddi-pfnd3dddi-destroylight.md) | The DestroyLight function deactivates a light source. |
| [PFND3DDDI_DESTROYOVERLAY callback](nc-d3dumddi-pfnd3dddi-destroyoverlay.md) | The DestroyOverlay function disables the overlay hardware and frees the overlay handle. |
| [PFND3DDDI_DESTROYOVERLAYCB callback](nc-d3dumddi-pfnd3dddi-destroyoverlaycb.md) | The pfnDestroyOverlayCb function disables the overlay hardware and destroys the kernel-mode overlay object. |
| [PFND3DDDI_DESTROYPAGINGQUEUECB callback](nc-d3dumddi-pfnd3dddi-destroypagingqueuecb.md) | pfnDestroyPagingQueueCb waits for a paging queue to finish all operations queued to it and destroys it along with the associated sync object. |
| [PFND3DDDI_DESTROYQUERY callback](nc-d3dumddi-pfnd3dddi-destroyquery.md) | The DestroyQuery function releases resources for a query. |
| [PFND3DDDI_DESTROYRESOURCE callback](nc-d3dumddi-pfnd3dddi-destroyresource.md) | The DestroyResource function releases a specified resource. |
| [PFND3DDDI_DESTROYSYNCHRONIZATIONOBJECTCB callback](nc-d3dumddi-pfnd3dddi-destroysynchronizationobjectcb.md) | The pfnDestroySynchronizationObjectCb function destroys the synchronization object that was created through a call to the pfnCreateSynchronizationObjectCb function. |
| [PFND3DDDI_DESTROYVIDEOPROCESSDEVICE callback](nc-d3dumddi-pfnd3dddi-destroyvideoprocessdevice.md) | The DestroyVideoProcessDevice function releases resources for a Microsoft DirectX Video Acceleration (VA) video processing device. |
| [PFND3DDDI_DISCARD callback](nc-d3dumddi-pfnd3dddi-discard.md) | Discards (evicts) a set of subresources from video display memory. Implemented by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [PFND3DDDI_DRAWINDEXEDPRIMITIVE callback](nc-d3dumddi-pfnd3dddi-drawindexedprimitive.md) | The DrawIndexedPrimitive function draws indexed primitives that the Microsoft Direct3D runtime has not transformed the index data in. |
| [PFND3DDDI_DRAWINDEXEDPRIMITIVE2 callback](nc-d3dumddi-pfnd3dddi-drawindexedprimitive2.md) | The DrawIndexedPrimitive2 function draws indexed primitives that the Microsoft Direct3D runtime has transformed the index data in. |
| [PFND3DDDI_DRAWPRIMITIVE callback](nc-d3dumddi-pfnd3dddi-drawprimitive.md) | The DrawPrimitive function draws nonindexed primitives in which the Microsoft Direct3D runtime has not transformed the vertex data. |
| [PFND3DDDI_DRAWPRIMITIVE2 callback](nc-d3dumddi-pfnd3dddi-drawprimitive2.md) | The DrawPrimitive2 function draws nonindexed primitives in which the Microsoft Direct3D runtime has transformed the vertex data. |
| [PFND3DDDI_DRAWRECTPATCH callback](nc-d3dumddi-pfnd3dddi-drawrectpatch.md) | The DrawRectPatch function draws a new or cached rectangular patch or updates the specification of a previously defined patch. |
| [PFND3DDDI_DRAWTRIPATCH callback](nc-d3dumddi-pfnd3dddi-drawtripatch.md) | The DrawTriPatch function draws a new or cached triangular patch or updates the specification of a previously defined patch. |
| [PFND3DDDI_DXVAHD_CREATEVIDEOPROCESSOR callback](nc-d3dumddi-pfnd3dddi-dxvahd-createvideoprocessor.md) | The CreateVideoProcessor function creates a Microsoft DirectX Video Acceleration (DirectX VA) video processor that is used to process high-definition video. |
| [PFND3DDDI_DXVAHD_DESTROYVIDEOPROCESSOR callback](nc-d3dumddi-pfnd3dddi-dxvahd-destroyvideoprocessor.md) | The DestroyVideoProcessor function releases resources for a Microsoft DirectX Video Acceleration (VA) video processor. |
| [PFND3DDDI_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE callback](nc-d3dumddi-pfnd3dddi-dxvahd-getvideoprocessbltstateprivate.md) | The GetVideoProcessBltStatePrivate function retrieves the state data of a private bit-block transfer (bitblt) for a video processor. |
| [PFND3DDDI_DXVAHD_GETVIDEOPROCESSSTREAMSTATEPRIVATE callback](nc-d3dumddi-pfnd3dddi-dxvahd-getvideoprocessstreamstateprivate.md) | The GetVideoProcessStreamStatePrivate function retrieves the private stream-state data for a video processor. |
| [PFND3DDDI_DXVAHD_SETVIDEOPROCESSBLTSTATE callback](nc-d3dumddi-pfnd3dddi-dxvahd-setvideoprocessbltstate.md) | The SetVideoProcessBltState function sets the state of a bit-block transfer (bitblt) for a video processor. |
| [PFND3DDDI_DXVAHD_SETVIDEOPROCESSSTREAMSTATE callback](nc-d3dumddi-pfnd3dddi-dxvahd-setvideoprocessstreamstate.md) | The SetVideoProcessStreamState function sets the stream state for a video processor. |
| [PFND3DDDI_DXVAHD_VIDEOPROCESSBLTHD callback](nc-d3dumddi-pfnd3dddi-dxvahd-videoprocessblthd.md) | The VideoProcessBltHD function processes video input streams and composes to an output surface. |
| [PFND3DDDI_ENCRYPTIONBLT callback](nc-d3dumddi-pfnd3dddi-encryptionblt.md) | The EncryptionBlt function reads encrypted data from a protected surface. |
| [PFND3DDDI_ESCAPECB callback](nc-d3dumddi-pfnd3dddi-escapecb.md) | The pfnEscapeCb callback function shares information with the display miniport driver. |
| [PFND3DDDI_EVICTCB callback](nc-d3dumddi-pfnd3dddi-evictcb.md) | pfnEvictCb is used to instruct the OS to decrement the residency reference count. Once this count reaches zero, it will remove the allocation from the device residency list. |
| [PFND3DDDI_EXTENSIONEXECUTE callback](nc-d3dumddi-pfnd3dddi-extensionexecute.md) | The ExtensionExecute function performs an operation by using the given Microsoft DirectX Video Accelerator (VA) extension device. |
| [PFND3DDDI_FINISHSESSIONKEYREFRESH callback](nc-d3dumddi-pfnd3dddi-finishsessionkeyrefresh.md) | The FinishSessionKeyRefresh function indicates that all buffers from that point in time use the updated session key value. |
| [PFND3DDDI_FLIPOVERLAY callback](nc-d3dumddi-pfnd3dddi-flipoverlay.md) | The FlipOverlay function causes the overlay hardware to start displaying the given new allocation. |
| [PFND3DDDI_FLIPOVERLAYCB callback](nc-d3dumddi-pfnd3dddi-flipoverlaycb.md) | The pfnFlipOverlayCb function changes the allocation to display on the overlay or indicates to display the other field of the currently displaying allocation, when deinterlacing an interleaved resource. |
| [PFND3DDDI_FLUSH callback](nc-d3dumddi-pfnd3dddi-flush.md) | The Flush function submits outstanding hardware commands that are in the hardware command buffer to the display miniport driver. |
| [PFND3DDDI_FLUSH1 callback](nc-d3dumddi-pfnd3dddi-flush1.md) | Called by the Microsoft Direct3D runtime to submit outstanding hardware commands that are in the hardware command buffer to the display miniport driver. Must be implemented by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [PFND3DDDI_FREEGPUVIRTUALADDRESSCB callback](nc-d3dumddi-pfnd3dddi-freegpuvirtualaddresscb.md) | pfnFreeGpuVirtualAddressCb releases a range of graphics processing unit (GPU) virtual addresses that was previously reserved or mapped. |
| [PFND3DDDI_GENERATEMIPSUBLEVELS callback](nc-d3dumddi-pfnd3dddi-generatemipsublevels.md) | The GenerateMipSubLevels function regenerates the sublevels of a MIP-map texture. |
| [PFND3DDDI_GETCAPS callback](nc-d3dumddi-pfnd3dddi-getcaps.md) | The GetCaps function queries for capabilities of the graphics adapter. |
| [PFND3DDDI_GETCAPTUREALLOCATIONHANDLE callback](nc-d3dumddi-pfnd3dddi-getcaptureallocationhandle.md) | The GetCaptureAllocationHandle function maps the given capture resource handle to a kernel-mode allocation handle. |
| [PFND3DDDI_GETENCRYPTIONBLTKEY callback](nc-d3dumddi-pfnd3dddi-getencryptionbltkey.md) | The GetEncryptionBltKey function returns the key that is used to decrypt the data that the driver's EncryptionBlt function returns. |
| [PFND3DDDI_GETINFO callback](nc-d3dumddi-pfnd3dddi-getinfo.md) | The GetInfo function retrieves information about the specified display device. |
| [PFND3DDDI_GETMULTISAMPLEMETHODLISTCB callback](nc-d3dumddi-pfnd3dddi-getmultisamplemethodlistcb.md) | The pfnGetMultisampleMethodListCb function retrieves a list of multiple-sample methods that are used for the given width, height, and format of an allocation. |
| [PFND3DDDI_GETOVERLAYCOLORCONTROLS callback](nc-d3dumddi-pfnd3dddi-getoverlaycolorcontrols.md) | The GetOverlayColorControls function retrieves color-control settings for the given overlay. |
| [PFND3DDDI_GETPITCH callback](nc-d3dumddi-pfnd3dddi-getpitch.md) | The GetPitch function retrieves the pitch of a protected or non-lockable surface. |
| [PFND3DDDI_GETQUERYDATA callback](nc-d3dumddi-pfnd3dddi-getquerydata.md) | The GetQueryData function retrieves information about a query. |
| [PFND3DDDI_GETRESOURCEPRESENTPRIVATEDRIVERDATACB callback](nc-d3dumddi-pfnd3dddi-getresourcepresentprivatedriverdatacb.md) | pfnGetResourcePresentPrivateDriverDataCb is used to query the resource private data, which is associated with the resource during Present. |
| [PFND3DDDI_ISSUEQUERY callback](nc-d3dumddi-pfnd3dddi-issuequery.md) | The IssueQuery function processes a query. |
| [PFND3DDDI_LOCK callback](nc-d3dumddi-pfnd3dddi-lock.md) | The Lock function locks the given resource or a surface within the resource. |
| [PFND3DDDI_LOCK2CB callback](nc-d3dumddi-pfnd3dddi-lock2cb.md) | The pfnLock2Cb function locks an allocation and obtains a pointer to the allocation from the display miniport driver or video memory manager. |
| [PFND3DDDI_LOCKASYNC callback](nc-d3dumddi-pfnd3dddi-lockasync.md) | The LockAsync function locks the specified resource or a surface within the resource. |
| [PFND3DDDI_LOCKCB callback](nc-d3dumddi-pfnd3dddi-lockcb.md) | The pfnLockCb function locks an allocation and obtains a pointer to the allocation from the display miniport driver or video memory manager. |
| [PFND3DDDI_LOGSTRINGTABLE callback](nc-d3dumddi-pfnd3dddi-logstringtable.md) | Called by the Microsoft Direct3D runtime to request that the user-mode display driver log a custom Event Tracing for Windows (ETW) marker event. Optionally implemented by Windows Display Driver Model (WDDM) 1.3 and later drivers. |
| [PFND3DDDI_LOGUMDMARKERCB callback](nc-d3dumddi-pfnd3dddi-logumdmarkercb.md) | Called by the user-mode display driver to log a custom Event Tracing for Windows (ETW) marker event. |
| [PFND3DDDI_MAKERESIDENTCB callback](nc-d3dumddi-pfnd3dddi-makeresidentcb.md) | pfnMakeResidentCb is used to instruct the OS to add a resource to the device residency list and increment the residency reference count on this allocation. |
| [PFND3DDDI_MAPGPUVIRTUALADDRESSCB callback](nc-d3dumddi-pfnd3dddi-mapgpuvirtualaddresscb.md) | pfnMapGpuVirtualAddressCb maps graphics processing unit (GPU) virtual address ranges to a specific allocation range or puts it to the Invalid or Zero state. |
| [PFND3DDDI_MULTIPLYTRANSFORM callback](nc-d3dumddi-pfnd3dddi-multiplytransform.md) | The MultiplyTransform function modifies the current transform. |
| [PFND3DDDI_OFFERALLOCATIONS2CB callback](nc-d3dumddi-pfnd3dddi-offerallocations2cb.md) | Called by the user-mode display driver to offer video memory allocations for reuse. |
| [PFND3DDDI_OFFERRESOURCES callback](nc-d3dumddi-pfnd3dddi-offerresources.md) | Called by the Microsoft Direct3D runtime to request that the user-mode display driver offer video memory resources for reuse. |
| [PFND3DDDI_OPENADAPTER callback](nc-d3dumddi-pfnd3dddi-openadapter.md) | The OpenAdapter function creates a graphics adapter object that is referenced in subsequent calls. |
| [PFND3DDDI_OPENRESOURCE callback](nc-d3dumddi-pfnd3dddi-openresource.md) | The OpenResource function informs the driver that a shared resource is opened. |
| [PFND3DDDI_PRESENT callback](nc-d3dumddi-pfnd3dddi-present.md) | The Present function notifies the user-mode display driver that an application finished rendering and requests that the driver display the source surface by either copying or flipping or that the driver perform a color-fill operation. |
| [PFND3DDDI_PRESENT1 callback](nc-d3dumddi-pfnd3dddi-present1.md) | Notifies the user-mode display driver that an application finished rendering and that all ownership of the shared resource is released, and requests that the driver display to the destination surface. |
| [PFND3DDDI_PRESENT1 callback](nc-d3dumddi-pfnd3dddi-present1~r1.md) | Notifies the user-mode display driver that an application finished rendering and that all ownership of the shared resource is released, and requests that the driver display to the destination surface. |
| [PFND3DDDI_PRESENTCB callback](nc-d3dumddi-pfnd3dddi-presentcb.md) | The pfnPresentCb function copies content from a source allocation. |
| [PFND3DDDI_PRESENTMULTIPLANEOVERLAY callback](nc-d3dumddi-pfnd3dddi-presentmultiplaneoverlay.md) | Called by the Microsoft Direct3D runtime to notify the user-mode display driver that an application finished rendering and requests that the driver display the source surface by either copying or flipping or that the driver perform a color-fill operation. Must be implemented by Windows Display Driver Model (WDDM) 1.3 or later drivers that support multiplane overlays. |
| [PFND3DDDI_QUERYADAPTERINFOCB callback](nc-d3dumddi-pfnd3dddi-queryadapterinfocb.md) | The pfnQueryAdapterInfoCb function retrieves graphics adapter information. |
| [PFND3DDDI_QUERYAUTHENTICATEDCHANNEL callback](nc-d3dumddi-pfnd3dddi-queryauthenticatedchannel.md) | The QueryAuthenticatedChannel function queries an authenticated channel for capability and state information. |
| [PFND3DDDI_QUERYDLISTFORAPPLICATION1 callback](nc-d3dumddi-pfnd3dddi-querydlistforapplication1.md) | Called during Microsoft Direct3D initialization on a hybrid system to determine which GPU an application should run on. A dList is a list of applications that need cross-adapter shared surfaces for high-performance rendering on the discrete GPU. |
| [PFND3DDDI_QUERYRESIDENCYCB callback](nc-d3dumddi-pfnd3dddi-queryresidencycb.md) | The pfnQueryResidencyCb function queries the residency status of a resource or list of allocations. |
| [PFND3DDDI_QUERYRESOURCERESIDENCY callback](nc-d3dumddi-pfnd3dddi-queryresourceresidency.md) | The QueryResourceResidency function determines the residency of the given list of resources. |
| [PFND3DDDI_RECLAIMALLOCATIONS3CB callback](nc-d3dumddi-pfnd3dddi-reclaimallocations3cb.md) | pfnReclaimAllocations3Cb is called by the user mode driver to reclaim video memory allocations that were previously offered for reuse. |
| [PFND3DDDI_RECLAIMRESOURCES callback](nc-d3dumddi-pfnd3dddi-reclaimresources.md) | Called by the Microsoft Direct3D runtime to reclaim video memory resources that it previously offered for reuse. |
| [PFND3DDDI_RENAME callback](nc-d3dumddi-pfnd3dddi-rename.md) | The Rename function informs a user-mode display driver to start using the renamed allocation that the LockAsync function previously returned for the specified resource. |
| [PFND3DDDI_RENDERCB callback](nc-d3dumddi-pfnd3dddi-rendercb.md) | The pfnRenderCb function submits the current command buffer for rendering to the display miniport driver. |
| [PFND3DDDI_RESERVEGPUVIRTUALADDRESSCB callback](nc-d3dumddi-pfnd3dddi-reservegpuvirtualaddresscb.md) | pfnReserveGPUVirtualAddressCb reserves an address range in the current process graphics processing unit (GPU) virtual address space. The address range is only reserved, there is no actual memory behind it. |
| [PFND3DDDI_RESOLVESHAREDRESOURCE callback](nc-d3dumddi-pfnd3dddi-resolvesharedresource.md) | The ResolveSharedResource function informs a user-mode display driver that ownership of a shared surface changed or that a surface is being used for GDI interoperation. |
| [PFND3DDDI_SETASYNCCALLBACKSCB callback](nc-d3dumddi-pfnd3dddi-setasynccallbackscb.md) | The pfnSetAsyncCallbacksCb function notifies the Microsoft Direct3D runtime whether the runtime will start or stop receiving calls to the runtime's callback functions from a worker thread. |
| [PFND3DDDI_SETCLIPPLANE callback](nc-d3dumddi-pfnd3dddi-setclipplane.md) | The SetClipPlane function sets a clip plane. |
| [PFND3DDDI_SETCONVOLUTIONKERNELMONO callback](nc-d3dumddi-pfnd3dddi-setconvolutionkernelmono.md) | The SetConvolutionKernelMono function defines the resolution and weights of the kernel filter, which is used when the D3DTEXF_CONVOLUTIONMONO texture filtering mode is set. |
| [PFND3DDDI_SETDECODERENDERTARGET callback](nc-d3dumddi-pfnd3dddi-setdecoderendertarget.md) | The SetDecodeRenderTarget function sets the render target surface for decoding operations. |
| [PFND3DDDI_SETDEPTHSTENCIL callback](nc-d3dumddi-pfnd3dddi-setdepthstencil.md) | The SetDepthStencil function sets the depth buffer in the driver's context. |
| [PFND3DDDI_SETDISPLAYMODE callback](nc-d3dumddi-pfnd3dddi-setdisplaymode.md) | The SetDisplayMode function switches to a display mode or primary that is not supported by the GDI desktop. |
| [PFND3DDDI_SETDISPLAYMODECB callback](nc-d3dumddi-pfnd3dddi-setdisplaymodecb.md) | The pfnSetDisplayModeCb function sets the allocation that is used to scan out to the display. |
| [PFND3DDDI_SETDISPLAYPRIVATEDRIVERFORMATCB callback](nc-d3dumddi-pfnd3dddi-setdisplayprivatedriverformatcb.md) | The pfnSetDisplayPrivateDriverFormatCb function changes the private-format attribute of a video present source. |
| [PFND3DDDI_SETINDICES callback](nc-d3dumddi-pfnd3dddi-setindices.md) | The SetIndices function sets the current index buffer. |
| [PFND3DDDI_SETINDICESUM callback](nc-d3dumddi-pfnd3dddi-setindicesum.md) | The SetIndicesUM function sets the current index buffer to the given user memory buffer. |
| [PFND3DDDI_SETLIGHT callback](nc-d3dumddi-pfnd3dddi-setlight.md) | The SetLight function sets properties for a light source. |
| [PFND3DDDI_SETMARKER callback](nc-d3dumddi-pfnd3dddi-setmarker.md) | Notifies the user-mode display driver that it must generate a new time stamp if any GPU work has completed since the last call to pfnSetMarker. |
| [PFND3DDDI_SETMARKERMODE callback](nc-d3dumddi-pfnd3dddi-setmarkermode.md) | Notifies the user-mode display driver that it should support a type of Event Tracing for Windows (ETW) marker event. |
| [PFND3DDDI_SETMATERIAL callback](nc-d3dumddi-pfnd3dddi-setmaterial.md) | The SetMaterial function sets the material properties that devices on the system use to create the required effect during rendering. |
| [PFND3DDDI_SETOVERLAYCOLORCONTROLS callback](nc-d3dumddi-pfnd3dddi-setoverlaycolorcontrols.md) | The SetOverlayColorControls function changes color-control settings for the given overlay. |
| [PFND3DDDI_SETPALETTE callback](nc-d3dumddi-pfnd3dddi-setpalette.md) | The SetPalette function associates a palette with a texture. |
| [PFND3DDDI_SETPIXELSHADER callback](nc-d3dumddi-pfnd3dddi-setpixelshader.md) | The SetPixelShader function sets a pixel shader to be used in all drawing operations. |
| [PFND3DDDI_SETPIXELSHADERCONST callback](nc-d3dumddi-pfnd3dddi-setpixelshaderconst.md) | The SetPixelShaderConst function sets one or more pixel shader constant registers with floating-point values. |
| [PFND3DDDI_SETPIXELSHADERCONSTB callback](nc-d3dumddi-pfnd3dddi-setpixelshaderconstb.md) | The SetPixelShaderConstB function sets one or more pixel shader constant registers with Boolean values. |
| [PFND3DDDI_SETPIXELSHADERCONSTI callback](nc-d3dumddi-pfnd3dddi-setpixelshaderconsti.md) | The SetPixelShaderConstI function sets one or more pixel shader constant registers with integer values. |
| [PFND3DDDI_SETPRIORITY callback](nc-d3dumddi-pfnd3dddi-setpriority.md) | The SetPriority function sets the eviction-from-memory priority for a managed texture. |
| [PFND3DDDI_SETPRIORITYCB callback](nc-d3dumddi-pfnd3dddi-setprioritycb.md) | The pfnSetPriorityCb function sets the priority level of a resource or list of allocations. |
| [PFND3DDDI_SETRENDERSTATE callback](nc-d3dumddi-pfnd3dddi-setrenderstate.md) | The SetRenderState function updates a render state. |
| [PFND3DDDI_SETRENDERTARGET callback](nc-d3dumddi-pfnd3dddi-setrendertarget.md) | The SetRenderTarget function sets the render target surface. |
| [PFND3DDDI_SETSCISSORRECT callback](nc-d3dumddi-pfnd3dddi-setscissorrect.md) | The SetScissorRect function marks a portion of a render target that rendering is confined to. |
| [PFND3DDDI_SETSTREAMSOURCE callback](nc-d3dumddi-pfnd3dddi-setstreamsource.md) | The SetStreamSource function binds a portion of a vertex stream source to a vertex buffer. |
| [PFND3DDDI_SETSTREAMSOURCEFREQ callback](nc-d3dumddi-pfnd3dddi-setstreamsourcefreq.md) | The SetStreamSourceFreq function sets the frequency divisor of a stream source that is bound to a vertex buffer. |
| [PFND3DDDI_SETSTREAMSOURCEUM callback](nc-d3dumddi-pfnd3dddi-setstreamsourceum.md) | The SetStreamSourceUM function binds a vertex stream source to a user memory buffer. |
| [PFND3DDDI_SETTEXTURE callback](nc-d3dumddi-pfnd3dddi-settexture.md) | The SetTexture function inserts a texture at a particular stage in a multiple-texture group. |
| [PFND3DDDI_SETTEXTURESTAGESTATE callback](nc-d3dumddi-pfnd3dddi-settexturestagestate.md) | The SetTextureStageState function updates the state of a texture at a particular stage in a multiple-texture group. |
| [PFND3DDDI_SETTRANSFORM callback](nc-d3dumddi-pfnd3dddi-settransform.md) | The SetTransform function sets up a transform. |
| [PFND3DDDI_SETVERTEXSHADERCONST callback](nc-d3dumddi-pfnd3dddi-setvertexshaderconst.md) | The SetVertexShaderConst function sets one or more vertex shader constant registers with floating-point values. |
| [PFND3DDDI_SETVERTEXSHADERCONSTB callback](nc-d3dumddi-pfnd3dddi-setvertexshaderconstb.md) | The SetVertexShaderConstB function sets one or more vertex shader constant registers with Boolean values. |
| [PFND3DDDI_SETVERTEXSHADERDECL callback](nc-d3dumddi-pfnd3dddi-setvertexshaderdecl.md) | The SetVertexShaderDecl function sets the vertex shader declaration so that all of the subsequent drawing operations use that declaration. |
| [PFND3DDDI_SETVERTEXSHADERFUNC callback](nc-d3dumddi-pfnd3dddi-setvertexshaderfunc.md) | The SetVertexShaderFunc function sets the vertex shader code so that all of the subsequent drawing operations use that code. |
| [PFND3DDDI_SETVIDEOPROCESSRENDERTARGET callback](nc-d3dumddi-pfnd3dddi-setvideoprocessrendertarget.md) | The SetVideoProcessRenderTarget function sets the render target surface that is used for video processing. |
| [PFND3DDDI_SETVIEWPORT callback](nc-d3dumddi-pfnd3dddi-setviewport.md) | The SetViewport function informs guard-band-aware drivers of the view-clipping rectangle. |
| [PFND3DDDI_SETZRANGE callback](nc-d3dumddi-pfnd3dddi-setzrange.md) | The SetZRange function informs the driver about the range of z values. |
| [PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECT2CB callback](nc-d3dumddi-pfnd3dddi-signalsynchronizationobject2cb.md) | Inserts a signal on the specified synchronization objects in the specified context direct memory access (DMA) stream. Used by WDDM 1.2 and later user-mode display drivers. |
| [PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECTCB callback](nc-d3dumddi-pfnd3dddi-signalsynchronizationobjectcb.md) | The pfnSignalSynchronizationObjectCb function inserts a signal on the specified synchronization objects in the specified context DMA stream. |
| [PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECTFROMCPUCB callback](nc-d3dumddi-pfnd3dddi-signalsynchronizationobjectfromcpucb.md) | pfnSignalSynchronizationObjectFromCpuCb enables a driver to signal a monitored fence. |
| [PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2CB callback](nc-d3dumddi-pfnd3dddi-signalsynchronizationobjectfromgpu2cb.md) | pfnSignalSynchronizationObjectFromGpu2Cb is used to signal a monitored fence. |
| [PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECTFROMGPUCB callback](nc-d3dumddi-pfnd3dddi-signalsynchronizationobjectfromgpucb.md) | pfnSignalSynchronizationObjectFromGpuCb is used to signal a monitored fence. |
| [PFND3DDDI_STARTSESSIONKEYREFRESH callback](nc-d3dumddi-pfnd3dddi-startsessionkeyrefresh.md) | The StartSessionKeyRefresh function returns a random number that the driver's FinishSessionKeyRefresh function subsequently uses to perform an exclusive OR operation (XOR) with the session key. |
| [PFND3DDDI_STATESET callback](nc-d3dumddi-pfnd3dddi-stateset.md) | The StateSet function sets a state block. |
| [PFND3DDDI_SUBMITCOMMANDCB callback](nc-d3dumddi-pfnd3dddi-submitcommandcb.md) | pfnSubmitCommandCb is used to submit command buffers on contexts that support graphics processing unit (GPU) virtual addressing. |
| [PFND3DDDI_SUBMITCOMMANDTOHWQUEUECB callback](nc-d3dumddi-pfnd3dddi-submitcommandtohwqueuecb.md) | A callback to submit a command to the hardware queue. |
| [PFND3DDDI_SUBMITSIGNALSYNCOBJECTSTOHWQUEUECB callback](nc-d3dumddi-pfnd3dddi-submitsignalsyncobjectstohwqueuecb.md) | A callback to submit a signal command to the hardware queue. |
| [PFND3DDDI_SUBMITWAITFORSYNCOBJECTSTOHWQUEUECB callback](nc-d3dumddi-pfnd3dddi-submitwaitforsyncobjectstohwqueuecb.md) | A callback to submit a wait command to the hardware queue. |
| [PFND3DDDI_TEXBLT callback](nc-d3dumddi-pfnd3dddi-texblt.md) | The TexBlt function performs a bit-block transfer (bitblt) operation from a source texture to a destination texture, including all of the sublevels of the source texture. |
| [PFND3DDDI_TEXBLT1 callback](nc-d3dumddi-pfnd3dddi-texblt1.md) | Performs a bit-block transfer (bitblt) operation from a source texture to a destination texture, including all of the sublevels of the source texture. Implemented by Windows Display Driver Model (WDDM) 1.2 or later user-mode display drivers. |
| [PFND3DDDI_TRIMRESIDENCYSET callback](nc-d3dumddi-pfnd3dddi-trimresidencyset.md) | pfnTrimResidencySet is used to trim the residency list for a given device. User mode drivers are required to implement this callback in order to participate in the new memory residency model. |
| [PFND3DDDI_UNLOCK callback](nc-d3dumddi-pfnd3dddi-unlock.md) | The Unlock function unlocks a resource or a surface within the resource that was previously locked by the Lock function. |
| [PFND3DDDI_UNLOCK2CB callback](nc-d3dumddi-pfnd3dddi-unlock2cb.md) | The pfnUnlock2Cb function unlocks an allocation that was locked by a call to the pfnLock2Cb function. |
| [PFND3DDDI_UNLOCKASYNC callback](nc-d3dumddi-pfnd3dddi-unlockasync.md) | The UnlockAsync function unlocks a resource or a surface within the resource that the LockAsync function previously locked. |
| [PFND3DDDI_UNLOCKCB callback](nc-d3dumddi-pfnd3dddi-unlockcb.md) | The pfnUnlockCb function unlocks an allocation that was locked by a call to the pfnLockCb function. |
| [PFND3DDDI_UPDATEALLOCATIONPROPERTYCB callback](nc-d3dumddi-pfnd3dddi-updateallocationpropertycb.md) | The pfnUpdateAllocationPropertyCb functions updates the property of an allocation without creating a new allocation. |
| [PFND3DDDI_UPDATEGPUVIRTUALADDRESSCB callback](nc-d3dumddi-pfnd3dddi-updategpuvirtualaddresscb.md) | pfnUpdateGpuVirtualAddressCb is a special operation used in the context of tile resources. |
| [PFND3DDDI_UPDATEOVERLAY callback](nc-d3dumddi-pfnd3dddi-updateoverlay.md) | The UpdateOverlay function reconfigures or moves an overlay that is being displayed. |
| [PFND3DDDI_UPDATEOVERLAYCB callback](nc-d3dumddi-pfnd3dddi-updateoverlaycb.md) | The pfnUpdateOverlayCb function modifies a kernel-mode overlay object. |
| [PFND3DDDI_UPDATEPALETTE callback](nc-d3dumddi-pfnd3dddi-updatepalette.md) | The UpdatePalette function updates a texture palette. |
| [PFND3DDDI_UPDATESUBRESOURCEUP callback](nc-d3dumddi-pfnd3dddi-updatesubresourceup.md) | Called by the Microsoft Direct3D runtime to update a destination subresource region from a source system-memory region. Must be implemented by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [PFND3DDDI_UPDATEWINFO callback](nc-d3dumddi-pfnd3dddi-updatewinfo.md) | The UpdateWInfo function updates the w range for w buffering. |
| [PFND3DDDI_VALIDATEDEVICE callback](nc-d3dumddi-pfnd3dddi-validatedevice.md) | The ValidateDevice function returns the number of passes in which the hardware can perform the blending operations that are specified in the current state. |
| [PFND3DDDI_VIDEOPROCESSBEGINFRAME callback](nc-d3dumddi-pfnd3dddi-videoprocessbeginframe.md) | The VideoProcessBeginFrame function notifies the user-mode display driver that processing of a video frame can begin on the specified Microsoft DirectX Video Accelerator (VA) video processing device. |
| [PFND3DDDI_VIDEOPROCESSBLT callback](nc-d3dumddi-pfnd3dddi-videoprocessblt.md) | The VideoProcessBlt function processes a video frame by using the specified Microsoft DirectX Video Accelerator (VA) video processing device. |
| [PFND3DDDI_VIDEOPROCESSENDFRAME callback](nc-d3dumddi-pfnd3dddi-videoprocessendframe.md) | The VideoProcessEndFrame function notifies the user-mode display driver that all of the data that is required to process the current frame was submitted. |
| [PFND3DDDI_VOLBLT callback](nc-d3dumddi-pfnd3dddi-volblt.md) | The VolBlt function performs a bit-block transfer (bitblt) operation from a source volume texture to a destination volume texture. |
| [PFND3DDDI_VOLBLT1 callback](nc-d3dumddi-pfnd3dddi-volblt1.md) | Performs a bit-block transfer (bitblt) operation from a source volume texture to a destination volume texture. Implemented by Windows Display Driver Model (WDDM) 1.2 or later user-mode display drivers. |
| [PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECT2CB callback](nc-d3dumddi-pfnd3dddi-waitforsynchronizationobject2cb.md) | Inserts a wait command for the specified synchronization objects in the specified context command stream. Used by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECTCB callback](nc-d3dumddi-pfnd3dddi-waitforsynchronizationobjectcb.md) | The pfnWaitForSynchronizationObjectCb function inserts a wait for the specified synchronization objects in the specified context DMA stream. |
| [PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPUCB callback](nc-d3dumddi-pfnd3dddi-waitforsynchronizationobjectfromcpucb.md) | pfnWaitForSynchronizationObjectFromCpuCb waits for a monitored fence to reach a certain value before processing subsequent context commands. |
| [PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMGPUCB callback](nc-d3dumddi-pfnd3dddi-waitforsynchronizationobjectfromgpucb.md) | pfnWaitForSynchronizationObjectFromGpuCb waits for a monitored fence to reach a certain value before processing subsequent context commands. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [D3D12DDICB_RECLAIMALLOCATIONS2 structure](ns-d3dumddi--d3d12ddicb-reclaimallocations2.md) | Describes video memory resources that are to be reclaimed and that the driver previously offered for reuse. |
| [D3DDDIARG_AUTHENTICATEDCHANNELKEYEXCHANGE structure](ns-d3dumddi--d3dddiarg-authenticatedchannelkeyexchange.md) | The D3DDDIARG_AUTHENTICATEDCHANNELKEYEXCHANGE structure describes a buffer that contains the session key, which the authenticated channel uses. |
| [D3DDDIARG_BLT structure](ns-d3dumddi--d3dddiarg-blt.md) | The D3DDDIARG_BLT structure describes the parameters of a bit-block transfer (bitblt). |
| [D3DDDIARG_BUFFERBLT structure](ns-d3dumddi--d3dddiarg-bufferblt.md) | The D3DDDIARG_BUFFERBLT structure describes the parameters of a buffer bit-block transfer (bitblt) operation. |
| [D3DDDIARG_BUFFERBLT1 structure](ns-d3dumddi--d3dddiarg-bufferblt1.md) | Describes the parameters of a buffer bit-block transfer (bitblt) operation. |
| [D3DDDIARG_CAPTURETOSYSMEM structure](ns-d3dumddi--d3dddiarg-capturetosysmem.md) | The D3DDDIARG_CAPTURETOSYSMEM structure describes the parameters of a bit-block transfer (bitblt) from a capture buffer to a video memory surface. |
| [D3DDDIARG_CHECKDIRECTFLIPSUPPORT structure](ns-d3dumddi--d3dddiarg-checkdirectflipsupport.md) | Specifies resources used for Direct Flip operations, in which video memory is seamlessly flipped between an application's managed primary allocations and the Desktop Window Manager's (DWM) managed primary allocations. |
| [D3DDDIARG_CHECKMULTIPLANEOVERLAYSUPPORT structure](ns-d3dumddi--d3dddiarg-checkmultiplaneoverlaysupport.md) | Used in a call to the pfnCheckMultiPlaneOverlaySupport (D3D) function to check details on hardware support for multiplane overlays. |
| [D3DDDIARG_CHECKPRESENTDURATIONSUPPORT structure](ns-d3dumddi-d3dddiarg-checkpresentdurationsupport.md) | Used in a call to the CheckPresentDurationSupport function to check details on hardware device support for seamlessly switching to a new monitor refresh rate. |
| [D3DDDIARG_CLEAR structure](ns-d3dumddi--d3dddiarg-clear.md) | The D3DDDIARG_CLEAR structure describes the parameters of a hardware-assisted clearing operation. |
| [D3DDDIARG_COLORFILL structure](ns-d3dumddi--d3dddiarg-colorfill.md) | The D3DDDIARG_COLORFILL structure describes the parameters of a color-fill operation. |
| [D3DDDIARG_COMPOSERECTS structure](ns-d3dumddi--d3dddiarg-composerects.md) | The D3DDDIARG_COMPOSERECTS structure describes the parameters that are used to compose rectangular areas. |
| [D3DDDIARG_CONFIGUREAUTHENICATEDCHANNEL structure](ns-d3dumddi--d3dddiarg-configureauthenicatedchannel.md) | The D3DDDIARG_CONFIGUREAUTHENTICATEDCHANNEL structure describes the state that is set within an authenticated channel by using the ConfigureAuthenticatedChannel function. |
| [D3DDDIARG_COPYFLAGS structure](ns-d3dumddi-d3dddiarg-copyflags.md) | Describes how to handle the existing contents of a resource during a copy or update operation of a region within that resource. Used by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [D3DDDIARG_COUNTER_INFO structure](ns-d3dumddi-d3dddiarg-counter-info.md) | Describes info to manipulate counters. |
| [D3DDDIARG_CREATEAUTHENICATEDCHANNEL structure](ns-d3dumddi--d3dddiarg-createauthenicatedchannel.md) | The D3DDDIARG_CREATEAUTHENTICATEDCHANNEL structure identifies a channel to create. |
| [D3DDDIARG_CREATECRYPTOSESSION structure](ns-d3dumddi--d3dddiarg-createcryptosession.md) | The D3DDDIARG_CREATECRYPTOSESSION structure describes an encryption session to create. |
| [D3DDDIARG_CREATEDECODEDEVICE structure](ns-d3dumddi--d3dddiarg-createdecodedevice.md) | The D3DDDIARG_CREATEDECODEDEVICE structure describes a Microsoft DirectX Video Acceleration (DirectX VA) decode device to create. |
| [D3DDDIARG_CREATEDEVICE structure](ns-d3dumddi--d3dddiarg-createdevice.md) | The D3DDDIARG_CREATEDEVICE structure contains information that describes the display device to create. |
| [D3DDDIARG_CREATEEXTENSIONDEVICE structure](ns-d3dumddi--d3dddiarg-createextensiondevice.md) | The D3DDDIARG_CREATEEXTENSIONDEVICE structure describes a Microsoft DirectX Video Acceleration (DirectX VA) extension device to create. |
| [D3DDDIARG_CREATELIGHT structure](ns-d3dumddi--d3dddiarg-createlight.md) | The D3DDDIARG_CREATELIGHT structure contains the index into the light array. |
| [D3DDDIARG_CREATEOVERLAY structure](ns-d3dumddi--d3dddiarg-createoverlay.md) | The D3DDDIARG_CREATEOVERLAY structure describes an overlay to create. |
| [D3DDDIARG_CREATEPIXELSHADER structure](ns-d3dumddi--d3dddiarg-createpixelshader.md) | The D3DDDIARG_CREATEPIXELSHADER structure specifies a shader handle to associate with pixel shader code. |
| [D3DDDIARG_CREATEQUERY structure](ns-d3dumddi--d3dddiarg-createquery.md) | The D3DDDIARG_CREATEQUERY structure identifies a query to create. |
| [D3DDDIARG_CREATEVERTEXSHADERDECL structure](ns-d3dumddi--d3dddiarg-createvertexshaderdecl.md) | The D3DDDIARG_CREATEVERTEXSHADERDECL structure specifies a shader handle to associate with the vertex shader declaration. |
| [D3DDDIARG_CREATEVERTEXSHADERFUNC structure](ns-d3dumddi--d3dddiarg-createvertexshaderfunc.md) | The D3DDDIARG_CREATEVERTEXSHADERFUNC structure specifies a shader handle to associate with vertex shader code. |
| [D3DDDIARG_CREATEVIDEOPROCESSDEVICE structure](ns-d3dumddi--d3dddiarg-createvideoprocessdevice.md) | The D3DDDIARG_CREATEVIDEOPROCESSDEVICE structure describes a Microsoft DirectX Video Acceleration (DirectX VA) video processing device to create. |
| [D3DDDIARG_CRYPTOSESSIONKEYEXCHANGE structure](ns-d3dumddi--d3dddiarg-cryptosessionkeyexchange.md) | The D3DDDIARG_CRYPTOSESSIONKEYEXCHANGE structure describes a buffer that contains the session key, which is used for encryption. |
| [D3DDDIARG_DECODEBEGINFRAME structure](ns-d3dumddi--d3dddiarg-decodebeginframe.md) | The D3DDDIARG_DECODEBEGINFRAME structure specifies the Microsoft DirectX Video Accelerator (VA) decoder that should start decoding a frame. |
| [D3DDDIARG_DECODEENDFRAME structure](ns-d3dumddi--d3dddiarg-decodeendframe.md) | The D3DDDIARG_DECODEENDFRAME structure specifies the Microsoft DirectX Video Accelerator (VA) decoder that should stop decoding a frame. |
| [D3DDDIARG_DECODEEXECUTE structure](ns-d3dumddi--d3dddiarg-decodeexecute.md) | The D3DDDIARG_DECODEEXECUTE structure describes a Microsoft DirectX Video Acceleration (VA) decode operation to perform. |
| [D3DDDIARG_DECODEEXTENSIONEXECUTE structure](ns-d3dumddi--d3dddiarg-decodeextensionexecute.md) | The D3DDDIARG_DECODEEXTENSIONEXECUTE structure describes a nonstandard Microsoft DirectX Video Acceleration (VA) decode operation to perform. |
| [D3DDDIARG_DECRYPTIONBLT structure](ns-d3dumddi--d3dddiarg-decryptionblt.md) | The D3DDDIARG_DECRYPTIONBLT structure describes the parameters of an decrypted bit-block transfer (bitblt) in a call to the DecryptionBlt function. |
| [D3DDDIARG_DEPTHFILL structure](ns-d3dumddi--d3dddiarg-depthfill.md) | The D3DDDIARG_DEPTHFILL structure describes the parameters of a depth-fill operation. |
| [D3DDDIARG_DESTROYAUTHENICATEDCHANNEL structure](ns-d3dumddi--d3dddiarg-destroyauthenicatedchannel.md) | The D3DDDIARG_DESTROYAUTHENTICATEDCHANNEL structure contains the handle to an authenticated channel that is destroyed in a call to the DestroyAuthenticatedChannel function. |
| [D3DDDIARG_DESTROYCRYPTOSESSION structure](ns-d3dumddi--d3dddiarg-destroycryptosession.md) | The D3DDDIARG_DESTROYCRYPTOSESSION structure contains the handle to an encryption session that is destroyed in a call to the DestroyCryptoSession function. |
| [D3DDDIARG_DESTROYLIGHT structure](ns-d3dumddi--d3dddiarg-destroylight.md) | The D3DDDIARG_DESTROYLIGHT structure contains the index into a light array for the light to destroy. |
| [D3DDDIARG_DESTROYOVERLAY structure](ns-d3dumddi--d3dddiarg-destroyoverlay.md) | The D3DDDIARG_DESTROYOVERLAY structure contains a handle to the overlay to disable. |
| [D3DDDIARG_DISCARD structure](ns-d3dumddi--d3dddiarg-discard.md) | Defines video display memory that can be discarded because the contents are no longer needed. |
| [D3DDDIARG_DRAWINDEXEDPRIMITIVE structure](ns-d3dumddi--d3dddiarg-drawindexedprimitive.md) | The D3DDDIARG_DRAWINDEXEDPRIMITIVE structure describes an indexed primitive to draw. |
| [D3DDDIARG_DRAWINDEXEDPRIMITIVE2 structure](ns-d3dumddi--d3dddiarg-drawindexedprimitive2.md) | The D3DDDIARG_DRAWINDEXEDPRIMITIVE2 structure describes an indexed primitive to draw. |
| [D3DDDIARG_DRAWPRIMITIVE structure](ns-d3dumddi--d3dddiarg-drawprimitive.md) | The D3DDDIARG_DRAWPRIMITIVE structure describes a nonindexed primitive to draw. |
| [D3DDDIARG_DRAWPRIMITIVE2 structure](ns-d3dumddi--d3dddiarg-drawprimitive2.md) | The D3DDDIARG_DRAWPRIMITIVE2 structure describes a nonindexed primitive to draw. |
| [D3DDDIARG_DRAWRECTPATCH structure](ns-d3dumddi--d3dddiarg-drawrectpatch.md) | The D3DDDIARG_DRAWRECTPATCH structure describes a rectangular patch to draw. |
| [D3DDDIARG_DRAWTRIPATCH structure](ns-d3dumddi--d3dddiarg-drawtripatch.md) | The D3DDDIARG_DRAWTRIPATCH structure describes a triangular patch to draw. |
| [D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR structure](ns-d3dumddi--d3dddiarg-dxvahd-createvideoprocessor.md) | The D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR structure describes a Microsoft DirectX Video Acceleration (DirectX VA) video processor to create. |
| [D3DDDIARG_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE structure](ns-d3dumddi--d3dddiarg-dxvahd-getvideoprocessbltstateprivate.md) | The D3DDDIARG_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE structure describes the private bit-block transfer (bitblt) state of the video processor to retrieve. |
| [D3DDDIARG_DXVAHD_GETVIDEOPROCESSSTREAMSTATEPRIVATE structure](ns-d3dumddi--d3dddiarg-dxvahd-getvideoprocessstreamstateprivate.md) | The D3DDDIARG_DXVAHD_GETVIDEOPROCESSSTREAMSTATEPRIVATE structure describes the private stream-state of the video processor to retrieve. |
| [D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE structure](ns-d3dumddi--d3dddiarg-dxvahd-setvideoprocessbltstate.md) | The D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE structure describes the bit-block transfer (bitblt) state of the video processor to change and the data that is used to change the state. |
| [D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE structure](ns-d3dumddi--d3dddiarg-dxvahd-setvideoprocessstreamstate.md) | The D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE structure describes the stream state of the video processor to change and the data that is used to change the state. |
| [D3DDDIARG_DXVAHD_VIDEOPROCESSBLTHD structure](ns-d3dumddi--d3dddiarg-dxvahd-videoprocessblthd.md) | The D3DDDIARG_DXVAHD_VIDEOPROCESSBLTHD structure describes a Microsoft DirectX Video Acceleration (VA) video processing high definition operation to perform. |
| [D3DDDIARG_ENCRYPTIONBLT structure](ns-d3dumddi--d3dddiarg-encryptionblt.md) | The D3DDDIARG_ENCRYPTIONBLT structure describes the parameters of an encrypted bit-block transfer (bitblt) in a call to the EncryptionBlt function. |
| [D3DDDIARG_EXTENSIONEXECUTE structure](ns-d3dumddi--d3dddiarg-extensionexecute.md) | The D3DDDIARG_EXTENSIONEXECUTE structure describes a Microsoft DirectX Video Acceleration (VA) extension operation to perform. |
| [D3DDDIARG_FINISHSESSIONKEYREFRESH structure](ns-d3dumddi--d3dddiarg-finishsessionkeyrefresh.md) | The D3DDDIARG_FINISHSESSIONKEYREFRESH structure contains the handle to an encryption session to end in a call to the FinishSessionKeyRefresh function. |
| [D3DDDIARG_FLIPOVERLAY structure](ns-d3dumddi--d3dddiarg-flipoverlay.md) | The D3DDDIARG_FLIPOVERLAY structure describes a new resource to display on a given overlay. |
| [D3DDDIARG_GENERATEMIPSUBLEVELS structure](ns-d3dumddi--d3dddiarg-generatemipsublevels.md) | The D3DDDIARG_GENERATEMIPSUBLEVELS structure describes how to generate the sublevels of a MIP-map texture. |
| [D3DDDIARG_GETCAPS structure](ns-d3dumddi--d3dddiarg-getcaps.md) | The D3DDDIARG_GETCAPS structure contains display device capabilities of a particular type. |
| [D3DDDIARG_GETCAPTUREALLOCATIONHANDLE structure](ns-d3dumddi--d3dddiarg-getcaptureallocationhandle.md) | The D3DDDIARG_GETCAPTUREALLOCATIONHANDLE structure describes the parameters for retrieving an allocation handle from a capture resource handle. |
| [D3DDDIARG_GETOVERLAYCOLORCONTROLS structure](ns-d3dumddi--d3dddiarg-getoverlaycolorcontrols.md) | The D3DDDIARG_GETOVERLAYCOLORCONTROLS structure describes the parameters for retrieving an overlay's color-control settings. |
| [D3DDDIARG_GETPITCH structure](ns-d3dumddi--d3dddiarg-getpitch.md) | The D3DDDIARG_GETPITCH structure describes an encrypted surface for which the GetPitch function retrieves the pitch. |
| [D3DDDIARG_GETQUERYDATA structure](ns-d3dumddi--d3dddiarg-getquerydata.md) | The D3DDDIARG_GETQUERYDATA structure contains query information that was retrieved from the user-mode display driver. |
| [D3DDDIARG_ISSUEQUERY structure](ns-d3dumddi--d3dddiarg-issuequery.md) | The D3DDDIARG_ISSUEQUERY structure describes how to process a query that was created by the CreateQuery function. |
| [D3DDDIARG_LOCK structure](ns-d3dumddi--d3dddiarg-lock.md) | The D3DDDIARG_LOCK structure describes a resource or a surface within the resource to lock. |
| [D3DDDIARG_LOCKASYNC structure](ns-d3dumddi--d3dddiarg-lockasync.md) | The D3DDDIARG_LOCKASYNC structure describes a resource or a surface within the resource to lock. |
| [D3DDDIARG_MULTIPLYTRANSFORM structure](ns-d3dumddi--d3dddiarg-multiplytransform.md) | The D3DDDIARG_MULTIPLYTRANSFORM structure describes how to modify the current transform. |
| [D3DDDIARG_OFFERRESOURCES structure](ns-d3dumddi--d3dddiarg-offerresources.md) | Describes video memory resources that the user-mode display driver offers for reuse. Used with the OfferResources function. |
| [D3DDDIARG_OPENADAPTER structure](ns-d3dumddi--d3dddiarg-openadapter.md) | The D3DDDIARG_OPENADAPTER structure contains information that describes the graphics adapter object. |
| [D3DDDIARG_OPENRESOURCE structure](ns-d3dumddi--d3dddiarg-openresource.md) | The D3DDDIARG_OPENRESOURCE structure contains information for opening a shared resource. |
| [D3DDDIARG_PRESENT structure](ns-d3dumddi--d3dddiarg-present.md) | The D3DDDIARG_PRESENT structure describes a resource to display. |
| [D3DDDIARG_PRESENT1 structure](ns-d3dumddi--d3dddiarg-present1.md) | Describes a resource to display. Used with the pfnPresent1(D3D) function by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [D3DDDIARG_PRESENTMULTIPLANEOVERLAY structure](ns-d3dumddi-d3dddiarg-presentmultiplaneoverlay.md) | Specifies a multiplane overlay resource to display. |
| [D3DDDIARG_PRESENTSURFACE structure](ns-d3dumddi-d3dddiarg-presentsurface.md) | Describes a surface to display. |
| [D3DDDIARG_QUERYAUTHENICATEDCHANNEL structure](ns-d3dumddi--d3dddiarg-queryauthenicatedchannel.md) | The D3DDDIARG_QUERYAUTHENTICATEDCHANNEL structure describes authenticated-channel information to query by using the QueryAuthenticatedChannel function. |
| [D3DDDIARG_QUERYRESOURCERESIDENCY structure](ns-d3dumddi--d3dddiarg-queryresourceresidency.md) | The D3DDDIARG_QUERYRESOURCERESIDENCY structure describes a list of resources on which residency is verified through the QueryResourceResidency function. |
| [D3DDDIARG_RECLAIMRESOURCES structure](ns-d3dumddi--d3dddiarg-reclaimresources.md) | Describes video memory resources that are to be reclaimed and that the user-mode display driver previously offered for reuse. Used with the ReclaimResources function. |
| [D3DDDIARG_RENAME structure](ns-d3dumddi--d3dddiarg-rename.md) | The D3DDDIARG_RENAME structure describes a resource or a surface within the resource to rename with a new allocation. |
| [D3DDDIARG_RENDERSTATE structure](ns-d3dumddi--d3dddiarg-renderstate.md) | The D3DDDIARG_RENDERSTATE structure describes how to update a specific render state. |
| [D3DDDIARG_RESOLVESHAREDRESOURCE structure](ns-d3dumddi--d3dddiarg-resolvesharedresource.md) | The D3DDDIARG_RESOLVESHAREDRESOURCE structure specifies the resource that the user-mode display driver's ResolveSharedResource function uses as a synchronized shared surface or a GDI interoperable surface. |
| [D3DDDIARG_SETCLIPPLANE structure](ns-d3dumddi--d3dddiarg-setclipplane.md) | The D3DDDIARG_SETCLIPPLANE structure describes a clip plane. |
| [D3DDDIARG_SETCONVOLUTIONKERNELMONO structure](ns-d3dumddi--d3dddiarg-setconvolutionkernelmono.md) | The D3DDDIARG_SETCONVOLUTIONKERNELMONO structure describes parameters for setting the monochrome convolution kernel. |
| [D3DDDIARG_SETDECODERENDERTARGET structure](ns-d3dumddi--d3dddiarg-setdecoderendertarget.md) | The D3DDDIARG_SETDECODERENDERTARGET structure describes the decode render target surface. |
| [D3DDDIARG_SETDEPTHSTENCIL structure](ns-d3dumddi--d3dddiarg-setdepthstencil.md) | The D3DDDIARG_SETDEPTHSTENCIL structure specifies a depth buffer. |
| [D3DDDIARG_SETDISPLAYMODE structure](ns-d3dumddi--d3dddiarg-setdisplaymode.md) | The D3DDDIARG_SETDISPLAYMODE structure describes parameters for setting the display mode. |
| [D3DDDIARG_SETINDICES structure](ns-d3dumddi--d3dddiarg-setindices.md) | The D3DDDIARG_SETINDICES structure describes parameters for setting the current index buffer. |
| [D3DDDIARG_SETLIGHT structure](ns-d3dumddi--d3dddiarg-setlight.md) | The D3DDDIARG_SETLIGHT structure describes how to set light properties. |
| [D3DDDIARG_SETMATERIAL structure](ns-d3dumddi--d3dddiarg-setmaterial.md) | The D3DDDIARG_SETMATERIAL structure describes the material properties that are used for rendering. |
| [D3DDDIARG_SETOVERLAYCOLORCONTROLS structure](ns-d3dumddi--d3dddiarg-setoverlaycolorcontrols.md) | The D3DDDIARG_SETOVERLAYCOLORCONTROLS structure describes the parameters for changing an overlay's color-control settings. |
| [D3DDDIARG_SETPALETTE structure](ns-d3dumddi--d3dddiarg-setpalette.md) | The D3DDDIARG_SETPALETTE structure describes how to associate a palette with a texture. |
| [D3DDDIARG_SETPIXELSHADERCONST structure](ns-d3dumddi--d3dddiarg-setpixelshaderconst.md) | The D3DDDIARG_SETPIXELSHADERCONST structure describes how to set the pixel shader constant registers. |
| [D3DDDIARG_SETPRIORITY structure](ns-d3dumddi--d3dddiarg-setpriority.md) | The D3DDDIARG_SETPRIORITY structure describes the priority level to set for a managed texture. |
| [D3DDDIARG_SETRENDERTARGET structure](ns-d3dumddi--d3dddiarg-setrendertarget.md) | The D3DDDIARG_SETRENDERTARGET structure describes the render target surface. |
| [D3DDDIARG_SETSTREAMSOURCE structure](ns-d3dumddi--d3dddiarg-setstreamsource.md) | The D3DDDIARG_SETSTREAMSOURCE structure describes the portion of the vertex stream to bind to a vertex buffer. |
| [D3DDDIARG_SETSTREAMSOURCEFREQ structure](ns-d3dumddi--d3dddiarg-setstreamsourcefreq.md) | The D3DDDIARG_SETSTREAMSOURCEFREQ structure describes how the frequency divisor for a portion of the vertex stream source is set. |
| [D3DDDIARG_SETSTREAMSOURCEUM structure](ns-d3dumddi--d3dddiarg-setstreamsourceum.md) | The D3DDDIARG_SETSTREAMSOURCEUM structure describes the vertex stream to bind to a user-memory buffer. |
| [D3DDDIARG_SETTRANSFORM structure](ns-d3dumddi--d3dddiarg-settransform.md) | The D3DDDIARG_SETTRANSFORM structure describes how to set up a transform. |
| [D3DDDIARG_SETVERTEXSHADERCONST structure](ns-d3dumddi--d3dddiarg-setvertexshaderconst.md) | The D3DDDIARG_SETVERTEXSHADERCONST structure describes how to set vertex shader constant registers. |
| [D3DDDIARG_SETVIDEOPROCESSRENDERTARGET structure](ns-d3dumddi--d3dddiarg-setvideoprocessrendertarget.md) | The D3DDDIARG_SETVIDEOPROCESSRENDERTARGET structure describes the render target surface for video processing. |
| [D3DDDIARG_STARTSESSIONKEYREFRESH structure](ns-d3dumddi--d3dddiarg-startsessionkeyrefresh.md) | The D3DDDIARG_STARTSESSIONKEYREFRESH structure contains information about the random number for the encryption session. |
| [D3DDDIARG_STATESET structure](ns-d3dumddi--d3dddiarg-stateset.md) | The D3DDDIARG_STATESET structure describes how to set a state block. |
| [D3DDDIARG_TEXBLT structure](ns-d3dumddi--d3dddiarg-texblt.md) | The D3DDDIARG_TEXBLT structure describes parameters for a texture bit-block transfer (bitblt) operation. |
| [D3DDDIARG_TEXBLT1 structure](ns-d3dumddi--d3dddiarg-texblt1.md) | Describes parameters for a texture bit-block transfer (bitblt) operation. |
| [D3DDDIARG_TEXTURESTAGESTATE structure](ns-d3dumddi--d3dddiarg-texturestagestate.md) | The D3DDDIARG_TEXTURESTAGESTATE structure describes how to update a texture at a particular stage in a multiple-texture group. |
| [D3DDDIARG_TRIMRESIDENCYSET structure](ns-d3dumddi-d3dddiarg-trimresidencyset.md) | D3DDDIARG_TRIMRESIDENCYSET is used with pfnTrimResidencySet by a user mode driver to trim the residency list for a given device. |
| [D3DDDIARG_UNLOCK structure](ns-d3dumddi--d3dddiarg-unlock.md) | The D3DDDIARG_UNLOCK structure describes a resource or a surface within the resource to unlock. |
| [D3DDDIARG_UNLOCKASYNC structure](ns-d3dumddi--d3dddiarg-unlockasync.md) | The D3DDDIARG_UNLOCKASYNC structure describes a resource or a surface within the resource to unlock. |
| [D3DDDIARG_UPDATEOVERLAY structure](ns-d3dumddi--d3dddiarg-updateoverlay.md) | The D3DDDIARG_UPDATEOVERLAY structure describes an overlay to modify. |
| [D3DDDIARG_UPDATEPALETTE structure](ns-d3dumddi--d3dddiarg-updatepalette.md) | The D3DDDIARG_UPDATEPALETTE structure describes parameters that are used to update a texture palette. |
| [D3DDDIARG_UPDATESUBRESOURCEUP structure](ns-d3dumddi-d3dddiarg-updatesubresourceup.md) | Describes info that's used to update a destination subresource region from a source system-memory region. Used by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [D3DDDIARG_VALIDATETEXTURESTAGESTATE structure](ns-d3dumddi--d3dddiarg-validatetexturestagestate.md) | The D3DDDIARG_VALIDATETEXTURESTAGESTATE structure contains the number of passes in which the hardware can perform the blending operations that are specified in the current state. |
| [D3DDDIARG_VIDEOPROCESSBLT structure](ns-d3dumddi--d3dddiarg-videoprocessblt.md) | The D3DDDIARG_VIDEOPROCESSBLT structure describes a Microsoft DirectX Video Acceleration (VA) video processing operation to perform. |
| [D3DDDIARG_VIDEOPROCESSENDFRAME structure](ns-d3dumddi--d3dddiarg-videoprocessendframe.md) | The D3DDDIARG_VIDEOPROCESSENDFRAME structure specifies the Microsoft DirectX Video Accelerator (VA) video process that should stop processing a frame. |
| [D3DDDIARG_VIEWPORTINFO structure](ns-d3dumddi--d3dddiarg-viewportinfo.md) | The D3DDDIARG_VIEWPORTINFO structure describes the location and size of a view-clipping rectangle. |
| [D3DDDIARG_VOLUMEBLT structure](ns-d3dumddi--d3dddiarg-volumeblt.md) | The D3DDDIARG_VOLUMEBLT structure describes parameters for a volume bit-block transfer (bitblt) operation. |
| [D3DDDIARG_VOLUMEBLT1 structure](ns-d3dumddi--d3dddiarg-volumeblt1.md) | Describes parameters for a volume bit-block transfer (bitblt) operation. |
| [D3DDDIARG_WINFO structure](ns-d3dumddi--d3dddiarg-winfo.md) | The D3DDDIARG_WINFO structure describes a w range for w buffering. |
| [D3DDDIARG_ZRANGE structure](ns-d3dumddi--d3dddiarg-zrange.md) | The D3DDDIARG_ZRANGE structure specifies z-range minimum and maximum values. |
| [D3DDDIBOX structure](ns-d3dumddi--d3dddibox.md) | Describes the bounds of a volume texture. |
| [D3DDDICAPS_ARCHITECTURE_INFO structure](ns-d3dumddi-d3dddicaps-architecture-info.md) | Describes information about display adapter architecture. |
| [D3DDDICAPS_SHADER_MIN_PRECISION_SUPPORT structure](ns-d3dumddi-d3dddicaps-shader-min-precision-support.md) | Describes precision support options for shaders in the user-mode display driver. |
| [D3DDDICAPS_SIMPLE_INSTANCING_SUPPORT structure](ns-d3dumddi-d3dddicaps-simple-instancing-support.md) | Describes whether simple instancing is supported. |
| [D3DDDICB_ALLOCATE structure](ns-d3dumddi--d3dddicb-allocate.md) | The D3DDDICB_ALLOCATE structure contains information for allocating memory. |
| [D3DDDICB_CREATECONTEXT structure](ns-d3dumddi--d3dddicb-createcontext.md) | The D3DDDICB_CREATECONTEXT structure describes a context to create. |
| [D3DDDICB_CREATECONTEXTVIRTUAL structure](ns-d3dumddi--d3dddicb-createcontextvirtual.md) | D3DDDICB_CREATECONTEXTVIRTUAL is used with pfnCreateContextVirtualCb to create contexts that support virtual addressing. |
| [D3DDDICB_CREATEHWCONTEXT structure](ns-d3dumddi--d3dddicb-createhwcontext.md) | A structure that gives information for creating a hardware context. |
| [D3DDDICB_CREATEHWQUEUE structure](ns-d3dumddi--d3dddicb-createhwqueue.md) | A structure that holds information to create a hardware queue. |
| [D3DDDICB_CREATEOVERLAY structure](ns-d3dumddi--d3dddicb-createoverlay.md) | The D3DDDICB_CREATEOVERLAY structure describes overlay hardware. |
| [D3DDDICB_CREATEPAGINGQUEUE structure](ns-d3dumddi-d3dddicb-createpagingqueue.md) | D3DDDICB_CREATEPAGINGQUEUE is used with pfnCreatePagingQueueCb to create a device paging queue that can be used to synchronize with video memory management operations for the device, such as making the device resource resident. |
| [D3DDDICB_CREATESYNCHRONIZATIONOBJECT structure](ns-d3dumddi--d3dddicb-createsynchronizationobject.md) | The D3DDDICB_CREATESYNCHRONIZATIONOBJECT structure describes a synchronization object that the pfnCreateSynchronizationObjectCb function creates. |
| [D3DDDICB_CREATESYNCHRONIZATIONOBJECT2 structure](ns-d3dumddi--d3dddicb-createsynchronizationobject2.md) | Describes a synchronization object that the pfnCreateSynchronizationObject2Cb function creates. |
| [D3DDDICB_DEALLOCATE structure](ns-d3dumddi--d3dddicb-deallocate.md) | The D3DDDICB_DEALLOCATE structure describes allocations to release. |
| [D3DDDICB_DEALLOCATE2 structure](ns-d3dumddi--d3dddicb-deallocate2.md) | The D3DDDICB_DEALLOCATE2 structure describes parameters for releasing allocations with pfnDeallocate2Cb. |
| [D3DDDICB_DESTROYCONTEXT structure](ns-d3dumddi--d3dddicb-destroycontext.md) | The D3DDDICB_DESTROYCONTEXT structure contains the handle to a context to destroy. |
| [D3DDDICB_DESTROYHWCONTEXT structure](ns-d3dumddi--d3dddicb-destroyhwcontext.md) | A structure that holds information to destroy a hardware context. |
| [D3DDDICB_DESTROYHWQUEUE structure](ns-d3dumddi--d3dddicb-destroyhwqueue.md) | A structure that holds information to destroy a hardware queue. |
| [D3DDDICB_DESTROYOVERLAY structure](ns-d3dumddi--d3dddicb-destroyoverlay.md) | The D3DDDICB_DESTROYOVERLAY structure contains the handle to the overlay to destroy. |
| [D3DDDICB_DESTROYSYNCHRONIZATIONOBJECT structure](ns-d3dumddi--d3dddicb-destroysynchronizationobject.md) | The D3DDDICB_DESTROYSYNCHRONIZATIONOBJECT structure contains the handle to a synchronization object to destroy. |
| [D3DDDICB_ESCAPE structure](ns-d3dumddi--d3dddicb-escape.md) | The D3DDDICB_ESCAPE structure describes information that a user-mode display driver shares with a display miniport driver. |
| [D3DDDICB_EVICT structure](ns-d3dumddi-d3dddicb-evict.md) | D3DKMT_EVICT is used with pfnEvictCb to subtract one from the residency reference count. |
| [D3DDDICB_FLIPOVERLAY structure](ns-d3dumddi--d3dddicb-flipoverlay.md) | The D3DDDICB_FLIPOVERLAY structure describes a new allocation to display for the overlay. |
| [D3DDDICB_FREEGPUVIRTUALADDRESS structure](ns-d3dumddi--d3dddicb-freegpuvirtualaddress.md) | D3DDDICB_FREEGPUVIRTUALADDRESS is used with pfnFreeGpuVirtualAddressCb to release a range of graphics processing unit (GPU) virtual addresses that were previously reserved or mapped. |
| [D3DDDICB_GETMULTISAMPLEMETHODLIST structure](ns-d3dumddi--d3dddicb-getmultisamplemethodlist.md) | The D3DDDICB_GETMULTISAMPLEMETHODLIST structure describes parameters to retrieve the list of multiple-sample methods for an allocation. |
| [D3DDDICB_LOCK structure](ns-d3dumddi--d3dddicb-lock.md) | The D3DDDICB_LOCK structure describes parameters for locking an allocation. |
| [D3DDDICB_LOCK2 structure](ns-d3dumddi--d3dddicb-lock2.md) | D3DDDICB_LOCK2 describes parameters for locking an allocation. |
| [D3DDDICB_LOGUMDMARKER structure](ns-d3dumddi-d3dddicb-logumdmarker.md) | Specifies info about the location of an Event Tracing for Windows (ETW) marker event that the user-mode display driver has defined. |
| [D3DDDICB_OFFERALLOCATIONS structure](ns-d3dumddi--d3dddicb-offerallocations.md) | Defines the video memory allocations that the driver offers for reuse. Used with the pfnOfferAllocationsCb function. |
| [D3DDDICB_PRESENT structure](ns-d3dumddi--d3dddicb-present.md) | The D3DDDICB_PRESENT structure describes allocations that content is copied to and from. |
| [D3DDDICB_PRESENTMULTIPLANEOVERLAY structure](ns-d3dumddi-d3dddicb-presentmultiplaneoverlay.md) | Describes multiplane overlay allocations that content is copied to and from. |
| [D3DDDICB_QUERYADAPTERINFO structure](ns-d3dumddi--d3dddicb-queryadapterinfo.md) | The D3DDDICB_QUERYADAPTERINFO structure contains information that describes the graphics adapter. |
| [D3DDDICB_QUERYRESIDENCY structure](ns-d3dumddi--d3dddicb-queryresidency.md) | The D3DDDICB_QUERYRESIDENCY structure describes the residency status of a resource or list of allocations. |
| [D3DDDICB_RECLAIMALLOCATIONS structure](ns-d3dumddi--d3dddicb-reclaimallocations.md) | Describes video memory resources that are to be reclaimed and that the user-mode display driver previously offered for reuse. Used with the pfnReclaimAllocationsCb function. |
| [D3DDDICB_RECLAIMALLOCATIONS2 structure](ns-d3dumddi--d3dddicb-reclaimallocations2.md) | D3DDDICB_RECLAIMALLOCATIONS2 is used with pfnReclaimAllocations2Cb to describe video memory resources, previously offered for reuse by the driver, that are to be reclaimed. |
| [D3DDDICB_RENDER structure](ns-d3dumddi--d3dddicb-render.md) | The D3DDDICB_RENDER structure describes the current command buffer to be rendered. |
| [D3DDDICB_RENDERFLAGS structure](ns-d3dumddi--d3dddicb-renderflags.md) | The D3DDDICB_RENDERFLAGS structure identifies information about a command buffer to be rendered. |
| [D3DDDICB_SETDISPLAYMODE structure](ns-d3dumddi--d3dddicb-setdisplaymode.md) | The D3DDDICB_SETDISPLAYMODE structure describes the primary allocation that is used to scan out to the display. |
| [D3DDDICB_SETDISPLAYPRIVATEDRIVERFORMAT structure](ns-d3dumddi--d3dddicb-setdisplayprivatedriverformat.md) | The D3DDDICB_SETDISPLAYPRIVATEDRIVERFORMAT structure describes the private-format attribute to set for a video present source in a call to the pfnSetDisplayPrivateDriverFormatCb function. |
| [D3DDDICB_SETPRIORITY structure](ns-d3dumddi--d3dddicb-setpriority.md) | The D3DDDICB_SETPRIORITY structure describes the priority level to which to set a resource or list of allocations. |
| [D3DDDICB_SIGNALSYNCHRONIZATIONOBJECT structure](ns-d3dumddi--d3dddicb-signalsynchronizationobject.md) | The D3DDDICB_SIGNALSYNCHRONIZATIONOBJECT structure describes the parameters that are required to set up signaling in a call to the pfnSignalSynchronizationObjectCb function. |
| [D3DDDICB_SIGNALSYNCHRONIZATIONOBJECT2 structure](ns-d3dumddi--d3dddicb-signalsynchronizationobject2.md) | Describes the parameters that are required to set up signaling in a call to the pfnSignalSynchronizationObject2Cb function. |
| [D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMCPU structure](ns-d3dumddi-d3dddicb-signalsynchronizationobjectfromcpu.md) | D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMCPU is used with pfnSignalSynchronizationObjectFromCpuCb to enable a driver to signal a monitored fence. |
| [D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU structure](ns-d3dumddi-d3dddicb-signalsynchronizationobjectfromgpu.md) | D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU is used with pfnSignalSynchronizationObjectFromGpuCb to signal a monitored fence. |
| [D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2 structure](ns-d3dumddi-d3dddicb-signalsynchronizationobjectfromgpu2.md) | D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2 is used with pfnSignalSynchronizationObjectFromGpu2Cb to signal a monitored fence. |
| [D3DDDICB_SUBMITCOMMAND structure](ns-d3dumddi--d3dddicb-submitcommand.md) | The D3DDDICB_SUBMITCOMMAND structure is used to submit command buffers on contexts that support graphics processing unit (GPU) virtual addressing. |
| [D3DDDICB_SUBMITCOMMANDFLAGS structure](ns-d3dumddi--d3dddicb-submitcommandflags.md) | D3DDDICB_SUBMITCOMMANDFLAGS is used to indicate how to process command buffers on contexts that support graphics processing unit (GPU) virtual addressing. |
| [D3DDDICB_SUBMITCOMMANDTOHWQUEUE structure](ns-d3dumddi--d3dddicb-submitcommandtohwqueue.md) | A structure that holds information to queue hardware flags. |
| [D3DDDICB_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE structure](ns-d3dumddi--d3dddicb-submitsignalsyncobjectstohwqueue.md) | A structure that holds information to submit a signal synchronization object to a hardware queue. |
| [D3DDDICB_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE structure](ns-d3dumddi--d3dddicb-submitwaitforsyncobjectstohwqueue.md) | A structure that holds information to wait for synchronized objects. |
| [D3DDDICB_UNLOCK structure](ns-d3dumddi--d3dddicb-unlock.md) | The D3DDDICB_UNLOCK structure describes allocations to unlock. |
| [D3DDDICB_UNLOCK2 structure](ns-d3dumddi--d3dddicb-unlock2.md) | D3DDDICB_UNLOCK2 describes an allocation to unlock. |
| [D3DDDICB_UPDATEGPUVIRTUALADDRESS structure](ns-d3dumddi--d3dddicb-updategpuvirtualaddress.md) | D3DDDICB_UPDATEGPUVIRTUALADDRESS is used with pfnUpdateGpuVirtualAddressCb to allow the user mode driver to specify a number of mapping operations to be applied to the process virtual address space in a single batch of page table updates. |
| [D3DDDICB_UPDATEOVERLAY structure](ns-d3dumddi--d3dddicb-updateoverlay.md) | The D3DDDICB_UPDATEOVERLAY structure describes parameters for modifying an overlay. |
| [D3DDDICB_WAITFORSYNCHRONIZATIONOBJECT structure](ns-d3dumddi--d3dddicb-waitforsynchronizationobject.md) | The D3DDDICB_WAITFORSYNCHRONIZATIONOBJECT structure describes the parameters that are required to set up the wait in a call to the pfnWaitForSynchronizationObjectCb function. |
| [D3DDDICB_WAITFORSYNCHRONIZATIONOBJECT2 structure](ns-d3dumddi--d3dddicb-waitforsynchronizationobject2.md) | Describes the parameters that are required to set up the wait in a call to the pfnWaitForSynchronizationObject2Cb function. |
| [D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU structure](ns-d3dumddi-d3dddicb-waitforsynchronizationobjectfromcpu.md) | D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU is used with pfnWaitForSynchronizationObjectFromCpuCb to wait for a monitored fence to reach a certain value. |
| [D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMGPU structure](ns-d3dumddi-d3dddicb-waitforsynchronizationobjectfromgpu.md) | D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMGPU is used with pfnWaitForSynchronizationObjectFromGpuCb to wait for a monitored fence to reach a certain value. |
| [D3DDDIDEVINFO_VCACHE structure](ns-d3dumddi--d3dddidevinfo-vcache.md) | The D3DDDIDEVINFO_VCACHE structure describes the vertex-cache information of a device. |
| [D3DDDIENCRYPTED_BLOCK_INFO structure](ns-d3dumddi--d3dddiencrypted-block-info.md) | The D3DDDIENCRYPTED_BLOCK_INFO structure describes the portions of a buffer that are encrypted. |
| [D3DDDIRANGE structure](ns-d3dumddi--d3dddirange.md) | Specifies a range of memory within a buffer. |
| [D3DDDIVERTEXELEMENT structure](ns-d3dumddi--d3dddivertexelement.md) | The D3DDDIVERTEXELEMENT structure describes an element in the array for a vertex shader declaration. |
| [D3DDDI_ADAPTERCALLBACKS structure](ns-d3dumddi--d3dddi-adaptercallbacks.md) | The D3DDDI_ADAPTERCALLBACKS structure contains Microsoft Direct3D runtime callback functions that the user-mode display driver can use. |
| [D3DDDI_ADAPTERFUNCS structure](ns-d3dumddi--d3dddi-adapterfuncs.md) | The D3DDDI_ADAPTERFUNCS structure contains functions that the user-mode display driver can implement to communicate with a graphics adapter object. |
| [D3DDDI_BLTFLAGS structure](ns-d3dumddi--d3dddi-bltflags.md) | The D3DDDI_BLTFLAGS structure identifies the type of bit-block transfer (bitblt) to perform. |
| [D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO structure](ns-d3dumddi-d3dddi-check-multiplane-overlay-support-plane-info.md) | Specifies the support attributes that the hardware provides for multiplane overlays. |
| [D3DDDI_COLORFILLFLAGS structure](ns-d3dumddi--d3dddi-colorfillflags.md) | The D3DDDI_COLORFILLFLAGS structure describes how to color-fill a rectangle on a surface. |
| [D3DDDI_CREATEDEVICEFLAGS structure](ns-d3dumddi--d3dddi-createdeviceflags.md) | The D3DDDI_CREATEDEVICEFLAGS structure describes how to create a device. |
| [D3DDDI_DEVICECALLBACKS structure](ns-d3dumddi--d3dddi-devicecallbacks.md) | The D3DDDI_DEVICECALLBACKS structure contains Microsoft Direct3D runtime callback functions that the user-mode display driver can use. |
| [D3DDDI_DEVICEFUNCS structure](ns-d3dumddi--d3dddi-devicefuncs.md) | The D3DDDI_DEVICEFUNCS structure contains functions that the user-mode display driver can implement to render graphics primitives and process state changes. |
| [D3DDDI_EXECUTIONSTATEESCAPE structure](ns-d3dumddi--d3dddi-executionstateescape.md) | Specifies the state of the device. |
| [D3DDDI_FLIPOVERLAYFLAGS structure](ns-d3dumddi--d3dddi-flipoverlayflags.md) | The D3DDDI_FLIPOVERLAYFLAGS structure identifies how to flip a resource on an overlay. |
| [D3DDDI_FRAMELATENCYESCAPE structure](ns-d3dumddi--d3dddi-framelatencyescape.md) | Specifies an app's maximum frame latency. |
| [D3DDDI_ISSUEQUERYFLAGS structure](ns-d3dumddi--d3dddi-issuequeryflags.md) | The D3DDDI_ISSUEQUERYFLAGS structure identifies the state of a query issue. |
| [D3DDDI_LIGHT structure](ns-d3dumddi--d3dddi-light.md) | The D3DDDI_LIGHT structure describes a set of lighting properties. |
| [D3DDDI_LOCKASYNCFLAGS structure](ns-d3dumddi--d3dddi-lockasyncflags.md) | The D3DDDI_LOCKASYNCFLAGS structure identifies how to lock a resource. |
| [D3DDDI_LOCKFLAGS structure](ns-d3dumddi--d3dddi-lockflags.md) | The D3DDDI_LOCKFLAGS structure identifies how to lock a resource. |
| [D3DDDI_MULTIPLANE_OVERLAY_ALLOCATION_INFO structure](ns-d3dumddi-d3dddi-multiplane-overlay-allocation-info.md) | Specifies info about a multiplane overlay allocation. |
| [D3DDDI_MULTIPLANE_OVERLAY_ATTRIBUTES structure](ns-d3dumddi--d3dddi-multiplane-overlay-attributes.md) | Used by the user-mode display driver to specify overlay plane attributes. |
| [D3DDDI_MULTIPLANE_OVERLAY_CAPS structure](ns-d3dumddi-d3dddi-multiplane-overlay-caps.md) | Used by the user-mode display driver to specify overlay plane capabilities. |
| [D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS structure](ns-d3dumddi-d3dddi-multiplane-overlay-group-caps.md) | Used by the user-mode display driver to specify a group of overlay plane capabilities. |
| [D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS_INPUT structure](ns-d3dumddi-d3dddi-multiplane-overlay-group-caps-input.md) | Specifies info on a multiplane overlay capability group. |
| [D3DDDI_OPENRESOURCEFLAGS structure](ns-d3dumddi--d3dddi-openresourceflags.md) | The D3DDDI_OPENRESOURCEFLAGS structure identifies the type of resource to open. |
| [D3DDDI_OVERLAYCOLORCONTROLS structure](ns-d3dumddi--d3dddi-overlaycolorcontrols.md) | The D3DDDI_OVERLAYCOLORCONTROLS structure describes color-control settings for an overlay. |
| [D3DDDI_OVERLAYCOLORCONTROLSFLAGS structure](ns-d3dumddi--d3dddi-overlaycolorcontrolsflags.md) | The D3DDDI_OVERLAYCOLORCONTROLSFLAGS structure identifies color-control settings that the overlay hardware supports. |
| [D3DDDI_OVERLAYINFO structure](ns-d3dumddi--d3dddi-overlayinfo.md) | The D3DDDI_OVERLAYINFO structure describes information about an overlay. |
| [D3DDDI_OVERLAYINFOFLAGS structure](ns-d3dumddi--d3dddi-overlayinfoflags.md) | The D3DDDI_OVERLAYINFOFLAGS structure identifies the type of overlay operation to perform. |
| [D3DDDI_PRESENTFLAGS structure](ns-d3dumddi--d3dddi-presentflags.md) | The D3DDDI_PRESENTFLAGS structure identifies how to perform a present operation. |
| [D3DDDI_PRESENT_MULTIPLANE_OVERLAY structure](ns-d3dumddi--d3dddi-present-multiplane-overlay.md) | Specifies an overlay plane to display. |
| [D3DDDI_UNLOCKASYNCFLAGS structure](ns-d3dumddi--d3dddi-unlockasyncflags.md) | The D3DDDI_UNLOCKASYNCFLAGS structure identifies how to unlock a resource. |
| [D3DDDI_UNLOCKFLAGS structure](ns-d3dumddi--d3dddi-unlockflags.md) | The D3DDDI_UNLOCKFLAGS structure identifies how to unlock a resource. |
| [DDICERTIFICATEINFO structure](ns-d3dumddi--ddicertificateinfo.md) | The DDICERTIFICATEINFO structure describes information about the certificate that the driver uses. |
| [DDICHECKOVERLAYSUPPORTINPUT structure](ns-d3dumddi--ddicheckoverlaysupportinput.md) | The DDICHECKOVERLAYSUPPORTINPUT structure describes an overlay display mode that the user-mode display driver uses to verify overlay support. |
| [DDICONTENTPROTECTIONCAPS structure](ns-d3dumddi--ddicontentprotectioncaps.md) | The DDICONTENTPROTECTIONCAPS structure describes a specific encryption and decode combination that the driver uses. |
| [DDIGAMMACAPS structure](ns-d3dumddi--ddigammacaps.md) | The DDIGAMMACAPS structure describes gamma-ramp capabilities that the user-mode display driver supports. |
| [DDIMULTISAMPLEQUALITYLEVELSDATA structure](ns-d3dumddi--ddimultisamplequalitylevelsdata.md) | The DDIMULTISAMPLEQUALITYLEVELSDATA structure describes the number of multiple-sample quality levels for a given render-target format. |
| [DDRAW_CAPS structure](ns-d3dumddi--ddraw-caps.md) | The DDRAW_CAPS structure describes general Microsoft DirectDraw capabilities that the user-mode display driver supports. |
| [DDRAW_MODE_SPECIFIC_CAPS structure](ns-d3dumddi--ddraw-mode-specific-caps.md) | The DDRAW_MODE_SPECIFIC_CAPS structure describes Microsoft DirectDraw capabilities that are specific to a particular display device (head) on the graphics card. |
| [DXVADDI_AYUVSAMPLE16 structure](ns-d3dumddi--dxvaddi-ayuvsample16.md) | The DXVADDI_AYUVSAMPLE16 structure describes 16-bit Cr, Cb, and Y color values and an associated opacity. |
| [DXVADDI_AYUVSAMPLE8 structure](ns-d3dumddi--dxvaddi-ayuvsample8.md) | The DXVADDI_AYUVSAMPLE8 structure describes 8-bit Cr, Cb, and Y color values and an associated opacity. |
| [DXVADDI_CONFIGPICTUREDECODE structure](ns-d3dumddi--dxvaddi-configpicturedecode.md) | The DXVADDI_CONFIGPICTUREDECODE structure describes the configuration for compressed picture decoding. |
| [DXVADDI_DECODEBUFFERDESC structure](ns-d3dumddi--dxvaddi-decodebufferdesc.md) | The DXVADDI_DECODEBUFFERDESC structure describes a buffer that is currently passed from the host decoder to the accelerator. |
| [DXVADDI_DECODEBUFFERINFO structure](ns-d3dumddi--dxvaddi-decodebufferinfo.md) | The DXVADDI_DECODEBUFFERINFO structure describes information about a particular type of compressed buffer that is required for a video decoding scenario. |
| [DXVADDI_DECODEINPUT structure](ns-d3dumddi--dxvaddi-decodeinput.md) | The DXVADDI_DECODEINPUT structure describes a render target format that is supported by a Microsoft DirectX Video Acceleration (DirectX VA) decode type. |
| [DXVADDI_EXTENDEDFORMAT structure](ns-d3dumddi--dxvaddi-extendedformat.md) | The DXVADDI_EXTENDEDFORMAT structure describes the extended format of the video frame. |
| [DXVADDI_FILTERVALUES structure](ns-d3dumddi--dxvaddi-filtervalues.md) | The DXVADDI_FILTERVALUES structure describes values that are related to a filter. |
| [DXVADDI_FIXED32 structure](ns-d3dumddi--dxvaddi-fixed32.md) | The DXVADDI_FIXED32 structure describes a floating-point number from a 16.16 fixed-point number. |
| [DXVADDI_FREQUENCY structure](ns-d3dumddi--dxvaddi-frequency.md) | The DXVADDI_FREQUENCY structure describes the video frame rate in Hertz (Hz). For example, NTSC TV is 60000 over 1001. |
| [DXVADDI_PRIVATEBUFFER structure](ns-d3dumddi--dxvaddi-privatebuffer.md) | The DXVADDI_PRIVATEBUFFER structure describes a private buffer that a nonstandard decoder uses to perform a decode operation. |
| [DXVADDI_PRIVATEDATA structure](ns-d3dumddi--dxvaddi-privatedata.md) | The DXVADDI_PRIVATEDATA structure describes data that is required for a particular decoder to operate. |
| [DXVADDI_PROCAMPVALUES structure](ns-d3dumddi--dxvaddi-procampvalues.md) | The DXVADDI_PROCAMPVALUES structure describes the ProcAmp control adjustment values. |
| [DXVADDI_PVP_SETKEY structure](ns-d3dumddi--dxvaddi-pvp-setkey.md) | The DXVADDI_PVP_SETKEY structure describes a key that the decode device uses to start decoding a frame. |
| [DXVADDI_QUERYEXTENSIONCAPSINPUT structure](ns-d3dumddi--dxvaddi-queryextensioncapsinput.md) | The DXVADDI_QUERYEXTENSIONCAPSINPUT structure describes a capability of an extension GUID that information is requested for. |
| [DXVADDI_QUERYFILTERPROPERTYRANGEINPUT structure](ns-d3dumddi--dxvaddi-queryfilterpropertyrangeinput.md) | The DXVADDI_QUERYFILTERPROPERTYRANGEINPUT structure describes a filter setting on a video stream that range information is requested for. |
| [DXVADDI_QUERYPROCAMPINPUT structure](ns-d3dumddi--dxvaddi-queryprocampinput.md) | The DXVADDI_QUERYPROCAMPINPUT structure describes a ProcAmp control property on a video stream that range information is requested for. |
| [DXVADDI_VALUERANGE structure](ns-d3dumddi--dxvaddi-valuerange.md) | The DXVADDI_VALUERANGE structure describes values of a property (such as, the value spread and default value). |
| [DXVADDI_VIDEODESC structure](ns-d3dumddi--dxvaddi-videodesc.md) | The DXVADDI_VIDEODESC structure describes a video stream. |
| [DXVADDI_VIDEOPROCESSBLTFLAGS structure](ns-d3dumddi--dxvaddi-videoprocessbltflags.md) | The DXVADDI_VIDEOPROCESSBLTFLAGS structure identifies changes in the current destination surface from the previous destination surface. |
| [DXVADDI_VIDEOPROCESSORCAPS structure](ns-d3dumddi--dxvaddi-videoprocessorcaps.md) | The DXVADDI_VIDEOPROCESSORCAPS structure describes the video processing capabilities of a specific deinterlace mode. |
| [DXVADDI_VIDEOPROCESSORINPUT structure](ns-d3dumddi--dxvaddi-videoprocessorinput.md) | The DXVADDI_VIDEOPROCESSORINPUT structure describes a video stream that is processed by a video processing device type. |
| [DXVADDI_VIDEOSAMPLE structure](ns-d3dumddi--dxvaddi-videosample.md) | The DXVADDI_VIDEOSAMPLE structure describes the format of a video sample that is used in a video processing operation. |
| [DXVADDI_VIDEOSAMPLEFLAGS structure](ns-d3dumddi--dxvaddi-videosampleflags.md) | The DXVADDI_VIDEOSAMPLEFLAGS structure identifies changes in the current sample frame from the previous sample frame. |
| [DXVAHDDDI_BLT_STATE_ALPHA_FILL_DATA structure](ns-d3dumddi--dxvahdddi-blt-state-alpha-fill-data.md) | The DXVAHDDDI_BLT_STATE_ALPHA_FILL_DATA structure describes data that specifies the alpha-fill mode of the output. |
| [DXVAHDDDI_BLT_STATE_BACKGROUND_COLOR_DATA structure](ns-d3dumddi--dxvahdddi-blt-state-background-color-data.md) | The DXVAHDDDI_BLT_STATE_BACKGROUND_COLOR_DATA structure describes data that specifies the background color to fill in the target rectangle of the output. |
| [DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA structure](ns-d3dumddi--dxvahdddi-blt-state-constriction-data.md) | The DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA structure describes data that specifies the down-sampling of the output. |
| [DXVAHDDDI_BLT_STATE_OUTPUT_COLOR_SPACE_DATA structure](ns-d3dumddi--dxvahdddi-blt-state-output-color-space-data.md) | The DXVAHDDDI_BLT_STATE_OUTPUT_COLOR_SPACE_DATA structure describes data that specifies the color space of the output. |
| [DXVAHDDDI_BLT_STATE_PRIVATE_DATA structure](ns-d3dumddi--dxvahdddi-blt-state-private-data.md) | The DXVAHDDDI_BLT_STATE_PRIVATE_DATA structure describes data that specifies the private bit-block transfer (bitblt) state. |
| [DXVAHDDDI_BLT_STATE_TARGET_RECT_DATA structure](ns-d3dumddi--dxvahdddi-blt-state-target-rect-data.md) | The DXVAHDDDI_BLT_STATE_TARGET_RECT_DATA structure describes data that specifies the target rectangle of the output. |
| [DXVAHDDDI_COLOR structure](ns-d3dumddi--dxvahdddi-color.md) | The DXVAHDDDI_COLOR union contains information that specifies color with either a YCbCr or RGB color structure. |
| [DXVAHDDDI_COLOR_RGBA structure](ns-d3dumddi--dxvahdddi-color-rgba.md) | The DXVAHDDDI_COLOR_RGBA structure describes color in RGB terms. |
| [DXVAHDDDI_COLOR_YCbCrA structure](ns-d3dumddi--dxvahdddi-color-ycbcra.md) | The DXVAHDDDI_COLOR_YCbCrA structure describes color in YCbCr terms. |
| [DXVAHDDDI_CONTENT_DESC structure](ns-d3dumddi--dxvahdddi-content-desc.md) | The DXVAHDDDI_CONTENT_DESC structure describes the video content that a decode device processes. |
| [DXVAHDDDI_CUSTOM_RATE_DATA structure](ns-d3dumddi--dxvahdddi-custom-rate-data.md) | The DXVAHDDDI_CUSTOM_RATE_DATA structure describes the video content that a decode device processes. |
| [DXVAHDDDI_DEVICE_DESC structure](ns-d3dumddi--dxvahdddi-device-desc.md) | The DXVAHDDDI_DEVICE_DESC structure describes a decode device. |
| [DXVAHDDDI_FILTER_RANGE_DATA structure](ns-d3dumddi--dxvahdddi-filter-range-data.md) | Describes a filter range. |
| [DXVAHDDDI_RATIONAL structure](ns-d3dumddi--dxvahdddi-rational.md) | The DXVAHDDDI_RATIONAL structure describes a fractional value that represents the vertical and horizontal frequencies of a video mode (that is, vertical sync and horizontal sync). |
| [DXVAHDDDI_STREAM_DATA structure](ns-d3dumddi--dxvahdddi-stream-data.md) | The DXVAHDDDI_STREAM_DATA structure describes an input stream that is processed. |
| [DXVAHDDDI_STREAM_STATE_ALPHA_DATA structure](ns-d3dumddi--dxvahdddi-stream-state-alpha-data.md) | The DXVAHDDDI_STREAM_STATE_ALPHA_DATA structure describes stream-state data that specifies the alpha blend level per-plane. |
| [DXVAHDDDI_STREAM_STATE_ASPECT_RATIO_DATA structure](ns-d3dumddi--dxvahdddi-stream-state-aspect-ratio-data.md) | The DXVAHDDDI_STREAM_STATE_ASPECT_RATIO_DATA structure describes stream-state data that specifies the pixel aspect ratio. |
| [DXVAHDDDI_STREAM_STATE_DESTINATION_RECT_DATA structure](ns-d3dumddi--dxvahdddi-stream-state-destination-rect-data.md) | The DXVAHDDDI_STREAM_STATE_DESTINATION_RECT_DATA structure describes stream-state data that specifies the destination rectangle. The driver scales the source rectangle within the input surface to the destination rectangle within the output surface. |
| [DXVAHDDDI_STREAM_STATE_FILTER_DATA structure](ns-d3dumddi--dxvahdddi-stream-state-filter-data.md) | The DXVAHDDDI_STREAM_STATE_FILTER_DATA structure describes stream-state data that specifies the filter level. |
| [DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA structure](ns-d3dumddi--dxvahdddi-stream-state-frame-format-data.md) | The DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA structure describes data that specifies the frame format of the input. |
| [DXVAHDDDI_STREAM_STATE_INPUT_COLOR_SPACE_DATA structure](ns-d3dumddi--dxvahdddi-stream-state-input-color-space-data.md) | The DXVAHDDDI_STREAM_STATE_INPUT_COLOR_SPACE_DATA structure describes stream-state data that specifies the color space of the input stream. |
| [DXVAHDDDI_STREAM_STATE_LUMA_KEY_DATA structure](ns-d3dumddi--dxvahdddi-stream-state-luma-key-data.md) | The DXVAHDDDI_STREAM_STATE_LUMA_KEY_DATA structure describes stream-state data that specifies the luma key of the input. The driver assumes that a pixel that has a luma value within the luma-key range is transparent. |
| [DXVAHDDDI_STREAM_STATE_OUTPUT_RATE_DATA structure](ns-d3dumddi--dxvahdddi-stream-state-output-rate-data.md) | The DXVAHDDDI_STREAM_STATE_OUTPUT_RATE_DATA structure describes stream-state data that specifies the output rate of the input stream. |
| [DXVAHDDDI_STREAM_STATE_PALETTE_DATA structure](ns-d3dumddi--dxvahdddi-stream-state-palette-data.md) | The DXVAHDDDI_STREAM_STATE_PALETTE_DATA structure describes stream-state data that specifies the palette entries of the input. |
| [DXVAHDDDI_STREAM_STATE_PRIVATE_DATA structure](ns-d3dumddi--dxvahdddi-stream-state-private-data.md) | The DXVAHDDDI_STREAM_STATE_PRIVATE_DATA structure describes stream-state data that specifies a private stream state. |
| [DXVAHDDDI_STREAM_STATE_PRIVATE_IVTC_DATA structure](ns-d3dumddi--dxvahdddi-stream-state-private-ivtc-data.md) | The DXVAHDDDI_STREAM_STATE_PRIVATE_IVTC_DATA structure describes private stream-state data that is used to query the inverse telecine statistics from the driver. |
| [DXVAHDDDI_STREAM_STATE_ROTATION_DATA structure](ns-d3dumddi--dxvahdddi-stream-state-rotation-data.md) | Describes stream-state data that specifies the clockwise rotation of the display output surface. |
| [DXVAHDDDI_STREAM_STATE_SOURCE_RECT_DATA structure](ns-d3dumddi--dxvahdddi-stream-state-source-rect-data.md) | The DXVAHDDDI_STREAM_STATE_SOURCE_RECT_DATA structure describes stream-state data that specifies the source rectangle of the input stream. |
| [DXVAHDDDI_SURFACE structure](ns-d3dumddi--dxvahdddi-surface.md) | The DXVAHDDDI_SURFACE structure describes a surface. |
| [DXVAHDDDI_VPCAPS structure](ns-d3dumddi--dxvahdddi-vpcaps.md) | Describes a video processor and its capabilities. |
| [DXVAHDDDI_VPDEVCAPS structure](ns-d3dumddi--dxvahdddi-vpdevcaps.md) | The DXVAHDDDI_VPDEVCAPS structure describes the video processor capabilities that the decode device supports. |
| [FORMATOP structure](ns-d3dumddi--formatop.md) | The FORMATOP structure describes a surface format and operations that can be performed with such a surface. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [D3DDDICAPS_SHADER_MIN_PRECISION enumeration](ne-d3dumddi-d3dddicaps-shader-min-precision.md) | Specifies minimum precision levels that the user-mode driver supports in shaders. |
| [D3DDDICAPS_TYPE enumeration](ne-d3dumddi--d3dddicaps-type.md) | The D3DDDICAPS_TYPE enumeration type contains values that identify the type of capability information that is received from a call to the driver's GetCaps function. |
| [D3DDDI_CERTIFICATETYPE enumeration](ne-d3dumddi--d3dddi-certificatetype.md) | The D3DDDI_CERTIFICATETYPE enumeration contains values that identify certificate types. |
| [D3DDDI_CHECK_DIRECT_FLIP_FLAGS enumeration](ne-d3dumddi-d3dddi-check-direct-flip-flags.md) | Used by the CheckDirectFlipFlags parameter of the CheckDirectFlipSupport function to specify seamless flipping of video memory. |
| [D3DDDI_COPY_FLAGS enumeration](ne-d3dumddi-d3dddi-copy-flags.md) | Specifies how to handle the existing contents of a resource during a copy or update operation of a region within that resource. |
| [D3DDDI_DEVICEEXECUTION_STATE enumeration](ne-d3dumddi--d3dddi-deviceexecution-state.md) | Indicates the state of the device. |
| [D3DDDI_FLUSH_FLAGS enumeration](ne-d3dumddi-d3dddi-flush-flags.md) | In calls to the pfnFlush1 function, indicates whether the driver should free as much memory as possible. Used by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [D3DDDI_MARKERLOGTYPE enumeration](ne-d3dumddi-d3dddi-markerlogtype.md) | Indicates the type of marker in the Event Tracing for Windows (ETW) log that the user-mode display driver supports. |
| [D3DDDI_MARKERTYPE enumeration](ne-d3dumddi-d3dddi-markertype.md) | Indicates the type of Event Tracing for Windows (ETW) marker event that the user-mode display driver supports. |
| [D3DDDI_MULTIPLANE_OVERLAY_BLEND enumeration](ne-d3dumddi--d3dddi-multiplane-overlay-blend.md) | Identifies a blend operation to be performed on an overlay plane. |
| [D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS enumeration](ne-d3dumddi--d3dddi-multiplane-overlay-feature-caps.md) | Identifies overlay capabilities. |
| [D3DDDI_MULTIPLANE_OVERLAY_FLAGS enumeration](ne-d3dumddi--d3dddi-multiplane-overlay-flags.md) | Identifies a flip operation to be performed on an overlay plane. |
| [D3DDDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY enumeration](ne-d3dumddi-d3dddi-multiplane-overlay-stretch-quality.md) | Identifies filtering processes that the hardware should perform when it stretches or shrinks multiplane overlay data. |
| [D3DDDI_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT enumeration](ne-d3dumddi-d3dddi-multiplane-overlay-video-frame-format.md) | Identifies the overlay plane's video frame format. Only the D3DDDI_MULIIPLANE_OVERLAY_VIDEO_FRAME_FORMAT_PROGRESSIVE value is supported. |
| [D3DDDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS enumeration](ne-d3dumddi-d3dddi-multiplane-overlay-ycbcr-flags.md) | Identifies YUV range and conversion info that describes a multiplane overlay. |
| [DDIAUTHENTICATEDCHANNELTYPE enumeration](ne-d3dumddi--ddiauthenticatedchanneltype.md) | The DDIAUTHENTICATEDCHANNELTYPE enumeration contains values that identify authenticated-channel types. |
| [DXVADDI_NOMINALRANGE enumeration](ne-d3dumddi--dxvaddi-nominalrange.md) | The DXVADDI_NOMINALRANGE enumeration type contains values that identify whether sample data includes headroom (that is, values beyond 1.0 white) and toeroom (that is, superblacks below the reference 0.0 black). |
| [DXVADDI_SAMPLEFORMAT enumeration](ne-d3dumddi--dxvaddi-sampleformat.md) | The DXVADDI_SAMPLEFORMAT enumeration type contains values that identify how a video frame is sampled. |
| [DXVADDI_VIDEOCHROMASUBSAMPLING enumeration](ne-d3dumddi--dxvaddi-videochromasubsampling.md) | The DXVADDI_VIDEOCHROMASUBSAMPLING enumeration type contains values that identify the chroma encoding scheme for Y'Cb'Cr' data. |
| [DXVADDI_VIDEOLIGHTING enumeration](ne-d3dumddi--dxvaddi-videolighting.md) | The DXVADDI_VIDEOLIGHTING enumeration type contains values that identify lighting conditions for viewing video. |
| [DXVADDI_VIDEOPRIMARIES enumeration](ne-d3dumddi--dxvaddi-videoprimaries.md) | The DXVADDI_VIDEOPRIMARIES enumeration type contains values that identify the color primaries, which state which RGB basis functions are used. |
| [DXVADDI_VIDEOTRANSFERFUNCTION enumeration](ne-d3dumddi--dxvaddi-videotransferfunction.md) | The DXVADDI_VIDEOTRANSFERFUNCTION enumeration type contains values that identify the conversion function from R'G'B' to RGB. |
| [DXVADDI_VIDEOTRANSFERMATRIX enumeration](ne-d3dumddi--dxvaddi-videotransfermatrix.md) | The DXVADDI_VIDEOTRANSFERMATRIX enumeration type contains values that identify the conversion matrix from Y'Cb'Cr' to (studio) R'G'B'. |
| [DXVAHDDDI_ALPHA_FILL_MODE enumeration](ne-d3dumddi--dxvahdddi-alpha-fill-mode.md) | The DXVAHDDDI_ALPHA_FILL_MODE enumeration contains values that identify the type of alpha fill mode to set. |
| [DXVAHDDDI_BLT_STATE enumeration](ne-d3dumddi--dxvahdddi-blt-state.md) | The DXVAHDDDI_BLT_STATE enumeration contains values that identify the bit-block transfer (bitblt) state data for a video processor. |
| [DXVAHDDDI_DEVICE_USAGE enumeration](ne-d3dumddi--dxvahdddi-device-usage.md) | The DXVAHDDDI_DEVICE_USAGE enumeration contains values that identify how the decode device plays video. |
| [DXVAHDDDI_FILTER enumeration](ne-d3dumddi--dxvahdddi-filter.md) | The DXVAHDDDI_FILTER enumeration contains values that identify the filter range, which the driver should retrieve when the driver's GetCaps function is called with the D3DDDICAPS_DXVAHD_GETVPFILTERRANGE value set. |
| [DXVAHDDDI_FRAME_FORMAT enumeration](ne-d3dumddi--dxvahdddi-frame-format.md) | The DXVAHDDDI_FRAME_FORMAT enumeration contains values that identify the frame format. |
| [DXVAHDDDI_NOMINAL_RANGE enumeration](ne-d3dumddi--dxvahdddi-nominal-range.md) | Indicates the luminance range of YUV data. |
| [DXVAHDDDI_OUTPUT_RATE enumeration](ne-d3dumddi--dxvahdddi-output-rate.md) | The DXVAHDDDI_OUTPUT_RATE enumeration contains values that identify the output rate that the driver should use. |
| [DXVAHDDDI_ROTATION enumeration](ne-d3dumddi--dxvahdddi-rotation.md) | Specifies the clockwise rotation of the display output surface. |
| [DXVAHDDDI_STREAM_STATE enumeration](ne-d3dumddi--dxvahdddi-stream-state.md) | The DXVAHDDDI_STREAM_STATE enumeration contains values that identify the stream-state data for a video processor. |
