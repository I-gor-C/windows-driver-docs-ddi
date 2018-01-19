---
UID : NS:ucxcontroller._UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS
title : _UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS
author : windows-driver-content
description : Stores the transport characteristics at relevant points in time. This structure is used in the EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS callback function.
old-location : buses\ucx_controller_transport_characteristics.htm
old-project : usbref
ms.assetid : 9F267427-8D70-45D5-A8E6-67A1C6B73CDB
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : _UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS, UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS, *PUCX_CONTROLLER_TRANSPORT_CHARACTERISTICS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ucxcontroller.h
req.include-header : Ucxclass.h
req.target-type : Windows
req.target-min-winverclnt : Windows 10, version 1709
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS
req.alt-loc : UcxController.h
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
req.typenames : UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS, *PUCX_CONTROLLER_TRANSPORT_CHARACTERISTICS
req.product : Windows 10 or later.
---

# _UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS structure
Stores the transport characteristics at relevant points in time. This structure is used in the   <a href="..\ucxcontroller\nc-ucxcontroller-evt_ucx_controller_get_transport_characteristics.md">EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS</a> callback function.

## Syntax
````
typedef struct _UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS {
  ULONG                       TransportCharacteristicsFlags;
  ULONG64                     CurrentRoundtripLatencyInMilliSeconds;
  ULONG64                     MaxPotentialBandwidth;
} UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS, *PUCX_CONTROLLER_TRANSPORT_CHARACTERISTICS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ucxcontroller.h (include Ucxclass.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ucxcontroller\nc-ucxcontroller-evt_ucx_controller_get_transport_characteristics.md">EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>