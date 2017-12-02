---
UID: NS.ndis._NET_PNP_EVENT
title: NET_PNP_EVENT
author: windows-driver-content
description: The NET_PNP_EVENT structure describes a network Plug and Play (PnP) event, an NDIS PnP event, or a power management event.
old-location: netvista\net_pnp_event.htm
old-project: netvista
ms.assetid: b68fb279-c1d4-4f0b-8b04-b17a01a65560
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NET_PNP_EVENT, NET_PNP_EVENT, *PNET_PNP_EVENT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 5.1, and NDIS 6.0 and later. For more information about the NDIS 5.1 version of this structure, see    NET_PNP_EVENT (NDIS 5.1).
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NET_PNP_EVENT
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

# NET_PNP_EVENT structure



## -description
<p>The <b>NET_PNP_EVENT</b> structure describes a network Plug and Play (PnP) event, an NDIS PnP event, or a
  power management event.</p>


## -syntax

````
typedef struct _NET_PNP_EVENT {
  NET_PNP_EVENT_CODE NetEvent;
  PVOID              Buffer;
  ULONG              BufferLength;
  ULONG_PTR          NdisReserved[4];
  ULONG_PTR          TransportReserved[4];
  ULONG_PTR          TdiReserved[4];
  ULONG_PTR          TdiClientReserved[4];
} NET_PNP_EVENT, *PNET_PNP_EVENT;
````


## -struct-fields
<dl>

### -field NetEvent

<dd>
<p>An event code that describes the event as one of the following:
     </p>
<p></p>
<dl>

### -field NetEventSetPower

<dd>
<p>Indicates that the power manager has sent a Set Power request, which specifies a transition to a
       system power state. NDIS translates this state to an appropriate device power state for the
       device.</p>
<p>For more information, see the Remarks section.</p>
</dd>

### -field NetEventQueryPower

<dd>
<p>Indicates that the power manager has sent a Query Power request, which requests a transition to
       a system power state. NDIS translates this state to an appropriate device power state for the
       device.</p>
<p>For more information, see the Remarks section.</p>
</dd>

### -field NetEventQueryRemoveDevice

<dd>
<p>Indicates that the PnP Manager has sent a Query Remove Device request. The PnP Manager sends
       this request to query whether a device can be removed without disrupting operations.</p>
</dd>

### -field NetEventCancelRemoveDevice

<dd>
<p>Indicates that the PnP Manager has sent a Cancel Remove Device request. The PnP Manager sends
       this request to cancel the removal of a device after the PnP Manager sends a Query Remove Device request.</p>
</dd>

### -field NetEventReconfigure

<dd>
<p>Indicates that the configuration has changed for a network component. For example, if a user,
       through the Network and Dial-up Connections folder, changes the IP address for TCP/IP, NDIS indicates
       the 
       <b>NetEventReconfigure</b> event to the TCP/IP protocol. Also, an intermediate driver typically uses
       this event as a trigger to call the 
       <a href="..\ndis\nf-ndis-ndisiminitializedeviceinstanceex.md">
       NdisIMInitializeDeviceInstanceEx</a> function and start its virtual miniports. For more information
       about 
       <b>NetEventReconfigure</b>, see 
       NetEventIMReEnableDevice.</p>
</dd>

### -field NetEventBindList

<dd>
<p>Indicates to a protocol driver that its bind list processing order has been reconfigured. This
       list indicates a relative order that applies to bindings when processing, for example, a user request
       that might be routed to one of several bindings. The buffer that is passed with this event contains a
       list of device names that are formatted as null-terminated Unicode strings. The format of each device
       name is identical to the 
       <b>AdapterName</b> member that is passed to a call to the 
       <a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a> function.</p>
</dd>

### -field NetEventBindsComplete

<dd>
<p>Indicates that a protocol driver has bound to all the NICs that it can bind to. NDIS will not
       indicate any more NICs to the protocol unless a PnP NIC is plugged into the system.</p>
</dd>

### -field NetEventPnPCapabilities

