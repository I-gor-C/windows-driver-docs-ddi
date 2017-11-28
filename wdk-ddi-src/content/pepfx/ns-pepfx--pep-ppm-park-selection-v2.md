---
UID: NS.pepfx._PEP_PPM_PARK_SELECTION_V2
title: PEP_PPM_PARK_SELECTION_V2
author: windows-driver-content
description: The PEP_PPM_PARK_SELECTION_V2 structure indicates the preferences of the operating system and platform extension plug-in (PEP) regarding which processors in the platform should be parked to reduce power consumption.
old-location: kernel\pep_ppm_park_selection_v2.htm
old-project: kernel
ms.assetid: D1EFB30D-E8E2-4585-AB0E-B7903F4D6656
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PEP_PPM_PARK_SELECTION_V2, PEP_PPM_PARK_SELECTION_V2, *PPEP_PPM_PARK_SELECTION_V2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_PPM_PARK_SELECTION_V2
req.alt-loc: pepfx.h
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

# PEP_PPM_PARK_SELECTION_V2 structure



## -description
<p>The <b>PEP_PPM_PARK_SELECTION_V2</b> structure indicates the preferences of the operating system and platform extension plug-in (PEP) regarding which processors in the platform should be parked to reduce power consumption.</p>


## -syntax

````
typedef struct _PEP_PPM_PARK_SELECTION_V2 {
  ULONG                                                   AdditionalUnparkedProcessors;
  ULONG                                                   Count;
  _Field_size_full_(Count) PPEP_PROCESSOR_PARK_PREFERENCE Processors;
  ULONGLONG                                               EvaluationTime;
  UCHAR                                                   EvaluationType;
} PEP_PPM_PARK_SELECTION_V2, *PPEP_PPM_PARK_SELECTION_V2;
````


## -struct-fields
<dl>

### -field <b>AdditionalUnparkedProcessors</b>

<dd>
<p>[in] The number of additional processors that need to be unparked.</p>
<p>This number includes all processors in the <b>Processors</b> array for which the PEP sets <b>PepPreference</b> to PROCESSOR_PARK_PREFERENCE_PARKED but the operating system sets <b>PoPreference</b> to either PROCESSOR_PARK_PREFERENCE_UNPARKED or PROCESSOR_PARK_PREFERENCE_NONE. For more information about these values, see <a href="https://msdn.microsoft.com/library/windows/hardware/mt186837">PEP_PROCESSOR_PARK_PREFERENCE</a>.</p>
<p>This number does not include processors in the <b>Processors</b> array for which the operating system sets the <b>PoPreference</b> value to PROCESSOR_PARK_PREFERENCE_PARKED.</p>
</dd>

### -field <b>Count</b>

<dd>
<p>[in] The number of elements in the array pointed to by the <b>Processors</b> member.</p>
</dd>

### -field <b>Processors</b>

<dd>
<p>[in/out] A pointer to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/mt186837">PEP_PROCESSOR_PARK_PREFERENCE</a> structures. Each array element indicates the parking preferences for a particular processor. The <b>Count</b> member specifies the number of elements in the array.</p>
</dd>

### -field <b>EvaluationTime</b>

<dd>
<p>The interrupt time of the performance check evaluation that initiated this notification.</p>
</dd>

### -field <b>EvaluationType</b>

<dd>
<p>The type of evaluation being performed. This can be one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="PROCESSOR_PARK_TYPE_CORE_PARKING"></a><a id="processor_park_type_core_parking"></a><dl>

### -field <b>PROCESSOR_PARK_TYPE_CORE_PARKING</b>


### -field 0x00

</dl>
</td>
<td width="60%">
<p>The processor should be parked.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="PROCESSOR_PARK_TYPE_INTERRUPT_STEERING"></a><a id="processor_park_type_interrupt_steering"></a><dl>

### -field <b>PROCESSOR_PARK_TYPE_INTERRUPT_STEERING</b>


### -field 0x01

</dl>
</td>
<td width="60%">
<p>Interrupts should be steered away from the processor.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186770">PEP_NOTIFY_PPM_PARK_SELECTION_V2 notification</a> notification. All three members of the structure contain input values that are set by the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx) before this notification is sent to the PEP.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>