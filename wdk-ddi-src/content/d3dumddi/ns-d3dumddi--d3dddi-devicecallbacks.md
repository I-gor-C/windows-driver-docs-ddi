---
UID: NS.d3dumddi._D3DDDI_DEVICECALLBACKS
title: D3DDDI_DEVICECALLBACKS
author: windows-driver-content
description: The D3DDDI_DEVICECALLBACKS structure contains Microsoft Direct3D runtime callback functions that the user-mode display driver can use.
old-location: display\d3dddi_devicecallbacks.htm
old-project: display
ms.assetid: 29810132-5f53-4ba6-8302-6de315ecd04a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_DEVICECALLBACKS, D3DDDI_DEVICECALLBACKS
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
req.alt-api: D3DDDI_DEVICECALLBACKS
req.alt-loc: D3dumddi.h
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

# D3DDDI_DEVICECALLBACKS structure



## -description
<p>The D3DDDI_DEVICECALLBACKS structure contains Microsoft Direct3D runtime callback functions that the user-mode display driver can use.</p>


## -syntax

````
typedef struct _D3DDDI_DEVICECALLBACKS {
  PFND3DDDI_ALLOCATECB                            pfnAllocateCb;
  PFND3DDDI_DEALLOCATECB                          pfnDeallocateCb;
  PFND3DDDI_SETPRIORITYCB                         pfnSetPriorityCb;
  PFND3DDDI_QUERYRESIDENCYCB                      pfnQueryResidencyCb;
  PFND3DDDI_SETDISPLAYMODECB                      pfnSetDisplayModeCb;
  PFND3DDDI_PRESENTCB                             pfnPresentCb;
  PFND3DDDI_RENDERCB                              pfnRenderCb;
  PFND3DDDI_LOCKCB                                pfnLockCb;
  PFND3DDDI_UNLOCKCB                              pfnUnlockCb;
  PFND3DDDI_ESCAPECB                              pfnEscapeCb;
  PFND3DDDI_CREATEOVERLAYCB                       pfnCreateOverlayCb;
  PFND3DDDI_UPDATEOVERLAYCB                       pfnUpdateOverlayCb;
  PFND3DDDI_FLIPOVERLAYCB                         pfnFlipOverlayCb;
  PFND3DDDI_DESTROYOVERLAYCB                      pfnDestroyOverlayCb;
  PFND3DDDI_CREATECONTEXTCB                       pfnCreateContextCb;
  PFND3DDDI_DESTROYCONTEXTCB                      pfnDestroyContextCb;
  PFND3DDDI_CREATESYNCHRONIZATIONOBJECTCB         pfnCreateSynchronizationObjectCb;
  PFND3DDDI_DESTROYSYNCHRONIZATIONOBJECTCB        pfnDestroySynchronizationObjectCb;
  PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECTCB        pfnWaitForSynchronizationObjectCb;
  PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECTCB         pfnSignalSynchronizationObjectCb;
  PFND3DDDI_SETASYNCCALLBACKSCB                   pfnSetAsyncCallbacksCb;
  PFND3DDDI_SETDISPLAYPRIVATEDRIVERFORMATCB       pfnSetDisplayPrivateDriverFormatCb;
#if (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WIN8)
  PFND3DDDI_OFFERALLOCATIONSCB                    pfnOfferAllocationsCb;
  PFND3DDDI_RECLAIMALLOCATIONSCB                  pfnReclaimAllocationsCb;
  PFND3DDDI_CREATESYNCHRONIZATIONOBJECT2CB        pfnCreateSynchronizationObject2Cb;
  PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECT2CB       pfnWaitForSynchronizationObject2Cb;
  PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECT2CB        pfnSignalSynchronizationObject2Cb;
  PFND3DDDI_PRESENTMULTIPLANEOVERLAYCB            pfnPresentMultiPlaneOverlayCb;
#endif 
#if (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM1_3)
  PFND3DDDI_LOGUMDMARKERCB                        pfnLogUMDMarkerCb;
#endif 
#if (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM2_0)
  PFND3DDDI_MAKERESIDENTCB                        pfnMakeResidentCb;
  PFND3DDDI_EVICTCB                               pfnEvictCb;
  PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPUCB pfnWaitForSynchronizationObjectFromCpuCb;
  PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECTFROMCPUCB  pfnSignalSynchronizationObjectFromCpuCb;
  PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMGPUCB pfnWaitForSynchronizationObjectFromGpuCb;
  PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECTFROMGPUCB  pfnSignalSynchronizationObjectFromGpuCb;
  PFND3DDDI_CREATEPAGINGQUEUECB                   pfnCreatePagingQueueCb;
  PFND3DDDI_DESTROYPAGINGQUEUECB                  pfnDestroyPagingQueueCb;
  PFND3DDDI_LOCK2CB                               pfnLock2Cb;
  PFND3DDDI_UNLOCK2CB                             pfnUnlock2Cb;
  PFND3DDDI_INVALIDATECACHECB                     pfnInvalidateCacheCb;
  PFND3DDDI_RESERVEGPUVIRTUALADDRESSCB            pfnReserveGpuVirtualAddressCb;
  PFND3DDDI_MAPGPUVIRTUALADDRESSCB                pfnMapGpuVirtualAddressCb;
  PFND3DDDI_FREEGPUVIRTUALADDRESSCB               pfnFreeGpuVirtualAddressCb;
  PFND3DDDI_UPDATEGPUVIRTUALADDRESSCB             pfnUpdateGpuVirtualAddressCb;
  PFND3DDDI_CREATECONTEXTVIRTUALCB                pfnCreateContextVirtualCb;
  PFND3DDDI_SUBMITCOMMANDCB                       pfnSubmitCommandCb;
  PFND3DDDI_DEALLOCATE2CB                         pfnDeallocate2Cb;
  PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2CB pfnSignalSynchronizationObjectFromGpu2Cb;
  PFND3DDDI_RECLAIMALLOCATIONS2CB                 pfnReclaimAllocations2Cb;
  PFND3DDDI_GETRESOURCEPRESENTPRIVATEDRIVERDATACB pfnGetResourcePresentPrivateDriverDataCb;
#endif 
#if (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM2_1_1)
  PFND3DDDI_UPDATEALLOCATIONPROPERTYCB            pfnUpdateAllocationPropertyCb;
#endif 
  PFND3DDDI_OFFERALLOCATIONS2CB                   pfnOfferAllocations2Cb;
  PFND3DDDI_RECLAIMALLOCATIONS3CB                 pfnReclaimAllocations3Cb;
} D3DDDI_DEVICECALLBACKS;
````