<dd>
<p>Indicates that the user enabled or disabled the wake-up capabilities of the underlying adapter.
       (The binding is specified by the 
       <i>ProtocolBindingContext</i> parameter that is passed to the 
       <a href="..\ndis\nc-ndis-protocol-net-pnp-event.md">
       ProtocolNetPnPEvent</a> function.)</p>
</dd>

### -field NetEventPause

<dd>
<p>Indicates that the specified protocol binding should enter the 
       Pausing state. The binding will enter the 
       Paused state after NDIS has completed all the outstanding send requests for the
       binding.</p>
</dd>

### -field NetEventRestart

<dd>
<p>Indicates that the specified protocol binding has entered the 
       Restarting state. After the protocol driver is ready to resume send and receive operations for
       the binding, the binding enters the 
       Running state.</p>
</dd>

### -field NetEventPortActivation

<dd>
<p>Indicates the activation of a list of ports that are associated with the specified
       binding.</p>
</dd>

### -field NetEventPortDeactivation

<dd>
<p>Indicates the deactivation of a list of ports that are associated with the specified
       binding.</p>
</dd>

### -field NetEventIMReEnableDevice

<dd>
<p>Indicates that the configuration has changed for a virtual miniport of an NDIS 6.0 or later
       intermediate driver. 
       <b>NetEventIMReEnableDevice</b> is similar to the 
       <b>NetEventReconfigure</b> event except that the intermediate driver receives this event for a single
       virtual miniport and the 
       <b>NetEventReconfigure</b> event applies to all the intermediate driver's virtual miniports. For
       example, an intermediate driver receives the 
       <b>NetEventIMReEnableDevice</b> event when a user disables and then enables a single virtual miniport
       from the Device Manager or another source. For examples of intermediate driver power management, see the 
    <a href="http://go.microsoft.com/fwlink/p/?LinkId=617916">NDIS MUX Intermediate Driver and Notify Object</a> driver sample available in the <a href="http://go.microsoft.com/fwlink/p/?LinkId=616507">Windows driver samples</a> repository on GitHub.</p>
</dd>

### -field NetEventNDKEnable

<dd>
<p>Indicates that Network Direct Kernel (NDK) is currently enabled.</p>
</dd>

### -field NetEventNDKDisable

<dd>
<p>Indicates that NDK is currently disabled.</p>
</dd>

### -field NetEventFilterPreDetach

<dd>
<p>Indicates that a filter is about to be detached, so that the filter can perform any necessary cleanup that isn't possible in the <a href="..\ndis\nc-ndis-filter-detach.md">FilterDetach</a> handler (because the OID and indication paths are closed at that time).</p>
</dd>

### -field NetEventBindFailed

<dd>
<p>Indicates that a binding event failure has occurred.</p>
</dd>

### -field NetEventSwitchActivate

<dd>
<p>Indicates that the Hyper-V Extensible Switch has completed activation, and switch extensions can now safely query for further switch configuration. The indication is only used in the Hyper-V Extensible Switch stack, issued by the extension miniport. See <a href="netvista.querying_the_hyper_v_extensible_switch_configuration">Querying the Hyper-V Extensible Switch Configuration</a> and <a href="..\fwpsk\ns-fwpsk--ndis-switch-parameters.md">NDIS_SWITCH_PARAMETERS</a> for more details. </p>
</dd>

### -field NetEventInhibitBindsAbove

<dd>
<p>A synchronous event that prevents other filters and protocols from binding to the miniport adapter. Any filters or protocols that were previously bound will be unbound before the event completes. The usage rules are below.</p>
<ul>
<li>Avoid leaving the miniport adapter in the inhibit state, for longer than 1000 milliseconds.</li>
<li>This event can only be issued after <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> begins and must not be issued after <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> returns.</li>
<li>This event can only be issued when the miniport adapter is in a D0 state.</li>
<li>Because this event is blocking, it should not be issued by any context that would cause a deadlock.</li>
<li>Locks must not be held while issuing this event.</li>
<li>This event must be issued at PASSIVE_LEVEL.</li>
</ul>
<p>This event is available starting with NDIS version 6.50
and must be used with V2 or later version of <b>NET_PNP_EVENT</b>. This event can optionally be issued by a miniport driver. Protocols and filters cannot receive this event or issue it.</p>
</dd>

