---
UID: NC.ndis.NDIS_SWITCH_REFERENCE_SWITCH_NIC
title: NDIS_SWITCH_REFERENCE_SWITCH_NIC
author: windows-driver-content
description: The ReferenceSwitchNic function increments the Hyper-V extensible switch reference counter for a network adapter that is connected to an extensible switch port.
old-location: netvista\ReferenceSwitchNic.htm
ms.assetid: 8F4C76FA-A386-4A3D-8C9F-3CFF69382702
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ReferenceSwitchNic
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
ms.keywords: RxNameCacheInitialize
req.iface: 
---

# NDIS_SWITCH_REFERENCE_SWITCH_NIC callback



## -description
<p>
<p>The <i>ReferenceSwitchNic</i> function increments the Hyper-V extensible switch reference counter for a network adapter that is connected to an extensible switch port.</p>
</p>
<p>The <i>ReferenceSwitchNic</i> function increments the Hyper-V extensible switch reference counter for a network adapter that is connected to an extensible switch port.</p>


## -prototype

````
NDIS_SWITCH_REFERENCE_SWITCH_NIC ReferenceSwitchNic;

NDIS_STATUS ReferenceSwitchNic(
  _In_ NDIS_SWITCH_CONTEXT   NdisSwitchContext,
  _In_ NDIS_SWITCH_PORT_ID   SwitchPortId,
  _In_ NDIS_SWITCH_NIC_INDEX SwitchNicIndex
)
{ ... }
````


## -parameters
<dl>

### -param <i>NdisSwitchContext</i> [in]

<dd>
<p>An NDIS_SWITCH_CONTEXT value that contains the handle of the extensible switch module to which the Hyper-V extensible switch extension is attached. When the  extension calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh598204">NdisFGetOptionalSwitchHandlers</a>,  this handle is returned through the <i>NdisSwitchContext</i> parameter.</p>
</dd>

### -param <i>SwitchPortId</i> [in]

<dd>
<p>An NDIS_SWITCH_PORT_ID value that contains the unique identifier of the extensible switch port  to which the virtual network adapter is connected.</p>
</dd>

### -param <i>SwitchNicIndex</i> [in]

<dd>
<p>An NDIS_SWITCH_NIC_INDEX value that specifies the index of the virtual network adapter for which the extensible switch reference counter is to be incremented.</p>
<p>For more information on NDIS_SWITCH_NIC_INDEX values, see <a href="NULL">Network Adapter Index Values</a>.</p>
<div class="alert"><b>Note</b>  This parameter must specify the index value of a network adapter that is in a connected state. Index values for network adapters that are in a created or disconnected state cannot be specified. For more information about network connection states, see <a href="NULL">Hyper-V Extensible Switch Port and Network Adapter States</a>.</div>
<div> </div>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns NDIS_STATUS_SUCCESS. Otherwise, it returns an NDIS_STATUS_<i>Xxx</i> error code that is defined in Ndis.h.

</p>

## -remarks
<p>The extensible switch extension calls <i>ReferenceSwitchNic</i> to increment a reference counter for a network adapter that is connected to an extensible switch port. While the reference counter has a nonzero value, the protocol edge of the extensible switch will not issue an object identifier (OID) set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598264">OID_SWITCH_NIC_DELETE</a> to delete the connection to the adapter. </p>

<p>After the extension calls <i>ReferenceSwitchNic</i>, it must call <a href="netvista.DereferenceSwitchNic">DereferenceSwitchNic</a> to decrement the extensible switch reference counter. </p>

<p>The extension  should call <i>ReferenceSwitchNic</i> before it performs the following operations:</p>

<p>Forwards an <a href="https://msdn.microsoft.com/library/windows/hardware/hh598266">OID_SWITCH_NIC_REQUEST</a> OID request over the extensible switch control path to an underlying physical network adapter. 
</p>

<p>For more information, see <a href="NULL">Managing OID Requests to Physical Network Adapters</a>.</p>

<p>Forwards an <a href="https://msdn.microsoft.com/library/windows/hardware/hh598205">NDIS_STATUS_SWITCH_NIC_STATUS</a> status indication over the extensible switch control path from an underlying external adapter.</p>

<p>For more information, see <a href="NULL">Managing NDIS Status Indications from Physical Network Adapters</a>.</p>

<p>The extension calls <i>ReferenceSwitchNic</i> after the network adapter connection has reached the <i>Network adapter connection created</i> state. The extension must not call <i>ReferenceSwitchNic</i> after the connection has reached the <i>Network adapter disconnected</i> or <i>Network adapter deleted</i> states. For more information about these states, see <a href="NULL">Hyper-V Extensible Switch Port and Network Adapter States</a>.</p>

<p>The extensible switch extension calls <i>ReferenceSwitchNic</i> to increment a reference counter for a network adapter that is connected to an extensible switch port. While the reference counter has a nonzero value, the protocol edge of the extensible switch will not issue an object identifier (OID) set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598264">OID_SWITCH_NIC_DELETE</a> to delete the connection to the adapter. </p>

<p>After the extension calls <i>ReferenceSwitchNic</i>, it must call <a href="netvista.DereferenceSwitchNic">DereferenceSwitchNic</a> to decrement the extensible switch reference counter. </p>

<p>The extension  should call <i>ReferenceSwitchNic</i> before it performs the following operations:</p>

<p>Forwards an <a href="https://msdn.microsoft.com/library/windows/hardware/hh598266">OID_SWITCH_NIC_REQUEST</a> OID request over the extensible switch control path to an underlying physical network adapter. 
</p>

<p>For more information, see <a href="NULL">Managing OID Requests to Physical Network Adapters</a>.</p>

<p>Forwards an <a href="https://msdn.microsoft.com/library/windows/hardware/hh598205">NDIS_STATUS_SWITCH_NIC_STATUS</a> status indication over the extensible switch control path from an underlying external adapter.</p>

<p>For more information, see <a href="NULL">Managing NDIS Status Indications from Physical Network Adapters</a>.</p>

<p>The extension calls <i>ReferenceSwitchNic</i> after the network adapter connection has reached the <i>Network adapter connection created</i> state. The extension must not call <i>ReferenceSwitchNic</i> after the connection has reached the <i>Network adapter disconnected</i> or <i>Network adapter deleted</i> states. For more information about these states, see <a href="NULL">Hyper-V Extensible Switch Port and Network Adapter States</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598205">NDIS_STATUS_SWITCH_NIC_STATUS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598204">NdisFGetOptionalSwitchHandlers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598264">OID_SWITCH_NIC_DELETE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598265">OID_SWITCH_NIC_DISCONNECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598266">OID_SWITCH_NIC_REQUEST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_REFERENCE_SWITCH_NIC callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