## -struct-fields
<dl>

### -field <b>pfnAllocateCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-allocatecb.md">pfnAllocateCb</a> function, which the user-mode display driver uses to request that the Direct3D runtime create a memory allocation for use by the driver.</p>
</dd>

### -field <b>pfnDeallocateCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-deallocatecb.md">pfnDeallocateCb</a> function, which the user-mode display driver uses to request that the Direct3D runtime free memory that was previously allocated.</p>
</dd>

### -field <b>pfnSetPriorityCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setprioritycb.md">pfnSetPriorityCb</a> function, which the user-mode display driver uses to set the priority of a resource or list of allocations.</p>
</dd>

### -field <b>pfnQueryResidencyCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-queryresidencycb.md">pfnQueryResidencyCb</a> function, which the user-mode display driver uses to query the residency status of a resource or list of allocations.</p>
</dd>

### -field <b>pfnSetDisplayModeCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setdisplaymodecb.md">pfnSetDisplayModeCb</a> function, which the user-mode display driver uses to set an allocation for displaying.</p>
</dd>

### -field <b>pfnPresentCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-presentcb.md">pfnPresentCb</a> function, which the user-mode display driver uses to submit a present command to the display miniport driver.</p>
</dd>

### -field <b>pfnRenderCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-rendercb.md">pfnRenderCb</a> function, which the user-mode display driver uses to submit a command buffer to the display miniport driver.</p>
</dd>

