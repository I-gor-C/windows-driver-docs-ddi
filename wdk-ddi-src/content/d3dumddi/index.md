---
UID: NA:d3dumddi
ms.assetid: 64c7511b-6379-3c2f-bd00-f08eab970dc2
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# d3dumddi.h header



d3dumddi.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [PFND3DDDI_ALLOCATECB](nc-d3dumddi-pfnd3dddi_allocatecb.md) | The pfnAllocateCb function allocates system or video memory. |
| [PFND3DDDI_AUTHENTICATEDCHANNELKEYEXCHANGE](nc-d3dumddi-pfnd3dddi_authenticatedchannelkeyexchange.md) | The AuthenticatedChannelKeyExchange function negotiates the session key. |
| [PFND3DDDI_BLT](nc-d3dumddi-pfnd3dddi_blt.md) | The Blt function copies the contents of a source surface to a destination surface. |
| [PFND3DDDI_BUFBLT](nc-d3dumddi-pfnd3dddi_bufblt.md) | The BufBlt function performs a bit-block transfer (bitblt) operation from a source vertex or index buffer to a destination vertex or index buffer. |
| [PFND3DDDI_BUFBLT1](nc-d3dumddi-pfnd3dddi_bufblt1.md) | Performs a bit-block transfer (bitblt) operation from a source vertex or index buffer to a destination vertex or index buffer. Implemented by Windows Display Driver Model (WDDM) 1.2 or later user-mode display drivers. |
| [PFND3DDDI_CAPTURETOSYSMEM](nc-d3dumddi-pfnd3dddi_capturetosysmem.md) | The CaptureToSysMem function copies the contents of a capture buffer to a destination surface. |
| [PFND3DDDI_CHECKCOUNTER](nc-d3dumddi-pfnd3dddi_checkcounter.md) | Called by the Microsoft Direct3D runtime to retrieve info that describes a counter. Must be implemented by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [PFND3DDDI_CHECKCOUNTERINFO](nc-d3dumddi-pfnd3dddi_checkcounterinfo.md) | Called by the Microsoft Direct3D runtime to determine global information that's related to manipulating counters. Must be implemented by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [PFND3DDDI_CHECKDIRECTFLIPSUPPORT](nc-d3dumddi-pfnd3dddi_checkdirectflipsupport.md) | Called by the Desktop Window Manager (DWM) to verify that the user-mode driver supports Direct Flip operations, in which video memory is seamlessly flipped between an application's managed primary allocations and the DWM's managed primary allocations. |
| [PFND3DDDI_CHECKMULTIPLANEOVERLAYSUPPORT](nc-d3dumddi-pfnd3dddi_checkmultiplaneoverlaysupport.md) | Called by the Microsoft Direct3D runtime to check the details on hardware support for multiplane overlays. |
| [PFND3DDDI_CHECKPRESENTDURATIONSUPPORT](nc-d3dumddi-pfnd3dddi_checkpresentdurationsupport.md) | Called by the Microsoft Direct3D runtime to request that the user-mode display driver get hardware device capabilities for seamlessly switching to a new monitor refresh rate. |
| [PFND3DDDI_CLEAR](nc-d3dumddi-pfnd3dddi_clear.md) | The Clear function performs hardware-assisted clearing on the rendering target, depth buffer, or stencil buffer. |
| [PFND3DDDI_CLOSEADAPTER](nc-d3dumddi-pfnd3dddi_closeadapter.md) | The CloseAdapter function releases resources for a graphics adapter object. |
| [PFND3DDDI_COLORFILL](nc-d3dumddi-pfnd3dddi_colorfill.md) | The ColorFill function fills a rectangle on the surface with a particular color. |
| [PFND3DDDI_COMPOSERECTS](nc-d3dumddi-pfnd3dddi_composerects.md) | The ComposeRects function composes two-dimensional areas from a source surface to a destination surface. |
| [PFND3DDDI_CONFIGUREAUTHENICATEDCHANNEL](nc-d3dumddi-pfnd3dddi_configureauthenicatedchannel.md) | The ConfigureAuthenticatedChannel function sets state within an authenticated channel. |
| [PFND3DDDI_CREATEAUTHENTICATEDCHANNEL](nc-d3dumddi-pfnd3dddi_createauthenticatedchannel.md) | The CreateAuthenticatedChannel function creates a channel that the Microsoft Direct3D runtime and the driver can use to set and query protections. |
| [PFND3DDDI_CREATECONTEXTVIRTUALCB](nc-d3dumddi-pfnd3dddi_createcontextvirtualcb.md) | pfnCreateContextVirtualCb should be used with contexts that support virtual addressing. |
| [PFND3DDDI_CREATECRYPTOSESSION](nc-d3dumddi-pfnd3dddi_createcryptosession.md) | The CreateCryptoSession function creates a crypto session that the Direct3D runtime uses to manage a session key and to perform crypto operations into and out of protected memory. |
| [PFND3DDDI_CREATEDECODEDEVICE](nc-d3dumddi-pfnd3dddi_createdecodedevice.md) | The CreateDecodeDevice function creates a Microsoft DirectX Video Acceleration (DirectX VA) decode device that is used to decode video. |
| [PFND3DDDI_CREATEDEVICE](nc-d3dumddi-pfnd3dddi_createdevice.md) | The CreateDevice function creates a graphics context that is referenced in subsequent calls. |
| [PFND3DDDI_CREATEEXTENSIONDEVICE](nc-d3dumddi-pfnd3dddi_createextensiondevice.md) | The CreateExtensionDevice function creates a Microsoft DirectX Video Acceleration (DirectX VA) extension device. |
| [PFND3DDDI_CREATEHWCONTEXTCB](nc-d3dumddi-pfnd3dddi_createhwcontextcb.md) | A callback to create a new hardware context. |
| [PFND3DDDI_CREATEHWQUEUECB](nc-d3dumddi-pfnd3dddi_createhwqueuecb.md) | A callback to create a new hardware queue. |
| [PFND3DDDI_CREATELIGHT](nc-d3dumddi-pfnd3dddi_createlight.md) | The CreateLight function creates a light source. |
| [PFND3DDDI_CREATEOVERLAY](nc-d3dumddi-pfnd3dddi_createoverlay.md) | The CreateOverlay function allocates overlay hardware and makes the overlay visible. |
| [PFND3DDDI_CREATEOVERLAYCB](nc-d3dumddi-pfnd3dddi_createoverlaycb.md) | The pfnCreateOverlayCb function creates a kernel-mode overlay object and calls the display miniport driver to display the overlay. |
| [PFND3DDDI_CREATEPAGINGQUEUECB](nc-d3dumddi-pfnd3dddi_createpagingqueuecb.md) | pfnCreatePagingQueueCb is used to create a device paging queue that can be used to synchronize with video memory management operations for the device, such as making the device resource resident. |
| [PFND3DDDI_CREATEPIXELSHADER](nc-d3dumddi-pfnd3dddi_createpixelshader.md) | The CreatePixelShader function converts pixel shader code into a hardware-specific format and associates this code with a shader handle. |
| [PFND3DDDI_CREATEQUERY](nc-d3dumddi-pfnd3dddi_createquery.md) | The CreateQuery function creates driver-side resources for a query that the Microsoft Direct3D runtime subsequently issues for processing. |
| [PFND3DDDI_CREATERESOURCE](nc-d3dumddi-pfnd3dddi_createresource.md) | The CreateResource function creates a resource. |
| [PFND3DDDI_CREATERESOURCE2](nc-d3dumddi-pfnd3dddi_createresource2.md) | Creates a resource. Implemented by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [PFND3DDDI_CREATESYNCHRONIZATIONOBJECT2CB](nc-d3dumddi-pfnd3dddi_createsynchronizationobject2cb.md) | Creates a GPU synchronization object that a device context can signal and wait for. Used by WDDM 1.2 and later user-mode display drivers. |
| [PFND3DDDI_CREATESYNCHRONIZATIONOBJECTCB](nc-d3dumddi-pfnd3dddi_createsynchronizationobjectcb.md) | The pfnCreateSynchronizationObjectCb function creates a synchronization object that a device context can signal and wait for. |
| [PFND3DDDI_CREATEVERTEXSHADERDECL](nc-d3dumddi-pfnd3dddi_createvertexshaderdecl.md) | The CreateVertexShaderDecl function converts the vertex shader declaration into a hardware-specific format and associates the declaration with a shader handle. |
| [PFND3DDDI_CREATEVERTEXSHADERFUNC](nc-d3dumddi-pfnd3dddi_createvertexshaderfunc.md) | The CreateVertexShaderFunc function converts vertex shader code into a hardware-specific format and associates the code with a shader handle. |
| [PFND3DDDI_CREATEVIDEOPROCESSDEVICE](nc-d3dumddi-pfnd3dddi_createvideoprocessdevice.md) | The CreateVideoProcessDevice function creates a Microsoft DirectX Video Acceleration (DirectX VA) video processing device that is used to process video (for example, to deinterlace the video and adjust ProcAmp properties of the video). |
| [PFND3DDDI_CRYPTOSESSIONKEYEXCHANGE](nc-d3dumddi-pfnd3dddi_cryptosessionkeyexchange.md) | The CryptoSessionKeyExchange function negotiates a session key. |
| [PFND3DDDI_DEALLOCATE2CB](nc-d3dumddi-pfnd3dddi_deallocate2cb.md) | The pfnDeallocate2Cb user mode callback function releases allocations for a kernel-mode resource object if the resource object was created. |
| [PFND3DDDI_DEALLOCATECB](nc-d3dumddi-pfnd3dddi_deallocatecb.md) | The pfnDeallocateCb callback function releases allocations or a kernel-mode resource object if the resource object was created. |
| [PFND3DDDI_DECODEBEGINFRAME](nc-d3dumddi-pfnd3dddi_decodebeginframe.md) | The DecodeBeginFrame function notifies the user-mode display driver that decoding can begin on the specified Microsoft DirectX Video Accelerator (VA) decode device. |
| [PFND3DDDI_DECODEENDFRAME](nc-d3dumddi-pfnd3dddi_decodeendframe.md) | The DecodeEndFrame function notifies the user-mode display driver that all of the data that was required to decode the current frame was submitted. |
| [PFND3DDDI_DECODEEXECUTE](nc-d3dumddi-pfnd3dddi_decodeexecute.md) | The DecodeExecute function performs a decode operation by using the given Microsoft DirectX Video Accelerator (VA) decode device. |
| [PFND3DDDI_DECODEEXTENSIONEXECUTE](nc-d3dumddi-pfnd3dddi_decodeextensionexecute.md) | The DecodeExtensionExecute function performs a decode operation by using the given Microsoft DirectX Video Accelerator (VA) nonstandard decode device. |
| [PFND3DDDI_DECRYPTIONBLT](nc-d3dumddi-pfnd3dddi_decryptionblt.md) | The DecryptionBlt function writes data to a protected surface. |
| [PFND3DDDI_DELETEPIXELSHADER](nc-d3dumddi-pfnd3dddi_deletepixelshader.md) | The DeletePixelShader function cleans up driver-side resources that are associated with pixel shader code. |
| [PFND3DDDI_DELETEVERTEXSHADERDECL](nc-d3dumddi-pfnd3dddi_deletevertexshaderdecl.md) | The DeleteVertexShaderDecl function cleans up driver-side resources that are associated with the vertex shader declaration. |
| [PFND3DDDI_DELETEVERTEXSHADERFUNC](nc-d3dumddi-pfnd3dddi_deletevertexshaderfunc.md) | The DeleteVertexShaderFunc function cleans up driver-side resources that are associated with vertex shader code. |
| [PFND3DDDI_DEPTHFILL](nc-d3dumddi-pfnd3dddi_depthfill.md) | The DepthFill function fills a depth buffer with a pixel value that is specified in native format. |
| [PFND3DDDI_DESTROYAUTHENTICATEDCHANNEL](nc-d3dumddi-pfnd3dddi_destroyauthenticatedchannel.md) | The DestroyAuthenticatedChannel function releases resources for the authenticated channel that the CreateAuthenticatedChannel function creates. |
| [PFND3DDDI_DESTROYCONTEXTCB](nc-d3dumddi-pfnd3dddi_destroycontextcb.md) | The pfnDestroyContextCb function destroys the context that was created through a call to the pfnCreateContextCb function. |
| [PFND3DDDI_DESTROYCRYPTOSESSION](nc-d3dumddi-pfnd3dddi_destroycryptosession.md) | The DestroyCryptoSession function releases resources for the encryption session that the CreateCryptoSession function creates. |
| [PFND3DDDI_DESTROYDECODEDEVICE](nc-d3dumddi-pfnd3dddi_destroydecodedevice.md) | The DestroyDecodeDevice function releases resources for a Microsoft DirectX Video Acceleration (VA) decode device. |
| [PFND3DDDI_DESTROYDEVICE](nc-d3dumddi-pfnd3dddi_destroydevice.md) | The DestroyDevice function destroys a graphics context. |
| [PFND3DDDI_DESTROYEXTENSIONDEVICE](nc-d3dumddi-pfnd3dddi_destroyextensiondevice.md) | The DestroyExtensionDevice function releases resources for a Microsoft DirectX Video Acceleration (VA) extension device. |
| [PFND3DDDI_DESTROYHWCONTEXTCB](nc-d3dumddi-pfnd3dddi_destroyhwcontextcb.md) | A callback to destroy a hardware context. |
| [PFND3DDDI_DESTROYHWQUEUECB](nc-d3dumddi-pfnd3dddi_destroyhwqueuecb.md) | A callback to destroy a hardware queue. |
| [PFND3DDDI_DESTROYLIGHT](nc-d3dumddi-pfnd3dddi_destroylight.md) | The DestroyLight function deactivates a light source. |
| [PFND3DDDI_DESTROYOVERLAY](nc-d3dumddi-pfnd3dddi_destroyoverlay.md) | The DestroyOverlay function disables the overlay hardware and frees the overlay handle. |
| [PFND3DDDI_DESTROYOVERLAYCB](nc-d3dumddi-pfnd3dddi_destroyoverlaycb.md) | The pfnDestroyOverlayCb function disables the overlay hardware and destroys the kernel-mode overlay object. |
| [PFND3DDDI_DESTROYPAGINGQUEUECB](nc-d3dumddi-pfnd3dddi_destroypagingqueuecb.md) | pfnDestroyPagingQueueCb waits for a paging queue to finish all operations queued to it and destroys it along with the associated sync object. |
| [PFND3DDDI_DESTROYQUERY](nc-d3dumddi-pfnd3dddi_destroyquery.md) | The DestroyQuery function releases resources for a query. |
| [PFND3DDDI_DESTROYRESOURCE](nc-d3dumddi-pfnd3dddi_destroyresource.md) | The DestroyResource function releases a specified resource. |
| [PFND3DDDI_DESTROYSYNCHRONIZATIONOBJECTCB](nc-d3dumddi-pfnd3dddi_destroysynchronizationobjectcb.md) | The pfnDestroySynchronizationObjectCb function destroys the synchronization object that was created through a call to the pfnCreateSynchronizationObjectCb function. |
| [PFND3DDDI_DESTROYVIDEOPROCESSDEVICE](nc-d3dumddi-pfnd3dddi_destroyvideoprocessdevice.md) | The DestroyVideoProcessDevice function releases resources for a Microsoft DirectX Video Acceleration (VA) video processing device. |
| [PFND3DDDI_DISCARD](nc-d3dumddi-pfnd3dddi_discard.md) | Discards (evicts) a set of subresources from video display memory. Implemented by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [PFND3DDDI_DRAWINDEXEDPRIMITIVE](nc-d3dumddi-pfnd3dddi_drawindexedprimitive.md) | The DrawIndexedPrimitive function draws indexed primitives that the Microsoft Direct3D runtime has not transformed the index data in. |
| [PFND3DDDI_DRAWINDEXEDPRIMITIVE2](nc-d3dumddi-pfnd3dddi_drawindexedprimitive2.md) | The DrawIndexedPrimitive2 function draws indexed primitives that the Microsoft Direct3D runtime has transformed the index data in. |
| [PFND3DDDI_DRAWPRIMITIVE](nc-d3dumddi-pfnd3dddi_drawprimitive.md) | The DrawPrimitive function draws nonindexed primitives in which the Microsoft Direct3D runtime has not transformed the vertex data. |
| [PFND3DDDI_DRAWPRIMITIVE2](nc-d3dumddi-pfnd3dddi_drawprimitive2.md) | The DrawPrimitive2 function draws nonindexed primitives in which the Microsoft Direct3D runtime has transformed the vertex data. |
| [PFND3DDDI_DRAWRECTPATCH](nc-d3dumddi-pfnd3dddi_drawrectpatch.md) | The DrawRectPatch function draws a new or cached rectangular patch or updates the specification of a previously defined patch. |
| [PFND3DDDI_DRAWTRIPATCH](nc-d3dumddi-pfnd3dddi_drawtripatch.md) | The DrawTriPatch function draws a new or cached triangular patch or updates the specification of a previously defined patch. |
| [PFND3DDDI_DXVAHD_CREATEVIDEOPROCESSOR](nc-d3dumddi-pfnd3dddi_dxvahd_createvideoprocessor.md) | The CreateVideoProcessor function creates a Microsoft DirectX Video Acceleration (DirectX VA) video processor that is used to process high-definition video. |
| [PFND3DDDI_DXVAHD_DESTROYVIDEOPROCESSOR](nc-d3dumddi-pfnd3dddi_dxvahd_destroyvideoprocessor.md) | The DestroyVideoProcessor function releases resources for a Microsoft DirectX Video Acceleration (VA) video processor. |
| [PFND3DDDI_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE](nc-d3dumddi-pfnd3dddi_dxvahd_getvideoprocessbltstateprivate.md) | The GetVideoProcessBltStatePrivate function retrieves the state data of a private bit-block transfer (bitblt) for a video processor. |
| [PFND3DDDI_DXVAHD_GETVIDEOPROCESSSTREAMSTATEPRIVATE](nc-d3dumddi-pfnd3dddi_dxvahd_getvideoprocessstreamstateprivate.md) | The GetVideoProcessStreamStatePrivate function retrieves the private stream-state data for a video processor. |
| [PFND3DDDI_DXVAHD_SETVIDEOPROCESSBLTSTATE](nc-d3dumddi-pfnd3dddi_dxvahd_setvideoprocessbltstate.md) | The SetVideoProcessBltState function sets the state of a bit-block transfer (bitblt) for a video processor. |
| [PFND3DDDI_DXVAHD_SETVIDEOPROCESSSTREAMSTATE](nc-d3dumddi-pfnd3dddi_dxvahd_setvideoprocessstreamstate.md) | The SetVideoProcessStreamState function sets the stream state for a video processor. |
| [PFND3DDDI_DXVAHD_VIDEOPROCESSBLTHD](nc-d3dumddi-pfnd3dddi_dxvahd_videoprocessblthd.md) | The VideoProcessBltHD function processes video input streams and composes to an output surface. |
| [PFND3DDDI_ENCRYPTIONBLT](nc-d3dumddi-pfnd3dddi_encryptionblt.md) | The EncryptionBlt function reads encrypted data from a protected surface. |
| [PFND3DDDI_ESCAPECB](nc-d3dumddi-pfnd3dddi_escapecb.md) | The pfnEscapeCb callback function shares information with the display miniport driver. |
| [PFND3DDDI_EVICTCB](nc-d3dumddi-pfnd3dddi_evictcb.md) | pfnEvictCb is used to instruct the OS to decrement the residency reference count. Once this count reaches zero, it will remove the allocation from the device residency list. |
| [PFND3DDDI_EXTENSIONEXECUTE](nc-d3dumddi-pfnd3dddi_extensionexecute.md) | The ExtensionExecute function performs an operation by using the given Microsoft DirectX Video Accelerator (VA) extension device. |
| [PFND3DDDI_FINISHSESSIONKEYREFRESH](nc-d3dumddi-pfnd3dddi_finishsessionkeyrefresh.md) | The FinishSessionKeyRefresh function indicates that all buffers from that point in time use the updated session key value. |
| [PFND3DDDI_FLIPOVERLAY](nc-d3dumddi-pfnd3dddi_flipoverlay.md) | The FlipOverlay function causes the overlay hardware to start displaying the given new allocation. |
| [PFND3DDDI_FLIPOVERLAYCB](nc-d3dumddi-pfnd3dddi_flipoverlaycb.md) | The pfnFlipOverlayCb function changes the allocation to display on the overlay or indicates to display the other field of the currently displaying allocation, when deinterlacing an interleaved resource. |
| [PFND3DDDI_FLUSH](nc-d3dumddi-pfnd3dddi_flush.md) | The Flush function submits outstanding hardware commands that are in the hardware command buffer to the display miniport driver. |
| [PFND3DDDI_FLUSH1](nc-d3dumddi-pfnd3dddi_flush1.md) | Called by the Microsoft Direct3D runtime to submit outstanding hardware commands that are in the hardware command buffer to the display miniport driver. Must be implemented by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [PFND3DDDI_FREEGPUVIRTUALADDRESSCB](nc-d3dumddi-pfnd3dddi_freegpuvirtualaddresscb.md) | pfnFreeGpuVirtualAddressCb releases a range of graphics processing unit (GPU) virtual addresses that was previously reserved or mapped. |
| [PFND3DDDI_GENERATEMIPSUBLEVELS](nc-d3dumddi-pfnd3dddi_generatemipsublevels.md) | The GenerateMipSubLevels function regenerates the sublevels of a MIP-map texture. |
| [PFND3DDDI_GETCAPS](nc-d3dumddi-pfnd3dddi_getcaps.md) | The GetCaps function queries for capabilities of the graphics adapter. |
| [PFND3DDDI_GETCAPTUREALLOCATIONHANDLE](nc-d3dumddi-pfnd3dddi_getcaptureallocationhandle.md) | The GetCaptureAllocationHandle function maps the given capture resource handle to a kernel-mode allocation handle. |
| [PFND3DDDI_GETENCRYPTIONBLTKEY](nc-d3dumddi-pfnd3dddi_getencryptionbltkey.md) | The GetEncryptionBltKey function returns the key that is used to decrypt the data that the driver's EncryptionBlt function returns. |
| [PFND3DDDI_GETINFO](nc-d3dumddi-pfnd3dddi_getinfo.md) | The GetInfo function retrieves information about the specified display device. |
| [PFND3DDDI_GETMULTISAMPLEMETHODLISTCB](nc-d3dumddi-pfnd3dddi_getmultisamplemethodlistcb.md) | The pfnGetMultisampleMethodListCb function retrieves a list of multiple-sample methods that are used for the given width, height, and format of an allocation. |
| [PFND3DDDI_GETOVERLAYCOLORCONTROLS](nc-d3dumddi-pfnd3dddi_getoverlaycolorcontrols.md) | The GetOverlayColorControls function retrieves color-control settings for the given overlay. |
| [PFND3DDDI_GETPITCH](nc-d3dumddi-pfnd3dddi_getpitch.md) | The GetPitch function retrieves the pitch of a protected or non-lockable surface. |
| [PFND3DDDI_GETQUERYDATA](nc-d3dumddi-pfnd3dddi_getquerydata.md) | The GetQueryData function retrieves information about a query. |
| [PFND3DDDI_GETRESOURCEPRESENTPRIVATEDRIVERDATACB](nc-d3dumddi-pfnd3dddi_getresourcepresentprivatedriverdatacb.md) | pfnGetResourcePresentPrivateDriverDataCb is used to query the resource private data, which is associated with the resource during Present. |
| [PFND3DDDI_ISSUEQUERY](nc-d3dumddi-pfnd3dddi_issuequery.md) | The IssueQuery function processes a query. |
| [PFND3DDDI_LOCK](nc-d3dumddi-pfnd3dddi_lock.md) | The Lock function locks the given resource or a surface within the resource. |
| [PFND3DDDI_LOCK2CB](nc-d3dumddi-pfnd3dddi_lock2cb.md) | The pfnLock2Cb function locks an allocation and obtains a pointer to the allocation from the display miniport driver or video memory manager. |
| [PFND3DDDI_LOCKASYNC](nc-d3dumddi-pfnd3dddi_lockasync.md) | The LockAsync function locks the specified resource or a surface within the resource. |
| [PFND3DDDI_LOCKCB](nc-d3dumddi-pfnd3dddi_lockcb.md) | The pfnLockCb function locks an allocation and obtains a pointer to the allocation from the display miniport driver or video memory manager. |
| [PFND3DDDI_LOGSTRINGTABLE](nc-d3dumddi-pfnd3dddi_logstringtable.md) | Called by the Microsoft Direct3D runtime to request that the user-mode display driver log a custom Event Tracing for Windows (ETW) marker event. Optionally implemented by Windows Display Driver Model (WDDM) 1.3 and later drivers. |
| [PFND3DDDI_LOGUMDMARKERCB](nc-d3dumddi-pfnd3dddi_logumdmarkercb.md) | Called by the user-mode display driver to log a custom Event Tracing for Windows (ETW) marker event. |
| [PFND3DDDI_MAKERESIDENTCB](nc-d3dumddi-pfnd3dddi_makeresidentcb.md) | pfnMakeResidentCb is used to instruct the OS to add a resource to the device residency list and increment the residency reference count on this allocation. |
| [PFND3DDDI_MAPGPUVIRTUALADDRESSCB](nc-d3dumddi-pfnd3dddi_mapgpuvirtualaddresscb.md) | pfnMapGpuVirtualAddressCb maps graphics processing unit (GPU) virtual address ranges to a specific allocation range or puts it to the Invalid or Zero state. |
| [PFND3DDDI_MULTIPLYTRANSFORM](nc-d3dumddi-pfnd3dddi_multiplytransform.md) | The MultiplyTransform function modifies the current transform. |
| [PFND3DDDI_OFFERALLOCATIONS2CB](nc-d3dumddi-pfnd3dddi_offerallocations2cb.md) | Called by the user-mode display driver to offer video memory allocations for reuse. |
| [PFND3DDDI_OFFERALLOCATIONSCB](nc-d3dumddi-pfnd3dddi_offerallocationscb.md) | Called by the user-mode display driver to offer video memory allocations for reuse. |
| [PFND3DDDI_OFFERRESOURCES](nc-d3dumddi-pfnd3dddi_offerresources.md) | Called by the Microsoft Direct3D runtime to request that the user-mode display driver offer video memory resources for reuse. |
| [PFND3DDDI_OPENADAPTER](nc-d3dumddi-pfnd3dddi_openadapter.md) | The OpenAdapter function creates a graphics adapter object that is referenced in subsequent calls. |
| [PFND3DDDI_OPENRESOURCE](nc-d3dumddi-pfnd3dddi_openresource.md) | The OpenResource function informs the driver that a shared resource is opened. |
| [PFND3DDDI_PRESENT](nc-d3dumddi-pfnd3dddi_present.md) | The Present function notifies the user-mode display driver that an application finished rendering and requests that the driver display the source surface by either copying or flipping or that the driver perform a color-fill operation. |
| [PFND3DDDI_PRESENT1](nc-d3dumddi-pfnd3dddi_present1.md) | Notifies the user-mode display driver that an application finished rendering and that all ownership of the shared resource is released, and requests that the driver display to the destination surface. |
| [PFND3DDDI_PRESENTCB](nc-d3dumddi-pfnd3dddi_presentcb.md) | The pfnPresentCb function copies content from a source allocation. |
| [PFND3DDDI_PRESENTMULTIPLANEOVERLAY](nc-d3dumddi-pfnd3dddi_presentmultiplaneoverlay.md) | Called by the Microsoft Direct3D runtime to notify the user-mode display driver that an application finished rendering and requests that the driver display the source surface by either copying or flipping or that the driver perform a color-fill operation. Must be implemented by Windows Display Driver Model (WDDM) 1.3 or later drivers that support multiplane overlays. |
| [PFND3DDDI_PRESENTMULTIPLANEOVERLAYCB](nc-d3dumddi-pfnd3dddi_presentmultiplaneoverlaycb.md) | Copies content from a source multiplane overlay allocation to a destination allocation. Can be called by Windows Display Driver Model (WDDM) 1.3 or later user-mode display drivers. |
| [PFND3DDDI_QUERYADAPTERINFOCB](nc-d3dumddi-pfnd3dddi_queryadapterinfocb.md) | The pfnQueryAdapterInfoCb function retrieves graphics adapter information. |
| [PFND3DDDI_QUERYAUTHENTICATEDCHANNEL](nc-d3dumddi-pfnd3dddi_queryauthenticatedchannel.md) | The QueryAuthenticatedChannel function queries an authenticated channel for capability and state information. |
| [PFND3DDDI_QUERYDLISTFORAPPLICATION1](nc-d3dumddi-pfnd3dddi_querydlistforapplication1.md) | Called during Microsoft Direct3D initialization on a hybrid system to determine which GPU an application should run on. A dList is a list of applications that need cross-adapter shared surfaces for high-performance rendering on the discrete GPU. |
| [PFND3DDDI_QUERYRESIDENCYCB](nc-d3dumddi-pfnd3dddi_queryresidencycb.md) | The pfnQueryResidencyCb function queries the residency status of a resource or list of allocations. |
| [PFND3DDDI_QUERYRESOURCERESIDENCY](nc-d3dumddi-pfnd3dddi_queryresourceresidency.md) | The QueryResourceResidency function determines the residency of the given list of resources. |
| [PFND3DDDI_RECLAIMALLOCATIONS2CB](nc-d3dumddi-pfnd3dddi_reclaimallocations2cb.md) | pfnReclaimAllocations2Cb is called by the user mode driver to reclaim video memory allocations that were previously offered for reuse. |
| [PFND3DDDI_RECLAIMALLOCATIONS3CB](nc-d3dumddi-pfnd3dddi_reclaimallocations3cb.md) | pfnReclaimAllocations3Cb is called by the user mode driver to reclaim video memory allocations that were previously offered for reuse. |
| [PFND3DDDI_RECLAIMALLOCATIONSCB](nc-d3dumddi-pfnd3dddi_reclaimallocationscb.md) | Called by the user-mode display driver to reclaim video memory allocations that were previously offered for reuse. |
| [PFND3DDDI_RECLAIMRESOURCES](nc-d3dumddi-pfnd3dddi_reclaimresources.md) | Called by the Microsoft Direct3D runtime to reclaim video memory resources that it previously offered for reuse. |
| [PFND3DDDI_RENAME](nc-d3dumddi-pfnd3dddi_rename.md) | The Rename function informs a user-mode display driver to start using the renamed allocation that the LockAsync function previously returned for the specified resource. |
| [PFND3DDDI_RENDERCB](nc-d3dumddi-pfnd3dddi_rendercb.md) | The pfnRenderCb function submits the current command buffer for rendering to the display miniport driver. |
| [PFND3DDDI_RESERVEGPUVIRTUALADDRESSCB](nc-d3dumddi-pfnd3dddi_reservegpuvirtualaddresscb.md) | pfnReserveGPUVirtualAddressCb reserves an address range in the current process graphics processing unit (GPU) virtual address space. The address range is only reserved, there is no actual memory behind it. |
| [PFND3DDDI_RESOLVESHAREDRESOURCE](nc-d3dumddi-pfnd3dddi_resolvesharedresource.md) | The ResolveSharedResource function informs a user-mode display driver that ownership of a shared surface changed or that a surface is being used for GDI interoperation. |
| [PFND3DDDI_SETASYNCCALLBACKSCB](nc-d3dumddi-pfnd3dddi_setasynccallbackscb.md) | The pfnSetAsyncCallbacksCb function notifies the Microsoft Direct3D runtime whether the runtime will start or stop receiving calls to the runtime's callback functions from a worker thread. |
| [PFND3DDDI_SETCLIPPLANE](nc-d3dumddi-pfnd3dddi_setclipplane.md) | The SetClipPlane function sets a clip plane. |
| [PFND3DDDI_SETCONVOLUTIONKERNELMONO](nc-d3dumddi-pfnd3dddi_setconvolutionkernelmono.md) | The SetConvolutionKernelMono function defines the resolution and weights of the kernel filter, which is used when the D3DTEXF_CONVOLUTIONMONO texture filtering mode is set. |
| [PFND3DDDI_SETDECODERENDERTARGET](nc-d3dumddi-pfnd3dddi_setdecoderendertarget.md) | The SetDecodeRenderTarget function sets the render target surface for decoding operations. |
| [PFND3DDDI_SETDEPTHSTENCIL](nc-d3dumddi-pfnd3dddi_setdepthstencil.md) | The SetDepthStencil function sets the depth buffer in the driver's context. |
| [PFND3DDDI_SETDISPLAYMODE](nc-d3dumddi-pfnd3dddi_setdisplaymode.md) | The SetDisplayMode function switches to a display mode or primary that is not supported by the GDI desktop. |
| [PFND3DDDI_SETDISPLAYMODECB](nc-d3dumddi-pfnd3dddi_setdisplaymodecb.md) | The pfnSetDisplayModeCb function sets the allocation that is used to scan out to the display. |
| [PFND3DDDI_SETDISPLAYPRIVATEDRIVERFORMATCB](nc-d3dumddi-pfnd3dddi_setdisplayprivatedriverformatcb.md) | The pfnSetDisplayPrivateDriverFormatCb function changes the private-format attribute of a video present source. |
| [PFND3DDDI_SETINDICES](nc-d3dumddi-pfnd3dddi_setindices.md) | The SetIndices function sets the current index buffer. |
| [PFND3DDDI_SETINDICESUM](nc-d3dumddi-pfnd3dddi_setindicesum.md) | The SetIndicesUM function sets the current index buffer to the given user memory buffer. |
| [PFND3DDDI_SETLIGHT](nc-d3dumddi-pfnd3dddi_setlight.md) | The SetLight function sets properties for a light source. |
| [PFND3DDDI_SETMARKER](nc-d3dumddi-pfnd3dddi_setmarker.md) | Notifies the user-mode display driver that it must generate a new time stamp if any GPU work has completed since the last call to pfnSetMarker. |
| [PFND3DDDI_SETMARKERMODE](nc-d3dumddi-pfnd3dddi_setmarkermode.md) | Notifies the user-mode display driver that it should support a type of Event Tracing for Windows (ETW) marker event. |
| [PFND3DDDI_SETMATERIAL](nc-d3dumddi-pfnd3dddi_setmaterial.md) | The SetMaterial function sets the material properties that devices on the system use to create the required effect during rendering. |
| [PFND3DDDI_SETOVERLAYCOLORCONTROLS](nc-d3dumddi-pfnd3dddi_setoverlaycolorcontrols.md) | The SetOverlayColorControls function changes color-control settings for the given overlay. |
| [PFND3DDDI_SETPALETTE](nc-d3dumddi-pfnd3dddi_setpalette.md) | The SetPalette function associates a palette with a texture. |
| [PFND3DDDI_SETPIXELSHADER](nc-d3dumddi-pfnd3dddi_setpixelshader.md) | The SetPixelShader function sets a pixel shader to be used in all drawing operations. |
| [PFND3DDDI_SETPIXELSHADERCONST](nc-d3dumddi-pfnd3dddi_setpixelshaderconst.md) | The SetPixelShaderConst function sets one or more pixel shader constant registers with floating-point values. |
| [PFND3DDDI_SETPIXELSHADERCONSTB](nc-d3dumddi-pfnd3dddi_setpixelshaderconstb.md) | The SetPixelShaderConstB function sets one or more pixel shader constant registers with Boolean values. |
| [PFND3DDDI_SETPIXELSHADERCONSTI](nc-d3dumddi-pfnd3dddi_setpixelshaderconsti.md) | The SetPixelShaderConstI function sets one or more pixel shader constant registers with integer values. |
| [PFND3DDDI_SETPRIORITY](nc-d3dumddi-pfnd3dddi_setpriority.md) | The SetPriority function sets the eviction-from-memory priority for a managed texture. |
| [PFND3DDDI_SETPRIORITYCB](nc-d3dumddi-pfnd3dddi_setprioritycb.md) | The pfnSetPriorityCb function sets the priority level of a resource or list of allocations. |
| [PFND3DDDI_SETRENDERSTATE](nc-d3dumddi-pfnd3dddi_setrenderstate.md) | The SetRenderState function updates a render state. |
| [PFND3DDDI_SETRENDERTARGET](nc-d3dumddi-pfnd3dddi_setrendertarget.md) | The SetRenderTarget function sets the render target surface. |
| [PFND3DDDI_SETSCISSORRECT](nc-d3dumddi-pfnd3dddi_setscissorrect.md) | The SetScissorRect function marks a portion of a render target that rendering is confined to. |
| [PFND3DDDI_SETSTREAMSOURCE](nc-d3dumddi-pfnd3dddi_setstreamsource.md) | The SetStreamSource function binds a portion of a vertex stream source to a vertex buffer. |
| [PFND3DDDI_SETSTREAMSOURCEFREQ](nc-d3dumddi-pfnd3dddi_setstreamsourcefreq.md) | The SetStreamSourceFreq function sets the frequency divisor of a stream source that is bound to a vertex buffer. |
| [PFND3DDDI_SETSTREAMSOURCEUM](nc-d3dumddi-pfnd3dddi_setstreamsourceum.md) | The SetStreamSourceUM function binds a vertex stream source to a user memory buffer. |
| [PFND3DDDI_SETTEXTURE](nc-d3dumddi-pfnd3dddi_settexture.md) | The SetTexture function inserts a texture at a particular stage in a multiple-texture group. |
| [PFND3DDDI_SETTEXTURESTAGESTATE](nc-d3dumddi-pfnd3dddi_settexturestagestate.md) | The SetTextureStageState function updates the state of a texture at a particular stage in a multiple-texture group. |
| [PFND3DDDI_SETTRANSFORM](nc-d3dumddi-pfnd3dddi_settransform.md) | The SetTransform function sets up a transform. |
| [PFND3DDDI_SETVERTEXSHADERCONST](nc-d3dumddi-pfnd3dddi_setvertexshaderconst.md) | The SetVertexShaderConst function sets one or more vertex shader constant registers with floating-point values. |
| [PFND3DDDI_SETVERTEXSHADERCONSTB](nc-d3dumddi-pfnd3dddi_setvertexshaderconstb.md) | The SetVertexShaderConstB function sets one or more vertex shader constant registers with Boolean values. |
| [PFND3DDDI_SETVERTEXSHADERDECL](nc-d3dumddi-pfnd3dddi_setvertexshaderdecl.md) | The SetVertexShaderDecl function sets the vertex shader declaration so that all of the subsequent drawing operations use that declaration. |
| [PFND3DDDI_SETVERTEXSHADERFUNC](nc-d3dumddi-pfnd3dddi_setvertexshaderfunc.md) | The SetVertexShaderFunc function sets the vertex shader code so that all of the subsequent drawing operations use that code. |
| [PFND3DDDI_SETVIDEOPROCESSRENDERTARGET](nc-d3dumddi-pfnd3dddi_setvideoprocessrendertarget.md) | The SetVideoProcessRenderTarget function sets the render target surface that is used for video processing. |
| [PFND3DDDI_SETVIEWPORT](nc-d3dumddi-pfnd3dddi_setviewport.md) | The SetViewport function informs guard-band-aware drivers of the view-clipping rectangle. |
| [PFND3DDDI_SETZRANGE](nc-d3dumddi-pfnd3dddi_setzrange.md) | The SetZRange function informs the driver about the range of z values. |
| [PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECT2CB](nc-d3dumddi-pfnd3dddi_signalsynchronizationobject2cb.md) | Inserts a signal on the specified synchronization objects in the specified context direct memory access (DMA) stream. Used by WDDM 1.2 and later user-mode display drivers. |
| [PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECTCB](nc-d3dumddi-pfnd3dddi_signalsynchronizationobjectcb.md) | The pfnSignalSynchronizationObjectCb function inserts a signal on the specified synchronization objects in the specified context DMA stream. |
| [PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECTFROMCPUCB](nc-d3dumddi-pfnd3dddi_signalsynchronizationobjectfromcpucb.md) | pfnSignalSynchronizationObjectFromCpuCb enables a driver to signal a monitored fence. |
| [PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2CB](nc-d3dumddi-pfnd3dddi_signalsynchronizationobjectfromgpu2cb.md) | pfnSignalSynchronizationObjectFromGpu2Cb is used to signal a monitored fence. |
| [PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECTFROMGPUCB](nc-d3dumddi-pfnd3dddi_signalsynchronizationobjectfromgpucb.md) | pfnSignalSynchronizationObjectFromGpuCb is used to signal a monitored fence. |
| [PFND3DDDI_STARTSESSIONKEYREFRESH](nc-d3dumddi-pfnd3dddi_startsessionkeyrefresh.md) | The StartSessionKeyRefresh function returns a random number that the driver's FinishSessionKeyRefresh function subsequently uses to perform an exclusive OR operation (XOR) with the session key. |
| [PFND3DDDI_STATESET](nc-d3dumddi-pfnd3dddi_stateset.md) | The StateSet function sets a state block. |
| [PFND3DDDI_SUBMITCOMMANDCB](nc-d3dumddi-pfnd3dddi_submitcommandcb.md) | pfnSubmitCommandCb is used to submit command buffers on contexts that support graphics processing unit (GPU) virtual addressing. |
| [PFND3DDDI_SUBMITCOMMANDTOHWQUEUECB](nc-d3dumddi-pfnd3dddi_submitcommandtohwqueuecb.md) | A callback to submit a command to the hardware queue. |
| [PFND3DDDI_SUBMITSIGNALSYNCOBJECTSTOHWQUEUECB](nc-d3dumddi-pfnd3dddi_submitsignalsyncobjectstohwqueuecb.md) | A callback to submit a signal command to the hardware queue. |
| [PFND3DDDI_SUBMITWAITFORSYNCOBJECTSTOHWQUEUECB](nc-d3dumddi-pfnd3dddi_submitwaitforsyncobjectstohwqueuecb.md) | A callback to submit a wait command to the hardware queue. |
| [PFND3DDDI_TEXBLT](nc-d3dumddi-pfnd3dddi_texblt.md) | The TexBlt function performs a bit-block transfer (bitblt) operation from a source texture to a destination texture, including all of the sublevels of the source texture. |
| [PFND3DDDI_TEXBLT1](nc-d3dumddi-pfnd3dddi_texblt1.md) | Performs a bit-block transfer (bitblt) operation from a source texture to a destination texture, including all of the sublevels of the source texture. Implemented by Windows Display Driver Model (WDDM) 1.2 or later user-mode display drivers. |
| [PFND3DDDI_TRIMRESIDENCYSET](nc-d3dumddi-pfnd3dddi_trimresidencyset.md) | pfnTrimResidencySet is used to trim the residency list for a given device. User mode drivers are required to implement this callback in order to participate in the new memory residency model. |
| [PFND3DDDI_UNLOCK](nc-d3dumddi-pfnd3dddi_unlock.md) | The Unlock function unlocks a resource or a surface within the resource that was previously locked by the Lock function. |
| [PFND3DDDI_UNLOCK2CB](nc-d3dumddi-pfnd3dddi_unlock2cb.md) | The pfnUnlock2Cb function unlocks an allocation that was locked by a call to the pfnLock2Cb function. |
| [PFND3DDDI_UNLOCKASYNC](nc-d3dumddi-pfnd3dddi_unlockasync.md) | The UnlockAsync function unlocks a resource or a surface within the resource that the LockAsync function previously locked. |
| [PFND3DDDI_UNLOCKCB](nc-d3dumddi-pfnd3dddi_unlockcb.md) | The pfnUnlockCb function unlocks an allocation that was locked by a call to the pfnLockCb function. |
| [PFND3DDDI_UPDATEALLOCATIONPROPERTYCB](nc-d3dumddi-pfnd3dddi_updateallocationpropertycb.md) | The pfnUpdateAllocationPropertyCb functions updates the property of an allocation without creating a new allocation. |
| [PFND3DDDI_UPDATEGPUVIRTUALADDRESSCB](nc-d3dumddi-pfnd3dddi_updategpuvirtualaddresscb.md) | pfnUpdateGpuVirtualAddressCb is a special operation used in the context of tile resources. |
| [PFND3DDDI_UPDATEOVERLAY](nc-d3dumddi-pfnd3dddi_updateoverlay.md) | The UpdateOverlay function reconfigures or moves an overlay that is being displayed. |
| [PFND3DDDI_UPDATEOVERLAYCB](nc-d3dumddi-pfnd3dddi_updateoverlaycb.md) | The pfnUpdateOverlayCb function modifies a kernel-mode overlay object. |
| [PFND3DDDI_UPDATEPALETTE](nc-d3dumddi-pfnd3dddi_updatepalette.md) | The UpdatePalette function updates a texture palette. |
| [PFND3DDDI_UPDATESUBRESOURCEUP](nc-d3dumddi-pfnd3dddi_updatesubresourceup.md) | Called by the Microsoft Direct3D runtime to update a destination subresource region from a source system-memory region. Must be implemented by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [PFND3DDDI_UPDATEWINFO](nc-d3dumddi-pfnd3dddi_updatewinfo.md) | The UpdateWInfo function updates the w range for w buffering. |
| [PFND3DDDI_VALIDATEDEVICE](nc-d3dumddi-pfnd3dddi_validatedevice.md) | The ValidateDevice function returns the number of passes in which the hardware can perform the blending operations that are specified in the current state. |
| [PFND3DDDI_VIDEOPROCESSBEGINFRAME](nc-d3dumddi-pfnd3dddi_videoprocessbeginframe.md) | The VideoProcessBeginFrame function notifies the user-mode display driver that processing of a video frame can begin on the specified Microsoft DirectX Video Accelerator (VA) video processing device. |
| [PFND3DDDI_VIDEOPROCESSBLT](nc-d3dumddi-pfnd3dddi_videoprocessblt.md) | The VideoProcessBlt function processes a video frame by using the specified Microsoft DirectX Video Accelerator (VA) video processing device. |
| [PFND3DDDI_VIDEOPROCESSENDFRAME](nc-d3dumddi-pfnd3dddi_videoprocessendframe.md) | The VideoProcessEndFrame function notifies the user-mode display driver that all of the data that is required to process the current frame was submitted. |
| [PFND3DDDI_VOLBLT](nc-d3dumddi-pfnd3dddi_volblt.md) | The VolBlt function performs a bit-block transfer (bitblt) operation from a source volume texture to a destination volume texture. |
| [PFND3DDDI_VOLBLT1](nc-d3dumddi-pfnd3dddi_volblt1.md) | Performs a bit-block transfer (bitblt) operation from a source volume texture to a destination volume texture. Implemented by Windows Display Driver Model (WDDM) 1.2 or later user-mode display drivers. |
| [PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECT2CB](nc-d3dumddi-pfnd3dddi_waitforsynchronizationobject2cb.md) | Inserts a wait command for the specified synchronization objects in the specified context command stream. Used by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECTCB](nc-d3dumddi-pfnd3dddi_waitforsynchronizationobjectcb.md) | The pfnWaitForSynchronizationObjectCb function inserts a wait for the specified synchronization objects in the specified context DMA stream. |
| [PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPUCB](nc-d3dumddi-pfnd3dddi_waitforsynchronizationobjectfromcpucb.md) | pfnWaitForSynchronizationObjectFromCpuCb waits for a monitored fence to reach a certain value before processing subsequent context commands. |
| [PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMGPUCB](nc-d3dumddi-pfnd3dddi_waitforsynchronizationobjectfromgpucb.md) | pfnWaitForSynchronizationObjectFromGpuCb waits for a monitored fence to reach a certain value before processing subsequent context commands. |
| [PFND3DDDICB_LOGSTRINGTABLEENTRY](nc-d3dumddi-pfnd3dddicb_logstringtableentry.md) | Locates a string table entry that is used by the LogMarkerStringTable function to log an Event Tracing for Windows (ETW) marker event. Optionally implemented by Windows Display Driver Model (WDDM) 1.3 and later drivers. |



