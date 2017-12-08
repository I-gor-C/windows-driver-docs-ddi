---
UID: NF.ndis.NdisCloseConfiguration
title: NdisCloseConfiguration function
author: windows-driver-content
description: The NdisCloseConfiguration function releases the handle to the registry key that was returned by the NdisOpenConfigurationEx, NdisOpenConfigurationKeyByIndex, or NdisOpenConfigurationKeyByName function.
old-location: netvista\ndiscloseconfiguration.htm
old-project: netvista
ms.assetid: 2d68f7dd-3954-4b3b-8673-1da63e1a1edc
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NdisCloseConfiguration
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisCloseConfiguration (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisCloseConfiguration (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisCloseConfiguration
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miscellaneous_Function, NdisOpenConfigurationEx
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

# NdisCloseConfiguration function



## -description
The 
  <b>NdisCloseConfiguration</b> function releases the handle to the registry key that was returned by the 
  <a href="netvista.ndisopenconfigurationex">NdisOpenConfigurationEx</a>, 
  <a href="netvista.ndisopenconfigurationkeybyindex">
  NdisOpenConfigurationKeyByIndex</a>, or 
  <a href="netvista.ndisopenconfigurationkeybyname">
  NdisOpenConfigurationKeyByName</a> function.


## -syntax

````
VOID NdisCloseConfiguration(
  _In_ NDIS_HANDLE ConfigurationHandle
);
````


## -parameters

### -param ConfigurationHandle [in]

The handle that the 
     <a href="netvista.ndisopenconfigurationex">NdisOpenConfigurationEx</a> function
     returns.

## -returns
None

## -remarks
This function frees any temporary storage allocated in calls to other 
    <b>Ndis<i>Xxx</i></b> functions that required the returned 
    <i>ConfigurationHandle</i> as a parameter.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/b3c417e5-7899-40fd-92c8-1c1531aa8943">NdisCloseConfiguration (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisCloseConfiguration (NDIS
   5.1)</b>) in Windows XP.
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
<a href="devtest.ndis_irql_miscellaneous_function">Irql_Miscellaneous_Function</a>, <a href="devtest.ndis_ndisopenconfigurationex">NdisOpenConfigurationEx</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.driverentry_of_ndis_protocol_drivers">DriverEntry of NDIS Protocol
   Drivers</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="netvista.ndisopenconfigurationex">NdisOpenConfigurationEx</a>
</dt>
<dt>
<a href="netvista.ndisopenconfigurationkeybyindex">
   NdisOpenConfigurationKeyByIndex</a>
</dt>
<dt>
<a href="netvista.ndisopenconfigurationkeybyname">
   NdisOpenConfigurationKeyByName</a>
</dt>
<dt>
<a href="netvista.ndisreadconfiguration">NdisReadConfiguration</a>
</dt>
<dt>
<a href="netvista.ndisreadnetworkaddress">NdisReadNetworkAddress</a>
</dt>
<dt>
<a href="netvista.ndiswriteconfiguration">NdisWriteConfiguration</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_bind_adapter_ex.md">ProtocolBindAdapterEx</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisCloseConfiguration function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
