---
UID: NS.d3dkmthk._D3DKMT_ACQUIREKEYEDMUTEX2
title: D3DKMT_ACQUIREKEYEDMUTEX2
author: windows-driver-content
description: Describes a keyed mutex object that the D3DKMTAcquireKeyedMutex2 function acquires that includes private data.
old-location: display\d3dkmt_acquirekeyedmutex2.htm
old-project: display
ms.assetid: 6e7ccf24-6403-44bf-9369-d2825646e950
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_ACQUIREKEYEDMUTEX2, D3DKMT_ACQUIREKEYEDMUTEX2
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
req.alt-api: D3DKMT_ACQUIREKEYEDMUTEX2
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

# D3DKMT_ACQUIREKEYEDMUTEX2 structure



## -description
<p>Describes a keyed mutex object that the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439340">D3DKMTAcquireKeyedMutex2</a> function acquires that includes private data.</p>


## -syntax

````
typedef struct _D3DKMT_ACQUIREKEYEDMUTEX2 {
  D3DKMT_HANDLE  hKeyedMutex;
  UINT64         Key;
  PLARGE_INTEGER pTimeout;
  UINT64         FenceValue;
  VOID           *pPrivateRuntimeData;
  UINT           PrivateRuntimeDataSize;
} D3DKMT_ACQUIREKEYEDMUTEX2;
````


## -struct-fields
<dl>

### -field <b>hKeyedMutex</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents a handle to the keyed mutex.</p>
</dd>

### -field <b>Key</b>

<dd>
<p>[in] The key value to acquire.</p>
</dd>

### -field <b>pTimeout</b>

<dd>
<p>[in] An NT-style timeout value.</p>
</dd>

### -field <b>FenceValue</b>

<dd>
<p>[out] The current fence value of the GPU sync object.</p>
</dd>

### -field <b>pPrivateRuntimeData</b>

<dd>
<p>[out] A pointer to a buffer to copy private data to.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439340">D3DKMTAcquireKeyedMutex2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_ACQUIREKEYEDMUTEX2 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
