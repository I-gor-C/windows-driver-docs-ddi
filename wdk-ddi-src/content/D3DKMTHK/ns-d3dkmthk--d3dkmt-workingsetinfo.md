---
UID: NS.d3dkmthk._D3DKMT_WORKINGSETINFO
title: D3DKMT_WORKINGSETINFO
author: windows-driver-content
description: The D3DKMT_WORKINGSETINFO structure describes information about the graphics adapter's working set that the OpenGL installable client driver (ICD) obtains by calling the D3DKMTQueryAdapterInfo function.
old-location: display\d3dkmt_workingsetinfo.htm
ms.assetid: 1a5b75e4-abdd-4916-b2b5-4dbb53a525ae
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_WORKINGSETINFO
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
ms.keywords: D3DKMT_WORKINGSETINFO, D3DKMT_WORKINGSETINFO
req.iface: 
---

# D3DKMT_WORKINGSETINFO structure



## -description
<p>The D3DKMT_WORKINGSETINFO structure describes information about the graphics adapter's working set that the OpenGL installable client driver (ICD) obtains by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547100">D3DKMTQueryAdapterInfo</a> function.</p>


## -syntax

````
typedef struct _D3DKMT_WORKINGSETINFO {
  D3DKMT_WORKINGSETFLAGS Flags;
  ULONG                  MinimumWorkingSetPercentile;
  ULONG                  MaximumWorkingSetPercentile;
} D3DKMT_WORKINGSETINFO;
````


## -struct-fields
<dl>

### -field <b>Flags</b>

<dd>
<p>[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff548448">D3DKMT_WORKINGSETFLAGS</a> structure that indicates, in bit-field flags, working-set properties.</p>
</dd>

### -field <b>MinimumWorkingSetPercentile</b>

<dd>
<p>[out] The minimum working-set percentile. </p>
</dd>

### -field <b>MaximumWorkingSetPercentile</b>

<dd>
<p>[out] The maximum working-set percentile. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548203">D3DKMT_QUERYADAPTERINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548448">D3DKMT_WORKINGSETFLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547100">D3DKMTQueryAdapterInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_WORKINGSETINFO structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