### -field NetEventAllowBindsAbove

<dd>
<p>An asynchronous event that reverses the effects of NetEventInhibitBindsAbove. The usage rules are below.</p>
<ul>
<li>This event can only be issued after <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> begins and must not be issued after <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> returns.</li>
<li>This event can only be issued when the miniport adapter is in a D0 state.</li>
<li>Locks must not be held while issuing this event.</li>
<li>This event must be issued at PASSIVE_LEVEL.</li>
</ul>
<p>This event is available starting with NDIS version 6.50 and must be used with V2 or later version of <b>NET_PNP_EVENT</b>. This event can optionally be issued by a miniport driver. Protocols and filters cannot receive this event or issue it.</p>
</dd>

### -field NetEventRequirePause

<dd>
<p>A synchronous event that indicates the protocols and filters including the miniport adapter must be paused. The protocols and filters and the miniport adapter are guaranteed to be paused when the <a href="..\ndis\nf-ndis-ndismnetpnpevent.md">NdisMNetPnPEvent</a> routine returns. The usage rules are below.</p>
<ul>
<li>Avoid delaying between NetEventAllowStart and NetEventRequirePause events for longer than 1000 milliseconds to prevent delay in user applications.</li>
<li>This event can only be issued after <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> begins and must not be issued after <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> returns.</li>
<li>There is no guarantee that NDIS will call <a href="..\ndis\nc-ndis-miniport-pause.md">MiniportPause</a> after this event is issued. In particular, if your miniport adapter is already paused, NDIS won't introduce an extra start-pause loop. This means that the amount of times <i>MiniportPause</i> called is not greater than, less than, or equal to the amount this event is issued.</li>
<li>Because this event is blocking, it should not be issued by any context that would cause a deadlock.</li>
<li>Locks must not be held while issuing this event.</li>
</ul>
<p>This event is available starting with NDIS version 6.50 and must be used with V2 or later version of <b>NET_PNP_EVENT</b>. This event can optionally be issued by a miniport driver. Protocols and filters cannot receive this event or issue it.</p>
</dd>

### -field NetEventAllowStart

<dd>
<p>An asynchronous event that indicates the protocols and filters including the miniport adapter does not need to be paused. The usage rules are below. There is no guaranteed pause state for any driver in the protocols and filters after the <a href="..\ndis\nf-ndis-ndismnetpnpevent.md">NdisMNetPnPEvent</a> routine returns. </p>
<ul>
<li>This event can only be issued after <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> begins and must not be issued after <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> returns.</li>
<li>Because this event is blocking, it should not be issued by any context that would cause a deadlock.</li>
<li>Locks must not be held while issuing this event.</li>
</ul>
<p>This event is available starting with NDIS version 6.50 and must be used with V2 or later version of <b>NET_PNP_EVENT</b>. This event can optionally be issued by a miniport driver. Protocols and filters cannot receive this event or issue it.</p>
</dd>
</dl>
</dd>

### -field Buffer

<dd>
<p>The address of a buffer that contains information that is specific to the event indicated in the 
     <b>NetEvent</b> member. For each type of event, the buffer contains the following information:
     </p>
<p></p>
<dl>

### -field NetEventSetPower

<dd>
<p>The buffer contains the device power state to which the device is transitioning.
       </p>
<p>When NDIS calls a protocol driver's 
       <a href="..\ndis\nc-ndis-protocol-net-pnp-event.md">ProtocolNetPnPEvent</a> function,
       the device state is NDIS_DEVICE_POWER_STATE, which can be one of the following values:</p>
<p></p>
<dl>

### -field NdisDeviceStateUnspecified

<dd>
<p>The network device does not support power management.</p>
</dd>

### -field NdisDeviceStateD0

