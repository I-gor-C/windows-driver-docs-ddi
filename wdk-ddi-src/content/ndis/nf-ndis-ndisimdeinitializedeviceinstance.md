---
UID: NF.ndis.NdisIMDeInitializeDeviceInstance
title: NdisIMDeInitializeDeviceInstance function
author: windows-driver-content
description: The NdisIMDeInitializeDeviceInstance function calls an NDIS intermediate driver's MiniportHaltEx function to tear down the driver's virtual miniport.
old-location: netvista\ndisimdeinitializedeviceinstance.htm
old-project: NetVista
ms.assetid: badfab43-ba58-4711-a181-af87dcfeba4d
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: NdisIMDeInitializeDeviceInstance
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see       NdisIMDeInitializeDeviceInstance (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see       NdisIMDeInitializeDeviceInstance (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisIMDeInitializeDeviceInstance
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_IM_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
---

# NdisIMDeInitializeDeviceInstance function



## -description
The 
  <b>NdisIMDeInitializeDeviceInstance</b> function calls an NDIS intermediate driver's 
  <a href="..\ndis\nc-ndis-miniport_halt.md">MiniportHaltEx</a> function to tear down the
  driver's virtual miniport.



## -syntax

````
NDIS_STATUS NdisIMDeInitializeDeviceInstance(
  _In_ NDIS_HANDLE NdisMiniportHandle
);
````


## -parameters

### -param NdisMiniportHandle [in]

The handle that NDIS supplied to the 
     <a href="..\ndis\nc-ndis-miniport_initialize.md">
     MiniportInitializeEx</a> function.


## -returns
<b>NdisIMDeInitializeDeviceInstance</b> returns NDIS_STATUS_SUCCESS if the NIC has been torn down.
     Otherwise, it can return NDIS_STATUS_FAILURE if the given 
     <i>NdisMiniportHandle</i> is invalid.


## -remarks
For NDIS intermediate drivers, 
    <b>NdisIMDeInitializeDeviceInstance</b> is the reciprocal of the 
    <a href="netvista.ndisiminitializedeviceinstanceex">
    NdisIMInitializeDeviceInstanceEx</a> function. Such a driver usually calls 
    <b>NdisIMDeInitializeDeviceInstance</b> from its 
    <a href="..\ndis\nc-ndis-protocol_unbind_adapter_ex.md">
    ProtocolUnbindAdapterEx</a> function, when the underlying miniport adapter to which it was bound is
    being removed from the system, possibly because it is being reconfigured.

The call to 
    <b>NdisIMDeInitializeDeviceInstance</b> causes an NDIS call to the intermediate driver's 
    <a href="..\ndis\nc-ndis-miniport_halt.md">MiniportHaltEx</a> function after NDIS has
    told all higher level protocol drivers that had bound themselves to the intermediate's virtual miniport
    that they must unbind.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/ad38b9a2-78ba-443f-9b0d-b7bb40d495e1">
   NdisIMDeInitializeDeviceInstance (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>
   NdisIMDeInitializeDeviceInstance (NDIS 5.1)</b>) in Windows XP.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.ndis_irql_im_function">Irql_IM_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport_halt.md">MiniportHaltEx</a>
</dt>
<dt>
<a href="netvista.ndisiminitializedeviceinstanceex">
   NdisIMInitializeDeviceInstanceEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_unbind_adapter_ex.md">ProtocolUnbindAdapterEx</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NdisIMDeInitializeDeviceInstance function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

