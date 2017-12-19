---
UID: NF.ndis.NdisOpenConfigurationEx
title: NdisOpenConfigurationEx function
author: windows-driver-content
description: NDIS drivers call the NdisOpenConfigurationEx function to get a configuration handle that allows access to configuration parameters in the registry.
old-location: netvista\ndisopenconfigurationex.htm
old-project: NetVista
ms.assetid: 76539106-6d8d-4a80-9c74-a6a4ca37c40e
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: NdisOpenConfigurationEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisOpenConfigurationEx
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

# NdisOpenConfigurationEx function



## -description
NDIS drivers call the 
  <b>NdisOpenConfigurationEx</b> function to get a configuration handle that allows access to configuration
  parameters in the registry.



## -syntax

````
NDIS_STATUS NdisOpenConfigurationEx(
  _In_  PNDIS_CONFIGURATION_OBJECT ConfigObject,
  _Out_ PNDIS_HANDLE               ConfigurationHandle
);
````


## -parameters

### -param ConfigObject [in]

A pointer to a caller-supplied and initialized 
     <a href="netvista.ndis_configuration_object">
     NDIS_CONFIGURATION_OBJECT</a> structure.


### -param ConfigurationHandle [out]

A pointer to a caller-supplied variable in which 
     <b>NdisOpenConfigurationEx</b> returns a handle to a registry key. The registry key identifies the
     configuration parameters.


## -returns
<b>NdisOpenConfigurationEx</b> returns one of the following status values:
<dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><b>NdisOpenConfigurationEx</b> successfully opened the registry key where the driver's configuration
       parameters are stored.
<dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><b>NdisOpenConfigurationEx</b> failed due to insufficient resources.
<dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><b>NdisOpenConfigurationEx</b> returns NDIS_STATUS_FAILURE if none of the preceding values
       applies.

 


## -remarks
<b>NdisOpenConfigurationEx</b> returns a configuration handle at the 
    <i>ConfigurationHandle</i> parameter. The configuration handle is associated with a registry key that
    identifies the location of the configuration parameters. The caller can pass the configuration handle to
    other NDIS configuration functions to read or write information in the registry.

To access the configuration information, use the configuration handle with the following
    functions:


<a href="netvista.ndisreadconfiguration">NdisReadConfiguration</a>



<a href="netvista.ndiswriteconfiguration">NdisWriteConfiguration</a>



<a href="netvista.ndisopenconfigurationkeybyname">
       NdisOpenConfigurationKeyByName</a>



<a href="netvista.ndisopenconfigurationkeybyindex">
       NdisOpenConfigurationKeyByIndex</a>


The type of registry data that is associated with the configuration handle depends on the type of
    handle that the caller passes to 
    <b>NdisOpenConfigurationEx</b> in the 
    <b>NdisHandle</b> member of the 
    <a href="netvista.ndis_configuration_object">
    NDIS_CONFIGURATION_OBJECT</a> structure that is referenced by the 
    <i>ConfigObject</i> parameter. The handle can identify parameters that are associated with the driver or
    with an instance of the driver.

If the driver obtained the handle in 
    <b>NdisHandle</b> by calling the 
    <a href="netvista.ndismregisterminiportdriver">
    NdisMRegisterMiniportDriver</a> function, 
    <b>NdisOpenConfigurationEx</b> provides a handle to the registry location where the miniport driver's
    configuration parameters are stored. The miniport driver can use the configuration handle until it calls
    the 
    <a href="netvista.ndismderegisterminiportdriver">
    NdisMDeregisterMiniportDriver</a> function.

If the driver obtained the handle in 
    <b>NdisHandle</b> from the 
    <i>MiniportAdapterHandle</i> parameter of the 
    <a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a> function, 
    <b>NdisOpenConfigurationEx</b> provides a handle to the registry location where a miniport adapter's
    configuration parameters are stored. A miniport driver can pass the configuration handle to the 
    <a href="netvista.ndisreadnetworkaddress">NdisReadNetworkAddress</a> function to
    retrieve network address information that can be configured by software and administered locally.
    Miniport drivers can use the configuration handle until NDIS halts the miniport adapter and the 
    <a href="..\ndis\nc-ndis-miniport_halt.md">MiniportHaltEx</a> function returns.

If the driver obtained the handle in 
    <b>NdisHandle</b> by calling the 
    <a href="netvista.ndisregisterprotocoldriver">
    NdisRegisterProtocolDriver</a> function, 
    <b>NdisOpenConfigurationEx</b> provides a handle to the registry location where the protocol driver's
    configuration parameters are stored. The protocol driver can use the configuration handle until it calls
    the 
    <a href="netvista.ndisderegisterprotocoldriver">
    NdisDeregisterProtocolDriver</a> function.

