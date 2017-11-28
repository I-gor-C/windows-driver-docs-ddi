---
UID: NS.d3dumddi._D3DDDIARG_LOCK
title: D3DDDIARG_LOCK
author: windows-driver-content
description: The D3DDDIARG_LOCK structure describes a resource or a surface within the resource to lock.
old-location: display\d3dddiarg_lock.htm
old-project: display
ms.assetid: 00f8b16c-3ec1-48ac-930b-17aca16cc04f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_LOCK, D3DDDIARG_LOCK
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
req.alt-api: D3DDDIARG_LOCK
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

# D3DDDIARG_LOCK structure



## -description
<p>The D3DDDIARG_LOCK structure describes a resource or a surface within the resource to lock. </p>


## -syntax

````
typedef struct _D3DDDIARG_LOCK {
  HANDLE           hResource;
  UINT             SubResourceIndex;
  union {
    D3DDDIRANGE Range;
    RECT        Area;
    D3DDDIBOX   Box;
  };
  VOID             *pSurfData;
  UINT             Pitch;
  UINT             SlicePitch;
  D3DDDI_LOCKFLAGS Flags;
} D3DDDIARG_LOCK;
````


## -struct-fields
<dl>

### -field <b>hResource</b>

<dd>
<p>[in] A handle to the resource to be locked. </p>
</dd>

### -field <b>SubResourceIndex</b>

<dd>
<p>[in] The zero-based index into the resource, which is specified by the handle that is specified by <b>hResource</b>. This index indicates the subresource or surface to be locked.</p>
</dd>

### -field <b>Range</b>

<dd>
<p>[in] A D3DDDIRANGE structure that describes the subrange of the linear resource to lock.</p>
</dd>

### -field <b>Area</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure that describes the subrectangle of the surface to lock.</p>
</dd>

### -field <b>Box</b>

<dd>
<p>[in] A D3DDDIBOX structure that describes the subvolume of the volume to lock.</p>
</dd>

### -field <b>pSurfData</b>

<dd>
<p>[out] A pointer to the memory region for the resource that was locked. The user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lock.md">Lock</a> function returns this pointer to the Microsoft Direct3D runtime.</p>
</dd>

### -field <b>Pitch</b>

<dd>
<p>[out] The pitch, in bytes, of the surface that was locked. The user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lock.md">Lock</a> function returns this pitch value to the Direct3D runtime.</p>
</dd>

### -field <b>SlicePitch</b>

<dd>
<p>[out] The slice pitch, in bytes, of the surface that was locked. The user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lock.md">Lock</a> function returns this slice pitch value to the Direct3D runtime.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544591">D3DDDI_LOCKFLAGS</a> structure that indicates, in bit-field flags, how to lock the resource. Note that some flags are mutually exclusive with other flags. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -remarks
<p>The members of the structure that is specified by the <b>Flags</b> member must adhere to the following rules:</p>

<p>The <b>ReadOnly</b> and <b>WriteOnly</b> bit-field flags must not be set simultaneously.</p>

<p>The <b>NoOverwrite</b> bit-field flag must not be simultaneously set with the <b>Discard</b> bit-field flag.</p>

<p>Only one of the <b>RangeValid</b>, <b>AreaValid</b>, and <b>BoxValid</b> bit-field flags must be set at any time.</p>

<p>The <b>ReadOnly</b> bit-field flag must not be simultaneously set with the <b>Discard</b> bit-field flag.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544591">D3DDDI_LOCKFLAGS</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lock.md">Lock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_LOCK structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
