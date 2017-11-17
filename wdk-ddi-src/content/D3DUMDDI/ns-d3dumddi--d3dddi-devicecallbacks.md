---
UID: NS.d3dumddi._D3DDDI_DEVICECALLBACKS
title: D3DDDI_DEVICECALLBACKS
author: windows-driver-content
description: The D3DDDI_DEVICECALLBACKS structure contains Microsoft Direct3D runtime callback functions that the user-mode display driver can use.
old-location: display\d3dddi_devicecallbacks.htm
ms.assetid: 29810132-5f53-4ba6-8302-6de315ecd04a
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
ms.keywords: D3DDDI_DEVICECALLBACKS, D3DDDI_DEVICECALLBACKS
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
<p>A pointer to the <a href="https://msdn.microsoft.com/a61e6c6a-3992-429c-ad8c-5f1a61dc7b8b">pfnAllocateCb</a> function, which the user-mode display driver uses to request that the Direct3D runtime create a memory allocation for use by the driver.</p>
</dd>

### -field <b>pfnDeallocateCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/2ffa0367-0451-45d2-be05-e450c45be116">pfnDeallocateCb</a> function, which the user-mode display driver uses to request that the Direct3D runtime free memory that was previously allocated.</p>
</dd>

### -field <b>pfnSetPriorityCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/1812cb0f-9232-4813-9c7b-74c9fa4d03cf">pfnSetPriorityCb</a> function, which the user-mode display driver uses to set the priority of a resource or list of allocations.</p>
</dd>

### -field <b>pfnQueryResidencyCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/707ba050-e70c-49f8-aac0-0bcc8fe9bf8b">pfnQueryResidencyCb</a> function, which the user-mode display driver uses to query the residency status of a resource or list of allocations.</p>
</dd>

### -field <b>pfnSetDisplayModeCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/a1f58757-809d-4351-8b1a-fd4420981c24">pfnSetDisplayModeCb</a> function, which the user-mode display driver uses to set an allocation for displaying.</p>
</dd>

### -field <b>pfnPresentCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/460b9be5-5817-4225-9089-f86ad64f4554">pfnPresentCb</a> function, which the user-mode display driver uses to submit a present command to the display miniport driver.</p>
</dd>

### -field <b>pfnRenderCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/f242162e-6237-469c-b178-5a51dcf69e32">pfnRenderCb</a> function, which the user-mode display driver uses to submit a command buffer to the display miniport driver.</p>
</dd>

### -field <b>pfnLockCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/69022797-432a-410b-8cbf-e1ef7111e7ea">pfnLockCb</a> function, which the user-mode display driver uses to request a lock from the display miniport driver. This lock cannot be handled completely by the user-mode display driver.</p>
</dd>

### -field <b>pfnUnlockCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/6684f350-da27-478d-ab7b-36e395f7df8d">pfnUnlockCb</a> function, which the user-mode display driver uses to call the display miniport driver for an unlock. This unlock cannot be handled completely by the user-mode display driver. </p>
</dd>

### -field <b>pfnEscapeCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/66c0347f-2cf3-42fc-8641-47c731e958c9">pfnEscapeCb</a> function, which the user-mode display driver uses to share information with the display miniport driver. </p>
</dd>

### -field <b>pfnCreateOverlayCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/fbd5b3af-0963-4e41-8be3-41e3e1ecf8bc">pfnCreateOverlayCb</a> function, which the user-mode display driver uses to create and display a kernel-mode overlay object. </p>
</dd>

### -field <b>pfnUpdateOverlayCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/17f89cea-350c-43f6-a60d-32fc2d299dd7">pfnUpdateOverlayCb</a> function, which the user-mode display driver uses to modify a kernel-mode overlay object. </p>
</dd>

### -field <b>pfnFlipOverlayCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/91e4876a-82c0-4e74-84c8-4b7a6abe0756">pfnFlipOverlayCb</a> function, which the user-mode display driver uses to change the allocation that the overlay displays. </p>
</dd>

