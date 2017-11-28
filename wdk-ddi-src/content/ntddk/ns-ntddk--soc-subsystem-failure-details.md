---
UID: NS.ntddk._SOC_SUBSYSTEM_FAILURE_DETAILS
title: SOC_SUBSYSTEM_FAILURE_DETAILS
author: windows-driver-content
description: The SOC_SUBSYSTEM_FAILURE_DETAILS structure holds information related to a System on a Chip (SoC) bug code.
old-location: whea\soc_subsystem_failure_details.htm
old-project: whea
ms.assetid: 416F9A0C-0A86-4FAA-9052-5D37D29C464D
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: SOC_SUBSYSTEM_FAILURE_DETAILS, SOC_SUBSYSTEM_FAILURE_DETAILS, *PSOC_SUBSYSTEM_FAILURE_DETAILS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SOC_SUBSYSTEM_FAILURE_DETAILS
req.alt-loc: ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# SOC_SUBSYSTEM_FAILURE_DETAILS structure



## -description
<p>The   <b>SOC_SUBSYSTEM_FAILURE_DETAILS</b> structure holds information related to a System on a Chip (SoC) bug code.</p>
<p>These bug codes store information in a 
  this structure.</p>


## -syntax

````
typedef struct _SOC_SUBSYSTEM_FAILURE_DETAILS {
  SOC_SUBSYSTEM_TYPE SubsysType;
  ULONG64            FirmwareVersion;
  ULONG64            HardwareVersion;
  ULONG              UnifiedFailureRegionSize;
  CHAR               UnifiedFailureRegion[1];
} SOC_SUBSYSTEM_FAILURE_DETAILS, *PSOC_SUBSYSTEM_FAILURE_DETAILS;
````


## -struct-fields
<dl>

### -field <b>SubsysType</b>

<dd>
<p>A value in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn376405">SOC_SYBSYSTEM_TYPE</a> enumeration or a vendor-defined subsystem type. Subsystem types in the range 0x10000 through 0x80000000 are reserved for independent hardware vendors. </p>
</dd>

### -field <b>FirmwareVersion</b>

<dd>
<p>A vendor-defined SoC firmware version number.</p>
</dd>

### -field <b>HardwareVersion</b>

<dd>
<p>A  vendor-defined SoC hardware version number.</p>
</dd>

### -field <b>UnifiedFailureRegionSize</b>

<dd>
<p>The size, in bytes, of the <b>UnifiedFailureRegion</b> string including the <b>NULL</b> terminator.</p>
</dd>

### -field <b>UnifiedFailureRegion</b>

<dd>
<p>A null-terminated string, defined by the vendor, that  contains classification details about the error that occurred.</p>
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
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h</dt>
</dl>
</td>
</tr>
</table>