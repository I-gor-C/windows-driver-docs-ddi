# Declarations in the d3dkmthk header
This header D3Dkmthk contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [D3DKMTChangeVideoMemoryReservation function](nf-d3dkmthk-d3dkmtchangevideomemoryreservation.md) | TBD |
| [D3DKMTAcquireKeyedMutex2 function](nf-d3dkmthk-d3dkmtacquirekeyedmutex2.md) | Acquires a keyed mutex object that includes private data. |
| [D3DKMTCreateHwQueue function](nf-d3dkmthk-d3dkmtcreatehwqueue.md) | Used to create a new hardware queue. |
| [D3DKMTQueryProcessOfferInfo function](nf-d3dkmthk-d3dkmtqueryprocessofferinfo.md) | TBD |
| [D3DKMTCheckVidPnExclusiveOwnership function](nf-d3dkmthk-d3dkmtcheckvidpnexclusiveownership.md) | The D3DKMTCheckVidPnExclusiveOwnership function determines the video present source in the path of a video present network (VidPN) topology that exclusively owns the VidPN. |
| [D3DKMTSetVidPnSourceOwner2 function](nf-d3dkmthk-d3dkmtsetvidpnsourceowner2.md) | Used to set the VidPN source owner. |
| [D3DKMTSignalSynchronizationObject function](nf-d3dkmthk-d3dkmtsignalsynchronizationobject.md) | The D3DKMTSignalSynchronizationObject function inserts a signal for the specified synchronization objects in the specified context stream. |
| [D3DKMTSubmitWaitForSyncObjectsToHwQueue function](nf-d3dkmthk-d3dkmtsubmitwaitforsyncobjectstohwqueue.md) | TBD |
| [D3DKMTTrimProcessCommitment function](nf-d3dkmthk-d3dkmttrimprocesscommitment.md) | TBD |
| [D3DKMTWaitForSynchronizationObjectFromGpu function](nf-d3dkmthk-d3dkmtwaitforsynchronizationobjectfromgpu.md) | D3DKMTWaitForSynchronizationObjectFromGpu waits for a monitored fence to reach a certain value before processing subsequent context commands. |
| [D3DKMTDestroySynchronizationObject function](nf-d3dkmthk-d3dkmtdestroysynchronizationobject.md) | The D3DKMTDestroySynchronizationObject function destroys a kernel-mode synchronization object. |
| [D3DKMTGetResourcePresentPrivateDriverData function](nf-d3dkmthk-d3dkmtgetresourcepresentprivatedriverdata.md) | TBD |
| [D3DKMTGetMultiPlaneOverlayCaps function](nf-d3dkmthk-d3dkmtgetmultiplaneoverlaycaps.md) | TBD |
| [D3DKMTGetSetSwapChainMetadata function](nf-d3dkmthk-d3dkmtgetsetswapchainmetadata.md) | TBD |
| [D3DKMTOpenAdapterFromHdc function](nf-d3dkmthk-d3dkmtopenadapterfromhdc.md) | The D3DKMTOpenAdapterFromHdc function maps a device context handle (HDC) to a graphics adapter handle and, if the adapter contains multiple monitor outputs, to one of those outputs. |
| [D3DKMTOpenResourceFromNtHandle function](nf-d3dkmthk-d3dkmtopenresourcefromnthandle.md) | Opens a shared resource from an NT handle. |
| [D3DKMTCreateKeyedMutex2 function](nf-d3dkmthk-d3dkmtcreatekeyedmutex2.md) | Creates a keyed mutex object that includes private data. |
| [D3DKMTSetGammaRamp function](nf-d3dkmthk-d3dkmtsetgammaramp.md) | The D3DKMTSetGammaRamp function sets the gamma ramp. |
| [D3DKMTCreateDevice function](nf-d3dkmthk-d3dkmtcreatedevice.md) | The D3DKMTCreateDevice function creates a kernel-mode device context. |
| [D3DKMTDestroyHwContext function](nf-d3dkmthk-d3dkmtdestroyhwcontext.md) | TBD |
| [D3DKMTOpenResource2 function](nf-d3dkmthk-d3dkmtopenresource2.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMTCreateBundleObject function](nf-d3dkmthk-d3dkmtcreatebundleobject.md) | Used to create a bundle object. |
| [D3DKMTWaitForVerticalBlankEvent2 function](nf-d3dkmthk-d3dkmtwaitforverticalblankevent2.md) | Waits for specified wait objects, including a vertical blank event, to occur and then returns. Supported starting with Windows 8. |
| [D3DKMTCreateSynchronizationObject2 function](nf-d3dkmthk-d3dkmtcreatesynchronizationobject2.md) | The D3DKMTCreateSynchronizationObject2 function creates a kernel-mode synchronization object. |
| [D3DKMTCheckOcclusion function](nf-d3dkmthk-d3dkmtcheckocclusion.md) | The D3DKMTCheckOcclusion function verifies whether the client area of a window is occluded. |
| [D3DKMTSharedPrimaryUnLockNotification function](nf-d3dkmthk-d3dkmtsharedprimaryunlocknotification.md) | The D3DKMTSharedPrimaryUnLockNotification function notifies the operating system that a shared primary surface was unlocked. |
| [D3DKMTOpenNtHandleFromName function](nf-d3dkmthk-d3dkmtopennthandlefromname.md) | From a given graphics adapter name, opens an NT handle to the process. |
| [D3DKMTSetProcessSchedulingPriorityClass function](nf-d3dkmthk-d3dkmtsetprocessschedulingpriorityclass.md) | The D3DKMTSetProcessSchedulingPriorityClass function sets the scheduling priority for a process. |
| [D3DKMTSetQueuedLimit function](nf-d3dkmthk-d3dkmtsetqueuedlimit.md) | The D3DKMTSetQueuedLimit function sets or retrieves the limit for the number of operations of the given type that can be queued for the given device. |
| [D3DKMTUnregisterTrimNotification function](nf-d3dkmthk-d3dkmtunregistertrimnotification.md) | D3DKMTUnregisterTrimNotification is used to remove a callback registration for a kernel mode device receiving notifications from a graphics framework (such as OpenGL). |
| [D3DKMTSetDodIndirectSwapchain function](nf-d3dkmthk-d3dkmtsetdodindirectswapchain.md) | TBD |
| [D3DKMTOutputDuplGetFrameInfo function](nf-d3dkmthk-d3dkmtoutputduplgetframeinfo.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMTOfferAllocations function](nf-d3dkmthk-d3dkmtofferallocations.md) | Offers video memory allocations for reuse. |
| [D3DKMTWaitForVerticalBlankEvent function](nf-d3dkmthk-d3dkmtwaitforverticalblankevent.md) | The D3DKMTWaitForVerticalBlankEvent function waits for the vertical blanking interval to occur and then returns. |
| [D3DKMTGetPresentHistory function](nf-d3dkmthk-d3dkmtgetpresenthistory.md) | The D3DKMTGetPresentHistory function retrieves copying history. |
| [D3DKMTCreateSynchronizationObject function](nf-d3dkmthk-d3dkmtcreatesynchronizationobject.md) | The D3DKMTCreateSynchronizationObject function creates a kernel-mode synchronization object. |
| [D3DKMTFlushHeapTransitions function](nf-d3dkmthk-d3dkmtflushheaptransitions.md) | TBD |
| [D3DKMTGetProcessSchedulingPriorityClass function](nf-d3dkmthk-d3dkmtgetprocessschedulingpriorityclass.md) | The D3DKMTGetProcessSchedulingPriorityClass function retrieves the scheduling priority for a process. |
| [D3DKMTQueryFSEBlock function](nf-d3dkmthk-d3dkmtqueryfseblock.md) | TBD |
| [D3DKMTSetHwProtectionTeardownRecovery function](nf-d3dkmthk-d3dkmtsethwprotectionteardownrecovery.md) | TBD |
| [D3DKMTReleaseKeyedMutex2 function](nf-d3dkmthk-d3dkmtreleasekeyedmutex2.md) | Releases a keyed mutex object that includes private data. |
| [D3DKMTSetAllocationPriority function](nf-d3dkmthk-d3dkmtsetallocationpriority.md) | The D3DKMTSetAllocationPriority function sets the priority level of a resource or list of allocations. |
| [D3DKMTGetRuntimeData function](nf-d3dkmthk-d3dkmtgetruntimedata.md) | The D3DKMTGetRuntimeData function is for system use only. |
| [D3DKMTDestroyHwQueue function](nf-d3dkmthk-d3dkmtdestroyhwqueue.md) | TBD |
| [D3DKMTPresent function](nf-d3dkmthk-d3dkmtpresent.md) | The D3DKMTPresent function submits a present command to the Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys). |
| [D3DKMTCreateAllocation function](nf-d3dkmthk-d3dkmtcreateallocation.md) | The D3DKMTCreateAllocation function creates allocations of system or video memory. |
| [D3DKMTEscape function](nf-d3dkmthk-d3dkmtescape.md) | The D3DKMTEscape function exchanges information with the display miniport driver. |
| [D3DKMTAdjustFullscreenGamma function](nf-d3dkmthk-d3dkmtadjustfullscreengamma.md) | TBD |
| [D3DKMTLock function](nf-d3dkmthk-d3dkmtlock.md) | The D3DKMTLock function locks an entire allocation or specific pages within an allocation. |
| [D3DKMTSetStablePowerState function](nf-d3dkmthk-d3dkmtsetstablepowerstate.md) | TBD |
| [D3DKMTSetDisplayPrivateDriverFormat function](nf-d3dkmthk-d3dkmtsetdisplayprivatedriverformat.md) | The D3DKMTSetDisplayPrivateDriverFormat function changes the private-format attribute of a video present source. |
| [D3DKMTDestroyOutputDupl function](nf-d3dkmthk-d3dkmtdestroyoutputdupl.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMTDestroyKeyedMutex function](nf-d3dkmthk-d3dkmtdestroykeyedmutex.md) | The D3DKMTDestroyKeyedMutex function destroys a keyed mutex object. |
| [D3DKMTUpdateAllocationProperty function](nf-d3dkmthk-d3dkmtupdateallocationproperty.md) | TBD |
| [D3DKMTWaitForSynchronizationObjectFromCpu function](nf-d3dkmthk-d3dkmtwaitforsynchronizationobjectfromcpu.md) | D3DKMTWaitForSynchronizationObjectFromCpu waits for a monitored fence to reach a certain value. |
| [D3DKMTOpenAdapterFromGdiDisplayName function](nf-d3dkmthk-d3dkmtopenadapterfromgdidisplayname.md) | The D3DKMTOpenAdapterFromGdiDisplayName function maps a GDI device name to a graphics adapter handle and, if the adapter contains multiple monitor outputs, to one of those outputs. |
| [D3DKMTCreateContextVirtual function](nf-d3dkmthk-d3dkmtcreatecontextvirtual.md) | The D3DKMTCreateContextVirtual function creates a kernel mode device context that supports virtual addressing. |
| [D3DKMTGetAllocationPriority function](nf-d3dkmthk-d3dkmtgetallocationpriority.md) | TBD |
| [D3DKMTGetContextInProcessSchedulingPriority function](nf-d3dkmthk-d3dkmtgetcontextinprocessschedulingpriority.md) | Called by an in-process (in-proc) Microsoft Direct3D composition device to retrieve the scheduling priority for a device context that is in the same process as other device contexts. |
| [D3DKMTReleaseSwapChain function](nf-d3dkmthk-d3dkmtreleaseswapchain.md) | TBD |
| [D3DKMTCreateOutputDupl function](nf-d3dkmthk-d3dkmtcreateoutputdupl.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMTConfigureSharedResource function](nf-d3dkmthk-d3dkmtconfiguresharedresource.md) | The D3DKMTConfigureSharedResource function configures a shared resource. |
| [D3DKMTInvalidateCache function](nf-d3dkmthk-d3dkmtinvalidatecache.md) | TBD |
| [D3DKMTOpenSyncObjectFromNtHandle2 function](nf-d3dkmthk-d3dkmtopensyncobjectfromnthandle2.md) | D3DKMTOpenSyncObjectFromNtHandle2 opens a monitored fence object from an NT handle previously created by D3DKMTShareObjects. |
| [D3DKMTSetContextInProcessSchedulingPriority function](nf-d3dkmthk-d3dkmtsetcontextinprocessschedulingpriority.md) | Called by an in-process (in-proc) Microsoft Direct3D composition device to set the scheduling priority for a device context that is in the same process as other device contexts. |
| [D3DKMTCloseAdapter function](nf-d3dkmthk-d3dkmtcloseadapter.md) | The D3DKMTCloseAdapter function closes a graphics adapter that was previously opened by using the D3DKMTOpenAdapterFromHdc function. |
| [D3DKMTAcquireKeyedMutex function](nf-d3dkmthk-d3dkmtacquirekeyedmutex.md) | The D3DKMTAcquireKeyedMutex function acquires a keyed mutex object. |
| [D3DKMTGetSharedResourceAdapterLuid function](nf-d3dkmthk-d3dkmtgetsharedresourceadapterluid.md) | Maps a shared resource to a locally unique identifier (LUID) that identifies the graphics adapter that the resource was created on. |
| [D3DKMTReclaimAllocations function](nf-d3dkmthk-d3dkmtreclaimallocations.md) | Reclaims video memory allocations. |
| [D3DKMTOpenProtectedSessionFromNtHandle function](nf-d3dkmthk-d3dkmtopenprotectedsessionfromnthandle.md) | Used to open a protected session from the NT handle. |
| [D3DKMTSubmitCommand function](nf-d3dkmthk-d3dkmtsubmitcommand.md) | D3DKMTSubmitCommand is used to submit command buffers on contexts that support graphics processing unit (GPU) virtual addressing. |
| [D3DKMTInvalidateActiveVidPn function](nf-d3dkmthk-d3dkmtinvalidateactivevidpn.md) | The D3DKMTInvalidateActiveVidPn function invalidates the active video present network (VidPN) currently in use.Note   This function is obsolete in Windows 7 and later versions of the Windows operating systems. |
| [D3DKMTOpenSynchronizationObject function](nf-d3dkmthk-d3dkmtopensynchronizationobject.md) | The D3DKMTOpenSynchronizationObject function opens a kernel-mode synchronization object. |
| [D3DKMTGetDWMVerticalBlankEvent function](nf-d3dkmthk-d3dkmtgetdwmverticalblankevent.md) | TBD |
| [D3DKMTSignalSynchronizationObjectFromCpu function](nf-d3dkmthk-d3dkmtsignalsynchronizationobjectfromcpu.md) | D3DKMTSignalSynchronizationObjectFromCpu enables a driver to signal a monitored fence.D3DKMTSignalSynchronizationObjectFromCpu enables a driver to signal a monitored fence. |
| [D3DKMTSetDeviceLostSupport function](nf-d3dkmthk-d3dkmtsetdevicelostsupport.md) | Used to indicate that the device has lost support. |
| [D3DKMTReserveGpuVirtualAddress function](nf-d3dkmthk-d3dkmtreservegpuvirtualaddress.md) | D3DKMTReserveGpuVirtualAddress reserves an address range in the current process graphics processing unit (GPU) virtual address space. The address range is only reserved, there is no actual memory behind it. |
| [D3DKMTFlipOverlay function](nf-d3dkmthk-d3dkmtflipoverlay.md) | The D3DKMTFlipOverlay function changes the allocation to display on the overlay. |
| [D3DKMTFreeGpuVirtualAddress function](nf-d3dkmthk-d3dkmtfreegpuvirtualaddress.md) | D3DKMTFreeGpuVirtualAddress releases a range of graphics processing unit (GPU) virtual addresses, which was previously reserved or mapped. |
| [D3DKMTGetOverlayState function](nf-d3dkmthk-d3dkmtgetoverlaystate.md) | The D3DKMTGetOverlayState function retrieves the status about an overlay. |
| [D3DKMTSetDisplayMode function](nf-d3dkmthk-d3dkmtsetdisplaymode.md) | The D3DKMTSetDisplayMode function sets the allocation that is used to scan out to the display. |
| [D3DKMTGetPresentQueueEvent function](nf-d3dkmthk-d3dkmtgetpresentqueueevent.md) | TBD |
| [D3DKMTQueryResourceInfo function](nf-d3dkmthk-d3dkmtqueryresourceinfo.md) | The D3DKMTQueryResourceInfo function retrieves information about a shared resource. |
| [D3DKMTQueryProtectedSessionStatus function](nf-d3dkmthk-d3dkmtqueryprotectedsessionstatus.md) | Used to query the status of the protected session. |
| [D3DKMTGetDisplayModeList function](nf-d3dkmthk-d3dkmtgetdisplaymodelist.md) | The D3DKMTGetDisplayModeList function retrieves a list of available display modes, including modes with extended format. |
| [D3DKMTPresentMultiPlaneOverlay function](nf-d3dkmthk-d3dkmtpresentmultiplaneoverlay.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMTDestroyPagingQueue function](nf-d3dkmthk-d3dkmtdestroypagingqueue.md) | D3DKMTDestroyPagingQueue waits for a paging queue to finish all operations queued to it, and destroys it along with the associated sync object. |
| [D3DKMTDestroyAllocation2 function](nf-d3dkmthk-d3dkmtdestroyallocation2.md) | The D3DKMTDestroyAllocation2 function releases a resource, a list of allocations, or both. |
| [D3DKMTOpenAdapterFromLuid function](nf-d3dkmthk-d3dkmtopenadapterfromluid.md) | Maps a locally unique identifier (LUID) to a graphics adapter handle. |
| [D3DKMTSetMonitorColorSpaceTransform function](nf-d3dkmthk-d3dkmtsetmonitorcolorspacetransform.md) | Used to set the color space transform for the selected monitor. |
| [D3DKMTPollDisplayChildren function](nf-d3dkmthk-d3dkmtpolldisplaychildren.md) | The D3DKMTPollDisplayChildren function queries for connectivity status of all child devices of the given adapter. |
| [D3DKMTGetMultisampleMethodList function](nf-d3dkmthk-d3dkmtgetmultisamplemethodlist.md) | The D3DKMTGetMultisampleMethodList function retrieves a list of multiple-sample methods that are used for an allocation. |
| [D3DKMTReleaseProcessVidPnSourceOwners function](nf-d3dkmthk-d3dkmtreleaseprocessvidpnsourceowners.md) | The D3DKMTReleaseProcessVidPnSourceOwners function releases the video present network source owners for a process. |
| [D3DKMTCheckMultiPlaneOverlaySupport2 function](nf-d3dkmthk-d3dkmtcheckmultiplaneoverlaysupport2.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMTQueryAllocationResidency function](nf-d3dkmthk-d3dkmtqueryallocationresidency.md) | The D3DKMTQueryAllocationResidency function retrieves the residency status of a resource or list of allocations. |
| [D3DKMTQueryProtectedSessionInfoFromNtHandle function](nf-d3dkmthk-d3dkmtqueryprotectedsessioninfofromnthandle.md) | Used to get information on the protected session. |
| [D3DKMTQueryVideoMemoryInfo function](nf-d3dkmthk-d3dkmtqueryvideomemoryinfo.md) | TBD |
| [D3DKMTWaitForSynchronizationObject function](nf-d3dkmthk-d3dkmtwaitforsynchronizationobject.md) | The D3DKMTWaitForSynchronizationObject function inserts a wait for the specified synchronization objects in the specified context stream. |
| [D3DKMTOpenAdapterFromDeviceName function](nf-d3dkmthk-d3dkmtopenadapterfromdevicename.md) | The D3DKMTOpenAdapterFromDeviceName function maps a device name to a graphics adapter handle and, if the adapter contains multiple monitor outputs, to one of those outputs. |
| [D3DKMTUpdateOverlay function](nf-d3dkmthk-d3dkmtupdateoverlay.md) | The D3DKMTUpdateOverlay function modifies a kernel-mode overlay object. |
| [D3DKMTExtractBundleObject function](nf-d3dkmthk-d3dkmtextractbundleobject.md) | Used to extract the bundle object. |
| [D3DKMTOpenSyncObjectNtHandleFromName function](nf-d3dkmthk-d3dkmtopensyncobjectnthandlefromname.md) | D3DKMTOpenSyncObjectNtHandleFromName opens an NT handle for a named shared monitored fence object, similar to what D3DKMTOpenNtHandleFromName does for shared allocations. |
| [D3DKMTOpenKeyedMutex2 function](nf-d3dkmthk-d3dkmtopenkeyedmutex2.md) | Opens a keyed mutex object that includes private data. |
| [D3DKMTEvict function](nf-d3dkmthk-d3dkmtevict.md) | D3DKMTEvict is used to decrement the allocation residency reference count. Once this count reaches zero, it will remove the allocation from the device residency list. |
| [D3DKMTOutputDuplGetMetaData function](nf-d3dkmthk-d3dkmtoutputduplgetmetadata.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMTCheckSharedResourceAccess function](nf-d3dkmthk-d3dkmtchecksharedresourceaccess.md) | The D3DKMTCheckSharedResourceAccess function determines if a process can access a shared resource. |
| [D3DKMTCheckMultiPlaneOverlaySupport function](nf-d3dkmthk-d3dkmtcheckmultiplaneoverlaysupport.md) | TBD |
| [D3DKMTSubmitSignalSyncObjectsToHwQueue function](nf-d3dkmthk-d3dkmtsubmitsignalsyncobjectstohwqueue.md) | TBD |
| [D3DKMTQueryAdapterInfo function](nf-d3dkmthk-d3dkmtqueryadapterinfo.md) | The D3DKMTQueryAdapterInfo function retrieves graphics adapter information. |
| [D3DKMTMarkDeviceAsError function](nf-d3dkmthk-d3dkmtmarkdeviceaserror.md) | TBD |
| [D3DKMTOpenResource function](nf-d3dkmthk-d3dkmtopenresource.md) | The D3DKMTOpenResource function opens a shared resource. |
| [D3DKMTDestroyDCFromMemory function](nf-d3dkmthk-d3dkmtdestroydcfrommemory.md) | The D3DKMTDestroyDCFromMemory function releases the display context. |
| [D3DKMTDestroyProtectedSession function](nf-d3dkmthk-d3dkmtdestroyprotectedsession.md) | Used to destroy a protected session. |
| [D3DKMTOpenSwapChain function](nf-d3dkmthk-d3dkmtopenswapchain.md) | TBD |
| [D3DKMTSignalSynchronizationObjectFromGpu function](nf-d3dkmthk-d3dkmtsignalsynchronizationobjectfromgpu.md) | D3DKMTSignalSynchronizationObjectFromGpu is used to signal a monitored fence. |
| [D3DKMTCreateAllocation2 function](nf-d3dkmthk-d3dkmtcreateallocation2.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMTRegisterTrimNotification function](nf-d3dkmthk-d3dkmtregistertrimnotification.md) | D3DKMTRegisterTrimNotification is used by a kernel mode video memory manager to register and implement a callback for each kernel mode device to receive notifications from a graphics framework (such as OpenGL). |
| [D3DKMTSharedPrimaryLockNotification function](nf-d3dkmthk-d3dkmtsharedprimarylocknotification.md) | The D3DKMTSharedPrimaryLockNotification function notifies the operating system about an upcoming lock to a shared primary surface. |
| [D3DKMTEnumAdapters function](nf-d3dkmthk-d3dkmtenumadapters.md) | Enumerates all graphics adapters on the system. |
| [D3DKMTUnlock function](nf-d3dkmthk-d3dkmtunlock.md) | The D3DKMTUnlock function unlocks a list of allocations. |
| [D3DKMTGetDeviceState function](nf-d3dkmthk-d3dkmtgetdevicestate.md) | The D3DKMTGetDeviceState function retrieves the state of a device. |
| [D3DKMTEnumAdapters2 function](nf-d3dkmthk-d3dkmtenumadapters2.md) | TBD |
| [D3DKMTRender function](nf-d3dkmthk-d3dkmtrender.md) | The D3DKMTRender function submits the current command buffer to the Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys). |
| [D3DKMTGetScanLine function](nf-d3dkmthk-d3dkmtgetscanline.md) | The D3DKMTGetScanLine function determines whether the given video present source of a video present network (VidPN) is in vertical blanking mode and retrieves the current scan line. |
| [D3DKMTSetSyncRefreshCountWaitTarget function](nf-d3dkmthk-d3dkmtsetsyncrefreshcountwaittarget.md) | TBD |
| [D3DKMTGetSharedPrimaryHandle function](nf-d3dkmthk-d3dkmtgetsharedprimaryhandle.md) | The D3DKMTGetSharedPrimaryHandle function retrieves the global shared handle for the primary surface. |
| [D3DKMTChangeSurfacePointer function](nf-d3dkmthk-d3dkmtchangesurfacepointer.md) | The D3DKMTChangeSurfacePointer function is for system use only. |
| [D3DKMTOutputDuplReleaseFrame function](nf-d3dkmthk-d3dkmtoutputduplreleaseframe.md) | Indicates that the driver has finished processing the duplicated desktop image. |
| [D3DKMTWaitForIdle function](nf-d3dkmthk-d3dkmtwaitforidle.md) | The D3DKMTWaitForIdle function waits for a display device to be idle. |
| [D3DKMTCreateHwContext function](nf-d3dkmthk-d3dkmtcreatehwcontext.md) | Used to create a new hardware context. |
| [D3DKMTPresentMultiPlaneOverlay3 function](nf-d3dkmthk-d3dkmtpresentmultiplaneoverlay3.md) | TBD |
| [D3DKMTMapGpuVirtualAddress function](nf-d3dkmthk-d3dkmtmapgpuvirtualaddress.md) | D3DKMTMapGpuVirtualAddress maps a graphics processing unit (GPU) virtual address ranges to a specific allocation range or puts it to the Invalid or Zero state. |
| [D3DKMTAbandonSwapChain function](nf-d3dkmthk-d3dkmtabandonswapchain.md) | TBD |
| [D3DKMTGetPostCompositionCaps function](nf-d3dkmthk-d3dkmtgetpostcompositioncaps.md) | TBD |
| [D3DKMTSignalSynchronizationObjectFromGpu2 function](nf-d3dkmthk-d3dkmtsignalsynchronizationobjectfromgpu2.md) | D3DKMTSignalSynchronizationObjectFromGpu2 is used to signal a monitored fence. |
| [D3DKMTGetProcessDeviceLostSupport function](nf-d3dkmthk-d3dkmtgetprocessdevicelostsupport.md) | Used to get the indicated process. |
| [D3DKMTGetContextSchedulingPriority function](nf-d3dkmthk-d3dkmtgetcontextschedulingpriority.md) | The D3DKMTGetContextSchedulingPriority function retrieves the scheduling priority for a device context. |
| [D3DKMTQueryRemoteVidPnSourceFromGdiDisplayName function](nf-d3dkmthk-d3dkmtqueryremotevidpnsourcefromgdidisplayname.md) | Maps a GDI display name to a remote video present network (VidPN) source ID that is needed for a call to the D3DKMTOutputDuplPresent function. |
| [D3DKMTSubmitCommandToHwQueue function](nf-d3dkmthk-d3dkmtsubmitcommandtohwqueue.md) | TBD |
| [D3DKMTReclaimAllocations2 function](nf-d3dkmthk-d3dkmtreclaimallocations2.md) | D3DKMTReclaimAllocations2 reclaims video memory allocations. |
| [D3DKMTCreateProtectedSession function](nf-d3dkmthk-d3dkmtcreateprotectedsession.md) | Used to create a protected session. |
| [D3DKMTCheckExclusiveOwnership function](nf-d3dkmthk-d3dkmtcheckexclusiveownership.md) | The D3DKMTCheckExclusiveOwnership function checks whether any kernel device object in the operating system has an exclusive level of ownership of any video present sources. |
| [D3DKMTLock2 function](nf-d3dkmthk-d3dkmtlock2.md) | The D3DKMTLock2 function locks an entire allocation or specific pages within an allocation. |
| [D3DKMTCreateDCFromMemory function](nf-d3dkmthk-d3dkmtcreatedcfrommemory.md) | The D3DKMTCreateDCFromMemory function creates a display context from a specified block of memory. |
| [D3DKMTDestroyDevice function](nf-d3dkmthk-d3dkmtdestroydevice.md) | The D3DKMTDestroyDevice function releases a kernel-mode device context. |
| [D3DKMTUpdateGpuVirtualAddress function](nf-d3dkmthk-d3dkmtupdategpuvirtualaddress.md) | D3DKMTUpdateGpuVirtualAddress is a special operation used in the context of tile resources. It allows the driver to specify a number of mapping operations to be applied to the process virtual address space in a single batch of page table updates. |
| [D3DKMTCreateSwapChain function](nf-d3dkmthk-d3dkmtcreateswapchain.md) | TBD |
| [D3DKMTSetVidPnSourceHwProtection function](nf-d3dkmthk-d3dkmtsetvidpnsourcehwprotection.md) | TBD |
| [D3DKMTSetContextSchedulingPriority function](nf-d3dkmthk-d3dkmtsetcontextschedulingpriority.md) | The D3DKMTSetContextSchedulingPriority function sets the scheduling priority for a device context. |
| [D3DKMTShareObjects function](nf-d3dkmthk-d3dkmtshareobjects.md) | Shares resource objects that were created with the D3DKMTCreateAllocation, D3DKMTCreateKeyedMutex2, and D3DKMTCreateSynchronizationObject2 functions. |
| [D3DKMTOpenSyncObjectFromNtHandle function](nf-d3dkmthk-d3dkmtopensyncobjectfromnthandle.md) | Maps an NT process handle to a graphics processing unit (GPU) synchronization object. |
| [D3DKMTWaitForSynchronizationObject2 function](nf-d3dkmthk-d3dkmtwaitforsynchronizationobject2.md) | The D3DKMTWaitForSynchronizationObject2 function inserts a wait for the specified synchronization objects in the specified context stream. |
| [D3DKMTMakeResident function](nf-d3dkmthk-d3dkmtmakeresident.md) | D3DKMTMakeResident is used to add a resource to the device residency list and increment the residency reference count on this allocation. |
| [D3DKMTAcquireSwapChain function](nf-d3dkmthk-d3dkmtacquireswapchain.md) | TBD |
| [D3DKMTSetVidPnSourceOwner1 function](nf-d3dkmthk-d3dkmtsetvidpnsourceowner1.md) | Sets and releases the video present source in the path of a video present network (VidPN) topology that owns the VidPN, and lets output duplication options be specified. Supported starting with Windows 8. |
| [D3DKMTPresentMultiPlaneOverlay2 function](nf-d3dkmthk-d3dkmtpresentmultiplaneoverlay2.md) | TBD |
| [D3DKMTOutputDuplGetPointerShapeData function](nf-d3dkmthk-d3dkmtoutputduplgetpointershapedata.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMTCheckMonitorPowerState function](nf-d3dkmthk-d3dkmtcheckmonitorpowerstate.md) | The D3DKMTCheckMonitorPowerState function verifies the power state of a monitor. |
| [D3DKMTDestroyContext function](nf-d3dkmthk-d3dkmtdestroycontext.md) | The D3DKMTDestroyContext function releases a kernel-mode device context. |
| [D3DKMTSignalSynchronizationObject2 function](nf-d3dkmthk-d3dkmtsignalsynchronizationobject2.md) | The D3DKMTSignalSynchronizationObject2 function inserts a signal for the specified synchronization objects in the specified context stream. |
| [D3DKMTReleaseKeyedMutex function](nf-d3dkmthk-d3dkmtreleasekeyedmutex.md) | The D3DKMTReleaseKeyedMutex function releases a keyed mutex object. |
| [D3DKMTSetFSEBlock function](nf-d3dkmthk-d3dkmtsetfseblock.md) | TBD |
| [D3DKMTQueryResourceInfoFromNtHandle function](nf-d3dkmthk-d3dkmtqueryresourceinfofromnthandle.md) | Maps a global NT handle to resource information that is needed for a call to the D3DKMTQueryResourceInfo function. |
| [D3DKMTCreateContext function](nf-d3dkmthk-d3dkmtcreatecontext.md) | The D3DKMTCreateContext function creates a kernel-mode device context. |
| [D3DKMTDestroyOverlay function](nf-d3dkmthk-d3dkmtdestroyoverlay.md) | The D3DKMTDestroyOverlay function destroys a kernel-mode overlay object. |
| [D3DKMTDestroyAllocation function](nf-d3dkmthk-d3dkmtdestroyallocation.md) | The D3DKMTDestroyAllocation function releases a resource, a list of allocations, or both. |
| [D3DKMTQueryVidPnExclusiveOwnership function](nf-d3dkmthk-d3dkmtqueryvidpnexclusiveownership.md) | TBD |
| [D3DKMTUnlock2 function](nf-d3dkmthk-d3dkmtunlock2.md) | The D3DKMTUnlock2 function unlocks a list of allocations. |
| [D3DKMTQueryClockCalibration function](nf-d3dkmthk-d3dkmtqueryclockcalibration.md) | TBD |
| [D3DKMTSetVidPnSourceOwner function](nf-d3dkmthk-d3dkmtsetvidpnsourceowner.md) | The D3DKMTSetVidPnSourceOwner function sets and releases the video present source in the path of a video present network (VidPN) topology that owns the VidPN. |
| [GET_OUTPUT_DUPL_DEBUG_INFO_FROM_SNAPSHOT function](nf-d3dkmthk-get-output-dupl-debug-info-from-snapshot.md) | TBD |
| [D3DKMTOutputDuplPresent function](nf-d3dkmthk-d3dkmtoutputduplpresent.md) | Submits a present command from the Desktop Duplication API swapchain of the Desktop Window Manager (DWM) to the Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys). |
| [D3DKMTOpenKeyedMutex function](nf-d3dkmthk-d3dkmtopenkeyedmutex.md) | The D3DKMTOpenKeyedMutex function opens a keyed mutex object. |
| [D3DKMTCheckMultiPlaneOverlaySupport3 function](nf-d3dkmthk-d3dkmtcheckmultiplaneoverlaysupport3.md) | TBD |
| [D3DKMTCreateOverlay function](nf-d3dkmthk-d3dkmtcreateoverlay.md) | The D3DKMTCreateOverlay function creates a kernel-mode overlay object. |
| [D3DKMTCreatePagingQueue function](nf-d3dkmthk-d3dkmtcreatepagingqueue.md) | D3DKMTCreatePagingQueue is used to create a device paging queue that can be used to synchronize with video memory management operations for the device, such as making the device resource resident. |
| [D3DKMTCreateKeyedMutex function](nf-d3dkmthk-d3dkmtcreatekeyedmutex.md) | The D3DKMTCreateKeyedMutex function creates a keyed mutex object. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [D3DKMT_ESCAPE structure](ns-d3dkmthk--d3dkmt-escape.md) | The D3DKMT_ESCAPE structure describes information that is exchanged with the display miniport driver. |
| [D3DKMT_RENDER structure](ns-d3dkmthk--d3dkmt-render.md) | The D3DKMT_RENDER structure describes the current command buffer to be rendered. |
| [D3DKMT_PINDIRECTFLIPRESOURCES structure](ns-d3dkmthk--d3dkmt-pindirectflipresources.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_OUTPUTDUPLCREATIONFLAGS structure](ns-d3dkmthk--d3dkmt-outputduplcreationflags.md) | TBD |
| [D3DKMT_QUERY_DEVICE_IDS structure](ns-d3dkmthk--d3dkmt-query-device-ids.md) | TBD |
| [D3DKMT_CREATESTANDARDALLOCATION structure](ns-d3dkmthk--d3dkmt-createstandardallocation.md) | Used to create a standard allocation. |
| [D3DKMT_WORKINGSETFLAGS structure](ns-d3dkmthk--d3dkmt-workingsetflags.md) | The D3DKMT_WORKINGSETFLAGS structure identifies working-set properties of the display miniport driver that the OpenGL installable client driver (ICD) obtains by calling the D3DKMTQueryAdapterInfo function. |
| [D3DKMT_REGISTERBUDGETCHANGENOTIFICATION structure](ns-d3dkmthk--d3dkmt-registerbudgetchangenotification.md) | TBD |
| [D3DKMT_GETSHAREDRESOURCEADAPTERLUID structure](ns-d3dkmthk--d3dkmt-getsharedresourceadapterluid.md) | Provides information that describes a shared resource and the graphics adapter that the resource was created on. |
| [D3DKMT_DESTROYHWQUEUE structure](ns-d3dkmthk--d3dkmt-destroyhwqueue.md) | A structure holding information to destroy a hardware queue. |
| [D3DKMT_QUERYPROCESSOFFERINFO structure](ns-d3dkmthk--d3dkmt-queryprocessofferinfo.md) | TBD |
| [D3DKMT_RELEASESWAPCHAIN structure](ns-d3dkmthk--d3dkmt-releaseswapchain.md) | TBD |
| [D3DKMT_GETCONTEXTSCHEDULINGPRIORITY structure](ns-d3dkmthk--d3dkmt-getcontextschedulingpriority.md) | The D3DKMT_GETDEVICESCHEDULINGPRIORITY structure describes parameters for retrieving scheduling priority for a device context. |
| [D3DKMT_UNLOCK structure](ns-d3dkmthk--d3dkmt-unlock.md) | The D3DKMT_UNLOCK structure describes allocations to unlock. |
| [D3DKMT_DISPLAYMODELIST structure](ns-d3dkmthk--d3dkmt-displaymodelist.md) | Describes a list of display modes. |
| [D3DKMT_OUTPUTDUPL_POINTER_POSITION structure](ns-d3dkmthk--d3dkmt-outputdupl-pointer-position.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_WAITFORSYNCHRONIZATIONOBJECTFROMGPU structure](ns-d3dkmthk--d3dkmt-waitforsynchronizationobjectfromgpu.md) | D3DKMT_WAITFORSYNCHRONIZATIONOBJECTFROMGPU is used with D3DKMTWaitForSynchronizationObjectFromGpu to wait for a monitored fence to reach a certain value. |
| [D3DKMDT_DISPLAYMODE_FLAGS structure](ns-d3dkmthk--d3dkmdt-displaymode-flags.md) | TBD |
| [D3DKMT_WAITFORSYNCHRONIZATIONOBJECTFROMCPU structure](ns-d3dkmthk--d3dkmt-waitforsynchronizationobjectfromcpu.md) | D3DKMT_WAITFORSYNCHRONIZATIONOBJECTFROMCPU is used with D3DKMTWaitForSynchronizationObjectFromCpu to wait for a monitored fence to reach a certain value. |
| [D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 structure](ns-d3dkmthk--d3dkmt-opensyncobjectfromnthandle2.md) | D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 is used with D3DKMTOpenSyncObjectFromNtHandle2 to open a monitored fence object. |
| [D3DKMT_QUERYREMOTEVIDPNSOURCEFROMGDIDISPLAYNAME structure](ns-d3dkmthk--d3dkmt-queryremotevidpnsourcefromgdidisplayname.md) | Describes information that is required to map a GDI display name to a remote video present network (VidPN) source ID. |
| [D3DKMT_EVICT structure](ns-d3dkmthk--d3dkmt-evict.md) | D3DKMT_EVICT is used with D3DKMTEvict to subtract one from the residency reference count. |
| [D3DKMT_BRIGHTNESS_POSSIBLE_LEVELS structure](ns-d3dkmthk--d3dkmt-brightness-possible-levels.md) | Contains information about all possible brightness levels that an integrated display panel supports. |
| [D3DKMT_SETCONTEXTINPROCESSSCHEDULINGPRIORITY structure](ns-d3dkmthk--d3dkmt-setcontextinprocessschedulingpriority.md) | Describes parameters for an in-process (in-proc) Microsoft Direct3D composition device to set the scheduling priority for a device context that is in the same process as other device contexts. |
| [D3DKMT_CHECK_MULTIPLANE_OVERLAY_PLANE3 structure](ns-d3dkmthk--d3dkmt-check-multiplane-overlay-plane3.md) | TBD |
| [D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN structure](ns-d3dkmthk--d3dkmt-flipmodel-presenthistorytoken.md) | The D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN structure identifies a flip present-history operation. |
| [D3DKMT_CREATEHWQUEUE structure](ns-d3dkmthk--d3dkmt-createhwqueue.md) | A structure holding information to create a hardware queue. |
| [D3DKMT_GETSHAREDPRIMARYHANDLE structure](ns-d3dkmthk--d3dkmt-getsharedprimaryhandle.md) | The D3DKMT_GETSHAREDPRIMARYHANDLE structure describes the parameters that are required to retrieve the global shared handle for the primary surface. |
| [D3DKMT_RENDERFLAGS structure](ns-d3dkmthk--d3dkmt-renderflags.md) | The D3DKMT_RENDERFLAGS structure identifies the type of command buffer to be rendered in a call to the D3DKMTRender function. |
| [D3DKMT_UPDATEGPUVIRTUALADDRESS structure](ns-d3dkmthk--d3dkmt-updategpuvirtualaddress.md) | D3DKMT_UPDATEGPUVIRTUALADDRESS is used with UpdateGpuVirtualAddress to allow the driver to specify a number of mapping operations to be applied to the process virtual address space in a single batch of page table updates. |
| [D3DKMT_VAD_DESC structure](ns-d3dkmthk--d3dkmt-vad-desc.md) | TBD |
| [D3DKMT_PRESENTHISTORYTOKEN structure](ns-d3dkmthk--d3dkmt-presenthistorytoken.md) | The D3DKMT_PRESENTHISTORYTOKEN structure identifies a type of present operation. |
| [D3DKMT_GET_MULTIPLANE_OVERLAY_CAPS structure](ns-d3dkmthk--d3dkmt-get-multiplane-overlay-caps.md) | TBD |
| [D3DKMT_GETVERTICALBLANKEVENT structure](ns-d3dkmthk--d3dkmt-getverticalblankevent.md) | TBD |
| [D3DKMT_ADDSURFACETOSWAPCHAIN structure](ns-d3dkmthk--d3dkmt-addsurfacetoswapchain.md) | Used to add a surface to the swapchain. |
| [D3DKMT_MIRACAST_DISPLAY_STOP_SESSIONS structure](ns-d3dkmthk--d3dkmt-miracast-display-stop-sessions.md) | TBD |
| [D3DKMT_HYBRID_LIST structure](ns-d3dkmthk--d3dkmt-hybrid-list.md) | TBD |
| [D3DKMT_PRESENT_STATS_DWM structure](ns-d3dkmthk--d3dkmt-present-stats-dwm.md) | TBD |
| [D3DKMT_UNREGISTERBUDGETCHANGENOTIFICATION structure](ns-d3dkmthk--d3dkmt-unregisterbudgetchangenotification.md) | TBD |
| [D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMCPU structure](ns-d3dkmthk--d3dkmt-signalsynchronizationobjectfromcpu.md) | D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMCPU is used with D3DKMTSignalSynchronizationObjectFromCpu to enable a driver to signal a monitored fence. |
| [D3DKMT_PRESENTFLAGS structure](ns-d3dkmthk--d3dkmt-presentflags.md) | The D3DKMT_PRESENTFLAGS structure identifies how to perform a present operation. |
| [D3DKMT_GPUMMU_CAPS structure](ns-d3dkmthk--d3dkmt-gpummu-caps.md) | TBD |
| [D3DKMT_MULTIPLANEOVERLAY_HUD_SUPPORT structure](ns-d3dkmthk--d3dkmt-multiplaneoverlay-hud-support.md) | TBD |
| [D3DKMT_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS structure](ns-d3dkmthk--d3dkmt-multiplane-overlay-post-composition-flags.md) | TBD |
| [D3DKMT_GETPRESENTHISTORY structure](ns-d3dkmthk--d3dkmt-getpresenthistory.md) | The D3DKMT_GETPRESENTHISTORY structure describes the state of copying history. |
| [D3DKMT_ADAPTER_VERIFIER_VIDMM_FLAGS structure](ns-d3dkmthk--d3dkmt-adapter-verifier-vidmm-flags.md) | TBD |
| [D3DKMT_GET_GPUMMU_CAPS structure](ns-d3dkmthk--d3dkmt-get-gpummu-caps.md) | TBD |
| [D3DKMT_SETCONTEXTSCHEDULINGPRIORITY structure](ns-d3dkmthk--d3dkmt-setcontextschedulingpriority.md) | The D3DKMT_SETCONTEXTSCHEDULINGPRIORITY structure describes parameters for setting scheduling priority for a device context. |
| [D3DKMT_OPENADAPTERFROMDEVICENAME structure](ns-d3dkmthk--d3dkmt-openadapterfromdevicename.md) | The D3DKMT_OPENADAPTERFROMDEVICENAME structure describes the mapping of the given name of a device to a graphics adapter handle and monitor output. |
| [D3DKMT_QUERYFSEBLOCK structure](ns-d3dkmthk--d3dkmt-queryfseblock.md) | TBD |
| [D3DKMT_INDEPENDENTFLIP_SUPPORT structure](ns-d3dkmthk--d3dkmt-independentflip-support.md) | TBD |
| [D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION structure](ns-d3dkmthk--d3dkmt-sharedprimaryunlocknotification.md) | The D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION structure describes the shared primary surface that an application just unlocked. |
| [D3DKMT_OUTDUPL_POINTER_SHAPE_INFO structure](ns-d3dkmthk--d3dkmt-outdupl-pointer-shape-info.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_PRESENT_MULTIPLANE_OVERLAY_FLAGS structure](ns-d3dkmthk--d3dkmt-present-multiplane-overlay-flags.md) | TBD |
| [D3DKMT_RELEASEKEYEDMUTEX2 structure](ns-d3dkmthk--d3dkmt-releasekeyedmutex2.md) | Describes a keyed mutex object that the D3DKMTReleaseKeyedMutex2 function releases that includes private data. |
| [D3DKMT_MULTISAMPLEMETHOD structure](ns-d3dkmthk--d3dkmt-multisamplemethod.md) | The D3DKMT_MULTISAMPLEMETHOD structure describes a multiple-sampling method. |
| [D3DKMT_QUERYADAPTERINFO structure](ns-d3dkmthk--d3dkmt-queryadapterinfo.md) | The D3DKMT_QUERYADAPTERINFO structure contains information that describes the graphics adapter. |
| [D3DKMT_WAITFORVERTICALBLANKEVENT structure](ns-d3dkmthk--d3dkmt-waitforverticalblankevent.md) | The D3DKMT_WAITFORVERTICALBLANKEVENT structure describes parameters for waiting for the vertical blanking interval to occur. |
| [D3DKMT_WAITFORVERTICALBLANKEVENT2 structure](ns-d3dkmthk--d3dkmt-waitforverticalblankevent2.md) | Describes parameters for multiple wait objects, including a vertical blank event. Supported starting with Windows 8. |
| [D3DKMT_PHYSICAL_ADAPTER_COUNT structure](ns-d3dkmthk--d3dkmt-physical-adapter-count.md) | TBD |
| [D3DKMT_SETGAMMARAMP structure](ns-d3dkmthk--d3dkmt-setgammaramp.md) | The D3DKMT_SETGAMMARAMP structure describes parameters for setting the gamma ramp. |
| [D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES2 structure](ns-d3dkmthk--d3dkmt-multiplane-overlay-attributes2.md) | TBD |
| [D3DKMT_GETMULTISAMPLEMETHODLIST structure](ns-d3dkmthk--d3dkmt-getmultisamplemethodlist.md) | The D3DKMT_GETMULTISAMPLEMETHODLIST structure describes parameters to retrieve the list of multiple-sample methods for an allocation. |
| [D3DKMT_VIDPNSOURCEOWNER_FLAGS structure](ns-d3dkmthk--d3dkmt-vidpnsourceowner-flags.md) | Specifies output duplication options for use with the D3DKMTSetVidPnSourceOwner1 function. |
| [D3DKMT_ACQUIRESWAPCHAIN structure](ns-d3dkmthk--d3dkmt-acquireswapchain.md) | TBD |
| [D3DKMT_CREATESYNCHRONIZATIONOBJECT structure](ns-d3dkmthk--d3dkmt-createsynchronizationobject.md) | The D3DKMT_CREATESYNCHRONIZATIONOBJECT structure describes a synchronization object that the D3DKMTCreateSynchronizationObject function creates. |
| [D3DKMT_SETDISPLAYMODE_FLAGS structure](ns-d3dkmthk--d3dkmt-setdisplaymode-flags.md) | TBD |
| [D3DKMT_GDIMODEL_PRESENTHISTORYTOKEN structure](ns-d3dkmthk--d3dkmt-gdimodel-presenthistorytoken.md) | The D3DKMT_GDIMODEL_PRESENTHISTORYTOKEN structure identifies a GDI present-history operation. |
| [D3DKMT_OUTPUTDUPL_KEYEDMUTEX structure](ns-d3dkmthk--d3dkmt-outputdupl-keyedmutex.md) | TBD |
| [D3DKMT_WORKINGSETINFO structure](ns-d3dkmthk--d3dkmt-workingsetinfo.md) | The D3DKMT_WORKINGSETINFO structure describes information about the graphics adapter's working set that the OpenGL installable client driver (ICD) obtains by calling the D3DKMTQueryAdapterInfo function. |
| [D3DKMT_FLIPOVERLAY structure](ns-d3dkmthk--d3dkmt-flipoverlay.md) | The D3DKMT_FLIPOVERLAY structure describes a new allocation to display for the overlay. |
| [D3DKMT_QUERY_MIRACAST_DRIVER_TYPE structure](ns-d3dkmthk--d3dkmt-query-miracast-driver-type.md) | TBD |
| [D3DKMT_OPENSYNCOBJECTFROMNTHANDLE structure](ns-d3dkmthk--d3dkmt-opensyncobjectfromnthandle.md) | Describes information that is required to map an NT process handle to a graphics processing unit (GPU) synchronization object. |
| [D3DKMT_QUERYVIDPNEXCLUSIVEOWNERSHIP structure](ns-d3dkmthk--d3dkmt-queryvidpnexclusiveownership.md) | TBD |
| [D3DKMT_UPDATEOVERLAY structure](ns-d3dkmthk--d3dkmt-updateoverlay.md) | The D3DKMT_UPDATEOVERLAY structure describes parameters for modifying an overlay. |
| [D3DKMT_OFFER_FLAGS structure](ns-d3dkmthk--d3dkmt-offer-flags.md) | TBD |
| [D3DKMT_FLIPQUEUEINFO structure](ns-d3dkmthk--d3dkmt-flipqueueinfo.md) | The D3DKMT_FLIPQUEUEINFO structure describes information about the graphics adapter's queue of flip operations that the OpenGL installable client driver (ICD) obtains by calling the D3DKMTQueryAdapterInfo function. |
| [D3DKMT_SETSYNCREFRESHCOUNTWAITTARGET structure](ns-d3dkmthk--d3dkmt-setsyncrefreshcountwaittarget.md) | TBD |
| [D3DKMT_SETVIDPNSOURCEOWNER structure](ns-d3dkmthk--d3dkmt-setvidpnsourceowner.md) | The D3DKMT_SETVIDPNSOURCEOWNER structure describes the parameters for setting or releasing the video present source in the path of a video present network (VidPN) topology that owns the VidPN. |
| [D3DKMT_CREATEDEVICE structure](ns-d3dkmthk--d3dkmt-createdevice.md) | The D3DKMT_CREATEDEVICE structure describes a kernel-mode device context. |
| [D3DKMT_SUBMITCOMMANDTOHWQUEUE structure](ns-d3dkmthk--d3dkmt-submitcommandtohwqueue.md) | A structure that holds information to submit a command to the hardware queue. |
| [D3DKMT_GETPROCESSDEVICELOSTSUPPORT structure](ns-d3dkmthk--d3dkmt-getprocessdevicelostsupport.md) | Used to get the indicated process. |
| [D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2 structure](ns-d3dkmthk--d3dkmt-waitforsynchronizationobject2.md) | The D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2 structure contains information about the synchronization events that the D3DKMTWaitForSynchronizationObject2 function waits for to occur. |
| [D3DKMT_PROCESS_VERIFIER_VIDMM_FLAGS structure](ns-d3dkmthk--d3dkmt-process-verifier-vidmm-flags.md) | TBD |
| [D3DKMT_ACTIVATE_SPECIFIC_DIAG_ESCAPE structure](ns-d3dkmthk--d3dkmt-activate-specific-diag-escape.md) | Indicates an escape type that is to be activated or deactivated. |
| [D3DKMT_SURFACECOMPLETE_PRESENTHISTORYTOKEN structure](ns-d3dkmthk--d3dkmt-surfacecomplete-presenthistorytoken.md) | A structure used to present the history token for a surface. |
| [D3DKMT_CHECK_MULTIPLANE_OVERLAY_PLANE structure](ns-d3dkmthk-d3dkmt-check-multiplane-overlay-plane.md) | TBD |
| [D3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT2 structure](ns-d3dkmthk--d3dkmt-checkmultiplaneoverlaysupport2.md) | TBD |
| [D3DKMT_DESTROYALLOCATION2 structure](ns-d3dkmthk--d3dkmt-destroyallocation2.md) | The D3DKMT_DESTROYALLOCATION2 structure describes parameters for releasing allocations with D3DKMTDestroyAllocation2. |
| [D3DKMT_OPENKEYEDMUTEX2 structure](ns-d3dkmthk--d3dkmt-openkeyedmutex2.md) | Describes a keyed mutex that the D3DKMTOpenKeyedMutex2 function opens. |
| [D3DKMT_CREATEKEYEDMUTEX2_FLAGS structure](ns-d3dkmthk--d3dkmt-createkeyedmutex2-flags.md) | Indicates how a handle to a keyed mutex is specified. |
| [DXGK_GRAPHICSPOWER_REGISTER_OUTPUT structure](ns-d3dkmthk--dxgk-graphicspower-register-output.md) | A structure containing output data used to manage shared power components. |
| [OUTPUTDUPL_CONTEXT_DEBUG_INFO structure](ns-d3dkmthk--outputdupl-context-debug-info.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_MIRACASTCOMPANIONDRIVERNAME structure](ns-d3dkmthk--d3dkmt-miracastcompaniondrivername.md) | TBD |
| [D3DKMT_SETDEVICELOSTSUPPORT structure](ns-d3dkmthk--d3dkmt-setdevicelostsupport.md) | Used to indicate whether a device can recover from losing a graphics device. |
| [D3DKMT_VA_RANGE_DESC structure](ns-d3dkmthk--d3dkmt-va-range-desc.md) | TBD |
| [D3DKMT_COMPOSITION_PRESENTHISTORYTOKEN structure](ns-d3dkmthk--d3dkmt-composition-presenthistorytoken.md) | Identifies a composition swap chain present-history operation. This type of presentation is used for Extensible Application Markup Language (XAML)-based apps. |
| [D3DKMT_PROCESS_VERIFIER_OPTION_DATA structure](ns-d3dkmthk--d3dkmt-process-verifier-option-data.md) | TBD |
| [D3DKMT_CREATE_OUTPUTDUPL structure](ns-d3dkmthk--d3dkmt-create-outputdupl.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_MIRACAST_DISPLAY_DEVICE_CAPS structure](ns-d3dkmthk--d3dkmt-miracast-display-device-caps.md) | TBD |
| [D3DKMT_TRIMPROCESSCOMMITMENT structure](ns-d3dkmthk--d3dkmt-trimprocesscommitment.md) | TBD |
| [D3DKMT_CREATEHWCONTEXT structure](ns-d3dkmthk--d3dkmt-createhwcontext.md) | A structure holding information to create a hardware context. |
| [D3DKMT_UNPINDIRECTFLIPRESOURCES structure](ns-d3dkmthk--d3dkmt-unpindirectflipresources.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_MPOKERNELCAPS_SUPPORT structure](ns-d3dkmthk--d3dkmt-mpokernelcaps-support.md) | TBD |
| [D3DKMT_REGISTERTRIMNOTIFICATION structure](ns-d3dkmthk--d3dkmt-registertrimnotification.md) | D3DKMT_REGISTERTRIMNOTIFICATION is used with D3DKMTRegisterTrimNotification to register a callback for a kernel mode device for notifications from a graphics framework (such as OpenGL). |
| [D3DKMT_OPENRESOURCE structure](ns-d3dkmthk--d3dkmt-openresource.md) | The D3DKMT_OPENRESOURCE structure describes parameters for opening a resource. |
| [D3DKMT_DIRTYREGIONS structure](ns-d3dkmthk--d3dkmt-dirtyregions.md) | The D3DKMT_DIRTYREGIONS structure describes active rectangles (dirty regions) of a surface. |
| [D3DKMT_SHAREDPRIMARYLOCKNOTIFICATION structure](ns-d3dkmthk--d3dkmt-sharedprimarylocknotification.md) | The D3DKMT_SHAREDPRIMARYLOCKNOTIFICATION structure describes the shared primary surface that an application is about to lock. |
| [D3DKMT_DESTROYHWCONTEXT structure](ns-d3dkmthk--d3dkmt-destroyhwcontext.md) | A structure holding information to destroy a hardware context. |
| [D3DKMT_OPENGLINFO structure](ns-d3dkmthk--d3dkmt-openglinfo.md) | The D3DKMT_OPENGLINFO structure describes OpenGL installable client driver (ICD) information. |
| [D3DKMT_EXTRACTBUNDLEOBJECT structure](ns-d3dkmthk--d3dkmt-extractbundleobject.md) | Used to extract the bundle object. |
| [D3DKMT_QUERYRESOURCEINFOFROMNTHANDLE structure](ns-d3dkmthk--d3dkmt-queryresourceinfofromnthandle.md) | Describes information that is required to map a global NT handle to resource information. |
| [D3DKMT_CREATESYNCHRONIZATIONOBJECT2 structure](ns-d3dkmthk--d3dkmt-createsynchronizationobject2.md) | The D3DKMT_CREATESYNCHRONIZATIONOBJECT2 structure describes a synchronization object that the D3DKMTCreateSynchronizationObject2 function creates. |
| [D3DKMT_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE structure](ns-d3dkmthk--d3dkmt-submitwaitforsyncobjectstohwqueue.md) | TBD |
| [D3DKMT_SETDODINDIRECTSWAPCHAIN structure](ns-d3dkmthk--d3dkmt-setdodindirectswapchain.md) | TBD |
| [D3DKMT_OUTPUTDUPLPRESENTFLAGS structure](ns-d3dkmthk--d3dkmt-outputduplpresentflags.md) | Describes options for a Desktop Duplication API swapchain present operation. |
| [D3DKMT_SET_COLORSPACE_TRANSFORM structure](ns-d3dkmthk--d3dkmt-set-colorspace-transform.md) | TBD. |
| [D3DKMT_MULTIPLANE_OVERLAY3 structure](ns-d3dkmthk--d3dkmt-multiplane-overlay3.md) | TBD |
| [D3DKMT_OPENADAPTERFROMLUID structure](ns-d3dkmthk--d3dkmt-openadapterfromluid.md) | Describes the mapping of the given locally unique identifier (LUID) of a device to a graphics adapter handle. |
| [D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES structure](ns-d3dkmthk-d3dkmt-multiplane-overlay-attributes.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_HWDRM_SUPPORT structure](ns-d3dkmthk--d3dkmt-hwdrm-support.md) | TBD |
| [D3DKMT_SETDISPLAYPRIVATEDRIVERFORMAT structure](ns-d3dkmthk--d3dkmt-setdisplayprivatedriverformat.md) | The D3DKMT_SETDISPLAYPRIVATEDRIVERFORMAT structure describes the private-format attribute to set for a video present source. |
| [D3DKMT_OPENSWAPCHAIN structure](ns-d3dkmthk--d3dkmt-openswapchain.md) | TBD |
| [D3DKMT_OUTPUTDUPL_FRAMEINFO structure](ns-d3dkmthk--d3dkmt-outputdupl-frameinfo.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES3 structure](ns-d3dkmthk--d3dkmt-multiplane-overlay-attributes3.md) | TBD |
| [D3DKMT_MULTIPLANEOVERLAY_SECONDARY_SUPPORT structure](ns-d3dkmthk--d3dkmt-multiplaneoverlay-secondary-support.md) | TBD |
| [D3DKMT_PAGE_TABLE_LEVEL_DESC structure](ns-d3dkmthk--d3dkmt-page-table-level-desc.md) | TBD |
| [D3DKMT_RECLAIMALLOCATIONS2 structure](ns-d3dkmthk--d3dkmt-reclaimallocations2.md) | D3DKMT_RECLAIMALLOCATIONS2 describes video memory resources that are to be reclaimed and that the driver previously offered for reuse. Used with the D3DKMTReclaimAllocations2 function. |
| [D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS structure](ns-d3dkmthk--d3dkmt-flipmodel-presenthistorytokenflags.md) | The D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS structure identifies attributes of a flip present-history operation. |
| [D3DKMT_MULTIPLANE_OVERLAY_POST_COMPOSITION_WITH_SOURCE structure](ns-d3dkmthk--d3dkmt-multiplane-overlay-post-composition-with-source.md) | TBD |
| [D3DKMT_CREATEKEYEDMUTEX2 structure](ns-d3dkmthk--d3dkmt-createkeyedmutex2.md) | Describes a keyed mutex that the D3DKMTCreateKeyedMutex2 function creates that includes private data. |
| [D3DKMT_PRESENT_RGNS structure](ns-d3dkmthk--d3dkmt-present-rgns.md) | Specifies dirty and move regions in a present operation. |
| [D3DKMT_CONFIGURESHAREDRESOURCE structure](ns-d3dkmthk--d3dkmt-configuresharedresource.md) | The D3DKMT_CONFIGURESHAREDRESOURCE structure describes parameters that the D3DKMTConfigureSharedResource function uses to configure a shared resource. |
| [D3DKMT_PLANE_SPECIFIC_OUTPUT_FLAGS structure](ns-d3dkmthk--d3dkmt-plane-specific-output-flags.md) | TBD |
| [D3DKMT_UNORDEREDPRESENTSWAPCHAIN structure](ns-d3dkmthk--d3dkmt-unorderedpresentswapchain.md) | Used to store information about the swapchain being presented. |
| [D3DKMT_ABANDONSWAPCHAIN structure](ns-d3dkmthk--d3dkmt-abandonswapchain.md) | TBD |
| [D3DKMT_PRESENT_REDIRECTED structure](ns-d3dkmthk--d3dkmt-present-redirected.md) | Used to give information on the status of the present history token. |
| [D3DKMT_FLUSHHEAPTRANSITIONS structure](ns-d3dkmthk--d3dkmt-flushheaptransitions.md) | TBD |
| [D3DKMT_INDEPENDENTFLIP_SECONDARY_SUPPORT structure](ns-d3dkmthk--d3dkmt-independentflip-secondary-support.md) | TBD |
| [D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME structure](ns-d3dkmthk--d3dkmt-opensyncobjectnthandlefromname.md) | D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME is used with D3DKMTOpenSyncObjectNtHandleFromName to open an NT handle for a named shared monitored fence object. |
| [D3DKMT_DESTROYDCFROMMEMORY structure](ns-d3dkmthk--d3dkmt-destroydcfrommemory.md) | The D3DKMT_DESTROYDCFROMMEMORY structure describes parameters for releasing the display context. |
| [D3DKMT_SETFSEBLOCKFLAGS structure](ns-d3dkmthk--d3dkmt-setfseblockflags.md) | TBD |
| [D3DKMT_SETVIDPNSOURCEOWNER2 structure](ns-d3dkmthk--d3dkmt-setvidpnsourceowner2.md) | Used to set the VidPN source owner. |
| [D3DKMT_FENCE_PRESENTHISTORYTOKEN structure](ns-d3dkmthk--d3dkmt-fence-presenthistorytoken.md) | The D3DKMT_FENCE_PRESENTHISTORYTOKEN structure identifies a fence present-history operation. |
| [D3DKMT_DESTROYOVERLAY structure](ns-d3dkmthk--d3dkmt-destroyoverlay.md) | The D3DKMT_DESTROYOVERLAY structure contains the handle to the overlay to destroy. |
| [D3DKMT_GETSCANLINE structure](ns-d3dkmthk--d3dkmt-getscanline.md) | The D3DKMT_GETSCANLINE structure contains information about a video present source's vertical blanking status. |
| [D3DKMT_GET_PTE structure](ns-d3dkmthk--d3dkmt-get-pte.md) | TBD |
| [D3DKMT_OUTPUTDUPL_METADATA structure](ns-d3dkmthk--d3dkmt-outputdupl-metadata.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_OPENPROTECTEDSESSIONFROMNTHANDLE structure](ns-d3dkmthk--d3dkmt-openprotectedsessionfromnthandle.md) | Used to open a protected session from the NT handle. |
| [D3DKMT_SETVIDPNSOURCEHWPROTECTION structure](ns-d3dkmthk--d3dkmt-setvidpnsourcehwprotection.md) | TBD |
| [D3DKMT_GDIMODEL_SYSMEM_PRESENTHISTORYTOKEN structure](ns-d3dkmthk--d3dkmt-gdimodel-sysmem-presenthistorytoken.md) | The D3DKMT_GDIMODEL_SYSMEM_PRESENTHISTORYTOKEN structure identifies a GDI system present-history operation. |
| [D3DKMT_MULTIPLANE_OVERLAY structure](ns-d3dkmthk-d3dkmt-multiplane-overlay.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_QUERY_GPUMMU_CAPS structure](ns-d3dkmthk--d3dkmt-query-gpummu-caps.md) | TBD |
| [D3DKMT_VIDSCH_ESCAPE structure](ns-d3dkmthk--d3dkmt-vidsch-escape.md) | The D3DKMT_VIDSCH_ESCAPE structure describes how to control the graphics processing unit (GPU) scheduler (which is part of Dxgkrnl.sys) in a call to the D3DKMTEscape function. |
| [D3DKMT_OPENSYNCHRONIZATIONOBJECT structure](ns-d3dkmthk--d3dkmt-opensynchronizationobject.md) | The D3DKMT_OPENSYNCHRONIZATIONOBJECT structure describes a synchronization object that the D3DKMTOpenSynchronizationObject function opens. |
| [D3DKMT_PROCESS_VERIFIER_OPTION structure](ns-d3dkmthk--d3dkmt-process-verifier-option.md) | TBD |
| [D3DKMT_SEGMENTSIZEINFO structure](ns-d3dkmthk--d3dkmt-segmentsizeinfo.md) | The D3DKMT_SEGMENTSIZEINFO structure describes the size, in bytes, of memory and aperture segments. |
| [D3DKMT_ISBADDRIVERFORHWPROTECTIONDISABLED structure](ns-d3dkmthk--d3dkmt-isbaddriverforhwprotectiondisabled.md) | TBD |
| [D3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT3 structure](ns-d3dkmthk--d3dkmt-checkmultiplaneoverlaysupport3.md) | TBD |
| [D3DKMT_DOD_SET_DIRTYRECT_MODE structure](ns-d3dkmthk--d3dkmt-dod-set-dirtyrect-mode.md) | TBD |
| [D3DKMT_OUTPUTDUPL_RELEASE_FRAME structure](ns-d3dkmthk--d3dkmt-outputdupl-release-frame.md) | Defines the duplicated desktop image that is to be released in a call to the D3DKMTOutputDuplReleaseFrame function. |
| [D3DKMT_REQUEST_MACHINE_CRASH_ESCAPE structure](ns-d3dkmthk--d3dkmt-request-machine-crash-escape.md) | TBD |
| [D3DKMT_GETOVERLAYSTATE structure](ns-d3dkmthk--d3dkmt-getoverlaystate.md) | The D3DKMT_GETOVERLAYSTATE structure describes parameters that the D3DKMTGetOverlayState function uses to retrieve status about an overlay. |
| [D3DKMT_REMOVESURFACEFROMSWAPCHAIN structure](ns-d3dkmthk--d3dkmt-removesurfacefromswapchain.md) | Used to remove a surface from the swap chain. |
| [D3DKMT_DEVICEPRESENT_STATE_DWM structure](ns-d3dkmthk--d3dkmt-devicepresent-state-dwm.md) | TBD |
| [D3DKMT_LOCK2 structure](ns-d3dkmthk--d3dkmt-lock2.md) | D3DKMT_LOCK2 describes parameters for locking an allocation. |
| [D3DKMT_OUTPUTDUPL_GET_POINTER_SHAPE_DATA structure](ns-d3dkmthk--d3dkmt-outputdupl-get-pointer-shape-data.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_PANELFITTER_SUPPORT structure](ns-d3dkmthk--d3dkmt-panelfitter-support.md) | TBD |
| [D3DKMT_SUBMITCOMMANDFLAGS structure](ns-d3dkmthk--d3dkmt-submitcommandflags.md) | TBD |
| [D3DKMT_UNLOCK2 structure](ns-d3dkmthk--d3dkmt-unlock2.md) | D3DKMT_UNLOCK2 describes an allocation to unlock. |
| [D3DKMT_BUDGETCHANGENOTIFICATION structure](ns-d3dkmthk--d3dkmt-budgetchangenotification.md) | TBD |
| [D3DKMT_LOCK structure](ns-d3dkmthk--d3dkmt-lock.md) | The D3DKMT_LOCK structure describes parameters for locking an allocation. |
| [D3DKMT_CREATEPROTECTEDSESSION structure](ns-d3dkmthk--d3dkmt-createprotectedsession.md) | Used to create a protected session. |
| [D3DKMT_VIRTUALADDRESSFLAGS structure](ns-d3dkmthk--d3dkmt-virtualaddressflags.md) | TBD |
| [D3DKMT_CPDRIVERNAME structure](ns-d3dkmthk--d3dkmt-cpdrivername.md) | TBD |
| [D3DKMT_CHECKOCCLUSION structure](ns-d3dkmthk--d3dkmt-checkocclusion.md) | The D3DKMT_CHECKOCCLUSION structure contains the handle to the window to check for occlusion. |
| [D3DKMT_CREATEBUNDLEOBJECT structure](ns-d3dkmthk--d3dkmt-createbundleobject.md) | Holds information to create a bundle object. |
| [D3DKMT_MULTIPLANE_OVERLAY_CAPS structure](ns-d3dkmthk--d3dkmt-multiplane-overlay-caps.md) | TBD |
| [D3DKMT_SUBMITCOMMAND structure](ns-d3dkmthk--d3dkmt-submitcommand.md) | The D3DKMT_SUBMITCOMMAND structure is used to submit command buffers on contexts that support graphics processing unit (GPU) virtual addressing. |
| [D3DKMT_ADJUSTFULLSCREENGAMMA structure](ns-d3dkmthk--d3dkmt-adjustfullscreengamma.md) | TBD |
| [D3DKMT_CREATEOVERLAY structure](ns-d3dkmthk--d3dkmt-createoverlay.md) | The D3DKMT_CREATEOVERLAY structure describes overlay hardware. |
| [D3DKMT_DEVICEPAGEFAULT_STATE structure](ns-d3dkmthk--d3dkmt-devicepagefault-state.md) | TBD |
| [D3DKMT_GETCONTEXTINPROCESSSCHEDULINGPRIORITY structure](ns-d3dkmthk--d3dkmt-getcontextinprocessschedulingpriority.md) | Describes information that is required for an in-process (in-proc) Microsoft Direct3D composition device to retrieve the scheduling priority for a device context that is in the same process as other device contexts. |
| [D3DKMT_MULTIPLANE_OVERLAY2 structure](ns-d3dkmthk--d3dkmt-multiplane-overlay2.md) | TBD |
| [D3DKMT_QUERYVIDEOMEMORYINFO structure](ns-d3dkmthk--d3dkmt-queryvideomemoryinfo.md) | TBD |
| [D3DKMT_DMM_ESCAPE structure](ns-d3dkmthk--d3dkmt-dmm-escape.md) | Do not use the D3DKMT_DMM_ESCAPE structure; it is for testing purposes only. The D3DKMT_DMM_ESCAPE structure describes how to control the display mode manager (DMM) in a call to the D3DKMTEscape function. |
| [D3DKMT_GET_SEGMENT_CAPS structure](ns-d3dkmthk--d3dkmt-get-segment-caps.md) | TBD |
| [D3DKMT_OPENADAPTERFROMGDIDISPLAYNAME structure](ns-d3dkmthk--d3dkmt-openadapterfromgdidisplayname.md) | The D3DKMT_OPENADAPTERFROMGDIDISPLAYNAME structure describes the mapping of the given name of a GDI device to a graphics adapter handle and monitor output. |
| [D3DKMT_STANDARDALLOCATION_EXISTINGHEAP structure](ns-d3dkmthk--d3dkmt-standardallocation-existingheap.md) | Holds information about the existing heap. |
| [D3DKMT_ADAPTER_VERIFIER_OPTION structure](ns-d3dkmthk--d3dkmt-adapter-verifier-option.md) | TBD |
| [D3DKMT_CHANGESURFACEPOINTER structure](ns-d3dkmthk--d3dkmt-changesurfacepointer.md) | TBD |
| [D3DKMT_OPENADAPTERFROMHDC structure](ns-d3dkmthk--d3dkmt-openadapterfromhdc.md) | The D3DKMT_OPENADAPTERFROMHDC structure describes the mapping of a device context handle (HDC) to a graphics adapter handle and monitor output. |
| [D3DKMT_CREATECONTEXT structure](ns-d3dkmthk--d3dkmt-createcontext.md) | The D3DKMT_CREATECONTEXT structure describes a kernel-mode device context to create. |
| [D3DKMT_VIRTUALADDRESSINFO structure](ns-d3dkmthk--d3dkmt-virtualaddressinfo.md) | TBD |
| [D3DKMT_MPO3DDI_SUPPORT structure](ns-d3dkmthk--d3dkmt-mpo3ddi-support.md) | A structure that holds the support status. |
| [D3DKMT_POLLDISPLAYCHILDREN structure](ns-d3dkmthk--d3dkmt-polldisplaychildren.md) | The D3DKMT_POLLDISPLAYCHILDREN structure describes parameters for querying for connectivity status of all child devices of the given display adapter. |
| [D3DKMT_PRESENT_MULTIPLANE_OVERLAY2 structure](ns-d3dkmthk--d3dkmt-present-multiplane-overlay2.md) | TBD |
| [D3DKMT_SETHWPROTECTIONTEARDOWNRECOVERY structure](ns-d3dkmthk--d3dkmt-sethwprotectionteardownrecovery.md) | TBD |
| [D3DKMT_OPENRESOURCEFROMNTHANDLE structure](ns-d3dkmthk--d3dkmt-openresourcefromnthandle.md) | Describes information that is required to open a shared resource from an NT handle to the process. The shared resource can be a set of allocations, a keyed mutex, or a synchronization object. |
| [D3DKMT_UMDFILENAMEINFO structure](ns-d3dkmthk--d3dkmt-umdfilenameinfo.md) | The D3DKMT_UMDFILENAMEINFO structure contains the name of an OpenGL ICD that is based on the specified version of the DirectX runtime. |
| [D3DKMT_VIDMM_ESCAPE structure](ns-d3dkmthk--d3dkmt-vidmm-escape.md) | The D3DKMT_VIDMM_ESCAPE structure describes how to control the video memory manager (which is part of Dxgkrnl.sys) in a call to the D3DKMTEscape function. |
| [D3DKMT_WAITFORIDLE structure](ns-d3dkmthk--d3dkmt-waitforidle.md) | The D3DKMT_WAITFORIDLE structure specifies a display device to wait for an idle condition. |
| [D3DKMT_ADAPTERREGISTRYINFO structure](ns-d3dkmthk--d3dkmt-adapterregistryinfo.md) | The D3DKMT_ADAPTERREGISTRYINFO structure contains registry information about the graphics adapter. |
| [D3DKMT_MULTIPLANE_OVERLAY_POST_COMPOSITION structure](ns-d3dkmthk--d3dkmt-multiplane-overlay-post-composition.md) | TBD |
| [D3DKMT_ADAPTER_VERIFIER_VIDMM_TRIM_INTERVAL structure](ns-d3dkmthk--d3dkmt-adapter-verifier-vidmm-trim-interval.md) | TBD |
| [D3DKMT_CHECK_MULTIPLANE_OVERLAY_PLANE2 structure](ns-d3dkmthk--d3dkmt-check-multiplane-overlay-plane2.md) | TBD |
| [D3DKMT_CREATEDEVICEFLAGS structure](ns-d3dkmthk--d3dkmt-createdeviceflags.md) | The D3DKMT_CREATEDEVICEFLAGS structure identifies the type of device context to be created in a call to the D3DKMTCreateDevice function. |
| [D3DKMT_QUERYRESOURCEINFO structure](ns-d3dkmthk--d3dkmt-queryresourceinfo.md) | The D3DKMT_QUERYRESOURCEINFO structure describes parameters for retrieving information about a resource. |
| [D3DKMT_XBOX structure](ns-d3dkmthk--d3dkmt-xbox.md) | TBD |
| [D3DKMT_DESTROYDEVICE structure](ns-d3dkmthk--d3dkmt-destroydevice.md) | The D3DKMT_DESTROYDEVICE structure contains a handle to the kernel-mode device context to release. |
| [D3DKMT_DEVICERESET_STATE structure](ns-d3dkmthk--d3dkmt-devicereset-state.md) | The D3DKMT_DEVICERESET_STATE structure identifies reset status. |
| [D3DKMT_CREATEALLOCATIONFLAGS structure](ns-d3dkmthk--d3dkmt-createallocationflags.md) | The D3DKMT_CREATEALLOCATIONFLAGS structure identifies how to create an allocation in a call to the D3DKMTCreateAllocation function. |
| [D3DKMT_DESTROYSYNCHRONIZATIONOBJECT structure](ns-d3dkmthk--d3dkmt-destroysynchronizationobject.md) | The D3DKMT_DESTROYSYNCHRONIZATIONOBJECT structure contains the handle to a synchronization object to destroy. |
| [D3DKMT_CREATESTANDARDALLOCATIONFLAGS structure](ns-d3dkmthk--d3dkmt-createstandardallocationflags.md) | Used to create standard allocation flags. |
| [D3DKMT_GETALLOCATIONPRIORITY structure](ns-d3dkmthk--d3dkmt-getallocationpriority.md) | TBD |
| [D3DKMT_ACQUIREKEYEDMUTEX structure](ns-d3dkmthk--d3dkmt-acquirekeyedmutex.md) | The D3DKMT_ACQUIREKEYEDMUTEX structure describes a keyed mutex that the D3DKMTAcquireKeyedMutex function acquires. |
| [D3DKMT_CREATEDCFROMMEMORY structure](ns-d3dkmthk--d3dkmt-createdcfrommemory.md) | The D3DKMT_CREATEDCFROMMEMORY structure describes parameters for creating the display context. |
| [D3DKMT_QUERYPROTECTEDSESSIONSTATUS structure](ns-d3dkmthk--d3dkmt-queryprotectedsessionstatus.md) | Used to query the status of the protected session. |
| [D3DKMT_HISTORY_BUFFER_STATUS structure](ns-d3dkmthk--d3dkmt-history-buffer-status.md) | TBD |
| [D3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT structure](ns-d3dkmthk--d3dkmt-checkmultiplaneoverlaysupport.md) | TBD |
| [D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2 structure](ns-d3dkmthk--d3dkmt-signalsynchronizationobjectfromgpu2.md) | D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2 is used with D3DKMTSignalSynchronizationObjectFromGpu2 to signal a monitored fence. |
| [D3DKMT_GETSETSWAPCHAINMETADATA structure](ns-d3dkmthk--d3dkmt-getsetswapchainmetadata.md) | TBD |
| [D3DKMT_RELEASEKEYEDMUTEX structure](ns-d3dkmthk--d3dkmt-releasekeyedmutex.md) | The D3DKMT_RELEASEKEYEDMUTEX structure describes a keyed mutex that the D3DKMTReleaseKeyedMutex function releases. |
| [D3DKMT_PRESENT_REDIRECTEDS_FLAGS structure](ns-d3dkmthk--d3dkmt-present-redirecteds-flags.md) | The flags used in D3DKMT_PRESENT_REDIRECTED. |
| [D3DKMT_FLIPINFOFLAGS structure](ns-d3dkmthk--d3dkmt-flipinfoflags.md) | The D3DKMT_FLIPINFOFLAGS structure identifies flipping capabilities of the display miniport driver that the OpenGL installable client driver (ICD) obtains by calling the D3DKMTQueryAdapterInfo function. |
| [D3DKMT_OPENNTHANDLEFROMNAME structure](ns-d3dkmthk--d3dkmt-opennthandlefromname.md) | Describes information that is required to open an NT handle to the process from a graphics adapter name. |
| [D3DKMT_OFFERALLOCATIONS structure](ns-d3dkmthk--d3dkmt-offerallocations.md) | Defines the video memory allocations that the driver offers for reuse. Used with the D3DKMTOfferAllocations function. |
| [D3DKMT_SETQUEUEDLIMIT structure](ns-d3dkmthk--d3dkmt-setqueuedlimit.md) | The D3DKMT_SETQUEUEDLIMIT structure describes parameters for setting or retrieving the limit for the number of operations of the given type that can be queued for the given device. |
| [D3DKMT_SCATTERBLT structure](ns-d3dkmthk--d3dkmt-scatterblt.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_SEGMENTGROUPSIZEINFO structure](ns-d3dkmthk--d3dkmt-segmentgroupsizeinfo.md) | A structure that holds information about the segment group size. |
| [D3DKMT_DESTROY_OUTPUTDUPL structure](ns-d3dkmthk--d3dkmt-destroy-outputdupl.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_INVALIDATEACTIVEVIDPN structure](ns-d3dkmthk--d3dkmt-invalidateactivevidpn.md) | The D3DKMT_INVALIDATEACTIVEVIDPN structure describes parameters that invalidate the active video present network (VidPN) currently in use. |
| [D3DKMT_QUERYFSEFLAGS structure](ns-d3dkmthk--d3dkmt-queryfseflags.md) | TBD |
| [D3DKMT_PRESENT structure](ns-d3dkmthk--d3dkmt-present.md) | The D3DKMT_PRESENT structure describes the present operation. |
| [D3DKMT_ADAPTERTYPE structure](ns-d3dkmthk--d3dkmt-adaptertype.md) | Specifies the type of display device that the graphics adapter supports. |
| [D3DKMT_ACQUIREKEYEDMUTEX2 structure](ns-d3dkmthk--d3dkmt-acquirekeyedmutex2.md) | Describes a keyed mutex object that the D3DKMTAcquireKeyedMutex2 function acquires that includes private data. |
| [D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU structure](ns-d3dkmthk--d3dkmt-signalsynchronizationobjectfromgpu.md) | D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU is used with D3DKMTSignalSynchronizationObjectFromGpu to signal a monitored fence. |
| [D3DKMT_PRESENT_MULTIPLANE_OVERLAY structure](ns-d3dkmthk-d3dkmt-present-multiplane-overlay.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_OUTPUTDUPL_GET_FRAMEINFO structure](ns-d3dkmthk--d3dkmt-outputdupl-get-frameinfo.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_GET_POST_COMPOSITION_CAPS structure](ns-d3dkmthk--d3dkmt-get-post-composition-caps.md) | TBD |
| [D3DKMT_MIRACAST_CHUNK_DATA structure](ns-d3dkmthk-d3dkmt-miracast-chunk-data.md) | TBD |
| [D3DKMT_INVALIDATECACHE structure](ns-d3dkmthk--d3dkmt-invalidatecache.md) | TBD |
| [D3DKMT_ENUMADAPTERS2 structure](ns-d3dkmthk--d3dkmt-enumadapters2.md) | TBD |
| [D3DKMT_RECLAIMALLOCATIONS structure](ns-d3dkmthk--d3dkmt-reclaimallocations.md) | Describes video memory resources that are to be reclaimed and that the driver previously offered for reuse. Used with the D3DKMTReclaimAllocations function. |
| [D3DKMT_UNREGISTERTRIMNOTIFICATION structure](ns-d3dkmthk--d3dkmt-unregistertrimnotification.md) | D3DKMT_UNREGISTERTRIMNOTIFICATION is used with D3DKMTUnregisterTrimNotification to remove a callback registration for a kernel mode device receiving notifications from a graphics framework (such as OpenGL). |
| [D3DKMT_BDDFALLBACK_CTL structure](ns-d3dkmthk--d3dkmt-bddfallback-ctl.md) | TBD |
| [D3DKMT_DEVICE_ESCAPE structure](ns-d3dkmthk--d3dkmt-device-escape.md) | Do not use the D3DKMT_DEVICE_ESCAPE structure or D3DKMT_DEVICEESCAPE_TYPE enumeration. They are for testing purposes only. The D3DKMT_DEVICE_ESCAPE structure describes how to control the display device in a call to the D3DKMTEscape function. |
| [D3DKMT_CLOSEADAPTER structure](ns-d3dkmthk--d3dkmt-closeadapter.md) | The D3DKMT_CLOSEADAPTER structure specifies the graphics adapter to close. |
| [D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2 structure](ns-d3dkmthk--d3dkmt-signalsynchronizationobject2.md) | The D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2 structure contains information about the synchronization events that the D3DKMTSignalSynchronizationObject2 function signals. |
| [D3DKMT_OUTPUTDUPLPRESENT structure](ns-d3dkmthk--d3dkmt-outputduplpresent.md) | Describes a Desktop Duplication API swapchain present operation. |
| [D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE structure](ns-d3dkmthk--d3dkmt-queryprotectedsessioninfofromnthandle.md) | Used to query information on the protected session. |
| [D3DKMT_CREATEKEYEDMUTEX structure](ns-d3dkmthk--d3dkmt-createkeyedmutex.md) | The D3DKMT_CREATEKEYEDMUTEX structure describes a keyed mutex that the D3DKMTCreateKeyedMutex function creates. |
| [D3DKMT_MIRACAST_DISPLAY_DEVICE_STATUS structure](ns-d3dkmthk--d3dkmt-miracast-display-device-status.md) | TBD |
| [D3DKMT_MARKDEVICEASERROR structure](ns-d3dkmthk--d3dkmt-markdeviceaserror.md) | TBD |
| [D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY structure](ns-d3dkmthk--d3dkmt-query-physical-adapter-pnp-key.md) | A structure that holds information to query the physical adapter PNP key. |
| [D3DKMT_FREEGPUVIRTUALADDRESS structure](ns-d3dkmthk--d3dkmt-freegpuvirtualaddress.md) | D3DKMT_FREEGPUVIRTUALADDRESS is used with FreeGpuVirtualAddress to release a range of graphics processing unit (GPU) virtual addresses that were previously reserved or mapped. |
| [D3DKMT_BLTMODEL_PRESENTHISTORYTOKEN structure](ns-d3dkmthk--d3dkmt-bltmodel-presenthistorytoken.md) | The D3DKMT_BLTMODEL_PRESENTHISTORYTOKEN structure identifies a bit-block transfer (bitblt) present-history operation. |
| [D3DKMT_CHECKSHAREDRESOURCEACCESS structure](ns-d3dkmthk--d3dkmt-checksharedresourceaccess.md) | The D3DKMT_CHECKSHAREDRESOURCEACCESS structure describes parameters that the D3DKMTCheckSharedResourceAccess function uses to determine if a process can access a shared resource. |
| [D3DKMT_MULTIPLANEOVERLAY_SUPPORT structure](ns-d3dkmthk--d3dkmt-multiplaneoverlay-support.md) | TBD |
| [D3DKMT_CHECKVIDPNEXCLUSIVEOWNERSHIP structure](ns-d3dkmthk--d3dkmt-checkvidpnexclusiveownership.md) | The D3DKMT_CHECKVIDPNEXCLUSIVEOWNERSHIP structure describes the parameters to determine the video present source in the path of a video present network (VidPN) topology that exclusively owns the VidPN. |
| [D3DKMT_WAITFORSYNCHRONIZATIONOBJECT structure](ns-d3dkmthk--d3dkmt-waitforsynchronizationobject.md) | The D3DKMT_WAITFORSYNCHRONIZATIONOBJECT structure contains information about the synchronization events that the D3DKMTWaitForSynchronizationObject function waits for to occur. |
| [D3DKMT_DESTROYCONTEXT structure](ns-d3dkmthk--d3dkmt-destroycontext.md) | The D3DKMT_DESTROYCONTEXT structure contains a handle to a kernel-mode device context to release. |
| [D3DKMT_ENUMADAPTERS structure](ns-d3dkmthk--d3dkmt-enumadapters.md) | Supplies information for enumerating all graphics adapters on the system. |
| [D3DKMT_SETDISPLAYMODE structure](ns-d3dkmthk--d3dkmt-setdisplaymode.md) | The D3DKMT_SETDISPLAYMODE structure describes the primary allocation that is used for scanning out to the display. |
| [D3DKMT_PRESENT_STATS structure](ns-d3dkmthk--d3dkmt-present-stats.md) | The D3DKMT_PRESENT_STATS structure describes present status for a rendering device. |
| [D3DKMT_TDRDBGCTRL_ESCAPE structure](ns-d3dkmthk--d3dkmt-tdrdbgctrl-escape.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_SETSTABLEPOWERSTATE structure](ns-d3dkmthk--d3dkmt-setstablepowerstate.md) | TBD |
| [D3DKMT_ADAPTER_VERIFIER_OPTION_DATA structure](ns-d3dkmthk--d3dkmt-adapter-verifier-option-data.md) | TBD |
| [D3DKMT_GETDISPLAYMODELIST structure](ns-d3dkmthk--d3dkmt-getdisplaymodelist.md) | The D3DKMT_GETDISPLAYMODELIST structure describes a list of display modes. |
| [D3DKMT_PRESENT_MULTIPLANE_OVERLAY3 structure](ns-d3dkmthk--d3dkmt-present-multiplane-overlay3.md) | TBD |
| [D3DKMT_CREATECONTEXTVIRTUAL structure](ns-d3dkmthk--d3dkmt-createcontextvirtual.md) | D3DKMT_CREATECONTEXTVIRTUAL is used with D3DKMTCreateContextVirtual to create a kernel mode device context that supports virtual addressing. |
| [D3DKMT_CREATESWAPCHAIN structure](ns-d3dkmthk--d3dkmt-createswapchain.md) | TBD |
| [D3DKMT_EVICTION_CRITERIA structure](ns-d3dkmthk--d3dkmt-eviction-criteria.md) | TBD |
| [D3DKMT_SETFSEBLOCK structure](ns-d3dkmthk--d3dkmt-setfseblock.md) | TBD |
| [D3DKMT_QUERYALLOCATIONRESIDENCY structure](ns-d3dkmthk--d3dkmt-queryallocationresidency.md) | The D3DKMT_QUERYALLOCATIONRESIDENCY structure describes information for retrieving the residency status from a resource or list of allocations. |
| [D3DKMT_BRIGHTNESS_INFO structure](ns-d3dkmthk--d3dkmt-brightness-info.md) | Contains information about the brightness of an integrated display panel. |
| [D3DKMT_DIRECTFLIP_SUPPORT structure](ns-d3dkmthk--d3dkmt-directflip-support.md) | Indicates whether the user-mode driver supports Direct Flip operations, in which video memory is seamlessly flipped between an application's managed primary allocations and the Desktop Window Manager (DWM) managed primary allocations. |
| [D3DKMT_TRIMPROCESSCOMMITMENT_FLAGS structure](ns-d3dkmthk--d3dkmt-trimprocesscommitment-flags.md) | TBD |
| [D3DKMT_CREATEALLOCATION structure](ns-d3dkmthk--d3dkmt-createallocation.md) | The D3DKMT_CREATEALLOCATION structure describes parameters for creating allocations. |
| [D3DKMT_GETRUNTIMEDATA structure](ns-d3dkmthk--d3dkmt-getruntimedata.md) | TBD |
| [D3DKMT_DEBUG_SNAPSHOT_ESCAPE structure](ns-d3dkmthk--d3dkmt-debug-snapshot-escape.md) | Do not use the D3DKMT_DEBUG_SNAPSHOT_ESCAPE structure; it is for testing purposes only. The D3DKMT_DEBUG_SNAPSHOT_ESCAPE structure describes a debug snapshot that is returned in a call to the D3DKMTEscape function. |
| [D3DKMT_PLANE_SPECIFIC_INPUT_FLAGS structure](ns-d3dkmthk--d3dkmt-plane-specific-input-flags.md) | TBD |
| [D3DKMT_CHANGEVIDEOMMEMORYRESERVATION structure](ns-d3dkmthk--d3dkmt-changevideommemoryreservation.md) | TBD |
| [D3DKMT_PROCESS_VERIFIER_VIDMM_RESTRICT_BUDGET structure](ns-d3dkmthk--d3dkmt-process-verifier-vidmm-restrict-budget.md) | TBD |
| [D3DKMT_GETDEVICESTATE structure](ns-d3dkmthk--d3dkmt-getdevicestate.md) | The D3DKMT_GETDEVICESTATE structure describes parameters for retrieving the state of a device. |
| [D3DKMT_DESTROYPROTECTEDSESSION structure](ns-d3dkmthk--d3dkmt-destroyprotectedsession.md) | Holds information to destroy a protected session. |
| [D3DKMT_TRIMNOTIFICATION structure](ns-d3dkmthk--d3dkmt-trimnotification.md) | D3DKMT_TRIMNOTIFICATION is used to notify a driver to trim its memory residency list. |
| [D3DKMT_OPENKEYEDMUTEX structure](ns-d3dkmthk--d3dkmt-openkeyedmutex.md) | The D3DKMT_OPENKEYEDMUTEX structure describes a keyed mutex that the D3DKMTOpenKeyedMutex function opens. |
| [D3DKMT_MULTIPLANEOVERLAY_STRETCH_SUPPORT structure](ns-d3dkmthk--d3dkmt-multiplaneoverlay-stretch-support.md) | TBD |
| [D3DKMT_SETALLOCATIONPRIORITY structure](ns-d3dkmthk--d3dkmt-setallocationpriority.md) | The D3DKMT_SETALLOCATIONPRIORITY structure describes the priority level to set a resource or list of allocations to. |
| [D3DKMT_CREATEPAGINGQUEUE structure](ns-d3dkmthk--d3dkmt-createpagingqueue.md) | D3DKMT_CREATEPAGINGQUEUE is used with D3DKMTCreatePagingQueue to create a device paging queue that can be used to synchronize with video memory management operations for the device, such as making the device resource resident. |
| [D3DKMT_UMD_DRIVER_VERSION structure](ns-d3dkmthk--d3dkmt-umd-driver-version.md) | Indicates the version number of the user-mode driver. |
| [D3DKMT_DISPLAYMODE structure](ns-d3dkmthk--d3dkmt-displaymode.md) | The D3DKMT_DISPLAYMODE structure describes a display mode. |
| [D3DKMT_DESTROYKEYEDMUTEX structure](ns-d3dkmthk--d3dkmt-destroykeyedmutex.md) | The D3DKMT_DESTROYKEYEDMUTEX structure describes a keyed mutex that the D3DKMTDestroyKeyedMutex function destroys. |
| [D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE structure](ns-d3dkmthk--d3dkmt-submitsignalsyncobjectstohwqueue.md) | A structure holding information to submit a signal to the hardware queue. |
| [D3DKMT_OUTPUTDUPLCONTEXTSCOUNT structure](ns-d3dkmthk--d3dkmt-outputduplcontextscount.md) | Specifies the number of current Desktop Duplication API (DDA) clients that are attached to a given video present network (VidPN). |
| [D3DKMT_DEVICE_IDS structure](ns-d3dkmthk--d3dkmt-device-ids.md) | TBD |
| [D3DKMT_GET_DEVICE_VIDPN_OWNERSHIP_INFO structure](ns-d3dkmthk--d3dkmt-get-device-vidpn-ownership-info.md) | TBD |
| [D3DKMT_ADAPTERINFO structure](ns-d3dkmthk--d3dkmt-adapterinfo.md) | Supplies configuration information about a graphics adapter. |
| [DXGK_GRAPHICSPOWER_REGISTER_INPUT_V_1_1 structure](ns-d3dkmthk--dxgk-graphicspower-register-input-v-1-1.md) | Used to register the power state of a new input. |
| [D3DKMT_SCATTERBLTS structure](ns-d3dkmthk--d3dkmt-scatterblts.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_ADAPTERADDRESS structure](ns-d3dkmthk--d3dkmt-adapteraddress.md) | The D3DKMT_ADAPTERADDRESS structure describes the physical location of the graphics adapter. |
| [D3DKMT_SEGMENT_CAPS structure](ns-d3dkmthk--d3dkmt-segment-caps.md) | TBD |
| [D3DKMT_DLIST_DRIVER_NAME structure](ns-d3dkmthk--d3dkmt-dlist-driver-name.md) | TBD |
| [D3DKMT_MULTIPLANEOVERLAY_DECODE_SUPPORT structure](ns-d3dkmthk--d3dkmt-multiplaneoverlay-decode-support.md) | TBD |
| [D3DKMT_SIGNALSYNCHRONIZATIONOBJECT structure](ns-d3dkmthk--d3dkmt-signalsynchronizationobject.md) | The D3DKMT_SIGNALSYNCHRONIZATIONOBJECT structure contains information about the synchronization events that the D3DKMTSignalSynchronizationObject function signals. |
| [D3DKMT_SETVIDPNSOURCEOWNER1 structure](ns-d3dkmthk--d3dkmt-setvidpnsourceowner1.md) | Describes the information, including output duplication options, needed to set or release the video present source in the path of a video present network (VidPN) topology that owns the VidPN. |
| [D3DKMT_DEVICEPRESENT_QUEUE_STATE structure](ns-d3dkmthk--d3dkmt-devicepresent-queue-state.md) | A structure that holds information on the queue state of a hardware device. |
| [DXGK_ESCAPE_GPUMMUCAPS structure](ns-d3dkmthk--dxgk-escape-gpummucaps.md) | TBD |
| [OBJECT_ATTRIBUTES structure](ns-d3dkmthk--object-attributes.md) | TBD |
| [D3DKMT_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO structure](ns-d3dkmthk-d3dkmt-check-multiplane-overlay-support-return-info.md) | TBD |
| [D3DKMT_OUTPUTDUPL_SNAPSHOT structure](ns-d3dkmthk--d3dkmt-outputdupl-snapshot.md) | Provides information on the current processes in which output duplication is occurring. |
| [D3DKMT_CURRENTDISPLAYMODE structure](ns-d3dkmthk--d3dkmt-currentdisplaymode.md) | The D3DKMT_CURRENTDISPLAYMODE structure describes the current display mode of the specified video source. |
| [D3DKMT_CHECKMONITORPOWERSTATE structure](ns-d3dkmthk--d3dkmt-checkmonitorpowerstate.md) | The D3DKMT_CHECKMONITORPOWERSTATE structure describes the connection to the monitor for which to check the power state. |
| [D3DKMT_DEVICEPRESENT_STATE structure](ns-d3dkmthk--d3dkmt-devicepresent-state.md) | The D3DKMT_DEVICEPRESENT_STATE structure describes parameters for retrieving the present status for a device. |
| [D3DKMT_DESTROYALLOCATION structure](ns-d3dkmthk--d3dkmt-destroyallocation.md) | The D3DKMT_DESTROYALLOCATION structure describes parameters for releasing allocations. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFND3DKMT_OFFERALLOCATIONS callback function](nc-d3dkmthk-pfnd3dkmt-offerallocations.md) | TBD |
| [PFND3DKMT_SETHWPROTECTIONTEARDOWNRECOVERY callback function](nc-d3dkmthk-pfnd3dkmt-sethwprotectionteardownrecovery.md) | TBD |
| [PFND3DKMT_MARKDEVICEASERROR callback function](nc-d3dkmthk-pfnd3dkmt-markdeviceaserror.md) | TBD |
| [PFND3DKMT_DESTROYSYNCHRONIZATIONOBJECT callback function](nc-d3dkmthk-pfnd3dkmt-destroysynchronizationobject.md) | TBD |
| [PFND3DKMT_GETOVERLAYSTATE callback function](nc-d3dkmthk-pfnd3dkmt-getoverlaystate.md) | TBD |
| [PFND3DKMT_SHAREOBJECTS callback function](nc-d3dkmthk-pfnd3dkmt-shareobjects.md) | TBD |
| [PFND3DKMT_UNREGISTERBUDGETCHANGENOTIFICATION callback function](nc-d3dkmthk-pfnd3dkmt-unregisterbudgetchangenotification.md) | TBD |
| [PFND3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT callback](nc-d3dkmthk-pfnd3dkmt-checkmultiplaneoverlaysupport.md) | Reserved for system use. Do not use in your driver. |
| [PFND3DKMT_ESCAPE callback function](nc-d3dkmthk-pfnd3dkmt-escape.md) | TBD |
| [PFND3DKMT_OPENADAPTERFROMDEVICENAME callback function](nc-d3dkmthk-pfnd3dkmt-openadapterfromdevicename.md) | TBD |
| [PFND3DKMT_RENDER callback function](nc-d3dkmthk-pfnd3dkmt-render.md) | TBD |
| [PFND3DKMT_UPDATEOVERLAY callback function](nc-d3dkmthk-pfnd3dkmt-updateoverlay.md) | TBD |
| [PFND3DKMT_CREATEOVERLAY callback function](nc-d3dkmthk-pfnd3dkmt-createoverlay.md) | TBD |
| [PFND3DKMT_OPENADAPTERFROMGDIDISPLAYNAME callback function](nc-d3dkmthk-pfnd3dkmt-openadapterfromgdidisplayname.md) | TBD |
| [PFND3DKMT_PRESENT callback function](nc-d3dkmthk-pfnd3dkmt-present.md) | TBD |
| [PFND3DKMT_DESTROYALLOCATION2 callback function](nc-d3dkmthk-pfnd3dkmt-destroyallocation2.md) | TBD |
| [PFND3DKMT_GETMULTISAMPLEMETHODLIST callback function](nc-d3dkmthk-pfnd3dkmt-getmultisamplemethodlist.md) | TBD |
| [PFND3DKMT_OPENRESOURCE2 callback function](nc-d3dkmthk-pfnd3dkmt-openresource2.md) | TBD |
| [PFND3DKMT_CREATEPAGINGQUEUE callback function](nc-d3dkmthk-pfnd3dkmt-createpagingqueue.md) | TBD |
| [PFND3DKMT_RECLAIMALLOCATIONS2 callback function](nc-d3dkmthk-pfnd3dkmt-reclaimallocations2.md) | TBD |
| [PFND3DKMT_WAITFORSYNCHRONIZATIONOBJECTFROMCPU callback function](nc-d3dkmthk-pfnd3dkmt-waitforsynchronizationobjectfromcpu.md) | TBD |
| [PFND3DKMT_CREATEOUTPUTDUPL callback function](nc-d3dkmthk-pfnd3dkmt-createoutputdupl.md) | TBD |
| [PFND3DKMT_CHANGEVIDEOMEMORYRESERVATION callback function](nc-d3dkmthk-pfnd3dkmt-changevideomemoryreservation.md) | TBD |
| [PFND3DKMT_CREATEDCFROMMEMORY callback function](nc-d3dkmthk-pfnd3dkmt-createdcfrommemory.md) | TBD |
| [PDXGK_FSTATE_NOTIFICATION callback function](nc-d3dkmthk-pdxgk-fstate-notification.md) | TBD |
| [PFND3DKMT_SETPROCESSSCHEDULINGPRIORITYCLASS callback function](nc-d3dkmthk-pfnd3dkmt-setprocessschedulingpriorityclass.md) | TBD |
| [PFND3DKMT_REGISTERTRIMNOTIFICATION callback function](nc-d3dkmthk-pfnd3dkmt-registertrimnotification.md) | TBD |
| [PFND3DKMT_FLIPOVERLAY callback function](nc-d3dkmthk-pfnd3dkmt-flipoverlay.md) | TBD |
| [PFND3DKMT_GETCONTEXTINPROCESSSCHEDULINGPRIORITY callback function](nc-d3dkmthk-pfnd3dkmt-getcontextinprocessschedulingpriority.md) | TBD |
| [PFND3DKMT_SETVIDPNSOURCEHWPROTECTION callback function](nc-d3dkmthk-pfnd3dkmt-setvidpnsourcehwprotection.md) | TBD |
| [PFND3DKMT_OPENRESOURCE callback function](nc-d3dkmthk-pfnd3dkmt-openresource.md) | TBD |
| [PFND3DKMT_DESTROYPAGINGQUEUE callback function](nc-d3dkmthk-pfnd3dkmt-destroypagingqueue.md) | TBD |
| [PFND3DKMT_GETDEVICESTATE callback function](nc-d3dkmthk-pfnd3dkmt-getdevicestate.md) | TBD |
| [PFND3DKMT_RESERVEGPUVIRTUALADDRESS callback function](nc-d3dkmthk-pfnd3dkmt-reservegpuvirtualaddress.md) | TBD |
| [PFND3DKMT_SETHYBRIDLISTVVALUE callback function](nc-d3dkmthk-pfnd3dkmt-sethybridlistvvalue.md) | TBD |
| [PFND3DKMT_POLLDISPLAYCHILDREN callback function](nc-d3dkmthk-pfnd3dkmt-polldisplaychildren.md) | TBD |
| [PFND3DKMT_CREATESYNCHRONIZATIONOBJECT callback function](nc-d3dkmthk-pfnd3dkmt-createsynchronizationobject.md) | TBD |
| [PFND3DKMT_DESTROYOVERLAY callback function](nc-d3dkmthk-pfnd3dkmt-destroyoverlay.md) | TBD |
| [PFND3DKMT_CREATEDEVICE callback function](nc-d3dkmthk-pfnd3dkmt-createdevice.md) | TBD |
| [PFND3DKMT_GETPRESENTHISTORY callback function](nc-d3dkmthk-pfnd3dkmt-getpresenthistory.md) | TBD |
| [PFND3DKMT_TRIMPROCESSCOMMITMENT callback function](nc-d3dkmthk-pfnd3dkmt-trimprocesscommitment.md) | TBD |
| [PFND3DKMT_CHECKVIDPNEXCLUSIVEOWNERSHIP callback function](nc-d3dkmthk-pfnd3dkmt-checkvidpnexclusiveownership.md) | TBD |
| [PFND3DKMT_DESTROYKEYEDMUTEX callback function](nc-d3dkmthk-pfnd3dkmt-destroykeyedmutex.md) | TBD |
| [PFND3DKMT_FREEGPUVIRTUALADDRESS callback function](nc-d3dkmthk-pfnd3dkmt-freegpuvirtualaddress.md) | TBD |
| [PFND3DKMT_UNLOCK2 callback function](nc-d3dkmthk-pfnd3dkmt-unlock2.md) | TBD |
| [PFND3DKMT_CLOSEADAPTER callback function](nc-d3dkmthk-pfnd3dkmt-closeadapter.md) | TBD |
| [PFND3DKMT_DESTROYCONTEXT callback function](nc-d3dkmthk-pfnd3dkmt-destroycontext.md) | TBD |
| [PFND3DKMT_QUERYVIDEOMEMORYINFO callback function](nc-d3dkmthk-pfnd3dkmt-queryvideomemoryinfo.md) | TBD |
| [PFND3DKMT_MAKERESIDENT callback function](nc-d3dkmthk-pfnd3dkmt-makeresident.md) | TBD |
| [PFND3DKMT_SETVIDPNSOURCEOWNER callback function](nc-d3dkmthk-pfnd3dkmt-setvidpnsourceowner.md) | TBD |
| [PFND3DKMT_LOCK callback function](nc-d3dkmthk-pfnd3dkmt-lock.md) | TBD |
| [PFND3DKMT_GETCONTEXTSCHEDULINGPRIORITY callback function](nc-d3dkmthk-pfnd3dkmt-getcontextschedulingpriority.md) | TBD |
| [PFND3DKMT_SETSTABLEPOWERSTATE callback function](nc-d3dkmthk-pfnd3dkmt-setstablepowerstate.md) | TBD |
| [PDXGK_REMOVAL_NOTIFICATION callback](nc-d3dkmthk-pdxgk-removal-notification.md) | A callback indicating that the graphics device is being removed. |
| [PFND3DKMT_DESTROYDEVICE callback function](nc-d3dkmthk-pfnd3dkmt-destroydevice.md) | TBD |
| [PDXGK_SET_SHARED_POWER_COMPONENT_STATE callback function](nc-d3dkmthk-pdxgk-set-shared-power-component-state.md) | TBD |
| [PFND3DKMT_OPENSWAPCHAIN callback function](nc-d3dkmthk-pfnd3dkmt-openswapchain.md) | TBD |
| [PFND3DKMT_OPENSYNCOBJECTFROMNTHANDLE callback function](nc-d3dkmthk-pfnd3dkmt-opensyncobjectfromnthandle.md) | TBD |
| [PFND3DKMT_GETALLOCATIONPRIORITY callback function](nc-d3dkmthk-pfnd3dkmt-getallocationpriority.md) | TBD |
| [PFND3DKMT_UNLOCK callback function](nc-d3dkmthk-pfnd3dkmt-unlock.md) | TBD |
| [PFND3DKMT_WAITFORVERTICALBLANKEVENT2 callback function](nc-d3dkmthk-pfnd3dkmt-waitforverticalblankevent2.md) | TBD |
| [PFND3DKMT_OPENADAPTERFROMHDC callback function](nc-d3dkmthk-pfnd3dkmt-openadapterfromhdc.md) | TBD |
| [PFND3DKMT_OUTPUTDUPLPRESENT callback function](nc-d3dkmthk-pfnd3dkmt-outputduplpresent.md) | TBD |
| [PFND3DKMT_QUERYFSEBLOCK callback function](nc-d3dkmthk-pfnd3dkmt-queryfseblock.md) | TBD |
| [PFND3DKMT_OPENRESOURCEFROMNTHANDLE callback function](nc-d3dkmthk-pfnd3dkmt-openresourcefromnthandle.md) | TBD |
| [PFND3DKMT_UNPINDIRECTFLIPRESOURCES callback](nc-d3dkmthk-pfnd3dkmt-unpindirectflipresources.md) | Reserved for system use. Do not use in your driver. |
| [PFND3DKMT_GETPOSTCOMPOSITIONCAPS callback function](nc-d3dkmthk-pfnd3dkmt-getpostcompositioncaps.md) | TBD |
| [PFND3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 callback function](nc-d3dkmthk-pfnd3dkmt-opensyncobjectfromnthandle2.md) | TBD |
| [PFND3DKMT_SETDISPLAYMODE callback function](nc-d3dkmthk-pfnd3dkmt-setdisplaymode.md) | TBD |
| [PFND3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION callback function](nc-d3dkmthk-pfnd3dkmt-sharedprimaryunlocknotification.md) | TBD |
| [PFND3DKMT_DESTROYOUTPUTDUPL callback function](nc-d3dkmthk-pfnd3dkmt-destroyoutputdupl.md) | TBD |
| [PFND3DKMT_SHAREDPRIMARYLOCKNOTIFICATION callback function](nc-d3dkmthk-pfnd3dkmt-sharedprimarylocknotification.md) | TBD |
| [PFND3DKMT_QUERYALLOCATIONRESIDENCY callback function](nc-d3dkmthk-pfnd3dkmt-queryallocationresidency.md) | TBD |
| [PFND3DKMT_CREATECONTEXT callback function](nc-d3dkmthk-pfnd3dkmt-createcontext.md) | TBD |
| [PFND3DKMT_UPDATEALLOCATIONPROPERTY callback function](nc-d3dkmthk-pfnd3dkmt-updateallocationproperty.md) | TBD |
| [PFND3DKMT_RELEASESWAPCHAIN callback function](nc-d3dkmthk-pfnd3dkmt-releaseswapchain.md) | TBD |
| [PFND3DKMT_CREATEKEYEDMUTEX2 callback function](nc-d3dkmthk-pfnd3dkmt-createkeyedmutex2.md) | TBD |
| [PFND3DKMT_DESTROYDCFROMMEMORY callback function](nc-d3dkmthk-pfnd3dkmt-destroydcfrommemory.md) | TBD |
| [PFND3DKMT_CREATESWAPCHAIN callback function](nc-d3dkmthk-pfnd3dkmt-createswapchain.md) | TBD |
| [PFND3DKMT_OPENKEYEDMUTEX callback function](nc-d3dkmthk-pfnd3dkmt-openkeyedmutex.md) | TBD |
| [PFND3DKMT_SETSYNCREFRESHCOUNTWAITTARGET callback function](nc-d3dkmthk-pfnd3dkmt-setsyncrefreshcountwaittarget.md) | TBD |
| [PFND3DKMT_REGISTERBUDGETCHANGENOTIFICATION callback function](nc-d3dkmthk-pfnd3dkmt-registerbudgetchangenotification.md) | TBD |
| [PFND3DKMT_PRESENTMULTIPLANEOVERLAY callback function](nc-d3dkmthk-pfnd3dkmt-presentmultiplaneoverlay.md) | TBD |
| [PFND3DKMT_QUERYRESOURCEINFOFROMNTHANDLE callback function](nc-d3dkmthk-pfnd3dkmt-queryresourceinfofromnthandle.md) | TBD |
| [PFND3DKMT_CREATEKEYEDMUTEX callback function](nc-d3dkmthk-pfnd3dkmt-createkeyedmutex.md) | TBD |
| [PFND3DKMT_TRIMNOTIFICATIONCALLBACK callback function](nc-d3dkmthk-pfnd3dkmt-trimnotificationcallback.md) | TBD |
| [PFND3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT2 callback function](nc-d3dkmthk-pfnd3dkmt-checkmultiplaneoverlaysupport2.md) | TBD |
| [PFND3DKMT_CHANGESURFACEPOINTER callback function](nc-d3dkmthk-pfnd3dkmt-changesurfacepointer.md) | TBD |
| [PFND3DKMT_PRESENTMULTIPLANEOVERLAY3 callback function](nc-d3dkmthk-pfnd3dkmt-presentmultiplaneoverlay3.md) | TBD |
| [PFND3DKMT_DESTROYALLOCATION callback function](nc-d3dkmthk-pfnd3dkmt-destroyallocation.md) | TBD |
| [PFND3DKMT_UPDATEGPUVIRTUALADDRESS callback function](nc-d3dkmthk-pfnd3dkmt-updategpuvirtualaddress.md) | TBD |
| [PFND3DKMT_OPENADAPTERFROMLUID callback function](nc-d3dkmthk-pfnd3dkmt-openadapterfromluid.md) | TBD |
| [PFND3DKMT_GETPROCESSDEVICELOSTSUPPORT callback function](nc-d3dkmthk-pfnd3dkmt-getprocessdevicelostsupport.md) | TBD |
| [PFND3DKMT_PRESENTMULTIPLANEOVERLAY2 callback function](nc-d3dkmthk-pfnd3dkmt-presentmultiplaneoverlay2.md) | TBD |
| [PFND3DKMT_QUERYREMOTEVIDPNSOURCEFROMGDIDISPLAYNAME callback function](nc-d3dkmthk-pfnd3dkmt-queryremotevidpnsourcefromgdidisplayname.md) | TBD |
| [PFND3DKMT_ADJUSTFULLSCREENGAMMA callback function](nc-d3dkmthk-pfnd3dkmt-adjustfullscreengamma.md) | TBD |
| [PFND3DKMT_CREATEALLOCATION callback function](nc-d3dkmthk-pfnd3dkmt-createallocation.md) | TBD |
| [PFND3DKMT_INVALIDATECACHE callback function](nc-d3dkmthk-pfnd3dkmt-invalidatecache.md) | TBD |
| [PFND3DKMT_OPENNTHANDLEFROMNAME callback function](nc-d3dkmthk-pfnd3dkmt-opennthandlefromname.md) | TBD |
| [PFND3DKMT_GETSHAREDPRIMARYHANDLE callback function](nc-d3dkmthk-pfnd3dkmt-getsharedprimaryhandle.md) | TBD |
| [PFND3DKMT_CHECKMONITORPOWERSTATE callback function](nc-d3dkmthk-pfnd3dkmt-checkmonitorpowerstate.md) | TBD |
| [PFND3DKMT_GETSETSWAPCHAINMETADATA callback function](nc-d3dkmthk-pfnd3dkmt-getsetswapchainmetadata.md) | TBD |
| [PFND3DKMT_OPENSYNCHRONIZATIONOBJECT callback function](nc-d3dkmthk-pfnd3dkmt-opensynchronizationobject.md) | TBD |
| [PFND3DKMT_WAITFORSYNCHRONIZATIONOBJECTFROMGPU callback function](nc-d3dkmthk-pfnd3dkmt-waitforsynchronizationobjectfromgpu.md) | TBD |
| [PFND3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMCPU callback function](nc-d3dkmthk-pfnd3dkmt-signalsynchronizationobjectfromcpu.md) | TBD |
| [PFND3DKMT_SUBMITCOMMAND callback function](nc-d3dkmthk-pfnd3dkmt-submitcommand.md) | TBD |
| [PFND3DKMT_OUTPUTDUPLGETMETADATA callback function](nc-d3dkmthk-pfnd3dkmt-outputduplgetmetadata.md) | TBD |
| [PFND3DKMT_SETCONTEXTSCHEDULINGPRIORITY callback function](nc-d3dkmthk-pfnd3dkmt-setcontextschedulingpriority.md) | TBD |
| [PFND3DKMT_SETCONTEXTINPROCESSSCHEDULINGPRIORITY callback function](nc-d3dkmthk-pfnd3dkmt-setcontextinprocessschedulingpriority.md) | TBD |
| [PFND3DKMT_FLUSHHEAPTRANSITIONS callback function](nc-d3dkmthk-pfnd3dkmt-flushheaptransitions.md) | TBD |
| [PFND3DKMT_SETSTEREOENABLED callback function](nc-d3dkmthk-pfnd3dkmt-setstereoenabled.md) | TBD |
| [PFND3DKMT_SETFSEBLOCK callback function](nc-d3dkmthk-pfnd3dkmt-setfseblock.md) | TBD |
| [PFND3DKMT_RELEASEPROCESSVIDPNSOURCEOWNERS callback function](nc-d3dkmthk-pfnd3dkmt-releaseprocessvidpnsourceowners.md) | TBD |
| [PFND3DKMT_GETDWMVERTICALBLANKEVENT callback function](nc-d3dkmthk-pfnd3dkmt-getdwmverticalblankevent.md) | TBD |
| [PFND3DKMT_WAITFORVERTICALBLANKEVENT callback function](nc-d3dkmthk-pfnd3dkmt-waitforverticalblankevent.md) | TBD |
| [PFND3DKMT_OUTPUTDUPLGETFRAMEINFO callback function](nc-d3dkmthk-pfnd3dkmt-outputduplgetframeinfo.md) | TBD |
| [PFND3DKMT_QUERYPROCESSOFFERINFO callback function](nc-d3dkmthk-pfnd3dkmt-queryprocessofferinfo.md) | TBD |
| [PFND3DKMT_GETRUNTIMEDATA callback function](nc-d3dkmthk-pfnd3dkmt-getruntimedata.md) | TBD |
| [PFND3DKMT_UNREGISTERTRIMNOTIFICATION callback function](nc-d3dkmthk-pfnd3dkmt-unregistertrimnotification.md) | TBD |
| [PFND3DKMT_GETRESOURCEPRESENTPRIVATEDRIVERDATA callback function](nc-d3dkmthk-pfnd3dkmt-getresourcepresentprivatedriverdata.md) | TBD |
| [PFND3DKMT_RECLAIMALLOCATIONS callback function](nc-d3dkmthk-pfnd3dkmt-reclaimallocations.md) | TBD |
| [PFND3DKMT_OUTPUTDUPLGETPOINTERSHAPEDATA callback function](nc-d3dkmthk-pfnd3dkmt-outputduplgetpointershapedata.md) | TBD |
| [PFND3DKMT_GETMULTIPLANEOVERLAYCAPS callback function](nc-d3dkmthk-pfnd3dkmt-getmultiplaneoverlaycaps.md) | TBD |
| [PFND3DKMT_INVALIDATEACTIVEVIDPN callback function](nc-d3dkmthk-pfnd3dkmt-invalidateactivevidpn.md) | TBD |
| [PFND3DKMT_RELEASEKEYEDMUTEX2 callback function](nc-d3dkmthk-pfnd3dkmt-releasekeyedmutex2.md) | TBD |
| [PFND3DKMT_SETDISPLAYPRIVATEDRIVERFORMAT callback function](nc-d3dkmthk-pfnd3dkmt-setdisplayprivatedriverformat.md) | TBD |
| [PFND3DKMT_SETVIDPNSOURCEOWNER2 callback function](nc-d3dkmthk-pfnd3dkmt-setvidpnsourceowner2.md) | TBD |
| [PDXGK_POWER_NOTIFICATION callback](nc-d3dkmthk-pdxgk-power-notification.md) | A callback providing notification that the graphics device will be undergoing a device power state transition. |
| [PFND3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME callback function](nc-d3dkmthk-pfnd3dkmt-opensyncobjectnthandlefromname.md) | TBD |
| [PFND3DKMT_LOCK2 callback function](nc-d3dkmthk-pfnd3dkmt-lock2.md) | TBD |
| [PFND3DKMT_GETSCANLINE callback function](nc-d3dkmthk-pfnd3dkmt-getscanline.md) | TBD |
| [PFND3DKMT_PINDIRECTFLIPRESOURCES callback](nc-d3dkmthk-pfnd3dkmt-pindirectflipresources.md) | Reserved for system use. Do not use in your driver. |
| [PFND3DKMT_GETPROCESSSCHEDULINGPRIORITYCLASS callback function](nc-d3dkmthk-pfnd3dkmt-getprocessschedulingpriorityclass.md) | TBD |
| [PFND3DKMT_SETVIDPNSOURCEOWNER1 callback function](nc-d3dkmthk-pfnd3dkmt-setvidpnsourceowner1.md) | TBD |
| [PFND3DKMT_OPENKEYEDMUTEX2 callback function](nc-d3dkmthk-pfnd3dkmt-openkeyedmutex2.md) | TBD |
| [PFND3DKMT_CHECKEXCLUSIVEOWNERSHIP callback function](nc-d3dkmthk-pfnd3dkmt-checkexclusiveownership.md) | TBD |
| [PFND3DKMT_SETDODINDIRECTSWAPCHAIN callback function](nc-d3dkmthk-pfnd3dkmt-setdodindirectswapchain.md) | TBD |
| [PFND3DKMT_CREATEALLOCATION2 callback function](nc-d3dkmthk-pfnd3dkmt-createallocation2.md) | TBD |
| [PFND3DKMT_ENUMADAPTERS2 callback function](nc-d3dkmthk-pfnd3dkmt-enumadapters2.md) | TBD |
| [PFND3DKMT_QUERYRESOURCEINFO callback function](nc-d3dkmthk-pfnd3dkmt-queryresourceinfo.md) | TBD |
| [PFND3DKMT_QUERYCLOCKCALIBRATION callback function](nc-d3dkmthk-pfnd3dkmt-queryclockcalibration.md) | TBD |
| [PFND3DKMT_EVICT callback function](nc-d3dkmthk-pfnd3dkmt-evict.md) | TBD |
| [PDXGK_GRAPHICSPOWER_UNREGISTER callback function](nc-d3dkmthk-pdxgk-graphicspower-unregister.md) | TBD |
| [PFND3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU callback function](nc-d3dkmthk-pfnd3dkmt-signalsynchronizationobjectfromgpu.md) | TBD |
| [PFND3DKMT_ENUMADAPTERS callback function](nc-d3dkmthk-pfnd3dkmt-enumadapters.md) | TBD |
| [PFND3DKMT_WAITFORIDLE callback function](nc-d3dkmthk-pfnd3dkmt-waitforidle.md) | TBD |
| [PFND3DKMT_GETDISPLAYMODELIST callback function](nc-d3dkmthk-pfnd3dkmt-getdisplaymodelist.md) | TBD |
| [PFND3DKMT_OUTPUTDUPLRELEASEFRAME callback function](nc-d3dkmthk-pfnd3dkmt-outputduplreleaseframe.md) | TBD |
| [PFND3DKMT_WAITFORSYNCHRONIZATIONOBJECT2 callback function](nc-d3dkmthk-pfnd3dkmt-waitforsynchronizationobject2.md) | TBD |
| [PFND3DKMT_SETGAMMARAMP callback function](nc-d3dkmthk-pfnd3dkmt-setgammaramp.md) | TBD |
| [PFND3DKMT_SIGNALSYNCHRONIZATIONOBJECT callback function](nc-d3dkmthk-pfnd3dkmt-signalsynchronizationobject.md) | TBD |
| [PFND3DKMT_ABANDONSWAPCHAIN callback function](nc-d3dkmthk-pfnd3dkmt-abandonswapchain.md) | TBD |
| [PFND3DKMT_RELEASEKEYEDMUTEX callback function](nc-d3dkmthk-pfnd3dkmt-releasekeyedmutex.md) | TBD |
| [PFND3DKMT_SETQUEUEDLIMIT callback function](nc-d3dkmthk-pfnd3dkmt-setqueuedlimit.md) | TBD |
| [PFND3DKMT_GETSHAREDRESOURCEADAPTERLUID callback function](nc-d3dkmthk-pfnd3dkmt-getsharedresourceadapterluid.md) | TBD |
| [PFND3DKMT_MAPGPUVIRTUALADDRESS callback function](nc-d3dkmthk-pfnd3dkmt-mapgpuvirtualaddress.md) | TBD |
| [PFND3DKMT_ACQUIREKEYEDMUTEX callback function](nc-d3dkmthk-pfnd3dkmt-acquirekeyedmutex.md) | TBD |
| [PFND3DKMT_QUERYVIDPNEXCLUSIVEOWNERSHIP callback function](nc-d3dkmthk-pfnd3dkmt-queryvidpnexclusiveownership.md) | TBD |
| [PFND3DKMT_CONFIGURESHAREDRESOURCE callback function](nc-d3dkmthk-pfnd3dkmt-configuresharedresource.md) | TBD |
| [PFND3DKMT_BUDGETCHANGENOTIFICATIONCALLBACK callback function](nc-d3dkmthk-pfnd3dkmt-budgetchangenotificationcallback.md) | TBD |
| [PFND3DKMT_CREATECONTEXTVIRTUAL callback function](nc-d3dkmthk-pfnd3dkmt-createcontextvirtual.md) | TBD |
| [PFND3DKMT_CHECKSHAREDRESOURCEACCESS callback function](nc-d3dkmthk-pfnd3dkmt-checksharedresourceaccess.md) | TBD |
| [PFND3DKMT_CREATESYNCHRONIZATIONOBJECT2 callback function](nc-d3dkmthk-pfnd3dkmt-createsynchronizationobject2.md) | TBD |
| [PFND3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT3 callback function](nc-d3dkmthk-pfnd3dkmt-checkmultiplaneoverlaysupport3.md) | TBD |
| [PFND3DKMT_SETALLOCATIONPRIORITY callback function](nc-d3dkmthk-pfnd3dkmt-setallocationpriority.md) | TBD |
| [PFND3DKMT_QUERYADAPTERINFO callback function](nc-d3dkmthk-pfnd3dkmt-queryadapterinfo.md) | TBD |
| [PFND3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2 callback function](nc-d3dkmthk-pfnd3dkmt-signalsynchronizationobjectfromgpu2.md) | TBD |
| [PFND3DKMT_ACQUIREKEYEDMUTEX2 callback function](nc-d3dkmthk-pfnd3dkmt-acquirekeyedmutex2.md) | TBD |
| [PFND3DKMT_QUERYHYBRIDLISTVALUE callback function](nc-d3dkmthk-pfnd3dkmt-queryhybridlistvalue.md) | TBD |
| [PFND3DKMT_CHECKOCCLUSION callback function](nc-d3dkmthk-pfnd3dkmt-checkocclusion.md) | TBD |
| [PFND3DKMT_ACQUIRESWAPCHAIN callback function](nc-d3dkmthk-pfnd3dkmt-acquireswapchain.md) | TBD |
| [PFND3DKMT_SIGNALSYNCHRONIZATIONOBJECT2 callback function](nc-d3dkmthk-pfnd3dkmt-signalsynchronizationobject2.md) | TBD |
| [PFND3DKMT_WAITFORSYNCHRONIZATIONOBJECT callback function](nc-d3dkmthk-pfnd3dkmt-waitforsynchronizationobject.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [D3DKMT_PNP_KEY_TYPE enumeration](ne-d3dkmthk--d3dkmt-pnp-key-type.md) | An enum that indicates the type of PNP key. |
| [D3DKMT_DMMESCAPETYPE enumeration](ne-d3dkmthk--d3dkmt-dmmescapetype.md) | TBD |
| [QAI_DRIVERVERSION enumeration](ne-d3dkmthk--qai-driverversion.md) | TBD |
| [D3DKMT_DEVICESTATE_TYPE enumeration](ne-d3dkmthk--d3dkmt-devicestate-type.md) | The D3DKMT_DEVICESTATE_TYPE enumeration type contains values that indicate the status of a device. |
| [unnamed_enum_0bca_69 enumeration](ne-d3dkmthk---unnamed-enum-0bca-69.md) | TBD |
| [D3DKMT_OUTPUTDUPL_METADATATYPE enumeration](ne-d3dkmthk--d3dkmt-outputdupl-metadatatype.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_PROTECTED_SESSION_STATUS enumeration](ne-d3dkmthk--d3dkmt-protected-session-status.md) | Indicates the status of the protected session. |
| [D3DKMT_SCHEDULINGPRIORITYCLASS enumeration](ne-d3dkmthk--d3dkmt-schedulingpriorityclass.md) | The D3DKMT_SCHEDULINGPRIORITYCLASS enumeration type contains values that describe the scheduling priority for a process. |
| [D3DKMT_MULTIPLANE_OVERLAY_BLEND enumeration](ne-d3dkmthk-d3dkmt-multiplane-overlay-blend.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_BRIGHTNESS_INFO_TYPE enumeration](ne-d3dkmthk--d3dkmt-brightness-info-type.md) | Indicates the type of information to retrieve or set for the brightness of an integrated display panel. |
| [D3DKMT_ESCAPETYPE enumeration](ne-d3dkmthk--d3dkmt-escapetype.md) | TBD |
| [D3DKMT_VERIFIER_OPTION_MODE enumeration](ne-d3dkmthk--d3dkmt-verifier-option-mode.md) | TBD |
| [D3DKMT_OFFER_PRIORITY enumeration](ne-d3dkmthk--d3dkmt-offer-priority.md) | Indicates the importance of video memory resources that the user-mode display driver offers for reuse. |
| [OUTPUTDUPL_CONTEXT_DEBUG_STATUS enumeration](ne-d3dkmthk--outputdupl-context-debug-status.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_ALLOCATIONRESIDENCYSTATUS enumeration](ne-d3dkmthk--d3dkmt-allocationresidencystatus.md) | TBD |
| [D3DKMT_FLIPMODEL_INDEPENDENT_FLIP_STAGE enumeration](ne-d3dkmthk--d3dkmt-flipmodel-independent-flip-stage.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_QUEUEDLIMIT_TYPE enumeration](ne-d3dkmthk--d3dkmt-queuedlimit-type.md) | The D3DKMT_QUEUEDLIMIT_TYPE enumeration type contains values that indicate the type of operations to set or retrieve the queued limit for in a call to the D3DKMTSetQueuedLimit function. |
| [D3DKMT_ADAPTER_VERIFIER_OPTION_TYPE enumeration](ne-d3dkmthk--d3dkmt-adapter-verifier-option-type.md) | TBD |
| [D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE enumeration](ne-d3dkmthk--d3dkmt-outdupl-pointer-shape-type.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_VIDSCHESCAPETYPE enumeration](ne-d3dkmthk--d3dkmt-vidschescapetype.md) | TBD |
| [DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE enumeration](ne-d3dkmthk--dxgkmt-multiplane-overlay-stereo-flip-mode.md) | Reserved for system use. Do not use it in your driver. |
| [D3DKMT_ESCAPE_PFN_CONTROL_COMMAND enumeration](ne-d3dkmthk--d3dkmt-escape-pfn-control-command.md) | TBD |
| [D3DKMT_CLIENTHINT enumeration](ne-d3dkmthk--d3dkmt-clienthint.md) | TBD |
| [D3DKMDT_MODE_PRUNING_REASON enumeration](ne-d3dkmthk--d3dkmdt-mode-pruning-reason.md) | The D3DKMDT_MODE_PRUNING_REASON enumeration type contains values that identify the reason why the monitor either supports a display mode or does not support a display mode. |
| [D3DKMT_PROCESS_VERIFIER_OPTION_TYPE enumeration](ne-d3dkmthk--d3dkmt-process-verifier-option-type.md) | TBD |
| [D3DKMT_DEVICEESCAPE_TYPE enumeration](ne-d3dkmthk--d3dkmt-deviceescape-type.md) | TBD |
| [D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS enumeration](ne-d3dkmthk-d3dkmt-multiplane-overlay-ycbcr-flags.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_HYBRID_QUERY_STATE enumeration](ne-d3dkmthk--d3dkmt-hybrid-query-state.md) | TBD |
| [D3DKMT_ACTIVATE_SPECIFIC_DIAG_TYPE enumeration](ne-d3dkmthk--d3dkmt-activate-specific-diag-type.md) | TBD |
| [D3DKMT_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT enumeration](ne-d3dkmthk-d3dkmt-multiplane-overlay-video-frame-format.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_DEFRAG_ESCAPE_OPERATION enumeration](ne-d3dkmthk--d3dkmt-defrag-escape-operation.md) | TBD |
| [D3DKMT_STANDARDALLOCATIONTYPE enumeration](ne-d3dkmthk--d3dkmt-standardallocationtype.md) | Used to give information on the allocation type. |
| [D3DKMT_MIRACAST_DRIVER_TYPE enumeration](ne-d3dkmthk--d3dkmt-miracast-driver-type.md) | TBD |
| [KMTQUERYADAPTERINFOTYPE enumeration](ne-d3dkmthk--kmtqueryadapterinfotype.md) | TBD |
| [D3DKMT_MEMORY_SEGMENT_GROUP enumeration](ne-d3dkmthk--d3dkmt-memory-segment-group.md) | TBD |
| [D3DKMT_VIDMMESCAPETYPE enumeration](ne-d3dkmthk--d3dkmt-vidmmescapetype.md) | TBD |
| [D3DKMT_TDRDBGCTRLTYPE enumeration](ne-d3dkmthk--d3dkmt-tdrdbgctrltype.md) | The D3DKMT_TDRDBGCTRLTYPE enumeration type contains values that affect the behavior of the operating system's Timeout Detection and Recovery (TDR) process in a call to the OpenGL D3DKMTEscape function. |
| [D3DKMT_VAD_ESCAPE_COMMAND enumeration](ne-d3dkmthk--d3dkmt-vad-escape-command.md) | TBD |
| [D3DKMT_PRESENT_MODEL enumeration](ne-d3dkmthk--d3dkmt-present-model.md) | The D3DKMT_PRESENT_MODEL enumeration type contains values that indicate the model for a present operation. |
| [KMTUMDVERSION enumeration](ne-d3dkmthk--kmtumdversion.md) | TBD |
| [D3DKMT_MIRACAST_DEVICE_STATUS enumeration](ne-d3dkmthk-d3dkmt-miracast-device-status.md) | TBD |
| [D3DKMT_DEVICEEXECUTION_STATE enumeration](ne-d3dkmthk--d3dkmt-deviceexecution-state.md) | Contains values that indicate the execution status for a device. |
| [D3DKMT_MIRACAST_DISPLAY_DEVICE_STATE enumeration](ne-d3dkmthk-d3dkmt-miracast-display-device-state.md) | TBD |
| [D3DKMT_DEVICE_ERROR_REASON enumeration](ne-d3dkmthk--d3dkmt-device-error-reason.md) | TBD |
| [DXGKMT_MULTIPLANE_OVERLAY_STRETCH_QUALITY enumeration](ne-d3dkmthk--dxgkmt-multiplane-overlay-stretch-quality.md) | TBD |
| [D3DKMT_VIDPNSOURCEOWNER_TYPE enumeration](ne-d3dkmthk--d3dkmt-vidpnsourceowner-type.md) | TBD |
| [D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT enumeration](ne-d3dkmthk-d3dkmt-multiplane-overlay-stereo-format.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_MULTIPLANE_OVERLAY_FLAGS enumeration](ne-d3dkmthk-d3dkmt-multiplane-overlay-flags.md) | Reserved for system use. Do not use in your driver. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_INTERNAL_GRAPHICSPOWER_REGISTER IOCTL](ni-d3dkmthk-ioctl-internal-graphicspower-register.md) | TBD |

This header is used in these topics:

- [display](..content/_display)
