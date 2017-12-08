---
UID: NS.fwpsk._NDIS_SWITCH_PARAMETERS
title: NDIS_SWITCH_PARAMETERS
author: windows-driver-content
description: The NDIS_SWITCH_PARAMETERS structure contains the configuration data for a Hyper-V extensible switch.
old-location: netvista\ndis_switch_parameters.htm
old-project: netvista
ms.assetid: 766e042a-3f21-4f57-a780-83f92bef0a6c
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_SWITCH_PARAMETERS,
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
req.alt-api: NDIS_SWITCH_PARAMETERS
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

# NDIS_SWITCH_PARAMETERS structure



## -description
<p>The <b>NDIS_SWITCH_PARAMETERS</b> structure contains the configuration data for a Hyper-V extensible switch.</p>


## -syntax

````
typedef struct _NDIS_SWITCH_PARAMETERS {
  NDIS_OBJECT_HEADER       Header;
  ULONG                    Flags;
  NDIS_SWITCH_NAME         SwitchName;
  NDIS_SWITCH_FRIENDLYNAME SwitchFriendlyName;
  UINT32                   NumSwitchPorts;
  BOOLEAN                  IsActive;
} NDIS_SWITCH_PARAMETERS, *PNDIS_SWITCH_PARAMETERS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The type, revision, and size of the <b>NDIS_SWITCH_PARAMETERS</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The <b>Type</b> member of <b>Header</b> must be set to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_SWITCH_PARAMETERS</b> structure, the <b>Revision</b> member of <b>Header</b> must be set to the following value: </p>
<p></p>
<dl>

### -field NDIS_SWITCH_PARAMETERS_REVISION_1

<dd>
<p>Original version for NDIS 6.30 and later.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NDIS_SWITCH_PARAMETERS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field Flags

<dd>
<p>A ULONG value that contains a bitwise <b>OR</b> of flags. This member is reserved for NDIS.

</p>
</dd>

### -field SwitchName

<dd>
<p> An <b>NDIS_SWITCH_NAME</b> value that specifies the unique internal name of the extensible switch.</p>
<p>The internal switch name is used by WMI-based policy management applications. For more information, see <a href="netvista.managing_hyper_v_extensible_switch_extensibility_policies">Managing Hyper-V Extensible Switch Policies</a>.</p>
</dd>

### -field SwitchFriendlyName

<dd>
<p> An <b>NDIS_SWITCH_FRIENDLYNAME</b> value that specifies the user-friendly description of the extensible switch.</p>
</dd>

### -field NumSwitchPorts

<dd>
<p>A UINT32 value that specifies the number of ports configured on the extensible switch.</p>
</dd>

### -field IsActive

<dd>
<p>A BOOLEAN that if TRUE indicates that the Hyper-V extensible switch activation has finished and it is safe to query for other switch configuration such as enumerating ports, NICs, and properties. If FALSE, the extension must wait for the <a href="..\ndis\ns-ndis--net-pnp-event.md">NetEventSwitchActivate</a> PNP event to be issued before querying for switch configuration. </p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_SWITCH_PARAMETERS</b> structure is used in the 
    OID request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598270">OID_SWITCH_PARAMETERS</a>.</p>

<p>This structure is also passed in the <i>vSwitch</i> parameter of the following callout functions for Windows Filtering Platform callout drivers:<ul>
<li>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-interface-event-callback0.md">FWPS_VSWITCH_INTERFACE_EVENT_CALLBACK0</a>
</li>
<li>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-lifetime-event-callback0.md">FWPS_VSWITCH_LIFETIME_EVENT_CALLBACK0</a>
</li>
<li>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-policy-event-callback0.md">FWPS_VSWITCH_POLICY_EVENT_CALLBACK0</a>
</li>
<li>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-port-event-callback0.md">FWPS_VSWITCH_PORT_EVENT_CALLBACK0</a>
</li>
<li>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-runtime-state-restore-callback0.md">FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0</a>
</li>
<li>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-runtime-state-save-callback0.md">FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0</a>
</li>
</ul>
</p>

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
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-interface-event-callback0.md">IF_COUNTEDFWPS_VSWITCH_INTERFACE_EVENT_CALLBACK0</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-lifetime-event-callback0.md">FWPS_VSWITCH_LIFETIME_EVENT_CALLBACK0</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-policy-event-callback0.md">FWPS_VSWITCH_POLICY_EVENT_CALLBACK0</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-port-event-callback0.md">FWPS_VSWITCH_PORT_EVENT_CALLBACK0</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-runtime-state-restore-callback0.md">FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-runtime-state-save-callback0.md">FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0</a>
</dt>
<dt>
<a href="netvista.if_counted_string">_STRING</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-pnp-event.md">NetEventSwitchActivate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598270">OID_SWITCH_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_PARAMETERS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
