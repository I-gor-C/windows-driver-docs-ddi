---
UID: NS.ntddndis._NDIS_NDK_STATISTICS_INFO
title: NDIS_NDK_STATISTICS_INFO
author: windows-driver-content
description: The NDIS_NDK_STATISTICS_INFO structure contains the NDK statistics.
old-location: netvista\ndis_ndk_statistics_info.htm
old-project: netvista
ms.assetid: F3FA3790-0754-4D5E-9F27-8ECD71278520
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_NDK_STATISTICS_INFO, NDIS_NDK_STATISTICS_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_NDK_STATISTICS_INFO
req.alt-loc: ntddndis.h
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
req.iface: 
---

# NDIS_NDK_STATISTICS_INFO structure



## -description
<p>The <b>NDIS_NDK_STATISTICS_INFO</b> structure contains the NDK statistics.</p>


## -syntax

````
typedef struct _NDIS_NDK_STATISTICS_INFO {
  NDIS_OBJECT_HEADER            Header;
  NDIS_NDK_PERFORMANCE_COUNTERS CounterSet;
} NDIS_NDK_STATISTICS_INFO, *PNDIS_NDK_STATISTICS_INFO;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>An <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure that describes this <b>NDIS_NDK_STATISTICS_INFO</b> structure. Set the members of the <b>NDIS_OBJECT_HEADER</b> structure as follows:</p>
<ul>
<li>Set the <b>Type</b> member to <b>NDIS_OBJECT_TYPE_DEFAULT</b>.</li>
<li>Set the <b>Revision</b> member to <b>NDIS_NDK_STATISTICS_INFO_REVISION_1</b>.</li>
<li>Set the <b>Size</b> member to <b>NDIS_SIZEOF_NDK_STATISTICS_INFO_REVISION_1</b>.</li>
</ul>
</dd>

### -field CounterSet

<dd>
<p>An <a href="..\ntddndis\ns-ntddndis--ndis-ndk-performance-counters.md">NDIS_NDK_PERFORMANCE_COUNTERS</a> structure that contains the NDK performance counters.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_NDK_STATISTICS_INFO</b> structure is returned with the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451813">OID_NDK_STATISTICS</a> OID. The <b>InformationBuffer</b> member of the <a href="..\ndis\ns-ndis--ndis-oid-request.md">NDIS_OID_REQUEST</a> structure contains a pointer to this structure.

</p>

<p>The NDK-capable miniport driver is required to fill in the <b>CounterSet</b> member, which is an <a href="..\ntddndis\ns-ntddndis--ndis-ndk-performance-counters.md">NDIS_NDK_PERFORMANCE_COUNTERS</a> structure.</p>

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
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-ndk-performance-counters.md">NDIS_NDK_PERFORMANCE_COUNTERS</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451813">OID_NDK_STATISTICS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_NDK_STATISTICS_INFO structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
