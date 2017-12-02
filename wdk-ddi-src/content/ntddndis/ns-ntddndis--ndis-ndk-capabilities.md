---
UID: NS.ntddndis._NDIS_NDK_CAPABILITIES
title: NDIS_NDK_CAPABILITIES
author: windows-driver-content
description: The NDIS_NDK_CAPABILITIES structure specifies the capabilities of an NDK adapter.
old-location: netvista\ndis_ndk_capabilities.htm
old-project: netvista
ms.assetid: 4E8AD6FA-BB89-4CB0-A06E-7B4917390311
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_NDK_CAPABILITIES, NDIS_NDK_CAPABILITIES, *PNDIS_NDK_CAPABILITIES
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
req.alt-api: NDIS_NDK_CAPABILITIES
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

# NDIS_NDK_CAPABILITIES structure



## -description
<p>The <b>NDIS_NDK_CAPABILITIES</b> structure specifies the capabilities of an NDK adapter.</p>


## -syntax

````
typedef struct _NDIS_NDK_CAPABILITIES {
  NDIS_OBJECT_HEADER Header;
  ULONG              MaxQpCount;
  ULONG              MaxCqCount;
  ULONG              MaxMrCount;
  ULONG              MaxPdCount;
  ULONG              MaxInboundReadLimit;
  ULONG              MaxOutboundReadLimit;
  ULONG              MaxMwCount;
  ULONG              MaxSrqCount;
  ULONG64            MissingCounterMask;
  NDK_ADAPTER_INFO   *NdkInfo;
} NDIS_NDK_CAPABILITIES, *PNDIS_NDK_CAPABILITIES;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure that describes this <b>NDIS_NDK_CAPABILITIES</b> structure. Set the members of the <b>NDIS_OBJECT_HEADER</b> structure as follows:</p>
<ul>
<li>Set the <b>Type</b> member to <b>NDIS_OBJECT_TYPE_DEFAULT</b>.</li>
<li>Set the <b>Revision</b> member to <b>NDIS_NDK_CAPABILITIES_REVISION_1</b>.</li>
<li>Set the <b>Size</b> member to <b>NDIS_SIZEOF_NDK_CAPABILITIES_REVISION_1</b>.</li>
</ul>
</dd>

### -field MaxQpCount

<dd>
<p>The maximum number of queue pairs (QPs) that can be supported by the adapter.</p>
</dd>

### -field MaxCqCount

<dd>
<p>The maximum number of completion queues (CQs) that can be supported by the adapter.</p>
</dd>

### -field MaxMrCount

<dd>
<p>The maximum number of memory regions (MRs) that can be supported by the adapter.</p>
</dd>

### -field MaxPdCount

<dd>
<p>The maximum number of protection domains (PDs) that can be supported by the adapter</p>
</dd>

### -field MaxInboundReadLimit

<dd>
<p>The maximum number of incoming outstanding read requests that can be supported by the adapter. 
     If this member is zero, there is no adapter limit. In this case, there is still a limit for each queue pair. The limit for each queue pair is specified in the <b>MaxInboundReadLimit</b> member of the <a href="netvista.ndk_adapter_info">NDK_ADAPTER_INFO</a> structure.</p>
</dd>

### -field MaxOutboundReadLimit

<dd>
<p>The maximum number of outgoing outstanding read requests that can be supported by the adapter. 
    If this member is zero, there is no adapter-wide limit.  In this case, there is still a limit for each queue pair. The limit for each queue pair is specified in the <b>MaxOutboundReadLimit</b> member of the <a href="netvista.ndk_adapter_info">NDK_ADAPTER_INFO</a> structure.</p>
</dd>

### -field MaxMwCount

<dd>
<p>The maximum number of memory windows (MWs) that are supported by the adapter.</p>
</dd>

### -field MaxSrqCount

<dd>
<p>The maximum number of shared receive queues (SRQs) that are supported by the adapter.</p>
</dd>

### -field MissingCounterMask

<dd>
<p>A bitmask that identifies counters that an NDK provider does not support. NDK providers are required to support all the performance counters that are included
    in the <a href="..\ntddndis\ns-ntddndis--ndis-ndk-performance-counters.md">NDIS_NDK_PERFORMANCE_COUNTERS</a> structure. However, in the rare case that
    a provider cannot support a counter due to extreme implementation difficulties,
    the provider must indicate any unsupported counters with the mask value for the
    counter which it cannot support.</p>
</dd>

### -field NdkInfo

<dd>
<p>A pointer to an <a href="netvista.ndk_adapter_info">NDK_ADAPTER_INFO</a> structure that specifies NDK adapter capabilities and limits that are relevant for an specific NDK consumer. These capabilities can be different from system-wide limits.</p>
</dd>
</dl>

## -remarks
<p><b>NDIS_NDK_CAPABILITIES</b> specifies capacity limits that are relevant for
    system-wide management or partitioning of resources that are available on a given NDK adapter.
</p>

<p>Independent of whether NDK functionality of an adapter is currently enabled or disabled,
    an NDK-capable adapter must always indicate its capabilities during miniport initialization.
</p>

<p>The <b>NDIS_NDK_CAPABILITIES</b> structure is used in the <a href="..\ndis\ns-ndis--ndis-miniport-adapter-ndk-attributes.md">NDIS_MINIPORT_ADAPTER_NDK_ATTRIBUTES</a> structure.</p>

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
<a href="..\ndis\ns-ndis--ndis-miniport-adapter-ndk-attributes.md">NDIS_MINIPORT_ADAPTER_NDK_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-ndk-performance-counters.md">NDIS_NDK_PERFORMANCE_COUNTERS</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="netvista.ndk_adapter_info">NDK_ADAPTER_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_NDK_CAPABILITIES structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
