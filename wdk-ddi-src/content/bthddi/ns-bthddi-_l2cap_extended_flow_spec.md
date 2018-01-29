---
UID : NS:bthddi._L2CAP_EXTENDED_FLOW_SPEC
title : _L2CAP_EXTENDED_FLOW_SPEC
author : windows-driver-content
description : The L2CAP_EXTENDED_FLOW_SPEC is reserved for future use.
old-location : bltooth\l2cap_extended_flow_spec.htm
old-project : bltooth
ms.assetid : B190484F-1A87-4C52-A1FF-4D4EB593A963
ms.author : windowsdriverdev
ms.date : 12/21/2017
ms.keywords : "*PL2CAP_EXTENDED_FLOW_SPEC, bthddi/PL2CAP_EXTENDED_FLOW_SPEC, _L2CAP_EXTENDED_FLOW_SPEC, L2CAP_EXTENDED_FLOW_SPEC, PL2CAP_EXTENDED_FLOW_SPEC, bthddi/L2CAP_EXTENDED_FLOW_SPEC, PL2CAP_EXTENDED_FLOW_SPEC structure pointer [Bluetooth Devices], bltooth.l2cap_extended_flow_spec, L2CAP_EXTENDED_FLOW_SPEC structure [Bluetooth Devices]"
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : bthddi.h
req.include-header : Bthddi.h
req.target-type : Windows
req.target-min-winverclnt : Supported in Windows 8 and later versions of Windows
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access   paged memory)
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : L2CAP_EXTENDED_FLOW_SPEC, *PL2CAP_EXTENDED_FLOW_SPEC
---

# _L2CAP_EXTENDED_FLOW_SPEC structure
The L2CAP_EXTENDED_FLOW_SPEC is reserved for future use.

## Syntax
````
typedef struct _L2CAP_EXTENDED_FLOW_SPEC {
  UCHAR  Identifier;
  UCHAR  ServiceType;
  USHORT MaxSDUSize;
  ULONG  SDUInterArrivalTime;
  ULONG  AccessLatency;
  ULONG  FlushTimeout;
} L2CAP_EXTENDED_FLOW_SPEC, *PL2CAP_EXTENDED_FLOW_SPEC;
````

## Members


`AccessLatency`

Reserved. Do not use.

`FlushTimeout`

Reserved. Do not use.

`Identifier`

Reserved. Do not use.

`MaxSDUSize`

Reserved. Do not use.

`SDUInterArrivalTime`

Reserved. Do not use.

`ServiceType`

Reserved. Do not use.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | bthddi.h (include Bthddi.h) |