---
UID: NC.ucxcontroller.EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS
title: EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS
author: windows-driver-content
description: UCX invokes this callback to retrieve the host controller characteristics.
old-location: buses\evt_ucx_controller_get_transport_characteristics.htm
old-project: usbref
ms.assetid: 4394199C-6644-4E11-BDAF-625C2F94DEE8
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCM_PD_REQUEST_DATA_OBJECT, UCM_PD_REQUEST_DATA_OBJECT, *PUCM_PD_REQUEST_DATA_OBJECT
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
req.iface: 
req.product: Windows 10 or later.
---

# EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS callback



## -description
<p> UCX invokes this callback to retrieve the host controller characteristics.</p>


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
<dl>

### -param UcxController [in]

<dd>
<p> A handle to the UCX controller that the client driver received in a previous call to  the <a href="buses._ucxcontrollercreate">UcxControllerCreate</a> method.</p>
</dd>

### -param UcxControllerTransportCharacteristics [out]

<dd>
<p>A pointer to a <a href="..\ucxcontroller\ns-ucxcontroller--ucx-controller-transport-characteristics.md">UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS</a> structure that the client driver for the host controller fills with transport characteristics.</p>
</dd>
</dl>

## -returns
<p>If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it must return a status value for which NT_SUCCESS(status) equals FALSE.</p>

## -remarks
<p>The UCX client driver registers its implementation with the USB host controller extension (UCX) by calling the <a href="buses._ucxcontrollercreate">UcxControllerCreate</a> method.</p>

<p>This callback function is optional. Whenever transport characteristics change, the client driver is responsible for notifying UCX that one of the characteristics have changed using a new function <a href="..\ucxcontroller\nf-ucxcontroller-ucxcontrollernotifytransportcharacteristicschange.md">UcxControllerNotifyTransportCharacteristicsChange</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>UcxController.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses._ucxcontrollercreate">UcxControllerCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS callback function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
