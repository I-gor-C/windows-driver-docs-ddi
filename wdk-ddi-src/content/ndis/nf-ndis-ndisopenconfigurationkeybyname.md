---
UID: NF.ndis.NdisOpenConfigurationKeyByName
title: NdisOpenConfigurationKeyByName function
author: windows-driver-content
description: The NdisOpenConfigurationKeyByName function opens a named subkey of a given open registry key that is designated by a caller-supplied handle.
old-location: netvista\ndisopenconfigurationkeybyname.htm
old-project: netvista
ms.assetid: 9ce7f40f-28f1-4303-9f7a-24ff1213bab1
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NdisOpenConfigurationKeyByName
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see       NdisOpenConfigurationKeyByName (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see       NdisOpenConfigurationKeyByName (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisOpenConfigurationKeyByName
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miscellaneous_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: < DISPATCH_LEVEL
---

# NdisOpenConfigurationKeyByName function



## -description
The 
  <b>NdisOpenConfigurationKeyByName</b> function opens a named subkey of a given open registry key that is
  designated by a caller-supplied handle.


## -syntax

````
VOID NdisOpenConfigurationKeyByName(
  _Out_ PNDIS_STATUS Status,
  _In_  NDIS_HANDLE  ConfigurationHandle,
  _In_  PNDIS_STRING SubKeyName,
  _Out_ PNDIS_HANDLE SubKeyHandle
);
````


## -parameters

### -param Status [out]

A pointer to a caller-supplied variable in which this function returns the status of its attempt
     to open the registry key. Possible return values are one of the following:
     


### -param NDIS_STATUS_SUCCESS

NDIS has initialized accessed to the subkey specified by 
       <i>SubKeyName</i> .

### -param NDIS_STATUS_FAILURE

The key could not be opened.
</dd>
</dl>

### -param ConfigurationHandle [in]

The handle to a registry key for which a subkey should be opened. Typically, 
     <i>ConfigurationHandle</i> is returned by the 
     <a href="netvista.ndisopenconfigurationex">
     NdisOpenConfigurationEx</a> function.

### -param SubKeyName [in]

A pointer to an NDIS_STRING type containing a caller-supplied, counted string in the
     system-default character set that specifies the name of the registry subkey to open. For Microsoft
     Windows 2000 and later drivers, this string contains Unicode characters. That is, for Windows 2000 and
     later, NDIS defines the NDIS_STRING type as a 
     <a href="kernel.unicode_string">UNICODE_STRING</a> type.

### -param SubKeyHandle [out]

A pointer to a caller-supplied variable in which this function returns a handle to the opened
     subkey if this call is successful.

## -returns
None

## -remarks
<b>NdisOpenConfigurationKeyByName</b> allows a driver to access configuration information that is stored
    in a named subkey in the registry.

Note that the 
    <i>ConfigurationHandle</i> passed in to 
    <b>NdisOpenConfigurationKeyByName</b> can be any valid handle to a registry key already opened by the
    caller. 
    <b>NdisOpenConfigurationKeyByName</b> returns configuration information for subkeys relative to any valid 
    <i>ConfigurationHandle</i> .

After a driver has consumed and, possibly, modified the registry configuration information, it must
    call the 
    <a href="netvista.ndiscloseconfiguration">NdisCloseConfiguration</a> function to
    release the handle that was obtained from 
    <b>NdisOpenConfigurationKeyByName</b>. 
    <b>NdisCloseConfiguration</b> also frees any temporary storage that NDIS allocated in the driver's calls
    to the 
    <a href="netvista.ndisreadconfiguration">NdisReadConfiguration</a>, 
    <a href="netvista.ndisreadnetworkaddress">NdisReadNetworkAddress</a>, or 
    <a href="netvista.ndiswriteconfiguration">NdisWriteConfiguration</a> functions
    with the 
    <i>SubKeyHandle</i> that 
    <b>NdisOpenConfigurationKeyByName</b> returned.

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
   <a href="https://msdn.microsoft.com/a820440c-6186-4172-a567-843d89e49ad5">
   NdisOpenConfigurationKeyByName (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>
   NdisOpenConfigurationKeyByName (NDIS 5.1)</b>) in Windows XP.
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
&lt; DISPATCH_LEVEL
</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules
</th>
<td width="70%">
<a href="devtest.ndis_irql_miscellaneous_function">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.ansi_string">ANSI_STRING</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="netvista.ndiscloseconfiguration">NdisCloseConfiguration</a>
</dt>
<dt>
<a href="netvista.ndisopenconfigurationex">NdisOpenConfigurationEx</a>
</dt>
<dt>
<a href="netvista.ndisopenconfigurationkeybyindex">
   NdisOpenConfigurationKeyByIndex</a>
</dt>
<dt>
<a href="netvista.ndisreadconfiguration">NdisReadConfiguration</a>
</dt>
<dt>
<a href="netvista.ndiswriteconfiguration">NdisWriteConfiguration</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_bind_adapter_ex.md">ProtocolBindAdapterEx</a>
</dt>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisOpenConfigurationKeyByName function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