### -field <b>pfnLockCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lockcb.md">pfnLockCb</a> function, which the user-mode display driver uses to request a lock from the display miniport driver. This lock cannot be handled completely by the user-mode display driver.</p>
</dd>

### -field <b>pfnUnlockCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-unlockcb.md">pfnUnlockCb</a> function, which the user-mode display driver uses to call the display miniport driver for an unlock. This unlock cannot be handled completely by the user-mode display driver. </p>
</dd>

### -field <b>pfnEscapeCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-escapecb.md">pfnEscapeCb</a> function, which the user-mode display driver uses to share information with the display miniport driver. </p>
</dd>

### -field <b>pfnCreateOverlayCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createoverlaycb.md">pfnCreateOverlayCb</a> function, which the user-mode display driver uses to create and display a kernel-mode overlay object. </p>
</dd>

### -field <b>pfnUpdateOverlayCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-updateoverlaycb.md">pfnUpdateOverlayCb</a> function, which the user-mode display driver uses to modify a kernel-mode overlay object. </p>
</dd>

### -field <b>pfnFlipOverlayCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-flipoverlaycb.md">pfnFlipOverlayCb</a> function, which the user-mode display driver uses to change the allocation that the overlay displays. </p>
</dd>

### -field <b>pfnDestroyOverlayCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroyoverlaycb.md">pfnDestroyOverlayCb</a> function, which the user-mode display driver uses to destroy a kernel-mode overlay object and stop the overlay from being displayed. </p>
</dd>

### -field <b>pfnCreateContextCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a> function, which the user-mode display driver uses to create a context to submit requests to. </p>
</dd>

### -field <b>pfnDestroyContextCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroycontextcb.md">pfnDestroyContextCb</a> function, which the user-mode display driver uses to destroy a context that <a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a> created. </p>
</dd>

### -field <b>pfnCreateSynchronizationObjectCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createsynchronizationobjectcb.md">pfnCreateSynchronizationObjectCb</a> function, which the user-mode display driver uses to create a synchronization object. </p>
</dd>

### -field <b>pfnDestroySynchronizationObjectCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroysynchronizationobjectcb.md">pfnDestroySynchronizationObjectCb</a> function, which the user-mode display driver uses to destroy a synchronization object that <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createsynchronizationobjectcb.md">pfnCreateSynchronizationObjectCb</a> created. </p>
</dd>

### -field <b>pfnWaitForSynchronizationObjectCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-waitforsynchronizationobjectcb.md">pfnWaitForSynchronizationObjectCb</a> function, which the user-mode display driver uses to wait for synchronization events to occur and then uses to return. </p>
</dd>

### -field <b>pfnSignalSynchronizationObjectCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-signalsynchronizationobjectcb.md">pfnSignalSynchronizationObjectCb</a> function, which the user-mode display driver uses to signal that synchronization events are no longer owned by a context. </p>
</dd>

### -field <b>pfnSetAsyncCallbacksCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setasynccallbackscb.md">pfnSetAsyncCallbacksCb</a> function that the user-mode display driver uses to notify the Direct3D runtime whether the runtime will start or stop receiving calls to the runtime's callback functions from a worker thread.</p>
<p>Only DirectX 9 and Direct 9L versions of the runtime support the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setasynccallbackscb.md">pfnSetAsyncCallbacksCb</a> function. DirectX 10 and later versions of the runtime set the <b>pfnSetAsyncCallbacksCb</b> member to <b>NULL</b> when the runtime calls the user-mode display driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a> function to create a rendering device. </p>
</dd>

### -field <b>pfnSetDisplayPrivateDriverFormatCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setdisplayprivatedriverformatcb.md">pfnSetDisplayPrivateDriverFormatCb</a> function that the user-mode display driver uses to change the format of the shared primary surface. </p>
</dd>

