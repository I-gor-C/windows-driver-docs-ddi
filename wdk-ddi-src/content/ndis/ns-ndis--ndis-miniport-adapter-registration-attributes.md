---
UID: NS.ndis._NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES
title: NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES
author: windows-driver-content
description: An NDIS miniport driver sets up an NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES structure to define registration attributes that are associated with a miniport adapter.
old-location: netvista\ndis_miniport_adapter_registration_attributes.htm
old-project: netvista
ms.assetid: 8f0d539a-50c5-4ecd-b62d-6b32fe7cfaba
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES, NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES, *PNDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES
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
req.alt-api: NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES
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

# NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES structure



## -description
<p>An NDIS miniport driver sets up an <b>NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES</b> structure to define
  registration attributes that are associated with a miniport adapter.</p>


## -syntax

````
typedef struct _NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES {
  NDIS_OBJECT_HEADER  Header;
  NDIS_HANDLE         MiniportAdapterContext;
  ULONG               AttributeFlags;
  UINT                CheckForHangTimeInSeconds;
  NDIS_INTERFACE_TYPE InterfaceType;
} NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES, *PNDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES. To specify the version of the <b>NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to one of the following values: </p>
<p></p>
<dl>

### -field <a id="NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES_REVISION_2"></a><a id="ndis_miniport_adapter_registration_attributes_revision_2"></a>NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES_REVISION_2

<dd>
<p>Added <b>AttributeFlags</b> flags for NDIS 6.30.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES_REVISION_2.</p>
</dd>

### -field <a id="NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES_REVISION_1"></a><a id="ndis_miniport_adapter_registration_attributes_revision_1"></a>NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES_REVISION_1

<dd>
<p>Original version for NDIS 6.0.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>MiniportAdapterContext</b>

<dd>
<p>A handle to a context area that the miniport driver allocated in its 
     <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function.
     The miniport driver uses this context area to maintain state information for a miniport adapter.</p>
</dd>

### -field <b>AttributeFlags</b>

<dd>
<p>A bitmask of flags that are combined with a bitwise OR. NDIS miniport drivers should set one or more of
     the following flags: 
     </p>
<p></p>
<dl>

### -field <a id="NDIS_MINIPORT_ATTRIBUTES_HARDWARE_DEVICE"></a><a id="ndis_miniport_attributes_hardware_device"></a>NDIS_MINIPORT_ATTRIBUTES_HARDWARE_DEVICE

<dd>
<p>Set if the miniport driver directly controls a physical device. The physical device is assigned
       hardware resources such as interrupts, I/O ports, memory-mapped I/O, or DMA channels that the miniport
       driver should claim from the 
       <a href="..\ndis\nc-ndis-miniport-initialize.md">
       MiniportInitializeEx</a> function.</p>
</dd>

### -field <a id="NDIS_MINIPORT_ATTRIBUTES_NDIS_WDM"></a><a id="ndis_miniport_attributes_ndis_wdm"></a>NDIS_MINIPORT_ATTRIBUTES_NDIS_WDM

<dd>
<p>Set if the lower-level interface of the miniport adapter is a WDM bus driver such as USB or IEEE
       1394. In this case, the miniport driver does not allocate hardware resources such as I/O ports,
       interrupts, memory-mapped I/O, or DMA channels. Instead, the driver communicates with the device
       through the underlying bus driver's WDM interface.</p>
</dd>

### -field <a id="NDIS_MINIPORT_ATTRIBUTES_BUS_MASTER"></a><a id="ndis_miniport_attributes_bus_master"></a>NDIS_MINIPORT_ATTRIBUTES_BUS_MASTER

<dd>
<p>Set if the caller's NIC is a bus-master DMA device.</p>
</dd>

### -field <a id="NDIS_MINIPORT_ATTRIBUTES_NO_HALT_ON_SUSPEND"></a><a id="ndis_miniport_attributes_no_halt_on_suspend"></a>NDIS_MINIPORT_ATTRIBUTES_NO_HALT_ON_SUSPEND

