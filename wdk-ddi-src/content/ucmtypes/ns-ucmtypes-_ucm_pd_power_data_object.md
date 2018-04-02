---
UID: NS:ucmtypes._UCM_PD_POWER_DATA_OBJECT
title: "_UCM_PD_POWER_DATA_OBJECT"
author: windows-driver-content
description: Describes a Power Data Object. For information about these members, see the Power Delivery specification.
old-location: buses\ucm_pd_power_data_object.htm
old-project: usbref
ms.assetid: C54750A9-EE64-4FE7-9ED6-EC9709A82C43
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUCM_PD_POWER_DATA_OBJECT, PUCM_PD_POWER_DATA_OBJECT, PUCM_PD_POWER_DATA_OBJECT union pointer [Buses], UCM_PD_POWER_DATA_OBJECT, UCM_PD_POWER_DATA_OBJECT union [Buses], _UCM_PD_POWER_DATA_OBJECT, buses.ucm_pd_power_data_object, ucmtypes/PUCM_PD_POWER_DATA_OBJECT, ucmtypes/UCM_PD_POWER_DATA_OBJECT"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucmtypes.h
req.include-header: Ucmcx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 2.15
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ucmtypes.h
api_name:
-	UCM_PD_POWER_DATA_OBJECT
product:
- Windows
targetos: Windows
req.typenames: UCM_PD_POWER_DATA_OBJECT, *PUCM_PD_POWER_DATA_OBJECT
req.product: Windows 10 or later.
---

# _UCM_PD_POWER_DATA_OBJECT structure
Describes a Power Data Object. For information about these members, see the <a href="http://www.usb.org/developers/docs/usb20_docs/">Power Delivery specification</a>.

## Syntax
```
typedef struct _UCM_PD_POWER_DATA_OBJECT {
  ULONG  Ul;
  struct {
    unsigned  : 30 Reserved;
    unsigned  : 2  Type;
  } Common;
  struct {
    unsigned  : 1  DataRoleSwap;
    unsigned  : 1  DualRolePower;
    unsigned  : 1  ExternallyPowered;
    unsigned  : 2  FixedSupply;
    unsigned  : 10 MaximumCurrentIn10mA;
    unsigned  : 2  PeakCurrent;
    unsigned  : 3  Reserved;
    unsigned  : 1  UsbCommunicationCapable;
    unsigned  : 1  UsbSuspendSupported;
    unsigned  : 10 VoltageIn50mV;
  } FixedSupplyPdo;
  struct {
    unsigned  : 10 MaximumCurrentIn10mA;
    unsigned  : 10 MaximumVoltageIn50mV;
    unsigned  : 10 MinimumVoltageIn50mV;
    unsigned  : 2  VariableSupportNonBattery;
  } VariableSupplyNonBatteryPdo;
  struct {
    unsigned  : 2  Battery;
    unsigned  : 10 MaximumAllowablePowerIn250mW;
    unsigned  : 10 MaximumVoltageIn50mV;
    unsigned  : 10 MinimumVoltageIn50mV;
  } BatterySupplyPdo;
} *PUCM_PD_POWER_DATA_OBJECT, UCM_PD_POWER_DATA_OBJECT;
```

## Members


`Ul`

Size of the structure.

`Common`

#### Reserved

Reserved.



#### Type

Type of Power Data Object.

`FixedSupplyPdo`

Describing a Fixed Supply type Power Data Object.



#### MaximumCurrentIn10mA

Maximum current in multiples of 10 mA.



#### VoltageIn50mV

Voltage in multiples of 50 mV.



#### PeakCurrent

Peak current.



#### Reserved

Reserved for future use.



#### DataRoleSwap

If set, indicates the Power Data Object can perform a data role swap.



#### UsbCommunicationCapable

If set, indicates the Power Data Object is USB communication capable. 



#### ExternallyPowered

If set, indicates the Power Data Object is externally powered.



#### UsbSuspendSupported

Indicates support for USB suspend.





#### DualRolePower

Dual role power



#### FixedSupply

fixed supply

`VariableSupplyNonBatteryPdo`

Contains bitfields describing a variable-supply non-battery PD object.



#### MaximumCurrentIn10mA

Describes the maximum current in multiples of 10 mA.



#### MinimumVoltageIn50mV

Desribes the minimum voltage in multiples of 50 mV.



#### MaximumVoltageIn50mV

Describes the maximum voltage in multiples of 50 mV.



#### VariableSupportNonBattery

Variable Support Non Battery type.

`BatterySupplyPdo`

Contains bitfields describing a battery supply PD object.



#### MaximumAllowablePowerIn250mW

Describes the maximum allowable power in multiples of 250 mW.



#### MinimumVoltageIn50mV

Describes the minimum voltage in multiples of 50 mV.



#### MaximumVoltageIn50mV

Describes the maximum voltage in multiples of 50 mV.



#### Battery

Battery type.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Minimum KMDF version** | 1.15 |
| **Minimum UMDF version** | 2.15 |
| **Header** | ucmtypes.h (include Ucmcx.h) |