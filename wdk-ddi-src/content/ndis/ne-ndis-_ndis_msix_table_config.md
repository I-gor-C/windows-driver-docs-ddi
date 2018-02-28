---
UID: NE:ndis._NDIS_MSIX_TABLE_CONFIG
title: "_NDIS_MSIX_TABLE_CONFIG"
author: windows-driver-content
description: The NDIS_MSIX_TABLE_OPERATION enumeration identifies the type of MSI-X configuration operation.
old-location: netvista\ndis_msix_table_operation.htm
old-project: netvista
ms.assetid: 7d1a4bb6-5db8-48b0-9be3-7468360951a1
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: "*PNDIS_MSIX_TABLE_OPERATION, NDIS_MSIX_TABLE_OPERATION, NDIS_MSIX_TABLE_OPERATION enumeration [Network Drivers Starting with Windows Vista], NdisMSIXTableConfigMaskTableEntry, NdisMSIXTableConfigMax, NdisMSIXTableConfigSetTableEntry, NdisMSIXTableConfigUnmaskTableEntry, PNDIS_MSIX_TABLE_OPERATION, PNDIS_MSIX_TABLE_OPERATION enumeration pointer [Network Drivers Starting with Windows Vista], _NDIS_MSIX_TABLE_CONFIG, ndis/NDIS_MSIX_TABLE_OPERATION, ndis/NdisMSIXTableConfigMaskTableEntry, ndis/NdisMSIXTableConfigMax, ndis/NdisMSIXTableConfigSetTableEntry, ndis/NdisMSIXTableConfigUnmaskTableEntry, ndis/PNDIS_MSIX_TABLE_OPERATION, ndis_msix_ref_b315600c-7d23-4251-bcdb-560c46d5fa79.xml, netvista.ndis_msix_table_operation"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.1 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ndis.h
api_name:
-	NDIS_MSIX_TABLE_OPERATION
product: Windows
targetos: Windows
req.typenames: NDIS_MSIX_TABLE_OPERATION, *PNDIS_MSIX_TABLE_OPERATION
---

# _NDIS_MSIX_TABLE_CONFIG Enumeration
The NDIS_MSIX_TABLE_OPERATION enumeration identifies the type of MSI-X configuration
  operation.

## Syntax
````
typedef enum _NDIS_MSIX_TABLE_CONFIG { 
  NdisMSIXTableConfigSetTableEntry,
  NdisMSIXTableConfigMaskTableEntry,
  NdisMSIXTableConfigUnmaskTableEntry,
  NdisMSIXTableConfigMax
} NDIS_MSIX_TABLE_OPERATION, *PNDIS_MSIX_TABLE_OPERATION;
````

## Constants

<table>
            
                <tr>
                    <td>NdisMSIXTableConfigMaskTableEntry</td>
                    <td>The interrupts from an MSI-X table entry source should be masked.</td>
                </tr>
            
                <tr>
                    <td>NdisMSIXTableConfigMax</td>
                    <td>The number of enumeration values in NDIS_MSIX_TABLE_OPERATION.</td>
                </tr>
            
                <tr>
                    <td>NdisMSIXTableConfigSetTableEntry</td>
                    <td>The MSI-X table entry should be mapped to an MSI-X message that the bus driver allocated to the
     device.</td>
                </tr>
            
                <tr>
                    <td>NdisMSIXTableConfigUnmaskTableEntry</td>
                    <td>The interrupts from an MSI-X table entry source should be unmasked.</td>
                </tr>
</table>

## Remarks

The NDIS_MSIX_TABLE_OPERATION enumeration is used in the 
    <a href="..\ndis\ns-ndis-_ndis_msix_config_parameters.md">
    NDIS_MSIX_CONFIG_PARAMETERS</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.1 and later. Supported in NDIS 6.1 and later. |
| **Header** | ndis.h (include Ndis.h) |

## See Also

<a href="..\ndis\ns-ndis-_ndis_msix_config_parameters.md">NDIS_MSIX_CONFIG_PARAMETERS</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_MSIX_TABLE_OPERATION enumeration%20 RELEASE:%20(2/16/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>