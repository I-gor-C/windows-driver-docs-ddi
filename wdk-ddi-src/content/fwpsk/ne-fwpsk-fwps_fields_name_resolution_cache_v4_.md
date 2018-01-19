---
UID : NE:fwpsk.FWPS_FIELDS_NAME_RESOLUTION_CACHE_V4_
title : FWPS_FIELDS_NAME_RESOLUTION_CACHE_V4_
author : windows-driver-content
description : The FWPS_FIELDS_NAME_RESOLUTION_CACHE_V4 enumeration type specifies the data field identifiers for the FWPS_LAYER_NAME_RESOLUTION_CACHE_V4 run-time filtering layer.
old-location : netvista\fwps_fields_name_resolution_cache_v4.htm
old-project : netvista
ms.assetid : 9e999c4d-381d-4106-8eeb-e6974e2f8a22
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : FWPS_FIELDS_NAME_RESOLUTION_CACHE_V4_, FWPS_FIELDS_NAME_RESOLUTION_CACHE_V4
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : fwpsk.h
req.include-header : Fwpsk.h
req.target-type : Windows
req.target-min-winverclnt : Supported starting withn Windows 7.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : FWPS_FIELDS_NAME_RESOLUTION_CACHE_V4
req.alt-loc : fwpsk.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : <= DISPATCH_LEVEL
req.typenames : FWPS_FIELDS_NAME_RESOLUTION_CACHE_V4
---

# FWPS_FIELDS_NAME_RESOLUTION_CACHE_V4_ Enumeration
The FWPS_FIELDS_NAME_RESOLUTION_CACHE_V4 enumeration type specifies the data field identifiers for
  the FWPS_LAYER_NAME_RESOLUTION_CACHE_V4 
  <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/aa366492">run-time filtering layer</a>.

## Syntax
````
typedef enum FWPS_FIELDS_NAME_RESOLUTION_CACHE_V4_ { 
  FWPS_FIELD_NAME_RESOLUTION_CACHE_V4_ALE_USER_ID,
  FWPS_FIELD_NAME_RESOLUTION_CACHE_V4_ALE_APP_ID,
  FWPS_FIELD_NAME_RESOLUTION_CACHE_V4_IP_REMOTE_ADDRESS,
  FWPS_FIELD_NAME_RESOLUTION_CACHE_V4_PEER_NAME,
  FWPS_FIELD_NAME_RESOLUTION_CACHE_V4_MAX
} FWPS_FIELDS_NAME_RESOLUTION_CACHE_V4;
````

## Constants

<table>

<tr>
<td>FWPS_FIELD_NAME_RESOLUTION_CACHE_V4_ALE_APP_ID</td>
<td>The full path of the application.</td>
</tr>

<tr>
<td>FWPS_FIELD_NAME_RESOLUTION_CACHE_V4_ALE_USER_ID</td>
<td>The identifier of the local user.</td>
</tr>

<tr>
<td>FWPS_FIELD_NAME_RESOLUTION_CACHE_V4_IP_REMOTE_ADDRESS</td>
<td>The remote IP address.</td>
</tr>

<tr>
<td>FWPS_FIELD_NAME_RESOLUTION_CACHE_V4_MAX</td>
<td>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</td>
</tr>

<tr>
<td>FWPS_FIELD_NAME_RESOLUTION_CACHE_V4_PEER_NAME</td>
<td>The machine name that is associated with the destination IP address.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | fwpsk.h (include Fwpsk.h) |