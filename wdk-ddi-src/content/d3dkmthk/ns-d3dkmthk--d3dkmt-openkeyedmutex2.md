---
UID: NS.d3dkmthk._D3DKMT_OPENKEYEDMUTEX2
title: D3DKMT_OPENKEYEDMUTEX2
author: windows-driver-content
description: Describes a keyed mutex that the D3DKMTOpenKeyedMutex2 function opens.
old-location: display\d3dkmt_openkeyedmutex2.htm
old-project: display
ms.assetid: 7d746cac-42fd-4fb3-9384-ea690c2235f8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_OPENKEYEDMUTEX2, D3DKMT_OPENKEYEDMUTEX2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_OPENKEYEDMUTEX2
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
req.iface: 
---

# D3DKMT_OPENKEYEDMUTEX2 structure



## -description
<p>Describes a keyed mutex that the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439405">D3DKMTOpenKeyedMutex2</a> function opens.</p>


## -syntax

````
typedef struct _D3DKMT_OPENKEYEDMUTEX2 {
  D3DKMT_HANDLE hSharedHandle;
  D3DKMT_HANDLE hKeyedMutex;
  VOID          *pPrivateRuntimeData;
  UINT          PrivateRuntimeDataSize;
} D3DKMT_OPENKEYEDMUTEX2;
````


## -struct-fields
<dl>

### -field <b>hSharedHandle</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents a global handle to a keyed mutex.</p>
</dd>

### -field <b>hKeyedMutex</b>

<dd>
<p>[out] A D3DKMT_HANDLE data type that represents a handle to the keyed mutex in this process.</p>
</dd>

### -field <b>pPrivateRuntimeData</b>

<dd>
<p>[in] A buffer that contains initial private data. This buffer is copied only if the keyed mutex does not already have private data.</p>
</dd>

### -field <b>PrivateRuntimeDataSize</b>

<dd>
<p>[in] The size, in bytes, of the <b>pPrivateRuntimeData</b> member.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439405">D3DKMTOpenKeyedMutex2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_OPENKEYEDMUTEX2 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
