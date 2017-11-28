---
UID: NE.ntddstor._STORAGE_DIAGNOSTIC_LEVEL
title: STORAGE_DIAGNOSTIC_LEVEL
author: windows-driver-content
description: The STORAGE_DIAGNOSTIC_LEVEL enumeration specifies the target type of a storage diagnostic.
old-location: storage\storage_diagnostic_level.htm
old-project: storage
ms.assetid: 6D705DA8-7F45-4C7A-813F-5AE4F5A1D8ED
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddstor.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10, version 1709.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_DIAGNOSTIC_LEVEL
req.alt-loc: ntddstor.h
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

# STORAGE_DIAGNOSTIC_LEVEL enumeration



## -description
<p>The <b>STORAGE_DIAGNOSTIC_LEVEL</b> enumeration specifies the target type of a storage diagnostic.</p>


## -syntax

````
typedef enum _STORAGE_DIAGNOSTIC_LEVEL { 
  StorageDiagnosticLevelDefault  = 0,
  StorageDiagnosticLevelMax
} STORAGE_DIAGNOSTIC_LEVEL, *PSTORAGE_DIAGNOSTIC_LEVEL;
````


## -enum-fields
<dl>

### -field <a id="StorageDiagnosticLevelDefault"></a><a id="storagediagnosticleveldefault"></a><a id="STORAGEDIAGNOSTICLEVELDEFAULT"></a><b>StorageDiagnosticLevelDefault</b>

<dd>
<p>Specifies the default diagnostic level.</p>
</dd>

### -field <a id="StorageDiagnosticLevelMax"></a><a id="storagediagnosticlevelmax"></a><a id="STORAGEDIAGNOSTICLEVELMAX"></a><b>StorageDiagnosticLevelMax</b>

<dd>
<p>Specifies the max diagnostic level.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 10, version 1709.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddstor.h</dt>
</dl>
</td>
</tr>
</table>