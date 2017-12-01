---
UID: NS.gnssdriver.PGNSS_DRIVERCOMMAND_PARAM
title: PGNSS_DRIVERCOMMAND_PARAM
author: windows-driver-content
description: This structure is used to send a command to the GNSS driver.
old-location: sensors\gnss_drivercommand_param.htm
old-project: sensors
ms.assetid: EC6EDD7A-B57F-4350-9EB9-56721EAC19BD
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PGNSS_DRIVERCOMMAND_PARAM, GNSS_DRIVERCOMMAND_PARAM, *PGNSS_DRIVERCOMMAND_PARAM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_DRIVERCOMMAND_PARAM
req.alt-loc: gnssdriver.h
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

# PGNSS_DRIVERCOMMAND_PARAM structure



## -description
<p>This structure is used to send a command to the GNSS driver.</p>
<p>The command may involve configuring certain parameters and state variables of the underlying GNSS driver or device, or executing certain defined actions through the driver.</p>


## -syntax

````
typedef struct {
  ULONG                   Size;
  ULONG                   Version;
  GNSS_DRIVERCOMMAND_TYPE CommandType;
  ULONG                   CommandFlag;
  ULONG                   CommandDataSize;
  BYTE                    Unused[512];
  BYTE                    CommandData[ANYSIZE_ARRAY];
} GNSS_DRIVERCOMMAND_PARAM, *PGNSS_DRIVERCOMMAND_PARAM;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Structure size.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Version number.</p>
</dd>

### -field <b>CommandType</b>

<dd>
<p>Identifies the specific command that the driver is required to execute.</p>
<p>This is a well-defined list of GNSS driver commands, as defined by the <a href="..\gnssdriver\ne-gnssdriver-gnss-drivercommand-type.md">GNSS_DRIVERCOMMAND_TYPE</a> enumeration.</p>
</dd>

### -field <b>CommandFlag</b>

<dd>
<p>Bitmask indicating certain aspects of the command.</p>
<p>The flags are defined by the GNSS_DRIVERCOMMAND_FLAG_* macro.</p>
</dd>

### -field <b>CommandDataSize</b>

<dd>
<p>Size of the configuration data being sent to the driver.</p>
</dd>

### -field <b>Unused[512]</b>

<dd>
<p>Padding buffer.</p>
</dd>

### -field <b>CommandData[ANYSIZE_ARRAY]</b>

<dd>
<p>Data associated with the specific command type.</p>
<p>The driver must cast this buffer to the appropriate data type depending on the specific command.</p>
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
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>