### -field <b>pfnDestroyOverlayCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/9fc83bad-c183-4cba-9514-bfe1c676cba5">pfnDestroyOverlayCb</a> function, which the user-mode display driver uses to destroy a kernel-mode overlay object and stop the overlay from being displayed. </p>
</dd>

### -field <b>pfnCreateContextCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a> function, which the user-mode display driver uses to create a context to submit requests to. </p>
</dd>

### -field <b>pfnDestroyContextCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/6b65d75b-544b-4153-b821-d59d6f85673d">pfnDestroyContextCb</a> function, which the user-mode display driver uses to destroy a context that <a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a> created. </p>
</dd>

### -field <b>pfnCreateSynchronizationObjectCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/1b87d3cc-685a-4768-b4fd-dbe0a0cbec37">pfnCreateSynchronizationObjectCb</a> function, which the user-mode display driver uses to create a synchronization object. </p>
</dd>

### -field <b>pfnDestroySynchronizationObjectCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/7ba549a2-f165-4b5e-8cf4-ab707222532c">pfnDestroySynchronizationObjectCb</a> function, which the user-mode display driver uses to destroy a synchronization object that <a href="https://msdn.microsoft.com/1b87d3cc-685a-4768-b4fd-dbe0a0cbec37">pfnCreateSynchronizationObjectCb</a> created. </p>
</dd>

### -field <b>pfnWaitForSynchronizationObjectCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/d33ca665-897d-4e99-b9a6-b794127fecfd">pfnWaitForSynchronizationObjectCb</a> function, which the user-mode display driver uses to wait for synchronization events to occur and then uses to return. </p>
</dd>

### -field <b>pfnSignalSynchronizationObjectCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/12ffa230-2c26-4cd3-ae83-f753a0b6ba38">pfnSignalSynchronizationObjectCb</a> function, which the user-mode display driver uses to signal that synchronization events are no longer owned by a context. </p>
</dd>

### -field <b>pfnSetAsyncCallbacksCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/7f046e5a-e8a2-4e39-ae31-d37afc03f21f">pfnSetAsyncCallbacksCb</a> function that the user-mode display driver uses to notify the Direct3D runtime whether the runtime will start or stop receiving calls to the runtime's callback functions from a worker thread.</p>
<p>Only DirectX 9 and Direct 9L versions of the runtime support the <a href="https://msdn.microsoft.com/7f046e5a-e8a2-4e39-ae31-d37afc03f21f">pfnSetAsyncCallbacksCb</a> function. DirectX 10 and later versions of the runtime set the <b>pfnSetAsyncCallbacksCb</b> member to <b>NULL</b> when the runtime calls the user-mode display driver's <a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a> function to create a rendering device. </p>
</dd>

### -field <b>pfnSetDisplayPrivateDriverFormatCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/499e6de7-67cc-4834-bcec-4f3907b180f7">pfnSetDisplayPrivateDriverFormatCb</a> function that the user-mode display driver uses to change the format of the shared primary surface. </p>
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
<p>A pointer to the <a href="https://msdn.microsoft.com/9B0F058C-B71F-4A4F-A053-F9381A5FD3A8">pfnCreateSynchronizationObject2Cb</a> function, which a WDDM 1.2 and later user-mode display driver uses to create a GPU synchronization object.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnWaitForSynchronizationObject2Cb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/4542C49F-C26C-45BE-B961-C5F65BDA78CF">pfnWaitForSynchronizationObject2Cb</a> function, which a WDDM 1.2 and later user-mode display driver uses to wait for GPU synchronization events to occur and then uses to return.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnSignalSynchronizationObject2Cb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/01B5E793-D075-42B5-9ADF-D033249AEE9F">pfnSignalSynchronizationObject2Cb</a> function, which a WDDM 1.2 and later user-mode display driver uses to signal that GPU synchronization events are no longer owned by a context.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pfnPresentMultiPlaneOverlayCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh780323">pfnPresentMultiPlaneOverlayCb (D3D)</a> function, which a WDDM 1.3 and later user-mode display driver uses to copy content from a source multiplane overlay allocation to a destination allocation.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnLogUMDMarkerCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/BD544686-20D3-4577-9950-9C3B6853C4BD">pfnLogUMDMarkerCb</a> function, which a WDDM 1.3 and later user-mode display driver calls to log a custom Event Tracing for Windows (ETW) marker event.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnMakeResidentCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/8D65C3F7-3D07-4341-A989-A1438F821802">pfnMakeResidentCb</a> function.</p>
</dd>

