---
UID: NS.d3dkmddi._DXGKARG_RELEASESWIZZLINGRANGE
title: DXGKARG_RELEASESWIZZLINGRANGE
author: windows-driver-content
description: The DXGKARG_RELEASESWIZZLINGRANGE structure describes parameters for releasing a swizzling range.
old-location: display\dxgkarg_releaseswizzlingrange.htm
old-project: display
ms.assetid: f7d1af11-c360-4f7f-a47a-cf7a182b2b78
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_RELEASESWIZZLINGRANGE, DXGKARG_RELEASESWIZZLINGRANGE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_RELEASESWIZZLINGRANGE
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
req.iface: 
---

# DXGKARG_RELEASESWIZZLINGRANGE structure



## -description
<p>The DXGKARG_RELEASESWIZZLINGRANGE structure describes parameters for releasing a swizzling range.</p>


## -syntax

````
typedef struct _DXGKARG_RELEASESWIZZLINGRANGE {
  HANDLE hAllocation;
  UINT   PrivateDriverData;
  UINT   RangeId;
} DXGKARG_RELEASESWIZZLINGRANGE;
````


## -struct-fields
<dl>

### -field hAllocation

<dd>
<p>[in] A handle to the allocation that the display miniport driver assigns and that is returned through the driver's <a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a> function.</p>
</dd>

### -field PrivateDriverData

<dd>
<p>[in] The 32 bits of private data that the user-mode display driver sent when the display miniport driver's <a href="display.dxgkddiacquireswizzlingrange">DxgkDdiAcquireSwizzlingRange</a> function was called to acquire the swizzling range.</p>
</dd>

### -field RangeId

<dd>
<p>[in] The zero-based identifier of the swizzling range that the <a href="display.dxgkddireleaseswizzlingrange">DxgkDdiReleaseSwizzlingRange</a> function releases.</p>
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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgkddiacquireswizzlingrange">DxgkDdiAcquireSwizzlingRange</a>
</dt>
<dt>
<a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a>
</dt>
<dt>
<a href="display.dxgkddireleaseswizzlingrange">DxgkDdiReleaseSwizzlingRange</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_RELEASESWIZZLINGRANGE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
