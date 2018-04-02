---
UID: NE:fwpsk.FWPS_FIELDS_STREAM_V4_
title: FWPS_FIELDS_STREAM_V4_
author: windows-driver-content
description: The FWPS_FIELDS_STREAM_V4 enumeration type specifies the data field identifiers for the FWPS_LAYER_STREAM_V4 and FWPS_LAYER_STREAM_V4_DISCARD run-time filtering layers.
old-location: netvista\fwps_fields_stream_v4.htm
old-project: netvista
ms.assetid: 1225f28d-3b89-4b14-82c3-5162de9fe8fd
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: FWPS_FIELDS_STREAM_V4, FWPS_FIELDS_STREAM_V4 enumeration [Network Drivers Starting with Windows Vista], FWPS_FIELDS_STREAM_V4_, FWPS_FIELD_STREAM_V4_DIRECTION, FWPS_FIELD_STREAM_V4_FLAGS, FWPS_FIELD_STREAM_V4_IP_LOCAL_ADDRESS, FWPS_FIELD_STREAM_V4_IP_LOCAL_ADDRESS_TYPE, FWPS_FIELD_STREAM_V4_IP_LOCAL_PORT, FWPS_FIELD_STREAM_V4_IP_REMOTE_ADDRESS, FWPS_FIELD_STREAM_V4_IP_REMOTE_PORT, FWPS_FIELD_STREAM_V4_MAX, fwpsk/FWPS_FIELDS_STREAM_V4, fwpsk/FWPS_FIELD_STREAM_V4_DIRECTION, fwpsk/FWPS_FIELD_STREAM_V4_FLAGS, fwpsk/FWPS_FIELD_STREAM_V4_IP_LOCAL_ADDRESS, fwpsk/FWPS_FIELD_STREAM_V4_IP_LOCAL_ADDRESS_TYPE, fwpsk/FWPS_FIELD_STREAM_V4_IP_LOCAL_PORT, fwpsk/FWPS_FIELD_STREAM_V4_IP_REMOTE_ADDRESS, fwpsk/FWPS_FIELD_STREAM_V4_IP_REMOTE_PORT, fwpsk/FWPS_FIELD_STREAM_V4_MAX, netvista.fwps_fields_stream_v4, wfp_ref_5_const_3_data_fields_767d81c5-f927-4512-812d-396966457b7a.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Unless otherwise noted, supported starting with Windows Vista.
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
-	FWPS_FIELDS_STREAM_V4
product:
- Windows
targetos: Windows
req.typenames: FWPS_FIELDS_STREAM_V4
---

# FWPS_FIELDS_STREAM_V4_ Enumeration
The FWPS_FIELDS_STREAM_V4 enumeration type specifies the data field identifiers for the
  FWPS_LAYER_STREAM_V4 and FWPS_LAYER_STREAM_V4_DISCARD 
  <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/aa366492">run-time filtering layers</a>.

## Syntax
```
typedef enum FWPS_FIELDS_STREAM_V4_ {
  FWPS_FIELD_STREAM_V4_IP_LOCAL_ADDRESS       ,
  FWPS_FIELD_STREAM_V4_IP_LOCAL_ADDRESS_TYPE  ,
  FWPS_FIELD_STREAM_V4_IP_REMOTE_ADDRESS      ,
  FWPS_FIELD_STREAM_V4_IP_LOCAL_PORT          ,
  FWPS_FIELD_STREAM_V4_IP_REMOTE_PORT         ,
  FWPS_FIELD_STREAM_V4_DIRECTION              ,
  FWPS_FIELD_STREAM_V4_FLAGS                  ,
  FWPS_FIELD_STREAM_V4_COMPARTMENT_ID         ,
  FWPS_FIELD_STREAM_V4_MAX
} FWPS_FIELDS_STREAM_V4;
```

## Constants

<table>
            
                <tr>
                    <td>FWPS_FIELD_STREAM_V4_IP_LOCAL_ADDRESS</td>
                    <td>The local IP address.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_STREAM_V4_IP_LOCAL_ADDRESS_TYPE</td>
                    <td>The local IP address type. The possible values are defined by the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568757">NL_ADDRESS_TYPE</a> enumeration.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_STREAM_V4_IP_REMOTE_ADDRESS</td>
                    <td>The remote IP address.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_STREAM_V4_IP_LOCAL_PORT</td>
                    <td>The local transport protocol port number.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_STREAM_V4_IP_REMOTE_PORT</td>
                    <td>The remote transport protocol port number.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_STREAM_V4_DIRECTION</td>
                    <td>#####  The possible values are:



#### FWP_DIRECTION_INBOUND



#### FWP_DIRECTION_OUTBOUND</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_STREAM_V4_FLAGS</td>
                    <td>A bitwise OR of a combination of filtering condition flags. For information about the possible
     flags, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff549942">Filtering Condition Flags</a>.
     

<div class="alert"><b>Note</b>  Supported in Windows Server 2008, Windows Vista SP1, and later versions of
     Windows.</div>
<div> </div></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_STREAM_V4_COMPARTMENT_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_STREAM_V4_MAX</td>
                    <td>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Unless otherwise noted, supported starting with Windows Vista. Unless otherwise noted, supported starting with Windows Vista. |
| **Header** | fwpsk.h (include Fwpsk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff568757">NL_ADDRESS_TYPE</a>