---
UID: NS.PEPFX._PEP_PPM_PARK_SELECTION_V2
title: _PEP_PPM_PARK_SELECTION_V2
author: windows-driver-content
description: The PEP_PPM_PARK_SELECTION_V2 structure indicates the preferences of the operating system and platform extension plug-in (PEP) regarding which processors in the platform should be parked to reduce power consumption.
old-location: kernel\pep_ppm_park_selection_v2.htm
old-project: kernel
ms.assetid: D1EFB30D-E8E2-4585-AB0E-B7903F4D6656
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: _PEP_PPM_PARK_SELECTION_V2, PEP_PPM_PARK_SELECTION_V2, *PPEP_PPM_PARK_SELECTION_V2
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
---

# _PEP_PPM_PARK_SELECTION_V2 structure



## -description
The <b>PEP_PPM_PARK_SELECTION_V2</b> structure indicates the preferences of the operating system and platform extension plug-in (PEP) regarding which processors in the platform should be parked to reduce power consumption.



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

### -field AdditionalUnparkedProcessors

[in] The number of additional processors that need to be unparked.

This number includes all processors in the <b>Processors</b> array for which the PEP sets <b>PepPreference</b> to PROCESSOR_PARK_PREFERENCE_PARKED but the operating system sets <b>PoPreference</b> to either PROCESSOR_PARK_PREFERENCE_UNPARKED or PROCESSOR_PARK_PREFERENCE_NONE. For more information about these values, see <a href="kernel.pep_processor_park_preference">PEP_PROCESSOR_PARK_PREFERENCE</a>.

This number does not include processors in the <b>Processors</b> array for which the operating system sets the <b>PoPreference</b> value to PROCESSOR_PARK_PREFERENCE_PARKED.


### -field Count

[in] The number of elements in the array pointed to by the <b>Processors</b> member.


### -field Processors

[in/out] A pointer to an array of <a href="kernel.pep_processor_park_preference">PEP_PROCESSOR_PARK_PREFERENCE</a> structures. Each array element indicates the parking preferences for a particular processor. The <b>Count</b> member specifies the number of elements in the array.


### -field EvaluationTime

The interrupt time of the performance check evaluation that initiated this notification.


### -field EvaluationType

The type of evaluation being performed. This can be one of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>

### -field PROCESSOR_PARK_TYPE_CORE_PARKING
### -field 0x00

</td>
<td width="60%">
The processor should be parked.

</td>
</tr>
<tr>

### -field PROCESSOR_PARK_TYPE_INTERRUPT_STEERING
### -field 0x01

</td>
<td width="60%">
Interrupts should be steered away from the processor.

</td>
</tr>
</table>
 


## -remarks
This structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186770">PEP_NOTIFY_PPM_PARK_SELECTION_V2 notification</a> notification. All three members of the structure contain input values that are set by the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx) before this notification is sent to the PEP.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported starting with Windows 10.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>