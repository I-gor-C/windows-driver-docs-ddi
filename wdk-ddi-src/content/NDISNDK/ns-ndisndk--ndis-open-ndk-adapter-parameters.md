---
UID: NS.ndisndk._NDIS_OPEN_NDK_ADAPTER_PARAMETERS
title: NDIS_OPEN_NDK_ADAPTER_PARAMETERS
author: windows-driver-content
description: The NDIS_OPEN_NDK_ADAPTER_PARAMETERS structure specifies parameters to open an NDK adapter instance on the NDK-capable miniport adapter.
old-location: netvista\ndis_open_ndk_adapter_parameters.htm
ms.assetid: AC8D4FA1-59E0-4934-A6C5-EA2E645C53FA
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndisndk.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_OPEN_NDK_ADAPTER_PARAMETERS
req.alt-loc: ndisndk.h
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
ms.keywords: NDIS_OPEN_NDK_ADAPTER_PARAMETERS, NDIS_OPEN_NDK_ADAPTER_PARAMETERS, *PNDIS_OPEN_NDK_ADAPTER_PARAMETERS
req.iface: 
---

# NDIS_OPEN_NDK_ADAPTER_PARAMETERS structure



## -description
<p>The <b>NDIS_OPEN_NDK_ADAPTER_PARAMETERS</b> structure specifies parameters to open an NDK adapter instance on the NDK-capable miniport adapter.</p>


## -syntax

````
typedef struct _NDIS_OPEN_NDK_ADAPTER_PARAMETERS {
  NDK_VERSION Version;
} NDIS_OPEN_NDK_ADAPTER_PARAMETERS, *PNDIS_OPEN_NDK_ADAPTER_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of the NDK provider interface (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439942">NDK_VERSION</a>) that is to be used. </p>
<p>For NDIS 6.30 (Windows Server 2012), the major version number is 1. The  minor version number is 1.</p>
<p>For NDIS 6.40 (Windows Server 2012 R2), the major version number is 1. The  minor version number is 2.</p>
</dd>
</dl>

## -remarks
<p>To open an NDK adapter, NDIS calls the <a href="https://msdn.microsoft.com/library/windows/hardware/hh440105">OPEN_NDK_ADAPTER_HANDLER</a> function and passes it a  pointer to an <b>NDIS_OPEN_NDK_ADAPTER_PARAMETERS</b> structure that defines the NDK adapter open parameters.</p>

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
<dt>Ndisndk.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439942">NDK_VERSION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh440105">OPEN_NDK_ADAPTER_HANDLER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_OPEN_NDK_ADAPTER_PARAMETERS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