<dd>
<p>Set if NDIS should not call a miniport driver's 
       <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> function before the
       system transitions to a low-power (sleeping) state. Drivers that rely on hardware-maintained state
       should not set this flag.</p>
</dd>

### -field <a id="NDIS_MINIPORT_ATTRIBUTES_SURPRISE_REMOVE_OK"></a><a id="ndis_miniport_attributes_surprise_remove_ok"></a>NDIS_MINIPORT_ATTRIBUTES_SURPRISE_REMOVE_OK

<dd>
<p>Set if the miniport driver can handle removal of its NIC without user notification. NDIS drivers receive
       surprise removal notifications at the 
       <a href="..\ndis\nc-ndis-miniport-device-pnp-event-notify.md">
       MiniportDevicePnPEventNotify</a> function.</p>
</dd>

### -field <a id="NDIS_MINIPORT_ATTRIBUTES_NOT_CO_NDIS"></a><a id="ndis_miniport_attributes_not_co_ndis"></a>NDIS_MINIPORT_ATTRIBUTES_NOT_CO_NDIS

<dd>
<p>Set by a miniport driver that can support both connection-oriented and connectionless devices to indicate
       that the device is a connectionless device.</p>
</dd>

### -field <a id="NDIS_MINIPORT_ATTRIBUTES_DO_NOT_BIND_TO_ALL_CO"></a><a id="ndis_miniport_attributes_do_not_bind_to_all_co"></a>NDIS_MINIPORT_ATTRIBUTES_DO_NOT_BIND_TO_ALL_CO

<dd>
<p>Set by a CoNDIS miniport driver that does not provide TAPI services. Setting
       NDIS_MINIPORT_ATTRIBUTES_DO_NOT_BIND_TO_ALL_CO prevents NDIS from binding the miniport driver to the
       NDIS TAPI proxy driver (NDPROXY). By default, NDIS binds NDPROXY to all CoNDIS miniport
       drivers.</p>
</dd>

### -field <a id="NDIS_MINIPORT_ATTRIBUTES_CONTROLS_DEFAULT_PORT"></a><a id="ndis_miniport_attributes_controls_default_port"></a>NDIS_MINIPORT_ATTRIBUTES_CONTROLS_DEFAULT_PORT

<dd>
<p>Set by a miniport driver that calls the 
       <a href="..\ndis\nf-ndis-ndismnetpnpevent.md">NdisMNetPnPEvent</a> function to activate
       its default port. If NDIS_MINIPORT_ATTRIBUTES_CONTROLS_DEFAULT_PORT is not set, the default port is
       active. NDIS does not bind protocol drivers or attach filter modules to a miniport adapter if its
       default port is not active.</p>
</dd>

### -field <a id="NDIS_MINIPORT_ATTRIBUTES_NO_PAUSE_ON_SUSPEND"></a><a id="ndis_miniport_attributes_no_pause_on_suspend"></a>NDIS_MINIPORT_ATTRIBUTES_NO_PAUSE_ON_SUSPEND

<dd>
<p>Starting with NDIS 6.30, this flag is set if the miniport driver  is able to transition to a low-power state without being paused. </p>
<p>For more information about this flag, see the Remarks section.</p>
</dd>

### -field <a id="NDIS_MINIPORT_ATTRIBUTES_REGISTER_BUGCHECK_CALLBACK"></a><a id="ndis_miniport_attributes_register_bugcheck_callback"></a>NDIS_MINIPORT_ATTRIBUTES_REGISTER_BUGCHECK_CALLBACK

<dd>
<p>Starting with NDIS 6.30 miniports, NDIS will not invoke the miniport's MiniportShutdownEx handler during a BugCheck unless this flag is set.  Most miniports should not set this flag. </p>
</dd>
</dl>
</dd>

### -field <b>CheckForHangTimeInSeconds</b>

