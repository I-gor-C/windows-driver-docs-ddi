---
UID: NS.d3dkmthk._D3DKMT_LOCK
title: D3DKMT_LOCK
author: windows-driver-content
description: The D3DKMT_LOCK structure describes parameters for locking an allocation.
old-location: display\d3dkmt_lock.htm
old-project: display
ms.assetid: 0f985d0b-2b98-413d-a736-c507743ac786
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_LOCK, D3DKMT_LOCK
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
req.alt-api: D3DKMT_LOCK
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

# D3DKMT_LOCK structure



## -description
<p>The D3DKMT_LOCK structure describes parameters for locking an allocation. </p>


## -syntax

````
typedef struct _D3DKMT_LOCK {
  D3DKMT_HANDLE          hDevice;
  D3DKMT_HANDLE          hAllocation;
  UINT                   PrivateDriverData;
  UINT                   NumPages;
  const UINT             *pPages;
  VOID                   *pData;
  D3DDDICB_LOCKFLAGS     Flags;
  D3DGPU_VIRTUAL_ADDRESS GpuVirtualAddress;
} D3DKMT_LOCK;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the device that the allocation is associated with.</p>
</dd>

### -field <b>hAllocation</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the allocation to lock.</p>
</dd>

### -field <b>PrivateDriverData</b>

<dd>
<p>[in] A UINT value that specifies 32 bits of private data (for example, MIP level) that is sent from the OpenGL ICD to the display miniport driver's <a href="display.dxgkddiacquireswizzlingrange">DxgkDdiAcquireSwizzlingRange</a> function.</p>
</dd>

### -field <b>NumPages</b>

<dd>
<p>[in] The number of pages in the page list that <b>pPages</b> specifies.</p>
</dd>

### -field <b>pPages</b>

<dd>
<p>[in] An array of pages to lock. Each page in the array is described by an integer offset. Zero means the first page in the surface, one means the second, and so on. </p>
</dd>

### -field <b>pData</b>

<dd>
<p>[out] A pointer to the memory that is returned from the display miniport driver and memory manager. When locking a memory page list, the pointer that is returned is a pointer to the first memory page.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544214">D3DDDICB_LOCKFLAGS</a> structure that identifies, in bit-field flags, how to lock the allocation.</p>
<p>Note that specifying some flags together is invalid and that some flags depend on other flags. For more information about these combinations, see the Remarks section of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544214">D3DDDICB_LOCKFLAGS</a>.</p>
</dd>

### -field <b>GpuVirtualAddress</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>This member is available beginning with Windows 7.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544214">D3DDDICB_LOCKFLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547028">D3DKMTLock</a>
</dt>
<dt>
<a href="display.dxgkddiacquireswizzlingrange">DxgkDdiAcquireSwizzlingRange</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_LOCK structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