### -field <b>pfnEvictCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/5E66A522-BC1C-4E7C-8732-87D40F99BBDA">pfnEvictCb</a> function.</p>
</dd>

### -field <b>pfnWaitForSynchronizationObjectFromCpuCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/304A5BCE-19E6-4F92-B840-FD3BE1CFB856">pfnWaitForSynchronizationObjectFromCpuCb</a> function.</p>
</dd>

### -field <b>pfnSignalSynchronizationObjectFromCpuCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/E6FD5215-09CE-4DC8-B5AB-F65E68E2A884">pfnSignalSynchronizationObjectFromCpuCb</a> function.</p>
</dd>

### -field <b>pfnWaitForSynchronizationObjectFromGpuCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/49023D25-D57E-418F-AD10-133377B90493">pfnWaitForSynchronizationObjectFromGpuCb</a> function.</p>
</dd>

### -field <b>pfnSignalSynchronizationObjectFromGpuCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/46F23D7A-5C7A-4BCC-A575-5D47F590B07C">pfnSignalSynchronizationObjectFromGpuCb</a> function.</p>
</dd>

### -field <b>pfnCreatePagingQueueCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/99E4CFCF-7A0A-43A9-9E23-B7A9F9375690">pfnCreatePagingQueueCb</a> function.</p>
</dd>

### -field <b>pfnDestroyPagingQueueCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/2C039656-5384-4864-8F29-A336B0ED06C0">pfnDestroyPagingQueueCb</a> function.</p>
</dd>

### -field <b>pfnLock2Cb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/C046F34A-4304-4B96-8D7A-7A951016437F">pfnLock2Cb</a> function.</p>
</dd>

### -field <b>pfnUnlock2Cb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/642C6A05-DA8C-453A-B1AA-030C59F32DA5">pfnUnlock2Cb</a> function.</p>
</dd>

### -field <b>pfnInvalidateCacheCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/56DF8936-4DD1-4352-9063-72F441FDF343">pfnInvalidateCacheCb</a> function.</p>
</dd>

### -field <b>pfnReserveGpuVirtualAddressCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/CEDE03E1-4B0D-4839-B7D6-0826CC103C5E">pfnReserveGpuVirtualAddressCb</a> function.</p>
</dd>

### -field <b>pfnMapGpuVirtualAddressCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/DA67A98C-BE9C-412D-9382-CAC5B05FEE3B">pfnMapGpuVirtualAddressCb</a> function.</p>
</dd>

### -field <b>pfnFreeGpuVirtualAddressCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/92F2A43C-699B-4580-8A56-472D837A76E2">pfnFreeGpuVirtualAddressCb</a> function.</p>
</dd>

### -field <b>pfnUpdateGpuVirtualAddressCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/99D075A0-4483-47D1-BA24-80C45BFF407A">pfnUpdateGpuVirtualAddressCb</a> function.</p>
</dd>

### -field <b>pfnCreateContextVirtualCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/7787FEDF-E18C-4120-A073-A13933856F57">pfnCreateContextVirtualCb</a> function.</p>
</dd>

### -field <b>pfnSubmitCommandCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/60300845-9050-4D0A-83D1-76A45EA823C1">pfnSubmitCommandCb</a> function.</p>
</dd>

### -field <b>pfnDeallocate2Cb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/68C7EC44-D744-4C69-86D9-35B3B089875A">pfnDeallocate2Cb</a> function.</p>
</dd>

### -field <b>pfnSignalSynchronizationObjectFromGpu2Cb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/03F9E47D-A3CA-44A1-A136-8236309D3D36">pfnSignalSynchronizationObjectFromGpu2Cb</a> function.</p>
</dd>

