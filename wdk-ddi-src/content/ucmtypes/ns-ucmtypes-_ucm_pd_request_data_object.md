---
UID: NS:ucmtypes._UCM_PD_REQUEST_DATA_OBJECT
title: "_UCM_PD_REQUEST_DATA_OBJECT"
author: windows-driver-content
description: Describes a Request Data Object (RDO). For information about these members, see the Power Delivery specification.
old-location: buses\ucm_pd_request_data_object.htm
old-project: usbref
ms.assetid: 2F5CC46B-3BFC-4C69-A9C8-C4BC4864E84B
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUCM_PD_REQUEST_DATA_OBJECT, PUCM_PD_REQUEST_DATA_OBJECT, PUCM_PD_REQUEST_DATA_OBJECT union pointer [Buses], UCM_PD_REQUEST_DATA_OBJECT, UCM_PD_REQUEST_DATA_OBJECT union [Buses], _UCM_PD_REQUEST_DATA_OBJECT, buses.ucm_pd_request_data_object, ucmtypes/PUCM_PD_REQUEST_DATA_OBJECT, ucmtypes/UCM_PD_REQUEST_DATA_OBJECT"
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
-	UCM_PD_REQUEST_DATA_OBJECT
product: Windows
targetos: Windows
req.typenames: UCM_PD_REQUEST_DATA_OBJECT, *PUCM_PD_REQUEST_DATA_OBJECT
req.product: Windows 10 or later.
---

# _UCM_PD_REQUEST_DATA_OBJECT structure
Describes a Request Data Object (RDO). For information about these members, see the <a href="http://www.usb.org/developers/docs/usb20_docs/">Power Delivery specification</a>.

## Syntax
```
typedef struct _UCM_PD_REQUEST_DATA_OBJECT {
  ULONG  Ul;
  struct {
    unsigned  : 3  ObjectPosition;
    unsigned  : 28 Reserved1;
    unsigned  : 1  Reserved2;
  } Common;
  struct {
    unsigned  : 1  CapabilityMismatch;
    unsigned  : 1  GiveBackFlag;
    unsigned  : 10 MaximumOperatingCurrentIn10mA;
    unsigned  : 1  NoUsbSuspend;
    unsigned  : 3  ObjectPosition;
    unsigned  : 10 OperatingCurrentIn10mA;
    unsigned  : 4  Reserved1;
    unsigned  : 1  Reserved2;
    unsigned  : 1  UsbCommunicationCapable;
  } FixedAndVariableRdo;
  struct {
    unsigned  : 1  CapabilityMismatch;
    unsigned  : 1  GiveBackFlag;
    unsigned  : 10 MaximumOperatingPowerIn250mW;
    unsigned  : 1  NoUsbSuspend;
    unsigned  : 3  ObjectPosition;
    unsigned  : 10 OperatingPowerIn250mW;
    unsigned  : 4  Reserved1;
    unsigned  : 1  Reserved2;
    unsigned  : 1  UsbCommunicationCapable;
  } BatteryRdo;
} *PUCM_PD_REQUEST_DATA_OBJECT, UCM_PD_REQUEST_DATA_OBJECT;
```

## Members


`Ul`

Size of the structure.

`Common`

#### Reserved1

Reserved.



#### ObjectPosition

Object position.



#### Reserved2

Reserved.

`FixedAndVariableRdo`

#### MaximumOperatingCurrentIn10mA

Maximum current in 10 mA units.



#### OperatingCurrentIn10mA

Operating current in 10mA units.



#### Reserved1

Reserved.



#### NoUsbSuspend

Indicates support for USB suspend.





#### UsbCommunicationCapable

USB communication capable. 



#### CapabilityMismatch

Capability Mismatch 



#### GiveBackFlag

GiveBack Flag.



#### ObjectPosition

Object Position.



#### Reserved2

Reserved for future use.

`BatteryRdo`

#### MaximumOperatingPowerIn250mW

Maximum Operating Power in 250mW units. 



#### OperatingPowerIn250mW

Operating Power in 250mW units.



#### Reserved1

Reserved for future use.



#### NoUsbSuspend

 USB Suspend. 



#### UsbCommunicationCapable

USB Communications Capable.



#### CapabilityMismatch

Capability Mismatch. 



#### GiveBackFlag

GiveBack Flag. 



#### ObjectPosition

Object Position.



#### Reserved2

Reserved.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Minimum KMDF version** | 1.15 |
| **Minimum UMDF version** | 2.15 |
| **Header** | ucmtypes.h (include Ucmcx.h) |