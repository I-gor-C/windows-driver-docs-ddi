---
UID: NS.ndis._NDIS_MINIPORT_INIT_PARAMETERS
title: NDIS_MINIPORT_INIT_PARAMETERS
author: windows-driver-content
description: The NDIS_MINIPORT_INIT_PARAMETERS structure defines the initialization parameters for a miniport adapter.
old-location: netvista\ndis_miniport_init_parameters.htm
ms.assetid: 945d921b-3024-4c4f-a50d-e996c6183db7
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
req.alt-api: NDIS_MINIPORT_INIT_PARAMETERS
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
ms.keywords: NDIS_MINIPORT_INIT_PARAMETERS, NDIS_MINIPORT_INIT_PARAMETERS, *PNDIS_MINIPORT_INIT_PARAMETERS
req.iface: 
---

# NDIS_MINIPORT_INIT_PARAMETERS structure



## -description
<p>The <b>NDIS_MINIPORT_INIT_PARAMETERS</b> structure defines the initialization parameters for a miniport
  adapter.</p>


## -syntax

````
typedef struct _NDIS_MINIPORT_INIT_PARAMETERS {
  NDIS_OBJECT_HEADER                   Header;
  ULONG                                Flags;
  PNDIS_RESOURCE_LIST                  AllocatedResources;
  NDIS_HANDLE                          IMDeviceInstanceContext;
  NDIS_HANDLE                          MiniportAddDeviceContext;
  NET_IFINDEX                          IfIndex;
  NET_LUID                             NetLuid;
  PNDIS_PORT_AUTHENTICATION_PARAMETERS DefaultPortAuthStates;
  PNDIS_PCI_DEVICE_CUSTOM_PROPERTIES   PciDeviceCustomProperties;
} NDIS_MINIPORT_INIT_PARAMETERS, *PNDIS_MINIPORT_INIT_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_MINIPORT_INIT_PARAMETERS structure. NDIS sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specified to NDIS_OBJECT_TYPE_MINIPORT_INIT_PARAMETERS, the 
     <b>Revision</b> member to NDIS_MINIPORT_INIT_PARAMETERS_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_MINIPORT_INIT_PARAMETER_REVISION_1.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>AllocatedResources</b>

<dd>
<p>A pointer to an NDIS_RESOURCE_LIST-type structure that lists the hardware resources that the Plug
     and Play Manager assigned to the miniport adapter. The NDIS_RESOURCE_LIST is type definition that is
     equivalent to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff541981">CM_PARTIAL_RESOURCE_LIST</a> on Windows
     2000 and later platforms.</p>
</dd>

### -field <b>IMDeviceInstanceContext</b>

<dd>
<p>A pointer to the context area for a virtual device that an intermediate driver supports. The
     driver passed this pointer to the 
     <a href="https://msdn.microsoft.com/f65c2974-4bf4-4948-ac07-527e69c96303">
     NdisIMInitializeDeviceInstanceEx</a> function at the 
     <i>DeviceContext</i> parameter. If the miniport driver is not an intermediate driver, 
     <b>IMDeviceInstanceContext</b> is <b>NULL</b>.</p>
</dd>

### -field <b>MiniportAddDeviceContext</b>

<dd>
<p>A handle for a driver-allocated context area, or <b>NULL</b>. The miniport driver specifies this handle,
     if any, in the 
     <a href="https://msdn.microsoft.com/50e04b5a-e430-484c-aabb-cc7b9ecb53b0">MiniportAddDevice</a> function.</p>
</dd>

### -field <b>IfIndex</b>

<dd>
<p>The network interface index that is associated with the miniport adapter.</p>
</dd>

### -field <b>NetLuid</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a> value that is associated with the
     miniport adapter.</p>
</dd>

### -field <b>DefaultPortAuthStates</b>

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/7c411d9e-1064-4278-9870-0546891d4743">
     NDIS_PORT_AUTHENTICATION_PARAMETERS</a> structure that defines the default port authentication
     parameters for the miniport adapter. For more information about port authentication parameters, see 
     <a href="netvista.oid_gen_port_authentication_parameters">
     OID_GEN_PORT_AUTHENTICATION_PARAMETERS</a>.</p>
</dd>

### -field <b>PciDeviceCustomProperties</b>

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/fd61184f-0502-492d-9014-6afbfd70c189">
     NDIS_PCI_DEVICE_CUSTOM_PROPERTIES</a> structure that defines the PCI custom properties for the
     miniport adapter.</p>
</dd>
</dl>

## -remarks
<p>NDIS passes a pointer to an initialized <b>NDIS_MINIPORT_INIT_PARAMETERS</b> structure in the 
    <i>MiniportInitParameters</i> parameter of the 
    <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> function.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541981">CM_PARTIAL_RESOURCE_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/50e04b5a-e430-484c-aabb-cc7b9ecb53b0">MiniportAddDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fd61184f-0502-492d-9014-6afbfd70c189">
   NDIS_PCI_DEVICE_CUSTOM_PROPERTIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7c411d9e-1064-4278-9870-0546891d4743">
   NDIS_PORT_AUTHENTICATION_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f65c2974-4bf4-4948-ac07-527e69c96303">
   NdisIMInitializeDeviceInstanceEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a>
</dt>
<dt>
<a href="netvista.oid_gen_port_authentication_parameters">
   OID_GEN_PORT_AUTHENTICATION_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_MINIPORT_INIT_PARAMETERS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
