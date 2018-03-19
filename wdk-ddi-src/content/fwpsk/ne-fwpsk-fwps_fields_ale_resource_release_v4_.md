---
UID: NE:fwpsk.FWPS_FIELDS_ALE_RESOURCE_RELEASE_V4_
title: FWPS_FIELDS_ALE_RESOURCE_RELEASE_V4_
author: windows-driver-content
description: The FWPS_FIELDS_ALE_RESOURCE_RELEASE_V4 enumeration type specifies the data field identifiers for the FWPS_LAYER_ALE_RESOURCE_RELEASE_V4 run-time filtering layer.
old-location: netvista\fwps_fields_ale_resource_release_v4.htm
old-project: netvista
ms.assetid: ad3d3099-58eb-4a34-b15c-a323dcedba84
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: FWPS_FIELDS_ALE_RESOURCE_RELEASE_V4, FWPS_FIELDS_ALE_RESOURCE_RELEASE_V4 enumeration [Network Drivers Starting with Windows Vista], FWPS_FIELDS_ALE_RESOURCE_RELEASE_V4_, FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_ALE_APP_ID, FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_ALE_PACKAGE_ID, FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_ALE_USER_ID, FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_FLAGS, FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_LOCAL_ADDRESS, FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_LOCAL_ADDRESS_TYPE, FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_LOCAL_INTERFACE, FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_LOCAL_PORT, FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_PROTOCOL, FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_MAX, fwpsk/FWPS_FIELDS_ALE_RESOURCE_RELEASE_V4, fwpsk/FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_ALE_APP_ID, fwpsk/FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_ALE_PACKAGE_ID, fwpsk/FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_ALE_USER_ID, fwpsk/FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_FLAGS, fwpsk/FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_LOCAL_ADDRESS, fwpsk/FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_LOCAL_ADDRESS_TYPE, fwpsk/FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_LOCAL_INTERFACE, fwpsk/FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_LOCAL_PORT, fwpsk/FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_PROTOCOL, fwpsk/FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_MAX, netvista.fwps_fields_ale_resource_release_v4, wfp_ref_5_const_3_data_fields_09378323-ec5f-4db4-89d3-8398e4b76fac.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 7.
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
req.irql: "<= DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	fwpsk.h
api_name:
-	FWPS_FIELDS_ALE_RESOURCE_RELEASE_V4
product: Windows
targetos: Windows
req.typenames: FWPS_FIELDS_ALE_RESOURCE_RELEASE_V4
---

# FWPS_FIELDS_ALE_RESOURCE_RELEASE_V4_ Enumeration
The FWPS_FIELDS_ALE_RESOURCE_RELEASE_V4 enumeration type specifies the data field identifiers for the
  FWPS_LAYER_ALE_RESOURCE_RELEASE_V4 
  <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/aa366492">run-time filtering layer</a>.

## Syntax
````
typedef enum FWPS_FIELDS_ALE_RESOURCE_RELEASE_V4_ { 
  FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_ALE_APP_ID,
  FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_ALE_USER_ID,
  FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_LOCAL_ADDRESS,
  FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_LOCAL_ADDRESS_TYPE,
  FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_LOCAL_PORT,
  FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_PROTOCOL,
  FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_LOCAL_INTERFACE,
  FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_FLAGS,
#if (NTDDI_VERSION >= NTDDI_WIN8)
  FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_ALE_PACKAGE_ID,
#endif 
  FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_MAX
} FWPS_FIELDS_ALE_RESOURCE_RELEASE_V4;
````

## Constants

<table>
            
                <tr>
                    <td>FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_ALE_APP_ID</td>
                    <td>The full path of the application.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_ALE_USER_ID</td>
                    <td>The identifier of the local user.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_LOCAL_ADDRESS</td>
                    <td>The local IP address.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_LOCAL_ADDRESS_TYPE</td>
                    <td>The local IP address type. The possible values are defined by the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568757">NL_ADDRESS_TYPE</a> enumeration.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_LOCAL_PORT</td>
                    <td>The local transport protocol port number.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_PROTOCOL</td>
                    <td>The IP protocol number, as specified in RFC 1700.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_IP_LOCAL_INTERFACE</td>
                    <td>The locally unique identifier (<a href="..\igpupvdev\ns-igpupvdev-_luid.md">LUID</a>) for the network interface associated with the
     local IP address.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_FLAGS</td>
                    <td>A bitwise OR of a combination of filtering condition flags. For information about the possible
     flags, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff549942">Filtering Condition Flags</a>.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_ALE_PACKAGE_ID</td>
                    <td>The package identifier is a security identifier (SID) that identifies the associated AppContainer process. For more information about the SID structure, see the description for the SID structure in the Microsoft Windows SDK documentation.

<div class="alert"><b>Note</b>  Supported starting with Windows 8.</div>
<div> </div></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_ALE_SECURITY_ATTRIBUTE_FQBN_VALUE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_COMPARTMENT_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_ALE_RESOURCE_RELEASE_V4_MAX</td>
                    <td>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 7. Supported starting with Windows 7. |
| **Header** | fwpsk.h (include Fwpsk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff568757">NL_ADDRESS_TYPE</a>



<a href="..\igpupvdev\ns-igpupvdev-_luid.md">LUID</a>