<dd>
<p>The fully powered state, in which the device delivers full functionality and
         performance.</p>
</dd>

### -field NdisDeviceStateD1

<dd>
<p>A low-power state, in which transmit requests from the host are not honored by the device,
         data received by the device is not transferred to host memory, and no interrupts can occur. Some
         device context may be lost. Depending on the capabilities of the NIC and its miniport driver, the
         device might be able to generate a wake-up signal.</p>
</dd>

### -field NdisDeviceStateD2

<dd>
<p>A low-power state that is similar to 
         <b>NdisDeviceStateD1</b>, except that more power and less context are typically saved and more time
         is required to transition to the fully powered state.</p>
</dd>

### -field NdisDeviceStateD3

<dd>
<p>The off state, in which power has been fully removed from the device.</p>
</dd>
</dl>
<p>For protocol drivers, 
       <b>NdisDeviceStateD0</b> means that the NIC is fully powered and is available for normal operations.
       Any other device state means that the device is not fully powered and is not available for sending and
       receiving network data.</p>
</dd>

### -field NetEventQueryPower

<dd>
<p>The buffer contains the device power state that is requested for the device. The device state is
       NDIS_DEVICE_POWER_STATE (which is described in the 
       <b>NetEventSetPower</b> value description).</p>
</dd>

### -field NetEventQueryRemoveDevice

<dd>
<p>The buffer contents are <b>NULL</b>.</p>
</dd>

### -field NetEventCancelRemoveDevice

<dd>
<p>The buffer contents are <b>NULL</b>.</p>
</dd>

### -field NetEventReconfigure

<dd>
<p>The buffer can contain protocol-specific data. The protocol driver is responsible for validating
       this data.</p>
</dd>

### -field NetEventBindList

<dd>
<p>The buffer contains a revised binding list for the network component that the 
       <a href="..\ndis\ns-ndis--net-pnp-event-notification.md">
       NET_PNP_EVENT_NOTIFICATION</a> structure is being passed to. The bind list, which is a series of
       null-terminated Unicode strings, has a REG_MULTI_SZ format. Each of the strings is an adapter name.
       TDI clients that are bound to a protocol use this bind list to reorder their bindings. The protocol
       driver is responsible for validating this list.</p>
</dd>

### -field NetEventBindsComplete

<dd>
<p>The buffer contents are <b>NULL</b>.</p>
</dd>

### -field NetEventPnPCapabilities

<dd>
<p>The buffer is a ULONG that contains a bitmask. When the NDIS_DEVICE_WAKE_UP_ENABLE flag is set
       in the bitmask, the wake-up capabilities of the NIC are enabled. Otherwise, the NIC's wake-up
       capabilities are disabled. (The binding is specified by the 
       <i>ProtocolBindingContext</i> parameter that is passed to 
       <a href="..\ndis\nc-ndis-protocol-net-pnp-event.md">ProtocolNetPnPEvent</a>.) When set
       to zero, this flag indicates that the NIC's wake-up capabilities are disabled.</p>
</dd>

### -field NetEventPause

<dd>
<p>The buffer contains an 
       <a href="..\ndis\ns-ndis--ndis-protocol-pause-parameters.md">
       NDIS_PROTOCOL_PAUSE_PARAMETERS</a> structure.</p>
</dd>

### -field NetEventRestart

<dd>
<p>The buffer might contain NULL or an 
       <a href="..\ndis\ns-ndis--ndis-protocol-restart-parameters.md">
       NDIS_PROTOCOL_RESTART_PARAMETERS</a> structure. NDIS provides a pointer to an 
       <a href="..\ndis\ns-ndis--ndis-restart-attributes.md">NDIS_RESTART_ATTRIBUTES</a> structure
       in the 
       <b>RestartAttributes</b> member of the NDIS_PROTOCOL_RESTART_PARAMETERS structure. </p>
<div class="alert"><b>Note</b>  If the buffer is NULL, the restart attributes have not changed since the previous restart.</div>
<div> </div>
</dd>

### -field NetEventPortActivation

