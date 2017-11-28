---
UID: NS.d3dkmthk._D3DKMT_CREATEDEVICE
title: D3DKMT_CREATEDEVICE
author: windows-driver-content
description: The D3DKMT_CREATEDEVICE structure describes a kernel-mode device context.
old-location: display\d3dkmt_createdevice.htm
old-project: display
ms.assetid: 9a624373-e483-484f-b9d1-f9d7aed1caa8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_CREATEDEVICE, D3DKMT_CREATEDEVICE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_CREATEDEVICE
req.alt-loc: d3dkmthk.h
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

# D3DKMT_CREATEDEVICE structure



## -description
<p>The D3DKMT_CREATEDEVICE structure describes a kernel-mode device context.</p>


## -syntax

````
typedef struct _D3DKMT_CREATEDEVICE {
  union {
    D3DKMT_HANDLE hAdapter;
    VOID          *pAdapter;
  };
  D3DKMT_CREATEDEVICEFLAGS Flags;
  D3DKMT_HANDLE            hDevice;
  VOID                     *pCommandBuffer;
  UINT                     CommandBufferSize;
  D3DDDI_ALLOCATIONLIST    *pAllocationList;
  UINT                     AllocationListSize;
  D3DDDI_PATCHLOCATIONLIST *pPatchLocationList;
  UINT                     PatchLocationListSize;
} D3DKMT_CREATEDEVICE;
````


## -struct-fields
<dl>

### -field <b>hAdapter</b>

<dd>
<p>[in] A handle to the graphics adapter that the device context is created on. This handle identifies the adapter for user-mode creation. </p>
</dd>

### -field <b>pAdapter</b>

<dd>
<p>[in] A pointer to a block of memory for the graphics adapter that the device context is created on. This pointer identifies the adapter for kernel-mode creation. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff547828">D3DKMT_CREATEDEVICEFLAGS</a> structure that indicates, in bit-field flags, the type of device context to be created.</p>
</dd>

### -field <b>hDevice</b>

<dd>
<p>[out] A handle to the device context that the Microsoft DirectX graphics kernel subsystem (<i>Dxgkrnl.sys</i>) supplied and that is returned from the call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546836">D3DKMTCreateDevice</a> function.</p>
</dd>

### -field <b>pCommandBuffer</b>

<dd>
<p>[out] A pointer to command buffer memory that the OpenGL ICD places commands into. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff546836">D3DKMTCreateDevice</a> function returns this memory pointer.</p>
</dd>

### -field <b>CommandBufferSize</b>

<dd>
<p>[out] The size, in bytes, of the memory block that <b>pCommandBuffer</b> points to. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff546836">D3DKMTCreateDevice</a> function returns this size value.</p>
</dd>

### -field <b>pAllocationList</b>

<dd>
<p>[out] An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544375">D3DDDI_ALLOCATIONLIST</a> structures that the OpenGL ICD inserts referenced allocations in.</p>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff546836">D3DKMTCreateDevice</a> function returns this value. </p>
</dd>

### -field <b>AllocationListSize</b>

<dd>
<p>[out] The number of elements in the array of allocations that is pointed to by <b>pAllocationList</b>. This quantity of allocations is available when submitting the command buffer that is pointed to by <b>pCommandBuffer</b> to the display miniport driver. </p>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff546836">D3DKMTCreateDevice</a> function returns this value. </p>
</dd>

### -field <b>pPatchLocationList</b>

<dd>
<p>[out] An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544630">D3DDDI_PATCHLOCATIONLIST</a> structures that the OpenGL ICD inserts patching information in.</p>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff546836">D3DKMTCreateDevice</a> function returns this value. </p>
</dd>

### -field <b>PatchLocationListSize</b>

<dd>
<p>[out] The number of elements in the patch-location list that is pointed to by <b>pPatchLocationList</b>. This quantity of patch locations is available when submitting the command buffer that is pointed to by <b>pCommandBuffer</b> to the display miniport driver. </p>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff546836">D3DKMTCreateDevice</a> function returns this value. </p>
</dd>
</dl>

## -remarks


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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547828">D3DKMT_CREATEDEVICEFLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546836">D3DKMTCreateDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_CREATEDEVICE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