## Structures
| Title | Description |
| ---- |:---- |
| [_D3D12DDICB_RECLAIMALLOCATIONS2](ns-d3dumddi-_d3d12ddicb_reclaimallocations2.md) | Describes video memory resources that are to be reclaimed and that the driver previously offered for reuse. |
| [_D3DDDI_ADAPTERCALLBACKS](ns-d3dumddi-_d3dddi_adaptercallbacks.md) | The D3DDDI_ADAPTERCALLBACKS structure contains Microsoft Direct3D runtime callback functions that the user-mode display driver can use. |
| [_D3DDDI_ADAPTERFUNCS](ns-d3dumddi-_d3dddi_adapterfuncs.md) | The D3DDDI_ADAPTERFUNCS structure contains functions that the user-mode display driver can implement to communicate with a graphics adapter object. |
| [_D3DDDI_BLTFLAGS](ns-d3dumddi-_d3dddi_bltflags.md) | The D3DDDI_BLTFLAGS structure identifies the type of bit-block transfer (bitblt) to perform. |
| [_D3DDDI_COLORFILLFLAGS](ns-d3dumddi-_d3dddi_colorfillflags.md) | The D3DDDI_COLORFILLFLAGS structure describes how to color-fill a rectangle on a surface. |
| [_D3DDDI_CREATEDEVICEFLAGS](ns-d3dumddi-_d3dddi_createdeviceflags.md) | The D3DDDI_CREATEDEVICEFLAGS structure describes how to create a device. |
| [_D3DDDI_DEVICECALLBACKS](ns-d3dumddi-_d3dddi_devicecallbacks.md) | The D3DDDI_DEVICECALLBACKS structure contains Microsoft Direct3D runtime callback functions that the user-mode display driver can use. |
| [_D3DDDI_DEVICEFUNCS](ns-d3dumddi-_d3dddi_devicefuncs.md) | The D3DDDI_DEVICEFUNCS structure contains functions that the user-mode display driver can implement to render graphics primitives and process state changes. |
| [_D3DDDI_EXECUTIONSTATEESCAPE](ns-d3dumddi-_d3dddi_executionstateescape.md) | Specifies the state of the device. |
| [_D3DDDI_FLIPOVERLAYFLAGS](ns-d3dumddi-_d3dddi_flipoverlayflags.md) | The D3DDDI_FLIPOVERLAYFLAGS structure identifies how to flip a resource on an overlay. |
| [_D3DDDI_FRAMELATENCYESCAPE](ns-d3dumddi-_d3dddi_framelatencyescape.md) | Specifies an app's maximum frame latency. |
| [_D3DDDI_ISSUEQUERYFLAGS](ns-d3dumddi-_d3dddi_issuequeryflags.md) | The D3DDDI_ISSUEQUERYFLAGS structure identifies the state of a query issue. |
| [_D3DDDI_LIGHT](ns-d3dumddi-_d3dddi_light.md) | The D3DDDI_LIGHT structure describes a set of lighting properties. |
| [_D3DDDI_LOCKASYNCFLAGS](ns-d3dumddi-_d3dddi_lockasyncflags.md) | The D3DDDI_LOCKASYNCFLAGS structure identifies how to lock a resource. |
| [_D3DDDI_LOCKFLAGS](ns-d3dumddi-_d3dddi_lockflags.md) | The D3DDDI_LOCKFLAGS structure identifies how to lock a resource. |
| [_D3DDDI_MULTIPLANE_OVERLAY_ATTRIBUTES](ns-d3dumddi-_d3dddi_multiplane_overlay_attributes.md) | Used by the user-mode display driver to specify overlay plane attributes. |
| [_D3DDDI_OPENRESOURCEFLAGS](ns-d3dumddi-_d3dddi_openresourceflags.md) | The D3DDDI_OPENRESOURCEFLAGS structure identifies the type of resource to open. |
| [_D3DDDI_OVERLAYCOLORCONTROLS](ns-d3dumddi-_d3dddi_overlaycolorcontrols.md) | The D3DDDI_OVERLAYCOLORCONTROLS structure describes color-control settings for an overlay. |
| [_D3DDDI_OVERLAYCOLORCONTROLSFLAGS](ns-d3dumddi-_d3dddi_overlaycolorcontrolsflags.md) | The D3DDDI_OVERLAYCOLORCONTROLSFLAGS structure identifies color-control settings that the overlay hardware supports. |
| [_D3DDDI_OVERLAYINFO](ns-d3dumddi-_d3dddi_overlayinfo.md) | The D3DDDI_OVERLAYINFO structure describes information about an overlay. |
| [_D3DDDI_OVERLAYINFOFLAGS](ns-d3dumddi-_d3dddi_overlayinfoflags.md) | The D3DDDI_OVERLAYINFOFLAGS structure identifies the type of overlay operation to perform. |
| [_D3DDDI_PRESENT_MULTIPLANE_OVERLAY](ns-d3dumddi-_d3dddi_present_multiplane_overlay.md) | Specifies an overlay plane to display. |
| [_D3DDDI_PRESENTFLAGS](ns-d3dumddi-_d3dddi_presentflags.md) | The D3DDDI_PRESENTFLAGS structure identifies how to perform a present operation. |
| [_D3DDDI_UNLOCKASYNCFLAGS](ns-d3dumddi-_d3dddi_unlockasyncflags.md) | The D3DDDI_UNLOCKASYNCFLAGS structure identifies how to unlock a resource. |
| [_D3DDDI_UNLOCKFLAGS](ns-d3dumddi-_d3dddi_unlockflags.md) | The D3DDDI_UNLOCKFLAGS structure identifies how to unlock a resource. |
| [_D3DDDIARG_AUTHENTICATEDCHANNELKEYEXCHANGE](ns-d3dumddi-_d3dddiarg_authenticatedchannelkeyexchange.md) | The D3DDDIARG_AUTHENTICATEDCHANNELKEYEXCHANGE structure describes a buffer that contains the session key, which the authenticated channel uses. |
| [_D3DDDIARG_BLT](ns-d3dumddi-_d3dddiarg_blt.md) | The D3DDDIARG_BLT structure describes the parameters of a bit-block transfer (bitblt). |
| [_D3DDDIARG_BUFFERBLT](ns-d3dumddi-_d3dddiarg_bufferblt.md) | The D3DDDIARG_BUFFERBLT structure describes the parameters of a buffer bit-block transfer (bitblt) operation. |
| [_D3DDDIARG_BUFFERBLT1](ns-d3dumddi-_d3dddiarg_bufferblt1.md) | Describes the parameters of a buffer bit-block transfer (bitblt) operation. |
| [_D3DDDIARG_CAPTURETOSYSMEM](ns-d3dumddi-_d3dddiarg_capturetosysmem.md) | The D3DDDIARG_CAPTURETOSYSMEM structure describes the parameters of a bit-block transfer (bitblt) from a capture buffer to a video memory surface. |
| [_D3DDDIARG_CHECKDIRECTFLIPSUPPORT](ns-d3dumddi-_d3dddiarg_checkdirectflipsupport.md) | Specifies resources used for Direct Flip operations, in which video memory is seamlessly flipped between an application's managed primary allocations and the Desktop Window Manager's (DWM) managed primary allocations. |
| [_D3DDDIARG_CHECKMULTIPLANEOVERLAYSUPPORT](ns-d3dumddi-_d3dddiarg_checkmultiplaneoverlaysupport.md) | Used in a call to the pfnCheckMultiPlaneOverlaySupport (D3D) function to check details on hardware support for multiplane overlays. |
| [_D3DDDIARG_CLEAR](ns-d3dumddi-_d3dddiarg_clear.md) | The D3DDDIARG_CLEAR structure describes the parameters of a hardware-assisted clearing operation. |
| [_D3DDDIARG_COLORFILL](ns-d3dumddi-_d3dddiarg_colorfill.md) | The D3DDDIARG_COLORFILL structure describes the parameters of a color-fill operation. |
| [_D3DDDIARG_COMPOSERECTS](ns-d3dumddi-_d3dddiarg_composerects.md) | The D3DDDIARG_COMPOSERECTS structure describes the parameters that are used to compose rectangular areas. |
| [_D3DDDIARG_CONFIGUREAUTHENICATEDCHANNEL](ns-d3dumddi-_d3dddiarg_configureauthenicatedchannel.md) | The D3DDDIARG_CONFIGUREAUTHENTICATEDCHANNEL structure describes the state that is set within an authenticated channel by using the ConfigureAuthenticatedChannel function. |
| [_D3DDDIARG_CREATEAUTHENICATEDCHANNEL](ns-d3dumddi-_d3dddiarg_createauthenicatedchannel.md) | The D3DDDIARG_CREATEAUTHENTICATEDCHANNEL structure identifies a channel to create. |
| [_D3DDDIARG_CREATECRYPTOSESSION](ns-d3dumddi-_d3dddiarg_createcryptosession.md) | The D3DDDIARG_CREATECRYPTOSESSION structure describes an encryption session to create. |
| [_D3DDDIARG_CREATEDECODEDEVICE](ns-d3dumddi-_d3dddiarg_createdecodedevice.md) | The D3DDDIARG_CREATEDECODEDEVICE structure describes a Microsoft DirectX Video Acceleration (DirectX VA) decode device to create. |
| [_D3DDDIARG_CREATEDEVICE](ns-d3dumddi-_d3dddiarg_createdevice.md) | The D3DDDIARG_CREATEDEVICE structure contains information that describes the display device to create. |
| [_D3DDDIARG_CREATEEXTENSIONDEVICE](ns-d3dumddi-_d3dddiarg_createextensiondevice.md) | The D3DDDIARG_CREATEEXTENSIONDEVICE structure describes a Microsoft DirectX Video Acceleration (DirectX VA) extension device to create. |
| [_D3DDDIARG_CREATELIGHT](ns-d3dumddi-_d3dddiarg_createlight.md) | The D3DDDIARG_CREATELIGHT structure contains the index into the light array. |
| [_D3DDDIARG_CREATEOVERLAY](ns-d3dumddi-_d3dddiarg_createoverlay.md) | The D3DDDIARG_CREATEOVERLAY structure describes an overlay to create. |
| [_D3DDDIARG_CREATEPIXELSHADER](ns-d3dumddi-_d3dddiarg_createpixelshader.md) | The D3DDDIARG_CREATEPIXELSHADER structure specifies a shader handle to associate with pixel shader code. |
| [_D3DDDIARG_CREATEQUERY](ns-d3dumddi-_d3dddiarg_createquery.md) | The D3DDDIARG_CREATEQUERY structure identifies a query to create. |
| [_D3DDDIARG_CREATEVERTEXSHADERDECL](ns-d3dumddi-_d3dddiarg_createvertexshaderdecl.md) | The D3DDDIARG_CREATEVERTEXSHADERDECL structure specifies a shader handle to associate with the vertex shader declaration. |
| [_D3DDDIARG_CREATEVERTEXSHADERFUNC](ns-d3dumddi-_d3dddiarg_createvertexshaderfunc.md) | The D3DDDIARG_CREATEVERTEXSHADERFUNC structure specifies a shader handle to associate with vertex shader code. |
| [_D3DDDIARG_CREATEVIDEOPROCESSDEVICE](ns-d3dumddi-_d3dddiarg_createvideoprocessdevice.md) | The D3DDDIARG_CREATEVIDEOPROCESSDEVICE structure describes a Microsoft DirectX Video Acceleration (DirectX VA) video processing device to create. |
| [_D3DDDIARG_CRYPTOSESSIONKEYEXCHANGE](ns-d3dumddi-_d3dddiarg_cryptosessionkeyexchange.md) | The D3DDDIARG_CRYPTOSESSIONKEYEXCHANGE structure describes a buffer that contains the session key, which is used for encryption. |
| [_D3DDDIARG_DECODEBEGINFRAME](ns-d3dumddi-_d3dddiarg_decodebeginframe.md) | The D3DDDIARG_DECODEBEGINFRAME structure specifies the Microsoft DirectX Video Accelerator (VA) decoder that should start decoding a frame. |
| [_D3DDDIARG_DECODEENDFRAME](ns-d3dumddi-_d3dddiarg_decodeendframe.md) | The D3DDDIARG_DECODEENDFRAME structure specifies the Microsoft DirectX Video Accelerator (VA) decoder that should stop decoding a frame. |
| [_D3DDDIARG_DECODEEXECUTE](ns-d3dumddi-_d3dddiarg_decodeexecute.md) | The D3DDDIARG_DECODEEXECUTE structure describes a Microsoft DirectX Video Acceleration (VA) decode operation to perform. |
| [_D3DDDIARG_DECODEEXTENSIONEXECUTE](ns-d3dumddi-_d3dddiarg_decodeextensionexecute.md) | The D3DDDIARG_DECODEEXTENSIONEXECUTE structure describes a nonstandard Microsoft DirectX Video Acceleration (VA) decode operation to perform. |
| [_D3DDDIARG_DECRYPTIONBLT](ns-d3dumddi-_d3dddiarg_decryptionblt.md) | The D3DDDIARG_DECRYPTIONBLT structure describes the parameters of an decrypted bit-block transfer (bitblt) in a call to the DecryptionBlt function. |
| [_D3DDDIARG_DEPTHFILL](ns-d3dumddi-_d3dddiarg_depthfill.md) | The D3DDDIARG_DEPTHFILL structure describes the parameters of a depth-fill operation. |
| [_D3DDDIARG_DESTROYAUTHENICATEDCHANNEL](ns-d3dumddi-_d3dddiarg_destroyauthenicatedchannel.md) | The D3DDDIARG_DESTROYAUTHENTICATEDCHANNEL structure contains the handle to an authenticated channel that is destroyed in a call to the DestroyAuthenticatedChannel function. |
| [_D3DDDIARG_DESTROYCRYPTOSESSION](ns-d3dumddi-_d3dddiarg_destroycryptosession.md) | The D3DDDIARG_DESTROYCRYPTOSESSION structure contains the handle to an encryption session that is destroyed in a call to the DestroyCryptoSession function. |
| [_D3DDDIARG_DESTROYLIGHT](ns-d3dumddi-_d3dddiarg_destroylight.md) | The D3DDDIARG_DESTROYLIGHT structure contains the index into a light array for the light to destroy. |
| [_D3DDDIARG_DESTROYOVERLAY](ns-d3dumddi-_d3dddiarg_destroyoverlay.md) | The D3DDDIARG_DESTROYOVERLAY structure contains a handle to the overlay to disable. |
| [_D3DDDIARG_DISCARD](ns-d3dumddi-_d3dddiarg_discard.md) | Defines video display memory that can be discarded because the contents are no longer needed. |
| [_D3DDDIARG_DRAWINDEXEDPRIMITIVE](ns-d3dumddi-_d3dddiarg_drawindexedprimitive.md) | The D3DDDIARG_DRAWINDEXEDPRIMITIVE structure describes an indexed primitive to draw. |
| [_D3DDDIARG_DRAWINDEXEDPRIMITIVE2](ns-d3dumddi-_d3dddiarg_drawindexedprimitive2.md) | The D3DDDIARG_DRAWINDEXEDPRIMITIVE2 structure describes an indexed primitive to draw. |
| [_D3DDDIARG_DRAWPRIMITIVE](ns-d3dumddi-_d3dddiarg_drawprimitive.md) | The D3DDDIARG_DRAWPRIMITIVE structure describes a nonindexed primitive to draw. |
| [_D3DDDIARG_DRAWPRIMITIVE2](ns-d3dumddi-_d3dddiarg_drawprimitive2.md) | The D3DDDIARG_DRAWPRIMITIVE2 structure describes a nonindexed primitive to draw. |
| [_D3DDDIARG_DRAWRECTPATCH](ns-d3dumddi-_d3dddiarg_drawrectpatch.md) | The D3DDDIARG_DRAWRECTPATCH structure describes a rectangular patch to draw. |
| [_D3DDDIARG_DRAWTRIPATCH](ns-d3dumddi-_d3dddiarg_drawtripatch.md) | The D3DDDIARG_DRAWTRIPATCH structure describes a triangular patch to draw. |
| [_D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR](ns-d3dumddi-_d3dddiarg_dxvahd_createvideoprocessor.md) | The D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR structure describes a Microsoft DirectX Video Acceleration (DirectX VA) video processor to create. |
| [_D3DDDIARG_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE](ns-d3dumddi-_d3dddiarg_dxvahd_getvideoprocessbltstateprivate.md) | The D3DDDIARG_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE structure describes the private bit-block transfer (bitblt) state of the video processor to retrieve. |
| [_D3DDDIARG_DXVAHD_GETVIDEOPROCESSSTREAMSTATEPRIVATE](ns-d3dumddi-_d3dddiarg_dxvahd_getvideoprocessstreamstateprivate.md) | The D3DDDIARG_DXVAHD_GETVIDEOPROCESSSTREAMSTATEPRIVATE structure describes the private stream-state of the video processor to retrieve. |
| [_D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE](ns-d3dumddi-_d3dddiarg_dxvahd_setvideoprocessbltstate.md) | The D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE structure describes the bit-block transfer (bitblt) state of the video processor to change and the data that is used to change the state. |
| [_D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE](ns-d3dumddi-_d3dddiarg_dxvahd_setvideoprocessstreamstate.md) | The D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE structure describes the stream state of the video processor to change and the data that is used to change the state. |
| [_D3DDDIARG_DXVAHD_VIDEOPROCESSBLTHD](ns-d3dumddi-_d3dddiarg_dxvahd_videoprocessblthd.md) | The D3DDDIARG_DXVAHD_VIDEOPROCESSBLTHD structure describes a Microsoft DirectX Video Acceleration (VA) video processing high definition operation to perform. |
| [_D3DDDIARG_ENCRYPTIONBLT](ns-d3dumddi-_d3dddiarg_encryptionblt.md) | The D3DDDIARG_ENCRYPTIONBLT structure describes the parameters of an encrypted bit-block transfer (bitblt) in a call to the EncryptionBlt function. |
| [_D3DDDIARG_EXTENSIONEXECUTE](ns-d3dumddi-_d3dddiarg_extensionexecute.md) | The D3DDDIARG_EXTENSIONEXECUTE structure describes a Microsoft DirectX Video Acceleration (VA) extension operation to perform. |
| [_D3DDDIARG_FINISHSESSIONKEYREFRESH](ns-d3dumddi-_d3dddiarg_finishsessionkeyrefresh.md) | The D3DDDIARG_FINISHSESSIONKEYREFRESH structure contains the handle to an encryption session to end in a call to the FinishSessionKeyRefresh function. |
| [_D3DDDIARG_FLIPOVERLAY](ns-d3dumddi-_d3dddiarg_flipoverlay.md) | The D3DDDIARG_FLIPOVERLAY structure describes a new resource to display on a given overlay. |
| [_D3DDDIARG_GENERATEMIPSUBLEVELS](ns-d3dumddi-_d3dddiarg_generatemipsublevels.md) | The D3DDDIARG_GENERATEMIPSUBLEVELS structure describes how to generate the sublevels of a MIP-map texture. |
| [_D3DDDIARG_GETCAPS](ns-d3dumddi-_d3dddiarg_getcaps.md) | The D3DDDIARG_GETCAPS structure contains display device capabilities of a particular type. |
| [_D3DDDIARG_GETCAPTUREALLOCATIONHANDLE](ns-d3dumddi-_d3dddiarg_getcaptureallocationhandle.md) | The D3DDDIARG_GETCAPTUREALLOCATIONHANDLE structure describes the parameters for retrieving an allocation handle from a capture resource handle. |
| [_D3DDDIARG_GETOVERLAYCOLORCONTROLS](ns-d3dumddi-_d3dddiarg_getoverlaycolorcontrols.md) | The D3DDDIARG_GETOVERLAYCOLORCONTROLS structure describes the parameters for retrieving an overlay's color-control settings. |
| [_D3DDDIARG_GETPITCH](ns-d3dumddi-_d3dddiarg_getpitch.md) | The D3DDDIARG_GETPITCH structure describes an encrypted surface for which the GetPitch function retrieves the pitch. |
| [_D3DDDIARG_GETQUERYDATA](ns-d3dumddi-_d3dddiarg_getquerydata.md) | The D3DDDIARG_GETQUERYDATA structure contains query information that was retrieved from the user-mode display driver. |
| [_D3DDDIARG_ISSUEQUERY](ns-d3dumddi-_d3dddiarg_issuequery.md) | The D3DDDIARG_ISSUEQUERY structure describes how to process a query that was created by the CreateQuery function. |
| [_D3DDDIARG_LOCK](ns-d3dumddi-_d3dddiarg_lock.md) | The D3DDDIARG_LOCK structure describes a resource or a surface within the resource to lock. |
| [_D3DDDIARG_LOCKASYNC](ns-d3dumddi-_d3dddiarg_lockasync.md) | The D3DDDIARG_LOCKASYNC structure describes a resource or a surface within the resource to lock. |
| [_D3DDDIARG_MULTIPLYTRANSFORM](ns-d3dumddi-_d3dddiarg_multiplytransform.md) | The D3DDDIARG_MULTIPLYTRANSFORM structure describes how to modify the current transform. |
| [_D3DDDIARG_OFFERRESOURCES](ns-d3dumddi-_d3dddiarg_offerresources.md) | Describes video memory resources that the user-mode display driver offers for reuse. Used with the OfferResources function. |
| [_D3DDDIARG_OPENADAPTER](ns-d3dumddi-_d3dddiarg_openadapter.md) | The D3DDDIARG_OPENADAPTER structure contains information that describes the graphics adapter object. |
| [_D3DDDIARG_OPENRESOURCE](ns-d3dumddi-_d3dddiarg_openresource.md) | The D3DDDIARG_OPENRESOURCE structure contains information for opening a shared resource. |
| [_D3DDDIARG_PRESENT](ns-d3dumddi-_d3dddiarg_present.md) | The D3DDDIARG_PRESENT structure describes a resource to display. |
| [_D3DDDIARG_PRESENT1](ns-d3dumddi-_d3dddiarg_present1.md) | Describes a resource to display. Used with the pfnPresent1(D3D) function by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [_D3DDDIARG_QUERYAUTHENICATEDCHANNEL](ns-d3dumddi-_d3dddiarg_queryauthenicatedchannel.md) | The D3DDDIARG_QUERYAUTHENTICATEDCHANNEL structure describes authenticated-channel information to query by using the QueryAuthenticatedChannel function. |
| [_D3DDDIARG_QUERYRESOURCERESIDENCY](ns-d3dumddi-_d3dddiarg_queryresourceresidency.md) | The D3DDDIARG_QUERYRESOURCERESIDENCY structure describes a list of resources on which residency is verified through the QueryResourceResidency function. |
| [_D3DDDIARG_RECLAIMRESOURCES](ns-d3dumddi-_d3dddiarg_reclaimresources.md) | Describes video memory resources that are to be reclaimed and that the user-mode display driver previously offered for reuse. Used with the ReclaimResources function. |
| [_D3DDDIARG_RENAME](ns-d3dumddi-_d3dddiarg_rename.md) | The D3DDDIARG_RENAME structure describes a resource or a surface within the resource to rename with a new allocation. |
| [_D3DDDIARG_RENDERSTATE](ns-d3dumddi-_d3dddiarg_renderstate.md) | The D3DDDIARG_RENDERSTATE structure describes how to update a specific render state. |
| [_D3DDDIARG_RESOLVESHAREDRESOURCE](ns-d3dumddi-_d3dddiarg_resolvesharedresource.md) | The D3DDDIARG_RESOLVESHAREDRESOURCE structure specifies the resource that the user-mode display driver's ResolveSharedResource function uses as a synchronized shared surface or a GDI interoperable surface. |
| [_D3DDDIARG_SETCLIPPLANE](ns-d3dumddi-_d3dddiarg_setclipplane.md) | The D3DDDIARG_SETCLIPPLANE structure describes a clip plane. |
| [_D3DDDIARG_SETCONVOLUTIONKERNELMONO](ns-d3dumddi-_d3dddiarg_setconvolutionkernelmono.md) | The D3DDDIARG_SETCONVOLUTIONKERNELMONO structure describes parameters for setting the monochrome convolution kernel. |
| [_D3DDDIARG_SETDECODERENDERTARGET](ns-d3dumddi-_d3dddiarg_setdecoderendertarget.md) | The D3DDDIARG_SETDECODERENDERTARGET structure describes the decode render target surface. |
| [_D3DDDIARG_SETDEPTHSTENCIL](ns-d3dumddi-_d3dddiarg_setdepthstencil.md) | The D3DDDIARG_SETDEPTHSTENCIL structure specifies a depth buffer. |
| [_D3DDDIARG_SETDISPLAYMODE](ns-d3dumddi-_d3dddiarg_setdisplaymode.md) | The D3DDDIARG_SETDISPLAYMODE structure describes parameters for setting the display mode. |
| [_D3DDDIARG_SETINDICES](ns-d3dumddi-_d3dddiarg_setindices.md) | The D3DDDIARG_SETINDICES structure describes parameters for setting the current index buffer. |
| [_D3DDDIARG_SETLIGHT](ns-d3dumddi-_d3dddiarg_setlight.md) | The D3DDDIARG_SETLIGHT structure describes how to set light properties. |
| [_D3DDDIARG_SETMATERIAL](ns-d3dumddi-_d3dddiarg_setmaterial.md) | The D3DDDIARG_SETMATERIAL structure describes the material properties that are used for rendering. |
| [_D3DDDIARG_SETOVERLAYCOLORCONTROLS](ns-d3dumddi-_d3dddiarg_setoverlaycolorcontrols.md) | The D3DDDIARG_SETOVERLAYCOLORCONTROLS structure describes the parameters for changing an overlay's color-control settings. |
| [_D3DDDIARG_SETPALETTE](ns-d3dumddi-_d3dddiarg_setpalette.md) | The D3DDDIARG_SETPALETTE structure describes how to associate a palette with a texture. |
| [_D3DDDIARG_SETPIXELSHADERCONST](ns-d3dumddi-_d3dddiarg_setpixelshaderconst.md) | The D3DDDIARG_SETPIXELSHADERCONST structure describes how to set the pixel shader constant registers. |
| [_D3DDDIARG_SETPRIORITY](ns-d3dumddi-_d3dddiarg_setpriority.md) | The D3DDDIARG_SETPRIORITY structure describes the priority level to set for a managed texture. |
| [_D3DDDIARG_SETRENDERTARGET](ns-d3dumddi-_d3dddiarg_setrendertarget.md) | The D3DDDIARG_SETRENDERTARGET structure describes the render target surface. |
| [_D3DDDIARG_SETSTREAMSOURCE](ns-d3dumddi-_d3dddiarg_setstreamsource.md) | The D3DDDIARG_SETSTREAMSOURCE structure describes the portion of the vertex stream to bind to a vertex buffer. |
| [_D3DDDIARG_SETSTREAMSOURCEFREQ](ns-d3dumddi-_d3dddiarg_setstreamsourcefreq.md) | The D3DDDIARG_SETSTREAMSOURCEFREQ structure describes how the frequency divisor for a portion of the vertex stream source is set. |
| [_D3DDDIARG_SETSTREAMSOURCEUM](ns-d3dumddi-_d3dddiarg_setstreamsourceum.md) | The D3DDDIARG_SETSTREAMSOURCEUM structure describes the vertex stream to bind to a user-memory buffer. |
| [_D3DDDIARG_SETTRANSFORM](ns-d3dumddi-_d3dddiarg_settransform.md) | The D3DDDIARG_SETTRANSFORM structure describes how to set up a transform. |
| [_D3DDDIARG_SETVERTEXSHADERCONST](ns-d3dumddi-_d3dddiarg_setvertexshaderconst.md) | The D3DDDIARG_SETVERTEXSHADERCONST structure describes how to set vertex shader constant registers. |
| [_D3DDDIARG_SETVIDEOPROCESSRENDERTARGET](ns-d3dumddi-_d3dddiarg_setvideoprocessrendertarget.md) | The D3DDDIARG_SETVIDEOPROCESSRENDERTARGET structure describes the render target surface for video processing. |
| [_D3DDDIARG_STARTSESSIONKEYREFRESH](ns-d3dumddi-_d3dddiarg_startsessionkeyrefresh.md) | The D3DDDIARG_STARTSESSIONKEYREFRESH structure contains information about the random number for the encryption session. |
| [_D3DDDIARG_STATESET](ns-d3dumddi-_d3dddiarg_stateset.md) | The D3DDDIARG_STATESET structure describes how to set a state block. |
| [_D3DDDIARG_TEXBLT](ns-d3dumddi-_d3dddiarg_texblt.md) | The D3DDDIARG_TEXBLT structure describes parameters for a texture bit-block transfer (bitblt) operation. |
| [_D3DDDIARG_TEXBLT1](ns-d3dumddi-_d3dddiarg_texblt1.md) | Describes parameters for a texture bit-block transfer (bitblt) operation. |
| [_D3DDDIARG_TEXTURESTAGESTATE](ns-d3dumddi-_d3dddiarg_texturestagestate.md) | The D3DDDIARG_TEXTURESTAGESTATE structure describes how to update a texture at a particular stage in a multiple-texture group. |
| [_D3DDDIARG_UNLOCK](ns-d3dumddi-_d3dddiarg_unlock.md) | The D3DDDIARG_UNLOCK structure describes a resource or a surface within the resource to unlock. |
| [_D3DDDIARG_UNLOCKASYNC](ns-d3dumddi-_d3dddiarg_unlockasync.md) | The D3DDDIARG_UNLOCKASYNC structure describes a resource or a surface within the resource to unlock. |
| [_D3DDDIARG_UPDATEOVERLAY](ns-d3dumddi-_d3dddiarg_updateoverlay.md) | The D3DDDIARG_UPDATEOVERLAY structure describes an overlay to modify. |
| [_D3DDDIARG_UPDATEPALETTE](ns-d3dumddi-_d3dddiarg_updatepalette.md) | The D3DDDIARG_UPDATEPALETTE structure describes parameters that are used to update a texture palette. |
| [_D3DDDIARG_VALIDATETEXTURESTAGESTATE](ns-d3dumddi-_d3dddiarg_validatetexturestagestate.md) | The D3DDDIARG_VALIDATETEXTURESTAGESTATE structure contains the number of passes in which the hardware can perform the blending operations that are specified in the current state. |
| [_D3DDDIARG_VIDEOPROCESSBLT](ns-d3dumddi-_d3dddiarg_videoprocessblt.md) | The D3DDDIARG_VIDEOPROCESSBLT structure describes a Microsoft DirectX Video Acceleration (VA) video processing operation to perform. |
| [_D3DDDIARG_VIDEOPROCESSENDFRAME](ns-d3dumddi-_d3dddiarg_videoprocessendframe.md) | The D3DDDIARG_VIDEOPROCESSENDFRAME structure specifies the Microsoft DirectX Video Accelerator (VA) video process that should stop processing a frame. |
| [_D3DDDIARG_VIEWPORTINFO](ns-d3dumddi-_d3dddiarg_viewportinfo.md) | The D3DDDIARG_VIEWPORTINFO structure describes the location and size of a view-clipping rectangle. |
| [_D3DDDIARG_VOLUMEBLT](ns-d3dumddi-_d3dddiarg_volumeblt.md) | The D3DDDIARG_VOLUMEBLT structure describes parameters for a volume bit-block transfer (bitblt) operation. |
| [_D3DDDIARG_VOLUMEBLT1](ns-d3dumddi-_d3dddiarg_volumeblt1.md) | Describes parameters for a volume bit-block transfer (bitblt) operation. |
| [_D3DDDIARG_WINFO](ns-d3dumddi-_d3dddiarg_winfo.md) | The D3DDDIARG_WINFO structure describes a w range for w buffering. |
| [_D3DDDIARG_ZRANGE](ns-d3dumddi-_d3dddiarg_zrange.md) | The D3DDDIARG_ZRANGE structure specifies z-range minimum and maximum values. |
| [_D3DDDIBOX](ns-d3dumddi-_d3dddibox.md) | Describes the bounds of a volume texture. |
| [_D3DDDICB_ALLOCATE](ns-d3dumddi-_d3dddicb_allocate.md) | The D3DDDICB_ALLOCATE structure contains information for allocating memory. |
| [_D3DDDICB_CREATECONTEXT](ns-d3dumddi-_d3dddicb_createcontext.md) | The D3DDDICB_CREATECONTEXT structure describes a context to create. |
| [_D3DDDICB_CREATECONTEXTVIRTUAL](ns-d3dumddi-_d3dddicb_createcontextvirtual.md) | D3DDDICB_CREATECONTEXTVIRTUAL is used with pfnCreateContextVirtualCb to create contexts that support virtual addressing. |
| [_D3DDDICB_CREATEHWCONTEXT](ns-d3dumddi-_d3dddicb_createhwcontext.md) | A structure that gives information for creating a hardware context. |
| [_D3DDDICB_CREATEHWQUEUE](ns-d3dumddi-_d3dddicb_createhwqueue.md) | A structure that holds information to create a hardware queue. |
| [_D3DDDICB_CREATEOVERLAY](ns-d3dumddi-_d3dddicb_createoverlay.md) | The D3DDDICB_CREATEOVERLAY structure describes overlay hardware. |
| [_D3DDDICB_CREATESYNCHRONIZATIONOBJECT](ns-d3dumddi-_d3dddicb_createsynchronizationobject.md) | The D3DDDICB_CREATESYNCHRONIZATIONOBJECT structure describes a synchronization object that the pfnCreateSynchronizationObjectCb function creates. |
| [_D3DDDICB_CREATESYNCHRONIZATIONOBJECT2](ns-d3dumddi-_d3dddicb_createsynchronizationobject2.md) | Describes a synchronization object that the pfnCreateSynchronizationObject2Cb function creates. |
| [_D3DDDICB_DEALLOCATE](ns-d3dumddi-_d3dddicb_deallocate.md) | The D3DDDICB_DEALLOCATE structure describes allocations to release. |
| [_D3DDDICB_DEALLOCATE2](ns-d3dumddi-_d3dddicb_deallocate2.md) | The D3DDDICB_DEALLOCATE2 structure describes parameters for releasing allocations with pfnDeallocate2Cb. |
| [_D3DDDICB_DESTROYCONTEXT](ns-d3dumddi-_d3dddicb_destroycontext.md) | The D3DDDICB_DESTROYCONTEXT structure contains the handle to a context to destroy. |
| [_D3DDDICB_DESTROYHWCONTEXT](ns-d3dumddi-_d3dddicb_destroyhwcontext.md) | A structure that holds information to destroy a hardware context. |
| [_D3DDDICB_DESTROYHWQUEUE](ns-d3dumddi-_d3dddicb_destroyhwqueue.md) | A structure that holds information to destroy a hardware queue. |
| [_D3DDDICB_DESTROYOVERLAY](ns-d3dumddi-_d3dddicb_destroyoverlay.md) | The D3DDDICB_DESTROYOVERLAY structure contains the handle to the overlay to destroy. |
| [_D3DDDICB_DESTROYSYNCHRONIZATIONOBJECT](ns-d3dumddi-_d3dddicb_destroysynchronizationobject.md) | The D3DDDICB_DESTROYSYNCHRONIZATIONOBJECT structure contains the handle to a synchronization object to destroy. |
| [_D3DDDICB_ESCAPE](ns-d3dumddi-_d3dddicb_escape.md) | The D3DDDICB_ESCAPE structure describes information that a user-mode display driver shares with a display miniport driver. |
| [_D3DDDICB_FLIPOVERLAY](ns-d3dumddi-_d3dddicb_flipoverlay.md) | The D3DDDICB_FLIPOVERLAY structure describes a new allocation to display for the overlay. |
| [_D3DDDICB_FREEGPUVIRTUALADDRESS](ns-d3dumddi-_d3dddicb_freegpuvirtualaddress.md) | D3DDDICB_FREEGPUVIRTUALADDRESS is used with pfnFreeGpuVirtualAddressCb to release a range of graphics processing unit (GPU) virtual addresses that were previously reserved or mapped. |
| [_D3DDDICB_GETMULTISAMPLEMETHODLIST](ns-d3dumddi-_d3dddicb_getmultisamplemethodlist.md) | The D3DDDICB_GETMULTISAMPLEMETHODLIST structure describes parameters to retrieve the list of multiple-sample methods for an allocation. |
| [_D3DDDICB_LOCK](ns-d3dumddi-_d3dddicb_lock.md) | The D3DDDICB_LOCK structure describes parameters for locking an allocation. |
| [_D3DDDICB_LOCK2](ns-d3dumddi-_d3dddicb_lock2.md) | D3DDDICB_LOCK2 describes parameters for locking an allocation. |
| [_D3DDDICB_OFFERALLOCATIONS](ns-d3dumddi-_d3dddicb_offerallocations.md) | Defines the video memory allocations that the driver offers for reuse. Used with the pfnOfferAllocationsCb function. |
| [_D3DDDICB_PRESENT](ns-d3dumddi-_d3dddicb_present.md) | The D3DDDICB_PRESENT structure describes allocations that content is copied to and from. |
| [_D3DDDICB_QUERYADAPTERINFO](ns-d3dumddi-_d3dddicb_queryadapterinfo.md) | The D3DDDICB_QUERYADAPTERINFO structure contains information that describes the graphics adapter. |
| [_D3DDDICB_QUERYRESIDENCY](ns-d3dumddi-_d3dddicb_queryresidency.md) | The D3DDDICB_QUERYRESIDENCY structure describes the residency status of a resource or list of allocations. |
| [_D3DDDICB_RECLAIMALLOCATIONS](ns-d3dumddi-_d3dddicb_reclaimallocations.md) | Describes video memory resources that are to be reclaimed and that the user-mode display driver previously offered for reuse. Used with the pfnReclaimAllocationsCb function. |
| [_D3DDDICB_RECLAIMALLOCATIONS2](ns-d3dumddi-_d3dddicb_reclaimallocations2.md) | D3DDDICB_RECLAIMALLOCATIONS2 is used with pfnReclaimAllocations2Cb to describe video memory resources, previously offered for reuse by the driver, that are to be reclaimed. |
| [_D3DDDICB_RENDER](ns-d3dumddi-_d3dddicb_render.md) | The D3DDDICB_RENDER structure describes the current command buffer to be rendered. |
| [_D3DDDICB_RENDERFLAGS](ns-d3dumddi-_d3dddicb_renderflags.md) | The D3DDDICB_RENDERFLAGS structure identifies information about a command buffer to be rendered. |
| [_D3DDDICB_SETDISPLAYMODE](ns-d3dumddi-_d3dddicb_setdisplaymode.md) | The D3DDDICB_SETDISPLAYMODE structure describes the primary allocation that is used to scan out to the display. |
| [_D3DDDICB_SETDISPLAYPRIVATEDRIVERFORMAT](ns-d3dumddi-_d3dddicb_setdisplayprivatedriverformat.md) | The D3DDDICB_SETDISPLAYPRIVATEDRIVERFORMAT structure describes the private-format attribute to set for a video present source in a call to the pfnSetDisplayPrivateDriverFormatCb function. |
| [_D3DDDICB_SETPRIORITY](ns-d3dumddi-_d3dddicb_setpriority.md) | The D3DDDICB_SETPRIORITY structure describes the priority level to which to set a resource or list of allocations. |
| [_D3DDDICB_SIGNALSYNCHRONIZATIONOBJECT](ns-d3dumddi-_d3dddicb_signalsynchronizationobject.md) | The D3DDDICB_SIGNALSYNCHRONIZATIONOBJECT structure describes the parameters that are required to set up signaling in a call to the pfnSignalSynchronizationObjectCb function. |
| [_D3DDDICB_SIGNALSYNCHRONIZATIONOBJECT2](ns-d3dumddi-_d3dddicb_signalsynchronizationobject2.md) | Describes the parameters that are required to set up signaling in a call to the pfnSignalSynchronizationObject2Cb function. |
| [_D3DDDICB_SUBMITCOMMAND](ns-d3dumddi-_d3dddicb_submitcommand.md) | The D3DDDICB_SUBMITCOMMAND structure is used to submit command buffers on contexts that support graphics processing unit (GPU) virtual addressing. |
| [_D3DDDICB_SUBMITCOMMANDFLAGS](ns-d3dumddi-_d3dddicb_submitcommandflags.md) | D3DDDICB_SUBMITCOMMANDFLAGS is used to indicate how to process command buffers on contexts that support graphics processing unit (GPU) virtual addressing. |
| [_D3DDDICB_SUBMITCOMMANDTOHWQUEUE](ns-d3dumddi-_d3dddicb_submitcommandtohwqueue.md) | A structure that holds information to queue hardware flags. |
| [_D3DDDICB_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE](ns-d3dumddi-_d3dddicb_submitsignalsyncobjectstohwqueue.md) | A structure that holds information to submit a signal synchronization object to a hardware queue. |
| [_D3DDDICB_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE](ns-d3dumddi-_d3dddicb_submitwaitforsyncobjectstohwqueue.md) | A structure that holds information to wait for synchronized objects. |
| [_D3DDDICB_UNLOCK](ns-d3dumddi-_d3dddicb_unlock.md) | The D3DDDICB_UNLOCK structure describes allocations to unlock. |
| [_D3DDDICB_UNLOCK2](ns-d3dumddi-_d3dddicb_unlock2.md) | D3DDDICB_UNLOCK2 describes an allocation to unlock. |
| [_D3DDDICB_UPDATEGPUVIRTUALADDRESS](ns-d3dumddi-_d3dddicb_updategpuvirtualaddress.md) | D3DDDICB_UPDATEGPUVIRTUALADDRESS is used with pfnUpdateGpuVirtualAddressCb to allow the user mode driver to specify a number of mapping operations to be applied to the process virtual address space in a single batch of page table updates. |
| [_D3DDDICB_UPDATEOVERLAY](ns-d3dumddi-_d3dddicb_updateoverlay.md) | The D3DDDICB_UPDATEOVERLAY structure describes parameters for modifying an overlay. |
| [_D3DDDICB_WAITFORSYNCHRONIZATIONOBJECT](ns-d3dumddi-_d3dddicb_waitforsynchronizationobject.md) | The D3DDDICB_WAITFORSYNCHRONIZATIONOBJECT structure describes the parameters that are required to set up the wait in a call to the pfnWaitForSynchronizationObjectCb function. |
| [_D3DDDICB_WAITFORSYNCHRONIZATIONOBJECT2](ns-d3dumddi-_d3dddicb_waitforsynchronizationobject2.md) | Describes the parameters that are required to set up the wait in a call to the pfnWaitForSynchronizationObject2Cb function. |
| [_D3DDDIDEVINFO_VCACHE](ns-d3dumddi-_d3dddidevinfo_vcache.md) | The D3DDDIDEVINFO_VCACHE structure describes the vertex-cache information of a device. |
| [_D3DDDIENCRYPTED_BLOCK_INFO](ns-d3dumddi-_d3dddiencrypted_block_info.md) | The D3DDDIENCRYPTED_BLOCK_INFO structure describes the portions of a buffer that are encrypted. |
| [_D3DDDIRANGE](ns-d3dumddi-_d3dddirange.md) | Specifies a range of memory within a buffer. |
| [_D3DDDIVERTEXELEMENT](ns-d3dumddi-_d3dddivertexelement.md) | The D3DDDIVERTEXELEMENT structure describes an element in the array for a vertex shader declaration. |
| [_DDICERTIFICATEINFO](ns-d3dumddi-_ddicertificateinfo.md) | The DDICERTIFICATEINFO structure describes information about the certificate that the driver uses. |
| [_DDICHECKOVERLAYSUPPORTINPUT](ns-d3dumddi-_ddicheckoverlaysupportinput.md) | The DDICHECKOVERLAYSUPPORTINPUT structure describes an overlay display mode that the user-mode display driver uses to verify overlay support. |
| [_DDICONTENTPROTECTIONCAPS](ns-d3dumddi-_ddicontentprotectioncaps.md) | The DDICONTENTPROTECTIONCAPS structure describes a specific encryption and decode combination that the driver uses. |
| [_DDIGAMMACAPS](ns-d3dumddi-_ddigammacaps.md) | The DDIGAMMACAPS structure describes gamma-ramp capabilities that the user-mode display driver supports. |
| [_DDIMULTISAMPLEQUALITYLEVELSDATA](ns-d3dumddi-_ddimultisamplequalitylevelsdata.md) | The DDIMULTISAMPLEQUALITYLEVELSDATA structure describes the number of multiple-sample quality levels for a given render-target format. |
| [_DDRAW_CAPS](ns-d3dumddi-_ddraw_caps.md) | The DDRAW_CAPS structure describes general Microsoft DirectDraw capabilities that the user-mode display driver supports. |
| [_DDRAW_MODE_SPECIFIC_CAPS](ns-d3dumddi-_ddraw_mode_specific_caps.md) | The DDRAW_MODE_SPECIFIC_CAPS structure describes Microsoft DirectDraw capabilities that are specific to a particular display device (head) on the graphics card. |
| [_DXVADDI_AYUVSAMPLE16](ns-d3dumddi-_dxvaddi_ayuvsample16.md) | The DXVADDI_AYUVSAMPLE16 structure describes 16-bit Cr, Cb, and Y color values and an associated opacity. |
| [_DXVADDI_AYUVSAMPLE8](ns-d3dumddi-_dxvaddi_ayuvsample8.md) | The DXVADDI_AYUVSAMPLE8 structure describes 8-bit Cr, Cb, and Y color values and an associated opacity. |
| [_DXVADDI_CONFIGPICTUREDECODE](ns-d3dumddi-_dxvaddi_configpicturedecode.md) | The DXVADDI_CONFIGPICTUREDECODE structure describes the configuration for compressed picture decoding. |
| [_DXVADDI_DECODEBUFFERDESC](ns-d3dumddi-_dxvaddi_decodebufferdesc.md) | The DXVADDI_DECODEBUFFERDESC structure describes a buffer that is currently passed from the host decoder to the accelerator. |
| [_DXVADDI_DECODEBUFFERINFO](ns-d3dumddi-_dxvaddi_decodebufferinfo.md) | The DXVADDI_DECODEBUFFERINFO structure describes information about a particular type of compressed buffer that is required for a video decoding scenario. |
| [_DXVADDI_DECODEINPUT](ns-d3dumddi-_dxvaddi_decodeinput.md) | The DXVADDI_DECODEINPUT structure describes a render target format that is supported by a Microsoft DirectX Video Acceleration (DirectX VA) decode type. |
| [_DXVADDI_EXTENDEDFORMAT](ns-d3dumddi-_dxvaddi_extendedformat.md) | The DXVADDI_EXTENDEDFORMAT structure describes the extended format of the video frame. |
| [_DXVADDI_FILTERVALUES](ns-d3dumddi-_dxvaddi_filtervalues.md) | The DXVADDI_FILTERVALUES structure describes values that are related to a filter. |
| [_DXVADDI_FIXED32](ns-d3dumddi-_dxvaddi_fixed32.md) | The DXVADDI_FIXED32 structure describes a floating-point number from a 16.16 fixed-point number. |
| [_DXVADDI_FREQUENCY](ns-d3dumddi-_dxvaddi_frequency.md) | The DXVADDI_FREQUENCY structure describes the video frame rate in Hertz (Hz). For example, NTSC TV is 60000 over 1001. |
| [_DXVADDI_PRIVATEBUFFER](ns-d3dumddi-_dxvaddi_privatebuffer.md) | The DXVADDI_PRIVATEBUFFER structure describes a private buffer that a nonstandard decoder uses to perform a decode operation. |
| [_DXVADDI_PRIVATEDATA](ns-d3dumddi-_dxvaddi_privatedata.md) | The DXVADDI_PRIVATEDATA structure describes data that is required for a particular decoder to operate. |
| [_DXVADDI_PROCAMPVALUES](ns-d3dumddi-_dxvaddi_procampvalues.md) | The DXVADDI_PROCAMPVALUES structure describes the ProcAmp control adjustment values. |
| [_DXVADDI_PVP_SETKEY](ns-d3dumddi-_dxvaddi_pvp_setkey.md) | The DXVADDI_PVP_SETKEY structure describes a key that the decode device uses to start decoding a frame. |
| [_DXVADDI_QUERYEXTENSIONCAPSINPUT](ns-d3dumddi-_dxvaddi_queryextensioncapsinput.md) | The DXVADDI_QUERYEXTENSIONCAPSINPUT structure describes a capability of an extension GUID that information is requested for. |
| [_DXVADDI_QUERYFILTERPROPERTYRANGEINPUT](ns-d3dumddi-_dxvaddi_queryfilterpropertyrangeinput.md) | The DXVADDI_QUERYFILTERPROPERTYRANGEINPUT structure describes a filter setting on a video stream that range information is requested for. |
| [_DXVADDI_QUERYPROCAMPINPUT](ns-d3dumddi-_dxvaddi_queryprocampinput.md) | The DXVADDI_QUERYPROCAMPINPUT structure describes a ProcAmp control property on a video stream that range information is requested for. |
| [_DXVADDI_VALUERANGE](ns-d3dumddi-_dxvaddi_valuerange.md) | The DXVADDI_VALUERANGE structure describes values of a property (such as, the value spread and default value). |
| [_DXVADDI_VIDEODESC](ns-d3dumddi-_dxvaddi_videodesc.md) | The DXVADDI_VIDEODESC structure describes a video stream. |
| [_DXVADDI_VIDEOPROCESSBLTFLAGS](ns-d3dumddi-_dxvaddi_videoprocessbltflags.md) | The DXVADDI_VIDEOPROCESSBLTFLAGS structure identifies changes in the current destination surface from the previous destination surface. |
| [_DXVADDI_VIDEOPROCESSORCAPS](ns-d3dumddi-_dxvaddi_videoprocessorcaps.md) | The DXVADDI_VIDEOPROCESSORCAPS structure describes the video processing capabilities of a specific deinterlace mode. |
| [_DXVADDI_VIDEOPROCESSORINPUT](ns-d3dumddi-_dxvaddi_videoprocessorinput.md) | The DXVADDI_VIDEOPROCESSORINPUT structure describes a video stream that is processed by a video processing device type. |
| [_DXVADDI_VIDEOSAMPLE](ns-d3dumddi-_dxvaddi_videosample.md) | The DXVADDI_VIDEOSAMPLE structure describes the format of a video sample that is used in a video processing operation. |
| [_DXVADDI_VIDEOSAMPLEFLAGS](ns-d3dumddi-_dxvaddi_videosampleflags.md) | The DXVADDI_VIDEOSAMPLEFLAGS structure identifies changes in the current sample frame from the previous sample frame. |
| [_DXVAHDDDI_BLT_STATE_ALPHA_FILL_DATA](ns-d3dumddi-_dxvahdddi_blt_state_alpha_fill_data.md) | The DXVAHDDDI_BLT_STATE_ALPHA_FILL_DATA structure describes data that specifies the alpha-fill mode of the output. |
| [_DXVAHDDDI_BLT_STATE_BACKGROUND_COLOR_DATA](ns-d3dumddi-_dxvahdddi_blt_state_background_color_data.md) | The DXVAHDDDI_BLT_STATE_BACKGROUND_COLOR_DATA structure describes data that specifies the background color to fill in the target rectangle of the output. |
| [_DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA](ns-d3dumddi-_dxvahdddi_blt_state_constriction_data.md) | The DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA structure describes data that specifies the down-sampling of the output. |
| [_DXVAHDDDI_BLT_STATE_OUTPUT_COLOR_SPACE_DATA](ns-d3dumddi-_dxvahdddi_blt_state_output_color_space_data.md) | The DXVAHDDDI_BLT_STATE_OUTPUT_COLOR_SPACE_DATA structure describes data that specifies the color space of the output. |
| [_DXVAHDDDI_BLT_STATE_PRIVATE_DATA](ns-d3dumddi-_dxvahdddi_blt_state_private_data.md) | The DXVAHDDDI_BLT_STATE_PRIVATE_DATA structure describes data that specifies the private bit-block transfer (bitblt) state. |
| [_DXVAHDDDI_BLT_STATE_TARGET_RECT_DATA](ns-d3dumddi-_dxvahdddi_blt_state_target_rect_data.md) | The DXVAHDDDI_BLT_STATE_TARGET_RECT_DATA structure describes data that specifies the target rectangle of the output. |
| [_DXVAHDDDI_COLOR](ns-d3dumddi-_dxvahdddi_color.md) | The DXVAHDDDI_COLOR union contains information that specifies color with either a YCbCr or RGB color structure. |
| [_DXVAHDDDI_COLOR_RGBA](ns-d3dumddi-_dxvahdddi_color_rgba.md) | The DXVAHDDDI_COLOR_RGBA structure describes color in RGB terms. |
| [_DXVAHDDDI_COLOR_YCbCrA](ns-d3dumddi-_dxvahdddi_color_ycbcra.md) | The DXVAHDDDI_COLOR_YCbCrA structure describes color in YCbCr terms. |
| [_DXVAHDDDI_CONTENT_DESC](ns-d3dumddi-_dxvahdddi_content_desc.md) | The DXVAHDDDI_CONTENT_DESC structure describes the video content that a decode device processes. |
| [_DXVAHDDDI_CUSTOM_RATE_DATA](ns-d3dumddi-_dxvahdddi_custom_rate_data.md) | The DXVAHDDDI_CUSTOM_RATE_DATA structure describes the video content that a decode device processes. |
| [_DXVAHDDDI_DEVICE_DESC](ns-d3dumddi-_dxvahdddi_device_desc.md) | The DXVAHDDDI_DEVICE_DESC structure describes a decode device. |
| [_DXVAHDDDI_FILTER_RANGE_DATA](ns-d3dumddi-_dxvahdddi_filter_range_data.md) | Describes a filter range. |
| [_DXVAHDDDI_RATIONAL](ns-d3dumddi-_dxvahdddi_rational.md) | The DXVAHDDDI_RATIONAL structure describes a fractional value that represents the vertical and horizontal frequencies of a video mode (that is, vertical sync and horizontal sync). |
| [_DXVAHDDDI_STREAM_DATA](ns-d3dumddi-_dxvahdddi_stream_data.md) | The DXVAHDDDI_STREAM_DATA structure describes an input stream that is processed. |
| [_DXVAHDDDI_STREAM_STATE_ALPHA_DATA](ns-d3dumddi-_dxvahdddi_stream_state_alpha_data.md) | The DXVAHDDDI_STREAM_STATE_ALPHA_DATA structure describes stream-state data that specifies the alpha blend level per-plane. |
| [_DXVAHDDDI_STREAM_STATE_ASPECT_RATIO_DATA](ns-d3dumddi-_dxvahdddi_stream_state_aspect_ratio_data.md) | The DXVAHDDDI_STREAM_STATE_ASPECT_RATIO_DATA structure describes stream-state data that specifies the pixel aspect ratio. |
| [_DXVAHDDDI_STREAM_STATE_DESTINATION_RECT_DATA](ns-d3dumddi-_dxvahdddi_stream_state_destination_rect_data.md) | The DXVAHDDDI_STREAM_STATE_DESTINATION_RECT_DATA structure describes stream-state data that specifies the destination rectangle. The driver scales the source rectangle within the input surface to the destination rectangle within the output surface. |
| [_DXVAHDDDI_STREAM_STATE_FILTER_DATA](ns-d3dumddi-_dxvahdddi_stream_state_filter_data.md) | The DXVAHDDDI_STREAM_STATE_FILTER_DATA structure describes stream-state data that specifies the filter level. |
| [_DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA](ns-d3dumddi-_dxvahdddi_stream_state_frame_format_data.md) | The DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA structure describes data that specifies the frame format of the input. |
| [_DXVAHDDDI_STREAM_STATE_INPUT_COLOR_SPACE_DATA](ns-d3dumddi-_dxvahdddi_stream_state_input_color_space_data.md) | The DXVAHDDDI_STREAM_STATE_INPUT_COLOR_SPACE_DATA structure describes stream-state data that specifies the color space of the input stream. |
| [_DXVAHDDDI_STREAM_STATE_LUMA_KEY_DATA](ns-d3dumddi-_dxvahdddi_stream_state_luma_key_data.md) | The DXVAHDDDI_STREAM_STATE_LUMA_KEY_DATA structure describes stream-state data that specifies the luma key of the input. The driver assumes that a pixel that has a luma value within the luma-key range is transparent. |
| [_DXVAHDDDI_STREAM_STATE_OUTPUT_RATE_DATA](ns-d3dumddi-_dxvahdddi_stream_state_output_rate_data.md) | The DXVAHDDDI_STREAM_STATE_OUTPUT_RATE_DATA structure describes stream-state data that specifies the output rate of the input stream. |
| [_DXVAHDDDI_STREAM_STATE_PALETTE_DATA](ns-d3dumddi-_dxvahdddi_stream_state_palette_data.md) | The DXVAHDDDI_STREAM_STATE_PALETTE_DATA structure describes stream-state data that specifies the palette entries of the input. |
| [_DXVAHDDDI_STREAM_STATE_PRIVATE_DATA](ns-d3dumddi-_dxvahdddi_stream_state_private_data.md) | The DXVAHDDDI_STREAM_STATE_PRIVATE_DATA structure describes stream-state data that specifies a private stream state. |
| [_DXVAHDDDI_STREAM_STATE_PRIVATE_IVTC_DATA](ns-d3dumddi-_dxvahdddi_stream_state_private_ivtc_data.md) | The DXVAHDDDI_STREAM_STATE_PRIVATE_IVTC_DATA structure describes private stream-state data that is used to query the inverse telecine statistics from the driver. |
| [_DXVAHDDDI_STREAM_STATE_ROTATION_DATA](ns-d3dumddi-_dxvahdddi_stream_state_rotation_data.md) | Describes stream-state data that specifies the clockwise rotation of the display output surface. |
| [_DXVAHDDDI_STREAM_STATE_SOURCE_RECT_DATA](ns-d3dumddi-_dxvahdddi_stream_state_source_rect_data.md) | The DXVAHDDDI_STREAM_STATE_SOURCE_RECT_DATA structure describes stream-state data that specifies the source rectangle of the input stream. |
| [_DXVAHDDDI_SURFACE](ns-d3dumddi-_dxvahdddi_surface.md) | The DXVAHDDDI_SURFACE structure describes a surface. |
| [_DXVAHDDDI_VPCAPS](ns-d3dumddi-_dxvahdddi_vpcaps.md) | Describes a video processor and its capabilities. |
| [_DXVAHDDDI_VPDEVCAPS](ns-d3dumddi-_dxvahdddi_vpdevcaps.md) | The DXVAHDDDI_VPDEVCAPS structure describes the video processor capabilities that the decode device supports. |
| [_FORMATOP](ns-d3dumddi-_formatop.md) | The FORMATOP structure describes a surface format and operations that can be performed with such a surface. |
| [_GETENCRYPTIONBLTKEY](ns-d3dumddi-_getencryptionbltkey.md) | The _GETENCRYPTIONBLTKEY structure describes an encrypted bit-block transfer (bitblt) session for which the GetEncryptionBltKey function retrieves the encryption key. |
| [D3DDDI_MULTIPLANE_OVERLAY_ALLOCATION_INFO](ns-d3dumddi-d3dddi_multiplane_overlay_allocation_info.md) | Specifies info about a multiplane overlay allocation. |
| [D3DDDI_MULTIPLANE_OVERLAY_CAPS](ns-d3dumddi-d3dddi_multiplane_overlay_caps.md) | Used by the user-mode display driver to specify overlay plane capabilities. |
| [D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS](ns-d3dumddi-d3dddi_multiplane_overlay_group_caps.md) | Used by the user-mode display driver to specify a group of overlay plane capabilities. |
| [D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS_INPUT](ns-d3dumddi-d3dddi_multiplane_overlay_group_caps_input.md) | Specifies info on a multiplane overlay capability group. |
| [D3DDDIARG_CHECKPRESENTDURATIONSUPPORT](ns-d3dumddi-d3dddiarg_checkpresentdurationsupport.md) | Used in a call to the CheckPresentDurationSupport function to check details on hardware device support for seamlessly switching to a new monitor refresh rate. |
| [D3DDDIARG_COPYFLAGS](ns-d3dumddi-d3dddiarg_copyflags.md) | Describes how to handle the existing contents of a resource during a copy or update operation of a region within that resource. Used by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [D3DDDIARG_COUNTER_INFO](ns-d3dumddi-d3dddiarg_counter_info.md) | Describes info to manipulate counters. |
| [D3DDDIARG_PRESENTMULTIPLANEOVERLAY](ns-d3dumddi-d3dddiarg_presentmultiplaneoverlay.md) | Specifies a multiplane overlay resource to display. |
| [D3DDDIARG_PRESENTSURFACE](ns-d3dumddi-d3dddiarg_presentsurface.md) | Describes a surface to display. |
| [D3DDDIARG_TRIMRESIDENCYSET](ns-d3dumddi-d3dddiarg_trimresidencyset.md) | D3DDDIARG_TRIMRESIDENCYSET is used with pfnTrimResidencySet by a user mode driver to trim the residency list for a given device. |
| [D3DDDIARG_UPDATESUBRESOURCEUP](ns-d3dumddi-d3dddiarg_updatesubresourceup.md) | Describes info that's used to update a destination subresource region from a source system-memory region. Used by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [D3DDDICAPS_ARCHITECTURE_INFO](ns-d3dumddi-d3dddicaps_architecture_info.md) | Describes information about display adapter architecture. |
| [D3DDDICAPS_SHADER_MIN_PRECISION_SUPPORT](ns-d3dumddi-d3dddicaps_shader_min_precision_support.md) | Describes precision support options for shaders in the user-mode display driver. |
| [D3DDDICAPS_SIMPLE_INSTANCING_SUPPORT](ns-d3dumddi-d3dddicaps_simple_instancing_support.md) | Describes whether simple instancing is supported. |
| [D3DDDICB_CREATEPAGINGQUEUE](ns-d3dumddi-d3dddicb_createpagingqueue.md) | D3DDDICB_CREATEPAGINGQUEUE is used with pfnCreatePagingQueueCb to create a device paging queue that can be used to synchronize with video memory management operations for the device, such as making the device resource resident. |
| [D3DDDICB_EVICT](ns-d3dumddi-d3dddicb_evict.md) | D3DKMT_EVICT is used with pfnEvictCb to subtract one from the residency reference count. |
| [D3DDDICB_LOGUMDMARKER](ns-d3dumddi-d3dddicb_logumdmarker.md) | Specifies info about the location of an Event Tracing for Windows (ETW) marker event that the user-mode display driver has defined. |
| [D3DDDICB_PRESENTMULTIPLANEOVERLAY](ns-d3dumddi-d3dddicb_presentmultiplaneoverlay.md) | Describes multiplane overlay allocations that content is copied to and from. |
| [D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMCPU](ns-d3dumddi-d3dddicb_signalsynchronizationobjectfromcpu.md) | D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMCPU is used with pfnSignalSynchronizationObjectFromCpuCb to enable a driver to signal a monitored fence. |
| [D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU](ns-d3dumddi-d3dddicb_signalsynchronizationobjectfromgpu.md) | D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU is used with pfnSignalSynchronizationObjectFromGpuCb to signal a monitored fence. |
| [D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2](ns-d3dumddi-d3dddicb_signalsynchronizationobjectfromgpu2.md) | D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2 is used with pfnSignalSynchronizationObjectFromGpu2Cb to signal a monitored fence. |
| [D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU](ns-d3dumddi-d3dddicb_waitforsynchronizationobjectfromcpu.md) | D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU is used with pfnWaitForSynchronizationObjectFromCpuCb to wait for a monitored fence to reach a certain value. |
| [D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMGPU](ns-d3dumddi-d3dddicb_waitforsynchronizationobjectfromgpu.md) | D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMGPU is used with pfnWaitForSynchronizationObjectFromGpuCb to wait for a monitored fence to reach a certain value. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_D3DDDI_CERTIFICATETYPE](ne-d3dumddi-_d3dddi_certificatetype.md) | The D3DDDI_CERTIFICATETYPE enumeration contains values that identify certificate types. |
| [_D3DDDI_DEVICEEXECUTION_STATE](ne-d3dumddi-_d3dddi_deviceexecution_state.md) | Indicates the state of the device. |
| [_D3DDDI_MULTIPLANE_OVERLAY_BLEND](ne-d3dumddi-_d3dddi_multiplane_overlay_blend.md) | Identifies a blend operation to be performed on an overlay plane. |
| [_D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS](ne-d3dumddi-_d3dddi_multiplane_overlay_feature_caps.md) | Identifies overlay capabilities. |
| [_D3DDDI_MULTIPLANE_OVERLAY_FLAGS](ne-d3dumddi-_d3dddi_multiplane_overlay_flags.md) | Identifies a flip operation to be performed on an overlay plane. |
| [_D3DDDICAPS_TYPE](ne-d3dumddi-_d3dddicaps_type.md) | The D3DDDICAPS_TYPE enumeration type contains values that identify the type of capability information that is received from a call to the driver's GetCaps function. |
| [_DDIAUTHENTICATEDCHANNELTYPE](ne-d3dumddi-_ddiauthenticatedchanneltype.md) | The DDIAUTHENTICATEDCHANNELTYPE enumeration contains values that identify authenticated-channel types. |
| [_DXVADDI_NOMINALRANGE](ne-d3dumddi-_dxvaddi_nominalrange.md) | The DXVADDI_NOMINALRANGE enumeration type contains values that identify whether sample data includes headroom (that is, values beyond 1.0 white) and toeroom (that is, superblacks below the reference 0.0 black). |
| [_DXVADDI_SAMPLEFORMAT](ne-d3dumddi-_dxvaddi_sampleformat.md) | The DXVADDI_SAMPLEFORMAT enumeration type contains values that identify how a video frame is sampled. |
| [_DXVADDI_VIDEOCHROMASUBSAMPLING](ne-d3dumddi-_dxvaddi_videochromasubsampling.md) | The DXVADDI_VIDEOCHROMASUBSAMPLING enumeration type contains values that identify the chroma encoding scheme for Y'Cb'Cr' data. |
| [_DXVADDI_VIDEOLIGHTING](ne-d3dumddi-_dxvaddi_videolighting.md) | The DXVADDI_VIDEOLIGHTING enumeration type contains values that identify lighting conditions for viewing video. |
| [_DXVADDI_VIDEOPRIMARIES](ne-d3dumddi-_dxvaddi_videoprimaries.md) | The DXVADDI_VIDEOPRIMARIES enumeration type contains values that identify the color primaries, which state which RGB basis functions are used. |
| [_DXVADDI_VIDEOTRANSFERFUNCTION](ne-d3dumddi-_dxvaddi_videotransferfunction.md) | The DXVADDI_VIDEOTRANSFERFUNCTION enumeration type contains values that identify the conversion function from R'G'B' to RGB. |
| [_DXVADDI_VIDEOTRANSFERMATRIX](ne-d3dumddi-_dxvaddi_videotransfermatrix.md) | The DXVADDI_VIDEOTRANSFERMATRIX enumeration type contains values that identify the conversion matrix from Y'Cb'Cr' to (studio) R'G'B'. |
| [_DXVAHDDDI_ALPHA_FILL_MODE](ne-d3dumddi-_dxvahdddi_alpha_fill_mode.md) | The DXVAHDDDI_ALPHA_FILL_MODE enumeration contains values that identify the type of alpha fill mode to set. |
| [_DXVAHDDDI_BLT_STATE](ne-d3dumddi-_dxvahdddi_blt_state.md) | The DXVAHDDDI_BLT_STATE enumeration contains values that identify the bit-block transfer (bitblt) state data for a video processor. |
| [_DXVAHDDDI_DEVICE_USAGE](ne-d3dumddi-_dxvahdddi_device_usage.md) | The DXVAHDDDI_DEVICE_USAGE enumeration contains values that identify how the decode device plays video. |
| [_DXVAHDDDI_FILTER](ne-d3dumddi-_dxvahdddi_filter.md) | The DXVAHDDDI_FILTER enumeration contains values that identify the filter range, which the driver should retrieve when the driver's GetCaps function is called with the D3DDDICAPS_DXVAHD_GETVPFILTERRANGE value set. |
| [_DXVAHDDDI_FRAME_FORMAT](ne-d3dumddi-_dxvahdddi_frame_format.md) | The DXVAHDDDI_FRAME_FORMAT enumeration contains values that identify the frame format. |
| [_DXVAHDDDI_NOMINAL_RANGE](ne-d3dumddi-_dxvahdddi_nominal_range.md) | Indicates the luminance range of YUV data. |
| [_DXVAHDDDI_OUTPUT_RATE](ne-d3dumddi-_dxvahdddi_output_rate.md) | The DXVAHDDDI_OUTPUT_RATE enumeration contains values that identify the output rate that the driver should use. |
| [_DXVAHDDDI_ROTATION](ne-d3dumddi-_dxvahdddi_rotation.md) | Specifies the clockwise rotation of the display output surface. |
| [_DXVAHDDDI_STREAM_STATE](ne-d3dumddi-_dxvahdddi_stream_state.md) | The DXVAHDDDI_STREAM_STATE enumeration contains values that identify the stream-state data for a video processor. |
| [D3DDDI_CHECK_DIRECT_FLIP_FLAGS](ne-d3dumddi-d3dddi_check_direct_flip_flags.md) | Used by the CheckDirectFlipFlags parameter of the CheckDirectFlipSupport function to specify seamless flipping of video memory. |
| [D3DDDI_COPY_FLAGS](ne-d3dumddi-d3dddi_copy_flags.md) | Specifies how to handle the existing contents of a resource during a copy or update operation of a region within that resource. |
| [D3DDDI_FLUSH_FLAGS](ne-d3dumddi-d3dddi_flush_flags.md) | In calls to the pfnFlush1 function, indicates whether the driver should free as much memory as possible. Used by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [D3DDDI_MARKERLOGTYPE](ne-d3dumddi-d3dddi_markerlogtype.md) | Indicates the type of marker in the Event Tracing for Windows (ETW) log that the user-mode display driver supports. |
| [D3DDDI_MARKERTYPE](ne-d3dumddi-d3dddi_markertype.md) | Indicates the type of Event Tracing for Windows (ETW) marker event that the user-mode display driver supports. |
| [D3DDDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY](ne-d3dumddi-d3dddi_multiplane_overlay_stretch_quality.md) | Identifies filtering processes that the hardware should perform when it stretches or shrinks multiplane overlay data. |
| [D3DDDI_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT](ne-d3dumddi-d3dddi_multiplane_overlay_video_frame_format.md) | Identifies the overlay plane's video frame format. Only the D3DDDI_MULIIPLANE_OVERLAY_VIDEO_FRAME_FORMAT_PROGRESSIVE value is supported. |
| [D3DDDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS](ne-d3dumddi-d3dddi_multiplane_overlay_ycbcr_flags.md) | Identifies YUV range and conversion info that describes a multiplane overlay. |
| [D3DDDICAPS_SHADER_MIN_PRECISION](ne-d3dumddi-d3dddicaps_shader_min_precision.md) | Specifies minimum precision levels that the user-mode driver supports in shaders. |