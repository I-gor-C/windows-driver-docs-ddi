---
UID : NS:ucmtypes._UCM_PD_REQUEST_DATA_OBJECT
title : _UCM_PD_REQUEST_DATA_OBJECT
author : windows-driver-content
description : Describes a Request Data Object (RDO). For information about these members, see the Power Delivery specification.
old-location : buses\ucm_pd_request_data_object.htm
old-project : usbref
ms.assetid : 2F5CC46B-3BFC-4C69-A9C8-C4BC4864E84B
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : buses.ucm_pd_request_data_object, PUCM_PD_REQUEST_DATA_OBJECT, PUCM_PD_REQUEST_DATA_OBJECT union pointer [Buses], ucmtypes/PUCM_PD_REQUEST_DATA_OBJECT, *PUCM_PD_REQUEST_DATA_OBJECT, _UCM_PD_REQUEST_DATA_OBJECT, UCM_PD_REQUEST_DATA_OBJECT, ucmtypes/UCM_PD_REQUEST_DATA_OBJECT, UCM_PD_REQUEST_DATA_OBJECT union [Buses]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ucmtypes.h
req.include-header : Ucmcx.h
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 1.15
req.umdf-ver : 2.15
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : UCM_PD_REQUEST_DATA_OBJECT, *PUCM_PD_REQUEST_DATA_OBJECT
req.product : Windows 10 or later.
---

# _UCM_PD_REQUEST_DATA_OBJECT structure
Describes a Request Data Object (RDO). For information about these members, see the <a href="http://www.usb.org/developers/docs/usb20_docs/">Power Delivery specification</a>.

## Syntax
````
typedef union _UCM_PD_REQUEST_DATA_OBJECT {
  Ulong  Ul;
  struct {
    unsigned Reserved1  :28;
    unsigned ObjectPosition  :3;
    unsigned Reserved2  :1;
  } Common;
  struct {
    unsigned MaximumOperatingCurrentIn10mA  :10;
    unsigned OperatingCurrentIn10mA  :10;
    unsigned Reserved1  :4;
    unsigned NoUsbSuspend  :1;
    unsigned UsbCommunicationCapable  :1;
    unsigned CapabilityMismatch  :1;
    unsigned GiveBackFlag  :1;
    unsigned ObjectPosition  :3;
    unsigned Reserved2  :1;
  } FixedAndVariableRdo;
  struct {
    unsigned MaximumOperatingPowerIn250mW  :10;
    unsigned OperatingPowerIn250mW  :10;
    unsigned Reserved1  :4;
    unsigned NoUsbSuspend  :1;
    unsigned UsbCommunicationCapable  :1;
    unsigned CapabilityMismatch  :1;
    unsigned GiveBackFlag  :1;
    unsigned ObjectPosition  :3;
    unsigned Reserved2  :1;
  } BatteryRdo;
} UCM_PD_REQUEST_DATA_OBJECT, *PUCM_PD_REQUEST_DATA_OBJECT;
````

## Members


`BatteryRdo`



`Common`



`FixedAndVariableRdo`



`Ul`

Size of the structure.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** | 1.15 |
| **Minimum UMDF version** | 2.15 |
| **Header** | ucmtypes.h (include Ucmcx.h) |