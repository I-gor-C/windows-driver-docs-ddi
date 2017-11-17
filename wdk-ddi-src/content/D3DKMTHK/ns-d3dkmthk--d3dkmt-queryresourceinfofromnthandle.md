---
UID: NS.d3dkmthk._D3DKMT_QUERYRESOURCEINFOFROMNTHANDLE
title: D3DKMT_QUERYRESOURCEINFOFROMNTHANDLE
author: windows-driver-content
description: Describes information that is required to map a global NT handle to resource information.
old-location: display\d3dkmt_queryresourceinfofromnthandle.htm
ms.assetid: 098fe3b9-1169-4ff6-8822-0eb277cb73f9
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_QUERYRESOURCEINFOFROMNTHANDLE
req.alt-loc: D3dkmthk.h
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
ms.keywords: D3DKMT_QUERYRESOURCEINFOFROMNTHANDLE, D3DKMT_QUERYRESOURCEINFOFROMNTHANDLE
req.iface: 
---

# D3DKMT_QUERYRESOURCEINFOFROMNTHANDLE structure



## -description
<p>Describes information that is required to map a global NT handle to resource information.</p>


## -syntax

````
typedef struct _D3DKMT_QUERYRESOURCEINFOFROMNTHANDLE {
  D3DKMT_HANDLE hDevice;
  HANDLE        hNtHandle;
  VOID          *pPrivateRuntimeData;
  UINT          PrivateRuntimeDataSize;
  UINT          TotalPrivateDriverDataSize;
  UINT          ResourcePrivateDriverDataSize;
  UINT          NumAllocations;
} D3DKMT_QUERYRESOURCEINFOFROMNTHANDLE;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the device.</p>
</dd>

### -field <b>hNtHandle</b>

<dd>
<p>[in] A global NT handle to the resource that is to be queried.</p>
</dd>

### -field <b>pPrivateRuntimeData</b>

<dd>
<p>[in] A pointer to a caller-supplied buffer where the runtime private data associated with the resource will be copied to.</p>
</dd>

### -field <b>PrivateRuntimeDataSize</b>

<dd>
<p>[in] The size, in bytes, of the buffer pointed to by the <b>pPrivateRuntimeData</b> member.</p>
<p>[out] If <b>pPrivateRuntimeData</b> is <b>NULL</b>, this member is the size, in bytes, of the buffer required to receive the runtime private data. Otherwise, this member is the size, in bytes, of runtime private data copied into the buffer.</p>
</dd>

### -field <b>TotalPrivateDriverDataSize</b>

<dd>
<p>[out] The size, in bytes, of the buffer that is required to hold all the driver private data for all allocations associated with the resource.</p>
</dd>

### -field <b>ResourcePrivateDriverDataSize</b>

<dd>
<p>[out] The size, in bytes, of the driver's resource private data.</p>
</dd>

### -field <b>NumAllocations</b>

<dd>
<p>[out] The number of allocations associated with the resource.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439446">D3DKMTQueryResourceInfoFromNtHandle</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_QUERYRESOURCEINFOFROMNTHANDLE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
