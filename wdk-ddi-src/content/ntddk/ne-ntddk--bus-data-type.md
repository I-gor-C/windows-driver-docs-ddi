---
UID: NE.ntddk._BUS_DATA_TYPE
title: BUS_DATA_TYPE
author: windows-driver-content
description: The BUS_DATA_TYPE enumeration indicates the type of bus configuration space.
old-location: kernel\bus_data_type.htm
old-project: kernel
ms.assetid: a2a2e964-b9ae-4367-85de-f0ebe3c7a952
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FILTER_INITIALIZATION_DATA, FILTER_INITIALIZATION_DATA, *PFILTER_INITIALIZATION_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BUS_DATA_TYPE
req.alt-loc: Ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# BUS_DATA_TYPE enumeration



## -description
<p>The <b>BUS_DATA_TYPE</b> enumeration indicates the type of bus configuration space.</p>


## -syntax

````
typedef enum _BUS_DATA_TYPE { 
  ConfigurationSpaceUndefined  = -1,
  Cmos                         = 0,
  EisaConfiguration            = 1,
  Pos                          = 2,
  CbusConfiguration            = 3,
  PCIConfiguration             = 4,
  VMEConfiguration             = 5,
  NuBusConfiguration           = 6,
  PCMCIAConfiguration          = 7,
  MPIConfiguration             = 8,
  MPSAConfiguration            = 9,
  PNPISAConfiguration          = 10,
  SgiInternalConfiguration     = 11,
  MaximumBusDataType           = 12
} BUS_DATA_TYPE, *PBUS_DATA_TYPE;
````


## -enum-fields
<dl>

### -field <a id="ConfigurationSpaceUndefined"></a><a id="configurationspaceundefined"></a><a id="CONFIGURATIONSPACEUNDEFINED"></a><b>ConfigurationSpaceUndefined</b>

<dd>
<p>Indicates that the type of bus configuration space is undefined.</p>
</dd>

### -field <a id="Cmos"></a><a id="cmos"></a><a id="CMOS"></a><b>Cmos</b>

<dd>
<p>Indicates CMOS data.</p>
</dd>

### -field <a id="EisaConfiguration"></a><a id="eisaconfiguration"></a><a id="EISACONFIGURATION"></a><b>EisaConfiguration</b>

<dd>
<p>Indicates an EISA bus configuration space.</p>
</dd>

### -field <a id="Pos"></a><a id="pos"></a><a id="POS"></a><b>Pos</b>

<dd>
<p>For internal use only.</p>
</dd>

### -field <a id="CbusConfiguration"></a><a id="cbusconfiguration"></a><a id="CBUSCONFIGURATION"></a><b>CbusConfiguration</b>

<dd>
<p>Indicates Cbus configuration space.</p>
</dd>

### -field <a id="PCIConfiguration"></a><a id="pciconfiguration"></a><a id="PCICONFIGURATION"></a><b>PCIConfiguration</b>

<dd>
<p>Indicates PCI configuration space.</p>
</dd>

### -field <a id="VMEConfiguration"></a><a id="vmeconfiguration"></a><a id="VMECONFIGURATION"></a><b>VMEConfiguration</b>

<dd>
<p>Indicates VME configuration space.</p>
</dd>

### -field <a id="NuBusConfiguration"></a><a id="nubusconfiguration"></a><a id="NUBUSCONFIGURATION"></a><b>NuBusConfiguration</b>

<dd>
<p>Indicates NuBus configuration space.</p>
</dd>

### -field <a id="PCMCIAConfiguration"></a><a id="pcmciaconfiguration"></a><a id="PCMCIACONFIGURATION"></a><b>PCMCIAConfiguration</b>

<dd>
<p>Indicates PCMCIA configuration space.</p>
</dd>

### -field <a id="MPIConfiguration"></a><a id="mpiconfiguration"></a><a id="MPICONFIGURATION"></a><b>MPIConfiguration</b>

<dd>
<p>Indicates MPI configuration space.</p>
</dd>

### -field <a id="MPSAConfiguration"></a><a id="mpsaconfiguration"></a><a id="MPSACONFIGURATION"></a><b>MPSAConfiguration</b>

<dd>
<p>Indicates MPSA configuration space.</p>
</dd>

### -field <a id="PNPISAConfiguration"></a><a id="pnpisaconfiguration"></a><a id="PNPISACONFIGURATION"></a><b>PNPISAConfiguration</b>

<dd>
<p>Indicates PNPISA configuration space.</p>
</dd>

### -field <a id="SgiInternalConfiguration"></a><a id="sgiinternalconfiguration"></a><a id="SGIINTERNALCONFIGURATION"></a><b>SgiInternalConfiguration</b>

<dd>
<p>Indicates SGI internal bus configuration space.</p>
</dd>

### -field <a id="MaximumBusDataType"></a><a id="maximumbusdatatype"></a><a id="MAXIMUMBUSDATATYPE"></a><b>MaximumBusDataType</b>

<dd>
<p>Indicates the upper limit of the bus configuration space types.</p>
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
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546599">HalGetBusData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546606">HalGetBusDataByOffset</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546628">HalSetBusData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546633">HalSetBusDataByOffset</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20BUS_DATA_TYPE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
