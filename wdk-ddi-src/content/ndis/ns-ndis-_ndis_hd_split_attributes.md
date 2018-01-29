---
UID : NS:ndis._NDIS_HD_SPLIT_ATTRIBUTES
title : _NDIS_HD_SPLIT_ATTRIBUTES
author : windows-driver-content
description : The NDIS_HD_SPLIT_ATTRIBUTES structure defines header-data split attributes, if any, that are associated with a miniport adapter.
old-location : netvista\ndis_hd_split_attributes.htm
old-project : netvista
ms.assetid : c3e28d66-1fe8-4cb0-ada0-4292387da19a
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : NDIS_HD_SPLIT_ATTRIBUTES, *PNDIS_HD_SPLIT_ATTRIBUTES, ndis/PNDIS_HD_SPLIT_ATTRIBUTES, netvista.ndis_hd_split_attributes, NDIS_HD_SPLIT_ATTRIBUTES structure [Network Drivers Starting with Windows Vista], PNDIS_HD_SPLIT_ATTRIBUTES, header_data_split_ref_32bcb512-6620-48a5-8073-7b9ef0ef1f18.xml, ndis/NDIS_HD_SPLIT_ATTRIBUTES, _NDIS_HD_SPLIT_ATTRIBUTES, PNDIS_HD_SPLIT_ATTRIBUTES structure pointer [Network Drivers Starting with Windows Vista]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ndis.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.1 and later.
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
req.irql : See Remarks section
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : NDIS_HD_SPLIT_ATTRIBUTES, *PNDIS_HD_SPLIT_ATTRIBUTES
---

# _NDIS_HD_SPLIT_ATTRIBUTES structure
The NDIS_HD_SPLIT_ATTRIBUTES structure defines header-data split attributes, if any, that are
  associated with a miniport adapter.

## Syntax
````
typedef struct _NDIS_HD_SPLIT_ATTRIBUTES {
  NDIS_OBJECT_HEADER Header;
  ULONG              HardwareCapabilities;
  ULONG              CurrentCapabilities;
  ULONG              HDSplitFlags;
  ULONG              BackfillSize;
  ULONG              MaxHeaderSize;
} NDIS_HD_SPLIT_ATTRIBUTES, *PNDIS_HD_SPLIT_ATTRIBUTES;
````

## Members


`BackfillSize`

The backfill size, in bytes, for the data portion of a split frame. The miniport driver should set
     
     <b>BackfillSize</b> to zero before calling 
     <b>NdisMSetMiniportAttributes</b>. NDIS sets this member if the miniport driver must pre-allocate
     backfill storage in the data portion for split frames. After 
     <b>NdisMSetMiniportAttributes</b> successfully returns, the driver must use the 
     <b>BackfillSize</b> value that NDIS set to pre-allocate the data buffers.

`CurrentCapabilities`

The current header-data split capabilities that the miniport adapter supports. The miniport driver
     uses the same flags that are defined for the 
     <b>HardwareCapabilities</b> member. In this case, the flags are set to indicate the current capabilities
     that depend on the current configuration settings.

`HardwareCapabilities`

The header-data split hardware capabilities that the miniport adapter supports. These capabilities
     should include capabilities that are currently disabled by INF file settings or through the 
     <b>Advanced</b> properties page. The value of 
     <b>HardwareCapabilities</b> is a bitwise OR of the following flags:

`HDSplitFlags`

A set of flags that control the status of header-data split for a miniport adapter. The miniport
     driver should set this member to zero before calling the 
     <mshelp:link keywords="netvista.ndismsetminiportattributes" tabindex="0"><b>
     NdisMSetMiniportAttributes</b></mshelp:link> function. After 
     <b>NdisMSetMiniportAttributes</b> successfully returns, the driver must check the flags and configure the
     hardware accordingly. NDIS sets this member with a bitwise OR of the following flags:

`Header`

The 
     <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure for the
     provider characteristics structure (NDIS_HD_SPLIT_ATTRIBUTES). The driver sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_HD_SPLIT_ATTRIBUTES, the 
     <b>Revision</b> member to NDIS_OBJECT_HD_SPLIT_ATTRIBUTES_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_HD_SPLIT_ATTRIBUTES_REVISION_1.

`MaxHeaderSize`

The maximum size, in bytes, for the header portion of a split frame. The miniport driver should
     set 
     <b>MaxHeaderSize</b> to zero before calling 
     <b>NdisMSetMiniportAttributes</b>. NDIS sets this member to the maximum size for the header buffer for
     split frames. After 
     <b>NdisMSetMiniportAttributes</b> successfully returns, the driver must use the value that NDIS provided.
     
     
<div class="alert"><b>Note</b>  If the length of a header exceeds 
     <b>MaxHeaderSize</b> because of the presence of IPv4 options, IPSec headers, or IPv6 extension headers,
     the frame must not be split. If a header that includes a TCP or UDP header exceeds 
     <b>MaxHeaderSize</b> because of the presence of TCP header, TCP options, or UDP header, the NIC must
     split the frame at the beginning of the upper layer protocol header or must not split the
     frame.</div><div> </div>

## Remarks
To support header-data split, a miniport driver passes a pointer to an 
    <mshelp:link keywords="netvista.ndis_miniport_adapter_hardware_assist_attributes" tabindex="0"><b>
    NDIS_MINIPORT_ADAPTER_HARDWARE_ASSIST_ATTRIBUTES</b></mshelp:link> structure in the 
    <i>MiniportAttributes</i> parameter of the 
    <mshelp:link keywords="netvista.ndismsetminiportattributes" tabindex="0"><b>
    NdisMSetMiniportAttributes</b></mshelp:link> function. The 
    <b>HDSplitAttributes</b> member of NDIS_MINIPORT_ADAPTER_HARDWARE_ASSIST_ATTRIBUTES contains a pointer to
    the NDIS_HD_SPLIT_ATTRIBUTES structure. A miniport driver calls 
    <b>NdisMSetMiniportAttributes</b> from its 
    <a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a> function
    during initialization.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ndis.h (include Ndis.h) |

## See Also

<a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>

<a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">NdisMSetMiniportAttributes</a>

<a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a>

<mshelp:link keywords="netvista.ndis_miniport_adapter_hardware_assist_attributes" tabindex="0"><b>
   NDIS_MINIPORT_ADAPTER_HARDWARE_ASSIST_ATTRIBUTES</b></mshelp:link>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_HD_SPLIT_ATTRIBUTES structure%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>