### -field <b>pfnReclaimAllocations2Cb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/dn903528">pfnReclaimAllocations2Cb</a> function.</p>
</dd>

### -field <b>pfnGetResourcePresentPrivateDriverDataCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/D4F0F272-60DC-4060-9762-3DB49236CE62">pfnGetResourcePresentPrivateDriverDataCb</a> function.</p>
</dd>

### -field <b>pfnUpdateAllocationPropertyCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/49E4189A-2183-4033-BF17-ADFAC1CF1EF2">pfnUpdateAllocationPropertyCb</a> function.</p>
</dd>

### -field <b>pfnOfferAllocations2Cb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/4A8123D3-3A7D-4716-BD02-DD6533DB22F6">pfnOfferAllocations2Cb</a> function.</p>
</dd>

### -field <b>pfnReclaimAllocations3Cb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/BA0A8BF0-39C2-4641-9952-05512B1B1662">pfnReclaimAllocations3Cb</a> function.</p>
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
<a href="https://msdn.microsoft.com/ce35bdac-af90-471f-af93-0e665be6c7f6">CreateDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a61e6c6a-3992-429c-ad8c-5f1a61dc7b8b">pfnAllocateCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fbd5b3af-0963-4e41-8be3-41e3e1ecf8bc">pfnCreateOverlayCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1b87d3cc-685a-4768-b4fd-dbe0a0cbec37">pfnCreateSynchronizationObjectCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/9B0F058C-B71F-4A4F-A053-F9381A5FD3A8">pfnCreateSynchronizationObject2Cb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2ffa0367-0451-45d2-be05-e450c45be116">pfnDeallocateCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6b65d75b-544b-4153-b821-d59d6f85673d">pfnDestroyContextCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/9fc83bad-c183-4cba-9514-bfe1c676cba5">pfnDestroyOverlayCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7ba549a2-f165-4b5e-8cf4-ab707222532c">pfnDestroySynchronizationObjectCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/66c0347f-2cf3-42fc-8641-47c731e958c9">pfnEscapeCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/91e4876a-82c0-4e74-84c8-4b7a6abe0756">pfnFlipOverlayCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/69022797-432a-410b-8cbf-e1ef7111e7ea">pfnLockCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/BD544686-20D3-4577-9950-9C3B6853C4BD">pfnLogUMDMarkerCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/460b9be5-5817-4225-9089-f86ad64f4554">pfnPresentCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/707ba050-e70c-49f8-aac0-0bcc8fe9bf8b">pfnQueryResidencyCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f242162e-6237-469c-b178-5a51dcf69e32">pfnRenderCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7f046e5a-e8a2-4e39-ae31-d37afc03f21f">pfnSetAsyncCallbacksCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a1f58757-809d-4351-8b1a-fd4420981c24">pfnSetDisplayModeCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/499e6de7-67cc-4834-bcec-4f3907b180f7">pfnSetDisplayPrivateDriverFormatCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1812cb0f-9232-4813-9c7b-74c9fa4d03cf">pfnSetPriorityCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/12ffa230-2c26-4cd3-ae83-f753a0b6ba38">pfnSignalSynchronizationObjectCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/01B5E793-D075-42B5-9ADF-D033249AEE9F">pfnSignalSynchronizationObject2Cb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6684f350-da27-478d-ab7b-36e395f7df8d">pfnUnlockCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/17f89cea-350c-43f6-a60d-32fc2d299dd7">pfnUpdateOverlayCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/d33ca665-897d-4e99-b9a6-b794127fecfd">pfnWaitForSynchronizationObjectCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4542C49F-C26C-45BE-B961-C5F65BDA78CF">pfnWaitForSynchronizationObject2Cb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh780323">pfnPresentMultiPlaneOverlayCb (D3D)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4A8123D3-3A7D-4716-BD02-DD6533DB22F6">pfnOfferAllocations2Cb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/BA0A8BF0-39C2-4641-9952-05512B1B1662">pfnReclaimAllocations3Cb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_DEVICECALLBACKS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
