---
UID: NC.ucmmanager.EVT_UCM_CONNECTOR_SET_POWER_ROLE
title: EVT_UCM_CONNECTOR_SET_POWER_ROLE
author: windows-driver-content
description: The client driver's implementation of the EVT_UCM_CONNECTOR_SET_POWER_ROLE event callback function that sets the power role of the connector to the specified role when attached to a partner connector.
old-location: buses\evt_ucm_connector_set_power_role.htm
old-project: UsbRef
ms.assetid: 56D5A78D-546E-439E-A69E-A87B0A3B288F
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _PORT_DATA_1, *PPORT_DATA_1, PPORT_DATA_1, PORT_DATA_1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ucmmanager.h
req.include-header: Ucmcx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 2.15
req.alt-api: PFN_UCM_CONNECTOR_SET_POWER_ROLE
req.alt-loc: Ucmmanager.h
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

# EVT_UCM_CONNECTOR_SET_POWER_ROLE callback



## -description
The client driver's implementation of the <i>EVT_UCM_CONNECTOR_SET_POWER_ROLE</i> event callback function that sets the power  role of the connector to the specified role when attached to a partner connector.  



## -prototype

````
EVT_UCM_CONNECTOR_SET_POWER_ROLE EvtSetDataRole;

NTSTATUS EvtSetDataRole(
  _In_ UCMCONNECTOR   Connector,
  _In_ UCM_POWER_ROLE PowerRole
)
{ ... }

typedef EVT_UCM_CONNECTOR_SET_POWER_ROLE PFN_UCM_CONNECTOR_SET_POWER_ROLE;
````


## -parameters

### -param Connector [in]

Handle to the connector that the client driver received in a previous call to  the <a href="buses.ucmconnectorcreate">UcmConnectorCreate</a> method.


### -param PowerRole [in]

A <a href="buses.ucm_power_role">UCM_POWER_ROLE</a>-typed flag that specifies the role to set.


## -returns
If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it must return a status value for which NT_SUCCESS(status) equals FALSE.


## -remarks
To register an <i>EVT_UCM_CONNECTOR_SET_POWER_ROLE</i> callback function, the client must call <a href="buses.ucmconnectorcreate">UcmConnectorCreate</a>.

The USB connector manager framework extension (UcmCx) can request either <b>UcmPowerRoleSink</b> or  <b>UcmPowerRoleSource</b>. If the port is already in the requested role, the client driver can complete the request without any changes. Otherwise, it starts a power-role swap operation (PR_Swap). The driver calls <a href="buses.ucmconnectorpowerdirectionchanged">UcmConnectorPowerDirectionChanged</a> to notify UcmCx about the success or failure of that operation. 
The driver can call that method within the callback function.

The role persists for the current connection.  

If a role-swap operation is pending, UcmCx does not request another role swap. Those operations are serialized across power and data role swaps.

After the swap operation completes, if the partner port sends a PR_Swap request, the client driver must reject the request. 


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

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
1.15

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.15

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ucmmanager.h (include Ucmcx.h)</dt>
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
<a href="buses.ucmconnectorcreate">UcmConnectorCreate</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [UsbRef\buses]:%20EVT_UCM_CONNECTOR_SET_POWER_ROLE callback function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

