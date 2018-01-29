---
UID : NC:ndis.IF_SET_OBJECT
title : IF_SET_OBJECT
author : windows-driver-content
description : The ProviderSetObject function sets information that is associated with a network interface.
old-location : netvista\providersetobject.htm
old-project : netvista
ms.assetid : e5dcb46e-5a8a-45b7-b6aa-150a9cec0155
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.providersetobject, ProviderSetObject callback function [Network Drivers Starting with Windows Vista], ProviderSetObject, IF_SET_OBJECT, IF_SET_OBJECT, ndis/ProviderSetObject, *IFP_SET_OBJECT callback function [Network Drivers Starting with Windows Vista], *IFP_SET_OBJECT, net_if_provider_functions_ref_8da505c4-dd64-43c8-a6a4-ad13cc4b18d0.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : ndis.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.0 and later.
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
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : VIDEO_STREAM_INIT_PARMS, *LPVIDEO_STREAM_INIT_PARMS
---


# IF_SET_OBJECT function
The 
  <i>ProviderSetObject</i> function sets information that is associated with a network interface.

## Syntax

```
IF_SET_OBJECT IfSetObject;

NDIS_STATUS() IfSetObject(
  NDIS_HANDLE ProviderIfContext,
  NET_IF_OBJECT_ID ObjectId,
  ULONG InputBufferLength,
  PVOID pInputBuffer
)
{...}
```

## Parameters

`ProviderIfContext`

A handle that identifies the interface provider's context area for the interface. The interface
     provider passed this handle to NDIS in a call to the 
     <mshelp:link keywords="netvista.ndisifregisterinterface" tabindex="0"><b>
     NdisIfRegisterInterface</b></mshelp:link> function.

`ObjectId`

An identifier for the object that is the target of the set request. For a list of object
     identifiers (OIDs) that apply to interface providers, see 
     <mshelp:link keywords="netvista.ndis_network_interface_oids" tabindex="0">NDIS Network Interface
     OIDs</mshelp:link>.

`InputBufferLength`

The length, in bytes, of the buffer that 
     <i>pInputBuffer</i> points to.

`pInputBuffer`

A pointer to an input buffer that specifies the information that the interface provider should use
     to set the object data.


## Return Value

<i>ProviderSetObject</i> returns one of the following status values:
<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The operation completed successfully.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl>
</td>
<td width="60%">
The operation failed because of insufficient resources.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>NDIS_STATUS_INVALID_PARAMETER</b></dt>
</dl>
</td>
<td width="60%">
The call failed because some of the input parameters were invalid.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>NDIS_STATUS_Xxx</b></dt>
</dl>
</td>
<td width="60%">
The call failed for some other reason. This function can propagate error codes from the
       functions that it calls or generate an appropriate error code.

</td>
</tr>
</table>

## Remarks

NDIS calls a network interface provider's 
    <i>ProviderSetObject</i> function to set information that is associated with an interface that the
    provider registered. For a list of OIDs that apply to interface providers, see 
    <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/mapping-of-ndis-network-interfaces-to-ndis-oids">NDIS Network Interface OIDs</a>.

Note that there are currently no set OIDs defined.

NDIS calls 
    <i>ProviderSetObject</i> at IRQL = PASSIVE_LEVEL.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ndis.h (include Ndis.h) |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |

## See Also

<a href="..\ndis\nf-ndis-ndisifregisterinterface.md">NdisIfRegisterInterface</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20IF_SET_OBJECT callback function%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>