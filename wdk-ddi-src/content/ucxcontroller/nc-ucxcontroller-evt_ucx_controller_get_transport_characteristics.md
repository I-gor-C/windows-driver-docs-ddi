---
UID: NC.ucxcontroller.EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS
title: EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS
author: windows-driver-content
description: UCX invokes this callback to retrieve the host controller characteristics.
old-location: buses\evt_ucx_controller_get_transport_characteristics.htm
old-project: usbref
ms.assetid: 4394199C-6644-4E11-BDAF-625C2F94DEE8
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: UcxInitializeDeviceInit
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ucxcontroller.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: *PFN_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS
req.alt-loc: UcxController.h
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
req.product: Windows 10 or later.
---

# EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS callback



## -description
 UCX invokes this callback to retrieve the host controller characteristics.



## -prototype

````
EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS EvUcxControllerGetTransportCharacteristics;

NTSTATUS EvUcxControllerGetTransportCharacteristics(
  _In_  UCXCONTROLLER                             UcxController,
  _Out_ PUCX_CONTROLLER_TRANSPORT_CHARACTERISTICS UcxControllerTransportCharacteristics
)
{ ... }

typedef EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS *PFN_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS;
````


## -parameters

### -param UcxController [in]

 A handle to the UCX controller that the client driver received in a previous call to  the <a href="buses._ucxcontrollercreate">UcxControllerCreate</a> method.


### -param UcxControllerTransportCharacteristics [out]

A pointer to a <a href="buses.ucx_controller_transport_characteristics">UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS</a> structure that the client driver for the host controller fills with transport characteristics.


## -returns
If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it must return a status value for which NT_SUCCESS(status) equals FALSE.


## -remarks
The UCX client driver registers its implementation with the USB host controller extension (UCX) by calling the <a href="buses._ucxcontrollercreate">UcxControllerCreate</a> method.

This callback function is optional. Whenever transport characteristics change, the client driver is responsible for notifying UCX that one of the characteristics have changed using a new function <a href="buses.ucxcontrollernotifytransportcharacteristicschange">UcxControllerNotifyTransportCharacteristicsChange</a>. 


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10, version 1709

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>UcxController.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses._ucxcontrollercreate">UcxControllerCreate</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS callback function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

