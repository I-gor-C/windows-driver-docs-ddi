---
UID: NS.fwpsk._NDIS_SWITCH_PORT_PARAMETERS
title: NDIS_SWITCH_PORT_PARAMETERS
author: windows-driver-content
description: The NDIS_SWITCH_PORT_PARAMETERS structure contains the configuration data for a Hyper-V extensible switch port.
old-location: netvista\ndis_switch_port_parameters.htm
old-project: netvista
ms.assetid: E68A9018-1E79-4DA6-8C7A-434A2468169F
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_SWITCH_PORT_PARAMETERS,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fwpsk.h
req.include-header: Ndis.h, Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_SWITCH_PORT_PARAMETERS
req.alt-loc: Ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NDIS_SWITCH_PORT_PARAMETERS structure



## -description
<p>The <b>NDIS_SWITCH_PORT_PARAMETERS</b> structure contains the configuration data for a Hyper-V extensible switch port. </p>


## -syntax

````
typedef struct _NDIS_SWITCH_PORT_PARAMETERS {
  NDIS_OBJECT_HEADER            Header;
  ULONG                         Flags;
  NDIS_SWITCH_PORT_ID           PortId;
  NDIS_SWITCH_PORT_NAME         PortName;
  NDIS_SWITCH_PORT_FRIENDLYNAME PortFriendlyName;
  NDIS_SWITCH_PORT_TYPE         PortType;
  BOOLEAN                       IsValidationPort;
  NDIS_SWITCH_PORT_PARAMETERS   PortState;
} NDIS_SWITCH_PORT_PARAMETERS, *PNDIS_SWITCH_PORT_PARAMETERS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The type, revision, and size of the <b>NDIS_SWITCH_PORT_PARAMETERS</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The <b>Type</b> member of <b>Header</b> must be set to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_SWITCH_PORT_PARAMETERS</b> structure, the <b>Revision</b> member of <b>Header</b> must be set to the following value:  </p>
<p></p>
<dl>

### -field NDIS_SWITCH_PORT_PARAMETERS_REVISION_1

<dd>
<p>Original version for NDIS 6.30 and later.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NDIS_SWITCH_PORT_PARAMETERS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field Flags

<dd>
<p>A ULONG value that contains a bitwise <b>OR</b> of flags. This member is reserved for NDIS.

</p>
</dd>

### -field PortId

<dd>
<p>An NDIS_SWITCH_PORT_ID value that contains the unique identifier of the extensible switch port.</p>
</dd>

### -field PortName

<dd>
<p> An NDIS_SWITCH_PORT_NAME value that specifies the unique internal name of the extensible switch port. </p>
<p>The internal port name is used by WMI-based policy management applications. For more information, see <a href="netvista.managing_hyper_v_extensible_switch_extensibility_policies">Managing Hyper-V Extensible Switch Policies</a>.</p>
</dd>

### -field PortFriendlyName

<dd>
<p> An NDIS_SWITCH_PORT_FRIENDLYNAME value that specifies the user-friendly description of the extensible switch port.</p>
</dd>

### -field PortType

<dd>
<p>An <a href="..\ntddndis\ne-ntddndis--ndis-switch-port-type.md">NDIS_SWITCH_PORT_TYPE</a> value that specifies the type of the extensible switch port.</p>
</dd>

### -field IsValidationPort

<dd>
<p> If TRUE, indicates a port that is temporarily created for test and validation purposes before a VM network adapter connection is established. For more information about this port type, see <a href="netvista.validation_ports">Validation Ports</a>.</p>
</dd>

### -field PortState

<dd>
<p> An <a href="..\ntddndis\ne-ntddndis--ndis-switch-port-state.md">NDIS_SWITCH_PORT_STATE</a> value that specifies the current state of the port. </p>
</dd>
</dl>

## -remarks
<p>The <b>InformationBuffer</b> member of the <a href="..\ndis\ns-ndis--ndis-oid-request.md">NDIS_OID_REQUEST</a>  structure contains a pointer to an <b>NDIS_SWITCH_PORT_PARAMETERS</b> structure for the following OID requests:</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598272">OID_SWITCH_PORT_CREATE</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh846217">OID_SWITCH_PORT_UPDATED</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598273">OID_SWITCH_PORT_DELETE</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598279">OID_SWITCH_PORT_TEARDOWN</a>
</p>

<p>OID query requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598271">OID_SWITCH_PORT_ARRAY</a> return an <a href="..\fwpsk\ns-fwpsk--ndis-switch-port-array.md">NDIS_SWITCH_PORT_ARRAY</a> structure that contains an array of elements. Each element is formatted as an <b>NDIS_SWITCH_PORT_PARAMETERS</b> structure.</p>

<p>Extensible switch extensions can access the  port property buffer inside an <b>NDIS_SWITCH_PORT_PARAMETERS</b> structure by using the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598223">NDIS_SWITCH_PORT_AT_ARRAY_INDEX</a> macro.</p>

## -requirements
<table>
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
<dt>Ndis.h (include Ndis.h or Fwpsk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="netvista.if_counted_string">IF_COUNTED_STRING</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-oid-request.md">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="..\fwpsk\ns-fwpsk--ndis-switch-port-array.md">NDIS_SWITCH_PORT_ARRAY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598223">NDIS_SWITCH_PORT_AT_ARRAY_INDEX</a>
</dt>
<dt>
<a href="..\fwpsk\ns-fwpsk--ndis-switch-port-parameters.md">NDIS_SWITCH_PORT_PARAMETERS</a>
</dt>
<dt>
<a href="..\ntddndis\ne-ntddndis--ndis-switch-port-state.md">NDIS_SWITCH_PORT_STATE</a>
</dt>
<dt>
<a href="..\ntddndis\ne-ntddndis--ndis-switch-port-type.md">NDIS_SWITCH_PORT_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598271">OID_SWITCH_PORT_ARRAY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598272">OID_SWITCH_PORT_CREATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598273">OID_SWITCH_PORT_DELETE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598279">OID_SWITCH_PORT_TEARDOWN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_PORT_PARAMETERS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
