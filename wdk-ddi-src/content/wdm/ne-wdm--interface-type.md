---
UID: NE.wdm._INTERFACE_TYPE
title: INTERFACE_TYPE
author: windows-driver-content
description: The INTERFACE_TYPE enumeration indicates the bus type.
old-location: kernel\interface_type.htm
old-project: kernel
ms.assetid: 4d20f3fd-d06e-420b-af69-9ef34addc611
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: INTERFACE_TYPE
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# INTERFACE_TYPE enumeration



## -description
<p>The <b>INTERFACE_TYPE</b> enumeration indicates the bus type. </p>


## -syntax

````
typedef enum _INTERFACE_TYPE { 
  InterfaceTypeUndefined  = -1,
  Internal,
  Isa,
  Eisa,
  MicroChannel,
  TurboChannel,
  PCIBus,
  VMEBus,
  NuBus,
  PCMCIABus,
  CBus,
  MPIBus,
  MPSABus,
  ProcessorInternal,
  InternalPowerBus,
  PNPISABus,
  PNPBus,
  Vmcs,
  ACPIBus,
  MaximumInterfaceType
} INTERFACE_TYPE, *PINTERFACE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="InterfaceTypeUndefined"></a><a id="interfacetypeundefined"></a><a id="INTERFACETYPEUNDEFINED"></a><b>InterfaceTypeUndefined</b>

<dd>
<p>Indicates that the interface type is undefined. </p>
</dd>

### -field <a id="Internal"></a><a id="internal"></a><a id="INTERNAL"></a><b>Internal</b>

<dd>
<p>For internal use only. </p>
</dd>

### -field <a id="Isa"></a><a id="isa"></a><a id="ISA"></a><b>Isa</b>

<dd>
<p>Indicates that the interface is published by the ISA bus driver. </p>
</dd>

### -field <a id="Eisa"></a><a id="eisa"></a><a id="EISA"></a><b>Eisa</b>

<dd>
<p>Indicates that the interface is published by the EISA bus driver. </p>
</dd>

### -field <a id="MicroChannel"></a><a id="microchannel"></a><a id="MICROCHANNEL"></a><b>MicroChannel</b>

<dd>
<p>Indicates that the interface is published by the MicroChannel bus driver.</p>
</dd>

### -field <a id="TurboChannel"></a><a id="turbochannel"></a><a id="TURBOCHANNEL"></a><b>TurboChannel</b>

<dd>
<p>Indicates that the interface is published by the TurboChannel bus driver.</p>
</dd>

### -field <a id="PCIBus"></a><a id="pcibus"></a><a id="PCIBUS"></a><b>PCIBus</b>

<dd>
<p>Indicates that the interface is published by the PCI bus driver.</p>
</dd>

### -field <a id="VMEBus"></a><a id="vmebus"></a><a id="VMEBUS"></a><b>VMEBus</b>

<dd>
<p>Indicates that the interface is published by the VME bus driver.</p>
</dd>

### -field <a id="NuBus"></a><a id="nubus"></a><a id="NUBUS"></a><b>NuBus</b>

<dd>
<p>Indicates that the interface is published by the NuBus driver.</p>
</dd>

### -field <a id="PCMCIABus"></a><a id="pcmciabus"></a><a id="PCMCIABUS"></a><b>PCMCIABus</b>

<dd>
<p>Indicates that the interface is published by the PCMCIA bus driver.</p>
</dd>

### -field <a id="CBus"></a><a id="cbus"></a><a id="CBUS"></a><b>CBus</b>

<dd>
<p>Indicates that the interface is published by the Cbus driver.</p>
</dd>

### -field <a id="MPIBus"></a><a id="mpibus"></a><a id="MPIBUS"></a><b>MPIBus</b>

<dd>
<p>Indicates that the interface is published by the MPI bus driver.</p>
</dd>

### -field <a id="MPSABus"></a><a id="mpsabus"></a><a id="MPSABUS"></a><b>MPSABus</b>

<dd>
<p>Indicates that the interface is published by the MPSA bus driver.</p>
</dd>

### -field <a id="ProcessorInternal"></a><a id="processorinternal"></a><a id="PROCESSORINTERNAL"></a><b>ProcessorInternal</b>

<dd>
<p>Indicates that the interface is published by the ISA bus driver.</p>
</dd>

### -field <a id="InternalPowerBus"></a><a id="internalpowerbus"></a><a id="INTERNALPOWERBUS"></a><b>InternalPowerBus</b>

<dd>
<p>Indicates that the interface is published for an internal power bus. Some devices have power control ports that allow them to share power control with other devices. The Windows architecture represents these devices as slots on a virtual bus called an "internal power bus." </p>
</dd>

### -field <a id="PNPISABus"></a><a id="pnpisabus"></a><a id="PNPISABUS"></a><b>PNPISABus</b>

<dd>
<p>Indicates that the interface is published by the PNPISA bus driver.</p>
</dd>

### -field <a id="PNPBus"></a><a id="pnpbus"></a><a id="PNPBUS"></a><b>PNPBus</b>

<dd>
<p>Indicates that the interface is published by the PNP bus driver.</p>
</dd>

### -field <a id="Vmcs"></a><a id="vmcs"></a><a id="VMCS"></a><b>Vmcs</b>

<dd>
<p>Reserved for use by the operating system.</p>
</dd>

### -field <a id="ACPIBus"></a><a id="acpibus"></a><a id="ACPIBUS"></a><b>ACPIBus</b>

<dd>
<p>Indicates that the interface is published by the ACPI bus driver. The ACPI bus driver enumerates devices that are described in the ACPI firmware of the hardware platform. These devices might physically reside on buses that are controlled by other bus drivers, but the ACPI bus driver must enumerate these devices because the other bus drivers cannot detect them. This interface type is defined starting with Windows 8.</p>
</dd>

### -field <a id="MaximumInterfaceType"></a><a id="maximuminterfacetype"></a><a id="MAXIMUMINTERFACETYPE"></a><b>MaximumInterfaceType</b>

<dd>
<p>Marks the upper limit of the possible bus types.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.hw_initialization_data__scsi_">HW_INITIALIZATION_DATA</a>
</dt>
<dt>
<a href="storage.port_configuration_information__scsi_">PORT_CONFIGURATION_INFORMATION</a>
</dt>
<dt>
<a href="..\srb\nf-srb-scsiportgetdevicebase.md">ScsiPortGetDeviceBase</a>
</dt>
<dt>
<a href="..\srb\nf-srb-scsiportvalidaterange.md">ScsiPortValidateRange</a>
</dt>
<dt>
<a href="..\storport\nf-storport-storportgetdevicebase.md">StorPortGetDeviceBase</a>
</dt>
<dt>
<a href="..\storport\nf-storport-storportvalidaterange.md">StorPortValidateRange</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20INTERFACE_TYPE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