<dd>
<p>The time-out interval, in seconds, at which NDIS should call the 
     <a href="..\ndis\nc-ndis-miniport-check-for-hang.md">
     MiniportCheckForHangEx</a> function. If a miniport driver has not responded to an OID request or a send request
     within two successive calls to 
     <i>MiniportCheckForHangEx</i>, NDIS can call the miniport driver's 
     <a href="..\ndis\nc-ndis-miniport-reset.md">MiniportResetEx</a> function.
     </p>
<p>The  interval that NDIS uses when calling 
     <i>MiniportCheckForHangEx</i> is always a multiple of 2 seconds. For example, if you specify 5
     seconds, the interval will be approximately 4 seconds.</p>
<p>If this member is 0, the default time-out interval is 2 seconds.</p>
<div class="alert"><b>Note</b>  The time-out interval must be greater than your miniport driver's initialization time. For more information, see <a href="NULL">Miniport Adapter Check-for-Hang and Reset Operations</a>.</div>
<div> </div>
</dd>

### -field <b>InterfaceType</b>

<dd>
<p>The I/O bus interface type of the miniport adapter. This is usually the type of I/O bus on which
     the miniport adapter is connected. The following values are supported in NDIS 6.0: 
     </p>
<p></p>
<dl>

### -field <a id="NdisInterfaceInternal"></a><a id="ndisinterfaceinternal"></a><a id="NDISINTERFACEINTERNAL"></a><b>NdisInterfaceInternal</b>

<dd>
<p>Specifies a host-specific internal interface.</p>
</dd>

### -field <a id="NdisInterfaceIsa"></a><a id="ndisinterfaceisa"></a><a id="NDISINTERFACEISA"></a><b>NdisInterfaceIsa</b>

<dd>
<p>Specifies the ISA interface.</p>
</dd>

### -field <a id="NdisInterfaceEisa"></a><a id="ndisinterfaceeisa"></a><a id="NDISINTERFACEEISA"></a><b>NdisInterfaceEisa</b>

<dd>
<p>Specifies the extended ISA (EISA) interface. This interface type is not supported in NDIS 6.0
       and later versions.</p>
</dd>

### -field <a id="NdisInterfaceMca"></a><a id="ndisinterfacemca"></a><a id="NDISINTERFACEMCA"></a><b>NdisInterfaceMca</b>

<dd>
<p>Refers to the MCA bus, which is no longer supported. This interface type is not supported in
       NDIS 6.0 and later versions.</p>
</dd>

### -field <a id="NdisInterfaceTurboChannel"></a><a id="ndisinterfaceturbochannel"></a><a id="NDISINTERFACETURBOCHANNEL"></a><b>NdisInterfaceTurboChannel</b>

<dd>
<p>Specifies the Turbo Channel interface.</p>
</dd>

### -field <a id="NdisInterfacePci"></a><a id="ndisinterfacepci"></a><a id="NDISINTERFACEPCI"></a><b>NdisInterfacePci</b>

<dd>
<p>Specifies the Peripheral Component Interconnect (PCI) interface.</p>
</dd>

### -field <a id="NdisInterfacePcMcia"></a><a id="ndisinterfacepcmcia"></a><a id="NDISINTERFACEPCMCIA"></a><b>NdisInterfacePcMcia</b>

<dd>
<p>Specifies the Personal Computer Memory Card International Association (PC Card)
       interface.</p>
</dd>

### -field <a id="NdisInterfaceCBus"></a><a id="ndisinterfacecbus"></a><a id="NDISINTERFACECBUS"></a><b>NdisInterfaceCBus</b>

<dd>
<p>Specifies the CBus.</p>
</dd>

### -field <a id="NdisInterfaceMPIBus"></a><a id="ndisinterfacempibus"></a><a id="NDISINTERFACEMPIBUS"></a><b>NdisInterfaceMPIBus</b>

<dd>
<p>Specifies the MPIBus.</p>
</dd>

### -field <a id="NdisInterfaceMPSABus"></a><a id="ndisinterfacempsabus"></a><a id="NDISINTERFACEMPSABUS"></a><b>NdisInterfaceMPSABus</b>

