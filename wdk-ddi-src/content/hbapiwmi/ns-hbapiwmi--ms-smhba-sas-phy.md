---
UID: NS.hbapiwmi._MS_SMHBA_SAS_PHY
title: MS_SMHBA_SAS_PHY
author: windows-driver-content
description: The MS_SMHBA_SAS_PHY structure is used to report the SAS physical port information.
old-location: storage\ms_smhba_sas_phy.htm
old-project: storage
ms.assetid: 9bbf2f63-4479-47ee-a014-78b13deccb4c
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MS_SMHBA_SAS_PHY, MS_SMHBA_SAS_PHY, *PMS_SMHBA_SAS_PHY
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
req.alt-api: MS_SMHBA_SAS_PHY
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

# MS_SMHBA_SAS_PHY structure



## -description
<p>The MS_SMHBA_SAS_PHY structure is used to report the SAS physical port information.</p>


## -syntax

````
typedef struct _MS_SMHBA_SAS_PHY {
  UCHAR PhyIdentifier;
  ULONG NegotiatedLinkRate;
  ULONG ProgrammedMinLinkRate;
  ULONG HardwareMinLinkRate;
  ULONG ProgrammedMaxLinkRate;
  ULONG HardwareMaxLinkRate;
  UCHAR domainPortWWN[8];
} MS_SMHBA_SAS_PHY, *PMS_SMHBA_SAS_PHY;
````


## -struct-fields
<dl>

### -field <b>PhyIdentifier</b>

<dd>
<p>The port whose physical configuration and link information is being returned. It is unique within the context of the SAS device that contains the physical port.</p>
</dd>

### -field <b>NegotiatedLinkRate</b>

<dd>
<p>The state or the transmission speed that is negotiated by the physical port for the physical link.</p>
</dd>

### -field <b>ProgrammedMinLinkRate</b>

<dd>
<p>The minimum physical link rate that is set by the physical port control mechanism.</p>
</dd>

### -field <b>HardwareMinLinkRate</b>

<dd>
<p>The minimum physical link rate that is supported by the physical port.</p>
</dd>

### -field <b>ProgrammedMaxLinkRate</b>

<dd>
<p>The maximum physical link rate that is set by the physical port control mechanism.</p>
</dd>

### -field <b>HardwareMaxLinkRate</b>

<dd>
<p>The maximum physical link rate that is supported by the physical port.</p>
</dd>

### -field <b>domainPortWWN</b>

<dd>
<p>The Port_Identifier that has the smallest value of any Port_Identifier of an expander SMP.</p>
</dd>
</dl>

## -remarks
<p>Link rates are defined in hpaapi.h as HBA_SASSPEED_1_5GBIT and HBA_SASSPEED_3GBIT.</p>

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