### -field <b>pfnOfferAllocationsCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451693">pfnOfferAllocationsCb</a> function, which a WDDM 1.2 and later user-mode display driver   calls to offer  video memory allocations for reuse.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnReclaimAllocationsCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451695">pfnReclaimAllocationsCb</a> function, which a WDDM 1.2 and later user-mode display driver   calls to reclaim access to video memory allocations that were previously offered  for reuse.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnCreateSynchronizationObject2Cb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createsynchronizationobject2cb.md">pfnCreateSynchronizationObject2Cb</a> function, which a WDDM 1.2 and later user-mode display driver uses to create a GPU synchronization object.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnWaitForSynchronizationObject2Cb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-waitforsynchronizationobject2cb.md">pfnWaitForSynchronizationObject2Cb</a> function, which a WDDM 1.2 and later user-mode display driver uses to wait for GPU synchronization events to occur and then uses to return.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnSignalSynchronizationObject2Cb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-signalsynchronizationobject2cb.md">pfnSignalSynchronizationObject2Cb</a> function, which a WDDM 1.2 and later user-mode display driver uses to signal that GPU synchronization events are no longer owned by a context.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnPresentMultiPlaneOverlayCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh780323">pfnPresentMultiPlaneOverlayCb (D3D)</a> function, which a WDDM 1.3 and later user-mode display driver uses to copy content from a source multiplane overlay allocation to a destination allocation.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnLogUMDMarkerCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-logumdmarkercb.md">pfnLogUMDMarkerCb</a> function, which a WDDM 1.3 and later user-mode display driver calls to log a custom Event Tracing for Windows (ETW) marker event.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnMakeResidentCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-makeresidentcb.md">pfnMakeResidentCb</a> function.</p>
</dd>

### -field <b>pfnEvictCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-evictcb.md">pfnEvictCb</a> function.</p>
</dd>

### -field <b>pfnWaitForSynchronizationObjectFromCpuCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-waitforsynchronizationobjectfromcpucb.md">pfnWaitForSynchronizationObjectFromCpuCb</a> function.</p>
</dd>

### -field <b>pfnSignalSynchronizationObjectFromCpuCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-signalsynchronizationobjectfromcpucb.md">pfnSignalSynchronizationObjectFromCpuCb</a> function.</p>
</dd>

### -field <b>pfnWaitForSynchronizationObjectFromGpuCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-waitforsynchronizationobjectfromgpucb.md">pfnWaitForSynchronizationObjectFromGpuCb</a> function.</p>
</dd>

### -field <b>pfnSignalSynchronizationObjectFromGpuCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-signalsynchronizationobjectfromgpucb.md">pfnSignalSynchronizationObjectFromGpuCb</a> function.</p>
</dd>

### -field <b>pfnCreatePagingQueueCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createpagingqueuecb.md">pfnCreatePagingQueueCb</a> function.</p>
</dd>

### -field <b>pfnDestroyPagingQueueCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroypagingqueuecb.md">pfnDestroyPagingQueueCb</a> function.</p>
</dd>

### -field <b>pfnLock2Cb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lock2cb.md">pfnLock2Cb</a> function.</p>
</dd>

### -field <b>pfnUnlock2Cb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-unlock2cb.md">pfnUnlock2Cb</a> function.</p>
</dd>

### -field <b>pfnInvalidateCacheCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/56DF8936-4DD1-4352-9063-72F441FDF343">pfnInvalidateCacheCb</a> function.</p>
</dd>

### -field <b>pfnReserveGpuVirtualAddressCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-reservegpuvirtualaddresscb.md">pfnReserveGpuVirtualAddressCb</a> function.</p>
</dd>

### -field <b>pfnMapGpuVirtualAddressCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-mapgpuvirtualaddresscb.md">pfnMapGpuVirtualAddressCb</a> function.</p>
</dd>

