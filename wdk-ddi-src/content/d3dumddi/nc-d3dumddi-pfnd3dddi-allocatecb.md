---
UID: NC.d3dumddi.PFND3DDDI_ALLOCATECB
title: PFND3DDDI_ALLOCATECB
author: windows-driver-content
description: The pfnAllocateCb function allocates system or video memory.
old-location: display\pfnallocatecb.htm
old-project: display
ms.assetid: a61e6c6a-3992-429c-ad8c-5f1a61dc7b8b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnAllocateCb
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

# PFND3DDDI_ALLOCATECB callback



## -description
<p>The <b>pfnAllocateCb</b> function allocates system or video memory.</p>


## -prototype

````
PFND3DDDI_ALLOCATECB pfnAllocateCb;

__checkReturn HRESULT APIENTRY CALLBACK pfnAllocateCb(
  _In_    HANDLE            hDevice,
  _Inout_ D3DDDICB_ALLOCATE *pData
)
{ ... }
````


## -parameters
<dl>

### -param hDevice [in]

<dd>
<p>A handle to the display device (graphics context).</p>
</dd>

### -param pData [in, out]

<dd>
<p>A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddicb-allocate.md">D3DDDICB_ALLOCATE</a> structure that describes the allocation.</p>
</dd>
</dl>

## -returns
<p><b>pfnAllocateCb</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The memory was successfully allocated.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p><b>pfnAllocateCb</b> could not allocate memory that was required for it to complete.</p><dl>
<dt><b>D3DERR_OUTOFVIDEOMEMORY </b></dt>
</dl><p><b>pfnAllocateCb</b> could not complete because of insufficient video memory. The video memory manager attempts to virtualize video memory; however, if the virtualization fails (such as, when virtual address space runs out), the memory manager might return this error code.</p><dl>
<dt><b>D3DDDIERR_DEVICEREMOVED</b></dt>
</dl><p><b>pfnAllocateCb</b> could not initiate a call to the display miniport driver's <a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a> function because a Plug and Play (PnP) stop or a Timeout Detection and Recovery (TDR) event occurred. The user-mode display driver function that called <b>pfnAllocateCb</b> (typically, the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createresource.md">CreateResource</a>, <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createresource.md">CreateResource(D3D10)</a>, or <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createresource.md">CreateResource(D3D11)</a> function) must return this error code back to the Direct3D runtime. </p>

<p><b>Direct3D Version 9 Note:  </b>For more information about returning error codes, see <a href="https://msdn.microsoft.com/4a2384e8-407f-4248-8b31-7c4e836b15dc">Returning Error Codes Received from Runtime Functions</a>.</p>

<p><b>Direct3D Versions 10 and 11 Note:  </b>If the driver function does not return a value (that is, has VOID for a return parameter type), the driver function calls the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> function to send an error code back to the runtime. For more information about handling error codes, see <a href="https://msdn.microsoft.com/ac4e056e-3304-4934-887a-5cc2b87989bd">Handling Errors</a>.</p>

<p> </p>

<p>This function might also return other HRESULT values.</p>

## -remarks
<p>A user-mode display driver calls <b>pfnAllocateCb</b> to allocate system or video memory (also known as an <i>allocation</i>). The Microsoft DirectX graphics kernel subsystem (<i>Dxgkrnl.sys</i>) then calls the display miniport driver's <a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a> function to interpret and store the private data that was passed in the <b>pfnAllocateCb</b> request. The display miniport driver returns information from the <i>DxgkDdiCreateAllocation</i> call that the video memory manager (which is part of <i>Dxgkrnl.sys</i>) uses to actually allocate the memory. </p>

<p>The user-mode display driver typically creates an allocation in response to a call to its <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createresource.md">CreateResource</a>, <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createresource.md">CreateResource(D3D10)</a>, or <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createresource.md">CreateResource(D3D11)</a> function. However, the user-mode display driver can create an allocation at anytime--for example, when the user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createdevice.md">CreateDevice</a>, or <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a> function creates scratch-pad areas in video memory. </p>

