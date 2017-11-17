---
UID: NS.ntddndis._NDIS_NDK_CONNECTIONS
title: NDIS_NDK_CONNECTIONS
author: windows-driver-content
description: The NDIS_NDK_CONNECTIONS structure describes the NDK connections that are active on a miniport adapter.
old-location: netvista\ndis_ndk_connections.htm
ms.assetid: 24149E73-6BA8-4C5E-8649-25A90A3D01AF
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_NDK_CONNECTIONS
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
ms.keywords: NDIS_NDK_CONNECTIONS, NDIS_NDK_CONNECTIONS
req.iface: 
---

# NDIS_NDK_CONNECTIONS structure



## -description
<p>The <b>NDIS_NDK_CONNECTIONS</b> structure describes the NDK connections that are active on a miniport adapter.</p>


## -syntax

````
typedef struct _NDIS_NDK_CONNECTIONS {
  NDIS_OBJECT_HEADER                            Header;
  ULONG                                         Count;
  BOOLEAN                                       NDConnectionsMappedtoTCPConnections;
  _Field_size_(Count) NDIS_NDK_CONNECTION_ENTRY Connections[1];
} NDIS_NDK_CONNECTIONS, *PNDIS_NDK_CONNECTIONS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure that describes this <b>NDIS_NDK_CONNECTIONS</b> structure. Set the members of the <b>NDIS_OBJECT_HEADER</b> structure as follows:</p>
<ul>
<li>Set the <b>Type</b> member to <b>NDIS_OBJECT_TYPE_DEFAULT</b>.</li>
<li>Set the <b>Revision</b> member to <b>NDIS_NDK_CONNECTIONS_REVISION_1</b>.</li>
<li>Set the <b>Size</b> member to (USHORT)min(MAXUSHORT, NDIS_SIZEOF_NDK_CONNECTIONS_REVISION_1(n)).</li>
</ul>
</dd>

### -field <b>Count</b>

<dd>
<p>The number of elements in the connection array that is passed in the <b>Connections</b> member. Each element in the array is an <a href="https://msdn.microsoft.com/library/windows/hardware/hh451562">NDIS_NDK_CONNECTION_ENTRY</a> structure. </p>
</dd>

### -field <b>NDConnectionsMappedtoTCPConnections</b>

<dd>
<p>A BOOLEAN value that specifies how the connections are mapped. If the RDMA technology for the NDK provider requires the provider to map ND connections to TCP connections, the NDK provider must set the <b>NDConnectionsMappedtoTCPConnections</b> member to TRUE. Otherwise, <b>NDConnectionsMappedtoTCPConnections</b> is FALSE.</p>
</dd>

### -field <b>Connections</b>

<dd>
<p>A variable-sized array of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451562">NDIS_NDK_CONNECTION_ENTRY</a> structures where the size of the array is determined by the number of connections being returned. The <b>Count</b> member  specifies the number of elements in the connection array. </p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_NDK_CONNECTIONS</b> structure is returned with the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451810">OID_NDK_CONNECTIONS</a> OID. The <b>InformationBuffer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a> structure contains a pointer to this structure.

</p>

<p>This structure is variable-sized and contains elements equal in number to the number of connections that are returned. The actual size of the connection array as an element count is indicated by the <b>Count</b> member. </p>

<p>If the RDMA technology for the NDK provider requires the provider to map ND connections to TCP connections, the NDK provider must also report the underlying TCP connection 4-tuple for each ND connection as follows:</p>

<p> The first entry contains the ND addressing information (local and remote IP address, and ND port number) and the immediate next entry contains the corresponding TCP connection's addressing information (local and remote IP address, and TCP port number). </p>

<p>Therefore, entries at index 0, 2, 4, and so on, contain ND addressing information (plus properly filled-in other members) and entries at index 1, 3, 5 and so on, contain TCP addressing info (where other members are left untouched).</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451562">NDIS_NDK_CONNECTION_ENTRY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451810">OID_NDK_CONNECTIONS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_NDK_CONNECTIONS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