<dd>
<p>The buffer contains the first entry in a list of 
       <a href="..\ntddndis\ns-ntddndis--ndis-port.md">NDIS_PORT</a> structures that identify the ports
       that NDIS will activate. You can use the 
       <b>Next</b> member of the NDIS_PORT structure to get the next structure in the list.</p>
</dd>

### -field NetEventPortDeactivation

<dd>
<p>The buffer contains an array of port numbers, of type NDIS_PORT_NUMBER (defined as ULONG), that
       identify the NDIS ports that NDIS will deactivate. To calculate the number of elements in the array,
       divide the value of the 
       <b>BufferLength</b> member, which is in the <b>NET_PNP_EVENT</b> structure that is specified in the 
       <b>NetPnPEvent</b> member of 
       <a href="..\ndis\ns-ndis--net-pnp-event-notification.md">NET_PNP_EVENT_NOTIFICATION</a>,
       by 
       sizeof(NDIS_PORT_NUMBER).</p>
</dd>

### -field NetEventIMReEnableDevice

<dd>
<p>The buffer contains a pointer to a variable of type NDIS_STRING that contains a null-terminated
       Unicode string that names the device object of a virtual miniport for the device that is being
       enabled. The string is a full path name—for example, 
       \Device\<i>DeviceName</i>.</p>
</dd>

### -field NetEventNDKEnable

<dd>
<p>The <b>Buffer</b> member is <b>NULL</b>.</p>
</dd>

### -field NetEventNDKDisable

<dd>
<p>The <b>Buffer</b> member is <b>NULL</b>.</p>
</dd>

### -field NetEventFilterPreDetach

<dd>
<p>The <b>Buffer</b> member is <b>NULL</b>.</p>
</dd>

### -field NetEventBindFailed

<dd>
<p>The buffer contains an <a href="..\ndis\ns-ndis--ndis-bind-failed-notification.md">NDIS_BIND_FAILED_NOTIFICATION</a> structure.</p>
</dd>

### -field NetEventSwitchActivate

<dd>
<p>The buffer contents are NULL.</p>
</dd>

### -field NetEventAllowBindsAbove

<dd>
<p>The buffer contents are NULL.</p>
</dd>

### -field NetEventInhibitBindsAbove

<dd>
<p>The buffer contents are NULL.</p>
</dd>

### -field NetEventAllowStart

<dd>
<p>The buffer contents are NULL.</p>
</dd>

### -field NetEventRequirePause

<dd>
<p>The buffer contents are NULL.</p>
</dd>
</dl>
</dd>

### -field BufferLength

<dd>
<p>The number of bytes of event-specific information at 
     <b>Buffer</b>.</p>
</dd>

### -field NdisReserved

<dd>
<p>An area reserved for used by NDIS.</p>
</dd>

### -field TransportReserved

<dd>
<p>An area reserved for used by the transport driver.</p>
</dd>

### -field TdiReserved

<dd>
<p>An area reserved for used by TDI.</p>
</dd>

### -field TdiClientReserved

<dd>
<p>An area reserved for used by a TDI client.</p>
</dd>
</dl>

## -remarks
<p>In NDIS 6.0 and later versions, when the operating system issues a system PnP event or a power
    management event to a target device object that represents a miniport adapter, NDIS translates the event
    into a 
    <a href="..\ndis\ns-ndis--net-pnp-event-notification.md">
    NET_PNP_EVENT_NOTIFICATION</a> structure. The 
    <b>NetPnPEvent</b> member of the <b>NET_PNP_EVENT_NOTIFICATION</b> structure is a <b>NET_PNP_EVENT</b> structure.</p>

<p>NDIS passes a pointer to the <b>NET_PNP_EVENT</b> structure to each protocol driver that is bound to the
    miniport adapter by calling the protocol driver's 
    <a href="..\ndis\nc-ndis-protocol-net-pnp-event.md">ProtocolNetPnPEvent</a> function. The
    protocol driver should save this pointer, because the pointer is an input parameter to the 
    <a href="..\ndis\nf-ndis-ndiscompletenetpnpevent.md">NdisCompleteNetPnPEvent</a> function,
    which the driver calls to complete the call to 
    <i>ProtocolNetPnPEvent</i> asynchronously.</p>

