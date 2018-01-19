---
UID : NE:fwpsk.FWPS_FIELDS_OUTBOUND_MAC_FRAME_NATIVE_
title : FWPS_FIELDS_OUTBOUND_MAC_FRAME_NATIVE_
author : windows-driver-content
description : The FWPS_FIELDS_OUTBOUND_MAC_FRAME_NATIVE enumeration type specifies the data field identifiers for the FWPS_LAYER_OUTBOUND_MAC_FRAME_NATIVE run-time filtering layer.
old-location : netvista\fwps_fields_outbound_mac_frame_native.htm
old-project : netvista
ms.assetid : 71244290-3DCD-45AF-9EF0-AD1C9103A69C
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : FWPS_FIELDS_OUTBOUND_MAC_FRAME_NATIVE_, FWPS_FIELDS_OUTBOUND_MAC_FRAME_NATIVE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : fwpsk.h
req.include-header : Fwpsk.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : FWPS_FIELDS_OUTBOUND_MAC_FRAME_NATIVE
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
req.typenames : FWPS_FIELDS_OUTBOUND_MAC_FRAME_NATIVE
---

# FWPS_FIELDS_OUTBOUND_MAC_FRAME_NATIVE_ Enumeration
The FWPS_FIELDS_OUTBOUND_MAC_FRAME_NATIVE enumeration type specifies the data field identifiers for the
  FWPS_LAYER_OUTBOUND_MAC_FRAME_NATIVE 
  <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/aa366492">run-time filtering layer</a>.

## Syntax
````
typedef enum  { 
  FWPS_FIELD_OUTBOUND_MAC_FRAME_NATIVE_NDIS_MEDIA_TYPE,
  FWPS_FIELD_OUTBOUND_MAC_FRAME_NATIVE_NDIS_PHYSICAL_MEDIA_TYPE,
  FWPS_FIELD_OUTBOUND_MAC_FRAME_NATIVE_INTERFACE,
  FWPS_FIELD_OUTBOUND_MAC_FRAME_NATIVE_INTERFACE_TYPE,
  FWPS_FIELD_OUTBOUND_MAC_FRAME_NATIVE_INTERFACE_INDEX,
  FWPS_FIELD_OUTBOUND_MAC_FRAME_NATIVE_NDIS_PORT,
  FWPS_FIELD_OUTBOUND_MAC_FRAME_NATIVE_FLAGS,
  FWPS_FIELD_OUTBOUND_MAC_FRAME_NATIVE_MAX
} FWPS_FIELDS_OUTBOUND_MAC_FRAME_NATIVE;
````

## Constants

<table>

<tr>
<td>FWPS_FIELD_OUTBOUND_MAC_FRAME_NATIVE_INTERFACE</td>
<td>The outbound MAC frame native interface field.</td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_MAC_FRAME_NATIVE_INTERFACE_INDEX</td>
<td>The outbound MAC frame native interface index field.</td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_MAC_FRAME_NATIVE_INTERFACE_TYPE</td>
<td>The outbound MAC frame native interface type field.</td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_MAC_FRAME_NATIVE_MAX</td>
<td>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_MAC_FRAME_NATIVE_NDIS_MEDIA_TYPE</td>
<td>The outbound MAC frame native NDIS media type field.</td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_MAC_FRAME_NATIVE_NDIS_PHYSICAL_MEDIA_TYPE</td>
<td>The outbound MAC frame native NDIS physical media type field.</td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_MAC_FRAME_NATIVE_NDIS_PORT</td>
<td>The outbound MAC frame native NDIS port field.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | fwpsk.h (include Fwpsk.h) |