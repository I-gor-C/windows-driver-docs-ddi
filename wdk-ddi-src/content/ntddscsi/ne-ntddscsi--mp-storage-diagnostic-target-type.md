---
UID: NE.ntddscsi._MP_STORAGE_DIAGNOSTIC_TARGET_TYPE
title: MP_STORAGE_DIAGNOSTIC_TARGET_TYPE
author: windows-driver-content
description: The MP_STORAGE_DIAGNOSTIC_TARGET_TYPE enumeration specifies the target type of a storage diagnostic.
old-location: storage\mp_storage_diagnostic_target_type.htm
old-project: storage
ms.assetid: 1A48FC0F-7ED2-4F9F-8B61-A498B0D13FE8
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: RILWRITEPHONEBOOKENTRYPARAMS, RILWRITEPHONEBOOKENTRYPARAMS, *LPRILWRITEPHONEBOOKENTRYPARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddscsi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10, version 1709.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MP_STORAGE_DIAGNOSTIC_TARGET_TYPE
req.alt-loc: ntddscsi.h
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

# MP_STORAGE_DIAGNOSTIC_TARGET_TYPE enumeration



## -description
<p>The <b>MP_STORAGE_DIAGNOSTIC_TARGET_TYPE</b> enumeration specifies the target type of a storage diagnostic.</p>


## -syntax

````
typedef enum _MP_STORAGE_DIAGNOSTIC_TARGET_TYPE { 
  StorageDiagnosticTargetTypeUndefined    = 0,
  StorageDiagnosticTargetTypePort         = 2,
  StorageDiagnosticTargetTypeMiniport,
  StorageDiagnosticTargetTypeHbaFirmware,
  StorageDiagnosticTargetTypeMax
} MP_STORAGE_DIAGNOSTIC_TARGET_TYPE, *PMP_STORAGE_DIAGNOSTIC_TARGET_TYPE;
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
<dt>Ntddscsi.h</dt>
</dl>
</td>
</tr>
</table>