### -field <b>pfnFreeGpuVirtualAddressCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-freegpuvirtualaddresscb.md">pfnFreeGpuVirtualAddressCb</a> function.</p>
</dd>

### -field <b>pfnUpdateGpuVirtualAddressCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-updategpuvirtualaddresscb.md">pfnUpdateGpuVirtualAddressCb</a> function.</p>
</dd>

### -field <b>pfnCreateContextVirtualCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createcontextvirtualcb.md">pfnCreateContextVirtualCb</a> function.</p>
</dd>

### -field <b>pfnSubmitCommandCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-submitcommandcb.md">pfnSubmitCommandCb</a> function.</p>
</dd>

### -field <b>pfnDeallocate2Cb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-deallocate2cb.md">pfnDeallocate2Cb</a> function.</p>
</dd>

### -field <b>pfnSignalSynchronizationObjectFromGpu2Cb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-signalsynchronizationobjectfromgpu2cb.md">pfnSignalSynchronizationObjectFromGpu2Cb</a> function.</p>
</dd>

### -field <b>pfnReclaimAllocations2Cb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/dn903528">pfnReclaimAllocations2Cb</a> function.</p>
</dd>

### -field <b>pfnGetResourcePresentPrivateDriverDataCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getresourcepresentprivatedriverdatacb.md">pfnGetResourcePresentPrivateDriverDataCb</a> function.</p>
</dd>

### -field <b>pfnUpdateAllocationPropertyCb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-updateallocationpropertycb.md">pfnUpdateAllocationPropertyCb</a> function.</p>
</dd>

### -field <b>pfnOfferAllocations2Cb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-offerallocations2cb.md">pfnOfferAllocations2Cb</a> function.</p>
</dd>

### -field <b>pfnReclaimAllocations3Cb</b>

<dd>
<p>A pointer to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-reclaimallocations3cb.md">pfnReclaimAllocations3Cb</a> function.</p>
</dd>
</dl>

## -remarks
<p>The following code, from D3dumddi.h, shows the function declarations for the callback functions that the members of <b>D3DDDI_DEVICECALLBACKS</b> point to.</p>

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
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-allocatecb.md">pfnAllocateCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createoverlaycb.md">pfnCreateOverlayCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createsynchronizationobjectcb.md">pfnCreateSynchronizationObjectCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createsynchronizationobject2cb.md">pfnCreateSynchronizationObject2Cb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-deallocatecb.md">pfnDeallocateCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroycontextcb.md">pfnDestroyContextCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroyoverlaycb.md">pfnDestroyOverlayCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroysynchronizationobjectcb.md">pfnDestroySynchronizationObjectCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-escapecb.md">pfnEscapeCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-flipoverlaycb.md">pfnFlipOverlayCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lockcb.md">pfnLockCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-logumdmarkercb.md">pfnLogUMDMarkerCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-presentcb.md">pfnPresentCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-queryresidencycb.md">pfnQueryResidencyCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-rendercb.md">pfnRenderCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setasynccallbackscb.md">pfnSetAsyncCallbacksCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setdisplaymodecb.md">pfnSetDisplayModeCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setdisplayprivatedriverformatcb.md">pfnSetDisplayPrivateDriverFormatCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setprioritycb.md">pfnSetPriorityCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-signalsynchronizationobjectcb.md">pfnSignalSynchronizationObjectCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-signalsynchronizationobject2cb.md">pfnSignalSynchronizationObject2Cb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-unlockcb.md">pfnUnlockCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-updateoverlaycb.md">pfnUpdateOverlayCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-waitforsynchronizationobjectcb.md">pfnWaitForSynchronizationObjectCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-waitforsynchronizationobject2cb.md">pfnWaitForSynchronizationObject2Cb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh780323">pfnPresentMultiPlaneOverlayCb (D3D)</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-offerallocations2cb.md">pfnOfferAllocations2Cb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-reclaimallocations3cb.md">pfnReclaimAllocations3Cb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_DEVICECALLBACKS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
