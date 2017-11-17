---
UID: NS.d3dkmddi._DXGKARG_DESCRIBEALLOCATION
title: DXGKARG_DESCRIBEALLOCATION
author: windows-driver-content
description: The DXGKARG_DESCRIBEALLOCATION structure describes an existing allocation.
old-location: display\dxgkarg_describeallocation.htm
ms.assetid: fd01ff3b-83b7-43d5-bbc6-6959485edd15
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with  Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_DESCRIBEALLOCATION
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: DXGKARG_DESCRIBEALLOCATION, DXGKARG_DESCRIBEALLOCATION
req.iface: 
---

# DXGKARG_DESCRIBEALLOCATION structure



## -description
<p>The DXGKARG_DESCRIBEALLOCATION structure describes an existing allocation.</p>


## -syntax

````
typedef struct _DXGKARG_DESCRIBEALLOCATION {
  HANDLE                       hAllocation;
  UINT                         Width;
  UINT                         Height;
  D3DDDIFORMAT                 Format;
  D3DDDI_MULTISAMPLINGMETHOD   MultisampleMethod;
  D3DDDI_RATIONAL              RefreshRate;
  UINT                         PrivateDriverFormatAttribute;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
  DXGK_DESCRIBEALLOCATIONFLAGS Flags;
  D3DDDI_ROTATION              Rotation;
#endif 
} DXGKARG_DESCRIBEALLOCATION;
````


## -struct-fields
<dl>

### -field <b>hAllocation</b>

<dd>
<p>[in] A handle to an allocation that information is requested for. The driver previously returned this handle in the <b>hAllocation</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560960">DXGK_ALLOCATIONINFO</a> structure from a call to the driver's <a href="https://msdn.microsoft.com/a28287d6-4dfa-4db4-92df-bbcd9379a5b2">DxgkDdiCreateAllocation</a> function.</p>
</dd>

### -field <b>Width</b>

<dd>
<p>[out] The width of the allocation, in pixels. The driver returns the width value.</p>
</dd>

### -field <b>Height</b>

<dd>
<p>[out] The height of the allocation, in pixels. The driver returns the height value.</p>
</dd>

### -field <b>Format</b>

<dd>
<p>[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544312">D3DDDIFORMAT</a>-typed value that indicates the pixel format of the allocation. The driver returns the format value.</p>
</dd>

### -field <b>MultisampleMethod</b>

<dd>
<p>[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544594">D3DDDI_MULTISAMPLINGMETHOD</a> structure that describes the multiple-sampling method that is used for the allocation. The driver returns the description.</p>
</dd>

### -field <b>RefreshRate</b>

<dd>
<p>[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544641">D3DDDI_RATIONAL</a> structure that indicates the refresh rate that the primary surface was created with, if applicable.</p>
</dd>

### -field <b>PrivateDriverFormatAttribute</b>

<dd>
<p>[out] A UINT value that specifies a private format attribute for the allocation. The driver specifies surface format attributes (for example, the pixel layout of a tiled surface) that it otherwise cannot expose to the operating system. </p>
<p>The operating system uses the information in <b>PrivateDriverFormatAttribute</b> to compare two surfaces. For example, an A8R8B8G8 800x600 surface and an X8R8B8G8 800x600 surface should have the same information in <b>PrivateDriverFormatAttribute</b> if they have the same format attributes, which includes pixel layout. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[out] This member is reserved.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>Rotation</b>

<dd>
<p>[out] This member is reserved.</p>
<p>Supported starting with Windows 8.</p>
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
<p>Available starting with  Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544594">D3DDDI_MULTISAMPLINGMETHOD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544641">D3DDDI_RATIONAL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544646">D3DDDI_ROTATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544312">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560960">DXGK_ALLOCATIONINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh464013">DXGK_DESCRIBEALLOCATIONFLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a28287d6-4dfa-4db4-92df-bbcd9379a5b2">DxgkDdiCreateAllocation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8ee65716-496c-4b0f-baa7-34a625847d5f">DxgkDdiDescribeAllocation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_DESCRIBEALLOCATION structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
