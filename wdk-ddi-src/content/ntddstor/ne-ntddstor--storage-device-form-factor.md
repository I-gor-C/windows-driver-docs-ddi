---
UID: NE.ntddstor._STORAGE_DEVICE_FORM_FACTOR
title: STORAGE_DEVICE_FORM_FACTOR
author: windows-driver-content
description: Indicates the form factor of a storage device.
old-location: storage\storage_device_form_factor.htm
old-project: storage
ms.assetid: EE59767B-2504-4E5F-A442-60EEBEE70B59
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_DEVICE_FORM_FACTOR
req.alt-loc: Ntddstor.h
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

# STORAGE_DEVICE_FORM_FACTOR enumeration



## -description
<p>Indicates the form factor of a storage device.</p>


## -syntax

````
typedef enum _STORAGE_DEVICE_FORM_FACTOR { 
  FormFactorUnknown     = 0, // 0x0
  FormFactor3_5,
  FormFactor2_5,
  FormFactor1_8,
  FormFactor1_8Less,
  FormFactorEmbedded,
  FormFactorMemoryCard,
  FormFactormSata,
  FormFactorM_2,
  FormFactorPCIeBoard,
  FormFactorDimm
} STORAGE_DEVICE_FORM_FACTOR, *PSTORAGE_DEVICE_FORM_FACTOR;
````


## -enum-fields
<dl>

### -field FormFactorUnknown

<dd>
<p>Unknown form factor.</p>
</dd>

### -field FormFactor3_5

<dd>
<p>3.5 inch nominal form factor.</p>
</dd>

### -field FormFactor2_5

<dd>
<p>2.5 inch nominal form factor.</p>
</dd>

### -field FormFactor1_8

<dd>
<p>1.8 inch nominal form factor.</p>
</dd>

### -field FormFactor1_8Less

<dd>
<p>Less than 1.8 inch nominal form factor.</p>
</dd>

### -field FormFactorEmbedded

<dd>
<p>The storage device is embedded on a board.</p>
</dd>

### -field FormFactorMemoryCard

<dd>
<p>A memory card, such as SmartMedia or CompactFlash.</p>
</dd>

### -field FormFactormSata

<dd>
<p>Mini-SATA (mSATA) form factor.</p>
</dd>

### -field FormFactorM_2

<dd>
<p>M.2 form factor.</p>
</dd>

### -field FormFactorPCIeBoard

<dd>
<p>PCI Express (PCIe) card form factor.</p>
</dd>

### -field FormFactorDimm

<dd>
<p>Dual in-line memory module (DIMM) slot form factor.</p>
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
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>