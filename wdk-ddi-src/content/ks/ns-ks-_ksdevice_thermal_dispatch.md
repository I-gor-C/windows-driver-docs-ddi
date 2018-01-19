---
UID : NS:ks._KSDEVICE_THERMAL_DISPATCH
title : _KSDEVICE_THERMAL_DISPATCH
author : windows-driver-content
description : The KSDEVICE_THERMAL_DISPATCH structure is used by the miniport driver in the API call to register thermal notification callbacks. This structure contains the callback function pointers for active and passive cooling interfaces.
old-location : stream\ksdevice_thermal_dispatch.htm
old-project : stream
ms.assetid : 6E4ADD86-EFC4-4369-83A1-1D2824235310
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _KSDEVICE_THERMAL_DISPATCH, KSDEVICE_THERMAL_DISPATCH, *PKSDEVICE_THERMAL_DISPATCH
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ks.h
req.include-header : Ks.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KSDEVICE_THERMAL_DISPATCH
req.alt-loc : ks.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : KSDEVICE_THERMAL_DISPATCH, *PKSDEVICE_THERMAL_DISPATCH
---

# _KSDEVICE_THERMAL_DISPATCH structure
The <b>KSDEVICE_THERMAL_DISPATCH</b> structure is used by the miniport driver in the API call to register thermal notification callbacks. This structure contains the callback function pointers for active and passive cooling interfaces.

## Syntax
````
typedef struct _KSDEVICE_THERMAL_DISPATCH {
  PFNKSDEVICETHERMALACTIVECOOLING  ActiveCooling;
  PFNKSDEVICETHERMALPASSIVECOOLING PassiveCooling;
} KSDEVICE_THERMAL_DISPATCH, *PKSDEVICE_THERMAL_DISPATCH;
````

## Members

        
            `ActiveCooling`

            The active thermal callback notification. The routine is defined as follows:

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
        
            `PassiveCooling`

            The passive thermal callback notification.. The routine is defined as follows:

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


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |