---
UID: NC.ndkpi.NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN
title: NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN
author: windows-driver-content
description: The NdkGetPrivilegedMemoryRegionToken (NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN) function gets an NDK privileged memory region token.
old-location: netvista\ndk_fn_get_privileged_memory_region_token.htm
old-project: netvista
ms.assetid: A6295FEE-3633-42E7-A2EA-BA0D3C9E4101
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_WWAN_VISIBLE_PROVIDERS, NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndkpi.h
req.include-header: Ndkpi.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdkGetPrivilegedMemoryRegionToken
req.alt-loc: ndkpi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN callback



## -description
<p>The <i>NdkGetPrivilegedMemoryRegionToken</i> (<i>NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN</i>) function gets an NDK privileged  memory region token.</p>


## -prototype

````
NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN NdkGetPrivilegedMemoryRegionToken;

VOID NdkGetPrivilegedMemoryRegionToken(
  _In_  NDK_PD *pNdkPd,
  _Out_ UINT32 *pToken
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkPd</i> [in]

<dd>
<p>A pointer to an NDK protection domain (PD) object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439931">NDK_PD</a>).</p>
</dd>

### -param <i>pToken</i> [out]

<dd>
<p>A memory token value is returned in this location.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><i>NdkGetPrivilegedMemoryRegionToken</i> gets a privileged  memory region token value that allows adapter logical addresses  to be used directly without memory registration. This token must provide LOCAL_READ and LOCAL_WRITE access. A provider must never allow remote access for the privileged memory region token.</p>

<p><i>NdkGetPrivilegedMemoryRegionToken</i> gets a privileged  memory region token value that allows adapter logical addresses  to be used directly without memory registration. This token must provide LOCAL_READ and LOCAL_WRITE access. A provider must never allow remote access for the privileged memory region token.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>None supported</p>
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
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndkpi.h (include Ndkpi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439931">NDK_PD</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
