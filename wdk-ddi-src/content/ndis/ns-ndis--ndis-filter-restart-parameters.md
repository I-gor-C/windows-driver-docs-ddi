---
UID: NS.ndis._NDIS_FILTER_RESTART_PARAMETERS
title: NDIS_FILTER_RESTART_PARAMETERS
author: windows-driver-content
description: The NDIS_FILTER_RESTART_PARAMETERS structure defines the restart parameters for the filter module.
old-location: netvista\ndis_filter_restart_parameters.htm
old-project: netvista
ms.assetid: f61e8c1b-5cc5-4d61-a4e2-39ca402cd710
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_FILTER_RESTART_PARAMETERS, NDIS_FILTER_RESTART_PARAMETERS, *PNDIS_FILTER_RESTART_PARAMETERS
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
req.alt-api: NDIS_FILTER_RESTART_PARAMETERS
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

# NDIS_FILTER_RESTART_PARAMETERS structure



## -description
<p>The NDIS_FILTER_RESTART_PARAMETERS structure defines the restart parameters for the filter
  module.</p>


## -syntax

````
typedef struct _NDIS_FILTER_RESTART_PARAMETERS {
  NDIS_OBJECT_HEADER       Header;
  NDIS_MEDIUM              MiniportMediaType;
  NDIS_PHYSICAL_MEDIUM     MiniportPhysicalMediaType;
  PNDIS_RESTART_ATTRIBUTES RestartAttributes;
  NET_IFINDEX              LowerIfIndex;
  NET_LUID                 LowerIfNetLuid;
  ULONG                    Flags;
} NDIS_FILTER_RESTART_PARAMETERS, *PNDIS_FILTER_RESTART_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure
     for the NDIS_FILTER_RESTART_PARAMETERS structure. NDIS sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_FILTER_RESTART_PARAMETERS, the 
     <b>Revision</b> member to NDIS_FILTER_RESTART_PARAMETERS_REVISION_1, and the Size member to
     NDIS_SIZEOF__FILTER_RESTART_PARAMETERS_REVISION_1.</p>
</dd>

### -field <b>MiniportMediaType</b>

<dd>
<p>The 
     NdisMedium
     <i>Xxx</i> type that the base underlying miniport adapter supports. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff565910">NDIS_MEDIUM</a>.</p>
</dd>

### -field <b>MiniportPhysicalMediaType</b>

<dd>
<p>The physical medium type for the base underlying miniport adapter. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569621">OID_GEN_PHYSICAL_MEDIUM</a>.</p>
</dd>

### -field <b>RestartAttributes</b>

<dd>
<p>
      A pointer to an NDIS_RESTART_ATTRIBUTES structure.
     </p>
</dd>

### -field <b>LowerIfIndex</b>

<dd>
<p>The NDIS network interface index of the interface just below the current filter module. That is,
     if there are filter modules or NDIS 5.<i>x</i> filter intermediate drivers that are installed over a physical miniport adapter or the
     highest-level MUX intermediate driver, this member contains the interface index of the filter module
     interface or filter intermediate driver interface that is just below the current filter module. If there
     are no filter module or filter intermediate driver interfaces installed over the physical miniport
     adapter or the highest-level MUX intermediate driver, this member contains the interface index of the
     underlying physical miniport adapter or the highest-level MUX intermediate driver virtual
     miniport.</p>
</dd>

### -field <b>LowerIfNetLuid</b>

<dd>
<p>The NDIS network interface 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a> value of the interface just below the
     current filter module. That is, if there are filter modules or NDIS 5.<i>x</i> filter intermediate drivers that are installed over a physical miniport adapter or the
     highest-level MUX intermediate driver, this member contains the network interface NET_LUID of the filter
     module interface or filter intermediate driver interface that is just below the current filter module.
     If there are no filter module or filter intermediate driver interfaces installed over the physical
     miniport adapter or the highest-level MUX intermediate driver, this member contains the network
     interface NET_LUID of the underlying physical miniport adapter or the highest-level MUX intermediate
     driver virtual miniport.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>

## -remarks
<p>To define filter module restart parameters, NDIS passes a pointer to an NDIS_FILTER_RESART_PARAMETERS
    structure to the 
    <a href="..\ndis\nc-ndis-filter-restart.md">FilterRestart</a> function.</p>

<p>Filter drivers can modify the restart attributes that are specified by underlying drivers. For more
    information about how to modify restart attributes, see 
    <a href="..\ndis\nc-ndis-filter-restart.md">FilterRestart</a>.</p>

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
<a href="..\ndis\nc-ndis-filter-restart.md">FilterRestart</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565910">NDIS_MEDIUM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567255">NDIS_RESTART_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569621">OID_GEN_PHYSICAL_MEDIUM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_FILTER_RESTART_PARAMETERS structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