<dd>
<p>Specifies the MPSABus.</p>
</dd>

### -field <a id="NdisInterfaceProcessorInternal"></a><a id="ndisinterfaceprocessorinternal"></a><a id="NDISINTERFACEPROCESSORINTERNAL"></a><b>NdisInterfaceProcessorInternal</b>

<dd>
<p>Specifies the processor internal bus.</p>
</dd>

### -field <a id="NdisInterfaceInternalPowerBus"></a><a id="ndisinterfaceinternalpowerbus"></a><a id="NDISINTERFACEINTERNALPOWERBUS"></a><b>NdisInterfaceInternalPowerBus</b>

<dd>
<p>Specifies the internal power bus.</p>
</dd>

### -field <a id="NdisInterfacePNPISABus"></a><a id="ndisinterfacepnpisabus"></a><a id="NDISINTERFACEPNPISABUS"></a><b>NdisInterfacePNPISABus</b>

<dd>
<p>Specifies the PNPISABus.</p>
</dd>

### -field <a id="NdisInterfacePNPBus"></a><a id="ndisinterfacepnpbus"></a><a id="NDISINTERFACEPNPBUS"></a><b>NdisInterfacePNPBus</b>

<dd>
<p>Specifies the PNPBus.</p>
</dd>
</dl>
<p>This parameter is irrelevant for intermediate drivers, which should specify 0 for this
     member.</p>
</dd>
</dl>

## -remarks
<p>A miniport driver passes a pointer to an NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES structure in
    the 
    <i>MiniportAttributes</i> parameter of the 
    <a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">
    NdisMSetMiniportAttributes</a> function. A miniport driver calls 
    <b>NdisMSetMiniportAttributes</b> from its 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function
    during initialization.</p>

<p>Miniport drivers should set the attributes in NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES as soon as
    possible within 
    <i>MiniportInitializeEx</i>. Setting these attributes is mandatory.</p>

<p>NDIS issues an OID  request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569780">OID_PNP_SET_POWER</a> to the miniport driver before the underlying miniport adapter is transitioned to a low power state of D1, D2, or D3. When the driver handles this OID, it must prepare the miniport adapter for the transition to the lower power state and must not wait for the completion of pending receive packet indications.</p>

<p>In some cases, before NDIS issues the OID request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569780">OID_PNP_SET_POWER</a> to the miniport driver, NDIS calls the miniport driver's <a href="..\ndis\nc-ndis-miniport-pause.md">MiniportPause</a> function as described below:</p>

<p>If the <b>NDIS_MINIPORT_ATTRIBUTES_NO_PAUSE_ON_SUSPEND</b> flag is not set, NDIS   calls the miniport driver's <a href="..\ndis\nc-ndis-miniport-pause.md">MiniportPause</a> function before the OID  request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569780">OID_PNP_SET_POWER</a> is issued to the driver. Within the context of the <i>MiniportPause</i> call, the driver must wait for the completion of pending receive packet indications.</p>

<p>If the <b>NDIS_MINIPORT_ATTRIBUTES_NO_PAUSE_ON_SUSPEND</b> flag is  set, NDIS does not call the miniport driver's <a href="..\ndis\nc-ndis-miniport-pause.md">MiniportPause</a> function before the OID  request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569780">OID_PNP_SET_POWER</a> is issued to the driver.  When the miniport driver  handles the OID request, it must not assume that it had been previously paused when preparing the miniport adapter for the transition to a low-power state.</p>

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
<a href="..\ndis\nc-ndis-miniport-check-for-hang.md">MiniportCheckForHangEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-device-pnp-event-notify.md">
   MiniportDevicePnPEventNotify</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-pause.md">MiniportPause</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-reset.md">MiniportResetEx</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismnetpnpevent.md">NdisMNetPnPEvent</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">NdisMSetMiniportAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569780">OID_PNP_SET_POWER</a>
</dt>
<dt>
<a href="NULL">Miniport Adapter Check-for-Hang and Reset Operations</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
