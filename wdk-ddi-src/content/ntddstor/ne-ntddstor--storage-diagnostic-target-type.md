---
UID: NE.ntddstor._STORAGE_DIAGNOSTIC_TARGET_TYPE
title: STORAGE_DIAGNOSTIC_TARGET_TYPE
author: windows-driver-content
description: The STORAGE_DIAGNOSTIC_TARGET_TYPE enumeration specifies the target type of a storage diagnostic.
old-location: storage\storage_diagnostic_target_type.htm
ms.assetid: 8BC338FB-7C76-49D3-96E5-0F20C4A250CE
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddstor.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10, version 1709.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_DIAGNOSTIC_TARGET_TYPE
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
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
req.iface: 
---

# STORAGE_DIAGNOSTIC_TARGET_TYPE enumeration



## -description
<p>The <b>STORAGE_DIAGNOSTIC_TARGET_TYPE</b> enumeration specifies the target type of a storage diagnostic.</p>


## -syntax

````
typedef enum _STORAGE_DIAGNOSTIC_TARGET_TYPE { 
  StorageDiagnosticTargetTypeUndefined    = 0,
  StorageDiagnosticTargetTypePort,
  StorageDiagnosticTargetTypeMiniport,
  StorageDiagnosticTargetTypeHbaFirmware,
  StorageDiagnosticTargetTypeMax
} STORAGE_DIAGNOSTIC_TARGET_TYPE, *PSTORAGE_DIAGNOSTIC_TARGET_TYPE;
````


## -enum-fields
<dl>

### -field <a id="StorageDiagnosticTargetTypeUndefined"></a><a id="storagediagnostictargettypeundefined"></a><a id="STORAGEDIAGNOSTICTARGETTYPEUNDEFINED"></a><b>StorageDiagnosticTargetTypeUndefined</b>

<dd>
<p>Specifies the target type is undefined.</p>
</dd>

### -field <a id="StorageDiagnosticTargetTypePort"></a><a id="storagediagnostictargettypeport"></a><a id="STORAGEDIAGNOSTICTARGETTYPEPORT"></a><b>StorageDiagnosticTargetTypePort</b>

<dd>
<p>Specifies the target type is a port driver.</p>
</dd>

### -field <a id="StorageDiagnosticTargetTypeMiniport"></a><a id="storagediagnostictargettypeminiport"></a><a id="STORAGEDIAGNOSTICTARGETTYPEMINIPORT"></a><b>StorageDiagnosticTargetTypeMiniport</b>

<dd>
<p>Specifies the target type is a Miniport driver.</p>
</dd>

### -field <a id="StorageDiagnosticTargetTypeHbaFirmware"></a><a id="storagediagnostictargettypehbafirmware"></a><a id="STORAGEDIAGNOSTICTARGETTYPEHBAFIRMWARE"></a><b>StorageDiagnosticTargetTypeHbaFirmware</b>

<dd>
<p>Specifies the target type is a Hba Firmware driver.</p>
</dd>

### -field <a id="StorageDiagnosticTargetTypeMax"></a><a id="storagediagnostictargettypemax"></a><a id="STORAGEDIAGNOSTICTARGETTYPEMAX"></a><b>StorageDiagnosticTargetTypeMax</b>

<dd>
<p>Specifies the target type is a Max driver.</p>
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