<p>NDIS passes a pointer to the <b>NET_PNP_EVENT</b> structure to each filter driver that is bound to the
    miniport adapter by calling the filter driver's 
    <a href="..\ndis\nc-ndis-filter-net-pnp-event.md">FilterNetPnPEvent</a> function. The
    filter driver does not have to save this pointer because the driver must complete the call to 
    <i>FilterNetPnPEvent</i> synchronously.</p>

<p>Starting with NDIS 6.30, the  protocol or filter driver must follow these guidelines when NDIS calls the <a href="..\ndis\nc-ndis-protocol-net-pnp-event.md">ProtocolNetPnPEvent</a> or <a href="..\ndis\nc-ndis-filter-net-pnp-event.md">FilterNetPnPEvent</a> functions:</p>

<p>If the <b>NetEvent</b> member of the <b>NET_PNP_EVENT</b> structure is set to <b>NetEventSetPower</b>, the driver must stop generating new I/O requests. Also, the driver must not wait for the completion of any pending I/O requests.</p>

<p>After the protocol or filter driver  returns from <a href="..\ndis\nc-ndis-protocol-net-pnp-event.md">ProtocolNetPnPEvent</a> or <a href="..\ndis\nc-ndis-filter-net-pnp-event.md">FilterNetPnPEvent</a>, NDIS will not pause and restart these drivers during power-state transitions if the following conditions are true:</p>

<p>The underlying miniport driver sets the <b>NDIS_MINIPORT_ATTRIBUTES_NO_PAUSE_ON_SUSPEND</b> flag in the <a href="..\ndis\ns-ndis--ndis-miniport-adapter-registration-attributes.md">NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES</a> structure. The driver passes a pointer to this structure in its call to the <a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">NdisMSetMiniportAttributes</a> function.
</p>

<p>All filter drivers that are attached to the miniport driver support NDIS 6.30 or later versions of NDIS.</p>

<p>All protocol drivers that are bound to the miniport driver support NDIS 6.30 or later versions of NDIS.</p>

<p>If the <b>NetEvent</b> member of the <b>NET_PNP_EVENT</b> structure is set to <b>NetEventSetPower</b> or <b>NetEventQueryPower</b>, the driver must not wait for the completion of any pending I/O requests.</p>

<p>The 
    <b>NetEvent</b> member in the <b>NET_PNP_EVENT</b> structure identifies the type of Plug and Play or power
    management event. The 
    <b>Buffer</b> contains information that is specific to the type of event.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 5.1, and NDIS 6.0 and later. For more information about the NDIS 5.1 version of this structure, see 
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff559141">NET_PNP_EVENT (NDIS 5.1)</a>.</p>
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
<a href="..\ndis\nc-ndis-filter-net-pnp-event.md">FilterNetPnPEvent</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-bind-failed-notification.md">NDIS_BIND_FAILED_NOTIFICATION</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-port.md">NDIS_PORT</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-protocol-pause-parameters.md">
   NDIS_PROTOCOL_PAUSE_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-protocol-restart-parameters.md">
   NDIS_PROTOCOL_RESTART_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-restart-attributes.md">NDIS_RESTART_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\fwpsk\ns-fwpsk--ndis-switch-parameters.md">NDIS_SWITCH_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscompletenetpnpevent.md">NdisCompleteNetPnPEvent</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisiminitializedeviceinstanceex.md">
   NdisIMInitializeDeviceInstanceEx</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-pnp-event-notification.md">NET_PNP_EVENT_NOTIFICATION</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-net-pnp-event.md">ProtocolNetPnPEvent</a>
</dt>
<dt>
<a href="netvista.querying_the_hyper_v_extensible_switch_configuration">Querying the Hyper-V Extensible Switch Configuration</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NET_PNP_EVENT structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
