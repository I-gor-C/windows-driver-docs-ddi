---
UID: NS.ucmtypes._UCM_PD_POWER_DATA_OBJECT
title: UCM_PD_POWER_DATA_OBJECT
author: windows-driver-content
description: Describes a Power Data Object. For information about these members, see the Power Delivery specification.
old-location: buses\ucm_pd_power_data_object.htm
old-project: usbref
ms.assetid: C54750A9-EE64-4FE7-9ED6-EC9709A82C43
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCM_PD_POWER_DATA_OBJECT, UCM_PD_POWER_DATA_OBJECT, *PUCM_PD_POWER_DATA_OBJECT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucmtypes.h
req.include-header: Ucmcx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 2.15
req.alt-api: UCM_PD_POWER_DATA_OBJECT
req.alt-loc: ucmtypes.h
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
req.product: Windows 10 or later.
---

# UCM_PD_POWER_DATA_OBJECT structure



## -description
<p>Describes a Power Data Object. For information about these members, see the <a href="http://www.usb.org/developers/docs/usb20_docs/#usb20spec">Power Delivery specification</a>.</p>


## -syntax

````
typedef union _UCM_PD_POWER_DATA_OBJECT {
  Ulong  Ul;
  struct {
    unsigned Reserved  :30;
    unsigned Type  :2;
  } Common;
  struct {
    unsigned MaximumCurrentIn10mA  :10;
    unsigned VoltageIn50mV  :10;
    unsigned PeakCurrent  :2;
    unsigned Reserved  :3;
    unsigned DataRoleSwap  :1;
    unsigned UsbCommunicationCapable  :1;
    unsigned ExternallyPowered  :1;
    unsigned UsbSuspendSupported  :1;
    unsigned DualRolePower  :1;
    unsigned FixedSupply  :2;
  } FixedSupplyPdo;
  struct {
    unsigned MaximumCurrentIn10mA  :10;
    unsigned MinimumVoltageIn50mV  :10;
    unsigned MaximumVoltageIn50mV  :10;
    unsigned VariableSupportNonBattery  :2;
  } VariableSupplyNonBatteryPdo;
  struct {
    unsigned MaximumAllowablePowerIn250mW  :10;
    unsigned MinimumVoltageIn50mV  :10;
    unsigned MaximumVoltageIn50mV  :10;
    unsigned Battery  :2;
  } BatterySupplyPdo;
} UCM_PD_POWER_DATA_OBJECT, *PUCM_PD_POWER_DATA_OBJECT;
````


## -struct-fields
<dl>

### -field <b>Ul</b>

<dd>
<p>Size of the structure.</p>
</dd>

### -field <b>Common</b>

<dd>
<dl>

### -field <b>Reserved</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>Type of Power Data Object.</p>
</dd>
</dl>
</dd>

### -field <b>FixedSupplyPdo</b>

<dd>
<p>Describing a Fixed Supply type Power Data Object.</p>
<dl>

### -field <b>MaximumCurrentIn10mA</b>

<dd>
<p>Maximum current in multiples of 10 mA.</p>
</dd>

### -field <b>VoltageIn50mV</b>

<dd>
<p>Voltage in multiples of 50 mV.</p>
</dd>

### -field <b>PeakCurrent</b>

<dd>
<p>Peak current.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>DataRoleSwap</b>

<dd>
<p>If set, indicates the Power Data Object can perform a data role swap.</p>
</dd>

### -field <b>UsbCommunicationCapable</b>

<dd>
<p>If set, indicates the Power Data Object is USB communication capable. </p>
</dd>

### -field <b>ExternallyPowered</b>

<dd>
<p>If set, indicates the Power Data Object is externally powered.</p>
</dd>

### -field <b>UsbSuspendSupported</b>

<dd>
<p>Indicates support for USB suspend.

</p>
</dd>

### -field <b>DualRolePower</b>

<dd>
<p>Dual role power</p>
</dd>

### -field <b>FixedSupply</b>

<dd>
<p>fixed supply</p>
</dd>
</dl>
</dd>

### -field <b>VariableSupplyNonBatteryPdo</b>

<dd>
<p>Contains bitfields describing a variable-supply non-battery PD object.</p>
<dl>

### -field <b>MaximumCurrentIn10mA</b>

<dd>
<p>Describes the maximum current in multiples of 10 mA.</p>
</dd>

### -field <b>MinimumVoltageIn50mV</b>

<dd>
<p>Desribes the minimum voltage in multiples of 50 mV.</p>
</dd>

### -field <b>MaximumVoltageIn50mV</b>

<dd>
<p>Describes the maximum voltage in multiples of 50 mV.</p>
</dd>

### -field <b>VariableSupportNonBattery</b>

<dd>
<p>Variable Support Non Battery type.</p>
</dd>
</dl>
</dd>

### -field <b>BatterySupplyPdo</b>

<dd>
<p>Contains bitfields describing a battery supply PD object.</p>
<dl>

### -field <b>MaximumAllowablePowerIn250mW</b>

<dd>
<p>Describes the maximum allowable power in multiples of 250 mW.</p>
</dd>

### -field <b>MinimumVoltageIn50mV</b>

<dd>
<p>Describes the minimum voltage in multiples of 50 mV.</p>
</dd>

### -field <b>MaximumVoltageIn50mV</b>

<dd>
<p>Describes the maximum voltage in multiples of 50 mV.</p>
</dd>

### -field <b>Battery</b>

<dd>
<p>Battery type.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ucmtypes.h (include Ucmcx.h)</dt>
</dl>
</td>
</tr>
</table>