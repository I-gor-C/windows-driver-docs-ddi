---
UID: NC.ndkpi.NDK_FN_RELEASE_LAM
title: NDK_FN_RELEASE_LAM
author: windows-driver-content
description: The NdkReleaseLam (NDK_FN_RELEASE_LAM) function releases an NDK adapter logical address mapping (LAM).
old-location: netvista\ndk_fn_release_lam.htm
old-project: netvista
ms.assetid: 8CEBDCCE-5B71-443D-9DE5-F789E16843D7
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: NdkReleaseLam
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

# NDK_FN_RELEASE_LAM callback



## -description
<p>The <i>NdkReleaseLam</i> (<i>NDK_FN_RELEASE_LAM</i>) function releases an NDK adapter logical address mapping (LAM).</p>


## -prototype

````
NDK_FN_RELEASE_LAM NdkReleaseLam;

VOID NdkReleaseLam(
  _In_ NDK_ADAPTER                 *pNdkAdapter,
  _In_ NDK_LOGICAL_ADDRESS_MAPPING *pNdkLAM
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkAdapter</i> [in]

<dd>
<p>A pointer to an NDK adapter object
(<a href="..\ndkpi\ns-ndkpi--ndk-adapter.md">NDK_ADAPTER</a>).</p>
</dd>

### -param <i>pNdkLAM</i> [in]

<dd>
<p>A pointer to an <a href="..\ndkpi\ns-ndkpi--ndk-logical-address-mapping.md">NDK_LOGICAL_ADDRESS_MAPPING</a> structure that was previously initialized by calling the <i>NdkBuildLAM</i>  (<a href="..\ndkpi\nc-ndkpi-ndk-fn-build-lam.md">NDK_FN_BUILD_LAM</a>) function.
</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><i>NdkReleaseLam</i> releases an adapter logical address mapping (LAM). The associated MDL  remains unchanged. That is, the MDL is in the same state it hand when it was  passed to the <i>NdkBuildLam</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-build-lam.md">NDK_FN_BUILD_LAM</a>) function. The NDK consumer must not release a LAM until after all of the work requests that use the LAM are completed.</p>

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
<a href="..\ndkpi\ns-ndkpi--ndk-adapter.md">NDK_ADAPTER</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-adapter-dispatch.md">NDK_ADAPTER_DISPATCH</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-build-lam.md">NDK_FN_BUILD_LAM</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-logical-address-mapping.md">NDK_LOGICAL_ADDRESS_MAPPING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_RELEASE_LAM callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
