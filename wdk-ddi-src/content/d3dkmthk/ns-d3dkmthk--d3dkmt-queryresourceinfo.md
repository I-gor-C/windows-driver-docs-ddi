---
UID: NS.d3dkmthk._D3DKMT_QUERYRESOURCEINFO
title: D3DKMT_QUERYRESOURCEINFO
author: windows-driver-content
description: The D3DKMT_QUERYRESOURCEINFO structure describes parameters for retrieving information about a resource.
old-location: display\d3dkmt_queryresourceinfo.htm
old-project: display
ms.assetid: 14078b2b-8951-48df-912a-e053bc997dde
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_QUERYRESOURCEINFO, D3DKMT_QUERYRESOURCEINFO
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
req.alt-api: D3DKMT_QUERYRESOURCEINFO
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

# D3DKMT_QUERYRESOURCEINFO structure



## -description
<p>The D3DKMT_QUERYRESOURCEINFO structure describes parameters for retrieving information about a resource.</p>


## -syntax

````
typedef struct _D3DKMT_QUERYRESOURCEINFO {
  D3DKMT_HANDLE hDevice;
  D3DKMT_HANDLE hGlobalShare;
  VOID          *pPrivateRuntimeData;
  UINT          PrivateRuntimeDataSize;
  UINT          TotalPrivateDriverDataSize;
  UINT          ResourcePrivateDriverDataSize;
  UINT          NumAllocations;
} D3DKMT_QUERYRESOURCEINFO;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A handle to the device that the resource and allocations are associated with.</p>
</dd>

### -field <b>hGlobalShare</b>

<dd>
<p>[in] A handle to the shared resource to open.</p>
</dd>

### -field <b>pPrivateRuntimeData</b>

<dd>
<p>[in] If non-<b>NULL</b>, a pointer to a buffer that receives the runtime-private data that is supplied at create time. The OpenGL ICD should first call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547124">D3DKMTQueryResourceInfo</a> function with <b>pPrivateRuntimeData</b> set to <b>NULL</b> to obtain the buffer size and then call again with the correct size buffer. </p>
</dd>

### -field <b>PrivateRuntimeDataSize</b>

<dd>
<p>[in/out] The size, in bytes, of the buffer that <b>pPrivateRuntimeData</b> points to. If <b>pPrivateRuntimeData</b> is <b>NULL</b>, <b>PrivateRuntimeDataSize</b> is set to the size, in bytes, that is required for the buffer to store the runtime-private data.</p>
</dd>

### -field <b>TotalPrivateDriverDataSize</b>

<dd>
<p>[out] The size, in bytes, of the buffer that is required to hold the private driver data for all of the allocations that are associated with the resource.</p>
</dd>

### -field <b>ResourcePrivateDriverDataSize</b>

<dd>
<p>[out] The size, in bytes, of the buffer that is required to hold the private driver data for the resource.</p>
</dd>

### -field <b>NumAllocations</b>

<dd>
<p>[out] The number of allocations that are associated with the resource.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547065">D3DKMTOpenResource</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547124">D3DKMTQueryResourceInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_QUERYRESOURCEINFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
