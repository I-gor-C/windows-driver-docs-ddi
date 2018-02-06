---
UID: NF:ucmmanager.UcmConnectorChargingStateChanged
title: UcmConnectorChargingStateChanged function
author: windows-driver-content
description: Notifies the USB connector manager framework extension (UcmCx) with the updated charging state of the partner connector.
old-location: buses\ucmconnectorchargingstatechanged.htm
old-project: usbref
ms.assetid: A645BFE0-4B7F-416F-9096-596ADAA37951
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: UcmConnectorChargingStateChanged method [Buses], UcmConnectorChargingStateChanged, buses.ucmconnectorchargingstatechanged, ucmmanager/UcmConnectorChargingStateChanged
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucmmanager.h
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
req.lib: UcmCxstub.lib
req.dll: 
req.irql: PASSIVE_LEVEL
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	UcmCxstub.lib
-	UcmCxstub.dll
apiname:
-	UcmConnectorChargingStateChanged
product: Windows
targetos: Windows
req.typenames: PORT_DATA_1, *PPORT_DATA_1
req.product: Windows 10 or later.
---


# UcmConnectorChargingStateChanged function
Notifies the USB connector manager framework extension (UcmCx) with the updated charging state of the partner connector.

## Syntax

````
NTSTATUS UcmConnectorChargingStateChanged(
  [in] UCMCONNECTOR        Connector,
  [in] UCM_CHARGING_STATE  ChargingState
);
````

## Parameters

`Connector`

Handle to the connector object that the client driver received in the previous call to <a href="..\ucmmanager\nf-ucmmanager-ucmconnectorcreate.md">UcmConnectorCreate</a>.

`ChargingState`

One of the <a href="..\ucmtypes\ne-ucmtypes-_ucm_charging_state.md">UCM_CHARGING_STATE</a>-typed flags that indicates the new charging state.


## Return Value

<b>UcmConnectorChargingStateChanged</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method can return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> value.

## Remarks

If the client driver determines that the charging state is non-optimal, it should report slow or trickle charging to UcmCx. Then, the operating system notifies the user of this condition.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.15 |
| **Minimum UMDF version** | 2.15 |
| **Header** | ucmmanager.h (include Ucmcx.h) |
| **Library** | UcmCxstub.lib |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="..\ucmmanager\nf-ucmmanager-ucmconnectorcreate.md">UcmConnectorCreate</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UcmConnectorChargingStateChanged method%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>