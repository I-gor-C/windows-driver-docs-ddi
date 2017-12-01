---
UID: NS.d3dkmthk._D3DKMT_RELEASEKEYEDMUTEX
title: D3DKMT_RELEASEKEYEDMUTEX
author: windows-driver-content
description: The D3DKMT_RELEASEKEYEDMUTEX structure describes a keyed mutex that the D3DKMTReleaseKeyedMutex function releases.
old-location: display\d3dkmt_releasekeyedmutex.htm
old-project: display
ms.assetid: 0ba40b4e-2e1d-45fa-9222-e162a39eea33
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_RELEASEKEYEDMUTEX, D3DKMT_RELEASEKEYEDMUTEX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: D3DKMT_RELEASEKEYEDMUTEX is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_RELEASEKEYEDMUTEX
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

# D3DKMT_RELEASEKEYEDMUTEX structure



## -description
<p>The D3DKMT_RELEASEKEYEDMUTEX structure describes a keyed mutex that the <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtreleasekeyedmutex.md">D3DKMTReleaseKeyedMutex</a> function releases. </p>


## -syntax

````
typedef struct _D3DKMT_RELEASEKEYEDMUTEX {
  D3DKMT_HANDLE hKeyedMutex;
  UINT64        Key;
  UINT64        FenceValue;
} D3DKMT_RELEASEKEYEDMUTEX;
````


## -struct-fields
<dl>

### -field <b>hKeyedMutex</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the keyed mutex object to release. </p>
</dd>

### -field <b>Key</b>

<dd>
<p>[in] A 64-bit value that specifies the key value to release the mutex to. </p>
</dd>

### -field <b>FenceValue</b>

<dd>
<p>[in] A 64-bit value that specifies the current fence value of the GPU synchronization object. </p>
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
<p>D3DKMT_RELEASEKEYEDMUTEX is supported beginning with the Windows 7 operating system. </p>
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
<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtreleasekeyedmutex.md">D3DKMTReleaseKeyedMutex</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_RELEASEKEYEDMUTEX structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
