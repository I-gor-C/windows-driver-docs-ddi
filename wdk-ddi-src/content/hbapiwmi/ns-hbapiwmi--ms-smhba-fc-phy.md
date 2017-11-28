---
UID: NS.hbapiwmi._MS_SMHBA_FC_PHY
title: MS_SMHBA_FC_PHY
author: windows-driver-content
description: The MS_SMHBA_FC_PHY structure is used to report the physical attributes of a fibre channel port.
old-location: storage\ms_smhba_fc_phy.htm
old-project: storage
ms.assetid: 7fb199b6-dcdb-41fc-b1c4-4eef2177018e
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MS_SMHBA_FC_PHY, MS_SMHBA_FC_PHY, *PMS_SMHBA_FC_PHY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MS_SMHBA_FC_PHY
req.alt-loc: hbapiwmi.h
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

# MS_SMHBA_FC_PHY structure



## -description
<p>The MS_SMHBA_FC_PHY structure is used to report the physical attributes of a fibre channel port.</p>


## -syntax

````
typedef struct _MS_SMHBA_FC_PHY {
  ULONG PhySupportSpeed;
  ULONG PhySpeed;
  UCHAR PhyType;
  ULONG MaxFrameSize;
} MS_SMHBA_FC_PHY, *PMS_SMHBA_FC_PHY;
````


## -struct-fields
<dl>

### -field <b>PhySupportSpeed</b>

<dd>
<p>The signaling bit rates at which the port can operate. For a list of the values that this member supports, see PhySpeed.</p>
</dd>

### -field <b>PhySpeed</b>

<dd>
<p>The signaling bit rates at which PortWWN is currently operating. This member must have one of the values in the following table.</p>
<table>
<tr>
<td>
<p><b>Value</b></p>
</td>
<td>
<p><b>Meaning</b></p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSPEED_UNKNOWN</p>
</td>
<td>
<p>Speed unknown. The transceiver is incapable of reporting the speed. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSPEED_1GBIT</p>
</td>
<td>
<p>1 gigabit per sec.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSPEED_2GBIT</p>
</td>
<td>
<p>2 gigabits per sec.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSPEED_10GBIT</p>
</td>
<td>
<p>10 gigabits per sec.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSPEED_4GBIT</p>
</td>
<td>
<p>4 gigabits per sec.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSPEED_NOT_NEGOTIATED</p>
</td>
<td>
<p>The speed at which the port will operate has not yet been established. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>PhyType</b>

<dd>
<p>The port type. This member must have one of the values in the following table.</p>
<table>
<tr>
<td>
<p><b>Value</b></p>
</td>
<td>
<p><b>Meaning</b></p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_UNKNOWN</p>
</td>
<td>
<p>Unknown port type. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_OTHER</p>
</td>
<td>
<p>Value that is not a port type. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_NOTPRESENT</p>
</td>
<td>
<p>Port not present.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_NPORT</p>
</td>
<td>
<p>Fabric. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_NLPORT</p>
</td>
<td>
<p>Public loop.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_FLPORT</p>
</td>
<td>
<p>Fabric on a loop. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_FPORT</p>
</td>
<td>
<p>Fabric port. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_EPORT</p>
</td>
<td>
<p>Fabric expansion port. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_GPORT</p>
</td>
<td>
<p>Generic fabric. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_LPORT</p>
</td>
<td>
<p>Private loop port. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_PTP</p>
</td>
<td>
<p>Point to point. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>MaxFrameSize</b>

<dd>
<p>The maximum frame size, in bytes, that is supported by PortWWN.</p>
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
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>