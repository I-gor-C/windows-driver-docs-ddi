---
UID: NS.ndis._NDIS_MINIPORT_PNP_CHARACTERISTICS
title: NDIS_MINIPORT_PNP_CHARACTERISTICS
author: windows-driver-content
description: The NDIS_MINIPORT_PNP_CHARACTERISTICS structure specifies entry points for functions that allow a miniport driver to process some Plug and Play (PnP) I/O request packets (IRPs).
old-location: netvista\ndis_miniport_pnp_characteristics.htm
ms.assetid: 97820a22-aa20-4d47-a4c2-0c0d50540823
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_MINIPORT_PNP_CHARACTERISTICS
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
ms.keywords: NDIS_MINIPORT_PNP_CHARACTERISTICS, NDIS_MINIPORT_PNP_CHARACTERISTICS, *PNDIS_MINIPORT_PNP_CHARACTERISTICS
req.iface: 
---

# NDIS_MINIPORT_PNP_CHARACTERISTICS structure



## -description
<p>The NDIS_MINIPORT_PNP_CHARACTERISTICS structure specifies entry points for functions that allow a
  miniport driver to process some Plug and Play (PnP) I/O request packets (IRPs).</p>


## -syntax

````
typedef struct _NDIS_MINIPORT_PNP_CHARACTERISTICS {
  NDIS_OBJECT_HEADER                            Header;
  MINIPORT_ADD_DEVICE_HANDLER                   MiniportAddDeviceHandler;
  MINIPORT_REMOVE_DEVICE_HANDLER                MiniportRemoveDeviceHandler;
  MINIPORT_FILTER_RESOURCE_REQUIREMENTS_HANDLER MiniportFilterResourceRequirementsHandler;
  MINIPORT_START_DEVICE_HANDLER                 MiniportStartDeviceHandler;
  ULONG                                         Flags;
} NDIS_MINIPORT_PNP_CHARACTERISTICS, *PNDIS_MINIPORT_PNP_CHARACTERISTICS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_MINIPORT_PNP_CHARACTERISTICS structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_MINIPORT_PNP_CHARACTERISTICS, the 
     <b>Revision</b> member to NDIS_MINIPORT_PNP_CHARACTERISTICS_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_MINIPORT_PNP_CHARACTERISTICS_REVISION_1.</p>
</dd>

### -field <b>MiniportAddDeviceHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/50e04b5a-e430-484c-aabb-cc7b9ecb53b0">MiniportAddDevice</a> function.</p>
</dd>

### -field <b>MiniportRemoveDeviceHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/24dd887b-575f-4790-bb53-7c3fb825bd61">
     MiniportRemoveDevice</a> function.</p>
</dd>

### -field <b>MiniportFilterResourceRequirementsHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/8bddb6c5-367c-4862-bdb8-4974015750da">
     MiniportFilterResourceRequirements</a> function.</p>
</dd>

### -field <b>MiniportStartDeviceHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/ccccb2c5-16ba-4463-bb35-1dc3dcc61a2f">MiniportStartDevice</a> function, if
     any. If this function is not required, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>

## -remarks
<p>Miniport drivers that support MSI-X and will change the interrupt affinity for each MSI-X message
    register functions that are defined in the NDIS_MINIPORT_PNP_CHARACTERISTICS structure. To register these
    functions, call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a> function
    from the 
    <a href="https://msdn.microsoft.com/feecae74-960c-43cf-aa70-8ab0da3d0dfe">MiniportSetOptions</a> function and
    specify an NDIS_MINIPORT_PNP_CHARACTERISTICS structure at the 
    <i>OptionalHandlers</i> parameter of 
    <b>NdisSetOptionalHandlers</b>.</p>

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
<a href="https://msdn.microsoft.com/50e04b5a-e430-484c-aabb-cc7b9ecb53b0">MiniportAddDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8bddb6c5-367c-4862-bdb8-4974015750da">
   MiniportFilterResourceRequirements</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/24dd887b-575f-4790-bb53-7c3fb825bd61">MiniportRemoveDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/feecae74-960c-43cf-aa70-8ab0da3d0dfe">MiniportSetOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/ccccb2c5-16ba-4463-bb35-1dc3dcc61a2f">MiniportStartDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_MINIPORT_PNP_CHARACTERISTICS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
