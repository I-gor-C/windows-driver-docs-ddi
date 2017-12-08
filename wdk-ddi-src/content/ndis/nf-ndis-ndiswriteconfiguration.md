---
UID: NF.ndis.NdisWriteConfiguration
title: NdisWriteConfiguration function
author: windows-driver-content
description: The NdisWriteConfiguration function writes a caller-supplied value for a specified entry into the registry. This function must be invoked serially with respect to itself and the NdisReadConfiguration function.
old-location: netvista\ndiswriteconfiguration.htm
old-project: netvista
ms.assetid: 63c94f4d-1c8c-43c2-ae58-993da42a80a4
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NdisWriteConfiguration
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisWriteConfiguration (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisWriteConfiguration (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisWriteConfiguration
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
req.irql: PASSIVE_LEVEL
---

# NdisWriteConfiguration function



## -description
The 
  <b>NdisWriteConfiguration</b> function writes a caller-supplied value for a specified entry into the
  registry. This function must be invoked serially with respect to itself and the <a href="netvista.ndisreadconfiguration">NdisReadConfiguration</a> function.


## -syntax

````
VOID NdisWriteConfiguration(
  _Out_ PNDIS_STATUS                  Status,
  _In_  NDIS_HANDLE                   ConfigurationHandle,
  _In_  PNDIS_STRING                  Keyword,
  _In_  PNDIS_CONFIGURATION_PARAMETER ParameterValue
);
````


## -parameters

### -param Status [out]

A pointer to a caller-supplied variable in which this function returns the status of the call as
     one of the following:
     


### -param NDIS_STATUS_SUCCESS

The supplied value at 
       <i>ParameterValue</i> was written into the registry. If this is a new entry, the name at 
       <i>Keyword</i> also was written into the registry.

### -param NDIS_STATUS_NOT_SUPPORTED

The supplied 
       <b>ParameterType</b> is invalid.

### -param NDIS_STATUS_RESOURCES

NDIS could not allocate resources, usually enough memory, to transfer the requested information
       to the registry.

### -param NDIS_STATUS_FAILURE

The requested information could not be written.
</dd>
</dl>

### -param ConfigurationHandle [in]

The handle to a registry key that was returned by the 
     <a href="netvista.ndisopenconfigurationex">NdisOpenConfigurationEx</a>, 
     <a href="netvista.ndisopenconfigurationkeybyindex">
     NdisOpenConfigurationKeyByIndex</a>, or 
     <a href="netvista.ndisopenconfigurationkeybyname">
     NdisOpenConfigurationKeyByName</a> function.

### -param Keyword [in]

A pointer to an NDIS_STRING type describing a caller-supplied counted string, in the
     system-default character set, specifying the name of an entry for which to write the value. For
     Microsoft Windows 2000 and later drivers, this string contains Unicode characters. That is, for Windows
     2000 and later, NDIS defines the NDIS_STRING type as a 
     <a href="kernel.unicode_string">UNICODE_STRING</a> type.

### -param ParameterValue [in]

Pointer to a caller-supplied 
     <a href="netvista.ndis_configuration_parameter">
     NDIS_CONFIGURATION_PARAMETER</a> structure.

## -returns
None

## -remarks
If an entry of the same name as at 
    <i>Keyword</i> already exists under the opened registry key, 
    <b>NdisWriteConfiguration</b> replaces its current value with the caller-supplied value. Otherwise, 
    <b>NdisWriteConfiguration</b> adds a new value entry with the given name and supplied value to the
    registry.

In the configuration registry of Windows 2000 and later versions, an NDIS 
    <i>Keyword</i> is a synonym for a
    <i>value entry name</i>. Such a name is a counted sequence of Unicode characters, terminated with a
    NUL.

<b>NdisWriteConfiguration</b> buffers and copies the caller-supplied string at 
    <i>Keyword</i> and the caller-supplied data specified at 
    <i>ParameterValue</i> . This memory is freed when the driver releases the 
    <i>ConfigurationHandle</i> with the 
    <a href="netvista.ndiscloseconfiguration">NdisCloseConfiguration</a> function.
    The caller of 
    <b>NdisWriteConfiguration</b> is responsible for releasing the buffered string at 
    <i>Keyword</i> and the memory allocated for the 
    <a href="netvista.ndis_configuration_parameter">
    NDIS_CONFIGURATION_PARAMETER</a> structure.

As an alternative to calling 
    <b>NdisWriteConfiguration</b>, every NDIS driver can set up configuration information in the registry for
    itself using the AddReg directive in the driver's INF file.

For more information about setup and installation files for Windows 2000 and later versions, see 
    <a href="devinst.overview_of_device_and_driver_installation">Device Installation
    Overview</a>.

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
   <a href="https://msdn.microsoft.com/c6d956fc-b634-4ca6-8597-ceeb1cd8d94f">NdisWriteConfiguration (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisWriteConfiguration (NDIS
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
<a href="netvista.ndis_configuration_parameter">NDIS_CONFIGURATION_PARAMETER</a>
</dt>
<dt>
<a href="netvista.ndisansistringtounicodestring">
   NdisAnsiStringToUnicodeString</a>
</dt>
<dt>
<a href="netvista.ndiscloseconfiguration">NdisCloseConfiguration</a>
</dt>
<dt>
<a href="netvista.ndisfreememory">NdisFreeMemory</a>
</dt>
<dt>
<a href="netvista.ndisfreestring">NdisFreeString</a>
</dt>
<dt>
<a href="netvista.ndisinitansistring">NdisInitAnsiString</a>
</dt>
<dt>
<a href="netvista.ndisinitializestring">NdisInitializeString</a>
</dt>
<dt>
<a href="netvista.ndisinitunicodestring">NdisInitUnicodeString</a>
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
<a href="netvista.ndisunicodestringtoansistring">
   NdisUnicodeStringToAnsiString</a>
</dt>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisWriteConfiguration function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