If the handle in 
    <b>NdisHandle</b> is a pointer to an 
    <a href="netvista.ndis_bind_parameters">NDIS_BIND_PARAMETERS</a> structure that
    NDIS passed at the 
    <i>BindParameters</i> parameter of the 
    <a href="..\ndis\nc-ndis-protocol_bind_adapter_ex.md">ProtocolBindAdapterEx</a> function, 
    <b>NdisOpenConfigurationEx</b> provides a handle to the registry location where configuration parameters
    for a protocol binding are stored. Protocol drivers can use the configuration handle until the bind
    operation is complete.

If the driver obtained the handle in 
    <b>NdisHandle</b> by calling the 
    <a href="netvista.ndisopenadapterex">NdisOpenAdapterEx</a> function, 
    <b>NdisOpenConfigurationEx</b> provides a handle to the registry location where the configuration
    parameters for a protocol binding are stored. The protocol driver can use the configuration handle until
    it calls the 
    <a href="netvista.ndiscloseadapterex">NdisCloseAdapterEx</a> function.

If a filter driver obtained the handle in 
    <b>NdisHandle</b> by calling the 
    <a href="netvista.ndisfregisterfilterdriver">
    NdisFRegisterFilterDriver</a> function, 
    <b>NdisOpenConfigurationEx</b> provides a handle to the registry location where the filter driver's
    configuration parameters are stored. Filter drivers can use the configuration handle until they call the 
    <a href="netvista.ndisfderegisterfilterdriver">
    NdisFDeregisterFilterDriver</a> function.

If a filter driver obtained the handle in 
    <b>NdisHandle</b> from the 
    <i>NdisFilterHandle</i> parameter of the 
    <a href="..\ndis\nc-ndis-filter_attach.md">FilterAttach</a> function, 
    <b>NdisOpenConfigurationEx</b> provides a handle to the registry location where a filter modules
    configuration parameters are stored. The filter driver can use the configuration handle until NDIS
    detaches the filter module and the 
    <a href="..\ndis\nc-ndis-filter_detach.md">FilterDetach</a> function returns. If a
    monitoring filter driver specifies the NDIS_CONFIG_FLAG_FILTER_INSTANCE_CONFIGURATION flag in the 
    <b>Flags</b> member of the 
    <a href="netvista.ndis_configuration_object">
    NDIS_CONFIGURATION_OBJECT</a> structure, the driver can access the filter module configuration for a
    specific filter module when there are multiple filter modules configured over the same miniport adapter.
    Modifying filter drivers must not use this flag.

After a driver is done accessing the configuration information, the driver must call the 
    <a href="netvista.ndiscloseconfiguration">NdisCloseConfiguration</a> function to
    release the configuration handle and related resources.


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
Supported in NDIS 6.0 and later.

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
<a href="..\ndis\nc-ndis-filter_attach.md">FilterAttach</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter_detach.md">FilterDetach</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_halt.md">MiniportHaltEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="netvista.ndis_bind_parameters">NDIS_BIND_PARAMETERS</a>
</dt>
<dt>
<a href="netvista.ndis_configuration_object">NDIS_CONFIGURATION_OBJECT</a>
</dt>
<dt>
<a href="netvista.ndiscloseadapterex">NdisCloseAdapterEx</a>
</dt>
<dt>
<a href="netvista.ndiscloseconfiguration">NdisCloseConfiguration</a>
</dt>
<dt>
<a href="netvista.ndisderegisterprotocoldriver">NdisDeregisterProtocolDriver</a>
</dt>
<dt>
<a href="netvista.ndisfderegisterfilterdriver">NdisFDeregisterFilterDriver</a>
</dt>
<dt>
<a href="netvista.ndisfregisterfilterdriver">NdisFRegisterFilterDriver</a>
</dt>
<dt>
<a href="netvista.ndismderegisterminiportdriver">
   NdisMDeregisterMiniportDriver</a>
</dt>
<dt>
<a href="netvista.ndismregisterminiportdriver">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="netvista.ndisopenadapterex">NdisOpenAdapterEx</a>
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
<a href="netvista.ndisregisterprotocoldriver">NdisRegisterProtocolDriver</a>
</dt>
<dt>
<a href="netvista.ndiswriteconfiguration">NdisWriteConfiguration</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_bind_adapter_ex.md">ProtocolBindAdapterEx</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NdisOpenConfigurationEx function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

