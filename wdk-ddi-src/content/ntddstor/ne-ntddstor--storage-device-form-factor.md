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

### -field <a id="FormFactorUnknown"></a><a id="formfactorunknown"></a><a id="FORMFACTORUNKNOWN"></a><b>FormFactorUnknown</b>

<dd>
<p>Unknown form factor.</p>
</dd>

### -field <a id="FormFactor3_5"></a><a id="formfactor3_5"></a><a id="FORMFACTOR3_5"></a><b>FormFactor3_5</b>

<dd>
<p>3.5 inch nominal form factor.</p>
</dd>

### -field <a id="FormFactor2_5"></a><a id="formfactor2_5"></a><a id="FORMFACTOR2_5"></a><b>FormFactor2_5</b>

<dd>
<p>2.5 inch nominal form factor.</p>
</dd>

### -field <a id="FormFactor1_8"></a><a id="formfactor1_8"></a><a id="FORMFACTOR1_8"></a><b>FormFactor1_8</b>

<dd>
<p>1.8 inch nominal form factor.</p>
</dd>

### -field <a id="FormFactor1_8Less"></a><a id="formfactor1_8less"></a><a id="FORMFACTOR1_8LESS"></a><b>FormFactor1_8Less</b>

<dd>
<p>Less than 1.8 inch nominal form factor.</p>
</dd>

### -field <a id="FormFactorEmbedded"></a><a id="formfactorembedded"></a><a id="FORMFACTOREMBEDDED"></a><b>FormFactorEmbedded</b>

<dd>
<p>The storage device is embedded on a board.</p>
</dd>

### -field <a id="FormFactorMemoryCard"></a><a id="formfactormemorycard"></a><a id="FORMFACTORMEMORYCARD"></a><b>FormFactorMemoryCard</b>

<dd>
<p>A memory card, such as SmartMedia or CompactFlash.</p>
</dd>

### -field <a id="FormFactormSata"></a><a id="formfactormsata"></a><a id="FORMFACTORMSATA"></a><b>FormFactormSata</b>

<dd>
<p>Mini-SATA (mSATA) form factor.</p>
</dd>

### -field <a id="FormFactorM_2"></a><a id="formfactorm_2"></a><a id="FORMFACTORM_2"></a><b>FormFactorM_2</b>

<dd>
<p>M.2 form factor.</p>
</dd>

### -field <a id="FormFactorPCIeBoard"></a><a id="formfactorpcieboard"></a><a id="FORMFACTORPCIEBOARD"></a><b>FormFactorPCIeBoard</b>

<dd>
<p>PCI Express (PCIe) card form factor.</p>
</dd>

### -field <a id="FormFactorDimm"></a><a id="formfactordimm"></a><a id="FORMFACTORDIMM"></a><b>FormFactorDimm</b>

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