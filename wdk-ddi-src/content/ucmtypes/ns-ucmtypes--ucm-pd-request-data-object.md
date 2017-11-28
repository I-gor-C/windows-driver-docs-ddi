---
UID: NS.ucmtypes._UCM_PD_REQUEST_DATA_OBJECT
title: UCM_PD_REQUEST_DATA_OBJECT
author: windows-driver-content
description: Describes a Request Data Object (RDO). For information about these members, see the Power Delivery specification.
old-location: buses\ucm_pd_request_data_object.htm
old-project: usbref
ms.assetid: 2F5CC46B-3BFC-4C69-A9C8-C4BC4864E84B
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCM_PD_REQUEST_DATA_OBJECT, UCM_PD_REQUEST_DATA_OBJECT, *PUCM_PD_REQUEST_DATA_OBJECT
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
req.alt-api: UCM_PD_REQUEST_DATA_OBJECT
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

# UCM_PD_REQUEST_DATA_OBJECT structure



## -description
<p>Describes a Request Data Object (RDO). For information about these members, see the <a href="http://www.usb.org/developers/docs/usb20_docs/#usb20spec">Power Delivery specification</a>.</p>


## -syntax

````
typedef union _UCM_PD_REQUEST_DATA_OBJECT {
  Ulong  Ul;
  struct {
    unsigned Reserved1  :28;
    unsigned ObjectPosition  :3;
    unsigned Reserved2  :1;
  } Common;
  struct {
    unsigned MaximumOperatingCurrentIn10mA  :10;
    unsigned OperatingCurrentIn10mA  :10;
    unsigned Reserved1  :4;
    unsigned NoUsbSuspend  :1;
    unsigned UsbCommunicationCapable  :1;
    unsigned CapabilityMismatch  :1;
    unsigned GiveBackFlag  :1;
    unsigned ObjectPosition  :3;
    unsigned Reserved2  :1;
  } FixedAndVariableRdo;
  struct {
    unsigned MaximumOperatingPowerIn250mW  :10;
    unsigned OperatingPowerIn250mW  :10;
    unsigned Reserved1  :4;
    unsigned NoUsbSuspend  :1;
    unsigned UsbCommunicationCapable  :1;
    unsigned CapabilityMismatch  :1;
    unsigned GiveBackFlag  :1;
    unsigned ObjectPosition  :3;
    unsigned Reserved2  :1;
  } BatteryRdo;
} UCM_PD_REQUEST_DATA_OBJECT, *PUCM_PD_REQUEST_DATA_OBJECT;
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

### -field <b>Reserved1</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>ObjectPosition</b>

<dd>
<p>Object position.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field <b>FixedAndVariableRdo</b>

<dd>
<dl>

### -field <b>MaximumOperatingCurrentIn10mA</b>

<dd>
<p>Maximum current in 10 mA units.</p>
</dd>

### -field <b>OperatingCurrentIn10mA</b>

<dd>
<p>Operating current in 10mA units.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>NoUsbSuspend</b>

<dd>
<p>Indicates support for USB suspend.

</p>
</dd>

### -field <b>UsbCommunicationCapable</b>

<dd>
<p>USB communication capable. </p>
</dd>

### -field <b>CapabilityMismatch</b>

<dd>
<p>Capability Mismatch </p>
</dd>

### -field <b>GiveBackFlag</b>

<dd>
<p>GiveBack Flag.</p>
</dd>

### -field <b>ObjectPosition</b>

<dd>
<p>Object Position.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>
</dd>

### -field <b>BatteryRdo</b>

<dd>
<dl>

### -field <b>MaximumOperatingPowerIn250mW</b>

<dd>
<p>Maximum Operating Power in 250mW units. </p>
</dd>

### -field <b>OperatingPowerIn250mW</b>

<dd>
<p>Operating Power in 250mW units.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>NoUsbSuspend</b>

<dd>
<p> USB Suspend. </p>
</dd>

### -field <b>UsbCommunicationCapable</b>

<dd>
<p>USB Communications Capable.</p>
</dd>

### -field <b>CapabilityMismatch</b>

<dd>
<p>Capability Mismatch. </p>
</dd>

### -field <b>GiveBackFlag</b>

<dd>
<p>GiveBack Flag. </p>
</dd>

### -field <b>ObjectPosition</b>

<dd>
<p>Object Position.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved.</p>
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