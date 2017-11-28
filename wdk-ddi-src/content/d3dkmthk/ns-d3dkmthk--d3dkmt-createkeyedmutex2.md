---
UID: NS.d3dkmthk._D3DKMT_CREATEKEYEDMUTEX2
title: D3DKMT_CREATEKEYEDMUTEX2
author: windows-driver-content
description: Describes a keyed mutex that the D3DKMTCreateKeyedMutex2 function creates that includes private data.
old-location: display\d3dkmt_createkeyedmutex2.htm
old-project: display
ms.assetid: 6c4c07ff-5e37-4094-9dc3-57082dec8edf
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_CREATEKEYEDMUTEX2, D3DKMT_CREATEKEYEDMUTEX2
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
req.alt-api: D3DKMT_CREATEKEYEDMUTEX2
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

# D3DKMT_CREATEKEYEDMUTEX2 structure



## -description
<p>Describes a keyed mutex that the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439345">D3DKMTCreateKeyedMutex2</a> function creates that includes private data.</p>


## -syntax

````
typedef struct _D3DKMT_CREATEKEYEDMUTEX2 {
  UINT64                         InitialValue;
  D3DKMT_HANDLE                  hSharedHandle;
  D3DKMT_HANDLE                  hKeyedMutex;
  VOID                           *pPrivateRuntimeData;
  UINT                           PrivateRuntimeDataSize;
  D3DKMT_CREATEKEYEDMUTEX2_FLAGS Flags;
} D3DKMT_CREATEKEYEDMUTEX2;
````


## -struct-fields
<dl>

### -field <b>InitialValue</b>

<dd>
<p>[in] A 64-bit value that specifies the initial value to create the keyed mutex for.</p>
</dd>

### -field <b>hSharedHandle</b>

<dd>
<p>[out] A value of type <b>D3DKMT_HANDLE</b> that represents a kernel-mode shared global handle to the keyed mutex object.</p>
</dd>

### -field <b>hKeyedMutex</b>

<dd>
<p>[out] A value of type <b>D3DKMT_HANDLE</b> that represents a kernel-mode handle to the keyed mutex object in the current process.</p>
</dd>

### -field <b>pPrivateRuntimeData</b>

<dd>
<p>[in] A pointer to a caller-supplied buffer where the runtime private data associated with the resource is stored.</p>
</dd>

### -field <b>PrivateRuntimeDataSize</b>

<dd>
<p>[in] The size, in bytes, of the buffer pointed to by the <b>pPrivateRuntimeData</b> member.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/hh780254">D3DKMT_CREATEKEYEDMUTEX2_FLAGS</a> structure that indicates how to specify a handle to a keyed mutex object.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh780254">D3DKMT_CREATEKEYEDMUTEX2_FLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439345">D3DKMTCreateKeyedMutex2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_CREATEKEYEDMUTEX2 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
