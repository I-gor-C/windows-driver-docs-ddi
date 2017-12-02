---
UID: NC.ndis.NDIS_SWITCH_REFERENCE_SWITCH_PORT
title: NDIS_SWITCH_REFERENCE_SWITCH_PORT
author: windows-driver-content
description: The ReferenceSwitchPort function increments the Hyper-V extensible switch reference counter for an extensible switch port.
old-location: netvista\ReferenceSwitchPort.htm
old-project: netvista
ms.assetid: 5FD2E931-AC9F-4157-9C45-F93261FC834D
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ReferenceSwitchPort
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

# NDIS_SWITCH_REFERENCE_SWITCH_PORT callback



## -description
<p>
<p>The <i>ReferenceSwitchPort</i> function increments the Hyper-V extensible switch reference counter for an extensible switch port.</p>
</p>
<p>The <i>ReferenceSwitchPort</i> function increments the Hyper-V extensible switch reference counter for an extensible switch port.</p>


## -prototype

````
NDIS_SWITCH_REFERENCE_SWITCH_PORT ReferenceSwitchPort;

NDIS_STATUS ReferenceSwitchPort(
  _In_ NDIS_SWITCH_CONTEXT NdisSwitchContext,
  _In_ NDIS_SWITCH_PORT_ID SwitchPortId
)
{ ... }
````


## -parameters
<dl>

### -param NdisSwitchContext [in]

<dd>
<p>An NDIS_SWITCH_CONTEXT value that contains the handle of the extensible switch module to which the Hyper-V extensible switch extension is attached. When the extension calls <a href="..\ndis\nf-ndis-ndisfgetoptionalswitchhandlers.md">NdisFGetOptionalSwitchHandlers</a>,  this handle is returned through the <i>NdisSwitchContext</i> parameter.</p>
</dd>

### -param SwitchPortId [in]

<dd>
<p>An NDIS_SWITCH_PORT_ID value that contains the unique identifier of the extensible switch port for which the extensible switch reference counter is incremented.</p>
<div class="alert"><b>Note</b>  The <i>SwitchPortId</i> parameter must specify the identifier of a port that is in a created state. Identifiers for ports that are in a teardown or deleted state cannot be specified. For more information about port states, see <a href="netvista.hyper_v_extensible_switch_port_and_network_adapter_states">Hyper-V Extensible Switch Port and Network Adapter States</a>.</div>
<div> </div>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns NDIS_STATUS_SUCCESS. Otherwise, it returns an NDIS_STATUS_<i>Xxx</i> error code that is defined in Ndis.h.

</p>

## -remarks
<p>The extensible switch extension calls <i>ReferenceSwitchPort</i> to increment the reference counter for an extensible switch port. While the reference counter has a nonzero value, the protocol edge of the extensible switch will not issue an object identifier (OID) set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598273">OID_SWITCH_PORT_DELETE</a> to delete the extensible switch port. </p>

<p>After the extension calls <i>ReferenceSwitchPort</i>, it must call <a href="netvista.DereferenceSwitchPort">DereferenceSwitchPort</a> to decrement the reference counter.</p>

<p>The extension calls <i>ReferenceSwitchPort</i> after the port has reached the <i>Port created</i> state. The extension must not call <i>ReferenceSwitchPort</i> after the connection has reached the <i>Port tearing down</i> or <i>Port not created</i> states. For more information about these states, see <a href="netvista.hyper_v_extensible_switch_port_and_network_adapter_states">Hyper-V Extensible Switch Port and Network Adapter States</a>.</p>

<p> The extension must call <i>ReferenceSwitchPort</i> when it performs any operation that requires the port to be in an active state. For example, the extension must  call <i>ReferenceSwitchPort</i> before it issues an OID method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598277">OID_SWITCH_PORT_PROPERTY_ENUM</a>.</p>

<p>The extension calls <i>ReferenceSwitchPort</i> after the port has reached the <i>Port created</i> state. The extension must not call <a href="netvista.ReferenceSwitchNic">ReferenceSwitchNic</a> after the port has reached the <i>Port tearing down</i> state. For more information about these states, see <a href="netvista.hyper_v_extensible_switch_port_and_network_adapter_states">Hyper-V Extensible Switch Port and Network Adapter States</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
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
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="netvista.DereferenceSwitchNic">DereferenceSwitchNic</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfgetoptionalswitchhandlers.md">NdisFGetOptionalSwitchHandlers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598273">OID_SWITCH_PORT_DELETE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598277">OID_SWITCH_PORT_PROPERTY_ENUM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598279">OID_SWITCH_PORT_TEARDOWN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_REFERENCE_SWITCH_PORT callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
