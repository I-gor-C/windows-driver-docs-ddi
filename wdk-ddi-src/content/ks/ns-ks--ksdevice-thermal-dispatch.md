---
UID: NS.ks._KSDEVICE_THERMAL_DISPATCH
title: KSDEVICE_THERMAL_DISPATCH
author: windows-driver-content
description: The KSDEVICE_THERMAL_DISPATCH structure is used by the miniport driver in the API call to register thermal notification callbacks. This structure contains the callback function pointers for active and passive cooling interfaces.
old-location: stream\ksdevice_thermal_dispatch.htm
ms.assetid: 6E4ADD86-EFC4-4369-83A1-1D2824235310
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSDEVICE_THERMAL_DISPATCH
req.alt-loc: ks.h
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
ms.keywords: KSDEVICE_THERMAL_DISPATCH, KSDEVICE_THERMAL_DISPATCH, *PKSDEVICE_THERMAL_DISPATCH
req.iface: 
---

# KSDEVICE_THERMAL_DISPATCH structure



## -description
<p>The <b>KSDEVICE_THERMAL_DISPATCH</b> structure is used by the miniport driver in the API call to register thermal notification callbacks. This structure contains the callback function pointers for active and passive cooling interfaces. </p>


## -syntax

````
typedef struct _KSDEVICE_THERMAL_DISPATCH {
  PFNKSDEVICETHERMALACTIVECOOLING  ActiveCooling;
  PFNKSDEVICETHERMALPASSIVECOOLING PassiveCooling;
} KSDEVICE_THERMAL_DISPATCH, *PKSDEVICE_THERMAL_DISPATCH;
````


## -struct-fields
<dl>

### -field <b>ActiveCooling</b>

<dd>
<p>The active thermal callback notification. The routine is defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>_IRQL_requires_max_(PASSIVE_LEVEL)
typedef
void
(*PFNKSDEVICETHERMALACTIVECOOLING)(
    _In_  PKSDEVICE KsDevice,
    _In_  BOOLEAN Engaged,
    _Out_ KSDEVICE_THERMAL_STATE* DeviceThermalState
);</pre>
</td>
</tr>
</table></span></div>
<dl class="indent">

### -field <a id="KsDevice"></a><a id="ksdevice"></a><a id="KSDEVICE"></a><p><a id="KsDevice"></a><a id="ksdevice"></a><a id="KSDEVICE"></a><b><i>KsDevice</i></b></p>


<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a> object representing the device managed by KS.</p>
</dd>

### -field <a id="Engaged"></a><a id="engaged"></a><a id="ENGAGED"></a><p><a id="Engaged"></a><a id="engaged"></a><a id="ENGAGED"></a><b><i>Engaged</i></b></p>


<dd>
<p>[in] Indicates whether to engage or disengage active cooling. If <b>TRUE</b>, the driver must engage active cooling (for example, by turning the fan on). If <b>FALSE</b>, the driver must disengage active cooling (for example, by turning the fan off).</p>
</dd>

### -field <a id="DeviceThermalState"></a><a id="devicethermalstate"></a><a id="DEVICETHERMALSTATE"></a><p><a id="DeviceThermalState"></a><a id="devicethermalstate"></a><a id="DEVICETHERMALSTATE"></a><b><i>DeviceThermalState</i></b></p>


<dd>
<p>[out] Return value: Avstream-determined thermal state. If the state changes the pipeline is notified of the change. The pipeline notifies any app registered for thermal notifications. For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/hh698235">ActiveCooling</a> routine.</p>
</dd>
</dl>
</dd>

### -field <b>PassiveCooling</b>

<dd>
<p>The passive thermal callback notification.. The routine is defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>_IRQL_requires_max_(PASSIVE_LEVEL)
typedef
void
(*PFNKSDEVICETHERMALPASSIVECOOLING)(
    _In_  PKSDEVICE KsDevice,
    _In_  ULONG Percentage,
    _Out_ KSDEVICE_THERMAL_STATE* DeviceThermalState
);</pre>
</td>
</tr>
</table></span></div>
<dl class="indent">

### -field <a id="KsDevice"></a><a id="ksdevice"></a><a id="KSDEVICE"></a><p><a id="KsDevice"></a><a id="ksdevice"></a><a id="KSDEVICE"></a><b><i>KsDevice</i></b></p>


<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a> object representing the device managed by KS.</p>
</dd>

### -field <a id="Percentage"></a><a id="percentage"></a><a id="PERCENTAGE"></a><p><a id="Percentage"></a><a id="percentage"></a><a id="PERCENTAGE"></a><b><i>Percentage</i></b></p>


<dd>
<p>[in] The percentage of full performance at which the device is permitted to operate. A parameter value of 100 indicates that the device is under no cooling restrictions and can operate at full performance level. A parameter value of zero indicates that the device must operate at its lowest thermal level. A parameter value between 0 and 100 indicates the degree to which the device's performance must be throttled to reduce heat generation. This parameter value is a threshold that the device must not exceed.</p>
</dd>

### -field <a id="DeviceThermalState"></a><a id="devicethermalstate"></a><a id="DEVICETHERMALSTATE"></a><p><a id="DeviceThermalState"></a><a id="devicethermalstate"></a><a id="DEVICETHERMALSTATE"></a><b><i>DeviceThermalState</i></b></p>


<dd>
<p>[out] Return value: Avstream-determined thermal state. If the state changes the pipeline is notified of the change. The pipeline notifies any app registered for thermal notifications. For more information, see the  <a href="https://msdn.microsoft.com/library/windows/hardware/hh698270">PassiveCooling</a> routine.</p>
</dd>
</dl>
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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>