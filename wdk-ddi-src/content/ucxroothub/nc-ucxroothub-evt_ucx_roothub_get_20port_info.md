---
UID : NC:ucxroothub.EVT_UCX_ROOTHUB_GET_20PORT_INFO
title : EVT_UCX_ROOTHUB_GET_20PORT_INFO
author : windows-driver-content
description : The client driver's implementation that UCX calls when it receives a request for information about USB 2.0 ports on the root hub.
old-location : buses\evt_ucx_roothub_get_20port_info.htm
old-project : usbref
ms.assetid : c4a328fb-ffbf-4da4-b52d-6cea58e56b5e
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : buses.evt_ucx_roothub_get_20port_info, EvtUcxRootHubGet20PortInfo callback function [Buses], EvtUcxRootHubGet20PortInfo, EVT_UCX_ROOTHUB_GET_20PORT_INFO, EVT_UCX_ROOTHUB_GET_20PORT_INFO, ucxroothub/EvtUcxRootHubGet20PortInfo, PEVT_UCX_ROOTHUB_GET_20PORT_INFO callback function pointer [Buses], PEVT_UCX_ROOTHUB_GET_20PORT_INFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : ucxroothub.h
req.include-header : Ucxclass.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 1.0
req.umdf-ver : 2.0
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : DISPATCH_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PUCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS, UCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS"
req.product : Windows 10 or later.
---


# EVT_UCX_ROOTHUB_GET_20PORT_INFO function
The client driver's implementation that UCX calls when it receives a request for information about USB  2.0 ports on the  root hub.

## Syntax

```
EVT_UCX_ROOTHUB_GET_20PORT_INFO EvtUcxRoothubGet20PortInfo;

void EvtUcxRoothubGet20PortInfo(
  UCXROOTHUB UcxRootHub,
  WDFREQUEST Request
)
{...}
```

## Parameters

`UcxRootHub`

A handle to a UCX object that represents the root hub.

`Request`

A structure of type <a href="..\ucxroothub\ns-ucxroothub-_roothub_20port_info.md">_ROOTHUB_20PORT_INFO</a>.


## Return Value

This callback function does not return a value.

## Remarks

The UCX client driver registers this callback function with the USB host controller extension (UCX) by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188048">UcxRootHubCreate</a>
 method.

 The <b>PortInfoArray</b> array of the <a href="..\ucxroothub\ns-ucxroothub-_roothub_20ports_info.md">_ROOTHUB_20PORTS_INFO</a> structure
    contains a list of USB 2.0 ports that the root hub supports.

The client driver returns completion status in <i>Request</i> and in the USBD_STATUS
    in the URB header.  The driver can complete the WDFREQUEST asynchronously.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | ucxroothub.h (include Ucxclass.h) |
| **Library** |  |
| **IRQL** | DISPATCH_LEVEL |
| **DDI compliance rules** |  |

## See Also

<a href="..\ucxroothub\ns-ucxroothub-_roothub_20ports_info.md">_ROOTHUB_20PORTS_INFO</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20EVT_UCX_ROOTHUB_GET_20PORT_INFO callback function%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>