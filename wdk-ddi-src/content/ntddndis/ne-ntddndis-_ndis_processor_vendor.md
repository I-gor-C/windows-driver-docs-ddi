---
UID : NE:ntddndis._NDIS_PROCESSOR_VENDOR
title : _NDIS_PROCESSOR_VENDOR
author : windows-driver-content
description : The NDIS_PROCESSOR_VENDOR enumeration identifies a processor vendor.
old-location : netvista\ndis_processor_vendor.htm
old-project : netvista
ms.assetid : c2d1b967-32fb-437a-a0bd-e0028acee022
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : ntddndis/NdisProcessorVendorAuthenticAMD, PNDIS_PROCESSOR_VENDOR, ndis_sysinfo_ref_7037b548-2ccc-4f39-9b34-33002f811bf1.xml, ntddndis/NdisProcessorVendorUnknown, ntddndis/NDIS_PROCESSOR_VENDOR, NDIS_PROCESSOR_VENDOR enumeration [Network Drivers Starting with Windows Vista], NdisProcessorVendorUnknown, ntddndis/NdisProcessorVendorGenuinIntel, ntddndis/PNDIS_PROCESSOR_VENDOR, PNDIS_PROCESSOR_VENDOR enumeration pointer [Network Drivers Starting with Windows Vista], NdisProcessorVendorGenuinIntel, _NDIS_PROCESSOR_VENDOR, NDIS_PROCESSOR_VENDOR, NdisProcessorVendorAuthenticAMD, netvista.ndis_processor_vendor, *PNDIS_PROCESSOR_VENDOR
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntddndis.h
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
req.typenames : "*PNDIS_PROCESSOR_VENDOR, NDIS_PROCESSOR_VENDOR"
---

# _NDIS_PROCESSOR_VENDOR Enumeration
The NDIS_PROCESSOR_VENDOR enumeration identifies a processor vendor.

## Syntax
````
typedef enum _NDIS_PROCESSOR_VENDOR { 
  NdisProcessorVendorUnknown,
  NdisProcessorVendorGenuinIntel,
  NdisProcessorVendorAuthenticAMD
} NDIS_PROCESSOR_VENDOR, *PNDIS_PROCESSOR_VENDOR;
````

## Constants

<table>

<tr>
<td>NdisProcessorVendorAuthenticAMD</td>
<td>The processor vendor is AMD.</td>
</tr>

<tr>
<td>NdisProcessorVendorGenuineIntel</td>
<td></td>
</tr>

<tr>
<td>NdisProcessorVendorGenuinIntel</td>
<td>The processor vendor is Intel.</td>
</tr>

<tr>
<td>NdisProcessorVendorUnknown</td>
<td>The processor vendor is unknown.</td>
</tr>
</table>

## Remarks

The NDIS_PROCESSOR_VENDOR enumeration is used in the 
    <mshelp:link keywords="netvista.ndis_system_processor_info" tabindex="0"><b>
    NDIS_SYSTEM_PROCESSOR_INFO</b></mshelp:link> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddndis.h (include Ndis.h) |

## See Also

<a href="..\ndis\ns-ndis-_ndis_system_processor_info.md">NDIS_SYSTEM_PROCESSOR_INFO</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PROCESSOR_VENDOR enumeration%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>