---
UID: NE.portcls.PC_REBALANCE_TYPE
title: PC_REBALANCE_TYPE
author: windows-driver-content
description: The PC_REBALANCE_TYPE enum describes the type of support for rebalancing.
old-location: audio\pc_rebalance_type.htm
old-project: audio
ms.assetid: CE700126-8C29-4218-9248-F722523A4DA3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BarcodeSymbologyAttributesData, BarcodeSymbologyAttributesData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PC_REBALANCE_TYPE
req.alt-loc: portcls.h
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

# PC_REBALANCE_TYPE enumeration



## -description
<p>The <code>PC_REBALANCE_TYPE</code> enum describes the type of support for rebalancing.</p>


## -syntax

````
typedef enum _PC_REBALANCE_TYPE { 
  PcRebalanceNotSupported      = 0,
  PcRebalanceRemoveSubdevices  = 
} PC_REBALANCE_TYPE;
````


## -enum-fields
<dl>

### -field PcRebalanceNotSupported 

<dd>
<p>Indicates that PcRebalance is not supported. </p>
</dd>

### -field PcRebalanceRemoveSubdevices

<dd>
<p>Indicates that PcRebalance is supported via unregistering and re-registering the audio subdevices.</p>
</dd>
</dl>

## -remarks
<p> Rebalancing is used in certain PCI scenarios. For example when additional devices are added to the PCI chain and the use of memory resources needs to be rearranged and consolidated.</p>

<p>For more information,  see <a href="https://msdn.microsoft.com/FCAD7F8B-AA9B-430A-BCAF-04E13FA15382">Implement PnP Rebalance for PortCls Audio Drivers</a>.</p>

<p>Available in Windows 10, version 1511 and later versions of Windows. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
</table>