<p>The user-mode display driver can create the following types of allocations: </p>

<p>System memory allocations in which the Microsoft Direct3D runtime preallocates the system memory. In this situation, the user-mode display driver cannot set alignment or any other parameter. If the user-mode display driver requires preallocated system memory that is accessible by the hardware, it calls <b>pfnAllocateCb</b>. The Direct3D runtime returns the system memory pointer in the <b>pSystemMem</b> member of the <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-allocationinfo.md">D3DDDI_ALLOCATIONINFO</a> structure for elements in the <b>pAllocationInfo</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddicb-allocate.md">D3DDDICB_ALLOCATE</a> structure that is pointed to by <i>pData</i>. If the user-mode display driver does not require preallocated system memory that is accessible by the hardware, it should not call <b>pfnAllocateCb</b> for this type of memory. </p>

<p>System and video memory allocations in which the user-mode display driver can participate in the creation. </p>

<p>When the driver attempts to create multiple allocations, the driver can associate all of the allocations with a parent resource (for example, when creating a flipping chain in which each backbuffer is an individual allocation). The driver can perform such an association by setting the <b>hResource</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddicb-allocate.md">D3DDDICB_ALLOCATE</a> structure that is pointed to by <i>pData</i> to the value that was passed to the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createresource.md">CreateResource</a>, <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createresource.md">CreateResource(D3D10)</a>, or <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createresource.md">CreateResource(D3D11)</a> function. In response, the Direct3D runtime returns a kernel-mode resource handle (which is of the D3DKMT_HANDLE data type) in the <b>hKMResource</b> member of D3DDDICB_ALLOCATE. The user-mode display driver can subsequently insert this kernel-mode resource handle in the command stream for use by the display miniport driver. </p>

<p>The display miniport driver can call the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-gethandledata.md">DxgkCbGetHandleData</a> function on this kernel-mode resource handle (typically within its <a href="display.dxgkddirender">DxgkDdiRender</a> function) to obtain private data that is associated with the resource, or the display miniport driver can call the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-enumhandlechildren.md">DxgkCbEnumHandleChildren</a> function to obtain all of the allocations that are associated with the resource. The display miniport driver can also call the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-gethandleparent.md">DxgkCbGetHandleParent</a> function to obtain the parent kernel-mode resource handle from a child allocation handle. </p>

<p>Note that if the <b>hResource</b> member of D3DDDICB_ALLOCATE is set to <b>NULL</b> when the user-mode display driver calls <b>pfnAllocateCb</b>, the allocation is associated with the device instead of with a resource. The driver can determine only that the difference is semantic. Associating allocations with a resource is optional but recommended for debugging and diagnostic purposes.</p>

<p><b>Direct3D Version 9 Note:  </b>For more information about creating and destroying resources, see <a href="https://msdn.microsoft.com/d443bdc3-1c5a-4372-9e6a-b8a4d21499b9">Handling Resource Creation and Destruction</a>.</p>

<p><b>Direct3D Version 11 Note:  </b>For more information about how the driver calls <b>pfnAllocateCb</b>, see <a href="https://msdn.microsoft.com/014a5e44-f8c4-45c0-96e8-d82f37b8b28d">Changes from Direct3D 10</a>.</p>

<p>The following code example shows how to allocate memory for a resource.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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
<a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createdevice.md">CreateDevice</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createresource.md">CreateResource</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createresource.md">CreateResource(D3D10)</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createresource.md">CreateResource(D3D11)</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddicb-allocate.md">D3DDDICB_ALLOCATE</a>
</dt>
<dt>
<a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-allocationinfo.md">D3DDDI_ALLOCATIONINFO</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddi-devicecallbacks.md">D3DDDI_DEVICECALLBACKS</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-enumhandlechildren.md">DxgkCbEnumHandleChildren</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-gethandledata.md">DxgkCbGetHandleData</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-gethandleparent.md">DxgkCbGetHandleParent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_ALLOCATECB callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
