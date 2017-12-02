---
UID: NS.ndis._NDIS_FILTER_INTERFACE
title: NDIS_FILTER_INTERFACE
author: windows-driver-content
description: The NDIS_FILTER_INTERFACE structure defines the attributes for an NDIS filter.
old-location: netvista\ndis_filter_interface.htm
old-project: netvista
ms.assetid: 0a765829-3558-48ea-b788-7cce6c4b64c6
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_FILTER_INTERFACE, NDIS_FILTER_INTERFACE, *PNDIS_FILTER_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_FILTER_INTERFACE
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
req.iface: 
---

# NDIS_FILTER_INTERFACE structure



## -description
<p>The NDIS_FILTER_INTERFACE structure defines the attributes for an NDIS filter.</p>


## -syntax

````
typedef struct _NDIS_FILTER_INTERFACE {
  NDIS_OBJECT_HEADER Header;
  ULONG              Flags;
  ULONG              FilterType;
  ULONG              FilterRunType;
  NET_IFINDEX        IfIndex;
  NET_LUID           NetLuid;
  NDIS_STRING        FilterClass;
  NDIS_STRING        FilterInstanceName;
} NDIS_FILTER_INTERFACE, *PNDIS_FILTER_INTERFACE;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     filter interface structure. </p>
<p>NDIS sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT.</p>
<p>If the handle passed to <a href="..\ndis\nf-ndis-ndisenumeratefiltermodules.md">NdisEnumerateFilterModules</a> belongs to an NDIS 6.30 or later object, then NDIS sets <b>Revision</b> to NDIS_FILTER_INTERFACE_REVISION_2 and <b>Size</b> to NDIS_SIZEOF_FILTER_INTERFACE_REVISION_2.</p>
<p>If the handle passed to <a href="..\ndis\nf-ndis-ndisenumeratefiltermodules.md">NdisEnumerateFilterModules</a> belongs to an NDIS 6.20 or earlier object, then NDIS sets <b>Revision</b> to NDIS_FILTER_INTERFACE_REVISION_1 and <b>Size</b> to NDIS_SIZEOF_FILTER_INTERFACE_REVISION_1.</p>
</dd>

### -field Flags

<dd>
<p>A bit field that defines the type of NDIS driver that implements the filter. This member must be
     set to one of the following driver types:
     </p>
<p></p>
<dl>

### -field NDIS_FILTER_INTERFACE_IM_FILTER

<dd>
<p>The filter is implemented in an NDIS 5.1 or earlier filter intermediate driver.</p>
</dd>

### -field NDIS_FILTER_INTERFACE_LW_FILTER

<dd>
<p>The filter is implemented in an NDIS 6.0 or later filter driver.</p>
</dd>

### -field NDIS_FILTER_INTERFACE_SEND_BYPASS

<dd>
<p>The filter is currently not attached to the send path.  This flag is only set if <b>Header.Revision</b> is greater than or equal to NDIS_FILTER_INTERFACE_REVISION_2.</p>
</dd>

### -field NDIS_FILTER_INTERFACE_RECEIVE_BYPASS

<dd>
<p>The filter is currently not attached to the receive path.  This flag is only set if <b>Header.Revision</b> is greater than or equal to NDIS_FILTER_INTERFACE_REVISION_2.
</p>
</dd>
</dl>
</dd>

### -field FilterType

<dd>
<p>The behavior type for the filter. This type must be one of the following values:
     </p>
<p></p>
<dl>

### -field NdisFilterTypeMonitoring = 1

<dd>
<p>A monitoring filter.</p>
</dd>

### -field NdisFilterTypeModifying = 2

<dd>
<p>A modifying filter.</p>
</dd>
</dl>
</dd>

### -field FilterRunType

<dd>
<p>The runtime attachment priority type for the filter. This type must be one of the following
     values:
     </p>
<p></p>
<dl>

### -field NdisFilterRunTypeMandatory = 1

<dd>
<p>A mandatory filter. If the filter does not attach to the driver stack, NDIS will tear down the
       rest of the stack.</p>
</dd>

### -field NdisFilterRunTypeOptional = 2

<dd>
<p>An optional filter. If the filter does not attach to the driver stack, NDIS will not tear down the
       rest of the stack.</p>
</dd>
</dl>
</dd>

### -field IfIndex

<dd>
<p>The NDIS interface index of the filter module.</p>
</dd>

### -field NetLuid

<dd>
<p>The 
     <a href="netvista.net_luid">NET_LUID</a> value that is assigned to the filter
     module. The NET_LUID is equivalent to the interface name (ifName in 
     RFC 2863).</p>
</dd>

### -field FilterClass

<dd>
<p>A UNICODE string that specifies the filter class. This string is the same as the 
     <b>FilterClass</b> INF file entry.</p>
</dd>

### -field FilterInstanceName

<dd>
<p>The filter instance name.</p>
</dd>
</dl>

## -remarks
<p>The 
    <a href="..\ndis\nf-ndis-ndisenumeratefiltermodules.md">
    NdisEnumerateFilterModules</a> function returns one NDIS_FILTER_INTERFACE structure for each filter in
    the driver stack. The 
    <b>Flags</b> member identifies the filter as an NDIS 5.1 or earlier filter intermediate driver or an NDIS
    6.0 or later NDIS filter module.</p>

<p>A light-weight filter may dynamically insert or remove itself from the send or receive path by calling <a href="..\ndis\nf-ndis-ndisfrestartfilter.md">NdisFRestartFilter</a> and providing a <a href="..\ndis\ns-ndis--ndis-filter-partial-characteristics.md">NDIS_FILTER_PARTIAL_CHARACTERISTICS</a> structure to <a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisenumeratefiltermodules.md">NdisEnumerateFilterModules</a>
</dt>
<dt>
<a href="netvista.net_luid">NET_LUID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_FILTER_INTERFACE structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
