---
UID: NS.ntddndis._NDIS_RECEIVE_FILTER_INFO
title: NDIS_RECEIVE_FILTER_INFO
author: windows-driver-content
description: The NDIS_RECEIVE_FILTER_INFO structure contains information about a receive filter that is currently configured on a miniport driver.
old-location: netvista\ndis_receive_filter_info.htm
old-project: netvista
ms.assetid: 12029cfd-58d0-4621-8cbc-c07e68db61b8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_RECEIVE_FILTER_INFO, NDIS_RECEIVE_FILTER_INFO, *PNDIS_RECEIVE_FILTER_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_RECEIVE_FILTER_INFO
req.alt-loc: Ntddndis.h
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

# NDIS_RECEIVE_FILTER_INFO structure



## -description
<p>
<p>The <b>NDIS_RECEIVE_FILTER_INFO</b> structure contains information about a receive filter that is currently configured on a miniport driver.</p>
</p>
<p>The <b>NDIS_RECEIVE_FILTER_INFO</b> structure contains information about a receive filter that is currently configured on a miniport driver.</p>
<p>NDIS receive filters are used in the following NDIS interfaces:</p>
<p>
<a href="NULL">NDIS Packet Coalescing</a>. For more information about how to use receive filters in this interface, see <a href="NULL">Managing Packet Coalescing Receive Filters</a>.</p>
<p>
<a href="NULL">Single Root I/O Virtualization (SR-IOV)</a>. For more information about how to use receive filters in this interface, see <a href="NULL">Setting a Receive Filter on a Virtual Port</a>.</p>
<p>
<a href="NULL">Virtual Machine Queue (VMQ)</a>. For more information about how to use receive filters in this interface, see <a href="NULL">Setting and Clearing VMQ Filters</a>.</p>


## -syntax

````
typedef struct _NDIS_RECEIVE_FILTER_INFO {
  NDIS_OBJECT_HEADER       Header;
  ULONG                    Flags;
  NDIS_RECEIVE_FILTER_TYPE FilterType;
  NDIS_RECEIVE_FILTER_ID   FilterId;
} NDIS_RECEIVE_FILTER_INFO, *PNDIS_RECEIVE_FILTER_INFO;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_RECEIVE_FILTER_INFO</b> structure. The driver sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT.</p>
<p>To indicate the version of the <b>NDIS_RECEIVE_FILTER_INFO</b> structure, the driver sets the 
     <b>Revision</b> member to one of the following values:</p>
<p></p>
<dl>

### -field <a id="NDIS_RECEIVE_FILTER_INFO_REVISION_1"></a><a id="ndis_receive_filter_info_revision_1"></a>NDIS_RECEIVE_FILTER_INFO_REVISION_1

<dd>
<p>Original version for NDIS 6.20.</p>
<p>The driver sets the 
        <b>Size</b> member to NDIS_SIZEOF_RECEIVE_FILTER_INFO_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitwise OR of flags. This member is reserved for NDIS.</p>
</dd>

### -field <b>FilterType</b>

<dd>
<p>The type of the receive filter.</p>
</dd>

### -field <b>FilterId</b>

<dd>
<p>A receive filter identifier. The filter identifier
     is an integer from one up to and including the number of receive filters that the network adapter
     supports. A value of zero is not valid.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_RECEIVE_FILTER_INFO</b> structure is used with the 
    <a href="..\ntddndis\ns-ntddndis--ndis-receive-filter-info-array.md">
    NDIS_RECEIVE_FILTER_INFO_ARRAY</a> structure for the 
    OID request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569787">OID_RECEIVE_FILTER_ENUM_FILTERS</a>. This OID request enumerates receive filters that have been configured on the miniport driver. This includes packet coalescing receive filters or the receive filters configured on a  receive queue that is used in the VMQ or SR-IOV interface.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.20 and later.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-receive-filter-info-array.md">
   NDIS_RECEIVE_FILTER_INFO_ARRAY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569787">OID_RECEIVE_FILTER_ENUM_FILTERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_RECEIVE_FILTER_INFO structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
